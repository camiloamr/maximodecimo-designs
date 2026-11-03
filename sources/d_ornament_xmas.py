"""Christmas 2026 ornament, modern Christmas scene (1950x1950, round, both sides).
Plan (frontend-design): subject = a cozy Christmas night: faceted pine with a gold star,
a reindeer on the left, Santa (Viejito Pascuero) on the right, gifts and snow.
Buyer = US families collecting a dated ornament each year. Palette: emerald night
#0B3327 -> #1B6B52, cream snow #FFF4E2, gold #F4B942, red #D7263D / #8E1328, reindeer
#A8693A / #E3B98A. Type: Bagel Fat One arched "Christmas" (bubbly, modern) and Titan One
"2026" on a red ribbon. Bold element: the two-tone faceted pine with the glowing star.
Reindeer keeps a brown nose (generic, no named character).
"""
import math, random, sys
sys.path.insert(0, ".")
from lib import arched, text, fit_size, svg, render, star_path

S, C = 1950, 975
rnd = random.Random(7)
CREAM, GOLD, RED, DRED = "#FFF4E2", "#F4B942", "#D7263D", "#8E1328"

defs = f"""
<radialGradient id="bg" cx="50%" cy="40%" r="62%"><stop offset="0" stop-color="#1B6B52"/><stop offset="1" stop-color="#0B3327"/></radialGradient>
<radialGradient id="starglow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{GOLD}" stop-opacity=".55"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<linearGradient id="snow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset="1" stop-color="#E4ECF2"/></linearGradient>
<clipPath id="round"><circle cx="{C}" cy="{C}" r="{C}"/></clipPath>
"""
b = [f'<rect width="{S}" height="{S}" fill="url(#bg)"/>']
# soft snowfall
for _ in range(120):
    x, y = rnd.uniform(0, S), rnd.uniform(0, 1450)
    b.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(3, 9):.1f}" fill="{CREAM}" opacity="{rnd.uniform(.35, .85):.2f}"/>')
# snowy ground
b.append(f'<path d="M0,1330 C420,1250 760,1330 975,1300 C1230,1265 1560,1240 {S},1330 L{S},{S} L0,{S} Z" fill="url(#snow)"/>')
b.append(f'<path d="M0,1420 C500,1370 1400,1440 {S},1390 L{S},{S} L0,{S} Z" fill="#FFFFFF" opacity=".7"/>')

# faceted pine (bold element)
b.append(f'<circle cx="{C}" cy="470" r="230" fill="url(#starglow)"/>')
tiers = [(520, 820, 230), (700, 1040, 330), (900, 1300, 430)]  # top y, base y, half width
for top, base, hw in tiers:
    b.append(f'<path d="M{C},{top} L{C - hw},{base} L{C},{base} Z" fill="#33B57A"/>')
    b.append(f'<path d="M{C},{top} L{C + hw},{base} L{C},{base} Z" fill="#1E7F56"/>')
    b.append(f'<path d="M{C - hw},{base} Q{C - hw * .5},{base - 40} {C},{base - 6} Q{C + hw * .5},{base - 40} {C + hw},{base} Q{C},{base + 26} {C - hw},{base} Z" fill="{CREAM}" opacity=".95"/>')
b.append(f'<rect x="{C - 45}" y="1290" width="90" height="70" fill="#6B3E22"/>')
for x, y, col in ((900, 760, RED), (1050, 900, GOLD), (860, 1000, GOLD), (1110, 1130, RED), (960, 1180, CREAM), (790, 1230, RED), (1180, 1250, GOLD), (1010, 640, CREAM)):
    b.append(f'<circle cx="{x}" cy="{y}" r="24" fill="{col}"/><circle cx="{x - 7}" cy="{y - 8}" r="7" fill="#FFFFFF" opacity=".6"/>')
b.append(f'<path d="{star_path(C, 500, 92, 38)}" fill="{GOLD}" stroke="#FFE7A3" stroke-width="8" stroke-linejoin="round"/>')

# gifts at the base
def gift(x, y, w, h, box, rib):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{box}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h * .22:.0f}" rx="10" fill="#000" opacity=".12"/>'
            f'<rect x="{x + w / 2 - 14:.0f}" y="{y}" width="28" height="{h}" fill="{rib}"/>'
            f'<path d="M{x + w / 2:.0f},{y} c-60,-70 -110,-10 -8,0 c-100,24 -70,-84 8,0 c60,-70 110,-10 8,0 c100,24 70,-84 -8,0" fill="none" stroke="{rib}" stroke-width="18" stroke-linecap="round"/>')
b.append(gift(700, 1250, 170, 140, RED, GOLD))
b.append(gift(1090, 1230, 190, 160, GOLD, RED))
b.append(gift(870, 1310, 120, 100, CREAM, RED))

# reindeer (left, facing the tree)
R = []
R.append('<ellipse cx="520" cy="1150" rx="150" ry="92" fill="#A8693A"/>')
R.append('<ellipse cx="520" cy="1180" rx="110" ry="52" fill="#E3B98A"/>')
for lx in (420, 470, 570, 620):
    R.append(f'<rect x="{lx - 14}" y="1190" width="28" height="140" rx="12" fill="#8A5229"/><rect x="{lx - 16}" y="1310" width="32" height="26" rx="8" fill="#3B2416"/>')
R.append('<path d="M600,1110 C640,1040 650,990 660,950 L720,965 C705,1020 690,1080 655,1140 Z" fill="#A8693A"/>')
R.append('<ellipse cx="715" cy="930" rx="78" ry="58" fill="#A8693A" transform="rotate(18 715 930)"/>')
R.append('<ellipse cx="775" cy="958" rx="42" ry="30" fill="#E3B98A" transform="rotate(18 775 958)"/>')
R.append('<circle cx="805" cy="962" r="17" fill="#3B2416"/>')
R.append('<circle cx="718" cy="912" r="11" fill="#1A120C"/><circle cx="714" cy="908" r="4" fill="#fff"/>')
R.append('<ellipse cx="672" cy="885" rx="30" ry="14" fill="#8A5229" transform="rotate(-35 672 885)"/>')
R.append('<path d="M690,875 C680,800 650,760 610,730 M668,812 C640,800 615,808 590,825 M700,872 C720,800 760,770 800,755 M735,805 C760,790 790,792 810,800" fill="none" stroke="#E3B98A" stroke-width="20" stroke-linecap="round"/>')
R.append('<ellipse cx="372" cy="1110" rx="26" ry="20" fill="#FFF4E2"/>')
R.append('<path d="M640,1015 C600,1050 600,1080 640,1100" fill="none" stroke="' + RED + '" stroke-width="22" stroke-linecap="round"/><circle cx="642" cy="1104" r="15" fill="' + GOLD + '"/>')
b.append("".join(R))

# Santa / Viejito Pascuero (right)
P = []
P.append(f'<path d="M1330,1340 L1610,1340 L1560,1060 L1380,1060 Z" fill="{RED}"/>')
P.append(f'<rect x="1328" y="1300" width="284" height="44" rx="20" fill="{CREAM}"/>')
P.append(f'<rect x="1372" y="1180" width="196" height="30" rx="10" fill="#2B1B12"/><rect x="1450" y="1176" width="40" height="38" rx="6" fill="{GOLD}"/>')
P.append(f'<rect x="1452" y="1060" width="36" height="240" fill="{CREAM}"/>')
P.append(f'<ellipse cx="1360" cy="1150" rx="40" ry="90" fill="{RED}" transform="rotate(20 1360 1150)"/><circle cx="1335" cy="1225" r="30" fill="#2B1B12"/>')
P.append(f'<ellipse cx="1585" cy="1150" rx="40" ry="90" fill="{RED}" transform="rotate(-20 1585 1150)"/><circle cx="1610" cy="1225" r="30" fill="#2B1B12"/>')
P.append('<circle cx="1470" cy="940" r="92" fill="#F3C6A2"/>')
P.append(f'<path d="M1378,950 C1380,1080 1430,1130 1470,1130 C1510,1130 1560,1080 1562,950 C1530,990 1410,990 1378,950 Z" fill="#FFFFFF"/>')
P.append('<ellipse cx="1438" cy="985" rx="44" ry="20" fill="#FFFFFF"/><ellipse cx="1502" cy="985" rx="44" ry="20" fill="#FFFFFF"/>')
P.append('<circle cx="1470" cy="968" r="18" fill="#E58C7E"/>')
P.append('<path d="M1428,930 q12,-14 24,0 M1488,930 q12,-14 24,0" fill="none" stroke="#3A231A" stroke-width="8" stroke-linecap="round"/>')
P.append('<circle cx="1420" cy="958" r="14" fill="#F08F8F" opacity=".7"/><circle cx="1520" cy="958" r="14" fill="#F08F8F" opacity=".7"/>')
P.append(f'<path d="M1370,880 C1380,780 1460,740 1530,760 C1590,780 1615,830 1640,880 L1585,895 C1570,860 1555,840 1540,835 C1555,860 1565,880 1570,885 Z" fill="{RED}"/>')
P.append(f'<rect x="1360" y="860" width="222" height="52" rx="26" fill="{CREAM}"/><circle cx="1640" cy="890" r="34" fill="{CREAM}"/>')
b.append("".join(P))

# title arc + year ribbon
b.append(arched("Christmas", "Bagel Fat One", 190, C + 6, C + 8, 690, DRED, track=6))
b.append(arched("Christmas", "Bagel Fat One", 190, C, C, 690, CREAM, track=6))
rx, ry, rw, rh = C - 300, 1490, 600, 170
b.append(f'<path d="M{rx - 90},{ry + 30} L{rx + 20},{ry + 30} L{rx + 20},{ry + rh + 20} L{rx - 90},{ry + rh + 20} L{rx - 50},{ry + rh / 2 + 25} Z" fill="{DRED}"/>')
b.append(f'<path d="M{rx + rw + 90},{ry + 30} L{rx + rw - 20},{ry + 30} L{rx + rw - 20},{ry + rh + 20} L{rx + rw + 90},{ry + rh + 20} L{rx + rw + 50},{ry + rh / 2 + 25} Z" fill="{DRED}"/>')
b.append(f'<rect x="{rx}" y="{ry}" width="{rw}" height="{rh}" rx="18" fill="{RED}"/>')
b.append(text(C, ry + 132, "2026", "Titan One", 128, CREAM, track=10))
for x in (rx + 70, rx + rw - 70):
    b.append(f'<path d="{star_path(x, ry + rh / 2, 26, 10)}" fill="{GOLD}"/>')
# gold rim

body = "".join(b)
out = sys.argv[1] if len(sys.argv) > 1 else "christmas-2026-ornament.png"
render(svg(S, S, body, defs), out)
print("saved", out)
