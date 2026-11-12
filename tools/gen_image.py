#!/usr/bin/env python3
"""
Generate or edit a still with Gemini's image models (Nano Banana Pro / 2).

New image, with Luna's sheet and her garden as references:

    .venv/bin/python tools/gen_image.py --prompt-file projects/003-mushroom-doghouse/images/H-hero.txt \
        --ref brand/luna-sheet.png --ref brand/luna-garden.png \
        --out projects/003-mushroom-doghouse/frames/H-hero.png -n 3

Edit an existing image (it is sent first, then any references):

    .venv/bin/python tools/gen_image.py --edit frames/H-hero.png \
        --prompt "Keep everything exactly the same ... change only this: remove the puppy." \
        --out frames/G-done.png

Every image gets a .json sidecar with the model, prompt and inputs, so any
frame can be regenerated or traced later. Uses the REST API directly, so no
SDK install is needed; the key comes from .env (GEMINI_API_KEY).
"""

import argparse
import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
API = "https://generativelanguage.googleapis.com/v1beta/models"
MODELS = {"pro": "gemini-3-pro-image", "flash": "gemini-3.1-flash-image"}
# USD per output image, from ai.google.dev/gemini-api/docs/pricing (Sep 2026)
PRICE = {"gemini-3-pro-image": {"1K": 0.134, "2K": 0.134, "4K": 0.24},
         "gemini-3.1-flash-image": {"1K": 0.067, "2K": 0.101, "4K": 0.151}}
MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp"}


def api_key():
    env = ROOT / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip().startswith(("GEMINI_API_KEY=", "GEMIMIAI_API_KEY=")):
                return line.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("No GEMINI_API_KEY in .env")


def image_part(path):
    p = Path(path)
    if not p.exists():
        sys.exit(f"not found: {p}")
    mime = MIME.get(p.suffix.lower())
    if not mime:
        sys.exit(f"unsupported image type: {p.suffix}")
    return {"inline_data": {"mime_type": mime,
                            "data": base64.b64encode(p.read_bytes()).decode()}}


def call(model, parts, aspect, size, key):
    body = {
        "contents": [{"parts": parts}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size},
        },
    }
    req = urllib.request.Request(
        f"{API}/{model}:generateContent", data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json", "x-goog-api-key": key})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            msg = e.read()[:400].decode(errors="replace")
            if e.code in (429, 500, 503) and attempt < 2:
                print(f"  HTTP {e.code}, retrying in {10 * (attempt + 1)}s ...")
                time.sleep(10 * (attempt + 1))
                continue
            sys.exit(f"HTTP {e.code}: {msg}")


def save_image(resp, out):
    cands = resp.get("candidates") or []
    if not cands:
        sys.exit("no image returned: " + json.dumps(resp)[:400])
    parts = cands[0].get("content", {}).get("parts", [])
    for p in parts:
        blob = p.get("inlineData") or p.get("inline_data")
        if blob:
            out.write_bytes(base64.b64decode(blob["data"]))
            return
    text = " ".join(p.get("text", "") for p in parts)
    reason = cands[0].get("finishReason", "")
    sys.exit(f"no image in reply ({reason}): {text[:400]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt")
    ap.add_argument("--prompt-file")
    ap.add_argument("--edit", help="image to edit; sent before the references")
    ap.add_argument("--ref", action="append", default=[], help="reference image(s)")
    ap.add_argument("--model", default="pro", help="pro | flash | full model id")
    ap.add_argument("--aspect", default="9:16")
    ap.add_argument("--size", default="2K", choices=("1K", "2K", "4K"))
    ap.add_argument("-n", type=int, default=1, help="how many variants")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if args.prompt_file:
        prompt = Path(args.prompt_file).read_text().strip()
    elif args.prompt:
        prompt = args.prompt.strip()
    else:
        sys.exit("give --prompt or --prompt-file")

    model = MODELS.get(args.model, args.model)
    inputs = ([args.edit] if args.edit else []) + args.ref
    parts = [image_part(p) for p in inputs] + [{"text": prompt}]
    key = api_key()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    price = PRICE.get(model, {}).get(args.size, 0)
    for i in range(1, args.n + 1):
        dest = out if args.n == 1 else out.with_name(f"{out.stem}_{i}{out.suffix}")
        t0 = time.time()
        save_image(call(model, parts, args.aspect, args.size, key), dest)
        dest.with_suffix(".json").write_text(json.dumps({
            "model": model, "size": args.size, "aspect": args.aspect,
            "edit": args.edit, "refs": args.ref, "prompt": prompt,
            "created": time.strftime("%Y-%m-%d %H:%M:%S"),
        }, indent=2))
        print(f"  {dest}  ({dest.stat().st_size // 1024} KB, {time.time() - t0:.0f}s)")
    print(f"{args.n} image(s) with {model} at {args.size} — about ${price * args.n:.2f}")


if __name__ == "__main__":
    main()
