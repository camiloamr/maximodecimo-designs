"""Sleigh Passed Inspection - ceramic mug 11/15 oz (Printify bp 478 / pp 29), 2475x1155.
Style v (technical-profession humor, Camilo's preferred look): very heavy stacked condensed sans in cream with
ONE amber word, a simple line chart (gift load climbing to a Dec 24 peak under an amber alarm limit) and a
short monospace line. White background (mug spec) with charcoal ink and a deep amber accent; all key content inside the front band x 760..1715.
Self-contained: downloads lib.py and the OFL font, renders sleigh-passed-inspection-mug.png next to the script.
"""
import os, subprocess, sys, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py", "lib.py")
GF = os.path.expanduser("~/.fonts/gf/"); os.makedirs(GF, exist_ok=True)
if not os.path.exists(GF + "Anton-Regular.ttf"):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf", GF + "Anton-Regular.ttf")
subprocess.run(["fc-cache", "-f"], check=False)
sys.path.insert(0, HERE)
from lib import text, fit_size, svg, render

W, H = 2475, 1155
CX = 1237.5; L, R = 790, 1685          # inner front band (30 px inside 760..1715)
BG = "#FFFFFF"; CREAM = "#1F1F22"; AMBER = "#D9861C"; GREY = "#6E7177"  # dark ink on the white mug (CREAM = main ink)
MONO = "DejaVu Sans Mono"
b = []
# stacked headline
y = 60
for word, col in (("SLEIGH", CREAM), ("PASSED", CREAM), ("INSPECTION", AMBER)):
    fs = fit_size(word, "Anton", 760, 400)
    cap = fs * 0.875
    y += cap
    b.append(text(CX, y, word, "Anton", fs, col))
    y += 22
# chart: axes
top, base = y + 45, y + 220
b.append(f'<polyline points="{L},{top} {L},{base} {R},{base}" fill="none" stroke="{CREAM}" stroke-width="7" stroke-linejoin="round"/>')
b.append(f'<path d="M{L},{top-22} L{L+11},{top} L{L-11},{top} Z" fill="{CREAM}"/>')
b.append(f'<path d="M{R+22},{base} L{R},{base-11} L{R},{base+11} Z" fill="{CREAM}"/>')
# amber alarm limit
lim = top + 40
b.append(f'<line x1="{L+6}" y1="{lim}" x2="{R-6}" y2="{lim}" stroke="{AMBER}" stroke-width="6" stroke-dasharray="26 18"/>')
b.append(text(L + 22, lim - 14, "MAX LOAD", MONO, 30, AMBER, anchor="start", extra='font-weight="700"'))
# gift load trend: calm, then climbs to the Dec 24 peak right at the limit, then drops to zero
pts = [(0, .08), (.12, .10), (.24, .09), (.34, .14), (.44, .2), (.54, .3), (.63, .45), (.70, .62), (.76, .8), (.80, .97), (.84, .05), (1, .04)]
xy = " ".join(f"{L + 20 + px * (R - L - 50):.0f},{base - 12 - py * (base - lim - 12):.0f}" for px, py in pts)
b.append(f'<polyline points="{xy}" fill="none" stroke="{CREAM}" stroke-width="11" stroke-linejoin="round" stroke-linecap="round"/>')
pkx = L + 20 + .80 * (R - L - 50)
b.append(f'<circle cx="{pkx:.0f}" cy="{lim + 2}" r="14" fill="{AMBER}"/>')
b.append(text(pkx + 34, lim + 58, "DEC 24", MONO, 30, GREY, anchor="start", extra='font-weight="700"'))
# monospace line
b.append(text(CX, H - 48, "work order 1224: closed", MONO, 50, CREAM, extra='font-weight="700"'))
out = os.path.join(HERE, "sleigh-passed-inspection-mug.png")
render(svg(W, H, "".join(b), bg=BG), out, W, H)
print("ok", out)

