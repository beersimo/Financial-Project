"""Back side for the moderator cards: Liebherr logo centred on every card (same 210 x 99 mm grid).

Usage: python3 cards_back.py NUMBER_OF_CARDS OUT_PDF [white|yellow] [LOGO_PNG]
  white  – black logo on white (after the black-on-white logo image)
  yellow – black logo on Liebherr yellow #F9D90A (after the yellow logo image)
"""
import base64, subprocess, sys, pathlib
n, out = int(sys.argv[1]), sys.argv[2]
style = sys.argv[3] if len(sys.argv) > 3 else "white"
logo = pathlib.Path(sys.argv[4]) if len(sys.argv) > 4 else None
bg = {"white": "#FFFFFF", "yellow": "#F9D90A"}[style]
if logo:
    mark = f'<img src="data:image/png;base64,{base64.b64encode(logo.read_bytes()).decode()}" style="width:150mm">'
else:
    mark = '<span style="font-family:Arimo,Arial,sans-serif;font-weight:700;font-size:44pt;letter-spacing:4pt;color:#000">LIEBHERR</span>'
pages = [min(3, n - j) for j in range(0, n, 3)]
card = f'<div class="card">{mark}</div>'
sep = '<div class="sep"></div>' if style == "yellow" else ""
doc = ('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:A4 portrait;margin:0}*{margin:0;padding:0;box-sizing:border-box}'
       'html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact}'
       '.page{width:210mm;height:297mm;page-break-after:always}.page:last-child{page-break-after:auto}'
       f'.card{{width:210mm;height:99mm;display:flex;align-items:center;justify-content:center;background:{bg}}}'
       '.sep{height:0}</style></head><body>'
       + "".join(f'<div class="page">{card * k}</div>' for k in pages) + '</body></html>')
src = pathlib.Path(out).with_suffix(".html")
src.write_text(doc)
js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();"
      f"await p.goto('file://{src}');await p.pdf({{path:'{out}',preferCSSPageSize:true,printBackground:true}});await b.close();}})();")
subprocess.run(["node", "-e", js], check=True, cwd=str(pathlib.Path(__file__).parent))
src.unlink()
