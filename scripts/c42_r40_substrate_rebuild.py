#!/usr/bin/env python3
"""c42_r40_substrate_rebuild.py — the T-C42 R40 gated merge point: substrate
re-build consuming the R39 operator override map AND the R39 promotions
amendment (the loop's FIFTH promotions-affecting re-application and the
SECOND exclusion-ONLY one) over the rebuilt store — the round that LANDS
the loop's SEVENTH and EIGHTH DEMOTEs (the R38 fresh REJECTs
a5b737e510606829 and d545cd5f5aeae9a9, adjudicated DEMOTE_TO_WORKLIST by
the operator-delegate at R39 — the loop's FIRST 2-row DEMOTE batch).

Fired by the operator directive "fire R39/R40" (2026-10-16, zai-web,
gateway trace 1a145a7c26a0d4e5) over the R39 record's NEXT lane (the R39
round landed the carriers and moved ZERO store bytes; this lane consumes
them); the next validation re-gate is NOT named by the directive and stays
the operator's call.

The lane is the R12/R16/R20/R24/R26/R28/R31/R34/R37 re-build precedent,
now consuming BOTH R39 carriers (the SECOND re-build under an
EXCLUSION-ONLY amended promotion surface, the THIRD consecutive with NO
tool-version move):

  R1. pre-state pins: HEAD == the round-start baseline (the R39-audit
      HEAD); the store on disk is byte-identical to the baseline blob; the
      working-tree dirt is inside the declared R40 footprint; the baseline
      store carries the R37/R38-of-record surface (917 rows, 830
      HUMAN_VALIDATED, meta.promotion_record present);
  R2. the R39 map AND amendment contracts: the map schema
      c42-r28-section-overrides/1.0 with exactly 2 verdicted
      DEMOTE_TO_WORKLIST entries (override_code null per the c40 R8 rule,
      pinned_code == current_code == the join-derived 4MA1-6.3A /
      4MA1-6.2B, mapping_ids == the R38 fresh REJECT ids) + ZERO
      REATTRIBUTEs + the retain/scoping/remarks/dated-correction blocks;
      the amendment schema c42-r31-promotions-amendment/1.0 with base_file
      == the R5 promotions path, base_file_sha256_16 == the live R5 sha,
      base_file_untouched true, exactly 0 supersedes_code + 2 excluded +
      0 added (the SECOND exclusion-ONLY record), each excluded entry ==
      the map's DEMOTE rows (ids, note_paths, ordinals, pinned_codes,
      disposition);
  R3. the promotions authority chain: the R38 regate check is still
      ALL PASS 10/10 on the R37 landing (its store sha pin == the baseline
      blob's); the R39 repair check is ALL PASS 9/9; the live promotions
      file sha256_16 equals the sha the R5 apply record pinned AND the
      amendment's base pin (the file is byte-unchanged since R5);
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.7.0 —
      STAYS; the third consecutive re-build with NO version move)
      constructs twice byte-identically, emits ALL-SUGGESTED rows, census
      917 = 832 anchored + 30 unresolved-span + 55 uncovered-SP (covered
      133 of 188 — the R39 projections landing: coverage UNCHANGED, gained
      none lost none — the DC-R24-01 compute-never-assert discipline);
  R5. the DEMOTE delta vs the baseline blob: the chunk-identity multiset is
      IDENTICAL (862 chunk rows — the W3 invariant); exactly the 2 map rows
      move — the DEMOTE batch (old: HUMAN_VALIDATED promoted at 4MA1-6.3A /
      4MA1-6.2B; new: mapping_ids recomputed to sha16("demoted|<note_path>|1")
      — the projected re-keys 09f012e4cabef0cc / 80d783fb13def4e2 verified
      live — spec_code None, no sp_title, no anchor, the round-tagged
      worklist_reason + disposition, provenance.override == the map blocks,
      SUGGESTED, no promotion block); every surviving row is BYTE-IDENTICAL
      to its baseline form (provenance.tool stays @2.7.0 — no version
      move); the non-chunk worklist rows are byte-identical (55 == 55, no
      DEFER-row vanish); the meta delta is exactly {stage, rows_anchored,
      rows_worklist_anchor_unresolved, promoted_rows} + the 4 additive
      re-dated promotion_reapplied* fields;
  R6. promotions re-application UNDER THE FIVE AMENDMENTS: the R5 file's
      832 entries resolved through the LANDED R26 amendment (its re-key
      read from the R28 record) AND the LANDED R30 amendment (its re-key
      read from the R31 record) AND the LANDED R33 amendment (its re-key
      read from the R34 record) AND the LANDED R36 exclusion (the
      a107f5041769fdd9 row skipped — its rebuilt form IS the demoted
      worklist row at 8254a7fc75ad2946, re-landed via the still-wired R36
      map) AND the fresh R39 exclusions (the 2 DEMOTE rows skipped — their
      rebuilt forms ARE the demoted worklist rows at the projected
      re-keys): 825 direct-or-chained identities (the 3 R33 supersedes
      re-keyed at the AMENDED code 1.8B -> 1.8D via the R34 record; the 5
      R30 supersedes re-keyed via the R31 record; the 3 R26 supersedes
      re-keyed via the R28 record; the R26 + R30 + R36 + R39 exclusions
      skipped) + the 3 R30-ADDED sign-off promotions re-applied
      byte-stably from the baseline blocks; every applied block == the R5
      tool shape AND the baseline store's block for the same chunk
      identity (byte-stable re-application);
      meta.promoted_rows SET 828 (830 - 2 exclusions — the surface narrows
      again);
  R7. consolidated row-set arithmetic: new_ids == old_ids - {the 2 demoted
      old ids} + {the 2 demoted new ids} (917 -> 917); final vs baseline:
      the 2 demoted rows carry exactly the enumerated landing fields with
      the round's ONLY status changes (HUMAN_VALIDATED -> SUGGESTED, both),
      every other row byte-identical (the 3 R30-added sign-off rows
      INCLUDED — their HV state + blocks restore byte-stably);
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk + sha/heading/chars); 832/832 coded rows inside the
      ratified 188;
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution in any promotion block, REJECT/hold/worklist
      categorically unpromoted, the 828 HV == the re-composed surface
      (825 + 3), the demoted rows land in the worklist RECORDED never
      forced — exactly TWO DEMOTEs this round (the loop's SEVENTH and
      EIGHTH, the first 2-row batch over promoted rows);
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R40_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r40_substrate_rebuild.py --dry-run
    python3 scripts/c42_r40_substrate_rebuild.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE = REPO / STORE_REL
MAP39 = HERE / "c42_section_overrides_r39.yaml"
AMENDMENT = HERE / "c42_r39_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R38_REGATE_CHECK.json"
REPAIR_CHECK = REPO / "graph/reports/C42_R39_REPAIR_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
R31_REC = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
R34_REC = REPO / "graph/reports/C42_R34_REBUILD_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R40_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R40_REBUILD_RECORD.md"

TOOL = "scripts/c42_r40_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "ad12bc9d92ffc6eadfa8a10dcfa07a4a69b9417a"
DIRECTIVE = ("fire R39/R40 — 2026-10-16, zai-web (gateway trace "
             "1a145a7c26a0d4e5)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
OPERATOR_ROUND = ("C42 R39 (surface 3: 2 verdicted DEMOTE_TO_WORKLIST — the "
                  "R38 fresh REJECTs adjudicated; ZERO REATTRIBUTEs, ZERO "
                  "sign-offs)")
DEMOTE_NOTE1 = ("notes/6-statistics-and-probability/probability-toolkit/"
                "basic-probability.json")
OLD_DEMOTE_ID1 = "a5b737e510606829"
NEW_DEMOTE_ID1 = "09f012e4cabef0cc"
DEMOTE_ORD1 = 1
DEMOTE_CODE1 = "4MA1-6.3A"
DEMOTE_NOTE2 = ("notes/6-statistics-and-probability/statistics-toolkit/"
                "calculations-with-the-mean.json")
OLD_DEMOTE_ID2 = "d545cd5f5aeae9a9"
NEW_DEMOTE_ID2 = "80d783fb13def4e2"
DEMOTE_ORD2 = 1
DEMOTE_CODE2 = "4MA1-6.2B"
# the LANDED R36 exclusion (read from the R37-of-record landing)
R36_NEW_DEMOTE_ID = "8254a7fc75ad2946"
R36_DEMOTE_NOTE = ("notes/1-numbers-and-the-number-system/percentages/"
                   "basic-percentages.json")
R36_DEMOTE_ORD = 4
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
# the R40 meta delta: stage + the two moving census keys + promoted_rows
# (830 -> 828, the SECOND re-application that NARROWS the surface) + the
# promotion_reapplied* fields whose VALUES move. NOTE computed honestly:
# promotion_reapplied itself is NOT in the delta BY VALUE — both R37 and
# R40 ran 2026-10-16, so the date string is byte-identical; the re-dating
# rides the by/directive/note fields (the R37 lesson applied).
WANT_META_DELTA = {"stage", "rows_anchored", "rows_worklist_anchor_unresolved",
                   "promoted_rows",
                   "promotion_reapplied_by",
                   "promotion_reapplied_directive",
                   "promotion_reapplied_note"}
REAPPLIED_META = {
    "promotion_reapplied": "2026-10-16",
    "promotion_reapplied_by": f"{TOOL}@{VERSION}",
    "promotion_reapplied_directive": DIRECTIVE,
    "promotion_reapplied_note": (
        "re-applied byte-stably over the R40 substrate re-build (the c40 "
        "tool emits all-SUGGESTED) AMENDED by "
        "scripts/c42_r39_promotions_amendment.yaml (schema "
        "c42-r31-promotions-amendment/1.0, the loop's FIFTH "
        "promotions-affecting repair record and the SECOND exclusion-ONLY: "
        "0 code supersedes + 2 exclusions + 0 additions, the R30 additions "
        "mechanism present and UNUSED, no sign-offs owed: the R30 round "
        "discharged all 4 H3 holds of record; 828 re-applied = 825 from "
        "the R5 chain [832 - 1 R26 exclusion - 3 R30 exclusions - 1 R36 "
        "exclusion - 2 R39 exclusions] + 3 R30-added sign-offs, the 3 R33 "
        "movers re-pinned within the set at 1.8D, the 2 R39 DEMOTE rows "
        "EXCLUDED — their rebuilt forms ARE the demoted unresolved-span "
        "worklist rows at the projected re-keys 09f012e4cabef0cc / "
        "80d783fb13def4e2, the R5 file byte-untouched per the P5 "
        "convention); meta.promoted_rows SET 828 (830 - 2 exclusions — the "
        "SECOND re-application that NARROWS the promoted surface); the 7 "
        "other R5 promotion meta fields byte-equal; the THIRD consecutive "
        "re-application with NO tool-version move (the c40 tool stays "
        "@2.7.0); see graph/reports/C42_R40_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R40 substrate re-build (2026-10-16, consuming the R39 operator "
    "override map: basic-probability ord 1 DEMOTE_TO_WORKLIST — the R38 "
    "fresh REJECT a5b737e510606829 adjudicated [the probability-scale "
    "surface with NO canonical target in the ratified 188] AND "
    "calculations-with-the-mean ord 1 DEMOTE_TO_WORKLIST — the R38 fresh "
    "REJECT d545cd5f5aeae9a9 adjudicated [the mean surface with NO "
    "canonical target] — the loop's FIRST 2-row DEMOTE batch, the SEVENTH "
    "and EIGHTH DEMOTEs; ZERO REATTRIBUTEs AND the R39 promotions amendment "
    "(0 code supersedes + 2 exclusions + 0 additions — the SECOND "
    "exclusion-ONLY re-application, NO tool-version move): the R5 §18 "
    "promotion surface re-applied AMENDED FIVE TIMES OVER — 828 rows "
    "HUMAN_VALIDATED (825 from the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 - "
    "2 R39 exclusions] + 3 R30-added sign-offs, the 3 R33 movers re-pinned "
    "at 1.8D, the R36 DEMOTE row excluded — it lands unresolved-span via "
    "the c40 DEMOTE convention at the projected re-key 8254a7fc75ad2946, "
    "the 2 R39 DEMOTE rows excluded — they land at 09f012e4cabef0cc / "
    "80d783fb13def4e2); 3 R22 REJECT rows stay SUGGESTED; the re-homed "
    "drawing ord 0 hold stays SUGGESTED; coverage 133/188 unchanged.\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r40_substrate_rebuild.py",
    "scripts/c42_r40_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R40_REBUILD_RECORD.json",
    "graph/reports/C42_R40_REBUILD_RECORD.md",
    "graph/reports/C42_R40_REBUILD_CHECK.json",
}

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"ok": bool(ok), "detail": detail}
    print(f"  {'PASS' if ok else 'FAIL'} {name}: {detail}")
    return ok


def die(msg: str):
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(REPO)] + list(args),
                          capture_output=True, text=True, check=True).stdout


def blob_at(commit: str, rel: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "show",
                           f"{commit}:{rel}"],
                          capture_output=True, check=True).stdout


def ident(row: dict) -> tuple:
    ch = row["chunk"]
    return (row["note_path"], ch["ordinal"], ch["heading"], ch["sha256_16"])


def strip_tool(row: dict) -> dict:
    return {k: ({**v, "tool": "-"} if k == "provenance" and isinstance(v, dict)
                else v) for k, v in row.items()}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    print("C42 R40 SUBSTRATE REBUILD — gated lane (both R39 carriers)")
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40          # amended @2.7.0
    import c42_r5_promotion_apply as r5                   # block shape + guards
    from c40_maths_a_chunk_sp_substrate import TOOL as C40_TOOL

    # graph parity PRE-census (the disk store is still the baseline state)
    pre_gc = subprocess.run(["python3", str(REPO / "scripts/graph_check.py")],
                            capture_output=True, text=True)
    pre_failures = {ln for ln in
                    (pre_gc.stdout + pre_gc.stderr).splitlines() if ln.strip()}

    # ---- R1 pre-state ---------------------------------------------------------
    head = git("rev-parse", "HEAD").strip()
    dirty = {ln[3:].strip() for ln in git("status", "--porcelain").splitlines()
             if ln.strip()}
    baseline_store_bytes = blob_at(BASELINE, STORE_REL)
    disk_ok = STORE.read_bytes() == baseline_store_bytes
    base = yaml.safe_load(baseline_store_bytes.decode("utf-8"))
    base_rows = {r["mapping_id"]: r for r in base["rows"]}
    base_anchored = {m for m, r in base_rows.items()
                     if r.get("chunk") and r.get("spec_code")}
    base_hv = {m for m, r in base_rows.items()
               if r.get("validation_status") == "HUMAN_VALIDATED"}
    r1 = (head == BASELINE and disk_ok and dirty <= EXPECTED_DIRTY
          and len(base["rows"]) == 917 and len(base_anchored) == 834
          and len(base_hv) == 830
          and base["meta"].get("promotion_record") == "scripts/c42_r5_promotions.yaml")
    if not gate("R1_pre_state", r1,
                f"HEAD {head[:12]} == baseline {BASELINE[:12]}; disk store == "
                f"baseline blob; dirty {len(dirty)} within the R40 footprint; "
                f"baseline census 917 = 834 anchored (830 HUMAN_VALIDATED) + "
                f"83 worklist (28 unresolved-span + 55 uncovered-SP); R5 "
                f"promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.7.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R39 map AND amendment contracts --------------------------------
    map_bytes = MAP39.read_bytes()
    map_sha = sha16(map_bytes)
    map_doc = yaml.safe_load(map_bytes.decode("utf-8"))
    registry = c40.load_registry()
    entries = map_doc.get("overrides") or []
    reattr = [e for e in entries if e.get("action") == "REATTRIBUTE"]
    demote = [e for e in entries if e.get("action") == "DEMOTE_TO_WORKLIST"]
    amend_bytes = AMENDMENT.read_bytes()
    amend_sha = sha16(amend_bytes)
    amend = yaml.safe_load(amend_bytes.decode("utf-8"))
    promo_sha = sha16(PROMOTIONS.read_bytes())
    sup = amend.get("supersedes_code") or []
    exc = amend.get("excluded") or []
    added = amend.get("added") or []
    exc_by_id = {e.get("mapping_id"): e for e in exc}
    demote_by_slug = {(d.get("note_slug"), d.get("chunk_ordinal")): d
                      for d in demote}
    r2 = (map_doc.get("schema") == "c42-r28-section-overrides/1.0"
          and map_doc.get("round") == "R39"
          and len(entries) == 2 and len(reattr) == 0 and len(demote) == 2
          and not map_doc.get("h3_signoffs")
          and set(map_doc.get("retain_rulings") or {}) == {"contract"}
          and len(map_doc.get("note_level_scoping") or []) == 2
          and len(map_doc.get("census_remarks") or []) == 2
          and len(map_doc.get("dated_corrections") or []) == 1
          and "note_level_adjudications" not in map_doc
          and demote_by_slug.get(("basic-probability", DEMOTE_ORD1), {})
          .get("mapping_id") == OLD_DEMOTE_ID1
          and demote_by_slug.get(("basic-probability", DEMOTE_ORD1), {})
          .get("current_code") == DEMOTE_CODE1
          and demote_by_slug.get(("calculations-with-the-mean", DEMOTE_ORD2),
                                 {}).get("mapping_id") == OLD_DEMOTE_ID2
          and demote_by_slug.get(("calculations-with-the-mean", DEMOTE_ORD2),
                                 {}).get("current_code") == DEMOTE_CODE2
          and all(d.get("provenance_class") == "verdicted"
                  and d.get("action") == "DEMOTE_TO_WORKLIST"
                  and d.get("override_code") is None for d in demote)
          and map_doc.get("promoted_surface_amendment", {}).get("supersedes") == 0
          and map_doc.get("promoted_surface_amendment", {}).get("excluded") == 2
          and map_doc.get("promoted_surface_amendment", {}).get("added") == 0
          and map_doc.get("promoted_surface_amendment", {}).get("base_file_untouched") is True
          and amend.get("schema") == "c42-r31-promotions-amendment/1.0"
          and amend.get("round") == "R39"
          and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
          and amend.get("base_file_sha256_16") == promo_sha
          and amend.get("base_file_untouched") is True
          and amend.get("prior_amendments") == \
          ["scripts/c42_r26_promotions_amendment.yaml",
           "scripts/c42_r30_promotions_amendment.yaml",
           "scripts/c42_r33_promotions_amendment.yaml",
           "scripts/c42_r36_promotions_amendment.yaml"]
          and len(sup) == 0 and len(exc) == 2 and len(added) == 0
          and exc_by_id.get(OLD_DEMOTE_ID1, {}).get("note_path") == DEMOTE_NOTE1
          and exc_by_id.get(OLD_DEMOTE_ID1, {}).get("chunk_ordinal") == DEMOTE_ORD1
          and exc_by_id.get(OLD_DEMOTE_ID1, {}).get("pinned_code") == DEMOTE_CODE1
          and exc_by_id.get(OLD_DEMOTE_ID2, {}).get("note_path") == DEMOTE_NOTE2
          and exc_by_id.get(OLD_DEMOTE_ID2, {}).get("chunk_ordinal") == DEMOTE_ORD2
          and exc_by_id.get(OLD_DEMOTE_ID2, {}).get("pinned_code") == DEMOTE_CODE2
          and all(x.get("disposition") == "DEMOTE_TO_WORKLIST"
                  for x in exc))
    if not gate("R2_map_and_amendment_contracts", r2,
                f"map schema c42-r28-section-overrides/1.0; exactly 2 "
                f"verdicted DEMOTE_TO_WORKLISTs ({OLD_DEMOTE_ID1} "
                f"basic-probability ord {DEMOTE_ORD1} at {DEMOTE_CODE1}; "
                f"{OLD_DEMOTE_ID2} calculations-with-the-mean ord "
                f"{DEMOTE_ORD2} at {DEMOTE_CODE2}; current_code == the "
                f"join-derived codes, override_code null per the c40 R8 "
                f"rule) + ZERO REATTRIBUTEs + ZERO sign-offs; the zero-"
                f"retain contract + the 2 STANDING scopings (the corpus "
                f"anchors spcpt_FVX7YRftjhnwYHQF / spcpt_n9ZtYfjh8sFCp5Kz) "
                f"+ 2 census remarks + EXACTLY 1 dated correction (the R38 "
                f"ledger-prose defect) recorded; amendment schema "
                f"c42-r31-promotions-amendment/1.0 with base sha "
                f"{amend.get('base_file_sha256_16')} == the live R5 sha, "
                f"0 supersedes + 2 excluded (ids == the map's DEMOTE rows) "
                f"+ 0 ADDED (the SECOND exclusion-ONLY record); map sha "
                f"{map_sha}, amendment sha {amend_sha}"):
        die("R2 map/amendment contracts failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check38 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    check39 = json.loads(REPAIR_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check38.get("result") == "ALL PASS" and check38.get("passed") == 10
          and check38.get("total") == 10
          and check38.get("store_sha256_16") == sha16(baseline_store_bytes)
          and check39.get("result") == "ALL PASS" and check39.get("passed") == 9
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R38 regate ALL PASS 10/10 with its store sha pin == the "
                f"baseline blob ({sha16(baseline_store_bytes)} — the R37 "
                f"landing of record, byte-identical through R38/R39); R39 "
                f"repair check ALL PASS 9/9; promotions file sha {promo_sha} "
                f"== the R5 apply record's pin AND the amendment's base pin "
                f"(byte-unchanged since R5); R21 verdict split 457 CONFIRM / "
                f"3 REJECT / 4 HOLD; R5 record promoted 832"):
        die("R3 authority chain failed")

    # ---- R4 re-build determinism + projected-census landing -----------------------
    doc_a, doc_b = c40.construct(), c40.construct()
    dump_a = yaml.safe_dump(doc_a, allow_unicode=True, sort_keys=False, width=100)
    dump_b = yaml.safe_dump(doc_b, allow_unicode=True, sort_keys=False, width=100)
    rows_new = doc_a["rows"]
    meta_new = doc_a["meta"]
    n_anchored = sum(1 for r in rows_new if r.get("spec_code") and "chunk" in r)
    n_span = sum(1 for r in rows_new if r.get("worklist_reason")
                 and "chunk" in r)
    n_unmapped = sum(1 for r in rows_new if r.get("worklist_reason")
                     and "chunk" not in r)
    covered = {r["spec_code"] for r in rows_new
               if r.get("spec_code") and "chunk" in r}
    ids_new = [r["mapping_id"] for r in rows_new]
    base_covered = {r["spec_code"] for r in base["rows"]
                    if r.get("spec_code") and "chunk" in r}
    gained = sorted(covered - base_covered)
    lost = sorted(base_covered - covered)
    r4 = (dump_a == dump_b
          and all(r.get("validation_status") == "SUGGESTED" for r in rows_new)
          and len(rows_new) == 917 and n_anchored == 832 and n_span == 30
          and n_unmapped == 55 and len(covered) == 133
          and len(ids_new) == len(set(ids_new))
          and "4MA1-6.3A" in covered and "4MA1-6.2B" in covered
          and "4MA1-1.6F" in covered and "4MA1-2.7C" in covered
          and "4MA1-1.8D" in covered and "4MA1-1.8B" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 917 = 832 anchored + 30 unresolved-span + 55 "
                f"uncovered-SP; covered 133 of 188 (the R39 projections "
                f"landing: coverage UNCHANGED — 6.3A keeps 17 anchored rows, "
                f"6.2B keeps 23; computed, never asserted — the DC-R24-01 "
                f"discipline); mapping_ids unique"):
        die("R4 rebuild failed")
    if gained or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 the DEMOTE delta vs the baseline blob ------------------------------
    DEMOTES = [(("basic-probability", DEMOTE_ORD1), DEMOTE_NOTE1,
                OLD_DEMOTE_ID1, NEW_DEMOTE_ID1, DEMOTE_CODE1),
               (("calculations-with-the-mean", DEMOTE_ORD2), DEMOTE_NOTE2,
                OLD_DEMOTE_ID2, NEW_DEMOTE_ID2, DEMOTE_CODE2)]
    old_chunk = {ident(r): r for r in base["rows"] if "chunk" in r}
    new_chunk = {ident(r): r for r in rows_new if "chunk" in r}
    r5_ok = (set(old_chunk) == set(new_chunk) and len(old_chunk) == 862
             and len(set(old_chunk)) == 862)
    moved, demote_pairs, drift = [], [], []
    if r5_ok:
        for k, orow in old_chunk.items():
            nrow = new_chunk[k]
            slug = orow.get("note_slug")
            entry = next((e for e in entries
                          if e["note_slug"] == slug
                          and e["chunk_ordinal"] == orow["chunk"]["ordinal"]), None)
            if entry and entry.get("action") == "DEMOTE_TO_WORKLIST":
                moved.append(k)
                want_block = {
                    "source": f"scripts/c42_section_overrides_r39.yaml@{map_sha}",
                    "operator_round": OPERATOR_ROUND,
                    "action": "DEMOTE_TO_WORKLIST",
                    "evidence": entry["evidence"],
                }
                want_mid = sha16(f"demoted|{orow['note_path']}|"
                                 f"{orow['chunk']['ordinal']}")
                want_reason = (
                    f"DEMOTE_TO_WORKLIST per the {OPERATOR_ROUND} operator "
                    "verdict round (provenance.override): no canonical 188 row "
                    "teaches this section's content and a REATTRIBUTE has no "
                    "target — recorded, never forced")
                want_disp = (
                    "WORKLIST — chunk-level mapping waits on fresh notes "
                    "coverage or a new operator anchor; recorded, not "
                    "forced (C42 R39 surface 3 demote)")
                ok_row = (
                    orow.get("validation_status") == "HUMAN_VALIDATED"
                    and "promotion" in orow
                    and nrow.get("spec_code") is None
                    and "sp_title" not in nrow
                    and "anchor" not in nrow
                    and nrow["mapping_id"] == want_mid
                    and nrow.get("worklist_reason") == want_reason
                    and nrow.get("disposition") == want_disp
                    and nrow.get("provenance", {}).get("override") == want_block
                    and nrow.get("validation_status") == "SUGGESTED"
                    and "promotion" not in nrow
                    and nrow["evidence_quote"] == orow["evidence_quote"]
                    and nrow["rationale"] == orow["rationale"])
                if not ok_row:
                    drift.append(f"demote row {k}")
                demote_pairs.append((orow["mapping_id"], nrow["mapping_id"]))
                continue
            if entry:  # a REATTRIBUTE — none this round; any hit is a defect
                drift.append(f"unexpected REATTRIBUTE entry {k}")
                continue
            # NO map entry: the surviving rows legitimately differ in
            # validation_status + promotion (restored at R6); the R5-stage
            # zero-drift claim strips those two fields plus tool
            def _strip_stage(row):
                row = strip_tool(row)
                row.pop("validation_status", None)
                row.pop("promotion", None)
                return row

            to_ = (so := orow).get("provenance") or {}
            tn = (sn := nrow).get("provenance") or {}
            if _strip_stage(so) != _strip_stage(sn) or \
                    to_.get("tool") != TOOL_OLD or tn.get("tool") != TOOL_NEW:
                drift.append(f"tool/zero-drift {k}")
        # non-chunk rows (the uncovered-SP worklist): byte-identical this
        # round — NO DEFER-row vanish
        old_nc = [r for r in base["rows"] if "chunk" not in r]
        new_nc = [r for r in rows_new if "chunk" not in r]
        if not (len(old_nc) == 55 and len(new_nc) == 55
                and {r["mapping_id"] for r in old_nc} ==
                {r["mapping_id"] for r in new_nc}):
            drift.append("non-chunk set shape")
        else:
            new_by_id = {r["mapping_id"]: r for r in new_nc}
            for orow in old_nc:
                nrow = new_by_id[orow["mapping_id"]]
                if orow != nrow:
                    drift.append(f"nonchunk {orow['mapping_id']}")
    want_pairs = [(OLD_DEMOTE_ID1, NEW_DEMOTE_ID1),
                  (OLD_DEMOTE_ID2, NEW_DEMOTE_ID2)]
    r5_pass = (r5_ok and len(moved) == 2 and len(demote_pairs) == 2
               and not drift
               and sorted(demote_pairs) == sorted(want_pairs))
    if not gate("R5_demote_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows — the W3 "
                f"invariant); exactly 2 rows move — the DEMOTE batch (the "
                f"loop's SEVENTH and EIGHTH DEMOTEs, the FIRST 2-row batch "
                f"over promoted rows): {OLD_DEMOTE_ID1} (HUMAN_VALIDATED "
                f"promoted at {DEMOTE_CODE1}) -> {NEW_DEMOTE_ID1} and "
                f"{OLD_DEMOTE_ID2} (promoted at {DEMOTE_CODE2}) -> "
                f"{NEW_DEMOTE_ID2} (the projected re-keys "
                f"sha16('demoted|<note_path>|1') verified live); "
                f"spec_code -> None, no sp_title, no anchor; the "
                f"round-tagged worklist_reason + disposition parse under "
                f"the 'C42 R39 (surface 3:' operator-round descriptor; "
                f"provenance.override == the map blocks (map sha {map_sha}); "
                f"evidence quote + rationale byte-carried; SUGGESTED with NO "
                f"promotion block; every surviving row BYTE-IDENTICAL to its "
                f"baseline form (provenance.tool stays @2.7.0 — the third "
                f"re-build with NO tool churn); the 55 non-chunk worklist "
                f"rows byte-identical (no DEFER-row vanish)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application UNDER THE FIVE AMENDMENTS ----------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    rec28 = json.loads(R28_REC.read_text(encoding="utf-8"))
    r26_rekey = dict(rec28["promotions"]["superseded_ids_rekeyed"])
    rec31 = json.loads(R31_REC.read_text(encoding="utf-8"))
    r30_rekey = dict(rec31["promotions"]["superseded_ids_rekeyed"])
    rec34 = json.loads(R34_REC.read_text(encoding="utf-8"))
    r33_rekey = dict(rec34["promotions"]["superseded_ids_rekeyed"])
    added_ids = set(rec31["promotions"]["added_ids"])
    r26_amend = yaml.safe_load((HERE / "c42_r26_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r26_sup = {e["mapping_id"]: e for e in r26_amend.get("supersedes_code") or []}
    r26_exc = {e["mapping_id"] for e in r26_amend.get("excluded") or []}
    r30_amend = yaml.safe_load((HERE / "c42_r30_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r30_sup = {e["mapping_id"]: e for e in r30_amend.get("supersedes_code") or []}
    r30_exc = {e["mapping_id"] for e in r30_amend.get("excluded") or []}
    r33_amend = yaml.safe_load((HERE / "c42_r33_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r33_sup = {e["mapping_id"]: e for e in r33_amend.get("supersedes_code") or []}
    r36_amend = yaml.safe_load((HERE / "c42_r36_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r36_exc = {e["mapping_id"] for e in r36_amend.get("excluded") or []}
    r39_exc = {e["mapping_id"] for e in exc}          # the fresh R39 exclusions
    # amendment pre-apply integrity: pinned_code verified against the R5 file
    # BEFORE the amendment applies — any drift fails the rebuild
    pentry_by_id = {}
    seen = set()
    problems = []
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        if not mid or mid in seen:
            problems.append(f"promotion[{n}] identity")
            continue
        seen.add(mid)
        pentry_by_id[mid] = e
    for eid, e in r33_sup.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R33 amendment supersedes {eid} drift vs the R5 file")
    for eid, e in r30_sup.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R30 amendment supersedes {eid} drift vs the R5 file")
    for eid in r30_exc:
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("note_path") is None
                or int(pe.get("chunk_ordinal", -1)) < 0):
            problems.append(f"R30 amendment excluded {eid} drift vs the R5 file")
    for eid, e in r26_sup.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R26 amendment supersedes {eid} drift vs the R5 file")
    for eid, e in {x["mapping_id"]: x for x in r36_amend.get("excluded") or []}.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R36 amendment excluded {eid} drift vs the R5 file")
    for eid, e in exc_by_id.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R39 amendment excluded {eid} drift vs the R5 file")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"amendment pre-apply problems: {problems[:4]}")
        die("R6 amendment pre-apply integrity failed")
    # resolve every R5 entry against the rebuilt rows through ALL FIVE
    # amendments (R39 exclusion -> R36 exclusion [LANDED] -> R33 newest ->
    # R30 -> R26 -> direct)
    resolved = {}
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        if (mid in r26_exc or mid in r30_exc or mid in r36_exc
                or mid in r39_exc):
            continue
        if mid in r33_sup:
            target_id = r33_rekey.get(mid)
            want_code = r33_sup[mid].get("amended_code")
            if target_id is None:
                problems.append(f"{where} no R33 old->new translation")
                continue
        elif mid in r30_sup:
            target_id = r30_rekey.get(mid)
            want_code = r30_sup[mid].get("amended_code")
            if target_id is None:
                problems.append(f"{where} no R30 old->new translation")
                continue
        elif mid in r26_sup:
            target_id = r26_rekey.get(mid)
            want_code = r26_sup[mid].get("amended_code")
            if target_id is None:
                problems.append(f"{where} no R26 old->new translation")
                continue
        else:
            target_id = mid
            want_code = row.get("spec_code")
        target = new_rows.get(target_id)
        if target is None:
            problems.append(f"{where} no rebuilt row")
            continue
        if (target.get("spec_code") != want_code
                or target.get("note_path") != row.get("note_path")
                or target["chunk"]["ordinal"] != row.get("chunk_ordinal")
                or target["chunk"]["heading"] != row.get("heading")
                or target["chunk"]["sha256_16"] != row.get("chunk_sha256_16")):
            problems.append(f"{where} identity drift")
        if "verdict" in e:
            n_sampled += 1
            if e["verdict"] != "CONFIRM" or mid not in vconf:
                problems.append(f"{where} sampled verdict")
        resolved[target_id] = (mid, want_code)
    # the excluded rows' rebuilt forms ARE the demoted worklist rows:
    # the R26 + R30 exclusions via chunk identity (the R37 convention);
    # the LANDED R36 exclusion at its re-key 8254a7fc75ad2946; the fresh
    # R39 exclusions at their projected re-keys
    by_ident_new = {(r["note_path"], r["chunk"]["ordinal"],
                     r["chunk"]["heading"], r["chunk"]["sha256_16"]): r
                    for r in rows_new if "chunk" in r}
    for eid in r26_exc | r30_exc:
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        trow = by_ident_new.get((pe.get("note_path"), pe.get("chunk_ordinal"),
                                 pe.get("heading"), pe.get("chunk_sha256_16")))
        if trow is None or trow.get("worklist_reason") is None \
                or trow.get("validation_status") != "SUGGESTED" \
                or "promotion" in trow:
            problems.append(f"the excluded row {eid} is not the demoted "
                            f"unresolved-span worklist row")
    trow36 = new_rows.get(R36_NEW_DEMOTE_ID)
    if trow36 is None or trow36.get("worklist_reason") is None \
            or trow36.get("validation_status") != "SUGGESTED" \
            or "promotion" in trow36 \
            or trow36.get("note_path") != R36_DEMOTE_NOTE \
            or trow36["chunk"]["ordinal"] != R36_DEMOTE_ORD:
        problems.append(f"the LANDED R36 excluded row is not the demoted "
                        f"unresolved-span worklist row at {R36_NEW_DEMOTE_ID}")
    for eid, new_id, note, ordn in (
            (OLD_DEMOTE_ID1, NEW_DEMOTE_ID1, DEMOTE_NOTE1, DEMOTE_ORD1),
            (OLD_DEMOTE_ID2, NEW_DEMOTE_ID2, DEMOTE_NOTE2, DEMOTE_ORD2)):
        trow = new_rows.get(new_id)
        if trow is None or trow.get("worklist_reason") is None \
                or trow.get("validation_status") != "SUGGESTED" \
                or "promotion" in trow \
                or trow.get("note_path") != note \
                or trow["chunk"]["ordinal"] != ordn:
            problems.append(f"the R39 excluded row {eid} is not the demoted "
                            f"unresolved-span worklist row at {new_id}")
    # the 3 R31-ADDED sign-off rows: verified against the LIVE rebuilt rows
    for mid in added_ids:
        brow = base_rows.get(mid)
        target = new_rows.get(mid)
        if brow is None or target is None:
            problems.append(f"added {mid} missing")
            continue
        if (target.get("spec_code") != brow.get("spec_code")
                or ident(target) != ident(brow)):
            problems.append(f"added {mid} identity drift")
    # surface arithmetic
    new_rows_by_ident = {ident(r): r for r in rows_new if "chunk" in r}
    keyed_new = {(rw.get("note_slug"),
                  (rw.get("chunk") or {}).get("ordinal")): rw
                 for rw in rows_new if "chunk" in rw}
    keyed_base = {(rw.get("note_slug"),
                   (rw.get("chunk") or {}).get("ordinal")): rw
                  for rw in base["rows"] if "chunk" in rw}
    vrej_new, vrej_old_check = set(), set()
    ov22 = yaml.safe_load((HERE / "c42_section_overrides_r22.yaml")
                          .read_text(encoding="utf-8"))
    for e22 in (ov22.get("overrides") or []):
        k22 = (e22.get("note_slug"), int(e22.get("chunk_ordinal")))
        nrow22 = keyed_new.get(k22)
        brow22 = keyed_base.get(k22)
        if nrow22 is None or brow22 is None:
            problems.append(f"R22 row missing {k22}")
            continue
        vrej_new.add(nrow22["mapping_id"])
        if brow22["spec_code"] != e22["override_code"] or \
                nrow22["spec_code"] != e22["override_code"]:
            problems.append(f"R22 row code drift {k22}")
        vrej_old_check.add(sha16(f"{nrow22['note_path']}|"
                                 f"{e22['current_code']}|"
                                 f"{c40.norm(nrow22['evidence_quote'])}"))
    if vrej_old_check != vrej:
        problems.append("the R22 rows' pre-R22 ids != the R21 REJECT set")
    # the R21-era HOLD set: 3 promoted via the R30 additions (ids stable), 1
    # re-keyed by the R30 map (read through the R31 record's re-key)
    vhold_promoted, vhold_rekeyed = set(), set()
    for mid in vhold:
        brow = base_rows[r30_rekey.get(mid, mid)]
        nrow = new_rows_by_ident[ident(brow)]
        if mid in added_ids:
            vhold_promoted.add(nrow["mapping_id"])
            if nrow["mapping_id"] != mid:
                problems.append(f"sign-off row re-keyed unexpectedly {mid}")
        else:
            vhold_rekeyed.add(nrow["mapping_id"])
    if vhold_promoted != added_ids:
        problems.append("the promoted hold set != the 3 R30-added sign-offs")
    if len(vhold_rekeyed) != 1:
        problems.append("the re-keyed hold set != the 1 re-homed 3.3F row")
    vhold_remaining = vhold_rekeyed
    anchored_new = {r["mapping_id"] for r in rows_new
                    if r.get("spec_code") and "chunk" in r}
    promote_set = anchored_new - vrej_new - vhold_remaining
    worklist_new = {r["mapping_id"] for r in rows_new
                    if r.get("worklist_reason")}
    if (len(resolved) != 825 or len(resolved) + len(added_ids) != 828
            or resolved.keys() | added_ids != promote_set
            or n_sampled != 457
            or promote_set & (vrej_new | vhold_remaining | worklist_new)):
        problems.append(f"round contract: resolved {len(resolved)} + added "
                        f"{len(added_ids)} vs surface {len(promote_set)}; "
                        f"sampled {n_sampled}")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"problems: {problems[:4]}")
        die("R6 promotions re-application failed")
    # flip + byte-stable blocks
    final_doc = yaml.safe_load(dump_a)  # fresh parse; rows are fresh dicts
    base_by_ident = {ident(r): r for r in base["rows"] if "chunk" in r}
    flipped = 0
    for row in final_doc["rows"]:
        mid = row["mapping_id"]
        if mid not in promote_set:
            continue
        if "promotion" in row or row.get("validation_status") != "SUGGESTED":
            die(f"row {mid} pre-poisoned — refusing")
        # the baseline block is looked up by CHUNK identity — every promoted
        # row (the 825 chain + the 3 R30-added sign-offs) carries one there
        base_block = base_by_ident[ident(row)].get("promotion")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if base_block is None or block != base_block:
            die(f"promotion block drift vs the baseline surface on {mid}")
        row["promotion"] = block
        flipped += 1
    if flipped != 828:
        die(f"flipped {flipped} != 828")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    meta_f["promoted_rows"] = 828            # SET — the narrowed surface
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"the amendment pre-apply integrity verified (pinned_code == the R5 "
         f"file on every supersedes entry of the LANDED amendments — R33 3 + "
         f"R30 5 + R26 3 — and the excluded entries' identities drift-free "
         f"vs the R5 file — R36 1 + R39 2 — any drift fails); 832 R5 entries "
         f"resolved through the LANDED R26 amendment (its re-key read from "
         f"the R28 record), the LANDED R30 amendment (its re-key read from "
         f"the R31 record), the LANDED R33 amendment (its re-key read from "
         f"the R34 record), the LANDED R36 exclusion (the demoted row's "
         f"rebuilt form verified at the re-key {R36_NEW_DEMOTE_ID}) and the "
         f"fresh R39 exclusions: 825 direct-or-chained identities (the 3 "
         f"R33 supersedes re-keyed at the AMENDED code 1.8B->1.8D — ords "
         f"6/7/8 of rounding-and-estimation REMAIN promoted; the 5 R30 "
         f"supersedes via the R31 record; the 3 R26 supersedes via the R28 "
         f"record; the R26 exclusion + the 3 R30 exclusions + THE R36 "
         f"EXCLUSION + THE 2 R39 EXCLUSIONS skipped — their rebuilt forms "
         f"ARE the demoted worklist rows) + the 3 R31-ADDED sign-off "
         f"promotions re-applied byte-stably from the baseline blocks; "
         f"validated_by operator everywhere; sampled 457 == the R21 CONFIRM "
         f"set; surface == anchored 832 - R22 REJECT 3 - the re-homed hold "
         f"1 == 828 both directions (825 + 3); every applied block == the "
         f"R5 tool shape AND the baseline store's block for the same chunk "
         f"identity (byte-stable re-application); meta promotion fields "
         f"restored byte-equal EXCEPT promoted_rows SET 828 (830 - 2 "
         f"exclusions — the SECOND re-application that NARROWS the surface) "
         f"+ 4 additive re-dated promotion_reapplied* fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = (old_ids - {OLD_DEMOTE_ID1, OLD_DEMOTE_ID2}) | \
               {NEW_DEMOTE_ID1, NEW_DEMOTE_ID2}
    r7 = new_ids == want_new and len(new_ids) == 917
    fin_chunk = {ident(r): r for r in final_doc["rows"] if "chunk" in r}
    moved_idents = set(moved)
    cons_drift, status_changes = [], []
    demote_keys = moved_idents.copy()
    for k, brow in old_chunk.items():
        frow = fin_chunk[k]
        if frow.get("validation_status") != brow.get("validation_status"):
            status_changes.append(k)
        if k in moved_idents:
            continue
        if strip_tool(brow) != strip_tool(frow):
            cons_drift.append(f"non-tool delta {k}")
        elif brow["provenance"]["tool"] != TOOL_OLD or \
                frow["provenance"]["tool"] != TOOL_NEW:
            cons_drift.append(f"tool swap {k}")
    fin_nc = {r["mapping_id"]: r for r in final_doc["rows"]
              if "chunk" not in r}
    for brow in base["rows"]:
        if "chunk" in brow:
            continue
        frow = fin_nc.get(brow["mapping_id"])
        if frow is None:
            continue
        if strip_tool(brow) != strip_tool(frow) or \
                brow["provenance"]["tool"] != TOOL_OLD or \
                frow["provenance"]["tool"] != TOOL_NEW:
            cons_drift.append(f"nonchunk {brow['mapping_id']}")
    # the meta delta: exactly {stage, the two moving census keys,
    # promoted_rows} + the 4 additive re-dated promotion_reapplied* fields
    meta_delta = {k for k in set(meta_f) & set(base["meta"])
                  if meta_f[k] != base["meta"][k]}
    r7 = (r7 and not cons_drift and set(meta_f) == set(base["meta"])
          and meta_delta == WANT_META_DELTA
          and len(status_changes) == 2
          and set(status_changes) == demote_keys
          and meta_f["promoted_rows"] == 828
          and base["meta"]["promoted_rows"] == 830)
    if not gate("R7_row_set_arithmetic", r7,
                f"new_ids == old_ids - the 2 demoted old ids + the 2 demoted "
                f"new ids (917 -> 917) exactly; consolidated final-vs-"
                f"baseline equality: EXACTLY TWO status changes — the "
                f"demoted rows (HUMAN_VALIDATED -> SUGGESTED, the round's "
                f"only ones), every non-moved row byte-identical "
                f"(provenance.tool stays @2.7.0, the 3 R30-added sign-off "
                f"rows restore byte-stably), the meta delta == exactly "
                f"stage + rows_anchored + rows_worklist_anchor_unresolved + "
                f"promoted_rows (830 -> 828 — the narrowed surface) + the "
                f"promotion_reapplied_by/directive/note fields (the "
                f"promotion_reapplied date value itself coincides — both "
                f"rounds ran 2026-10-16 — so the re-dating rides the other "
                f"three fields)"
                + (f"; DRIFT {cons_drift[:3]}" if cons_drift else "")):
        die("R7 row-set arithmetic failed")

    # ---- R8 G4-at-apply fresh re-chunk --------------------------------------------------
    r = c40.R()
    _, notes = c40.load_corpus(r)
    by_note, _ = c40.span_chunks(notes)
    r.close()
    failed = []
    n_coded = 0
    for row in final_doc["rows"]:
        if "chunk" not in row:
            continue
        chs = by_note.get(row["note_path"]) or []
        ch = next((c for c in chs
                   if c["ordinal"] == row["chunk"]["ordinal"]), None)
        probs = []
        if ch is None:
            probs.append("ordinal missing")
        else:
            if c40.sha16(ch["text"]) != row["chunk"]["sha256_16"]:
                probs.append("sha")
            if ch["heading"] != row["chunk"]["heading"]:
                probs.append("heading")
            if len(ch["text"]) != row["chunk"]["chars"]:
                probs.append("chars")
            if c40.norm(row["evidence_quote"]) not in c40.norm(ch["text"]):
                probs.append("quote")
        if row.get("spec_code"):
            n_coded += 1
            if row["spec_code"] not in registry:
                probs.append("code")
        if probs:
            failed.append((row["mapping_id"], probs))
    r8 = not failed and n_coded == 832
    if not gate("R8_g4_at_apply", r8,
                f"all {sum(1 for x in final_doc['rows'] if 'chunk' in x)} chunk "
                f"rows re-verified against a fresh re-chunking (quote-in-chunk "
                f"+ sha/heading/chars); {n_coded}/832 coded rows inside the "
                f"ratified 188" + (f"; FAIL {failed[:3]}" if failed else "")):
        die("R8 G4-at-apply failed")

    # ---- R9 anti-forgery sweep ------------------------------------------------------------
    hv = [x for x in final_doc["rows"]
          if x.get("validation_status") == "HUMAN_VALIDATED"]
    sug_anch = {x["mapping_id"] for x in final_doc["rows"]
                if x.get("chunk") and x.get("spec_code")
                and x.get("validation_status") == "SUGGESTED"}
    demoted_ids = {n for _, n in demote_pairs}
    tiers_ok = all(x.get("provenance", {}).get("tier") == "RULE_DERIVED"
                   for x in final_doc["rows"])
    attribution_ok = all(
        x["promotion"]["promoted_by"] == "operator"
        and not r5.AI_PAT.search(json.dumps(x["promotion"]))
        for x in hv)
    dem_rows = [x for x in final_doc["rows"] if x["mapping_id"] in demoted_ids]
    r9 = (len(hv) == 828 and {x["mapping_id"] for x in hv} == promote_set
          and sug_anch == vrej_new | vhold_remaining
          and tiers_ok and attribution_ok
          and not (demoted_ids & {x["mapping_id"] for x in hv})
          and len(dem_rows) == 2
          and all(x.get("worklist_reason") and "promotion" not in x
                  and x.get("validation_status") == "SUGGESTED"
                  for x in dem_rows)
          and not (promote_set & (worklist_new | vhold_remaining | vrej_new)))
    if not gate("R9_anti_forgery", r9,
                f"828 HUMAN_VALIDATED == the re-composed promotion set "
                f"(825 from the R5 chain + 3 R30-added sign-offs, the 3 R33 "
                f"movers re-pinned within it); the SUGGESTED anchored "
                f"residue == the 3 R22 re-attributed REJECTs + the 1 "
                f"re-homed hold; EXACTLY TWO DEMOTEs this round — the "
                f"loop's SEVENTH and EIGHTH, the FIRST 2-row batch, landing "
                f"unresolved-span RECORDED never forced (the worklist's "
                f"demote-landed class deepens 8 -> 10); provenance tiers "
                f"RULE_DERIVED everywhere; operator attribution clean; "
                f"REJECT/hold/worklist categorically unpromoted"):
        die("R9 anti-forgery failed")

    # ---- compose + parity + write ----------------------------------------------------------
    header = ("# SyllabAI 4MA1 chunk→SP mapping substrate — T-C40 K2 Lane B, "
              "graph-as-code (C31 §6, C13 pattern)\n"
              "# Generated by scripts/c40_maths_a_chunk_sp_substrate.py — DO "
              "NOT hand-edit: re-run the script.\n" + HEADER_LINE_REBUILD)
    new_text = header + "\n" + yaml.safe_dump(
        final_doc, allow_unicode=True, sort_keys=False, width=100)
    out_doc = yaml.safe_load(new_text)
    if yaml.safe_dump(out_doc, allow_unicode=True, sort_keys=False, width=100) \
            != yaml.safe_dump(final_doc, allow_unicode=True, sort_keys=False,
                              width=100):
        die("round-trip unstable")

    if args.dry_run:
        print(f"c42_r40_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 917 rows (828 HUMAN_VALIDATED re-applied "
              f"AMENDED FIVE TIMES OVER: 825 + 3 R30-added sign-offs, the 3 "
              f"R33 movers re-pinned at 1.8D; 2 DEMOTEs landing "
              f"{OLD_DEMOTE_ID1} -> {NEW_DEMOTE_ID1} and {OLD_DEMOTE_ID2} -> "
              f"{NEW_DEMOTE_ID2} + 0 REATTRIBUTEs; coverage 133/188 "
              f"unchanged); no files written")
        return 0

    STORE.write_text(new_text, encoding="utf-8")

    # graph parity POST (requires the rebuilt store on disk)
    post_gc = subprocess.run(["python3", str(REPO / "scripts/graph_check.py")],
                             capture_output=True, text=True)
    post_failures = {ln for ln in
                     (post_gc.stdout + post_gc.stderr).splitlines() if ln.strip()}
    kg = subprocess.run(
        ["python3", str(REPO / "scripts/kg_export.py"), "--verify-golden"],
        capture_output=True, text=True)
    r10 = (pre_failures == post_failures and kg.returncode == 0)
    gate("R10_ci_parity", r10,
         f"graph_check failure census IDENTICAL pre vs post "
         f"({len(pre_failures)} lines — the pre-existing sparse-checkout "
         f"environmental set, zero delta from this lane); kg_export "
         f"--verify-golden exit {kg.returncode} (golden gate GREEN)"
         + ("" if kg.returncode == 0 else f"; kg tail: {kg.stdout[-200:]}"))
    if not r10:
        STORE.write_text(baseline_store_bytes.decode("utf-8"),
                         encoding="utf-8")
        die("R10 parity failed — store restored to the baseline bytes")

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    demote_landings = [
        {"note_slug": "basic-probability",
         "chunk_ordinal": DEMOTE_ORD1,
         "mapping_id_old": OLD_DEMOTE_ID1, "mapping_id_new": NEW_DEMOTE_ID1,
         "from_code": DEMOTE_CODE1, "to_code": None,
         "disposition": "DEMOTE_TO_WORKLIST",
         "landing": "unresolved-span via the c40 DEMOTE convention "
                    "(round-tagged worklist_reason + disposition; chunk "
                    "identity intact — the W3 invariant; RECORDED never "
                    "forced)",
         "round_tag": OPERATOR_ROUND},
        {"note_slug": "calculations-with-the-mean",
         "chunk_ordinal": DEMOTE_ORD2,
         "mapping_id_old": OLD_DEMOTE_ID2, "mapping_id_new": NEW_DEMOTE_ID2,
         "from_code": DEMOTE_CODE2, "to_code": None,
         "disposition": "DEMOTE_TO_WORKLIST",
         "landing": "unresolved-span via the c40 DEMOTE convention "
                    "(round-tagged worklist_reason + disposition; chunk "
                    "identity intact — the W3 invariant; RECORDED never "
                    "forced)",
         "round_tag": OPERATOR_ROUND},
    ]
    rec = {
        "schema": "c42-r40-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r40-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R39 record's NEXT lane, fired by the directive: the "
                 "substrate re-build consuming the R39 override map (schema "
                 "c42-r28-section-overrides/1.0) AND the R39 promotions "
                 "amendment (schema c42-r31-promotions-amendment/1.0, the "
                 "SECOND exclusion-ONLY); the next validation re-gate NOT "
                 "named by the directive — the operator's call"),
        "rebuild": {
            "tool": f"{TOOL_OLD.split('@')[0]}@2.7.0",
            "tool_version_move": "NONE — TOOL_VERSION stays 2.7.0 (the third "
                                 "consecutive re-build with no version move; "
                                 "provenance.tool byte-stable on every row)",
            "join": "the R27-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged; the FOUR R26 STANDING pins verified "
                    "in-generator; the basic-probability corpus anchor "
                    "spcpt_FVX7YRftjhnwYHQF STANDS at 6.3A and the "
                    "calculations-with-the-mean corpus anchor "
                    "spcpt_n9ZtYfjh8sFCp5Kz STANDS at 6.2B — the R39 "
                    "scoping rides the store rows, the join layer untouched)",
            "override_maps_consumed": ("ELEVEN: R1 + R6 (with the subsumption "
                                       "registry) + R10 + R14 + R18 + R22 + "
                                       "R26 + R30 + R33 + R36 + R39, all "
                                       "fail-closed"),
            "rows_pre": 917, "rows_post": 917,
            "anchored": 832, "unresolved_span": 30, "uncovered_sp": 55,
            "covered_pre": 133, "covered_post": 133,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r39.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "reattribute": len(reattr), "demote": len(demote),
            "landings": [],
            "demote_landings": demote_landings,
            "standing_pins": ("the FOUR R26 STANDING joins verified "
                              "in-generator (unchanged); the R39 STANDING "
                              "scoping rides the map's note_level_scoping "
                              "blocks — the basic-probability corpus anchor "
                              "spcpt_FVX7YRftjhnwYHQF STANDS at 6.3A (the "
                              "note keeps ords 0/2/3/4/5) and the "
                              "calculations-with-the-mean corpus anchor "
                              "spcpt_n9ZtYfjh8sFCp5Kz STANDS at 6.2B (the "
                              "note keeps ord 0); NO new c40-pinned "
                              "adjudications this round"),
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "amendment": {
                "path": "scripts/c42_r39_promotions_amendment.yaml",
                "sha256_16": amend_sha,
                "schema": "c42-r31-promotions-amendment/1.0",
                "supersedes": len(sup), "excluded": len(exc),
                "added": len(added),
                "pre_apply_integrity": "pinned_code verified against the R5 "
                                       "file BEFORE the amendment applies "
                                       "(all FIVE amendments: R39 excluded + "
                                       "R36 excluded [LANDED] + R33 + R30 + "
                                       "R26)",
                "re_applied": 828,
                "re_applied_composition": "825 from the R5 chain [832 - 1 "
                                          "R26 - 3 R30 - 1 R36 - 2 R39 "
                                          "exclusions] + 3 R30-added "
                                          "sign-offs, the 3 R33 movers "
                                          "re-pinned within the set",
                "meta_promoted_rows_restated": "828 (830 - 2 exclusions — the "
                                               "SECOND re-application that "
                                               "NARROWS the promoted surface; "
                                               "the 7 other R5 promotion meta "
                                               "fields byte-equal)",
            },
            "reapplication": ("byte-stable: every applied block for all 828 "
                              "== the R5 tool's block shape AND the baseline "
                              "store's block for the same chunk identity "
                              "(the R30-added sign-offs INCLUDED — their "
                              "baseline blocks restore byte-stably); the 3 "
                              "superseded rows REMAIN in the promoted set at "
                              "their amended codes (re-keyed old->new, the "
                              "R24 id_pairs convention); the R26 + R30 + "
                              "R36 + R39 excluded rows stay unpromoted "
                              "worklist rows (the R36 one re-lands via the "
                              "still-wired R36 map at 8254a7fc75ad2946; the "
                              "R39 pair via the fresh map at the projected "
                              "re-keys); meta gains ONLY the additive "
                              "re-dated promotion_reapplied* fields + the "
                              "narrowed promoted_rows"),
            "superseded_ids_rekeyed": {},
            "excluded_ids": [OLD_DEMOTE_ID1, OLD_DEMOTE_ID2],
            "added_ids": [],
            "r33_chain": {"rekey_source": "graph/reports/"
                                          "C42_R34_REBUILD_RECORD.json",
                          "rekey": r33_rekey},
            "r30_chain": {"rekey_source": "graph/reports/"
                                          "C42_R31_REBUILD_RECORD.json",
                          "rekey": r30_rekey,
                          "added_ids": sorted(added_ids)},
            "r26_chain": {"rekey_source": "graph/reports/"
                                          "C42_R28_REBUILD_RECORD.json",
                          "rekey": r26_rekey},
            "r36_exclusion": {"source": "scripts/"
                                        "c42_r36_promotions_amendment.yaml",
                              "status": "LANDED (the R37 landing; re-applied "
                                        "via the still-wired R36 map)",
                              "excluded_id": "a107f5041769fdd9",
                              "landed_re_key": R36_NEW_DEMOTE_ID,
                              "landing_class": "unresolved-span worklist"},
            "r39_exclusion": {"source": "scripts/"
                                        "c42_r39_promotions_amendment.yaml",
                              "sha256_16": amend_sha,
                              "excluded_ids": [OLD_DEMOTE_ID1, OLD_DEMOTE_ID2],
                              "landed_re_keys": [NEW_DEMOTE_ID1,
                                                 NEW_DEMOTE_ID2],
                              "landing_class": "unresolved-span worklist "
                                               "(demote-landed class 8 -> 10)"},
        },
        "structural_diff": {
            "rows": "917 -> 917 (no row vanishes; the 2 DEMOTE rows RE-KEY "
                    "into the worklist — chunk identity intact, the W3 "
                    "invariant)",
            "rows_moved": 2,
            "moved_fields": ["spec_code -> None", "mapping_id (the demote "
                             "re-keys)", "sp_title (removed)", "anchor "
                             "(removed)", "worklist_reason (round-tagged, "
                             "added)", "disposition (round-tagged, added)",
                             "provenance.override (added blocks)",
                             "validation_status HUMAN_VALIDATED -> SUGGESTED "
                             "(the round's ONLY status changes) — the DEMOTE "
                             "batch of 2"],
            "promoted_surface_delta": "830 -> 828 HUMAN_VALIDATED (the set "
                                      "narrows by the R39 exclusions); the "
                                      "other 828 promoted rows "
                                      "BYTE-IDENTICAL (no tool churn)",
            "status_changes": "EXACTLY TWO (the demoted rows "
                              "HUMAN_VALIDATED -> SUGGESTED)",
            "header_delta": "status line re-dated (line 3), lines 1-2 verbatim",
        },
        "store_sha256_16_pre": sha16(baseline_store_bytes),
        "store_sha256_16_post": sha16(new_text.encode("utf-8")),
        "ci_parity": {
            "graph_check": "failure census identical pre/post (pre-existing "
                           "sparse-checkout environmental set)",
            "graph_check_failures": len(pre_failures),
            "kg_export": "kg_export --verify-golden GREEN on the rebuilt "
                         "state",
        },
        "post_check": "scripts/c42_r40_rebuild_check.py",
        "not_done": [
            "the next validation re-gate (R41-shaped) NOT fired by this lane "
            "(NOT named by the directive — the operator's call, explicit "
            "instruction only)",
            "no resolution-file / corpus / Lane C / chemistry writes",
            "no R5 promotions-file edits (byte-unchanged since R5, "
            "sha-pinned; the amendments are the dated records)",
        ],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    md = f"""# C42 R40 — Substrate Re-build consuming BOTH R39 carriers — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive fired the R39 record's NEXT lane: this re-build (the store
move the R39 round deferred). The next validation re-gate is NOT named by
the directive — the operator's call, explicit instruction only.

## What this is

The FIFTH substrate re-build consuming a promotions AMENDMENT — and the
SECOND consuming an EXCLUSION-ONLY one, and the third consecutive with NO
tool-version move: the amended c40 tool ({TOOL_OLD.split('@')[0]}@2.7.0)
re-emits the store ALL-SUGGESTED consuming the ELEVEN operator override
maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30 + R33 + R36 + **R39**,
the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED FIVE TIMES OVER**:
`scripts/c42_r39_promotions_amendment.yaml` (schema
`c42-r31-promotions-amendment/1.0`, the loop's FIFTH
promotions-affecting repair record and the SECOND exclusion-ONLY): the 2
DEMOTE rows are EXCLUDED from the re-applied set (they land
unresolved-span via the c40 DEMOTE convention, chunk identity intact —
the W3 invariant), ZERO supersedes and ZERO additions (the R30 additions
mechanism present and UNUSED — no sign-offs owed). The re-applied count
**830 -> 828** (825 from the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 - 2
R39 exclusions] + 3 R30-added sign-offs, the 3 R33 movers re-pinned at
1.8D) — the SECOND re-application that NARROWS the promoted surface.

## The DEMOTE landings (from the R39 map, fail-closed — the loop's FIRST 2-row batch)

- `4MA1-6.3A` -> worklist — basic-probability ord {DEMOTE_ORD1}
  (mapping_id `{OLD_DEMOTE_ID1}` -> `{NEW_DEMOTE_ID1}` = the projected
  re-key `sha16("demoted|<note_path>|{DEMOTE_ORD1}")`, verified live;
  the loop's SEVENTH DEMOTE).
- `4MA1-6.2B` -> worklist — calculations-with-the-mean ord {DEMOTE_ORD2}
  (mapping_id `{OLD_DEMOTE_ID2}` -> `{NEW_DEMOTE_ID2}` = the projected
  re-key, verified live; the loop's EIGHTH DEMOTE).

Both rows land unresolved-span with the round-tagged `worklist_reason` +
`disposition` (the operator-round descriptor `C42 R39 (surface 3: ...`
parsing under the DEMOTE handler's regex, the R16 discipline), RECORDED
never forced, the worklist's demote-landed class deepening 8 -> 10. The
LANDED R36 exclusion re-applies via the still-wired R36 map (the demoted
row re-lands at the same re-key `8254a7fc75ad2946`).

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 -> 133** (UNCHANGED: 6.3A keeps 17 anchored rows via the
tree-diagrams quartet + the combined/conditional 8 + basic-probability
ords 0/2/3/4/5; 6.2B keeps 23; gained `[]`, lost `[]`), uncovered-SP
**55 -> 55**; rows **917 -> 917**; anchored **834 -> 832**;
unresolved-span **28 -> 30**. Per-code: 4MA1-6.3A anchored **18 -> 17**;
4MA1-6.2B anchored **24 -> 23**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R39 map consumed fail-closed (2 verdicted
  DEMOTE_TO_WORKLISTs, override_code null per the R8 rule, current_code ==
  join-derived) + the FOUR R26 STANDING pins verified in-generator
  (unchanged) + coverage recomputed (gained/lost computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R38 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R39 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical — the W3
  invariant; every surviving row BYTE-IDENTICAL — no tool churn; no
  DEFER-row vanish; meta delta == stage + the 2 moving census keys +
  promoted_rows + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  FIVE amendments), the 828-row re-application (825 chained through
  R39-exclusion+R36-exclusion+R33+R30+R26 + 3 R30-added byte-stable), the
  row-set arithmetic, the meta delta assertion, G4-at-apply over every
  chunk row, the anti-forgery sweep, and CI parity (graph_check census
  identical pre/post; kg golden GREEN).
- `scripts/c42_r40_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R37 state) | Post (R40) |
|---|---|---|
| rows | 917 | 917 (the DEMOTE batch re-keys into the worklist) |
| HUMAN_VALIDATED | 830 | 828 (the R39 exclusions narrow the surface) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 28 | 30 (the R39 DEMOTE batch) |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r39.yaml` | `{map_sha}` |
| `c42_r39_promotions_amendment.yaml` | `{amend_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the next validation re-gate (R41-shaped) — NOT named by the directive;
  the operator's call, explicit instruction only
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r40_substrate_rebuild: APPLIED — 917 rows (828 "
          f"HUMAN_VALIDATED re-pinned: 825 chained "
          f"R39+R36-exclusion+R33+R30+R26 + 3 R30-added sign-offs; 2 DEMOTEs "
          f"{OLD_DEMOTE_ID1} -> {NEW_DEMOTE_ID1} and {OLD_DEMOTE_ID2} -> "
          f"{NEW_DEMOTE_ID2} landing unresolved-span; coverage 133/188 "
          f"unchanged)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
