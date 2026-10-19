#!/usr/bin/env python3
"""c42_r5_promotion_check.py — the two-way audit for the T-C42 R5 §18 substrate
apply (the c11.13 / c41_maths_a_promotion_check.py analog, instantiated for the
c40-chunk-convention-1 store).

Audits the REAL repo files in both directions, fail-closed, zero-LLM:

  store -> record : every HUMAN_VALIDATED row is an exact promotions entry
                    (mapping_id + spec_code + note_path + chunk_ordinal +
                    heading + chunk_sha256_16) with exact operator attribution;
  record -> store : every promotions entry lands on exactly one store row that
                    is HUMAN_VALIDATED and carries the promotion block;
  exclusions      : the 3 REJECT rows, the 4 H3 HOLD rows and the 82 worklist
                    rows are NOT promoted and stay SUGGESTED (recorded, never
                    forced);
  structural      : the non-validation delta vs the pinned pre-apply baseline
                    blob (git) is exactly zero outside the 832 promoted rows'
                    validation_status/promotion fields + the meta promotion
                    fields + the re-dated header status line;
  mechanical      : an independent fresh re-chunk pass over all 832 promoted
                    rows (quote-in-chunk under the shared norm(), chunk
                    sha256_16/heading/chars, registry membership);
  negative        : AI-attribution strings fail the attribution gate; duplicate
                    identities would fail; a worklist id is absent by construct.

Emits graph/reports/C42_R5_APPLY_CHECK.json (result ALL PASS, exit 0).
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
STORE = REPO / "graph" / QUAL / "spec_chunk_mappings.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REC_JSON = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
CHECK_JSON = REPO / "graph/reports/C42_R5_APPLY_CHECK.json"
HEADER_LINE_NEW = ("# T-C42 R5 §18 apply (2026-10-04, operator gate 3): 832 anchored "
                   "rows HUMAN_VALIDATED (839 - 3 REJECT - 4 H3 HOLD); the worklist "
                   "rows stay SUGGESTED; provenance tiers unchanged (RULE_DERIVED).\n")
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
AI_PAT = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b|llm|agent|model|bot", re.I)


def die(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def main() -> int:
    checks = []

    def ok(name, detail):
        checks.append({"check": name, "ok": True, "detail": detail})
        print(f"  PASS {name}: {detail}")

    for p in (STORE, PROMOTIONS, VERDICTS, REC_JSON):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")
    rec = json.loads(REC_JSON.read_text(encoding="utf-8"))
    if rec.get("schema") != "c42-r5-apply-record/1.0":
        die("apply record schema unexpected")

    # ---- load the real repo files -------------------------------------------
    store_text = STORE.read_text(encoding="utf-8")
    lines = store_text.splitlines(keepends=True)
    i = 0
    while i < len(lines) and lines[i].startswith("#"):
        i += 1
    header = "".join(lines[:i])
    doc = yaml.safe_load(store_text)
    rows = {r["mapping_id"]: r for r in doc["rows"]}
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    entries = promo["promotions"]
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}

    anchored = {mid: r for mid, r in rows.items()
                if r.get("chunk") and r.get("spec_code")}
    worklist = set(rows) - set(anchored)
    hv = {mid for mid, r in rows.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}

    # ---- 1. store -> record ---------------------------------------------------
    promo_ids = {e["row"]["mapping_id"] for e in entries}
    if len(promo_ids) != len(entries):
        die("duplicate identities in the promotions record")
    if hv != promo_ids:
        die(f"two-way mismatch: store HV {len(hv)} vs record {len(promo_ids)}; "
            f"only-store {sorted(hv - promo_ids)[:3]}...; only-record "
            f"{sorted(promo_ids - hv)[:3]}...")
    ok("store_to_record", f"{len(hv)} HUMAN_VALIDATED rows == promotions entries")

    # ---- 2. per-entry exact identity + attribution ----------------------------
    bad = []
    for e in entries:
        row = e["row"]
        mid = row["mapping_id"]
        srow = rows.get(mid)
        if srow is None:
            bad.append((mid, "no store row"))
            continue
        if (srow.get("spec_code") != row["spec_code"]
                or srow.get("note_path") != row["note_path"]
                or srow["chunk"]["ordinal"] != row["chunk_ordinal"]
                or srow["chunk"]["heading"] != row["heading"]
                or srow["chunk"]["sha256_16"] != row["chunk_sha256_16"]):
            bad.append((mid, "identity drift"))
        if srow.get("promotion", {}).get("promoted_by") != e["validated_by"] \
                or srow["promotion"]["promoted_date"] != e["validated_date"]:
            bad.append((mid, "attribution drift"))
        if AI_PAT.search(e["validated_by"]):
            bad.append((mid, "AI attribution"))
        if e["validated_by"] != "operator":
            bad.append((mid, "validated_by is not operator"))
    if bad:
        for mid, why in bad[:10]:
            print(f"  FAIL {mid}: {why}", file=sys.stderr)
        die(f"{len(bad)} promotion entries failed identity/attribution")
    ok("record_to_store", f"{len(entries)} entries: exact identity + operator "
                          f"attribution on both surfaces")

    # ---- 3. sampled-CONFIRM consistency with the R21 record --------------------
    sampled = {e["row"]["mapping_id"] for e in entries if "verdict" in e}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    if sampled != vconf:
        die("sampled-CONFIRM entries != the R21 CONFIRM set")
    for e in entries:
        if "verdict" in e and verdicts[e["row"]["mapping_id"]]["source"] != e["verdict_source"]:
            die(f"verdict_source drift on {e['row']['mapping_id']}")
    ok("r21_confirm_consistency", "457 sampled entries == the R21 CONFIRM set, "
                                  "sources verbatim")

    # ---- 4. exclusions ----------------------------------------------------------
    if hv & (vrej | vhold | worklist):
        die("REJECT/HOLD/worklist rows promoted — forbidden")
    sug_anch = {mid for mid, r in rows.items()
                if r.get("chunk") and r.get("spec_code")
                and r.get("validation_status") == "SUGGESTED"}
    if sug_anch != (vrej | vhold):
        die(f"SUGGESTED anchored residue != REJECT|HOLD: {len(sug_anch)}")
    if any(rows[m].get("validation_status") != "SUGGESTED" for m in worklist):
        die("a worklist row left SUGGESTED")
    if any("promotion" in rows[m] for m in (vrej | vhold | worklist)):
        die("an excluded row carries a promotion block")
    ok("exclusions", "3 REJECT + 4 H3 HOLD + 82 worklist rows stay SUGGESTED, "
                     "no promotion blocks")

    # ---- 5. census + meta + header ----------------------------------------------
    if (len(rows) != 921 or len(anchored) != 839 or len(hv) != 832
            or doc["meta"]["promoted_rows"] != 832
            or doc["meta"]["promotion_applied"] != "2026-10-04"
            or doc["meta"]["promotion_record"] != "scripts/c42_r5_promotions.yaml"
            or doc["meta"]["apply_record"] != "graph/reports/C42_R5_APPLY_RECORD.json"):
        die("post-apply census/meta drifted")
    if header.splitlines()[2] != HEADER_LINE_NEW.rstrip("\n"):
        die("header status line is not the re-dated R5 line")
    if any(r.get("provenance", {}).get("tier") != "RULE_DERIVED" for r in doc["rows"]):
        die("a provenance tier moved")
    if sha16(store_text.encode("utf-8")) != rec["round"]["store_sha256_16_post"]:
        die("post-apply store sha drifts from the apply record pin")
    ok("census_meta_header", "921 rows = 832 HV + 7 SUGGESTED anchored (REJECT|HOLD) "
                             "+ 82 worklist; meta promotion fields + re-dated header "
                             "match the record; tiers unchanged; store sha pinned")

    # ---- 6. structural re-proof vs the pinned baseline blob ---------------------
    baseline = rec["baseline"]
    try:
        pre_bytes = subprocess.run(
            ["git", "-C", str(REPO), "show", f"{baseline}:graph/igcse-maths-a/"
                                             "spec_chunk_mappings.yaml"],
            capture_output=True, check=True).stdout
    except subprocess.CalledProcessError:
        die(f"cannot read the pre-apply store blob at {baseline}")
    if sha16(pre_bytes) != rec["round"]["store_sha256_16_pre"]:
        die("pre-apply blob sha drifts from the apply record pin")
    pre_doc = yaml.safe_load(pre_bytes.decode("utf-8"))
    if len(pre_doc["rows"]) != len(doc["rows"]):
        die("row count drift vs baseline")
    mutated_unpromoted, nonval_delta = [], []
    for oe, ne in zip(pre_doc["rows"], doc["rows"]):
        mid = ne["mapping_id"]
        if mid in promo_ids:
            if {k: v for k, v in oe.items() if k != "validation_status"} != \
               {k: v for k, v in ne.items()
                if k not in ("validation_status", "promotion")}:
                nonval_delta.append(mid)
        else:
            if oe != ne:
                mutated_unpromoted.append(mid)
    om, nm = pre_doc["meta"], doc["meta"]
    if {k: v for k, v in om.items()} != {k: v for k, v in nm.items()
                                         if k not in PROMO_META_KEYS}:
        die("meta carries a non-promotion delta vs baseline")
    if set(nm) - set(om) != PROMO_META_KEYS:
        die("meta promotion-field set drifted vs baseline")
    if nonval_delta or mutated_unpromoted:
        die(f"structural re-proof FAIL: nonval_delta={nonval_delta[:3]}... "
            f"mutated_unpromoted={mutated_unpromoted[:3]}...")
    ok("structural_diff_zero", "non-validation delta vs baseline "
                               f"{baseline[:12]} is exactly zero across all 921 "
                               "rows (832 validation-only flips; 0 unpromoted "
                               "mutations; meta delta = 8 promotion fields)")

    # ---- 7. independent mechanical pass (fresh re-chunk) --------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40
    r = c40.R()
    _, notes = c40.load_corpus(r)
    by_note, _ = c40.span_chunks(notes)
    registry = c40.load_registry()
    r.close()
    failed = []
    for mid in sorted(promo_ids):
        row = rows[mid]
        chs = by_note.get(row["note_path"])
        ch = next((c for c in (chs or [])
                   if c["ordinal"] == row["chunk"]["ordinal"]), None)
        probs = []
        if ch is None:
            probs.append("ordinal missing")
        else:
            if c40.sha16(ch["text"]) != row["chunk"]["sha256_16"]:
                probs.append("sha mismatch")
            if ch["heading"] != row["chunk"]["heading"]:
                probs.append("heading mismatch")
            if c40.norm(row["evidence_quote"]) not in c40.norm(ch["text"]):
                probs.append("quote not contained")
        if row["spec_code"] not in registry:
            probs.append("code outside the 188")
        if probs:
            failed.append((mid, probs))
    if failed:
        for mid, probs in failed[:10]:
            print(f"  FAIL {mid}: {probs}", file=sys.stderr)
        die(f"mechanical pass failed for {len(failed)} row(s)")
    ok("mechanical_reverify", f"{len(promo_ids)}/{len(promo_ids)} promoted rows "
                              "quote-in-chunk + chunk-identity + registry PASS "
                              "(fresh re-chunk, independent pass)")

    # ---- 8. negative controls ------------------------------------------------------
    if AI_PAT.search("Super Z (GLM agent)") is None:
        die("attribution gate lost its teeth (negative control failed)")
    if AI_PAT.search("operator"):
        die("attribution gate false-positives on 'operator'")
    gap_sample = sorted(worklist)[:1]
    if gap_sample and gap_sample[0] in promo_ids:
        die("a worklist id appears in the promotions record")
    ok("negative_controls", "AI-attribution strings fail the gate; 'operator' "
                            "passes; worklist ids absent from the record")

    out = {
        "schema": "c42-r5-apply-check/1.0",
        "task": "T-C42",
        "stage": "r5-s18-apply-check",
        "generated_utc": subprocess.run(
            ["git", "-C", str(REPO), "log", "-1", "--format=%cI"],
            capture_output=True, text=True).stdout.strip() or None,
        "audits": {
            "store": sha16(store_text.encode("utf-8")),
            "promotions": sha16(PROMOTIONS.read_bytes()),
            "baseline": baseline,
            "baseline_store": sha16(pre_bytes),
        },
        "promoted": len(promo_ids),
        "reject_stay_suggested": sorted(vrej),
        "hold_stay_suggested": sorted(vhold),
        "worklist_stay_suggested": len(worklist),
        "checks": checks,
        "passed": len(checks),
        "total": len(checks),
        "result": "ALL PASS",
    }
    CHECK_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"c42_r5_promotion_check: {out['result']} ({len(checks)}/{len(checks)}) "
          f"-> {CHECK_JSON.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
