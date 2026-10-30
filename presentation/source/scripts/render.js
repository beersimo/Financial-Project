const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
(async () => {
  const dir = process.argv[2];
  fs.mkdirSync(path.join(dir, 'shots'), { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.goto('file://' + path.join(dir, 'deck.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(500);
  const slides = await page.$$('section.slide');
  for (let i = 0; i < slides.length; i++) {
    await slides[i].screenshot({ path: path.join(dir, 'shots', `s${String(i + 1).padStart(2, '0')}.png`) });
  }
  await page.pdf({ path: path.join(dir, 'deck.pdf'), width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true });
  const n = await browser.newPage();
  await n.goto('file://' + path.join(dir, 'notes.html'));
  await n.evaluate(() => document.fonts.ready);
  await n.pdf({ path: path.join(dir, 'notes.pdf'), format: 'A4', landscape: true, printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('rendered', slides.length);
})();
