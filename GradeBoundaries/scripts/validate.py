#!/usr/bin/env python3
"""Validation gates for the GradeBoundaries lane.

G1 SCHEMA      every parsed subject/ladder is complete and monotonic;
               U/ungraded column present; 0 <= boundary <= maxMark.
G2 PARITY      golden-master: 4CH1 linear sessions must match the
               operator-supplied MathsGenie corpus of record exactly
               (curated/maths-genie-4ch1-golden.json) on every overlapping
               session — byte-exact numbers, no rounding, no excuses.
G3 COVERAGE    the corpus covers >= 6 of the 8 golden sessions for the pilot
               subject before the bundle may serve a calculator.

Fail-loud: any gate failure exits 1 with the offending rows printed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from gb_common import CURATED, PARSED, monotonic_ok

GOLDEN = CURATED / "maths-genie-4ch1-golden.json"


def load(family: str) -> list[dict]:
    d = PARSED / family
    if not d.exists():
        return []
    return [json.loads(p.read_text()) for p in sorted(d.glob("*.json"))]


def check_doc(doc: dict) -> list[str]:
    errs: list[str] = []
    fam = doc["family"]
    for s in doc["subjects"]:
        code = s.get("code") or "?"
        ladders: list[tuple[str, dict, list[str]]] = []
        if s.get("overall"):
            ladders.append(("overall", s["overall"], s["gradeLadder"]))
        for u in s.get("units", []):
            ladders.append((f"unit {u['code']}", u, s["gradeLadder"]))
            if u.get("ums"):
                ladders.append((f"unit {u['code']} UMS", u["ums"],
                                s["gradeLadder"]))
        for c in s.get("cashIns", []):
            ladders.append((f"cash-in {c['code']}", c, s["gradeLadder"]))
        if fam == "pearson-int-gcse-linear" and not s.get("overall"):
            errs.append(f"{fam}/{doc['session']} {code}: no overall row")
        for name, row, ladder in ladders:
            if not row.get("boundaries"):
                errs.append(f"{fam}/{doc['session']} {code} {name}: empty")
                continue
            b = row["boundaries"]
            for g, v in b.items():
                if v is not None and (v < 0 or v > row.get(
                        "maxMark", 10 ** 6)):
                    errs.append(f"{fam}/{doc['session']} {code} {name}: "
                                f"{g}={v} outside 0..{row.get('maxMark')}")
            if not monotonic_ok(b, ladder or list(b)):
                errs.append(f"{fam}/{doc['session']} {code} {name}: "
                            f"non-monotonic {b}")
    for w in doc.get("parse_warnings", []):
        if "column count" in w or "unparseable" in w:
            errs.append(f"{fam}/{doc['session']}: WARNING {w}")
    return errs


def grade_key_match(ours: dict, golden: dict, ladder: list[str]) -> list[str]:
    errs = []
    for g in ladder:
        ours_v, gold_v = ours.get(g), golden.get(g)
        if gold_v is None:
            continue
        if g == "U":
            continue
        if ours_v != gold_v:
            errs.append(f"grade {g}: ours={ours_v} golden={gold_v}")
    return errs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-parity", action="store_true")
    args = ap.parse_args()

    errors: list[str] = []
    all_docs = []
    for fam in ("pearson-int-gcse-linear", "pearson-int-gcse-modular",
                "pearson-ial"):
        docs = load(fam)
        all_docs += docs
        for doc in docs:
            errors += check_doc(doc)
    for d in (PARSED / "cie").glob("*/*.json") if (PARSED / "cie").exists() \
            else []:
        doc = json.loads(d.read_text())
        for c in doc.get("components", []) + doc.get("routes", []):
            if not c.get("ok", False):
                errors.append(f"{doc['family']}/{doc['session']}: bad row")
        if doc.get("parse_warnings"):
            errors.append(f"{doc['family']}/{doc['session']}: "
                          f"{len(doc['parse_warnings'])} warnings")

    # ---- G2/G3: MathsGenie golden-master parity for 4CH1 ----
    if not args.skip_parity:
        if not GOLDEN.exists():
            errors.append(f"missing golden fixture {GOLDEN}")
        else:
            golden = json.loads(GOLDEN.read_text())
            linear = {d["session"]: d for d in all_docs
                      if d["family"] == "pearson-int-gcse-linear"}
            matched, mismatches, overlap = 0, 0, 0
            for g in golden:
                session, want = g["examSeries"], g["overallBoundaries"]
                doc = linear.get(session)
                if not doc:
                    continue
                rows = [s for s in doc["subjects"]
                        if s.get("code") == "4CH1" and s.get("overall")]
                if not rows:
                    errors.append(f"parity: {session}: 4CH1 row missing")
                    mismatches += 1
                    continue
                overlap += 1
                # The doc may carry several variants per session (standard
                # 1C/2C and regional 1CR/2CR); the golden master matches the
                # variant MG tracks — parity = at least one exact row.
                if any(grade_key_match(r["overall"]["boundaries"], want,
                                       r["gradeLadder"]) == []
                       for r in rows):
                    matched += 1
                else:
                    got = " | ".join(
                        json.dumps(r["overall"]["boundaries"]) for r in rows)
                    errors.append(f"parity {session} 4CH1: no variant row "
                                  f"matches golden; parsed: {got}")
                    mismatches += 1
            print(f"PARITY: {matched} exact matches, {mismatches} mismatches, "
                  f"{overlap} overlapping sessions")
            if overlap < 6:
                errors.append(f"coverage: only {overlap} golden sessions "
                              f"present in the parsed corpus (need >= 6)")
            if mismatches:
                errors.append("parity failures present — corpus numbers have "
                              "drifted from the golden master")

    print(f"VALIDATE: {len(all_docs)} Pearson docs checked, "
          f"{len(errors)} errors")
    for e in errors[:40]:
        print("  -", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
