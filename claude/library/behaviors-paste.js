// Landing Kit behaviors, ready to paste inside one script tag. Generated from behaviors.js.
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

function lpkNotices(now) {
  document.querySelectorAll('[data-until]').forEach(function (el) {
    var today = lpkLocal(now || new Date(), el.dataset.tz || 'UTC').date;
    if (today >= el.dataset.until) el.hidden = true;
  });
}

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

function lpkNav(sel) {
  var nav = document.querySelector(sel || 'header');
  if (!nav) return;
  var on = function () { nav.classList.toggle('scrolled', window.scrollY > 8); };
  on(); addEventListener('scroll', on, { passive: true });
}

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

function lpkCopy() {
  document.querySelectorAll('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.dataset.copy, done = function (ok) { b.textContent = ok ? 'Copied' : 'Select and copy'; setTimeout(function () { b.textContent = 'Copy'; }, 1800); };
      if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(v).then(function () { done(true); }, function () { done(false); });
      else done(false);
    });
  });
}
