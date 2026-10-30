"""Backup slides 13-29 (not part of the 10-minute talk), in the style of the main deck.

Content follows the team's Canva backup outline (DAHZeoU9vLQ); every figure is taken from the
report and the workbook.
"""
import charts as C

INDEX = 13  # slide number of the backup index


def add_backup(slides, frame, band, dots):
    def hdr(section, title, sub=""):
        return band(f"Backup · {section}", title, sub) + (
            f'<a class="backlink" data-goto="{INDEX}" style="position:absolute;right:96px;top:36px;font-size:18px;font-weight:800;'
            f'letter-spacing:2px;color:var(--navy);text-decoration:none;border:2px solid var(--navy);border-radius:20px;padding:4px 14px">◂ INDEX</a>')

    def card(x, y, w, h, title, body, kind="white", tag=None):
        bg, fg, tc, sh = {"white": ("#fff", "var(--navy)", "var(--navy)", "0 6px 24px rgba(0,24,46,.10)"),
                          "navy": ("var(--navy)", "#fff", "var(--y)", "none"),
                          "yellow": ("var(--y)", "var(--navy)", "var(--navy)", "none"),
                          "grey": ("var(--light)", "var(--navy)", "var(--navy)", "none")}[kind]
        top = "border-top:10px solid var(--y);" if kind == "white" else ""
        t = f'<span class="tag" style="background:{tag[1]};color:{tag[2]};margin-bottom:10px">{tag[0]}</span>' if tag else ""
        return (f'<div class="card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{bg};color:{fg};box-shadow:{sh};{top}">'
                f'{t}<div class="h" style="font-size:30px;color:{tc};margin-bottom:14px;line-height:1.2">{title}</div>'
                f'<div style="font-size:24px;line-height:1.4">{body}</div></div>')

    def ul(items, size=24):
        return '<ul class="b">' + "".join(f'<li style="font-size:{size}px;margin-bottom:14px">{i}</li>' for i in items) + "</ul>"

    def kpi(x, y, w, big, label, kind="white"):
        bg, fg = {"white": ("#fff", "var(--navy)"), "navy": ("var(--navy)", "#fff"), "yellow": ("var(--y)", "var(--navy)")}[kind]
        return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:170px;background:{bg};color:{fg};border-radius:16px;'
                f'padding:20px 24px;box-shadow:0 6px 24px rgba(0,24,46,.10)"><div class="big" style="font-size:52px;color:inherit">{big}</div>'
                f'<div style="font-size:21px;font-weight:700;line-height:1.3;margin-top:4px;opacity:.85">{label}</div></div>')

    # ---------------------------------------------------------------- 13 Backup index
    rows = [("A", "Business model and environment", "DESTEP · Porter's five forces · VRIO and SWOT", 14, "yellow"),
            ("B", "Accounting analysis", "Red flags · room for judgement · adjustments · reliability of ratios", 17, "navy"),
            ("C", "Financial analysis", "Growth and costs · DuPont · liquidity and benchmark · cash flow", 21, "yellow"),
            ("D", "Recommendation, scenarios and risks", "Why 3.9 % is a trigger · scenarios · risks and drop trigger", 25, "navy"),
            ("E", "Likely questions and answers", "Six short answers for the Q&amp;A", 28, "yellow")]
    body = "".join(
        f'<a data-goto="{g}" style="position:absolute;left:96px;top:{270 + i * 128}px;width:1300px;height:108px;display:flex;align-items:center;gap:30px;'
        f'background:#fff;border-radius:16px;box-shadow:0 6px 24px rgba(0,24,46,.10);text-decoration:none;color:var(--navy);cursor:pointer">'
        f'<div class="big" style="width:108px;height:108px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:54px;'
        f'background:{"var(--y)" if k == "yellow" else "var(--navy)"};color:{"var(--navy)" if k == "yellow" else "var(--y)"}">{L}</div>'
        f'<div><div class="h" style="font-size:30px">{t}</div><div style="font-size:21px;color:var(--muted);margin-top:4px">{d}</div></div>'
        f'<div style="margin-left:auto;margin-right:34px;font-size:22px;font-weight:800">Slides {g}–{[16, 20, 24, 27, 29][i]} ▸</div></a>'
        for i, (L, t, d, g, k) in enumerate(rows))
    slides.append(frame(INDEX, None, f"""
{band('Backup', 'Backup slides for the questions', 'Not part of the 10-minute talk – click a section to jump there')}
{body}
<div class="card" style="left:1440px;top:270px;width:384px;height:620px;background:var(--navy);color:#fff">
  <div style="font-size:19px;font-weight:800;letter-spacing:2px;color:var(--y)">HOW TO USE</div>
  <div style="font-size:25px;line-height:1.45;margin-top:14px">Each backup slide answers one likely question in depth.<br><br>Every slide links back here with <b style="color:var(--y)">◂ INDEX</b>.<br><br>All figures come from the report and the Excel workbook.</div>
</div>"""))

    # ---------------------------------------------------------------- A1 DESTEP
    destep = [("Economic", "European construction equipment market +4.6 % in 2025, +2 to 2.5 % expected for 2026 – while Liebherr's construction and mining revenue fell 5.5 %.", "yellow"),
              ("Political", "US tariffs cut Liebherr's North American crane revenue in 2025. Caterpillar expected a tariff impact of $2,600 m in 2026.", "navy"),
              ("Social", "Construction had 792 fatal accidents at work in the EU in 2023, 24.0 % of the total. Safety becomes a purchase criterion.", "white"),
              ("Technological", "Autonomous and electrified machines. EU Regulation 2023/1230 covers autonomous functions from 20 January 2027.", "navy"),
              ("Ecological", "EU emission limits for non-road machinery and the target of at least 55 % net emission cuts by 2030 make low-emission machines a purchase criterion.", "white"),
              ("Demographic", "Shortages of skilled workers and machine operators push costs up. Personnel expenses reached 28.6 % of revenue in 2025.", "yellow")]
    cards = "".join(card(96 + (i % 3) * 586, 250 + (i // 3) * 318, 556, 296, t, b, k) for i, (t, b, k) in enumerate(destep))
    slides.append(frame(14, "Report §3.1.1; CECE (2026), Eurostat (2025), European Union (2023), Liebherr-International AG (2026), Caterpillar Inc. (2026)",
                        hdr("A | Business model", "Environment: a modest recovery, but costs rise first", "DESTEP scan") + cards))

    # ---------------------------------------------------------------- A2 Porter
    forces = [("New entrants", "Moderate, rising", "#F6C343", "Chinese producers enter with cheaper, simplified machines. Mobile and crawler crane revenue fell 6.8 % in 2025."),
              ("Supplier power", "Moderate, rising", "#F6C343", "Cost of materials is 52.7 % of revenue. Electrification shifts power to battery and electronics suppliers."),
              ("Buyer power", "High, stable", "#D9534F", "Receivables rose 9.1 % against revenue growth of 1.0 % in 2025. About half of fleet owners may reconsider their brands by 2028."),
              ("Substitutes", "Low to moderate, rising", "#7FB77E", "Renting and automation change how much equipment is needed. The rental fleet took €305 m, 28.8 % of 2025 investment."),
              ("Rivalry", "High, rising", "#D9534F", "The fixed cost of staying in the market rises. The operating margin fell from 4.6 % in 2024 to 2.8 % in 2025.")]
    rws = "".join(
        f'<div style="position:absolute;left:96px;top:{248 + i * 124}px;width:1728px;height:108px;background:#fff;border-radius:14px;box-shadow:0 4px 16px rgba(0,24,46,.08);display:flex;align-items:center">'
        f'<div style="width:330px;padding-left:28px"><div class="h" style="font-size:28px">{f}</div></div>'
        f'<div style="width:300px"><span style="display:inline-block;background:{c};color:var(--navy);font-weight:800;font-size:19px;padding:8px 16px;border-radius:20px">{r}</span></div>'
        f'<div style="flex:1;font-size:23px;line-height:1.35;padding-right:30px">{e}</div></div>'
        for i, (f, r, c, e) in enumerate(forces))
    slides.append(frame(15, "Report §3.1.2, Table 1; ratings are the judgement of the report",
                        hdr("A | Business model", "Competitive forces squeeze the margin", "Porter's five forces") + rws +
                        '<div class="pill" style="top:880px"><b>Investor lens</b> Limited industry profit potential – consistent with the fall to 2.8 %</div>'))

    # ---------------------------------------------------------------- A3 VRIO + SWOT
    vrio = ul(["<b>Sustained advantage:</b> in-house key technologies (40+ production sites in 16 countries), application engineering (R&amp;D €708 m, 4.8 % of revenue), family ownership with permanent capital (equity ratio 53.5 %)",
               "<b>Parity only:</b> wholly-owned sales and service network, decentralised divisional structure",
               "<b>Temporary to sustained:</b> internal capital market"], 24)
    sw = [("Strengths", "Vertical integration · equity ratio 53.5 % · 13 segments", "#E3F1E4"),
          ("Weaknesses", "Margin 2.8 % vs. 17.2 % at Caterpillar · operating cash flow €1,171 m → €530 m · no segment disclosure", "#FBE3E3"),
          ("Opportunities", "Low-emission and automated machines · European market +4.6 % in 2025", "#FFF4C2"),
          ("Threats", "Low-price competitors from China · US tariffs · transition costs for new drives and autonomy", "#E9EBEE")]
    swot = "".join(f'<div style="position:absolute;left:{1000 + (i % 2) * 418}px;top:{250 + (i // 2) * 316}px;width:398px;height:296px;background:{c};border-radius:16px;padding:24px 26px">'
                   f'<div class="h" style="font-size:28px;margin-bottom:10px">{t}</div><div style="font-size:23px;line-height:1.4">{b}</div></div>' for i, (t, b, c) in enumerate(sw))
    slides.append(frame(16, "Report §3.2 and §3.4, Tables E1 and D1",
                        hdr("A | Business model", "Hard-to-copy resources – locked in the asset base", "VRIO and SWOT") +
                        card(96, 250, 870, 612, "VRIO: what is hard to copy", vrio, "navy") + swot))

    # ---------------------------------------------------------------- B1 Red flags
    flags = ul(["<b>Provision reversals:</b> €143 m in 2025, 34.6 % of the operating result if credited within it",
                "<b>Receivables vs. revenue:</b> receivables +9.1 % against revenue +1.0 % in 2025",
                "<b>Profit vs. tax:</b> effective tax rate 99.2 %, 45.1 %, 58.2 % and 37.8 % (2022–2025), no reconciliation",
                "<b>Impairment:</b> €55 m in 2023, six times the level of the other years"])
    rest = ul(["<b>Clean:</b> no off-balance-sheet arrangements disclosed · same auditor (Ernst &amp; Young), no qualified opinion · no change of policy or estimate",
               "<b>Not testable:</b> related party transactions (no note in four years) · large year-end adjustments (no interim figures)"])
    tally = "".join(f'<div style="position:absolute;left:{1480}px;top:{250 + i * 208}px;width:344px;height:188px;background:{bg};color:{fg};border-radius:16px;text-align:center;padding-top:22px">'
                    f'<div class="big" style="font-size:76px;color:inherit">{n}</div><div style="font-size:22px;font-weight:800">{l}</div></div>'
                    for i, (n, l, bg, fg) in enumerate([("4", "flags raised", "var(--y)", "var(--navy)"), ("3", "clean", "#fff", "var(--navy)"), ("2", "not testable", "#5A6570", "#fff")]))
    slides.append(frame(17, "Report §4.4, Table H1; financial statements 2022–2025",
                        hdr("B | Accounting analysis", "Red-flag screen: reasons to ask, not proof", "Nine tests over four years") +
                        card(96, 250, 700, 600, "Four red flags", flags, "navy") + card(826, 250, 624, 600, "Clean or not testable", rest, "white") +
                        tally))

    # ---------------------------------------------------------------- B2 Room for judgement
    cols = [("Highest flexibility", ["Inventories: €6,341 m, 36.3 % of total assets, allowance not disclosed", "Provisions: €864 m, of which €530 m warranty", "Impairment test", "Deferred tax assets: €285 m"], "navy", ("High", "var(--y)", "var(--navy)")),
            ("Also material", ["Own work capitalised: €317 m, 77 % of the operating result", "PP&amp;E: €4,304 m, machinery written off over 5 to 21 years", "Revenue timing: advance payments €896 m, contract liabilities €289 m"], "white", ("Medium", "#FFF4C2", "#6B5300")),
            ("Lowest flexibility", ["Borrowing costs", "Lessee accounting", "Translation of foreign currency", "The standard prescribes the mechanics – little choice for management"], "grey", ("Low", "#E3F1E4", "#1E6B2A"))]
    cc = "".join(card(96 + i * 586, 250, 556, 600, t, ul(b), k, tag=(tg[0] + " flexibility", tg[1], tg[2])) for i, (t, b, k, tg) in enumerate(cols))
    slides.append(frame(18, "Report §4.2–4.3, Table G2 (30 treatments, nine of them key)",
                        hdr("B | Accounting analysis", "Where management has room for judgement", "Rated by the judgement the standard allows and the materiality of the amount") + cc))

    # ---------------------------------------------------------------- B3 Adjustments and limits
    tri = [("7", "not adjustable", "Red flags and disclosure gaps, e.g. provision reversals of €143 m, missing related party note", "navy"),
           ("5", "reversed in the workbook", "e.g. Caterpillar LIFO → FIFO: equity +$4,305 m, operating profit +$441 m; goodwill impairment 2022", "yellow"),
           ("10", "not reversible", "Disclosure too thin, e.g. undefined normal capacity, own work capitalised €317 m", "white")]
    tt = "".join(f'<div style="position:absolute;left:96px;top:{250 + i * 206}px;width:820px;height:186px;background:{ {"navy": "var(--navy)", "yellow": "var(--y)", "white": "#fff"}[k]};'
                 f'color:{"#fff" if k == "navy" else "var(--navy)"};border-radius:16px;padding:20px 28px;display:flex;gap:26px;align-items:center;box-shadow:0 6px 24px rgba(0,24,46,.10)">'
                 f'<div class="big" style="font-size:80px;min-width:110px;color:{"var(--y)" if k == "navy" else "var(--navy)"}">{n}</div>'
                 f'<div><div style="font-size:26px;font-weight:800">{l}</div><div style="font-size:22px;line-height:1.35;margin-top:4px;opacity:.9">{d}</div></div></div>'
                 for i, (n, l, d, k) in enumerate(tri))
    slides.append(frame(19, "Report chapter 4, Tables H2, H3 and J13; Excel workbook, sheets C1 and D9",
                        hdr("B | Accounting analysis", "22 findings: what we could adjust and what we could not", "Short list of the accounting analysis") + tt +
                        f'<div class="card" style="left:946px;top:250px;width:878px;height:598px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)">'
                        f'<span class="tag" style="background:#E9EBEE;color:var(--cat)">Illustrative sensitivity · not booked</span>'
                        f'<div class="h" style="font-size:27px;margin-top:12px">Liebherr operating margin 2025</div>'
                        f'<div style="position:absolute;left:30px;top:130px">{C.sensitivity(820, 340)}</div>'
                        f'<div style="position:absolute;left:30px;top:500px;width:810px;font-size:20px;line-height:1.35">The quantified effects point to a weaker result – the weakness is, if anything, understated.</div></div>'))

    # ---------------------------------------------------------------- B4 Reliability of ratios
    rel = [("Reliable", "#1E6B2A", "#E3F1E4", ["Operating margin trend", "Inventory and payable days", "Current ratio 2.31, quick ratio 1.16", "Cash conversion 53.0 % and free cash flow −€176 m"]),
           ("Usable with bias", "#6B5300", "#FFF4C2", ["Margin level 2.8 % – scenarios 1.6 % to 2.8 %", "Days sales outstanding 73.8", "Equity ratio 53.5 % (50.4 % at Caterpillar's depreciation rate)", "Fixed asset turnover 3.49"]),
           ("Not usable", "#A11B1B", "#FBE3E3", ["Net margin 1.8 % and return on equity 3.0 % – tax rate 37.8 % to 99.2 %", "Interest cover", "Comparisons with Caterpillar built on equity"])]
    rr = "".join(f'<div class="card" style="left:{96 + i * 586}px;top:250px;width:556px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10);padding:0;overflow:hidden">'
                 f'<div style="background:{bg};padding:22px 28px;display:flex;align-items:center;gap:14px"><div style="width:26px;height:26px;border-radius:50%;background:{fg}"></div>'
                 f'<div class="h" style="font-size:28px;color:{fg}">{t}</div></div><div style="padding:24px 28px">{ul(b)}</div></div>' for i, (t, fg, bg, b) in enumerate(rel))
    slides.append(frame(20, "Report §6.3, Table J13; 2025 figures; Excel workbook, sheets D3 and D9",
                        hdr("B | Accounting analysis", "How far the key ratios can be trusted", "After the accounting analysis the ratios fall into three groups") + rr))

    # ---------------------------------------------------------------- C1 Growth and cost structure
    yrs = [("2022", "12,589", "454", "3.6 %"), ("2023", "14,042", "619", "4.4 %"), ("2024", "14,622", "674", "4.6 %"), ("2025", "14,772", "413", "2.8 %")]
    yt = "".join(f'<div style="position:absolute;left:{96 + i * 438}px;top:250px;width:414px;height:190px;background:{"var(--y)" if i == 3 else "#fff"};border-radius:16px;padding:20px 26px;box-shadow:0 6px 24px rgba(0,24,46,.10)">'
                 f'<div style="font-size:22px;font-weight:800;opacity:.7">{y}</div><div class="big" style="font-size:44px;margin-top:4px">{m}</div>'
                 f'<div style="font-size:22px;font-weight:700;line-height:1.4;margin-top:6px">Revenue €{r} m<br>Operating profit €{o} m</div></div>' for i, (y, r, o, m) in enumerate(yrs))
    slides.append(frame(21, "Report §5.2; Excel workbook, sheets D1 and D6",
                        hdr("C | Financial analysis", "Growth and cost structure 2022–2025", "Operating margin per year, with revenue and operating profit") + yt +
                        card(96, 470, 852, 380, "Where growth stalled", ul(["Revenue growth 11.5 % (2023) → 4.1 % (2024) → 1.0 % (2025)", "Construction and mining −5.5 % to €9,345 m", "Other segments +14.7 % to €5,427 m, components +35.5 %"]), "white") +
                        card(972, 470, 852, 380, "Where the margin went", ul(["Personnel expense +5.3 % to €4,226 m vs. revenue +1.0 %", "Personnel share of revenue 26.4 % (2023) → 28.6 % (2025)", "Other operating items cost another 1.25 pp", "Each margin point = €148 m operating profit"]), "navy")))

    # ---------------------------------------------------------------- C2 DuPont
    slides.append(frame(22, "Report §5.3, Figure 2a, Table J4; Excel workbook, sheets D4 and D6 (logarithmic split)",
                        hdr("C | Financial analysis", "DuPont: the margin, not leverage, drives returns down", "Pre-tax return on equity 2023 → 2025") +
                        f'<div class="card" style="left:96px;top:250px;width:1100px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)">'
                        f'<div class="ctitle">Contributions to the change in pre-tax ROE, percentage points</div>'
                        f'<div style="position:absolute;left:30px;top:80px">{C.dupont(1040, 490)}</div></div>' +
                        card(1226, 250, 598, 600, "What it means",
                             ul(["<b>Profitability −2.89 pp:</b> lower pre-tax margin", "<b>Efficiency −0.20 pp:</b> slightly lower asset turnover", "<b>Leverage +0.28 pp:</b> more debt even helped a little",
                                 "After tax, ROE was 3.0 % vs. 16.4 % in the US industry – but the tax charge is volatile, so the trend is read before tax"]), "navy")))

    # ---------------------------------------------------------------- C3 Liquidity, solvency, benchmark
    tbl = [("Operating margin", "2.8 %", "15.9 %", "17.2 %"), ("EBITDA margin", "6.8 %", "19.6 %", "19.8 %"), ("Return on equity", "3.0 %", "16.4 %", "38.1 %*"),
           ("Inventories, % of revenue", "42.9 %", "16.6 %", "33.2 %"), ("Debt / EBITDA", "2.90", "2.30", "3.52")]
    trs = "".join(f'<tr><td style="padding:22px 18px;font-weight:700">{a}</td><td style="text-align:center;background:#FFF4C2;font-weight:800">{b}</td>'
                  f'<td style="text-align:center">{c}</td><td style="text-align:center">{d}</td></tr>' for a, b, c, d in tbl)
    table = (f'<table style="width:100%;border-collapse:collapse;font-size:26px"><tr style="font-size:19px;letter-spacing:1px">'
             f'<th style="text-align:left;padding:12px 18px;background:var(--navy);color:#fff">2025</th><th style="background:var(--y);padding:12px">LIEBHERR</th>'
             f'<th style="background:#D0D3D8;padding:12px">US INDUSTRY</th><th style="background:var(--cat);color:#fff;padding:12px">CATERPILLAR</th></tr>{trs}</table>'
             f'<div style="font-size:19px;color:var(--muted);margin-top:18px">* Not comparable – Caterpillar\'s equity is reduced by treasury shares. Caterpillar on the FIFO basis.</div>')
    slides.append(frame(23, "Report §5.1 and §5.5, Table J14; Damodaran (2026), US machinery industry, January 2026; Excel workbook, sheets D3, D7 and D10",
                        hdr("C | Financial analysis", "Strong solvency, far weaker returns", "Liquidity, solvency and benchmark 2025") +
                        card(96, 250, 760, 600, "Balance sheet strength", ul(["Equity ratio 53.5 %; bank and lease liabilities 23.7 % of capital (industry 39.3 %)", "Cash and current financial assets €3,147 m cover current debt of €1,215 m 2.6×", "Current ratio 2.31 vs. 1.55 at Caterpillar",
                                                                               "Net financial position €523 m (2022) → net debt €85 m (2023) → €249 m (2025)", "Debt / EBITDA 2.14 → 2.90; interest cover 11.07 (2022) → 3.90 (2025)"], 22), "white") +
                        f'<div class="card" style="left:886px;top:250px;width:938px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)">{table}</div>'))

    # ---------------------------------------------------------------- C4 Cash flow and capital allocation
    kp = kpi(96, 250, 414, "190.2 %", "Capex in % of operating cash flow, 2022–2025", "navy") + kpi(534, 250, 414, "−€1,151 m", "Free cash flow in total, 2022–2025") + \
         kpi(972, 250, 414, "28.4 %", "of EBITDA became operating cash flow, 2022–2025 (53.0 % in 2025)") + kpi(1410, 250, 414, "€530 m", "Operating cash flow 2025, down from €1,171 m (2024)", "yellow")
    slides.append(frame(24, "Report §5.6, Figure 4; Excel workbook, sheets D5, D7 and D10",
                        hdr("C | Financial analysis", "Liebherr invests ahead of its cash", "Cash flow and capital allocation") + kp +
                        card(96, 450, 852, 400, "Liebherr invests ahead of its cash", ul(["Capex and R&amp;D 9.6 % of revenue vs. 7.4 % at Caterpillar – at a margin of 2.8 % vs. 17.2 %", "Shortfall after distributions €388 m (2023–2025)", "Bank and lease liabilities +€562 m (2022–2025)"]), "white") +
                        card(972, 450, 852, 400, "Caterpillar returns cash", ul(["Free cash flow $7,453 m in 2025, 11.0 % of revenue", "73.1 % of operating cash flow returned to shareholders (2022–2025)", "Liebherr distributed €56 m in 2025 – little current income for an investor"]), "navy")))

    # ---------------------------------------------------------------- D1 Why 3.9 % is only a trigger
    kp = kpi(96, 250, 414, "3.9 %", "Average operating margin 2022–2025 (3.86 %)", "yellow") + kpi(534, 250, 414, "+€157 m", "Operating profit at 2025 revenue (€14,772 m)") + \
         kpi(972, 250, 414, "3.5 %", "ROCE before tax 2025 vs. 7.70 % after-tax benchmark") + kpi(1410, 250, 414, "6–8 %", "Operating margin needed to earn the benchmark", "navy")
    slides.append(frame(25, "Report §5.3 and §5.7, chapter 8; Excel workbook, sheets D3 and D10; Damodaran (2026a)",
                        hdr("D | Recommendation", "Why 3.9 % is only a trigger, not a target", "Condition 1 of the reassessment") + kp +
                        card(96, 450, 852, 400, "What the trigger means", ul(["A return to 3.9 % is the first realistic sign of recovery – Liebherr has earned it on average", "It is a test, not a target return", "Each margin point is worth €148 m"]), "white") +
                        card(972, 450, 852, 400, "Why it is not enough", ul(["Even in 2024, at a 4.6 % margin, ROCE was only 5.9 % before tax – below the 7.70 % benchmark", "The benchmark is the US machinery industry, not Liebherr's own cost of capital", "A margin recovery alone does not prove an adequate return"]), "navy")))

    # ---------------------------------------------------------------- D2 Scenarios
    sc = [("2025 actual", 2.80, 413, ""), ("Four-year average", 3.86, 570, "+€157 m"), ("Best year 2024", 4.61, 681, "+€268 m"), ("US industry average", 15.86, 2343, "+€1,930 m")]
    bars = "".join(f'<div style="margin-bottom:34px"><div style="font-size:24px;font-weight:700">{n} · {m:.2f} % margin</div>'
                   f'<div style="display:flex;align-items:center;gap:14px;margin-top:8px"><div class="sbar" style="height:46px;width:{max(v / 2343 * 600, 8):.0f}px;background:{"#D0D3D8" if i == 3 else ("var(--y)" if i else "var(--cat)")};border-radius:4px"></div>'
                   f'<div style="font-size:27px;font-weight:800">€{v:,} m</div><div style="font-size:23px;font-weight:700;color:#1E6B2A">{d}</div></div></div>' for i, (n, m, v, d) in enumerate(sc))
    slides.append(frame(26, "Report Table J15; Excel workbook, sheet D10. Margins Liebherr has earned or the industry average – nothing is assumed",
                        hdr("D | Recommendation", "What the scenarios are worth", "Operating profit at 2025 revenue (€14,772 m) – illustrations, not forecasts") +
                        f'<div class="card" style="left:96px;top:250px;width:1000px;height:600px;background:#fff;box-shadow:0 6px 24px rgba(0,24,46,.10)"><div class="ctitle" style="margin-bottom:20px">Margin scenarios</div>{bars}'
                        f'<div style="font-size:20px;color:var(--muted)">The industry figure shows the size of the gap and is not a target.</div></div>' +
                        card(1126, 250, 698, 600, "Cash scenarios (2025)", ul(["Free cash flow −€176 m: the net financial position of €249 m covers it 1.4 years", "After distributions (−€232 m): 1.1 years", "Capex at the level of depreciation (€587 m): +€119 m, free cash flow still −€57 m", "Cash conversion cycle 10 days shorter: €405 m released once"]), "navy")))

    # ---------------------------------------------------------------- D3 Risks and drop trigger
    risks = [("Demand", "Construction and mining revenue −5.5 % in 2025; no significant upswing expected before 2027"),
             ("Costs", "US tariffs and the cost of autonomous and electrified machines press on the margin"),
             ("Information", "The largest cost increase of 2025 cannot be explained from the summary statements"),
             ("Valuation", "Not assessed in the report – price and contract rights decide the case")]
    rk = "".join(card(96 + i * 438, 250, 414, 290, t, b, "white") for i, (t, b) in enumerate(risks))
    slides.append(frame(27, "Report §5.5, §5.7, §6.1 and chapter 8",
                        hdr("D | Recommendation", "Risks, limits and when to drop the case", "What could still go wrong – and the alternative for a cautious investor") + rk +
                        card(96, 570, 852, 280, "Alternative for a risk-averse investor", "Equity is unsuitable: low payout, shares not traded. A loan may fit better, as equity of 53.5 % limits the default risk – but pricing, maturity, collateral and covenants are not disclosed.", "grey") +
                        card(972, 570, 852, 280, "Drop trigger", "If the margin stays near 2.8 % in 2026 <b>and</b> the net financial position turns negative, the investor should drop the case rather than wait for 2027. A recovery should not rest on large provision releases.", "navy")))

    # ---------------------------------------------------------------- E1 / E2 Q&A
    def qa(n, title, sub, qs, src):
        qq = "".join(f'<div style="position:absolute;left:96px;top:{250 + i * 206}px;width:1728px;height:186px;background:#fff;border-radius:16px;box-shadow:0 6px 24px rgba(0,24,46,.10);display:flex;overflow:hidden">'
                     f'<div style="width:520px;background:{"var(--y)" if i % 2 == 0 else "var(--navy)"};color:{"var(--navy)" if i % 2 == 0 else "#fff"};padding:24px 30px;display:flex;align-items:center;gap:18px">'
                     f'<div class="big" style="font-size:54px;color:inherit;opacity:.5">Q</div><div class="h" style="font-size:29px;color:inherit;line-height:1.2">{q}</div></div>'
                     f'<div style="flex:1;padding:22px 32px;display:flex;align-items:center"><div style="font-size:24px;line-height:1.42">{a}</div></div></div>' for i, (q, a) in enumerate(qs))
        slides.append(frame(n, src, hdr("E | Likely questions", title, sub) + qq))
    qa(28, "Why not invest now?", "Likely questions (1/2)",
       [("Why not invest now?", "Neither financial condition was met in 2025: the margin of 2.8 % is below its four-year average of 3.9 %, and free cash flow was −€176 m. The answer is <b>not yet</b>, rather than no."),
        ("Why is 3.9 % the first test?", "It is the average Liebherr earned from 2022 to 2025 – a realistic first sign of recovery. At 2025 revenue it adds €157 m of operating profit. A trigger, not a target return."),
        ("Is the LIFO to FIFO adjustment fair?", "IAS 2 does not permit LIFO, so FIFO puts both groups on one basis. Caterpillar's LIFO reserve of $4,305 m lifts its margin only from 16.50 % to 17.15 % – the gap stays large.")],
       "Report chapters 4 to 8; Excel workbook, sheets C1, D3 and D10")
    qa(29, "What the balance sheet cannot fix", "Likely questions (2/2)",
       [("What do the red flags mean?", "They are reasons to ask, not proof of manipulation. Four flags are raised, three tests are clean and two cannot be run on the published statements – that is why information rights come first."),
        ("Why is ROCE so low?", "ROCE is 3.5 % before tax against a 7.70 % after-tax benchmark: the margin is only 2.8 %, and inventories of 42.9 % of revenue and a cash cycle 77 days longer than Caterpillar's tie up capital."),
        ("Why is a strong balance sheet not a return?", "An equity ratio of 53.5 % and a net financial position of €249 m limit the risk, but do not earn the cost of capital. They would cover a shortfall like 2025 (−€232 m) for about 1.1 years.")],
       "Report chapters 4 to 8; Excel workbook, sheets C1, D3 and D10")


BACKUP_NOTES = [
    ("Backup index", "—", "Backup slides, not part of the 10-minute talk. Use them to answer questions: A covers the business model, B the accounting analysis, C the financial analysis, D the recommendation and scenarios, E likely questions. Click a section to jump there; every backup slide links back to this index."),
    ("Backup A – DESTEP", "—", "The DESTEP scan shows a modest European recovery from 2026, set against higher financing costs, tariff uncertainty and a technology and labour transition that raises costs before it raises prices. Economic and political factors carry the largest near-term risk, technological and ecological factors the largest long-term opportunity. A market recovery alone does not show that the margin recovers."),
    ("Backup A – Five forces", "—", "Buyer power and rivalry are high, the threat of new entrants and supplier power are moderate and rising, and substitutes are a low to moderate threat. The industry profit potential is therefore limited and squeezed from the customer side and by low-cost entrants. This is consistent with the fall of the operating margin to 2.8 per cent in 2025 against 17.2 per cent at Caterpillar."),
    ("Backup A – VRIO and SWOT", "—", "The VRIO test shows that in-house technology, application engineering and family capital are sustained advantages, while the sales and service network is only at parity, because Caterpillar's independent dealers provide comparable access. The SWOT sums it up: vertical integration and the equity ratio are the strengths that matter, the weakness is the margin and the weakening internal funding, the opportunity is demand for low-emission and automated machines, and the threats are low-price competitors and tariffs."),
    ("Backup B – Red flags", "—", "We ran nine red-flag tests over four years. Four raised a flag, three came back clean and two cannot be run. The flags are the provision reversals of 143 million euro, receivables growing faster than revenue, an effective tax rate between 37.8 and 99.2 per cent without a reconciliation, and the impairment of 55 million euro in 2023. The tests that cannot be run are related party transactions and year-end adjustments. Red flags are reasons to ask, not proof of manipulation."),
    ("Backup B – Room for judgement", "—", "Flexibility is rated on two criteria: the degree of judgement the standard permits and the materiality of the amount. It is highest for inventories and their allowance, the impairment test, the provisions and deferred tax assets. Own work capitalised, property, plant and equipment and revenue timing follow. It is lowest where the standard prescribes the mechanics, as with borrowing costs, lessee accounting and currency translation."),
    ("Backup B – Adjustments and limits", "—", "The short list holds 22 accounting findings. Seven are red flags or disclosure gaps that no adjustment can remove, five were reversed in the workbook, and ten cannot be reversed because the disclosure is too thin. The quantified effects make the 2025 result look better, not worse: the operating margin of 2.8 per cent falls to between about 1.6 and 2.7 per cent in the measured scenarios, so the weakness is, if anything, understated."),
    ("Backup B – Reliability of ratios", "—", "After the accounting analysis the ratios fall into three groups. Reliable are the trend of the operating margin, inventory and payable days, liquidity and cash conversion. Usable with a stated bias are the level of the margin, days sales outstanding, fixed asset turnover and the equity ratio. Not usable for a conclusion are the net margin and the return on equity as a trend, interest cover and every comparison with Caterpillar built on equity."),
    ("Backup C – Growth and costs", "—", "Revenue growth slowed from 11.5 per cent in 2023 to 1.0 per cent in 2025. The slowdown came from construction and mining, which fell 5.5 per cent, while the other segments grew 14.7 per cent. The margin fell from 4.6 to 2.8 per cent because personnel expense grew 5.3 per cent against revenue growth of 1.0 per cent, and other operating items added to the burden. Each margin point is worth 148 million euro."),
    ("Backup C – DuPont", "—", "We read the return on equity before tax because the tax charge is volatile. The pre-tax return fell from 7.6 per cent in 2023 to 4.8 per cent in 2025. The DuPont decomposition assigns 2.89 percentage points of the fall to the lower pre-tax margin and 0.20 points to lower asset turnover, while higher leverage added 0.28 points. Leverage is therefore not the cause – the margin is."),
    ("Backup C – Liquidity and benchmark", "—", "Solvency is the clearest strength, with an equity ratio of 53.5 per cent and a current ratio of 2.31. The cushion is shrinking, though: the net financial position fell from 523 million euro in 2022 to a net debt of 85 million in 2023 and stood at 249 million in 2025, and debt to EBITDA rose to 2.90, above the industry's 2.30. Against the industry and Caterpillar, margins and returns are far lower and inventories tie up much more capital. Caterpillar's return on equity is not comparable because of its treasury shares."),
    ("Backup C – Cash flow", "—", "Cash flow is the weakest part of the figures. From 2022 to 2025 capital expenditure equalled 190.2 per cent of operating cash flow and free cash flow totalled minus 1,151 million euro. Operating cash flow fell from 1,171 million euro in 2024 to 530 million in 2025. Liebherr spends more than Caterpillar relative to revenue but earns a far lower margin, and borrowing helped fund investment and distributions. Caterpillar generated free cash flow of 7,453 million dollars and returned 73.1 per cent of its operating cash flow to shareholders."),
    ("Backup D – Why 3.9 %", "—", "The margin of 3.9 per cent is the four-year average and therefore a realistic first test of recovery. At 2025 revenue it would add 157 million euro of operating profit. It is a trigger, not a target return: even in 2024, at a margin of 4.6 per cent, the return on capital employed was 5.9 per cent before tax, below the 7.70 per cent after-tax benchmark. Earning the benchmark would need a margin of about 6 to 8 per cent. The benchmark is that of listed US machinery companies, not Liebherr's own cost of capital."),
    ("Backup D – Scenarios", "—", "The margin scenarios apply margins Liebherr has already earned to the revenue of 2025 – illustrations on published figures, not forecasts. The industry margin shows the size of the gap and is not a target. On the cash side the net financial position of 249 million euro covers the free cash flow shortfall of 176 million euro for 1.4 years and the shortfall after distributions for 1.1 years. Capital expenditure at the level of depreciation would improve free cash flow by 119 million euro, but it would still be negative at minus 57 million. Ten fewer days in the cash conversion cycle would release about 405 million euro, once."),
    ("Backup D – Risks and drop trigger", "—", "Demand, tariffs and the cost of new technology are the main external risks. Financing is not the immediate constraint, but prolonged underperformance would make it one. The investor needs information rights because the largest cost increase of 2025 cannot be explained. The report does not assess a valuation. For a risk-averse investor an equity stake is unsuitable and a loan might fit better in principle, but its terms are not disclosed. The drop trigger is a margin near 2.8 per cent in 2026 together with a negative net financial position."),
    ("Backup E – Questions 1/2", "—", "Answer 1 is the recommendation in short. Answer 2 explains why the four-year average is only a first test. Answer 3 shows that the adjustment of Caterpillar to FIFO is small compared with the gap in margin."),
    ("Backup E – Questions 2/2", "—", "The red flags are reasons to ask. ROCE is low because of the low margin and the capital tied up in inventories. The balance sheet protects the investor, but it cannot replace better returns and cash conversion."),
]
