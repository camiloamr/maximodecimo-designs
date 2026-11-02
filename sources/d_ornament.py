"""Christmas 2026 woodland mushroom ornament (1950x1950, round ceramic).
Plan: subject = cottagecore woodland Christmas keepsake; audience = US buyers of dated
ornaments; job = a jewel-like round scene that still reads on a tree. Palette: forest
#173F2F/#24563F, toadstool red #D7263D, cream #FFF4E0, gold #E9B949, snow #F4F8FA,
moss #6FA35A. Type: Shrikhand (warm retro script) for "Christmas", Alfa Slab One for 2026.
Bold element: the two glossy toadstools under falling snow. All key content inside 90%.
"""
import math, random, sys
from lib import *

W = H = 1950
C = W / 2
R = W / 2
SAFE = R * .9
rnd = random.Random(26)

defs = """
<radialGradient id="bg" cx="50%" cy="38%" r="70%"><stop offset="0" stop-color="#2E6B50"/><stop offset=".7" stop-color="#1D4A37"/><stop offset="1" stop-color="#123326"/></radialGradient>
<radialGradient id="cap" cx="40%" cy="30%" r="80%"><stop offset="0" stop-color="#F2545B"/><stop offset=".7" stop-color="#C81D35"/><stop offset="1" stop-color="#8E1426"/></radialGradient>
<linearGradient id="stem" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E8D7BE"/><stop offset=".45" stop-color="#FFF8EC"/><stop offset="1" stop-color="#D9C3A2"/></linearGradient>
<linearGradient id="snowg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#CFE2EC"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6DA8B"/><stop offset=".5" stop-color="#E9B949"/><stop offset="1" stop-color="#B9852A"/></linearGradient>
<clipPath id="inner"><circle cx="975" cy="975" r="805"/></clipPath>
""" + glow("g8", 8)

b = [f'<rect width="{W}" height="{H}" fill="url(#bg)"/>']
# gold inner ring (inside the safe circle)
b.append(f'<circle cx="{C}" cy="{C}" r="{SAFE - 30}" fill="none" stroke="url(#gold)" stroke-width="22"/>')
b.append(f'<circle cx="{C}" cy="{C}" r="{SAFE - 75}" fill="none" stroke="#E9B949" stroke-width="5" stroke-dasharray="6 18" stroke-linecap="round"/>')
# background pines
scene_start = len(b)
for (x, h, w, col) in [(520, 520, 300, "#1A4434"), (700, 680, 360, "#215441"), (1260, 640, 340, "#215441"), (1440, 500, 290, "#1A4434")]:
    base = 1330
    b.append(f'<path d="M{x},{base - h} L{x + w / 2},{base} L{x - w / 2},{base} Z" fill="{col}"/>'
             f'<path d="M{x},{base - h} l{w * .14:.0f},{h * .2:.0f} q{-w * .14:.0f},{-30} {-w * .28:.0f},0 Z" fill="#F4F8FA"/>')
# snowy ground
b.append(f'<path d="M150,1330 Q600,1230 975,1300 T1800,1290 L1800,1800 L150,1800 Z" fill="url(#snowg)"/>')
# toadstools


def toad(x, base, h, capw, caph, tilt):
    s = []
    s.append(f'<ellipse cx="{x}" cy="{base + 10}" rx="{capw * .5}" ry="34" fill="#9DB8C6" opacity=".6"/>')
    s.append(f'<path d="M{x - capw * .16},{base} Q{x - capw * .2},{base - h * .55} {x - capw * .12},{base - h} L{x + capw * .12},{base - h} Q{x + capw * .2},{base - h * .55} {x + capw * .16},{base} Z" fill="url(#stem)" stroke="#8C6E4A" stroke-width="6"/>')
    s.append(f'<path d="M{x - capw * .14},{base - h * .62} Q{x},{base - h * .5} {x + capw * .14},{base - h * .62}" stroke="#E2CFAF" stroke-width="14" fill="none"/>')
    g = f'transform="rotate({tilt} {x} {base - h})"'
    cap = f'M{x - capw / 2},{base - h + 10} Q{x - capw * .48},{base - h - caph * 1.1} {x},{base - h - caph} Q{x + capw * .48},{base - h - caph * 1.1} {x + capw / 2},{base - h + 10} Q{x},{base - h - caph * .12} {x - capw / 2},{base - h + 10} Z'
    s.append(f'<g {g}><path d="{cap}" fill="url(#cap)" stroke="#6E0F1E" stroke-width="8"/>')
    for (dx, dy, r) in [(-.28, .45, .07), (-.05, .78, .08), (.22, .5, .065), (.36, .22, .045), (-.4, .16, .045), (.05, .35, .05)]:
        s.append(f'<ellipse cx="{x + dx * capw:.0f}" cy="{base - h - dy * caph:.0f}" rx="{r * capw:.0f}" ry="{r * capw * .8:.0f}" fill="#FFF4E0"/>')
    s.append(f'<path d="M{x - capw * .3},{base - h - caph * .88} Q{x},{base - h - caph * 1.12} {x + capw * .32},{base - h - caph * .86} Q{x + capw * .1},{base - h - caph * .97} {x - capw * .3},{base - h - caph * .88} Z" fill="#FFFFFF"/>')
    s.append(f'<path d="M{x - capw * .22},{base - h - caph * .5} Q{x - capw * .3},{base - h - caph * .25} {x - capw * .38},{base - h - caph * .05}" stroke="#FFFFFF" stroke-width="14" fill="none" stroke-linecap="round" opacity=".55"/></g>')
    return "".join(s)


b.append(toad(1180, 1470, 260, 420, 230, 8))
b.append(toad(820, 1500, 360, 560, 300, -6))
# moss & tiny sprigs
for x in (560, 1000, 1380):
    b.append(f'<path d="M{x},1500 q-30,-60 0,-110 q30,50 0,110 M{x},1500 q40,-40 80,-30 q-30,40 -80,30" fill="#6FA35A"/>')
# falling snow
for _ in range(70):
    a, rr = rnd.uniform(0, 2 * math.pi), rnd.uniform(0, SAFE - 110)
    x, y = C + rr * math.cos(a), C + rr * math.sin(a)
    if y > 1250:
        continue
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.choice([6, 8, 10, 13])}" fill="#FFFFFF" opacity="{rnd.uniform(.5, .95):.2f}"/>')
# clip the scene to the inner ring
scene = b[scene_start:]
del b[scene_start:]
b.append('<g clip-path="url(#inner)">' + ''.join(scene) + '</g>')
# type
b.append(text(C, 520, "Christmas", "Shrikhand", 210, "#123326", extra='stroke="#123326" stroke-width="26" stroke-linejoin="round"'))
b.append(text(C, 520, "Christmas", "Shrikhand", 210, "#FFF4E0"))
b.append(f'<rect x="{C - 230}" y="1600" width="460" height="150" rx="75" fill="url(#gold)" stroke="#7A5418" stroke-width="8"/>')
b.append(text(C, 1712, "2026", "Alfa Slab One", 128, "#123326", track=10))
for s in (-1, 1):
    b.append(f'<path d="{star_path(C + s * 330, 1675, 34, 14, 4)}" fill="#E9B949"/>')

out = sys.argv[1] if len(sys.argv) > 1 else "ornament.png"
render(svg(W, H, "\n".join(b), defs), out)
print("saved", out)
