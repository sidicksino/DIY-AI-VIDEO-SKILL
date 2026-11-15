#!/usr/bin/env python3
"""
Join generated clips into one finished vertical Short.

Reads <project>/edit.json, trims each segment, fits it to 1080x1920, joins
the segments in the order given, keeps the clips' own sound (an optional
"music" bed is only added when edit.json asks for it), adds the logo and normalises loudness to -14 LUFS.

Prints a pace report and warns when the edit breaks the growth rules in
brand/growth-playbook.md (opening, shot length, total length, beat count).

Paths in edit.json: clips and output are relative to the project folder;
music and logo are relative to the repo root.

Optional in edit.json:
    "hook": {...}   legacy only; the channel never uses on-screen text (2026-11-14)
        Big rounded caption in the first seconds (most people scroll on mute;
        the words are what stop them). Fades in at 0.1 s, out at "end".
    "loop": 0.4
        Dissolves the last 0.4 s into the opening frame, so the Short ends on
        its own first frame and restarts seamlessly (replays count heavily).

Usage:
    .venv/bin/python tools/assemble.py projects/010-kitten-igloo
    .venv/bin/python tools/assemble.py projects/016-melted-trash-tiles --edit edit-P1.json
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W, H = 1080, 1920
FPS = 24  # Veo renders 24 fps; converting to 30 duplicates frames and makes motion judder

# Quality: every intermediate is near-lossless so only the final encode costs detail.
# The final master is high-bitrate H.264 (YouTube re-encodes it; cleaner input = cleaner Short).
MID = ["-c:v", "libx264", "-preset", "medium", "-crf", "12", "-pix_fmt", "yuv420p"]
FINAL = ["-c:v", "libx264", "-preset", "slow", "-crf", "16", "-tune", "film",
         "-profile:v", "high", "-pix_fmt", "yuv420p", "-maxrate", "40M", "-bufsize", "60M"]


def fit_filter(src_h):
    """Scale to 1080x1920 with Lanczos; add a light unsharp only when upscaling a smaller clip."""
    f = (f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,"
         f"crop={W}:{H},setsar=1,fps={FPS}")
    if src_h and src_h < H:
        f += ",unsharp=5:5:0.5:5:5:0.0"
    return f


def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"command failed:\n{' '.join(map(str, cmd))}\n\n{r.stderr[-3000:]}")
    return r


def probe(path):
    data = json.loads(run(["ffprobe", "-v", "error", "-show_streams",
                           "-show_format", "-of", "json", path]).stdout)
    has_audio = any(s.get("codec_type") == "audio" for s in data["streams"])
    return float(data["format"]["duration"]), has_audio


def loudness(path):
    """Integrated loudness in LUFS, or None if ffmpeg reports none."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(path), "-vn",
                        "-af", "ebur128=framelog=quiet", "-f", "null", "-"],
                       capture_output=True, text=True)
    tail = r.stderr[r.stderr.rfind("Integrated loudness"):]
    for line in tail.splitlines():
        if line.strip().startswith("I:"):
            return float(line.split()[1])
    return None


def cut(seg, project, dest, clip_db):
    src = project / seg["clip"]
    if not src.exists():
        sys.exit(f"missing clip: {src}")
    dur, has_audio = probe(src)
    src_h = int(run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                     "stream=height", "-of", "csv=p=0", src]).stdout.strip() or 0)
    start = float(seg.get("start", 0))
    end = min(float(seg.get("end", dur)), dur)
    if end - start < 0.2:
        sys.exit(f"{seg['clip']}: start {start}s / end {end}s leaves nothing "
                 f"(clip is {dur:.2f}s)")
    length = end - start
    volume = "0" if seg.get("mute") else f"{clip_db}dB"

    # -ss/-t before -i: they limit what is read from the input
    cmd = ["ffmpeg", "-y", "-ss", f"{start:.3f}", "-t", f"{length:.3f}", "-i", src]
    if not has_audio:
        cmd += ["-f", "lavfi", "-t", f"{length:.3f}", "-i", "anullsrc=r=48000:cl=stereo"]
    cmd += [
        "-map", "0:v:0", "-map", "0:a:0" if has_audio else "1:a:0",
        "-vf", fit_filter(src_h),
        "-af", f"aresample=48000,aformat=channel_layouts=stereo,volume={volume}",
        *MID, "-c:a", "aac", "-b:a", "256k", "-t", f"{length:.3f}", dest,
    ]
    run(cmd)
    return length


HOOK_FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"


def pace_report(edit, lengths):
    """Warn when the edit breaks the growth rules (brand/growth-playbook.md)."""
    segs = edit["segments"]
    total = sum(lengths)
    warn = []
    first = (segs[0].get("label") or "").lower()
    if any(w in first for w in ("hook", "finished", "reveal", "hero", "result")):
        warn.append("opening: the first segment looks like the finished piece. "
                    "Open on Luna in action (R1)")
    last = len(segs) - 1
    for i, (seg, n) in enumerate(zip(segs, lengths)):
        label = (seg.get("label") or "").lower()
        if i == last:
            if n > 3.6:
                warn.append(f"ending: segment {i} is {n:.1f}s, keep it to 3.5s (R6)")
        elif n > 2.6 and "time-lapse" not in label and "timelapse" not in label:
            warn.append(f"pace: segment {i} is {n:.1f}s, split it into 1-2s beats (R4)")
    if not (15 <= total <= 22 or 45 <= total <= 62):
        warn.append(f"length: {total:.1f}s is outside Quick build 15-22s and "
                    f"Big transformation 45-60s (R7)")
    need = 8 if total <= 30 else 20
    if len(segs) < need:
        warn.append(f"beats: {len(segs)} segments, aim for {need}+ at this length (R5)")
    print(f"\n  pace: {len(segs)} beats, {total:.1f}s, {total / len(segs):.2f}s per beat")
    for w in warn:
        print(f"  ! {w}")
    if not warn:
        print("  growth rules: ok")


def render_hook(text, dest):
    """White rounded caption with a dark outline, centred, on a transparent 1080x1920 PNG."""
    from PIL import Image, ImageDraw, ImageFont
    # the font has no emoji; drop anything outside the Basic Multilingual Plane
    text = "".join(ch for ch in text if ord(ch) < 0x2600 or ch == "…").strip()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    size = 92
    while True:
        font = ImageFont.truetype(HOOK_FONT, size)
        words, lines, line = text.split(), [], ""
        for w in words:  # wrap to 86% of the width
            test = (line + " " + w).strip()
            if d.textlength(test, font=font) <= W * 0.86:
                line = test
            else:
                lines.append(line)
                line = w
        lines.append(line)
        if len(lines) <= 2 or size <= 60:
            break
        size -= 6
    stroke = max(6, size // 11)
    y = int(H * 0.22)
    for ln in lines:
        tw = d.textlength(ln, font=font)
        d.text(((W - tw) / 2, y), ln, font=font, fill="white", stroke_width=stroke, stroke_fill=(20, 20, 20))
        y += int(size * 1.18)
    img.save(dest)


def add_loop(joined, work, seconds):
    """Dissolve the last `seconds` into a still of the opening frame (same total length)."""
    total, _ = probe(joined)
    first = work / "first_frame.png"
    run(["ffmpeg", "-y", "-i", joined, "-frames:v", "1", first])
    looped = work / "joined_loop.mp4"
    run(["ffmpeg", "-y", "-i", joined, "-loop", "1", "-t", f"{seconds + 0.1:.3f}", "-i", first,
         "-filter_complex",
         f"[0:v]fps={FPS},format=yuv420p,settb=AVTB[a];"
         f"[1:v]scale={W}:{H},setsar=1,fps={FPS},format=yuv420p,settb=AVTB[b];"
         f"[a][b]xfade=transition=fade:duration={seconds:.3f}:offset={total - seconds:.3f}[v]",
         "-map", "[v]", "-map", "0:a", *MID, "-c:a", "copy", "-t", f"{total:.3f}", looped])
    return looped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--edit", default="edit.json", help="edit file inside the project (default edit.json)")
    args = ap.parse_args()

    project = Path(args.project).resolve()
    edit = json.loads((project / args.edit).read_text())
    global FPS
    FPS = int(edit.get("fps", FPS))
    work = project / ("work" if args.edit == "edit.json" else "work-" + Path(args.edit).stem)
    work.mkdir(exist_ok=True)
    out = project / edit.get("output", "output/final.mp4")
    out.parent.mkdir(parents=True, exist_ok=True)

    parts, total, lengths = [], 0.0, []
    for i, seg in enumerate(edit["segments"]):
        dest = work / f"seg{i:02d}.mp4"
        length = cut(seg, project, dest, edit.get("clip_db", 0))
        parts.append(dest)
        lengths.append(length)
        total += length
        print(f"  {i:2d}  {length:5.2f}s  {seg['clip']:<16} {seg.get('label', '')}")
    pace_report(edit, lengths)

    listing = work / "concat.txt"
    listing.write_text("".join(f"file '{p}'\n" for p in parts))
    joined = work / "joined.mp4"
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", listing, "-c", "copy", joined])
    if edit.get("loop"):
        joined = add_loop(joined, work, float(edit["loop"]))
        print(f"  loop: last {float(edit['loop']):.2f}s dissolves into the opening frame")
    total, _ = probe(joined)

    cmd = ["ffmpeg", "-y", "-i", joined]
    audio = "[0:a]"
    filters = []
    n = 1

    music = edit.get("music")
    if music:
        music = ROOT / music
        if not music.exists():
            sys.exit(f"missing music: {music}")
        cmd += ["-stream_loop", "-1", "-i", music]
        fade = max(total - 1.5, 0)
        filters.append(
            f"[{n}:a]atrim=0:{total:.3f},asetpts=PTS-STARTPTS,"
            f"aresample=48000,volume={edit.get('music_db', -18)}dB,"
            f"afade=t=out:st={fade:.3f}:d=1.5[mus]")
        filters.append("[0:a][mus]amix=inputs=2:duration=first:normalize=0[mixed]")
        audio = "[mixed]"
        n += 1
    filters.append(f"{audio}loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[a]")

    video = "0:v"
    # grain: YouTube's encoder smears heavy noise into blocks; keep it subtle (2-3)
    grain = min(int(edit.get("grain", 0)), 3)
    if grain:
        # light moving sensor noise takes the too-clean sheen off generated
        # footage; 4-6 reads as a phone camera, above ~10 it looks dirty
        filters.append(f"[0:v]noise=alls={grain}:allf=t+u[grain]")
        video = "[grain]"

    hook = edit.get("hook")
    if hook and hook.get("text"):
        png = work / "hook.png"
        render_hook(hook["text"], png)
        end = float(hook.get("end", 2.4))
        cmd += ["-loop", "1", "-t", f"{total:.3f}", "-i", png]
        base = video if video.startswith("[") else "[0:v]"
        filters.append(f"[{n}:v]format=rgba,fade=t=in:st=0.1:d=0.2:alpha=1,"
                       f"fade=t=out:st={end - 0.25:.3f}:d=0.25:alpha=1[hk];"
                       f"{base}[hk]overlay=0:0:enable='lte(t,{end:.3f})'[hooked]")
        video = "[hooked]"
        n += 1
        print(f"  hook text: \"{hook['text']}\" until {end:.1f}s")

    logo = edit.get("logo")
    if logo and (ROOT / logo).exists():
        cmd += ["-i", ROOT / logo]
        base = video if video.startswith("[") else "[0:v]"
        # centred; 70% down by default (below the action, above the Shorts
        # caption area). "logo_y" moves it when the subject sits there.
        logo_y = edit.get("logo_y", 0.70)
        # soft by default: semi-transparent and slightly blurred, so it reads
        # as a quiet signature, not a sticker. "logo_opacity" / "logo_blur" override.
        op = float(edit.get("logo_opacity", 0.45))
        bl = float(edit.get("logo_blur", 1.2))
        soft = f",gblur=sigma={bl}" if bl > 0 else ""
        filters.append(f"[{n}:v]scale={int(W * 0.42)}:-1,format=rgba{soft},"
                       f"colorchannelmixer=aa={op}[lg];"
                       f"{base}[lg]overlay=(W-w)/2:H*{logo_y}[v]")
        video = "[v]"
    elif logo:
        print(f"  (no logo at {logo} yet — rendering without it)")

    cmd += ["-filter_complex", ";".join(filters), "-map", video, "-map", "[a]"]
    if video == "0:v":
        cmd += ["-c:v", "copy"]
    else:
        cmd += FINAL
    cmd += ["-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out]
    run(cmd)

    # single-pass loudnorm undershoots on a 20-30 s mix (it measured -17.7
    # on the mushroom Short), so measure the result and correct the gain
    level = loudness(out)
    if level is not None and abs(level + 14) > 0.7:
        fixed = work / "loud_fixed.mp4"
        run(["ffmpeg", "-y", "-i", out, "-c:v", "copy",
             "-af", f"volume={-14 - level:.2f}dB,alimiter=limit=0.89:level=false",
             "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", fixed])
        fixed.replace(out)
        print(f"  loudness {level:.1f} LUFS -> corrected to {loudness(out):.1f}")

    final, _ = probe(out)
    print(f"\n{out}  {final:.1f}s  {W}x{H}")
    if final > 60:
        print("  note: over 60s — fine for Shorts (limit 180s), but the examples all sit at 13-56s")


if __name__ == "__main__":
    main()
