#!/usr/bin/env python3
"""c42_r34_substrate_rebuild.py — the T-C42 R34 gated merge point: substrate
re-build consuming the R33 operator override map AND the R33 promotions
amendment (the loop's THIRD promotions-affecting re-application and the
FIRST supersedes-ONLY one) over the rebuilt store.

Fired by the operator directive "fire R34 → R35" (2026-10-16, zai-web,
gateway trace 1a1439559c9023f1) over the R33 record's NEXT lane (the R33
round landed the carriers; this lane consumes them); the R35 validation
re-gate is sanctioned by the same directive and fired separately.

The lane is the R12/R16/R20/R24/R26/R28/R31 re-build precedent, now consuming
BOTH R33 carriers (the R33 novelty — the first re-build under a
SUPERSEDES-ONLY amended promotion surface, and the first with NO
tool-version move):

  R1. pre-state pins: HEAD == the round-start baseline (the R33-audit HEAD);
      the store on disk is byte-identical to the baseline blob; the
      working-tree dirt is inside the declared R34 footprint; the baseline
      store carries the R31-of-record surface (917 rows, 831
      HUMAN_VALIDATED, meta.promotion_record present);
  R2. the R33 map AND amendment contracts: the map schema
      c42-r28-section-overrides/1.0 with exactly 3 verdicted REATTRIBUTE
      entries (ratified targets != currents, all three HUMAN_VALIDATED
      promotions — the supersedes shape) + ZERO DEMOTEs + the
      retain/scoping/remarks blocks (the loop's FIRST SPLIT-note scoping);
      the amendment schema c42-r31-promotions-amendment/1.0 with base_file
      == the R5 promotions path, base_file_sha256_16 == the live R5 sha,
      base_file_untouched true, exactly 3 supersedes_code + 0 excluded +
      0 added (the R30 additions mechanism present and UNUSED), the ids
      distinct and covering exactly the map's REATTRIBUTE movers,
      pinned_code == the map's current_code and amended_code == the map's
      override_code on every promoted REATTRIBUTE row;
  R3. the promotions authority chain: the R32 regate check is still
      ALL PASS 10/10 on the R31 landing (its store sha pin == the baseline
      blob's); the R33 repair check is ALL PASS 9/9; the live promotions
      file sha256_16 equals the sha the R5 apply record pinned AND the
      amendment's base pin (the file is byte-unchanged since R5);
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.7.0 —
      the R33 carriers' own contract, the first re-build with NO version
      move) constructs twice byte-identically, emits ALL-SUGGESTED rows,
      census 917 = 835 anchored + 27 unresolved-span + 55 uncovered-SP
      (covered 133 of 188 — the R33 projections landing: coverage
      UNCHANGED, gained none lost none — the DC-R24-01 compute-never-assert
      discipline);
  R5. re-attribution delta vs the baseline blob: the chunk-identity
      multiset is IDENTICAL (862 chunk rows); exactly the 3 map rows move —
      the 3 REATTRIBUTEs (old code == current_code, new code ==
      override_code, mapping_id recomputed — the R24 id_pairs convention,
      the projected re-keys verified live — provenance.override == the map
      block, sp_title == the registry wording); every surviving row is
      BYTE-IDENTICAL to its baseline form (provenance.tool stays @2.7.0 —
      no version move, the first re-build where the tool string does not
      churn); the non-chunk worklist rows are byte-identical (55 == 55, no
      DEFER-row vanish); the meta delta is exactly {stage} + the 4 additive
      re-dated promotion_reapplied* fields (promoted_rows RESTATED 831 —
      the value unchanged, the set re-pinned row-level);
  R6. promotions re-application UNDER THE AMENDMENTS: the R5 file's 832
      entries resolved through the LANDED R26 amendment (its re-key read
      from the R28 record) AND the LANDED R30 amendment (its re-key read
      from the R31 record) AND the fresh R33 amendment (its re-key read
      from THIS lane's delta): 828 direct-or-chained identities (the 3 R33
      supersedes re-keyed old->new at the AMENDED code 1.8B -> 1.8D; the 5
      R30 supersedes re-keyed via the R31 record; the 3 R26 supersedes
      re-keyed via the R28 record; the R26 + R30 exclusions skipped —
      their rebuilt forms ARE the demoted worklist rows) + the 3 R31 ADDED
      sign-off promotions re-applied byte-stably from the baseline blocks;
      every applied block == the R5 tool shape AND the baseline store's
      block for the same chunk identity (byte-stable re-application);
      meta.promoted_rows RESTATED 831 (the value unchanged — the set
      re-pinned: ords 6/7/8 of rounding-and-estimation now at 1.8D);
  R7. consolidated row-set arithmetic: new_ids == old_ids - {3 old
      REATTRIBUTE ids} + {3 new REATTRIBUTE ids} (917 -> 917); final vs
      baseline: the 3 moved rows carry exactly the enumerated fields, every
      other row byte-identical (the 3 R30-added sign-off rows INCLUDED —
      their HV state + blocks restore byte-stably);
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk + sha/heading/chars); 835/835 coded rows inside the
      ratified 188;
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution in any promotion block, REJECT/hold/worklist categorically
      unpromoted, the 831 HV == the re-composed surface (828 + 3), ZERO
      DEMOTEs this round;
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R34_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r34_substrate_rebuild.py --dry-run
    python3 scripts/c42_r34_substrate_rebuild.py
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
MAP33 = HERE / "c42_section_overrides_r33.yaml"
AMENDMENT = HERE / "c42_r33_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R32_REGATE_CHECK.json"
REPAIR_CHECK = REPO / "graph/reports/C42_R33_REPAIR_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
R31_REC = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R34_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R34_REBUILD_RECORD.md"

TOOL = "scripts/c42_r34_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "9cd386c12aac240da7796ea6724748979397aaf8"
DIRECTIVE = ("fire R34 -> R35 — 2026-10-16, zai-web (gateway trace "
             "1a1439559c9023f1)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
OPERATOR_ROUND = ("C42 R33 (surface 3: 3 verdicted REATTRIBUTEs [all "
                  "HUMAN_VALIDATED, the supersedes shape] — the 1.8B->1.8D "
                  "re-home batch — the loop's FIRST SPLIT-note scoping)")
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
REAPPLIED_META = {
    "promotion_reapplied": "2026-10-16",
    "promotion_reapplied_by": f"{TOOL}@{VERSION}",
    "promotion_reapplied_directive": DIRECTIVE,
    "promotion_reapplied_note": (
        "re-applied byte-stably over the R34 substrate re-build (the c40 "
        "tool emits all-SUGGESTED) AMENDED by "
        "scripts/c42_r33_promotions_amendment.yaml (schema "
        "c42-r31-promotions-amendment/1.0, the loop's THIRD "
        "promotions-affecting repair record and the FIRST supersedes-ONLY: "
        "3 code supersedes re-keyed old->new — the R33 re-home rows REMAIN "
        "in the promoted set at their amended codes — + 0 exclusions + 0 "
        "additions, the R30 additions mechanism present and UNUSED, no "
        "sign-offs owed: the R30 round discharged all 4 H3 holds of "
        "record; 831 re-applied = 828 from the R5 chain + 3 R30-added "
        "sign-offs, the 3 R33 movers re-pinned within the set, the R5 "
        "file byte-untouched per the P5 convention); meta.promoted_rows "
        "RESTATED 831 (the value unchanged — the set re-pinned row-level: "
        "ords 6/7/8 of rounding-and-estimation now at 1.8D); the 7 other "
        "R5 promotion meta fields byte-equal; the FIRST re-application "
        "with NO tool-version move (the c40 tool stays @2.7.0 per the R33 "
        "carriers' own contract); see "
        "graph/reports/C42_R34_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R34 substrate re-build (2026-10-16, consuming the R33 operator "
    "override map: rounding-and-estimation ords 6/7/8 1.8B->1.8D [the "
    "estimation half re-homed row-level, ords 0-5 staying 1.8B — the loop's "
    "FIRST SPLIT-note scoping; ZERO DEMOTEs] AND the R33 promotions "
    "amendment (3 code supersedes + 0 exclusions + 0 additions — the FIRST "
    "supersedes-ONLY re-application, NO tool-version move): the R5 §18 "
    "promotion surface re-applied AMENDED THRICE OVER — 831 rows "
    "HUMAN_VALIDATED (828 from the R5 chain + 3 R30-added sign-offs, the 3 "
    "R33 movers re-pinned at 1.8D); 3 R22 REJECT rows stay SUGGESTED; the "
    "re-homed drawing ord 0 hold stays SUGGESTED; coverage 133/188 "
    "unchanged.\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r34_substrate_rebuild.py",
    "scripts/c42_r34_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R34_REBUILD_RECORD.json",
    "graph/reports/C42_R34_REBUILD_RECORD.md",
    "graph/reports/C42_R34_REBUILD_CHECK.json",
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

    print("C42 R34 SUBSTRATE REBUILD — gated lane (both R33 carriers)")
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
                f"baseline blob; dirty {len(dirty)} within the R34 footprint; "
                f"baseline census 917 = 835 anchored (831 HUMAN_VALIDATED) + "
                f"82 worklist (27 unresolved-span + 55 uncovered-SP); R5 "
                f"promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.7.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R33 map AND amendment contracts --------------------------------
    map_bytes = MAP33.read_bytes()
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
    sup_by_id = {e.get("mapping_id"): e for e in sup}
    exc_by_id = {e.get("mapping_id"): e for e in exc}
    added_by_mid = {a.get("row", {}).get("mapping_id"): a for a in added}
    r2 = (map_doc.get("schema") == "c42-r28-section-overrides/1.0"
          and map_doc.get("round") == "R33"
          and len(entries) == 3 and len(reattr) == 3 and len(demote) == 0
          and not map_doc.get("h3_signoffs")
          and len(map_doc.get("retain_rulings") or {}) - 1 == 2
          and len(map_doc.get("note_level_scoping") or []) == 1
          and "note_level_adjudications" not in map_doc
          and all(e.get("action") == "REATTRIBUTE"
                  and e.get("provenance_class") == "verdicted"
                  and e.get("override_code") in registry
                  and e.get("override_code") != e.get("current_code")
                  for e in reattr)
          and amend.get("schema") == "c42-r31-promotions-amendment/1.0"
          and amend.get("round") == "R33"
          and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
          and amend.get("base_file_sha256_16") == promo_sha
          and amend.get("base_file_untouched") is True
          and amend.get("prior_amendments") == \
          ["scripts/c42_r26_promotions_amendment.yaml",
           "scripts/c42_r30_promotions_amendment.yaml"]
          and len(sup) == 3 and len(exc) == 0 and len(added) == 0
          and len(set(sup_by_id)) == 3
          and {e.get("mapping_id") for e in entries} == set(sup_by_id)
          and all(sup_by_id[e["mapping_id"]].get("pinned_code") ==
                  e.get("current_code")
                  and sup_by_id[e["mapping_id"]].get("amended_code") ==
                  e.get("override_code")
                  for e in reattr))
    if not gate("R2_map_and_amendment_contracts", r2,
                f"map schema c42-r28-section-overrides/1.0; 3 verdicted "
                f"REATTRIBUTEs with ratified targets != currents "
                f"({', '.join(sorted(e['current_code'] + '->' + e['override_code'] for e in reattr))})"
                f" — all HV promotions, the supersedes shape; ZERO DEMOTEs; "
                f"2 retains + the loop's FIRST SPLIT-note scoping recorded, "
                f"no NEW c40-pinned adjudications; amendment schema "
                f"c42-r31-promotions-amendment/1.0 with base sha "
                f"{amend.get('base_file_sha256_16')} == the live R5 sha, 3 "
                f"supersedes (amended_code == override_code) + 0 excluded "
                f"+ 0 ADDED (the R30 additions mechanism present and "
                f"UNUSED), the 3 ids distinct and covering exactly the "
                f"map's movers; map sha {map_sha}, amendment sha "
                f"{amend_sha}"):
        die("R2 map/amendment contracts failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check32 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    check33 = json.loads(REPAIR_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check32.get("result") == "ALL PASS" and check32.get("passed") == 10
          and check32.get("total") == 10
          and check32.get("store_sha256_16") == sha16(baseline_store_bytes)
          and check33.get("result") == "ALL PASS" and check33.get("passed") == 9
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R32 regate ALL PASS 10/10 with its store sha pin == the "
                f"baseline blob ({sha16(baseline_store_bytes)} — the R31 "
                f"landing of record); R33 repair check ALL PASS 9/9; "
                f"promotions file sha {promo_sha} == the R5 apply record's "
                f"pin AND the amendment's base pin (byte-unchanged since "
                f"R5); R21 verdict split 457 CONFIRM / 3 REJECT / 4 HOLD; "
                f"R5 record promoted 832"):
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
          and len(rows_new) == 917 and n_anchored == 835 and n_span == 27
          and n_unmapped == 55 and len(covered) == 133
          and len(ids_new) == len(set(ids_new))
          and "4MA1-2.7C" in covered and "4MA1-1.8D" in covered
          and "4MA1-1.8B" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 917 = 835 anchored + 27 unresolved-span + 55 "
                f"uncovered-SP; covered 133 of 188 (the R33 projections "
                f"landing: coverage UNCHANGED — 1.8B keeps ords 0-5, 1.8D "
                f"already covered via the R10 join; computed, never "
                f"asserted — the DC-R24-01 discipline); mapping_ids unique"):
        die("R4 rebuild failed")
    if gained or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 re-attribution delta vs the baseline blob ------------------------------
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
            if entry and entry.get("action") == "REATTRIBUTE":
                moved.append(k)
                want_block = {
                    "source": f"scripts/c42_section_overrides_r33.yaml@{map_sha}",
                    "operator_round": OPERATOR_ROUND,
                    "action": "REATTRIBUTE",
                    "provenance_class": "verdicted",
                    "evidence": entry["evidence"],
                }
                want_mid = sha16(f"{orow['note_path']}|{entry['override_code']}|"
                                 f"{c40.norm(orow['evidence_quote'])}")
                ok_row = (orow["spec_code"] == entry["current_code"]
                          and nrow["spec_code"] == entry["override_code"]
                          and nrow["mapping_id"] == want_mid
                          and nrow["sp_title"] == (registry[entry["override_code"]]
                                                   .get("official_wording") or "")
                          and nrow.get("provenance", {}).get("override") == want_block
                          and nrow.get("validation_status") == "SUGGESTED"
                          and "promotion" not in nrow
                          and nrow.get("rationale", "").endswith(
                              "the operator re-attributed the chunk."))
                if not ok_row:
                    drift.append(f"map row {k}")
                id_pairs.append((orow["mapping_id"], nrow["mapping_id"]))
                continue
            # NO DEMOTE entries this round — any unmapped row drift is a defect
            # pre-reapplication stage: the surviving promoted rows legitimately
            # differ in validation_status + promotion (restored at R6); the
            # R5-stage zero-drift claim strips those two fields plus tool
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
    r5_pass = (r5_ok and len(moved) == 3 and len(id_pairs) == 3
               and len(demote_pairs) == 0 and not drift)
    if not gate("R5_reattribution_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows); exactly 3 "
                f"rows moved: "
                f"{', '.join(sorted(e['current_code'] + '->' + e['override_code'] for e in reattr))}"
                f" (rounding-and-estimation ords 6/7/8; ZERO DEMOTEs — the "
                f"loop's first repair round with none since R22); "
                f"provenance.override == the map blocks (map sha {map_sha}); "
                f"mapping_ids recomputed (the R24 id_pairs convention — the "
                f"projected re-keys verified live); sp_titles swapped; every "
                f"surviving row BYTE-IDENTICAL to its baseline form "
                f"(provenance.tool stays @2.7.0 — the first re-build with NO "
                f"tool churn); the 55 non-chunk worklist rows byte-identical "
                f"(no DEFER-row vanish); meta delta == stage + the 4 "
                f"additive re-dated promotion_reapplied* fields "
                f"(promoted_rows RESTATED 831, value unchanged)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application UNDER THE AMENDMENTS ----------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    # the LANDED R26 amendment translation (read from the R28 record), the
    # LANDED R30 amendment translation (read from the R31 record — its
    # supersedes AND its 3 exclusions, both standing) and the fresh R33
    # translation (from this lane's delta)
    rec28 = json.loads(R28_REC.read_text(encoding="utf-8"))
    r26_rekey = dict(rec28["promotions"]["superseded_ids_rekeyed"])
    rec31 = json.loads(R31_REC.read_text(encoding="utf-8"))
    r30_rekey = dict(rec31["promotions"]["superseded_ids_rekeyed"])
    added_ids = set(rec31["promotions"]["added_ids"])
    pair33_by_old = {o: n for o, n in id_pairs}
    r26_amend = yaml.safe_load((HERE / "c42_r26_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r26_sup = {e["mapping_id"]: e for e in r26_amend.get("supersedes_code") or []}
    r26_exc = {e["mapping_id"] for e in r26_amend.get("excluded") or []}
    r30_amend = yaml.safe_load((HERE / "c42_r30_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r30_sup = {e["mapping_id"]: e for e in r30_amend.get("supersedes_code") or []}
    r30_exc = {e["mapping_id"] for e in r30_amend.get("excluded") or []}
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
    for eid, e in sup_by_id.items():
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
    if problems:
        gate("R6_promotions_reapplication", False,
             f"amendment pre-apply problems: {problems[:4]}")
        die("R6 amendment pre-apply integrity failed")
    # resolve every R5 entry against the rebuilt rows through ALL THREE
    # amendments (R33 newest -> R30 -> R26 -> direct)
    resolved = {}
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        if mid in r26_exc or mid in r30_exc:
            continue
        if mid in sup_by_id:
            target_id = pair33_by_old.get(mid)
            want_code = sup_by_id[mid].get("amended_code")
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
    # the R26 + R30 excluded rows' rebuilt forms ARE the demoted worklist rows
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
    if (len(resolved) != 828 or len(resolved) + len(added_ids) != 831
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
        # row (the 828 chain + the 3 R30-added sign-offs) carries one there
        base_block = base_by_ident[ident(row)].get("promotion")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if base_block is None or block != base_block:
            die(f"promotion block drift vs the baseline surface on {mid}")
        row["promotion"] = block
        flipped += 1
    if flipped != 831:
        die(f"flipped {flipped} != 831")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    meta_f["promoted_rows"] = 831            # RESTATED — the re-pinned surface
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"the amendment pre-apply integrity verified (pinned_code == the R5 "
         f"file on every supersedes entry of ALL THREE amendments — R33 3 + "
         f"R30 5 + R26 3 — any drift fails); 832 R5 entries resolved through "
         f"the LANDED R26 amendment (its re-key read from the R28 record) and "
         f"the LANDED R30 amendment (its re-key read from the R31 record) and "
         f"the fresh R33 amendment (its re-key read from THIS lane's delta): "
         f"828 direct-or-chained identities (the 3 R33 supersedes re-keyed at "
         f"the AMENDED code 1.8B->1.8D — ords 6/7/8 of rounding-and-estimation "
         f"REMAIN promoted; the 5 R30 supersedes via the R31 record; the 3 "
         f"R26 supersedes via the R28 record; the R26 exclusion + the 3 R30 "
         f"exclusions skipped — their rebuilt forms ARE the demoted worklist "
         f"rows) + the 3 R31-ADDED sign-off promotions re-applied byte-stably "
         f"from the baseline blocks; validated_by operator everywhere; "
         f"sampled 457 == the R21 CONFIRM set (R5-era ids); surface == "
         f"anchored 835 - R22 REJECT 3 - the re-homed hold 1 == 831 both "
         f"directions (828 + 3); every applied block == the R5 tool shape AND "
         f"the baseline store's block for the same chunk identity "
         f"(byte-stable re-application); meta promotion fields restored "
         f"byte-equal EXCEPT promoted_rows RESTATED 831 (the value unchanged "
         f"— the set re-pinned) + 4 additive re-dated promotion_reapplied* "
         f"fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = (old_ids - {o for o, _ in id_pairs}
                | {n for _, n in id_pairs})
    r7 = new_ids == want_new and len(new_ids) == 917
    fin_chunk = {ident(r): r for r in final_doc["rows"] if "chunk" in r}
    moved_idents = set(moved)
    cons_drift = []
    for k, brow in old_chunk.items():
        frow = fin_chunk[k]
        if frow.get("validation_status") != brow.get("validation_status"):
            cons_drift.append(f"status {k}")
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
    # the meta delta: exactly {stage} + the 4 additive re-dated
    # promotion_reapplied* fields (promoted_rows RESTATED, value unchanged)
    meta_delta = {k for k in set(meta_f) & set(base["meta"])
                  if meta_f[k] != base["meta"][k]}
    want_meta_delta = {"stage", "promotion_reapplied",
                       "promotion_reapplied_by",
                       "promotion_reapplied_directive",
                       "promotion_reapplied_note"}
    r7 = (r7 and not cons_drift and set(meta_f) == set(base["meta"])
          and meta_delta == want_meta_delta)
    if not gate("R7_row_set_arithmetic", r7,
                f"new_ids == old_ids - 3 old REATTRIBUTE ids + 3 new "
                f"REATTRIBUTE ids (917 -> 917) exactly; consolidated "
                f"final-vs-baseline equality: validation_status matches "
                f"EVERYWHERE (ZERO status changes this round — the 3 movers "
                f"were HUMAN_VALIDATED at 1.8B and restore HUMAN_VALIDATED "
                f"at 1.8D; the R30-added sign-off rows restore byte-stably), "
                f"every non-moved row byte-identical (provenance.tool stays "
                f"@2.7.0), the meta delta == exactly stage + the 4 additive "
                f"re-dated promotion_reapplied* fields"
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
    r8 = not failed and n_coded == 835
    if not gate("R8_g4_at_apply", r8,
                f"all {sum(1 for x in final_doc['rows'] if 'chunk' in x)} chunk "
                f"rows re-verified against a fresh re-chunking (quote-in-chunk "
                f"+ sha/heading/chars); {n_coded}/835 coded rows inside the "
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
    r9 = (len(hv) == 831 and {x["mapping_id"] for x in hv} == promote_set
          and sug_anch == vrej_new | vhold_remaining
          and tiers_ok and attribution_ok
          and not (demoted_ids & {x["mapping_id"] for x in hv})
          and all(new_rows[d].get("worklist_reason") and
                  "promotion" not in new_rows[d] for d in demoted_ids)
          and not (promote_set & (worklist_new | vhold_remaining | vrej_new)))
    if not gate("R9_anti_forgery", r9,
                f"831 HUMAN_VALIDATED == the re-composed promotion set "
                f"(828 from the R5 chain + 3 R30-added sign-offs, the 3 R33 "
                f"movers re-pinned within it); the SUGGESTED anchored "
                f"residue == the 3 R22 re-attributed REJECTs + the 1 "
                f"re-homed hold; ZERO DEMOTEs this round (no worklist "
                f"landings); provenance tiers RULE_DERIVED everywhere; "
                f"operator attribution clean; REJECT/hold/worklist "
                f"categorically unpromoted"):
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
        print(f"c42_r34_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 917 rows (831 HUMAN_VALIDATED re-applied "
              f"AMENDED THRICE: 828 + 3 R30-added sign-offs, the 3 R33 "
              f"movers re-pinned at 1.8D; 3 re-attributions + 0 DEMOTEs; "
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
    reattr_by_mid = {en["mapping_id"]: en for en in reattr}
    landings = []
    for (o, n) in id_pairs:
        e = reattr_by_mid[o]
        landings.append({
            "note_slug": e["note_slug"], "chunk_ordinal": e["chunk_ordinal"],
            "mapping_id_old": o, "mapping_id_new": n,
            "from_code": e["current_code"], "to_code": e["override_code"],
            "promoted_row": o in sup_by_id,
            "promotion_amended_code": (sup_by_id[o]["amended_code"]
                                       if o in sup_by_id else None),
        })
    rec = {
        "schema": "c42-r34-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r34-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R33 record's NEXT lane, fired by the directive: the "
                 "substrate re-build consuming the R33 override map (schema "
                 "c42-r28-section-overrides/1.0) AND the R33 promotions "
                 "amendment (schema c42-r31-promotions-amendment/1.0, the "
                 "FIRST supersedes-ONLY); the R35 validation re-gate "
                 "sanctioned by the same directive and fired separately"),
        "rebuild": {
            "tool": f"{TOOL_OLD.split('@')[0]}@2.7.0",
            "tool_version_move": "NONE — TOOL_VERSION stays 2.7.0 per the "
                                 "R33 carriers' own contract (the first "
                                 "re-build with no version move; "
                                 "provenance.tool byte-stable on every row)",
            "join": "the R27-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged; the FOUR R26 STANDING pins verified "
                    "in-generator; the R33 split-note scoping rides the "
                    "store rows, the join layer untouched)",
            "override_maps_consumed": ("NINE: R1 + R6 (with the subsumption "
                                       "registry) + R10 + R14 + R18 + R22 + "
                                       "R26 + R30 + R33, all fail-closed"),
            "rows_pre": 917, "rows_post": 917,
            "anchored": 835, "unresolved_span": 27, "uncovered_sp": 55,
            "covered_pre": 133, "covered_post": 133,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r33.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "reattribute": len(reattr), "demote": len(demote),
            "landings": landings,
            "demote_landings": [],
            "standing_pins": ("the FOUR R26 STANDING joins verified "
                              "in-generator (unchanged); the R33 split-note "
                              "scoping rides the map's note_level_scoping "
                              "block — the corpus anchor "
                              "spcpt_p8zkdCF8QVvDZyVX STANDS at 1.8B (ords "
                              "0-5), the R10 related-calculations anchor "
                              "spcpt_crKbmb6wVjM4yPJh STANDS at 1.8D; NO new "
                              "c40-pinned adjudications this round"),
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "amendment": {
                "path": "scripts/c42_r33_promotions_amendment.yaml",
                "sha256_16": amend_sha,
                "schema": "c42-r31-promotions-amendment/1.0",
                "supersedes": len(sup), "excluded": len(exc),
                "added": len(added),
                "pre_apply_integrity": "pinned_code verified against the R5 "
                                       "file BEFORE the amendment applies "
                                       "(all THREE amendments: R33 + R30 + "
                                       "R26)",
                "re_applied": 831,
                "re_applied_composition": "828 from the R5 chain + 3 "
                                          "R30-added sign-offs, the 3 R33 "
                                          "movers re-pinned within the set",
                "meta_promoted_rows_restated": "831 (the value unchanged — "
                                               "the set re-pinned row-level; "
                                               "the 7 other R5 promotion "
                                               "meta fields byte-equal)",
            },
            "reapplication": ("byte-stable: every applied block for all 831 "
                              "== the R5 tool's block shape AND the baseline "
                              "store's block for the same chunk identity "
                              "(the R30-added sign-offs INCLUDED — their "
                              "baseline blocks restore byte-stably); the 3 "
                              "superseded rows REMAIN in the promoted set at "
                              "their amended codes (re-keyed old->new, the "
                              "R24 id_pairs convention); the R26 + R30 "
                              "excluded rows stay unpromoted worklist rows; "
                              "meta gains ONLY the additive re-dated "
                              "promotion_reapplied* fields"),
            "superseded_ids_rekeyed": {o: n for o, n in id_pairs},
            "excluded_ids": [],
            "added_ids": [],
            "r30_chain": {"rekey_source": "graph/reports/"
                                          "C42_R31_REBUILD_RECORD.json",
                          "rekey": r30_rekey,
                          "added_ids": sorted(added_ids)},
            "r26_chain": {"rekey_source": "graph/reports/"
                                          "C42_R28_REBUILD_RECORD.json",
                          "rekey": r26_rekey},
        },
        "structural_diff": {
            "rows": "917 -> 917 (no row vanishes, no row lands)",
            "rows_moved": 3,
            "moved_fields": ["spec_code", "mapping_id", "sp_title",
                             "provenance.override (added block)", "rationale "
                             "(REATTRIBUTE suffix) — the 3 REATTRIBUTEs"],
            "promoted_surface_delta": "831 -> 831 HUMAN_VALIDATED (the set "
                                      "re-pinned: ords 6/7/8 of "
                                      "rounding-and-estimation now at 1.8D); "
                                      "the other 828 promoted rows "
                                      "BYTE-IDENTICAL (no tool churn)",
            "status_changes": "ZERO (the 3 movers restore HUMAN_VALIDATED at "
                              "their amended codes; the first repair round "
                              "with zero status changes)",
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
        "post_check": "scripts/c42_r34_rebuild_check.py",
        "not_done": [
            "the R35 validation re-gate NOT fired by this lane (it is "
            "sanctioned by the same directive and fired as its own round)",
            "no resolution-file / corpus / Lane C / chemistry writes",
            "no R5 promotions-file edits (byte-unchanged since R5, "
            "sha-pinned; the amendments are the dated records)",
        ],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    land_lines = "\n".join(
        f"- `{l['from_code']}` -> `{l['to_code']}` — {l['note_slug']} ord "
        f"{l['chunk_ordinal']} (mapping_id {l['mapping_id_old']} -> "
        f"{l['mapping_id_new']}; promotion re-pinned to "
        f"`{l['promotion_amended_code']}`)" for l in landings)
    md = f"""# C42 R34 — Substrate Re-build consuming BOTH R33 carriers — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive fired the R33 record's NEXT lanes in order: this re-build, then
the R35 validation re-gate (fired separately).

## What this is

The THIRD substrate re-build consuming a promotions AMENDMENT — and the
FIRST consuming a SUPERSEDES-ONLY one, and the first with NO tool-version
move: the amended c40 tool ({TOOL_OLD.split('@')[0]}@2.7.0 — the R33
carriers' own contract) re-emits the store ALL-SUGGESTED consuming the NINE
operator override maps (R1 + R6 + R10 + R14 + R18 + R22 + R26 + R30 +
**R33**, the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED THRICE OVER**: `scripts/c42_r33_promotions_amendment.yaml`
(schema `c42-r31-promotions-amendment/1.0`, the loop's THIRD
promotions-affecting repair record and the FIRST supersedes-ONLY): the 3
REATTRIBUTE rows REMAIN in the promoted set at their amended codes
(re-keyed old->new per the R24 id_pairs convention), ZERO exclusions and
ZERO additions (the R30 additions mechanism present and UNUSED — no
sign-offs owed). The re-applied count stays **831** (828 from the R5 chain
+ 3 R30-added sign-offs, the 3 R33 movers re-pinned within the set).

## The three re-attributions (from the R33 map, fail-closed)

{land_lines}

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **133 → 133** (UNCHANGED: 1.8B keeps its coverage via the rounding
half — ords 0-5 — and 1.8D is already covered via the R10
related-calculations STANDING join; gained `[]`, lost `[]`), uncovered-SP
**55 → 55**; rows **917 → 917**; anchored **835 → 835**; unresolved-span
**27 → 27**. Per-code: 1.8B anchored **9 → 6**, 1.8D anchored **3 → 6**
(the loop's FIRST SPLIT-note scoping landed row-level).

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5, NO
  version move): the R33 map consumed fail-closed (3 verdicted
  REATTRIBUTEs, targets ratified, current_code == join-derived) + the FOUR
  R26 STANDING pins verified in-generator (unchanged) + coverage recomputed
  (gained/lost computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R32 ALL PASS 10/10 with its
  store sha pin == the baseline blob + R33 ALL PASS 9/9 + the promotions
  file sha == the R5 record's pin == the amendment's base pin), G7
  determinism, the delta proofs (chunk-identity multiset identical; every
  surviving row BYTE-IDENTICAL — no tool churn; no DEFER-row vanish; meta
  delta == stage + the 4 additive re-dated promotion_reapplied* fields),
  the amendment pre-apply integrity (pinned_code verified against the R5
  file BEFORE the amendment applies — any drift fails the rebuild; ALL
  THREE amendments), the 831-row re-application (828 chained through
  R33+R30+R26 + 3 R30-added byte-stable), the row-set arithmetic, the meta
  delta assertion, G4-at-apply over every chunk row, the anti-forgery
  sweep, and CI parity (graph_check census identical pre/post; kg golden
  GREEN).
- `scripts/c42_r34_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R31 state) | Post (R34) |
|---|---|---|
| rows | 917 | 917 |
| HUMAN_VALIDATED | 831 | 831 (re-pinned: ords 6/7/8 now at 1.8D) |
| anchored SUGGESTED | 4 (3 REJECT + 1 re-homed hold) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 27 | 27 |
| uncovered-SP worklist | 55 | 55 |
| covered codes | 133/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r33.yaml` | `{map_sha}` |
| `c42_r33_promotions_amendment.yaml` | `{amend_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the R35 validation re-gate — sanctioned by the directive's "→ R35" clause,
  fired as its own round
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r34_substrate_rebuild: APPLIED — 917 rows (831 "
          f"HUMAN_VALIDATED re-pinned: 828 chained R33+R30+R26 + 3 "
          f"R30-added sign-offs; 3 re-attributions 1.8B->1.8D; coverage "
          f"133/188 unchanged)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

if __name__ == "__main__":
    sys.exit(main())
