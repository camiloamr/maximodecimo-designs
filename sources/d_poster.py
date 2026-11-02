"""Orion winter night poster (5400x7200, 3:4).
Plan: subject = the Orion constellation in the winter sky (real star positions);
audience = US astronomy & cabin-decor buyers; job = cinematic wall art. Reference
pattern (generic, no franchise): dramatic scene + a huge title across the bottom.
Palette: night #050B1E/#10224A, deep teal #1F5560, ice #DCEBFA, star gold #FFD9A0,
Betelgeuse #FF9A5C, Rigel #A9CBFF, nebula rose #E26D9A. Type: Big Shoulders Display
(condensed, monumental) + Gloock for the one line of copy. Bold element: the giant title.
"""
import math, random, sys
from lib import *

W, H = 5400, 7200
rnd = random.Random(42)

defs = """
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#050B1E"/><stop offset=".55" stop-color="#10224A"/><stop offset=".8" stop-color="#1F5560"/><stop offset="1" stop-color="#2B6E73"/></linearGradient>
<radialGradient id="neb" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#E26D9A" stop-opacity=".75"/><stop offset=".5" stop-color="#8E5BC8" stop-opacity=".3"/><stop offset="1" stop-color="#8E5BC8" stop-opacity="0"/></radialGradient>
<radialGradient id="haze" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#6FA8DC" stop-opacity=".22"/><stop offset="1" stop-color="#6FA8DC" stop-opacity="0"/></radialGradient>
<linearGradient id="ridge1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#14304A"/><stop offset="1" stop-color="#0A1A2C"/></linearGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4F9FF"/><stop offset="1" stop-color="#A9CBFF"/></linearGradient>
""" + glow("g20", 20) + glow("g60", 60) + glow("g140", 140)

b = [f'<rect width="{W}" height="{H}" fill="url(#sky)"/>']
# milky haze band + faint star field
b.append(f'<ellipse cx="3600" cy="1800" rx="2600" ry="900" fill="url(#haze)" transform="rotate(-28 3600 1800)"/>')
for _ in range(900):
    x, y = rnd.uniform(0, W), rnd.uniform(0, 5200)
    r = rnd.choice([3, 4, 4, 5, 6, 8])
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#DCEBFA" opacity="{rnd.uniform(.25, .85):.2f}"/>')

stars = {"Betelgeuse": (5 + 55.2 / 60, 7.41, 0.5, "#FF9A5C"), "Bellatrix": (5 + 25.1 / 60, 6.35, 1.64, "#CFE0FF"),
         "Meissa": (5 + 35.1 / 60, 9.93, 3.39, "#DCEBFA"), "Mintaka": (5 + 32.0 / 60, -0.30, 2.23, "#DCEBFA"),
         "Alnilam": (5 + 36.2 / 60, -1.20, 1.69, "#DCEBFA"), "Alnitak": (5 + 40.8 / 60, -1.94, 1.77, "#DCEBFA"),
         "Saiph": (5 + 47.8 / 60, -9.67, 2.06, "#CFE0FF"), "Rigel": (5 + 14.5 / 60, -8.20, 0.13, "#A9CBFF")}
ra0, dec0, scale, cx, cy = 5 + 35 / 60, 0.1, 215, W / 2, 2330


def pos(ra, dec):
    return cx - (ra - ra0) * 15 * math.cos(math.radians(dec)) * scale, cy - (dec - dec0) * scale


P = {k: pos(v[0], v[1]) for k, v in stars.items()}
# Orion nebula (M42) in the sword, below the belt
nx, ny = pos(5 + 35.3 / 60, -5.4)
b.append(f'<circle cx="{nx:.0f}" cy="{ny:.0f}" r="520" fill="url(#neb)"/>')
for k in range(3):
    sx, sy = pos(5 + 35.3 / 60, -4.7 - k * .7)
    b.append(f'<circle cx="{sx:.0f}" cy="{sy:.0f}" r="{16 - k * 3}" fill="#F4F9FF"/>')
lines = [("Meissa", "Betelgeuse"), ("Meissa", "Bellatrix"), ("Betelgeuse", "Alnitak"), ("Bellatrix", "Mintaka"),
         ("Mintaka", "Alnilam"), ("Alnilam", "Alnitak"), ("Alnitak", "Saiph"), ("Mintaka", "Rigel")]
for a, c in lines:
    b.append(f'<line x1="{P[a][0]:.0f}" y1="{P[a][1]:.0f}" x2="{P[c][0]:.0f}" y2="{P[c][1]:.0f}" stroke="#DCEBFA" stroke-width="9" opacity=".45" stroke-dasharray="2 26" stroke-linecap="round"/>')
for k, (ra, dec, mag, col) in stars.items():
    x, y = P[k]
    r = 70 - mag * 14
    gid = "s" + k
    b.append(f'<radialGradient id="{gid}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{col}" stop-opacity=".8"/><stop offset=".25" stop-color="{col}" stop-opacity=".35"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>')
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r * 5:.0f}" fill="url(#{gid})"/>')
    b.append(f'<path d="{star_path(x, y, r * 3.2, r * .3, 4)}" fill="{col}" opacity=".9"/>')
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r * .55:.0f}" fill="#FFFFFF"/>')
# mountain ridges and pine silhouettes
b.append('<path d="M0,5300 L700,4700 L1300,5050 L2100,4420 L2900,5000 L3600,4600 L4400,5100 L5400,4650 L5400,7200 L0,7200 Z" fill="url(#ridge1)" opacity=".85"/>')
b.append('<path d="M0,5550 L900,5150 L1700,5450 L2600,5050 L3500,5480 L4300,5150 L5400,5500 L5400,7200 L0,7200 Z" fill="#081422"/>')
for i in range(42):
    x = i * 135 + rnd.uniform(-30, 30)
    h = rnd.uniform(420, 900)
    base = 5750
    w = h * .42
    b.append(f'<path d="M{x:.0f},{base - h:.0f} L{x + w / 2:.0f},{base:.0f} L{x - w / 2:.0f},{base:.0f} Z" fill="#050D17"/>')
b.append(f'<rect x="0" y="5740" width="{W}" height="{H - 5740}" fill="#050D17"/>')
# title (bold element) + one line of copy
ts = fit_size("ORION", "Big Shoulders Display", 4700, 1700, .04)
b.append(text(W / 2, 6720, "ORION", "Big Shoulders Display", ts, "url(#title)", track=ts * .04, extra='font-weight="900"'))
b.append(text(W / 2, 6980, "The winter hunter rises over the pines", "Gloock", 150, "#A9CBFF", track=6))

out = sys.argv[1] if len(sys.argv) > 1 else "poster.png"
render(svg(W, H, "\n".join(b), defs), out)
print("saved", out, ts)
