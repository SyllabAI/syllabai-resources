#!/usr/bin/env python3
"""Probe page-number corners of the physics book."""
import subprocess, os, sys
import fitz

PDF = '/home/z/my-project/data/physics/student-book.pdf'
OUT = '/home/z/my-project/data/physics/probe'
os.makedirs(OUT, exist_ok=True)
doc = fitz.open(PDF)

def corner(i, side, dpi=300):
    p = doc[i]
    r = p.rect
    if side == 'L':
        clip = fitz.Rect(r.x0, r.y1 - r.height * 0.09, r.x0 + r.width * 0.28, r.y1)
    else:
        clip = fitz.Rect(r.x1 - r.width * 0.28, r.y1 - r.height * 0.09, r.x1, r.y1)
    pix = p.get_pixmap(dpi=dpi, clip=clip)
    img = f'{OUT}/cor_{side}_{i+1:03d}.png'
    pix.save(img)
    out = subprocess.run(['tesseract', img, 'stdout', '--psm', '7',
                          '-c', 'tessedit_char_whitelist=0123456789ivxIVX '],
                         capture_output=True, text=True).stdout.strip()
    return out

for i0 in [int(x) for x in sys.argv[1:]] or list(range(9, 20)):
    i = i0 - 1
    print(f'PDF {i0:3d}   L: {corner(i,"L")!r:22s}  R: {corner(i,"R")!r}')
