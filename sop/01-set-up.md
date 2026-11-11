# 1. Set up

Start small. **Level 1** is everything you need to finish one paid job. Do Level 2 and Level 3 as you go.

**Easiest way to follow along:** in the kit folder, double-click `tools/setup/index.html`. It's this same list with tick boxes, and it shows what to do next. Your ticks are saved in that browser.

## Level 1 · Finish your first paid job (about an hour)

1. **Claude account.** Sign up at claude.ai. A paid plan is needed for regular use.
2. **Claude Project.** Create a Project called "Websites". Download the latest version of this kit from the **Releases** section on the right of the GitHub page (the file named `landing-kit-…zip`), unzip it, and drag everything in the `claude` folder into the Project's files: `PROMPT.md`, `check_page.py`, and the files in `claude/library`. Add `templates/emails.md` too.
3. **Project instructions.** Type: `Follow PROMPT.md for every website.`
4. **Model.** In each chat, pick **Claude Opus 5.5** or a newer Opus from the model menu. This kit was built and tested with Opus.
5. **Netlify.** Create a free account at netlify.com. This is where the site goes online.
6. **Your prices.** Double-click `tools/pricing/index.html` in the kit folder (no upload needed). Fill in your own hours and costs. It suggests prices and writes a quote.
7. **Your agreement.** Fill in [`templates/agreement.md`](../templates/agreement.md): your name, prices, included rounds, and how many small updates the monthly care covers.
8. **Getting paid for one job.** The invoice maker (`tools/invoice/index.html` in the kit folder) is enough: the client pays by bank transfer, check or a payment link.
9. **Business basics.** Check your city and state rules for a business license or registered name, keep a separate bank account if you can, and ask an accountant about taxes. (This kit isn't legal or tax advice.)

## Level 2 · Get organised (about 45 minutes)

10. **Your tracker.** Upload `tools/tracker/tracker.xlsx` to Google Sheets (File, then Import) or open it in Excel. Every client, payment and round lives here, and each client gets a "Next step".
11. **Your tool pages online.** Drag the whole `tools` folder onto app.netlify.com/drop, once. You get one link; your pages are at `/intake/` (the question page you send clients), `/pricing/`, `/invoice/` and `/setup/` on it. Save them in the setup page's "Your links".
12. **Card payments.** Open a Square, Stripe or PayPal account so clients can pay by card, including automatic monthly billing for care plans.
13. **Your hosting budget.** All your clients' sites live in your Netlify account. If its monthly credits run out, **every site you host pauses** (visitors see "Site not available") until the next month, unless you upgrade or turn on auto recharge. Move to the $9 Personal plan once you have a few clients, check usage once a month, and decide whether to turn on auto recharge and with what monthly limit.
14. **Gmail (optional).** Connect Gmail to Claude in claude.ai's settings, under connectors. Claude can then read a client's emails for details and draft your replies. It never sends anything for you.

## Level 3 · Win more clients (about 2 to 4 hours)

15. **Two sample sites.** Build sites for two different kinds of business (a friend's or family member's), labelled "Sample".
16. **Your own site.** In a new chat in your Websites Project, say "Build my own site" and attach screenshots of your samples. You get a portfolio page with your examples, your packages, your phone and email, and a short enquiry form.
17. **Test it on your phone.** Send yourself a message from the enquiry form, tap your phone number and email, and open every example.
18. **Social posts (optional).** Ask Claude for a month of posts that point to your site, then schedule them with the platform's own scheduler (for Facebook and Instagram, Meta Business Suite).

**Not sure what to do next?** In your Websites Project, ask Claude "What do I do next?" and paste your tracker's Dashboard. The setup page has a button that writes the question for you.

Next: [2. Find clients](02-find-clients.md)
