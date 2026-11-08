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
G-STRUCT       (T-GB-STRUCT-1) every embedded qualification-structure
               block is arithmetically sound and provenance-complete:
               Σ(rawMax×weightFactor) == total.maxMark, weights sum to
               the whole, >= 1 full-sha-pinned source per block, and the
               graded total equals the boundaries-document maxMark on
               every served session.

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
    # T-GRADE-8: cancelled/no-award sessions (e.g. January 2021, November
    # 2020) publish component boundaries only — the source genuinely has no
    # overall rows for ANY subject. That is an honest absence, not a parse
    # failure; a doc with SOME overall rows missing others stays an error
    # (that asymmetry is what the guard exists to catch).
    doc_has_any_overall = any(
        s.get("overall") for s in doc["subjects"]
    ) if fam == "pearson-int-gcse-linear" else True
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
        if fam == "pearson-int-gcse-linear" and not s.get("overall") \
                and doc_has_any_overall:
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
        sel = calc.get("selection") or {}
        pool = list(sel.get("pool", []))
        # T-GRADE-9 era-guard enforcement: a SERVED row must carry at least
        # one required-spec unit. Rows with none are foreign-era cash-ins
        # (legacy YMA01 rendered on 2018-spec maths pages) — the builder
        # suppresses them; a regression here is a hard error, not info.
        # T-GRADE-10 selection-mode twin (YFM01): unit codes cannot date an
        # FM row (WFM01-03 are shared across specs) and a session may
        # honestly examine only part of the pool — so the hard check is
        # the builder's pool-membership invariant (any unit OUTSIDE the
        # official pool is a foreign-era row), while partial coverage and
        # units-absent rows are honest absences.
        for s in entry["series"]:
            unit_rows = s.get("calculatorUnits") or s.get("units", [])
            served = {u["code"] for u in unit_rows}
            if pool and unit_rows:
                stray = sorted(set(served) - set(pool))
                if stray:
                    errs.append(f"{slug} {s['session']}: served row has "
                                f"units outside the selection pool "
                                f"{stray} — era-guard regression")
            elif required and unit_rows and not (set(required) & served):
                errs.append(f"{slug} {s['session']}: served row has no "
                            f"required-spec unit {sorted(required)[:3]}.. — "
                            f"era-guard regression")
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
            if pool:
                # selection-mode composition (T-GRADE-10, YFM01): the
                # candidate's `size` units are drawn from the official pool
                # (mustInclude + atLeastOneOf guards eligibility); every
                # pool unit carries UMS max 100, so any size-subset sums to
                # the cash-in maximum — verify exactly that, per session.
                bad_max = [c for c in units
                           if c in pool
                           and (units[c].get("ums") or {}).get("maxMark")
                           != 100]
                if bad_max:
                    errs.append(f"{slug} {s['session']}: pool units whose "
                                f"UMS max != 100 {bad_max}")
                    continue
                with_ums = [c for c in pool
                            if (units.get(c) or {}).get("ums", {}).get(
                                "maxMark")]
                ok = (all(c in with_ums for c in sel.get("mustInclude", []))
                      and any(c in with_ums
                              for c in sel.get("atLeastOneOf", []))
                      and len(with_ums) >= sel.get("size", 6))
                if not ok:
                    infos.append(f"{slug} {s['session']}: no eligible "
                                 f"{sel.get('size', 6)}-unit selection from "
                                 f"the pool this session (honest absence)")
                    continue
                total = sel.get("size", 6) * 100
            elif pairs:
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
                    line = (f"{slug} {s['session']}: A2 units missing "
                            f"{a2_missing}")
                    if pool:
                        # selection-mode: a session may not examine every
                        # pool unit — the Rule-1 combination just cannot
                        # select the missing ones (honest per-session absence)
                        infos.append(line + " (honest absence)")
                    else:
                        errs.append(line)
            if a_star and pool:
                # selection-mode A* rule is rate-form (T-GRADE-10): the A2
                # UMS maximum depends on which units the combination uses,
                # so the board's "at least 90% of the A2 UMS" is carried as
                # a2Rate, not a fixed a2Min
                if a_star.get("a2Rate") != 0.9:
                    errs.append(f"{slug} {s['session']}: selection-mode "
                                f"aStar must carry a2Rate 0.9 "
                                f"(got {a_star.get('a2Rate')})")
                stray = [c for c in a_star.get("a2Units", [])
                         if c not in pool]
                if stray:
                    errs.append(f"{slug} {s['session']}: a2Units outside "
                                f"the selection pool {stray}")
            if a_star and a_star.get("overallMin") is not None:
                printed_a = cashin["boundaries"].get("A")
                if printed_a is not None and printed_a != a_star["overallMin"]:
                    errs.append(f"{slug} {s['session']}: aStar.overallMin "
                                f"{a_star['overallMin']} != printed A "
                                f"boundary {printed_a}")
            # T-GB-STRUCT-3: 9-1 modular cash-ins have no printed A; the
            # embedded law's fixed thresholds must equal EVERY grade the
            # served cash-in row prints, session by session
            law = calc.get("gradeThresholds") or {}
            if law:
                for g, v in law.items():
                    printed = cashin["boundaries"].get(g)
                    if printed is not None and printed != v:
                        errs.append(f"{slug} {s['session']}: law "
                                    f"grade {g}={v} != printed boundary "
                                    f"{printed}")
            satisfiable += 1
        if satisfiable == 0:
            errs.append(f"{slug}: NO session can compose the "
                        f"{calc['cashIn']} aggregation")
        else:
            print(f"  agg {slug}: {satisfiable}/{len(entry['series'])} "
                  f"sessions calculator-eligible")
    return errs, infos


CURATED_ADAPTED = json.loads(
    (CURATED / "structure.json").read_text()).get("adaptedSessions") or {}


def check_structure(bundle: dict) -> list[str]:
    """G-STRUCT (T-GB-STRUCT-1): embedded structure blocks must be
    arithmetically sound and provenance-complete. The arithmetic law:
    Σ(rawMax × weightFactor) == total.maxMark — this is precisely the
    'Maths B shows 300, not 200' fact, now checked instead of assumed."""
    errs: list[str] = []
    n_struct = 0
    for slug, entry in bundle["courses"].items():
        st = entry.get("structure")
        if not st:
            continue
        n_struct += 1
        head = f"structure {slug}"
        papers = st.get("papers") or []
        if not papers:
            errs.append(f"{head}: no papers")
            continue
        total = st.get("total") or {}
        if not isinstance(total.get("maxMark"), int) or total["maxMark"] <= 0:
            errs.append(f"{head}: total.maxMark missing/invalid")
            continue
        weight_sum = 0.0
        weighted_total = 0
        for p in papers:
            pf = f"{head} {p.get('code', '?')}"
            raw = p.get("rawMax")
            wf = p.get("weightFactor")
            w = p.get("weight") or {}
            if not isinstance(raw, int) or raw <= 0:
                errs.append(f"{pf}: rawMax missing/invalid")
                continue
            if not isinstance(wf, int) or wf < 1:
                errs.append(f"{pf}: weightFactor missing/< 1")
                continue
            if not (isinstance(w.get("num"), int)
                    and isinstance(w.get("den"), int) and w["den"] > 0):
                errs.append(f"{pf}: weight num/den missing")
                continue
            weight_sum += w["num"] / w["den"]
            weighted_total += raw * wf
        if weighted_total != total["maxMark"]:
            errs.append(f"{head}: Σ(rawMax×weightFactor)={weighted_total} "
                        f"!= total.maxMark {total['maxMark']}")
        if papers and abs(weight_sum - 1.0) > 1e-9:
            errs.append(f"{head}: weights sum to {weight_sum!r}, not 1")
        srcs = st.get("sources") or []
        if not srcs:
            errs.append(f"{head}: no resolved sources")
        for s in srcs:
            if not s.get("sha256_16") or len(s["sha256_16"]) != 16:
                errs.append(f"{head} source {s.get('id', '?')}: no sha pin")
            if not s.get("url"):
                errs.append(f"{head} source {s.get('id', '?')}: no url")
        if not st.get("awardRules"):
            errs.append(f"{head}: awardRules absent (no stubs)")
        # cross-document consistency: the graded total must equal the
        # boundaries-document maxMark on every served session
        calc = entry.get("calculator") or {}
        if calc.get("mode") == "linear-total" \
                and calc.get("maxMark") != total["maxMark"]:
            errs.append(f"{head}: calculator.maxMark {calc.get('maxMark')} "
                        f"!= structure total {total['maxMark']}")
        adapted = (CURATED_ADAPTED.get(entry.get("code") or "")
                   or {})
        for sr in entry.get("series", []):
            if sr.get("maxMark") is not None \
                    and sr["maxMark"] != total["maxMark"]:
                rec = adapted.get(sr["session"])
                if rec and rec.get("servedMaxMark") == sr["maxMark"]:
                    continue  # official adapted session (recorded, pinned)
                errs.append(f"{head} {sr['session']}: boundaries maxMark "
                            f"{sr['maxMark']} != structure total "
                            f"{total['maxMark']}")
    print(f"STRUCTURE: {n_struct} structure blocks checked")
    return errs



def check_modular_awards(bundle: dict) -> list[str]:
    """T-GB-STRUCT-3: the embedded modular award law (fixed UMS grade
    thresholds from the official modular specifications) must be internally
    sound and consistent with the served unit UMS data."""
    errs: list[str] = []
    n = 0
    for slug, entry in bundle["courses"].items():
        calc = entry.get("calculator") or {}
        if calc.get("mode") != "aggregate-ums" \
                or "gradeThresholds" not in calc:
            continue
        n += 1
        head = f"modular-award {slug}"
        ums_max = calc.get("umsMax")
        uum = calc.get("unitUmsMax") or {}
        if not isinstance(ums_max, int) or sum(uum.values()) != ums_max:
            errs.append(f"{head}: umsMax {ums_max} != \u03a3 unitUmsMax "
                        f"{sum(uum.values())}")
        th = calc.get("gradeThresholds") or {}
        vals = list(th.values())
        if any(not isinstance(v, int) for v in vals):
            errs.append(f"{head}: non-integer threshold")
        elif any(a <= b for a, b in zip(vals, vals[1:])):
            errs.append(f"{head}: thresholds not strictly descending")
        if isinstance(ums_max, int) and any(v > ums_max for v in vals):
            errs.append(f"{head}: threshold above umsMax")
        a = calc.get("aStar") or {}
        if vals and a.get("overallMin") != max(vals):
            errs.append(f"{head}: aStar.overallMin != top threshold")
        # served-data cross-check: every served session's unit UMS max
        # must equal the law's unit UMS max
        ums_seen = {}
        for s in entry.get("series", []):
            for u in (s.get("calculatorUnits") or s.get("units", [])):
                um = (u.get("ums") or {}).get("maxMark")
                if um:
                    ums_seen[u["code"]] = um
        for code, m in uum.items():
            if code in ums_seen and ums_seen[code] != m:
                errs.append(f"{head} {code}: served UMS max "
                            f"{ums_seen[code]} != law {m}")
    print(f"MODULAR-AWARD: {n} modular award laws checked")
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

    # ---- T-GRADE-8 run-003 bundle shape law (the run-014 upstream note) ----
    # No series row may carry a present-but-empty optional array: the hub
    # prebuild validator rejects that shape outright, and the honest
    # cash-in-only emission is key-absent (units-absent).
    # ---- G3(c): aggregation calculator structural soundness ----
    if BUNDLE.exists():
        bundle = json.loads(BUNDLE.read_text())
        shape_bad = []
        for slug, entry in bundle["courses"].items():
            for s in entry.get("series", []):
                for k in ("units", "cashIns", "components", "routes",
                          "calculatorUnits"):
                    if k in s and s[k] == []:
                        shape_bad.append(f"{slug} {s['session']}: {k}: []")
        if shape_bad:
            errors.append("bundle shape law: present-empty optional arrays: "
                          + "; ".join(shape_bad[:12]))
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
        # ---- G-STRUCT: qualification-structure soundness (T-GB-STRUCT-1) ----
        errors += check_structure(bundle)
        # ---- G-STRUCT-3: modular award law soundness (T-GB-STRUCT-3) ----
        errors += check_modular_awards(bundle)
    else:
        errors.append(f"bundle missing: {BUNDLE}")

    for e in errors[:40]:
        print("  -", e)
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
