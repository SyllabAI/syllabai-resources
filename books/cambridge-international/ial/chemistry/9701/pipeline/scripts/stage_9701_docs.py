#!/usr/bin/env python3
"""stage_9701_docs.py — render full_book md + parse_report + parsed/README for the 9701 lane."""
import json, os, sys, collections, hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9701 import BOOK_TITLE, AUTHOR, PDF_PAGES_TOTAL

CORPUS = "/home/z/my-project/download/rag_9701/cie_a_level_chemistry_9701_chunks_v1.jsonl"
LANE = "/home/z/my-project/syllabai-resources/books/cambridge-international/ial/chemistry/9701"

recs = [json.loads(l) for l in open(CORPUS, encoding="utf-8")]

# ---- full markdown ----
md = [f"# {BOOK_TITLE} — {AUTHOR}", ""]
last = None
for c in recs:
    key = c["chapter_no"]
    if key != last:
        md.append(f"\n## {c['chapter_title']}\n")
        last = key
    if c["section"] and c["text"].split("\n\n")[0] != c["section"]:
        md.append(f"\n#### {c['section']}")
    md.append(c["text"])
md_path = os.path.join(os.path.dirname(CORPUS), "full_book_textlayer.md")
with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md))

# ---- report ----
types = collections.Counter(c["content_type"] for c in recs)
sizes = sorted(c["char_count"] for c in recs)
sha = hashlib.sha256(open(os.path.join(LANE, "source/student-book.pdf"), "rb").read()).hexdigest()
sub = sum(1 for c in recs if any(x in c["text"] for x in "₀₁₂₃₄₅₆₇₈₉"))
sup = sum(1 for c in recs if any(x in c["text"] for x in "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺"))
report = {
    "book": BOOK_TITLE,
    "author": AUTHOR,
    "qual_code": "CIE 9701 (2017 line, exams from 2022)",
    "source_pdf": "source/student-book.pdf",
    "source_sha256": sha,
    "source_pages": PDF_PAGES_TOTAL,
    "source_class": "regenerated/accessibility re-layout (DejaVu/STIX, single column, 9.2pt body)",
    "extractor": "PyMuPDF dict-mode span-pool assembly (extract_9701.py) — no OCR",
    "corpus": "cie_a_level_chemistry_9701_chunks_v1.jsonl",
    "n_chunks": len(recs),
    "content_types": dict(types),
    "size_min": sizes[0], "size_median": sizes[len(sizes)//2], "size_max": sizes[-1],
    "unicode_subscript_chunks": sub,
    "unicode_superscript_chunks": sup,
    "decisions": {
        "D-1": "pdf-page-anchored: the re-layout carries NO printed page numbers (TOC numberless, no edge digits, zero 'page N' self-refs) — book_pages=None on all chunks",
        "D-2": "margin features (Study tip / Link / Extension) are absent from this render as text — types tip/cross_link/extension_work not emitted",
        "D-3": "watermark (WeChat CLASS0608 ad overlay, pdf 31+66) stripped at line level; validator asserts zero CJK/CLASS0608",
        "D-4": "sub/superscripts rebuilt from span geometry (6.9pt spans offset vs 9.2pt baseline); stacked isotope pairs ordered sup-before-sub: ⁵²₂₄Cr²⁺",
        "D-5": "chapter map = 30 LEARNING INTENTIONS openers + P1 (pdf 522) + P2 (pdf 870) + appendices/acks; TOC used for titles only",
        "D-6": "'images' alt-text junk lines (32) dropped; 22 residual <80-char fragments accepted for v1 (2%)",
    },
}
rep_path = os.path.join(os.path.dirname(CORPUS), "parse_report_v1.json")
json.dump(report, open(rep_path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"md: {md_path} ({os.path.getsize(md_path)} B)")
print(f"report: {rep_path}")
print(json.dumps({k: report[k] for k in ("n_chunks", "size_median", "unicode_subscript_chunks")}, indent=1))
