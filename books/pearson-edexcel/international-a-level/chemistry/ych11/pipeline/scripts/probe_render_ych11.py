"""Phase 2 visual probe renders for YCH11 SB1 (chemistry lane).

Renders selected PDF pages to PNG for agent visual inspection:
cover, front matter, TOC, chapter openers, back matter (index/glossary).
PNGs go to data/ych11_sb1/probe/ (workspace scratch, not the repo).
"""
import fitz, os, sys

PDF = "/home/z/my-project/scratch/ych11/ych11_sb1_taleem360.pdf"
OUT = "/home/z/my-project/data/ych11_sb1/probe"
os.makedirs(OUT, exist_ok=True)

pages = [int(x) for x in sys.argv[1:]] or [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 20, 23, 40, 325, 326, 327, 328, 329,
]

doc = fitz.open(PDF)
for pno in pages:
    if pno > doc.page_count:
        continue
    page = doc[pno - 1]
    pix = page.get_pixmap(dpi=110)
    fp = f"{OUT}/p{pno:03d}.png"
    pix.save(fp)
    print(f"rendered {fp} ({pix.width}x{pix.height})")
doc.close()
