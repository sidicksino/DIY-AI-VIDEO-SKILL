#!/usr/bin/env python3
"""Score a finished Short against the growth rules (brand/growth-playbook.md).

    .venv/bin/python tools/score_video.py projects/019-bunk-house
    .venv/bin/python tools/score_video.py path/to/video.mp4

Measures what can be measured on the file itself:
  length band, movement in the first 0.5 s, shot lengths (pace), ending
  length, sound on every second, music key in edit.json, hook text key.
Writes <project>/output/_score/:
  opening.jpg   frames at 0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0 s + the last frame
  shots.jpg     the middle frame of every shot with its length
  score.json    every number
Prints a score out of 100 and the list of fixes. The rules a file cannot
show (is the opening an action on the junk? is there a reason? does someone
use the piece at the end?) are judged by looking at opening.jpg and
shots.jpg: the /luna-score skill does that.
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def sh(cmd):
    return subprocess.run([str(c) for c in cmd], capture_output=True, text=True)


def duration(video):
    return float(sh(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                     "-of", "csv=p=0", video]).stdout.strip())


def frame(video, t, width=270):
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{max(t, 0):.3f}", "-i", str(video),
                        "-frames:v", "1", "-vf", f"scale={width}:-2", "-f", "image2pipe",
                        "-vcodec", "png", "-"], capture_output=True)
    from io import BytesIO
    return Image.open(BytesIO(r.stdout)).convert("RGB")


def diff(a, b):
    """Mean absolute difference between two frames, 0-255."""
    x = np.asarray(a.resize((135, 240)), dtype=np.int16)
    y = np.asarray(b.resize((135, 240)), dtype=np.int16)
    return float(np.abs(x - y).mean())


def shots(video, total):
    from scenedetect import ContentDetector, detect
    found = detect(str(video), ContentDetector(threshold=27, min_scene_len=8))
    cuts = [(a.get_seconds(), b.get_seconds()) for a, b in found]
    return cuts or [(0.0, total)]


def loudness_per_second(video, total):
    """RMS level in dB for every second of audio; None if there is no audio."""
    r = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(video), "-vn", "-ac", "1",
                        "-ar", "8000", "-f", "s16le", "-"], capture_output=True)
    pcm = np.frombuffer(r.stdout, dtype=np.int16).astype(np.float64)
    if pcm.size == 0:
        return None
    out = []
    for s in range(int(total)):
        chunk = pcm[s * 8000:(s + 1) * 8000]
        if chunk.size == 0:
            break
        rms = np.sqrt((chunk ** 2).mean()) / 32768
        out.append(round(20 * np.log10(max(rms, 1e-6)), 1))
    return out


def sheet(images, labels, dest, width=270):
    h = images[0].height
    out = Image.new("RGB", (width * len(images), h + 24), "white")
    d = ImageDraw.Draw(out)
    for i, (im, lab) in enumerate(zip(images, labels)):
        out.paste(im, (i * width, 24))
        d.text((i * width + 6, 6), lab, fill="black")
    out.save(dest, quality=85)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = Path(sys.argv[1]).resolve()
    if target.is_dir():
        project, video = target, target / "output" / "final.mp4"
    else:
        video = target
        project = target.parent.parent if target.parent.name == "output" else None
    if not video.exists():
        sys.exit(f"missing video: {video}")
    out_dir = (video.parent / "_score")
    out_dir.mkdir(exist_ok=True)
    edit = {}
    if project and (project / "edit.json").exists():
        edit = json.loads((project / "edit.json").read_text())

    total = duration(video)
    cuts = shots(video, total)
    lens = [b - a for a, b in cuts]
    checks = []  # (points, max, name, detail, fix or None)

    def add(points, most, name, detail, fix=None):
        checks.append((points, most, name, detail, fix if points < most else None))

    # R7 length
    steps = edit.get("format") == "steps"
    if steps:
        ok = 18 <= total <= 36
        add(10 if ok else (5 if 14 <= total <= 42 else 0), 10, "Length",
            f"{total:.1f}s (steps video, 18-36s)", "aim for 18-36s: speed up slow clips or trim dead seconds")
    else:
        quick, big = 11 <= total <= 25.5, 45 <= total <= 62
        add(10 if quick or big else (5 if 9 <= total <= 32 or 40 <= total <= 70 else 0), 10,
            "Length", f"{total:.1f}s ({'Quick build' if quick else 'Big transformation' if big else 'outside both formats'})",
            "aim for 11-25s (Quick build) or 45-60s (Big transformation)")

    # R1 movement in the first 0.5 s
    f0, f05, f1 = frame(video, 0.0), frame(video, 0.5), frame(video, 1.0)
    early, first_sec = diff(f0, f05), diff(f0, f1)
    add(20 if early >= 6 else (10 if early >= 3 else 0), 20,
        "Opening moves", f"change 0→0.5s = {early:.1f}, 0→1.0s = {first_sec:.1f} (6+ is clear action)",
        "frame 0 is nearly still: trim the first segment into the action")

    # R1 the opening is not the finished piece
    segs = edit.get("segments") or []
    same_clip = len(segs) > 1 and segs[0].get("clip") == segs[-1].get("clip")
    third = [frame(video, t) for t in np.arange(total * 0.67, total - 0.1, 0.5)]
    closest = min(diff(f0, f) for f in third)
    if same_clip:
        pts, why = 0, f"the first and last segments both come from {segs[0]['clip']}"
    else:
        pts = 15 if closest >= 18 else (7 if closest >= 10 else 0)
        why = f"frame 0 vs the last third: closest difference {closest:.1f} (under 10 = same picture)"
    add(pts, 15, "Opening is not the result", why,
        "the video opens on the finished piece: open on Luna in action instead")

    # R4 pace
    body = lens[:-1] if len(lens) > 1 else lens
    avg = total / len(cuts)
    if steps:
        # whole 8 s clips: judge movement inside the shots, not shot length
        long = [(round(cuts[i][0], 1), round(n, 1)) for i, n in enumerate(body) if n > 6.6]
        still = []
        for t in np.arange(0.5, total - 1.0, 1.0):
            if diff(frame(video, t), frame(video, t + 1.0)) < 2.0:
                still.append(round(float(t), 1))
        pace_pts = 20 if not long and len(still) <= 1 else (12 if len(long) <= 1 and len(still) <= 3 else 4)
        add(pace_pts, 20, "Pace (steps)",
            f"{len(cuts)} shots, {avg:.2f}s average, over 6.5s at {long or 'none'}, still seconds at {still or 'none'}",
            "speed up or trim the still seconds; keep every shot at 6.5s or less")
    else:
        long = [(round(cuts[i][0], 1), round(n, 1)) for i, n in enumerate(body) if n > 2.6]
        pace_pts = 20 if not long and avg <= 2.0 else (14 if len(long) <= 1 and avg <= 2.6 else (7 if avg <= 3.2 else 0))
        add(pace_pts, 20, "Pace", f"{len(cuts)} shots, {avg:.2f}s average, shots over 2.5s at {long or 'none'}",
            "split long shots into 1-2s beats (a fixed-camera time-lapse with a change every second is fine: check shots.jpg)")

    # R4 first 3 seconds
    early_cuts = sum(1 for a, _ in cuts if a < 3.0)
    if steps:
        add(5 if lens[0] <= 6.6 else 0, 5, "First shot", f"first shot {lens[0]:.1f}s (steps: 6.5s or less)",
            "speed up or trim the first clip")
    else:
        add(5 if early_cuts >= 2 else 0, 5, "First 3 seconds", f"{early_cuts} shot(s) start in the first 3s",
            "add a second beat inside the first 3s")

    # R6 ending length
    end_len = lens[-1]
    end_max = 6.6 if steps else 3.6
    add(10 if end_len <= end_max else (5 if end_len <= end_max + 1.5 else 0), 10, "Ending length",
        f"last shot {end_len:.1f}s", f"shorten the last shot to {end_max - 0.1:.1f}s")

    # R8 sound
    levels = loudness_per_second(video, total)
    if levels is None:
        add(0, 10, "Sound", "no audio track", "the video has no sound")
    else:
        quiet = [i for i, v in enumerate(levels) if v < -45]
        add(10 if not quiet else (5 if len(quiet) <= 2 else 0), 10, "Sound on every beat",
            f"quiet seconds (under -45 dB): {quiet or 'none'}",
            "some seconds are almost silent: pick trims with a clear action sound")

    # house rules
    add(5 if not edit.get("music") else 0, 5, "No music", "edit.json has no music" if not edit.get("music") else "edit.json adds music",
        "remove the music key (unless the user asked for it)")
    add(5 if not (edit.get("hook") or {}).get("text") else 0, 5, "No on-screen text",
        "no hook text" if not (edit.get("hook") or {}).get("text") else "edit.json has hook text",
        "remove the hook key")

    score = sum(c[0] for c in checks)
    most = sum(c[1] for c in checks)

    times = [0.0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, total - 0.15]
    sheet([frame(video, t) for t in times], [f"{t:.2f}s" for t in times[:-1]] + ["LAST"], out_dir / "opening.jpg")
    mids = [frame(video, (a + b) / 2, 180) for a, b in cuts[:40]]
    sheet(mids, [f"#{i + 1} {n:.1f}s" for i, n in enumerate(lens[:40])], out_dir / "shots.jpg", 180)
    (out_dir / "score.json").write_text(json.dumps({
        "video": str(video), "seconds": round(total, 2), "score": score, "max": most,
        "shots": [round(n, 2) for n in lens],
        "checks": [{"name": n, "points": p, "max": m, "detail": d, "fix": f} for p, m, n, d, f in checks],
    }, indent=1))

    print(f"\n{video}\n")
    for p, m, name, detail, _ in checks:
        print(f"  {p:>2}/{m:<2}  {name:<26} {detail}")
    print(f"\n  MEASURED SCORE  {score}/{most}")
    fixes = [f"{n}: {f}" for _, _, n, _, f in checks if f]
    if fixes:
        print("\n  Fix:")
        for f in fixes:
            print(f"   - {f}")
    print(f"\n  Look at {out_dir / 'opening.jpg'} and {out_dir / 'shots.jpg'} for the judged rules.")


if __name__ == "__main__":
    main()
