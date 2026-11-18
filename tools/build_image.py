#!/usr/bin/env python3
"""Build the 1024x1024 front-page poster for news-image-20261117.

Real world news of Tuesday 17 November 2026, from BBC / AP / Al Jazeera /
Reuters / Spaceflight Now (via Level Headlines daily brief + NPR + ASAS Press).
Flat-vector illustrations drawn with PIL primitives; all text is real text.
Deterministic: fixed coordinates, no random, no clock, no network.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (251, 247, 236)
NAVY = (14, 42, 71)
INK = (20, 20, 20)
GRAY = (90, 90, 90)
RED = (176, 30, 40)
GOLD = (232, 184, 75)
LIGHT = (159, 179, 200)

F = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = F + "DejaVuSerif-Bold.ttf"
SERIF = F + "DejaVuSerif.ttf"
SANS_B = F + "DejaVuSans-Bold.ttf"
SANS = F + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w, draw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def center(draw, y, text, fnt, fill, x0=0, x1=W):
    w = draw.textlength(text, font=fnt)
    draw.text(((x0 + x1 - w) / 2, y), text, font=fnt, fill=fill)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 150], fill=NAVY)
center(d, 22, "TUESDAY, 17 NOVEMBER 2026", font(SERIF_B, 46), (255, 255, 255))
d.line([32, 86, 992, 86], fill=GOLD, width=3)
center(d, 100, "THE WORLD IN ONE IMAGE", font(SANS_B, 30), GOLD)

# ---------- lead story: Kerch Bridge ----------
d.text((32, 166), "UKRAINE  •  CRIMEA", font=font(SANS_B, 24), fill=RED)
d.text((32, 198), "KERCH BRIDGE COLLAPSES", font=font(SERIF_B, 54), fill=INK)
d.text((32, 258), "AFTER UKRAINIAN STRIKE", font=font(SERIF_B, 54), fill=INK)
d.text((32, 326), "Road span falls into the strait; Kremlin vows to rebuild it.",
       font=font(SANS, 23), fill=GRAY)

# bridge illustration (x 32..992, y 392..542)
bx0, by0, bx1, by1 = 32, 392, 992, 542
d.rectangle([bx0, by0, bx1, 472], fill=(207, 227, 238))   # sky
d.rectangle([bx0, 472, bx1, by1], fill=(46, 110, 142))    # sea
# towers
for tx in (250, 700):
    d.rectangle([tx, 408, tx + 20, 478], fill=(58, 58, 58))
    d.rectangle([tx - 14, 420, tx + 34, 430], fill=(58, 58, 58))
# deck: left span intact, middle span broken down into the water, right span intact
d.rectangle([40, 440, 560, 452], fill=(51, 51, 51))
d.polygon([(560, 440), (600, 500), (614, 498), (576, 438)], fill=(51, 51, 51))
d.rectangle([648, 440, 984, 452], fill=(51, 51, 51))
# explosion + smoke above the gap
d.polygon([(596, 408), (606, 428), (626, 428), (610, 440), (616, 458),
           (596, 446), (576, 458), (582, 440), (566, 428), (586, 428)],
          fill=(232, 122, 30))
for cx, cy, r, col in [(560, 408, 20, (140, 140, 140)), (596, 388, 24, (160, 160, 160)),
                       (636, 410, 18, (140, 140, 140)), (612, 372, 16, (170, 170, 170))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=col)
# waves
for wx in (80, 220, 380, 700, 850):
    d.arc([wx, 505, wx + 60, 535], 180, 360, fill=(255, 255, 255), width=3)
    d.arc([wx + 90, 518, wx + 140, 542], 180, 360, fill=(255, 255, 255), width=3)

# divider
d.line([32, 566, 992, 566], fill=(180, 175, 160), width=2)

# ---------- three panels ----------
panels = [
    dict(x0=32, x1=344, kicker="ASEAN SUMMIT",
         head="TRUMP LANDS IN MANILA",
         cap="Trade pact with Thailand signed; Xi\u2013Putin talks next in China.",
         kind="manila"),
    dict(x0=356, x1=668, kicker="GULF TENSIONS",
         head="TANKERS HIT BY MINES",
         cap="Two tankers ablaze; third US carrier arrives in the region.",
         kind="hormuz"),
    dict(x0=680, x1=992, kicker="SPACE",
         head="VULCAN ROCKET FAILS",
         cap="40 Amazon internet satellites lost in flight anomaly.",
         kind="vulcan"),
]

for p in panels:
    x0, x1 = p["x0"], p["x1"]
    ix0, iy0, ix1, iy1 = x0, 582, x1, 702
    kind = p["kind"]
    if kind == "manila":
        d.rectangle([ix0, iy0, ix1, iy1], fill=(247, 215, 116))  # sunset sky
        d.ellipse([ix1 - 78, iy0 + 14, ix1 - 34, iy0 + 58], fill=(232, 134, 46))  # sun
        # skyline
        for bx, bw, bh in [(0, 42, 52), (48, 30, 74), (84, 46, 44), (136, 34, 66),
                           (176, 40, 48), (222, 30, 80), (258, 54, 58)]:
            d.rectangle([ix0 + bx, iy1 - bh, ix0 + bx + bw, iy1], fill=(30, 52, 84))
        # windows
        for wx, wy in [(10, 96), (56, 66), (96, 104), (146, 74), (186, 100), (232, 58), (272, 88)]:
            d.rectangle([ix0 + wx, iy0 + wy, ix0 + wx + 6, iy0 + wy + 8], fill=GOLD)
        # plane + contrail
        d.line([ix0 + 8, iy0 + 22, ix0 + 70, iy0 + 30], fill=(255, 255, 255), width=2)
        d.polygon([(ix0 + 74, iy0 + 24), (ix0 + 96, iy0 + 30), (ix0 + 74, iy0 + 36)],
                  fill=(255, 255, 255))
    elif kind == "hormuz":
        d.rectangle([ix0, iy0, ix1, iy1], fill=(217, 232, 240))  # sky
        d.rectangle([ix0, iy0 + 62, ix1, iy1], fill=(31, 92, 122))  # sea
        # tanker hull + containers
        d.rectangle([ix0 + 24, iy0 + 66, ix0 + 250, iy0 + 100], fill=(122, 42, 32))
        d.polygon([(ix0 + 250, iy0 + 66), (ix0 + 282, iy0 + 82), (ix0 + 250, iy0 + 100)],
                  fill=(122, 42, 32))
        for cx, col in [(40, (232, 184, 75)), (72, (70, 130, 90)), (104, (200, 90, 60)),
                        (136, (90, 110, 160))]:
            d.rectangle([ix0 + cx, iy0 + 46, ix0 + cx + 28, iy0 + 66], fill=col)
        # flame + smoke
        d.polygon([(ix0 + 176, iy0 + 46), (ix0 + 196, iy0 + 8), (ix0 + 216, iy0 + 46)],
                  fill=(232, 122, 30))
        d.polygon([(ix0 + 186, iy0 + 46), (ix0 + 196, iy0 + 24), (ix0 + 206, iy0 + 46)],
                  fill=(247, 201, 72))
        for cx, cy, r in [(196, 12, 12), (214, 22, 9)]:
            d.ellipse([ix0 + cx - r, iy0 + cy - r, ix0 + cx + r, iy0 + cy + r],
                      fill=(150, 150, 150))
        # naval mine in the water
        mx, my = ix0 + 268, iy0 + 100
        d.ellipse([mx - 8, my - 8, mx + 8, my + 8], fill=(20, 20, 20))
        for ang in (0, 45, 90, 135, 180, 225, 270, 315):
            import math
            a = math.radians(ang)
            d.line([mx + 8 * math.cos(a), my + 8 * math.sin(a),
                    mx + 15 * math.cos(a), my + 15 * math.sin(a)],
                   fill=(20, 20, 20), width=2)
    else:  # vulcan
        d.rectangle([ix0, iy0, ix1, iy1], fill=(20, 31, 51))  # night sky
        for sx, sy in [(16, 14), (60, 40), (110, 10), (160, 34), (210, 12),
                       (260, 44), (292, 20), (40, 78), (280, 84)]:
            d.ellipse([ix0 + sx, iy0 + sy, ix0 + sx + 3, iy0 + sy + 3], fill=(255, 255, 255))
        # rocket, tilted up-right
        d.polygon([(ix0 + 120, iy0 + 88), (ix0 + 150, iy0 + 30), (ix0 + 168, iy0 + 44),
                   (ix0 + 150, iy0 + 96)], fill=(240, 240, 240))
        d.polygon([(ix0 + 150, iy0 + 30), (ix0 + 168, iy0 + 44), (ix0 + 162, iy0 + 22)],
                  fill=(176, 30, 40))
        d.polygon([(ix0 + 120, iy0 + 88), (ix0 + 150, iy0 + 96), (ix0 + 138, iy0 + 108)],
                  fill=(176, 30, 40))
        d.polygon([(ix0 + 128, iy0 + 94), (ix0 + 142, iy0 + 100), (ix0 + 122, iy0 + 118)],
                  fill=(232, 122, 30))
        # debris
        for dx, dy, col in [(210, 40, (232, 122, 30)), (236, 66, (200, 200, 200)),
                            (196, 84, (232, 122, 30)), (258, 92, (200, 200, 200)),
                            (224, 108, (232, 184, 75))]:
            d.ellipse([ix0 + dx, iy0 + dy, ix0 + dx + 6, iy0 + dy + 6], fill=col)

    y = 712
    d.text((x0, y), p["kicker"], font=font(SANS_B, 19), fill=RED)
    y += 30
    for ln in wrap(p["head"], font(SERIF_B, 28), x1 - x0, d):
        d.text((x0, y), ln, font=font(SERIF_B, 28), fill=INK)
        y += 33
    y += 4
    for ln in wrap(p["cap"], font(SANS, 19), x1 - x0, d):
        d.text((x0, y), ln, font=font(SANS, 19), fill=GRAY)
        y += 24

# column dividers
d.line([350, 582, 350, 856], fill=(200, 195, 180), width=2)
d.line([674, 582, 674, 856], fill=(200, 195, 180), width=2)

# ---------- ticker ----------
d.rectangle([0, 872, W, H], fill=NAVY)
d.text((32, 886), "ALSO TODAY", font=font(SANS_B, 22), fill=GOLD)
ticker = [
    "JPMorgan blames software bug for Monday banking outage",
    "West urges Israel to open Gaza crossings for aid",
    "Estonia to shut Russia border crossings on 1 December",
]
y = 916
for t in ticker:
    d.text((32, y), "\u2022  " + t, font=font(SANS, 21), fill=(255, 255, 255))
    y += 28
d.text((32, 1000), "Sources: BBC \u2022 AP \u2022 Al Jazeera \u2022 Reuters \u2022 Spaceflight Now",
       font=font(SANS, 15), fill=LIGHT)

img.save("assets/entry.png", optimize=True)
print("saved assets/entry.png")
