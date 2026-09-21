#!/usr/bin/env python3
"""T-C11 session 55 — extract the batch-5 (S2 Inorganic, first slice)
slice-relevant PMT Unit-2 Paper-2 mark schemes to pinned text files under
scripts/c11_evidence/ (the same "=== PAGE N ===" convention as the
pilot/batch-1..4 pins — the established FN-B2-1-closing machinery, now
applied to Section 2).

Batch-5 slice = 4CH1-2.1–2.14 (S2 subsections a Group 1 (Alkali Metals),
b Group 7 (Halogens), c Gases in the Atmosphere — 14 SPs) + the 2.14
practical (4CH1-PR-05). Commissioned by the operator's "run batch 5"
directive (2026-09-22, session 55) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml).

Coverage note (recorded, not silent): PMT Unit 2 publishes exactly one
Paper-2 MS per batch-5 family — Group 1 (Alkali Metals), Group 7
(Halogens), Gases in the Atmosphere — ALL pinned here, so (as in batch 4,
unlike batches 1-3) no batch-5 family is left without pinned mark-scheme
evidence. Paper-1 variants (Group 1, Group 7 1/2, Gases in the Atmosphere)
exist and remain unpinned per the Paper-2-first convention batches 2-4
established (a future evidence pass can extend them; the misconception-
class mining this batch needs is fully covered by the pinned three).

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: GROUP1_MS_P2.txt, GROUP7_MS_P2.txt, GASES_MS_P2.txt.
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
    ("Group 1 (Alkali Metals) - Lithium, Sodium, Potassium MS.pdf",
     "GROUP1_MS_P2.txt"),
    ("Group 7 (Halogens) - Chlorine, Bromine, Iodine MS.pdf",
     "GROUP7_MS_P2.txt"),
    ("Gases in the Atmosphere MS.pdf", "GASES_MS_P2.txt"),
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
