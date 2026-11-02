"""Two maintenance/reliability-engineer tees (dark fabrics, 4500x5100 transparent).

A) I Saw That Failure Coming
Plan: subject = predictive maintenance humour; audience = reliability/maintenance
engineers and their gift givers; job = an in-joke that reads instantly. Palette: cyan
#43D9E6, violet #7B5CFF, deep #1A1240, amber #FFB000, alarm #FF5A4E, cream #F3EFE6.
Type: Rubik Mono One (instrument-panel feel). Bold element: the glowing crystal ball
with a vibration spike inside.

B) Mean Time Between Coffees
Plan: subject = reliability metric pun (MTBF); same audience; job = cosy retro diner
badge. Palette: cream #FFF1D6, caramel #E9A15B, teal #3BB3A8, tomato #E5533D, mocha
#7A4A2E. Type: Shrikhand (retro script) + Chango (fat display). Bold element: the
steaming mug whose band is a sawtooth reliability chart.
"""
import math, sys
from lib import *

W, H = 4500, 5100
CX = W / 2


def saw_failure(out):
    defs = """
<radialGradient id="ball" cx="40%" cy="35%" r="70%"><stop offset="0" stop-color="#9C86FF"/><stop offset=".55" stop-color="#4B33B8"/><stop offset="1" stop-color="#1A1240"/></radialGradient>
<radialGradient id="aura" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#43D9E6" stop-opacity=".45"/><stop offset=".6" stop-color="#7B5CFF" stop-opacity=".15"/><stop offset="1" stop-color="#7B5CFF" stop-opacity="0"/></radialGradient>
<linearGradient id="brass" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8A5A1C"/><stop offset=".35" stop-color="#FFE29A"/><stop offset=".6" stop-color="#F2B84B"/><stop offset="1" stop-color="#7A4B14"/></linearGradient>
<clipPath id="ballclip"><circle cx="2250" cy="2300" r="1050"/></clipPath>
"""
    bx, by, br = CX, 2300, 1050
    b = []
    b.append(f'<circle cx="{bx}" cy="{by}" r="{br + 520}" fill="url(#aura)"/>')
    b.append(f'<circle cx="{bx}" cy="{by}" r="{br}" fill="url(#ball)"/>')
    g = []
    # grid inside the ball like an analyser screen
    for k in range(-5, 6):
        g.append(f'<line x1="{bx - br}" y1="{by + k * 180}" x2="{bx + br}" y2="{by + k * 180}" stroke="#43D9E6" stroke-width="5" opacity=".18"/>')
        g.append(f'<line x1="{bx + k * 180}" y1="{by - br}" x2="{bx + k * 180}" y2="{by + br}" stroke="#43D9E6" stroke-width="5" opacity=".18"/>')
    # vibration trace: calm, then the spike it predicted
    pts = []
    for i in range(0, 1701):
        x = bx - 850 + i
        t = i / 1700
        amp = 70 + 30 * math.sin(i / 37)
        if 0.62 < t < 0.78:
            amp += 520 * math.sin((t - .62) / .16 * math.pi)
        y = by + 120 + amp * math.sin(i / 11) * (0.6 + 0.4 * math.sin(i / 97))
        pts.append(f"{x:.0f},{y:.0f}")
    g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#43D9E6" stroke-width="16" stroke-linejoin="round"/>')
    # alarm marker over the spike
    sx = bx - 850 + int(1700 * .70)
    g.append(f'<line x1="{sx}" y1="{by - 650}" x2="{sx}" y2="{by + 700}" stroke="#FFB000" stroke-width="10" stroke-dasharray="40 26"/>')
    g.append(f'<path d="M{sx},{by - 860} L{sx + 150},{by - 610} L{sx - 150},{by - 610} Z" fill="#FFB000" stroke="#1A1240" stroke-width="16" stroke-linejoin="round"/>')
    g.append(text(sx, by - 645, "!", "Rubik Mono One", 190, "#1A1240"))
    b.append(f'<g clip-path="url(#ballclip)">{"".join(g)}</g>')
    # glass highlights
    b.append(f'<path d="M{bx - 720},{by - 420} A820,820 0 0 1 {bx - 160},{by - 900}" stroke="#FFFFFF" stroke-width="60" fill="none" stroke-linecap="round" opacity=".45"/>')
    b.append(f'<circle cx="{bx - 560}" cy="{by - 700}" r="40" fill="#FFFFFF" opacity=".6"/>')
    b.append(f'<circle cx="{bx}" cy="{by}" r="{br}" fill="none" stroke="#F3EFE6" stroke-width="24" opacity=".85"/>')
    # brass hex-nut stand
    sy = by + br - 60
    b.append(f'<path d="M{bx - 560},{sy} L{bx + 560},{sy} L{bx + 700},{sy + 300} L{bx - 700},{sy + 300} Z" fill="url(#brass)" stroke="#3A2410" stroke-width="18" stroke-linejoin="round"/>')
    b.append(f'<rect x="{bx - 820}" y="{sy + 290}" width="1640" height="150" rx="40" fill="url(#brass)" stroke="#3A2410" stroke-width="18"/>')
    for dx in (-560, -190, 190, 560):
        b.append(f'<circle cx="{bx + dx}" cy="{sy + 365}" r="40" fill="#7A4B14" stroke="#3A2410" stroke-width="10"/><path d="M{bx + dx - 22},{sy + 365} h44" stroke="#FFE29A" stroke-width="10"/>')
    # type
    s1 = fit_size("I SAW THAT", "Rubik Mono One", 3300, 380)
    b.append(text(CX, 950, "I SAW THAT", "Rubik Mono One", s1, "#F3EFE6"))
    s2 = fit_size("FAILURE", "Rubik Mono One", 3700, 560)
    b.append(text(CX, 4380, "FAILURE", "Rubik Mono One", s2, "#FF5A4E"))
    s3 = fit_size("COMING", "Rubik Mono One", 3000, 470)
    b.append(text(CX, 4380 + s3 * 1.15, "COMING", "Rubik Mono One", s3, "#43D9E6"))
    render(svg(W, H, '<g transform="translate(0,-240)">' + "\n".join(b) + "</g>", defs), out)
    return s1, s2, s3


def mtbc(out):
    defs = """
<linearGradient id="mug" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E9DCC3"/><stop offset=".35" stop-color="#FFF8EA"/><stop offset="1" stop-color="#D8C6A6"/></linearGradient>
<linearGradient id="coffee" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8A5636"/><stop offset="1" stop-color="#4A2C1D"/></linearGradient>
<radialGradient id="disc" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#2F8F86"/><stop offset="1" stop-color="#1D5F5A"/></radialGradient>
"""
    b = []
    cy = 2550
    R = 1380
    b.append(f'<circle cx="{CX}" cy="{cy}" r="{R}" fill="url(#disc)"/>')
    b.append(f'<circle cx="{CX}" cy="{cy}" r="{R}" fill="none" stroke="#FFF1D6" stroke-width="30"/>')
    b.append(f'<circle cx="{CX}" cy="{cy}" r="{R - 80}" fill="none" stroke="#E9A15B" stroke-width="12" stroke-dasharray="4 34" stroke-linecap="round"/>')
    # steam
    for dx, ph in ((-260, 0), (0, 1), (260, 2)):
        x0 = CX + dx
        d = f"M{x0},{cy - 380} "
        for k in range(4):
            sgn = 1 if (k + ph) % 2 else -1
            d += f"q{sgn * 120},-110 0,-220 "
        b.append(f'<path d="{d}" stroke="#FFF1D6" stroke-width="46" fill="none" stroke-linecap="round" opacity=".9"/>')
    # mug body
    mx, my, mw, mh = CX - 560, cy - 330, 1120, 1080
    b.append(f'<path d="M{mx + mw - 20},{my + 230} C{mx + mw + 420},{my + 200} {mx + mw + 420},{my + 760} {mx + mw - 40},{my + 740}" stroke="#FFF1D6" stroke-width="120" fill="none"/>')
    b.append(f'<path d="M{mx + mw - 20},{my + 230} C{mx + mw + 420},{my + 200} {mx + mw + 420},{my + 760} {mx + mw - 40},{my + 740}" stroke="#E9DCC3" stroke-width="60" fill="none"/>')
    b.append(f'<path d="M{mx},{my} L{mx + mw},{my} L{mx + mw - 70},{my + mh} Q{CX},{my + mh + 70} {mx + 70},{my + mh} Z" fill="url(#mug)" stroke="#FFF1D6" stroke-width="22"/>')
    b.append(f'<ellipse cx="{CX}" cy="{my}" rx="{mw / 2}" ry="95" fill="#FFF8EA" stroke="#FFF1D6" stroke-width="22"/>')
    b.append(f'<ellipse cx="{CX}" cy="{my + 12}" rx="{mw / 2 - 60}" ry="62" fill="url(#coffee)"/>')
    # reliability chart band on the mug: sawtooth refills
    band_y, band_h = my + 330, 380
    b.append(f'<rect x="{mx + 35}" y="{band_y}" width="{mw - 85}" height="{band_h}" fill="#E5533D"/>')
    pts = []
    x = mx + 90
    level_top, level_bot = band_y + 60, band_y + band_h - 50
    seg = (mw - 200) / 4
    pts.append(f"{x:.0f},{level_top}")
    for k in range(4):
        pts.append(f"{x + seg * .92:.0f},{level_bot}")
        pts.append(f"{x + seg:.0f},{level_top}")
        x += seg
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#FFF1D6" stroke-width="26" stroke-linejoin="round" stroke-linecap="round"/>')
    for k in range(4):
        rx = mx + 90 + seg * (k + 1)
        b.append(f'<circle cx="{rx:.0f}" cy="{level_top}" r="30" fill="#E9A15B" stroke="#FFF1D6" stroke-width="10"/>')
    # type: arched script on top, fat word below
    b.append(arched("Mean Time Between", "Shrikhand", 330, CX, cy, R + 120, "#E9A15B", track=8))
    cs = fit_size("COFFEES", "Chango", 3500, 640)
    b.append(text(CX + 26, 4560 + 26, "COFFEES", "Chango", cs, "#E5533D", track=12))
    b.append(text(CX, 4560, "COFFEES", "Chango", cs, "#FFF1D6", track=12))
    render(svg(W, H, "\n".join(b), defs), out)
    return cs


if __name__ == "__main__":
    print(saw_failure("out/saw-that-failure-coming-v2.png"))
    print(mtbc("out/mean-time-between-coffees-v2.png"))
