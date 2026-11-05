"""Snow Zoomies sweatshirt (Gildan 18000, 4500x5100 transparent). Style iii minimal icon dog.
Self-contained: downloads lib.py + OFL font, renders snow-zoomies-sweatshirt.png (light ink, dark fabrics)
and snow-zoomies-sweatshirt-light.png (dark ink, light fabrics)."""
import os, subprocess, sys, math, random
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
if not os.path.exists("lib.py"):
    subprocess.run(["curl", "-sO", "https://raw.githubusercontent.com/camiloamr/maximodecimo-designs/main/sources/lib.py"], check=True)
FD = os.path.expanduser("~/.fonts/gf/")
os.makedirs(FD, exist_ok=True)
if not os.path.exists(FD + "RammettoOne-Regular.ttf"):
    subprocess.run(["curl", "-so", FD + "RammettoOne-Regular.ttf",
                    "https://raw.githubusercontent.com/google/fonts/main/ofl/rammettoone/RammettoOne-Regular.ttf"], check=True)
    subprocess.run(["fc-cache", "-f"])
sys.path.insert(0, HERE)
from lib import svg, render, text, fit_size

W, H = 4500, 5100
FAM = "Rammetto One"
PAL = {
    "dark": dict(ink="#F6F1E7", fur="#E7A962", ear="#B8743A", scarf="#E5484D", snow="#A9D3EE", eye="#2A2420"),
    "light": dict(ink="#12284A", fur="#D08A45", ear="#8E5427", scarf="#C8323A", snow="#3C86B8", eye="#12284A"),
}


def dog(p):
    """Leaping dog from a handful of rounded shapes, facing right, centred around (2250, 2560)."""
    g = []
    cx, cy = 2180, 2620
    # snow spray (bold element): a plume of snow kicked up by the back paws, arcing up and back
    rnd = random.Random(7)
    P0, P1, P2 = (cx - 950, cy + 430), (cx - 1550, cy + 260), (cx - 1180, cy - 430)
    for i in range(34):
        t = i / 33
        x = (1 - t) ** 2 * P0[0] + 2 * (1 - t) * t * P1[0] + t * t * P2[0]
        y = (1 - t) ** 2 * P0[1] + 2 * (1 - t) * t * P1[1] + t * t * P2[1]
        rad = 150 - 95 * t
        g.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad:.0f}" fill="{p["snow"]}"/>')
        if i % 3 == 0:
            ox, oy = rnd.uniform(90, 200), rnd.uniform(-160, 60)
            g.append(f'<circle cx="{x + ox:.0f}" cy="{y + oy:.0f}" r="{rad * 0.38:.0f}" fill="{p["snow"]}"/>')
    g.append(f'<path d="M{cx-1150},{cy+600} C{cx-600},{cy+540} {cx+300},{cy+560} {cx+1000},{cy+620}" fill="none" stroke="{p["snow"]}" stroke-width="70" stroke-linecap="round"/>')
    # legs (stretched gallop): rounded strokes
    leg = f'stroke="{p["fur"]}" stroke-width="170" stroke-linecap="round" fill="none"'
    g.append(f'<path d="M{cx-520},{cy+120} L{cx-1020},{cy+360}" {leg}/>')   # back leg
    g.append(f'<path d="M{cx-380},{cy+160} L{cx-860},{cy+470}" {leg}/>')
    g.append(f'<path d="M{cx+420},{cy+120} L{cx+900},{cy+330}" {leg}/>')    # front legs
    g.append(f'<path d="M{cx+300},{cy+170} L{cx+760},{cy+450}" {leg}/>')
    # tail
    g.append(f'<path d="M{cx-650},{cy-60} C{cx-900},{cy-200} {cx-950},{cy-420} {cx-880},{cy-560}" stroke="{p["fur"]}" stroke-width="150" stroke-linecap="round" fill="none"/>')
    # body
    g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="760" ry="330" fill="{p["fur"]}" transform="rotate(-6 {cx} {cy})"/>')
    # head
    hx, hy = cx + 820, cy - 420
    g.append(f'<circle cx="{hx}" cy="{hy}" r="360" fill="{p["fur"]}"/>')
    # snout
    g.append(f'<ellipse cx="{hx+330}" cy="{hy+90}" rx="250" ry="175" fill="{p["fur"]}"/>')
    # floppy ear, flying back
    g.append(f'<path d="M{hx-120},{hy-280} C{hx-520},{hy-470} {hx-760},{hy-260} {hx-560},{hy-30} C{hx-420},{hy+60} {hx-200},{hy-60} {hx-60},{hy-170} Z" fill="{p["ear"]}"/>')
    # eye + nose
    g.append(f'<circle cx="{hx+120}" cy="{hy-90}" r="62" fill="{p["eye"]}"/>')
    g.append(f'<ellipse cx="{hx+560}" cy="{hy+40}" rx="85" ry="68" fill="{p["eye"]}"/>')
    # scarf (holiday accent): collar band + two short tails fluttering back under the chin
    g.append(f'<path d="M{hx-300},{hy+150} C{hx-150},{hy+320} {hx+150},{hy+320} {hx+280},{hy+210}" stroke="{p["scarf"]}" stroke-width="150" stroke-linecap="round" fill="none"/>')
    g.append(f'<path d="M{hx-40},{hy+280} C{hx-180},{hy+420} {hx-360},{hy+380} {hx-520},{hy+470} L{hx-470},{hy+560} C{hx-300},{hy+500} {hx-120},{hy+520} {hx+40},{hy+330} Z" fill="{p["scarf"]}"/>')
    g.append(f'<path d="M{hx+40},{hy+290} C{hx-60},{hy+470} {hx-200},{hy+520} {hx-300},{hy+640} L{hx-220},{hy+700} C{hx-100},{hy+590} {hx+40},{hy+540} {hx+120},{hy+320} Z" fill="{p["scarf"]}"/>')
    return "".join(g)


def build(mode):
    p = PAL[mode]
    b = []
    s1 = fit_size("Snow", FAM, 2300, 980)
    b.append(text(2250, 1480, "Snow", FAM, s1, p["ink"]))
    b.append(dog(p))
    s2 = fit_size("Zoomies", FAM, 3400, 900)
    b.append(text(2250, 4280, "Zoomies", FAM, s2, p["ink"]))
    return svg(W, H, "".join(b))


if __name__ == "__main__":
    render(build("dark"), os.path.join(HERE, "snow-zoomies-sweatshirt.png"))
    render(build("light"), os.path.join(HERE, "snow-zoomies-sweatshirt-light.png"))
    print("ok")
