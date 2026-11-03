"""Mean Time Between Coffees, original v1 style (rebuilt at print size from the v1 preview).
Bold condensed-feel stacked headline (Inter Display Black), amber accent, sawtooth
"coffee level" chart with a dashed refill line, monospace labels. 4500x5100, transparent.
"""
import subprocess, sys
from PIL import ImageFont

W, H, K = 4500, 5100, 4.25          # K maps the 1059x1200 reference to print size
CREAM, AMBER, GREY = "#F3EFE6", "#F2A33A", "#9A9A9A"
HEAD = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
REG = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"


def fit(s, path, maxw, start):
    size = start
    while ImageFont.truetype(path, size).getlength(s) > maxw:
        size -= 4
    return size


def t(x, y, s, fam, size, fill, weight=400, anchor="middle", ls=0):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{fam}" font-weight="{weight}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{s}</text>')


def P(x, y):
    return f"{x * K:.0f},{y * K:.0f}"


b = []
cx = 530 * K
b.append(t(cx, 122 * K, "RELIABILITY ENGINEERING", "DejaVu Sans Mono", 118, AMBER, 700, ls=34))
for word, base, col in (("MEAN TIME", 295, CREAM), ("BETWEEN", 448, CREAM), ("COFFEES", 612, AMBER)):
    size = fit(word, HEAD, 3810, 900)
    b.append(t(cx, base * K, word, "Inter Display", size, col, 900, ls=-8))
# axes with arrow heads
b.append(f'<polyline points="{P(148, 690)} {P(148, 955)} {P(930, 955)}" fill="none" stroke="{CREAM}" stroke-width="20" stroke-linejoin="round"/>')
b.append(f'<path d="M{P(148, 664)} L{P(160, 690)} L{P(136, 690)} Z" fill="{CREAM}"/>')
b.append(f'<path d="M{P(948, 955)} L{P(922, 943)} L{P(922, 967)} Z" fill="{CREAM}"/>')
b.append(t(163 * K, 688 * K, "LEVEL", "Inter", 96, GREY, 400, anchor="start", ls=4))
b.append(t(918 * K, 1000 * K, "t", "DejaVu Sans Mono", 120, GREY, 700))
# refill threshold
b.append(f'<line x1="{155 * K:.0f}" y1="{903 * K:.0f}" x2="{915 * K:.0f}" y2="{903 * K:.0f}" stroke="{AMBER}" stroke-width="17" stroke-dasharray="68 50"/>')
b.append(t(884 * K, 937 * K, "REFILL", "DejaVu Sans Mono", 88, AMBER, 700, anchor="end", ls=6))
# sawtooth coffee level
saw = [(155, 718), (327, 903), (343, 718), (513, 903), (530, 718), (700, 903), (716, 718), (888, 903)]
b.append(f'<polyline points="{" ".join(P(x, y) for x, y in saw)}" fill="none" stroke="{CREAM}" stroke-width="26" stroke-linejoin="miter" stroke-linecap="square"/>')
b.append(t(cx, 1065 * K, "MTBC: KEEP IT HIGH. NEVER RUN DRY.", "DejaVu Sans Mono", 116, CREAM, 700, ls=10))

svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(b)}</svg>'
out = sys.argv[1] if len(sys.argv) > 1 else "mean-time-between-coffees.png"
subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H), "-o", out], input=svg.encode(), check=True)
print("saved", out)
