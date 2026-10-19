#!/usr/bin/env python3
"""Batch OCR for the chemistry book. Resumable: skips pages whose .txt already exists.
Usage: python3 ocr_batch.py [start_page end_page]  (1-based inclusive)
Writes one text file per page to /home/z/my-project/data/ocr_pages/
"""
import os, sys, time
from multiprocessing import Pool

import pypdfium2 as pdfium
import pytesseract
from PIL import Image

PDF = "/home/z/my-project/data/chemistry_book.pdf"
OUT_DIR = "/home/z/my-project/data/ocr_pages"
SCALE = 3.0
TESS_CONFIG = "--oem 1 --psm 3 -l eng"

os.makedirs(OUT_DIR, exist_ok=True)

_pdf = None

def get_pdf():
    global _pdf
    if _pdf is None:
        _pdf = pdfium.PdfDocument(PDF)
    return _pdf

def ocr_page(page_no_1based: int) -> str:
    """OCR a single 1-based page, write result, return status."""
    out_path = os.path.join(OUT_DIR, f"page_{page_no_1based:03d}.txt")
    if os.path.exists(out_path) and os.path.getsize(out_path) >= 0:
        return f"skip {page_no_1based}"
    try:
        pdf = get_pdf()
        bitmap = pdf[page_no_1based - 1].render(scale=SCALE)
        img = bitmap.to_pil().convert("L")
        txt = pytesseract.image_to_string(img, lang="eng", config=TESS_CONFIG)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(txt)
        return f"done {page_no_1based} chars={len(txt)}"
    except Exception as e:
        return f"ERROR {page_no_1based}: {e}"

def init_worker():
    global _pdf
    _pdf = pdfium.PdfDocument(PDF)

if __name__ == "__main__":
    import pypdfium2 as _p
    n_pages = len(_p.PdfDocument(PDF))
    start, end = 1, n_pages
    if len(sys.argv) == 3:
        start, end = int(sys.argv[1]), int(sys.argv[2])
    pages = [p for p in range(start, end + 1)
             if not os.path.exists(os.path.join(OUT_DIR, f"page_{p:03d}.txt"))]
    print(f"total={n_pages} todo={len(pages)} range=[{start},{end}]", flush=True)
    t0 = time.time()
    with Pool(processes=2, initializer=init_worker) as pool:
        for i, status in enumerate(pool.imap_unordered(ocr_page, pages, chunksize=2)):
            if i % 20 == 0 or status.startswith("ERROR"):
                el = time.time() - t0
                print(f"[{i+1}/{len(pages)}] {el:.0f}s {status}", flush=True)
    print(f"ALL DONE in {time.time()-t0:.0f}s", flush=True)
