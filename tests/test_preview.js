const assert = require('assert');
const { lkPreview, lkPreviewMessage } = require('../tools/preview/preview.js');
const src = `<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Vito's Pizzeria</title>
<script type="application/ld+json">{"@type":"Restaurant","name":"Vito's"}</script></head><body>
<a href="https://order.example-pos.com/vitos" target="_blank" rel="noopener">Order online</a>
<a href="tel:+12295550142">Call</a> <a href='mailto:hi@vitos.test'>Email</a> <a href="sms:+12295550142">Text</a>
<a href="#menu">Menu</a> <a href="//maps.google.com/?q=x">Map</a>
<form action="https://api.web3forms.com/submit" method="POST"><input name="n"></form></body></html>`;
const out = lkPreview(src, { business: "Vito's Pizzeria", version: '2', from: 'Andre' });
assert(!/href="(https?:|tel:|mailto:|sms:|\/\/)/.test(out), 'a live outside link is left');
assert(!/href='mailto/.test(out));
assert(out.includes('href="#menu"'), 'links inside the page stay');
assert(!/target=|rel=/.test(out.split('<body')[1].split('<script>')[0]), 'target/rel removed from rewritten links');
assert(out.includes('action="#lk-preview"') && !out.includes('web3forms'), 'form does not post');
assert(!out.includes('ld+json'), 'structured data removed');
assert(out.includes('content="noindex, nofollow"') && out.includes('<title>PREVIEW: Vito'), 'noindex and title');
assert(out.includes('id="lk-preview"') && out.includes('version 2') && out.includes('Reply to Andre'), 'banner');
assert((out.match(/<\/body>/g) || []).length === 1 && out.includes('lk-preview-msg'), 'submit guard once');
assert(/html::after\{[^}]*pointer-events:none/.test(out), 'watermark does not block taps');
const msg = lkPreviewMessage({ business: "Vito's Pizzeria", contact: 'Sal', version: '2', from: 'Andre' });
assert(msg.startsWith('Hi Sal,') && msg.includes('tap the attachment') && msg.endsWith('Andre'));
console.log('preview maker: all tests passed');
