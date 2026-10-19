#!/usr/bin/env python3
"""Scan a PDF page range for chapter openers (LEARNING OBJECTIVES boxes) + headers."""
import subprocess, os, sys
import fitz

PDF = '/home/z/my-project/data/physics/student-book.pdf'
OUT = '/home/z/my-project/data/physics/probe'
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

def top_strip(i, frac=0.45, dpi=150):
    p = doc[i]
    r = p.rect
    clip = fitz.Rect(r.x0, r.y0, r.x1, r.y0 + r.height * frac)
    img = f'{OUT}/top_{i+1:03d}.png'
    p.get_pixmap(dpi=dpi, clip=clip).save(img)
    out = subprocess.run(['tesseract', img, 'stdout', '--psm', '3'],
                         capture_output=True, text=True).stdout
    return out

lo, hi = int(sys.argv[1]), int(sys.argv[2])
for i0 in range(lo, hi + 1):
    i = i0 - 1
    t = top_strip(i)
    tl = t.lower()
    has_obj = 'learning objectives' in tl
    # first non-empty line as title hint
    lines = [l.strip() for l in t.splitlines() if l.strip()]
    first = lines[0][:60] if lines else ''
    ch_hint = ' '.join(l for l in lines[:4] if len(l) < 40)[:70]
    flag = 'OPENER?' if has_obj else ''
    print(f'PDF {i0:3d} {flag:8s} {ch_hint}')
