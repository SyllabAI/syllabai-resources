#!/usr/bin/env python3
"""Tesseract fallback for pages that break the Docling 2.33 pipeline (18-19).
Writes the same page JSON schema so the chunker treats them uniformly."""
import json, os, subprocess, sys
import fitz

PDF = '/home/z/my-project/data/physics/student-book.pdf'
OUT = '/home/z/my-project/data/physics/docling_pages'
OFFSET = 10
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

for pno in [int(x) for x in sys.argv[1:]] or [18, 19]:
    p = doc[pno - 1]
    img = f'/tmp/fb_{pno}.png'
    p.get_pixmap(dpi=260).save(img)
    txt = subprocess.run(['tesseract', img, 'stdout', '--psm', '3'],
                         capture_output=True, text=True).stdout
    items = []
    for block in txt.split('\n\n'):
        block = block.strip()
        if not block:
            continue
        items.append({'label': 'text', 'text': block, 'bbox': None})
    rec = {'pdf_page': pno, 'book_page': pno - OFFSET, 'items': items,
           'parser': 'tesseract-fallback'}
    with open(f'{OUT}/page_{pno:03d}.json', 'w') as f:
        json.dump(rec, f, ensure_ascii=False)
    print(f'page {pno}: {len(items)} blocks, {len(txt)} chars')
