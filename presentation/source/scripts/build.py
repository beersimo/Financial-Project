import sys, pathlib, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import charts as C

BUILD = pathlib.Path(sys.argv[1])
FONTS = (BUILD / "fonts" / "local.css").read_text()

CSS = FONTS + """
:root{--y:#FFCF00;--y2:#F2BF00;--navy:#00182E;--cat:#3A444E;--grey:#D0D3D8;--light:#F3F4F6;--muted:#5E6873;}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff}
body{font-family:Assistant,Arimo,sans-serif;color:var(--navy)}
@page{size:1920px 1080px;margin:0}
.slide{position:relative;width:1920px;height:1080px;overflow:hidden;background:#fff;page-break-after:always;break-after:page}
h1,h2,.h{font-family:Arimo,Arial,sans-serif;font-weight:700;letter-spacing:-0.5px;color:var(--navy)}
.band{position:absolute;left:0;top:0;width:1920px;height:210px;background:var(--y)}
.band h2{position:absolute;left:96px;top:66px;font-size:56px;line-height:1.08;max-width:1500px}
.band .sub{position:absolute;left:98px;top:150px;font-size:27px;font-weight:600;color:var(--navy)}
.eyebrow{position:absolute;left:98px;top:34px;font-size:20px;font-weight:800;letter-spacing:3px;text-transform:uppercase;color:var(--navy);opacity:.75}
.strip{position:absolute;left:0;bottom:0;width:1920px;height:22px;background:var(--y)}
.src{position:absolute;left:98px;bottom:38px;font-size:17px;color:var(--muted);max-width:1500px}
.pno{position:absolute;right:70px;bottom:36px;font-size:18px;font-weight:800;color:var(--navy)}
.pill{position:absolute;left:50%;transform:translateX(-50%);background:var(--y);border-radius:44px;padding:16px 46px;font-size:27px;font-weight:800;white-space:nowrap;color:var(--navy)}
.pill b{font-weight:800;opacity:.65;margin-right:10px;text-transform:uppercase;font-size:20px;letter-spacing:2px}
.card{position:absolute;background:var(--light);border-radius:18px;padding:30px 34px}
.card h3{font-family:Arimo,Arial,sans-serif;font-size:27px;font-weight:700;margin-bottom:12px}
.ctitle{font-size:24px;font-weight:800;margin-bottom:6px}
.cnote{font-size:19px;color:var(--muted)}
.photo{position:absolute;background-size:cover;background-position:center}
.dots{position:absolute}
.tag{display:inline-block;font-size:17px;font-weight:800;letter-spacing:2px;text-transform:uppercase;padding:6px 14px;border-radius:8px}
ul.b{list-style:none}
ul.b li{position:relative;padding-left:34px;font-size:24px;line-height:1.32;margin-bottom:12px}
ul.b li:before{content:"";position:absolute;left:4px;top:11px;width:13px;height:13px;border-radius:50%;background:var(--y);box-shadow:0 0 0 4px rgba(255,207,0,.25)}
.big{font-family:Arimo,Arial,sans-serif;font-weight:700;letter-spacing:-1px}
.legend{font-size:20px;font-weight:700}
.legend i{display:inline-block;width:18px;height:18px;margin:0 8px 0 22px;vertical-align:-2px}
"""

def dots(x, y, cols=5, rows=3, col="#fff", gap=22, r=3.2, op=0.9):
    w, h = cols * gap, rows * gap
    c = "".join(f'<circle cx="{gap/2+i*gap}" cy="{gap/2+j*gap}" r="{r}" fill="{col}"/>' for i in range(cols) for j in range(rows))
    return f'<svg class="dots" style="left:{x}px;top:{y}px;opacity:{op}" width="{w}" height="{h}">{c}</svg>'

def swirl(x, y, scale=1.0, col="#E6B800", op=0.55, rot=0):
    return (f'<svg style="position:absolute;left:{x}px;top:{y}px;opacity:{op};transform:rotate({rot}deg) scale({scale});transform-origin:0 0" width="420" height="300" viewBox="0 0 420 300">'
            f'<path d="M10 240 C 80 120, 160 60, 230 120 S 250 260, 180 230 S 220 60, 330 40 S 420 110, 400 190" fill="none" stroke="{col}" stroke-width="9" stroke-linecap="round"/></svg>')

def photo(name, x, y, w, h, pos="center", radius=0, extra=""):
    return (f'<div class="photo" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
            f'background-image:url(img/{name});background-position:{pos};border-radius:{radius}px;{extra}"></div>')

def frame(n, src, body, pill=None, pill_y=905):
    n = len(slides) + 1
    p = f'<div class="pill" style="top:{pill_y}px">{pill}</div>' if pill else ""
    s = f'<div class="src">Source: {src}</div>' if src else ""
    return f'<section class="slide">{body}{p}{s}<div class="pno">{n:02d}</div><div class="strip"></div></section>'

def band(eyebrow, title, sub=""):
    return (f'<div class="band"><div class="eyebrow">{eyebrow}</div><h2>{title}</h2>'
            + (f'<div class="sub">{sub}</div>' if sub else "") + '</div>'
            + swirl(1560, -40, 1.0) + dots(1740, 150))

slides, notes = [], []

# ---------------------------------------------------------------- 1 Title
slides.append(f"""<section class="slide">
<div style="position:absolute;left:0;top:0;width:28px;height:1080px;background:var(--y)"></div>
<div style="position:absolute;left:390px;top:0;width:1530px;height:1000px;background:var(--y)"></div>
{photo('2.jpg', 70, 0, 660, 1000, '42% center')}
{dots(560, 830, 6, 3)}
{swirl(1500, 640, 1.0, '#E6B800', .5, 0)}
<div style="position:absolute;left:830px;top:150px;font-size:24px;font-weight:800;letter-spacing:4px">HAT1 FINANCIAL REPORTING · 2026</div>
<h1 style="position:absolute;left:826px;top:200px;font-size:112px;line-height:1.0">Liebherr Group</h1>
<div class="h" style="position:absolute;left:830px;top:330px;font-size:46px;line-height:1.15;max-width:1000px">Financial Reporting and<br>Investment Analysis 2022–2025</div>
<div style="position:absolute;left:830px;top:490px;width:960px;background:#fff;border-radius:18px;padding:26px 34px">
  <div style="font-size:19px;font-weight:800;letter-spacing:3px;opacity:.6">CENTRAL QUESTION</div>
  <div style="font-size:31px;font-weight:700;line-height:1.25;margin-top:6px">Should a long-term investor take a minority stake in Liebherr – and if not, why not yet?</div>
</div>
<div style="position:absolute;left:830px;top:735px;font-size:21px;font-weight:600">Benchmark: Caterpillar Inc. and the average of 105 listed US machinery companies</div>
<div style="position:absolute;left:830px;top:800px;font-size:20px;font-weight:800;letter-spacing:2px;opacity:.7">PRESENTED BY</div>
<div style="position:absolute;left:830px;top:830px;font-size:26px;font-weight:800;max-width:1000px;line-height:1.3">Simon Beermann · Adam Fliegel · Zofia Narkiewicz · Philipp Hoffmann · Zarah Gilmore Islam</div>
<div style="position:absolute;left:70px;top:1022px;font-size:19px;font-weight:600;color:var(--muted)">Fontys University of Applied Sciences, Venlo · International Finance and Control · Lecturer: Kim Verspeek</div>
</section>""")

# ---------------------------------------------------------------- 2 Executive summary
def kcard(x, kind, color, big, label, text):
    tagbg = {"Strength": "#E3F1E4", "Weakness": "#FBE3E3", "Accounting": "#FFF4C2"}[kind]
    tagfg = {"Strength": "#1E6B2A", "Weakness": "#A11B1B", "Accounting": "#6B5300"}[kind]
    return f"""<div class="card" style="left:{x}px;top:300px;width:400px;height:420px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10);border-top:10px solid {color}">
<span class="tag" style="background:{tagbg};color:{tagfg}">{kind}</span>
<div class="big" style="font-size:{76 if len(big)<9 else 62}px;margin-top:22px;white-space:nowrap">{big}</div>
<div style="font-size:24px;font-weight:800;margin-top:4px">{label}</div>
<div style="font-size:22px;line-height:1.35;margin-top:16px;color:#2B3540">{text}</div></div>"""

slides.append(frame(2, "Report, Executive summary and chapters 7–8; Excel workbook, sheet Dashboard", f"""
<div style="position:absolute;left:0;top:0;width:1920px;height:470px;background:var(--y)"></div>
{swirl(1540,-30)}{dots(1720,170)}
<div class="eyebrow">The answer first</div>
<h2 style="position:absolute;left:96px;top:72px;font-size:60px;line-height:1.08">Financially sound – but not yet an adequate return</h2>
<div style="position:absolute;left:98px;top:160px;font-size:27px;font-weight:600">Four findings decide the investment case</div>
{kcard(98,'Strength','#2E7D32','53.5 %','Equity ratio 2025','Cash and current financial assets cover current debt <b>2.6 times</b>.')}
{kcard(538,'Weakness','#C8102E','2.8 %','Operating margin 2025','Less than a fifth of Caterpillar (17.2 %) and the industry (15.9 %).')}
{kcard(978,'Weakness','#C8102E','−€176 m','Free cash flow 2025','Negative in three of four years – investment runs ahead of cash generation.')}
{kcard(1418,'Accounting','#FFCF00','1.6–2.8 %','Margin range in our tests','The measurable accounting effects point to a <b>weaker</b>, not a stronger result.')}
<div style="position:absolute;left:98px;top:760px;width:1720px;height:110px;background:var(--navy);border-radius:18px;color:#fff;display:flex;align-items:center;padding:0 44px;gap:34px">
  <div class="big" style="font-size:46px;color:var(--y);white-space:nowrap">Not yet.</div>
  <div style="font-size:27px;font-weight:600;line-height:1.3">Do not invest at present – reassess the case on the <b style="color:var(--y)">2026 financial statements</b>.</div>
</div>"""))

# ---------------------------------------------------------------- 3 Company & environment
def kpi(x, y, big, small, w=255):
    return f"""<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:135px;background:#fff;border-radius:14px;padding:18px 22px;border-top:6px solid var(--y)">
<div class="big" style="font-size:44px">{big}</div><div style="font-size:19px;font-weight:600;color:var(--muted);margin-top:2px">{small}</div></div>"""

slides.append(frame(3, "Report, chapters 2 and 3 (§3.1.1) and §5.7; Liebherr-International AG (2026); EUROCONSTRUCT (2026); European Central Bank (2026)", f"""
<div style="position:absolute;left:0;top:0;width:1150px;height:620px;background:var(--y)"></div>
{swirl(-60,430,.9,'#E6B800',.45,-10)}
<div class="eyebrow">Company and environment</div>
<h2 style="position:absolute;left:96px;top:72px;font-size:52px;line-height:1.1;width:1000px">Diversification kept Liebherr growing while construction weakened</h2>
{kpi(98,250,'€14,772 m','Revenue 2025, +1.0 %')}
{kpi(368,250,'55,963','Employees')}
{kpi(638,250,'13','Product segments')}
{kpi(908,250,'1949','Family-owned · Bulle (CH)',210)}
<div style="position:absolute;left:98px;top:425px;width:1020px">
  <div style="font-size:21px;font-weight:800;margin-bottom:10px">Revenue 2025 by sector</div>
  <div style="display:flex;height:64px;border-radius:10px;overflow:hidden;font-weight:800;font-size:24px">
    <div style="width:63.3%;background:var(--navy);color:#fff;display:flex;align-items:center;padding-left:20px">63.3 % · Construction & mining · −5.5 %</div>
    <div style="width:36.7%;background:#fff;display:flex;align-items:center;padding-left:18px">36.7 % · Other · +14.7 %</div>
  </div>
  <div style="font-size:19px;font-weight:600;margin-top:8px">€9,345 m vs. €5,427 m – components alone grew 35.5 %</div>
</div>
{photo('6.jpg', 1150, 0, 770, 620, '62% center')}
{dots(1180,40,5,3)}
<div style="position:absolute;left:98px;top:655px;width:1060px">
  <div class="h" style="font-size:28px;margin-bottom:16px">External pressures</div>
  <ul class="b">
   <li><b>Demand:</b> European construction output forecast to grow only about 2 % a year until 2028</li>
   <li><b>Prices and costs:</b> US tariffs and low-cost competitors – reported by Liebherr for its cranes</li>
   <li><b>Financing:</b> ECB main refinancing rate 2.65 % (Sept. 2026) – machines cost customers more to finance</li>
  </ul>
</div>
<div class="card" style="left:1220px;top:660px;width:600px;height:215px;background:var(--navy);color:#fff">
  <div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">LIEBHERR'S OWN OUTLOOK</div>
  <div style="font-size:23px;line-height:1.35;margin-top:10px">Orders at the start of 2026 above the previous year – further growth expected, but <b style="color:var(--y)">no significant upswing before 2027</b>. US tariff policy remains a risk.</div>
</div>"""))

# ---------------------------------------------------------------- 4 Competitive advantage
def adv(x, n, img, title, text, metric, mlabel, cost):
    return f"""<div class="card" style="left:{x}px;top:262px;width:420px;height:640px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.12);padding:0;overflow:hidden">
<div style="height:190px;background:url(img/{img}) center/cover"></div>
<div style="position:absolute;left:24px;top:166px;background:var(--y);border-radius:30px;padding:9px 22px;font-family:Arimo,Arial,sans-serif;font-weight:700;font-size:23px;box-shadow:0 3px 10px rgba(0,0,0,.15)">{title}</div>
<div style="padding:44px 28px 0"><div style="font-size:20px;line-height:1.35;color:#2B3540;height:82px">{text}</div>
<div class="big" style="font-size:50px;margin-top:6px">{metric}</div><div style="font-size:18.5px;font-weight:700;color:var(--muted);line-height:1.3">{mlabel}</div></div>
<div style="position:absolute;left:0;right:0;bottom:0;background:var(--light);padding:14px 28px;height:112px">
<div style="font-size:17px;font-weight:800;letter-spacing:2px;color:#A11B1B">THE PRICE</div>
<div style="font-size:20px;line-height:1.3;margin-top:4px">{cost}</div></div></div>"""

slides.append(frame(4, "Report §3.2–3.3, Appendix E (VRIO); Liebherr-International AG (2023–2026); Caterpillar Inc. (2026)", f"""
<div style="position:absolute;left:0;top:0;width:1920px;height:230px;background:var(--y)"></div>
{swirl(1560,-40,1.0)}{dots(1740,150)}
<div class="eyebrow">Business model and competitive strategy</div>
<h2 style="position:absolute;left:96px;top:72px;font-size:54px;line-height:1.08;width:1260px">How Liebherr creates competitive advantage</h2>
<div style="position:absolute;left:98px;top:158px;font-size:26px;font-weight:600;width:1260px">Differentiation in custom segments, scale in volume segments – financed by patient family capital</div>
{adv(96,1,'3.jpg','Diversified product portfolio','13 segments, from mining excavators to aerospace components, spread the market risk.','+14.7 %','other segments 2025, while construction & mining fell 5.5 %','Stabilises revenue, but does not raise the margin.')}
{adv(536,2,'canva_factory.jpg','Vertical integration','Key technologies built in-house; own sales and service companies instead of dealers.','29.1 %','PP&amp;E in % of revenue (Caterpillar 22.4 %)','Capital tied up in assets and stock – inventories 42.9 % of revenue.')}
{adv(976,3,'canva_loader.jpg','Innovation &amp; research','Research and development rose every year, fully expensed, financed from retained profit.','€708 m','R&amp;D 2025 = 4.8 % of revenue (Caterpillar 3.2 %)','Spending kept rising while operating profit fell 39 % in 2025.')}
<div class="card" style="left:1416px;top:262px;width:408px;height:640px;background:var(--navy);color:#fff;padding:34px 32px">
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:var(--y)">WHAT IT MEANS</div>
  <div class="h" style="font-size:34px;line-height:1.2;color:#fff;margin-top:14px">The advantage is real – but it sits in the asset base, not yet in the margin.</div>
  <div style="font-size:21px;line-height:1.4;margin-top:22px;opacity:.9">For the investor the question is not <i>whether</i> the advantage exists, but whether it is turned into returns.</div>
  <div style="position:absolute;left:32px;bottom:30px;right:32px;font-size:19px;line-height:1.35;color:var(--y);font-weight:700">Only €56 m of a €272 m profit was distributed in 2025.</div>
</div>
"""))

# ---------------------------------------------------------------- 4 Performance
slides.append(frame(4, "Report §5.2–5.3, Figures 1, 2a and J2; Excel workbook, sheets D4, D6, D10 and Dashboard. Caterpillar on the FIFO basis; industry = Damodaran (2026c), 2025 reference level", f"""
{band('Financial performance', 'Growth has stalled and the margin fell to 2.8 %', 'Revenue growth 11.5 % → 4.1 % → 1.0 % (2023–2025) · the falling return comes from profitability, not leverage')}
<div class="card" style="left:96px;top:250px;width:1110px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.08)">
  <div class="ctitle">Operating margin, in % of revenue</div>
  <div style="position:absolute;left:30px;top:90px">{C.margin_lines(1050,480)}</div>
</div>
<div class="card" style="left:1240px;top:250px;width:584px;height:290px;padding:22px 26px">
  <div class="ctitle">DuPont: why the return on equity fell</div>
  <div style="position:absolute;left:12px;top:44px">{C.dupont(560,240)}</div>
</div>
<div class="card" style="left:1240px;top:560px;width:584px;height:290px;padding:22px 26px">
  <div class="ctitle">Margin bridge 2024 → 2025</div>
  <div style="position:absolute;left:12px;top:46px">{C.bridge(560,240)}</div>
</div>
""", pill="<b>Investor lens</b> Each percentage point of margin is worth about €148 m of operating profit", pill_y=880))

# ---------------------------------------------------------------- 5 Accounting judgements
def acc(x, title, amount, sub, items, w=415, dark=False):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f"""<div class="card" style="left:{x}px;top:320px;width:{w}px;height:520px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.08);border-top:10px solid var(--y)">
<div style="font-size:20px;font-weight:800;letter-spacing:2px;color:var(--muted)">{title}</div>
<div class="big" style="font-size:58px;margin-top:6px">{amount}</div>
<div style="font-size:20px;font-weight:700;color:var(--muted);margin-bottom:18px">{sub}</div>
<ul class="b">{lis}</ul></div>"""

slides.append(frame(5, "Report §4.1–4.4, Appendix G (Table G2) and Appendix H (Table H1); Excel workbook, sheets C2 and D9", f"""
{band('Accounting analysis', 'Key figures rest on judgements we cannot verify', 'Most room for judgement: inventories, provisions and fixed assets – and one cost line without any note')}
<div style="position:absolute;left:96px;top:240px;display:flex;gap:14px">
 <span class="tag" style="background:var(--navy);color:#fff">Reporting limit</span>
 <span style="font-size:22px;font-weight:600;padding-top:4px">Summary statements only (ISA 810) · full audited statements not public · no segment note (IFRS 8 not applicable)</span>
</div>
{acc(96,'INVENTORIES · IAS 2','€6,341 m','36.3 % of total assets',['Overhead allocated at a “normal capacity” that is not defined','Allowance for obsolete stock not disclosed'])}
{acc(531,'PROVISIONS · IAS 37','€864 m','of which warranty €530 m',['Gross reversals rose from €90 m (2022) to €143 m (2025)','But the net charge stayed flat: €195 m → €194 m'])}
{acc(966,'PP&E · IAS 16','€4,304 m','25 % of total assets',['Depreciation 5.5 % of cost vs. 6.6 % at Caterpillar','Own work capitalised €317 m = 77 % of the operating result'])}
<div class="card" style="left:1401px;top:320px;width:423px;height:520px;background:var(--navy);color:#fff;border-top:10px solid var(--y)">
<div style="font-size:20px;font-weight:800;letter-spacing:2px;color:var(--y)">DISCLOSURE GAP</div>
<div class="big" style="font-size:58px;margin-top:6px;color:#fff">+€228 m</div>
<div style="font-size:20px;font-weight:700;opacity:.8;margin-bottom:18px">other operating expenses 2025 (+11.7 %)</div>
<ul class="b" style="color:#fff"><li>The largest cost increase of 2025 has no note at all</li><li>4 of 9 red-flag tests raised a flag</li></ul>
</div>
""", pill="<b>Investor lens</b> The 2025 operating result is not a reliable base for extrapolation", pill_y=876))

# ---------------------------------------------------------------- 6 Adjustments vs sensitivities
def box(x, y, w, h, top, big, bg="#fff", fg="var(--navy)"):
    return f"""<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{fg};border-radius:14px;padding:14px 18px;text-align:center">
<div style="font-size:18px;font-weight:700;opacity:.8">{top}</div><div class="big" style="font-size:36px;margin-top:4px">{big}</div></div>"""

slides.append(frame(6, "Report §4.4, §6.1, Table J9 and Table H3; Excel workbook, sheets C1 (block A), D9 and D11. Caterpillar figures in USD m, Liebherr in € m – never combined", f"""
{band('Accounting adjustments and sensitivities', 'Adjusting for comparability widens the gap', 'Actual adjustment (Caterpillar) vs. illustrative sensitivities (Liebherr)')}
<div class="card" style="left:96px;top:250px;width:830px;height:600px;background:var(--light)">
  <span class="tag" style="background:var(--navy);color:#fff">Actual adjustment · booked in the workbook</span>
  <div class="h" style="font-size:30px;margin-top:16px">Caterpillar: inventories restated LIFO → FIFO</div>
  <div style="font-size:21px;margin-top:6px;color:#2B3540">IAS 2 prohibits LIFO and Liebherr does not use it. The disclosed LIFO reserve makes the correction exact, not estimated.</div>
  {box(34,215,230,105,'Inventories (LIFO)','$18,135 m')}
  <div class="big" style="position:absolute;left:276px;top:240px;font-size:44px">+</div>
  {box(312,215,230,105,'LIFO reserve','$4,305 m','var(--y)')}
  <div class="big" style="position:absolute;left:554px;top:240px;font-size:44px">=</div>
  {box(590,215,210,105,'FIFO basis','$22,440 m','var(--navy)','#fff')}
  <div style="position:absolute;left:34px;top:350px;width:766px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px">
    <div style="background:#fff;border-radius:14px;padding:14px 16px"><div style="font-size:18px;font-weight:700;color:var(--muted)">Equity (before tax)</div><div class="big" style="font-size:30px">+$4,305 m</div></div>
    <div style="background:#fff;border-radius:14px;padding:14px 16px"><div style="font-size:18px;font-weight:700;color:var(--muted)">Operating profit 2025</div><div class="big" style="font-size:30px">+$441 m</div></div>
    <div style="background:#fff;border-radius:14px;padding:14px 16px"><div style="font-size:18px;font-weight:700;color:var(--muted)">Operating margin</div><div class="big" style="font-size:30px">16.5 → 17.2 %</div></div>
  </div>
  <div style="position:absolute;left:34px;top:478px;width:766px;font-size:21px;line-height:1.35"><b>Also reclassified:</b> Caterpillar's 2022 goodwill impairment of $925 m as non-recurring. At equal depreciation the gap would be up to <b>15.1 pp</b> instead of 14.4 pp.</div>
</div>
<div class="card" style="left:956px;top:250px;width:868px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.08)">
  <span class="tag" style="background:#E9EBEE;color:var(--cat)">Illustrative sensitivity · not booked</span>
  <div class="h" style="font-size:30px;margin-top:16px">Liebherr operating margin 2025 under the findings</div>
  <div style="position:absolute;left:34px;top:140px">{C.sensitivity(800,350)}</div>
  <div style="position:absolute;left:34px;top:500px;width:800px;font-size:20px;line-height:1.35;color:#2B3540">Own work capitalised cannot be measured. The equity ratio would still be <b>50.4 %</b> at Caterpillar's depreciation rate – the balance sheet strength holds.</div>
</div>
""", pill="<b>Investor lens</b> Accounting does not rescue the case – the reported 2.8 % is, if anything, flattered", pill_y=880))

# ---------------------------------------------------------------- 7 Financial position & cash
def mini(y, big, label, note):
    return f"""<div style="position:absolute;left:96px;top:{y}px;width:470px;height:150px;background:var(--light);border-radius:16px;padding:18px 24px;border-left:10px solid var(--y)">
<div class="big" style="font-size:48px">{big}</div><div style="font-size:21px;font-weight:800">{label}</div><div style="font-size:18px;color:var(--muted)">{note}</div></div>"""

slides.append(frame(7, "Report §5.5–5.6, Figures 3 and 4, Table 2; Excel workbook, sheets D3, D5, D7 and Dashboard; industry: Damodaran (2026b)", f"""
{band('Financial position and cash flow', 'A strong balance sheet is financing a cash shortfall', 'Liquidity and solvency are solid – but investment runs ahead of operating cash flow')}
{mini(250,'53.5 %','Equity ratio 2025','Bank and lease liabilities 23.7 % of capital vs. 39.3 % industry')}
{mini(420,'2.6×','Cash cover of current debt','€3,147 m cash and current financial assets vs. €1,215 m')}
{mini(590,'2.90×','Debt / EBITDA 2025','Up from 2.14 in 2024 – above the industry’s 2.30')}
<div class="card" style="left:600px;top:250px;width:740px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.08)">
  <div class="ctitle">Operating cash flow vs. capital expenditure, € m</div>
  <div class="legend" style="margin-left:-22px"><i style="background:var(--y)"></i>Operating cash flow<i style="background:var(--cat)"></i>Capital expenditure<i style="background:var(--navy);border-radius:50%"></i>Free cash flow</div>
  <div style="position:absolute;left:14px;top:110px">{C.cash_bars(710,470)}</div>
</div>
<div class="card" style="left:1370px;top:250px;width:454px;height:600px;background:var(--navy);color:#fff">
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:var(--y)">2022–2025 CUMULATIVE</div>
  <div style="font-size:23px;line-height:1.35;margin-top:10px">Capex <b>€2,427 m</b> vs. operating cash flow <b>€1,276 m</b> = <b style="color:var(--y)">190 %</b></div>
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:var(--y);margin-top:26px">NET FINANCIAL POSITION, € m</div>
  <div style="background:#fff;border-radius:14px;margin-top:10px;padding:4px 0">{C.nfp_line(406,210)}</div>
  <div style="font-size:21px;line-height:1.35;margin-top:16px">Covers the 2025 shortfall after distributions (€232 m) for only <b style="color:var(--y)">≈ 1.1 years</b>.</div>
</div>
""", pill="<b>Investor lens</b> Low risk of distress – but the cushion is shrinking", pill_y=880))

# ---------------------------------------------------------------- 8 Working capital
slides.append(frame(8, "Report §5.4, Figure 2b, Table J5; Excel workbook, sheets D3 (block E) and Dashboard; industry: Damodaran (2026e). Days on a revenue basis – a proxy, as Liebherr reports no cost of sales", f"""
{band('Working capital', 'Inventories tie up 42.9 % of revenue', '2.6 times the industry average – the cash conversion cycle is a revenue-based proxy')}
<div class="card" style="left:96px;top:250px;width:600px;height:600px;background:var(--light)">
  <div class="ctitle">Inventories in % of revenue, 2025</div>
  <div style="position:absolute;left:40px;top:90px">{C.inv_share(520,300)}</div>
  <div style="position:absolute;left:34px;top:410px;width:540px">
    <ul class="b"><li style="font-size:22px">Causes: in-house production, long order cycles, stock held by own sales companies</li>
    <li style="font-size:22px">Finished goods alone: €2,490 m</li></ul>
  </div>
</div>
<div class="card" style="left:726px;top:250px;width:1098px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.08)">
  <div style="display:flex;justify-content:space-between"><div class="ctitle">Working-capital days 2025 (revenue basis)</div>
  <div class="legend"><i style="background:var(--y)"></i>Liebherr<i style="background:var(--cat)"></i>Caterpillar</div></div>
  <div style="position:absolute;left:34px;top:80px">{C.wc_days(700,480)}</div>
  <div style="position:absolute;left:760px;top:120px;width:300px;height:400px;background:var(--y);border-radius:16px;padding:26px">
    <div style="font-size:19px;font-weight:800;letter-spacing:2px">THE LEVER</div>
    <div class="big" style="font-size:64px;margin-top:6px">€405 m</div>
    <div style="font-size:22px;line-height:1.35;margin-top:6px">released by a cycle <b>10 days shorter</b> (€40.5 m revenue a day)</div>
    <div style="font-size:21px;line-height:1.35;margin-top:16px;font-weight:700">… but only once. A lasting turnaround needs margin.</div>
  </div>
</div>
""", pill="<b>Investor lens</b> 77 days longer cash cycle than Caterpillar – limits Liebherr’s financial flexibility", pill_y=880))

# ---------------------------------------------------------------- 10 Investment assessment
def cond(x, n, title, status, ok=False):
    return f"""<div style="position:absolute;left:{x}px;top:470px;width:560px;height:200px;background:#fff;border-radius:18px;padding:22px 26px;box-shadow:0 6px 24px rgba(0,24,46,.10)">
<div style="display:flex;gap:16px;align-items:flex-start"><div style="min-width:52px;height:52px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:26px">{n}</div>
<div style="font-size:24px;font-weight:800;line-height:1.25">{title}</div></div>
<div style="position:absolute;left:26px;bottom:20px;right:26px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid var(--light);padding-top:12px">
<div style="font-size:21px;font-weight:600;color:var(--muted)">Status 2025</div>
<div style="font-size:23px;font-weight:800;color:#A11B1B">✗ {status}</div></div></div>"""

slides.append(frame(10, "Report §5.3, §5.7 and chapter 8, Table 3; Excel workbook, sheets D3, D10 and D11; benchmark: Damodaran (2026a)", f"""
<div style="position:absolute;left:0;top:0;width:1920px;height:420px;background:var(--y)"></div>
{photo('canva_crane_night.jpg', 1240, 0, 680, 420, 'center 30%')}
{dots(1180,40,3,3)}
<div class="eyebrow">Overall assessment and investment perspective</div>
<h2 style="position:absolute;left:96px;top:72px;font-size:56px;line-height:1.08;width:1100px">What would have to change: three conditions for a reassessment</h2>
<div style="position:absolute;left:98px;top:250px;width:1080px;font-size:25px;line-height:1.35;font-weight:600">Check them on the 2026 statements – a new assessment only if <b>all three</b> are met. In 2025 none of them is.</div>
{cond(96,1,'Operating margin of at least 3.9 % (four-year average)','2.8 %')}
{cond(680,2,'Free cash flow positive and, over time, covering distributions','−€176 m')}
{cond(1264,3,'Information rights: audited statements and other operating expenses','Not secured')}
<div class="card" style="left:96px;top:700px;width:860px;height:170px;background:var(--light);padding:20px 28px">
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:#1E6B2A">REWARD</div>
  <div style="font-size:22px;line-height:1.35;margin-top:6px">Resilient, diversified group · back to the 3.9 % average margin = <b>+€157 m</b> operating profit at 2025 revenue</div>
</div>
<div class="card" style="left:964px;top:700px;width:860px;height:170px;background:var(--navy);color:#fff;padding:20px 28px">
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:var(--y)">RISK AND LIMITS</div>
  <div style="font-size:22px;line-height:1.35;margin-top:6px">ROCE 3.5 % (pre-tax) vs. 7.70 % benchmark – needs a margin of ~6–8 % · minority stake: little influence, low payout, hard to sell</div>
</div>
<div style="position:absolute;left:98px;top:885px;font-size:19px;color:var(--muted);font-weight:600">Even then: meeting the conditions triggers a new analysis, not a purchase – a minority stake in an unlisted group would only make sense at a discounted price.</div>
"""))

# ---------------------------------------------------------------- 11 Conclusion
def take(y, n, head, text):
    return f"""<div style="position:absolute;left:96px;top:{y}px;width:1000px;display:flex;gap:22px">
<div class="big" style="min-width:70px;height:70px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-size:34px">{n}</div>
<div><div style="font-size:27px;font-weight:800">{head}</div><div style="font-size:22px;line-height:1.35;color:#2B3540;margin-top:4px">{text}</div></div></div>"""

slides.append(frame(11, None, f"""
{photo('1.jpg', 0, 0, 760, 1058, 'center')}
<div style="position:absolute;left:760px;top:0;width:1160px;height:300px;background:var(--y)"></div>
{swirl(1580,40,.8,'#E6B800',.5)}{dots(1460,230,5,2)}
<div class="eyebrow" style="left:840px">Conclusion</div>
<h2 style="position:absolute;left:838px;top:74px;font-size:66px;line-height:1.05">Financially strong.<br>Operationally challenged.</h2>
<div style="position:absolute;left:744px;top:340px;width:1100px;height:450px">
{take(0,1,'The balance sheet is strong – and stays strong','53.5 % equity ratio and 2.6× cash cover; still ≈ 50 % equity ratio in our depreciation sensitivity.')}
{take(150,2,'Returns and cash generation are too weak','2.8 % margin, 12.5–16.2 pp below Caterpillar in every year; free cash flow negative in 3 of 4 years.')}
{take(300,3,'The accounting sharpens the verdict','The measured effects point to a margin of 1.6–2.8 %, and key estimates cannot be verified from outside.')}
</div>
<div style="position:absolute;left:840px;top:812px;width:990px;background:var(--navy);color:#fff;border-radius:18px;padding:26px 34px">
<div style="font-size:30px;font-weight:800;line-height:1.25">Not yet: the investor should see the turn in the figures <span style="color:var(--y)">before</span> committing capital.</div></div>
""").replace('<div class="src">', '<div class="src" style="left:840px">'))

# ---------------------------------------------------------------- 12 Thank you
slides.append(f"""<section class="slide">
<div style="position:absolute;left:0;top:0;width:1920px;height:1080px;background:var(--y)"></div>
{photo('9.jpg', 70, 40, 780, 900, '38% center')}
<div style="position:absolute;left:0;top:960px;width:1920px;height:120px;background:#fff"></div>
{swirl(1520,-30,1.0,'#E6B800',.5)}{dots(1700,760,5,3)}
<h1 style="position:absolute;left:960px;top:250px;font-size:200px;line-height:1;letter-spacing:-4px">Thank<br>you.</h1>
<div style="position:absolute;left:96px;top:995px;font-size:22px;font-weight:700">Simon Beermann · Adam Fliegel · Zofia Narkiewicz · Philipp Hoffmann · Zarah Gilmore Islam &nbsp;·&nbsp; HAT1 Financial Reporting · Fontys Venlo</div>
</section>""")

from notes import NOTES as notes
import re as _re
slides = [_re.sub(r"(\d) %", "\\1&nbsp;%", x) for x in slides]
slides = [_re.sub(r"(\d) (m|pp|bn)\b", "\\1&nbsp;\\2", x) for x in slides]
doc = f'<!doctype html><html><head><meta charset="utf-8"><title>Liebherr Group Investment Analysis</title><style>{CSS}</style></head><body>{"".join(slides)}</body></html>'
(BUILD / "deck.html").write_text(doc)

# speaker notes document
rows = []
for i, (t, d, txt) in enumerate(notes, 1):
    paras = "".join(f"<p>{html.escape(p)}</p>" for p in txt.split("\n\n"))
    rows.append(f'<section class="np"><div class="hd"><span class="n">{i:02d}</span><span class="t">{html.escape(t)}</span><span class="d">{d}</span></div>'
                f'<img src="shots/s{i:02d}.png"><div class="tx">{paras}</div></section>')
NCSS = FONTS + """
@page{size:A4 landscape;margin:12mm}
body{font-family:Assistant,sans-serif;color:#00182E}
.np{page-break-after:always;display:grid;grid-template-columns:52% 1fr;grid-template-rows:auto 1fr;gap:6mm 8mm;height:178mm;overflow:hidden}
.np:last-child{page-break-after:auto}
.hd{grid-column:1/3;display:flex;align-items:center;gap:4mm;border-bottom:3px solid #FFCF00;padding-bottom:2mm}
.n{background:#FFCF00;font-weight:800;padding:1mm 3mm;border-radius:2mm;font-size:13pt}
.t{font-family:Arimo,sans-serif;font-weight:700;font-size:16pt;flex:1}
.d{font-weight:800;font-size:12pt;color:#5E6873}
img{width:100%;border:1px solid #D0D3D8}
.tx p{font-size:11.5pt;line-height:1.45;margin:0 0 3mm}
.cover h1{font-family:Arimo;font-size:26pt;margin:20mm 0 4mm}
"""
total = sum(int(d.split(":")[0]) * 60 + int(d.split(":")[1]) for _, d, _ in notes if ":" in d)
words = sum(len(t.split()) for _, _, t in notes[:-1])
cover = (f'<section class="np cover" style="display:block"><h1>Liebherr Group – Speaker notes</h1>'
         f'<p style="font-size:13pt">HAT1 Financial Reporting · 12 slides · planned speaking time {total//60}:{total%60:02d} min · {words} words of notes (≈ 130 words per minute)</p>'
         '<p style="font-size:12pt;margin-top:6mm">Red line: <b>Should a long-term investor take a minority stake in Liebherr – and if not, why not yet?</b><br>'
         'Answer first (slide 2) → why: company and model (3) → performance (4) → can we trust the figures? (5–6) → position, cash and working capital (7–8) → '
         'how the workbook supports it (9) → conditions for reassessment (10) → conclusion (11).</p>'
         '<p style="font-size:11pt;color:#5E6873;margin-top:6mm">All figures are taken from the report and the Excel workbook. Actual adjustments (Caterpillar LIFO → FIFO, 2022 goodwill reclassification) are kept separate from illustrative sensitivities (provision charge, depreciation rate).</p></section>')
(BUILD / "notes.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><title>Liebherr Speaker Notes</title><style>{NCSS}</style></head><body>{cover}{"".join(rows)}</body></html>')
import json
(BUILD / "notes.json").write_text(json.dumps(notes, indent=1, ensure_ascii=False))
print("ok", len(slides), "slides; planned", total, "s;", words, "words")
