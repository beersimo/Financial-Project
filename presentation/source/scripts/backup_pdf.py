"""Standalone PDF of the backup slides (13-30) with clickable index / back links."""
import json, sys
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.generic import ArrayObject, NumberObject, NameObject

full, manifest, out = sys.argv[1:4]
FIRST = 13
r = PdfReader(full)
w = PdfWriter()
for p in r.pages[FIRST - 1:]:
    w.add_page(p)
links = [m.get("links", []) for m in json.load(open(manifest))]
k = 0.75  # 1920 x 1080 px -> 1440 x 810 pt
for i in range(len(w.pages)):
    for l in links[FIRST - 1 + i]:
        to = l["to"] - FIRST
        if not 0 <= to < len(w.pages):
            continue
        x0, y1 = l["x"] * k, 810 - l["y"] * k
        x1, y0 = (l["x"] + l["w"]) * k, 810 - (l["y"] + l["h"]) * k
        ann = Link(rect=(x0, y0, x1, y1), target_page_index=to)
        ann[NameObject("/Border")] = ArrayObject([NumberObject(0)] * 3)
        w.add_annotation(page_number=i, annotation=ann)
w.add_metadata({"/Title": "Liebherr Group – Backup slides for the Q&A"})
w.write(out)
print(len(w.pages), "pages,", sum(len(links[FIRST - 1 + i]) for i in range(len(w.pages))), "links")
