#!/usr/bin/env python3
"""Probe PDF anatomy: page count, text/image blocks, question anchors."""
import sys, hashlib
import fitz

def probe(path):
    doc = fitz.open(path)
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]
    print(f"== {path} | pages={len(doc)} | sha256[:16]={sha}")
    tot_img = tot_txt = 0
    anchors_total = []
    for pno in range(min(len(doc), 4)):
        page = doc[pno]
        d = page.get_text("dict")
        imgs = [b for b in d["blocks"] if b["type"] == 1]
        txts = [b for b in d["blocks"] if b["type"] == 0]
        tot_img += len(imgs); tot_txt += len(txts)
        print(f"  p{pno}: text_blocks={len(txts)} image_blocks={len(imgs)} page_size={tuple(round(x) for x in page.rect[2:])}")
        txt_all = page.get_text()
        import re
        anchors = re.findall(r"\(?\s*Total for (?:Question|question)\s*(\d+)[^\)]*?(\d+)\s*marks", txt_all)
        anchors2 = re.findall(r"^\s*(\d{1,2})\s*[\.\)]?\s*$", txt_all, re.M)
        marks = re.findall(r"\((\d+)\s*marks?\)", txt_all)
        print(f"     anchors 'Total for Question N': {anchors[:8]}")
        print(f"     standalone number lines: {anchors2[:12]}")
        print(f"     '(N marks)' occurrences: {len(marks)}")
        head = " | ".join(txt_all.strip().splitlines()[:8])
        print(f"     head text: {head[:220]}")
    print(f"  totals(first<=4p): images={tot_img} textblocks={tot_txt}")

for p in sys.argv[1:]:
    probe(p)
