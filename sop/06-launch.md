# 6. Launch

The Claude link is only a preview. To put the real site online you need, once per site:

**Before you start**
- [ ] A **computer** (not a phone or tablet): step 3 is drag and drop.
- [ ] **Signed in to your Netlify account** (setup Level 1). A site dropped without signing in isn't saved to your account and can be deleted after a short time.
- [ ] The client has said the site is approved.
- [ ] About 30 minutes the first time.

**Steps**

1. Say **"approved"** in the client's chat. Claude runs a final check and gives you the final page, a list of every outside link on it, the hosting steps, and a row for your tracker's Clients tab.
   **Tap every link on the list on your phone** (booking, store, maps, socials, phone, email). Anything that opens the wrong page or "not found" gets fixed before launch.
2. **Download** the final page from Claude (the download option on the page), rename the file to `index.html`, and put it **alone in a new folder** named after the client (for example `vitos-pizzeria`).
3. **Put it online:** go to app.netlify.com/drop while signed in and drag the **folder** (not the file) onto the page. You get a link like `something.netlify.app`, and the site appears in your Netlify account. Rename it under Site configuration.
4. **Contact form** (if the site has one): get a free key at web3forms.com with the email that should receive messages, paste the key into the Claude chat, download the updated page, and drag its folder onto the site's **Deploys** page in Netlify. Then send a test message from the live site and check it arrives.
5. **Domain:** help the client buy their domain in their own name (any registrar), then connect it in Netlify under Domain management. Netlify adds the secure padlock (https) by itself; it can take a little while.
   **If they already have a domain, and especially email on it:** don't move the domain or change its nameservers. At the domain seller, add only the website records Netlify shows you, and never change or delete the email (MX) records. If anything is unclear, stop and ask the domain seller's support first. Breaking a client's email is the worst mistake you can make here.
6. **Email the client** that it's live, with the final invoice (email 7).
7. **Track it:** click the first empty cell in column A of the Clients tab and paste Claude's row. Set Stage to "Live" or "Care plan" and add the website address, domain and renewal date. Save the final `index.html` in the client's backup folder, named by date.

**If you get stuck**
- **The client's link asks them to sign in.** It's a work or company Claude account. Publish from a personal account, or ask your admin to allow outside sharing (see step 5 of the guide).
- **Netlify asks you to sign up or "claim" the site.** You weren't signed in. Sign in and claim it, or drop the folder again while signed in.
- **The site disappeared.** It was dropped without signing in. Sign in and drop the folder again.
- **Netlify shows a list of files or "Page not found".** The page isn't named `index.html`, or you dropped the file instead of its folder.
- **You're on a phone or tablet.** Drag and drop needs a computer. Do the launch later at a computer.
- **Photos or the logo are missing.** Tell Claude "the photos aren't showing on the live site"; it makes a version with everything inside the one file.

Next: [7. Bill and track](07-bill-and-track.md)
