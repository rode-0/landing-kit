# Rehearsal: a cold start with a non-technical tester

**Purpose:** see whether someone new can go from the kit to a live practice site, and where they get stuck.
This is a rehearsal, not a sale: no real customers, payments or social posts. Paid-client results come later.

**People:** the tester (does everything), and an observer (plays the client, keeps the logs, helps only
when the tester is stuck and asks, or after 5 minutes stuck on one step).

**Bring:** a laptop, the tester's phone, a Claude paid plan for the tester, and their own email.
**Safe test destinations:** the sample client in `sample-client.md`; a fictional 555-01xx phone number
(never dial it); the tester's own email for form messages. No booking links: the sample client books by text.

## Script

Write the clock time at the start and end of each step in the time log. Count only the tester's time.

| # | Step | The tester does | Expected outcome |
|---|---|---|---|
| 1 | Setup, Level 1 | Opens the setup page (https://rode-0.github.io/landing-kit/tools/setup/), follows Level 1 (adds the Landing Kit plugin in Claude, Netlify free account, prices, agreement) | Project has the kit files and the instruction; pricing page filled in; Level 2 unlocks on the setup page |
| 2 | Setup, Level 2 | Gets the tracker from Claude, imports it into Google Sheets (or Excel); saves the links | Tracker opens with the example row and Dashboard numbers; tool pages load at /intake/, /pricing/, /invoice/, /setup/ |
| 3 | Discovery and quote | Reads the sample client's answers, notes what the client already has, sends a quote from the pricing page | Quote shows the price, included rounds, extra-round price and the care update cap |
| 4 | Deposit (simulated) | Makes a deposit invoice in the invoice maker and saves it as PDF; logs "Payment" in the tracker | PDF made; the Log row shows in "Money received this month" |
| 5 | Build | New chat, "Use the landing kit to build a website for Blue Ridge Mobile Grooming": pastes the answers, attaches the 4 photos | Version 1 with a customer brief, "Checks: passed" or what wasn't checked, a request for phone screenshots, a Log line in a box |
| 6 | Preview and phone check | Downloads the version, makes a preview package in tools/preview, opens the preview on their phone, sends 3 screenshots to Claude | Claude reviews the screenshots and fixes anything it sees |
| 7 | Rounds | Sends round notes 1 and 2, then 3 | Rounds 1-2 done with "What changed"; round 3 stops with an extra-round email draft; after "the client said yes" it's done |
| 8 | Tracker paste | Pastes each Log line, and the Clients row after approval | Every value lands in its named column; grey columns fill in; Next step shows something sensible |
| 9 | Launch (safe) | Says "approved", taps each link on Claude's list, drags the page folder onto Netlify Drop, makes a Web3Forms key with their own email, gets the page updated with it, sends a test message from the live site | Live netlify.app link opens on the phone; the test message arrives in their inbox |
| 10 | Own site | New chat: "Build my own site" with screenshots of the practice site | Portfolio page with the example labelled "Sample design", packages, phone and email, a short enquiry form |
| 11 | Marketing (rehearsal) | New chat: "Make my marketing plan" for dog groomers | One-line positioning, 3 themes, a post design, a month of posts with captions, a queue with approved = no. **Don't post or schedule anything** |
| 12 | Care update and backup | Sends the care update to Claude, re-uploads the new page on the site's Deploys page, saves the final page in a backup folder named by date, logs the update | The live site shows Monday hours; backup folder has the dated file |
| 13 | What next | On the setup page, presses "Copy question for Claude", pastes it into a Claude chat with the Dashboard | One clear next step with how to start it |

Check first in step 2: **whether the tracker imports cleanly into Google Sheets.** It was tested only in
LibreOffice before release. Note any formula errors (#NAME?, #VALUE!) or missing colors.

## Time log

| # | Start | End | Minutes | Notes |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |
| 6 | | | | |
| 7 | | | | |
| 8 | | | | |
| 9 | | | | |
| 10 | | | | |
| 11 | | | | |
| 12 | | | | |
| 13 | | | | |

## Help log (every time the tester asks, or the observer steps in)

| Time | Step | What they were trying to do | What they asked or where they got stuck | Help given | Minutes lost |
|---|---|---|---|---|---|
| | | | | | |

## Defect log

| # | Step | What happened | What should have happened | Severity (blocks / slows / cosmetic) | Screenshot |
|---|---|---|---|---|---|
| | | | | | |

## Pass or fail

Pass if steps 1-9 are done with no hands-on help (questions answered are fine), the test message arrives,
and the tracker numbers are right. Record total tester minutes for steps 1-2 (setup) and 3-9 (one client).
