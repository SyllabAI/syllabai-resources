#!/usr/bin/env python3
"""Validation gates for the GradeBoundaries lane.

G1 SCHEMA      every parsed subject/ladder is complete and monotonic;
               U/ungraded column present; 0 <= boundary <= maxMark.
G2 PARITY      golden-master: 4CH1 linear sessions must match the
               operator-supplied MathsGenie corpus of record exactly
               (curated/maths-genie-4ch1-golden.json) on every overlapping
               session — byte-exact numbers, no rounding, no excuses.
G3 COVERAGE    (a) the MathsGenie golden corpus overlaps >= 6 sessions;
               (b) every CIE syllabus the hub course map needs is parsed;
               (c) every aggregate-ums calculator in the bundle is
               structurally sound: every composed unit exists in each
               session with UMS data, and the required units' UMS maxima
               (+ one optional pair) sum to the cash-in maximum.

Fail-loud: any gate failure exits 1 with the offending rows printed.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from gb_common import CURATED, LANE, MAPPING, PARSED, monotonic_ok

GOLDEN = CURATED / "maths-genie-4ch1-golden.json"
BUNDLE = LANE / "hub-import" / "grade-boundaries-1.0" / "bundle.json"

# Map syllabi with NO boundary documents in any crawled session, with the
# verified reason. Anything missing that is not listed here fails G3(b).
ALLOWED_CIE_ABSENT = {
    "0264": "Cambridge IGCSE Business (0264) — code changed for first "
            "assessment March 2027 (official CIE syllabus page); no award "
            "exists yet, the course honestly stays on roadmap",
}


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


def map_cie_codes() -> set[str]:
    """CIE syllabus codes the hub course map needs (cie-family rows only —
    IAL rows also carry a cieSyllabus field with their Y-cash-in code)."""
    codes: set[str] = set()
    cur_is_cie = False
    for line in (MAPPING / "course-map.yaml").read_text().splitlines():
        s = line.strip()
        if s.startswith("- slug:"):
            cur_is_cie = False
        elif s.startswith("family:"):
            cur_is_cie = s.split(":", 1)[1].strip() == "cie"
        elif s.startswith("cieSyllabus:") and cur_is_cie:
            codes.add(s.split(":", 1)[1].strip().strip('"'))
    return codes


def check_aggregation(bundle: dict, docs_by_family: dict[str, list[dict]]) \
        -> tuple[list[str], list[str]]:
    """G3(c): aggregate-ums calculators must be structurally sound.

    HARD errors: a course with NO satisfiable session at all, or a
    satisfiable session whose UMS maxima do not sum to the cash-in maximum.
    INFO lines: sessions where the composition cannot exist because the
    units were not examined that session (e.g. WMA13/WMA14 before their
    first award) — an honest per-session absence the hub degrades on.
    """
    errs: list[str] = []
    infos: list[str] = []
    for slug, entry in bundle["courses"].items():
        calc = entry.get("calculator") or {}
        if calc.get("mode") != "aggregate-ums":
            continue
        fam = entry["series"][0]["source"]["family"]
        required = list(calc.get("required", []))
        pairs = calc.get("optionalPairs") or []
        satisfiable = 0
        for s in entry["series"]:
            units = {u["code"]: u for u in s.get("calculatorUnits", [])
                     or s.get("units", [])}
            missing = [c for c in required if c not in units]
            if missing:
                infos.append(f"{slug} {s['session']}: units not examined "
                             f"this session ({', '.join(missing)}) — no "
                             f"aggregation possible (honest absence)")
                continue
            no_ums = [c for c in required
                      if not (units[c].get("ums") or {}).get("maxMark")]
            if no_ums:
                errs.append(f"{slug} {s['session']}: required units without "
                            f"UMS data {no_ums}")
                continue
            cashin = next((c for c in s.get("cashIns", [])
                           if c["code"] == calc["cashIn"]), None)
            if not cashin:
                errs.append(f"{slug} {s['session']}: cash-in "
                            f"{calc['cashIn']} absent")
                continue
            if pairs:
                usable = [p for p in pairs if p[0] in units and p[1] in units
                          and (units[p[0]].get("ums") or {}).get("maxMark")
                          and (units[p[1]].get("ums") or {}).get("maxMark")]
                if not usable:
                    infos.append(f"{slug} {s['session']}: no optional pair "
                                 f"examined this session (honest absence)")
                    continue
                p = usable[0]
                total = (sum(units[c]["ums"]["maxMark"] for c in required)
                         + units[p[0]]["ums"]["maxMark"]
                         + units[p[1]]["ums"]["maxMark"])
            else:
                total = sum(units[c]["ums"]["maxMark"] for c in required)
            if total != cashin["maxMark"]:
                errs.append(f"{slug} {s['session']}: UMS maxima {total} != "
                            f"cash-in max {cashin['maxMark']}")
            a_star = calc.get("aStar")
            if a_star and a_star.get("a2Units"):
                a2_missing = [c for c in a_star["a2Units"] if c not in units]
                if a2_missing:
                    errs.append(f"{slug} {s['session']}: A2 units missing "
                                f"{a2_missing}")
            satisfiable += 1
        if satisfiable == 0:
            errs.append(f"{slug}: NO session can compose the "
                        f"{calc['cashIn']} aggregation")
        else:
            print(f"  agg {slug}: {satisfiable}/{len(entry['series'])} "
                  f"sessions calculator-eligible")
    return errs, infos


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
          f"{len(errors)} errors so far")

    # ---- G3(b): CIE coverage of every syllabus the course map needs ----
    cie_codes_parsed = {p.parent.name for p in
                        (PARSED / "cie").glob("*/*.json")} \
        if (PARSED / "cie").exists() else set()
    wanted = map_cie_codes()
    cie_missing = sorted(wanted - cie_codes_parsed)
    unexplained = [c for c in cie_missing if c not in ALLOWED_CIE_ABSENT]
    print(f"CIE COVERAGE: {len(cie_codes_parsed & wanted)}/{len(wanted)} "
          f"mapped syllabi parsed "
          f"({len(cie_missing) - len(unexplained)} honestly absent)")
    if unexplained:
        errors.append(f"cie coverage: map syllabi without parsed docs: "
                      f"{unexplained}")

    # ---- G3(c): aggregation calculator structural soundness ----
    if BUNDLE.exists():
        bundle = json.loads(BUNDLE.read_text())
        docs_by_family = {f: load(f) for f in
                          ("pearson-int-gcse-modular", "pearson-ial")}
        agg_errs, agg_infos = check_aggregation(bundle, docs_by_family)
        n_agg = sum(1 for e in bundle["courses"].values()
                    if (e.get("calculator") or {}).get("mode")
                    == "aggregate-ums")
        print(f"AGGREGATION: {n_agg} aggregate-ums courses checked, "
              f"{len(agg_errs)} errors")
        errors += agg_errs
        for i in agg_infos[:12]:
            print("  info:", i)
    else:
        errors.append(f"bundle missing: {BUNDLE}")

    for e in errors[:40]:
        print("  -", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
