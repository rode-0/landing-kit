"""Posting queue runner for a technical owner (optional; the kit's default is the platform's own scheduler).

Reads an approved post queue (tab-separated, as Claude's marketing plan gives it) and publishes posts that
are due. Dry run by default: it prints what it would post and changes nothing but its state file.

    python3 post_queue.py queue.tsv --tz America/New_York            # dry run
    python3 post_queue.py queue.tsv --tz America/New_York --live     # needs an adapter (see README)

Safety: only rows with approved=yes; each id is posted at most once (state file); a PAUSED file next to
the queue stops everything; failed posts retry at most --max-retries times; expired access stops and
alerts; posts more than --window minutes late are not posted late, they alert. Exit code 0 = fine,
2 = something needs a person (cron mails the output when MAILTO is set).
"""
import argparse, csv, datetime as dt, importlib, json, os, sys
from zoneinfo import ZoneInfo

class AuthError(Exception): """Access token missing, expired or revoked. Raised by an adapter."""

def load_queue(path):
    with open(path, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    need = {'id', 'date', 'time', 'platform', 'caption', 'image file name', 'link', 'approved'}
    missing = need - set(rows[0].keys() if rows else need)
    if missing: raise SystemExit(f"queue is missing columns: {', '.join(sorted(missing))}")
    return rows

def run(queue_path, tz, state_path, live=False, now=None, max_retries=3, window=30, adapter=None, out=print):
    alerts = []
    if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(queue_path)), 'PAUSED')):
        out('Paused (PAUSED file present). Nothing posted.'); return 0, alerts
    zone = ZoneInfo(tz)
    now = now or dt.datetime.now(zone)
    state = json.load(open(state_path)) if os.path.exists(state_path) else {'posted': {}, 'attempts': {}, 'failed': {}}
    for row in load_queue(queue_path):
        pid = row['id'].strip()
        if row['approved'].strip().lower() != 'yes' or pid in state['posted'] or pid in state['failed']: continue
        when = dt.datetime.fromisoformat(f"{row['date'].strip()}T{row['time'].strip()}").replace(tzinfo=zone)
        if when > now: continue
        if now - when > dt.timedelta(minutes=window):
            state['failed'][pid] = 'missed'; alerts.append(f"Post {pid} was due {when:%b %d %H:%M} and was missed; not posting late. Reschedule it.")
            continue
        if not live:
            out(f"DRY RUN would post {pid} to {row['platform']}: {row['caption'][:60]}"); state['posted'][pid] = 'dry-run'
            continue
        try:
            ext = adapter.publish(row); state['posted'][pid] = str(ext); out(f"Posted {pid} ({ext})")
        except AuthError as e:
            alerts.append(f"Access problem posting {pid}: {e}. Stopped; reconnect the account, then run again."); break
        except Exception as e:  # network or platform error: bounded retries
            n = state['attempts'].get(pid, 0) + 1; state['attempts'][pid] = n
            if n >= max_retries: state['failed'][pid] = str(e)[:200]; alerts.append(f"Post {pid} failed {n} times ({e}); giving up on it.")
    json.dump(state, open(state_path, 'w'), indent=1)
    for a in alerts: out('ALERT: ' + a)
    return (2 if alerts else 0), alerts

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('queue'); ap.add_argument('--tz', required=True)
    ap.add_argument('--state', default='post_state.json'); ap.add_argument('--live', action='store_true')
    ap.add_argument('--max-retries', type=int, default=3); ap.add_argument('--window', type=int, default=30)
    a = ap.parse_args(); adapter = None
    if a.live:
        name = os.environ.get('POST_ADAPTER')
        if not name: sys.exit('Live mode needs POST_ADAPTER=<module with publish(row)>. See README. Nothing posted.')
        adapter = importlib.import_module(name)
    code, _ = run(a.queue, a.tz, a.state, live=a.live, max_retries=a.max_retries, window=a.window, adapter=adapter)
    sys.exit(code)
