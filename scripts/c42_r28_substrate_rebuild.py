#!/usr/bin/env python3
"""c42_r28_substrate_rebuild.py — the T-C42 R28 gated merge point: substrate
re-build consuming the R26 operator override map AND the R26 promotions
amendment (the loop's FIRST promotions-affecting re-application) over the
rebuilt store.

Fired by the operator directive "R27 join re-run + R28 rebuild consuming both
carriers" (2026-10-04, zai-web, gateway trace 1a106d1aa121ab59) naming exactly
the R26 record's next-decision menu option (a) verbatim; the R29 re-gate is
NOT fired.

The lane is the R12/R16/R20/R24 re-build precedent, now consuming BOTH R26
carriers (the R26 novelty — the first re-build under an amended promotion
surface):

  R1. pre-state pins: HEAD == the round-start baseline (the R27-closed HEAD);
      the store on disk is byte-identical to the baseline blob; the
      working-tree dirt is inside the declared R28 footprint; the baseline
      store carries the R5 promotion surface (920 rows, 832 HUMAN_VALIDATED,
      meta.promotion_record present);
  R2. the R26 map AND amendment contracts: the map schema
      c42-r28-section-overrides/1.0 with exactly 3 verdicted REATTRIBUTE
      entries (ratified targets != currents) + 1 DEMOTE_TO_WORKLIST
      (override_code null) + 4 note-level STANDING adjudications; the
      amendment schema c42-r28-promotions-amendment/1.0 with base_file ==
      the R5 promotions path, base_file_sha256_16 == the live R5 sha,
      base_file_untouched true, exactly 3 supersedes_code + 1 excluded, the
      4 ids distinct and covering exactly the map's 4 rows, pinned_code ==
      the map's current_code and amended_code == the map's override_code on
      every REATTRIBUTE row;
  R3. the promotions authority chain: the R25 regate check is still
      all_pass 13/13; the R26 repair check is ALL PASS 9/9; the live
      promotions file sha256_16 equals the sha the R5 apply record pinned
      AND the amendment's base pin (the file is byte-unchanged since R5);
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.6.0,
      the R16->R20->R24 rebuild-lane convention) constructs twice
      byte-identically, emits ALL-SUGGESTED rows, census 918 = 838 anchored
      + 24 unresolved-span + 56 uncovered-SP (covered 132 of 188 — the R26
      projections landing: gained 4MA1-1.1A + 4MA1-5.1C computed vs the
      baseline, lost none — the DC-R24-01 compute-never-assert discipline);
  R5. re-attribution + DEMOTE delta vs the baseline blob: the chunk-identity
      multiset is IDENTICAL (862 chunk rows); exactly the 4 map rows move —
      the 3 REATTRIBUTEs (old code == current_code, new code ==
      override_code, mapping_id recomputed, provenance.override == the map
      block, sp_title == the registry wording) and the DEMOTE (spec_code
      -> None, mapping_id -> demoted|note|ordinal, worklist_reason +
      disposition + provenance.override landed, chunk identity intact — the
      W3 invariant); the 2 resolved DEFER rows (1.1A / 5.1C) are the ONLY
      vanishing rows; every surviving row differs ONLY in provenance.tool
      @2.5.0 -> @2.6.0; the meta delta is exactly {stage, tool,
      sp_codes_covered, sp_codes_uncovered, rows_worklist_unmapped_sps,
      rows_anchored, rows_worklist_anchor_unresolved, upstream_store};
  R6. promotions re-application UNDER THE AMENDMENT: the R5 file's 832
      entries are resolved against the rebuilt rows — every supersedes_code
      entry re-pins one promoted row (identity by mapping_id + note_path +
      chunk_ordinal, pinned_code verified against the R5 file BEFORE the
      amendment applies — any drift fails the rebuild; the rebuilt row is
      found via the old->new id translation at the AMENDED code), the
      excluded entry is NOT re-applied (its rebuilt form is verified to be
      the demoted unresolved-span worklist row), the other 828 entries hit
      direct identities; validated_by operator everywhere (AI-name patterns
      fail closed), the sampled 457 == the R21 CONFIRM set (keyed by the
      R5-era ids), the re-applied set == anchored 838 - R22 REJECT 3 - HOLD 4
      == 831 both directions; every applied promotion block equals BOTH the
      R5 tool's block shape AND the baseline store's block for the same
      chunk identity (byte-stable re-application); the 7 non-count meta
      promotion fields are restored byte-equal to the R5 values,
      meta.promoted_rows is RESTATED 832 -> 831 (the store records its
      surface honestly — the amendment's own projection) and the meta gains
      ONLY the additive promotion_reapplied* fields;
  R7. consolidated row-set arithmetic: new_ids == old_ids - {3 old
      REATTRIBUTE ids} - {the DEMOTE old id} - {2 DEFER ids} + {3 new
      REATTRIBUTE ids} + {the demoted id} exactly (920 -> 918);
      consolidated final-vs-baseline equality: validation_status matches
      the baseline everywhere EXCEPT the enumerated DEMOTE row
      (HUMAN_VALIDATED -> SUGGESTED worklist — the DEMOTE's nature, the
      loop's first promoted-row status change); non-moved rows differ only
      in the provenance.tool string;
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk under the shared norm(), chunk sha256_16/heading/chars,
      ratified-188 registry membership for every coded row — 838 coded);
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution, REJECT/HOLD/worklist categorically unpromoted, every
      HUMAN_VALIDATED row carries a promotion block backed by the amended
      file chain, the DEMOTE row carries NO promotion block;
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R28_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r28_substrate_rebuild.py --dry-run
    python3 scripts/c42_r28_substrate_rebuild.py
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
QUAL = "igcse-maths-a"
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE = REPO / STORE_REL
MAP26 = HERE / "c42_section_overrides_r26.yaml"
AMENDMENT = HERE / "c42_r26_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R25_REGATE_CHECK.json"
REPAIR_CHECK = REPO / "graph/reports/C42_R26_REPAIR_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R28_REBUILD_RECORD.md"

TOOL = "scripts/c42_r28_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "11c2fc49299103c2aa58aad67a87ed808df97601"
DIRECTIVE = ("R27 join re-run + R28 rebuild consuming both carriers — "
             "2026-10-04, zai-web (gateway trace 1a106d1aa121ab59)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.5.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.6.0"
OPERATOR_ROUND = ("C42 R26 (surface 3: 3 verdicted REATTRIBUTEs + the "
                  "loop's fourth DEMOTE_TO_WORKLIST — the FIRST of a "
                  "promoted row)")
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
REAPPLIED_META = {
    "promotion_reapplied": "2026-10-04",
    "promotion_reapplied_by": f"{TOOL}@{VERSION}",
    "promotion_reapplied_directive": DIRECTIVE,
    "promotion_reapplied_note": (
        "re-applied byte-stably over the R28 substrate re-build (the c40 "
        "tool emits all-SUGGESTED) AMENDED by "
        "scripts/c42_r26_promotions_amendment.yaml (schema "
        "c42-r28-promotions-amendment/1.0, the loop's FIRST "
        "promotions-affecting repair record: 3 code supersedes re-keyed "
        "old->new + 1 exclusion — the DEMOTE row lands unresolved-span; "
        "832 -> 831, the R5 file byte-untouched per the P5 convention); "
        "meta.promoted_rows is RESTATED 832 -> 831 to match the re-applied "
        "surface (the 7 other R5 promotion meta fields byte-equal); see "
        "graph/reports/C42_R28_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R28 substrate re-build (2026-10-04, consuming the R26 operator "
    "override map: 1.1G->1.1A / 5.1D->5.1C / 3.3F->3.3H + the loop's fourth "
    "DEMOTE (factorising-by-grouping ord 2, the FIRST of a promoted row) AND "
    "the R26 promotions amendment (3 code supersedes + 1 exclusion)): the R5 "
    "§18 promotion surface re-applied AMENDED — 831 rows HUMAN_VALIDATED at "
    "the amended codes; 3 R22 REJECT rows stay SUGGESTED; 4 H3 HOLD rows "
    "stay SUGGESTED; the DEMOTE row lands unresolved-span; coverage "
    "132/188 (gained 1.1A + 5.1C).\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r28_substrate_rebuild.py",
    "scripts/c42_r28_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R28_REBUILD_RECORD.json",
    "graph/reports/C42_R28_REBUILD_RECORD.md",
    "graph/reports/C42_R28_REBUILD_CHECK.json",
}

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"pass": bool(ok), "detail": detail}
    print(f"  {name}: {'PASS' if ok else 'FAIL'} — {detail[:900]}")
    return bool(ok)


def die(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def git(*args) -> str:
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, text=True, check=True).stdout


def blob_at(commit: str, rel: str) -> bytes:
    return subprocess.run(
        ["git", "-C", str(REPO), "show", f"{commit}:{rel}"],
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

    print("C42 R28 SUBSTRATE REBUILD — gated lane (both R26 carriers)")
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40          # amended @2.6.0
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
          and len(base["rows"]) == 920 and len(base_anchored) == 839
          and len(base_hv) == 832
          and base["meta"].get("promotion_record") == "scripts/c42_r5_promotions.yaml")
    if not gate("R1_pre_state", r1,
                f"HEAD {head[:12]} == baseline {BASELINE[:12]}; disk store == "
                f"baseline blob; dirty {len(dirty)} within the R28 footprint; "
                f"baseline census 920 = 839 anchored (832 HUMAN_VALIDATED) + "
                f"81 worklist; R5 promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.6.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R26 map AND amendment contracts --------------------------------
    map_bytes = MAP26.read_bytes()
    map_sha = sha16(map_bytes)
    map_doc = yaml.safe_load(map_bytes.decode("utf-8"))
    registry = c40.load_registry()
    entries = map_doc.get("overrides") or []
    adj = map_doc.get("note_level_adjudications") or []
    reattr = [e for e in entries if e.get("action") == "REATTRIBUTE"]
    demote = [e for e in entries if e.get("action") == "DEMOTE_TO_WORKLIST"]
    amend_bytes = AMENDMENT.read_bytes()
    amend_sha = sha16(amend_bytes)
    amend = yaml.safe_load(amend_bytes.decode("utf-8"))
    promo_sha = sha16(PROMOTIONS.read_bytes())
    sup = amend.get("supersedes_code") or []
    exc = amend.get("excluded") or []
    sup_by_id = {e.get("mapping_id"): e for e in sup}
    exc_by_id = {e.get("mapping_id"): e for e in exc}
    r2 = (map_doc.get("schema") == "c42-r28-section-overrides/1.0"
          and map_doc.get("round") == "R26"
          and len(entries) == 4 and len(reattr) == 3 and len(demote) == 1
          and len(adj) == 4
          and all(e.get("action") == "REATTRIBUTE"
                  and e.get("provenance_class") == "verdicted"
                  and e.get("override_code") in registry
                  and e.get("override_code") != e.get("current_code")
                  for e in reattr)
          and all(e.get("action") == "DEMOTE_TO_WORKLIST"
                  and e.get("override_code") is None for e in demote)
          and all(a.get("ruling") == "STANDING" for a in adj)
          and amend.get("schema") == "c42-r28-promotions-amendment/1.0"
          and amend.get("round") == "R26"
          and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
          and amend.get("base_file_sha256_16") == promo_sha
          and amend.get("base_file_untouched") is True
          and len(sup) == 3 and len(exc) == 1
          and len(set(sup_by_id) | set(exc_by_id)) == 4
          and {e.get("mapping_id") for e in entries} ==
              set(sup_by_id) | set(exc_by_id)
          and all(sup_by_id[e["mapping_id"]].get("pinned_code") ==
                  e.get("current_code")
                  and sup_by_id[e["mapping_id"]].get("amended_code") ==
                  e.get("override_code")
                  for e in reattr)
          and all(exc_by_id[e["mapping_id"]].get("pinned_code") ==
                  e.get("current_code")
                  and exc_by_id[e["mapping_id"]].get("disposition") ==
                  "DEMOTE_TO_WORKLIST"
                  for e in demote))
    if not gate("R2_map_and_amendment_contracts", r2,
                f"map schema c42-r28-section-overrides/1.0; 3 verdicted "
                f"REATTRIBUTEs with ratified targets != currents "
                f"({', '.join(e['current_code'] + '->' + e['override_code'] for e in reattr)})"
                f" + 1 DEMOTE (override_code null); 4 note-level STANDING "
                f"adjudications; amendment schema "
                f"c42-r28-promotions-amendment/1.0 with base sha "
                f"{amend.get('base_file_sha256_16')} == the live R5 sha, 3 "
                f"supersedes (amended_code == override_code) + 1 excluded "
                f"DEMOTE, the 4 ids covering exactly the map's rows; map sha "
                f"{map_sha}, amendment sha {amend_sha}"):
        die("R2 map/amendment contracts failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check25 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    check26 = json.loads(REPAIR_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check25.get("all_pass") is True and check25.get("passed") == 13
          and check26.get("result") == "ALL PASS" and check26.get("passed") == 9
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R25 regate all_pass 13/13; R26 repair check ALL PASS 9/9; "
                f"promotions file sha {promo_sha} == the R5 apply record's "
                f"pin AND the amendment's base pin (byte-unchanged since R5); "
                f"R21 verdict split 457 CONFIRM / 3 REJECT / 4 HOLD; R5 "
                f"record promoted 832"):
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
          and len(rows_new) == 918 and n_anchored == 838 and n_span == 24
          and n_unmapped == 56 and len(covered) == 132
          and len(ids_new) == len(set(ids_new))
          and "4MA1-1.1A" in covered and "4MA1-5.1C" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 918 = 838 anchored + 24 unresolved-span + 56 "
                f"uncovered-SP; covered 132 of 188 (the R26 projections "
                f"landing: gained 4MA1-1.1A + 4MA1-5.1C — both DEFER rows "
                f"resolved; computed, never asserted — the DC-R24-01 "
                f"discipline); mapping_ids unique"):
        die("R4 rebuild failed")
    if gained != ["4MA1-1.1A", "4MA1-5.1C"] or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 re-attribution + DEMOTE delta vs the baseline blob ---------------------
    old_chunk = {ident(r): r for r in base["rows"] if "chunk" in r}
    new_chunk = {ident(r): r for r in rows_new if "chunk" in r}
    r5_ok = (set(old_chunk) == set(new_chunk) and len(old_chunk) == 862
             and len(set(old_chunk)) == 862)
    moved, id_pairs, demote_pair, drift = [], [], None, []
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
                    "source": f"scripts/c42_section_overrides_r26.yaml@{map_sha}",
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
            if entry and entry.get("action") == "DEMOTE_TO_WORKLIST":
                moved.append(k)
                want_block = {
                    "source": f"scripts/c42_section_overrides_r26.yaml@{map_sha}",
                    "operator_round": OPERATOR_ROUND,
                    "action": "DEMOTE_TO_WORKLIST",
                    "evidence": entry["evidence"],
                }
                want_did = sha16(f"demoted|{orow['note_path']}|"
                                 f"{orow['chunk']['ordinal']}")
                ok_row = (orow["spec_code"] == entry["current_code"]
                          and nrow.get("spec_code") is None
                          and nrow["mapping_id"] == want_did
                          and "sp_title" not in nrow and "anchor" not in nrow
                          and nrow.get("provenance", {}).get("override") == want_block
                          and (nrow.get("worklist_reason") or "").startswith(
                              "DEMOTE_TO_WORKLIST per the C42 R26")
                          and "(C42 R26 surface 3 demote)" in (nrow.get("disposition") or "")
                          and nrow.get("validation_status") == "SUGGESTED"
                          and "promotion" not in nrow
                          and nrow["chunk"] == orow["chunk"])
                if not ok_row:
                    drift.append(f"demote row {k}")
                demote_pair = (orow["mapping_id"], nrow["mapping_id"])
                continue
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
        # non-chunk rows (the unmapped-SP worklist only — the unresolved-span
        # rows DO carry chunk blocks and were covered above): the 1.1A and
        # 5.1C DEFER rows vanish; survivors tool-only
        old_nc = [r for r in base["rows"] if "chunk" not in r]
        new_nc = [r for r in rows_new if "chunk" not in r]
        defer_ids = {sha16("unmapped|4MA1-1.1A"), sha16("unmapped|4MA1-5.1C")}
        vanished = [r for r in old_nc if r["mapping_id"] not in
                    {x["mapping_id"] for x in new_nc}]
        if not (len(old_nc) == 58 and len(new_nc) == 56
                and len(vanished) == 2
                and {r["mapping_id"] for r in vanished} == defer_ids
                and {r.get("spec_code") for r in vanished} ==
                    {"4MA1-1.1A", "4MA1-5.1C"}):
            drift.append("defer-row vanish shape")
        else:
            new_by_id = {r["mapping_id"]: r for r in new_nc}
            for orow in old_nc:
                nrow = new_by_id.get(orow["mapping_id"])
                if nrow is None:
                    continue
                if strip_tool(orow) != strip_tool(nrow) or \
                        orow["provenance"]["tool"] != TOOL_OLD or \
                        nrow["provenance"]["tool"] != TOOL_NEW:
                    drift.append(f"nonchunk {orow['mapping_id']}")
        om, nm = base["meta"], meta_new
        common = set(om) & set(nm)
        meta_diff = {k for k in common if om[k] != nm[k]}
        census_ok = (nm.get("sp_codes_covered") == 132
                     and nm.get("sp_codes_uncovered") == sorted(
                         set(registry) - covered)
                     and "4MA1-1.1A" not in nm.get("sp_codes_uncovered", [])
                     and "4MA1-5.1C" not in nm.get("sp_codes_uncovered", [])
                     and om.get("sp_codes_covered") == 130
                     and "4MA1-1.1A" in om.get("sp_codes_uncovered", [])
                     and "4MA1-5.1C" in om.get("sp_codes_uncovered", [])
                     and nm.get("rows_worklist_unmapped_sps") == 56
                     and om.get("rows_worklist_unmapped_sps") == 58
                     and nm.get("rows_anchored") == 838
                     and om.get("rows_anchored") == 839
                     and nm.get("rows_worklist_anchor_unresolved") == 24
                     and om.get("rows_worklist_anchor_unresolved") == 23)
        if set(om) - set(nm) != (PROMO_META_KEYS | set(REAPPLIED_META)) \
                or meta_diff != {"stage", "tool", "sp_codes_covered",
                                 "sp_codes_uncovered",
                                 "rows_worklist_unmapped_sps",
                                 "rows_anchored",
                                 "rows_worklist_anchor_unresolved",
                                 "upstream_store"} \
                or not census_ok \
                or "re-run at R27 with" not in nm.get("upstream_store", ""):
            drift.append(f"meta delta {sorted(meta_diff)} / missing "
                         f"{sorted(set(om) - set(nm))[:3]} / census_ok "
                         f"{census_ok}")
    r5_pass = (r5_ok and len(moved) == 4 and len(id_pairs) == 3
               and demote_pair is not None and not drift)
    if not gate("R5_reattribution_demote_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows); exactly 4 rows "
                f"moved: {', '.join(e['current_code'] + '->' + e['override_code'] for e in reattr)}"
                f" + the DEMOTE (2.2F -> unresolved-span, demoted id "
                f"{demote_pair[1] if demote_pair else '?'}); "
                f"provenance.override == the map blocks; mapping_ids "
                f"recomputed; sp_titles swapped; all other rows differ ONLY in "
                f"provenance.tool {TOOL_OLD.split('@')[1]} -> "
                f"{TOOL_NEW.split('@')[1]}; the 4MA1-1.1A + 4MA1-5.1C DEFER "
                f"rows are the only vanishing rows; meta delta == "
                f"stage+tool+census keys (the R26 projections landing "
                f"130->132 / 58->56 / 839->838 / 23->24)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application UNDER THE AMENDMENT ----------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    pair_by_old = {o: n for o, n in id_pairs}
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
            problems.append(f"amendment supersedes {eid} drift vs the R5 file")
    for eid, e in exc_by_id.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
            problems.append(f"amendment excluded {eid} drift vs the R5 file")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"amendment pre-apply problems: {problems[:4]}")
        die("R6 amendment pre-apply integrity failed")
    # resolve every R5 entry against the rebuilt rows (re-key supersedes,
    # skip the exclusion)
    resolved = {}
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        if mid in exc_by_id:
            continue
        if mid in sup_by_id:
            target_id = pair_by_old.get(mid)
            want_code = sup_by_id[mid].get("amended_code")
            if target_id is None:
                problems.append(f"{where} no old->new translation")
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
    # the excluded row's rebuilt form IS the demoted worklist row
    exc_old_id = next(iter(exc_by_id))
    if demote_pair[0] != exc_old_id:
        problems.append("the excluded id is not the DEMOTE row's old id")
    elif new_rows.get(demote_pair[1], {}).get("worklist_reason") is None \
            or new_rows[demote_pair[1]].get("validation_status") != "SUGGESTED" \
            or "promotion" in new_rows[demote_pair[1]]:
        problems.append("the excluded row's rebuilt form is not the demoted "
                        "unresolved-span worklist row")
    # surface arithmetic
    new_rows_by_ident = {ident(r): r for r in rows_new if "chunk" in r}
    # the R22 REJECT rows: re-attributed at R22/R24 — they sit at their
    # R24-era ids in BOTH the baseline and this build; the R21-era verdict
    # ids are cross-checked against the R22 map's would-be pre-R22 ids (the
    # R24 gate's old_reject_ids == vrej convention, reproduced here)
    ov22 = yaml.safe_load((HERE / "c42_section_overrides_r22.yaml")
                          .read_text(encoding="utf-8"))
    keyed_new = {(rw.get("note_slug"),
                  (rw.get("chunk") or {}).get("ordinal")): rw
                 for rw in rows_new if "chunk" in rw}
    keyed_base = {(rw.get("note_slug"),
                   (rw.get("chunk") or {}).get("ordinal")): rw
                  for rw in base["rows"] if "chunk" in rw}
    vrej_new, vrej_old_check = set(), set()
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
    vhold_new = set()
    for mid in vhold:
        brow = base_rows[mid]
        nrow = new_rows_by_ident[ident(brow)]
        vhold_new.add(nrow["mapping_id"])
        if nrow["spec_code"] != brow["spec_code"]:
            problems.append(f"hold row moved {mid}")
    anchored_new = {r["mapping_id"] for r in rows_new
                    if r.get("spec_code") and "chunk" in r}
    promote_set = anchored_new - vrej_new - vhold_new
    worklist_new = {r["mapping_id"] for r in rows_new
                    if r.get("worklist_reason")}
    if (len(resolved) != 831 or set(resolved) != promote_set
            or n_sampled != 457
            or promote_set & (vrej_new | vhold_new | worklist_new)):
        problems.append(f"round contract: resolved {len(resolved)} vs surface "
                        f"{len(promote_set)}; sampled {n_sampled}")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"problems: {problems[:4]}")
        die("R6 promotions re-application failed")
    # flip + byte-stable blocks
    final_doc = yaml.safe_load(dump_a)  # fresh parse; rows are fresh dicts
    flipped = 0
    for row in final_doc["rows"]:
        mid = row["mapping_id"]
        if mid not in promote_set:
            continue
        old_mid, _want_code = resolved[mid]
        base_block = base_rows[old_mid].get("promotion") \
            if old_mid in base_rows else None
        if "promotion" in row or row.get("validation_status") != "SUGGESTED":
            die(f"row {mid} pre-poisoned — refusing")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if block != base_block:
            die(f"promotion block drift vs the R5 surface on {mid} "
                f"(via {old_mid})")
        row["promotion"] = block
        flipped += 1
    if flipped != 831:
        die(f"flipped {flipped} != 831")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    meta_f["promoted_rows"] = 831            # RESTATED — the amended surface
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"the amendment pre-apply integrity verified (pinned_code == the R5 "
         f"file on every supersedes/excluded entry — any drift fails); 832 "
         f"entries resolved: 828 direct identities + 3 superseded re-keyed "
         f"old->new at the AMENDED codes (1.1G->1.1A / 5.1D->5.1C / "
         f"3.3F->3.3H) + 1 excluded (the DEMOTE row, verified landed "
         f"unresolved-span, NOT re-promoted); validated_by operator "
         f"everywhere; sampled 457 == the R21 CONFIRM set (R5-era ids); "
         f"surface == anchored 838 - R22 REJECT 3 - HOLD 4 == 831 both "
         f"directions; every applied block == the R5 tool shape AND the "
         f"baseline store's block (byte-stable re-application); meta "
         f"promotion fields restored byte-equal EXCEPT promoted_rows "
         f"RESTATED 832 -> 831 + 4 additive promotion_reapplied* fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = (old_ids - {o for o, _ in id_pairs} - {demote_pair[0]}
                - {sha16("unmapped|4MA1-1.1A"), sha16("unmapped|4MA1-5.1C")}
                | {n for _, n in id_pairs} | {demote_pair[1]})
    r7 = new_ids == want_new and len(new_ids) == 918
    fin_chunk = {ident(r): r for r in final_doc["rows"] if "chunk" in r}
    moved_idents = set(moved)
    demote_ident = next(k for k in old_chunk
                        if old_chunk[k]["mapping_id"] == demote_pair[0])
    cons_drift = []
    for k, brow in old_chunk.items():
        frow = fin_chunk[k]
        if k == demote_ident:
            # the DEMOTE row: the enumerated status change (HV -> SUGGESTED
            # worklist) IS the round's action
            if frow.get("validation_status") != "SUGGESTED" or \
                    "promotion" in frow or frow.get("spec_code") is not None:
                cons_drift.append(f"demote final shape {k}")
            continue
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
    r7 = r7 and not cons_drift
    if not gate("R7_row_set_arithmetic", r7,
                f"new_ids == old_ids - 3 old REATTRIBUTE ids - the DEMOTE old "
                f"id - 2 DEFER ids + 3 new REATTRIBUTE ids + the demoted id "
                f"(920 -> 918) exactly; consolidated final-vs-baseline "
                f"equality: validation_status matches everywhere EXCEPT the "
                f"enumerated DEMOTE row (HUMAN_VALIDATED -> SUGGESTED "
                f"worklist — the loop's first promoted-row status change), "
                f"the only non-moved delta is the provenance.tool string, "
                f"the 4 moved rows carry exactly the enumerated fields"
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
    r8 = not failed and n_coded == 838
    if not gate("R8_g4_at_apply", r8,
                f"all {sum(1 for x in final_doc['rows'] if 'chunk' in x)} chunk "
                f"rows re-verified against a fresh re-chunking (quote-in-chunk "
                f"+ sha/heading/chars); {n_coded}/838 coded rows inside the "
                f"ratified 188" + (f"; FAIL {failed[:3]}" if failed else "")):
        die("R8 G4-at-apply failed")

    # ---- R9 anti-forgery sweep ------------------------------------------------------------
    hv = [x for x in final_doc["rows"]
          if x.get("validation_status") == "HUMAN_VALIDATED"]
    sug_anch = {x["mapping_id"] for x in final_doc["rows"]
                if x.get("chunk") and x.get("spec_code")
                and x.get("validation_status") == "SUGGESTED"}
    demoted_row = new_rows[demote_pair[1]]
    tiers_ok = all(x.get("provenance", {}).get("tier") == "RULE_DERIVED"
                   for x in final_doc["rows"])
    attribution_ok = all(
        x["promotion"]["promoted_by"] == "operator"
        and not r5.AI_PAT.search(json.dumps(x["promotion"]))
        for x in hv)
    r9 = (len(hv) == 831 and {x["mapping_id"] for x in hv} == promote_set
          and sug_anch == vrej_new | vhold_new
          and tiers_ok and attribution_ok
          and "promotion" not in demoted_row
          and demoted_row.get("worklist_reason")
          and not (promote_set & (worklist_new | vhold_new | vrej_new)))
    if not gate("R9_anti_forgery", r9,
                f"831 HUMAN_VALIDATED == the amended promotion set; the "
                f"SUGGESTED anchored residue == the 3 R22 re-attributed "
                f"REJECTs + the 4 H3 HOLDs; the DEMOTE row carries NO "
                f"promotion block (unresolved-span worklist); provenance "
                f"tiers RULE_DERIVED everywhere; operator attribution clean; "
                f"REJECT/HOLD/worklist categorically unpromoted"):
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
        print(f"c42_r28_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 918 rows (831 HUMAN_VALIDATED re-applied "
              f"AMENDED; 3 re-attributions + 1 DEMOTE; coverage 132/188); "
              f"no files written")
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
    landings = []
    for (o, n) in id_pairs:
        e = next(en for en in reattr
                 if en["current_code"] == base_rows[o]["spec_code"])
        landings.append({
            "note_slug": e["note_slug"], "chunk_ordinal": e["chunk_ordinal"],
            "mapping_id_old": o, "mapping_id_new": n,
            "from_code": e["current_code"], "to_code": e["override_code"],
            "promotion_amended_code": sup_by_id[o]["amended_code"],
        })
    rec = {
        "schema": "c42-r28-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r28-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R26 record's next-decision menu option (a): the "
                 "substrate re-build consuming the R26 override map (schema "
                 "c42-r28-section-overrides/1.0) AND the R26 promotions "
                 "amendment (schema c42-r28-promotions-amendment/1.0); the "
                 "R29 re-gate NOT fired"),
        "rebuild": {
            "tool": f"{C40_TOOL}@{c40.TOOL_VERSION}",
            "tool_version_move": "2.5.0 -> 2.6.0 (the R16->R20->R24 "
                                 "rebuild-lane convention; provenance.tool "
                                 "moves on every row — the store records its "
                                 "builder)",
            "join": "the R27-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged; the FOUR R26 STANDING pins verified "
                    "in-generator)",
            "override_maps_consumed": ("SEVEN: R1 + R6 (with the subsumption "
                                       "registry) + R10 + R14 + R18 + R22 + "
                                       "R26, all fail-closed"),
            "rows_pre": 920, "rows_post": 918,
            "anchored": 838, "unresolved_span": 24, "uncovered_sp_pre": 58,
            "uncovered_sp_post": 56,
            "covered_pre": 130, "covered_post": 132,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r26.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "reattribute": len(reattr), "demote": len(demote),
            "landings": landings,
            "demote_landing": {
                "note_slug": demote[0]["note_slug"],
                "chunk_ordinal": demote[0]["chunk_ordinal"],
                "mapping_id_old": demote_pair[0],
                "mapping_id_new": demote_pair[1],
                "from_code": demote[0]["current_code"],
                "to": "unresolved-span worklist (the c40 DEMOTE convention; "
                      "chunk identity intact — the W3 invariant)",
            },
            "standing_pins": [f"{a['note_slug']} -> {a['joined_code']} on "
                              f"{a['anchor_id']}" for a in adj],
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "amendment": {
                "path": "scripts/c42_r26_promotions_amendment.yaml",
                "sha256_16": amend_sha,
                "schema": "c42-r28-promotions-amendment/1.0",
                "supersedes": len(sup), "excluded": len(exc),
                "pre_apply_integrity": "pinned_code verified against the R5 "
                                       "file BEFORE the amendment applies",
                "re_applied": 831,
                "meta_promoted_rows_restated": "832 -> 831 (the 7 other R5 "
                                               "promotion meta fields "
                                               "byte-equal)",
            },
            "reapplication": ("byte-stable: every applied block == the R5 "
                              "tool's block shape AND the baseline store's "
                              "block for the same chunk identity (831/831); "
                              "the 3 superseded rows REMAIN in the promoted "
                              "set at their amended codes (re-keyed "
                              "old->new); the DEMOTE row leaves the promoted "
                              "set entirely; meta gains ONLY the additive "
                              "promotion_reapplied* fields"),
            "superseded_ids_rekeyed": {o: n for o, n in id_pairs},
            "excluded_id": demote_pair[0],
        },
        "structural_diff": {
            "rows": "920 -> 918 (the 2 resolving DEFER rows: 1.1A + 5.1C)",
            "rows_moved": 4,
            "moved_fields": ["spec_code", "mapping_id", "sp_title",
                             "provenance.override (added block)", "rationale "
                             "(REATTRIBUTE suffix) — the 3 REATTRIBUTEs; "
                             "spec_code -> None, mapping_id -> demoted|…, "
                             "worklist_reason + disposition added, sp_title/"
                             "anchor popped — the DEMOTE"],
            "promoted_surface_delta": "832 -> 831 HUMAN_VALIDATED (the "
                                      "amendment); the 3 superseded rows "
                                      "re-keyed at the amended codes; the "
                                      "other 828 differ ONLY in the "
                                      f"provenance.tool string "
                                      f"({TOOL_OLD} -> {TOOL_NEW})",
            "status_changes": "exactly 1: the DEMOTE row HUMAN_VALIDATED -> "
                              "SUGGESTED (worklist) — the loop's first "
                              "promoted-row status change, enumerated",
            "header_delta": "status line re-dated (line 3), lines 1-2 verbatim",
        },
        "store_sha256_16_pre": sha16(baseline_store_bytes),
        "store_sha256_16_post": sha16(new_text.encode("utf-8")),
        "ci_parity": {
            "graph_check": "failure census identical pre/post (pre-existing "
                           "sparse-checkout environmental set)",
            "kg_export": "kg_export --verify-golden GREEN on the rebuilt "
                         "state",
        },
        "post_check": "scripts/c42_r28_rebuild_check.py",
        "not_done": [
            "the R29 re-gate NOT fired (explicit operator instruction only)",
            "the 4 H3 HOLD rows untouched (per-row operator sign-off owed)",
            "the ord-3 promoted-surface extension candidate NOT adjudicated "
            "(operator-level decision; the promotions file pins the row)",
            "the promoted-surface same-class candidates (grouping ords 0/1/3, "
            "drawing ord 5, vectors ord 4) NOT adjudicated — operator census "
            "remarks per the R26 record",
            "the rational/irrational corpus gap NOT adjudicated — operator "
            "decision",
            "no resolution-file / corpus / Lane C / chemistry writes",
            "no R5 promotions-file edits (byte-unchanged since R5, "
            "sha-pinned; the amendment is the dated record)",
        ],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    land_lines = "\n".join(
        f"- `{l['from_code']}` -> `{l['to_code']}` — {l['note_slug']} ord "
        f"{l['chunk_ordinal']} (mapping_id {l['mapping_id_old']} -> "
        f"{l['mapping_id_new']}; promotion re-pinned to "
        f"`{l['promotion_amended_code']}`)" for l in landings)
    demote_l = demote[0]
    md = f"""# C42 R28 — Substrate Re-build consuming BOTH R26 carriers — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive names exactly the R26 record's next-decision menu option (a);
**the R29 re-gate is NOT fired**.

## What this is

The first substrate re-build consuming a promotions AMENDMENT (the R26
novelty): the amended c40 tool ({C40_TOOL}@2.6.0 — the R16→R20→R24
rebuild-lane version convention) re-emits the store ALL-SUGGESTED consuming
the SEVEN operator override maps (R1 + R6 + R10 + R14 + R18 + R22 +
**R26**, the new one, schema `c42-r28-section-overrides/1.0`), and the R5
promotions file (832 exact row identities, byte-untouched per the P5
convention) is re-applied **AMENDED** by `scripts/c42_r26_promotions_amendment.yaml`
(schema `c42-r28-promotions-amendment/1.0`, the loop's FIRST
promotions-affecting repair record): the 3 REATTRIBUTE rows REMAIN in the
promoted set at their amended codes (re-keyed old→new), the DEMOTE row LEAVES
it (832 → 831) and lands unresolved-span. Every applied block is byte-stable
against both the R5 tool shape and the baseline store's block.

## The three re-attributions + the DEMOTE (from the R26 map, fail-closed)

{land_lines}
- `4MA1-2.2F` -> unresolved-span — {demote_l['note_slug']} ord
  {demote_l['chunk_ordinal']} (mapping_id {demote_pair[0]} ->
  {demote_pair[1]}; the loop's fourth DEMOTE and the FIRST of a PROMOTED row;
  its promotion is EXCLUDED by the amendment — the status change
  HUMAN_VALIDATED → SUGGESTED is enumerated and recorded)

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **130 → 132** (gained `['4MA1-1.1A', '4MA1-5.1C']` — both DEFER rows
`da25da48e0be5c64` / `2332964a4f1b02ca` resolving into anchored rows, the
R12/R16/R20/R24 coverage-gain precedent), lost `[]` (1.1G keeps 7, 5.1D keeps
4, 3.3F keeps 6, 2.2F keeps 17 — verified row-by-row at R26); uncovered-SP
**58 → 56**; rows **920 → 918**; anchored **839 → 838**; unresolved-span
**23 → 24**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.6.0 (amended per P5): the
  R26 map consumed fail-closed (3 verdicted REATTRIBUTEs + 1 DEMOTE, targets
  ratified, current_code == join-derived) + the FOUR R26 STANDING pins
  verified in-generator (list-shaped adjudications, the R24 R22-pins
  precedent) + coverage recomputed (gained/lost computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R25 all_pass 13/13 + R26 ALL
  PASS 9/9 + the promotions file sha == the R5 record's pin == the
  amendment's base pin), G7 determinism, the delta proofs (chunk-identity
  multiset identical; tool-string-only churn elsewhere; the DEFER-row vanish
  shape; meta delta == stage+tool+census keys), the amendment pre-apply
  integrity (pinned_code verified against the R5 file BEFORE the amendment
  applies — any drift fails the rebuild), the 831-row byte-stable
  re-application with the 3 supersedes re-keyed, the row-set arithmetic,
  G4-at-apply over every chunk row, the anti-forgery sweep, and CI parity
  (graph_check census identical pre/post; kg golden GREEN).
- `scripts/c42_r28_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R26 state) | Post (R28) |
|---|---|---|
| rows | 920 | 918 |
| HUMAN_VALIDATED | 832 | 831 (re-applied AMENDED byte-stably) |
| anchored SUGGESTED | 7 (3 REJECT + 4 HOLD) | 7 (3 REJECT + 4 HOLD) |
| unresolved-span worklist | 23 | 24 (the DEMOTE row lands) |
| uncovered-SP worklist | 58 | 56 (1.1A + 5.1C resolved) |
| covered codes | 130/188 | 132/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r26.yaml` | `{map_sha}` |
| `c42_r26_promotions_amendment.yaml` | `{amend_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the R29 re-gate (explicit instruction only)
- the 4 H3 HOLD rows (per-row sign-off owed: 1.7B / 6.3J / 3.3F / 2.2C)
- the ord-3 promoted-surface extension candidate (3d-pythagoras SOHCAHTOA-3D)
- the promoted-surface same-class candidates (grouping ords 0/1/3, drawing
  ord 5, vectors ord 4) + the rational/irrational corpus gap — operator
  census remarks per the R26 record
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r28_substrate_rebuild: APPLIED — 918 rows (831 "
          f"HUMAN_VALIDATED re-applied AMENDED byte-stably; 3 "
          f"re-attributions + 1 DEMOTE; coverage 132/188)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
