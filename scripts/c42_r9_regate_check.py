#!/usr/bin/env python3
"""c42-r9 check — the deterministic verification battery for the R9 re-gate
fill, the loop's second gate-2 pass (zero-LLM, read-only toward graph/ except
its own report). Mirrors the R4 battery conventions. ALL gates must pass for
the fill record to stand; the GATE OUTCOME ITSELF (Part A per-class precision)
is recorded honestly by the fill and is NOT a check failure here — X9 asserts
the arithmetic is correctly computed and correctly reported, whichever way it
falls."""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402
from c40_maths_a_chunk_sp_substrate import span_chunks, load_corpus, R, norm  # noqa: E402

QUAL = "igcse-maths-a"
REPO = HERE.parent
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
R1_VERDICTS = HERE / "c42_repair_verdicts.yaml"
OVERRIDES = HERE / "c42_section_overrides.yaml"
C40_VERDICTS = HERE / "c40_maths_a_substrate_review_verdicts.yaml"
R6_VERDICTS = HERE / "c42_r6_repair_verdicts.yaml"
OVERRIDES_R6 = HERE / "c42_section_overrides_r6.yaml"
FRESH_FILE = HERE / "c42_r9_fresh_verdicts.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R9_SHEET = GP.reports_dir(QUAL) / "C42_R9_MATHS_A_REGATE_REVIEW_SHEET.md"
R9_VERDICTS = HERE / "c42_r9_review_verdicts.yaml"
R9_FILL_JSON = GP.reports_dir(QUAL) / "C42_R9_MATHS_A_REGATE_FILL_RECORD.json"
CHECK_JSON = GP.reports_dir(QUAL) / "C42_R9_REGATE_CHECK.json"
BASELINE = "03b6ce5a82b36343f2f23b2a1a045fd9ec70fb91"  # the R7/R8 commit (HEAD when the fill ran)

results: list[dict] = []


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def gate(name, ok, detail):
    results.append({"gate": name, "ok": bool(ok), "detail": detail})
    print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    return ok


def main() -> int:
    ok_all = True

    # ---- inputs ----------------------------------------------------------------
    store_p = GP.store("spec_chunk_mappings", QUAL)
    store_doc = yaml.safe_load(store_p.read_text(encoding="utf-8"))
    rows = store_doc["rows"]
    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    worklist = [r for r in rows if "worklist_reason" in r]
    by_mid = {r["mapping_id"]: r for r in rows}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    ledger_map = {x["official_code"]: x for x in ledger}
    sp_doc = yaml.safe_load(
        GP.store("specification_points", QUAL).read_text(encoding="utf-8"))
    sp_by_code = {p["code"]: p for p in sp_doc["specification_points"]}
    r1 = yaml.safe_load(R1_VERDICTS.read_text(encoding="utf-8"))
    r6 = yaml.safe_load(R6_VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    ovr6 = yaml.safe_load(OVERRIDES_R6.read_text(encoding="utf-8"))
    r4 = yaml.safe_load(R4_VERDICTS.read_text(encoding="utf-8"))
    fresh = yaml.safe_load(FRESH_FILE.read_text(encoding="utf-8"))
    r9 = yaml.safe_load(R9_VERDICTS.read_text(encoding="utf-8"))
    fill = json.loads(R9_FILL_JSON.read_text(encoding="utf-8"))

    # X1 input pins --------------------------------------------------------------
    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    g1 = (len(rows) == 925 and len(anchored) == 842 and len(worklist) == 83
          and len(ledger_map) == 54 and len(r1["verdicts"]) == 45
          and len(r6["verdicts"]) == 10
          and len(ovr["overrides"]) == 16 and len(ovr6["overrides"]) == 7
          and len(r4["verdicts"]) == 467
          and len(fresh["verdicts"]) == 50 and fill["baseline"] == BASELINE)
    ok_all &= gate("X1 input_pins",
                   g1,
                   f"store 925=842+83, ledger 54, R1 45, R6 10, overrides 16+7, "
                   f"R4 record 467, fresh 50; fill baseline == {BASELINE[:12]} (the R7/R8 commit); "
                   f"HEAD {head[:12]}")

    # X2 sampling ----------------------------------------------------------------
    seed = sha16(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).encode())

    def stratum(r):
        s = r["provenance"]["upstream"].get("join_score")
        return "none" if s is None else ("exact" if float(s) >= 1.0 else "partial")

    def rank(mid):
        return sha16(f"{seed}|{mid}".encode())

    by = {}
    for r in anchored:
        if r.get("anchor", {}).get("ambiguous_hits", 0) == 0:
            by.setdefault(stratum(r), []).append(r)
    sample = {}
    for cls in sorted(by):
        lst = sorted(by[cls], key=lambda r: rank(r["mapping_id"]))
        n = len(lst) if cls in ("none", "partial") else -(-len(lst) * 20 // 100)
        for r in lst[:n]:
            sample[r["mapping_id"]] = (cls, r)
    g2 = (seed == r9["sampling"]["seed"]
          and {cls: len(by[cls]) for cls in by} == r9["sampling"]["strata"]
          and {cls: sum(1 for c, _ in sample.values() if c == cls) for cls in by}
          == r9["sampling"]["sampled"]
          and len(sample) == 465)
    ok_all &= gate("X2 sampling", g2,
                   f"seed {seed}; strata { {cls: len(by[cls]) for cls in sorted(by)} }; "
                   f"sampled {dict(Counter(c for c, _ in sample.values()))} == recorded")

    # X3 verdict-record agreement --------------------------------------------------
    v4 = r9["verdicts"]
    g3 = set(v4) == set(sample)
    bad_fields = [m for m, v in v4.items()
                  if v["spec_code"] != sample[m][1]["spec_code"]
                  or v["note_path"] != sample[m][1]["note_path"]
                  or v["heading"] != sample[m][1]["chunk"]["heading"]
                  or v["stratum"] != sample[m][0]
                  or not v.get("both_tier")
                  or v["both_tier"]["tier_signature"] not in
                  ("STORE_HIGHER", "LEDGER_FOUNDATION", "BOTH_IDENTICAL")]
    g3 = g3 and not bad_fields
    src_c = Counter(v["source"] for v in v4.values())
    g3 = g3 and dict(src_c) == r9["verdict_sources"]
    fresh_keys = {m for m, v in v4.items() if v["source"] == "r9-fresh"}
    g3 = g3 and fresh_keys == set(fresh["verdicts"])
    ok_all &= gate("X3 record_agreement", g3,
                   f"465 verdicts == sample; fields+strata+tier signatures agree; "
                   f"sources {dict(src_c)}; fresh set == the committed judgment file")

    # X4 mechanical replay ---------------------------------------------------------
    r_reader = R()
    _, notes = load_corpus(r_reader)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}
    head_of = {(n["manifest"]["path"], c["ordinal"]): c["heading"]
               for n in notes for c in by_note[n["manifest"]["path"]]}
    fails = 0
    for m, (cls, r) in sample.items():
        ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        if not (ctext is not None
                and sha16(ctext.encode()) == r["chunk"]["sha256_16"]
                and norm(r["evidence_quote"]) in norm(ctext)
                and head_of[(r["note_path"], r["chunk"]["ordinal"])] == r["chunk"]["heading"]
                and r["validation_status"] == "SUGGESTED"
                and r["provenance"]["tier"] == "RULE_DERIVED"):
            fails += 1
    ok_all &= gate("X4 mechanical_replay", fails == 0,
                   f"{len(sample) - fails}/{len(sample)} rows re-verified "
                   f"(quote-in-chunk, hash/heading, SUGGESTED/RULE_DERIVED)")

    # X5 carry-forward integrity ----------------------------------------------------
    carried = [m for m, v in v4.items() if v["source"] == "r4-carried"]
    bad = []
    for m in carried:
        r4v = r4["verdicts"].get(m)
        r = sample[m][1]
        if (r4v is None or r4v["verdict"] != "CONFIRM"
                or r4v["spec_code"] != r["spec_code"]
                or r4v["note_path"] != r["note_path"]
                or r4v["heading"] != r["chunk"]["heading"]
                or r["provenance"]["upstream"]["anchor_id"] in r1["verdicts"]
                or r["provenance"]["upstream"]["anchor_id"] in r6["verdicts"]
                or "override" in r.get("provenance", {})
                or "override_subsumed" in r.get("provenance", {})):
            bad.append(m)
    ok_all &= gate("X5 carry_forward", not bad,
                   f"{len(carried)} carried CONFIRMs: triple-identical in the R4 "
                   f"record, outside the R6 surface (0 violations)")

    # X6 R6 + R1 + override consistency ------------------------------------------
    def _has_ov(r):
        return "override" in r.get("provenance", {}) or \
               "override_subsumed" in r.get("provenance", {})
    on_r6 = [m for m, (cls, r) in sample.items()
             if r["provenance"]["upstream"]["anchor_id"] in r6["verdicts"]
             and not _has_ov(r)]
    bad = []
    for m in on_r6:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        a = r6["verdicts"][aid]
        r = sample[m][1]
        if a["disposition"] == "CORRECT":
            if v4[m]["source"] != "r6-id-verdict" or v4[m]["verdict"] != "CONFIRM" \
                    or r["spec_code"] != a["corrected_code"]:
                bad.append(m)
        else:
            bad.append(m)  # UNRESOLVED anchors cannot carry rows
    on_r1 = [m for m, (cls, r) in sample.items()
             if r["provenance"]["upstream"]["anchor_id"] in r1["verdicts"]
             and r["provenance"]["upstream"]["anchor_id"] not in r6["verdicts"]
             and not _has_ov(r)]
    for m in on_r1:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        a = r1["verdicts"][aid]
        r = sample[m][1]
        if a["disposition"] == "AFFIRM":
            if v4[m]["source"] != "r1-id-verdict" or v4[m]["verdict"] != "CONFIRM":
                bad.append(m)
        elif a["disposition"] == "CORRECT":
            if v4[m]["source"] != "r1-id-verdict" or v4[m]["verdict"] != "CONFIRM" \
                    or r["spec_code"] != a["corrected_code"]:
                bad.append(m)
        else:
            bad.append(m)
    ovr6_rows = [m for m, (cls, r) in sample.items()
                 if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R6")]
    ovr6_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr6["overrides"]}
    for m in ovr6_rows:
        r = sample[m][1]
        ov = ovr6_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r6-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
            bad.append(m)
    ovr1_rows = [m for m, (cls, r) in sample.items()
                 if "override" in r.get("provenance", {})
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R6")]
    ovr1_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr["overrides"]}
    holds = []
    for m in ovr1_rows:
        r = sample[m][1]
        ov = ovr1_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r1-section-override":
            bad.append(m)
        elif ov["action"] == "REATTRIBUTE":
            if v4[m]["verdict"] != "CONFIRM" or r["spec_code"] != ov["override_code"]:
                bad.append(m)
        elif "heading-only" in (ov["evidence"] or ""):
            if v4[m]["verdict"] != "HOLD":
                bad.append(m)
            else:
                holds.append(m)
        elif v4[m]["verdict"] != "CONFIRM":
            bad.append(m)
    sub_rows = [m for m, (cls, r) in sample.items()
                if "override_subsumed" in r.get("provenance", {})]
    for m in sub_rows:
        if v4[m]["source"] != "r1-subsumed" or v4[m]["verdict"] != "CONFIRM":
            bad.append(m)
    ok_all &= gate("X6 r6_r1_override_consistency", not bad,
                   f"{len(on_r6)} R6-anchor rows + {len(on_r1)} R1-anchor rows "
                   f"CONFIRM on operator verdicts (CORRECT codes landed verbatim); "
                   f"{len(ovr6_rows)} R6 override rows + {len(ovr1_rows)} R1 override "
                   f"rows follow the operator rulings incl. {len(holds)} explicit "
                   f"heading-only HOLD; {len(sub_rows)} subsumed rows ride the join")

    # X7 both-tier discipline ---------------------------------------------------------
    sig_c = Counter(v["both_tier"]["tier_signature"] for v in v4.values())
    bad = []
    for m, v in v4.items():
        code = sample[m][1]["spec_code"]
        lrow = ledger_map.get(code.split("-", 1)[1])
        if v["both_tier"]["tier_signature"] == "LEDGER_FOUNDATION" and not lrow:
            bad.append(m)
        fv = fresh["verdicts"].get(m)
        if fv and fv["tier_signature"] != v["both_tier"]["tier_signature"]:
            bad.append(m)
    ok_all &= gate("X7 both_tier", not bad,
                   f"signatures {dict(sig_c)}; LEDGER_FOUNDATION rows all on "
                   f"ledger codes; fresh-file signatures match the recomputation")

    # X8 Part B completeness -------------------------------------------------------------
    pb = r9["part_b_verdicts"]
    surf = Counter(v["surface"] for v in pb.values())
    g8 = (set(pb) == {r["mapping_id"] for r in worklist}
          and all(v["verdict"] == "DEFER" for v in pb.values())
          and surf["C32 §3 residual (R1 KEPT UNRESOLVED)"] == 2
          and surf["C42 R1 surface-1 cleared span"] == 6
          and surf["C42 R6 surface-1 cleared span"] == 12
          and surf["uncovered-SP corpus gap (125-code bound)"] == 63)
    ok_all &= gate("X8 part_b", g8,
                   f"{len(pb)}/{len(worklist)} worklist rows DEFER; surfaces "
                   f"2 residual + 6 R1-cleared + 12 R6-cleared + 63 gap")

    # X9 gate arithmetic + anti-forgery ---------------------------------------------------
    rollup = {}
    for cls in ("exact", "partial", "none"):
        rc = [v for v in v4.values() if v["stratum"] == cls]
        conf = sum(1 for v in rc if v["verdict"] == "CONFIRM")
        rollup[cls] = {"rows": len(rc), "confirm": conf,
                       "reject": sum(1 for v in rc if v["verdict"] == "REJECT"),
                       "hold": sum(1 for v in rc if v["verdict"] == "HOLD"),
                       "precision": round(conf / len(rc), 4) if rc else None}
    rec = r9["gate"]["part_a"]["by_stratum"]
    g9 = all(rollup[c] == rec[c] for c in rollup)
    total = {"rows": len(v4),
             "confirm": sum(1 for v in v4.values() if v["verdict"] == "CONFIRM"),
             "reject": sum(1 for v in v4.values() if v["verdict"] == "REJECT"),
             "hold": sum(1 for v in v4.values() if v["verdict"] == "HOLD")}
    total["precision"] = round(total["confirm"] / total["rows"], 4)
    g9 = g9 and total == r9["gate"]["part_a"]["total"]
    classes_pass = all(v["precision"] >= 0.9 for v in rollup.values() if v["rows"])
    g9 = g9 and r9["gate"]["part_a"]["classes_pass"] == classes_pass
    g9 = g9 and r9["gate"]["outcome"] == ("PASS" if (classes_pass and len(pb) == 83) else "FAIL")
    bad_status = [r for r in rows if r.get("validation_status") != "SUGGESTED"
                  or r["provenance"]["tier"] != "RULE_DERIVED"]
    g9 = g9 and not bad_status
    ok_all &= gate("X9 gate_arithmetic_antiforgery", g9,
                   f"rollup recomputed == recorded "
                   f"(exact {rollup['exact']['precision'] * 100:.1f}% / "
                   f"partial {rollup['partial']['precision'] * 100:.1f}% / "
                   f"none {rollup['none']['precision'] * 100:.1f}%); outcome "
                   f"{r9['gate']['outcome']} correctly derived; all 925 rows "
                   f"SUGGESTED / RULE_DERIVED")

    # X10 protected surfaces ----------------------------------------------------------------
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                           capture_output=True, text=True).stdout.strip().splitlines()
    dirty_set = sorted(l[3:].strip() for l in dirty)
    expected = sorted(["graph/reports/C42_R9_MATHS_A_REGATE_FILL_RECORD.json",
                       "graph/reports/C42_R9_MATHS_A_REGATE_FILL_RECORD.md",
                       "graph/reports/C42_R9_MATHS_A_REGATE_REVIEW_SHEET.md",
                       "scripts/c42_r9_fresh_verdicts.yaml",
                       "scripts/c42_r9_regate_fill.py",
                       "scripts/c42_r9_review_verdicts.yaml",
                       "scripts/c42_r9_regate_check.py"])
    if CHECK_JSON.exists():  # present on re-runs after the first
        expected.append("graph/reports/C42_R9_REGATE_CHECK.json")
    expected = sorted(expected)
    changed = subprocess.run(
        ["git", "-C", str(REPO), "diff", "--name-only", BASELINE, "HEAD"],
        capture_output=True, text=True).stdout.strip().splitlines()
    g10 = dirty_set == expected and changed == []
    ok_all &= gate("X10 protected_surfaces", g10,
                   f"dirty set == the R9 footprint exactly ({len(dirty_set)} files, "
                   f"all new); zero tracked-file changes vs {BASELINE[:12]} "
                   f"(Lane C stores, chemistry, spec-links, C25-C41 + C42 "
                   f"scope/R0-R8 records, corpora all byte-untouched)")

    # X11 determinism (re-run the fill; sheet + verdicts byte-identical) ----------------------
    before = (R9_SHEET.read_bytes(), R9_VERDICTS.read_bytes())
    rc = subprocess.run([sys.executable, str(HERE / "c42_r9_regate_fill.py")],
                        capture_output=True, text=True)
    after = (R9_SHEET.read_bytes(), R9_VERDICTS.read_bytes())
    g11 = rc.returncode == 0 and before == after
    ok_all &= gate("X11 determinism", g11,
                   "fill re-run: sheet + verdict record byte-identical")

    passed = sum(1 for r in results if r["ok"])
    out = {"schema": "c42-r9-regate-check/1.0", "task": "T-C42", "stage": "r9-regate",
           "baseline": BASELINE, "head": head,
           "fill_record": str(R9_FILL_JSON.relative_to(REPO)),
           "gates": results, "passed": passed, "total": len(results),
           "all_pass": bool(ok_all),
           "gate_outcome_recorded_by_fill": r9["gate"]["outcome"]}
    CHECK_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"\n{passed}/{len(results)} gates PASS; all_pass={ok_all}; "
          f"fill gate outcome (recorded): {r9['gate']['outcome']}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
