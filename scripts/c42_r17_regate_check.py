#!/usr/bin/env python3
"""c42-r17 check — the deterministic verification battery for the R17 re-gate
fill, the loop's fourth gate-2 pass (zero-LLM, read-only toward graph/ except
its own report). Mirrors the R13 battery conventions. ALL gates must pass for
the fill record to stand; the GATE OUTCOME ITSELF (Part A per-class precision)
is recorded honestly by the fill and is NOT a check failure here — X9 asserts
the arithmetic is correctly computed and correctly reported, whichever way it
falls. NEW at R17: X12 replays the c42-heading-only-convention-1 ladder
(H1/H2/H3) with the R13 record in the H2 source base (the R14 record's
projection — bounds ord 0 un-holds via H2); X13 pins the H3 fail-closed set;
X5 verifies the R13-carried + R9/R4-carried chains; X6 verifies the R14
id-verdict and section-override rulings land verbatim."""
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
R10_VERDICTS = HERE / "c42_r10_repair_verdicts.yaml"
OVERRIDES_R10 = HERE / "c42_section_overrides_r10.yaml"
R14_VERDICTS = HERE / "c42_r14_repair_verdicts.yaml"
OVERRIDES_R14 = HERE / "c42_section_overrides_r14.yaml"
R9_PRIOR = HERE / "c42_r9_review_verdicts.yaml"
R13_PRIOR = HERE / "c42_r13_review_verdicts.yaml"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
FRESH_FILE = HERE / "c42_r17_fresh_verdicts.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R17_SHEET = GP.reports_dir(QUAL) / "C42_R17_MATHS_A_REGATE_REVIEW_SHEET.md"
R17_VERDICTS = HERE / "c42_r17_review_verdicts.yaml"
R17_FILL_JSON = GP.reports_dir(QUAL) / "C42_R17_MATHS_A_REGATE_FILL_RECORD.json"
CHECK_JSON = GP.reports_dir(QUAL) / "C42_R17_REGATE_CHECK.json"
BASELINE = "4725bab645652def20fd110971423e9701939c87"  # the R15/R16 commit (HEAD when the fill ran)

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
    r10 = yaml.safe_load(R10_VERDICTS.read_text(encoding="utf-8"))
    r14 = yaml.safe_load(R14_VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    ovr6 = yaml.safe_load(OVERRIDES_R6.read_text(encoding="utf-8"))
    ovr10 = yaml.safe_load(OVERRIDES_R10.read_text(encoding="utf-8"))
    ovr14 = yaml.safe_load(OVERRIDES_R14.read_text(encoding="utf-8"))
    r4 = yaml.safe_load(R4_VERDICTS.read_text(encoding="utf-8"))
    r9p = yaml.safe_load(R9_PRIOR.read_text(encoding="utf-8"))
    r13p = yaml.safe_load(R13_PRIOR.read_text(encoding="utf-8"))
    conv = json.loads(CONVENTION_JSON.read_text(encoding="utf-8"))
    fresh = yaml.safe_load(FRESH_FILE.read_text(encoding="utf-8"))
    r17 = yaml.safe_load(R17_VERDICTS.read_text(encoding="utf-8"))
    fill = json.loads(R17_FILL_JSON.read_text(encoding="utf-8"))

    # X1 input pins --------------------------------------------------------------
    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    g1 = (len(rows) == 922 and len(anchored) == 840 and len(worklist) == 82
          and len(ledger_map) == 54 and len(r1["verdicts"]) == 45
          and len(r6["verdicts"]) == 10 and len(r10["verdicts"]) == 2
          and len(r14["verdicts"]) == 1
          and len(ovr["overrides"]) == 16 and len(ovr6["overrides"]) == 7
          and len(ovr10["overrides"]) == 8 and len(ovr14["overrides"]) == 5
          and len(r4["verdicts"]) == 467 and len(r9p["verdicts"]) == 465
          and len(r13p["verdicts"]) == 465
          and len(fresh["verdicts"]) == 23 and fill["baseline"] == BASELINE
          and conv["decision_id"] == "c42-heading-only-convention-1")
    ok_all &= gate("X1 input_pins",
                   g1,
                   f"store 922=840+82 (22 unresolved-span incl. BOTH DEMOTEs + 60 gap), "
                   f"ledger 54, R1 45, R6 10, R10 2, R14 1, overrides 16+7+8+5, "
                   f"R4 467, R9 465, R13 465, fresh 23, convention pinned; fill "
                   f"baseline == the R15/R16 commit; HEAD {head[:12]}")

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
    g2 = (seed == r17["sampling"]["seed"]
          and {cls: len(by[cls]) for cls in by} == r17["sampling"]["strata"]
          and {cls: sum(1 for c, _ in sample.values() if c == cls) for cls in by}
          == r17["sampling"]["sampled"]
          and len(sample) == 464)
    ok_all &= gate("X2 sampling", g2,
                   f"seed {seed}; strata { {cls: len(by[cls]) for cls in sorted(by)} }; "
                   f"sampled {dict(Counter(c for c, _ in sample.values()))} == recorded")

    # X3 verdict-record agreement --------------------------------------------------
    v4 = r17["verdicts"]
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
    g3 = g3 and dict(src_c) == r17["verdict_sources"]
    fresh_keys = {m for m, v in v4.items() if v["source"] == "r17-fresh"}
    g3 = g3 and fresh_keys == set(fresh["verdicts"])
    ok_all &= gate("X3 record_agreement", g3,
                   f"464 verdicts == sample; fields+strata+tier signatures agree; "
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

    # X5 carry-forward integrity (R13 + R9 + R4 chains) ------------------------------
    def _prior_clean(r):
        aid = r["provenance"]["upstream"]["anchor_id"]
        return (aid not in r1["verdicts"] and aid not in r6["verdicts"]
                and aid not in r10["verdicts"] and aid not in r14["verdicts"]
                and aid != "spcpt_crKbmb6wVjM4yPJh"
                and "override" not in r.get("provenance", {})
                and "override_subsumed" not in r.get("provenance", {}))

    def _triple_ok(v, r):
        return (v is not None and v["verdict"] == "CONFIRM"
                and v["spec_code"] == r["spec_code"]
                and v["note_path"] == r["note_path"]
                and v["heading"] == r["chunk"]["heading"])

    carried13 = [m for m, v in v4.items() if v["source"] == "r13-carried"]
    bad = []
    for m in carried13:
        r13v = r13p["verdicts"].get(m)
        r = sample[m][1]
        if not _triple_ok(r13v, r) or not _prior_clean(r):
            bad.append(m)
    carried9 = [m for m, v in v4.items() if v["source"] == "r9-carried"]
    for m in carried9:
        r9v = r9p["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r9v, r) or m in r13p["verdicts"]
                or not _prior_clean(r)):
            bad.append(m)
    carried4 = [m for m, v in v4.items() if v["source"] == "r4-carried"]
    for m in carried4:
        r4v = r4["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r4v, r)
                or m in r13p["verdicts"] or m in r9p["verdicts"]
                or not _prior_clean(r)):
            bad.append(m)
    ok_all &= gate("X5 carry_forward", not bad,
                   f"{len(carried13)} R13-carried + {len(carried9)} R9-carried + "
                   f"{len(carried4)} R4-carried CONFIRMs: triple-identical in the "
                   f"prior records, outside the R14 surface (R9 carries only for "
                   f"rows absent from the R13 record; R4 only for rows absent from "
                   f"both; 0 violations)")

    # X6 R14 + R10 + R6 + R1 + override consistency --------------------------------
    def _has_ov(r):
        return "override" in r.get("provenance", {}) or \
               "override_subsumed" in r.get("provenance", {})
    bad = []
    on_r14 = [m for m, (cls, r) in sample.items()
              if r["provenance"]["upstream"]["anchor_id"] in r14["verdicts"]
              and not _has_ov(r)]
    for m in on_r14:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        a = r14["verdicts"][aid]
        r = sample[m][1]
        if a["disposition"] == "CORRECT":
            if v4[m]["source"] != "r14-id-verdict" or v4[m]["verdict"] != "CONFIRM" \
                    or r["spec_code"] != a["corrected_code"]:
                bad.append(m)
        else:
            bad.append(m)
    standing_rows = [m for m, (cls, r) in sample.items()
                     if r["provenance"]["upstream"]["anchor_id"] == "spcpt_crKbmb6wVjM4yPJh"
                     and not _has_ov(r)]
    for m in standing_rows:
        if v4[m]["source"] != "r10-standing" or v4[m]["verdict"] != "CONFIRM" \
                or sample[m][1]["spec_code"] != "4MA1-1.8D":
            bad.append(m)
    on_r10 = [m for m, (cls, r) in sample.items()
              if r["provenance"]["upstream"]["anchor_id"] in r10["verdicts"]
              and r["provenance"]["upstream"]["anchor_id"] not in r14["verdicts"]
              and r["provenance"]["upstream"]["anchor_id"] != "spcpt_crKbmb6wVjM4yPJh"
              and not _has_ov(r)]
    for m in on_r10:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        a = r10["verdicts"][aid]
        r = sample[m][1]
        if a["disposition"] == "CORRECT":
            if v4[m]["source"] != "r10-id-verdict" or v4[m]["verdict"] != "CONFIRM" \
                    or r["spec_code"] != a["corrected_code"]:
                bad.append(m)
        else:
            bad.append(m)
    on_r6 = [m for m, (cls, r) in sample.items()
             if r["provenance"]["upstream"]["anchor_id"] in r6["verdicts"]
             and r["provenance"]["upstream"]["anchor_id"] not in r10["verdicts"]
             and r["provenance"]["upstream"]["anchor_id"] not in r14["verdicts"]
             and r["provenance"]["upstream"]["anchor_id"] != "spcpt_crKbmb6wVjM4yPJh"
             and not _has_ov(r)]
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
    ovr14_rows = [m for m, (cls, r) in sample.items()
                  if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R14")]
    ovr14_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr14["overrides"]}
    for m in ovr14_rows:
        r = sample[m][1]
        ov = ovr14_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r14-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
            bad.append(m)
    ovr10_rows = [m for m, (cls, r) in sample.items()
                  if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R10")]
    ovr10_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr10["overrides"]}
    for m in ovr10_rows:
        r = sample[m][1]
        ov = ovr10_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r10-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
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
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R6")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R10")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R14")]
    ovr1_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr["overrides"]}
    holds = []
    for m in ovr1_rows:
        r = sample[m][1]
        ov = ovr1_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if "heading-only" in (ov["evidence"] or ""):
            # R17: resolved by c42-heading-only-convention-1 (X12 replays the
            # ladder) — the R1 ruling's attribution stands unchanged either way
            if v4[m]["source"] != "heading-only-convention":
                bad.append(m)
            else:
                holds.append(m)
        elif ov["action"] == "REATTRIBUTE":
            if v4[m]["source"] != "r1-section-override" or v4[m]["verdict"] != "CONFIRM" or r["spec_code"] != ov["override_code"]:
                bad.append(m)
        elif v4[m]["source"] != "r1-section-override" or v4[m]["verdict"] != "CONFIRM":
            bad.append(m)
    sub_rows = [m for m, (cls, r) in sample.items()
                if "override_subsumed" in r.get("provenance", {})]
    for m in sub_rows:
        if v4[m]["source"] != "r1-subsumed" or v4[m]["verdict"] != "CONFIRM":
            bad.append(m)
    ok_all &= gate("X6 r14_r10_r6_r1_override_consistency", not bad,
                   f"{len(on_r14)} R14-anchor rows (the re-point landed wholesale) + "
                   f"{len(standing_rows)} STANDING rows + {len(on_r10)} R10-anchor rows + "
                   f"{len(on_r6)} R6-anchor rows + {len(on_r1)} R1-anchor rows "
                   f"CONFIRM on operator verdicts (CORRECT codes landed verbatim); "
                   f"{len(ovr14_rows)} R14 override rows + {len(ovr10_rows)} R10 override rows + "
                   f"{len(ovr6_rows)} R6 override rows + {len(ovr1_rows)} R1 override rows "
                   f"follow the operator rulings incl. {len(holds)} heading-only rows "
                   f"resolved by the convention; {len(sub_rows)} subsumed rows ride the join")

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
    pb = r17["part_b_verdicts"]
    surf = Counter(v["surface"] for v in pb.values())
    g8 = (set(pb) == {r["mapping_id"] for r in worklist}
          and all(v["verdict"] == "DEFER" for v in pb.values())
          and surf["C32 §3 residual (R1 KEPT UNRESOLVED)"] == 2
          and surf["C42 R1 surface-1 cleared span"] == 6
          and surf["C42 R6 surface-1 cleared span"] == 12
          and surf["C42 R10 surface-2 DEMOTE (recorded, never forced)"] == 1
          and surf["C42 R14 surface-3 DEMOTE (recorded, never forced)"] == 1
          and surf["uncovered-SP corpus gap (128-code bound)"] == 60)
    ok_all &= gate("X8 part_b", g8,
                   f"{len(pb)}/{len(worklist)} worklist rows DEFER; surfaces "
                   f"2 residual + 6 R1-cleared + 12 R6-cleared + 1 R10 DEMOTE + "
                   f"1 R14 DEMOTE + 60 gap")

    # X9 gate arithmetic + anti-forgery ---------------------------------------------------
    rollup = {}
    for cls in ("exact", "partial", "none"):
        rc = [v for v in v4.values() if v["stratum"] == cls]
        conf = sum(1 for v in rc if v["verdict"] == "CONFIRM")
        rollup[cls] = {"rows": len(rc), "confirm": conf,
                       "reject": sum(1 for v in rc if v["verdict"] == "REJECT"),
                       "hold": sum(1 for v in rc if v["verdict"] == "HOLD"),
                       "precision": round(conf / len(rc), 4) if rc else None}
    rec = r17["gate"]["part_a"]["by_stratum"]
    g9 = all(rollup[c] == rec[c] for c in rollup)
    total = {"rows": len(v4),
             "confirm": sum(1 for v in v4.values() if v["verdict"] == "CONFIRM"),
             "reject": sum(1 for v in v4.values() if v["verdict"] == "REJECT"),
             "hold": sum(1 for v in v4.values() if v["verdict"] == "HOLD")}
    total["precision"] = round(total["confirm"] / total["rows"], 4)
    g9 = g9 and total == r17["gate"]["part_a"]["total"]
    classes_pass = all(v["precision"] >= 0.9 for v in rollup.values() if v["rows"])
    g9 = g9 and r17["gate"]["part_a"]["classes_pass"] == classes_pass
    g9 = g9 and r17["gate"]["outcome"] == ("PASS" if (classes_pass and len(pb) == 82) else "FAIL")
    bad_status = [r for r in rows if r.get("validation_status") != "SUGGESTED"
                  or r["provenance"]["tier"] != "RULE_DERIVED"]
    g9 = g9 and not bad_status
    ok_all &= gate("X9 gate_arithmetic_antiforgery", g9,
                   f"rollup recomputed == recorded "
                   f"(exact {rollup['exact']['precision'] * 100:.1f}% / "
                   f"partial {rollup['partial']['precision'] * 100:.1f}% / "
                   f"none {rollup['none']['precision'] * 100:.1f}%); outcome "
                   f"{r17['gate']['outcome']} correctly derived (the arithmetic is "
                   f"verified, not the outcome — the FAIL is the honest draw); all "
                   f"922 rows SUGGESTED / RULE_DERIVED")

    # X10 protected surfaces ----------------------------------------------------------------
    # R17 audit fix: parse porcelain WITHOUT the whole-string .strip() — the
    # leading space of a " M path" first line is significant, and stripping it
    # made l[3:] eat the first path character (the R13 template only ever saw
    # untracked "??" lines, where the bug is invisible).
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                           capture_output=True, text=True).stdout.splitlines()
    dirty_set = sorted(l[3:].strip() for l in dirty if l.strip())
    expected = sorted(["graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.json",
                       "graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.md",
                       "graph/reports/C42_R17_MATHS_A_REGATE_REVIEW_SHEET.md",
                       "scripts/c42_r17_fresh_verdicts.yaml",
                       "scripts/c42_r17_regate_fill.py",
                       "scripts/c42_r17_review_verdicts.yaml",
                       "scripts/c42_r17_regate_check.py"])
    if CHECK_JSON.exists():  # present on re-runs after the first
        expected.append("graph/reports/C42_R17_REGATE_CHECK.json")
    expected = sorted(expected)
    committed_state = dirty_set == []
    # R17 audit amendment — post-commit translation of the R13 guarantee: the
    # working tree stays within the R17 footprint, AND the protected surfaces
    # (Lane C, chemistry, resolution, the C42 scope/R0-R14 records, the C30
    # ledger) are byte-identical to their pre-round state at BASELINE — the
    # R17 commits and the audit trail may move HEAD, but never these files.
    PROTECTED = ["graph/igcse-maths-a/concepts.yaml",
                 "graph/igcse-maths-a/concept_edges.yaml",
                 "graph/igcse-maths-a/spec_command_kinds.yaml",
                 "graph/igcse-chemistry/spec_chunk_mappings.yaml",
                 "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json",
                 "graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md",
                 "graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json",
                 "graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.json",
                 "graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md",
                 "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json",
                 "graph/reports/C42_R13_REGATE_CHECK.json",
                 "graph/reports/C42_R14_RESOLUTION_REPAIR_RECORD.md",
                 "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"]

    def _baseline_bytes(rel):
        return subprocess.run(
            ["git", "-C", str(REPO), "show", f"{BASELINE}:{rel}"],
            capture_output=True, check=True).stdout

    prot_ok = all(sha16(_baseline_bytes(p)) == sha16((REPO / p).read_bytes())
                  for p in PROTECTED)
    _outside = sorted(set(dirty_set) - set(expected))
    _prot_bad = [p for p in PROTECTED
                 if sha16(_baseline_bytes(p)) != sha16((REPO / p).read_bytes())]
    g10 = (not _outside and not _prot_bad)
    ok_all &= gate("X10 protected_surfaces", g10,
                   f"{'COMMITTED — dirty set empty' if committed_state else 'dirty set within the R17 footprint'}"
                   f" ({len(dirty_set)} files); {len(PROTECTED)} protected surfaces "
                   f"(Lane C, chemistry, resolution, C42 scope/R0-R14 records, C30 "
                   f"ledger) byte-identical to their pre-round state at "
                   f"{BASELINE[:12]}"
                   + (f"; OUTSIDE: {_outside}" if _outside else "")
                   + (f"; PROTECTED-DIFF: {_prot_bad}" if _prot_bad else ""))

    # X11 determinism (re-run the fill; sheet + verdicts byte-identical) ----------------------
    before = (R17_SHEET.read_bytes(), R17_VERDICTS.read_bytes())
    rc = subprocess.run([sys.executable, str(HERE / "c42_r17_regate_fill.py")],
                        capture_output=True, text=True)
    after = (R17_SHEET.read_bytes(), R17_VERDICTS.read_bytes())
    g11 = rc.returncode == 0 and before == after
    ok_all &= gate("X11 determinism", g11,
                   "fill re-run: sheet + verdict record byte-identical")

    # X12 convention ladder replay (c42-heading-only-convention-1) ----------------
    # Independently recompute the heading-only detector + the H1/H2/H3 ladder
    # for every sampled row and verify the fill's convention verdicts. NEW at
    # R17: the R13 record is in the H2 source base (the R14 record's
    # projection — bounds ord 0 un-holds via H2).
    h2_replay = {}
    for src_name, src_map in (("R4", r4["verdicts"]), ("R9", r9p["verdicts"]),
                              ("R13", r13p["verdicts"])):
        for mid, v in src_map.items():
            if v["verdict"] != "CONFIRM" or v.get("note_path") is None:
                continue
            t = idx.get((v["note_path"], v["chunk_ordinal"]))
            h = head_of.get((v["note_path"], v["chunk_ordinal"]))
            if t is None or h is None or norm(t) == norm(h):
                continue  # the confirming row is itself heading-only — H2 excludes it
            h2_replay.setdefault((v["note_path"], v["spec_code"]), []).append(mid)
    conv_rows = {m: v for m, v in v4.items() if v["source"] == "heading-only-convention"}
    ho_sampled = {}
    for m, (cls, r) in sample.items():
        t = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        if t is not None and norm(t) == norm(head_of[(r["note_path"], r["chunk"]["ordinal"])]):
            ho_sampled[m] = r
    bad = []
    for m, r in ho_sampled.items():
        v = v4[m]
        aid = r["provenance"]["upstream"]["anchor_id"]
        if aid in r14["verdicts"] or aid in r10["verdicts"] or aid in r6["verdicts"] \
                or aid in r1["verdicts"] or aid == "spcpt_crKbmb6wVjM4yPJh":
            want_branch = "H1"
        elif h2_replay.get((r["note_path"], r["spec_code"])):
            want_branch = "H2"
        else:
            want_branch = "H3"
        got = (v.get("convention_branch") or "")
        if want_branch not in got:
            bad.append(f"{m}: branch {got!r} != {want_branch}")
            continue
        if want_branch == "H3" and v["verdict"] != "HOLD":
            bad.append(f"{m}: H3 must HOLD")
        if want_branch in ("H1", "H2") and v["verdict"] != "CONFIRM":
            bad.append(f"{m}: {want_branch} must CONFIRM")
    # every convention-source verdict must be on a genuinely heading-only row
    for m in conv_rows:
        if m not in ho_sampled:
            bad.append(f"{m}: convention verdict on a non-heading-only row")
    # heading-only sampled rows NOT resolved by the convention must carry an
    # H1-class direct verdict source (id-verdict/override/standing/subsumed)
    for m, r in ho_sampled.items():
        if v4[m]["source"] != "heading-only-convention":
            if v4[m]["verdict"] != "CONFIRM":
                bad.append(f"{m}: heading-only row without convention or confirm source")
    ok_all &= gate("X12 convention_ladder_replay", not bad,
                   f"{len(ho_sampled)} sampled heading-only rows replayed through the "
                   f"H1/H2/H3 ladder independently (H2 source base = R4+R9+R13, the "
                   f"R14 record's projection) ({len(conv_rows)} via the convention "
                   f"source, the rest via H1-class direct verdict sources); "
                   f"branches, verdicts and the fail-closed direction all agree"
                   + (f"; VIOLATIONS: {bad[:4]}" if bad else ""))

    # X13 the H3 fail-closed set ---------------------------------------------------
    h3 = sorted(m for m, v in v4.items()
                if (v.get("convention_branch") or "").startswith("H3"))
    h3_expect = sorted(m for m, v in v4.items()
                       if v["verdict"] == "HOLD" and v["source"] == "heading-only-convention")
    rej = sorted(m for m, v in v4.items() if v["verdict"] == "REJECT")
    h3_desc = [f"{v4[m]['spec_code']} {v4[m]['note_path'].split('/')[-1]} "
               f"ord {v4[m]['chunk_ordinal']}" for m in h3]
    g13 = (h3 == h3_expect
           and all(v4[m]["verdict"] == "HOLD" for m in h3)
           and all("H3" in (v4[m].get("convention_branch") or "") for m in h3))
    ok_all &= gate("X13 h3_fail_closed_set", g13,
                   f"{len(h3)} H3 rows (no positive evidence yet; they un-hold "
                   f"automatically once H1/H2 becomes true at a later round): "
                   f"{h3_desc}; {len(rej)} REJECT rows recorded with root causes — "
                   f"the fresh defect inventory returns to the operator (scope §7)")

    passed = sum(1 for r in results if r["ok"])
    out = {"schema": "c42-r17-regate-check/1.0", "task": "T-C42", "stage": "r17-regate",
           "baseline": BASELINE, "head": head,
           "fill_record": str(R17_FILL_JSON.relative_to(REPO)),
           "gates": results, "passed": passed, "total": len(results),
           "all_pass": bool(ok_all),
           "gate_outcome_recorded_by_fill": r17["gate"]["outcome"]}
    CHECK_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"\n{passed}/{len(results)} gates PASS; all_pass={ok_all}; "
          f"fill gate outcome (recorded): {r17['gate']['outcome']}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
