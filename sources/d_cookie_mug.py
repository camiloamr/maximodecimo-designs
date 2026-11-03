#!/usr/bin/env python3
"""Cookie Quality Inspector - Christmas mug (Printify bp 478 / pp 29). PNG 2475x1155, white.
Self-contained: downloads lib.py and the OFL font it uses, renders the PNG.
All main content sits inside the front band x 760..1715."""
import os, subprocess, sys, math
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
FD = os.path.expanduser("~/.fonts/gf/"); os.makedirs(FD, exist_ok=True)
if not os.path.exists(FD + "BagelFatOne-Regular.ttf"):
    subprocess.run(["curl", "-sfo", FD + "BagelFatOne-Regular.ttf", "https://raw.githubusercontent.com/google/fonts/main/ofl/bagelfatone/BagelFatOne-Regular.ttf"], check=True)
    subprocess.run(["fc-cache", "-f"], check=True)
sys.path.insert(0, HERE)
from lib import font, fit_size, esc, star_path, svg, render

W, H = 2475, 1155
CX = 1237.5
CHOC = "#4A2414"; GINGER = "#C47A3A"; RED = "#D6303B"; MINT = "#3FA77A"; BUTTER = "#F7C948"; ICING = "#FFFDF7"
FAM = "Bagel Fat One"
COLS = [(RED, "#F2646C"), (MINT, "#7BD3A8"), (BUTTER, "#FFE58F"), (GINGER, "#E6A56A")]

defs = "".join(f'<linearGradient id="g{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{l}"/><stop offset="0.55" stop-color="{c}"/><stop offset="1" stop-color="{c}"/></linearGradient>'
               for i, (c, l) in enumerate(COLS))
defs += f'''<radialGradient id="ck" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stop-color="#E7A562"/><stop offset="1" stop-color="#B86A2C"/></radialGradient>
<radialGradient id="lens" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.75"/><stop offset="1" stop-color="#CFEFF5" stop-opacity="0.35"/></radialGradient>'''
b = []

def bubbly_line(s, cy, maxw, start, ci):
    size = fit_size(s, FAM, maxw, start)
    f = font(FAM, size)
    track = size * 0.02
    widths = [f.getlength(c) for c in s]
    total = sum(widths) + track * (len(s) - 1)
    x = CX - total / 2
    sw = size * 0.16
    out_sh, out_st, out_fill, out_gl = [], [], [], []
    for k, (c, w) in enumerate(zip(s, widths)):
        mx = x + w / 2
        g = (ci + k) % len(COLS)
        t = lambda dy, extra: f'<text x="{mx:.1f}" y="{cy+dy:.1f}" font-family="{FAM}" font-size="{size}" text-anchor="middle" {extra}>{esc(c)}</text>'
        out_sh.append(t(size*0.07, f'fill="{CHOC}" stroke="{CHOC}" stroke-width="{sw:.0f}" stroke-linejoin="round"'))
        out_st.append(t(0, f'fill="{CHOC}" stroke="{CHOC}" stroke-width="{sw:.0f}" stroke-linejoin="round"'))
        out_fill.append(t(0, f'fill="url(#g{g})"'))
        if c not in " ":
            out_gl.append(f'<ellipse cx="{mx - w*0.18:.1f}" cy="{cy - size*0.52:.1f}" rx="{size*0.07:.1f}" ry="{size*0.035:.1f}" fill="#FFFFFF" opacity="0.85" transform="rotate(-25 {mx - w*0.18:.1f} {cy - size*0.52:.1f})"/>')
        x += w + track
    return "".join(out_sh + out_st + out_fill + out_gl), size

# cookie + magnifier (top of the front band)
ccx, ccy, cr = CX - 60, 290, 175
bite = f'<clipPath id="bite"><path d="M0,0 H{W} V{H} H0 Z M{ccx+cr*0.95},{ccy-cr*0.75} m-70,0 a70,70 0 1,0 140,0 a70,70 0 1,0 -140,0 M{ccx+cr*1.08},{ccy-cr*0.3} m-55,0 a55,55 0 1,0 110,0 a55,55 0 1,0 -110,0" clip-rule="evenodd"/></clipPath>'
b.append(bite)
b.append(f'<g clip-path="url(#bite)"><circle cx="{ccx}" cy="{ccy}" r="{cr+12}" fill="{CHOC}"/><circle cx="{ccx}" cy="{ccy}" r="{cr}" fill="url(#ck)"/></g>')
for dx, dy, r in [(-80, -60, 24), (30, -100, 20), (-20, 10, 26), (80, 40, 22), (-90, 80, 20), (20, 110, 18), (100, -30, 16)]:
    b.append(f'<ellipse cx="{ccx+dx}" cy="{ccy+dy}" rx="{r}" ry="{r*0.8}" fill="{CHOC}" transform="rotate(20 {ccx+dx} {ccy+dy})"/>')
b.append(f'<ellipse cx="{ccx-70}" cy="{ccy-110}" rx="50" ry="18" fill="#FFFFFF" opacity="0.35" transform="rotate(-30 {ccx-70} {ccy-110})"/>')
# magnifier
mx, my, mr = ccx + 165, ccy + 30, 105
hx2, hy2 = mx + mr*0.7 + 130, my - mr*0.7 - 120
b.append(f'<line x1="{mx+mr*0.7:.0f}" y1="{my-mr*0.7:.0f}" x2="{hx2:.0f}" y2="{hy2:.0f}" stroke="{CHOC}" stroke-width="64" stroke-linecap="round"/>')
b.append(f'<line x1="{mx+mr*0.7+40:.0f}" y1="{my-mr*0.7-32:.0f}" x2="{hx2:.0f}" y2="{hy2:.0f}" stroke="{RED}" stroke-width="40" stroke-linecap="round"/>')
b.append(f'<circle cx="{mx}" cy="{my}" r="{mr+26}" fill="{CHOC}"/><circle cx="{mx}" cy="{my}" r="{mr+12}" fill="{BUTTER}"/>')
b.append(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="#D99050"/>')
b.append(f'<ellipse cx="{mx+8}" cy="{my+10}" rx="48" ry="38" fill="{CHOC}" transform="rotate(20 {mx+8} {my+10})"/>')
b.append(f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="url(#lens)"/>')
b.append(f'<path d="M{mx-55},{my-40} a70,70 0 0,1 60,-40" stroke="#FFFFFF" stroke-width="16" fill="none" stroke-linecap="round"/>')
# approval badge (mint check rosette) upper-left of the cookie
bx, by = ccx - 190, ccy - 120
b.append(f'<path d="{star_path(bx, by, 78, 62, 12)}" fill="{CHOC}"/><path d="{star_path(bx, by, 66, 52, 12)}" fill="{MINT}"/>')
b.append(f'<path d="M{bx-28},{by+2} l20,22 l40,-44" stroke="{ICING}" stroke-width="16" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
# three bubbly lines
y0 = 625
for i, s in enumerate(["Cookie", "Quality", "Inspector"]):
    g, size = bubbly_line(s, y0 + i * 205, 840, 212, i)
    b.append(g)
# tiny side sprinkles (optional decoration)
import random
rnd = random.Random(3)
for side in (0, 1):
    for _ in range(9):
        x = rnd.uniform(470, 690) if side == 0 else rnd.uniform(1785, 2005)
        y = rnd.uniform(220, 950); a = rnd.uniform(0, 180); col = COLS[rnd.randrange(3)][0]
        b.append(f'<rect x="{x-22:.0f}" y="{y-8:.0f}" width="44" height="16" rx="8" fill="{col}" transform="rotate({a:.0f} {x:.0f} {y:.0f})"/>')
out = sys.argv[1] if len(sys.argv) > 1 else "cookie-quality-inspector-mug.png"
render(svg(W, H, "".join(b), defs, bg="#FFFFFF"), out, W, H)
print(out)
