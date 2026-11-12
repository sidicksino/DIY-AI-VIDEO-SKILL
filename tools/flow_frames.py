"""Generate frames from a project's plan.md in Google Flow (via flow-auto), then save + clean them.

    .venv/bin/python tools/flow_frames.py projects/016-melted-trash-tiles <run-tag> NAME[:REF,REF] ...
    add --pro to use Nano Banana Pro (more detail; use it for anchors: H-hero, B-hero, Pn-H, Pn-B)

NAME is a frame heading in plan.md Part 1 ("### NAME — ..."); its prompt is taken from the
code block under it, with <lock sentence> expanded. REF tokens: `luna` = brand/luna-sheet.png,
anything else = frames/<REF>.png of the project. References are sent as small JPEGs (the
Flow Connector rejects messages over 64 MB, so never send full PNGs or huge batches).

Jobs are submitted together (the extension paces them), the script waits for the queue,
copies each download to frames/raw/<NAME>.jpg and frames/<NAME>.png, untouched.
"""
import glob
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
REFS = Path(tempfile.gettempdir()) / "luna-flow-refs"


def clean_and_save(src, proj, name):
    """Save the download as frames/raw/<name>.jpg and frames/<name>.png, untouched.
    (Checked 2026-11-12: Flow downloads carry no visible watermark, so nothing is patched.)"""
    im = Image.open(src).convert("RGB")
    (proj / "frames/raw").mkdir(parents=True, exist_ok=True)
    im.save(proj / f"frames/raw/{name}.jpg", quality=95)
    im.save(proj / f"frames/{name}.png")


def ref(proj, tok):
    REFS.mkdir(exist_ok=True)
    src = ROOT / "brand/luna-sheet.png" if tok == "luna" else proj / f"frames/{tok}.png"
    out = REFS / f"{proj.name[:3]}-{tok}.jpg"
    Image.open(src).convert("RGB").save(out, quality=90)
    return out


def main():
    if len([a for a in sys.argv[1:] if a != "--pro"]) < 3:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != "--pro"]
    model = "nano-banana-pro" if "--pro" in sys.argv else "nano-banana-2"
    proj, tag, items = (ROOT / args[0]).resolve(), args[1], args[2:]
    plan = (proj / "plan.md").read_text()
    lock = re.search(r"\*\*Lock sentence used at the start of every edit below:\*\*\n`(.*?)`", plan, re.S).group(1)
    jobs = []
    for i, item in enumerate(items, 1):
        name, _, refs = item.partition(":")
        block = plan.split(f"### {name} —")[1]
        prompt = re.search(r"```\n(.*?)```", block, re.S).group(1).strip().replace("<lock sentence>", lock)
        cmd = ["flow-auto", "generate", "create", "flow-image-to-image", "--prompt", prompt]
        for r in filter(None, refs.split(",")):
            cmd += ["--image", str(ref(proj, r))]
        cmd += ["--model", model, "--aspect-ratio", "9:16", "--outputs", "1",
                "--index", str(i), "--folder", tag]
        subprocess.run(cmd, capture_output=True, text=True)
        jobs.append((i, name))
    for _ in range(160):
        out = subprocess.run(["flow-auto", "generate", "list"], capture_output=True, text=True).stdout
        if not re.search(r"\b(queued|running|downloading)\b", out):
            break
        time.sleep(15)
    dl = Path.home() / "Downloads" / tag
    for i, name in jobs:
        found = sorted(glob.glob(str(dl / f"{i} - *")))
        if not found:
            print("MISSING", name)
            continue
        clean_and_save(found[0], proj, name)
        print("saved", name)
    fail = subprocess.run(["flow-auto", "generate", "list", "--failed", "--run", tag],
                          capture_output=True, text=True).stdout
    print("\n".join(l for l in fail.splitlines() if "failed:" in l) or "no failures")


if __name__ == "__main__":
    main()
