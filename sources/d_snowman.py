"""Snowman Building Committee crewneck (dark fabrics).
Plan: subject = snow-day fun, audience = US adults buying cozy Christmas crewnecks,
job = a club-badge joke readable across a room. Palette: midnight #12284A, ice #A9D6F5,
snow #F7FBFF, cranberry #C8243B, pine #2F6B4F, carrot #F28C28. Type: Alfa Slab One only.
Bold element: the cranberry ribbon carrying COMMITTEE. Everything else quiet.
"""
import math, random, sys
from lib import *

W, H = 4500, 5100
CX = 2250
CY = 2350
R = 1350
rnd = random.Random(7)

defs = """
<radialGradient id="night" cx="50%" cy="40%" r="65%"><stop offset="0" stop-color="#2A4F80"/><stop offset="1" stop-color="#12284A"/></radialGradient>
<radialGradient id="ball" cx="38%" cy="32%" r="75%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".6" stop-color="#EAF4FB"/><stop offset="1" stop-color="#9FC4E0"/></radialGradient>
<linearGradient id="hat" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E23B52"/><stop offset="1" stop-color="#9E1A2D"/></linearGradient>
<linearGradient id="rib" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#DA3149"/><stop offset="1" stop-color="#A51C30"/></linearGradient>
<linearGradient id="ground" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F7FBFF"/><stop offset="1" stop-color="#BFDDF2"/></linearGradient>
<clipPath id="disc"><circle cx="2250" cy="2350" r="1350"/></clipPath>
"""

b = []
# badge disc with night sky, snowfall, hills, pines
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#night)"/>')
g = []
for _ in range(90):
    x, y, r = rnd.uniform(CX - R, CX + R), rnd.uniform(CY - R, CY + R * .5), rnd.choice([8, 10, 12, 16, 20])
    g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" fill="#F7FBFF" opacity="{rnd.uniform(.35, .9):.2f}"/>')
for (x, y, s) in [(1300, 1500, 70), (3150, 1400, 60), (1500, 2200, 45), (3000, 2050, 50)]:
    g.append(snowflake(x, y, s, "#A9D6F5", 12))
# pines on the horizon
for (x, h, w) in [(1150, 520, 260), (1380, 700, 320), (3150, 650, 300), (3380, 480, 240), (1700, 380, 190), (2850, 400, 200)]:
    base = 3050
    g.append(f'<path d="M{x},{base - h} L{x + w / 2},{base} L{x - w / 2},{base} Z" fill="#1E4D3A"/>'
             f'<path d="M{x},{base - h} L{x + w * .3},{base - h * .45} L{x - w * .3},{base - h * .45} Z" fill="#2F6B4F"/>'
             f'<path d="M{x},{base - h} l{w * .12:.0f},{h * .18:.0f} l{-w * .24:.0f},0 Z" fill="#F7FBFF"/>')
g.append(f'<path d="M{CX - R},3050 Q{CX - 600},2850 {CX},2980 T{CX + R},2950 L{CX + R},{CY + R} L{CX - R},{CY + R} Z" fill="url(#ground)"/>')
b.append(f'<g clip-path="url(#disc)">{"".join(g)}</g>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#F7FBFF" stroke-width="40"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R + 70}" fill="none" stroke="#A9D6F5" stroke-width="14" stroke-dasharray="40 30"/>')

# snowman (three shaded balls)
sx = CX
b.append(f'<ellipse cx="{sx}" cy="3150" rx="560" ry="80" fill="#9FC4E0" opacity=".7"/>')
for (cy, r) in [(2850, 400), (2290, 300), (1830, 225)]:
    b.append(f'<circle cx="{sx}" cy="{cy}" r="{r}" fill="url(#ball)" stroke="#7FA9CC" stroke-width="10"/>')
# twig arms
for s in (-1, 1):
    b.append(f'<path d="M{sx + s * 270},{2240} L{sx + s * 640},{2010} M{sx + s * 520},{2085} L{sx + s * 600},{1930} M{sx + s * 560},{2060} L{sx + s * 700},{2080}" '
             f'stroke="#6B4423" stroke-width="34" stroke-linecap="round" fill="none"/>')
# coal buttons
for y in (2180, 2300, 2420, 2760, 2900):
    b.append(f'<circle cx="{sx}" cy="{y}" r="30" fill="#22252B"/>')
# face
for dx in (-80, 80):
    b.append(f'<circle cx="{sx + dx}" cy="1790" r="30" fill="#22252B"/><circle cx="{sx + dx + 9}" cy="1780" r="9" fill="#FFFFFF"/>')
b.append(f'<path d="M{sx},1850 L{sx + 230},1890 L{sx},1900 Z" fill="#F28C28" stroke="#C9631A" stroke-width="8"/>')
for i, dx in enumerate((-110, -60, 0, 60, 110)):
    b.append(f'<circle cx="{sx + dx}" cy="{1945 - (0 if i in (0, 4) else 18 if i in (1, 3) else 24)}" r="14" fill="#22252B"/>')
for dx in (-150, 150):
    b.append(f'<circle cx="{sx + dx}" cy="1870" r="40" fill="#F4A3B2" opacity=".55"/>')
# scarf
b.append(f'<path d="M{sx - 250},2050 Q{sx},2140 {sx + 250},2050 L{sx + 260},2140 Q{sx},2230 {sx - 260},2140 Z" fill="url(#rib)"/>')
b.append(f'<path d="M{sx + 120},2120 L{sx + 230},2460 L{sx + 110},2470 L{sx + 30},2140 Z" fill="url(#rib)"/>')
for k in range(4):
    b.append(f'<path d="M{sx - 200 + k * 130},2080 l20,90" stroke="#F7FBFF" stroke-width="22" opacity=".85"/>')
b.append(f'<path d="M{sx + 150},2290 l50,-10 M{sx + 170},2380 l50,-10" stroke="#F7FBFF" stroke-width="22"/>')
# knit beanie with stripe + pompom
b.append(f'<path d="M{sx - 230},1700 Q{sx - 210},1380 {sx},1370 Q{sx + 210},1380 {sx + 230},1700 Z" fill="url(#hat)"/>')
b.append(f'<rect x="{sx - 260}" y="1640" width="520" height="120" rx="50" fill="#F7FBFF"/>')
for k in range(9):
    b.append(f'<line x1="{sx - 220 + k * 55}" y1="1655" x2="{sx - 220 + k * 55}" y2="1745" stroke="#D5E6F3" stroke-width="10"/>')
b.append(f'<path d="M{sx - 190},1520 Q{sx},1490 {sx + 190},1520" stroke="#F7FBFF" stroke-width="36" fill="none"/>')
b.append(f'<circle cx="{sx}" cy="1340" r="95" fill="#F7FBFF"/><circle cx="{sx - 25}" cy="1315" r="40" fill="#FFFFFF"/>')

# arched title above the badge (outlined slab, like a varsity patch)
title = "SNOWMAN BUILDING"
size = 300
arc = arched(title, "Alfa Slab One", size, CX, CY, R + 230, "#F7FBFF", track=18,
             extra='stroke="#12284A" stroke-width="0"')
arc_shadow = arched(title, "Alfa Slab One", size, CX, CY + 22, R + 230, "#C8243B", track=18)
b.insert(0, arc_shadow)
b.append(arc)

# ribbon banner (bold element)
ry, rh = 3420, 470
rw = 1580
b.append(f'<path d="M{CX - rw - 280},{ry + 120} L{CX - rw + 40},{ry + 120} L{CX - rw + 40},{ry + rh + 120} L{CX - rw - 280},{ry + rh + 120} L{CX - rw - 150},{ry + rh / 2 + 120} Z" fill="#8E1526"/>')
b.append(f'<path d="M{CX + rw + 280},{ry + 120} L{CX + rw - 40},{ry + 120} L{CX + rw - 40},{ry + rh + 120} L{CX + rw + 280},{ry + rh + 120} L{CX + rw + 150},{ry + rh / 2 + 120} Z" fill="#8E1526"/>')
b.append(f'<path d="M{CX - rw},{ry} Q{CX},{ry - 120} {CX + rw},{ry} L{CX + rw},{ry + rh} Q{CX},{ry + rh - 120} {CX - rw},{ry + rh} Z" fill="url(#rib)" stroke="#F7FBFF" stroke-width="22"/>')
csize = fit_size("COMMITTEE", "Alfa Slab One", rw * 2 - 260, 400)
b.append(text(CX, ry + rh / 2 + csize * .33 - 20, "COMMITTEE", "Alfa Slab One", csize, "#F7FBFF", track=10))
b.append(text(CX, ry + rh + 330, "EST. FIRST SNOWFALL", "Alfa Slab One", 150, "#A9D6F5", track=30))

out = sys.argv[1] if len(sys.argv) > 1 else "snowman.png"
render(svg(W, H, "\n".join(b), defs), out)
print("saved", out)
