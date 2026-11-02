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
    rows = [("Profitability", [("Operating margin", "EBIT / revenue", "2.8 %", "17.2 %"),
                               ("Pre-tax margin", "Profit before tax / revenue", "3.0 %", "17.9 %"),
                               ("Net profit margin", "Profit after tax / revenue", "1.8 %", "13.8 %"),
                               ("EBITDA margin", "EBITDA / revenue", "6.8 %", "19.8 %")]),
            ("Returns", [("ROA", "EBIT / average total assets", "2.4 %", "11.9 %"),
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
        '<div style="font-size:19px;opacity:.85;margin-bottom:18px">leverage = average total assets / average equity</div>'
        '<table style="width:100%;border-collapse:collapse;font-size:22px;color:#fff;margin-top:6px">'
        '<tr style="color:var(--y);font-size:16px;letter-spacing:1px"><td></td><td>MARGIN</td><td>TURNOVER</td><td>LEVERAGE</td><td>ROE</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">2025</td><td>1.84 %</td><td>× 0.85</td><td>× 1.89</td><td style="font-weight:800">3.0 %</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">pre-tax</td><td>2.96 %</td><td>× 0.85</td><td>× 1.89</td><td style="font-weight:800">4.8 %</td></tr>'
        '<tr><td style="padding:8px 0;font-weight:700">2023 pre-tax</td><td>4.76 %</td><td>× 0.88</td><td>× 1.81</td><td style="font-weight:800">7.6 %</td></tr></table>'
        '<div style="font-size:20px;line-height:1.4;margin-top:20px;border-top:1px solid rgba(255,255,255,.2);padding-top:16px">'
        'Leverage works on ROE, <b style="color:var(--y)">not on the EBIT margin</b> – EBIT is measured before interest.</div>')
    slides.append(frame(0, "Excel workbook, sheets D3 (blocks C and D) and D4; Report §5.3, Table J14. 2025; Caterpillar on the FIFO basis",
        CSS + scope("t14", [(".rt", "font-size:22px"), (".rt td", "padding:12px 14px"), (".rt td.f", "font-size:18.5px"), ("td.g", "width:130px")]) + hdr(SEC, "Ratios I: returns are low because the margin is low", "Profitability and returns – formula, Liebherr and Caterpillar, 2025") +
        f'<div class="t14" style="position:absolute;left:96px;top:240px;width:1130px">{table}</div>' +
        box(1256, 240, 568, 640, dupont, "var(--navy)", False) +
        note(820, "* Not comparable – treasury shares reduce Caterpillar's equity. ROA is measured on EBIT,<br>because Liebherr's interest expense is not disclosed.", w=1130)))

    # ------------------------------------------------------------- A2 Ratios II: utilisation, working capital, liquidity, solvency
    rows = [("Asset utilisation", [("Asset turnover", "Revenue / average total assets", "0.85", "0.69"),
                                   ("Fixed asset turnover", "Revenue / average PP&amp;E", "3.49", "4.74")]),
            ("Working capital", [("Days inventory outstanding", "Avg. inventories / revenue × 365", "157.5", "116.5"),
                                 ("Days sales outstanding", "Avg. receivables / revenue × 365", "73.8", "54.5"),
                                 ("Days payables outstanding", "Avg. payables / revenue × 365", "28.6", "44.9"),
                                 ("Cash conversion cycle", "DIO + DSO − DPO", "202.7", "126.1")]),
            ("Liquidity", [("Current ratio", "Current assets / current liabilities", "2.31", "1.55"),
                           ("Quick ratio", "(Current assets − inventories) / current liab.", "1.16", "0.94"),
                           ("Cash cover", "Cash + current fin. assets / current debt", "2.6×", "–")]),
            ("Solvency", [("Equity ratio", "Equity / total assets", "53.5 %", "24.9 %"),
                          ("Debt / equity", "Debt incl. pensions / equity", "0.40", "1.84"),
                          ("Debt / capital", "Bank + lease liab. / (those + equity)", "23.7 %", "64.8 %"),
                          ("Debt / EBITDA", "Bank + lease liabilities / EBITDA", "2.90", "3.52")])]
    trs = ""
    for g, items in rows:
        for i, (r, f, l, c) in enumerate(items):
            gcell = f'<td class="g" rowspan="{len(items)}">{g}</td>' if i == 0 else ""
            trs += f'<tr>{gcell}<td style="font-weight:700">{r}</td><td class="f">{f}</td><td class="n l">{l}</td><td class="n">{c}</td></tr>'
    table = (f'<table class="rt" style="font-size:20px"><tr><th>Group</th><th>Ratio</th><th>Formula</th><th class="l">Liebherr</th><th class="c">Caterpillar</th></tr>{trs}</table>')
    slides.append(frame(0, "Excel workbook, sheets D3 (blocks D, E, G, H) and D7; Report Tables J5 and J14. 2025; days on average balances; Caterpillar on the FIFO basis",
        scope("t15", [(".rt", "font-size:21px"), (".rt td", "padding:10px 14px"), (".rt td.f", "font-size:18px")]) + hdr(SEC, "Ratios II: strong liquidity, slow capital", "Asset utilisation, working capital, liquidity and solvency – 2025") +
        f'<div class="t15" style="position:absolute;left:96px;top:236px;width:1310px">{table}</div>' +
        box(1436, 236, 388, 650,
            '<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">READ WITH CARE</div>'
            '<div style="font-size:21px;line-height:1.45;margin-top:14px;color:#fff">'
            '<b style="color:var(--y)">Days on a revenue basis:</b> Liebherr reports no cost of sales. On its own cost basis DIO would be 299 days – not comparable.<br><br>'
            '<b style="color:var(--y)">Two debt measures:</b> “debt” includes pensions (€3,714 m); bank and lease liabilities (€2,898 m) match the Damodaran benchmark.<br><br>'
            '<b style="color:var(--y)">Interest cover:</b> not computable – no interest expense disclosed. Indicator: operating profit / interest paid 3.90.</div>',
            "var(--navy)", False)))

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

    # ------------------------------------------------------------- A7 Long list to short list
    st = [("1", "Long list", "30", "accounting treatments with room for choice", "Table G2", "yellow"),
          ("2", "Key treatments", "9", "key account × high or medium-to-high flexibility", "Table G1", "navy"),
          ("3", "Red-flag screen", "9", "8 tests + 1 consistency check → 4 flags · 3 clean · 2 not testable", "Table H1", "yellow"),
          ("4", "Short list", "22", "findings → 7 not adjustable · 5 reversed · 10 not reversible", "Table H2", "navy")]
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
        hdr(SEC, "From 30 treatments to 22 findings", "How the long list became the short list – four steps") + flow +
        card(96, 570, 852, 290, "The nine key treatments", "Inventory cost and write-down · own work capitalised · impairment · expected credit losses · three provision categories · deferred taxes. "
             "<span style='color:var(--muted)'>Revenue timing and the by-nature format are added – they affect every ratio.</span>", "white") +
        card(972, 570, 852, 290, "Left out – and why", "Borrowing costs, lessee accounting and currency translation: the standard prescribes the mechanics. "
             "Development costs: never capitalised, kept only for the comparison. <span style='color:var(--y)'>The two “9”s are different counts.</span>", "navy")))

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
        f'<div style="position:absolute;left:1206px;top:480px;width:618px;height:380px;background:#1E6B2A;color:#fff;border-radius:16px;padding:26px 30px">'
        f'<div style="font-size:18px;font-weight:800;letter-spacing:2px;opacity:.85">CHECKS · SHEET E2</div>'
        f'<div class="big" style="font-size:96px;color:#fff;line-height:1.05;margin-top:6px">0</div>'
        f'<div style="font-size:24px;font-weight:800">open differences</div>'
        f'<div style="font-size:20px;line-height:1.4;margin-top:14px">Every recast subtotal is a live formula against the published figure. Three deliberate differences are labelled: '
        f'Caterpillar goodwill 2022, equity in affiliates after tax, and the depreciation difference (judgement 12).</div></div>'))


NOTES = [
    ("Backup A – Ratios I", "—", "Return on equity is profit after tax divided by average equity: 272 over 9,128 is 3.0 per cent. Before tax it is 4.8 per cent. DuPont splits it into net margin, asset turnover and leverage, where leverage is average total assets over average equity. Leverage works on return on equity, not on the EBIT margin, because EBIT is measured before interest. ROA is measured on EBIT because Liebherr does not disclose its interest expense. Caterpillar's return on equity is inflated by its treasury shares and is not comparable."),
    ("Backup A – Ratios II", "—", "The current ratio and the quick ratio are liquidity ratios; equity ratio, debt to equity and debt to EBITDA are solvency ratios. The working-capital days are calculated on revenue, because Liebherr reports no cost of sales; on its own cost basis inventory days would be 299 and not comparable. There are two debt measures: debt including pensions of 3,714 million euro, which gives debt to equity of 0.40, and bank and lease liabilities of 2,898 million euro, which match the Damodaran benchmark and give 23.7 per cent of capital and 2.90 times EBITDA. Interest cover cannot be computed for Liebherr."),
    ("Backup A – What-if I", "—", "If suppliers are paid in cash, current assets and current liabilities fall by the same amount, so a current ratio above one rises – with 500 million euro it would go from 2.31 to 2.44. An inventory write-down lowers profit and the current ratio, but also the inventory days, so the ratio looks better while the position is weaker. New debt lowers the equity ratio and raises leverage, but leaves the EBIT margin unchanged. A shorter cash conversion cycle releases cash once, it does not improve the margin."),
    ("Backup A – What-if II", "—", "Accounting choices move profit, not cash. A provision addition is an expense, usage settles the obligation in cash without a profit effect, and a reversal increases profit without cash. Slower depreciation and more own work capitalised raise EBIT today. Caterpillar's switch from LIFO to FIFO raises profit and equity. That is why operating cash flow, only 28.4 per cent of EBITDA over four years, is our check on the accruals."),
    ("Backup A – Provisions", "—", "Provisions under IAS 37 need a present obligation from a past event, a probable outflow and a reliable estimate. In 2025 the opening balance of 855 million euro rose by 337 of additions, fell by 185 of usage and by 143 of reversals, to 864. Usage is the real outflow and has no profit effect; only additions and reversals touch profit. The net charge – additions less reversals – stayed at 194 against 195, so a hidden reserve being released to support profit is not visible. We keep the flag because other provisions built up in 2023 are now being released and the notes cannot explain why."),
    ("Backup A – Sensitivity", "—", "We measure two effects without booking them. If the net provision charge had been at its 2022 to 2024 average of 1.76 per cent of revenue instead of 1.31, EBIT would be 347 million euro and the margin 2.35 per cent; without the high charge of 2023 it would be 2.68. At Caterpillar's depreciation rate depreciation would be 105 million euro higher and the margin 2.08 per cent. Both together give 242 million euro, or 1.64 per cent. Sheet D9 also shows a gross-reversal view, but the report uses the net charge because additions rose with the reversals."),
    ("Backup A – Long list to short list", "—", "Step one is the long list of 30 accounting treatments with room for choice. Step two keeps the nine that combine a key account with high or medium-to-high flexibility. Step three is the red-flag screen: eight tests plus one consistency check, with four flags, three clean and two not testable. Step four is the short list of 22 findings: seven that no adjustment can remove, five reversed in the workbook and ten the disclosure does not allow us to reverse. The two counts of nine are a coincidence."),
    ("Backup A – Workbook", "—", "The workbook starts with the published statements typed exactly as printed. The B sheets recast both companies into one format by nature using formulas only, with 21 documented mapping decisions. The C sheets hold the LIFO to FIFO restatement and the note data, the D sheets the analysis. Sheet E1 documents 44 judgements and sheet E2 reconciles every recast subtotal with the published figure: zero open differences, apart from three labelled ones."),
]

QA3 = [("Why pre-tax ROE?", "The effective tax rate was 99.2 %, 45.1 %, 58.2 % and 37.8 % (2022–2025), with no tax reconciliation published – the after-tax trend says little."),
       ("Why Caterpillar as the peer?", "The world's leading maker of construction and mining equipment – the core market of Liebherr's largest sector (63.3 % of revenue). We compare ratios only, never € and $ figures."),
       ("Why a US industry benchmark?", "Damodaran publishes consistent data for 105 listed machinery companies. It is a reference level, not Liebherr's own cost of capital."),
       ("R&amp;D expensed, yet €317 m capitalised?", "Own work capitalised is self-built assets and rental machines (IAS 16), not development costs (IAS 38), which are never capitalised."),
       ("Why days on a revenue basis?", "Liebherr reports no cost of sales, so DIO and DPO use revenue for both groups – comparable, but not the textbook formula.")]

QA3_NOTE = ("Backup F – Questions 3/3", "—", "We read returns before tax because the effective tax rate swung between 37.8 and 99.2 per cent without a reconciliation. Caterpillar is the world's leading maker of construction and mining equipment, the market of Liebherr's largest sector, and we only compare ratios. The Damodaran industry is a reference level, not Liebherr's cost of capital. Own work capitalised is self-built equipment, not development costs. Working-capital days use revenue because Liebherr reports no cost of sales.")
