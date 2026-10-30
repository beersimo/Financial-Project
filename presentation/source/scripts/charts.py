"""SVG chart helpers in the visual language of the Canva reference deck."""

Y = "#FFCF00"      # Liebherr / accent yellow
NAVY = "#00182E"   # text / dark panels
CAT = "#3A444E"    # Caterpillar
IND = "#C4C8CD"    # industry
GRID = "#E3E5E8"
MUTED = "#6B7480"
RED = "#C8102E"
GREEN = "#2E7D32"
FONT = "Assistant, Arimo, sans-serif"


def _t(x, y, s, size=22, weight=600, fill=NAVY, anchor="middle", extra=""):
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>')


def margin_lines(w=1040, h=470, show_years=True):
    """Operating margin 2022-2025: Liebherr vs Caterpillar (FIFO) + industry 2025 reference."""
    years = ["2022", "2023", "2024", "2025"]
    lh = [3.606, 4.408, 4.609, 2.796]
    cat = [16.07, 19.49, 20.85, 17.15]
    ind = 15.86
    l, r, t, b = 70, 190, 30, 60
    pw, ph = w - l - r, h - t - b
    ymax = 25
    X = lambda i: l + pw * (i + 0.5) / 4
    Yv = lambda v: t + ph * (1 - v / ymax)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    for v in range(0, 26, 5):
        o.append(f'<line x1="{l}" x2="{l+pw}" y1="{Yv(v):.1f}" y2="{Yv(v):.1f}" stroke="{GRID}" stroke-width="1.5"/>')
        o.append(_t(l - 14, Yv(v) + 7, f"{v} %", 19, 400, MUTED, "end"))
    for i, yr in enumerate(years):
        if show_years:
            o.append(_t(X(i), h - 22, yr, 22, 600, NAVY))
    # industry reference
    o.append(f'<line x1="{l}" x2="{l+pw}" y1="{Yv(ind):.1f}" y2="{Yv(ind):.1f}" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 8"/>')
    o.append(_t(l + pw + 14, Yv(ind) + 26, "Industry 15.9 %", 20, 700, MUTED, "start"))
    for data, labels, col, lab, dy in ((cat, ["16.1", "19.5", "20.9", "17.2"], CAT, "Caterpillar (FIFO)", -18),
                                       (lh, ["3.6", "4.4", "4.6", "2.8"], Y, "Liebherr", -18)):
        pts = " ".join(f"{X(i):.1f},{Yv(v):.1f}" for i, v in enumerate(data))
        o.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>')
        for i, v in enumerate(data):
            lab_v = labels[i]
            o.append(f'<circle cx="{X(i):.1f}" cy="{Yv(v):.1f}" r="10" fill="{col}" stroke="#fff" stroke-width="3"/>')
            o.append(_t(X(i), Yv(v) + dy, f"{lab_v} %", 22, 800, NAVY))
        o.append(_t(l + pw + 14, Yv(data[-1]) + (7 if col == Y else -8), lab, 20, 700, NAVY if col == Y else CAT, "start"))
    # gap bracket at 2025
    gx = X(3) + 34
    o.append(f'<line x1="{gx}" x2="{gx}" y1="{Yv(cat[3])+16:.1f}" y2="{Yv(lh[3])-16:.1f}" stroke="{NAVY}" stroke-width="2.5" marker-start="url(#a)" marker-end="url(#a)"/>')
    o.append('<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#00182E"/></marker></defs>')
    o.append(f'<rect x="{gx+10}" y="{(Yv(cat[3])+Yv(lh[3]))/2-20:.1f}" width="118" height="40" rx="20" fill="{NAVY}"/>')
    o.append(_t(gx + 69, (Yv(cat[3]) + Yv(lh[3])) / 2 + 8, "−14.4 pp", 21, 800, "#fff"))
    o.append("</svg>")
    return "".join(o)


def revenue_bars(w=560, h=300):
    vals = [12.589, 14.042, 14.622, 14.772]
    growth = ["", "+11.5 %", "+4.1 %", "+1.0 %"]
    years = ["2022", "2023", "2024", "2025"]
    l, t, b = 10, 60, 50
    pw, ph = w - 2 * l, h - t - b
    bw = pw / 4 * 0.58
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    for i, v in enumerate(vals):
        cx = l + pw * (i + 0.5) / 4
        bh = ph * v / 16
        col = Y if i == 3 else "#D0D3D8"
        o.append(f'<rect x="{cx-bw/2:.1f}" y="{t+ph-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{col}"/>')
        o.append(_t(cx, t + ph - bh - 12, f"{v:.2f}", 24, 800))
        o.append(_t(cx, h - 18, years[i], 20, 600, MUTED))
        if growth[i]:
            o.append(_t(cx, t + ph - bh + 34, growth[i], 19, 700, NAVY))
    o.append("</svg>")
    return "".join(o)


def bridge(w=560, h=300):
    steps = [("2024", 4.609, "total"), ("Materials", 0.540, "d"), ("Personnel", -1.156, "d"),
             ("D&A", 0.054, "d"), ("Other items", -1.252, "d"), ("2025", 2.796, "total")]
    l, t, b = 10, 40, 56
    pw, ph = w - 2 * l, h - t - b
    n = len(steps)
    bw = pw / n * 0.66
    ymax = 5.6
    Yv = lambda v: t + ph * (1 - v / ymax)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    run = 0
    for i, (lab, v, kind) in enumerate(steps):
        cx = l + pw * (i + 0.5) / n
        if kind == "total":
            y0, y1, col, txt = 0, v, (CAT if i == 0 else Y), f"{v:.2f} %"
            run = v
        else:
            y0, y1 = run, run + v
            col = "#7FB77E" if v > 0 else "#D9534F"
            txt = f"{v:+.2f}".replace("-", "−")
            run = y1
        top, bot = max(y0, y1), min(y0, y1)
        o.append(f'<rect x="{cx-bw/2:.1f}" y="{Yv(top):.1f}" width="{bw:.1f}" height="{max(Yv(bot)-Yv(top),3):.1f}" fill="{col}"/>')
        o.append(_t(cx, Yv(top) - 10, txt, 19, 800))
        o.append(_t(cx, h - 30, lab, 16.5, 600, MUTED))
    o.append(_t(w / 2, h - 6, "contribution in percentage points of revenue", 15, 400, MUTED))
    o.append("</svg>")
    return "".join(o)


def cash_bars(w=860, h=470):
    years = ["2022", "2023", "2024", "2025"]
    ocf = [-415, -10, 1171, 530]
    capex = [510, 579, 632, 706]
    fcf = [-925, -589, 539, -176]
    l, r, t, b = 80, 20, 40, 120
    pw, ph = w - l - r, h - t - b
    lo, hi = -600, 1300
    Yv = lambda v: t + ph * (hi - v) / (hi - lo)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    for v in range(-400, 1300, 400):
        o.append(f'<line x1="{l}" x2="{l+pw}" y1="{Yv(v):.1f}" y2="{Yv(v):.1f}" stroke="{GRID}" stroke-width="1.5"/>')
        o.append(_t(l - 12, Yv(v) + 7, f"{v:,}".replace("-", "−"), 18, 400, MUTED, "end"))
    o.append(f'<line x1="{l}" x2="{l+pw}" y1="{Yv(0):.1f}" y2="{Yv(0):.1f}" stroke="{NAVY}" stroke-width="2"/>')
    gw = pw / 4
    bw = gw * 0.3
    for i in range(4):
        cx = l + gw * (i + 0.5)
        for j, (v, col) in enumerate(((ocf[i], Y), (capex[i], CAT))):
            x = cx - bw - 4 if j == 0 else cx + 4
            y = Yv(max(v, 0)); hh = abs(Yv(v) - Yv(0))
            o.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{max(hh,3):.1f}" fill="{col}"/>')
            ly = Yv(v) - 10 if v >= 0 else Yv(v) + 26
            o.append(_t(x + bw / 2, ly, f"{v:,}".replace("-", "−"), 19, 800))
        o.append(_t(cx, h - 78, years[i], 21, 700))
        good = fcf[i] > 0
        o.append(f'<rect x="{cx-62:.1f}" y="{h-62}" width="124" height="40" rx="20" fill="{Y if good else NAVY}"/>')
        o.append(_t(cx, h - 34, f"{fcf[i]:+,}".replace("-", "−"), 21, 800, NAVY if good else "#fff"))
    o.append(_t(l - 12, h - 34, "FCF", 19, 800, NAVY, "end"))
    o.append("</svg>")
    return "".join(o)


def nfp_line(w=520, h=230):
    years = ["2022", "2023", "2024", "2025"]
    v = [523, -85, 413, 249]
    l, r, t, b = 30, 30, 40, 40
    pw, ph = w - l - r, h - t - b
    lo, hi = -230, 600
    X = lambda i: l + pw * (i + 0.5) / 4
    Yv = lambda x: t + ph * (hi - x) / (hi - lo)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    o.append(f'<line x1="{l}" x2="{l+pw}" y1="{Yv(0):.1f}" y2="{Yv(0):.1f}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="6 6"/>')
    pts = " ".join(f"{X(i):.1f},{Yv(x):.1f}" for i, x in enumerate(v))
    o.append(f'<polyline points="{pts}" fill="none" stroke="{NAVY}" stroke-width="5"/>')
    for i, x in enumerate(v):
        o.append(f'<circle cx="{X(i):.1f}" cy="{Yv(x):.1f}" r="9" fill="{Y}" stroke="{NAVY}" stroke-width="3"/>')
        o.append(_t(X(i), Yv(x) + (-16 if x > 0 else 32), f"{x:,}".replace("-", "−"), 20, 800))
        o.append(_t(X(i), h - 8, years[i], 18, 600, MUTED))
    o.append("</svg>")
    return "".join(o)


def wc_days(w=900, h=440):
    rows = [("Days inventory outstanding", 157.5, 116.5), ("Days sales outstanding", 73.8, 54.5),
            ("Days payables outstanding", 28.6, 44.9), ("Cash conversion cycle", 202.7, 126.1)]
    l, r, t = 10, 140, 10
    pw = w - l - r
    rowh = (h - t) / 4
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    for i, (lab, a, c) in enumerate(rows):
        y = t + i * rowh
        bold = i == 3
        o.append(_t(l, y + 26, lab, 22, 800 if bold else 700, NAVY, "start"))
        for j, (v, col) in enumerate(((a, Y), (c, CAT))):
            by = y + 40 + j * 30
            bw = pw * v / 210
            o.append(f'<rect x="{l}" y="{by}" width="{bw:.1f}" height="24" fill="{col}"/>')
            o.append(_t(l + bw + 10, by + 20, f"{v:.1f} days", 20, 800 if j == 0 else 600, NAVY, "start"))
    o.append("</svg>")
    return "".join(o)


def inv_share(w=520, h=270):
    rows = [("Liebherr", 42.9, Y), ("Caterpillar", 33.2, CAT), ("Industry", 16.6, IND)]
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    bw, gap, base = 110, 50, h - 40
    for i, (lab, v, col) in enumerate(rows):
        x = 30 + i * (bw + gap)
        bh = (h - 90) * v / 45
        o.append(f'<rect x="{x}" y="{base-bh:.1f}" width="{bw}" height="{bh:.1f}" fill="{col}"/>')
        o.append(_t(x + bw / 2, base - bh - 12, f"{v:.1f} %", 24, 800))
        o.append(_t(x + bw / 2, h - 10, lab, 19, 600, MUTED))
    o.append("</svg>")
    return "".join(o)


def sensitivity(w=860, h=420):
    rows = [("As reported", 2.796, "rep"),
            ("Net provision charge at 2022–2024 average", 2.4, "s"),
            ("… excluding the high 2023 charge", 2.7, "s"),
            ("Caterpillar's depreciation rate (upper bound)", 2.084, "s"),
            ("Both effects together", 1.6, "s")]
    labels = ["2.8 %", "2.4 %", "2.7 %", "2.1 %", "≈ 1.6 %"]
    l, r = 10, 110
    pw = w - l - r
    rowh = h / len(rows)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">',
         '<defs><pattern id="hatch" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="12" height="12" fill="#E9EBEE"/><line x1="0" y1="0" x2="0" y2="12" stroke="{CAT}" stroke-width="5"/></pattern></defs>']
    for i, (lab, v, kind) in enumerate(rows):
        y = i * rowh
        o.append(_t(l, y + 26, lab, 21, 700 if kind == "rep" else 600, NAVY, "start"))
        bw = pw * v / 3.2
        fill = Y if kind == "rep" else "url(#hatch)"
        o.append(f'<rect x="{l}" y="{y+38}" width="{bw:.1f}" height="30" fill="{fill}"/>')
        o.append(_t(l + bw + 12, y + 62, labels[i], 24, 800, NAVY, "start"))
    o.append("</svg>")
    return "".join(o)


def dupont(w=560, h=250):
    """Pre-tax ROE 2023 -> 2025 split into the three DuPont drivers (report §5.3)."""
    steps = [("ROE 2023", 7.6, "total", "7.6 %"), ("Profitability", -2.89, "d", "−2.89"),
             ("Efficiency", -0.20, "d", "−0.20"), ("Leverage", 0.28, "d", "+0.28"), ("ROE 2025", 4.8, "total", "4.8 %")]
    l, t, b = 10, 36, 52
    pw, ph = w - 2 * l, h - t - b
    n = len(steps)
    bw = pw / n * 0.62
    ymax = 8.6
    Yv = lambda v: t + ph * (1 - v / ymax)
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    run = 0
    for i, (lab, v, kind, txt) in enumerate(steps):
        cx = l + pw * (i + 0.5) / n
        if kind == "total":
            y0, y1, col = 0, v, (CAT if i == 0 else Y)
            run = v
        else:
            y0, y1 = run, run + v
            col = "#7FB77E" if v > 0 else "#D9534F"
            run = y1
        top, bot = max(y0, y1), min(y0, y1)
        o.append(f'<rect x="{cx-bw/2:.1f}" y="{Yv(top):.1f}" width="{bw:.1f}" height="{max(Yv(bot)-Yv(top),3):.1f}" fill="{col}"/>')
        o.append(_t(cx, Yv(top) - 9, txt, 19, 800))
        o.append(_t(cx, h - 26, lab, 16.5, 700 if i in (1, 2, 3) else 600, MUTED))
    o.append(_t(w / 2, h - 4, "pre-tax return on equity · contributions in pp", 15, 400, MUTED))
    o.append("</svg>")
    return "".join(o)


def revenue_strip(w=1050, h=190):
    """Revenue bars aligned with the year columns of margin_lines (same l/r margins)."""
    vals = [12.589, 14.042, 14.622, 14.772]
    growth = ["", "+11.5 %", "+4.1 %", "+1.0 %"]
    years = ["2022", "2023", "2024", "2025"]
    l, r, t, b = 70, 190, 34, 40
    pw, ph = w - l - r, h - t - b
    X = lambda i: l + pw * (i + 0.5) / 4
    bw = pw / 4 * 0.42
    o = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">']
    o.append(f'<line x1="{l}" x2="{l+pw}" y1="{t+ph}" y2="{t+ph}" stroke="{NAVY}" stroke-width="2"/>')
    for i, v in enumerate(vals):
        bh = ph * v / 15.5
        col = Y if i == 3 else "#D0D3D8"
        o.append(f'<rect x="{X(i)-bw/2:.1f}" y="{t+ph-bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" fill="{col}"/>')
        o.append(_t(X(i), t + ph - bh - 10, f"€{v:.2f} bn", 21, 800))
        if growth[i]:
            o.append(_t(X(i), t + ph - bh / 2 + 7, growth[i], 19, 800, NAVY))
        o.append(_t(X(i), h - 8, years[i], 22, 700, NAVY))
    o.append(_t(l + pw + 14, t + ph / 2 + 7, "Revenue", 20, 700, NAVY, "start"))
    o.append("</svg>")
    return "".join(o)
