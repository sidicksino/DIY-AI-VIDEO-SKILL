"""Detailed visual review for Luna projects: frames pixel by pixel, clips frame by frame.

    .venv/bin/python tools/review.py frames projects/010-kitten-igloo
    .venv/bin/python tools/review.py clip projects/010-kitten-igloo/clips/C1.mp4

frames: reads the image order from plan.md (### <name> headings in Part 1) and
  writes into frames/_review/:
  - drift.jpg     every frame next to a heat map of where it differs from
                  H-hero. The garden, fence and shed should stay dark;
                  only the piece and Luna should light up.
  - pairs_*.jpg   each frame next to the next one, at full resolution, cropped
                  to the piece, Luna's face and her hands, for checking
                  shape, size, colour and identity side by side.
  It prints the background drift per frame; anything flagged needs a close look.
  - checks.md     the logic check: each frame's **Check:** facts from plan.md (what
                  must and must not be in it), to answer YES/NO on zoom_<frame>.jpg
                  (a full-resolution crop of its **Focus:** box) before the user sees it
  - size_*.jpg    clip start | end (and **Same size as:** pairs) side by side with a
                  10% grid, to compare the piece's size and spot
  It also prints, per clip pair, how much changes inside the Focus box; under 6 means
  start and end are nearly the same picture (the clip would have nothing to show).

clip: decodes every frame and writes into clips/_review/<clip>/:
  - grid.jpg      a frame every 0.25 s
  - jump_*.jpg    the frames around every sudden change (pop-ins, vanishing
                  objects, morphs), which show up as spikes in frame difference
  It prints the frame-difference spikes with timestamps, and the clean
  windows between them.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

# Luna camera convention: piece left of centre, Luna kneeling right.
BOXES = {  # fractions of width/height: x0, y0, x1, y1
    "piece": (0.10, 0.45, 0.72, 0.80),
    "face": (0.55, 0.18, 0.95, 0.40),
    "hands": (0.35, 0.40, 0.95, 0.75),
}
BACKGROUND = (0.0, 0.0, 1.0, 0.30)  # sky, trees, fence, shed: should never change in sunny frames


def crop(im, box):
    w, h = im.size
    x0, y0, x1, y1 = box
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))


def gray(im):
    return np.asarray(im.convert("L").filter(ImageFilter.GaussianBlur(2)), dtype=np.float32)


def frame_order(project):
    plan = (project / "plan.md").read_text()
    part1 = plan.split("## Part 1")[1].split("## Part 2")[0]
    names = re.findall(r"^### ([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+) —", part1, re.M)
    return names


def review_frames(project):
    fdir = project / "frames"
    out = fdir / "_review"
    out.mkdir(exist_ok=True)
    names = [n for n in frame_order(project) if (fdir / f"{n}.png").exists()]
    # each frame is compared with the anchor it was edited from ("**Source:** edit of X")
    plan = (project / "plan.md").read_text()
    source = {}
    for n in names:
        m = re.search(rf"### {re.escape(n)}\b[^\n]*\n\*\*Source:\*\* edit of ([A-Za-z0-9-]+)", plan)
        source[n] = m.group(1) if m and (fdir / f"{m.group(1)}.png").exists() else None
    anchors = {}

    # 1. drift heat maps vs each frame's own anchor
    tw, th = 240, 430
    sheet = Image.new("RGB", (len(names) * (tw * 2 + 20) // 2 + 20, th * 2 + 70), "white")
    d = ImageDraw.Draw(sheet)
    print("Background drift vs each frame's source anchor (top 30%; should be < 6):")
    for k, n in enumerate(names):
        im = Image.open(fdir / f"{n}.png").convert("RGB")
        src = source.get(n)
        if src is None:
            diff = np.zeros(gray(im).shape, dtype=np.float32)
            bgscore = 0.0
            label = "anchor"
        else:
            if src not in anchors:
                anchors[src] = gray(Image.open(fdir / f"{src}.png").convert("RGB"))
            diff = np.abs(gray(im) - anchors[src])
            bgscore = float(np.asarray(crop(Image.fromarray(diff.astype(np.uint8)), BACKGROUND)).mean())
            label = f"vs {src}"
        flag = "  <-- check" if bgscore > 6 and not n.startswith("R-") else ""
        print(f"  {n:12s} {bgscore:5.1f}  ({label}){flag}")
        heat = Image.fromarray(np.clip(diff * 4, 0, 255).astype(np.uint8)).convert("RGB")
        col, row = k % ((len(names) + 1) // 2), k // ((len(names) + 1) // 2)
        x, y = 10 + col * (tw + 10), 10 + row * (th + 30)
        sheet.paste(im.resize((tw // 2, th // 2)), (x, y + 20))
        sheet.paste(heat.resize((tw // 2, th // 2)), (x + tw // 2, y + 20))
        d.text((x, y + 4), f"{n} bg={bgscore:.1f}", fill="black")
    sheet.save(out / "drift.jpg", quality=88)

    # 2. pairs, full-res crops: each clip's start -> end frame (from Part 2 of the plan);
    #    falls back to consecutive frames when the plan has no clip list
    part2 = plan.split("## Part 2")[1] if "## Part 2" in plan else ""
    pairs = [(a, b) for a, b in re.findall(r"^### (?:[A-Z]\d+-)?C\d+[^\n]*?· ([A-Za-z0-9-]+) → ([A-Za-z0-9-]+)", part2, re.M)
             if (fdir / f"{a}.png").exists() and (fdir / f"{b}.png").exists()]
    if not pairs:
        pairs = list(zip(names, names[1:]))
    for old_sheet in out.glob("pairs_*.jpg"):
        old_sheet.unlink()
    for a, b in pairs:
        ia = Image.open(fdir / f"{a}.png").convert("RGB")
        ib = Image.open(fdir / f"{b}.png").convert("RGB")
        tiles = []
        for key, box in BOXES.items():
            ca, cb = crop(ia, box), crop(ib, box)
            pair = Image.new("RGB", (ca.width * 2 + 10, ca.height + 24), "white")
            pair.paste(ca, (0, 24))
            pair.paste(cb, (ca.width + 10, 24))
            ImageDraw.Draw(pair).text((4, 4), f"{key}: {a}  |  {b}", fill="black")
            tiles.append(pair)
        W = max(t.width for t in tiles)
        H = sum(t.height for t in tiles) + 10 * len(tiles)
        page = Image.new("RGB", (W, H), "white")
        y = 0
        for t in tiles:
            page.paste(t, (0, y))
            y += t.height + 10
        page.save(out / f"pairs_{a}__{b}.jpg", quality=90)
    print(f"Wrote {out}/drift.jpg and {len(pairs)} clip pair sheets.")

    # 3. logic checks: per-frame Check facts + Focus zooms, clip-pair change, size grids
    logic_checks(project, names, pairs, plan, out)


def frame_meta(plan, name):
    """The **Check:** facts, **Focus:** box and **Same size as:** frame written under a frame heading."""
    part = plan.split(f"### {name} —", 1)
    if len(part) < 2:
        return [], None, None
    block = part[1].split("\n### ", 1)[0].split("\n## ", 1)[0]
    facts = []
    m = re.search(r"^\*\*Check:\*\*(.+)$", block, re.M)
    if m:
        facts = [f.strip(" .") for f in re.split(r"\s+·\s+|;", m.group(1)) if f.strip(" .")]
    box = None
    m = re.search(r"^\*\*Focus:\*\*\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)", block, re.M)
    if m:
        box = tuple(float(v) for v in m.groups())
    m = re.search(r"^\*\*Same size as:\*\*\s*([A-Za-z0-9-]+)", block, re.M)
    return facts, box, (m.group(1) if m else None)


def grid(im, step=0.1):
    """A copy with a labelled 10% grid, so piece edges can be compared between frames."""
    im = im.copy()
    d = ImageDraw.Draw(im)
    w, h = im.size
    for k in range(1, int(1 / step)):
        x, y = int(w * k * step), int(h * k * step)
        d.line([(x, 0), (x, h)], fill=(255, 0, 0), width=1)
        d.line([(0, y), (w, y)], fill=(255, 0, 0), width=1)
        d.text((x + 2, 2), f"{k * 10}", fill=(255, 0, 0))
        d.text((2, y + 2), f"{k * 10}", fill=(255, 0, 0))
    return im


def side_by_side(a, b, la, lb, width=560):
    a = a.resize((width, int(a.height * width / a.width)))
    b = b.resize((width, int(b.height * width / b.width)))
    page = Image.new("RGB", (width * 2 + 10, max(a.height, b.height) + 24), "white")
    page.paste(a, (0, 24))
    page.paste(b, (width + 10, 24))
    d = ImageDraw.Draw(page)
    d.text((4, 4), la, fill="black")
    d.text((width + 14, 4), lb, fill="black")
    return page


def logic_checks(project, names, pairs, plan, out):
    fdir = project / "frames"
    for old in list(out.glob("zoom_*.jpg")) + list(out.glob("size_*.jpg")):
        old.unlink()
    lines = ["# Logic check (fill in before showing the user)", "",
             "Answer every fact YES or NO by looking at the zoom image at full size.",
             "Any NO: fix the frame (reword, regenerate from its anchor) and rerun review.py.", ""]
    missing = []
    for n in names:
        facts, box, same = frame_meta(plan, n)
        im = Image.open(fdir / f"{n}.png").convert("RGB")
        if box:
            z = crop(im, box)
            scale = 900 / max(z.size)
            z.resize((int(z.width * scale), int(z.height * scale))).save(out / f"zoom_{n}.jpg", quality=92)
        lines.append(f"## {n}")
        lines.append(f"Zoom: `{out / ('zoom_' + n + '.jpg')}`" if box else "Zoom: (no **Focus:** box in plan.md: look at the full frame)")
        if not facts:
            missing.append(n)
            lines.append("- [ ] (no **Check:** facts in plan.md: write them first)")
        for f in facts:
            lines.append(f"- [ ] {f}")
        if same and (fdir / f"{same}.png").exists():
            other = Image.open(fdir / f"{same}.png").convert("RGB")
            side_by_side(grid(other), grid(im), same, n).save(out / f"size_{same}__{n}.jpg", quality=88)
            lines.append(f"- [ ] Same spot and size as {same}: piece edges on the same grid lines (`size_{same}__{n}.jpg`)")
        lines.append("")

    print("\nClip pairs, change inside the Focus box (start vs end; under 6 = almost nothing happens):")
    lines.append("## Clip pairs")
    for a, b in pairs:
        _, box, _ = frame_meta(plan, a)
        ia = Image.open(fdir / f"{a}.png").convert("RGB")
        ib = Image.open(fdir / f"{b}.png").convert("RGB").resize(ia.size)
        region = box or (0.0, 0.35, 1.0, 1.0)
        change = float(np.abs(gray(crop(ia, region)) - gray(crop(ib, region))).mean())
        flag = "  <-- start and end look the same" if change < 6 else ""
        print(f"  {a:12s} -> {b:12s} {change:5.1f}{flag}")
        side_by_side(grid(ia), grid(ib), a, b).save(out / f"size_{a}__{b}.jpg", quality=88)
        lines.append(f"- [ ] {a} -> {b}: change {change:.1f}{' (FLAG: almost no change)' if flag else ''}; "
                     f"piece the same size and spot on the grid (`size_{a}__{b}.jpg`); only this clip's action differs")
    (out / "checks.md").write_text("\n".join(lines) + "\n")
    if missing:
        print("  no **Check:** facts for: " + ", ".join(missing))
    print(f"Wrote {out}/checks.md, zoom_*.jpg and size_*.jpg")


def read_frames(clip, fps_out=None):
    tmp = Path(tempfile.mkdtemp())
    vf = f"fps={fps_out}," if fps_out else ""
    subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(clip), "-vf", f"{vf}scale=360:-2",
                    str(tmp / "f%05d.png")], check=True)
    files = sorted(tmp.glob("f*.png"))
    fps = float(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                "stream=r_frame_rate", "-of", "csv=p=0", str(clip)],
                               capture_output=True, text=True).stdout.strip().split("/")[0]) / float(
        subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=r_frame_rate", "-of", "csv=p=0", str(clip)],
                       capture_output=True, text=True).stdout.strip().split("/")[1])
    return [Image.open(f).convert("RGB") for f in files], (fps_out or fps)


def review_clip(clip):
    clip = Path(clip)
    out = clip.parent / "_review" / clip.stem
    out.mkdir(parents=True, exist_ok=True)
    frames, fps = read_frames(clip)
    g = [gray(f) for f in frames]
    diffs = np.array([np.abs(g[i] - g[i - 1]).mean() for i in range(1, len(g))])
    med = float(np.median(diffs))
    mad = float(np.median(np.abs(diffs - med))) or 0.5
    thresh = max(med + 8 * mad, med * 3, 4.0)
    spikes = [i + 1 for i, v in enumerate(diffs) if v > thresh]

    # grid every 0.25 s
    step = max(1, round(fps / 4))
    pick = list(range(0, len(frames), step))
    cols = 8
    tw, th = frames[0].width // 2, frames[0].height // 2
    rows = (len(pick) + cols - 1) // cols
    grid = Image.new("RGB", (cols * tw, rows * (th + 16)), "white")
    d = ImageDraw.Draw(grid)
    for k, i in enumerate(pick):
        x, y = (k % cols) * tw, (k // cols) * (th + 16)
        grid.paste(frames[i].resize((tw, th)), (x, y + 16))
        d.text((x + 3, y + 2), f"{i / fps:.2f}s" + (" !" if any(abs(i - s) <= step // 2 for s in spikes) else ""),
               fill="red" if any(abs(i - s) <= step // 2 for s in spikes) else "black")
    grid.save(out / "grid.jpg", quality=85)

    # zoom around every spike
    for s in spikes:
        idx = [i for i in range(s - 3, s + 3) if 0 <= i < len(frames)]
        strip = Image.new("RGB", (len(idx) * frames[0].width, frames[0].height + 18), "white")
        dd = ImageDraw.Draw(strip)
        for k, i in enumerate(idx):
            strip.paste(frames[i], (k * frames[0].width, 18))
            dd.text((k * frames[0].width + 3, 3), f"{i / fps:.3f}s", fill="red" if i == s else "black")
        strip.save(out / f"jump_{s / fps:05.2f}s.jpg", quality=88)

    dur = len(frames) / fps
    print(f"{clip.name}: {len(frames)} frames, {dur:.2f}s at {fps:.0f} fps; median change {med:.2f}, spike threshold {thresh:.2f}")
    if spikes:
        print("  sudden changes at: " + ", ".join(f"{s / fps:.2f}s ({diffs[s - 1]:.1f})" for s in spikes))
    else:
        print("  no sudden changes detected")
    cuts = [0.0] + [s / fps for s in spikes] + [dur]
    windows = [(a, b) for a, b in zip(cuts, cuts[1:]) if b - a >= 1.0]
    print("  clean windows (>= 1 s): " + (", ".join(f"{a:.2f}-{b:.2f}s" for a, b in windows) or "none"))
    print(f"  review images: {out}")


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("frames", "clip"):
        sys.exit(__doc__)
    if sys.argv[1] == "frames":
        review_frames(Path(sys.argv[2]))
    else:
        review_clip(sys.argv[2])
