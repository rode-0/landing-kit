# 1. Set up (once, about an hour)

1. **Claude account.** Sign up at claude.ai. A paid plan is needed for regular use.
2. **Claude Project.** Create a Project called "Websites". Download this kit (green **Code** button, then **Download ZIP**), unzip it, and drag everything in the `claude` folder into the Project's files: `PROMPT.md`, `check_page.py`, and the three files in `claude/library`. Add `templates/emails.md` too.
3. **Project instructions.** Type: `Follow PROMPT.md for every website.`
4. **Model.** In each chat, pick **Claude Opus 5.5** or a newer Opus from the model menu. This kit was built and tested with Opus.
5. **Gmail (recommended).** Connect Gmail to Claude in claude.ai's settings, under connectors. Claude can then read a client's emails for details and draft your replies. It never sends anything for you.
6. **Netlify.** Create an account at netlify.com. All your clients' sites will live here. Start free; move to the $9 Personal plan once you have a few clients.
7. **Your tools.** Drag each of these folders onto app.netlify.com/drop to get a link for each: `tools/intake` (the question page you send clients), `tools/pricing` and `tools/invoice`. Bookmark them.
8. **Your dashboard.** Upload `tools/tracker/tracker.xlsx` to Google Sheets (File, then Import) or open it in Excel. This is where every client, payment and round lives.
9. **Getting paid.** Open a free Square, Stripe or PayPal account so clients can pay invoices by card, including monthly automatic billing.
10. **Business basics.** Check your city and state rules for a business license or registered name, keep a separate bank account if you can, and ask an accountant about taxes. (This kit isn't legal or tax advice.)

Next: [2. Find clients](02-find-clients.md)
