"""Phase 2 helper: render YPH11 SB1 pages to PNG for visual structure probing."""
import fitz
import sys

PDF = "/home/z/my-project/data/yph11_sb1.pdf"
OUT = "/home/z/my-project/data/yph11_sb1/probe_png"

import os
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)
pages = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else list(range(1, 13)) + [210, 215, 218, 220, 222, 224, 225]
for pno in pages:
    page = doc[pno - 1]
    pix = page.get_pixmap(matrix=fitz.Matrix(1.3, 1.3))
    path = f"{OUT}/p{pno:03d}.png"
    pix.save(path)
    print(f"{path} {pix.width}x{pix.height}")
doc.close()
