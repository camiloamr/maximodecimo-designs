"""Newly Wed, Newly Merry 2026 - round ceramic ornament (Printify bp 537 / pp 41), 1950x1950 full color.
Style iii (minimal cute icons): two penguins leaning together, joined by ONE long red scarf whose
loose ends cross into a heart between them (the bold element). Deep spruce-teal dusk, snow ground.
Self-contained: downloads lib.py and OFL fonts, renders newly-wed-newly-merry-ornament.png next to the script.
"""
import os, subprocess, sys, urllib.request, random
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py", "lib.py")
GF = os.path.expanduser("~/.fonts/gf/"); os.makedirs(GF, exist_ok=True)
for fam, fn in (("dmserifdisplay", "DMSerifDisplay-Regular.ttf"), ("titanone", "TitanOne-Regular.ttf")):
    if not os.path.exists(GF + fn):
        urllib.request.urlretrieve(f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{fn}", GF + fn)
subprocess.run(["fc-cache", "-f"], check=False)
sys.path.insert(0, HERE)
from lib import text, arched, fit_size, svg, render

W = 1950; C = W / 2
SPRUCE, SPRUCE_D = "#1F4A4C", "#123234"
SNOW = "#F4F7F9"; RED = "#C8323C"; RED_D = "#8F1F29"; INK = "#1C2230"; GOLD = "#F2B33D"
random.seed(26)
defs = f'''
<clipPath id="c"><circle cx="{C}" cy="{C}" r="{C}"/></clipPath>
<radialGradient id="sky" cx="50%" cy="40%" r="65%"><stop offset="0" stop-color="#2C6366"/><stop offset="0.6" stop-color="{SPRUCE}"/><stop offset="1" stop-color="{SPRUCE_D}"/></radialGradient>
<radialGradient id="moon" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.22"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
<linearGradient id="belly" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCE6EC"/></linearGradient>
<linearGradient id="scarf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E04550"/><stop offset="1" stop-color="{RED}"/></linearGradient>
'''
b = [f'<g clip-path="url(#c)"><rect width="{W}" height="{W}" fill="url(#sky)"/>',
     f'<circle cx="{C}" cy="880" r="560" fill="url(#moon)"/>']
for _ in range(70):
    x, y = random.uniform(150, 1800), random.uniform(150, 1500)
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{random.uniform(5, 13):.1f}" fill="{SNOW}" opacity="{random.uniform(.35, .8):.2f}"/>')
# snow ground
b.append(f'<path d="M0,1240 C400,1180 700,1215 975,1205 C1250,1195 1550,1170 1950,1235 L1950,1950 L0,1950 Z" fill="{SNOW}"/>')
b.append(f'<path d="M0,1290 C500,1250 1400,1260 1950,1300" fill="none" stroke="#CFDCE3" stroke-width="10"/>')


def penguin(cx, lean, flip):
    s = -1 if flip else 1
    g = [f'<g transform="rotate({lean} {cx} 1230)">']
    g.append(f'<ellipse cx="{cx}" cy="990" rx="200" ry="255" fill="{INK}"/>')            # body
    g.append(f'<ellipse cx="{cx}" cy="1035" rx="140" ry="195" fill="url(#belly)"/>')    # belly
    g.append(f'<circle cx="{cx}" cy="755" r="150" fill="{INK}"/>')                      # head
    g.append(f'<ellipse cx="{cx + s*8}" cy="775" rx="98" ry="88" fill="{SNOW}"/>')       # face
    for ex in (-38, 42):
        g.append(f'<circle cx="{cx + s*ex}" cy="760" r="17" fill="{INK}"/><circle cx="{cx + s*ex + 6}" cy="753" r="6" fill="#fff"/>')
    g.append(f'<path d="M{cx + s*-26},800 L{cx + s*30},800 L{cx + s*2},838 Z" fill="{GOLD}"/>')  # beak
    for ex in (-62, 66):
        g.append(f'<ellipse cx="{cx + s*ex}" cy="812" rx="22" ry="12" fill="#F29AA0" opacity="0.7"/>')
    g.append(f'<ellipse cx="{cx - s*175}" cy="1010" rx="48" ry="150" fill="{INK}" transform="rotate({s*18} {cx - s*175} 1010)"/>')  # outer flipper
    g.append(f'<ellipse cx="{cx - 70}" cy="1238" rx="62" ry="24" fill="{GOLD}"/><ellipse cx="{cx + 70}" cy="1238" rx="62" ry="24" fill="{GOLD}"/>')
    g.append('</g>')
    return "".join(g)

b.append(f'<ellipse cx="{C}" cy="1255" rx="470" ry="40" fill="#B9CAD4" opacity="0.6"/>')
b.append(penguin(C - 245, 7, False))
b.append(penguin(C + 245, -7, True))
# ONE shared scarf: wraps both necks as one band, loose ends meet in a heart between them
b.append(f'<path d="M{C-400},880 C{C-250},945 {C-120},930 {C},905 C{C+120},930 {C+250},945 {C+400},880 L{C+395},935 C{C+250},1000 {C+120},985 {C},960 C{C-120},985 {C-250},1000 {C-395},935 Z" fill="url(#scarf)" stroke="{RED_D}" stroke-width="6"/>')
hx, hy = C, 1080
b.append(f'<path d="M{hx},{hy+120} C{hx-170},{hy+10} {hx-150},{hy-120} {hx-60},{hy-120} C{hx-15},{hy-120} {hx},{hy-85} {hx},{hy-60} C{hx},{hy-85} {hx+15},{hy-120} {hx+60},{hy-120} C{hx+150},{hy-120} {hx+170},{hy+10} {hx},{hy+120} Z" fill="url(#scarf)" stroke="{RED_D}" stroke-width="6"/>')
b.append(f'<ellipse cx="{C}" cy="952" rx="44" ry="34" fill="{RED}" stroke="{RED_D}" stroke-width="6"/>')  # knot
for k in range(-2, 3):
    b.append(f'<line x1="{hx + k*22}" y1="{hy+128}" x2="{hx + k*24}" y2="{hy+168}" stroke="{RED}" stroke-width="10" stroke-linecap="round"/>')
# type
b.append(arched("Newly Wed,", "DM Serif Display", 190, C, 1000, 690, SNOW, track=6))
fs = fit_size("Newly Merry", "DM Serif Display", 1100, 200)
b.append(text(C, 1495, "Newly Merry", "DM Serif Display", fs, SPRUCE_D))
b.append(text(C, 1690, "2026", "Titan One", 170, RED, track=18))
b.append('</g>')
out = os.path.join(HERE, "newly-wed-newly-merry-ornament.png")
render(svg(W, W, "".join(b), defs), out, W, W)
print("ok", out)

