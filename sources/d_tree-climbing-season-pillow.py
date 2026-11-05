#!/usr/bin/env python3
"""Tree Climbing Season cat pillow (square pillow 2:1, both faces) - MaximoDecimo. Style (iii): minimal cute icon.
Output: tree-climbing-season-pillow.png 5850x2925 (two identical 2925 squares)."""
import os, sys, math, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
GF = os.path.expanduser("~/.fonts/gf/"); os.makedirs(GF, exist_ok=True)
for fam, fn in [("chango", "Chango-Regular.ttf")]:
    if not os.path.exists(GF + fn):
        subprocess.run(["curl", "-sfo", GF + fn, f"https://raw.githubusercontent.com/google/fonts/main/ofl/{fam}/{fn}"], check=True)
        subprocess.run(["fc-cache", "-f"])
sys.path.insert(0, HERE)
from lib import svg, render, text, fit_size

S = 2925
BLUSH, BLUSH2 = "#F6D2D4", "#EFB9BE"
PINE, PINE_D = "#1E5B45", "#143F30"
CAT, RED, GOLD, SNOW = "#1C1A24", "#D7263D", "#FFC94A", "#FFFFFF"
cx = S / 2


def tier(top, bottom, half_w, fill):
    # rounded triangle-ish tier with a scalloped bottom edge
    x0, x1 = cx - half_w, cx + half_w
    n = 5
    sc = []
    for i in range(n):
        a = x1 - (i) * (2 * half_w / n); b_ = x1 - (i + 1) * (2 * half_w / n)
        sc.append(f"Q{(a+b_)/2:.1f},{bottom+70:.1f} {b_:.1f},{bottom:.1f}")
    return (f'<path d="M{cx:.1f},{top:.1f} Q{cx+40:.1f},{top+30:.1f} {x1:.1f},{bottom:.1f} {" ".join(sc)} '
            f'Q{cx-40:.1f},{top+30:.1f} {cx:.1f},{top:.1f} Z" fill="{fill}"/>')


def face():
    b = []
    # snow dots, quiet tone-on-tone
    import random
    rnd = random.Random(7)
    for _ in range(70):
        x, y = rnd.uniform(60, S - 60), rnd.uniform(60, S - 60)
        b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(10, 26):.0f}" fill="{SNOW}" opacity="0.55"/>')
    # trunk + tiers
    b.append(f'<rect x="{cx-110}" y="1880" width="220" height="200" rx="30" fill="#7A4A2E"/>')
    b.append(tier(1150, 1900, 820, PINE_D))
    b.append(tier(760, 1500, 640, PINE))
    b.append(tier(380, 1080, 460, PINE_D))
    # cat tail hanging out of the bottom tier (curled tip)
    b.append(f'<path d="M{cx+430},{1880} C{cx+420},{2020} {cx+520},{2090} {cx+590},{2010}" fill="none" stroke="{CAT}" stroke-width="80" stroke-linecap="round"/>')
    # cat head peeking from the middle tier
    hx, hy = cx - 40, 1230
    b.append(f'<path d="M{hx-250},{hy-90} L{hx-215},{hy-360} L{hx-60},{hy-215} Z" fill="{CAT}" stroke="{CAT}" stroke-width="40" stroke-linejoin="round"/>')
    b.append(f'<path d="M{hx+250},{hy-90} L{hx+215},{hy-360} L{hx+60},{hy-215} Z" fill="{CAT}" stroke="{CAT}" stroke-width="40" stroke-linejoin="round"/>')
    b.append(f'<path d="M{hx-205},{hy-140} L{hx-190},{hy-290} L{hx-100},{hy-205} Z" fill="{BLUSH2}"/>')
    b.append(f'<path d="M{hx+205},{hy-140} L{hx+190},{hy-290} L{hx+100},{hy-205} Z" fill="{BLUSH2}"/>')
    b.append(f'<ellipse cx="{hx}" cy="{hy}" rx="300" ry="260" fill="{CAT}"/>')
    for s_ in (-1, 1):
        ex = hx + s_ * 115
        b.append(f'<ellipse cx="{ex}" cy="{hy-20}" rx="62" ry="78" fill="{GOLD}"/>')
        b.append(f'<ellipse cx="{ex}" cy="{hy-15}" rx="22" ry="58" fill="{CAT}"/>')
        b.append(f'<circle cx="{ex+20}" cy="{hy-55}" r="14" fill="{SNOW}"/>')
    b.append(f'<path d="M{hx-30},{hy+70} L{hx+30},{hy+70} L{hx},{hy+105} Z" fill="#F08A9A"/>')
    # paws over the tier edge
    for px in (hx - 170, hx + 170):
        b.append(f'<ellipse cx="{px}" cy="{hy+250}" rx="95" ry="70" fill="{CAT}"/>')
    # one paw batting a dangling ornament (the bold moment)
    ox, oy = hx + 170, hy + 560
    b.append(f'<line x1="{ox}" y1="{hy+300}" x2="{ox}" y2="{oy-150}" stroke="{GOLD}" stroke-width="12"/>')
    b.append(f'<rect x="{ox-45}" y="{oy-175}" width="90" height="60" rx="12" fill="{GOLD}"/>')
    b.append(f'<circle cx="{ox}" cy="{oy}" r="150" fill="url(#orn)"/>')
    b.append(f'<ellipse cx="{ox-55}" cy="{oy-55}" rx="40" ry="26" fill="{SNOW}" opacity="0.7" transform="rotate(-35 {ox-55} {oy-55})"/>')
    # small lights on the tree (quiet)
    for (x, y) in [(cx-300, 960), (cx+250, 900), (cx-480, 1700), (cx+430, 1640), (cx-120, 1810), (cx+40, 620)]:
        b.append(f'<circle cx="{x}" cy="{y}" r="34" fill="{GOLD}"/>')
    # star on top
    from lib import star_path
    b.append(f'<path d="{star_path(cx, 330, 130, 58)}" fill="{GOLD}" stroke="#E0A21F" stroke-width="10" stroke-linejoin="round"/>')
    # title
    l1, l2 = "Tree Climbing", "Season"
    s1 = fit_size(l1, "Chango", 2150, 300)
    b.append(text(cx, 2330, l1, "Chango", s1, PINE_D))
    b.append(text(cx, 2330 + s1 * 1.15, l2, "Chango", s1, PINE_D))
    return "".join(b)


defs = f'<radialGradient id="orn" cx="38%" cy="35%" r="70%"><stop offset="0" stop-color="#FF6B7D"/><stop offset="1" stop-color="#9E1328"/></radialGradient>'
half = f'<g transform="translate({S/2},{S/2}) scale(0.92) translate({-S/2},{-S/2})">' + face() + '</g>'
body = f'<rect width="{2*S}" height="{S}" fill="{BLUSH}"/><g>{half}</g><g transform="translate({S},0)">{half}</g>'
render(svg(2 * S, S, body, defs), "tree-climbing-season-pillow.png")
print("ok tree-climbing-season-pillow.png")

