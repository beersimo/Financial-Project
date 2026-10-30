// Backup PowerPoint: pixel-identical slides (base image + content layers) with speaker notes.
const pptxgen = require('pptxgenjs'); const fs = require('fs'); const path = require('path');
const [layersDir, notesFile, outFile] = process.argv.slice(2);
const manifest = JSON.parse(fs.readFileSync(path.join(layersDir, 'manifest.json')));
const notes = JSON.parse(fs.readFileSync(notesFile));
const pres = new pptxgen();
pres.layout = 'LAYOUT_WIDE';               // 13.333 x 7.5 in = 1920 x 1080 px at 144 px/in
pres.title = 'Liebherr Group – Investment Analysis 2022–2025';
pres.author = 'Simon Beermann, Adam Fliegel, Zofia Narkiewicz, Philipp Hoffmann, Zarah Gilmore Islam';
pres.subject = 'HAT1 Financial Reporting, Fontys University of Applied Sciences';
const IN = v => v / 144;
manifest.forEach((m, i) => {
  const s = pres.addSlide();
  s.addImage({ path: path.join(layersDir, m.base), x: 0, y: 0, w: 13.333, h: 7.5, altText: `Slide ${i + 1}: ${notes[i][0]}`, objectName: 'Base' });
  m.layers.forEach((l, k) => s.addImage({ path: path.join(layersDir, l.file), x: IN(l.x), y: IN(l.y), w: IN(l.w), h: IN(l.h),
    altText: `${notes[i][0]} – element ${k + 1}`, objectName: (l.chart ? 'Chart ' : 'Element ') + (k + 1) }));
  // focus states (one condition framed in yellow, rest dimmed) appear on click, see pptx_effects.py
  for (let k = 1; fs.existsSync(path.join(layersDir, `s${i + 1}_focus${k}.jpg`)); k++)
    s.addImage({ path: path.join(layersDir, `s${i + 1}_focus${k}.jpg`), x: 0, y: 0, w: 13.333, h: 7.5,
      altText: `${notes[i][0]} – condition ${k} highlighted`, objectName: `Focus ${k}` });
  // invisible clickable areas for index / back links (slide jumps in the slide show)
  (m.links || []).forEach(l => s.addText('', { x: IN(l.x), y: IN(l.y), w: IN(l.w), h: IN(l.h), isTextBox: true,
    hyperlink: { slide: l.to, tooltip: 'Go to slide ' + l.to }, fill: { color: 'FFFFFF', transparency: 100 }, objectName: 'Link ' + l.to }));
  s.addNotes(notes[i][2]);
});
pres.writeFile({ fileName: outFile }).then(f => console.log('written', f));
