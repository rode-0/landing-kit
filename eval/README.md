# Time study

How long a website takes and what it costs, measured on ten example businesses.

**Results:** [results.md](results.md)

## How it was run
- **Dataset** (`dataset/`): ten made-up businesses across trades (groomer, bookkeeper, bakery, architect, physical therapy, barber, plumber, yoga studio, restaurant, florist). Four came in by email (to simulate Gmail), six through the question page. Each has three rounds of client changes. Photos are free-licence stand-ins, some deliberately wrong for the business; three have a client logo.
- **Each run:** a fresh copy of the kit from GitHub, followed as written: Version 1, then the three rounds, then "approved". Each step was timed. The runs had no browser, like Claude in claude.ai.
- **Prompt feedback:** each run also reports what was hard to understand in the kit's instructions, as
  structured entries: the rule quoted, the kind of problem (unclear, conflicting, missing, too long), what it
  did instead, minutes lost, and a suggested fix. These are summarised in [results.md](results.md) and drive
  the next changes to `claude/PROMPT.md`.
- **Scored:** the page checker on every version, whether every requested change was made, whether round 3 was flagged as billable, and whether tracker lines were given. A separate design review scored the final pages.

## Assumptions for your time
These are estimates, not measurements. Adjust them in `tools/pricing` to match how you work.

| Step | Minutes |
|---|---|
| Collect the answers, logo and photos, start the chat | 6 |
| Review Version 1 (on phone and computer) | 8 |
| Pass on one round of client notes | 6 by form, 3 with Gmail connected |
| Review one new version | 5 |
| Launch: download, Netlify, test the form | 12 |
| Invoice and tracker | 6 |
| Connect a client's domain (first time) | 15 |

## Cost
Opus 5.5 is priced at $4 per million input tokens and $20 per million output tokens (cache reads $0.20). The test reports one combined token number, so the cost is shown as a range: the low end assumes most input is read from cache, the high end assumes none is. On a Claude Pro or Max plan, this work uses your plan's limits rather than costing money directly.

## Summary file each run writes
```json
{"case": "...", "checker": {"v1": "...", "final": "..."},
 "requests": [{"round": 1, "asked": 2, "done": 2, "waiting": 0}],
 "round3_flagged_billable": true, "tracker_lines_given": true,
 "photos_used": 3, "photos_left_out": 1,
 "prompt_feedback": [{"rule": "quoted text from PROMPT.md", "kind": "unclear|conflict|missing|too long",
   "did_instead": "...", "minutes_lost": 2, "fix": "suggested wording"}],
 "notes": "..."}
```

## Run it again
Maintainers: see `MAINTAINING.md`. Re-run the study after changing `claude/PROMPT.md` or the library, and compare against `results.json`.
