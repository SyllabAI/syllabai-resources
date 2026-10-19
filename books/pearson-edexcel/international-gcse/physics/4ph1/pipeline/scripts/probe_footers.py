#!/usr/bin/env python3
"""Probe footers of physics book pages to find book-page = pdf-page offset."""
import subprocess, os, sys
import fitz

PDF = '/home/z/my-project/data/physics/student-book.pdf'
OUT = '/home/z/my-project/data/physics/probe'
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

def footer(i, dpi=220):
    """OCR bottom 12% strip of page i (0-based)."""
    p = doc[i]
    r = p.rect
    clip = fitz.Rect(r.x0, r.y1 - r.height * 0.12, r.x1, r.y1)
    pix = p.get_pixmap(dpi=dpi, clip=clip)
    img = f'{OUT}/foot_{i+1:03d}.png'
    pix.save(img)
    out = subprocess.run(['tesseract', img, 'stdout', '--psm', '6'],
                         capture_output=True, text=True).stdout
    return ' | '.join(l.strip() for l in out.splitlines() if l.strip())

def header(i, dpi=220):
    """OCR top 10% strip."""
    p = doc[i]
    r = p.rect
    clip = fitz.Rect(r.x0, r.y0, r.x1, r.y0 + r.height * 0.10)
    pix = p.get_pixmap(dpi=dpi, clip=clip)
    img = f'{OUT}/head_{i+1:03d}.png'
    pix.save(img)
    out = subprocess.run(['tesseract', img, 'stdout', '--psm', '6'],
                         capture_output=True, text=True).stdout
    return ' | '.join(l.strip() for l in out.splitlines() if l.strip())

for i0 in [int(x) for x in sys.argv[1:]] or [10, 11, 12, 13, 14, 15]:
    i = i0 - 1
    print(f'PDF {i0:3d}  HEAD: {header(i)[:70]:70s}  FOOT: {footer(i)[:70]}')
