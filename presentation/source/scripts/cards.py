"""Moderator cards: one third of an A4 page (210 x 99 mm) per slide, cut lines between cards.

Usage: python3 cards.py BUILD_DIR SPEAKER OUT_PDF
"""
import html, json, re, subprocess, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from notes import SPEAKERS

build, who, out = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]
notes = json.loads((build / "notes.json").read_text())
idx = [i for i in range(1, 13) if SPEAKERS.get(i) == who]

def fmt(p):
    p = html.escape(p)
    p = re.sub(r"\[Handover\]", '<span class="cue ho">→ HANDOVER</span>', p)
    p = re.sub(r"\[(CLICK[^\]]*)\]", lambda m: f'<span class="cue ck">● {m.group(1).upper()}</span>', p)
    p = re.sub(r"\[Q&amp;A\]", '<span class="cue qa">Q&amp;A</span>', p)
    return p

cards = []
for k, i in enumerate(idx, 1):
    t, d, txt = notes[i - 1]
    title = t.rsplit(" – ", 1)[0]
    paras = "".join(f"<p>{fmt(p)}</p>" for p in txt.split("\n\n"))
    nxt = notes[i][0].rsplit(" – ", 1)[0] if i < 12 else "Q&amp;A"
    cards.append(f'''<div class="card"><div class="hd"><span class="n">{i:02d}</span><span class="t">{html.escape(title)}</span>
<span class="d">{d if d != "—" else ""}</span><img src="shots/s{i:02d}.png"></div>
<div class="tx">{paras}</div><div class="ft"><span>{who} · card {k}/{len(idx)}</span><span>next: {nxt}</span></div></div>''')

pages = ["".join(cards[j:j + 3]) for j in range(0, len(cards), 3)]
doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4 portrait;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Arimo,Arial,sans-serif;color:#00182E}}
.page{{width:210mm;height:297mm;page-break-after:always;display:flex;flex-direction:column}}
.page:last-child{{page-break-after:auto}}
.card{{position:relative;width:210mm;height:99mm;padding:5mm 8mm 4mm;border-bottom:0.4mm dashed #9AA3AC;display:flex;flex-direction:column}}
.hd{{display:flex;align-items:center;gap:3mm;border-bottom:0.8mm solid #FFCF00;padding-bottom:1.5mm;margin-bottom:2mm}}
.n{{background:#00182E;color:#FFCF00;font-weight:800;font-size:13pt;padding:.6mm 2.4mm;border-radius:1.5mm}}
.t{{font-weight:700;font-size:14pt;flex:1}}
.d{{font-weight:800;font-size:11pt;color:#5E6873}}
.hd img{{height:12mm;border:0.2mm solid #D0D3D8}}
.tx{{flex:1;overflow:hidden}}
.tx p{{line-height:1.32;margin:0 0 1.1mm}}
.cue{{display:inline-block;font-weight:800;font-size:.72em;letter-spacing:.3pt;border-radius:1mm;padding:.2mm 1.6mm;margin-right:1mm}}
.ho{{background:#00182E;color:#FFCF00}}.ck{{background:#FFCF00;color:#00182E}}.qa{{background:#E9EBEE}}
.ft{{display:flex;justify-content:space-between;font-size:8pt;color:#8A939C;margin-top:1mm}}
</style></head><body>{"".join(f'<div class="page">{p}</div>' for p in pages)}
<script>
// largest font size (max 15pt) at which each card's text fits
document.querySelectorAll('.tx').forEach(t=>{{let s=15;t.style.fontSize=s+'pt';
  while((t.scrollHeight>t.clientHeight)&&s>8.5){{s-=0.25;t.style.fontSize=s+'pt';}} t.dataset.size=s;}});
</script></body></html>'''
src = build / f"cards_{who}.html"
src.write_text(doc)
js = f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.emulateMedia({{media:'print'}});await p.goto('file://{src}');await p.waitForTimeout(600);
await p.evaluate(()=>document.querySelectorAll('.tx').forEach(t=>{{let s=15;t.style.fontSize=s+'pt';while(t.scrollHeight>t.clientHeight+1&&s>8.5){{s-=0.25;t.style.fontSize=s+'pt';}}t.dataset.size=s;}}));
console.log(JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('.tx')].map(t=>t.dataset.size))));
await p.pdf({{path:'{out}',preferCSSPageSize:true,printBackground:true}});await b.close();}})();'''
r = subprocess.run(["node", "-e", js], capture_output=True, text=True, cwd=str(pathlib.Path(__file__).parent))
print("font sizes (pt):", r.stdout.strip(), r.stderr[-300:])
