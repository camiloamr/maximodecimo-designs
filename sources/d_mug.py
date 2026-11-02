"""Currently Hibernating With a Book — 11/15 oz mug wrap (2475x1155, white).
Plan: subject = winter reading, audience = US book lovers & their gift givers, job = a
cozy joke that reads from the front of the mug. Palette: ink #2B2140, berry #D6336C,
teal #1F9E9E, mustard #F2B134, coral #F26B5B, plum #6A3D9A, bear #8B5A3C.
Type: Cherry Bomb One (bubbly, per the bestseller mug reference). Bold element: the
multicolour HIBERNATING. Everything inside the front band x 760..1715.
"""
import math, sys
from lib import *

W, H = 2475, 1155
CX = 1237
COLS = ["#D6336C", "#1F9E9E", "#F2B134", "#F26B5B", "#6A3D9A"]
FAM = "Cherry Bomb One"
INK = "#2B2140"

defs = """
<radialGradient id="fur" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#B07A52"/><stop offset="1" stop-color="#7A4A2E"/></radialGradient>
<radialGradient id="shine" cx="35%" cy="25%" r="70%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".7"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
"""


def multicolor(s, y, size, track, start=0):
    f = font(FAM, size)
    ws = [f.getlength(c) for c in s]
    total = sum(ws) + track * (len(s) - 1)
    x = CX - total / 2
    outl, fill = [], []
    for i, (c, w) in enumerate(zip(s, ws)):
        rot = (-1) ** i * 3
        tr = f'transform="rotate({rot} {x + w / 2:.0f} {y - size * .35:.0f})"'
        outl.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FAM}" font-size="{size}" fill="{INK}" stroke="{INK}" stroke-width="{size * .12:.0f}" stroke-linejoin="round" {tr}>{esc(c)}</text>')
        fill.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FAM}" font-size="{size}" fill="{COLS[(i + start) % 5]}" {tr}>{esc(c)}</text>'
                    f'<text x="{x + 3:.0f}" y="{y - 5:.0f}" font-family="{FAM}" font-size="{size}" fill="url(#shine)" {tr}>{esc(c)}</text>')
        x += w + track
    return outl + fill


b = []
# small side decorations (kept light so the front reads first)
for (x, y, s, c) in [(300, 260, 46, "#F2B134"), (520, 820, 34, "#1F9E9E"), (420, 560, 26, "#D6336C"),
                     (2175, 260, 46, "#F2B134"), (1955, 820, 34, "#1F9E9E"), (2055, 560, 26, "#D6336C")]:
    b.append(f'<path d="{star_path(x, y, s, s * .42)}" fill="{c}"/>')
for (x, y) in [(640, 330), (1835, 330)]:
    b.append(snowflake(x, y, 50, "#9CC7E0", 10))

# book stack
books = [("#1F9E9E", 470), ("#D6336C", 430), ("#F2B134", 450)]
by = 640
for col, w in books:
    b.append(f'<rect x="{CX - w / 2}" y="{by - 58}" width="{w}" height="58" rx="10" fill="{col}" stroke="{INK}" stroke-width="10"/>'
             f'<rect x="{CX - w / 2 + 14}" y="{by - 44}" width="{w - 50}" height="10" fill="#FFF6E5" opacity=".9"/>')
    by -= 62
top = by + 4
# sleeping bear lying on the books
b.append(f'<ellipse cx="{CX + 10}" cy="{top - 70}" rx="230" ry="95" fill="url(#fur)" stroke="{INK}" stroke-width="10"/>')
hx, hy = CX - 175, top - 105
for ex in (-62, 62):
    b.append(f'<circle cx="{hx + ex}" cy="{hy - 80}" r="38" fill="url(#fur)" stroke="{INK}" stroke-width="10"/><circle cx="{hx + ex}" cy="{hy - 80}" r="17" fill="#E9B79A"/>')
b.append(f'<circle cx="{hx}" cy="{hy}" r="105" fill="url(#fur)" stroke="{INK}" stroke-width="10"/>')
b.append(f'<ellipse cx="{hx - 8}" cy="{hy + 38}" rx="52" ry="38" fill="#E9C3A5" stroke="{INK}" stroke-width="7"/>')
b.append(f'<ellipse cx="{hx - 8}" cy="{hy + 22}" rx="18" ry="12" fill="{INK}"/>')
for ex in (-42, 32):
    b.append(f'<path d="M{hx + ex - 18},{hy - 12} Q{hx + ex},{hy + 2} {hx + ex + 18},{hy - 12}" stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"/>')
b.append(f'<circle cx="{hx - 70}" cy="{hy + 30}" r="16" fill="#F49BAA" opacity=".7"/><circle cx="{hx + 55}" cy="{hy + 30}" r="16" fill="#F49BAA" opacity=".7"/>')
# open book as a blanket
b.append(f'<path d="M{CX - 60},{top - 40} Q{CX + 70},{top - 110} {CX + 210},{top - 60} L{CX + 210},{top + 4} Q{CX + 70},{top - 50} {CX - 60},{top + 4} Z" fill="#FFF6E5" stroke="{INK}" stroke-width="8"/>')
b.append(f'<path d="M{CX - 60},{top - 40} Q{CX - 190},{top - 100} {CX - 60},{top - 40}" fill="none"/>')
# paws on the book
b.append(f'<ellipse cx="{CX - 50}" cy="{top - 20}" rx="42" ry="28" fill="url(#fur)" stroke="{INK}" stroke-width="8"/>')
# zzz
for (dx, dy, s) in [(-150, -120, 44), (-205, -185, 56), (-270, -260, 70)]:
    b.append(text(hx + dx, hy + dy, "z", FAM, s, "#6A3D9A"))

# type
b.append(text(CX, 150, "currently", FAM, 74, INK, track=4))
hs = fit_size("HIBERNATING", FAM, 920, 230, .02)
b += multicolor("HIBERNATING", 845, hs, hs * .02)
ws = fit_size("with a good book", FAM, 760, 120)
b.append(text(CX, 995, "with a good book", FAM, ws, "#6A3D9A", track=2))
b.append(f'<path d="M{CX - 260},1040 Q{CX},1085 {CX + 260},1040" stroke="#F2B134" stroke-width="14" fill="none" stroke-linecap="round"/>')

out = sys.argv[1] if len(sys.argv) > 1 else "mug.png"
render(svg(W, H, "\n".join(b), defs, bg="#FFFFFF"), out)
print("saved", out, hs, ws)
