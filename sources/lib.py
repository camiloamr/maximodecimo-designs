"""SVG design helpers: build SVG strings in Python, render with rsvg-convert.

Fonts come from ~/.fonts/gf (Google Fonts, OFL). Arched text is laid out per glyph
using Pillow's glyph advances so it matches the rendered font.
"""
import math, os, subprocess, random
from PIL import ImageFont

FONTS = os.path.expanduser("~/.fonts/gf/")
FILES = {
    "Bagel Fat One": "BagelFatOne-Regular.ttf", "Cherry Bomb One": "CherryBombOne-Regular.ttf",
    "Anton": "Anton-Regular.ttf", "Alfa Slab One": "AlfaSlabOne-Regular.ttf",
    "Shrikhand": "Shrikhand-Regular.ttf", "Yatra One": "YatraOne-Regular.ttf",
    "Gloock": "Gloock-Regular.ttf", "Rubik Mono One": "RubikMonoOne-Regular.ttf",
    "Chango": "Chango-Regular.ttf", "DM Serif Display": "DMSerifDisplay-Regular.ttf",
    "Rammetto One": "RammettoOne-Regular.ttf", "Titan One": "TitanOne-Regular.ttf",
    "Big Shoulders Display": "BigShouldersDisplay[wght].ttf",
}


def font(family, size):
    return ImageFont.truetype(FONTS + FILES[family], int(size))


def text_width(s, family, size, track=0):
    f = font(family, size)
    return f.getlength(s) + track * (len(s) - 1)


def fit_size(s, family, maxw, start, track_em=0):
    size = start
    while text_width(s, family, size, track_em * size) > maxw and size > 10:
        size -= 2
    return size


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, s, family, size, fill, anchor="middle", track=0, extra=""):
    ls = f' letter-spacing="{track}"' if track else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{family}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}"{ls} {extra}>{esc(s)}</text>')


def arched(s, family, size, cx, cy, r, fill, track=0, up=True, extra=""):
    """Glyphs on a circle of radius r centred at (cx, cy); baseline on the arc.
    up=True arches over the top (reads left to right), up=False along the bottom."""
    f = font(family, size)
    widths = [f.getlength(c) for c in s]
    total = sum(widths) + track * (len(s) - 1)
    ang_total = total / r
    out = []
    a = -ang_total / 2
    for c, w in zip(s, widths):
        mid = a + (w / 2) / r
        if up:
            x, y, rot = cx + r * math.sin(mid), cy - r * math.cos(mid), math.degrees(mid)
        else:
            x, y, rot = cx - r * math.sin(mid), cy + r * math.cos(mid), -math.degrees(mid)
        out.append(f'<text x="0" y="0" font-family="{family}" font-size="{size}" fill="{fill}" text-anchor="middle" '
                   f'transform="translate({x:.1f},{y:.1f}) rotate({rot:.2f})" {extra}>{esc(c)}</text>')
        a += (w + track) / r
    return "\n".join(out)


def svg(w, h, body, defs="", bg=None):
    bgr = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs>{defs}</defs>{bgr}{body}</svg>')


def render(svg_str, out_png, w=None, h=None):
    tmp = out_png + ".svg"
    open(tmp, "w").write(svg_str)
    cmd = ["rsvg-convert", tmp, "-o", out_png]
    if w:
        cmd += ["-w", str(w)]
    if h:
        cmd += ["-h", str(h)]
    subprocess.run(cmd, check=True)
    os.remove(tmp)
    return out_png


def glow(id_, std):
    return (f'<filter id="{id_}" x="-50%" y="-50%" width="200%" height="200%">'
            f'<feGaussianBlur stdDeviation="{std}"/></filter>')


def star_path(cx, cy, r_out, r_in, n=5, rot=-90):
    pts = []
    for i in range(2 * n):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return "M" + " L".join(pts) + " Z"


def snowflake(cx, cy, r, stroke, sw):
    p = []
    for k in range(6):
        a = math.radians(k * 60)
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        p.append(f'<line x1="{cx:.1f}" y1="{cy:.1f}" x2="{x2:.1f}" y2="{y2:.1f}"/>')
        for t in (0.55,):
            bx, by = cx + r * t * math.cos(a), cy + r * t * math.sin(a)
            for s in (-1, 1):
                b = a + s * math.radians(40)
                p.append(f'<line x1="{bx:.1f}" y1="{by:.1f}" x2="{bx + r * .35 * math.cos(b):.1f}" y2="{by + r * .35 * math.sin(b):.1f}"/>')
    return f'<g stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round">{"".join(p)}</g>'
