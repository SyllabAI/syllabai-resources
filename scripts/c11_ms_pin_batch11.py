#!/usr/bin/env python3
"""T-C11 session 66 — extract the batch-11 (S4 Organic, THIRD slice: g
Esters + h Synthetic polymers) slice-relevant PMT Unit-4 Paper-2 mark
scheme to a pinned text file under scripts/c11_evidence/ (the same
"=== PAGE N ===" convention as the pilot/batch-1..10 pins —
c11_ms_pin_batch10.py pattern, batch-11-scoped).

Batch-11 slice = S4-g Esters (4.38C-4.43C incl. the 4.43C practical) +
S4-h Synthetic polymers (4.44-4.50C) = 13 authorable SPs (one
practical-typed: the 4.43C ethyl-ethanoate preparation, carried by the
scoped T-C10 practical 4CH1-PR-12 — the batch-3 1.60C/PR-04 precedent).
Commissioned by the operator's "commission batch 11" directive (2026-09-25,
session 66) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml); the S4 slice plan (batches 9-11) is
recorded in the session-62 commissioning record. Batch 11 completes S4.

Coverage note: the S4-h family has exactly ONE Paper-2 MS file in this
corpus — "Synthetic Polymers MS.pdf" — pinned here as
SYNTHETIC_POLYMERS_MS_P2.txt. There is NO dedicated Esters Paper-2 MS
file in this corpus, so the slice's mark-scheme documentation surface is
the SYNTHETIC_POLYMERS pin plus the two ALREADY-PINNED files the
session-64 future-boundary notes routed to batch 11: the Alkenes MS
Q2(c) polymer-drawing Reject row ('Any double-bonded product scores
0/2' — recorded in the session-64 ruling as BATCH-11's mint evidence)
and the Crude Oil MS condensation-polymerisation/disposal surfaces
(CRUDE_OIL_MS_P2.txt, pinned at the batch-3 crude-oil slice). A
PARTIAL-coverage shape — the batch-3/4/10 precedent. Paper-1 variants
remain unpinned per the Paper-2-first convention batches 2-10
established.

This script ONLY extracts text from a PDF already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: SYNTHETIC_POLYMERS_MS_P2.txt. Idempotent: an existing pin is
skipped.
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

PINS = [
    ("Synthetic Polymers MS.pdf", "SYNTHETIC_POLYMERS_MS_P2.txt"),
]


def sha1_12(p: Path) -> str:
    import hashlib
    return hashlib.sha1(p.read_bytes()).hexdigest()[:12]


def main() -> int:
    OUT.mkdir(exist_ok=True)
    ok = True
    for pdf_name, txt_name in PINS:
        pdf = MS / pdf_name
        txt = OUT / txt_name
        if not pdf.exists():
            print(f"FAIL-CLOSED: missing PDF {pdf}")
            ok = False
            continue
        if txt.exists():
            print(f"SKIP {txt_name} (exists — idempotent)")
            continue
        info = subprocess.run(["pdfinfo", str(pdf)], capture_output=True,
                              text=True).stdout
        pages = next((ln.split(":")[1].strip() for ln in info.splitlines()
                      if ln.startswith("Pages:")), "?")
        parts = []
        for p in range(1, int(pages) + 1):
            r = subprocess.run(
                ["pdftotext", "-f", str(p), "-l", str(p), str(pdf), "-"],
                capture_output=True, text=True)
            parts.append(f"=== PAGE {p} ===\n" + r.stdout)
        txt.write_text("\n".join(parts), encoding="utf-8")
        print(f"PINNED {txt_name}: source={pdf_name} "
              f"sha1_12={sha1_12(pdf)} pages={pages}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
