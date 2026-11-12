"""Make a preview package: a copy of the page the client can look at but can't use as their website.
Same output as the kit's preview maker page (tools/preview/preview.js).

    python3 make_preview.py page.html preview.html --business "Vito's Pizzeria" --version 2 --owner Sal --from Andre

Prints the message to send with the file."""
import argparse, re, sys
from urllib.parse import quote

def esc(s):
    return re.sub(r'[&<>"]', lambda m: {'&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;'}[m.group(0)], str(s))

def preview(html, business='your business', version='1', sender=''):
    biz, ver, frm = business or 'your business', version or '1', sender or ''
    def fix_a(m):
        tag = m.group(0)
        if not re.search(r'href\s*=\s*["\']?\s*(https?:|tel:|mailto:|sms:|//)', tag, re.I):
            return tag
        tag = re.sub(r'\shref\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)', ' href="#lk-preview"', tag, count=1, flags=re.I)
        return re.sub(r'\s(target|rel)\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)', '', tag, flags=re.I)
    out = re.sub(r'<a\b[^>]*>', fix_a, html, flags=re.I)
    out = re.sub(r'(<form\b[^>]*?)\saction\s*=\s*("[^"]*"|\'[^\']*\'|[^\s>]+)', r'\1 action="#lk-preview"', out, flags=re.I)
    out = re.sub(r'<script\b[^>]*application/ld\+json[^>]*>[\s\S]*?</script>', '', out, flags=re.I)
    head = '<meta name="robots" content="noindex, nofollow">'
    out = re.sub(r'<head\b[^>]*>', lambda m: m.group(0) + head, out, count=1, flags=re.I) if re.search(r'<head\b[^>]*>', out, re.I) else head + out
    out = re.sub(r'<title>', '<title>PREVIEW: ', out, count=1, flags=re.I)
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="360" height="220"><text x="20" y="120" transform="rotate(-24 180 110)" '
           'font-family="Arial,sans-serif" font-size="28" font-weight="700" fill="#000">PREVIEW · not for use</text></svg>')
    mark = quote(svg, safe="-_.!~*'()")
    style = ('<style>#lk-preview{position:relative;z-index:2147483001;background:#1d1b18;color:#fff;font:15px/1.45 system-ui,sans-serif;padding:14px max(16px,env(safe-area-inset-left,0px));}'
             '#lk-preview strong{color:#ffd27a}#lk-preview p{margin:4px 0 0;max-width:70ch}'
             'html::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:2147483000;opacity:.10;background:url("data:image/svg+xml,' + mark + '") repeat;}'
             '@media (prefers-color-scheme:dark){html::after{filter:invert(1)}}'
             '.lk-preview-msg{font:600 15px/1.4 system-ui,sans-serif;background:#ffd27a;color:#1d1b18;padding:10px 12px;border-radius:6px}</style>')
    poss = "'" if biz.lower().endswith('s') else "'s"
    banner = ('<div id="lk-preview" role="note" tabindex="-1"><strong>PREVIEW of ' + esc(biz) + poss + " new website, version " + esc(ver) + '.</strong>'
              '<p>Scroll through it on your phone and computer. Buttons for booking, ordering, calling and maps are switched off in the preview, and the form doesn\'t send. They all work on the live site.</p>'
              '<p>Reply to ' + (esc(frm) if frm else 'me') + ' with anything you\'d like changed. Please don\'t share or post this preview.</p></div>')
    guard = ('<script>document.addEventListener("submit",function(e){e.preventDefault();e.stopPropagation();var f=e.target,m=f.querySelector(".lk-preview-msg");'
             'if(!m){m=document.createElement("p");m.className="lk-preview-msg";m.setAttribute("role","status");f.appendChild(m)}m.textContent="Preview: on the live site this sends the message.";},true);</script>')
    out = re.sub(r'</head>', lambda m: style + '</head>', out, count=1, flags=re.I) if re.search(r'</head>', out, re.I) else style + out
    out = re.sub(r'<body\b[^>]*>', lambda m: m.group(0) + banner, out, count=1, flags=re.I) if re.search(r'<body\b[^>]*>', out, re.I) else banner + out
    if re.search(r'</body>', out, re.I):
        i = [m.start() for m in re.finditer(r'</body>', out, re.I)][-1]
        out = out[:i] + guard + out[i:]
    else:
        out += guard
    return out

def message(business, contact='', version='1', sender=''):
    return ('Hi ' + (contact or 'there') + ', here is a preview of the new ' + (business or 'your business') + ' website (version ' + (version or '1') + '), attached.\n\n'
            'To look at it: tap the attachment. It opens in your web browser (on a computer, double-click it). If it shows as code, save it and open it with Safari or Chrome.\n\n'
            'It is marked PREVIEW, and the booking, ordering, call and map buttons are switched off until the site is live. Have a look on your phone and reply with anything you would like changed.\n\n'
            'Thanks,\n' + (sender or ''))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('page'); ap.add_argument('out')
    ap.add_argument('--business', default=''); ap.add_argument('--version', default='1'); ap.add_argument('--owner', default=''); ap.add_argument('--from', dest='sender', default='')
    a = ap.parse_args()
    html = open(a.page, encoding='utf-8').read()
    if not a.business:
        t = re.search(r'<title>([^<]*)</title>', html, re.I)
        a.business = re.split(r'[|·–—-]', t.group(1))[0].strip() if t else ''
    open(a.out, 'w', encoding='utf-8').write(preview(html, a.business, a.version, a.sender))
    print(message(a.business, a.owner, a.version, a.sender))
