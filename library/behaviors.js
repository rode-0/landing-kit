/* Landing Page Kit: tested behaviors.
   Copy only the blocks a page needs into one script tag at the end of the page body.
   Copy the functions only; leave these comments out of the page.
   Put this in the head first: a script tag containing  document.documentElement.classList.add('js')
   These are behavior only. Layout and look always come from the page's own design. */

/* ---------- 1. Open now / closed (or availability) ----------
   cfg = {
     tz: 'America/New_York',
     hours: { mon:[], tue:[], wed:[['07:00','14:00']], thu:[['07:00','14:00']], fri:[['07:00','14:00']],
              sat:[['07:00','14:00']], sun:[['07:00','14:00']] },     // 24h strings; [] = closed
     closed: { '2026-11-26':'Thanksgiving', '2026-11-27':'Thanksgiving' }, // optional
     words: { open:'Open now until {close}', soon:'Opens at {open} today',
              closed:'Closed now. Back {day} at {open}', holiday:'Closed today for {why}. Back {day} at {open}' }
   }
   For a mobile or appointment business use words like
   { open:'Booking today until {close}', closed:'Back on the road {day} at {open}', ... }.
   Times are shown the way people in the US write them (7am, 2pm, 5:30pm). */
function lpkLocal(now, tz) {
  var p = new Intl.DateTimeFormat('en-US', { timeZone: tz, year: 'numeric', month: '2-digit', day: '2-digit',
    hour: '2-digit', minute: '2-digit', hourCycle: 'h23', weekday: 'short' }).formatToParts(now);
  var o = {}; p.forEach(function (x) { o[x.type] = x.value; });
  return { date: o.year + '-' + o.month + '-' + o.day, wd: o.weekday.toLowerCase().slice(0, 3),
           mins: (+o.hour % 24) * 60 + (+o.minute) };
}
function lpkClock(hhmm) {
  var h = +hhmm.slice(0, 2), m = hhmm.slice(3, 5), ap = h < 12 ? 'am' : 'pm', h12 = h % 12 || 12;
  return h12 + (m === '00' ? '' : ':' + m) + ap;
}
function lpkStatus(now, cfg) {
  var days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  var t = lpkLocal(now, cfg.tz), toMin = function (s) { return +s.slice(0, 2) * 60 + +s.slice(3, 5); };
  var w = cfg.words, fill = function (s, v) { return s.replace(/\{(\w+)\}/g, function (_, k) { return v[k] || ''; }); };
  var closed = cfg.closed || {}, why = closed[t.date];
  var today = why ? [] : (cfg.hours[t.wd] || []);
  for (var i = 0; i < today.length; i++) {
    var a = toMin(today[i][0]), b = toMin(today[i][1]);
    if (t.mins >= a && t.mins < b) return { open: true, text: fill(w.open, { close: lpkClock(today[i][1]) }) };
    if (t.mins < a) return { open: false, text: fill(w.soon || w.closed, { open: lpkClock(today[i][0]), day: 'today' }) };
  }
  // find the next open day (skips closed dates), up to 14 days ahead
  var base = new Date(t.date + 'T12:00:00Z'), idx = days.indexOf(t.wd);
  for (var d = 1; d <= 14; d++) {
    var nd = new Date(base.getTime() + d * 864e5), key = nd.toISOString().slice(0, 10), wd = days[(idx + d) % 7];
    var hrs = closed[key] ? [] : (cfg.hours[wd] || []);
    if (hrs.length) {
      var label = d === 1 ? 'tomorrow' : names[(idx + d) % 7];
      if (d >= 7) label += ', ' + nd.toLocaleDateString('en-US', { month: 'short', day: 'numeric', timeZone: 'UTC' });
      return { open: false, text: fill(why ? (w.holiday || w.closed) : w.closed, { day: label, open: lpkClock(hrs[0][0]), why: why }) };
    }
  }
  return { open: false, text: '' };
}
// Use: var s = lpkStatus(new Date(), CFG); el.textContent = s.text; el.dataset.open = s.open;
// Emergency or 24/7 phone lines: keep the regular hours in CFG and add the 24/7 line as fixed text next
// to the status ("Emergency calls answered 24/7"), so the status never contradicts it.
// Keep the plain written hours in the HTML too, so the page works without JavaScript.

/* ---------- 1b. Next class (for class-based businesses: yoga, fitness, lessons) ----------
   schedule = { tz:'America/Chicago', classes:[ {day:'mon', time:'06:15', name:'Gentle Flow'}, ... ] }
   Returns 'Next class: Gentle Flow, today at 5:30pm' (or 'tomorrow at', or a weekday). */
function lpkNextClass(now, sch) {
  var days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'], names = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  var t = lpkLocal(now, sch.tz), idx = days.indexOf(t.wd);
  for (var d = 0; d < 8; d++) {
    var wd = days[(idx + d) % 7];
    var todays = sch.classes.filter(function (c) { return c.day === wd; })
      .map(function (c) { return { c: c, m: +c.time.slice(0, 2) * 60 + +c.time.slice(3, 5) }; })
      .filter(function (x) { return d > 0 || x.m > t.mins; })
      .sort(function (a, b) { return a.m - b.m; });
    if (todays.length) {
      var when = d === 0 ? 'today' : d === 1 ? 'tomorrow' : names[(idx + d) % 7];
      var c = todays[0].c;
      return 'Next class: ' + (c.name ? c.name + ', ' : '') + when + ' at ' + lpkClock(c.time);
    }
  }
  return '';
}

/* ---------- 2. Notice bar that hides itself ----------
   <div class="notice" data-until="2026-11-28" data-tz="America/New_York">Closed Nov 26-27 for Thanksgiving.</div>
   Shows until (not including) the date in data-until, in the business's time zone. */
function lpkNotices(now) {
  document.querySelectorAll('[data-until]').forEach(function (el) {
    var today = lpkLocal(now || new Date(), el.dataset.tz || 'UTC').date;
    if (today >= el.dataset.until) el.hidden = true;
  });
}

/* ---------- 3. Safe scroll reveals ----------
   CSS:  html.js .rv{opacity:0;transform:translateY(14px);transition:opacity .4s var(--ease),transform .4s var(--ease)}
         html.js .rv.in, html.js.all-in .rv{opacity:1;transform:none}
         @media (prefers-reduced-motion:reduce){html.js .rv{opacity:1;transform:none;transition:none}}
   Put class="rv" on blocks (never on an element that is fully clipped; for photo reveals, put rv on the
   frame and animate the img inside it). Content always shows if the observer is missing or never runs. */
function lpkReveal() {
  var root = document.documentElement, els = [].slice.call(document.querySelectorAll('.rv'));
  var showAll = function () { root.classList.add('all-in'); };
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) return showAll();
  var ran = false;
  var io = new IntersectionObserver(function (es) {
    ran = true;
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  els.forEach(function (el) { io.observe(el); });
  setTimeout(function () { if (!ran) showAll(); }, 3000);
}

/* ---------- 4. Nav gets a background after scrolling ---------- */
function lpkNav(sel) {
  var nav = document.querySelector(sel || 'header');
  if (!nav) return;
  var on = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
  on(); addEventListener('scroll', on, { passive: true });
}

/* ---------- 5. Web3Forms contact or request form ----------
   <form id="request" action="https://api.web3forms.com/submit" method="POST">
     <input type="hidden" name="access_key" value="REAL-KEY">
     <input type="hidden" name="subject" value="New request from the website">
     <input type="checkbox" name="botcheck" hidden tabindex="-1" autocomplete="off">
     ... fields with name="" ...  <button type="submit">Send request</button>
     <p class="form-msg" role="status" aria-live="polite"></p>
   </form>
   Without JavaScript the form still posts (Web3Forms shows its own thank-you page). */
function lpkForm(id, fallbackText) {
  var f = document.getElementById(id); if (!f) return;
  var msg = f.querySelector('.form-msg'), btn = f.querySelector('[type=submit]');
  f.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!f.checkValidity()) { f.reportValidity(); return; }
    btn.disabled = true; msg.textContent = 'Sending...';
    fetch(f.action, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(f) })
      .then(function (r) { return r.json().then(function (d) { return r.ok && d.success; }, function () { return false; }); })
      .then(function (ok) {
        msg.textContent = ok ? 'Sent. We will get back to you soon.' : 'That did not send. ' + fallbackText;
        if (ok) f.reset();
      }, function () { msg.textContent = 'That did not send. ' + fallbackText; })
      .then(function () { btn.disabled = false; });
  });
}
// Use: lpkForm('request', 'Please email or call us instead.')  (put the real email and phone in the text)

/* ---------- 6. One Copy button (use sparingly: the email address only) ----------
   <button type="button" data-copy="hello@business.com">Copy</button> */
function lpkCopy() {
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.dataset.copy, done = function (ok) { b.textContent = ok ? 'Copied' : 'Select and copy'; setTimeout(function () { b.textContent = 'Copy'; }, 1800); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(v).then(function () { done(true); }, function () { done(false); });
      else done(false);
    });
  });
}

/* ---------- 7. Sticky action bar on phones (CSS + HTML, no JavaScript) ----------
   <nav class="mbar" aria-label="Quick actions"><a href="BOOKING-OR-tel:">Book</a><a href="sms:+1...">Text</a></nav>
   .mbar{position:fixed;left:0;right:0;bottom:0;z-index:30;display:grid;grid-template-columns:1fr 1fr;
         padding-bottom:env(safe-area-inset-bottom,0px);background:var(--ink)}
   .mbar a{min-height:52px;display:grid;place-items:center;color:var(--bg);text-decoration:none}
   @media (min-width:760px){.mbar{display:none}}
   body{padding-bottom:64px} on phones so the bar never covers the footer. */

if (typeof module !== 'undefined') module.exports = { lpkStatus: lpkStatus, lpkLocal: lpkLocal, lpkClock: lpkClock, lpkNextClass: lpkNextClass };
