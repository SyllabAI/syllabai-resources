#!/usr/bin/env python3
"""T-C11 session 64 — extract the batch-10 (S4 Organic, SECOND slice: d
Alkenes + e Alcohols + f Carboxylic acids) slice-relevant PMT Unit-4
Paper-2 mark scheme to a pinned text file under scripts/c11_evidence/ (the
same "=== PAGE N ===" convention as the pilot/batch-1..9 pins —
c11_ms_pin_batch9.py pattern, batch-10-scoped).

Batch-10 slice = S4-d Alkenes (4.23-4.28) + S4-e Alcohols (4.29C-4.33C) +
S4-f Carboxylic acids (4.34C-4.37C) = 15 authorable SPs (none
practical-typed — the 4.43C practical belongs to batch 11's slice).
Commissioned by the operator's "commission batch 10" directive (2026-09-25,
session 64) under the session-46 §16 authorization
(scripts/c11_s16_authorization.yaml); the S4 slice plan (batches 9-11) is
recorded in the session-62 commissioning record.

Coverage note: the S4-d/e/f families have exactly ONE Paper-2 MS file in
this corpus — "Alkenes MS.pdf" (the Unit-4 Paper-2 pack covers the alkene
surfaces incl. the bromine-water test) — pinned here as
ALKENES_MS_P2.txt. There is NO dedicated Alcohols or Carboxylic Acids
Paper-2 MS file in this corpus, so the slice's mark-scheme documentation
surface is the ALKENES pin alone (a PARTIAL-coverage shape — the
batch-3/4 precedent where only some families had MS pins; families
without MS pins mint misconceptions only if another pinned MS documents
the class, else the doubt is HELD). Paper-1 variants remain unpinned per
the Paper-2-first convention batches 2-9 established. The Synthetic
Polymers MS file belongs to batch 11 and stays unpinned here.

This script ONLY extracts text from a PDF already in the repo (pdftotext
page-by-page, no layout flag — same convention as the existing pins).
It writes: ALKENES_MS_P2.txt. Idempotent: an existing pin is skipped.
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
    ("Alkenes MS.pdf", "ALKENES_MS_P2.txt"),
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
