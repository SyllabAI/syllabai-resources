#!/usr/bin/env python3
"""Probe the 4PH1 physics book: render sample pages, OCR, look for TOC/offset."""
import sys, subprocess, os
import fitz

PDF = '/home/z/my-project/data/physics/student-book.pdf'
OUT = '/home/z/my-project/data/physics/probe'
os.makedirs(OUT, exist_ok=True)

doc = fitz.open(PDF)

def ocr_page(i, dpi=200):
    p = doc[i]
    pix = p.get_pixmap(dpi=dpi)
    img = f'{OUT}/p{i+1:03d}.png'
    pix.save(img)
    r = subprocess.run(['tesseract', img, 'stdout', '--psm', '3'],
                       capture_output=True, text=True)
    return r.stdout

pages = [int(x) for x in sys.argv[1:]] or [2, 3, 4, 5, 6, 7, 8]
for i0 in pages:
    i = i0 - 1
    txt = ocr_page(i)
    print(f'===== PDF PAGE {i0} =====')
    print(txt[:1800])
    print()
