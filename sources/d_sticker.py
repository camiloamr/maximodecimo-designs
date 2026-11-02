"""Twinkle Light Technician die-cut sticker.
Plan: subject = the family member who untangles the Christmas lights; audience = US
stocking-stuffer shoppers; job = a cheerful, instantly readable die-cut at 2-3 inches.
Palette: bulb red #E63946, green #2A9D5C, gold #FFC23D, blue #3A86FF, pink #FF5FA2,
outline navy #1B2A49, border white. Type: Bagel Fat One (bubbly, like the bestseller mug lettering).
Bold element: each letter is a bulb colour; one white die-cut border holds it all in one piece.
"""
import math, sys
from lib import *

W = H = 1664
CX = W / 2
COLS = ["#E63946", "#2A9D5C", "#FFC23D", "#3A86FF", "#FF5FA2"]
FAM = "Bagel Fat One"

defs = """
<radialGradient id="shine" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".75"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
""" + glow("bglow", 14)


def word(s, y, size, track, layer):
    f = font(FAM, size)
    ws = [f.getlength(c) for c in s]
    total = sum(ws) + track * (len(s) - 1)
    x = CX - total / 2
    out = []
    for i, (c, w) in enumerate(zip(s, ws)):
        if c == " ":
            x += w + track
            continue
        col = COLS[(i + (0 if y < 900 else 2)) % len(COLS)]
        wob = (-1) ** i * 2.5
        tr = f'transform="rotate({wob} {x + w / 2:.0f} {y - size * .35:.0f})"'
        if layer == "border":
            out.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FAM}" font-size="{size}" fill="#FFFFFF" stroke="#FFFFFF" stroke-width="110" stroke-linejoin="round" {tr}>{esc(c)}</text>')
        elif layer == "outline":
            out.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FAM}" font-size="{size}" fill="#1B2A49" stroke="#1B2A49" stroke-width="34" stroke-linejoin="round" {tr}>{esc(c)}</text>')
        else:
            out.append(f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FAM}" font-size="{size}" fill="{col}" {tr}>{esc(c)}</text>'
                       f'<text x="{x + 6:.0f}" y="{y - 8:.0f}" font-family="{FAM}" font-size="{size}" fill="url(#shine)" {tr}>{esc(c)}</text>')
        x += w + track
    return out


l1, l2 = "TWINKLE", "LIGHT",
s1 = fit_size("TWINKLE", FAM, 1220, 330, .02)
s2 = fit_size("LIGHT", FAM, 900, s1, .02)
s3 = fit_size("TECHNICIAN", FAM, 1300, 260, .01)
y1, y2, y3 = 760, 760 + s2 * .92, 760 + s2 * .92 + s3 * .98

# light string with bulbs above the words
wire_pts = []
bulbs = []
for k in range(7):
    t = k / 6
    x = 330 + t * 1004
    y = 330 + 70 * math.sin(t * math.pi * 2)
    bulbs.append((x, y, COLS[k % 5], (-1) ** k * 14))
wire = "M250,330 " + " ".join(f"Q{(bulbs[i][0] + bulbs[i + 1][0]) / 2:.0f},{bulbs[i][1] - 90:.0f} {bulbs[i + 1][0]:.0f},{bulbs[i + 1][1]:.0f}" for i in range(6))
wire = f"M{bulbs[0][0]:.0f},{bulbs[0][1]:.0f} " + wire.split(" ", 1)[1]


def bulb(x, y, col, rot, layer):
    tr = f'transform="rotate({rot} {x:.0f} {y:.0f})"'
    body = f'M{x - 52:.0f},{y + 40:.0f} C{x - 70:.0f},{y + 150:.0f} {x - 20:.0f},{y + 215:.0f} {x:.0f},{y + 225:.0f} C{x + 20:.0f},{y + 215:.0f} {x + 70:.0f},{y + 150:.0f} {x + 52:.0f},{y + 40:.0f} Z'
    if layer == "border":
        return f'<path d="{body}" fill="#FFF" stroke="#FFF" stroke-width="110" stroke-linejoin="round" {tr}/><rect x="{x - 40:.0f}" y="{y - 10:.0f}" width="80" height="60" fill="#FFF" stroke="#FFF" stroke-width="110" {tr}/>'
    return (f'<g {tr}><circle cx="{x:.0f}" cy="{y + 140:.0f}" r="95" fill="{col}" opacity=".35" filter="url(#bglow)"/>'
            f'<path d="{body}" fill="{col}" stroke="#1B2A49" stroke-width="16"/>'
            f'<path d="M{x - 25:.0f},{y + 70:.0f} Q{x - 38:.0f},{y + 130:.0f} {x - 14:.0f},{y + 175:.0f}" stroke="#FFFFFF" stroke-width="16" fill="none" stroke-linecap="round" opacity=".8"/>'
            f'<rect x="{x - 40:.0f}" y="{y - 10:.0f}" width="80" height="60" rx="10" fill="#2E7D4F" stroke="#1B2A49" stroke-width="14"/></g>')


b = []
# white die-cut border layer (one piece): wire, bulbs and words all fattened in white
b.append(f'<path d="{wire}" stroke="#FFFFFF" stroke-width="150" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
b += [bulb(x, y, c, r, "border") for x, y, c, r in bulbs]
for s, y, sz in (("TWINKLE", y1, s1), ("LIGHT", y2, s2), ("TECHNICIAN", y3, s3)):
    b += word(s, y, sz, sz * .02, "border")
# navy outline layer
b.append(f'<path d="{wire}" stroke="#1B2A49" stroke-width="22" fill="none" stroke-linecap="round"/>')
for s, y, sz in (("TWINKLE", y1, s1), ("LIGHT", y2, s2), ("TECHNICIAN", y3, s3)):
    b += word(s, y, sz, sz * .02, "outline")
# fills
b.append(f'<path d="{wire}" stroke="#2E7D4F" stroke-width="10" fill="none" stroke-linecap="round"/>')
b += [bulb(x, y, c, r, "fill") for x, y, c, r in bulbs]
for s, y, sz in (("TWINKLE", y1, s1), ("LIGHT", y2, s2), ("TECHNICIAN", y3, s3)):
    b += word(s, y, sz, sz * .02, "fill")

out = sys.argv[1] if len(sys.argv) > 1 else "sticker.png"
render(svg(W, H, "<g transform=\"translate(0,112)\">" + "\n".join(b) + "</g>", defs), out)
print("saved", out, s1, s2, s3)
