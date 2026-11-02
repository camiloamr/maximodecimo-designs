"""Hindu tee: brass diya on a lotus inside a peacock-blue halo ringed with rangoli.
Plan (frontend-design): subject = Diwali / Hindu festival of lights, audience = Hindu
diaspora & gift buyers in the US, job = rich devotional art that reads from across a room.
Palette: peacock #0E4C75/#072B47, marigold #F6A21E, saffron #E8590C, lotus #F06292/#FFC2D9,
gold #F7D774, ivory #FFF4D6. One bold element: the flame's glow. No text, no deity image.
"""
import math, sys
from lib import *

W, H = 4500, 5100
CX, CY = 2250, 2350
R = 1750


def petal(cx, cy, length, width, angle, grad):
    a = math.radians(angle)
    tx, ty = cx + length * math.sin(a), cy - length * math.cos(a)
    nx, ny = math.cos(a), math.sin(a)
    c1 = (cx + width * nx + length * .55 * math.sin(a), cy + width * ny - length * .55 * math.cos(a))
    c2 = (cx - width * nx + length * .55 * math.sin(a), cy - width * ny - length * .55 * math.cos(a))
    return (f'<path d="M{cx:.0f},{cy:.0f} Q{c1[0]:.0f},{c1[1]:.0f} {tx:.0f},{ty:.0f} '
            f'Q{c2[0]:.0f},{c2[1]:.0f} {cx:.0f},{cy:.0f} Z" fill="url(#{grad})" stroke="#B83B6C" stroke-width="10"/>'
            f'<path d="M{cx:.0f},{cy:.0f} L{cx + length * .8 * math.sin(a):.0f},{cy - length * .8 * math.cos(a):.0f}" '
            f'stroke="#D9487F" stroke-width="8" opacity=".55"/>')


defs = """
<radialGradient id="halo" cx="50%" cy="45%" r="60%">
  <stop offset="0" stop-color="#1A6A9A"/><stop offset=".6" stop-color="#0E4C75"/><stop offset="1" stop-color="#072B47"/>
</radialGradient>
<linearGradient id="petalA" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FFE3EE"/><stop offset=".55" stop-color="#F59BBE"/><stop offset="1" stop-color="#E0457F"/></linearGradient>
<linearGradient id="petalB" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#FFF4D6"/><stop offset=".6" stop-color="#FFC2D9"/><stop offset="1" stop-color="#F06292"/></linearGradient>
<linearGradient id="brass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFE9A6"/><stop offset=".35" stop-color="#F2C14E"/><stop offset=".75" stop-color="#C8892B"/><stop offset="1" stop-color="#8A5A1C"/></linearGradient>
<linearGradient id="brassH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9C6A22"/><stop offset=".3" stop-color="#FFE9A6"/><stop offset=".55" stop-color="#F2C14E"/><stop offset="1" stop-color="#8A5A1C"/></linearGradient>
<radialGradient id="flame" cx="50%" cy="72%" r="60%"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".25" stop-color="#FFF3B0"/><stop offset=".6" stop-color="#FFB627"/><stop offset="1" stop-color="#E8590C"/></radialGradient>
<radialGradient id="aura" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#FFD66B" stop-opacity=".95"/><stop offset=".45" stop-color="#F6A21E" stop-opacity=".45"/><stop offset="1" stop-color="#F6A21E" stop-opacity="0"/></radialGradient>
<linearGradient id="leaf" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3FA37A"/><stop offset="1" stop-color="#1D6B4F"/></linearGradient>
""" + glow("soft", 40)

b = []
# halo disc + gold rims
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#halo)"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="none" stroke="#F7D774" stroke-width="34"/>')
b.append(f'<circle cx="{CX}" cy="{CY}" r="{R - 70}" fill="none" stroke="#F7D774" stroke-width="10" opacity=".7"/>')
# rangoli ring: alternating marigold petals and pink dots
ring_r = R - 190
n = 36
for i in range(n):
    a = 2 * math.pi * i / n
    x, y = CX + ring_r * math.sin(a), CY - ring_r * math.cos(a)
    if i % 2 == 0:
        rot = math.degrees(a)
        b.append(f'<ellipse cx="0" cy="0" rx="42" ry="88" fill="#F6A21E" transform="translate({x:.0f},{y:.0f}) rotate({rot:.1f})"/>'
                 f'<ellipse cx="0" cy="0" rx="18" ry="44" fill="#FFF4D6" transform="translate({x:.0f},{y:.0f}) rotate({rot:.1f})"/>')
    else:
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="34" fill="#F06292"/><circle cx="{x:.0f}" cy="{y:.0f}" r="12" fill="#FFF4D6"/>')
inner = ring_r - 140
for i in range(72):
    a = 2 * math.pi * i / 72
    b.append(f'<circle cx="{CX + inner * math.sin(a):.0f}" cy="{CY - inner * math.cos(a):.0f}" r="11" fill="#F7D774" opacity=".85"/>')
# sparkles inside the halo
for (sx, sy, s) in [(1250, 1350, 70), (3230, 1450, 90), (1500, 2050, 45), (3050, 2150, 55), (2700, 1050, 40), (1800, 1000, 50)]:
    b.append(f'<path d="{star_path(sx, sy, s, s * .28, 4, -90)}" fill="#FFF4D6" opacity=".9"/>')
# flame aura (the bold element)
fx, fy = CX, 2250
b.append(f'<circle cx="{fx}" cy="{fy}" r="1050" fill="url(#aura)"/>')
# lotus leaves
for s in (-1, 1):
    b.append(f'<path d="M{CX},{3350} C{CX + s * 500},{3200} {CX + s * 1150},{3230} {CX + s * 1330},{3420} '
             f'C{CX + s * 1000},{3570} {CX + s * 450},{3520} {CX},{3420} Z" fill="url(#leaf)" stroke="#145A40" stroke-width="12"/>')
# lotus back row then front row
base_y = 3420
for ang in (-78, -52, -26, 0, 26, 52, 78):
    b.append(petal(CX, base_y, 1050 if ang == 0 else 980 - abs(ang) * 3, 300, ang, "petalA"))
for ang in (-60, -30, 0, 30, 60):
    b.append(petal(CX, base_y + 40, 760 - abs(ang) * 3, 270, ang * .9, "petalB"))
# diya (brass lamp), front view, sitting in the lotus; flame on the centre line
dy = 2780  # rim centre
lw = 820   # half width
b.append(f'<path d="M{CX - lw},{dy} C{CX - lw + 60},{dy + 470} {CX + lw - 60},{dy + 470} {CX + lw},{dy} Z" fill="url(#brass)" stroke="#7A4B14" stroke-width="14"/>')
for i in range(11):  # engraved bead band
    x = CX - 600 + i * 120
    yy = dy + 150 + 0.00028 * (x - CX) ** 2 * -1 + 40
    b.append(f'<circle cx="{x}" cy="{yy:.0f}" r="22" fill="#8A5A1C" opacity=".55"/>')
b.append(f'<path d="M{CX - 520},{dy + 250} Q{CX},{dy + 330} {CX + 520},{dy + 250}" stroke="#FFE9A6" stroke-width="14" fill="none" opacity=".6"/>')
b.append(f'<ellipse cx="{CX}" cy="{dy}" rx="{lw}" ry="150" fill="url(#brassH)" stroke="#7A4B14" stroke-width="14"/>')
b.append(f'<ellipse cx="{CX}" cy="{dy + 10}" rx="{lw - 90}" ry="105" fill="#6B3E10"/>')
b.append(f'<ellipse cx="{CX}" cy="{dy + 30}" rx="{lw - 150}" ry="70" fill="#A8671E" opacity=".8"/>')
# front spout (pointed lip toward the viewer) carrying the wick
b.append(f'<path d="M{CX - 170},{dy + 110} Q{CX},{dy + 330} {CX + 170},{dy + 110} Z" fill="url(#brass)" stroke="#7A4B14" stroke-width="12"/>')
wx, wy = CX, dy + 120
b.append(f'<path d="M{wx},{wy + 20} Q{wx + 25},{wy - 40} {wx},{wy - 110}" stroke="#3A2410" stroke-width="26" fill="none" stroke-linecap="round"/>')
fl = 900
b.append(f'<path d="M{wx},{wy - fl - 80} C{wx + 300},{wy - fl * .55} {wx + 290},{wy - 170} {wx},{wy - 90} '
         f'C{wx - 290},{wy - 170} {wx - 300},{wy - fl * .55} {wx},{wy - fl - 80} Z" fill="#F6A21E" filter="url(#soft)" opacity=".85"/>')
b.append(f'<path d="M{wx},{wy - fl} C{wx + 250},{wy - fl * .55} {wx + 240},{wy - 180} {wx},{wy - 100} '
         f'C{wx - 240},{wy - 180} {wx - 250},{wy - fl * .55} {wx},{wy - fl} Z" fill="url(#flame)"/>')
b.append(f'<ellipse cx="{wx}" cy="{wy - 330}" rx="85" ry="170" fill="#FFFFFF" opacity=".92"/>')
# marigold garland drooping across the halo top
for side in (-1, 1):
    for k in range(9):
        t = k / 8
        x = CX + side * (180 + t * 960)
        y = 860 + 330 * math.sin(t * math.pi * .95) + t * 260
        col = "#F6A21E" if k % 2 else "#E8590C"
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="66" fill="{col}"/><circle cx="{x:.0f}" cy="{y:.0f}" r="66" fill="none" stroke="#B5400A" stroke-width="10" stroke-dasharray="18 14"/>')
b.append(f'<path d="M{CX - 110},{830} l110,-120 l110,120 l-110,120 Z" fill="#F7D774"/>')

out = sys.argv[1] if len(sys.argv) > 1 else "diya.png"
render(svg(W, H, "\n".join(b), defs), out)
print("saved", out)
