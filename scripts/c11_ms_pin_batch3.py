#!/usr/bin/env python3
"""T-C11 session 51 — extract the batch-3 slice-relevant PMT Unit-1 Paper-2
mark schemes to pinned text files under scripts/c11_evidence/ (the same
"=== PAGE N ===" convention as the pilot/batch-1/batch-2 pins).

Batch-3 slice = 4CH1-1.37–1.60C (ionic bonding, covalent bonding, simple
molecular + giant covalent structures, metallic bonding, electrolysis) +
practical PR-04 (the 1.60C aqueous-electrolysis investigation).

Per FN-B2-1 (deferred to batch 3): "the Paper-2 variants remain unpinned
for both slices. Batch 3 should pin Paper-2." — this script pins the three
Paper-2 topic MS that exist for this slice:
  * Ionic Bonding MS.pdf (Paper 2)        — 1.37–1.43 family
  * Covalent Bonding MS.pdf (Paper 2)     — 1.44–1.51 family
  * Chemical Formulae, Equations, Calculations MS.pdf (Paper 2) — 1.39 support

Coverage note (recorded, not silent): PMT Unit 1 publishes NO metallic-
bonding or electrolysis MS (Paper 1 or Paper 2) — those families have note
evidence only in this batch; no MS misconception evidence is available for
1.52C–1.60C beyond what the pinned three-topic set covers incidentally.

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: IONIC_MS_P2.txt, COVALENT_MS_P2.txt, CFEC_MS_P2.txt.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MS = REPO / "PMT Edexcel IGCSE Chemistry Resources" / "Unit 1" / "Mark Schemes" / "Paper 2"
OUT = HERE / "c11_evidence"

TARGETS = [
    ("Ionic Bonding MS.pdf", "IONIC_MS_P2.txt"),
    ("Covalent Bonding MS.pdf", "COVALENT_MS_P2.txt"),
    ("Chemical Formulae, Equations, Calculations MS.pdf", "CFEC_MS_P2.txt"),
]


def main() -> int:
    if not MS.exists():
        print(f"FATAL: {MS} missing", file=sys.stderr)
        return 1
    for pdf_name, txt_name in TARGETS:
        pdf = MS / pdf_name
        if not pdf.exists():
            print(f"FATAL: {pdf} missing", file=sys.stderr)
            return 1
        out = OUT / txt_name
        if out.exists():
            print(f"skip (exists): {txt_name}")
            continue
        # page count via pdfinfo
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                              text=True).stdout
        pages = 0
        for line in info.splitlines():
            if line.startswith("Pages:"):
                pages = int(line.split()[-1])
        if pages <= 0:
            print(f"FATAL: no page count for {pdf_name}", file=sys.stderr)
            return 1
        chunks = []
        for p in range(1, pages + 1):
            txt = subprocess.run(
                ["pdftotext", "-f", str(p), "-l", str(p), str(pdf), "-"],
                capture_output=True, text=True).stdout
            chunks.append(f"\n=== PAGE {p} ===\n{txt}")
        out.write_text("".join(chunks), encoding="utf-8")
        print(f"wrote {txt_name} ({pages} pages, {out.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
