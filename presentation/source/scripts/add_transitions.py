"""Add a fade transition to every page of the PDF (played in full-screen mode, e.g. Acrobat Ctrl+L)."""
import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import DictionaryObject, NameObject, FloatObject
src, dst = sys.argv[1], sys.argv[2]
w = PdfWriter(clone_from=PdfReader(src))
for p in w.pages:
    p[NameObject("/Trans")] = DictionaryObject({NameObject("/Type"): NameObject("/Trans"),
                                                NameObject("/S"): NameObject("/Fade"),
                                                NameObject("/D"): FloatObject(0.6)})
w.write(dst)
