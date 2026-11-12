"""Photo and logo helpers for building a page (Python + Pillow).

    import sys; sys.path.insert(0, "/path/to/the/folder/with/photo_tools.py")  # needed with python -I
    from photo_tools import data_uri, crop_ratio, remove_white_bg
    hero = data_uri(crop_ratio("photo1.jpg", 4, 5), width=1600)        # JPEG data URI, quality 75
    logo = data_uri(remove_white_bg("logo.jpg"), fmt="PNG")              # transparent PNG data URI
    html = template.replace("{{HERO}}", hero).replace("{{LOGO}}", logo)  # plain replacement, no f-strings
"""
import base64, io
from PIL import Image, ImageOps

def load(path_or_img):
    img = path_or_img if isinstance(path_or_img, Image.Image) else Image.open(path_or_img)
    return ImageOps.exif_transpose(img)

def crop_ratio(path_or_img, w, h, focus=(0.5, 0.5)):
    """Crop to a w:h shape around a focus point (0..1 from left/top). Keep the subject whole: check the result."""
    img = load(path_or_img); W, H = img.size; target = w / h
    if W / H > target:
        nw = int(H * target); x = int((W - nw) * focus[0]); return img.crop((x, 0, x + nw, H))
    nh = int(W / target); y = int((H - nh) * focus[1]); return img.crop((0, y, W, y + nh))

def remove_white_bg(path_or_img, threshold=245, trim=True):
    """Make near-white pixels transparent (for logos supplied as JPG on white) and trim empty edges.
    Never changes the logo's own colors or shapes."""
    img = load(path_or_img).convert("RGBA")
    px = [(r, g, b, 0) if r >= threshold and g >= threshold and b >= threshold else (r, g, b, a) for r, g, b, a in img.getdata()]
    img.putdata(px)
    if trim:
        box = img.getbbox()
        if box: img = img.crop(box)
    return img

def data_uri(path_or_img, width=1600, fmt="JPEG", quality=75):
    """Resize to at most `width` pixels wide and return a data: URI."""
    img = load(path_or_img)
    if img.width > width:
        img = img.resize((width, round(img.height * width / img.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if fmt.upper() == "JPEG":
        img.convert("RGB").save(buf, "JPEG", quality=quality, optimize=True, progressive=True); mime = "image/jpeg"
    else:
        img.save(buf, "PNG", optimize=True); mime = "image/png"
    return "data:%s;base64,%s" % (mime, base64.b64encode(buf.getvalue()).decode())
