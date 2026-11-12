"""Tool pages' scripts parse; demos have no live outside links; paste bundle is current."""
import glob, re, subprocess, tempfile, os, sys
ok = True
for page in sorted(glob.glob('tools/*/index.html') + ['tools/index.html']):
    src = open(page, encoding='utf-8').read()
    for i, code in enumerate(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', src, re.S)):
        with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False) as fh: fh.write(code)
        r = subprocess.run(['node', '--check', fh.name], capture_output=True, text=True); os.unlink(fh.name)
        if r.returncode: print('JS error in', page, r.stderr.splitlines()[-1:]); ok = False
for demo in sorted(glob.glob('examples/demos/*.html')):
    src = open(demo, encoding='utf-8').read()
    body = src.split('<aside')[0]
    live = re.findall(r'<a\b[^>]*href="(?:https?:|tel:|mailto:|sms:)[^"]*"', body)
    if live or 'id="sample-note"' not in src or 'Photo credits' not in src or '<title>Sample:' not in src:
        print('demo not safe:', demo, live[:2]); ok = False
want = subprocess.run([sys.executable, 'tests/make_paste.py', 'plugin/skills/landing-kit/scripts/behaviors.js'], capture_output=True, text=True).stdout
if want != open('plugin/skills/landing-kit/scripts/behaviors-paste.js', encoding='utf-8').read():
    print('behaviors-paste.js is out of date: run python3 tests/make_paste.py plugin/skills/landing-kit/scripts/behaviors.js > plugin/skills/landing-kit/scripts/behaviors-paste.js'); ok = False
assert ok
print('kit: tool scripts parse, demos are safe, paste bundle current')
