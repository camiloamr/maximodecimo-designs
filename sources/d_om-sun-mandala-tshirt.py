#!/usr/bin/env python3
"""Om Sun Mandala tee (Bella+Canvas 3001) - MaximoDecimo. Style (i): devotional centre illustration
inside a circular badge. Output: om-sun-mandala-tshirt.png 4500x5100 transparent (works on dark and light)."""
import os, sys, math, subprocess
W, H = 4500, 5100
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
GF = os.path.expanduser("~/.fonts/gf/"); os.makedirs(GF, exist_ok=True)
for fam, fn in [("yatraone", "YatraOne-Regular.ttf")]:
    if not os.path.exists(GF + fn):
        subprocess.run(["curl", "-sfo", GF + fn, f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{fn}"], check=True)
        subprocess.run(["fc-cache", "-f"])
sys.path.insert(0, HERE)
from lib import svg, render

INDIGO, INDIGO2 = "#1A1440", "#2C2370"
SAFFRON, MARIGOLD, GOLD, IVORY = "#F29E1F", "#FFB627", "#F7D774", "#FFF6E0"
KUMKUM, LEAF, LEAF2 = "#C8102E", "#2F7D4F", "#1F5C39"
cx, cy = 2250, 2420
R = 1850  # outer garland radius


def P(a, r):
    return cx + r * math.cos(a), cy + r * math.sin(a)


def petal_ring(n, r_in, r_out, width_ang, fill, rot=0, extra=""):
    out = []
    for k in range(n):
        a = math.radians(rot + k * 360 / n - 90)
        x1, y1 = P(a - width_ang, r_in); x2, y2 = P(a + width_ang, r_in)
        tx, ty = P(a, r_out)
        c1x, c1y = P(a - width_ang * 0.9, (r_in + r_out) * 0.55)
        c2x, c2y = P(a + width_ang * 0.9, (r_in + r_out) * 0.55)
        out.append(f'<path d="M{x1:.1f},{y1:.1f} Q{c1x:.1f},{c1y:.1f} {tx:.1f},{ty:.1f} Q{c2x:.1f},{c2y:.1f} {x2:.1f},{y2:.1f} Z" fill="{fill}" {extra}/>')
    return "".join(out)


def marigold(x, y, r, shade):
    s = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{shade}"/>']
    for k in range(10):
        a = math.radians(k * 36)
        s.append(f'<circle cx="{x + r*0.62*math.cos(a):.1f}" cy="{y + r*0.62*math.sin(a):.1f}" r="{r*0.42:.1f}" fill="{shade}" stroke="#B85F00" stroke-width="{r*0.07:.1f}" stroke-opacity="0.55"/>')
    s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*0.42:.1f}" fill="url(#mg)"/>')
    return "".join(s)


defs = f'''
<radialGradient id="field" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="{INDIGO2}"/><stop offset="1" stop-color="{INDIGO}"/></radialGradient>
<radialGradient id="halo" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{GOLD}" stop-opacity="0.75"/><stop offset="0.55" stop-color="{SAFFRON}" stop-opacity="0.28"/><stop offset="1" stop-color="{SAFFRON}" stop-opacity="0"/></radialGradient>
<linearGradient id="om" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF1B8"/><stop offset="0.45" stop-color="{GOLD}"/><stop offset="1" stop-color="{SAFFRON}"/></linearGradient>
<linearGradient id="ray" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{MARIGOLD}"/><stop offset="1" stop-color="{SAFFRON}"/></linearGradient>
<radialGradient id="mg" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#FFE08A"/><stop offset="1" stop-color="#E07B00"/></radialGradient>
<clipPath id="disc"><circle cx="{cx}" cy="{cy}" r="1540"/></clipPath>
'''
b = []
# outer kumkum ring (keeps the edge readable on white and black fabric)
b.append(f'<circle cx="{cx}" cy="{cy}" r="{R+120}" fill="{KUMKUM}"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="{R+60}" fill="{INDIGO}"/>')
# mango-leaf ring between garland flowers
n = 30
for k in range(n):
    a = (k + 0.5) * 2 * math.pi / n - math.pi / 2
    x, y = P(a, R - 60)
    rot = math.degrees(a) + 90
    b.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="58" ry="150" fill="{LEAF}" stroke="{LEAF2}" stroke-width="10" transform="rotate({rot:.1f} {x:.1f} {y:.1f})"/>')
# marigold garland
for k in range(n):
    a = k * 2 * math.pi / n - math.pi / 2
    x, y = P(a, R - 60)
    b.append(marigold(x, y, 118, MARIGOLD if k % 2 == 0 else SAFFRON))
# field
b.append(f'<circle cx="{cx}" cy="{cy}" r="1600" fill="{GOLD}"/>')
b.append(f'<circle cx="{cx}" cy="{cy}" r="1560" fill="url(#field)"/>')
g = []
# sun mandala: two petal rings + dotted ring
g.append(petal_ring(24, 760, 1420, math.radians(7.5), "url(#ray)", rot=7.5, extra='opacity="0.55"'))
g.append(petal_ring(24, 760, 1250, math.radians(6.2), "url(#ray)"))
for k in range(48):
    a = math.radians(k * 7.5 - 90)
    x, y = P(a, 1470)
    g.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="22" fill="{GOLD}" opacity="0.8"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="1100" fill="url(#halo)"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="790" fill="{INDIGO}" stroke="{GOLD}" stroke-width="26"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="740" fill="none" stroke="{GOLD}" stroke-width="8" stroke-dasharray="4 40" stroke-linecap="round"/>')
g.append(f'<circle cx="{cx}" cy="{cy}" r="720" fill="url(#halo)" opacity="0.7"/>')
b.append(f'<g clip-path="url(#disc)">{"".join(g)}</g>')
# Om glyph: shadow, gold body, highlight
from lib import font
_bb = font("Yatra One", 1250).getbbox("\u0950", anchor="ls")  # (x0, y0, x1, y1) from baseline/left
_w = _bb[2] - _bb[0]
ox = cx - _w / 2 - _bb[0] + _w / 2  # centre of ink
ox = cx - (_bb[0] + _bb[2]) / 2 + 0  # text placed with anchor start
oy = cy - (_bb[1] + _bb[3]) / 2
b.append(f'<text x="{ox+22}" y="{oy+30}" font-family="Yatra One" font-size="1250" fill="#0B0820" opacity="0.55" text-anchor="start">&#x950;</text>')
b.append(f'<text x="{ox}" y="{oy}" font-family="Yatra One" font-size="1250" fill="url(#om)" stroke="#8A4A00" stroke-width="10" text-anchor="start">&#x950;</text>')
b.append(f'<text x="{ox-8}" y="{oy-10}" font-family="Yatra One" font-size="1250" fill="none" stroke="#FFFBE6" stroke-opacity="0.35" stroke-width="6" text-anchor="start">&#x950;</text>')

render(svg(W, H, f'<g transform="translate({cx},{cy}) scale(0.93) translate({-cx},{-cy})">' + "".join(b) + "</g>", defs), "om-sun-mandala-tshirt.png")
print("ok om-sun-mandala-tshirt.png")

