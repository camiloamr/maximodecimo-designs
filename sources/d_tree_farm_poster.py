"""Christmas wall art poster: 'Last Light at the Tree Farm' (style iv, cinematic). 5400x7200 PNG."""
import os, subprocess, math, random, sys
os.makedirs(os.path.expanduser("~/.fonts/gf"), exist_ok=True)
G = os.path.expanduser("~/.fonts/gf/")
FONTS = {"Anton-Regular.ttf": "anton", "DMSerifDisplay-Italic.ttf": "dmserifdisplay", "DMSerifDisplay-Regular.ttf": "dmserifdisplay"}
for f, fam in FONTS.items():
    if not os.path.exists(G + f):
        subprocess.run(["curl", "-sfL", "-o", G + f, f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{f}"], check=True)
subprocess.run(["fc-cache", "-f"], check=True)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sfLO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
sys.path.insert(0, ".")
from lib import text, fit_size, svg, render, star_path, esc

W, H = 5400, 7200
OUT = sys.argv[1] if len(sys.argv) > 1 else "tree-farm-poster.png"
random.seed(1226)

PLUM = "#2E2342"      # dusk plum, upper sky
LILAC = "#9C86C4"     # frost lilac, mid sky
APRICOT = "#F4A259"   # afterglow apricot, horizon
SPRUCE = "#173533"    # spruce night, trees and ground
SNOW = "#EEF0F8"      # cool snow white
GOLD = "#FFC95E"      # window gold

defs = f"""
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#1B1530"/><stop offset=".30" stop-color="{PLUM}"/>
 <stop offset=".58" stop-color="#6D5A9A"/><stop offset=".78" stop-color="{LILAC}"/>
 <stop offset=".92" stop-color="#E6A27A"/><stop offset="1" stop-color="{APRICOT}"/></linearGradient>
<radialGradient id="sun" cx=".5" cy=".5" r=".5">
 <stop offset="0" stop-color="#FFE3B0" stop-opacity=".95"/><stop offset=".25" stop-color="{APRICOT}" stop-opacity=".55"/>
 <stop offset="1" stop-color="{APRICOT}" stop-opacity="0"/></radialGradient>
<radialGradient id="win" cx=".5" cy=".5" r=".5">
 <stop offset="0" stop-color="{GOLD}" stop-opacity=".9"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<linearGradient id="h1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#D8C3D9"/><stop offset="1" stop-color="#A895BF"/></linearGradient>
<linearGradient id="h2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E9D6DC"/><stop offset="1" stop-color="#B7A6CC"/></linearGradient>
<linearGradient id="h3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F6E6E0"/><stop offset="1" stop-color="#C9BCD9"/></linearGradient>
<linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#22304A"/><stop offset=".35" stop-color="{SPRUCE}"/><stop offset="1" stop-color="#0F2422"/></linearGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".55" stop-color="{SNOW}"/><stop offset="1" stop-color="#F7CFA6"/></linearGradient>
"""

b = [f'<rect width="{W}" height="{H}" fill="url(#sky)"/>']
# stars in upper sky
for _ in range(140):
    x, y = random.uniform(150, W - 150), random.uniform(120, 2300)
    r = random.choice([6, 8, 10, 12, 16])
    op = 0.35 + 0.6 * (1 - y / 2300)
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#FFFFFF" opacity="{op:.2f}"/>')
for (x, y, r) in [(4300, 900, 70), (980, 1500, 55), (3200, 520, 48)]:
    b.append(f'<path d="{star_path(x, y, r, r*.32, 4, -90)}" fill="#FFF6E6" opacity=".9"/>')
# low sun glow behind hills
b.append(f'<ellipse cx="3500" cy="4050" rx="2300" ry="1300" fill="url(#sun)"/>')
b.append(f'<circle cx="3500" cy="4020" r="200" fill="#FFE7BE" opacity=".95"/>')


def hill(base, amp, freq, phase):
    pts = [(x, base - amp * math.sin(freq * x / W * math.pi * 2 + phase) - amp * .4 * math.sin(freq * 2.3 * x / W * math.pi + phase * 1.7))
           for x in range(-100, W + 101, 50)]
    return pts


def path_of(pts, bottom):
    d = f"M{pts[0][0]},{bottom} " + " ".join(f"L{x:.0f},{y:.0f}" for x, y in pts) + f" L{pts[-1][0]},{bottom} Z"
    return d


def pine(x, y, h, col, snow=True, trunk=True):
    w = h * .42
    parts = []
    for i, (t, s) in enumerate([(0, 1.0), (.28, .78), (.52, .56)]):
        top = y - h * (.45 + t * 1.0) - h * .1
        bot = y - h * t * .85
        ww = w * s
        parts.append(f'<path d="M{x - ww:.0f},{bot:.0f} L{x:.0f},{top - h*.12:.0f} L{x + ww:.0f},{bot:.0f} Z" fill="{col}"/>')
        if snow:
            parts.append(f'<path d="M{x - ww*.42:.0f},{top + (bot-top)*.38:.0f} L{x:.0f},{top - h*.12:.0f} L{x + ww*.42:.0f},{top + (bot-top)*.38:.0f} Q{x:.0f},{top + (bot-top)*.25:.0f} {x - ww*.42:.0f},{top + (bot-top)*.38:.0f} Z" fill="{SNOW}" opacity=".9"/>')
    if trunk: parts.append(f'<rect x="{x - h*.035:.0f}" y="{y - h*.06:.0f}" width="{h*.07:.0f}" height="{h*.08:.0f}" fill="#3A2A2A"/>')
    return "".join(parts)


def interp(pts, x):
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if x1 <= x <= x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return pts[-1][1]


# far ridge: dark forest silhouette
far = hill(4200, 120, 1.3, .4)
b.append(f'<path d="{path_of(far, 7200)}" fill="#5E4F82"/>')
for x in range(-60, W + 60, 70):
    y = interp(far, max(-100, min(W + 100, x)))
    h = random.uniform(160, 300)
    b.append(f'<path d="M{x-h*.3:.0f},{y+10:.0f} L{x:.0f},{y-h:.0f} L{x+h*.3:.0f},{y+10:.0f} Z" fill="#4C4170"/>')

layers = [(4500, 150, 1.0, 1.2, "url(#h1)", "#3E4F6A", 210, 330),
          (4900, 180, .8, 2.6, "url(#h2)", "#2C4A4C", 330, 520),
          (5350, 140, .7, 4.0, "url(#h3)", "#1F3F3C", 520, 800)]
barn_layer = 1
for li, (base, amp, freq, ph, fill, tcol, hmin, hmax) in enumerate(layers):
    pts = hill(base, amp, freq, ph)
    b.append(f'<path d="{path_of(pts, 7200)}" fill="{fill}"/>')
    if li == barn_layer:
        # small barn with glowing window, left of center
        bx = 1450
        by = interp(pts, bx) + 30
        bw, bh = 720, 470
        b.append(f'<ellipse cx="{bx}" cy="{by - bh*.45:.0f}" rx="900" ry="620" fill="url(#win)" opacity=".55"/>')
        b.append(f'<path d="M{bx-bw/2},{by} L{bx-bw/2},{by-bh} L{bx-bw/2-40},{by-bh} L{bx},{by-bh-360} L{bx+bw/2+40},{by-bh} L{bx+bw/2},{by-bh} L{bx+bw/2},{by} Z" fill="#8E2F3A"/>')
        b.append(f'<path d="M{bx-bw/2-60},{by-bh+20} L{bx},{by-bh-380} L{bx+bw/2+60},{by-bh+20} L{bx+bw/2+20},{by-bh+40} L{bx},{by-bh-320} L{bx-bw/2-20},{by-bh+40} Z" fill="{SNOW}"/>')
        b.append(f'<rect x="{bx-120}" y="{by-300}" width="240" height="300" fill="#5C1E27"/>')
        b.append(f'<path d="M{bx-120},{by-300} L{bx+120},{by} M{bx+120},{by-300} L{bx-120},{by}" stroke="{SNOW}" stroke-width="18" opacity=".8"/>')
        b.append(f'<rect x="{bx-80}" y="{by-bh-170}" width="160" height="150" fill="{GOLD}"/>')
        b.append(f'<path d="M{bx},{by-bh-170} V{by-bh-20} M{bx-80},{by-bh-95} H{bx+80}" stroke="#8E2F3A" stroke-width="16"/>')
        b.append(f'<ellipse cx="{bx}" cy="{by+20}" rx="520" ry="50" fill="{SNOW}" opacity=".6"/>')
    # rows of trees along the hill
    step = hmin * .62
    x = -40 + random.uniform(0, step)
    while x < W + 60:
        if li >= barn_layer and 900 < x < 2000:
            x += step; continue
        h = random.uniform(hmin, hmax)
        y = interp(pts, max(-100, min(W + 100, x))) + h * .18 + (li * 20)
        b.append(pine(x, y, h, tcol))
        x += step * random.uniform(.85, 1.25)

# foreground: dark snowy field with two tall pines framing, and a sled track
fg = hill(5650, 90, .6, 5.1)
b.append(f'<path d="{path_of(fg, 7200)}" fill="url(#ground)"/>')
b.append(pine(250, 6000, 1500, "#0E2220", trunk=False))
b.append(pine(5170, 5950, 1350, "#0E2220", trunk=False))
# light snowfall
for _ in range(220):
    x, y = random.uniform(0, W), random.uniform(300, 5600)
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([7, 9, 12, 15])}" fill="#FFFFFF" opacity="{random.uniform(.45,.85):.2f}"/>')

# title block
M = 300
sub = "Last light at the"
ts = fit_size("TREE FARM", "Anton", W - 2 * M - 40, 1700, 0.02)
b.append(text(W / 2, 6930, "TREE FARM", "Anton", ts, "url(#title)", track=round(ts * .02)))
b.append(text(W / 2, 6930 - ts * 0.9, sub, "DM Serif Display", 330, "#F7D9B8", extra='font-style="italic"'))

render(svg(W, H, "".join(b), defs), OUT)
print(OUT, ts)
