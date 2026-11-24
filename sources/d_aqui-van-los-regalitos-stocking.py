#!/usr/bin/env python3
"""Christmas stocking 'Aqui Van los Regalitos' (3184x3246). Self-contained."""
import os, subprocess, sys, math, random, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py", "lib.py")
FD = os.path.expanduser("~/.fonts/gf/"); os.makedirs(FD, exist_ok=True)
for fam, fn in [("bagelfatone", "BagelFatOne-Regular.ttf")]:
    if not os.path.exists(FD + fn):
        urllib.request.urlretrieve(f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{fn}", FD + fn)
        subprocess.run(["fc-cache", "-f"], check=False)
sys.path.insert(0, HERE)
from lib import font, fit_size, esc, render, star_path

W, H = 3184, 3246
BG, BG_D = "#B81E2C", "#8E1420"
OUT = "#3E0B12"
COLS = ["#FFF1D0", "#FFC23D", "#7FD6BC", "#FF9BBE", "#93CBFF"]
FAM = "Bagel Fat One"
rnd = random.Random(11)

defs = f'''
<radialGradient id="bg" cx="0.5" cy="0.38" r="0.75"><stop offset="0" stop-color="#D02A36"/><stop offset="0.7" stop-color="{BG}"/><stop offset="1" stop-color="{BG_D}"/></radialGradient>
<linearGradient id="gloss2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.55"/><stop offset="0.45" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="gloss" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.65"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
'''
b = [f'<rect width="{W}" height="{H}" fill="url(#bg)"/>']
# quiet background: tiny four-point sparkles in a darker red, sparse
for i in range(70):
    x, y = rnd.uniform(60, W - 60), rnd.uniform(60, H - 60)
    s = rnd.uniform(14, 30)
    b.append(f'<path d="{star_path(x, y, s, s*0.32, 4, -90)}" fill="#E04B52" opacity="0.55"/>')

def bubbly_word(s, cx, base, size, colors, track=0):
    f = font(FAM, size)
    ws = [f.getlength(c) for c in s]
    total = sum(ws) + track * (len(s) - 1)
    x = cx - total / 2
    under, mid, top, shine = [], [], [], []
    for i, (c, w) in enumerate(zip(s, ws)):
        if c == " ":
            x += w + track; continue
        col = colors[i % len(colors)]
        lx = x + w / 2
        rot = (-4, 3, -2, 4, -3)[i % 5]
        tr = f'transform="rotate({rot} {lx:.1f} {base - size*0.35:.1f})"'
        common = f'x="{lx:.1f}" y="{base:.1f}" font-family="{FAM}" font-size="{size}" text-anchor="middle" {tr}'
        under.append(f'<text {common} fill="{OUT}" stroke="{OUT}" stroke-width="{size*0.20:.1f}" stroke-linejoin="round" dy="{size*0.06:.1f}">{esc(c)}</text>')
        mid.append(f'<text {common} fill="{col}" stroke="{OUT}" stroke-width="{size*0.085:.1f}" stroke-linejoin="round" paint-order="stroke">{esc(c)}</text>')
        top.append(f'<text {common} fill="{col}">{esc(c)}</text>')
        shine.append(f'<text {common} fill="url(#gloss2)">{esc(c)}</text>')
        x += w + track
    return "".join(under + mid + top + shine)

# safe zone x 478..2706, y 325..2110
cx = W / 2
s1 = fit_size("Aquí Van", FAM, 1900, 600)
s3 = fit_size("Regalitos", FAM, 2050, 600)
s2 = int(min(s1, s3) * 0.62)
y1 = 330 + s1 * 0.95
y2 = y1 + s2 * 1.02
y3 = y2 + s3 * 1.0
b.append(bubbly_word("Aquí Van", cx, y1, s1, COLS[:3] + COLS[3:], track=10))
b.append(bubbly_word("los", cx, y2, s2, [COLS[0]], track=8))
b.append(bubbly_word("Regalitos", cx, y3, s3, [COLS[1], COLS[2], COLS[3], COLS[4], COLS[0]], track=6))

# three small wrapped gifts under the words
def gift(x, y, w, h, box, rib):
    g = [f'<rect x="{x-w/2:.1f}" y="{y-h:.1f}" width="{w:.1f}" height="{h:.1f}" rx="18" fill="{box}" stroke="{OUT}" stroke-width="16"/>',
         f'<rect x="{x-w/2-14:.1f}" y="{y-h-50:.1f}" width="{w+28:.1f}" height="60" rx="16" fill="{box}" stroke="{OUT}" stroke-width="16"/>',
         f'<rect x="{x-20:.1f}" y="{y-h-50:.1f}" width="40" height="{h+50:.1f}" fill="{rib}" stroke="{OUT}" stroke-width="10"/>',
         f'<path d="M{x:.1f},{y-h-52:.1f} C{x-90:.1f},{y-h-150:.1f} {x-130:.1f},{y-h-40:.1f} {x:.1f},{y-h-52:.1f} Z" fill="{rib}" stroke="{OUT}" stroke-width="14" stroke-linejoin="round"/>',
         f'<path d="M{x:.1f},{y-h-52:.1f} C{x+90:.1f},{y-h-150:.1f} {x+130:.1f},{y-h-40:.1f} {x:.1f},{y-h-52:.1f} Z" fill="{rib}" stroke="{OUT}" stroke-width="14" stroke-linejoin="round"/>',
         f'<rect x="{x-w/2+24:.1f}" y="{y-h+20:.1f}" width="{w*0.18:.1f}" height="{h*0.45:.1f}" rx="10" fill="url(#gloss)"/>']
    return "".join(g)
gy = min(y3 + 470, 2090)
b.append(gift(cx - 380, gy, 230, 190, COLS[2], COLS[0]))
b.append(gift(cx, gy, 290, 240, COLS[1], COLS[3]))
b.append(gift(cx + 380, gy, 230, 190, COLS[4], COLS[1]))

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{defs}</defs>{"".join(b)}</svg>')
out = sys.argv[1] if len(sys.argv) > 1 else "aqui-van-los-regalitos-stocking.png"
render(svg, out, W, H)
print(out, y1, y2, y3, gy)
