#!/usr/bin/env python3
"""c42_r24_substrate_rebuild.py — the T-C42 R24 gated merge point: substrate
re-build consuming the R22 operator override map + re-application of the R5
promotions file over the rebuilt store.

Fired by the operator directive "R24" (2026-10-04, discord, gateway trace
44ed8bf6a3f36790164951e2f79c451b) naming exactly the R22 record's
next-decision gate ("R24 (substrate re-build consuming the R22 map +
re-applying the R5 promotions file)"); the R25 re-gate is NOT fired.

The lane is the R12/R16/R20 re-build precedent UNDER a promoted surface for
the first time (the R24 novelty), fused with the R5 apply discipline:

  R1. pre-state pins: HEAD == the round-start baseline 6133463; the store on
      disk is byte-identical to the baseline blob; the working-tree dirt is
      inside the declared R24 footprint; the baseline store carries the R5
      promotion surface (921 rows, 832 HUMAN_VALIDATED, meta.promotion_record
      present);
  R2. the R22 map contract: schema c42-r24-section-overrides/1.0, exactly 3
      verdicted REATTRIBUTE entries with ratified targets != currents, the
      3 note-level STANDING adjudications present;
  R3. the promotions authority chain: the R21 regate check is still
      all_pass 13/13; the live promotions file sha256_16 equals the sha the
      R5 apply record pinned (the file is byte-unchanged since R5); the R21
      verdict record carries the 3 REJECT / 4 HOLD split;
  R4. re-build determinism (G7): the amended c40 tool (TOOL_VERSION 2.5.0,
      the R16->R20 rebuild-lane convention) constructs twice byte-identically,
      emits ALL-SUGGESTED rows, census 920 = 839 anchored + 23 unresolved-span
      + 58 uncovered-SP (covered 130 of 188 — the DC-R24-01 coverage-gain
      correction: the R22 map's 'stationary 129/188' projection was asserted,
      not computed; 4.8F had ZERO anchored rows and GAINS coverage, its DEFER
      worklist row resolving into an anchored row, the R12/R16/R20 precedent);
  R5. re-attribution delta vs the baseline blob: the chunk-identity multiset
      (note_path, ordinal, heading, sha256_16) is IDENTICAL (862 chunk rows);
      exactly the 3 map rows move (old code == current_code, new code ==
      override_code, mapping_id recomputed, provenance.override == the map
      block, sp_title == the registry wording); every surviving row differs
      ONLY in provenance.tool @2.4.0 -> @2.5.0 (the builder string moves
      honestly); the 4MA1-4.8F DEFER row is the ONLY row to vanish; the meta
      delta is exactly {stage, tool} (the 8 R5 promotion fields are re-added
      at R6);
  R6. promotions re-application: the 832 entries hit the rebuilt rows with
      exact identities (mapping_id + spec_code + note_path + ordinal +
      heading + chunk sha), validated_by operator everywhere (AI-name
      patterns fail closed), the sampled 457 == the R21 CONFIRM set, the
      promotion set == anchored 839 - REJECT 3 - HOLD 4 both directions with
      the REJECT ids translated old->new (the 3 re-attributed rows re-key);
      every applied promotion block equals BOTH the R5 tool's block shape AND
      the baseline store's block for the same row (byte-stable re-application
      — the promotion surface is re-applied, not re-decided); the 8 meta
      promotion fields are restored byte-equal to the R5 values and the meta
      gains ONLY the additive promotion_reapplied* fields;
  R7. consolidated row-set arithmetic: new_ids == old_ids - {3 old REJECT
      ids} - {the 4.8F DEFER id} + {3 new REJECT ids} exactly;
  R8. G4-at-apply: every chunk row re-verified against a fresh re-chunking
      (quote-in-chunk under the shared norm(), chunk sha256_16/heading/chars,
      ratified-188 registry membership for every coded row);
  R9. anti-forgery sweep: provenance tiers RULE_DERIVED everywhere, no AI
      attribution, REJECT/HOLD/worklist categorically unpromoted, every
      HUMAN_VALIDATED row carries a promotion block backed by the file;
  R10. CI parity: graph_check failure census IDENTICAL pre vs post (the
      pre-existing sparse-checkout environmental set) and
      kg_export --verify-golden GREEN on the rebuilt state.

Emits graph/reports/C42_R24_REBUILD_RECORD.{json,md}. Re-run fails closed
(the round is idempotent-by-refusal; the committed store + records are the
round's only outputs).

Usage:
    python3 scripts/c42_r24_substrate_rebuild.py --dry-run
    python3 scripts/c42_r24_substrate_rebuild.py
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
MAP22 = HERE / "c42_section_overrides_r22.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
REGATE_CHECK = REPO / "graph/reports/C42_R21_REGATE_CHECK.json"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
REC_JSON = REPO / "graph/reports/C42_R24_REBUILD_RECORD.json"
REC_MD = REPO / "graph/reports/C42_R24_REBUILD_RECORD.md"

TOOL = "scripts/c42_r24_substrate_rebuild.py"
VERSION = "1.0.0"
BASELINE = "61334637b8948042116dae5a8038796a9bcd57ac"
DIRECTIVE = ("R24 — 2026-10-04, discord (gateway trace "
             "44ed8bf6a3f36790164951e2f79c451b)")
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.4.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.5.0"
PROMO_META_KEYS = {"promotion_applied", "promoted_rows", "promotion_record",
                   "promotion_apply", "promotion_gate", "promotion_directive",
                   "promotion_reverification", "apply_record"}
REAPPLIED_META = {
    "promotion_reapplied": "2026-10-04",
    "promotion_reapplied_by": f"{TOOL}@{VERSION}",
    "promotion_reapplied_directive": DIRECTIVE,
    "promotion_reapplied_note": (
        "re-applied byte-stably over the R24 substrate re-build (the c40 "
        "tool emits all-SUGGESTED); the promoted 832-row surface is identity- "
        "and code-stable per the R22 map contract (schema "
        "c42-r24-section-overrides/1.0); see "
        "graph/reports/C42_R24_REBUILD_RECORD.json"),
}
HEADER_LINE_REBUILD = (
    "# T-C42 R24 substrate re-build (2026-10-04, consuming the R22 operator "
    "override map: 4.8D->4.8F / 2.2F->2.2B / 2.6B->3.3E): the R5 §18 "
    "promotion surface (832 rows HUMAN_VALIDATED) re-applied byte-stably; "
    "3 REJECT rows re-attributed stay SUGGESTED; 4 H3 HOLD + 81 worklist "
    "rows stay SUGGESTED; coverage 130/188 (gained 4.8F).\n")
EXPECTED_DIRTY = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r24_substrate_rebuild.py",
    "scripts/c42_r24_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R24_REBUILD_RECORD.json",
    "graph/reports/C42_R24_REBUILD_RECORD.md",
    "graph/reports/C42_R24_REBUILD_CHECK.json",
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

    print("C42 R24 SUBSTRATE REBUILD — gated lane")
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40          # amended @2.5.0
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
          and len(base["rows"]) == 921 and len(base_anchored) == 839
          and len(base_hv) == 832
          and base["meta"].get("promotion_record") == "scripts/c42_r5_promotions.yaml")
    if not gate("R1_pre_state", r1,
                f"HEAD {head[:12]} == baseline {BASELINE[:12]}; disk store == "
                f"baseline blob; dirty {len(dirty)} within the R24 footprint; "
                f"baseline census 921 = 839 anchored (832 HUMAN_VALIDATED) + "
                f"82 worklist; R5 promotion_record present"):
        die("R1 pre-state failed")
    if c40.TOOL_VERSION != "2.5.0":
        die(f"c40 TOOL_VERSION drifted: {c40.TOOL_VERSION}")

    # ---- R2 the R22 map contract ------------------------------------------------
    map_bytes = MAP22.read_bytes()
    map_sha = sha16(map_bytes)
    map_doc = yaml.safe_load(map_bytes.decode("utf-8"))
    registry = c40.load_registry()
    entries = map_doc.get("overrides") or []
    adj = map_doc.get("note_level_adjudications") or []
    r2 = (map_doc.get("schema") == "c42-r24-section-overrides/1.0"
          and map_doc.get("round") == "R22"
          and len(entries) == 3 and len(adj) == 3
          and all(e.get("action") == "REATTRIBUTE"
                  and e.get("provenance_class") == "verdicted"
                  and e.get("override_code") in registry
                  and e.get("override_code") != e.get("current_code")
                  for e in entries)
          and all(a.get("ruling") == "STANDING" for a in adj))
    if not gate("R2_r22_map_contract", r2,
                f"schema c42-r24-section-overrides/1.0; 3 verdicted REATTRIBUTE "
                f"entries with ratified targets != currents "
                f"({', '.join(e['current_code'] + '->' + e['override_code'] for e in entries)})"
                f"; 3 note-level STANDING adjudications; map sha {map_sha}"):
        die("R2 map contract failed")

    # ---- R3 promotions authority chain ------------------------------------------
    check21 = json.loads(REGATE_CHECK.read_text(encoding="utf-8"))
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    promo_sha = sha16(PROMOTIONS.read_bytes())
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r3 = (check21.get("all_pass") is True and check21.get("passed") == 13
          and r5rec.get("promotion_record", {}).get("sha256_16") == promo_sha
          and r5rec.get("promotion_record", {}).get("entries") == 832
          and len(vrej) == 3 and len(vhold) == 4 and len(vconf) == 457
          and r5rec.get("round", {}).get("promoted") == 832)
    if not gate("R3_promotions_authority", r3,
                f"R21 regate all_pass 13/13; promotions file sha {promo_sha} == "
                f"the R5 apply record's pin (byte-unchanged since R5); R21 "
                f"verdict split 457 CONFIRM / 3 REJECT / 4 HOLD; R5 record "
                f"promoted 832"):
        die("R3 authority chain failed")

    # ---- R4 re-build determinism + corrected census ------------------------------
    doc_a, doc_b = c40.construct(), c40.construct()
    dump_a = yaml.safe_dump(doc_a, allow_unicode=True, sort_keys=False, width=100)
    dump_b = yaml.safe_dump(doc_b, allow_unicode=True, sort_keys=False, width=100)
    rows_new = doc_a["rows"]
    meta_new = doc_a["meta"]
    n_anchored = sum(1 for r in rows_new if r.get("spec_code") and "chunk" in r)
    n_span = sum(1 for r in rows_new if r.get("worklist_reason") and "chunk" in r)
    n_unmapped = sum(1 for r in rows_new if r.get("worklist_reason")
                     and "chunk" not in r)
    covered = {r["spec_code"] for r in rows_new
               if r.get("spec_code") and "chunk" in r}
    ids_new = [r["mapping_id"] for r in rows_new]
    r4 = (dump_a == dump_b
          and all(r.get("validation_status") == "SUGGESTED" for r in rows_new)
          and len(rows_new) == 920 and n_anchored == 839 and n_span == 23
          and n_unmapped == 58 and len(covered) == 130
          and len(ids_new) == len(set(ids_new))
          and "4MA1-4.8F" in covered)
    if not gate("R4_rebuild_determinism", r4,
                f"G7 two constructions byte-identical; emission ALL-SUGGESTED; "
                f"census 920 = 839 anchored + 23 unresolved-span + 58 "
                f"uncovered-SP; covered 130 of 188 (gained 4MA1-4.8F — the "
                f"DC-R24-01 correction, its DEFER row resolved); mapping_ids "
                f"unique"):
        die("R4 rebuild failed")
    gained = sorted(covered - {r["spec_code"] for r in base["rows"]
                               if r.get("spec_code") and "chunk" in r})
    lost = sorted({r["spec_code"] for r in base["rows"]
                   if r.get("spec_code") and "chunk" in r} - covered)
    if gained != ["4MA1-4.8F"] or lost:
        die(f"coverage landing drifted: gained {gained} lost {lost}")

    # ---- R5 re-attribution delta vs the baseline blob ------------------------------
    old_chunk = {ident(r): r for r in base["rows"] if "chunk" in r}
    new_chunk = {ident(r): r for r in rows_new if "chunk" in r}
    # identity multiset: idents are unique per construction (path+ordinal);
    # compare KEY SETS (Counter over the dicts would compare row VALUES)
    r5_ok = (set(old_chunk) == set(new_chunk) and len(old_chunk) == 862
             and len(set(old_chunk)) == 862)
    moved, id_pairs, drift = [], [], []
    if r5_ok:
        for k, orow in old_chunk.items():
            nrow = new_chunk[k]
            slug = orow.get("note_slug")
            entry = next((e for e in entries
                          if e["note_slug"] == slug
                          and e["chunk_ordinal"] == orow["chunk"]["ordinal"]), None)
            if entry:
                moved.append(k)
                want_block = {
                    "source": f"scripts/c42_section_overrides_r22.yaml@{map_sha}",
                    "operator_round": ("C42 R22 (surface 3: 3 verdicted "
                                       "REATTRIBUTEs, the loop's first "
                                       "zero-census-movement repair round)"),
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
            so, sn = orow, nrow

            # pre-reapplication stage: the 832 promoted rows legitimately
            # differ in validation_status + promotion (restored at R6); the
            # R5-stage zero-drift claim strips those two fields plus the
            # tool string
            def _strip_stage(row):
                row = strip_tool(row)
                row.pop("validation_status", None)
                row.pop("promotion", None)
                return row

            to_ = (so.get("provenance") or {}).get("tool")
            tn = (sn.get("provenance") or {}).get("tool")
            if _strip_stage(so) != _strip_stage(sn) or to_ != TOOL_OLD \
                    or tn != TOOL_NEW:
                drift.append(f"tool/zero-drift {k}")
        # non-chunk rows (the unmapped-SP worklist only — the 23
        # unresolved-span rows DO carry chunk blocks and were covered above):
        # the 4.8F DEFER row vanishes; survivors tool-only
        old_nc = [r for r in base["rows"] if "chunk" not in r]
        new_nc = [r for r in rows_new if "chunk" not in r]
        defer_id = sha16("unmapped|4MA1-4.8F")
        vanished = [r for r in old_nc if r["mapping_id"] not in
                    {x["mapping_id"] for x in new_nc}]
        if not (len(old_nc) == 59 and len(new_nc) == 58
                and len(vanished) == 1
                and vanished[0]["mapping_id"] == defer_id
                and vanished[0].get("spec_code") == "4MA1-4.8F"):
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
        # stage + tool move with the re-build; the covered/uncovered census
        # keys move with the DC-R24-01 coverage gain (129->130, 59->58 list)
        census_ok = (nm.get("sp_codes_covered") == 130
                     and nm.get("sp_codes_uncovered") == sorted(
                         set(registry) - covered)
                     and "4MA1-4.8F" not in nm.get("sp_codes_uncovered", [])
                     and om.get("sp_codes_covered") == 129
                     and "4MA1-4.8F" in om.get("sp_codes_uncovered", [])
                     and nm.get("rows_worklist_unmapped_sps") == 58
                     and om.get("rows_worklist_unmapped_sps") == 59)
        if set(om) - set(nm) != PROMO_META_KEYS \
                or meta_diff != {"stage", "tool", "sp_codes_covered",
                                 "sp_codes_uncovered",
                                 "rows_worklist_unmapped_sps",
                                 "upstream_store"} \
                or not census_ok \
                or "re-run at R23 with content-identical joins" \
                not in nm.get("upstream_store", ""):
            drift.append(f"meta delta {sorted(meta_diff)} / missing "
                         f"{sorted(set(om) - set(nm))[:3]} / census_ok "
                         f"{census_ok}")
    r5_pass = r5_ok and len(moved) == 3 and not drift
    if not gate("R5_reattribution_delta", r5_pass,
                f"chunk-identity multiset identical (862 rows); exactly 3 rows "
                f"moved: {', '.join(e['current_code'] + '->' + e['override_code'] for e in entries)}"
                f"; provenance.override == the map blocks; mapping_ids "
                f"recomputed; sp_titles swapped; all other rows differ ONLY in "
                f"provenance.tool {TOOL_OLD.split('@')[1]} -> "
                f"{TOOL_NEW.split('@')[1]}; the 4MA1-4.8F DEFER row is the "
                f"only vanishing row; meta delta == stage+tool+census keys "
                f"(the DC-R24-01 coverage landing 129->130 / 59->58)"
                + (f"; DRIFT {drift[:3]}" if drift else "")):
        die("R5 delta proof failed")

    # ---- R6 promotions re-application -----------------------------------------------
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    new_rows = {r["mapping_id"]: r for r in rows_new}
    seen, problems = set(), []
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        where = f"promotion[{n}]"
        if not mid or mid in seen:
            problems.append(f"{where} identity")
            continue
        seen.add(mid)
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"{where} attribution")
        target = new_rows.get(mid)
        if target is None:
            problems.append(f"{where} no rebuilt row")
            continue
        if (target.get("spec_code") != row.get("spec_code")
                or target.get("note_path") != row.get("note_path")
                or target["chunk"]["ordinal"] != row.get("chunk_ordinal")
                or target["chunk"]["heading"] != row.get("heading")
                or target["chunk"]["sha256_16"] != row.get("chunk_sha256_16")):
            problems.append(f"{where} identity drift")
        if "verdict" in e:
            n_sampled += 1
            if e["verdict"] != "CONFIRM" or mid not in vconf:
                problems.append(f"{where} sampled verdict")
    # old->new REJECT id translation (the 3 re-attributed rows re-key)
    old_reject_ids = {o for o, _ in id_pairs}
    new_reject_ids = {n for _, n in id_pairs}
    if old_reject_ids != vrej:
        problems.append(f"the 3 moved rows are not exactly the R21 REJECT set "
                        f"({sorted(old_reject_ids)} vs {sorted(vrej)})")
    new_rows_by_ident = {ident(r): r for r in rows_new if "chunk" in r}
    vhold_new = set()
    for mid in vhold:
        brow = base_rows[mid]
        nrow = new_rows_by_ident[ident(brow)]
        vhold_new.add(nrow["mapping_id"])
        if nrow["spec_code"] != brow["spec_code"]:
            problems.append(f"hold row moved {mid}")
    anchored_new = {r["mapping_id"] for r in rows_new
                    if r.get("spec_code") and "chunk" in r}
    promote_set = anchored_new - new_reject_ids - vhold_new
    worklist_new = {r["mapping_id"] for r in rows_new
                    if r.get("worklist_reason")}
    if (seen != promote_set or len(seen) != 832 or n_sampled != 457
            or seen & (new_reject_ids | vhold_new | worklist_new)
            or not vconf <= seen):
        problems.append(f"round contract: entries {len(seen)} vs surface "
                        f"{len(promote_set)}; sampled {n_sampled}")
    if problems:
        gate("R6_promotions_reapplication", False,
             f"problems: {problems[:4]}")
        die("R6 promotions re-application failed")
    # flip + byte-stable blocks
    final_doc = yaml.safe_load(dump_a)  # fresh parse; rows are fresh dicts
    flipped = 0
    base_blocks = {}
    for m in promote_set:
        brow = base_rows[m]
        base_blocks[m] = brow.get("promotion")
    for row in final_doc["rows"]:
        mid = row["mapping_id"]
        if mid not in promote_set:
            continue
        if "promotion" in row or row.get("validation_status") != "SUGGESTED":
            die(f"row {mid} pre-poisoned — refusing")
        row["validation_status"] = "HUMAN_VALIDATED"
        block = r5.promotion_block()
        if block != base_blocks.get(mid):
            die(f"promotion block drift vs the R5 surface on {mid}")
        row["promotion"] = block
        flipped += 1
    if flipped != 832:
        die(f"flipped {flipped} != 832")
    meta_f = final_doc["meta"]
    for k in PROMO_META_KEYS:
        meta_f[k] = base["meta"][k]          # byte-equal R5 values
    for k, v in REAPPLIED_META.items():
        meta_f[k] = v                        # additive, appended last
    gate("R6_promotions_reapplication", True,
         f"832 entries hit the rebuilt rows with exact identities; "
         f"validated_by operator everywhere (AI-patterns fail closed); "
         f"sampled 457 == the R21 CONFIRM set; surface == anchored 839 - "
         f"REJECT 3 (old ids == the R21 set, re-keyed old->new) - HOLD 4 both "
         f"directions; every applied block == the R5 tool shape AND the "
         f"baseline store's block (byte-stable re-application); meta "
         f"promotion fields restored byte-equal + 4 additive "
         f"promotion_reapplied* fields")

    # ---- R7 consolidated row-set arithmetic + final equality -------------------------
    old_ids = set(base_rows)
    new_ids = {r["mapping_id"] for r in final_doc["rows"]}
    want_new = old_ids - old_reject_ids - {sha16("unmapped|4MA1-4.8F")} \
        | new_reject_ids
    r7 = new_ids == want_new and len(new_ids) == 920
    # consolidated final-vs-baseline equality: for every chunk row the ONLY
    # permitted deltas are the provenance.tool string (every row) plus the
    # enumerated re-attribution fields (exactly the 3 moved rows);
    # validation_status matches the baseline everywhere; non-chunk rows are
    # equal except the vanished 4.8F DEFER row
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
    r7 = r7 and not cons_drift
    if not gate("R7_row_set_arithmetic", r7,
                f"new_ids == old_ids - 3 old REJECT ids - the 4.8F DEFER id "
                f"+ 3 new REJECT ids (921 -> 920) exactly; consolidated "
                f"final-vs-baseline equality: validation_status matches "
                f"everywhere, the only non-moved delta is the "
                f"provenance.tool string, the 3 moved rows carry exactly the "
                f"enumerated re-attribution fields"
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
    r8 = not failed and n_coded == 839
    if not gate("R8_g4_at_apply", r8,
                f"all {sum(1 for x in final_doc['rows'] if 'chunk' in x)} chunk "
                f"rows re-verified against a fresh re-chunking (quote-in-chunk "
                f"+ sha/heading/chars); {n_coded}/839 coded rows inside the "
                f"ratified 188" + (f"; FAIL {failed[:3]}" if failed else "")):
        die("R8 G4-at-apply failed")

    # ---- R9 anti-forgery sweep ------------------------------------------------------------
    hv = [x for x in final_doc["rows"]
          if x.get("validation_status") == "HUMAN_VALIDATED"]
    sug_anch = {x["mapping_id"] for x in final_doc["rows"]
                if x.get("chunk") and x.get("spec_code")
                and x.get("validation_status") == "SUGGESTED"}
    tiers_ok = all(x.get("provenance", {}).get("tier") == "RULE_DERIVED"
                   for x in final_doc["rows"])
    attribution_ok = all(
        x["promotion"]["promoted_by"] == "operator"
        and not r5.AI_PAT.search(json.dumps(x["promotion"]))
        for x in hv)
    r9 = (len(hv) == 832 and {x["mapping_id"] for x in hv} == promote_set
          and sug_anch == new_reject_ids | vhold_new
          and tiers_ok and attribution_ok
          and not (promote_set & (worklist_new | vhold_new | new_reject_ids)))
    if not gate("R9_anti_forgery", r9,
                f"832 HUMAN_VALIDATED == the promotion set; the SUGGESTED "
                f"anchored residue == the 3 re-attributed REJECTs + the 4 H3 "
                f"HOLDs; provenance tiers RULE_DERIVED everywhere; operator "
                f"attribution clean; REJECT/HOLD/worklist categorically "
                f"unpromoted"):
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
        print(f"c42_r24_substrate_rebuild --dry-run: ALL GATES GREEN — the "
              f"rebuild would emit 920 rows (832 HUMAN_VALIDATED re-applied) "
              f"with 3 re-attributions; no files written")
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
        e = next(en for en in entries
                 if en["current_code"] == base_rows[o]["spec_code"])
        landings.append({
            "note_slug": e["note_slug"], "chunk_ordinal": e["chunk_ordinal"],
            "mapping_id_old": o, "mapping_id_new": n,
            "from_code": e["current_code"], "to_code": e["override_code"],
        })
    rec = {
        "schema": "c42-r24-rebuild-record/1.0",
        "task": "T-C42",
        "stage": "r24-substrate-rebuild",
        "generated_utc": now,
        "baseline": BASELINE,
        "operator_directive": DIRECTIVE,
        "gate": ("the R22 record's next-decision gate: the substrate re-build "
                 "consuming the R22 override map (schema "
                 "c42-r24-section-overrides/1.0) + the R5 promotions-file "
                 "re-application; the R25 re-gate NOT fired"),
        "rebuild": {
            "tool": f"{C40_TOOL}@{c40.TOOL_VERSION}",
            "tool_version_move": "2.4.0 -> 2.5.0 (the R16->R20 rebuild-lane "
                                 "convention; provenance.tool moves on every "
                                 "row — the store records its builder)",
            "join": "the R23-refreshed T-C32 join (content-identical, census "
                    "198/5 unchanged)",
            "rows_pre": 921, "rows_post": 920,
            "anchored": 839, "unresolved_span": 23, "uncovered_sp_pre": 59,
            "uncovered_sp_post": 58,
            "covered_pre": 129, "covered_post": 130,
            "coverage_gained": gained, "coverage_lost": lost,
        },
        "dc_r24_01": {
            "id": "DC-R24-01",
            "corrects": ("the R22 map's contract text and the R22 record's "
                         "projection: 'coverage STATIONARY 129/188 (all three "
                         "targets already covered)' — asserted, not computed"),
            "fact": ("TRUE for 3.3E (2 anchored rows) and 2.2B (10) but FALSE "
                     "for 4.8F: it carried ZERO anchored rows (its "
                     "uncovered-SP DEFER row sat on the worklist). The "
                     "actual landing is a coverage GAIN: covered 129 -> 130, "
                     "gained ['4MA1-4.8F'], lost [], the 4MA1-4.8F DEFER row "
                     "resolving into an anchored row (the R12/R16/R20 "
                     "coverage-gain precedent); rows 921 -> 920 (the "
                     "resolving DEFER row, not a moved chunk row); anchored "
                     "839 / unresolved-span 23 unchanged (zero row-census "
                     "movement among chunk rows — no DEMOTEs)"),
            "action": ("recorded here per the P5 convention (landed records "
                       "never edited); the R22 re-attribution SUBSTANCE (the "
                       "three verdicts) is unaffected"),
        },
        "overrides": {
            "path": "scripts/c42_section_overrides_r22.yaml",
            "sha256_16": map_sha,
            "entries": len(entries),
            "landings": landings,
            "standing_pins": [f"{a['note_slug']} -> {a['joined_code']} on "
                              f"{a['anchor_id']}" for a in adj],
        },
        "promotions": {
            "path": "scripts/c42_r5_promotions.yaml",
            "sha256_16": promo_sha,
            "entries": len(pentries),
            "sampled_confirm": n_sampled,
            "reapplication": ("byte-stable: every applied block == the R5 "
                              "tool's block shape AND the baseline store's "
                              "block for the same row (832/832); the 8 meta "
                              "promotion fields restored byte-equal to the R5 "
                              "values; meta gains ONLY the additive "
                              "promotion_reapplied* fields"),
            "reject_ids_rekeyed": {o: n for o, n in id_pairs},
        },
        "structural_diff": {
            "rows": "921 -> 920 (the resolving 4MA1-4.8F DEFER row)",
            "rows_moved": 3,
            "moved_fields": ["spec_code", "mapping_id", "sp_title",
                             "provenance.override (added block)", "rationale "
                             "(REATTRIBUTE suffix)"],
            "promoted_surface_delta": "provenance.tool string only "
                                      f"({TOOL_OLD} -> {TOOL_NEW})",
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
        "post_check": "scripts/c42_r24_rebuild_check.py",
        "not_done": [
            "the R25 re-gate NOT fired (explicit operator instruction only)",
            "the 4 H3 HOLD rows untouched (per-row operator sign-off owed)",
            "the ord-3 promoted-surface extension candidate NOT adjudicated "
            "(operator-level decision; the promotions file pins the row)",
            "no resolution-file / corpus / Lane C / chemistry writes",
            "no promotion-file edits (byte-unchanged since R5, sha-pinned)",
        ],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    land_lines = "\n".join(
        f"- `{l['from_code']}` -> `{l['to_code']}` — {l['note_slug']} ord "
        f"{l['chunk_ordinal']} (mapping_id {l['mapping_id_old']} -> "
        f"{l['mapping_id_new']})" for l in landings)
    md = f"""# C42 R24 — Substrate Re-build + Promotions Re-application — igcse-maths-a

**Generated:** {now}  |  **Baseline:** `{BASELINE[:12]}`
**Operator directive:** "R24" ({DIRECTIVE.split(' — ')[1]}). The directive
names exactly the R22 record's next-decision gate; **the R25 re-gate is NOT
fired**.

## What this is

The first substrate re-build UNDER a promoted surface (the R24 novelty): the
amended c40 tool ({C40_TOOL}@2.5.0 — the R16→R20 rebuild-lane version
convention) re-emits the store ALL-SUGGESTED consuming the SIX operator
override maps (R1 + R6 + R10 + R14 + R18 + **R22**, the new one), and the R5
promotions file (832 exact row identities) is re-applied byte-stably. The 3
R22 override rows stayed SUGGESTED at R5, so the promotion set is identity-
and code-stable under the re-attributions (verified, not assumed). Every
surviving row differs from the baseline ONLY in `provenance.tool`
(@2.4.0 → @2.5.0) — the store records its builder honestly.

## The three re-attributions (from the R22 map, fail-closed)

{land_lines}

## DC-R24-01 — the R22 coverage projection, corrected

The R22 map asserted "coverage STATIONARY 129/188 (all three targets already
covered)" **without computing it**. True for 3.3E (2 rows) and 2.2B (10
rows); FALSE for **4.8F — it carried ZERO anchored rows**. The actual
landing is a coverage GAIN (the R12/R16/R20 precedent shape): covered
**129 → 130**, gained `['4MA1-4.8F']`, lost `[]`; the 4MA1-4.8F uncovered-SP
DEFER row resolves into an anchored row; rows **921 → 920**; anchored 839 /
unresolved-span 23 unchanged (zero row-census movement among chunk rows —
no DEMOTEs). Recorded per P5; the R22 records stay byte-untouched; the
re-attribution substance is unaffected.

## Mechanics

- `scripts/c40_maths_a_chunk_sp_substrate.py` @2.5.0 (amended per P5): the
  R22 map consumed fail-closed (3 verdicted REATTRIBUTEs, targets ratified,
  current_code == join-derived) + the THREE R22 STANDING pins verified
  in-generator (list-shaped adjudications, the R23 precedent) + coverage
  recomputed (gained/lost computed, never assumed).
- `{TOOL}@{VERSION}` (this lane): pre-state pins, map contract, promotions
  authority chain (R21 regate all_pass + the promotions file sha == the R5
  record's pin), G7 determinism, the delta proofs (chunk-identity multiset
  identical; tool-string-only churn elsewhere; the DEFER-row vanish shape;
  meta delta == stage+tool), the 832-row byte-stable re-application, the
  row-set arithmetic, G4-at-apply over every chunk row, the anti-forgery
  sweep, and CI parity (graph_check census identical pre/post; kg golden
  GREEN).
- `scripts/c42_r24_rebuild_check.py` (the committed-clean audit).

## Census

| Surface | Pre (R5 state) | Post (R24) |
|---|---|---|
| rows | 921 | 920 |
| HUMAN_VALIDATED | 832 | 832 (re-applied byte-stably) |
| anchored SUGGESTED | 7 (3 REJECT + 4 HOLD) | 7 (3 re-attributed + 4 HOLD) |
| unresolved-span worklist | 23 | 23 |
| uncovered-SP worklist | 59 | 58 (4.8F resolved) |
| covered codes | 129/188 | 130/188 |

## Pins

| Artifact | sha256_16 |
|---|---|
| store (pre, baseline blob) | `{rec['store_sha256_16_pre']}` |
| store (post) | `{rec['store_sha256_16_post']}` |
| `c42_section_overrides_r22.yaml` | `{map_sha}` |
| `c42_r5_promotions.yaml` (byte-unchanged since R5) | `{promo_sha}` |

## Open operator decisions (untouched by this lane)

- the R25 re-gate (explicit instruction only)
- the 4 H3 HOLD rows (per-row sign-off owed: 1.7B / 6.3J / 3.3F / 2.2C)
- the ord-3 promoted-surface extension candidate (3d-pythagoras SOHCAHTOA-3D)
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")
    print(f"c42_r24_substrate_rebuild: APPLIED — 920 rows (832 "
          f"HUMAN_VALIDATED re-applied byte-stably; 3 re-attributions; "
          f"coverage 130/188)")
    print(f"  store sha256_16 {rec['store_sha256_16_post']} "
          f"(pre {rec['store_sha256_16_pre']})")
    print(f"  WROTE {REC_JSON.relative_to(REPO)}")
    print(f"  WROTE {REC_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
