#!/usr/bin/env python3
"""T-C11 session 57 — extract the batch-6 (S2 Inorganic, second slice)
slice-relevant PMT Unit-2 Paper-2 mark scheme to a pinned text file under
scripts/c11_evidence/ (the same "=== PAGE N ===" convention as the
pilot/batch-1..5 pins — c11_ms_pin_batch5.py pattern, batch-6-scoped).

Batch-6 slice = 4CH1-2.15–2.27 (S2 subsections d Reactivity Series,
e Extraction & Uses of Metals — 13 SPs) + the 2.21 practical (4CH1-PR-06).
Commissioned by the operator's "commission batch 6" directive (2026-09-22,
session 57) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml).

Coverage note (recorded, not silent): PMT Unit 2 publishes exactly one
Paper-2 MS touching the batch-6 families — "Reactivity Series MS.pdf" —
pinned here as REACTIVITY_MS_P2.txt. NO PMT mark scheme exists for the
Extraction & Uses of Metals family in ANY unit of this corpus (Unit 1
principles, Unit 2 inorganic, Unit 3 physical, Unit 4 organic — verified
by directory listing 2026-09-22), so — as in batches 1-3, unlike batches
4-5 — the batch carries an UNPINNED family: misconception-class mining is
confined to the reactivity-series surface the pinned MS documents, and the
extraction/uses/alloys surfaces are note-anchored only. Recorded in the
decision record's meta.ms_coverage_note. Paper-1 variants (Reactivity
Series MS Paper 1) exist and remain unpinned per the Paper-2-first
convention batches 2-5 established.

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: REACTIVITY_MS_P2.txt.
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
    ("Reactivity Series MS.pdf", "REACTIVITY_MS_P2.txt"),
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
