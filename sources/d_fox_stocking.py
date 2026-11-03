#!/usr/bin/env python3
"""Snug as a Fox - Christmas stocking (Printify bp 734 / pp 99). PNG 3184x3246 full bleed.
Self-contained: downloads lib.py and the OFL font it uses, renders the PNG."""
import os, subprocess, sys, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
FD = os.path.expanduser("~/.fonts/gf/"); os.makedirs(FD, exist_ok=True)
if not os.path.exists(FD + "Gloock-Regular.ttf"):
    subprocess.run(["curl", "-sfo", FD + "Gloock-Regular.ttf", "https://raw.githubusercontent.com/google/fonts/main/ofl/gloock/Gloock-Regular.ttf"], check=True)
    subprocess.run(["fc-cache", "-f"], check=True)
sys.path.insert(0, HERE)
from lib import text, fit_size, star_path, snowflake, svg, render

W, H = 3184, 3246
SPRUCE, SPRUCE2 = "#16323A", "#0F242B"
MOON = "#F3E9D2"; FOX = "#D9772E"; FOXD = "#9C4A1C"; FROST = "#A9C8D4"; BERRY = "#B3262E"; INK = "#2A1A12"
CX, CY = 1592, 1060

defs = f'''
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{SPRUCE2}"/><stop offset="1" stop-color="{SPRUCE}"/></linearGradient>
<radialGradient id="halo" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="{MOON}" stop-opacity="0.55"/><stop offset="0.7" stop-color="{MOON}" stop-opacity="0.12"/><stop offset="1" stop-color="{MOON}" stop-opacity="0"/></radialGradient>
<radialGradient id="moon" cx="0.45" cy="0.4" r="0.6"><stop offset="0" stop-color="#FFF8E8"/><stop offset="1" stop-color="#E6D6B4"/></radialGradient>
<linearGradient id="fur" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E88A3C"/><stop offset="1" stop-color="{FOXD}"/></linearGradient>
<linearGradient id="tail" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EE9446"/><stop offset="1" stop-color="#B85A22"/></linearGradient>
<radialGradient id="snow" cx="0.5" cy="0.3" r="0.7"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="{FROST}"/></radialGradient>
<radialGradient id="shine" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.55"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
'''
b = [f'<rect width="{W}" height="{H}" fill="url(#bg)"/>']
# falling snow (deterministic)
rnd = random.Random(7)
for _ in range(170):
    x, y, r = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(6, 18)
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#FFFFFF" opacity="{rnd.uniform(.25,.7):.2f}"/>')
# halo + moon disc + ornamental ring
b.append('<g transform="translate(1592,1010) scale(0.8) translate(-1592,-1060)">')
b.append(f'<circle cx="{CX}" cy="{CY}" r="980" fill="url(#halo)"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="690" fill="url(#moon)"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="760" fill="none" stroke="{MOON}" stroke-width="10" opacity="0.85"/>')
for k in range(48):
    a = math.radians(k * 7.5)
    x, y = CX + 815 * math.cos(a), CY + 815 * math.sin(a)
    if k % 4 == 0:
        b.append(f'<path d="{star_path(x, y, 34, 14, 4, rot=math.degrees(a))}" fill="{MOON}"/>')
    else:
        b.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{MOON}" opacity="0.8"/>')
# soft moon craters
for (dx, dy, r) in [(-380, -330, 70), (300, -420, 45), (430, -120, 60), (-480, 80, 40)]:
    b.append(f'<circle cx="{CX+dx}" cy="{CY+dy}" r="{r}" fill="#E2D0AA" opacity="0.55"/>')
# snow mound (clipped to moon so the fox sits inside the circle)
b.append(f'<clipPath id="mc"><circle cx="{CX}" cy="{CY}" r="690"/></clipPath>')
b.append(f'<g clip-path="url(#mc)"><ellipse cx="{CX}" cy="{CY+560}" rx="900" ry="330" fill="url(#snow)"/>'
         f'<ellipse cx="{CX-260}" cy="{CY+470}" rx="260" ry="60" fill="#FFFFFF" opacity="0.8"/></g>')
# shadow under fox
b.append(f'<ellipse cx="{CX+20}" cy="{CY+330}" rx="520" ry="70" fill="#6F8E9A" opacity="0.45"/>')
# --- curled sleeping fox ---
fx, fy = CX + 40, CY + 120
# body
b.append(f'<ellipse cx="{fx+60}" cy="{fy}" rx="430" ry="250" fill="url(#fur)"/>')
b.append(f'<ellipse cx="{fx+120}" cy="{fy-110}" rx="260" ry="90" fill="url(#shine)" opacity="0.7"/>')
# hind leg hint
b.append(f'<path d="M{fx+300},{fy+40} q120,-160 160,40 q-60,120 -200,110 z" fill="{FOXD}" opacity="0.55"/>')
# tail wrapping the front, white tip at left
tail = (f'M{fx+470},{fy+20} C{fx+520},{fy+250} {fx+160},{fy+330} {fx-250},{fy+290} '
        f'C{fx-470},{fy+270} {fx-560},{fy+150} {fx-500},{fy+60} '
        f'C{fx-380},{fy+170} {fx-80},{fy+200} {fx+170},{fy+150} C{fx+330},{fy+120} {fx+420},{fy+80} {fx+470},{fy+20} Z')
b.append(f'<path d="{tail}" fill="url(#tail)"/>')
b.append(f'<clipPath id="tc"><path d="{tail}"/></clipPath>')
b.append(f'<g clip-path="url(#tc)"><ellipse cx="{fx-500}" cy="{fy+200}" rx="190" ry="170" fill="#FFF8EE"/></g>')
b.append(f'<path d="M{fx-60},{fy+235} C{fx+120},{fy+225} {fx+300},{fy+170} {fx+400},{fy+90}" stroke="#F6B07A" stroke-width="14" fill="none" stroke-linecap="round" opacity="0.8"/>')
# head resting on tail (left side)
hx, hy = fx - 230, fy + 30
b.append(f'<path d="M{hx-120},{hy-170} L{hx-60},{hy-330} L{hx+20},{hy-150} Z" fill="{FOXD}"/>')
b.append(f'<path d="M{hx+60},{hy-160} L{hx+170},{hy-300} L{hx+190},{hy-110} Z" fill="{FOXD}"/>')
b.append(f'<path d="M{hx-90},{hy-185} L{hx-62},{hy-280} L{hx-10},{hy-165} Z" fill="{INK}" opacity="0.55"/>')
b.append(f'<path d="M{hx+90},{hy-160} L{hx+160},{hy-250} L{hx+165},{hy-130} Z" fill="{INK}" opacity="0.55"/>')
b.append(f'<ellipse cx="{hx+20}" cy="{hy}" rx="200" ry="165" fill="url(#fur)"/>')
# snout pointing left-down: orange bridge, cream jaw
b.append(f'<path d="M{hx-100},{hy-40} C{hx-200},{hy+10} {hx-300},{hy+80} {hx-355},{hy+115} C{hx-280},{hy+120} {hx-160},{hy+95} {hx-60},{hy+60} Z" fill="#E07F36"/>')
b.append(f'<path d="M{hx+30},{hy+60} C{hx-40},{hy+140} {hx-200},{hy+150} {hx-340},{hy+125} C{hx-230},{hy+100} {hx-90},{hy+70} {hx+30},{hy+60} Z" fill="#FFF8EE"/>')
b.append(f'<ellipse cx="{hx-350}" cy="{hy+118}" rx="34" ry="26" fill="{INK}"/>')
# closed eye + cheek
b.append(f'<path d="M{hx-90},{hy-20} q45,40 95,0" stroke="{INK}" stroke-width="16" fill="none" stroke-linecap="round"/>')
b.append(f'<ellipse cx="{hx+60}" cy="{hy+40}" rx="40" ry="24" fill="#F08A80" opacity="0.6"/>')
b.append(f'<ellipse cx="{hx+40}" cy="{hy-90}" rx="110" ry="40" fill="url(#shine)" opacity="0.6"/>')
# little "z" puffs above head
for i, (dx, dy, s) in enumerate([(-30, -420, 70), (60, -520, 56)]):
    b.append(text(hx + dx, hy + dy, "z", "Gloock", s, SPRUCE, extra='opacity="0.75"'))
# holly sprig on the snow, right
hx2, hy2 = CX + 470, CY + 430
for ang in (-35, 25):
    b.append(f'<g transform="translate({hx2},{hy2}) rotate({ang})"><path d="M0,0 C40,-60 120,-70 170,-40 C130,-20 120,20 150,40 C90,50 40,30 0,0 Z" fill="#2F6B4A"/></g>')
for dx, dy in [(-10, 10), (25, 30), (-35, 40)]:
    b.append(f'<circle cx="{hx2+dx}" cy="{hy2+dy}" r="26" fill="{BERRY}"/><circle cx="{hx2+dx-8}" cy="{hy2+dy-8}" r="7" fill="#FFFFFF" opacity="0.6"/>')
b.append('</g>')
# snowflakes flanking
for (x, y, r) in [(640, 560, 75), (2540, 700, 70)]:
    b.append(snowflake(x, y, r, "#FFFFFF", 12))
# title
t = "Snug as a Fox"
size = fit_size(t, "Gloock", 2000, 330)
b.append(text(CX + 6, 1975 + 10, t, "Gloock", size, "#0A1A1F", extra='opacity="0.5"'))
b.append(text(CX, 1975, t, "Gloock", size, MOON))
out = sys.argv[1] if len(sys.argv) > 1 else "snug-as-a-fox-stocking.png"
render(svg(W, H, "".join(b), defs), out, W, H)
print(out, size)
