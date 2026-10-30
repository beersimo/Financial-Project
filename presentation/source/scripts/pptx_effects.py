"""Add a fade slide transition and automatic, staggered entrance effects to every slide of an unpacked deck.

Content layers fade in one after another as soon as the slide appears (no extra clicks needed);
chart layers wipe in from the bottom so the bars appear to grow.
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1])
TRANS = '<p:transition spd="med"><p:fade/></p:transition>'


def effect(ctn, spid, delay, chart):
    preset, sub, filt, dur = ("22", "4", "wipe(up)", 700) if chart else ("10", "0", "fade", 600)
    a, b, c = ctn, ctn + 1, ctn + 2
    return (f'<p:par><p:cTn id="{a}" presetID="{preset}" presetClass="entr" presetSubtype="{sub}" fill="hold" nodeType="withEffect">'
            f'<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>'
            f'<p:set><p:cBhvr><p:cTn id="{b}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr>'
            f'<p:to><p:strVal val="visible"/></p:to></p:set>'
            f'<p:animEffect transition="in" filter="{filt}"><p:cBhvr><p:cTn id="{c}" dur="{dur}"/>'
            f'<p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect></p:childTnLst></p:cTn></p:par>')


def click_step(ctn, spid):
    """One click: fade in a full-slide focus overlay (uses ids ctn .. ctn+4)."""
    return (f'<p:par><p:cTn id="{ctn}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
            f'<p:par><p:cTn id="{ctn + 1}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            + effect(ctn + 2, spid, 0, False).replace('nodeType="withEffect"', 'nodeType="clickEffect"').replace('dur="600"', 'dur="350"') +
            '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')


for f in sorted((root / "ppt" / "slides").glob("slide*.xml")):
    x = f.read_text(encoding="utf-8")
    pics = re.findall(r'<p:cNvPr id="(\d+)" name="([^"]+)"', x)
    layers = [(i, n) for i, n in pics if n != "Base" and not n.startswith("Focus")]
    focus = [i for i, n in pics if n.startswith("Focus")]
    timing = ""
    if layers:
        ctn, eff = 5, []
        for k, (spid, name) in enumerate(layers):
            eff.append(effect(ctn, spid, 150 + k * 250, name.startswith("Chart")))
            ctn += 3
        timing = ('<p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
                  '<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>'
                  '<p:par><p:cTn id="3" fill="hold"><p:stCondLst><p:cond delay="indefinite"/>'
                  '<p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond></p:stCondLst><p:childTnLst>'
                  '<p:par><p:cTn id="4" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                  + "".join(eff).replace('nodeType="withEffect"', 'nodeType="afterEffect"', 1) +
                  '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>'
                  + "".join(click_step(ctn + 3 * k + 2 * k, spid) for k, spid in enumerate(focus)) +
                  '</p:childTnLst></p:cTn>'
                  '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
                  '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
                  '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')
    x = x.replace("</p:clrMapOvr>", "</p:clrMapOvr>" + TRANS + timing, 1)
    f.write_text(x, encoding="utf-8")
    print(f.name, len(layers), "effects")
