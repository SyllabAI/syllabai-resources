"""Phase 1 PDF inspection for YPH11 SB1 (T-PARSE-YPH11-1), per books/README.md §5.

Expected per lane README: 225 pages, image-only print replica (~150 DPI,
one full-page image per page, zero text layer) -> OCR route mandatory.
Confirms: page count, producer, text layer on sampled pages, images/page,
outline shape, page geometry (spot any 2-up spreads like 4BI1's).
"""
import fitz  # PyMuPDF
import hashlib

PDF = "/home/z/my-project/data/yph11_sb1.pdf"

sha = hashlib.sha256(open(PDF, "rb").read()).hexdigest()
print(f"sha256 = {sha}")
print(f"pinned = aa1aed604d627fda8a46cf67bd562234b2934abe9d26690e1bf38c27f9c015d0")
print(f"match  = {sha == 'aa1aed604d627fda8a46cf67bd562234b2934abe9d26690e1bf38c27f9c015d0'}")

doc = fitz.open(PDF)
print(f"\npages = {doc.page_count}")
print(f"metadata producer = {doc.metadata.get('producer')!r}")
print(f"metadata creator  = {doc.metadata.get('creator')!r}")

print("\n--- text layer census (sampled) ---")
samples = [1, 5, 10, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 225]
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
