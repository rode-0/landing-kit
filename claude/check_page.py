"""Landing page checker. Run: python3 check_page.py index.html
Prints PASS/FAIL/WARN lines. Fix every FAIL before showing a version."""
import sys, re, json, base64, io
from html.parser import HTMLParser

src = open(sys.argv[1], encoding="utf-8").read()
fails, warns = [], []
def fail(m): fails.append(m)
def warn(m): warns.append(m)

class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.tags = []; s.imgs = []; s.jsonld = []; s._in_ld = False; s.text = []; s.stack = []
        s.skip = 0
    def handle_starttag(s, t, a):
        a = dict(a); s.tags.append((t, a))
        if t == "img": s.imgs.append(a)
        if t == "script" and a.get("type") == "application/ld+json": s._in_ld = True; s.jsonld.append("")
        if t in ("script", "style"): s.skip += 1
    def handle_endtag(s, t):
        if t == "script": s._in_ld = False
        if t in ("script", "style"): s.skip = max(0, s.skip - 1)
    def handle_data(s, d):
        if s._in_ld: s.jsonld[-1] += d
        elif not s.skip: s.text.append(d)
p = P(); p.feed(src)
tags = {t for t, _ in p.tags}
text = " ".join(p.text)

# Basics
for m in re.finditer(r"<script(?![^>]*src)[^>]*>(.*?)</script>", src, re.S):
    if "<script" in m.group(1): fail("A script contains the text '<script'; a '</script>' inside script text ends the script early. Rephrase it")
if not re.match(r"\s*<!doctype html>", src, re.I): fail("Missing <!doctype html> at the top")
if not any(t == "html" and a.get("lang") for t, a in p.tags): fail("<html> needs a lang attribute")
if "title" not in tags: fail("Missing <title>")
if not any(t == "meta" and a.get("name") == "description" for t, a in p.tags): fail("Missing meta description")
if not any(t == "meta" and a.get("name") == "viewport" for t, a in p.tags): fail("Missing viewport meta")
if not any(t == "meta" and a.get("property") == "og:title" for t, a in p.tags): warn("No og:title")
h1 = sum(1 for t, _ in p.tags if t == "h1")
if h1 != 1: fail(f"Page should have exactly one <h1> (found {h1})")

# Size
total = len(src.encode()); code = len(re.sub(r"data:[^\"')\s]+", "", src).encode())
if total > 3_000_000: fail(f"Page is {total/1e6:.1f} MB; keep under 3 MB (resize photos)")
if code > 100_000: fail(f"Code is {code/1000:.0f} KB; keep under 100 KB")

# Structured data
for i, b in enumerate(p.jsonld):
    try: json.loads(b)
    except Exception as e: fail(f"JSON-LD block {i+1} is not valid JSON: {e}")

# Photos
for a in p.imgs:
    if "alt" not in a: fail(f"Image without alt text: {a.get('src','')[:40]}")
for m in re.finditer(r"data:image/(\w+);base64,([A-Za-z0-9+/=]+)", src):
    try:
        raw = base64.b64decode(m.group(2), validate=True)
        try:
            from PIL import Image
            Image.open(io.BytesIO(raw)).verify()
        except ImportError: pass
    except Exception as e: fail(f"Embedded image is broken ({m.group(1)}): {e}")
for a in p.imgs:
    s = a.get("src", "")
    if re.search(r"unsplash|pexels|placehold|picsum|via\.placeholder|loremflickr", s): fail(f"Stock/placeholder image: {s[:60]}")

# Hidden content / motion safety
css = " ".join(re.findall(r"<style[^>]*>(.*?)</style>", src, re.S))
for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
    sel = sel.strip()
    if re.search(r"opacity\s*:\s*0(\D|$)", body) or re.search(r"visibility\s*:\s*hidden", body):
        if sel.startswith("@") or re.fullmatch(r"(from|to|[\d.]+%)(\s*,\s*(from|to|[\d.]+%))*", sel) or re.search(r"\.js\b|js-|\[data-js|\.ready|\.reveal-on|:hover|:focus|::|\.skip|sr-only|\.visually|hp|honeypot|\.hp\b|\[hidden\]", sel): continue
        warn(f"'{sel[:50]}' starts hidden without a JS-only guard; content may never show without JavaScript")
if "IntersectionObserver" in src:
    if not re.search(r"setTimeout\([^)]*\)|setTimeout\(function", src): fail("Scroll reveals have no timeout fallback; content can stay hidden")
    reveal_css = " ".join(b for sel, b in re.findall(r"([^{}]+)\{([^{}]*)\}", css) if re.search(r"\.js\b|js-|\.rv\b|reveal", sel))
    if re.search(r"clip-path\s*:\s*inset\(\s*(100|50)%|clip-path\s*:\s*inset\([^)]*100%", reveal_css):
        warn("A fully clipped element is used in a reveal. Observe a wrapper and clip an inner element, or photos may never appear")
if re.search(r"(transition|animation)\s*:", css) and "prefers-reduced-motion" not in src:
    fail("Animations present but no prefers-reduced-motion rule")
if re.search(r"height\s*:\s*100s?vh|min-height\s*:\s*100s?vh|height\s*:\s*100dvh", css) and not re.search(r"max-height|min\(", css):
    warn("Full-screen section without a max height; it can get huge on tall screens")

# Big text squeezed by a ch width set on a parent (ch uses the parent's small font)
rules = re.findall(r"([^{}]+)\{([^{}]*)\}", css)
for sel, body in rules:
    sel = sel.strip()
    m = re.search(r"max-width\s*:\s*(\d+)ch", body)
    if not m or "font" in body: continue
    for sel2, body2 in rules:
        sel2 = sel2.strip()
        if sel2 != sel and sel2.startswith(sel + " ") and re.search(r"font(-size)?\s*:[^;]*(clamp\(|[3-9](\.\d+)?rem|\d+vw)", body2):
            fail(f"'{sel}' limits width to {m.group(1)}ch but its child '{sel2}' has big text; ch uses the parent's small font, so the big text gets squeezed. Move the max-width onto '{sel2}'")
            break

# Tabular numbers on running text (some fonts widen punctuation)
for sel, body in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
    if re.search(r"(^|[\s,])(body|html|p|:root)\s*$", sel.strip()) and re.search(r"tnum|tabular-nums", body):
        warn(f"Tabular numbers set on '{sel.strip()}' (running text). Some fonts then widen commas and periods; keep tnum to prices, tables and times")
# Missing space before an inline link inside text
for m in re.finditer(r"[A-Za-z,.:;]<a\b", src):
    ctx = src[max(0, m.start()-25):m.start()+1]
    if re.search(r"[>\s]$", ctx[:-1]) is None and not re.search(r"</\w+>$", ctx): 
        snip = re.sub(r"\s+", " ", ctx[-25:])
        warn("No space before a link: ..." + snip + "<a")
        break

# Contact
for m in re.finditer(r'name="access_key"\s+value="([^"]*)"', src):
    k = m.group(1)
    if not k or re.search(r"test|0000|your|xxxx|key_here|example|sample", k, re.I): fail(f"Contact form key looks like a placeholder ({k[:12]}...). Ask for the real Web3Forms key or remove the form")
for a in [a for t, a in p.tags if t == "a"]:
    h = a.get("href", "")
    if h in ("#", "") : warn("A link has an empty href")
    if re.search(r"example\.com|[-/_.]example\b|[-/_]sample\b|your-?(link|booking|name)", h, re.I): fail(f"Placeholder link: {h}. Ask for the real one or leave it out")

# Fictional phone numbers (555-0100 to 555-0199 are reserved for fiction)
if re.search(r"555[-.\s)]*01\d\d", text): warn("The phone number is in the 555-01xx range, which is reserved for fiction. Confirm the real number")

# Copy tells
tells = ["Welcome to", "Elevate", "Unlock", "Seamless", "seamless", "Your trusted partner", "lorem ipsum", "Lorem ipsum",
         "world-class", "cutting-edge", "state-of-the-art", "Look no further", "[Your", "TODO", "PLACEHOLDER"]
for t in tells:
    if t in text: fail(f"Generic or placeholder phrase on the page: '{t}'")
if re.search(r"[\U0001F300-\U0001FAFF☀-➿]", text): fail("Emoji in page text")

fails = list(dict.fromkeys(fails)); warns = list(dict.fromkeys(warns))
for f in fails: print("FAIL", f)
for w in warns: print("WARN", w)
print(f"{'PASS' if not fails else 'NOT READY'}: {len(fails)} fails, {len(warns)} warnings")
sys.exit(1 if fails else 0)
