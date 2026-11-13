"""Break a reference video into shots so it can be remade shot by shot.

    .venv/bin/python tools/analyze_ref.py same-idea/<video>.mp4

Writes same-idea/_analysis/<video-name>/:
  shots.json      every shot: number, start, end, duration (s)
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
    shots = [{"shot": i, "start": round(a, 2), "end": round(b, 2), "duration": round(b - a, 2)}
             for i, (a, b) in enumerate(cuts, 1)]
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
        d.text((x + 2, y + 6), f"#{s['shot']}  {s['start']:.1f}-{s['end']:.1f}s ({s['duration']:.1f}s)", fill="black")
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
    print(f"analysis: {out}")


if __name__ == "__main__":
    main()
