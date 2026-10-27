#!/usr/bin/env python3
"""T-C11 session 49 — extract the batch-2 slice-relevant PMT Unit-1 Paper-1
mark schemes to pinned text files under scripts/c11_evidence/ (the same
"=== PAGE N ===" convention as the pilot/batch-1 pins).

Batch-2 slice = 4CH1-1.13–1.24 (paper chromatography practical, atomic
structure, Periodic Table). Per FN-B1-1 the MS-mining also completes the
ECM family (ECM1/ECM3) for the 1.10–1.13 separation-technique surface.

This script ONLY extracts text from PDFs already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: ATOM1_MS_P1.txt, ATOM2_MS_P1.txt, ATOM3_MS_P1.txt,
PT_MS_P1.txt, ECM1_MS_P1.txt, ECM3_MS_P1.txt.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
MS = REPO / "PMT Edexcel IGCSE Chemistry Resources" / "Unit 1" / "Mark Schemes" / "Paper 1"
OUT = HERE / "c11_evidence"

TARGETS = [
    ("Atomic Structure 1 MS.pdf", "ATOM1_MS_P1.txt"),
    ("Atomic Structure 2 MS.pdf", "ATOM2_MS_P1.txt"),
    ("Atomic Structure 3 MS.pdf", "ATOM3_MS_P1.txt"),
    ("The Periodic Table MS.pdf", "PT_MS_P1.txt"),
    ("Elements, Compounds, Mixtures 1 MS.pdf", "ECM1_MS_P1.txt"),
    ("Elements, Compounds, Mixtures 3 MS.pdf", "ECM3_MS_P1.txt"),
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
