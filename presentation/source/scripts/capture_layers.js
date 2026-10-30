// Split every slide into a static base image (backgrounds, photos, title) and one transparent PNG per content element.
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const dir = process.argv[2], out = process.argv[3]; fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(dir, 'deck.html')); await p.waitForTimeout(500);
  const n = await p.evaluate(() => document.querySelectorAll('section.slide').length);
  const manifest = [];
  for (let s = 0; s < n; s++) {
    // classify children of slide s
    const items = await p.evaluate((s) => {
      document.querySelectorAll('section.slide').forEach((el, i) => el.style.display = i === s ? 'block' : 'none');
      const sl = document.querySelectorAll('section.slide')[s];
      const res = [];
      [...sl.children].forEach((el, k) => {
        el.dataset.k = k;
        const st = el.style, w = parseFloat(st.width) || el.getBoundingClientRect().width, top = parseFloat(st.top) || 0;
        const isBg = el.classList.contains('band') || el.classList.contains('photo') || el.classList.contains('strip') ||
          el.classList.contains('pno') || el.classList.contains('src') || el.classList.contains('eyebrow') ||
          el.tagName === 'H1' || el.tagName === 'H2' || el.tagName === 'svg' && !el.querySelector('rect,polyline') ||
          (w >= 1100 && top <= 0) || (el.tagName === 'DIV' && !el.textContent.trim() && !el.querySelector('svg,img'));
        const r = el.getBoundingClientRect();
        res.push({ k, bg: isBg, x: r.left, y: r.top, w: r.width, h: r.height, chart: !!el.querySelector('svg rect.gv,svg rect.gvn,svg rect.gh,svg polyline.ln') });
      });
      return res;
    }, s);
    const sl = await p.$$('section.slide');
    // base: content hidden
    await p.evaluate((s) => { const sl = document.querySelectorAll('section.slide')[s];
      [...sl.children].forEach(el => el.style.visibility = ''); }, s);
    const contentKs = items.filter(i => !i.bg).map(i => i.k);
    await p.evaluate(([s, ks]) => { const sl = document.querySelectorAll('section.slide')[s];
      ks.forEach(k => sl.children[k].style.visibility = 'hidden'); }, [s, contentKs]);
    const base = `s${s + 1}_base.jpg`;
    await sl[s].screenshot({ path: path.join(out, base), type: 'jpeg', quality: 90 });
    // each content element alone, transparent
    const layers = [];
    for (const it of items.filter(i => !i.bg)) {
      await p.evaluate(([s, k]) => {
        document.documentElement.style.background = 'transparent'; document.body.style.background = 'transparent';
        const sl = document.querySelectorAll('section.slide')[s]; sl.style.background = 'transparent';
        [...sl.children].forEach((el, j) => el.style.visibility = j === k ? 'visible' : 'hidden');
      }, [s, it.k]);
      const m = 34, x = Math.max(0, it.x - m), y = Math.max(0, it.y - m);
      const w = Math.min(1920, it.x + it.w + m) - x, h = Math.min(1080, it.y + it.h + m) - y;
      const file = `s${s + 1}_e${it.k}.png`;
      await p.screenshot({ path: path.join(out, file), clip: { x, y, width: w, height: h }, omitBackground: true });
      layers.push({ file, x, y, w, h, chart: it.chart });
    }
    await p.evaluate((s) => { const sl = document.querySelectorAll('section.slide')[s]; sl.style.background = '';
      [...sl.children].forEach(el => el.style.visibility = ''); document.body.style.background = ''; document.documentElement.style.background = ''; }, s);
    manifest.push({ base, layers });
  }
  fs.writeFileSync(path.join(out, 'manifest.json'), JSON.stringify(manifest, null, 1));
  console.log(manifest.map((m, i) => `${i + 1}:${m.layers.length}`).join(' '));
  await b.close();
})();
