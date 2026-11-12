# Time study results

Ten made-up businesses, each run through the whole flow: Version 1, three rounds of client changes (two included, one extra), and approval. Kit revision `40ed252`, Claude Opus 5.5. Method and assumptions: [README.md](README.md).

## Summary

| | Per site |
|---|---|
| **Your hands-on time** (estimate) | about **61 minutes** with three rounds (56 by email, 65 by form), plus 15 minutes the first time you connect a client's domain |
| **Waiting on Claude** (claude.ai, estimate) | about **8 to 15 minutes** across Version 1, three rounds and the final check |
| **Claude work measured in the test** | 3.7 minutes, about 120k tokens |
| **API-equivalent cost of that work** | $0.30 to $0.60 (on a Claude plan it comes out of your usage, not a bill) |
| **Each extra round** | about **10 to 13 minutes** of your time plus 1 to 3 minutes waiting |
| **Requested changes made** | 44 of 44 |
| **Final pages passing the checker** | 10 of 10 |
| **Billable third round flagged** | 10 of 10 |

**What to charge for an extra round:** at $50 an hour, an extra round costs you about $10 to $15 of time. A price of $40 to $60 covers that plus the back-and-forth with the client.

## Every run

| Business | Intake | V1 min | Rounds 1/2/3 min | Total min | Tokens | API-equivalent | Your min (est.) | Changes made | Round 3 flagged |
|---|---|---|---|---|---|---|---|---|---|
| groomer | form | 3.0 | 0.4 / 0.3 / 0.5 | 4.4 | 114k | $0.28–$0.60 | 65 | 6/6 | yes |
| bookkeeping | email | 2.7 | 0.1 / 0.2 / 0.1 | 3.4 | 109k | $0.27–$0.58 | 56 | 5/5 | yes |
| bakery | form | 2.8 | 0.5 / 0.4 / 0.2 | 4.1 | 119k | $0.30–$0.63 | 65 | 5/5 | yes |
| architect | email | 2.5 | 0.4 / 0.1 / 0.2 | 3.4 | 122k | $0.30–$0.64 | 56 | 4/4 | yes |
| physio | form | 2.5 | 0.1 / 0.1 / 0.3 | 3.2 | 126k | $0.31–$0.66 | 65 | 5/5 | yes |
| barber | form | 2.6 | 0.5 / 0.4 / 0.2 | 3.9 | 125k | $0.31–$0.66 | 65 | 4/4 | yes |
| plumber | email | 2.2 | 0.2 / 0.2 / 0.2 | 3.1 | 117k | $0.29–$0.62 | 56 | 4/4 | yes |
| yoga | form | 2.7 | 0.2 / 0.2 / 0.3 | 3.6 | 119k | $0.29–$0.63 | 65 | 3/3 | yes |
| restaurant | email | 2.8 | 0.2 / 0.1 / 0.2 | 3.5 | 112k | $0.28–$0.59 | 56 | 4/4 | yes |
| florist | form | 3.4 | 0.2 / 0.2 / 0.2 | 4.2 | 132k | $0.33–$0.70 | 65 | 4/4 | yes |

Measured minutes are the test agent's working time. It edits pages with code, so it's a lower bound for claude.ai, where Claude writes the whole page into the chat each version (about 20 KB of code, roughly 5,000 to 6,000 tokens of output per version).

## Design review of the final pages

A separate reviewer scored each final page from screenshots alone (1 to 10; for "looks AI-made", lower is better).

| Average | Designer | Looks AI-made | Customer fit |
|---|---|---|---|
| All ten | 6.6 | 5.2 | 7.4 |

| Business | Designer | Looks AI-made | Fit | Most important fix |
|---|---|---|---|---|
| groomer | 8 | 4 | 8 | Put Dana's tappable phone number in the header and hero; move the long request form below the trust and how-it-works sections |
| bookkeeping | 7 | 6 | 8 | Add a real photo of Priya to the faceless founder block and drop the landmark photo jammed under the contact CTA |
| bakery | 8 | 4 | 9 | Replace the dark, charred-looking hero loaf with a warm, well-lit shot; remove the stray tab stubs under the chalkboard |
| architect | 4 | 6 | 4 | Fix the broken project grid: about 800px of dead space under 'Chapel renovation'; lead with an old house, not a church altar |
| physio | 6 | 6 | 8 | Show Sam's face in 'Who you'll see' and replace the thin gym strip with a real treatment-room photo |
| barber | 5 | 5 | 6 | Stop the clipping: logo cut off in header and footer, razor graphic falls off the hero edge, and the tall arch and skewed razor photos leave dead space |
| plumber | 7 | 5 | 8 | Don't open an emergency page with 'Closed now'; lead with 'Emergencies answered now' and cut the stray steel-sink photo |
| yoga | 7 | 6 | 8 | Swap the paddleboard headstand hero, which scares beginners, for a calm class shot; make the tiny logo legible |
| restaurant | 7 | 5 | 8 | Make the food big: two postage-stamp photos float under the menu, and the private-room photo is a sleek modern bar, not a family room |
| florist | 7 | 5 | 7 | Fix the empty, unlabeled button in the sympathy band; replace the carnations-on-a-desk hero with a real garden-style bouquet |

Checked afterwards: the florist's blank button was a real bug (a section style overrode the button's colors); the architect's empty block was a screenshot timing artifact, not a page bug.

## What Claude found hard to understand

Every run reported where the instructions slowed it down. Grouped by how many of the ten runs hit each one, with what changed in the kit afterwards.

| Issue | Runs | What changed |
|---|---|---|
| Copying the library code into a page by hand (stripping comments, escaping braces in Python) | 9 | Added `behaviors-paste.js` (no comments) and told Claude to swap in photos with plain placeholders |
| Photo rules that overlap: crop or leave out, doubtful or contradicting, crests and ornaments, a client asking for a doubtful photo bigger | 9 | One rule: crop if that removes the problem cleanly, otherwise leave it out; ornaments on the client's own building are fine; a client's request wins, noted as unconfirmed |
| The checker can't see layout, contrast or invented facts, and had two false alarms | 6 | Fixed the false alarms; added the button-override bug and wide no-wrap text to the review list. Layout and contrast still need a human look |
| Tracker lines: unclear for Version 1; the 14-column Clients row is easy to get wrong | 5 | Version 1 now gets a Log line; a reply checklist lists what each reply needs |
| Gmail section asks for email dates the inputs didn't have | 5 | Cite date and subject when available, otherwise sender and a short quote |
| Rules spread across a long prompt; re-reading before every reply | 2 | Added a short reply checklist at the end of the prompt |
| Smaller conflicts: question headings for clinics, "cut it in half" with no measure, a newer partial timetable, what a notice's end date means, invented dropdown price bands, a domain the form never asked for | 1 each | Each now has a one-line rule, and the form asks for the domain |

## Re-run on the fix release (candidate fcf2267, 2026-11-11)

Same 10 cases, run by Claude Code agents (not a claude.ai Project), with round 3 set past the 2 included rounds so the
extra-round stop is tested. Human minutes are not measured here; the estimates above still apply.

| Check | Result |
|---|---|
| Checker on every version | 50/50 PASS (each with 1 warning: the fictional 555-01xx phone number) |
| Requested changes made | 45/45 |
| Round 3 stopped for the client's OK, with an extra-round email draft | 10/10 and 10/10 |
| Round 3 done after "go ahead" | 10/10 |
| Log lines tab-separated; Clients row has exactly 18 fields | 10/10; 10/10 |
| Outside links listed for tapping at approval | 10/10 |
| Phone screenshots requested | 10/10 |
| Claude working time per site (lower bound for claude.ai) | 4.2 minutes on average |
| Tokens per site | about 134k |

| Business | V1 | R1 | R2 | R3 stop | R3 after OK | Final | Total min | Tokens |
|---|---|---|---|---|---|---|---|---|
| groomer | 3.1 | 0.3 | 0.3 | 0.1 | 0.5 | 0.3 | 4.5 | 141k |
| bookkeeping | 3.0 | 0.4 | 0.6 | 0.1 | 0.4 | 0.3 | 4.8 | 138k |
| bakery | 2.4 | 0.5 | 0.4 | 0.1 | 0.3 | 0.3 | 4.0 | 126k |
| architect | 2.2 | 0.7 | 0.3 | 0.1 | 0.4 | 0.3 | 3.9 | 135k |
| physio | 2.4 | 0.2 | 0.3 | 0.1 | 0.3 | 0.3 | 3.6 | 135k |
| barber | 2.5 | 0.4 | 0.4 | 0.1 | 0.2 | 0.3 | 3.9 | 124k |
| plumber | 2.0 | 0.6 | 0.2 | 0.1 | 0.2 | 0.3 | 3.6 | 134k |
| yoga | 2.7 | 0.6 | 0.3 | 0.1 | 0.2 | 0.4 | 4.3 | 133k |
| restaurant | 2.7 | 0.6 | 0.2 | 0.1 | 0.2 | 0.4 | 4.1 | 138k |
| florist | 3.0 | 0.7 | 0.7 | 0.1 | 0.3 | 0.6 | 5.4 | 134k |

**Rendered check** (headless Chromium at 1366px and 375px, on the final pages): no script errors; no small tap
targets; scroll reveals all appear with normal scrolling. One defect: the barber page scrolled sideways at 375px
(a decorative drawing 18px past the edge). The prompt now tells Claude to clip off-edge graphics.

**What Claude found hard to understand** (every run reported its own list; most common first):
- Tracker fields (hours, rounds used, started, domain, Log line on the stop reply): 13 mentions
- Approval reply when no phone screenshots have arrived (hold back or not): 10 mentions
- No extra-round price on the form for email 5: 9 mentions
- Doubtful photo rules (placement, premises that can't match, brand marks): 9 mentions
- Other (half-text counts, button labels, Gmail drafts per round, same-day cutoff days): 9 mentions
- Whether a map link built from the address counts as a guessed link: 3 mentions

All of these were clarified in PROMPT.md (commit bef1b3d), and 3 cases were re-run on that version to confirm.

### Confirmation on the clarified prompt (bef1b3d, 3 cases: plumber, barber, bakery)

| Check | Result |
|---|---|
| Checker on every version | 15/15 PASS (1 warning each: the 555-01xx number) |
| Requested changes made | 12/12 |
| Round 3 stopped, email drafted with the extra-round price filled in | 3/3 |
| Round 3 done after "go ahead"; tab-separated Log lines; 18-field Clients row | 3/3; 3/3; 3/3 |
| Outside links listed; phone screenshots requested | 3/3; 3/3 |
| Barber page width at 320, 375 and 414px | fits (no sideways scroll) |

The approval and extra-round price confusion from the first re-run didn't come up again. One run first wrote a
16-field Clients row, so the prompt now shows a full 18-field example (checked by `tests/test_tracker.py`; it
was added after this confirmation run).

**Known items for the next version** (judgment calls the confirmation runs still mentioned): small maker's marks
on tools in photos; a contact-name fallback when the form has none; whether to draft client emails each round
without Gmail; where "Checks: passed" goes relative to the tracker lines; weekly content that goes out of date;
partly answered customer questions.

**Not tested here:** a real claude.ai Project, real phone screenshots, Netlify deploys, Web3Forms delivery,
Google Sheets import, and a real non-technical person. The first user rehearsal is planned (`eval/user-test`).

## Time study 3: preview package and payment-first launch (candidate dab9098, 2026-11-11)

Same 10 cases on the v1.0.3 candidate, run by Claude Code agents (not a claude.ai Project). New checks: Claude points the
user to the preview package (not the real page or a public link), and the final invoice comes before launch.

| Check | Result |
|---|---|
| Checker on every version | 50/50 PASS (1 warning each: the fictional 555-01xx number) |
| Requested changes made | 45/45 |
| Round 3 stopped for the client's OK; email drafted with the $60 price | 10/10; 10/10 |
| Round 3 done after "go ahead" | 10/10 |
| Tab-separated Log lines; 18-field Clients row | 10/10; 10/10 |
| Outside links listed; phone screenshots requested | 10/10; 10/10 |
| Preview package suggested instead of the real page | 10/10 |
| Final invoice before launch | 10/10 |
| Claude's time per site, whole run (reading, building, checking, all rounds) | 5.2 minutes on average (4.5 to 5.7) |
| Tokens per site; API-equivalent cost | about 131k; $0.33 to $0.69 |

Whole-run time replaces per-step minutes here: some agents logged a step's text in the same command as its time marks,
so per-step times understate drafting. Claude in claude.ai is slower (it writes the whole page into the chat each version).

**Your time per site (estimate, not measured):** about 38 minutes straight to live with no change rounds, about 66 with the
2 included rounds and about 80 with 3 when notes come by form (about 3 minutes less per round with Gmail connected), plus
about 15 minutes the first time you connect a client's domain. These add 3 minutes per preview package and 3 minutes for
the final invoice to the step table in eval/README.md.

**What Claude found hard:** every run hit two leftovers from the preview change (a hosting-steps line still said to send the
page file; email 7 still attached the final invoice after launch). Both are fixed, along with: where the preview maker is
and how to run it, a contact-name fallback, which email draft goes with which step, setup-paid blanks, dated content, and
re-reading copy for unsupported claims. A 3-case confirmation runs on the fixed prompt before release.

### Confirmation on the released wording (f9c8967, 3 cases: plumber, bakery, barber)

All checks passed in 3/3: checker 15/15, requested changes 12/12, extra round stopped with the $60 price and done after
"go ahead", tab-separated Log lines, 18-field Clients row, outside links listed, phone screenshots requested, preview
package suggested with the preview maker steps explained, final invoice (email 6) before launch. Whole-run Claude time
5.0 to 5.2 minutes.

**Known items for the next version** (small wording notes from these runs): when to repeat the preview steps (in full
the first time, one line after); always draft the matching client email even without Gmail; no page or Checks line in
the extra-round stop reply; add dated content with an end date by default; remind the user to fill in $[amount] in email
6 when no setup price was given; staff names don't count as the owner for the contact field.

### Plugin layout check (c121d29, 3 cases: bakery, plumber, barber)

Agents worked as Claude with the Landing Kit plugin installed: they read the skill first and opened its files only
when needed. 3/3 passed every check: checker 15/15, preview package made with `scripts/make_preview.py` (banner, no live
links), extra round stopped with the $60 price and done after "go ahead", tab-separated Log lines and an 18-field
Clients row, outside links listed, final invoice before launch, tracker file handed over. One defect found and fixed
(c8a59e8): the preview banner said "Barbers's". A local install from the repo marketplace in Claude Code showed one
skill, about 120 tokens per session and 7.3k when used. Not yet tried by a person in claude.ai.

**Known items:** whether a style request may swap a font; whether each round includes a fresh preview file; whether
"give me the tracker" means a blank copy or one pre-filled with the session's lines.
