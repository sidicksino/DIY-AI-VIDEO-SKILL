#!/usr/bin/env python3
"""
Turn the ChatGPT images into YouTube's channel art.

    brand/avatar-raw.png  -> brand/avatar.png      800x800, face-centred square
                          -> brand/watermark.png   150x150 round badge (Studio's
                                                   "Video watermark")
    brand/banner-raw.png  -> brand/banner.png      2560x1440, name and tagline
                                                   inside the 1546x423 box that
                                                   every device shows

Usage:
    .venv/bin/python tools/branding.py                 # all that have a raw file
    .venv/bin/python tools/branding.py --brand DIR     # other folder (testing)
"""

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parent.parent
FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
NAME = "Luna Upcycles"
# plain ASCII: Arial Rounded has no arrow or middle-dot glyph (they render as boxes)
TAGLINE = "Old junk. Garden magic. New project every day."
BANNER = (2560, 1440)
SAFE = (1546, 423)


def cover(img, size):
    """Scale to fill `size` and centre-crop, like CSS object-fit: cover."""
    return ImageOps.fit(img.convert("RGB"), size, Image.LANCZOS, centering=(0.5, 0.45))


def avatar(brand):
    raw = Image.open(brand / "avatar-raw.png")
    out = cover(raw, (800, 800))
    out.save(brand / "avatar.png")

    badge = cover(raw, (150, 150)).convert("RGBA")
    mask = Image.new("L", (600, 600), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, 599, 599), fill=255)
    badge.putalpha(mask.resize((150, 150), Image.LANCZOS))
    badge.save(brand / "watermark.png")
    print("avatar.png 800x800, watermark.png 150x150")


def text_with_shadow(canvas, xy, text, font, fill=(255, 255, 255, 255)):
    layer = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text(xy, text, font=font, fill=(0, 0, 0, 170), anchor="mm")
    layer = layer.filter(ImageFilter.GaussianBlur(10))
    canvas.alpha_composite(layer)
    ImageDraw.Draw(canvas).text(xy, text, font=font, fill=fill, anchor="mm")


def banner(brand):
    base = cover(Image.open(brand / "banner-raw.png"), BANNER).convert("RGBA")
    W, H = BANNER
    cx, cy = W // 2, H // 2

    # a soft dark band behind the safe box so white text reads on any photo
    band = Image.new("RGBA", BANNER, (0, 0, 0, 0))
    bw, bh = SAFE[0] + 200, SAFE[1] + 40
    ImageDraw.Draw(band).rounded_rectangle(
        (cx - bw // 2, cy - bh // 2, cx + bw // 2, cy + bh // 2), radius=60,
        fill=(20, 30, 20, 95))
    base.alpha_composite(band.filter(ImageFilter.GaussianBlur(40)))

    text_with_shadow(base, (cx, cy - 45), NAME, ImageFont.truetype(FONT, 150))
    text_with_shadow(base, (cx, cy + 85), TAGLINE, ImageFont.truetype(FONT, 50),
                     fill=(240, 246, 232, 255))

    base.convert("RGB").save(brand / "banner.png", optimize=True)

    # what a phone shows: only the safe box
    sw, sh = SAFE
    base.crop((cx - sw // 2, cy - sh // 2, cx + sw // 2, cy + sh // 2)) \
        .convert("RGB").save(brand / "banner-phone-preview.png")
    print("banner.png 2560x1440, banner-phone-preview.png (what phones show)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--brand", default=str(ROOT / "brand"))
    brand = Path(ap.parse_args().brand)

    done = False
    if (brand / "avatar-raw.png").exists():
        avatar(brand)
        done = True
    if (brand / "banner-raw.png").exists():
        banner(brand)
        done = True
    if not done:
        print(f"no avatar-raw.png or banner-raw.png in {brand} yet")


if __name__ == "__main__":
    main()
