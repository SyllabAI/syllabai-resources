#!/usr/bin/env python3
"""T-C11 session 62 — extract the batch-9 (S4 Organic, FIRST slice: a
Introduction + b Crude Oil & Fuels + c Alkanes) slice-relevant PMT Unit-4
Paper-2 mark schemes to pinned text files under scripts/c11_evidence/ (the
same "=== PAGE N ===" convention as the pilot/batch-1..8 pins —
c11_ms_pin_batch8.py pattern, batch-9-scoped).

Batch-9 slice = 4CH1-4.1-4.22 minus the 4CH1-4.15 negative-control carve-out
(21 authorable SPs: S4-a 4.1-4.6 + S4-b 4.7-4.18 [11 authorable] + S4-c
4.19-4.22; none practical-typed — the 4.43C practical belongs to batch 11's
slice). Commissioned by the operator's "commission a new section" directive
(2026-09-24, session 62) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml); the S4 slice plan (batches 9-11) is
recorded in the session-62 commissioning record.

Coverage note: the S4-a/b/c families have TWO Paper-2 MS files in this
corpus — "Crude Oil MS.pdf" (covers the introduction + crude oil/fuels
surfaces) and "Alkanes MS.pdf" (covers the alkane family) — pinned here as
CRUDE_OIL_MS_P2.txt and ALKANES_MS_P2.txt. This keeps FULL Paper-2 coverage
for the slice (two families, two pins — the batch-7 FULL shape). Paper-1
variants (the 1/2/3/4-suffixed MS files) remain unpinned per the
Paper-2-first convention batches 2-8 established. The Alkenes/Synthetic
Polymers MS files belong to batches 10-11 and stay unpinned here.

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: CRUDE_OIL_MS_P2.txt, ALKANES_MS_P2.txt. Idempotent: existing
pins skipped.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MS = (REPO / "PMT Edexcel IGCSE Chemistry Resources" / "Unit 4"
      / "Mark Schemes" / "Paper 2")
OUT = HERE / "c11_evidence"

TARGETS = [
    ("Crude Oil MS.pdf", "CRUDE_OIL_MS_P2.txt"),
    ("Alkanes MS.pdf", "ALKANES_MS_P2.txt"),
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
