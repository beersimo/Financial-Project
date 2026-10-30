// Render the references slide as page 13 of the hand-in PDF (no backup label, no index link).
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const [dir, out] = process.argv.slice(2);
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1920, height: 1080 } });
  await p.goto('file://' + path.join(dir, 'deck.html')); await p.waitForTimeout(500);
  await p.evaluate(() => {
    const all = [...document.querySelectorAll('section.slide')], s = all[29];
    all.forEach(x => { if (x !== s) x.remove(); });
    s.querySelectorAll('.backlink').forEach(e => e.remove());
    s.querySelector('.eyebrow').textContent = 'References';
    s.querySelector('.sub').textContent = 'Sources cited on the slides (APA 7th edition) – full entries with URLs in the report';
    s.querySelector('.pno').textContent = '13';
  });
  await p.pdf({ path: out, width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  await b.close();
})();
