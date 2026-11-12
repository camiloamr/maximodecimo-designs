#!/usr/bin/env python3
"""Poster 'Scarlet on the Snowline' (5400x7200). Self-contained: downloads lib.py and fonts."""
import os, subprocess, sys, math, random, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py", "lib.py")
FD = os.path.expanduser("~/.fonts/gf/"); os.makedirs(FD, exist_ok=True)
for fam, fn in [("gloock", "Gloock-Regular.ttf")]:
    if not os.path.exists(FD + fn):
        urllib.request.urlretrieve(f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{fn}", FD + fn)
        subprocess.run(["fc-cache", "-f"], check=False)
sys.path.insert(0, HERE)
from lib import text, fit_size, render

W, H = 1080, 1440  # design units, rendered x5
SKY_TOP, SKY_BOT = "#AFC6D4", "#E8F0F4"
MOON = "#F6E7BE"; GOLD = "#C9A256"
RED, RED_D, RED_L = "#C8202F", "#7E1220", "#E8483F"
PINE, PINE_D = "#2B5546", "#173A30"
SNOW = "#FBFDFF"; INK = "#1E2F3A"; BARK = "#5B3B2A"
rnd = random.Random(7)

defs = f'''
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SKY_TOP}"/><stop offset="1" stop-color="{SKY_BOT}"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFF8E4" stop-opacity="1"/><stop offset="0.62" stop-color="{MOON}" stop-opacity="1"/><stop offset="0.80" stop-color="{MOON}" stop-opacity="0.55"/><stop offset="1" stop-color="{MOON}" stop-opacity="0"/></radialGradient>
<radialGradient id="body" cx="0.35" cy="0.3" r="0.8"><stop offset="0" stop-color="{RED_L}"/><stop offset="0.6" stop-color="{RED}"/><stop offset="1" stop-color="{RED_D}"/></radialGradient>
<linearGradient id="wing" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#A3172A"/><stop offset="1" stop-color="#5E0C16"/></linearGradient>
<linearGradient id="tail" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9C1626"/><stop offset="1" stop-color="#4E0A12"/></linearGradient>
<radialGradient id="shine" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#fff" stop-opacity="0.55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
<linearGradient id="hill" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#D7E3EA"/></linearGradient>
'''
b = []
b.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')
# distant pine silhouettes
def pine(x, base, h, col):
    w = h * 0.42
    pts = []
    tiers = 5
    for i in range(tiers):
        y0 = base - h * i / tiers
        y1 = base - h * (i + 1.3) / tiers
        ww = w * (1 - i / tiers)
        pts.append(f'<path d="M{x-ww/2:.1f},{y0:.1f} L{x:.1f},{y1:.1f} L{x+ww/2:.1f},{y0:.1f} Z" fill="{col}"/>')
    return "".join(pts)
for i in range(16):
    x = -20 + i * 75 + rnd.uniform(-20, 20)
    b.append(pine(x, 1080 + rnd.uniform(-10, 10), rnd.uniform(120, 200), "#8FAABA"))
for i in range(11):
    x = 10 + i * 110 + rnd.uniform(-25, 25)
    b.append(pine(x, 1120, rnd.uniform(160, 240), "#6F8FA1"))
b.append(f'<path d="M0,1090 C220,1050 420,1110 600,1080 C800,1050 950,1080 1080,1060 L1080,1440 L0,1440 Z" fill="url(#hill)"/>')

# halo with ornamental ring
CX, CY, R = 540, 560, 330
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R+70}" fill="url(#halo)"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="{GOLD}" stroke-width="3"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R+16}" fill="none" stroke="{GOLD}" stroke-width="1.2" stroke-dasharray="2 9" stroke-linecap="round"/>')

def holly(x, y, ang, s=1.0):
    leaf = ("M0,0 C8,-6 14,-4 18,-12 C22,-6 28,-8 34,-14 C34,-6 40,-2 46,-4 C42,4 44,10 50,14 "
            "C42,16 38,22 36,28 C30,22 24,24 18,28 C16,20 10,16 2,16 C6,10 4,4 0,0 Z")
    g = []
    for a, col in ((-28, PINE), (28, PINE_D)):
        g.append(f'<path d="{leaf}" transform="rotate({a}) scale(1,{1 if a<0 else -1})" fill="{col}" stroke="#123026" stroke-width="1"/>')
    for dx, dy in ((-2, -3), (6, 4), (-4, 7)):
        g.append(f'<circle cx="{dx}" cy="{dy}" r="6.5" fill="{RED}" stroke="{RED_D}" stroke-width="1.2"/><circle cx="{dx-2}" cy="{dy-2}" r="1.8" fill="#fff" opacity="0.7"/>')
    return f'<g transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f}) scale({s})">{"".join(g)}</g>'
for k in (0, 1, 2, 3, 5, 6, 7):  # bottom sprig removed (clashed with the tree line)
    a = math.radians(-90 + k * 45)
    x, y = CX + (R + 16) * math.cos(a), CY + (R + 16) * math.sin(a)
    b.append(holly(x, y, math.degrees(a) + 90, 0.9))

# snowflakes / falling snow (soft dots)
for i in range(140):
    x, y = rnd.uniform(40, W - 40), rnd.uniform(30, 1060)
    if (x - CX) ** 2 + (y - CY) ** 2 < (R - 10) ** 2: continue
    rr = rnd.uniform(1.5, 4.5)
    b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{rr:.1f}" fill="{SNOW}" opacity="{rnd.uniform(.55, .95):.2f}"/>')

# pine bough across the halo
BY = 735
bough = f'<path d="M-20,{BY+40} C200,{BY+10} 380,{BY+8} 560,{BY} C700,{BY-6} 820,{BY-26} 900,{BY-60}" fill="none" stroke="{BARK}" stroke-width="13" stroke-linecap="round"/>'
needles = []
def bez(t, p0, p1, p2, p3):
    return [(1-t)**3*p0[i] + 3*(1-t)**2*t*p1[i] + 3*(1-t)*t*t*p2[i] + t**3*p3[i] for i in (0, 1)]
segs = [((-20, BY+40), (200, BY+10), (380, BY+8), (560, BY)), ((560, BY), (700, BY-6), (820, BY-26), (900, BY-60))]
for seg in segs:
    for j in range(70):
        t = j / 70
        x, y = bez(t, *seg)
        for side in (-1, 1):
            for n in range(3):
                a = math.radians(side * (35 + n * 22) - 90 * side * 0 + (0 if side > 0 else 180))
                L = rnd.uniform(26, 44)
                ang = math.radians((-145 + n * 25) if side < 0 else (145 - n * 25)) * (1 if side < 0 else -1)
                L = L if side < 0 else L * 0.7
                x2, y2 = x + L * math.cos(ang), y - L * math.sin(ang) * side
                col = PINE if n != 1 else PINE_D
                needles.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="3.2" stroke-linecap="round"/>')
b.append("".join(needles))
b.append(bough)
# snow caps on the bough
caps = []
for seg in segs:
    for j in range(0, 70, 5):
        x, y = bez(j / 70, *seg)
        caps.append(f'<ellipse cx="{x:.1f}" cy="{y-14:.1f}" rx="{rnd.uniform(24, 36):.1f}" ry="{rnd.uniform(9, 13):.1f}" fill="{SNOW}"/>')
b.append(f'<g>{"".join(caps)}</g>')

# cardinal (facing left), perched at x~520
bird = []
bird.append(f'<path d="M100,20 C150,60 205,105 245,150 C235,160 222,165 210,160 C170,120 130,90 85,62 Z" fill="url(#tail)"/>')
bird.append(f'<path d="M-95,-78 C-80,-120 -60,-150 -42,-178 C-34,-150 -18,-128 8,-112 C62,-96 108,-50 118,8 C122,40 98,70 60,86 C20,100 -32,98 -66,68 C-104,36 -112,-24 -95,-78 Z" fill="url(#body)" stroke="{RED_D}" stroke-width="2"/>')
bird.append(f'<path d="M-6,-46 C42,-66 98,-36 124,14 C104,44 58,56 12,34 C-14,18 -22,-22 -6,-46 Z" fill="url(#wing)"/>')
for k in range(4):
    bird.append(f'<path d="M{20+k*22},{-30+k*8} C{45+k*22},{-10+k*8} {70+k*18},{8+k*6} {96+k*8},{18+k*4}" fill="none" stroke="#3F0810" stroke-width="2.2" opacity="0.7"/>')
bird.append(f'<ellipse cx="-40" cy="-40" rx="46" ry="34" fill="url(#shine)"/>')
bird.append('<path d="M-104,-90 C-90,-108 -58,-106 -46,-86 C-42,-62 -62,-44 -86,-44 C-100,-50 -108,-70 -104,-90 Z" fill="#1A1416"/>')
bird.append('<path d="M-100,-92 L-146,-72 L-100,-54 C-94,-66 -94,-80 -100,-92 Z" fill="#F08A2B" stroke="#9A4A12" stroke-width="2"/>')
bird.append('<path d="M-100,-92 L-146,-72 L-108,-74 Z" fill="#FFB25A" opacity="0.8"/>')
bird.append('<circle cx="-66" cy="-84" r="7" fill="#050505"/><circle cx="-68.5" cy="-86.5" r="2.4" fill="#fff"/>')
for fx in (-14, 22):
    bird.append(f'<path d="M{fx},90 L{fx-4},118 M{fx-4},118 L{fx-16},124 M{fx-4},118 L{fx+8},124" stroke="#4A3328" stroke-width="5" stroke-linecap="round" fill="none"/>')
b.append(f'<g transform="translate(540,{BY-118}) scale(1.35)"><g transform="translate(0,-10)">{"".join(bird)}</g></g>')

# title (bottom, two lines)
t1, t2 = "Scarlet on", "the Snowline"
size = fit_size(t2, "Gloock", 860, 190)
b.append(text(540, 1240, t1, "Gloock", size, INK))
b.append(text(540, 1240 + size * 0.98, t2, "Gloock", size, INK))
body = "".join(b)
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="5400" height="7200" viewBox="0 0 {W} {H}"><defs>{defs}</defs>{body}</svg>')
out = sys.argv[1] if len(sys.argv) > 1 else "scarlet-snowline-poster.png"
render(svg, out, 5400, 7200)
print(out)

