"""Phase 1 PDF inspection for IAL Chemistry SB1 (YCH11 lane), per books/README.md §5.

Expected per the YPH11 sibling lane: image-only print replica (~150 DPI,
one full-page image per page, zero text layer) -> OCR route mandatory.
Confirms: page count, producer, text layer on sampled pages, images/page,
outline shape, page geometry (spot any 2-up spreads like 4BI1's).
dokumen.pub listing promises 328 pages / 2018 / ISBN 9781292244860 (L-021:
check page count against the book's own TOC promises later, not listings).
"""
import fitz  # PyMuPDF
import hashlib

PDF = "/home/z/my-project/scratch/ych11/ych11_sb1_taleem360.pdf"

sha = hashlib.sha256(open(PDF, "rb").read()).hexdigest()
print(f"sha256 = {sha}")
print(f"bytes  = {len(open(PDF, 'rb').read())}")

doc = fitz.open(PDF)
print(f"\npages = {doc.page_count}")
print(f"metadata producer = {doc.metadata.get('producer')!r}")
print(f"metadata creator  = {doc.metadata.get('creator')!r}")

print("\n--- text layer census (sampled) ---")
samples = [1, 5, 10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320, 328]
for pno in samples:
    if pno > doc.page_count:
        continue
    page = doc[pno - 1]
    txt = page.get_text("text")
    imgs = page.get_images(full=True)
    r = page.rect
    print(f"pdf {pno:3d}: chars={len(txt):4d} images={len(imgs)} size={r.width:.0f}x{r.height:.0f}")

print("\n--- outline ---")
toc = doc.get_toc()
print(f"outline entries = {len(toc)}")
for lvl, title, pg in toc[:12]:
    print(f"  L{lvl} p{pg:3d} {title[:60]!r}")

print("\n--- geometry uniformity (every 15th page) ---")
sizes = {}
for pno in range(1, doc.page_count + 1, 15):
    r = doc[pno - 1].rect
    key = (round(r.width), round(r.height))
    sizes[key] = sizes.get(key, 0) + 1
print(f"distinct page sizes: {sizes}")
doc.close()
