# Posting queue (optional, for a technical owner)

**Most people don't need this.** The kit's recommended way to schedule posts is the platform's own free
scheduler (Meta Business Suite for Facebook and Instagram). See [sop/10](../../sop/10-market-your-business.md).

This folder is for someone technical who wants posts to go out from a script on a timer (a "cron job").
It is **dry run by default** and ships **without** any connection to a social platform.

## Who owns what
- **Technical owner** (not the beginner): runs the script on a computer or server that's always on,
  writes or installs the platform connector, keeps access tokens out of spreadsheets and chats, reads the
  alerts, and pauses it when something looks wrong.
- **Business owner**: decides which posts are approved (the `approved` column) and owns the social accounts.
- **Claude**: drafts posts and the queue. It never posts.

## How it works
1. Claude's marketing plan gives a tab-separated queue: `id, date, time, platform, caption, image file name, link, approved`.
   Save it as `queue.tsv` next to the images. Change `approved` to `yes` only for posts the business owner approved.
2. Dry run: `python3 post_queue.py queue.tsv --tz America/New_York` prints what it would post now.
3. Live: write a connector module with `publish(row)` that posts through the platform's **official API**
   and returns the post id, raising `post_queue.AuthError` when access is missing or expired. Run with
   `POST_ADAPTER=my_connector python3 post_queue.py queue.tsv --tz America/New_York --live`.
   Instagram and Facebook publishing goes through Meta's Graph API, which needs a business account linked
   to a Facebook Page, a Meta app and approved permissions. None of that is set up by this kit.
4. Timer, every 15 minutes (cron mails the output when `MAILTO` is set):
   `MAILTO=you@example.com`
   `*/15 * * * * cd /path/to/queue && python3 post_queue.py queue.tsv --tz America/New_York --live`

## Safety built in
- Only `approved=yes` rows post. Each `id` posts at most once (`post_state.json`).
- A file named `PAUSED` next to the queue stops all posting.
- A failed post retries at most 3 times (`--max-retries`), then alerts.
- Expired or missing access stops the run and alerts; nothing retries in a loop.
- A post more than 30 minutes late (`--window`) is not posted late; it alerts so a person can reschedule.
- Times are in the business's time zone (`--tz`).

Tests: `python3 test_post_queue.py`.
