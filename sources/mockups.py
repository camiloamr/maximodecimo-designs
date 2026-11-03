"""Lifestyle mockups for MaximoDecimo listings (2400x1800, 4:3 = Etsy search thumbnail).

Design plan (frontend-design process, adapted to product photos)
- Brief: show each print-on-demand product in a believable cozy-winter home so a US
  holiday shopper understands size, colour and use from the search thumbnail.
- Palette (scene, never competing with the art): frost wall #D3DCDD, slate #5D6B70,
  oak #A8724A / #7E5333, pine #2E5B45, brass #C9A24A, charcoal #2A2E31.
- Type (detail card only): Fraunces for the one headline, Figtree for facts.
- Bold element: the product itself, large and centred-left; props stay small, desaturated
  and on the right third. Reviewed against generic defaults: no cream/terracotta, no
  all-caps labels, no badge clutter.

Usage: python3 mockups.py <kind> <design.png> <out.jpg> [garment_hex]
kinds: tee, sweatshirt, mug, ornament, poster, sticker, pillow, blanket
"""
import base64, io, math, random, subprocess, sys
from PIL import Image, ImageFilter

W, H = 2400, 1800
FROST, SLATE, OAK, OAK_D, PINE, BRASS, CHAR = "#D3DCDD", "#5D6B70", "#A8724A", "#7E5333", "#2E5B45", "#C9A24A", "#2A2E31"


def b64(img, maxside=1600, fmt="PNG"):
    img = img.copy()
    img.thumbnail((maxside, maxside), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, fmt)
    return "data:image/%s;base64,%s" % (fmt.lower(), base64.b64encode(buf.getvalue()).decode())


def render(svg, out, grain=True):
    png = subprocess.run(["rsvg-convert", "-w", str(W), "-h", str(H)], input=svg.encode(), capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(png)).convert("RGB")
    if grain:
        rnd = random.Random(7)
        noise = Image.effect_noise((W, H), 18).convert("L")
        im = Image.blend(im, Image.merge("RGB", (noise, noise, noise)), 0.035)
    im.save(out, quality=90)
    return out


def doc(body, defs=""):
    return f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}"><defs>{COMMON}{defs}</defs>{body}</svg>'


COMMON = f"""
<linearGradient id="wall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#E1E8E8"/><stop offset="1" stop-color="{FROST}"/></linearGradient>
<linearGradient id="oak" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#B98257"/><stop offset="1" stop-color="{OAK_D}"/></linearGradient>
<radialGradient id="vig" cx="50%" cy="45%" r="75%"><stop offset=".6" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></radialGradient>
<filter id="soft" filterUnits="userSpaceOnUse" x="-200" y="-200" width="2800" height="2200"><feGaussianBlur stdDeviation="28"/></filter>
<filter id="soft2" filterUnits="userSpaceOnUse" x="-200" y="-200" width="2800" height="2200"><feGaussianBlur stdDeviation="10"/></filter>
"""


def wood_grain(y0, y1):
    rnd = random.Random(3)
    s = []
    for i in range(70):
        y = rnd.uniform(y0, y1)
        a = rnd.uniform(.04, .12)
        s.append(f'<path d="M0,{y:.0f} C600,{y + rnd.uniform(-14, 14):.0f} 1500,{y + rnd.uniform(-14, 14):.0f} 2400,{y + rnd.uniform(-10, 10):.0f}" stroke="#5A3820" stroke-opacity="{a:.2f}" stroke-width="{rnd.uniform(2, 6):.1f}" fill="none"/>')
    return "".join(s)


def pine_sprig(x, y, ang, scale=1.0):
    rnd = random.Random(int(x * 7 + y))
    s = [f'<g transform="translate({x},{y}) rotate({ang}) scale({scale})">',
         '<path d="M0,0 Q260,-30 520,10" stroke="#5B4330" stroke-width="9" fill="none" stroke-linecap="round"/>']
    for i in range(6, 510, 7):
        t = i / 520
        yb = -30 * 4 * t * (1 - t) + 10 * t
        for sgn in (-1, 1):
            L = (70 - 30 * t) * rnd.uniform(.75, 1.15)
            a = math.radians(rnd.uniform(35, 65)) * sgn
            dx, dy = L * math.cos(a), L * math.sin(a)
            col = rnd.choice([PINE, "#3F7559", "#24493A", "#4C8467"])
            s.append(f'<path d="M{i},{yb:.0f} l{dx:.0f},{dy:.0f}" stroke="{col}" stroke-width="{rnd.uniform(4, 7):.1f}" stroke-linecap="round"/>')
    s.append("</g>")
    return "".join(s)


def gift_box(x, y, w, h, col="#B8433A", ribbon=BRASS):
    return (f'<ellipse cx="{x + w / 2}" cy="{y + h + 10}" rx="{w * .6}" ry="30" fill="#000" opacity=".25" filter="url(#soft2)"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{col}"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="url(#boxshade)"/>'
            f'<rect x="{x + w / 2 - 22}" y="{y}" width="44" height="{h}" fill="{ribbon}"/>'
            f'<rect x="{x}" y="{y + h * .35}" width="{w}" height="40" fill="{ribbon}" opacity=".95"/>'
            f'<path d="M{x + w / 2},{y} c-90,-110 -170,-20 -10,0 c-160,40 -120,-130 10,0" fill="none" stroke="{ribbon}" stroke-width="26" stroke-linecap="round"/>'
            f'<path d="M{x + w / 2},{y} c90,-110 170,-20 10,0" fill="none" stroke="{ribbon}" stroke-width="26" stroke-linecap="round"/>')


KNIT = '<pattern id="knit" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M0,18 L18,0 L36,18 M0,36 L18,18 L36,36" stroke="#fff" stroke-opacity=".10" stroke-width="6" fill="none"/></pattern>'
BOXSHADE = '<linearGradient id="boxshade" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".18"/><stop offset="1" stop-color="#000" stop-opacity=".28"/></linearGradient>'


def table_scene(top=1050):
    return (f'<rect width="{W}" height="{H}" fill="url(#wall)"/>'
            f'<rect y="{top}" width="{W}" height="{H - top}" fill="url(#oak)"/>{wood_grain(top, H)}'
            f'<rect y="{top}" width="{W}" height="14" fill="#C79468" opacity=".7"/>')


# ---------------------------------------------------------------- garments
def garment(design, color, sweat=False):
    d = Image.open(design).convert("RGBA")
    # flat lay on linen-blue throw over oak
    cx, top = 1000, 170
    if sweat:
        path = ("M820,170 C860,250 1140,250 1180,170 L1430,250 C1560,300 1620,420 1680,700 L1780,1260 L1600,1300 "
                "L1460,720 L1440,1560 L560,1560 L540,720 L400,1300 L220,1260 L320,700 C380,420 440,300 570,250 Z")
        cuffs = ('<path d="M1600,1300 L1780,1260 L1795,1340 L1615,1380 Z" fill="#000" opacity=".22"/>'
                 '<path d="M400,1300 L220,1260 L205,1340 L385,1380 Z" fill="#000" opacity=".22"/>'
                 '<rect x="560" y="1480" width="880" height="80" fill="#000" opacity=".18"/>')
        dw = 690
    else:
        path = ("M830,170 C870,250 1130,250 1170,170 L1430,250 C1520,280 1600,360 1680,560 L1520,660 L1450,560 "
                "L1440,1560 L560,1560 L550,560 L480,660 L320,560 C400,360 480,280 570,250 Z")
        cuffs = ""
        dw = 740
    body = [f'<rect width="2400" height="1800" fill="url(#oak)"/>{wood_grain(0, 1800)}{wood_grain(0, 1800)}',
            '<rect x="-40" y="-40" width="2000" height="1880" rx="30" fill="#AFBEC2" transform="rotate(-3 1000 900)"/>',
            '<rect x="-40" y="-40" width="2000" height="1880" rx="30" fill="url(#knit)" transform="rotate(-3 1000 900)"/>',
            f'<path d="{path}" fill="#000" opacity=".35" transform="translate(26,34)" filter="url(#soft)"/>',
            f'<path d="{path}" fill="{color}"/>',
            f'<clipPath id="shirt"><path d="{path}"/></clipPath>',
            '<path d="M830,170 C870,250 1130,250 1170,170" stroke="#000" stroke-opacity=".35" stroke-width="34" fill="none"/>',
            cuffs]
    dh = dw * d.height / d.width
    body.append(f'<image x="{cx - dw / 2}" y="{360}" width="{dw}" height="{dh:.0f}" xlink:href="{b64(d, 1500)}" opacity=".97"/>')
    body.append('<g clip-path="url(#shirt)"><rect width="2400" height="1800" fill="url(#fold)"/>'
                '</g>')
    body.append(pine_sprig(1720, 1560, -20, 1.1))
    body.append(pine_sprig(2380, 260, 160, .8))
    body.append(gift_box(1960, 700, 300, 300))
    body.append('<rect width="2400" height="1800" fill="url(#vig)"/>')
    defs = BOXSHADE + KNIT + '<linearGradient id="fold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".22"/><stop offset=".3" stop-color="#fff" stop-opacity=".04"/><stop offset=".7" stop-color="#fff" stop-opacity=".02"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></linearGradient>'
    return doc("".join(body), defs)


# ---------------------------------------------------------------- mug
def mug(design):
    d = Image.open(design).convert("RGB")
    front = d.crop((620, 0, 1855, d.height))  # visible front + a little wrap
    # cylinder projection: compress columns towards the edges
    fw, fh = front.size
    outw = 900
    strip = Image.new("RGB", (outw, fh))
    for x in range(outw):
        t = (x / (outw - 1)) * 2 - 1
        src = (math.asin(max(-1, min(1, t))) / (math.pi / 2) + 1) / 2 * (fw - 1)
        strip.paste(front.crop((int(src), 0, int(src) + 1, fh)), (x, 0))
    mx, my, mw, mh = 640, 520, 900, 900 * fh / outw * 1.0
    mh = 900
    strip = strip.resize((mw, int(mh * 0.86)))
    body = [table_scene(1180),
            f'<ellipse cx="{mx + mw / 2 + 60}" cy="{my + mh + 10}" rx="{mw * .66}" ry="70" fill="#000" opacity=".35" filter="url(#soft)"/>',
            # handle
            f'<path d="M{mx + mw - 10},{my + 190} C{mx + mw + 330},{my + 170} {mx + mw + 330},{my + 640} {mx + mw - 10},{my + 620}" stroke="#F4F4F2" stroke-width="95" fill="none"/>',
            f'<path d="M{mx + mw - 10},{my + 190} C{mx + mw + 330},{my + 170} {mx + mw + 330},{my + 640} {mx + mw - 10},{my + 620}" stroke="#000" stroke-opacity=".12" stroke-width="95" fill="none"/>',
            f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" rx="40" fill="#FAFAF8"/>',
            f'<image x="{mx}" y="{my + mh * .07:.0f}" width="{mw}" height="{mh * .86:.0f}" preserveAspectRatio="none" xlink:href="{b64(strip, 1400, "JPEG")}"/>',
            f'<rect x="{mx}" y="{my}" width="{mw}" height="{mh}" rx="40" fill="url(#cyl)"/>',
            f'<ellipse cx="{mx + mw / 2}" cy="{my}" rx="{mw / 2}" ry="70" fill="#F2F2EF"/>',
            f'<ellipse cx="{mx + mw / 2}" cy="{my + 8}" rx="{mw / 2 - 34}" ry="50" fill="#5A3A26"/>',
            f'<ellipse cx="{mx + mw / 2}" cy="{my + 14}" rx="{mw / 2 - 60}" ry="34" fill="#7A5236"/>']
    for dx in (-150, 30, 200):
        x0 = mx + mw / 2 + dx
        body.append(f'<path d="M{x0},{my - 40} c-60,-80 60,-140 0,-230 c-50,-80 40,-130 10,-200" stroke="#fff" stroke-opacity=".55" stroke-width="22" fill="none" stroke-linecap="round" filter="url(#soft2)"/>')
    # books stack
    for i, (c, w) in enumerate((("#2E5B45", 620), ("#5D6B70", 560), ("#8C3B34", 600))):
        y = 1260 + i * -95
        body.append(f'<rect x="{1720 - w / 2}" y="{y + 300}" width="{w}" height="90" rx="10" fill="{c}"/><rect x="{1720 - w / 2 + 14}" y="{y + 312}" width="{w - 28}" height="10" fill="#fff" opacity=".25"/>')
    body.append(pine_sprig(1880, 1660, -15, .9))
    body.append('<rect width="2400" height="1800" fill="url(#vig)"/>')
    defs = '<linearGradient id="cyl" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity=".30"/><stop offset=".18" stop-color="#000" stop-opacity=".05"/><stop offset=".32" stop-color="#fff" stop-opacity=".35"/><stop offset=".4" stop-color="#fff" stop-opacity="0"/><stop offset=".85" stop-color="#000" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".32"/></linearGradient>'
    return doc("".join(body), defs)


# ---------------------------------------------------------------- ornament
def ornament(design):
    d = Image.open(design).convert("RGB")
    cx, cy, r = 1150, 1000, 560
    rnd = random.Random(11)
    body = ['<rect width="2400" height="1800" fill="#16271F"/>']
    for _ in range(60):
        x, y, rr = rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(30, 120)
        col = rnd.choice(["#FFD27A", "#FFB45C", "#F4E3B1", "#E8F0FF"])
        body.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rr:.0f}" fill="{col}" opacity="{rnd.uniform(.08, .3):.2f}" filter="url(#soft2)"/>')
    body.append(pine_sprig(-80, 260, 8, 2.2))
    body.append(pine_sprig(1300, 120, 170, 2.0))
    body.append(pine_sprig(2500, 1400, 200, 1.6))
    body += [f'<path d="M{cx},{cy - r - 60} L{cx},40" stroke="#B8433A" stroke-width="20"/>',
             f'<circle cx="{cx + 30}" cy="{cy + 40}" r="{r}" fill="#000" opacity=".45" filter="url(#soft)"/>',
             f'<clipPath id="orn"><circle cx="{cx}" cy="{cy}" r="{r}"/></clipPath>',
             f'<image x="{cx - r}" y="{cy - r}" width="{2 * r}" height="{2 * r}" clip-path="url(#orn)" xlink:href="{b64(d, 1400, "JPEG")}"/>',
             f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glaze)"/>',
             f'<circle cx="{cx}" cy="{cy}" r="{r - 4}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="8"/>',
             f'<path d="M{cx - r * .62},{cy - r * .45} A{r * .8},{r * .8} 0 0 1 {cx - r * .1},{cy - r * .78}" stroke="#fff" stroke-opacity=".5" stroke-width="34" fill="none" stroke-linecap="round"/>',
             f'<rect x="{cx - 46}" y="{cy - r - 70}" width="92" height="84" rx="14" fill="url(#gold)"/>',
             f'<circle cx="{cx}" cy="{cy - r - 80}" r="26" fill="none" stroke="url(#gold)" stroke-width="12"/>',
             '<rect width="2400" height="1800" fill="url(#vig)"/>']
    defs = ('<radialGradient id="glaze" cx="38%" cy="32%" r="75%"><stop offset="0" stop-color="#fff" stop-opacity=".22"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".35"/></radialGradient>'
            '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7A5B1E"/><stop offset=".45" stop-color="#F2D58A"/><stop offset="1" stop-color="#8A6A25"/></linearGradient>')
    return doc("".join(body), defs)


# ---------------------------------------------------------------- poster
def poster(design):
    d = Image.open(design).convert("RGB")
    pw, ph = 720, 960
    px, py = 1200 - pw / 2 - 180, 170
    body = [f'<rect width="2400" height="1800" fill="#AEBCC0"/><rect width="2400" height="1800" fill="url(#wall)" opacity=".45"/>',
            f'<rect y="1560" width="2400" height="240" fill="url(#oak)"/>{wood_grain(1560, 1800)}',
            f'<rect x="{px + 30}" y="{py + 50}" width="{pw + 40}" height="{ph + 40}" fill="#000" opacity=".35" filter="url(#soft)"/>',
            f'<rect x="{px - 20}" y="{py - 20}" width="{pw + 40}" height="{ph + 40}" fill="{CHAR}"/>',
            f'<image x="{px}" y="{py}" width="{pw}" height="{ph}" preserveAspectRatio="none" xlink:href="{b64(d, 1300, "JPEG")}"/>',
            f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="url(#sheen)"/>',
            # console table
            f'<rect x="300" y="1300" width="1400" height="46" rx="6" fill="{OAK_D}"/>',
            '<rect x="360" y="1346" width="30" height="214" fill="#5A3820"/><rect x="1610" y="1346" width="30" height="214" fill="#5A3820"/>',
            # lamp
            '<rect x="1500" y="1080" width="16" height="220" fill="#3B3F42"/><path d="M1380,1080 L1636,1080 L1580,900 L1436,900 Z" fill="#E9E1CF"/>'
            '<ellipse cx="1508" cy="1300" rx="90" ry="16" fill="#3B3F42"/>',
            # plant
            '<path d="M1900,1560 L1870,1340 L2090,1340 L2060,1560 Z" fill="#C9C1B4"/>']
    rnd = random.Random(5)
    for i in range(9):
        a = -70 + i * 17
        body.append(f'<path d="M1980,1345 q{rnd.uniform(-40, 40):.0f},-120 {260 * math.sin(math.radians(a)):.0f},{-380 * math.cos(math.radians(a)) :.0f}" stroke="{PINE}" stroke-width="26" fill="none" stroke-linecap="round"/>')
    body.append('<rect width="2400" height="1800" fill="url(#vig)"/>')
    defs = '<linearGradient id="sheen" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".10"/><stop offset=".4" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".10"/></linearGradient>'
    return doc("".join(body), defs)


# ---------------------------------------------------------------- sticker
def sticker(design):
    d = Image.open(design).convert("RGBA")
    body = [table_scene(380),
            '<g transform="rotate(-6 1100 1000)">',
            '<rect x="420" y="380" width="1380" height="960" rx="60" fill="#000" opacity=".35" transform="translate(30,40)" filter="url(#soft)"/>',
            '<rect x="420" y="380" width="1380" height="960" rx="60" fill="url(#alu)"/>',
            '<rect x="420" y="380" width="1380" height="960" rx="60" fill="none" stroke="#fff" stroke-opacity=".4" stroke-width="6"/>']
    s = 560
    body.append(f'<image x="{1110 - s / 2 + 12}" y="{860 - s / 2 + 16}" width="{s}" height="{s}" xlink:href="{b64(shadow_of(d), 900)}" opacity=".35"/>')
    body.append(f'<image x="{1110 - s / 2}" y="{860 - s / 2}" width="{s}" height="{s}" xlink:href="{b64(d, 1200)}"/>')
    body.append('</g>')
    body.append(pine_sprig(1850, 1700, -40, 1.0))
    body.append(gift_box(1900, 900, 300, 240, "#2E5B45"))
    body.append('<rect width="2400" height="1800" fill="url(#vig)"/>')
    defs = BOXSHADE + '<linearGradient id="alu" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#D9DDE0"/><stop offset=".5" stop-color="#BFC4C8"/><stop offset="1" stop-color="#A3A9AE"/></linearGradient>'
    return doc("".join(body), defs)


def shadow_of(rgba):
    a = rgba.split()[3].filter(ImageFilter.GaussianBlur(12))
    sh = Image.new("RGBA", rgba.size, (0, 0, 0, 0))
    sh.putalpha(a)
    return sh


# ---------------------------------------------------------------- pillow
def sofa(back_col="#6E8086"):
    return (f'<rect width="2400" height="1800" fill="url(#wall)"/>'
            f'<rect y="1560" width="2400" height="240" fill="url(#oak)"/>{wood_grain(1560, 1800)}'
            f'<rect x="120" y="640" width="2160" height="620" rx="90" fill="{back_col}"/>'
            f'<rect x="120" y="640" width="2160" height="620" rx="90" fill="url(#velvet)"/>'
            f'<rect x="60" y="1120" width="2280" height="380" rx="70" fill="{back_col}"/>'
            f'<rect x="60" y="1120" width="2280" height="380" rx="70" fill="#000" opacity=".12"/>'
            f'<rect x="0" y="900" width="260" height="620" rx="80" fill="{back_col}"/><rect x="2140" y="900" width="260" height="620" rx="80" fill="{back_col}"/>'
            f'<rect x="0" y="900" width="260" height="620" rx="80" fill="#000" opacity=".08"/><rect x="2140" y="900" width="260" height="620" rx="80" fill="#000" opacity=".08"/>'
            '<rect x="180" y="1500" width="40" height="80" fill="#3B2A1C"/><rect x="2180" y="1500" width="40" height="80" fill="#3B2A1C"/>')


VELVET = '<linearGradient id="velvet" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".10"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient>'


def pillow(design):
    d = Image.open(design).convert("RGB")
    half = d.crop((0, 0, d.height, d.height))
    x, y, s = 700, 520, 820
    shape = (f"M{x + 40},{y + 30} Q{x + s / 2},{y + 70} {x + s - 40},{y + 30} Q{x + s - 70},{y + s / 2} {x + s - 40},{y + s - 30} "
             f"Q{x + s / 2},{y + s - 70} {x + 40},{y + s - 30} Q{x + 70},{y + s / 2} {x + 40},{y + 30} Z")
    body = [sofa(),
            f'<path d="{shape}" fill="#000" opacity=".35" transform="translate(30,40)" filter="url(#soft)"/>',
            f'<clipPath id="pil"><path d="{shape}"/></clipPath>',
            f'<image x="{x}" y="{y}" width="{s}" height="{s}" clip-path="url(#pil)" xlink:href="{b64(half, 1400, "JPEG")}"/>',
            f'<path d="{shape}" fill="url(#puff)"/>',
            # second plain pillow behind right
            '<g transform="rotate(8 1800 900)"><rect x="1560" y="640" width="560" height="560" rx="120" fill="#C7B79E"/><rect x="1560" y="640" width="560" height="560" rx="120" fill="url(#velvet)"/></g>',
            '<rect width="2400" height="1800" fill="url(#vig)"/>']
    body.insert(1, '')
    defs = VELVET + '<radialGradient id="puff" cx="45%" cy="40%" r="65%"><stop offset="0" stop-color="#fff" stop-opacity=".14"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".38"/></radialGradient>'
    return doc("".join(body), defs)


# ---------------------------------------------------------------- blanket
def blanket(design):
    d = Image.open(design).convert("RGB")
    bw = 1000
    bh = bw * d.height / d.width
    x, y = 600, 300
    body = [sofa("#5D6B70"),
            f'<rect x="{x + 30}" y="{y + 40}" width="{bw}" height="{min(bh, 1300)}" fill="#000" opacity=".3" filter="url(#soft)"/>',
            f'<clipPath id="bl"><rect x="{x}" y="{y}" width="{bw}" height="{min(bh, 1300)}" rx="18"/></clipPath>',
            f'<image x="{x}" y="{y}" width="{bw}" height="{bh:.0f}" clip-path="url(#bl)" xlink:href="{b64(d, 1500, "JPEG")}"/>']
    waves = "".join(f'<rect x="{x + i * 125}" y="{y}" width="125" height="1300" fill="{"#000" if i % 2 else "#fff"}" opacity="{.05 if i % 2 else .02}"/>' for i in range(8))
    body.append(f'<g clip-path="url(#bl)" filter="url(#soft2)">{waves}</g>')
    body.append(f'<rect x="{x}" y="{y}" width="{bw}" height="110" fill="url(#overfold)" clip-path="url(#bl)"/>')
    body.append('<rect width="2400" height="1800" fill="url(#vig)"/>')
    return doc("".join(body), VELVET + '<linearGradient id="overfold" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".25"/><stop offset="1" stop-color="#000" stop-opacity="0"/></linearGradient>')


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;")


def wrap(t, n):
    out, line = [], ""
    for w in t.split():
        if len(line) + len(w) + 1 > n and line:
            out.append(line); line = w
        else:
            line = (line + " " + w).strip()
    out.append(line)
    return out


def card(kind, design, color, headline, facts):
    """Detail card: the art large on the left, one headline and three plain facts."""
    d = Image.open(design)
    if kind == "pillow":
        d = d.crop((0, 0, d.height, d.height))
    if kind == "mug":
        d = d.crop((693, 0, 1782, d.height))
    panel = color if kind in ("tee", "sweatshirt") else ("#DCE3E4" if kind == "sticker" else None)
    body = ['<rect width="2400" height="1800" fill="#E6ECEC"/>',
            f'<rect x="0" y="0" width="1260" height="1800" fill="{panel or "#2A2E31"}"/>']
    iw, ih = d.size
    box = 1020
    sc = min(box / iw, box / ih)
    w, h = iw * sc, ih * sc
    if kind == "ornament":
        body.append('<clipPath id="c"><circle cx="630" cy="900" r="510"/></clipPath>')
        body.append(f'<image x="{630 - w / 2}" y="{900 - h / 2}" width="{w}" height="{h}" clip-path="url(#c)" xlink:href="{b64(d, 1400, "PNG")}"/>')
    else:
        body.append(f'<image x="{630 - w / 2}" y="{900 - h / 2}" width="{w}" height="{h}" xlink:href="{b64(d, 1400, "PNG")}"/>')
    y = 520
    for ln in wrap(headline, 20):
        body.append(f'<text x="1400" y="{y}" font-family="Fraunces" font-weight="700" font-size="104" fill="#2A2E31">{esc(ln)}</text>')
        y += 120
    y += 40
    body.append(f'<rect x="1400" y="{y}" width="140" height="10" rx="5" fill="{PINE}"/>')
    y += 120
    for f in facts:
        for ln in wrap(f, 30):
            body.append(f'<text x="1400" y="{y}" font-family="Figtree" font-size="56" fill="#3B4245">{esc(ln)}</text>')
            y += 70
        y += 34
    return doc("".join(body))


KINDS = {"tee": lambda d, c: garment(d, c or "#1F2124"), "sweatshirt": lambda d, c: garment(d, c or "#2C4A3B", True),
         "mug": lambda d, c: mug(d), "ornament": lambda d, c: ornament(d), "poster": lambda d, c: poster(d),
         "sticker": lambda d, c: sticker(d), "pillow": lambda d, c: pillow(d), "blanket": lambda d, c: blanket(d)}

if __name__ == "__main__" and sys.argv[1] == "card":
    import json
    spec = json.loads(sys.argv[2])
    render(card(spec["kind"], spec["design"], spec.get("color"), spec["headline"], spec["facts"]), spec["out"], grain=False)
    print("saved", spec["out"])
elif __name__ == "__main__":
    kind, design, out = sys.argv[1:4]
    color = sys.argv[4] if len(sys.argv) > 4 else None
    render(KINDS[kind](design, color), out)
    print("saved", out)
