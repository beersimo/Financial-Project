"""Further backup slides: accounting strategy, ratio reliability (J13), common-size analysis,
levers and monitoring (chapter 7, Table 3) and a fourth Q&A slide.

All figures come from the report (§4.3, chapter 6, chapters 7–8, Tables 3, J13) and the workbook (D1, D2, D3, D5, D8).
"""
from ratios import scope

UP = '<span class="arw" style="background:var(--y);color:var(--navy)">▲</span>'
DN = '<span class="arw" style="background:var(--navy);color:#fff">▼</span>'


def _tag(text, bg, fg, size=16):
    return f'<span style="display:inline-block;background:{bg};color:{fg};font-weight:800;font-size:{size}px;padding:4px 10px;border-radius:7px;white-space:nowrap">{text}</span>'


def conservative(slides, frame, hdr, card, ul, sec):
    col = lambda x, t, items, bg, fg: (
        f'<div class="card" style="left:{x}px;top:236px;width:556px;height:580px;background:{bg};color:{fg}">'
        f'<div class="h" style="font-size:30px;color:inherit;margin-bottom:16px">{t}</div>{ul(items, 24)}</div>')
    slides.append(frame(0, "Report §4.3 (accounting strategy) and §6.1–6.3; Palepu et al. (2019); Liebherr-International AG (2026)",
        hdr(sec, "Conservative or aggressive? Both, in parts", "Step 3 of the accounting analysis – the evidence points both ways") +
        col(96, "Points to conservative", [
            "Development costs never capitalised (IAS 38.57)",
            "Policies worded identically in all four years",
            "Incentives to inflate profit are absent: unlisted, family-owned, no share-based pay, no disclosed covenant",
            "Warranty provision 3.6 % of revenue – assumptions not disclosed, so not provable"], "#E3F1E4", "var(--navy)") +
        col(682, "Points to aggressive", [
            "Own work capitalised €317 m = 77 % of the operating result",
            "Provision reversals €143 m = 34.6 % of the operating result",
            "Deferred tax assets €285 m, with announced instead of enacted tax rates",
            "Slower depreciation than Caterpillar (5.5 % vs. 6.6 % of cost)"], "#FBE3E3", "var(--navy)") +
        f'<div class="card" style="left:1268px;top:236px;width:556px;height:580px;background:var(--navy);color:#fff">'
        f'<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">OUR VERDICT</div>'
        f'<div class="h" style="font-size:30px;color:#fff;margin-top:10px;line-height:1.2">Conservatism is plausible, but not proven</div>'
        f'<div style="font-size:23px;line-height:1.45;margin-top:18px">Palepu: conservative accounting can mislead too – reserves built in good years can be released in weak ones.'
        f'<br><br>That fits other provisions built up in 2023 (+€146 m) and released in 2025 (€63 m).</div></div>' +
        '<div class="pill" style="top:860px"><b>Investor lens</b> The measurable effects make 2025 look better: margin 1.6–2.8 % instead of 2.8 %</div>'))


def reliability_j13(slides, frame, hdr, sec):
    rows = [("Profitability", [
                ("Operating margin 2.8 %", "Reversals 143, slower depreciation, own work 317, other expenses without note", "Overstated", "1.6–2.8 % in the scenarios", "bias"),
                ("Pre-tax margin 3.0 %", "Finance result not split; fair value gains 55 = 12.6 % of profit before tax", "Mixed", "–", "bias"),
                ("Net margin 1.8 %, ROE 3.0 %", "Tax rate 37.8–99.2 %, no reconciliation", "Volatile", "after tax +0.08 pp vs. pre-tax −2.14 pp", "no")]),
            ("Efficiency", [
                ("DIO 157.5", "Overhead at undefined normal capacity, allowance not disclosed", "Value possibly overstated", "not measurable", "rel"),
                ("DSO 73.8", "Contract assets inside, allowance and guarantees not disclosed", "Exposure understated", "not measurable", "bias"),
                ("DPO 28.6", "Trade payables taken from note 7", "None", "–", "rel"),
                ("Fixed asset turnover 3.49", "Depreciation 5.5 % vs. 6.6 % at Caterpillar", "Understated vs. CAT", "4.76 at CAT's rate (CAT 4.74)", "bias")]),
            ("Leverage", [
                ("Equity ratio 53.5 %, D/E 0.40", "Pension assumptions, guarantees, depreciation", "Slightly overstated", "50.4 % at CAT's rate", "bias"),
                ("Interest cover", "Finance result without interest component", "Not computable", "indicator 3.90 (2022: 11.07)", "no")]),
            ("Liquidity", [
                ("Current 2.31, quick 1.16", "Securities 1,568 at fair value; Cat Financial at CAT", "Moves with markets", "fair value loss 209 in 2022", "rel")])]
    use = {"rel": _tag("Reliable", "#E3F1E4", "#1E6B2A", 15), "bias": _tag("With bias", "#FFF4C2", "#6B5300", 15), "no": _tag("Not usable", "#FBE3E3", "#A11B1B", 15)}
    trs = ""
    for g, items in rows:
        for i, (r, f, d, sz, u) in enumerate(items):
            gcell = f'<td class="g" rowspan="{len(items)}">{g}</td>' if i == 0 else ""
            trs += f'<tr>{gcell}<td style="font-weight:700">{r}</td><td>{f}</td><td>{d}</td><td>{sz}</td><td>{use[u]}</td></tr>'
    table = ('<table class="rt"><tr><th>Group</th><th style="width:300px">Ratio 2025</th><th>Finding of chapter 4</th><th style="width:230px">Direction</th>'
             f'<th style="width:300px">Size where measurable</th><th style="width:140px">Use</th></tr>{trs}</table>')
    slides.append(frame(0, "Report §6.3, Table J13; Excel workbook, sheets C1, C2, D3–D7, D9 and D11. Liebherr 2025, € m",
        scope("tJ13", [(".rt", "font-size:20px"), (".rt td", "padding:14px 10px;line-height:1.25"), ("td.g", "width:150px;font-size:17px;color:var(--navy)")]) +
        hdr(sec, "How far the key ratios can be trusted", "Table J13 by ratio group – what the accounting analysis does to each ratio") +
        f'<div class="tJ13" style="position:absolute;left:96px;top:236px;width:1728px">{table}</div>'))


def common_size(slides, frame, hdr, card, sec):
    def bars(items, mx):
        out = ""
        for lab, v, hl in items:
            w = max(v / mx * 380, 4)
            out += (f'<div style="display:flex;align-items:center;gap:12px;margin:7px 0"><div style="width:250px;font-size:20px;font-weight:{800 if hl else 600}">{lab}</div>'
                    f'<div style="height:26px;width:{w:.0f}px;background:{"var(--y)" if hl else "#C4C8CD"};border-radius:4px"></div>'
                    f'<div style="font-size:21px;font-weight:800">{v:.1f} %</div></div>')
        return out
    bs = bars([("Inventories", 36.3, True), ("PP&amp;E", 24.6, False), ("Cash", 18.0, False), ("Trade receivables", 17.8, False), ("Equity", 53.5, True), ("Current debt", 7.0, False)], 55)
    pl = bars([("Cost of materials", 52.7, False), ("Personnel", 28.6, True), ("Other items (net)", 12.0, False), ("Depreciation", 4.0, False), ("Operating profit", 2.8, True)], 55)
    hz = [("Personnel expense", "+5.3 %", True), ("Operating profit", "−38.7 %", True), ("Trade receivables", "+9.1 %", True), ("Current debt", "+26.3 %", True),
          ("Inventories", "−1.0 %", False), ("Revenue", "+1.0 %", False)]
    hzh = "".join(f'<div style="display:flex;justify-content:space-between;font-size:21px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.18)">'
                  f'<span>{a}</span><b style="color:{"var(--y)" if h else "#fff"}">{v}</b></div>' for a, v, h in hz)
    slides.append(frame(0, "Excel workbook, sheets D1 (vertical and horizontal analysis) and D2; Report §5.2 and §6.1. Liebherr, recast statements",
        hdr(sec, "Common size: stock and staff dominate, profit is a sliver", "Vertical analysis 2025 (balance sheet in % of total assets, P&amp;L in % of revenue) and horizontal change 2024 → 2025") +
        f'<div class="card" style="left:96px;top:236px;width:740px;height:330px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)"><div class="ctitle">Balance sheet, % of total assets</div>{bs}</div>' +
        f'<div class="card" style="left:96px;top:586px;width:740px;height:290px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)"><div class="ctitle">Income statement, % of revenue</div>{pl}</div>' +
        f'<div class="card" style="left:866px;top:236px;width:460px;height:640px;background:var(--navy);color:#fff"><div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">HORIZONTAL 2024 → 2025</div><div style="margin-top:10px">{hzh}</div></div>' +
        card(1356, 236, 468, 640, "Why we recast", "Published, the cost of materials fell from <b>60.0 %</b> of revenue (2022) to <b>54.6 %</b> (2025) – as if vertical integration paid off.<br><br>"
             "Recast – with the change in inventories and own work capitalised in the cost line – it stayed at <b>52.7–53.2 %</b>.<br><br>The “saving” was the stock build of 2022 and 2023.", "white")))


def levers_and_changes(slides, frame, hdr, card, ul, sec):
    lv = [("1", "Demand", "Construction and mining −5.5 % in 2025; European construction about +2 % a year to 2028; no significant upswing before 2027", "Threats: US tariffs, customer financing costs, low-price competitors"),
          ("2", "Margin", "Each percentage point = €148 m of operating profit at 2025 revenue", "Threats: tariffs, cost of autonomous and electrified machines"),
          ("3", "Working capital", "10 days less cash conversion cycle = about €405 m released", "But only once – lasting free cash flow needs margin")]
    lvh = "".join(f'<div style="position:absolute;left:96px;top:{236 + i * 216}px;width:840px;height:200px;background:#fff;border-radius:14px;box-shadow:0 4px 16px rgba(0,24,46,.08);display:flex;align-items:center;gap:20px;padding:0 24px">'
                  f'<div class="big" style="min-width:64px;height:64px;border-radius:50%;background:var(--y);display:flex;align-items:center;justify-content:center;font-size:32px">{n}</div>'
                  f'<div><div class="h" style="font-size:27px">{t}</div><div style="font-size:21px;line-height:1.35;margin-top:4px">{d}</div>'
                  f'<div style="font-size:18px;color:var(--muted);margin-top:4px">{th}</div></div></div>' for i, (n, t, d, th) in enumerate(lv))
    slides.append(frame(0, "Report chapter 7 (three levers) and chapter 8 (changes to monitor, due diligence), sections 3.2.1, 3.3.3, 4.1, 5.2–5.7",
        hdr(sec, "Three levers and three changes to monitor", "Chapter 7: what drives future performance · chapter 8: what Liebherr would have to change") +
        '<div style="position:absolute;left:96px;top:236px;width:840px;font-size:0"></div>' + lvh +
        f'<div class="card" style="left:966px;top:236px;width:858px;height:440px;background:var(--navy);color:#fff">'
        f'<div style="font-size:18px;font-weight:800;letter-spacing:2px;color:var(--y)">THREE CHANGES TO MONITOR IN 2026</div>'
        f'<div style="margin-top:16px">{ul(["<b>Personnel costs follow orders and revenue</b> – a falling personnel ratio (28.6 % → towards 26.4 %)", "<b>Capex prioritised by expected return</b> and within operating cash flow over time – not simply cut", "<b>A shorter cash conversion cycle</b> – but it releases cash once, so lasting free cash flow also needs the margin"], 24)}</div></div>' +
        card(966, 696, 858, 184, "Due diligence", "Request <b>segment results and assets</b> – without them capital allocation across 13 segments cannot be assessed.", "yellow")))


def monitor_table3(slides, frame, hdr, sec):
    rows = [("Operating margin", "2.8 %", "At least 3.9 %, without large provision releases", True),
            ("Free cash flow", "−€176 m", "Positive and, over time, covering distributions", True),
            ("Information", "Summary statements only", "Audited statements and composition of other operating expenses", True),
            ("Personnel expenses / revenue", "28.6 %", "Falling back towards 26.4 % (2023)", False),
            ("Other operating expenses / revenue", "14.7 %", "Back towards 13.3 % (2024), composition disclosed", False),
            ("Capex / operating cash flow", "190.2 % (2022–2025)", "Below 100 % over a rolling four-year period", False),
            ("Cash conversion cycle", "202.7 days", "At least 10 days shorter as a first step", False),
            ("Net financial position", "€249 m", "Stays positive", False),
            ("Bank and lease liabilities / EBITDA", "2.90×", "Back towards the industry's 2.30×", False),
            ("ROCE before tax", "3.5 %", "Rising towards 7.70 % – needs a margin of about 6–8 %", False)]
    trs = "".join(f'<tr style="{"background:#FFF8D6" if c else ""}"><td style="font-weight:700">{a}</td><td class="n">{b}</td><td>{t}</td>'
                  f'<td>{_tag("Condition", "var(--navy)", "#FFCF00", 15) if c else _tag("Signal", "#E9EBEE", "#3A444E", 15)}</td></tr>' for a, b, t, c in rows)
    table = ('<table class="rt"><tr><th>Indicator</th><th style="width:300px;text-align:center">2025</th><th>Threshold or signal</th>'
             f'<th style="width:150px">Type</th></tr>{trs}</table>')
    slides.append(frame(0, "Report chapter 8, Table 3; Excel workbook, sheets C2, D1, D3, D5–D8, D10 and D11; Damodaran (2026a, 2026b). Thresholds are the judgement of the report",
        scope("tT3", [(".rt", "font-size:23px"), (".rt td", "padding:17px 14px")]) +
        hdr(sec, "What to check in the 2026 statements", "Table 3 – three conditions for a reassessment and seven supporting signals (not automatic triggers)") +
        f'<div class="tT3" style="position:absolute;left:96px;top:236px;width:1728px">{table}</div>'))


QA4 = [("What is the sustainable growth rate?", "ROE × (1 − payout ratio) = 2.4 % in 2025. Faster growth needs better returns, lower capital intensity or outside financing."),
       ("Does the advice differ by investor?", "Risk-averse: equity unsuitable, a loan may fit better. Long-term: not yet. Risk-seeking: only at a price that reflects the risk – without influence as a minority."),
       ("Why is the pre-tax margin above the operating margin?", "3.0 % against 2.8 %: the finance result was positive in 2025 (+€24 m), partly fair value gains on securities (€55 m)."),
       ("Which DSO do you quote?", "73.8 days on average balances (ratio table) or 77 days on year-end balances (strategy chapter) – say which basis."),
       ("What is not on the balance sheet?", "Guarantees for customer financing – the volume is not disclosed in any year, so receivables understate the credit exposure.")]

NOTES = {
    "conservative": ("Backup C – Conservative or aggressive?", "—", "The report gives no simple answer, because the evidence points both ways. On the conservative side, development costs are never capitalised, and the usual incentives to inflate profit are absent, because Liebherr is unlisted and family-owned, with no share-based pay and no disclosed covenant. On the other side, own work capitalised equals 77 per cent of the operating result, provision reversals 34.6 per cent, and deferred tax assets are recognised at announced rather than enacted rates. So conservatism is plausible but not proven. Palepu reminds us that conservative accounting can mislead as well, because reserves built in good years can be released in weak ones, which fits the other provisions built up in 2023 and released in 2025."),
    "j13": ("Backup C – Reliability of ratios", "—", "Table J13 shows what the accounting analysis does to each ratio, grouped like our ratio slides. For profitability, the operating margin trend is reliable, but its level is overstated on the measured items, so the scenarios range from 1.6 to 2.8 per cent. Net margin and after-tax return on equity are not usable because of the tax charge. For efficiency, inventory and payable days measure the capital tied up, not its quality. For leverage, the equity ratio is slightly overstated, about 50 per cent at Caterpillar's depreciation rate, and interest cover cannot be computed. Liquidity is reliable for the Liebherr trend."),
    "common": ("Backup D – Common size", "—", "The common-size balance sheet shows that inventories are 36.3 per cent of total assets and equity 53.5 per cent. In the income statement, materials take 52.7 per cent of revenue and personnel 28.6 per cent, so only 2.8 per cent is left as operating profit. The horizontal analysis shows personnel costs up 5.3 per cent while revenue grew 1 per cent, and operating profit down 38.7 per cent. The recast matters here. As published, the materials ratio fell from 60.0 to 54.6 per cent, but after the recast it stayed between 52.7 and 53.2 per cent, so the apparent saving was only the stock build."),
    "levers": ("Backup E – Levers and changes", "—", "Chapter 7 names three levers for future performance. The first is demand, which is weak until 2027. The second is the margin, where each point is worth 148 million euro. The third is working capital, where ten days less release about 405 million euro, but only once. From these, chapter 8 derives three changes to monitor. Personnel costs should follow orders and revenue, capital expenditure should be prioritised by expected return and stay within operating cash flow over time, and the cash conversion cycle should shorten. In due diligence the investor should also request segment results and assets."),
    "table3": ("Backup E – What to check in 2026", "—", "Table 3 lists the indicators for a reassessment. The first three rows are the conditions, namely a margin of at least 3.9 per cent, positive free cash flow that covers distributions, and information rights. The other rows are supporting signals, not automatic triggers. These are a personnel ratio falling back towards 26.4 per cent, other operating expenses back towards 13.3 per cent, capex below 100 per cent of operating cash flow over four years, a cash conversion cycle at least ten days shorter, a positive net financial position, debt to EBITDA back towards 2.30, and a ROCE rising towards the 7.70 per cent benchmark."),
    "qa4": ("Backup F – Questions 4/4", "—", "The sustainable growth rate is return on equity times one minus the payout ratio, so 2.4 per cent. The advice depends on the investor. For a risk-averse investor equity is unsuitable and a loan may fit better, for our long-term investor the answer is not yet, and a risk-seeking investor would need a price that reflects the risk. The pre-tax margin is above the operating margin because the finance result was positive in 2025. Days sales outstanding are 73.8 on average balances or 77 on year-end balances, so always say which basis you quote. And the guarantees for customer financing are not on the balance sheet, and their volume is not disclosed."),
}
