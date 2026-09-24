#!/usr/bin/env python3
"""T-C11 session 61 — extract the batch-8 (S2 Inorganic, fourth slice)
slice-relevant PMT Unit-2 Paper-2 mark scheme to a pinned text file under
scripts/c11_evidence/ (the same "=== PAGE N ===" convention as the
pilot/batch-1..7 pins — c11_ms_pin_batch7.py pattern, batch-8-scoped).

Batch-8 slice = 4CH1-2.44-2.50 (S2 subsection h Chemical Tests — 7 SPs,
none practical-typed, no C-suffixed variants). Commissioned by the
operator's "Proceed with batch 8" directive (2026-09-24, session 61)
under the session-46 §16 authorization (scripts/c11_s16_authorization.yaml).

Coverage note: the single S2-h family "Chemical Tests" has one Paper-2 MS
in this corpus — "Chemical Tests MS.pdf" — pinned here as
CHEMICAL_TESTS_MS_P2.txt (the batch-7 meta anticipated this pin: "its
Chemical Tests MS.pdf is NOT pinned here"). This keeps FULL Paper-2
coverage for the slice (one family, one pin — same FULL shape as batch 7,
not the batch-6 partial). Paper-1 variants (the 1/2-suffixed MS files)
remain unpinned per the Paper-2-first convention batches 2-7 established.

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: CHEMICAL_TESTS_MS_P2.txt. Idempotent: existing pins skipped.
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
    ("Chemical Tests MS.pdf", "CHEMICAL_TESTS_MS_P2.txt"),
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
