#!/usr/bin/env python3
"""Inspect the chemistry PDF: pages, metadata, text layer, outline/bookmarks."""
import json
import sys

PDF = "/home/z/my-project/data/chemistry_book.pdf"

report = {}

# --- pypdf: metadata + outline ---
try:
    from pypdf import PdfReader
    reader = PdfReader(PDF)
    report["encrypted"] = reader.is_encrypted
    report["num_pages"] = len(reader.pages)
    meta = reader.metadata or {}
    report["metadata"] = {k: str(v) for k, v in meta.items()}

    def walk_outline(items, depth=0, out=None, max_depth=3):
        if out is None:
            out = []
        if depth > max_depth:
            return out
        for it in items:
            if isinstance(it, list):
                walk_outline(it, depth + 1, out, max_depth)
            else:
                try:
                    page_idx = reader.get_destination_page_number(it)
                except Exception:
                    page_idx = None
                out.append({"depth": depth, "title": str(it.title)[:80], "page": page_idx})
        return out

    try:
        ol = reader.outline
        report["outline_count"] = len(walk_outline(ol, max_depth=0))
        report["outline_sample"] = walk_outline(ol, max_depth=2)[:60]
    except Exception as e:
        report["outline_error"] = str(e)
except Exception as e:
    report["pypdf_error"] = str(e)

# --- pdfplumber: text layer check on sample pages ---
try:
    import pdfplumber
    samples = {}
    with pdfplumber.open(PDF) as pdf:
        n = len(pdf.pages)
        report["plumber_num_pages"] = n
        report["page_size"] = [round(pdf.pages[0].width, 1), round(pdf.pages[0].height, 1)]
        for idx in [0, 1, 5, 10, 20, 50, 100, 200, n // 2, n - 20]:
            if 0 <= idx < n:
                t = pdf.pages[idx].extract_text() or ""
                samples[f"page_{idx+1}"] = {
                    "chars": len(t),
                    "images": len(pdf.pages[idx].images),
                    "first_120": t[:120].replace("\n", " | "),
                }
        report["text_samples"] = samples
except Exception as e:
    report["plumber_error"] = str(e)

print(json.dumps(report, indent=1, ensure_ascii=False))
