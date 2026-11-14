"""Break a reference video into shots so it can be remade shot by shot.

    .venv/bin/python tools/analyze_ref.py same-idea/<video>.mp4

Writes same-idea/_analysis/<video-name>/:
  shots.json      every shot: number, start, end, duration (s), camera move + framing hint
  shots.jpg       one labelled keyframe (middle of the shot) per shot, in order
  shot_NN.jpg     full-size keyframe of each shot (to look at details)
  timeline.jpg    a frame every 0.5 s with timestamps (to see motion inside shots)
Prints a short summary: length, number of shots, average shot length.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent


def frame_at(video, t, dest, width=None):
    vf = ["-vf", f"scale={width}:-2"] if width else []
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{t:.3f}", "-i", str(video),
                    "-frames:v", "1", *vf, str(dest)], check=True)


def camera_move(video, start, end):
    """Estimate what the camera does inside a shot from frame-to-frame similarity transforms.

    Returns (label, details): label is one of static, push-in, pull-out, pan-left, pan-right,
    tilt-up, tilt-down, orbit/arc, handheld. Zoom and travel are accumulated over the shot."""
    import cv2
    import numpy as np
    cap = cv2.VideoCapture(str(video))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24
    cap.set(cv2.CAP_PROP_POS_MSEC, start * 1000)
    step = max(1, int(fps / 8))
    prev, scale, dx, dy, rot, jitter, n = None, 1.0, 0.0, 0.0, 0.0, [], 0
    orb = cv2.ORB_create(800)
    t = start
    while t < end - 0.05:
        ok, frame = cap.read()
        if not ok:
            break
        if n % step == 0:
            g = cv2.cvtColor(cv2.resize(frame, (360, 640)), cv2.COLOR_BGR2GRAY)
            if prev is not None:
                k1, d1 = orb.detectAndCompute(prev, None)
                k2, d2 = orb.detectAndCompute(g, None)
                if d1 is not None and d2 is not None and len(k1) > 20 and len(k2) > 20:
                    m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d1, d2)
                    if len(m) > 15:
                        a = np.float32([k1[x.queryIdx].pt for x in m])
                        b = np.float32([k2[x.trainIdx].pt for x in m])
                        M, _ = cv2.estimateAffinePartial2D(a, b, method=cv2.RANSAC)
                        if M is not None:
                            sc = float(np.hypot(M[0, 0], M[1, 0]))
                            scale *= sc
                            dx += float(M[0, 2]); dy += float(M[1, 2])
                            rot += float(np.degrees(np.arctan2(M[1, 0], M[0, 0])))
                            jitter.append(abs(M[0, 2]) + abs(M[1, 2]))
            prev = g
        n += 1
        t = start + n / fps
    cap.release()
    zoom = (scale - 1) * 100
    travel = (dx ** 2 + dy ** 2) ** 0.5
    if zoom > 6:
        label = "push-in/forward"
    elif zoom < -6:
        label = "pull-out"
    elif travel > 60 and abs(dx) >= abs(dy):
        label = "pan-left" if dx > 0 else "pan-right"
    elif travel > 60:
        label = "tilt-up" if dy > 0 else "tilt-down"
    elif abs(rot) > 4:
        label = "orbit/arc"
    elif jitter and sum(jitter) / len(jitter) > 1.5:
        label = "handheld"
    else:
        label = "static"
    return label, {"zoom_pct": round(zoom, 1), "travel_px": round(travel), "rotation_deg": round(rot, 1)}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    video = Path(sys.argv[1]).resolve()
    out = ROOT / "same-idea/_analysis" / video.stem
    out.mkdir(parents=True, exist_ok=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                str(video)], capture_output=True, text=True).stdout.strip())

    from scenedetect import detect, ContentDetector
    scenes = detect(str(video), ContentDetector(threshold=27.0, min_scene_len=8))
    cuts = [(s.seconds, e.seconds) for s, e in scenes] or [(0.0, dur)]
    shots = []
    for i, (a, b) in enumerate(cuts, 1):
        move, details = camera_move(video, a, b)
        shots.append({"shot": i, "start": round(a, 2), "end": round(b, 2), "duration": round(b - a, 2),
                      "camera": move, **details})
    (out / "shots.json").write_text(json.dumps({"video": video.name, "duration": round(dur, 2),
                                                "shots": shots}, indent=2))

    # keyframes + labelled contact sheet
    thumbs = []
    for s in shots:
        mid = (s["start"] + s["end"]) / 2
        full = out / f"shot_{s['shot']:02d}.jpg"
        frame_at(video, mid, full)
        thumbs.append((s, Image.open(full).convert("RGB")))
    tw = 220
    th = int(thumbs[0][1].height * tw / thumbs[0][1].width)
    cols = 8
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * (tw + 6) + 6, rows * (th + 30) + 6), "white")
    d = ImageDraw.Draw(sheet)
    for k, (s, im) in enumerate(thumbs):
        x, y = 6 + (k % cols) * (tw + 6), 6 + (k // cols) * (th + 30)
        sheet.paste(im.resize((tw, th)), (x, y + 24))
        d.text((x + 2, y + 2), f"#{s['shot']}  {s['start']:.1f}-{s['end']:.1f}s ({s['duration']:.1f}s)", fill="black")
        d.text((x + 2, y + 13), f"camera: {s['camera']}", fill=(180, 30, 30))
    sheet.save(out / "shots.jpg", quality=88)

    # timeline every 0.5 s
    tmp = Path(tempfile.mkdtemp())
    subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(video), "-vf", "fps=2,scale=150:-2",
                    str(tmp / "t%04d.png")], check=True)
    frames = sorted(tmp.glob("t*.png"))
    if frames:
        w, h = Image.open(frames[0]).size
        cols = 12
        rows = (len(frames) + cols - 1) // cols
        tl = Image.new("RGB", (cols * w, rows * (h + 14)), "white")
        dd = ImageDraw.Draw(tl)
        for k, f in enumerate(frames):
            x, y = (k % cols) * w, (k // cols) * (h + 14)
            tl.paste(Image.open(f), (x, y + 14))
            dd.text((x + 2, y + 1), f"{k * 0.5:.1f}s", fill="black")
        tl.save(out / "timeline.jpg", quality=80)

    avg = dur / len(shots)
    print(f"{video.name}: {dur:.1f}s, {len(shots)} shots, average {avg:.1f}s per shot")
    for s in shots:
        print(f"  #{s['shot']:<3} {s['start']:5.1f}-{s['end']:5.1f}s  {s['camera']:<10} zoom {s['zoom_pct']:+5.1f}%  travel {s['travel_px']:4d}px")
    print(f"analysis: {out}")


if __name__ == "__main__":
    main()
