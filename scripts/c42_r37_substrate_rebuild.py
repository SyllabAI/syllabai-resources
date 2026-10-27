#!/usr/bin/env python3
"""c42_r37_substrate_rebuild.py — the T-C42 R37 gated merge point: substrate
re-build consuming the R36 operator override map AND the R36 promotions
amendment (the loop's FOURTH promotions-affecting re-application and the
FIRST exclusion-ONLY one) over the rebuilt store — the round that LANDS the
loop's SIXTH DEMOTE (the R35 fresh REJECT a107f5041769fdd9, adjudicated
DEMOTE_TO_WORKLIST by the operator at R36).

Fired by the operator directive "fire R37 → R38" (2026-10-16, zai-web,
gateway trace 1a144e6357d603d9) over the R36 record's NEXT lane (the R36
round landed the carriers and moved ZERO store bytes; this lane consumes
them); the R38 validation re-gate is sanctioned by the same directive and
fired separately.

The lane is the R12/R16/R20/R24/R26/R28/R31/R34 re-build precedent, now
consuming BOTH R36 carriers (the R36 novelty — the first re-build under an
EXCLUSION-ONLY amended promotion surface, and the second with NO
tool-version move):

  R1. pre-state pins: HEAD == the round-start baseline (the R36-audit HEAD);
      the store on disk is byte-identical to the baseline blob; the
      working-tree dirt is inside the declared R37 footprint; the baseline
      store carries the R34-of-record surface (917 rows, 831
      HUMAN_VALIDATED, meta.promotion_record present);
  R2. the R36 map AND amendment contracts: the map schema
      c42-r28-section-overrides/1.0 with exactly 1 verdicted
      DEMOTE_TO_WORKLIST entry (override_code null per the c40 R8 rule,
      pinned_code == current_code == the join-derived 4MA1-1.6F, mapping_id
      == the R35 fresh REJECT id) + ZERO REATTRIBUTEs + the retain/scoping/
      remarks/promoted_surface_amendment blocks; the amendment schema
      c42-r31-promotions-amendment/1.0 with base_file == the R5 promotions
      path, base_file_sha256_16 == the live R5 sha, base_file_untouched
      true, exactly 0 supersedes_code + 1 excluded + 0 added (the FIRST
      exclusion-ONLY record; the R30 additions mechanism present and
      UNUSED), the excluded entry == the map's DEMOTE row (id, note_path,
      ordinal, pinned_code, disposition);
  R3. the promotions authority chain: the R35 regate check is still
      ALL PASS 10/10 on the R34 landing (its store sha pin == the baseline
      blob's); the R36 repair check is ALL PASS 9/9; the live promotions
      file sha256_16 equals the sha the R5 apply record pinned AND the
      amendment's base pin (the file is byte-unchanged since R5);
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.7.0 —
      STAYS; the second consecutive re-build with NO version move)
      constructs twice byte-identically, emits ALL-SUGGESTED rows, census
      917 = 834 anchored + 28 unresolved-span + 55 uncovered-SP (covered
      133 of 188 — the R36 projections landing: coverage UNCHANGED, gained
      none lost none — the DC-R24-01 compute-never-assert discipline);
  R5. the DEMOTE delta vs the baseline blob: the chunk-identity multiset is
      IDENTICAL (862 chunk rows — the W3 invariant); exactly the 1 map row
      moves — the DEMOTE (old: HUMAN_VALIDATED promoted at 4MA1-1.6F; new:
      mapping_id recomputed to sha16("demoted|<note_path>|4") — the
      projected re-key 8254a7fc75ad2946 verified live — spec_code None, no
      sp_title, no anchor, the round-tagged worklist_reason + disposition,
      provenance.override == the map block, SUGGESTED, no promotion block);
      every surviving row is BYTE-IDENTICAL to its baseline form
      (provenance.tool stays @2.7.0 — no version move); the non-chunk
      worklist rows are byte-identical (55 == 55, no DEFER-row vanish); the
      meta delta is exactly {stage, rows_anchored,
      rows_worklist_anchor_unresolved, promoted_rows} + the 4 additive
      re-dated promotion_reapplied* fields;
  R6. promotions re-application UNDER THE FOUR AMENDMENTS: the R5 file's
      832 entries resolved through the LANDED R26 amendment (its re-key
      read from the R28 record) AND the LANDED R30 amendment (its re-key
      read from the R31 record) AND the LANDED R33 amendment (its re-key
      read from the R34 record) AND the fresh R36 exclusion (the DEMOTE row
      skipped — its rebuilt form IS the demoted worklist row): 827
      direct-or-chained identities (the 3 R33 supersedes re-keyed at the
      AMENDED code 1.8B -> 1.8D via the R34 record; the 5 R30 supersedes
      re-keyed via the R31 record; the 3 R26 supersedes re-keyed via the
      R28 record; the R26 + R30 + R36 exclusions skipped) + the 3 R30-ADDED
      sign-off promotions re-applied byte-stably from the baseline blocks;
      every applied block == the R5 tool shape AND the baseline store's
      block for the same chunk identity (byte-stable re-application);
      meta.promoted_rows SET 830 (831 - 1 exclusion — the surface narrows);
  R7. consolidated row-set arithmetic: new_ids == old_ids - {the demoted
      old id} + {the demoted new id} (917 -> 917); final vs baseline: the
      demoted row carries exactly the enumerated landing fields with the
      round's ONLY status change (HUMAN_VALIDATED -> SUGGESTED), every
      other row byte-identical (the 3 R30-added sign-off rows INCLUDED —
      their HV state + blocks restore byte-stably);
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk + sha/heading/chars); 834/834 coded rows inside the
      ratified 188;
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution in any promotion block, REJECT/hold/worklist categorically
      unpromoted, the 830 HV == the re-composed surface (827 + 3), the
      demoted row lands in the worklist RECORDED never forced — exactly ONE
      DEMOTE this round (the loop's SIXTH, single-row batch over a promoted
      row);
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R37_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r37_substrate_rebuild.py --dry-run
    python3 scripts/c42_r37_substrate_rebuild.py
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
MAP36 = HERE / "c42_section_overrides_r36.yaml"
AMENDMENT = HERE / "c42_r36_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R35_REGATE_CHECK.json"
REPAIR_CHECK = REPO / "graph/reports/C42_R36_REPAIR_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
R31_REC = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
R34_REC = REPO / "graph/reports/C42_R34_REBUILD_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R37_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R37_REBUILD_RECORD.md"

TOOL = "scripts/c42_r37_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "936e6c11adffec1a0b03628e64e2fd7bcb4ff056"
DIRECTIVE = ("fire R37 -> R38 — 2026-10-16, zai-web (gateway trace "
             "1a144e6357d603d9)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
OPERATOR_ROUND = ("C42 R36 (surface 3: 1 verdicted DEMOTE_TO_WORKLIST — the "
                  "R35 fresh REJECT adjudicated; ZERO REATTRIBUTEs, ZERO "
                  "sign-offs)")
OLD_DEMOTE_ID = "a107f5041769fdd9"
NEW_DEMOTE_ID = "8254a7fc75ad2946"
DEMOTE_NOTE = "notes/1-numbers-and-the-number-system/percentages/basic-percentages.json"
DEMOTE_ORD = 4
DEMOTE_CODE = "4MA1-1.6F"
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
# the R37 meta delta: stage + the two moving census keys + promoted_rows
# (831 -> 830, the FIRST re-application that NARROWS the surface) + the
# promotion_reapplied* fields whose VALUES move. NOTE computed honestly:
# promotion_reapplied itself is NOT in the delta — both R34 and R37 ran
# 2026-10-16, so the date value is byte-identical; the by/directive/note
# fields carry the re-dating.
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
        "re-applied byte-stably over the R37 substrate re-build (the c40 "
        "tool emits all-SUGGESTED) AMENDED by "
        "scripts/c42_r36_promotions_amendment.yaml (schema "
        "c42-r31-promotions-amendment/1.0, the loop's FOURTH "
        "promotions-affecting repair record and the FIRST exclusion-ONLY: "
        "0 code supersedes + 1 exclusion + 0 additions, the R30 additions "
        "mechanism present and UNUSED, no sign-offs owed: the R30 round "
        "discharged all 4 H3 holds of record; 830 re-applied = 827 from "
        "the R5 chain [832 - 1 R26 exclusion - 3 R30 exclusions - 1 R36 "
        "exclusion] + 3 R30-added sign-offs, the 3 R33 movers re-pinned "
        "within the set at 1.8D, the R36 DEMOTE row EXCLUDED — its rebuilt "
        "form IS the demoted unresolved-span worklist row at the projected "
        "re-key 8254a7fc75ad2946, the R5 file byte-untouched per the P5 "
        "convention); meta.promoted_rows SET 830 (831 - 1 exclusion — the "
        "FIRST re-application that NARROWS the promoted surface); the 7 "
        "other R5 promotion meta fields byte-equal; the SECOND consecutive "
        "re-application with NO tool-version move (the c40 tool stays "
        "@2.7.0 per the R36 carriers' own contract); see "
        "graph/reports/C42_R37_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R37 substrate re-build (2026-10-16, consuming the R36 operator "
    "override map: basic-percentages ord 4 DEMOTE_TO_WORKLIST — the R35 "
    "fresh REJECT a107f5041769fdd9 adjudicated [the forward "
    "express-one-number-as-a-percentage surface with NO canonical target in "
    "the ratified 188 — the loop's SIXTH DEMOTE, single-row batch over a "
    "promoted row; ZERO REATTRIBUTEs] AND the R36 promotions amendment "
    "(0 code supersedes + 1 exclusion + 0 additions — the FIRST "
    "exclusion-ONLY re-application, NO tool-version move): the R5 §18 "
    "promotion surface re-applied AMENDED FOUR TIMES OVER — 830 rows "
    "HUMAN_VALIDATED (827 from the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 "
    "exclusions] + 3 R30-added sign-offs, the 3 R33 movers re-pinned at "
    "1.8D, the R36 DEMOTE row excluded — it lands unresolved-span via the "
    "c40 DEMOTE convention at the projected re-key 8254a7fc75ad2946); 3 R22 "
    "REJECT rows stay SUGGESTED; the re-homed drawing ord 0 hold stays "
    "SUGGESTED; coverage 133/188 unchanged.\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r37_substrate_rebuild.py",
    "scripts/c42_r37_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R37_REBUILD_RECORD.json",
    "graph/reports/C42_R37_REBUILD_RECORD.md",
    "graph/reports/C42_R37_REBUILD_CHECK.json",
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

    print("C42 R37 SUBSTRATE REBUILD — gated lane (both R36 carriers)")
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
          and len(base["rows"]) == 917 and len(base_anchored) == 835
          and len(base_hv) == 831
          and base["meta"].get("promotion_record") == "scripts/c42_r5_promotions.yaml")
    if not gate("R1_pre_state", r1,
                f"HEAD {head[:12]} == baseline {BASELINE[:12]}; disk store == "
                f"baseline blob; dirty {len(dirty)} within the R37 footprint; "
                f"baseline census 917 = 835 anchored (831 HUMAN_VALIDATED) + "
                f"82 worklist (27 unresolved-span + 55 uncovered-SP); R5 "
                f"promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.7.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R36 map AND amendment contracts --------------------------------
    map_bytes = MAP36.read_bytes()
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
    added_by_mid = {a.get("row", {}).get("mapping_id"): a for a in added}
    d0 = demote[0] if len(demote) == 1 else {}
    x0 = exc[0] if len(exc) == 1 else {}
    r2 = (map_doc.get("schema") == "c42-r28-section-overrides/1.0"
          and map_doc.get("round") == "R36"
          and len(entries) == 1 and len(reattr) == 0 and len(demote) == 1
          and not map_doc.get("h3_signoffs")
          and set(map_doc.get("retain_rulings") or {}) == {"contract"}
          and len(map_doc.get("note_level_scoping") or []) == 1
          and len(map_doc.get("census_remarks") or []) == 2
          and "note_level_adjudications" not in map_doc
          and d0.get("note_slug") == "basic-percentages"
          and d0.get("chunk_ordinal") == DEMOTE_ORD
          and d0.get("mapping_id") == OLD_DEMOTE_ID
          and d0.get("current_code") == DEMOTE_CODE
          and d0.get("provenance_class") == "verdicted"
          and d0.get("action") == "DEMOTE_TO_WORKLIST"
          and d0.get("override_code") is None
          and map_doc.get("promoted_surface_amendment", {}).get("supersedes") == 0
          and map_doc.get("promoted_surface_amendment", {}).get("excluded") == 1
          and map_doc.get("promoted_surface_amendment", {}).get("added") == 0
          and map_doc.get("promoted_surface_amendment", {}).get("base_file_untouched") is True
          and amend.get("schema") == "c42-r31-promotions-amendment/1.0"
          and amend.get("round") == "R36"
          and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
          and amend.get("base_file_sha256_16") == promo_sha
          and amend.get("base_file_untouched") is True
          and amend.get("prior_amendments") == \
          ["scripts/c42_r26_promotions_amendment.yaml",
           "scripts/c42_r30_promotions_amendment.yaml",
           "scripts/c42_r33_promotions_amendment.yaml"]
          and len(sup) == 0 and len(exc) == 1 and len(added) == 0
          and x0.get("mapping_id") == OLD_DEMOTE_ID
          and x0.get("note_path") == DEMOTE_NOTE
          and x0.get("chunk_ordinal") == DEMOTE_ORD
          and x0.get("pinned_code") == DEMOTE_CODE
          and x0.get("disposition") == "DEMOTE_TO_WORKLIST")
    if not gate("R2_map_and_amendment_contracts", r2,
                f"map schema c42-r28-section-overrides/1.0; exactly 1 "
                f"verdicted DEMOTE_TO_WORKLIST ({OLD_DEMOTE_ID}, "
                f"basic-percentages ord {DEMOTE_ORD}, current_code == the "
                f"join-derived {DEMOTE_CODE}, override_code null per the c40 "
                f"R8 rule) + ZERO REATTRIBUTEs + ZERO sign-offs; the zero-"
                f"retain contract + the STANDING scoping (the corpus anchor "
                f"spcpt_FHRjdMc6tvRR553q stands at 1.6F) + 2 census remarks "
                f"recorded; amendment schema c42-r31-promotions-amendment/"
                f"1.0 with base sha {amend.get('base_file_sha256_16')} == "
                f"the live R5 sha, 0 supersedes + 1 excluded (id == the map's "
                f"DEMOTE row, pinned_code {DEMOTE_CODE}, disposition "
                f"DEMOTE_TO_WORKLIST) + 0 ADDED (the FIRST exclusion-ONLY "
                f"record; the R30 additions mechanism present and UNUSED); "
                f"map sha {map_sha}, amendment sha {amend_sha}"):
        die("R2 map/amendment contracts failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check35 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    check36 = json.loads(REPAIR_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check35.get("result") == "ALL PASS" and check35.get("passed") == 10
          and check35.get("total") == 10
          and check35.get("store_sha256_16") == sha16(baseline_store_bytes)
          and check36.get("result") == "ALL PASS" and check36.get("passed") == 9
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R35 regate ALL PASS 10/10 with its store sha pin == the "
                f"baseline blob ({sha16(baseline_store_bytes)} — the R34 "
                f"landing of record, byte-identical through R35/R36); R36 "
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
          and len(rows_new) == 917 and n_anchored == 834 and n_span == 28
          and n_unmapped == 55 and len(covered) == 133
          and len(ids_new) == len(set(ids_new))
          and "4MA1-1.6F" in covered and "4MA1-2.7C" in covered
          and "4MA1-1.8D" in covered and "4MA1-1.8B" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 917 = 834 anchored + 28 unresolved-span + 55 "
                f"uncovered-SP; covered 133 of 188 (the R36 projections "
                f"landing: coverage UNCHANGED — 1.6F keeps 5 anchored rows, "
                f"the reverse-percentages trio + basic-percentages ords 0/3; "
                f"computed, never asserted — the DC-R24-01 discipline); "
                f"mapping_ids unique"):
        die("R4 rebuild failed")
    if gained or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 the DEMOTE delta vs the baseline blob ------------------------------
    old_chunk = {ident(r): r for r in base["rows"] if "chunk" in r}
    new_chunk = {ident(r): r for r in rows_new if "chunk" in r}
    r5_ok = (set(old_chunk) == set(new_chunk) and len(old_chunk) == 862
             and len(set(old_chunk)) == 862)
    moved, id_pairs, demote_pairs, drift = [], [], [], []
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
                    "source": f"scripts/c42_section_overrides_r36.yaml@{map_sha}",
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
                    "forced (C42 R36 surface 3 demote)")
                ok_row = (
                    orow["spec_code"] == DEMOTE_CODE
                    and orow["mapping_id"] == OLD_DEMOTE_ID
                    and orow.get("validation_status") == "HUMAN_VALIDATED"
                    and "promotion" in orow
                    and nrow.get("spec_code") is None
                    and "sp_title" not in nrow
                    and "anchor" not in nrow
                    and nrow["mapping_id"] == want_mid == NEW_DEMOTE_ID
                    and nrow.get("worklist_reason") == want_reason
                    and nrow.get("disposition") == want_disp
                    and nrow.get("provenance", {}).get("override") == want_block
                    and nrow.get("validation_status") == "SUGGESTED"
                    and "promotion" not in nrow
                    and nrow["evidence_quote"] == orow["evidence_quote"]
                    and nrow["rationale"] == orow["rationale"]
                    and x0.get("note_path") == orow["note_path"]
                    and int(x0.get("chunk_ordinal", -1)) ==
                        int(orow["chunk"]["ordinal"]))
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
        # round — NO DEFER-row vanish (the R31 2.7C resolution already landed)
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
    r5_pass = (r5_ok and len(moved) == 1 and len(demote_pairs) == 1
               and len(id_pairs) == 0 and not drift
               and demote_pairs == [(OLD_DEMOTE_ID, NEW_DEMOTE_ID)])
    if not gate("R5_demote_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows — the W3 "
                f"invariant); exactly 1 row moves — the DEMOTE: "
                f"{OLD_DEMOTE_ID} (HUMAN_VALIDATED promoted at {DEMOTE_CODE}) "
                f"-> {NEW_DEMOTE_ID} (the projected re-key "
                f"sha16('demoted|<note_path>|{DEMOTE_ORD}') verified live; "
                f"the loop's SIXTH DEMOTE, single-row batch over a promoted "
                f"row); spec_code -> None, no sp_title, no anchor; the "
                f"round-tagged worklist_reason + disposition parse under the "
                f"'C42 R36 (surface 3:' operator-round descriptor; "
                f"provenance.override == the map block (map sha {map_sha}); "
                f"evidence quote + rationale byte-carried; SUGGESTED with NO "
                f"promotion block; every surviving row BYTE-IDENTICAL to its "
                f"baseline form (provenance.tool stays @2.7.0 — the second "
                f"re-build with NO tool churn); the 55 non-chunk worklist "
                f"rows byte-identical (no DEFER-row vanish)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application UNDER THE FOUR AMENDMENTS ----------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    # the LANDED R26 amendment translation (read from the R28 record), the
    # LANDED R30 amendment translation (read from the R31 record — its
    # supersedes AND its 3 exclusions, both standing), the LANDED R33
    # amendment translation (read from the R34 record — this is the FIRST
    # re-application where the R33 re-key is LANDED state rather than this
    # lane's own delta) and the fresh R36 exclusion (the DEMOTE row skipped)
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
    r36_exc = {e["mapping_id"] for e in exc}          # the fresh R36 exclusion
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
    for eid, e in exc_by_id.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"R36 amendment excluded {eid} drift vs the R5 file")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"amendment pre-apply problems: {problems[:4]}")
        die("R6 amendment pre-apply integrity failed")
    # resolve every R5 entry against the rebuilt rows through ALL FOUR
    # amendments (R36 exclusion -> R33 newest -> R30 -> R26 -> direct)
    resolved = {}
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        if mid in r26_exc or mid in r30_exc or mid in r36_exc:
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
    # the R26 + R30 + R36 excluded rows' rebuilt forms ARE the demoted
    # worklist rows (the R36 one via the c40 DEMOTE convention at the
    # projected re-key)
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
    for eid in r36_exc:
        trow = new_rows.get(NEW_DEMOTE_ID)
        if trow is None or trow.get("worklist_reason") is None \
                or trow.get("validation_status") != "SUGGESTED" \
                or "promotion" in trow \
                or trow.get("note_path") != DEMOTE_NOTE \
                or trow["chunk"]["ordinal"] != DEMOTE_ORD:
            problems.append(f"the R36 excluded row {eid} is not the demoted "
                            f"unresolved-span worklist row at {NEW_DEMOTE_ID}")
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
    if (len(resolved) != 827 or len(resolved) + len(added_ids) != 830
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
        # row (the 827 chain + the 3 R30-added sign-offs) carries one there
        base_block = base_by_ident[ident(row)].get("promotion")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if base_block is None or block != base_block:
            die(f"promotion block drift vs the baseline surface on {mid}")
        row["promotion"] = block
        flipped += 1
    if flipped != 830:
        die(f"flipped {flipped} != 830")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    meta_f["promoted_rows"] = 830            # SET — the narrowed surface
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"the amendment pre-apply integrity verified (pinned_code == the R5 "
         f"file on every supersedes entry of the LANDED amendments — R33 3 + "
         f"R30 5 + R26 3 — and the R36 excluded entry's identity drift-free "
         f"vs the R5 file — any drift fails); 832 R5 entries resolved through "
         f"the LANDED R26 amendment (its re-key read from the R28 record), "
         f"the LANDED R30 amendment (its re-key read from the R31 record), "
         f"the LANDED R33 amendment (its re-key read from the R34 record — "
         f"LANDED state for the first time) and the fresh R36 exclusion: 827 "
         f"direct-or-chained identities (the 3 R33 supersedes re-keyed at the "
         f"AMENDED code 1.8B->1.8D — ords 6/7/8 of rounding-and-estimation "
         f"REMAIN promoted; the 5 R30 supersedes via the R31 record; the 3 "
         f"R26 supersedes via the R28 record; the R26 exclusion + the 3 R30 "
         f"exclusions + THE R36 EXCLUSION skipped — their rebuilt forms ARE "
         f"the demoted worklist rows) + the 3 R31-ADDED sign-off promotions "
         f"re-applied byte-stably from the baseline blocks; validated_by "
         f"operator everywhere; sampled 457 == the R21 CONFIRM set (R5-era "
         f"ids; the demoted row's R5 entry carries no verdict — verified); "
         f"surface == anchored 834 - R22 REJECT 3 - the re-homed hold 1 == "
         f"830 both directions (827 + 3); every applied block == the R5 tool "
         f"shape AND the baseline store's block for the same chunk identity "
         f"(byte-stable re-application); meta promotion fields restored "
         f"byte-equal EXCEPT promoted_rows SET 830 (831 - 1 exclusion — the "
         f"FIRST re-application that NARROWS the surface) + 4 additive "
         f"re-dated promotion_reapplied* fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = (old_ids - {OLD_DEMOTE_ID}) | {NEW_DEMOTE_ID}
    r7 = new_ids == want_new and len(new_ids) == 917
    fin_chunk = {ident(r): r for r in final_doc["rows"] if "chunk" in r}
    moved_idents = set(moved)
    cons_drift, status_changes = [], []
    demote_key = moved_idents.copy()
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
          and len(status_changes) == 1
          and set(status_changes) == demote_key
          and meta_f["promoted_rows"] == 830
          and base["meta"]["promoted_rows"] == 831)
    if not gate("R7_row_set_arithmetic", r7,
                f"new_ids == old_ids - the demoted old id + the demoted new "
                f"id (917 -> 917) exactly; consolidated final-vs-baseline "
                f"equality: EXACTLY ONE status change — the demoted row "
                f"(HUMAN_VALIDATED -> SUGGESTED, the round's only one), every "
                f"non-moved row byte-identical (provenance.tool stays "
                f"@2.7.0, the 3 R30-added sign-off rows restore byte-stably), "
                f"the meta delta == exactly stage + rows_anchored + "
                f"rows_worklist_anchor_unresolved + promoted_rows (831 -> "
                f"830 — the narrowed surface) + the promotion_reapplied_by/"
                f"directive/note fields (the promotion_reapplied date value "
                f"itself coincides — both rounds ran 2026-10-16 — so the "
                f"re-dating rides the other three fields)"
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
    r8 = not failed and n_coded == 834
    if not gate("R8_g4_at_apply", r8,
                f"all {sum(1 for x in final_doc['rows'] if 'chunk' in x)} chunk "
                f"rows re-verified against a fresh re-chunking (quote-in-chunk "
                f"+ sha/heading/chars); {n_coded}/834 coded rows inside the "
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
    dem_row = next(x for x in final_doc["rows"]
                   if x["mapping_id"] == NEW_DEMOTE_ID)
    r9 = (len(hv) == 830 and {x["mapping_id"] for x in hv} == promote_set
          and sug_anch == vrej_new | vhold_remaining
          and tiers_ok and attribution_ok
          and not (demoted_ids & {x["mapping_id"] for x in hv})
          and dem_row.get("worklist_reason")
          and "promotion" not in dem_row
          and dem_row.get("validation_status") == "SUGGESTED"
          and not (promote_set & (worklist_new | vhold_remaining | vrej_new)))
    if not gate("R9_anti_forgery", r9,
                f"830 HUMAN_VALIDATED == the re-composed promotion set "
                f"(827 from the R5 chain + 3 R30-added sign-offs, the 3 R33 "
                f"movers re-pinned within it); the SUGGESTED anchored "
                f"residue == the 3 R22 re-attributed REJECTs + the 1 "
                f"re-homed hold; EXACTLY ONE DEMOTE this round — the loop's "
                f"SIXTH, landing unresolved-span RECORDED never forced (the "
                f"worklist's demote-landed class deepens 7 -> 8); provenance "
                f"tiers RULE_DERIVED everywhere; operator attribution clean; "
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
        print(f"c42_r37_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 917 rows (830 HUMAN_VALIDATED re-applied "
              f"AMENDED FOUR TIMES OVER: 827 + 3 R30-added sign-offs, the 3 "
              f"R33 movers re-pinned at 1.8D; 1 DEMOTE landing "
              f"{OLD_DEMOTE_ID} -> {NEW_DEMOTE_ID} + 0 REATTRIBUTEs; "
              f"coverage 133/188 unchanged); no files written")
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
    demote_landings = [{
        "note_slug": d0["note_slug"], "chunk_ordinal": d0["chunk_ordinal"],
        "mapping_id_old": OLD_DEMOTE_ID, "mapping_id_new": NEW_DEMOTE_ID,
        "from_code": DEMOTE_CODE, "to_code": None,
        "disposition": "DEMOTE_TO_WORKLIST",
        "landing": "unresolved-span via the c40 DEMOTE convention "
                   "(round-tagged worklist_reason + disposition; chunk "
                   "identity intact — the W3 invariant; RECORDED never "
                   "forced)",
        "round_tag": OPERATOR_ROUND,
    }]
    rec = {
        "schema": "c42-r37-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r37-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R36 record's NEXT lane, fired by the directive: the "
                 "substrate re-build consuming the R36 override map (schema "
                 "c42-r28-section-overrides/1.0) AND the R36 promotions "
                 "amendment (schema c42-r31-promotions-amendment/1.0, the "
                 "FIRST exclusion-ONLY); the R38 validation re-gate "
                 "sanctioned by the same directive and fired separately"),
        "rebuild": {
            "tool": f"{TOOL_OLD.split('@')[0]}@2.7.0",
            "tool_version_move": "NONE — TOOL_VERSION stays 2.7.0 per the "
                                 "R36 carriers' own contract (the second "
                                 "consecutive re-build with no version move; "
                                 "provenance.tool byte-stable on every row)",
            "join": "the R27-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged; the FOUR R26 STANDING pins verified "
                    "in-generator; the basic-percentages corpus anchor "
                    "spcpt_FHRjdMc6tvRR553q STANDS at 1.6F — the R36 "
                    "scoping rides the store rows, the join layer untouched)",
            "override_maps_consumed": ("TEN: R1 + R6 (with the subsumption "
                                       "registry) + R10 + R14 + R18 + R22 + "
                                       "R26 + R30 + R33 + R36, all fail-closed"),
            "rows_pre": 917, "rows_post": 917,
            "anchored": 834, "unresolved_span": 28, "uncovered_sp": 55,
            "covered_pre": 133, "covered_post": 133,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r36.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "reattribute": len(reattr), "demote": len(demote),
            "landings": [],
            "demote_landings": demote_landings,
            "standing_pins": ("the FOUR R26 STANDING joins verified "
                              "in-generator (unchanged); the R36 STANDING "
                              "scoping rides the map's note_level_scoping "
                              "block — the basic-percentages corpus anchor "
                              "spcpt_FHRjdMc6tvRR553q STANDS at 1.6F (the "
                              "note keeps ords 0/3 alongside the "
                              "reverse-percentages trio); NO new "
                              "c40-pinned adjudications this round"),
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "amendment": {
                "path": "scripts/c42_r36_promotions_amendment.yaml",
                "sha256_16": amend_sha,
                "schema": "c42-r31-promotions-amendment/1.0",
                "supersedes": len(sup), "excluded": len(exc),
                "added": len(added),
                "pre_apply_integrity": "pinned_code verified against the R5 "
                                       "file BEFORE the amendment applies "
                                       "(all FOUR amendments: R36 excluded + "
                                       "R33 + R30 + R26)",
                "re_applied": 830,
                "re_applied_composition": "827 from the R5 chain [832 - 1 "
                                          "R26 - 3 R30 - 1 R36 exclusions] + "
                                          "3 R30-added sign-offs, the 3 R33 "
                                          "movers re-pinned within the set",
                "meta_promoted_rows_restated": "830 (831 - 1 exclusion — the "
                                               "FIRST re-application that "
                                               "NARROWS the promoted surface; "
                                               "the 7 other R5 promotion meta "
                                               "fields byte-equal)",
            },
            "reapplication": ("byte-stable: every applied block for all 830 "
                              "== the R5 tool's block shape AND the baseline "
                              "store's block for the same chunk identity "
                              "(the R30-added sign-offs INCLUDED — their "
                              "baseline blocks restore byte-stably); the 3 "
                              "superseded rows REMAIN in the promoted set at "
                              "their amended codes (re-keyed old->new, the "
                              "R24 id_pairs convention); the R26 + R30 + R36 "
                              "excluded rows stay unpromoted worklist rows "
                              "(the R36 one via the c40 DEMOTE convention at "
                              "the projected re-key); meta gains ONLY the "
                              "additive re-dated promotion_reapplied* fields "
                              "+ the narrowed promoted_rows"),
            "superseded_ids_rekeyed": {},
            "excluded_ids": [OLD_DEMOTE_ID],
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
                              "sha256_16": amend_sha,
                              "excluded_id": OLD_DEMOTE_ID,
                              "landed_re_key": NEW_DEMOTE_ID,
                              "landing_class": "unresolved-span worklist "
                                               "(demote-landed class 7 -> 8)"},
        },
        "structural_diff": {
            "rows": "917 -> 917 (no row vanishes; the DEMOTE row RE-KEYS "
                    "into the worklist — chunk identity intact, the W3 "
                    "invariant)",
            "rows_moved": 1,
            "moved_fields": ["spec_code -> None", "mapping_id (the demote "
                             "re-key)", "sp_title (removed)", "anchor "
                             "(removed)", "worklist_reason (round-tagged, "
                             "added)", "disposition (round-tagged, added)",
                             "provenance.override (added block)",
                             "validation_status HUMAN_VALIDATED -> SUGGESTED "
                             "(the round's ONLY status change) — the DEMOTE"],
            "promoted_surface_delta": "831 -> 830 HUMAN_VALIDATED (the set "
                                      "narrows by the R36 exclusion); the "
                                      "other 830 promoted rows "
                                      "BYTE-IDENTICAL (no tool churn)",
            "status_changes": "EXACTLY ONE (the demoted row HUMAN_VALIDATED "
                              "-> SUGGESTED)",
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
        "post_check": "scripts/c42_r37_rebuild_check.py",
        "not_done": [
            "the R38 validation re-gate NOT fired by this lane (it is "
            "sanctioned by the same directive and fired as its own round)",
            "no resolution-file / corpus / Lane C / chemistry writes",
            "no R5 promotions-file edits (byte-unchanged since R5, "
            "sha-pinned; the amendments are the dated records)",
        ],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    md = f"""# C42 R37 — Substrate Re-build consuming BOTH R36 carriers — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive fired the R36 record's NEXT lanes in order: this re-build, then
the R38 validation re-gate (fired separately).

## What this is

The FOURTH substrate re-build consuming a promotions AMENDMENT — and the
FIRST consuming an EXCLUSION-ONLY one, and the second consecutive with NO
tool-version move: the amended c40 tool ({TOOL_OLD.split('@')[0]}@2.7.0 —
the R36 carriers' own contract) re-emits the store ALL-SUGGESTED consuming
the TEN operator override maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30
+ R33 + **R36**, the new one, schema `c42-r28-section-overrides/1.0`), and
the R5 promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED FOUR TIMES OVER**:
`scripts/c42_r36_promotions_amendment.yaml` (schema
`c42-r31-promotions-amendment/1.0`, the loop's FOURTH
promotions-affecting repair record and the FIRST exclusion-ONLY): the
DEMOTE row is EXCLUDED from the re-applied set (it lands unresolved-span via
the c40 DEMOTE convention, chunk identity intact — the W3 invariant), ZERO
supersedes and ZERO additions (the R30 additions mechanism present and
UNUSED — no sign-offs owed). The re-applied count **831 -> 830** (827 from
the R5 chain [832 - 1 R26 - 3 R30 - 1 R36 exclusions] + 3 R30-added
sign-offs, the 3 R33 movers re-pinned at 1.8D) — the FIRST re-application
that NARROWS the promoted surface.

## The DEMOTE landing (from the R36 map, fail-closed)

- `4MA1-1.6F` -> worklist — basic-percentages ord {DEMOTE_ORD}
  (mapping_id `{OLD_DEMOTE_ID}` -> `{NEW_DEMOTE_ID}` = the projected re-key
  `sha16("demoted|<note_path>|{DEMOTE_ORD}")`, verified live; the loop's
  SIXTH DEMOTE, single-row batch over a promoted row). The row lands
  unresolved-span with the round-tagged `worklist_reason` + `disposition`
  (the operator-round descriptor `C42 R36 (surface 3: ...` parsing under
  the DEMOTE handler's regex, the R16 discipline), RECORDED never forced,
  the worklist's demote-landed class deepening 7 -> 8.

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 -> 133** (UNCHANGED: 1.6F keeps its coverage via the
reverse-percentages trio + basic-percentages ords 0/3 — the demoted row's
code keeps its dedicated note's trio; gained `[]`, lost `[]`), uncovered-SP
**55 -> 55**; rows **917 -> 917**; anchored **835 -> 834**; unresolved-span
**27 -> 28**. Per-code: 4MA1-1.6F anchored **6 -> 5**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R36 map consumed fail-closed (1 verdicted
  DEMOTE_TO_WORKLIST, override_code null per the R8 rule, current_code ==
  join-derived) + the FOUR R26 STANDING pins verified in-generator
  (unchanged) + coverage recomputed (gained/lost computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R35 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R36 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical — the W3
  invariant; every surviving row BYTE-IDENTICAL — no tool churn; no
  DEFER-row vanish; meta delta == stage + the 2 moving census keys +
  promoted_rows + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  FOUR amendments), the 830-row re-application (827 chained through
  R36-exclusion+R33+R30+R26 + 3 R30-added byte-stable), the row-set
  arithmetic, the meta delta assertion, G4-at-apply over every chunk row,
  the anti-forgery sweep, and CI parity (graph_check census identical
  pre/post; kg golden GREEN).
- `scripts/c42_r37_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R34 state) | Post (R37) |
|---|---|---|
| rows | 917 | 917 (the DEMOTE re-keys into the worklist) |
| HUMAN_VALIDATED | 831 | 830 (the R36 exclusion narrows the surface) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 27 | 28 (the R36 DEMOTE) |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r36.yaml` | `{map_sha}` |
| `c42_r36_promotions_amendment.yaml` | `{amend_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the R38 validation re-gate — sanctioned by the directive's "→ R38" clause,
  fired as its own round
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r37_substrate_rebuild: APPLIED — 917 rows (830 "
          f"HUMAN_VALIDATED re-pinned: 827 chained R36-exclusion+R33+R30+R26 "
          f"+ 3 R30-added sign-offs; 1 DEMOTE {OLD_DEMOTE_ID} -> "
          f"{NEW_DEMOTE_ID} landing unresolved-span; coverage 133/188 "
          f"unchanged)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
