"""Ceramic ornament: 'First Christmas Under This Roof 2026' (style iii, minimalist icon). 1950x1950 PNG."""
import os, subprocess, sys, random, math
G = os.path.expanduser("~/.fonts/gf/")
os.makedirs(G, exist_ok=True)
for f, fam in {"TitanOne-Regular.ttf": "titanone"}.items():
    if not os.path.exists(G + f):
        subprocess.run(["curl", "-sfL", "-o", G + f, f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{f}"], check=True)
subprocess.run(["fc-cache", "-f"], check=True)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sfLO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
sys.path.insert(0, ".")
from lib import text, arched, svg, render, snowflake

S = 1950
C = S / 2
OUT = sys.argv[1] if len(sys.argv) > 1 else "under-this-roof-ornament.png"

CRAN = "#9B2335"    # cranberry field
DEEP = "#6E1626"    # cranberry shadow
SNOW = "#FBF4EC"    # warm snow
GOLD = "#FFC24B"    # lamp gold
PINE = "#24493F"    # pine door/roof

defs = f"""
<clipPath id="c"><circle cx="{C}" cy="{C}" r="{C}"/></clipPath>
<radialGradient id="bg" cx=".5" cy=".42" r=".62"><stop offset="0" stop-color="#B8324A"/><stop offset=".7" stop-color="{CRAN}"/><stop offset="1" stop-color="{DEEP}"/></radialGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{GOLD}" stop-opacity=".75"/><stop offset=".45" stop-color="{GOLD}" stop-opacity=".22"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<linearGradient id="win" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE9A8"/><stop offset="1" stop-color="{GOLD}"/></linearGradient>
"""
b = [f'<g clip-path="url(#c)"><rect width="{S}" height="{S}" fill="url(#bg)"/>']
random.seed(7)
for _ in range(38):
    a, r = random.uniform(0, 2 * math.pi), random.uniform(250, 900)
    x, y = C + r * math.cos(a), C + r * math.sin(a)
    if abs(x - C) < 460 and 520 < y < 1600:
        continue
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.choice([7, 9, 12])}" fill="{SNOW}" opacity=".55"/>')
b.append(snowflake(C - 610, C + 30, 48, SNOW, 9).replace("<g ", '<g opacity=".7" '))
b.append(snowflake(C + 610, C + 30, 48, SNOW, 9).replace("<g ", '<g opacity=".7" '))

# the house: 4 shapes (body, roof, window, door) + snow on roof
hx, hy = C, 1120          # bottom center of house body
bw, bh = 500, 350
b.append(f'<ellipse cx="{C}" cy="{hy - 190}" rx="560" ry="460" fill="url(#glow)"/>')
b.append(f'<rect x="{hx - bw/2}" y="{hy - bh}" width="{bw}" height="{bh}" rx="26" fill="{SNOW}"/>')
b.append(f'<rect x="{hx + 120}" y="{hy - bh - 300}" width="80" height="170" rx="10" fill="{SNOW}"/>')          # chimney
b.append(f'<path d="M{hx - bw/2 - 70},{hy - bh + 14} L{hx},{hy - bh - 290} L{hx + bw/2 + 70},{hy - bh + 14} Z" fill="{PINE}" stroke="{PINE}" stroke-width="40" stroke-linejoin="round"/>')
b.append(f'<path d="M{hx - 150},{hy - bh - 290 + 150*290/(bw/2+70)} L{hx},{hy - bh - 290} L{hx + 150},{hy - bh - 290 + 150*290/(bw/2+70)} Q{hx + 75},{hy - bh - 290 + 150*290/(bw/2+70) - 30} {hx + 20},{hy - bh - 290 + 150*290/(bw/2+70) + 25} Q{hx - 60},{hy - bh - 290 + 150*290/(bw/2+70) - 20} {hx - 150},{hy - bh - 290 + 150*290/(bw/2+70)} Z" fill="{SNOW}" stroke="{SNOW}" stroke-width="30" stroke-linejoin="round"/>')
b.append(f'<rect x="{hx - 190}" y="{hy - bh + 80}" width="150" height="150" rx="18" fill="url(#win)"/>')        # window
b.append(f'<path d="M{hx - 115},{hy - bh + 80} V{hy - bh + 230} M{hx - 190},{hy - bh + 155} H{hx - 40}" stroke="{SNOW}" stroke-width="14"/>')
b.append(f'<rect x="{hx + 50}" y="{hy - 230}" width="130" height="230" rx="65" fill="{PINE}"/>')                 # door
b.append(f'<circle cx="{hx + 115}" cy="{hy - 160}" r="34" fill="none" stroke="#3F7A55" stroke-width="16"/>')     # tiny wreath
b.append(f'<path d="M{C - 470},{hy} H{C + 470}" stroke="{SNOW}" stroke-width="30" stroke-linecap="round"/>')

# text
b.append(arched("FIRST CHRISTMAS", "Titan One", 150, C, C + 40, 700, SNOW, track=8, up=True))
b.append(text(C, 1320, "under this roof", "Titan One", 118, SNOW))
b.append(text(C, 1560, "2026", "Titan One", 210, GOLD, track=14))
b.append('</g>')
render(svg(S, S, "".join(b), defs), OUT)
print(OUT)
