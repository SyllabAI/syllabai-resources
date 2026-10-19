#!/usr/bin/env python3
"""T-C11 session 52 — extract the batch-4 (S3 Physical Chemistry)
slice-relevant PMT Unit-3 Paper-2 mark schemes to pinned text files under
scripts/c11_evidence/ (the same "=== PAGE N ===" convention as the
pilot/batch-1/batch-2/batch-3 pins — the established FN-B2-1-closing
machinery, now applied to Section 3).

Batch-4 slice = 4CH1-3.1–3.22C (Energetics, Rates of Reaction,
Reversibility & Equilibria — 22 SPs) + the 3.8/3.15/3.16 practicals.
Commissioned by the operator's session-52 directive: "Then move immediately
to Batch 4 ... Batch 4 = Section 3 — Physical Chemistry. Use the
established machinery."

Coverage note (recorded, not silent): PMT Unit 3 publishes exactly one
Paper-2 MS per S3 family — Energetics, Rates of Reaction, Reversible
Reactions and Equilibria — ALL pinned here, so unlike batches 1-3 there is
no unpinned Paper-2 family for this slice. Paper-1 variants (Energetics,
Rates 1/2/3, Reversible Reactions and Equilibria) exist and remain
unpinned by the same Paper-2-first convention batches 2-3 established
(a future evidence pass can extend them; the misconception-class mining
this batch needs is fully covered by the pinned three).

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: ENERGETICS_MS_P2.txt, RATES_MS_P2.txt, RRE_MS_P2.txt.
Idempotent: existing pins are skipped.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MS = (REPO / "PMT Edexcel IGCSE Chemistry Resources" / "Unit 3"
      / "Mark Schemes" / "Paper 2")
OUT = HERE / "c11_evidence"

TARGETS = [
    ("Energetics MS.pdf", "ENERGETICS_MS_P2.txt"),
    ("Rates of Reaction MS.pdf", "RATES_MS_P2.txt"),
    ("Reversible Reactions and Equilibria MS.pdf", "RRE_MS_P2.txt"),
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
