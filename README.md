# Landing Page Kit

Make a clean, professional website for a small business with Claude. No coding.

You collect the business's details and photos, Claude designs the page with you, and you put it online for free by dragging one file onto a website.

![Five example sites made with this kit](examples/overview.png)

*Five made-up businesses, each designed for its own customers. Photo credits are in [examples/CREDITS.md](examples/CREDITS.md).*


---

## Set up once (about 10 minutes)

1. **Get a Claude account** at [claude.ai](https://claude.ai). A paid plan gives you more room for back-and-forth.
2. **Make a Project** in Claude called "Websites".
3. **Add this kit to the Project.** On this page, click the green **Code** button, then **Download ZIP**. Unzip it, then drag `PROMPT.md`, `check_page.py` and everything in the `library` folder into the Project's files.
4. **In the Project instructions**, type: `Follow PROMPT.md for every website.`
5. **Pick the model.** When you start a chat, open the model menu (next to the message box) and choose **Claude Opus 5.5**, or a newer Opus if there is one. This kit was built and tested with Opus.
6. **Get a free Netlify account** at [netlify.com](https://www.netlify.com). This is where the websites live.
7. **Put the question page online** (you only do this once): drag the `intake` folder from the ZIP onto [app.netlify.com/drop](https://app.netlify.com/drop). Netlify gives you a link. That's the page you'll send to every client.

---

## For each new client

1. **Send the client your question page link.** They answer on their phone, tap **Copy my answers**, and text or email them back to you. Ask them to send their logo and 4 to 10 of their own photos too.
2. **Start a new chat in your Websites Project** (with Claude Opus 5.5 or newer selected). Paste their answers and attach their logo and photos.
3. **Pick a direction (optional).** Say "show me concepts" if you'd like three quick layout ideas to choose from first.
4. **Look at the page Claude makes.** Tell Claude what to change in plain words, as many times as you like. Claude keeps a numbered version each time and tells you what changed.
5. **Show the client.** Click **Publish** on the page in Claude and send the client the link. Paste their comments back into the chat.
6. **When everyone is happy, say "approved".** Claude checks the page one last time and gives you the final file.
7. **Put it online.** Download the file, put it in a folder by itself, and drag the folder onto [app.netlify.com/drop](https://app.netlify.com/drop). You'll get a link like `something.netlify.app`. In Netlify you can rename it or connect the business's own domain.

---

## What it costs, and what to charge

- **You pay:** a Claude plan (Pro is $20 a month; Max is $100 or $200 for much more use). That's usually it.
- **Free:** hosting on Netlify (give each client their own free account, so they own their site) and contact forms for up to 250 messages a month.
- **The client pays:** their domain name, usually $10 to $20 a year.
- **How many sites your plan covers** isn't a fixed number, because Claude's limits reset every few hours and weekly. After your first two or three sites, check how much of your weekly limit each one used.

Put the `pricing` folder online the same way as the question page, and open it to work out your prices. It shows what each site costs you, what you really earn per hour, and writes a quote you can send the client.

*Prices as of November 2026. Check claude.com/pricing and netlify.com/pricing for current prices.*

## Changing a site later

Open the same chat (or a new one in the Project), say what changed ("new hours", "closed for the holidays until Jan 2"), and get the new file. In Netlify, open the site, go to **Deploys**, and drag the folder with the new file onto the page.

## Contact forms (optional)

Want visitors to send messages from the site? Go to [web3forms.com](https://web3forms.com), enter the email address that should receive the messages, and you'll get a key by email. Give that key to Claude and ask for a contact form. It's free and needs no account.

## Online booking (optional)

If the business already uses Square, Calendly, Jane, OpenTable or similar, give Claude the booking link. The site's main button will open it.

---

## If something goes wrong

- **"Copy my answers" doesn't work for the client.** They probably opened the link inside Instagram or Facebook. Ask them to open it in Safari or Chrome.
- **The contact form doesn't send.** Check that the Web3Forms key is the real one from the email, not a sample. The form also won't send from the Claude preview link, only from the real Netlify site.
- **Photos don't show up.** Tell Claude "the photos aren't showing" and it will fix it.
- **Something looks wrong on a phone.** Take a screenshot, attach it in the chat, and say what's wrong.

## What's in this kit

| File | What it's for |
|---|---|
| `PROMPT.md` | The instructions Claude follows. You don't need to read it. |
| `check_page.py` | A checker Claude runs on each page before showing it to you. |
| `intake/` | The question page you send to clients. |
| `pricing/` | A calculator for your costs and prices, with a quote you can send. |
| `library/` | Notes and tested pieces Claude uses to design well. Add the whole folder to the Project. |
| `examples/` | Pictures of sites made with this kit. |
