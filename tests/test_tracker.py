"""Tracker structure must match what Claude pastes (claude/PROMPT.md), and formulas must be intact."""
import re, openpyxl
wb = openpyxl.load_workbook('tools/tracker/tracker.xlsx')
c, d, lg = wb['Clients'], wb['Dashboard'], wb['Log']
prompt = open('claude/PROMPT.md', encoding='utf-8').read()
order = re.search(r'exactly 18\s+fields in this order, empty where unknown: (.*?)\. Example', prompt, re.S).group(1)
fields = [re.sub(r'\s*\(.*?\)', '', f).strip().lower() for f in re.split(r',\s*', ' '.join(order.split()))]
headers = [str(c.cell(1, i).value).lower() for i in range(1, 19)]
assert len(fields) == 18, fields
for f, h in zip(fields, headers):
    assert f.rstrip('?') == h.rstrip('?'), f'prompt field "{f}" vs tracker column "{h}"'
assert [c.cell(1, i).value for i in (19, 20, 21)] == ['Days until renewal (automatic)', 'Extra rounds to bill (automatic)', 'Next step (automatic)']
for r in (2, 100, 201):
    assert str(c[f'S{r}'].value).startswith('=IF(H'), r
    assert str(c[f'T{r}'].value).startswith('=IF(OR(M'), r
    assert 'CHOOSE(MATCH(L' in str(c[f'U{r}'].value), r
# Log: Claude's 6 fields map to A-F
assert [lg.cell(1, i).value for i in range(1, 7)] == ['Date', 'Client', 'Type', 'What happened', 'Amount received', 'Hours']
# Dashboard reads the right Clients columns
f = ' '.join(str(x.value) for row in d.iter_rows() for x in row if isinstance(x.value, str) and x.value.startswith('='))
assert 'COUNTIF(Clients!L2:L201' in f and 'SUMIF(Clients!L2:L201,"Care plan",Clients!K2:K201)' in f
assert 'SUM(Clients!T2:T201)' in f and 'Clients!S2:S201' in f and 'COUNTIF(Clients!J2:J201,"No")' in f
assert not re.search(r'Clients!(I|M|N|O|P|Q|R)\d', f), 'Dashboard points at a typed column it should not'
print('tracker: structure, paste order and formulas ok')
# The Clients example row in the prompt has exactly 18 fields and the stage sits in the Stage column
ex = re.search(r'Example \(18 fields[^`]*`([^`]+)`', prompt).group(1).split('<TAB>')
assert len(ex) == 18, len(ex)
assert ex[headers.index('stage')] == 'Building' and ex[headers.index('setup price')] == '600'
print('tracker: prompt example row has 18 fields in tracker order')
