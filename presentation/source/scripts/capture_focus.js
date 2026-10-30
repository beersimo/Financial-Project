// Capture the focus states (yellow frame on one condition, rest dimmed) of every slide that has .focus-step elements.
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [dir, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(dir, 'present.html')); await p.waitForTimeout(500);
  await p.addStyleTag({ content: '#progress,#hint,#dots{display:none!important}' });
  const targets = await p.evaluate(() => [...document.querySelectorAll('#stage .slide')].map((s, i) => [i, s.querySelectorAll('.focus-step').length]).filter(x => x[1] > 0));
  for (const [i, n] of targets) {
    await p.evaluate(i => { location.hash = '#' + (i + 1); show(i); }, i);
    await p.waitForTimeout(4000);                       // let the entrance animations finish
    for (let k = 1; k <= n; k++) {
      await p.keyboard.press('ArrowRight'); await p.waitForTimeout(900);
      await p.screenshot({ path: path.join(out, `s${i + 1}_focus${k}.jpg`), type: 'jpeg', quality: 90 });
      console.log(`slide ${i + 1} focus ${k}`);
    }
  }
  await b.close();
})();
