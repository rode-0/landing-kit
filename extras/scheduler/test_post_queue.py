import datetime as dt, os, tempfile, sys
from zoneinfo import ZoneInfo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post_queue as pq
NY = ZoneInfo('America/New_York')
def q(d, rows):
    p = os.path.join(d, 'q.tsv')
    with open(p, 'w') as f:
        f.write('id\tdate\ttime\tplatform\tcaption\timage file name\tlink\tapproved\n')
        for r in rows: f.write('\t'.join(r) + '\n')
    return p
def at(s): return dt.datetime.fromisoformat(s).replace(tzinfo=NY)
class Ok:
    calls = 0
    def publish(self, row): Ok.calls += 1; return 'ext-' + row['id']
class Flaky:
    def publish(self, row): raise RuntimeError('timeout')
class Expired:
    def publish(self, row): raise pq.AuthError('token expired')
silent = lambda *a: None
with tempfile.TemporaryDirectory() as d:
    p = q(d, [['1','2026-12-01','09:00','ig','a','a.png','l','yes'], ['2','2026-12-01','09:00','ig','b','b.png','l','no'], ['3','2026-12-01','18:00','ig','c','c.png','l','yes']])
    st = os.path.join(d, 's.json')
    code, al = pq.run(p, 'America/New_York', st, live=True, now=at('2026-12-01T09:10'), adapter=Ok(), out=silent)
    assert code == 0 and Ok.calls == 1, (code, Ok.calls)            # only approved and due; 3 is later today
    pq.run(p, 'America/New_York', st, live=True, now=at('2026-12-01T09:20'), adapter=Ok(), out=silent)
    assert Ok.calls == 1                                              # never posted twice
    # time zone: 09:00 New York is 14:00 UTC; at 13:59 UTC nothing is due
    st2 = os.path.join(d, 's2.json')
    pq.run(p, 'America/New_York', st2, live=True, now=dt.datetime(2026,12,1,13,59,tzinfo=dt.timezone.utc), adapter=Ok(), out=silent)
    assert Ok.calls == 1
    # missed window alerts instead of posting late
    code, al = pq.run(p, 'America/New_York', os.path.join(d, 's3.json'), live=True, now=at('2026-12-01T11:00'), adapter=Ok(), out=silent)
    assert code == 2 and 'missed' in al[0] and Ok.calls == 1
    # bounded retries
    s4 = os.path.join(d, 's4.json')
    for i in range(5): code, al = pq.run(p, 'America/New_York', s4, live=True, now=at('2026-12-01T09:05'), adapter=Flaky(), out=silent)
    import json; assert json.load(open(s4))['attempts']['1'] == 3
    # expired access stops and alerts
    code, al = pq.run(p, 'America/New_York', os.path.join(d, 's5.json'), live=True, now=at('2026-12-01T09:05'), adapter=Expired(), out=silent)
    assert code == 2 and 'Access problem' in al[0]
    # pause file
    open(os.path.join(d, 'PAUSED'), 'w').close()
    code, al = pq.run(p, 'America/New_York', os.path.join(d, 's6.json'), live=True, now=at('2026-12-01T09:05'), adapter=Ok(), out=silent)
    assert code == 0 and Ok.calls == 1
    os.remove(os.path.join(d, 'PAUSED'))
    # dry run never calls an adapter
    code, al = pq.run(p, 'America/New_York', os.path.join(d, 's7.json'), live=False, now=at('2026-12-01T09:05'), adapter=None, out=silent)
    assert code == 0
print('scheduler: all tests passed')
