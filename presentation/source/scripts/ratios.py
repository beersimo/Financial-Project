"""Backup section A: ratios with formulas, what-if logic, provisions, sensitivities, long list and workbook.

All figures come from the Excel workbook (sheets A2, D3, D4, D7, D9, D11) and the report (Tables G1, G2, H1, H2, J13, J14).
"""

SEC = "A | Ratios and workbook"

UP = '<span class="arw" style="background:var(--y);color:var(--navy)">▲</span>'
DN = '<span class="arw" style="background:var(--navy);color:#fff">▼</span>'
NO = '<span class="arw" style="background:#E9EBEE;color:#8A939C">–</span>'

CSS = """<style>
.rt{border-collapse:collapse;width:100%;font-size:21px;color:var(--navy)}
.rt th{background:var(--navy);color:#fff;font-size:17px;letter-spacing:1.5px;text-transform:uppercase;text-align:left;padding:10px 14px}
.rt th.l{background:var(--y);color:var(--navy);text-align:center}.rt th.c{background:var(--cat);text-align:center}
.rt td{padding:8px 14px;border-bottom:1px solid #E3E5E8;vertical-align:middle}
.rt td.n{text-align:center;font-weight:800;white-space:nowrap}.rt td.l{background:#FFF8D6}
.rt td.g{font-size:16px;font-weight:800;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted);background:var(--light);border-right:2px solid #fff;width:150px}
.rt td.f{font-family:'JetBrains Mono',Consolas,monospace;font-size:17.5px;color:#2B3540}
.arw{display:inline-flex;align-items:center;justify-content:center;width:34px;height:30px;border-radius:8px;font-size:17px;font-weight:800}
</style>"""


def scope(cls, rules):
    """Table overrides for one slide only (all slides share one document, so global rules would leak)."""
    return "<style>" + "".join(f".{cls} {sel}{{{r}}}" for sel, r in rules) + "</style>"


def add_ratios(slides, frame, hdr, card, ul):
    def box(x, y, w, h, inner, bg="#fff", shadow=True):
        sh = "box-shadow:0 6px 24px rgba(0,24,46,.10);" if shadow else ""
        fg = "#fff" if bg == "var(--navy)" else "var(--navy)"
        return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{fg};border-radius:16px;{sh}padding:22px 26px">{inner}</div>'

    def note(y, text, x=96, w=1728):
        return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;font-size:18px;line-height:1.4;color:var(--muted)">{text}</div>'

    def pill(text, y=880):
        return f'<div class="pill" style="top:{y}px">{text}</div>'

    # ------------------------------------------------------------- A1 Ratios I: profitability and returns
    rows = [('Profitability<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">margins</div>', [("Operating margin", "EBIT / revenue", "2.8 %", "17.2 %"),
                               ("Pre-tax margin", "Profit before tax / revenue", "3.0 %", "17.9 %"),
                               ("Net profit margin", "Profit after tax / revenue", "1.8 %", "13.8 %"),
                               ("EBITDA margin", "EBITDA / revenue", "6.8 %", "19.8 %")]),
            ('Profitability<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">returns on capital</div>', [("ROA", "EBIT / average total assets", "2.4 %", "11.9 %"),
                         ("ROCE", "EBIT / (avg. equity + avg. non-current debt)", "3.5 %", "20.2 %"),
                         ("ROE", "Profit after tax / average equity", "3.0 %", "38.1 %*"),
                         ("Pre-tax ROE", "Profit before tax / average equity", "4.8 %", "49.4 %")])]
    trs = ""
    for g, items in rows:
        for i, (r, f, l, c) in enumerate(items):
            gcell = f'<td class="g" rowspan="{len(items)}">{g}</td>' if i == 0 else ""
            trs += f'<tr>{gcell}<td style="font-weight:700">{r}</td><td class="f">{f}</td><td class="n l">{l}</td><td class="n">{c}</td></tr>'
    table = (f'<table class="rt"><tr><th>Group</th><th>Ratio</th><th>Formula</th><th class="l">Liebherr</th><th class="c">Caterpillar</th></tr>{trs}</table>')
    dupont = (
        '<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">DUPONT</div>'
        '<div class="h" style="font-size:28px;color:#fff;margin:8px 0 14px;line-height:1.25">ROE = net margin × asset turnover × leverage</div>'
        '<div style="font-size:19px;opacity:.85;margin-bottom:8px">leverage = average total assets / average equity</div>'
        '<div style="font-size:19px;margin-bottom:14px">= <b style="color:var(--y)">profitability</b> × <b style="color:var(--y)">efficiency</b> × <b style="color:var(--y)">leverage</b> – the ratio groups of slides 14 and 15</div>'
        '<table style="width:100%;border-collapse:collapse;font-size:22px;color:#fff;margin-top:6px">'
        '<tr style="color:var(--y);font-size:16px;letter-spacing:1px"><td></td><td>MARGIN</td><td>TURNOVER</td><td>LEVERAGE</td><td>ROE</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">2025</td><td>1.84 %</td><td>× 0.85</td><td>× 1.89</td><td style="font-weight:800">3.0 %</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">pre-tax</td><td>2.96 %</td><td>× 0.85</td><td>× 1.89</td><td style="font-weight:800">4.8 %</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">2023 pre-tax</td><td>4.76 %</td><td>× 0.88</td><td>× 1.81</td><td style="font-weight:800">7.6 %</td></tr></table>'
        '<div style="font-size:20px;line-height:1.4;margin-top:20px;border-top:1px solid rgba(255,255,255,.2);padding-top:16px">'
        'Leverage works on ROE, <b style="color:var(--y)">not on the EBIT margin</b> – EBIT is measured before interest.</div>')
    slides.append(frame(0, "Excel workbook, sheets D3 (blocks C and D) and D4; Report §5.3, Table J14. 2025; Caterpillar on the FIFO basis",
        CSS + scope("t14", [(".rt", "font-size:22px"), (".rt td", "padding:12px 14px"), (".rt td.f", "font-size:18.5px"), ("td.g", "width:170px;font-size:19px;color:var(--navy)")]) + hdr(SEC, "Profitability: returns are low because the margin is low", "Margins and returns on capital – formula, Liebherr and Caterpillar, 2025") +
        f'<div class="t14" style="position:absolute;left:96px;top:240px;width:1130px">{table}</div>' +
        box(1256, 240, 568, 640, dupont, "var(--navy)", False) +
        note(820, "* Not comparable – treasury shares reduce Caterpillar's equity. ROA is measured on EBIT,<br>because Liebherr's interest expense is not disclosed.", w=1130)))

    # ------------------------------------------------------------- A2 Ratios II: utilisation, working capital, liquidity, solvency
    rows = [('Efficiency<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">asset utilisation · working capital</div>', [
                ("Asset turnover", "Revenue / average total assets", "0.85", "0.69"),
                ("Fixed asset turnover", "Revenue / average PP&amp;E", "3.49", "4.74"),
                ("Days inventory outstanding", "Avg. inventories / revenue × 365", "157.5", "116.5"),
                ("Days sales outstanding", "Avg. receivables / revenue × 365", "73.8", "54.5"),
                ("Days payables outstanding", "Avg. payables / revenue × 365", "28.6", "44.9"),
                ("Cash conversion cycle", "DIO + DSO − DPO", "202.7", "126.1")]),
            ('Leverage<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">solvency</div>', [
                ("Equity ratio", "Equity / total assets", "53.5 %", "24.9 %"),
                ("Leverage (DuPont)", "Avg. total assets / avg. equity", "1.89", "3.97"),
                ("Debt / equity", "Debt incl. pensions / equity", "0.40", "1.84"),
                ("Debt / capital", "Bank + lease liab. / (those + equity)", "23.7 %", "64.8 %"),
                ("Debt / EBITDA", "Bank + lease liabilities / EBITDA", "2.90", "3.52")]),
            ('Liquidity<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">short term</div>', [
                ("Current ratio", "Current assets / current liabilities", "2.31", "1.55"),
                ("Quick ratio", "(Current assets − inventories) / current liab.", "1.16", "0.94"),
                ("Cash cover", "Cash + current fin. assets / current debt", "2.6×", "–")])]
    trs = ""
    for g, items in rows:
        for i, (r, f, l, c) in enumerate(items):
            gcell = f'<td class="g" rowspan="{len(items)}">{g}</td>' if i == 0 else ""
            trs += f'<tr>{gcell}<td style="font-weight:700">{r}</td><td class="f">{f}</td><td class="n l">{l}</td><td class="n">{c}</td></tr>'
    table = (f'<table class="rt" style="font-size:20px"><tr><th>Group</th><th>Ratio</th><th>Formula</th><th class="l">Liebherr</th><th class="c">Caterpillar</th></tr>{trs}</table>')
    slides.append(frame(0, "Excel workbook, sheets D3 (blocks D, E, G, H), D4 and D7; Report Tables J5 and J14. 2025; days on average balances; Caterpillar on the FIFO basis",
        scope("t15", [(".rt", "font-size:20px"), (".rt td", "padding:8px 14px"), (".rt td.f", "font-size:17px"), ("td.g", "width:190px;font-size:19px;color:var(--navy)")]) + hdr(SEC, "Efficiency, leverage, liquidity: slow capital, solid finance", "How capital is used, how it is financed and how liquid Liebherr is – 2025") +
        f'<div class="t15" style="position:absolute;left:96px;top:236px;width:1310px">{table}</div>' +
        f'<div style="position:absolute;left:96px;top:852px;width:1728px;height:150px;background:var(--navy);border-radius:16px;display:flex;align-items:center;padding:0 8px"><div style="flex:1;padding:0 22px;"><div style="font-size:19px;font-weight:800;letter-spacing:1.5px;color:var(--y);text-transform:uppercase">Profitability</div><div style="font-size:20px;line-height:1.35;color:#fff;margin-top:6px">How much profit a company earns – on its revenue and on the capital it employs.</div></div><div style="flex:1;padding:0 22px;border-left:1px solid rgba(255,255,255,.25);"><div style="font-size:19px;font-weight:800;letter-spacing:1.5px;color:var(--y);text-transform:uppercase">Efficiency</div><div style="font-size:20px;line-height:1.35;color:#fff;margin-top:6px">How well a company uses its assets and working capital to generate revenue.</div></div><div style="flex:1;padding:0 22px;border-left:1px solid rgba(255,255,255,.25);"><div style="font-size:19px;font-weight:800;letter-spacing:1.5px;color:var(--y);text-transform:uppercase">Leverage</div><div style="font-size:20px;line-height:1.35;color:#fff;margin-top:6px">How strongly a company uses debt relative to its equity to finance its assets.</div></div><div style="flex:1;padding:0 22px;border-left:1px solid rgba(255,255,255,.25);"><div style="font-size:19px;font-weight:800;letter-spacing:1.5px;color:var(--y);text-transform:uppercase">Liquidity</div><div style="font-size:20px;line-height:1.35;color:#fff;margin-top:6px">Whether a company can pay its short-term obligations from its short-term assets.</div></div></div>' +
        box(1436, 236, 388, 596,
            '<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">READ WITH CARE</div>'
            '<div style="font-size:19.5px;line-height:1.4;margin-top:12px;color:#fff">'
            '<b style="color:var(--y)">Days = efficiency, but they drive liquidity:</b> 203 days of revenue must be financed.<br><br>'
            '<b style="color:var(--y)">Revenue basis:</b> Liebherr reports no cost of sales; on its own cost basis DIO would be 299 days – not comparable.<br><br>'
            '<b style="color:var(--y)">Two debt measures:</b> “debt” includes pensions (€3,714 m); bank and lease liabilities (€2,898 m) match the Damodaran benchmark.<br><br>'
            '<b style="color:var(--y)">Interest cover:</b> not computable – no interest expense disclosed. Indicator: operating profit / interest paid 3.90.</div>',
            "var(--navy)", False)))

    # ------------------------------------------------------------- A2b Cash flow, payout and growth ratios
    rows = [("Cash flow", "converting profit into cash", [
                ("Cash conversion", "Operating cash flow / EBITDA", "53.0 %", "87.5 %"),
                ("Capex / depreciation", "Capex / depreciation and amortisation", "1.20", "1.90"),
                ("OCF / capex", "Operating cash flow / capex", "0.75", "2.74"),
                ("Free cash flow", "Operating cash flow − capex (€ m / $ m)", "−176", "7,453"),
                ("FCF margin", "Free cash flow / revenue", "−1.2 %", "11.0 %")]),
            ("Payout and growth", "what is left to grow with", [
                ("Revenue growth", "Revenue / prior-year revenue − 1", "1.0 %", "4.3 %"),
                ("Payout ratio", "(Dividends + buy-backs) / profit after tax", "20.6 %", "85.2 %"),
                ("Sustainable growth rate", "ROE × (1 − payout ratio)", "2.4 %", "5.7 %")])]
    trs = ""
    for g, sub, items in rows:
        for i, (r, f, l, c) in enumerate(items):
            gcell = f'<td class="g" rowspan="{len(items)}">{g}<div style="font-size:15px;letter-spacing:.3px;text-transform:none;font-weight:600;margin-top:4px;color:#5E6873">{sub}</div></td>' if i == 0 else ""
            trs += f'<tr>{gcell}<td style="font-weight:700">{r}</td><td class="f">{f}</td><td class="n l">{l}</td><td class="n">{c}</td></tr>'
    table = (f'<table class="rt"><tr><th>Group</th><th>Ratio</th><th>Formula</th><th class="l">Liebherr</th><th class="c">Caterpillar</th></tr>{trs}</table>')
    slides.append(frame(0, "Excel workbook, sheets D5 (rows 20–25), D7 and D8 (rows 51–52); Report §5.3 and §5.6. 2025; Caterpillar capex incl. leased equipment",
        scope("t16", [(".rt", "font-size:22px"), (".rt td", "padding:15px 14px"), (".rt td.f", "font-size:18.5px"), ("td.g", "width:190px;font-size:19px;color:var(--navy)")]) +
        hdr(SEC, "Cash flow and growth: profit does not turn into cash", "Cash flow, payout and growth ratios – 2025") +
        f'<div class="t16" style="position:absolute;left:96px;top:240px;width:1270px">{table}</div>' +
        box(1396, 240, 428, 620,
            '<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">READ WITH CARE</div>'
            '<div style="font-size:21px;line-height:1.45;margin-top:14px;color:#fff">'
            '<b style="color:var(--y)">Rental fleet counted once:</b> its investment sits inside operating cash flow, not in capex.<br><br>'
            '<b style="color:var(--y)">Two "cash conversions":</b> OCF / EBITDA (53.0 %) is not the cash conversion <i>cycle</i> (202.7 days).<br><br>'
            '<b style="color:var(--y)">Sustainable growth 2.4 %:</b> faster growth needs better returns, less capital or outside money.</div>',
            "var(--navy)", False)))

    # ------------------------------------------------------------- A3 From workbook to ratio (sheet D3, real cell formulas)
    rows = [(7, "Revenue", "14,772", "='B1 Income statement by nature'!B5"),
            (8, "Operating profit (EBIT)", "413", "='C1 Accounting adjustments'!B30"),
            (10, "Profit after tax", "272", "='B1 Income statement by nature'!B18+'C1…'!B27"),
            (14, "Total equity", "9,354", "='C1 Accounting adjustments'!B21"),
            (16, "Inventories", "6,341", "='C1 Accounting adjustments'!B13"),
            (19, "Current assets", "12,709", "='B2 Restructured balance sheet'!B17+'C1…'!B12"),
            (20, "Current liabilities", "5,498", "='B2 Restructured balance sheet'!B33"),
            (27, "Average total equity", "9,128", "=(B14+C14)/2"),
            (29, "Average inventories", "6,373", "=(B16+C16)/2"),
            (35, "Operating margin", "2.80 %", "=B8/B7"),
            (40, "Return on equity (ROE)", "2.98 %", "=B10/B27"),
            (49, "Days inventory outstanding", "157.5", "=B29/B7*365"),
            (60, "Current ratio", "2.31", "=B19/B20")]
    hl = {40: "#FFE680", 60: "#CDE8FF", 49: "#D6F0D0"}
    grid = ('<div style="font-family:Arial,sans-serif;font-size:22px;border:1px solid #C6C6C6;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.12)">'
            '<div style="background:#217346;color:#fff;font-size:16px;font-weight:700;padding:6px 12px">Liebherr-Caterpillar-Restructured-financial-statements.xlsx · sheet D3 Ratios</div>'
            '<div style="display:flex;border-bottom:1px solid #C6C6C6;font-size:17px"><div style="width:70px;padding:6px 10px;border-right:1px solid #C6C6C6;color:#555">B40</div>'
            '<div style="padding:6px 12px;font-style:italic;color:#555">fx</div><div style="padding:6px 4px;font-family:Consolas,monospace">=B10/B27</div></div>'
            '<table style="border-collapse:collapse;width:100%">'
            '<tr style="background:#F3F3F3;color:#555;font-size:15px;text-align:center"><td style="width:46px;border:1px solid #D4D4D4"></td><td style="border:1px solid #D4D4D4">A</td>'
            '<td style="width:120px;border:1px solid #D4D4D4">B · 2025</td><td style="width:430px;border:1px solid #D4D4D4">formula in column B</td></tr>')
    for r, lab, v, f in rows:
        bg = hl.get(r, "#fff")
        grid += (f'<tr><td style="background:#F3F3F3;color:#555;font-size:15px;text-align:center;border:1px solid #D4D4D4">{r}</td>'
                 f'<td style="padding:9px 12px;border:1px solid #E1E1E1">{lab}</td>'
                 f'<td style="padding:9px 12px;border:1px solid #E1E1E1;text-align:right;background:{bg};{"font-weight:700;outline:2px solid #217346" if r == 40 else ""}">{v}</td>'
                 f'<td style="padding:9px 12px;border:1px solid #E1E1E1;font-family:Consolas,monospace;font-size:16px;color:#2B3540">{f}</td></tr>')
    grid += "</table></div>"
    calc = [("#FFE680", "Return on equity", "=B10/B27", "272 / 9,128", "3.0 %"),
            ("#D6F0D0", "Days inventory outstanding", "=B29/B7*365", "6,373 / 14,772 × 365", "157.5 days"),
            ("#CDE8FF", "Current ratio", "=B19/B20", "12,709 / 5,498", "2.31")]
    cc = "".join(f'<div style="background:#fff;border-radius:14px;box-shadow:0 6px 24px rgba(0,24,46,.10);padding:22px 24px;margin-bottom:22px;border-left:12px solid {c}">'
                 f'<div style="font-size:20px;font-weight:800">{n} <span style="font-family:Consolas,monospace;font-size:17px;font-weight:400;color:var(--muted)">{f}</span></div>'
                 f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-top:4px"><span style="font-size:21px">{x}</span>'
                 f'<span class="big" style="font-size:36px">{r}</span></div></div>' for c, n, f, x, r in calc)
    slides.append(frame(0, "Excel workbook, sheet D3 Ratios (cell formulas as in the file), column B = Liebherr 2025, € m; checks on sheet E2",
        hdr(SEC, "From workbook to ratio: every figure is a formula", "Excerpt of sheet D3 – inputs link to the recast statements, ratios link to the inputs") +
        f'<div style="position:absolute;left:96px;top:236px;width:1110px">{grid}</div>' +
        f'<div style="position:absolute;left:1236px;top:236px;width:588px">{cc}'
        f'<div style="background:#1E6B2A;color:#fff;border-radius:14px;padding:16px 22px"><span class="big" style="font-size:40px;color:#fff">0</span>'
        f'<span style="font-size:20px;font-weight:700;margin-left:12px">open differences on sheet E2</span>'
        f'<div style="font-size:18px;line-height:1.35;margin-top:4px;opacity:.9">Inputs come from the recast statements B1/B2 and the adjustments on C1 – nothing is typed in.</div></div></div>'))

    # ------------------------------------------------------------- A3 What-if I: balance sheet and liquidity
    wi = [("Suppliers paid in cash", f"Current ratio {UP} &nbsp; Cash {DN}",
           "Both sides fall by the same amount, so a ratio above 1 rises: €500 m paid → 2.31 to 2.44 (illustration)."),
          ("Inventory write-down", f"EBIT {DN} &nbsp; Current ratio {DN} &nbsp; DIO {DN}",
           "The days <b>look</b> better while the position is weaker – the allowance is not disclosed."),
          ("New bank debt for capex", f"Equity ratio {DN} &nbsp; Debt/EBITDA {UP} &nbsp; Leverage {UP}",
           "EBIT margin unchanged; net margin falls through interest. ROE rises only if the return beats the interest rate."),
          ("Cash conversion cycle −10 days", f"Cash {UP} &nbsp; Margin {NO}",
           "Releases about €405 m once (€40.5 m revenue a day) – not a recurring improvement."),
          ("Receivables collected faster", f"DSO {DN} &nbsp; OCF {UP} &nbsp; Current ratio {NO}",
           "Cash replaces receivables inside current assets, so liquidity ratios barely move.")]
    rw = "".join(
        f'<div style="position:absolute;left:96px;top:{240 + i * 122}px;width:1728px;height:108px;background:#fff;border-radius:14px;box-shadow:0 4px 16px rgba(0,24,46,.08);display:flex;align-items:center">'
        f'<div style="width:400px;padding-left:28px" class="h"><span style="font-size:26px">{e}</span></div>'
        f'<div style="width:540px;font-size:20px;font-weight:700">{eff}</div>'
        f'<div style="flex:1;font-size:21px;line-height:1.35;padding-right:28px">{r}</div></div>' for i, (e, eff, r) in enumerate(wi))
    slides.append(frame(0, "Report §5.4–5.5; Excel workbook, sheets D3 and D7. Directions are logical consequences; the €500 m case is an illustration on 2025 balances",
        hdr(SEC, "What-if I: direction matters more than the formula", "Balance sheet and liquidity – what happens to the ratios") + rw +
        pill("<b>Investor lens</b> A better ratio is not always a better company")))

    # ------------------------------------------------------------- A4 What-if II: accounting choices
    rows = [("Provision addition", DN, DN, NO, "Expense now – the obligation is estimated"),
            ("Provision usage (utilisation)", NO, NO, DN, "Obligation settled – no profit effect"),
            ("Provision reversal (release)", UP, UP, NO, "Estimate no longer needed – profit without cash"),
            ("Slower depreciation (longer life)", UP, UP, NO, "Liebherr 5.5 % vs. Caterpillar 6.6 % of cost"),
            ("More own work capitalised", UP + " now", UP, NO, "€317 m = 77 % of 2025 EBIT; returns as depreciation"),
            ("LIFO → FIFO, rising prices (CAT)", UP, UP, NO, "+$441 m EBIT, +$4,305 m equity before tax")]
    trs = "".join(f'<tr><td style="font-weight:700;font-size:24px">{a}</td><td class="n">{b}</td><td class="n">{c}</td><td class="n">{d}</td><td>{e}</td></tr>' for a, b, c, d, e in rows)
    table = (f'<table class="rt" style="font-size:23px"><tr><th>Change</th><th style="text-align:center">EBIT</th><th style="text-align:center">Equity</th>'
             f'<th style="text-align:center">Cash / OCF</th><th>Liebherr example</th></tr>{trs.replace("padding:8px 14px", "")}</table>')
    slides.append(frame(0, "Report §4.2–4.4 and §6.2; Excel workbook, sheets A2 (note 10), C1, C2 and D9",
        scope("t17", [(".rt", "font-size:23px"), (".rt td", "padding:22px 16px"), (".arw", "width:46px;height:40px;font-size:20px")]) + hdr(SEC, "What-if II: accounting choices move profit, not cash", "Effect of an accounting choice on EBIT, equity and cash") +
        f'<div class="t17" style="position:absolute;left:96px;top:240px;width:1728px">{table}</div>' +
        pill("<b>Investor lens</b> Operating cash flow is the check on the accruals – only 28.4 % of EBITDA in 2022–2025")))

    # ------------------------------------------------------------- A5 Provisions
    steps = [("Opening 1 Jan", 855, "t"), ("Additions", 337, "+"), ("Usage", -185, "-"), ("Reversals", -143, "-"), ("Closing 31 Dec", 864, "t")]
    sub = ["", "expense ▼ profit", "cash out, no P&amp;L", "income ▲ profit", ""]
    W, H, l, t, b = 980, 420, 20, 40, 70
    pw, ph = W - 2 * l, H - t - b
    bw, top = pw / 5 * 0.58, 1250
    Y = lambda v: t + ph * (1 - v / top)
    svg = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
    run = 0
    for i, (lab, v, k) in enumerate(steps):
        cx = l + pw * (i + 0.5) / 5
        if k == "t":
            y0, y1, col = 0, v, ("#3A444E" if i == 0 else "#FFCF00"); run = v
        else:
            y0, y1 = run, run + v; run = y1
            col = "#D9534F" if k == "+" else "#7FB77E"
        hi, lo = max(y0, y1), min(y0, y1)
        svg.append(f'<rect class="gv" x="{cx-bw/2:.1f}" y="{Y(hi):.1f}" width="{bw:.1f}" height="{Y(lo)-Y(hi):.1f}" fill="{col}"/>')
        txt = f"{v:+,}".replace("+", "+" if k != "t" else "").replace("-", "−")
        svg.append(f'<text x="{cx:.1f}" y="{Y(hi)-10:.1f}" text-anchor="middle" font-family="Arimo" font-size="24" font-weight="700" fill="#00182E">{txt}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{H-42}" text-anchor="middle" font-family="Arimo" font-size="20" font-weight="700" fill="#00182E">{lab}</text>')
        svg.append(f'<text x="{cx:.1f}" y="{H-16}" text-anchor="middle" font-family="Arimo" font-size="17" fill="#5E6873">{sub[i]}</text>')
    svg.append("</svg>")
    nc = "".join(f'<div style="text-align:center"><div style="font-size:16px;color:var(--muted);font-weight:700">{y}</div><div class="big" style="font-size:30px">{v}</div></div>'
                 for y, v in (("2022", 193), ("2023", 338), ("2024", 195), ("2025", 194)))
    slides.append(frame(0, "Excel workbook, sheets A2 (note 10, rows 68–80), C2 and D11 (block B); Report §4.2 and §4.4, Table H1 test 1. € m",
        hdr(SEC, "Provisions: reversals rose – but so did additions", "Movement of provisions 2025 (IAS 37), € m – of which warranty 530") +
        box(96, 240, 1030, 610, '<div class="ctitle">Roll-forward 2025, all provisions</div>' + f'<div style="margin-top:10px">{"".join(svg)}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:6px;border-top:2px solid var(--light);padding-top:10px">'
            f'<div style="font-size:18px;font-weight:800;max-width:260px;line-height:1.3">Net charge<br><span style="font-weight:600;color:var(--muted)">= additions − reversals</span></div>{nc}</div>') +
        card(1156, 240, 668, 610, "How to read it", ul([
            "<b>IAS 37:</b> present obligation from a past event, probable outflow, reliable estimate",
            "<b>Usage ≠ reversal:</b> only additions and reversals touch profit",
            "<b>Hidden reserve test:</b> a release to support profit would show as a <i>falling</i> net charge – 195 → 194, so not visible",
            "<b>Flag kept:</b> other provisions built up by €146 m in 2023 are being released (€63 m in 2025); the notes cannot show why"], 21), "navy")))

    # ------------------------------------------------------------- A6 Sensitivity step by step
    rows = [("As reported", "–", "413", "2.80 %", True),
            ("Net provision charge at the 2022–2024 average", "413 − (1.76 % − 1.31 %) × 14,772", "347", "2.35 %", False),
            ("… without the high charge of 2023", "413 − (1.43 % − 1.31 %) × 14,772", "395", "2.68 %", False),
            ("Caterpillar's depreciation rate (6.6 % instead of 5.5 % of cost)", "413 − 105", "308", "2.08 %", False),
            ("Both effects together", "413 − 66 − 105", "242", "1.64 %", True)]
    trs = "".join(f'<tr style="{"background:#FFF8D6" if h else ""}"><td style="font-weight:700">{a}</td><td class="f">{b}</td><td class="n">{c}</td><td class="n" style="font-size:24px">{d}</td></tr>' for a, b, c, d, h in rows)
    table = (f'<table class="rt" style="font-size:24px"><tr><th>Step</th><th>Calculation, € m</th><th style="text-align:center">EBIT</th><th style="text-align:center">Margin</th></tr>{trs}</table>')
    slides.append(frame(0, "Excel workbook, sheets D9 (blocks A and B) and D11 (block B); Report §6.1, Tables H3 and J13",
        scope("t19", [(".rt", "font-size:24px"), (".rt td", "padding:24px 18px"), (".rt td.f", "font-size:21px")]) + hdr(SEC, "Sensitivity: every measured effect lowers the margin", "Liebherr operating margin 2025 – illustrations on published figures, not booked adjustments") +
        f'<div class="t19" style="position:absolute;left:96px;top:240px;width:1728px">{table}</div>' +
        box(96, 690, 1728, 150,
            '<div style="display:flex;gap:40px;align-items:center;height:100%"><div class="big" style="font-size:40px;white-space:nowrap">2.80 − 0.44 − 0.71 = 1.64 %</div>'
            '<div style="font-size:20px;line-height:1.4">Sheet D9 also shows a <b>gross-reversal</b> view (2.5 % at average reversals, 1.8 % without any reversal). '
            'The report uses the <b>net charge</b> (D11), because additions rose together with the reversals. Own work capitalised (€317 m) cannot be measured.</div></div>',
            "var(--light)", False)))

    import extra as _X
    _X.six_steps(slides, frame, hdr, SEC)

    # ------------------------------------------------------------- A7 Long list to short list
    st = [("1", "Long list", "30", "accounting treatments with room for choice", "Table G2", "yellow"),
          ("2", "Key treatments", "9", "key account × high or medium-to-high flexibility", "Table G1", "navy"),
          ("3", "Red-flag screen", "9", "8 tests + 1 consistency check → 4 flags · 3 clean · 2 not testable", "Table H1", "yellow"),
          ("4", "Short list", "22", "findings – red flags, gaps and comparability issues, not a subset of the 30", "Table H2", "navy")]
    flow = ""
    for i, (n, t, big, d, s, k) in enumerate(st):
        x = 96 + i * 442
        bg, fg, ac = ("var(--y)", "var(--navy)", "var(--navy)") if k == "yellow" else ("var(--navy)", "#fff", "var(--y)")
        flow += (f'<div style="position:absolute;left:{x}px;top:240px;width:402px;height:300px;background:{bg};color:{fg};border-radius:16px;padding:22px 26px">'
                 f'<div style="font-size:17px;font-weight:800;letter-spacing:2px;opacity:.75">STEP {n} · {s.upper()}</div>'
                 f'<div class="h" style="font-size:28px;color:inherit;margin-top:8px">{t}</div>'
                 f'<div class="big" style="font-size:84px;color:{ac};line-height:1.05;margin-top:6px">{big}</div>'
                 f'<div style="font-size:20px;line-height:1.35;margin-top:8px">{d}</div></div>')
        if i < 3:
            flow += f'<div style="position:absolute;left:{x + 406}px;top:360px;font-size:34px;font-weight:800;color:var(--navy)">▸</div>'
    slides.append(frame(0, "Report §4.2–4.4, Tables G1, G2, H1 and H2",
        hdr(SEC, "From 30 treatments to 22 findings", "Four steps of the accounting analysis – the short list adds what the screen and the comparison found") + flow +
        card(96, 570, 852, 290, "The nine key treatments", "Inventory cost and write-down · own work capitalised · impairment · expected credit losses · three provision categories · deferred taxes. "
             "<span style='color:var(--muted)'>Revenue timing and the by-nature format are added – they affect every ratio.</span>", "white") +
        card(972, 570, 852, 290, "Left out – and why", "Borrowing costs, lessee accounting and currency translation: the standard prescribes the mechanics. "
             "Development costs: never capitalised, kept only for the comparison. <span style='color:var(--y)'>7 key accounts hold 9 key treatments; the 9 tests are a different count.</span>", "navy")))

    # ------------------------------------------------------------- A7b Long list (Table G2), two slides
    G2 = [('A', 'Revenue and customer contracts', [('A1', 'Timing of revenue (IFRS 15)', 'Medium', 'cost-to-cost estimate, over-time share not disclosed', 'Yes'), ('A2', 'Sale of rental machines (IAS 16.68A)', 'Medium', 'residual value, amount not disclosed', 'Partly'), ('A3', 'Leases as lessor (IFRS 16)', 'Medium', 'risks and rewards judgement, small balance', 'No'), ('A4', 'Sales with repurchase obligations (IFRS 15)', 'Low', 'rule-based test, liability 32', 'No'), ('A5', 'Financial guarantees for customer financing (IFRS 9)', 'Medium', 'allowance judgement, volume not disclosed', 'Gap'), ('A6', 'Advance payments and contract liabilities (IFRS 15)', 'Low–medium', 'balances 896 and 289', 'Partly')]), ('B', 'Operating assets', [('B1', 'Cost of inventories (IAS 2)', 'High', 'normal capacity estimate, inventories 6,341', 'Yes'), ('B2', 'Write-down of inventories (IAS 2)', 'High', 'undisclosed allowance on 6,341', 'Yes'), ('B3', 'Own work capitalised (IAS 16, IAS 38)', 'Medium–high', 'attributable cost, 77 % of EBIT', 'Yes'), ('B4', 'Development costs (IAS 38.57)', 'Medium', 'IAS 38 criteria, R&amp;D 708', 'Peer only'), ('B5', 'Useful lives and residual values (IAS 16)', 'Medium', 'bounded by disclosed ranges, on 4,304', 'Partly'), ('B6', 'Impairment of non-current assets (IAS 36)', 'High', 'indicator and cash flow judgements', 'Yes'), ('B7', 'Subsequent expenditure on PP&amp;E (IAS 16.13)', 'Medium', 'undefined threshold, additions 1,050', 'Partly'), ('B8', 'Borrowing costs (IAS 23)', 'Low', 'rule-based, 14 capitalised', 'No'), ('B9', 'Goodwill (IFRS 3, IAS 36)', 'Low', 'immaterial, intangibles 29', 'No'), ('B10', 'Leases as lessee (IFRS 16)', 'Low', 'largely rule-based, liability 238', 'No'), ('B11', 'Expected credit losses on receivables (IFRS 9)', 'Medium', 'provision matrix, allowance not disclosed', 'Yes'), ('B12', 'Derecognition of receivables (IFRS 9)', 'Low–medium', 'rule-based, no sale disclosed', 'No')]), ('C', 'Provisions and employee benefits', [('C1', 'Warranty provisions (IAS 37)', 'High', 'failure-rate estimate, provision 530', 'Yes'), ('C2', 'Expected losses from pending transactions (IAS 37)', 'High', 'contract cost estimate, linked to A1', 'Yes'), ('C3', 'Other provisions and product liability (IAS 37)', 'High', 'content undefined, reversals 63', 'Yes'), ('C4', 'Restructuring provisions (IAS 37)', 'Low–medium', 'rule-based trigger, none disclosed', 'No'), ('C5', 'Post-employment benefits (IAS 19)', 'Medium', 'actuarial estimates, 791', 'Partly')]), ('D', 'Tax and financial items', [('D1', 'Deferred tax assets and tax expense (IAS 12)', 'High', 'probability judgement, swings the tax charge', 'Yes'), ('D2', 'Securities at fair value (IFRS 9, IFRS 13)', 'Low', 'level 1 and 2 inputs, 1,568', 'Partly'), ('D3', 'Derivatives and hedge accounting (IFRS 9)', 'Medium', 'designation choice, movement 160', 'Partly'), ('D4', 'Foreign currency and hyperinflation (IAS 21, IAS 29)', 'Low', 'rule-based, effect not quantified', 'No')]), ('E', 'Scope and presentation', [('E1', 'Scope of consolidation (IFRS 10, 11, IAS 28)', 'Low', 'control judgement, equity-accounted 2', 'No'), ('E2', 'Income statement by nature (IAS 1)', 'Medium', 'line allocation, other operating expenses 2,170', 'Yes'), ('E3', 'Presentation of the finance result (IAS 1, IFRS 7)', 'Medium', 'finance lines not split', 'Partly')])]
    fcol = {"High": ("#FBE3E3", "#A11B1B"), "Medium–high": ("#FDEBD3", "#8A4B00"), "Medium": ("#FFF4C2", "#6B5300"),
            "Low–medium": ("#EEF1E5", "#4E5F2B"), "Low": ("#E3F1E4", "#1E6B2A")}
    kcol = {"Yes": ("var(--navy)", "#FFCF00"), "Partly": ("#E9EBEE", "#3A444E"), "No": ("#fff", "#8A939C"), "Gap": ("#FBE3E3", "#A11B1B"), "Peer only": ("#E9EBEE", "#3A444E")}
    def lltable(groups):
        out = ('<table class="rt"><tr><th style="width:70px">#</th><th>Account and policy (standard)</th><th style="width:170px">Flexibility</th>'
               '<th style="width:560px">Why</th><th style="width:150px;text-align:center">Key account?</th></tr>')
        for L, name, items in groups:
            out += f'<tr><td colspan="5" style="background:var(--light);font-weight:800;font-size:16px;letter-spacing:1.5px;text-transform:uppercase;color:var(--muted)">{L} · {name}</td></tr>'
            for c, a, fl, why, k in items:
                fb, ff = fcol[fl]; kb, kf = kcol[k]
                out += (f'<tr><td class="n" style="color:var(--muted)">{c}</td><td style="font-weight:700">{a}</td>'
                        f'<td><span style="display:inline-block;background:{fb};color:{ff};font-weight:800;font-size:15px;padding:3px 9px;border-radius:7px">{fl}</span></td>'
                        f'<td>{why}</td><td style="text-align:center"><span style="display:inline-block;background:{kb};color:{kf};font-weight:800;font-size:15px;padding:3px 10px;border-radius:7px;border:1px solid #D0D3D8">{k}</span></td></tr>')
        return out + "</table>"
    slides.append(frame(0, "Report Appendix G, Table G2 (30 treatments, notes of the 2025 annual report); flexibility = judgement the standard permits × materiality",
        scope("tL1", [(".rt", "font-size:17px"), (".rt td", "padding:4px 10px;line-height:1.2")]) +
        hdr(SEC, "Long list I: revenue and operating assets", "Treatments 1–18 of 30 (Table G2) – where Liebherr's accounts leave room for choice") +
        f'<div class="tL1" style="position:absolute;left:96px;top:232px;width:1728px">{lltable(G2[:2])}</div>'))
    slides.append(frame(0, "Report Appendix G, Table G2 (30 treatments, notes of the 2025 annual report); flexibility = judgement the standard permits × materiality",
        scope("tL2", [(".rt", "font-size:19px"), (".rt td", "padding:9px 12px;line-height:1.25")]) +
        hdr(SEC, "Long list II: provisions, tax and presentation", "Treatments 19–30 of 30 (Table G2) – “Yes” = key treatment carried into section 4.2") +
        f'<div class="tL2" style="position:absolute;left:96px;top:236px;width:1728px">{lltable(G2[2:])}</div>'))

    # ------------------------------------------------------------- A8 Key accounts (Table G1)
    ka = [("Inventories", "B1, B2", "6,341", "42.9 % of revenue", "IAS 2", "Fixed overheads absorbed at an undefined normal capacity; allowance not disclosed", "High",
           "Largest account – 36.3 % of total assets; quality cannot be verified"),
          ("Provisions", "C1–C3", "864", "of which warranty 530", "IAS 37", "Recognition, measurement and reversal of the estimate", "High",
           "Reversals €143 m = 34.6 % of the operating result if credited within it"),
          ("PP&amp;E and rental fleet", "B5–B7", "4,304", "24.6 % of total assets", "IAS 16 / IAS 36", "Useful lives, residual values, indicator-based impairment", "High (impairment), medium (lives)",
           "Depreciation 5.5 % of cost vs. 6.6 % at Caterpillar"),
          ("Own work capitalised", "B3", "317", "77 % of the operating result", "IAS 16 / IAS 38", "Which production cost is capitalised rather than expensed", "Medium to high",
           "Moves cost out of the year – returns later as depreciation"),
          ("Trade receivables and contract assets", "B11", "3,116", "17.8 % of total assets", "IFRS 9", "Simplified lifetime expected credit loss through a provision matrix", "Medium",
           "Grew 9.1 % against revenue +1.0 % in 2025; allowance not disclosed"),
          ("Revenue", "A1, A2", "14,772", "", "IFRS 15", "Point in time against over time; cost-to-cost estimate", "Medium",
           "Share recognised over time not disclosed – affects every ratio"),
          ("Deferred tax assets and tax charge", "D1", "285", "tax rate 37.8–99.2 %", "IAS 12", "Probability of future taxable profit; announced instead of enacted rates", "High",
           "No tax reconciliation – after-tax ratios not usable")]
    flexcol = {"High": ("#FBE3E3", "#A11B1B"), "Medium": ("#FFF4C2", "#6B5300"), "Medium to high": ("#FDEBD3", "#8A4B00")}
    trs = ""
    for a, ll, amt, sub, std, j, fl, why in ka:
        bg, fg = flexcol.get(fl, ("#FBE3E3", "#A11B1B"))
        trs += (f'<tr><td><div style="font-weight:800">{a}</div><div style="font-size:15px;color:var(--muted)">long list {ll}</div></td>'
                f'<td class="n l">{amt}<div style="font-size:15px;font-weight:600;color:var(--muted)">{sub}</div></td>'
                f'<td><b>{std}</b> – {j}</td>'
                f'<td><span style="display:inline-block;background:{bg};color:{fg};font-weight:800;font-size:16px;padding:5px 10px;border-radius:8px">{fl}</span></td>'
                f'<td>{why}</td></tr>')
    table = (f'<table class="rt"><tr><th style="width:250px">Key account</th><th class="l" style="width:170px">2025, € m</th><th>Standard and judgement</th>'
             f'<th style="width:190px">Flexibility</th><th style="width:420px">Why it is on the short list</th></tr>{trs}</table>')
    slides.append(frame(0, "Report §4.2–4.3, Tables G1 and G2; Liebherr-International AG (2026); IFRS Foundation (n.d.)",
        scope("t22", [(".rt", "font-size:21px"), (".rt td", "padding:15px 12px;line-height:1.3")]) +
        hdr(SEC, "Seven key accounts carry the judgement", "Key accounts × flexibility = the nine key treatments of the long list") +
        f'<div class="t22" style="position:absolute;left:96px;top:236px;width:1728px">{table}</div>'))

    # ------------------------------------------------------------- A9 Red-flag screen (Table H1)
    tests = [("1", "Unexplained transactions that boost profits", "Provision reversals 90 → 143 (2022–2025) = 34.6 % of 2025 EBIT; net charge flat (195 → 194); credited line not disclosed", "Raised"),
             ("2", "Inventories or receivables rise faster than sales", "Inventories +27.3 % vs. revenue +8.2 % (2022); receivables +9.1 % vs. revenue +1.0 % (2025)", "Raised twice"),
             ("3", "Gap between profit and cash flow or taxable profit", "Operating cash flow −415 and −10 (2022–23) against profit; tax rate 99.2 % → 37.8 %, no reconciliation", "Raised"),
             ("4", "R&amp;D partnerships, special purpose entities, sold receivables", "None disclosed in four years; R&amp;D fully expensed", "No flag"),
             ("5", "Unexpected large asset write-offs", "PP&amp;E impairment 8, 55, 9, 3 – 2023 six times the other years, same one-sentence explanation", "Raised for 2023"),
             ("6", "Large year-end adjustments", "No interim figures published, so no within-year comparison", "Not testable"),
             ("7", "Qualified opinions or auditor changes", "Ernst &amp; Young all four years, no qualification, no restatement (ISA 810 opinion)", "No flag"),
             ("8", "Related party transactions", "No note in four years – family-owned group that also runs six hotels", "Not testable"),
             ("9", "Changes in accounting policies or estimates", "Policies worded identically; new standards without material effect", "No flag")]
    vc = {"Raised": ("#FBE3E3", "#A11B1B"), "Raised twice": ("#FBE3E3", "#A11B1B"), "Raised for 2023": ("#FBE3E3", "#A11B1B"),
          "No flag": ("#E3F1E4", "#1E6B2A"), "Not testable": ("#E9EBEE", "#3A444E")}
    trs = "".join(f'<tr><td class="n" style="color:var(--muted)">{n}</td><td style="font-weight:700">{t}</td><td>{e}</td>'
                  f'<td><span style="display:inline-block;background:{vc[v][0]};color:{vc[v][1]};font-weight:800;font-size:17px;padding:5px 12px;border-radius:8px;white-space:nowrap">{v}</span></td></tr>'
                  for n, t, e, v in tests)
    table = (f'<table class="rt"><tr><th style="width:44px">#</th><th style="width:470px">Test</th><th>Evidence 2022–2025</th><th style="width:200px">Verdict</th></tr>{trs}</table>')
    slides.append(frame(0, "Report §4.4, Table H1 (8 tests of step 5 + consistency check of step 3); Liebherr-International AG (2023–2026)",
        scope("t25", [(".rt", "font-size:20px"), (".rt td", "padding:12px 12px;line-height:1.3")]) +
        hdr(SEC, "Red-flag screen: nine tests, four flags", "4 raised · 3 clean · 2 not testable – reasons to ask, not proof of manipulation") +
        f'<div class="t25" style="position:absolute;left:96px;top:236px;width:1728px">{table}</div>'))

    # ------------------------------------------------------------- A9/A10 Short list of 22 findings (Table H2)
    groups = [("Not adjustable – red flags and disclosure gaps", 7, "#FBE3E3", "#A11B1B", [
                  ("Provision reversals rise as the result falls (test 1)", "Provisions, 864", "Not adjustable: the income line carrying the reversal is not disclosed"),
                  ("Inventories and receivables grow faster than sales (test 2)", "Inventories 6,341, receivables 3,116", "Not adjustable: neither allowance is disclosed"),
                  ("Volatile and unreconciled tax charge (test 3)", "Deferred tax assets, 285 (IAS 12)", "Not adjustable: no tax reconciliation is published"),
                  ("Impairment spike in 2023 (test 5)", "PP&amp;E, impairment 55", "Not adjustable: no test assumptions are disclosed"),
                  ("Composition of other operating expenses not disclosed", "Other operating expenses, 2,170", "Not adjustable: the line has no note"),
                  ("No related party disclosure in four years (test 8)", "Whole group", "The information is not in the published statements"),
                  ("Customer credit risk carried off balance sheet", "Financial guarantees, not quantified", "Not adjustable: no amount is disclosed")]),
              ("Reversed in the workbook", 5, "#E3F1E4", "#1E6B2A", [
                  ("Caterpillar inventories on LIFO", "Inventories, equity, operating profit", "FIFO excess disclosed – exact correction: $4,305 m"),
                  ("Caterpillar goodwill impairment 2022 inside operating costs", "Operating profit 2022", "Moved to other income as a non-recurring item"),
                  ("Liebherr change in inventories and own work shown as income", "Revenue, cost of materials", "Both mapped into the cost line (standardised format)"),
                  ("Caterpillar finance receivables inside trade receivables", "Trade receivables", "Mapped to other current assets and non-operating investments"),
                  ("Liebherr trade payables not shown on the balance sheet", "Trade payables", "Taken from note 7, published subtotal preserved")]),
              ("Not reversible – disclosure too thin", 10, "#E9EBEE", "#3A444E", [
                  ("Gross presentation of rental machine disposals", "Revenue, cost of materials", "The amount is not disclosed"),
                  ("The interest element of the finance result", "Finance income 1,043, expenses 1,015", "No split is published"),
                  ("No segment note under IFRS 8", "Whole income statement", "Segment data only in the management report"),
                  ("The effect of hyperinflation accounting", "Turkish and Ghanaian entities", "Not quantified in any year"),
                  ("Actuarial assumptions behind the pension obligation", "Post-employment benefits, 791", "No discount rate and no sensitivity disclosed"),
                  ("Inventory and receivable allowances", "Inventories 6,341, receivables 3,116", "Neither balance nor charge is disclosed"),
                  ("The two groups do not depreciate at the same rate", "PP&amp;E, 4,304", "Measured (Table H3), not carried into the recast – asset mixes differ"),
                  ("Cat Financial inside every Caterpillar figure", "Caterpillar balance sheet", "The consolidated basis was set by the assignment"),
                  ("Caterpillar discloses no cost of materials or personnel expense", "Cost structure comparison", "Not estimated – operating costs shown as one line"),
                  ("Potential refund of US tariffs after the balance sheet date", "Not recognised; note 12", "Non-adjusting event (IAS 10), no reliable estimate")])]

    def ftable(gs):
        out = '<table class="rt"><tr><th style="width:44px">#</th><th>Finding</th><th style="width:430px">Account affected (€ m / $ m)</th><th style="width:600px">Treatment</th></tr>'
        k = sum(len(g[4]) for g in groups[:groups.index(gs[0])])
        for title, n, bg, fg, items in gs:
            out += f'<tr><td colspan="4" style="background:{bg};color:{fg};font-weight:800;font-size:17px;letter-spacing:1.5px;text-transform:uppercase">{title} · {n}</td></tr>'
            for f, a, t in items:
                k += 1
                out += f'<tr><td class="n" style="color:var(--muted)">{k}</td><td style="font-weight:700">{f}</td><td>{a}</td><td>{t}</td></tr>'
        return out + "</table>"

    slides.append(frame(0, "Report §4.4, Table H2 (short list, 22 findings); Excel workbook, sheets B3, C1, C2, E1 and E2",
        scope("t23", [(".rt", "font-size:20px"), (".rt td", "padding:10px 12px;line-height:1.25")]) +
        hdr(SEC, "Short list I: what cannot be fixed – and what we fixed", "Findings 1–12 of 22 (Table H2)") +
        f'<div class="t23" style="position:absolute;left:96px;top:236px;width:1728px">{ftable(groups[:2])}</div>'))
    slides.append(frame(0, "Report §4.4, Table H2 (short list, 22 findings); Excel workbook, sheets B3, C1, C2, E1 and E2",
        scope("t24", [(".rt", "font-size:21px"), (".rt td", "padding:16px 12px;line-height:1.25")]) +
        hdr(SEC, "Short list II: what the disclosure does not let us reverse", "Findings 13–22 of 22 (Table H2)") +
        f'<div class="t24" style="position:absolute;left:96px;top:236px;width:1728px">{ftable(groups[2:])}</div>'))

    # ------------------------------------------------------------- A8 Workbook
    wf = [("A1–A4", "Published statements", "typed exactly as printed"),
          ("B1–B3", "Recast by nature", "formulas only · 21 mapping decisions"),
          ("C1–C2", "Adjustments", "LIFO → FIFO · goodwill 2022 · note data"),
          ("D1–D11", "Analysis", "ratios · DuPont · sensitivities · benchmark"),
          ("E1–E2", "Judgements and checks", "44 judgements · every subtotal reconciled")]
    flow = ""
    for i, (c, t, d) in enumerate(wf):
        x = 96 + i * 352
        last = i == 4
        flow += (f'<div style="position:absolute;left:{x}px;top:240px;width:326px;height:210px;background:{"var(--navy)" if last else "#fff"};color:{"#fff" if last else "var(--navy)"};'
                 f'border-radius:16px;box-shadow:0 6px 24px rgba(0,24,46,.10);padding:20px 22px">'
                 f'<div style="display:inline-block;background:var(--y);color:var(--navy);font-weight:800;font-size:22px;border-radius:8px;padding:6px 12px">{c}</div>'
                 f'<div class="h" style="font-size:26px;color:inherit;margin-top:14px">{t}</div><div style="font-size:19px;line-height:1.35;margin-top:6px;opacity:.85">{d}</div></div>')
    slides.append(frame(0, "Excel workbook, sheets Method, B1–B3, C1, E1 and E2; Report §4.5 and Appendix K",
        hdr(SEC, "Workbook: every number traces back to the report", "From the published statements to the ratios – and how we know it adds up") + flow +
        card(96, 480, 1080, 380, "Key mapping decisions", ul([
            "Change in inventories and own work capitalised mapped into the cost of materials",
            "Caterpillar's finance receivables taken out of trade receivables",
            "Liebherr's trade payables taken from note 7",
            "Caterpillar's operating costs kept as one line – no materials or personnel split published",
            "Liebherr in €, Caterpillar in $ – never added or divided across companies"], 21), "white") +
        f'<div style="position:absolute;left:1206px;top:480px;width:618px;height:178px;background:#1E6B2A;color:#fff;border-radius:16px;padding:18px 26px;display:flex;gap:20px;align-items:center">'
        f'<div class="big" style="font-size:84px;color:#fff;line-height:1">0</div><div><div style="font-size:16px;font-weight:800;letter-spacing:2px;opacity:.85">CHECKS · SHEET E2</div>'
        f'<div style="font-size:22px;font-weight:800">open differences</div><div style="font-size:17px;line-height:1.35;margin-top:4px">Three deliberate differences are labelled (goodwill 2022, affiliates after tax, depreciation)</div></div></div>'
        f'<div style="position:absolute;left:1206px;top:678px;width:618px;height:182px;background:var(--y);border-radius:16px;padding:16px 26px">'
        f'<div style="font-size:16px;font-weight:800;letter-spacing:2px">WHY BY NATURE, NOT BY FUNCTION</div>'
        f'<div style="font-size:18.5px;line-height:1.38;margin-top:6px">Liebherr reports by nature (materials, personnel, depreciation), Caterpillar by function (cost of sales, SG&amp;A, R&amp;D). '
        f'A function format would leave every Liebherr cost line empty and show no depreciation for either group – so both are recast by nature.</div></div>'))


NOTES = [
    ("Backup A – Profitability ratios", "—", "We group the ratios into four families. This slide shows profitability, both margins and returns on capital. Return on equity is profit after tax divided by average equity, so 272 over 9,128, which is 3.0 per cent, or 4.8 per cent before tax. ROA, ROCE and ROE belong to profitability, because they measure profit against the capital used. DuPont links the families. ROE equals profitability times efficiency times leverage, and leverage is average total assets over average equity. Leverage works on ROE, not on the EBIT margin, because EBIT is measured before interest. Caterpillar's ROE is inflated by its treasury shares and is not comparable."),
    ("Backup A – Efficiency, leverage, liquidity", "—", "The other three families are efficiency, leverage and liquidity. Efficiency, also called asset utilisation, covers the turnover ratios and the working-capital days. The days are efficiency ratios, but they drive liquidity, because 203 days of revenue have to be financed. Leverage, or solvency, shows how Liebherr is financed in the long run, with an equity ratio of 53.5 per cent and a DuPont leverage of 1.89 against 3.97 at Caterpillar. Liquidity is short term. The current ratio of 2.31 and the quick ratio of 1.16 are liquidity ratios, not leverage ratios. Days are on a revenue basis because Liebherr reports no cost of sales, and there are two debt measures, one including pensions of 3,714 million euro and the bank and lease liabilities of 2,898 million euro used for the benchmark."),
    ("Backup A – Cash flow and growth ratios", "—", "These ratios show how well profit turns into cash. Operating cash flow was only 53 per cent of EBITDA in 2025, against 87.5 per cent at Caterpillar. Capital expenditure was 1.2 times depreciation, so the asset base is growing, and operating cash flow covered only three quarters of capex. Free cash flow was minus 176 million euro, or minus 1.2 per cent of revenue. Liebherr paid out about a fifth of its profit. The sustainable growth rate, return on equity times one minus the payout ratio, is only 2.4 per cent, so faster growth would need better returns, less capital or outside financing. Note that cash conversion as a ratio is not the cash conversion cycle in days."),
    ("Backup A – Workbook to ratio", "—", "This is an excerpt of sheet D3 for Liebherr in 2025. Every input is a formula that links to the recast statements or to the adjustments sheet, so nothing is typed in. Return on equity in cell B40 is B10 divided by B27, so 272 over the average equity of 9,128, which gives 3.0 per cent. Inventory days are average inventories divided by revenue times 365, which gives 157.5 days. The current ratio is current assets of 12,709 divided by current liabilities of 5,498, which gives 2.31. Sheet E2 reconciles every subtotal, with zero open differences."),
    ("Backup A – What-if I", "—", "If suppliers are paid in cash, current assets and current liabilities fall by the same amount, so a current ratio above one rises – with 500 million euro it would go from 2.31 to 2.44. An inventory write-down lowers profit and the current ratio, but also the inventory days, so the ratio looks better while the position is weaker. New debt lowers the equity ratio and raises leverage, but leaves the EBIT margin unchanged. A shorter cash conversion cycle releases cash once, it does not improve the margin."),
    ("Backup A – What-if II", "—", "Accounting choices move profit, not cash. A provision addition is an expense, usage settles the obligation in cash without a profit effect, and a reversal increases profit without cash. Slower depreciation and more own work capitalised raise EBIT today. Caterpillar's switch from LIFO to FIFO raises profit and equity. That is why operating cash flow, only 28.4 per cent of EBITDA over four years, is our check on the accruals."),
    ("Backup A – Provisions", "—", "Provisions under IAS 37 need a present obligation from a past event, a probable outflow and a reliable estimate. In 2025 the opening balance of 855 million euro rose by 337 of additions, fell by 185 of usage and by 143 of reversals, to 864. Usage is the real outflow and has no profit effect; only additions and reversals touch profit. The net charge – additions less reversals – stayed at 194 against 195, so a hidden reserve being released to support profit is not visible. We keep the flag because other provisions built up in 2023 are now being released and the notes cannot explain why."),
    ("Backup A – Sensitivity", "—", "We measure two effects without booking them. If the net provision charge had been at its 2022 to 2024 average of 1.76 per cent of revenue instead of 1.31, EBIT would be 347 million euro and the margin 2.35 per cent; without the high charge of 2023 it would be 2.68. At Caterpillar's depreciation rate depreciation would be 105 million euro higher and the margin 2.08 per cent. Both together give 242 million euro, or 1.64 per cent. Sheet D9 also shows a gross-reversal view, but the report uses the net charge because additions rose with the reversals."),
    __import__("extra").NOTES["six_steps"],
    ("Backup A – Long list to short list", "—", "Step one is the long list of 30 accounting treatments with room for choice. Step two keeps the nine that combine a key account with high or medium-to-high flexibility. Step three is the red-flag screen: eight tests plus one consistency check, with four flags, three clean and two not testable. Step four is the short list of 22 findings: seven that no adjustment can remove, five reversed in the workbook and ten the disclosure does not allow us to reverse. Seven key accounts hold the nine key treatments, and the nine tests are a different count. The short list is not a subset of the 30, because it also contains red flags, disclosure gaps and comparability issues."),
    ("Backup A – Long list I", "—", "The long list has 30 accounting treatments from the notes, each rated by two criteria, the judgement the standard permits and the materiality of the amount. In revenue and operating assets, the highest flexibility lies in the cost and write-down of inventories and in impairment. Own work capitalised is medium to high because it equals 77 per cent of the operating result. Borrowing costs, goodwill and lessee accounting are low, because the standard prescribes the mechanics or the amounts are small."),
    ("Backup A – Long list II", "—", "The second half covers provisions, tax, financial items and presentation. All three provision categories and deferred taxes are rated high. Pensions, securities and derivatives matter only partly, because they affect solvency or the finance result rather than the operating margin. The income statement by nature is a key treatment because it affects every ratio, and we corrected it in the recast. In total nine items combine a key account with high flexibility, plus revenue timing and the by-nature format."),
    ("Backup A – Key accounts", "—", "Seven key accounts carry the judgement. Inventories under IAS 2, provisions under IAS 37, property, plant and equipment under IAS 16 and 36, own work capitalised, receivables under IFRS 9, revenue under IFRS 15 and deferred taxes under IAS 12. They are on the short list because they combine a material amount with high or medium flexibility: inventories are 36.3 per cent of total assets, provision reversals equal 34.6 per cent of the operating result, own work capitalised 77 per cent, and the tax rate swings between 37.8 and 99.2 per cent without a reconciliation."),
    ("Backup A – Red-flag screen", "—", "We ran the eight red-flag tests of step five over four years, plus one consistency check of step three. Four raised a flag. Provision reversals rose while the result fell, inventories and receivables grew faster than sales, the tax rate swung without a reconciliation, and the impairment of 2023 was six times the normal level. Three tests are clean, namely off-balance-sheet structures, the audit opinion and policy changes. Two cannot be run, because there are no interim figures and no related party note. A red flag is a reason to ask, not proof of manipulation."),
    ("Backup A – Short list I", "—", "The short list has 22 findings. Seven are red flags or disclosure gaps that no adjustment can remove – for example the provision reversals, the unexplained tax charge and the other operating expenses without a note. Five distortions we reversed in the workbook – the most important is Caterpillar's LIFO inventory, restated to FIFO with the disclosed excess of 4,305 million dollars."),
    ("Backup A – Short list II", "—", "Ten distortions cannot be reversed because the disclosure is too thin: for example the gross presentation of rental machine disposals, the missing interest split, the missing segment note, the pension assumptions and the undisclosed allowances. The different depreciation rates we measured in a sensitivity, but did not book, because the asset mixes differ."),
    ("Backup A – Workbook", "—", "The workbook starts with the published statements typed exactly as printed. The B sheets recast both companies into one format by nature using formulas only, with 21 documented mapping decisions. The C sheets hold the LIFO to FIFO restatement and the note data, the D sheets the analysis. Sheet E1 documents 44 judgements and sheet E2 reconciles every recast subtotal with the published figure: zero open differences, apart from three labelled ones."),
]

QA3 = [("Why pre-tax ROE?", "The effective tax rate was 99.2 %, 45.1 %, 58.2 % and 37.8 % (2022–2025), with no tax reconciliation published – the after-tax trend says little."),
       ("Why Caterpillar as the peer?", "The world's leading maker of construction and mining equipment – the core market of Liebherr's largest sector (63.3 % of revenue). We compare ratios only, never € and $ figures."),
       ("Why a US industry benchmark?", "Damodaran publishes consistent data for 105 listed machinery companies. It is a reference level, not Liebherr's own cost of capital."),
       ("R&amp;D expensed, yet €317 m capitalised?", "Own work capitalised is self-built assets and rental machines (IAS 16), not development costs (IAS 38), which are never capitalised."),
       ("Why days on a revenue basis?", "Liebherr reports no cost of sales, so DIO and DPO use revenue for both groups – comparable, but not the textbook formula.")]

QA3_NOTE = ("Backup F – Questions 3/4", "—", "We read returns before tax because the effective tax rate swung between 37.8 and 99.2 per cent without a reconciliation. Caterpillar is the world's leading maker of construction and mining equipment, the market of Liebherr's largest sector, and we only compare ratios. The Damodaran industry is a reference level, not Liebherr's cost of capital. Own work capitalised is self-built equipment, not development costs. Working-capital days use revenue because Liebherr reports no cost of sales.")
