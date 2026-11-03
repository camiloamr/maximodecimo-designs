"""Feliz Navidad pillow: Viejito Pascuero (Santa) in a snowy moon badge.
Plan (frontend-design): subject = Santa's jolly face on a snowy Christmas night; buyer =
Hispanic families in the US; job = warm, instantly-readable Christmas pillow.
Palette: midnight #0F2A4D -> #1C4A7A, snow #F6FAFF, Santa red #D3202E / #97121E,
gold ring #F2C14E, skin #F3C6A2, pine #1E6B4B. Type: Shrikhand for "Feliz Navidad"
(cream with a deep-red offset shadow). Bold element: the big Santa face inside a
gold-ringed moon; everything else (snow, two pines, hills) stays quiet.
Output: 5850x2925, two identical 2925 squares (front and back of the pillow).
"""
import math, random, sys
sys.path.insert(0, ".")
from lib import text, fit_size, svg, render, star_path

S = 2925
CX = S / 2
rnd = random.Random(12)


def snow(n, y0, y1, rmin, rmax, op):
    return "".join(f'<circle cx="{rnd.uniform(0, S):.0f}" cy="{rnd.uniform(y0, y1):.0f}" r="{rnd.uniform(rmin, rmax):.1f}" fill="#FFFFFF" opacity="{rnd.uniform(*op):.2f}"/>' for _ in range(n))


def pine(x, base, h, w):
    g = [f'<rect x="{x - w * .06:.0f}" y="{base - h * .12:.0f}" width="{w * .12:.0f}" height="{h * .14:.0f}" fill="#5A3B22"/>']
    for i, f in enumerate((1.0, .78, .56)):
        top = base - h * (0.35 + i * .25) - h * .25
        bot = base - h * (0.1 + i * .25)
        hw = w / 2 * f
        g.append(f'<path d="M{x},{top:.0f} L{x + hw:.0f},{bot:.0f} L{x - hw:.0f},{bot:.0f} Z" fill="#1E6B4B"/>')
        g.append(f'<path d="M{x},{top:.0f} L{x + hw * .45:.0f},{top + (bot - top) * .45:.0f} Q{x},{top + (bot - top) * .55:.0f} {x - hw * .45:.0f},{top + (bot - top) * .45:.0f} Z" fill="#F6FAFF"/>')
    return "".join(g)


def square():
    defs = """
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0F2A4D"/><stop offset="1" stop-color="#1C4A7A"/></linearGradient>
<radialGradient id="moon" cx="50%" cy="42%" r="60%"><stop offset="0" stop-color="#4E86BF"/><stop offset="1" stop-color="#21507F"/></radialGradient>
<radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset=".6" stop-color="#F2C14E" stop-opacity=".22"/><stop offset="1" stop-color="#F2C14E" stop-opacity="0"/></radialGradient>
<radialGradient id="skin" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#F8D5B6"/><stop offset="1" stop-color="#E8AE88"/></radialGradient>
<radialGradient id="nose" cx="40%" cy="35%" r="65%"><stop offset="0" stop-color="#F6B2A0"/><stop offset="1" stop-color="#D9695E"/></radialGradient>
<linearGradient id="red" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E33A42"/><stop offset="1" stop-color="#97121E"/></linearGradient>
<linearGradient id="fur" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#DCE8F3"/></linearGradient>
<clipPath id="badge"><circle cx="1462.5" cy="1110" r="720"/></clipPath>
"""
    b = [f'<rect width="{S}" height="{S}" fill="url(#sky)"/>', snow(260, 0, 2500, 4, 13, (.35, .9))]
    # moon glow + badge
    b.append(f'<circle cx="{CX}" cy="1110" r="960" fill="url(#glow)"/>')
    inner = [f'<rect width="{S}" height="{S}" fill="url(#moon)"/>', snow(90, 380, 1800, 5, 12, (.4, .9))]
    # coat shoulders
    inner.append(f'<path d="M700,1960 C760,1560 1080,1440 {CX},1440 C1845,1440 2165,1560 2225,1960 Z" fill="url(#red)"/>')
    inner.append(f'<path d="M700,1960 C760,1560 1080,1440 {CX},1440 C1845,1440 2165,1560 2225,1960" fill="none" stroke="#F6FAFF" stroke-width="0"/>')
    # face
    inner.append(f'<ellipse cx="{CX}" cy="1000" rx="300" ry="262" fill="url(#skin)"/>')
    # beard: shadow puffs then white puffs along a U
    pts = []
    for i in range(15):
        a = math.pi * (0.02 + 0.96 * i / 14)
        x = CX - math.cos(a) * 330
        y = 1060 + math.sin(a) * 470
        r = 150 + 40 * math.sin(a)
        pts.append((x, y, r))
    for x, y, r in pts:
        inner.append(f'<circle cx="{x + 18:.0f}" cy="{y + 26:.0f}" r="{r:.0f}" fill="#C9DAEA"/>')
    for x, y, r in pts:
        inner.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.0f}" fill="url(#fur)"/>')
    inner.append(f'<ellipse cx="{CX}" cy="1330" rx="300" ry="230" fill="url(#fur)"/>')
    # mouth, mustache, nose, cheeks, eyes, brows
    inner.append(f'<ellipse cx="{CX}" cy="1205" rx="62" ry="40" fill="#8E1B24"/><ellipse cx="{CX}" cy="1222" rx="34" ry="16" fill="#E46A6A"/>')
    for s in (-1, 1):
        inner.append(f'<ellipse cx="{CX + s * 125:.0f}" cy="1128" rx="150" ry="78" fill="#DCE8F3" transform="rotate({s * 14} {CX + s * 125:.0f} 1128)"/>')
        inner.append(f'<ellipse cx="{CX + s * 118:.0f}" cy="1116" rx="142" ry="70" fill="#FFFFFF" transform="rotate({s * 14} {CX + s * 118:.0f} 1116)"/>')
        inner.append(f'<ellipse cx="{CX + s * 175:.0f}" cy="1045" rx="72" ry="44" fill="#F08F8F" opacity=".75"/>')
        inner.append(f'<path d="M{CX + s * 150 - 52:.0f},968 Q{CX + s * 150:.0f},918 {CX + s * 150 + 52:.0f},968" fill="none" stroke="#3A231A" stroke-width="22" stroke-linecap="round"/>')
        inner.append(f'<path d="M{CX + s * 150 - 78:.0f},905 Q{CX + s * 150:.0f},848 {CX + s * 150 + 78:.0f},900" fill="none" stroke="#FFFFFF" stroke-width="44" stroke-linecap="round"/>')
    inner.append(f'<circle cx="{CX}" cy="1045" r="66" fill="url(#nose)"/><circle cx="{CX - 20}" cy="1022" r="16" fill="#FFFFFF" opacity=".55"/>')
    # hat: cone flopping to the right, then fur brim and pompom
    inner.append('<path d="M1110,800 C1140,560 1330,430 1520,430 C1760,430 1930,600 1985,790 L1870,840 Z" fill="url(#red)"/>')
    inner.append(f'<rect x="1060" y="735" width="805" height="165" rx="82" fill="url(#fur)"/>')
    inner.append('<circle cx="1975" cy="790" r="92" fill="url(#fur)"/>')
    b.append(f'<g clip-path="url(#badge)">{"".join(inner)}</g>')
    b.append(f'<circle cx="{CX}" cy="1110" r="720" fill="none" stroke="#F2C14E" stroke-width="34"/>')
    for x, y, r in ((560, 520, 46), (2380, 600, 38), (2250, 330, 26), (690, 1650, 30), (2290, 1700, 34)):
        b.append(f'<path d="{star_path(x, y, r, r * .32, 4)}" fill="#F2C14E"/>')
    # snowy ground with two pines
    b.append(f'<path d="M0,2470 C600,2380 1100,2520 1500,2450 C1950,2380 2400,2470 {S},2420 L{S},{S} L0,{S} Z" fill="#DCE8F3"/>')
    b.append(f'<path d="M0,2560 C700,2480 1300,2620 1900,2540 C2350,2490 2700,2560 {S},2530 L{S},{S} L0,{S} Z" fill="#F6FAFF"/>')
    b.append(pine(300, 2600, 640, 360))
    b.append(pine(2625, 2600, 640, 360))
    # title
    fs = fit_size("Feliz Navidad", "Shrikhand", 1880, 380)
    b.append(text(CX + 16, 2290 + 18, "Feliz Navidad", "Shrikhand", fs, "#97121E"))
    b.append(text(CX, 2290, "Feliz Navidad", "Shrikhand", fs, "#FFF6E5"))
    return defs, "".join(b)


defs, body = square()
full = f'<g>{body}</g><g transform="translate({S},0)">{body}</g>'
out = sys.argv[1] if len(sys.argv) > 1 else "feliz-navidad-santa-pillow.png"
render(svg(2 * S, S, full, defs), out)
print("saved", out)
