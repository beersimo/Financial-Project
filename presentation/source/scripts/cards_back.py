"""Back side for the moderator cards: 'LIEBHERR' in black, centred on every card (same 99 mm grid).

Usage: python3 cards_back.py NUMBER_OF_CARDS OUT_PDF
"""
import subprocess, sys, pathlib
n, out = int(sys.argv[1]), sys.argv[2]
pages = [min(3, n - j) for j in range(0, n, 3)]
card = '<div class="card"><span>LIEBHERR</span></div>'
doc = ('<!doctype html><html><head><meta charset="utf-8"><style>@page{size:A4 portrait;margin:0}*{margin:0;padding:0;box-sizing:border-box}'
       '.page{width:210mm;height:297mm;page-break-after:always}.page:last-child{page-break-after:auto}'
       '.card{width:210mm;height:99mm;display:flex;align-items:center;justify-content:center}'
       '.card span{font-family:Arimo,Arial,sans-serif;font-weight:700;font-size:44pt;letter-spacing:4pt;color:#000}</style></head><body>'
       + "".join(f'<div class="page">{card * k}</div>' for k in pages) + '</body></html>')
src = pathlib.Path(out).with_suffix(".html")
src.write_text(doc)
js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();"
      f"await p.goto('file://{src}');await p.pdf({{path:'{out}',preferCSSPageSize:true}});await b.close();}})();")
subprocess.run(["node", "-e", js], check=True, cwd=str(pathlib.Path(__file__).parent))
src.unlink()
