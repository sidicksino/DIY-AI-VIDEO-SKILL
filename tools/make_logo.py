#!/usr/bin/env python3
"""
Make the on-video watermark: a small leaf and LUNA UPCYCLES, white at partial
opacity with a soft shadow so it reads on grass, concrete and sky alike.

Usage:
    .venv/bin/python tools/make_logo.py            # -> brand/logo.png
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FONT = "/System/Library/Fonts/Supplemental/Arial Rounded Bold.ttf"
TEXT = "LUNA UPCYCLES"
OPACITY = 0.72


def leaf(draw, x, y, size, fill):
    # two arcs meeting at the tips, and a stem-vein down the middle
    box = [x, y, x + size, y + size]
    draw.chord(box, 135, 315, fill=fill)
    draw.chord([x + size * 0.02, y + size * 0.02, x + size * 1.02, y + size * 1.02],
               315, 135, fill=fill)
    draw.line([x + size * 0.2, y + size * 0.8, x + size * 0.85, y + size * 0.15],
              fill=(0, 0, 0, 0), width=max(2, size // 14))


def main():
    font = ImageFont.truetype(FONT, 96)
    pad, gap, icon = 40, 26, 92
    tw, th = font.getbbox(TEXT)[2:]
    w, h = pad * 2 + icon + gap + tw, pad * 2 + max(th, icon)

    mark = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(mark)
    white = (255, 255, 255, 255)
    leaf(d, pad, (h - icon) // 2, icon, white)
    d.text((pad + icon + gap, (h - th) // 2 - 6), TEXT, font=font, fill=white)

    alpha = mark.getchannel("A")
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shadow.putalpha(alpha.point(lambda a: int(a * 0.45)))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))

    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    out.alpha_composite(shadow, (3, 4))
    out.alpha_composite(mark)
    out.putalpha(out.getchannel("A").point(lambda a: int(a * OPACITY)))

    dest = ROOT / "brand" / "logo.png"
    out.save(dest)
    print(dest, out.size)


if __name__ == "__main__":
    main()
