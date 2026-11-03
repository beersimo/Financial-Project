"""Two moderator cards per A4 page (210 x 148.5 mm), two slides per card, plus key figures.

Usage: python3 cards2.py BUILD_DIR OUT_PDF
Card 1 = slides 9 and 10, card 2 = slides 11 and 12 (without the Q&A block) and key figures.
"""
import html, json, re, subprocess, sys, pathlib

build, out = pathlib.Path(sys.argv[1]), sys.argv[2]
notes = json.loads((build / "notes.json").read_text())

def fmt(p):
    p = html.escape(p)
    p = re.sub(r"\[Handover\]", '<span class="cue ho">→ HANDOVER</span>', p)
    p = re.sub(r"\[(CLICK[^\]]*)\]", lambda m: f'<span class="cue ck">● {m.group(1).upper()}</span>', p)
    return p

def section(i, grow):
    t, d, txt = notes[i - 1]
    txt = txt.split("[Q&A]")[0].strip()
    paras = "".join(f"<p>{fmt(p)}</p>" for p in txt.split("\n\n") if p.strip())
    return (f'<div class="sec"><div class="hd"><span class="n">{i:02d}</span><span class="t">{html.escape(t.rsplit(" – ", 1)[0])}</span>'
            f'<span class="d">{d if d != "—" else ""}</span><img src="shots/s{i:02d}.png"></div><div class="tx">{paras}</div></div>')

# key figures – all from the report and workbook (Dashboard, D3, D5, D7, D10, Table 2 and 3)
figs = [("Revenue 2025", "€14,772 m, +1.0 %"), ("Operating margin", "2.8 % · CAT 17.2 % · industry 15.9 %"),
        ("ROE", "3.0 % after tax · 4.8 % before tax"), ("ROCE (pre-tax)", "3.5 % vs. 7.70 % benchmark"),
        ("Equity ratio", "53.5 % · CAT 24.9 %"), ("Current ratio", "2.31 · cash cover 2.6×"),
        ("Free cash flow", "−€176 m · negative 3 of 4 years"), ("Net financial position", "€249 m (2022: €523 m)"),
        ("Debt / EBITDA", "2.90 · industry 2.30"), ("Cash conversion cycle", "202.7 days · CAT 126.1"),
        ("Inventories", "42.9 % of revenue · industry 16.6 %"), ("Levers", "1 margin point = €148 m · −10 days CCC = €405 m once")]
fig = "".join(f'<li><b>{a}</b> {b}</li>' for a, b in figs)
key = (f'<div class="sec key"><div class="hd"><span class="n">★</span><span class="t">Key figures Liebherr</span>'
       f'<span class="d">conditions: margin ≥ 3.9 % · FCF &gt; 0 · information</span></div><ul>{fig}</ul></div>')

card1 = f'<div class="card">{section(9, 0.9)}{section(10, 1.45)}<div class="sp"></div><div class="ft"><span>Simon · card 1/2</span><span>next: Conclusion</span></div></div>'
card2 = f'<div class="card">{section(11, 1.0)}{section(12, 0.3)}{key}<div class="ft"><span>Simon · card 2/2</span><span>then: Q&amp;A – press I for the backup index</span></div></div>'

doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4 portrait;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Arimo,Arial,sans-serif;color:#00182E}}
.page{{width:210mm;height:297mm;overflow:hidden}}html,body{{width:210mm;height:297mm;overflow:hidden}}
.card{{width:210mm;height:148.4mm;overflow:hidden;padding:6mm 9mm 4mm;display:flex;flex-direction:column;gap:2.5mm}}
.card:first-child{{border-bottom:0.4mm dashed #9AA3AC}}
.sec{{flex:none}}.key{{flex:1}}.sp{{flex:1}}
.hd{{display:flex;align-items:center;gap:3mm;border-bottom:0.8mm solid #FFCF00;padding-bottom:1.2mm;margin-bottom:1.5mm}}
.n{{background:#00182E;color:#FFCF00;font-weight:800;font-size:12pt;padding:.5mm 2.2mm;border-radius:1.5mm}}
.t{{font-weight:700;font-size:13pt;flex:1}}.d{{font-weight:800;font-size:9.5pt;color:#5E6873}}
.hd img{{height:10mm;border:0.2mm solid #D0D3D8}}
.tx p{{line-height:1.32;margin:0 0 1.1mm}}
.cue{{display:inline-block;font-weight:800;font-size:.72em;border-radius:1mm;padding:.2mm 1.5mm;margin-right:1mm}}
.ho{{background:#00182E;color:#FFCF00}}.ck{{background:#FFCF00;color:#00182E}}
.key{{background:#F3F4F6;border-radius:2mm;padding:2mm 3mm}}
.key ul{{list-style:none;columns:2;column-gap:6mm;font-size:.9em;line-height:1.25}}
.key li{{break-inside:avoid;margin-bottom:.9mm;padding-left:3mm;position:relative}}
.key li:before{{content:"";position:absolute;left:0;top:1.6mm;width:1.6mm;height:1.6mm;border-radius:50%;background:#FFCF00}}
.key li b{{display:block;font-size:8.5pt;letter-spacing:.3pt;text-transform:uppercase;color:#5E6873}}
.ft{{display:flex;justify-content:space-between;font-size:8pt;color:#8A939C}}
</style></head><body><div class="page">{card1}{card2}</div></body></html>'''
src = build / "cards2_Simon.html"
src.write_text(doc)
js = f'''const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.emulateMedia({{media:'print'}});await p.goto('file://{src}');await p.waitForTimeout(600);
const sizes=await p.evaluate(()=>[...document.querySelectorAll('.card')].map(c=>{{let s=16;c.style.fontSize=s+'pt';
 while(c.scrollHeight>c.clientHeight+1&&s>8){{s-=0.25;c.style.fontSize=s+'pt';}}return s;}}));
console.log(JSON.stringify({{sizes}}));
await p.pdf({{path:'{out}',preferCSSPageSize:true,printBackground:true}});await b.close();}})();'''
r = subprocess.run(["node", "-e", js], capture_output=True, text=True, cwd=str(pathlib.Path(__file__).parent))
print(r.stdout.strip(), r.stderr[-300:])
