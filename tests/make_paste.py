# Builds plugin/skills/landing-kit/scripts/behaviors-paste.js from behaviors.js (comments removed). Run: python3 tests/make_paste.py plugin/skills/landing-kit/scripts/behaviors.js > plugin/skills/landing-kit/scripts/behaviors-paste.js
import re,sys
src=open(sys.argv[1]).read()
src=re.sub(r'/\*.*?\*/','',src,flags=re.S)
out=[]
for line in src.split('\n'):
    s=line.strip()
    if s.startswith('//') or 'module.exports' in s: continue
    if not s:
        if out and out[-1]!='': out.append('')
        continue
    out.append(line.rstrip())
while out and out[-1]=='': out.pop()
while out and out[0]=='': out.pop(0)
print("// Landing Kit behaviors, ready to paste inside one script tag. Generated from behaviors.js.")
print('\n'.join(out))
