#!/usr/bin/env python3
"""T-C11 session 59 — extract the batch-7 (S2 Inorganic, third slice)
slice-relevant PMT Unit-2 Paper-2 mark schemes to pinned text files under
scripts/c11_evidence/ (the same "=== PAGE N ===" convention as the
pilot/batch-1..6 pins — c11_ms_pin_batch6.py pattern, batch-7-scoped).

Batch-7 slice = 4CH1-2.28–2.43C (S2 subsections f Acids, Alkalis &
Titrations 2.28-2.33C, g Acids, Bases & Salt Preparations 2.34-2.43C —
16 SPs) + the two in-slice practicals 4CH1-PR-07 (2.42) and 4CH1-PR-08
(2.43C) (the practicals own their practical-type SPs per the
1.13/1.60C/2.14/2.21 precedent — no concept node attached).
Commissioned by the operator's "Proceed with batch 7" directive
(2026-09-23, session 59) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml).

Coverage note (recorded, not silent): unlike batch 6 (one partial pin),
BOTH batch-7 families have a Paper-2 MS in this corpus — "Acids, Alkalis
and Titrations MS.pdf" (family f) and "Acids, Bases and Salt Preparations
MS.pdf" (family g) — both pinned here. Paper-1 variants (the 1/2-suffixed
MS files) exist and remain unpinned per the Paper-2-first convention
batches 2-6 established. The S2-h Chemical Tests family (2.44-2.50) is
batch-8 scope — its "Chemical Tests MS.pdf" is NOT pinned here (the
batch-7 slices end at 2.43C).

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: ACIDS_ALKALIS_TITRATIONS_MS_P2.txt, ACIDS_BASES_SALT_PREP_MS_P2.txt.
Idempotent: existing pins are skipped.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MS = (REPO / "PMT Edexcel IGCSE Chemistry Resources" / "Unit 2"
      / "Mark Schemes" / "Paper 2")
OUT = HERE / "c11_evidence"

TARGETS = [
    ("Acids, Alkalis and Titrations MS.pdf", "ACIDS_ALKALIS_TITRATIONS_MS_P2.txt"),
    ("Acids, Bases and Salt Preparations MS.pdf", "ACIDS_BASES_SALT_PREP_MS_P2.txt"),
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
