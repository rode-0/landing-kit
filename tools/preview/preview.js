/* Landing Kit preview maker: turns a finished page into a preview the client can look at but can't use.
   Outside links, phone, email and text buttons go to the preview note; forms don't send; search engines are
   told not to index it; structured data is removed; "PREVIEW" is marked across every screen. */
function lkPreview(html, opts) {
  var biz = (opts && opts.business) || 'your business', ver = (opts && opts.version) || '1', from = (opts && opts.from) || '';
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
  var out = html;
  // links that leave the page, or call / email / text
  out = out.replace(/<a\b[^>]*>/gi, function (tag) {
    if (!/href\s*=\s*["']?\s*(https?:|tel:|mailto:|sms:|\/\/)/i.test(tag)) return tag;
    return tag.replace(/\shref\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/i, ' href="#lk-preview"').replace(/\s(target|rel)\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, '');
  });
  // forms post nowhere
  out = out.replace(/(<form\b[^>]*?)\saction\s*=\s*("[^"]*"|'[^']*'|[^\s>]+)/gi, '$1 action="#lk-preview"');
  // no structured data, no indexing
  out = out.replace(/<script\b[^>]*application\/ld\+json[^>]*>[\s\S]*?<\/script>/gi, '');
  var head = '<meta name="robots" content="noindex, nofollow">';
  out = /<head\b[^>]*>/i.test(out) ? out.replace(/<head\b[^>]*>/i, function (m) { return m + head; }) : head + out;
  out = /<title>/i.test(out) ? out.replace(/<title>/i, '<title>PREVIEW: ') : out;
  var mark = encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="360" height="220"><text x="20" y="120" transform="rotate(-24 180 110)" font-family="Arial,sans-serif" font-size="28" font-weight="700" fill="#000">PREVIEW · not for use</text></svg>');
  var style = '<style>#lk-preview{position:relative;z-index:2147483001;background:#1d1b18;color:#fff;font:15px/1.45 system-ui,sans-serif;padding:14px max(16px,env(safe-area-inset-left,0px));}' +
    '#lk-preview strong{color:#ffd27a}#lk-preview p{margin:4px 0 0;max-width:70ch}' +
    'html::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:2147483000;opacity:.10;background:url("data:image/svg+xml,' + mark + '") repeat;}' +
    '@media (prefers-color-scheme:dark){html::after{filter:invert(1)}}' +
    '.lk-preview-msg{font:600 15px/1.4 system-ui,sans-serif;background:#ffd27a;color:#1d1b18;padding:10px 12px;border-radius:6px}</style>';
  var banner = '<div id="lk-preview" role="note" tabindex="-1"><strong>PREVIEW of ' + esc(biz) + "'s new website, version " + esc(ver) + '.</strong>' +
    '<p>Scroll through it on your phone and computer. Buttons for booking, ordering, calling and maps are switched off in the preview, and the form doesn\'t send. They all work on the live site.</p>' +
    '<p>Reply to ' + (from ? esc(from) : 'me') + ' with anything you\'d like changed. Please don\'t share or post this preview.</p></div>';
  var guard = '<script>document.addEventListener("submit",function(e){e.preventDefault();e.stopPropagation();var f=e.target,m=f.querySelector(".lk-preview-msg");' +
    'if(!m){m=document.createElement("p");m.className="lk-preview-msg";m.setAttribute("role","status");f.appendChild(m)}m.textContent="Preview: on the live site this sends the message.";},true);</script>';
  out = /<\/head>/i.test(out) ? out.replace(/<\/head>/i, style + '</head>') : style + out;
  out = /<body\b[^>]*>/i.test(out) ? out.replace(/<body\b[^>]*>/i, function (m) { return m + banner; }) : banner + out;
  out = /<\/body>/i.test(out) ? out.replace(/<\/body>(?![\s\S]*<\/body>)/i, guard + '</body>') : out + guard;
  return out;
}
function lkPreviewMessage(opts) {
  var biz = opts.business || 'your business', name = opts.contact || 'there', from = opts.from || '';
  return 'Hi ' + name + ', here is a preview of the new ' + biz + ' website (version ' + (opts.version || '1') + '), attached.\n\n' +
    'To look at it: tap the attachment. It opens in your web browser (on a computer, double-click it). If it shows as code, save it and open it with Safari or Chrome.\n\n' +
    'It is marked PREVIEW, and the booking, ordering, call and map buttons are switched off until the site is live. Have a look on your phone and reply with anything you would like changed.\n\n' +
    'Thanks,\n' + from;
}
if (typeof module !== 'undefined') module.exports = { lkPreview: lkPreview, lkPreviewMessage: lkPreviewMessage };
