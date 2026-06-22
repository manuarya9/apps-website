#!/usr/bin/env python3
"""Generate the ShowPoint Open Graph card (1200x630) using brand colors/fonts."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
BG = (13, 13, 16)          # --bg #0d0d10
TEXT = (240, 238, 232)     # --text #f0eee8
MUTED = (136, 136, 147)    # --muted #888893
ACCENT = (232, 168, 74)    # --accent #e8a84a

ICON = "/home/user/cursoroverlay/CursorOverlay/Assets.xcassets/AppIcon.appiconset/icon_1024.png"
OUT = "/home/user/apps-website/showpoint/og.png"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

img = Image.new("RGB", (W, H), BG)

# Subtle amber radial glow behind the icon (depth, matches --accent-glow).
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)
gd.ellipse([60, 150, 520, 610], fill=(232, 168, 74, 38))
glow = glow.filter(ImageFilter.GaussianBlur(90))
img.paste(Image.alpha_composite(img.convert("RGBA"), glow).convert("RGB"), (0, 0))

# App icon, crisp downscale from 1024, with a soft drop shadow.
icon_px = 300
icon = Image.open(ICON).convert("RGBA").resize((icon_px, icon_px), Image.LANCZOS)
ix, iy = 96, (H - icon_px) // 2
shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
shadow.paste((0, 0, 0, 150), (ix + 8, iy + 18, ix + icon_px + 8, iy + icon_px + 18))
shadow = shadow.filter(ImageFilter.GaussianBlur(28))
base = Image.alpha_composite(img.convert("RGBA"), shadow)
base.paste(icon, (ix, iy), icon)
img = base.convert("RGB")

draw = ImageDraw.Draw(img)
tx = ix + icon_px + 72  # text column start

f_title = ImageFont.truetype(SERIF, 88)
f_tag = ImageFont.truetype(SANS, 38)
f_meta = ImageFont.truetype(MONO, 27)

draw.text((tx, 178), "ShowPoint", font=f_title, fill=TEXT)

# Tagline, wrapped to the available width.
tag = "Your cursor, finally\nimpossible to miss."
draw.multiline_text((tx, 292), tag, font=f_tag, fill=TEXT, spacing=12)

# Accent meta line + domain.
draw.text((tx, 430), "Cursor Highlighter for Mac", font=f_meta, fill=ACCENT)
draw.text((tx, 470), "Free  ·  $4.99 Lifetime  ·  vedynapps.com", font=f_meta, fill=MUTED)

img.save(OUT, "PNG", optimize=True)
print("wrote", OUT, img.size)
