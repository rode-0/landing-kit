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
