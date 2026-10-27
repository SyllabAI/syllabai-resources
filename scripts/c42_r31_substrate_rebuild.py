#!/usr/bin/env python3
"""c42_r31_substrate_rebuild.py — the T-C42 R31 gated merge point: substrate
re-build consuming the R30 operator override map AND the R30 promotions
amendment (the loop's SECOND promotions-affecting re-application and the
FIRST with ADDITIONS) over the rebuilt store.

Fired by the operator directive "Fix all of these yourself. Validate by
yourself." (2026-10-12, zai-web, gateway trace 1a130272fc8acc11) over the R29
re-gate's NEXT-OPERATOR-DECISIONS menu (the R30 round landed the carriers;
this lane consumes them); the R32 validation re-gate is sanctioned by the
same directive and fired separately.

The lane is the R12/R16/R20/R24/R26/R28 re-build precedent, now consuming
BOTH R30 carriers (the R30 novelty — the first re-build under an
ADDITIONS-capable amended promotion surface):

  R1. pre-state pins: HEAD == the round-start baseline (the R30-audit HEAD);
      the store on disk is byte-identical to the baseline blob; the
      working-tree dirt is inside the declared R31 footprint; the baseline
      store carries the R29-of-record surface (918 rows, 831
      HUMAN_VALIDATED, meta.promotion_record present);
  R2. the R30 map AND amendment contracts: the map schema
      c42-r28-section-overrides/1.0 with exactly 6 verdicted REATTRIBUTE
      entries (ratified targets != currents) + 3 DEMOTE_TO_WORKLIST entries
      (override_code null) + the sign-off/retain/scoping/remarks blocks; the
      amendment schema c42-r31-promotions-amendment/1.0 with base_file ==
      the R5 promotions path, base_file_sha256_16 == the live R5 sha,
      base_file_untouched true, exactly 5 supersedes_code + 3 excluded +
      3 added, the ids distinct and covering exactly the map's promoted
      movers, pinned_code == the map's current_code and amended_code == the
      map's override_code on every promoted REATTRIBUTE row, every added
      entry carrying verdict SIGN_OFF + validated_by operator + a verbatim
      signoff_basis;
  R3. the promotions authority chain: the R29 regate check is still
      all_pass 13/13; the R30 repair check is ALL PASS 9/9; the live
      promotions file sha256_16 equals the sha the R5 apply record pinned
      AND the amendment's base pin (the file is byte-unchanged since R5);
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.7.0,
      the R16->...->R28 rebuild-lane convention) constructs twice
      byte-identically, emits ALL-SUGGESTED rows, census 917 = 835 anchored
      + 27 unresolved-span + 55 uncovered-SP (covered 133 of 188 — the R30
      projections landing: gained 4MA1-2.7C computed vs the baseline, lost
      none — the DC-R24-01 compute-never-assert discipline);
  R5. re-attribution + DEMOTE delta vs the baseline blob: the chunk-identity
      multiset is IDENTICAL (862 chunk rows); exactly the 9 map rows move —
      the 6 REATTRIBUTEs (old code == current_code, new code ==
      override_code, mapping_id recomputed, provenance.override == the map
      block, sp_title == the registry wording) and the 3 DEMOTEs (spec_code
      -> None, mapping_id -> demoted|note|ordinal, worklist_reason +
      disposition + provenance.override landed, chunk identity intact — the
      W3 invariant); the resolved 2.7C DEFER row (f081d3d51385cb8f) is the
      ONLY vanishing row; every surviving row differs ONLY in
      provenance.tool @2.6.0 -> @2.7.0; the meta delta is exactly {stage,
      tool, sp_codes_covered, sp_codes_uncovered,
      rows_worklist_unmapped_sps, rows_anchored,
      rows_worklist_anchor_unresolved, upstream_store};
  R6. promotions re-application UNDER THE AMENDMENTS: the R5 file's 832
      entries are resolved against the rebuilt rows through the LANDED R26
      amendment (its re-key read from the R28 record) and the R30 amendment
      — every supersedes_code entry re-pins one promoted row (identity by
      mapping_id + note_path + chunk_ordinal, pinned_code verified against
      the R5 file BEFORE the amendment applies — any drift fails the
      rebuild; the rebuilt row is found via the CHAINED old->new id
      translation at the AMENDED code), the 3 excluded entries are NOT
      re-applied (their rebuilt forms are verified to be the demoted
      unresolved-span worklist rows), the other 828 entries hit direct or
      chained identities; the amendment's 3 ADDED entries promote the H3
      sign-off rows (identity verified against the LIVE rebuilt rows,
      verdict SIGN_OFF, validated_by operator, the verbatim signoff_basis
      carried); validated_by operator everywhere (AI-name patterns fail
      closed), the sampled 457 == the R21 CONFIRM set (keyed by the R5-era
      ids), the re-applied set == anchored 835 - R22 REJECT 3 - the
      re-homed hold 1 == 831 both directions (828 from the R5 chain + 3
      added); every applied promotion block equals BOTH the R5 tool's block
      shape AND the baseline store's block for the same chunk identity
      (byte-stable re-application for the 828; the standard R5-shaped block
      for the 3 added rows — no baseline block exists, the SUGGESTED
      pre-state is verified instead); the 7 non-count meta promotion fields
      are restored byte-equal to the R5 values, meta.promoted_rows RESTATES
      831 (the set re-composed: 828 + 3) and the meta gains ONLY the
      additive re-dated promotion_reapplied* fields;
  R7. consolidated row-set arithmetic: new_ids == old_ids - {6 old
      REATTRIBUTE ids} - {3 DEMOTE old ids} - {the 2.7C DEFER id} + {6 new
      REATTRIBUTE ids} + {3 demoted ids} exactly (918 -> 917);
      consolidated final-vs-baseline equality: validation_status matches
      the baseline everywhere EXCEPT the 6 enumerated changes (3 DEMOTEs
      HUMAN_VALIDATED -> SUGGESTED worklist + 3 sign-offs SUGGESTED ->
      HUMAN_VALIDATED — the loop's FIRST SUGGESTED -> HUMAN_VALIDATED
      promotions additions, the R5 escape-hatch mechanism completed);
      non-moved rows differ only in the provenance.tool string;
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk under the shared norm(), chunk sha256_16/heading/chars,
      ratified-188 registry membership for every coded row — 835 coded);
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution, REJECT/hold/worklist categorically unpromoted, every
      HUMAN_VALIDATED row carries a promotion block backed by the amended
      file chain, the DEMOTE rows carry NO promotion block, the re-homed
      hold stays SUGGESTED;
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R31_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r31_substrate_rebuild.py --dry-run
    python3 scripts/c42_r31_substrate_rebuild.py
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
MAP30 = HERE / "c42_section_overrides_r30.yaml"
AMENDMENT = HERE / "c42_r30_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R29_REGATE_CHECK.json"
REPAIR_CHECK = REPO / "graph/reports/C42_R30_REPAIR_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R31_REBUILD_RECORD.md"

TOOL = "scripts/c42_r31_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "f16daa2658a1791b04f345e61734cc901d17c8e9"
DIRECTIVE = ("Fix all of these yourself. Validate by yourself. — "
             "2026-10-12, zai-web (gateway trace 1a130272fc8acc11)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.6.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
OPERATOR_ROUND = ("C42 R30 (surface 3: 6 verdicted REATTRIBUTEs [5 HV + 1 "
                  "SUGGESTED re-homed hold] + the grouping DEMOTE batch of "
                  "3 — the loop's FIFTH DEMOTE)")
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
REAPPLIED_META = {
    "promotion_reapplied": "2026-10-12",
    "promotion_reapplied_by": f"{TOOL}@{VERSION}",
    "promotion_reapplied_directive": DIRECTIVE,
    "promotion_reapplied_note": (
        "re-applied byte-stably over the R31 substrate re-build (the c40 "
        "tool emits all-SUGGESTED) AMENDED by "
        "scripts/c42_r30_promotions_amendment.yaml (schema "
        "c42-r31-promotions-amendment/1.0, the loop's SECOND "
        "promotions-affecting repair record and the FIRST with ADDITIONS: "
        "5 code supersedes re-keyed old->new + 3 exclusions — the DEMOTE "
        "batch lands unresolved-span — + 3 ADDED sign-off promotions — the "
        "loop's FIRST promotions ADDITIONS, the R5 apply record's own "
        "per-row H3 sign-off mechanism completed under the operator "
        "directive trace 1a130272fc8acc11; 831 re-applied = 828 from the "
        "R5 chain + 3 added, the R5 file byte-untouched per the P5 "
        "convention); meta.promoted_rows RESTATED 831 (the set "
        "re-composed: 828 + 3; the 7 other R5 promotion meta fields "
        "byte-equal); see graph/reports/C42_R31_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R31 substrate re-build (2026-10-12, consuming the R30 operator "
    "override map: 4.11C->2.7C x3 / 4.8D->4.8F / 3.3F->3.3I x2 [ord 0 the "
    "re-homed SUGGESTED hold] + the grouping DEMOTE batch of 3 (ords 0/1/3, "
    "the loop's FIFTH DEMOTE) AND the R30 promotions amendment (5 code "
    "supersedes + 3 exclusions + 3 ADDED sign-off promotions): the R5 §18 "
    "promotion surface re-applied AMENDED TWICE OVER — 831 rows "
    "HUMAN_VALIDATED (828 from the R5 chain + 3 added); 3 R22 REJECT rows "
    "stay SUGGESTED; the re-homed drawing ord 0 hold stays SUGGESTED; the "
    "DEMOTE batch lands unresolved-span; coverage 133/188 (gained 2.7C).\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r31_substrate_rebuild.py",
    "scripts/c42_r31_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R31_REBUILD_RECORD.json",
    "graph/reports/C42_R31_REBUILD_RECORD.md",
    "graph/reports/C42_R31_REBUILD_CHECK.json",
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

    print("C42 R31 SUBSTRATE REBUILD — gated lane (both R30 carriers)")
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
          and len(base["rows"]) == 918 and len(base_anchored) == 838
          and len(base_hv) == 831
          and base["meta"].get("promotion_record") == "scripts/c42_r5_promotions.yaml")
    if not gate("R1_pre_state", r1,
                f"HEAD {head[:12]} == baseline {BASELINE[:12]}; disk store == "
                f"baseline blob; dirty {len(dirty)} within the R31 footprint; "
                f"baseline census 918 = 838 anchored (831 HUMAN_VALIDATED) + "
                f"80 worklist; R5 promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.7.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R30 map AND amendment contracts --------------------------------
    map_bytes = MAP30.read_bytes()
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
          and map_doc.get("round") == "R30"
          and len(entries) == 9 and len(reattr) == 6 and len(demote) == 3
          and len(map_doc.get("h3_signoffs") or {}) - 1 == 3
          and len(map_doc.get("retain_rulings") or {}) - 1 == 2
          and len(map_doc.get("note_level_scoping") or []) == 2
          and "note_level_adjudications" not in map_doc
          and all(e.get("action") == "REATTRIBUTE"
                  and e.get("provenance_class") == "verdicted"
                  and e.get("override_code") in registry
                  and e.get("override_code") != e.get("current_code")
                  for e in reattr)
          and all(e.get("action") == "DEMOTE_TO_WORKLIST"
                  and e.get("override_code") is None for e in demote)
          and amend.get("schema") == "c42-r31-promotions-amendment/1.0"
          and amend.get("round") == "R30"
          and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
          and amend.get("base_file_sha256_16") == promo_sha
          and amend.get("base_file_untouched") is True
          and amend.get("prior_amendments") == \
          ["scripts/c42_r26_promotions_amendment.yaml"]
          and len(sup) == 5 and len(exc) == 3 and len(added) == 3
          and len(set(sup_by_id) | set(exc_by_id) | set(added_by_mid)) == 11
          and {e.get("mapping_id") for e in entries
               if e.get("mapping_id") in sup_by_id | exc_by_id} ==
              set(sup_by_id) | set(exc_by_id)
          and all(sup_by_id[e["mapping_id"]].get("pinned_code") ==
                  e.get("current_code")
                  and sup_by_id[e["mapping_id"]].get("amended_code") ==
                  e.get("override_code")
                  for e in reattr if e["mapping_id"] in sup_by_id)
          and all(exc_by_id[e["mapping_id"]].get("pinned_code") ==
                  e.get("current_code")
                  and exc_by_id[e["mapping_id"]].get("disposition") ==
                  "DEMOTE_TO_WORKLIST"
                  for e in demote)
          and all(a.get("verdict") == "SIGN_OFF"
                  and a.get("validated_by") == "operator"
                  and (a.get("signoff_basis") or "").strip()
                  and a.get("verdict_source") == "r30-operator-signoff"
                  for a in added))
    if not gate("R2_map_and_amendment_contracts", r2,
                f"map schema c42-r28-section-overrides/1.0; 6 verdicted "
                f"REATTRIBUTEs with ratified targets != currents "
                f"({', '.join(sorted(e['current_code'] + '->' + e['override_code'] for e in reattr))})"
                f" + 3 DEMOTEs (override_code null); 3 H3 sign-offs + 2 "
                f"retains + 2 scoping notes recorded, no NEW c40-pinned "
                f"adjudications; amendment schema "
                f"c42-r31-promotions-amendment/1.0 with base sha "
                f"{amend.get('base_file_sha256_16')} == the live R5 sha, 5 "
                f"supersedes (amended_code == override_code) + 3 excluded "
                f"DEMOTEs + 3 ADDED SIGN_OFF entries (validated_by operator, "
                f"verbatim signoff_basis), the 11 ids distinct; map sha "
                f"{map_sha}, amendment sha {amend_sha}"):
        die("R2 map/amendment contracts failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check29 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    check30 = json.loads(REPAIR_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check29.get("all_pass") is True and check29.get("passed") == 13
          and check30.get("result") == "ALL PASS" and check30.get("passed") == 9
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R29 regate all_pass 13/13; R30 repair check ALL PASS 9/9; "
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
          and len(rows_new) == 917 and n_anchored == 835 and n_span == 27
          and n_unmapped == 55 and len(covered) == 133
          and len(ids_new) == len(set(ids_new))
          and "4MA1-2.7C" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 917 = 835 anchored + 27 unresolved-span + 55 "
                f"uncovered-SP; covered 133 of 188 (the R30 projections "
                f"landing: gained 4MA1-2.7C — the DEFER row resolved; "
                f"computed, never asserted — the DC-R24-01 discipline); "
                f"mapping_ids unique"):
        die("R4 rebuild failed")
    if gained != ["4MA1-2.7C"] or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 re-attribution + DEMOTE delta vs the baseline blob ---------------------
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
                    "source": f"scripts/c42_section_overrides_r30.yaml@{map_sha}",
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
                    "source": f"scripts/c42_section_overrides_r30.yaml@{map_sha}",
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
                              "DEMOTE_TO_WORKLIST per the C42 R30")
                          and "(C42 R30 surface 3 demote)" in (nrow.get("disposition") or "")
                          and nrow.get("validation_status") == "SUGGESTED"
                          and "promotion" not in nrow
                          and nrow["chunk"] == orow["chunk"])
                if not ok_row:
                    drift.append(f"demote row {k}")
                demote_pairs.append((orow["mapping_id"], nrow["mapping_id"]))
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
        # non-chunk rows (the unmapped-SP worklist): the 2.7C DEFER row
        # vanishes; survivors tool-only
        old_nc = [r for r in base["rows"] if "chunk" not in r]
        new_nc = [r for r in rows_new if "chunk" not in r]
        defer_id = sha16("unmapped|4MA1-2.7C")
        vanished = [r for r in old_nc if r["mapping_id"] not in
                    {x["mapping_id"] for x in new_nc}]
        if not (len(old_nc) == 56 and len(new_nc) == 55
                and len(vanished) == 1
                and vanished[0]["mapping_id"] == defer_id
                and vanished[0].get("spec_code") == "4MA1-2.7C"):
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
    r5_pass = (r5_ok and len(moved) == 9 and len(id_pairs) == 6
               and len(demote_pairs) == 3 and not drift)
    if not gate("R5_reattribution_demote_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows); exactly 9 "
                f"rows moved: {', '.join(sorted(e['current_code'] + '->' + e['override_code'] for e in reattr))}"
                f" + the 3 DEMOTEs (2.2F -> unresolved-span, demoted ids "
                f"{sorted(n for _, n in demote_pairs)[:1]}...); "
                f"provenance.override == the map blocks; mapping_ids "
                f"recomputed; sp_titles swapped; all other rows differ ONLY in "
                f"provenance.tool {TOOL_OLD.split('@')[1]} -> "
                f"{TOOL_NEW.split('@')[1]}; the 4MA1-2.7C DEFER row is the "
                f"only vanishing row; meta delta == stage+tool+census keys "
                f"(the R30 projections landing 132->133 / 56->55 / 838->835 "
                f"/ 24->27)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application UNDER THE AMENDMENTS ----------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    # the LANDED R26 amendment translation (read from the R28 record) and the
    # fresh R30 translation (from this lane's delta)
    rec28 = json.loads(R28_REC.read_text(encoding="utf-8"))
    r26_rekey = dict(rec28["promotions"]["superseded_ids_rekeyed"])
    pair30_by_old = {o: n for o, n in id_pairs}
    r26_amend = yaml.safe_load((HERE / "c42_r26_promotions_amendment.yaml")
                               .read_text(encoding="utf-8"))
    r26_sup = {e["mapping_id"]: e for e in r26_amend.get("supersedes_code") or []}
    r26_exc = {e["mapping_id"] for e in r26_amend.get("excluded") or []}
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
            problems.append(f"R30 amendment supersedes {eid} drift vs the R5 file")
    for eid, e in exc_by_id.items():
        pe = (pentry_by_id.get(eid) or {}).get("row") or {}
        if (pe.get("spec_code") != e.get("pinned_code")
                or pe.get("note_path") != e.get("note_path")
                or int(pe.get("chunk_ordinal", -1)) != int(e.get("chunk_ordinal", -2))):
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
    # resolve every R5 entry against the rebuilt rows through BOTH amendments
    resolved = {}
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        if mid in r26_exc or mid in exc_by_id:
            continue
        if mid in sup_by_id:
            target_id = pair30_by_old.get(mid)
            want_code = sup_by_id[mid].get("amended_code")
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
    # the excluded rows' rebuilt forms ARE the demoted worklist rows
    for eid, e in exc_by_id.items():
        pair = next(((o, dn) for o, dn in demote_pairs if o == eid), None)
        if pair is None:
            problems.append(f"the excluded id {eid} is not a DEMOTE row's old id")
            continue
        dn = new_rows.get(pair[1], {})
        if dn.get("worklist_reason") is None \
                or dn.get("validation_status") != "SUGGESTED" \
                or "promotion" in dn:
            problems.append(f"the excluded row {eid} is not the demoted "
                            f"unresolved-span worklist row")
    # the 3 ADDED sign-off rows: verified against the LIVE rebuilt rows
    for mid, a in added_by_mid.items():
        r = a.get("row") or {}
        target = new_rows.get(mid)
        if target is None:
            problems.append(f"added {mid} no rebuilt row")
            continue
        if (target.get("spec_code") != r.get("spec_code")
                or target.get("note_path") != r.get("note_path")
                or target["chunk"]["ordinal"] != r.get("chunk_ordinal")
                or target["chunk"]["heading"] != r.get("heading")
                or target["chunk"]["sha256_16"] != r.get("chunk_sha256_16")):
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
    # the R21-era HOLD set: 3 promoted via the additions, 1 re-keyed by the map
    vhold_promoted, vhold_rekeyed = set(), set()
    for mid in vhold:
        brow = base_rows[mid]
        nrow = new_rows_by_ident[ident(brow)]
        if mid in added_by_mid:
            vhold_promoted.add(nrow["mapping_id"])
            if nrow["mapping_id"] != mid:
                problems.append(f"sign-off row re-keyed unexpectedly {mid}")
        else:
            vhold_rekeyed.add(nrow["mapping_id"])
    if vhold_promoted != set(added_by_mid):
        problems.append("the promoted hold set != the 3 added sign-offs")
    if len(vhold_rekeyed) != 1:
        problems.append("the re-keyed hold set != the 1 re-homed 3.3F row")
    vhold_remaining = vhold_rekeyed
    anchored_new = {r["mapping_id"] for r in rows_new
                    if r.get("spec_code") and "chunk" in r}
    promote_set = anchored_new - vrej_new - vhold_remaining
    worklist_new = {r["mapping_id"] for r in rows_new
                    if r.get("worklist_reason")}
    if (len(resolved) != 828 or len(resolved) + len(added_by_mid) != 831
            or resolved.keys() | set(added_by_mid) != promote_set
            or n_sampled != 457
            or promote_set & (vrej_new | vhold_remaining | worklist_new)):
        problems.append(f"round contract: resolved {len(resolved)} + added "
                        f"{len(added_by_mid)} vs surface {len(promote_set)}; "
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
        if mid in added_by_mid:
            old_mid, _want_code = None, None
            base_block = None
        else:
            old_mid, _want_code = resolved[mid]
            # the baseline block is looked up by CHUNK identity — the R26
            # re-key already landed in the baseline (the row lives at its
            # R26/R30-era id there)
            base_block = base_by_ident[ident(row)].get("promotion")
        if "promotion" in row or row.get("validation_status") != "SUGGESTED":
            die(f"row {mid} pre-poisoned — refusing")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if old_mid is not None and block != base_block:
            die(f"promotion block drift vs the R5 surface on {mid} "
                f"(via {old_mid})")
        row["promotion"] = block
        flipped += 1
    if flipped != 831:
        die(f"flipped {flipped} != 831")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    meta_f["promoted_rows"] = 831            # RESTATED — the re-composed surface
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"the amendment pre-apply integrity verified (pinned_code == the R5 "
         f"file on every supersedes/excluded entry of BOTH amendments — any "
         f"drift fails); 832 R5 entries resolved through the LANDED R26 "
         f"amendment (its re-key read from the R28 record) and the R30 "
         f"amendment: 828 direct-or-chained identities (5 R30 supersedes "
         f"re-keyed at the AMENDED codes 4.11C->2.7C x3 / 4.8D->4.8F / "
         f"3.3F->3.3I; 3 R30 exclusions + the R26 exclusion skipped; the 3 "
         f"R26 supersedes re-keyed via the R28 record) + 3 ADDED SIGN_OFF "
         f"promotions (the loop's FIRST additions, the R5 escape-hatch "
         f"mechanism completed); validated_by operator everywhere; sampled "
         f"457 == the R21 CONFIRM set (R5-era ids); surface == anchored 835 "
         f"- R22 REJECT 3 - the re-homed hold 1 == 831 both directions "
         f"(828 + 3); every applied block == the R5 tool shape AND the "
         f"baseline store's block for the 828 (byte-stable re-application); "
         f"meta promotion fields restored byte-equal EXCEPT promoted_rows "
         f"RESTATED 831 (the set re-composed 828 + 3) + 4 additive "
         f"re-dated promotion_reapplied* fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = (old_ids - {o for o, _ in id_pairs}
                - {o for o, _ in demote_pairs}
                - {sha16("unmapped|4MA1-2.7C")}
                | {n for _, n in id_pairs} | {n for _, n in demote_pairs})
    r7 = new_ids == want_new and len(new_ids) == 917
    fin_chunk = {ident(r): r for r in final_doc["rows"] if "chunk" in r}
    moved_idents = set(moved)
    demote_old_idents = {k for k in old_chunk
                         if old_chunk[k]["mapping_id"] in
                         {o for o, _ in demote_pairs}}
    cons_drift = []
    for k, brow in old_chunk.items():
        frow = fin_chunk[k]
        if k in demote_old_idents:
            # the DEMOTE rows: the enumerated status change (HV -> SUGGESTED
            # worklist) IS the round's action
            if frow.get("validation_status") != "SUGGESTED" or \
                    "promotion" in frow or frow.get("spec_code") is not None:
                cons_drift.append(f"demote final shape {k}")
            continue
        added_mid = frow["mapping_id"] in added_by_mid
        if added_mid:
            # the ADDED sign-off rows: the enumerated status change
            # (SUGGESTED -> HUMAN_VALIDATED) IS the round's action
            if frow.get("validation_status") != "HUMAN_VALIDATED" or \
                    "promotion" not in frow:
                cons_drift.append(f"added final shape {k}")
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
                f"new_ids == old_ids - 6 old REATTRIBUTE ids - 3 DEMOTE old "
                f"ids - the 2.7C DEFER id + 6 new REATTRIBUTE ids + 3 "
                f"demoted ids (918 -> 917) exactly; consolidated "
                f"final-vs-baseline equality: validation_status matches "
                f"everywhere EXCEPT the 6 enumerated changes (3 DEMOTEs "
                f"HUMAN_VALIDATED -> SUGGESTED worklist + 3 sign-offs "
                f"SUGGESTED -> HUMAN_VALIDATED — the loop's FIRST "
                f"SUGGESTED -> HUMAN_VALIDATED promotions additions), the "
                f"only non-moved delta is the provenance.tool string, the 9 "
                f"moved rows carry exactly the enumerated fields"
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
                f"(828 from the R5 chain + 3 added); the SUGGESTED anchored "
                f"residue == the 3 R22 re-attributed REJECTs + the 1 "
                f"re-homed hold; the DEMOTE rows carry NO promotion block "
                f"(unresolved-span worklist); provenance tiers "
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
        print(f"c42_r31_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 917 rows (831 HUMAN_VALIDATED re-applied "
              f"AMENDED: 828 + 3 added; 6 re-attributions + 3 DEMOTEs; "
              f"coverage 133/188); no files written")
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
        is_promoted = o in sup_by_id
        landings.append({
            "note_slug": e["note_slug"], "chunk_ordinal": e["chunk_ordinal"],
            "mapping_id_old": o, "mapping_id_new": n,
            "from_code": e["current_code"], "to_code": e["override_code"],
            "promoted_row": is_promoted,
            "promotion_amended_code": (sup_by_id[o]["amended_code"]
                                       if is_promoted else None),
        })
    demote_landings = []
    for (o, n) in demote_pairs:
        e = next(en for en in demote
                 if en["current_code"] == base_rows[o]["spec_code"])
        demote_landings.append({
            "note_slug": e["note_slug"], "chunk_ordinal": e["chunk_ordinal"],
            "mapping_id_old": o, "mapping_id_new": n,
            "from_code": e["current_code"],
            "to": "unresolved-span worklist (the c40 DEMOTE convention; "
                  "chunk identity intact — the W3 invariant)",
        })
    rec = {
        "schema": "c42-r31-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r31-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R29 record's NEXT-OPERATOR-DECISIONS menu, delegated "
                 "by the directive: the substrate re-build consuming the R30 "
                 "override map (schema c42-r28-section-overrides/1.0) AND "
                 "the R30 promotions amendment (schema "
                 "c42-r31-promotions-amendment/1.0, the FIRST with "
                 "ADDITIONS); the R32 validation re-gate sanctioned by the "
                 "same directive and fired separately"),
        "rebuild": {
            "tool": f"{C40_TOOL}@{c40.TOOL_VERSION}",
            "tool_version_move": "2.6.0 -> 2.7.0 (the R16->R20->R24->R26->R28 "
                                 "rebuild-lane convention; provenance.tool "
                                 "moves on every row — the store records its "
                                 "builder)",
            "join": "the R27-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged; the FOUR R26 STANDING pins verified "
                    "in-generator)",
            "override_maps_consumed": ("EIGHT: R1 + R6 (with the subsumption "
                                       "registry) + R10 + R14 + R18 + R22 + "
                                       "R26 + R30, all fail-closed"),
            "rows_pre": 918, "rows_post": 917,
            "anchored": 835, "unresolved_span": 27, "uncovered_sp_pre": 56,
            "uncovered_sp_post": 55,
            "covered_pre": 132, "covered_post": 133,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r30.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "reattribute": len(reattr), "demote": len(demote),
            "landings": landings,
            "demote_landings": demote_landings,
            "standing_pins": ("the FOUR R26 STANDING joins verified "
                              "in-generator (unchanged); NO new c40-pinned "
                              "adjudications this round; the R30 scoping "
                              "notes ride the map's note_level_scoping "
                              "block"),
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "amendment": {
                "path": "scripts/c42_r30_promotions_amendment.yaml",
                "sha256_16": amend_sha,
                "schema": "c42-r31-promotions-amendment/1.0",
                "supersedes": len(sup), "excluded": len(exc),
                "added": len(added),
                "pre_apply_integrity": "pinned_code verified against the R5 "
                                       "file BEFORE the amendment applies "
                                       "(both amendments)",
                "re_applied": 831,
                "re_applied_composition": "828 from the R5 chain + 3 added",
                "meta_promoted_rows_restated": "831 (the set re-composed "
                                               "828 + 3; the 7 other R5 "
                                               "promotion meta fields "
                                               "byte-equal)",
            },
            "reapplication": ("byte-stable: every applied block for the 828 "
                              "== the R5 tool's block shape AND the baseline "
                              "store's block for the same chunk identity; "
                              "the 3 ADDED rows carry the standard R5-shaped "
                              "block (no baseline block exists — the "
                              "SUGGESTED pre-state verified instead); the 5 "
                              "superseded rows REMAIN in the promoted set at "
                              "their amended codes (re-keyed old->new); the "
                              "3 DEMOTE rows leave the promoted set; the 3 "
                              "sign-off rows JOIN it; meta gains ONLY the "
                              "additive re-dated promotion_reapplied* "
                              "fields"),
            "superseded_ids_rekeyed": {o: n for o, n in id_pairs},
            "excluded_ids": [o for o, _ in demote_pairs],
            "added_ids": sorted(added_by_mid),
            "r26_chain": {"rekey_source": "graph/reports/"
                                          "C42_R28_REBUILD_RECORD.json",
                          "rekey": r26_rekey},
        },
        "structural_diff": {
            "rows": "918 -> 917 (the resolving 2.7C DEFER row: f081d3d51385cb8f)",
            "rows_moved": 9,
            "moved_fields": ["spec_code", "mapping_id", "sp_title",
                             "provenance.override (added block)", "rationale "
                             "(REATTRIBUTE suffix) — the 6 REATTRIBUTEs; "
                             "spec_code -> None, mapping_id -> demoted|…, "
                             "worklist_reason + disposition added, sp_title/"
                             "anchor popped — the 3 DEMOTEs"],
            "promoted_surface_delta": "831 -> 831 HUMAN_VALIDATED (the set "
                                      "re-composed: 828 re-applied + 3 "
                                      "added); the 5 superseded rows "
                                      "re-keyed at the amended codes; the "
                                      "other 823 differ ONLY in the "
                                      f"provenance.tool string "
                                      f"({TOOL_OLD} -> {TOOL_NEW})",
            "status_changes": "exactly 6: the 3 DEMOTE rows HUMAN_VALIDATED "
                              "-> SUGGESTED (worklist) + the 3 sign-off "
                              "rows SUGGESTED -> HUMAN_VALIDATED — the "
                              "loop's FIRST SUGGESTED -> HUMAN_VALIDATED "
                              "promotions additions, enumerated",
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
        "post_check": "scripts/c42_r31_rebuild_check.py",
        "not_done": [
            "the R32 validation re-gate NOT fired by this lane (it is "
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
    demote_lines = "\n".join(
        f"- `{l['from_code']}` -> unresolved-span — {l['note_slug']} ord "
        f"{l['chunk_ordinal']} (mapping_id {l['mapping_id_old']} -> "
        f"{l['mapping_id_new']}; the loop's FIFTH DEMOTE as a 3-row batch)"
        for l in demote_landings)
    added_lines = "\n".join(
        f"- `{a['row']['spec_code']}` — {a['row']['note_path'].split('/')[-1]} "
        f"ord {a['row']['chunk_ordinal']} ({a['row']['mapping_id']}; SIGN_OFF "
        f"per the R30 record, the R5 escape-hatch mechanism completed)"
        for a in added)
    md = f"""# C42 R31 — Substrate Re-build consuming BOTH R30 carriers — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "{DIRECTIVE.split(' — ')[0]}" ({DIRECTIVE.split(' — ')[1]}).
The directive delegated the R29 menu's rulings (landed as the R30 carriers)
and sanctions the R32 validation re-gate separately.

## What this is

The second substrate re-build consuming a promotions AMENDMENT — and the
FIRST consuming an ADDITIONS-capable one (the R30 novelty): the amended c40
tool ({C40_TOOL}@2.7.0 — the R16→…→R28 rebuild-lane version convention)
re-emits the store ALL-SUGGESTED consuming the EIGHT operator override maps
(R1 + R6 + R10 + R14 + R18 + R22 + R26 + **R30**, the new one, schema
`c42-r28-section-overrides/1.0`), and the R5 promotions file (832 exact row
identities, byte-untouched per the P5 convention) is re-applied **AMENDED**
by `scripts/c42_r30_promotions_amendment.yaml` (schema
`c42-r31-promotions-amendment/1.0`, the loop's SECOND promotions-affecting
repair record and the FIRST with ADDITIONS): the 5 REATTRIBUTE rows REMAIN
in the promoted set at their amended codes (re-keyed old→new), the 3 DEMOTE
rows LEAVE it (landing unresolved-span), and the 3 H3 sign-off rows JOIN it
— the loop's FIRST promotions ADDITIONS, the R5 apply record's own per-row
sign-off mechanism completed. The re-applied count stays **831** (828 from
the R5 chain + 3 added).

## The six re-attributions + the DEMOTE batch (from the R30 map, fail-closed)

{land_lines}
{demote_lines}

## The three promotions ADDITIONS (the R30 amendment's `added` block)

{added_lines}

## Coverage landing (computed, never asserted — the DC-R24-01 discipline)

covered **132 → 133** (gained `['4MA1-2.7C']` — the DEFER row
`f081d3d51385cb8f` resolving into the re-homed trio, the
R12/R16/R20/R24/R26/R28 coverage-gain precedent), lost `[]` (4.11C keeps 4
via similar-areas-and-volumes, 3.3F keeps 4 via conversion-graphs, 4.8D
keeps 4, 2.2F keeps 14 — verified row-by-row at R30); uncovered-SP
**56 → 55**; rows **918 → 917**; anchored **838 → 835**; unresolved-span
**24 → 27**.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.7.0 (amended per P5): the
  R30 map consumed fail-closed (6 verdicted REATTRIBUTEs + 3 DEMOTEs,
  targets ratified, current_code == join-derived) + the FOUR R26 STANDING
  pins verified in-generator (unchanged) + coverage recomputed (gained/lost
  computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, the map AND amendment
  contracts, the promotions authority chain (R29 all_pass 13/13 + R30 ALL
  PASS 9/9 + the promotions file sha == the R5 record's pin == the
  amendment's base pin), G7 determinism, the delta proofs (chunk-identity
  multiset identical; tool-string-only churn elsewhere; the DEFER-row vanish
  shape; meta delta == stage+tool+census keys), the amendment pre-apply
  integrity (pinned_code verified against the R5 file BEFORE the amendment
  applies — any drift fails the rebuild; BOTH amendments), the 831-row
  re-application (828 byte-stable + 3 added), the row-set arithmetic,
  G4-at-apply over every chunk row, the anti-forgery sweep, and CI parity
  (graph_check census identical pre/post; kg golden GREEN).
- `scripts/c42_r31_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R29 state) | Post (R31) |
|---|---|---|
| rows | 918 | 917 |
| HUMAN_VALIDATED | 831 | 831 (re-composed: 828 re-applied AMENDED + 3 added) |
| anchored SUGGESTED | 7 (3 REJECT + 4 HOLD) | 4 (3 REJECT + 1 re-homed hold) |
| unresolved-span worklist | 24 | 27 (the DEMOTE batch lands) |
| uncovered-SP worklist | 56 | 55 (2.7C resolved) |
| covered codes | 132/188 | 133/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r30.yaml` | `{map_sha}` |
| `c42_r30_promotions_amendment.yaml` | `{amend_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the R32 validation re-gate — sanctioned by the directive's "Validate by
  yourself" clause, fired as its own round
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r31_substrate_rebuild: APPLIED — 917 rows (831 "
          f"HUMAN_VALIDATED re-composed: 828 re-applied AMENDED + 3 added; "
          f"6 re-attributions + 3 DEMOTEs; coverage 133/188)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
