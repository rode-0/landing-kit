// The Python preview script and the browser preview maker must produce the same file and message.
const assert = require('assert'), fs = require('fs'), { execFileSync } = require('child_process'), os = require('os'), path = require('path');
const { lkPreview, lkPreviewMessage } = require('../tools/preview/preview.js');
const pages = ['tests/fixtures/good.html'].concat(fs.readdirSync('examples/demos').map(f => 'examples/demos/' + f).slice(0, 2));
const extra = path.join(os.tmpdir(), 'lk-parity-src.html');
fs.writeFileSync(extra, `<!doctype html><html lang="en"><head><title>Vito's Pizzeria | Valdosta</title><script type="application/ld+json">{}</script></head><body><a href="https://x.test/o" target="_blank">Order</a><a href='tel:+1'>Call</a><a href="#m">Menu</a><form action="https://api.web3forms.com/submit"></form></body></html>`);
pages.push(extra);
for (const biz of ["Vito's Pizzeria", 'Ridgeline Barbers']) for (const p of pages) {
  const html = fs.readFileSync(p, 'utf8'), out = path.join(os.tmpdir(), 'lk-parity-out.html');
  const msg = execFileSync('python3', ['plugin/skills/landing-kit/scripts/make_preview.py', p, out, '--business', biz, '--version', '2', '--owner', 'Sal', '--from', 'Andre'], { encoding: 'utf8' });
  const py = fs.readFileSync(out, 'utf8'), js = lkPreview(html, { business: biz, version: '2', from: 'Andre' });
  assert.strictEqual(py, js, 'preview differs for ' + p);
  assert.strictEqual(msg.replace(/\n$/, ''), lkPreviewMessage({ business: biz, contact: 'Sal', version: '2', from: 'Andre' }), 'message differs');
}
console.log('preview parity (Python vs browser): ' + pages.length + ' pages identical');
