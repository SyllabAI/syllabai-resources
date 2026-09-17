#!/usr/bin/env python3
"""Verification gates for Official-Specifications corpus.

G1 schema+totals: manifest parses, qualification count, course coverage
G2 integrity: every PDF exists, %PDF magic, pypdf-openable, sha1 matches
   spec.json, byte count matches
G3 coverage: every SME course dir appears in exactly one qualification
G4 codes: every qualification has spec_codes + cover_code
G5 duplicates: chemistry-2017 copy identical to repo-root legacy PDF (or
   divergence documented)
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pypdf

REPO = Path("/home/z/my-project/download/syllabai-resources")
OUT = REPO / "Official-Specifications"

fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    print(("  PASS " if cond else "  FAIL ") + msg)
    if not cond:
        fails.append(msg)


manifest = json.loads((OUT / "manifest.json").read_text())
quals = manifest["qualifications"]

print("G1 schema+totals")
check(manifest["schema"] == "syllabai.official-specifications/1.0",
      "schema id")
check(len(quals) == manifest["totals"]["qualifications"],
      f"quals count {len(quals)} == totals")
covered = sorted({c for q in quals for c in q["sme_courses"]})
check(len(covered) == manifest["totals"]["sme_courses_covered"],
      "covered count truthful")
check(manifest["totals"]["missing_courses"] == [], "no missing courses")

print("G2 integrity")
for q in quals:
    pdf = OUT / q["slug"] / q["pdf"]
    ok = pdf.exists()
    if ok:
        raw = pdf.read_bytes()
        ok = raw.startswith(b"%PDF") and len(raw) == q["bytes"] and \
            hashlib.sha1(raw).hexdigest() == q["sha1"]
        if ok:
            try:
                ok = len(pypdf.PdfReader(str(pdf)).pages) == q["pages"]
            except Exception:  # noqa: BLE001
                ok = False
    check(ok, f"{q['slug']}: {q['pdf']} ({q['pages']}p)")

print("G3 course coverage")
course_dirs = sorted(p.name for p in (REPO / "SME-ExamQuestion").iterdir()
                     if p.is_dir())
multi = [c for c in covered if
         sum(c in q["sme_courses"] for q in quals) > 1]
check(sorted(covered) == course_dirs,
      f"all {len(course_dirs)} SME course dirs covered, names match")
check(multi == [], "no course in 2+ qualifications")

print("G4 codes")
no_code = [q["slug"] for q in quals
           if not q["spec_codes"] or not q.get("cover_code")]
check(no_code == [], f"all quals have spec_codes+cover_code ({no_code})")

print("G5 legacy chemistry copy")
legacy = REPO / "international-gcse-chemistry-2017-specification.pdf"
chem = next(q for q in quals if q["slug"] == "igcse-chemistry")
same = legacy.exists() and hashlib.sha1(legacy.read_bytes()).hexdigest() \
    == chem["sha1"]
print(f"  {'PASS' if same else 'NOTE'} legacy root PDF sha1 vs corpus: "
      f"{'identical document' if same else 'DIFFERENT (issue drift?)'}")

print(f"\n{'ALL GATES PASS' if not fails else f'{len(fails)} FAILURES'}")
raise SystemExit(1 if fails else 0)
