# Landing Kit

Run a small website business with Claude. No coding.

You find local businesses, collect their details, logo and photos, Claude designs a professional one-page site with you, and you put it online by dragging one file onto a website. Then you keep it updated for a monthly fee.

![Five example sites made with this kit](examples/overview.png)

*Example sites for made-up businesses. Photo credits are in [examples/CREDITS.md](examples/CREDITS.md).*

---

## How the business runs

Follow these steps in order. Each one is a short page.

1. [Set up](sop/01-set-up.md): Claude, your Project, Gmail, Netlify, your tools and dashboard (once, about an hour)
2. [Find clients](sop/02-find-clients.md): who to approach and what to say
3. [Sell and sign](sop/03-sell-and-sign.md): prices, the first meeting, the agreement, the deposit
4. [Collect the details](sop/04-collect-details.md): answers, logo and photos
5. [Build and review](sop/05-build-and-review.md): Version 1 and rounds of changes with the client
6. [Launch](sop/06-launch.md): put it online and connect their domain
7. [Bill and track](sop/07-bill-and-track.md): invoices, monthly billing, your dashboard
8. [Care and updates](sop/08-care-and-updates.md): monthly changes and renewals
9. [Back up](sop/09-back-up.md): keeping every client's work safe

---

## What it costs, and what to charge

- **You pay:** a Claude plan (Pro is $20 a month; Max is $100 or $200 for much more use) and Netlify hosting for all your clients (start free; Personal is $9 a month).
- **The client pays you:** a one-time price for the site (including 2 rounds of changes), a set price for each extra round, and a monthly care price that covers hosting, the contact form and small updates.
- **The client pays directly:** only their domain name (usually $10 to $20 a year), bought in their name so they own it.
- **How many sites your Claude plan covers** isn't a fixed number, because Claude's limits reset every few hours and weekly. See the [time study](eval/README.md) for what a typical site takes.

Use the pricing page in `tools/pricing` to set your numbers.

*Prices as of November 2026. Check claude.com/pricing and netlify.com/pricing.*

---

## What's in the kit

| Folder | What it's for |
|---|---|
| `sop/` | The step-by-step guide to running the business. |
| `claude/` | Everything that goes into your Claude Project: the instructions Claude follows, a page checker, and design notes. You don't need to read these. |
| `tools/intake/` | The question page you send clients. |
| `tools/pricing/` | Works out your prices and writes a quote. |
| `tools/invoice/` | Makes invoices you can save as a PDF. |
| `tools/tracker/` | Your dashboard spreadsheet: clients, stages, money, rounds, renewals. |
| `templates/` | Messages to find clients, emails for each stage, and a simple client agreement. |
| `eval/` | The time study: how long a site takes and what it costs. |
| `examples/` | Pictures of sites made with this kit. |

## If something goes wrong

- **"Copy my answers" doesn't work for the client.** They probably opened the link inside Instagram or Facebook. Ask them to open it in Safari or Chrome.
- **The contact form doesn't send.** Check the Web3Forms key is the real one from the email. Forms only send from the live Netlify site, not the Claude preview.
- **Photos or the logo don't show.** Tell Claude "the photos aren't showing" and it will fix it.
- **Something looks wrong on a phone.** Attach a screenshot in the chat and say what's wrong.
