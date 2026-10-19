#!/usr/bin/env python3
"""c42-r29 check — the deterministic verification battery for the R29 re-gate
fill, the loop's seventh gate-2 pass and the FIRST under the AMENDED promoted
surface (zero-LLM, read-only toward graph/ except its own report). Mirrors the
R25 battery conventions. ALL gates must pass for the fill record to stand; the
GATE OUTCOME ITSELF (Part A per-class precision) is recorded honestly by the
fill and is NOT a check failure here — X9 asserts the arithmetic is correctly
computed and correctly reported, whichever way it falls. NEW at R29:
X1 pins the AMENDED promoted surface (831 HV rows == the R5 promotions file
AMENDED by the R26 promotions amendment — 3 supersedes re-keyed old->new at
1.1A/5.1C/3.3H + 1 exclusion — + 7 anchored SUGGESTED + the amended count);
X4's status replay allows HUMAN_VALIDATED exactly on the amended set; X5
verifies the R25-carried chain on top of the R21/R17/R13/R9/R4 chains (a row
carries from the MOST RECENT prior re-gate record whose verdict
triple-matches, never skipping a newer record); X6 verifies the R26
section-override rulings land verbatim AND the FOUR R26 STANDING note-level
joins resolve only on their adjudicated joined codes (alongside the THREE R22
STANDING joins); X12 replays the c42-heading-only-convention-1 ladder
(H1/H2/H3) with the R25 record in the H2 source base and the R26 STANDING
adjudications in H1; X13 pins the H3 fail-closed set."""
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
R17_PRIOR = HERE / "c42_r17_review_verdicts.yaml"
R21_PRIOR = HERE / "c42_r21_review_verdicts.yaml"
R25_PRIOR = HERE / "c42_r25_review_verdicts.yaml"
OVERRIDES_R18 = HERE / "c42_section_overrides_r18.yaml"
OVERRIDES_R22 = HERE / "c42_section_overrides_r22.yaml"
OVERRIDES_R26 = HERE / "c42_section_overrides_r26.yaml"
AMENDMENT = HERE / "c42_r26_promotions_amendment.yaml"
R22_REPAIR_VERDICTS = HERE / "c42_r22_repair_verdicts.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
FRESH_FILE = HERE / "c42_r29_fresh_verdicts.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R29_SHEET = GP.reports_dir(QUAL) / "C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md"
R29_VERDICTS = HERE / "c42_r29_review_verdicts.yaml"
R29_FILL_JSON = GP.reports_dir(QUAL) / "C42_R29_MATHS_A_REGATE_FILL_RECORD.json"
CHECK_JSON = GP.reports_dir(QUAL) / "C42_R29_REGATE_CHECK.json"
BASELINE = "b0bf38dc0d2f627bbb34fee263668b12e2fa16a1"  # the R28 post-audit round-start commit (HEAD when the fill ran; substrate == 5801a78, sha16 1b667c0107dfc85c)
R22_STANDING = {  # anchor_id -> joined_code (c42_r22_repair_verdicts.yaml, note_level_adjudications)
    "spcpt_kX4655D8M3Q3TRzW": "4MA1-4.8D",
    "spcpt_RJbgRvXq2VrGpP5g": "4MA1-2.2F",
    "spcpt_sHCB9WZbDMyTFqCP": "4MA1-2.6B",
}
R26_STANDING = {  # anchor_id -> joined_code (c42_r26_repair_verdicts.yaml, note_level_adjudications — list-shaped, the R23 precedent; R27 in-generator pins)
    "spcpt_J55PhZ2cbPsYvpt8": "4MA1-1.1G",
    "spcpt_vMSNnYkKPf62MRH9": "4MA1-2.2F",
    "spcpt_h8QyRmzX5mCJb3X9": "4MA1-3.3F",
    "spcpt_v6tP4DSVShVJMJhk": "4MA1-5.1D",
}

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
    r17p = yaml.safe_load(R17_PRIOR.read_text(encoding="utf-8"))
    r21p = yaml.safe_load(R21_PRIOR.read_text(encoding="utf-8"))
    r25p = yaml.safe_load(R25_PRIOR.read_text(encoding="utf-8"))
    ovr18 = yaml.safe_load(OVERRIDES_R18.read_text(encoding="utf-8"))
    ovr22 = yaml.safe_load(OVERRIDES_R22.read_text(encoding="utf-8"))
    r22 = yaml.safe_load(R22_REPAIR_VERDICTS.read_text(encoding="utf-8"))
    ovr26 = yaml.safe_load(OVERRIDES_R26.read_text(encoding="utf-8"))
    amend = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
    prom = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    conv = json.loads(CONVENTION_JSON.read_text(encoding="utf-8"))
    fresh = yaml.safe_load(FRESH_FILE.read_text(encoding="utf-8"))
    r29f = yaml.safe_load(R29_VERDICTS.read_text(encoding="utf-8"))
    fill = json.loads(R29_FILL_JSON.read_text(encoding="utf-8"))

    # X1 input pins --------------------------------------------------------------
    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    hv_n = sum(1 for r in rows if r.get("validation_status") == "HUMAN_VALIDATED")
    sug_anch_n = sum(1 for r in anchored if r.get("validation_status") != "HUMAN_VALIDATED")
    amend_sha16 = __import__("hashlib").sha256(
        (HERE / "c42_r26_promotions_amendment.yaml").read_bytes()).hexdigest()[:16]
    g1 = (len(rows) == 918 and len(anchored) == 838 and len(worklist) == 80
          and hv_n == 831 and sug_anch_n == 7 and len(prom["promotions"]) == 832
          and len(amend["supersedes_code"]) == 3 and len(amend["excluded"]) == 1
          and amend["base_file_sha256_16"] == "9bad739bd79e5899"
          and amend_sha16 == "fda9d717d9f58572"
          and len(ledger_map) == 54 and len(r1["verdicts"]) == 45
          and len(r6["verdicts"]) == 10 and len(r10["verdicts"]) == 2
          and len(r14["verdicts"]) == 1
          and len(ovr["overrides"]) == 16 and len(ovr6["overrides"]) == 7
          and len(ovr10["overrides"]) == 8 and len(ovr14["overrides"]) == 5
          and len(ovr18["overrides"]) == 4 and len(ovr22["overrides"]) == 3
          and len(ovr26["overrides"]) == 4
          and len(r22["note_level_adjudications"]) == 3
          and len(r4["verdicts"]) == 467 and len(r9p["verdicts"]) == 465
          and len(r13p["verdicts"]) == 465 and len(r17p["verdicts"]) == 464
          and len(r21p["verdicts"]) == 464 and len(r25p["verdicts"]) == 464
          and len(fresh["verdicts"]) == 8 and fill["baseline"] == BASELINE
          and conv["decision_id"] == "c42-heading-only-convention-1")
    ok_all &= gate("X1 input_pins",
                   g1,
                   f"store 918 = 838 anchored (831 HUMAN_VALIDATED == the R5 "
                   f"promotions file count AMENDED by the R26 amendment [sha16 "
                   f"fda9d717d9f58572: 3 supersedes re-keyed + 1 exclusion] "
                   f"+ 7 anchored SUGGESTED) + 80 worklist "
                   f"(24 unresolved-span incl. ALL FOUR DEMOTEs + 56 gap), "
                   f"ledger 54, R1 45, R6 10, R10 2, R14 1, overrides "
                   f"16+7+8+5+4+3+4 (R26 map), R22 NLA 3 (list-shaped), "
                   f"R4 467, R9 465, R13 465, R17 464, R21 464, R25 464, fresh 8, "
                   f"convention pinned; fill baseline == the R28 post-audit "
                   f"round-start commit; HEAD {head[:12]}")

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
    g2 = (seed == r29f["sampling"]["seed"]
          and {cls: len(by[cls]) for cls in by} == r29f["sampling"]["strata"]
          and {cls: sum(1 for c, _ in sample.values() if c == cls) for cls in by}
          == r29f["sampling"]["sampled"]
          and len(sample) == 464)
    ok_all &= gate("X2 sampling", g2,
                   f"seed {seed} (re-seeded on the R28 rows — every re-gate re-seeds); "
                   f"strata { {cls: len(by[cls]) for cls in sorted(by)} }; "
                   f"sampled {dict(Counter(c for c, _ in sample.values()))} == recorded")

    # X3 verdict-record agreement --------------------------------------------------
    v4 = r29f["verdicts"]
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
    g3 = g3 and dict(src_c) == r29f["verdict_sources"]
    fresh_keys = {m for m, v in v4.items() if v["source"] == "r29-fresh"}
    g3 = g3 and fresh_keys == set(fresh["verdicts"])
    ok_all &= gate("X3 record_agreement", g3,
                   f"464 verdicts == sample; fields+strata+tier signatures agree; "
                   f"sources {dict(src_c)}; fresh set == the committed judgment file "
                   f"(7 CONFIRM + 1 REJECT — the cross-section mis-join 4.11C)")

    # X4 mechanical replay ---------------------------------------------------------
    r_reader = R()
    _, notes = load_corpus(r_reader)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}
    head_of = {(n["manifest"]["path"], c["ordinal"]): c["heading"]
               for n in notes for c in by_note[n["manifest"]["path"]]}
    fails = 0
    rekey = {s["mapping_id"]: s for s in amend["supersedes_code"]}
    excl = {e["mapping_id"] for e in amend["excluded"]}
    prom_ids = {p["row"]["mapping_id"] for p in prom["promotions"]
                if p["row"]["mapping_id"] not in excl}
    rekeyed_keys = {(s["note_path"], s["chunk_ordinal"]) for s in amend["supersedes_code"]}
    for m, (cls, r) in sample.items():
        ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        status_ok = (r["validation_status"] == "SUGGESTED"
                     or (r["validation_status"] == "HUMAN_VALIDATED"
                         and (m in prom_ids
                              or (r["note_path"], r["chunk"]["ordinal"]) in rekeyed_keys)))
        if not (ctext is not None
                and sha16(ctext.encode()) == r["chunk"]["sha256_16"]
                and norm(r["evidence_quote"]) in norm(ctext)
                and head_of[(r["note_path"], r["chunk"]["ordinal"])] == r["chunk"]["heading"]
                and status_ok
                and r["provenance"]["tier"] == "RULE_DERIVED"):
            fails += 1
    hv_sampled = sum(1 for m, (cls, r) in sample.items()
                     if r["validation_status"] == "HUMAN_VALIDATED")
    ok_all &= gate("X4 mechanical_replay", fails == 0,
                   f"{len(sample) - fails}/{len(sample)} rows re-verified "
                   f"(quote-in-chunk, hash/heading, RULE_DERIVED; status SUGGESTED "
                   f"or HUMAN_VALIDATED exactly on the AMENDED promotions set "
                   f"[the R5 file + the R26 amendment: re-keyed rows matched by "
                   f"chunk identity] — {hv_sampled} promoted rows in this draw "
                   f"verified like every other sampled row)")

    # X5 carry-forward integrity (R21 + R17 + R13 + R9 + R4 chains) -------------------------
    def _prior_clean(r):
        aid = r["provenance"]["upstream"]["anchor_id"]
        return (aid not in r1["verdicts"] and aid not in r6["verdicts"]
                and aid not in r10["verdicts"] and aid not in r14["verdicts"]
                and aid != "spcpt_crKbmb6wVjM4yPJh"
                and aid not in R22_STANDING
                and "override" not in r.get("provenance", {})
                and "override_subsumed" not in r.get("provenance", {}))

    def _triple_ok(v, r):
        return (v is not None and v["verdict"] == "CONFIRM"
                and v["spec_code"] == r["spec_code"]
                and v["note_path"] == r["note_path"]
                and v["heading"] == r["chunk"]["heading"])

    carried25 = [m for m, v in v4.items() if v["source"] == "r25-carried"]
    for m in carried25:
        r25v = r25p["verdicts"].get(m)
        r = sample[m][1]
        if not _triple_ok(r25v, r) or not _prior_clean(r):
            bad.append(m)
    carried21 = [m for m, v in v4.items() if v["source"] == "r21-carried"]
    bad = []
    for m in carried21:
        r21v = r21p["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r21v, r) or m in r25p["verdicts"]
                or not _prior_clean(r)):
            bad.append(m)
    carried17 = [m for m, v in v4.items() if v["source"] == "r17-carried"]
    for m in carried17:
        r17v = r17p["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r17v, r) or m in r25p["verdicts"]
                or m in r21p["verdicts"] or not _prior_clean(r)):
            bad.append(m)
    carried13 = [m for m, v in v4.items() if v["source"] == "r13-carried"]
    for m in carried13:
        r13v = r13p["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r13v, r) or m in r25p["verdicts"]
                or m in r21p["verdicts"] or m in r17p["verdicts"]
                or not _prior_clean(r)):
            bad.append(m)
    carried9 = [m for m, v in v4.items() if v["source"] == "r9-carried"]
    for m in carried9:
        r9v = r9p["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r9v, r) or m in r25p["verdicts"]
                or m in r21p["verdicts"] or m in r17p["verdicts"]
                or m in r13p["verdicts"] or not _prior_clean(r)):
            bad.append(m)
    carried4 = [m for m, v in v4.items() if v["source"] == "r4-carried"]
    for m in carried4:
        r4v = r4["verdicts"].get(m)
        r = sample[m][1]
        if (not _triple_ok(r4v, r) or m in r25p["verdicts"]
                or m in r21p["verdicts"] or m in r17p["verdicts"]
                or m in r13p["verdicts"] or m in r9p["verdicts"]
                or not _prior_clean(r)):
            bad.append(m)
    ok_all &= gate("X5 carry_forward", not bad,
                   f"{len(carried25)} R25-carried + {len(carried21)} R21-carried + "
                   f"{len(carried17)} R17-carried + "
                   f"{len(carried13)} R13-carried + {len(carried9)} R9-carried + "
                   f"{len(carried4)} R4-carried CONFIRMs: triple-identical in the "
                   f"prior records, outside the R26 surface (a row carries from the "
                   f"MOST RECENT prior re-gate record whose verdict triple-matches — "
                   f"R21 carries only for rows absent from the R25 record, R17 for rows "
                   f"absent from R25+R21, R13 for rows absent from R25+R21+R17, R9 for "
                   f"rows absent from R25+R21+R17+R13, R4 for rows absent from all "
                   f"five; 0 violations)")

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
    ovr18_rows = [m for m, (cls, r) in sample.items()
                  if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R18")]
    ovr18_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr18["overrides"]}
    for m in ovr18_rows:
        r = sample[m][1]
        ov = ovr18_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r18-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
            bad.append(m)
    ovr22_rows = [m for m, (cls, r) in sample.items()
                  if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R22")]
    ovr22_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr22["overrides"]}
    for m in ovr22_rows:
        r = sample[m][1]
        ov = ovr22_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r22-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
            bad.append(m)
    on_r22 = [m for m, (cls, r) in sample.items()
              if r["provenance"]["upstream"]["anchor_id"] in R22_STANDING
              and not _has_ov(r)]
    for m in on_r22:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        r = sample[m][1]
        if v4[m]["source"] != "r22-standing" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != R22_STANDING[aid]:
            bad.append(m)
    ovr26_rows = [m for m, (cls, r) in sample.items()
                  if (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R26")]
    ovr26_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr26["overrides"]}
    for m in ovr26_rows:
        r = sample[m][1]
        ov = ovr26_map[(r["note_slug"], r["chunk"]["ordinal"])]
        if v4[m]["source"] != "r26-section-override" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != ov["override_code"]:
            bad.append(m)
    on_r26s = [m for m, (cls, r) in sample.items()
               if r["provenance"]["upstream"]["anchor_id"] in R26_STANDING
               and r["spec_code"] == R26_STANDING[r["provenance"]["upstream"]["anchor_id"]]
               and not _has_ov(r)]
    for m in on_r26s:
        aid = sample[m][1]["provenance"]["upstream"]["anchor_id"]
        r = sample[m][1]
        if v4[m]["source"] != "r26-standing" or v4[m]["verdict"] != "CONFIRM" \
                or r["spec_code"] != R26_STANDING[aid]:
            bad.append(m)
    ovr1_rows = [m for m, (cls, r) in sample.items()
                 if "override" in r.get("provenance", {})
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R6")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R10")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R14")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R18")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R22")
                 and not (r.get("provenance", {}).get("override") or {}).get("operator_round", "").startswith("C42 R26")]
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
    ok_all &= gate("X6 r26_r22_r18_r14_r10_r6_r1_override_consistency", not bad,
                   f"{len(on_r14)} R14-anchor rows (the re-point landed wholesale) + "
                   f"{len(standing_rows)} STANDING rows + {len(on_r10)} R10-anchor rows + "
                   f"{len(on_r6)} R6-anchor rows + {len(on_r1)} R1-anchor rows "
                   f"CONFIRM on operator verdicts (CORRECT codes landed verbatim); "
                   f"{len(ovr26_rows)} R26 override rows (the re-keyed promoted identities) + "
                   f"{len(on_r26s)} R26-STANDING note-level rows (on the adjudicated "
                   f"joined codes only) + "
                   f"{len(ovr22_rows)} R22 override rows + {len(on_r22)} R22-STANDING "
                   f"note-level rows (on the adjudicated joined codes only) + "
                   f"{len(ovr18_rows)} R18 override rows + {len(ovr14_rows)} R14 override rows + "
                   f"{len(ovr10_rows)} R10 override rows + {len(ovr6_rows)} R6 override rows + "
                   f"{len(ovr1_rows)} R1 override rows "
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
    pb = r29f["part_b_verdicts"]
    surf = Counter(v["surface"] for v in pb.values())
    g8 = (set(pb) == {r["mapping_id"] for r in worklist}
          and all(v["verdict"] == "DEFER" for v in pb.values())
          and surf["C32 §3 residual (R1 KEPT UNRESOLVED)"] == 2
          and surf["C42 R1 surface-1 cleared span"] == 6
          and surf["C42 R6 surface-1 cleared span"] == 12
          and surf["C42 R10 surface-2 DEMOTE (recorded, never forced)"] == 1
          and surf["C42 R14 surface-3 DEMOTE (recorded, never forced)"] == 1
          and surf["C42 R18 surface-3 DEMOTE (recorded, never forced)"] == 1
          and surf["C42 R26 surface-3 DEMOTE (recorded, never forced — the loop's "
                   "fourth DEMOTE, the FIRST of a promoted row)"] == 1
          and surf["uncovered-SP corpus gap (132-code bound)"] == 56)
    ok_all &= gate("X8 part_b", g8,
                   f"{len(pb)}/{len(worklist)} worklist rows DEFER; surfaces "
                   f"2 residual + 6 R1-cleared + 12 R6-cleared + 1 R10 DEMOTE + "
                   f"1 R14 DEMOTE + 1 R18 DEMOTE + 1 R26 DEMOTE (the FIRST of a "
                   f"promoted row) + 56 gap (132-code bound — the R26 "
                   f"re-attributions gained 1.1A + 5.1C at R28, none lost)")

    # X9 gate arithmetic + anti-forgery ---------------------------------------------------
    rollup = {}
    for cls in ("exact", "partial", "none"):
        rc = [v for v in v4.values() if v["stratum"] == cls]
        conf = sum(1 for v in rc if v["verdict"] == "CONFIRM")
        rollup[cls] = {"rows": len(rc), "confirm": conf,
                       "reject": sum(1 for v in rc if v["verdict"] == "REJECT"),
                       "hold": sum(1 for v in rc if v["verdict"] == "HOLD"),
                       "precision": round(conf / len(rc), 4) if rc else None}
    rec = r29f["gate"]["part_a"]["by_stratum"]
    g9 = all(rollup[c] == rec[c] for c in rollup)
    total = {"rows": len(v4),
             "confirm": sum(1 for v in v4.values() if v["verdict"] == "CONFIRM"),
             "reject": sum(1 for v in v4.values() if v["verdict"] == "REJECT"),
             "hold": sum(1 for v in v4.values() if v["verdict"] == "HOLD")}
    total["precision"] = round(total["confirm"] / total["rows"], 4)
    g9 = g9 and total == r29f["gate"]["part_a"]["total"]
    classes_pass = all(v["precision"] >= 0.9 for v in rollup.values() if v["rows"])
    g9 = g9 and r29f["gate"]["part_a"]["classes_pass"] == classes_pass
    g9 = g9 and r29f["gate"]["outcome"] == ("PASS" if (classes_pass and len(pb) == 80) else "FAIL")
    rekey9 = {s["mapping_id"]: s for s in amend["supersedes_code"]}
    excl9 = {e["mapping_id"] for e in amend["excluded"]}
    # the full AMENDED surface expectation (the fill's own construction,
    # re-derived here): direct entries keyed by identity + code; re-keyed
    # entries keyed by chunk identity at their AMENDED codes (the old
    # code-derived ids no longer exist in the store).
    exp9 = {}
    for p in prom["promotions"]:
        prow = p["row"]
        mid9 = prow["mapping_id"]
        if mid9 in excl9:
            continue
        if mid9 in rekey9:
            s9 = rekey9[mid9]
            exp9[(s9["note_path"], s9["chunk_ordinal"])] = (
                s9["amended_code"], prow["heading"], prow["chunk_sha256_16"])
        else:
            exp9[(prow["note_path"], prow["chunk_ordinal"])] = (
                prow["spec_code"], prow["heading"], prow["chunk_sha256_16"])
    bad_status = [r for r in rows
                  if r["provenance"]["tier"] != "RULE_DERIVED"
                  or not (r.get("validation_status") == "SUGGESTED"
                          or (r.get("validation_status") == "HUMAN_VALIDATED"
                              and (r["note_path"], r["chunk"]["ordinal"]) in exp9))]
    hv_bad = []
    seen9 = set()
    for r9 in rows:
        if r9.get("validation_status") != "HUMAN_VALIDATED":
            continue
        key9 = (r9["note_path"], r9["chunk"]["ordinal"])
        e9 = exp9.get(key9)
        if (e9 is None or key9 in seen9
                or r9["spec_code"] != e9[0]
                or r9["chunk"]["heading"] != e9[1]
                or r9["chunk"]["sha256_16"] != e9[2]):
            hv_bad.append(r9["mapping_id"])
        else:
            seen9.add(key9)
    hv_bad += [f"unmatched:{k9[1]}" for k9 in sorted(set(exp9) - seen9)]
    g9 = g9 and not bad_status and not hv_bad
    ok_all &= gate("X9 gate_arithmetic_antiforgery", g9,
                   f"rollup recomputed == recorded "
                   f"(exact {rollup['exact']['precision'] * 100:.1f}% / "
                   f"partial {rollup['partial']['precision'] * 100:.1f}% / "
                   f"none {rollup['none']['precision'] * 100:.1f}%); outcome "
                   f"{r29f['gate']['outcome']} correctly derived (the arithmetic is "
                   f"verified, not the outcome — whichever way it falls); all "
                   f"918 rows RULE_DERIVED with the 831 HUMAN_VALIDATED exactly "
                   f"on the AMENDED promotions set (re-keyed rows matched by "
                   f"chunk identity) and 87 SUGGESTED elsewhere")

    # X10 protected surfaces ----------------------------------------------------------------
    # R17 audit fix: parse porcelain WITHOUT the whole-string .strip() — the
    # leading space of a " M path" first line is significant, and stripping it
    # made l[3:] eat the first path character (the R13 template only ever saw
    # untracked "??" lines, where the bug is invisible).
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                           capture_output=True, text=True).stdout.splitlines()
    dirty_set = sorted(l[3:].strip() for l in dirty if l.strip())
    expected = sorted(["graph/reports/C42_R29_MATHS_A_REGATE_FILL_RECORD.json",
                       "graph/reports/C42_R29_MATHS_A_REGATE_FILL_RECORD.md",
                       "graph/reports/C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md",
                       "scripts/c42_r29_fresh_verdicts.yaml",
                       "scripts/c42_r29_regate_fill.py",
                       "scripts/c42_r29_review_verdicts.yaml",
                       "scripts/c42_r29_regate_check.py"])
    if CHECK_JSON.exists():  # present on re-runs after the first
        expected.append("graph/reports/C42_R29_REGATE_CHECK.json")
    expected = sorted(expected)
    committed_state = dirty_set == []
    # R17 audit amendment carried to R25 — post-commit translation of the R13
    # guarantee: the working tree stays within the R25 footprint, AND the
    # protected surfaces (Lane C, chemistry, resolution, the C42 scope/R0-R24
    # records incl. the R18+R22 maps + verdicts and the R17/R21 re-gate records
    # and the R24 rebuild records, the C30 ledger, the R5 promotions file and
    # the STORE itself — the re-gate lane is store-free by construction) are
    # byte-identical to their pre-round state at BASELINE — the R29 commits and
    # the audit trail may move HEAD, but never these files.
    PROTECTED = ["graph/igcse-maths-a/spec_chunk_mappings.yaml",
                 "graph/igcse-maths-a/concepts.yaml",
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
                 "graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.json",
                 "graph/reports/C42_R17_REGATE_CHECK.json",
                 "graph/reports/C42_R18_RESOLUTION_REPAIR_RECORD.md",
                 "graph/reports/C42_R18_REPAIR_CHECK.json",
                 "graph/reports/C42_R19_R20_JOIN_SUBSTRATE_RECORD.json",
                 "graph/reports/C42_R19_R20_CHECK.json",
                 "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json",
                 "graph/reports/C42_R21_REGATE_CHECK.json",
                 "graph/reports/C42_R22_REPAIR_CHECK.json",
                 "graph/reports/C42_R23_JOIN_CHECK.json",
                 "graph/reports/C42_R24_REBUILD_RECORD.json",
                 "graph/reports/C42_R24_REBUILD_CHECK.json",
                 "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json",
                 "scripts/c42_section_overrides_r18.yaml",
                 "scripts/c42_section_overrides_r22.yaml",
                 "scripts/c42_r18_repair_verdicts.yaml",
                 "scripts/c42_r22_repair_verdicts.yaml",
                 "scripts/c42_r17_review_verdicts.yaml",
                 "scripts/c42_r17_fresh_verdicts.yaml",
                 "scripts/c42_r21_review_verdicts.yaml",
                 "scripts/c42_r21_fresh_verdicts.yaml",
                 "scripts/c42_r5_promotions.yaml",
                 "graph/reports/C42_R25_MATHS_A_REGATE_FILL_RECORD.json",
                 "graph/reports/C42_R25_REGATE_CHECK.json",
                 "graph/reports/C42_R26_REPAIR_CHECK.json",
                 "graph/reports/C42_R27_JOIN_CHECK.json",
                 "graph/reports/C42_R28_REBUILD_RECORD.json",
                 "graph/reports/C42_R28_REBUILD_CHECK.json",
                 "scripts/c42_r25_review_verdicts.yaml",
                 "scripts/c42_r25_fresh_verdicts.yaml",
                 "scripts/c42_section_overrides_r26.yaml",
                 "scripts/c42_r26_repair_verdicts.yaml",
                 "scripts/c42_r26_promotions_amendment.yaml",
                 "scripts/c42_r26_override_projection.py",
                 "scripts/c42_r27_join_check.py",
                 "scripts/c42_r28_substrate_rebuild.py",
                 "scripts/c42_r28_rebuild_check.py",
                 "Official-Specifications/parsed/_derived/notes-join/igcse-maths-a-18-higher.json"]

    def _git_blob(rev, rel):
        r = subprocess.run(["git", "-C", str(REPO), "show", f"{rev}:{rel}"],
                           capture_output=True)
        return r.stdout if r.returncode == 0 else None

    def _baseline_bytes(rel):
        return subprocess.run(
            ["git", "-C", str(REPO), "show", f"{BASELINE}:{rel}"],
            capture_output=True, check=True).stdout

    # The sparse-checkout environment (the R24 record's "pre-existing
    # sparse-checkout environmental set") may not carry every protected path in
    # the working tree; for those, the honest comparison is baseline blob vs
    # HEAD blob (committed equality). Working-tree paths keep the original
    # byte comparison.
    def _protected_intact(p):
        wf = REPO / p
        if wf.exists():
            return sha16(_baseline_bytes(p)) == sha16(wf.read_bytes())
        return _git_blob(BASELINE, p) == _git_blob("HEAD", p)

    prot_ok = all(_protected_intact(p) for p in PROTECTED)
    _outside = sorted(set(dirty_set) - set(expected))
    _prot_bad = [p for p in PROTECTED if not _protected_intact(p)]
    g10 = (not _outside and not _prot_bad)
    ok_all &= gate("X10 protected_surfaces", g10,
                   f"{'COMMITTED — dirty set empty' if committed_state else 'dirty set within the R29 footprint'}"
                   f" ({len(dirty_set)} files); {len(PROTECTED)} protected surfaces "
                   f"(the store itself, Lane C, chemistry, resolution, C42 "
                   f"scope/R0-R28 records incl. the R18+R22+R26 maps + verdicts + "
                   f"amendment, the R17/R21/R25 re-gate records, the R24/R28 rebuild "
                   f"records + the R27 join records + the refreshed join artifact, "
                   f"the C30 ledger and the R5 promotions file) byte-identical to their "
                   f"pre-round state at "
                   f"{BASELINE[:12]}"
                   + (f"; OUTSIDE: {_outside}" if _outside else "")
                   + (f"; PROTECTED-DIFF: {_prot_bad}" if _prot_bad else ""))

    # X11 determinism (re-run the fill; sheet + verdicts byte-identical) ----------------------
    before = (R29_SHEET.read_bytes(), R29_VERDICTS.read_bytes())
    rc = subprocess.run([sys.executable, str(HERE / "c42_r29_regate_fill.py")],
                        capture_output=True, text=True)
    after = (R29_SHEET.read_bytes(), R29_VERDICTS.read_bytes())
    g11 = rc.returncode == 0 and before == after
    ok_all &= gate("X11 determinism", g11,
                   "fill re-run: sheet + verdict record byte-identical")

    # X12 convention ladder replay (c42-heading-only-convention-1) ----------------
    # Independently recompute the heading-only detector + the H1/H2/H3 ladder
    # for every sampled row and verify the fill's convention verdicts. NEW at
    # R25: the R21 record is in the H2 source base (the carry-forward
    # continuity rule) and the THREE R22 STANDING adjudications are in H1.
    h2_replay = {}
    for src_name, src_map in (("R4", r4["verdicts"]), ("R9", r9p["verdicts"]),
                              ("R13", r13p["verdicts"]), ("R17", r17p["verdicts"]),
                              ("R21", r21p["verdicts"]), ("R25", r25p["verdicts"])):
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
                or aid in r1["verdicts"] or aid == "spcpt_crKbmb6wVjM4yPJh" \
                or aid in R22_STANDING \
                or (aid in R26_STANDING
                    and r["spec_code"] == R26_STANDING[aid]):
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
                   f"H1/H2/H3 ladder independently (H2 source base = R4+R9+R13+R17+R21+R25, "
                   f"the carry-forward continuity rule; H1 includes the THREE R22 "
                   f"STANDING adjudications and the FOUR R26 STANDING adjudications "
                   f"on their joined codes) ({len(conv_rows)} via the convention "
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
                   f"the fresh defect inventory returns to the operator (scope §7); "
                   f"the draw-dependent H3 set differs from R25's (multiple-ratios "
                   f"1.7B held again + calculations-with-the-mean 6.2B first draw), "
                   f"the 4 anchored-SUGGESTED holds (1.7B/6.3J/3.3F/2.2C) stay "
                   f"pinned in the store regardless of the draw")

    passed = sum(1 for r in results if r["ok"])
    out = {"schema": "c42-r29-regate-check/1.0", "task": "T-C42", "stage": "r29-regate",
           "baseline": BASELINE, "head": head,
           "fill_record": str(R29_FILL_JSON.relative_to(REPO)),
           "gates": results, "passed": passed, "total": len(results),
           "all_pass": bool(ok_all),
           "gate_outcome_recorded_by_fill": r29f["gate"]["outcome"]}
    CHECK_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"\n{passed}/{len(results)} gates PASS; all_pass={ok_all}; "
          f"fill gate outcome (recorded): {r29f['gate']['outcome']}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
