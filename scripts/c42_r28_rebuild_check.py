#!/usr/bin/env python3
"""c42_r28_rebuild_check.py — T-C42 R28 verification battery (committed-clean).

The R28 lane is the scope §7 loop's substrate re-build consuming the R26
override map AND the R26 promotions amendment (the R26 record's next-decision
menu option (a), fired together with R27 by the operator directive "R27 join
re-run + R28 rebuild consuming both carriers"; the R29 re-gate NOT fired).
Verified:

  B1 census+meta       918 rows = 838 anchored (831 HUMAN_VALIDATED + 7
                       SUGGESTED: the 3 R22 re-attributed REJECTs + the 4 H3
                       HOLDs) + 24 unresolved-span + 56 uncovered-SP; covered
                       132/188 (gained 4MA1-1.1A + 4MA1-5.1C — the R26
                       projections landing; lost none); meta promotion fields
                       byte-equal to the R5 values EXCEPT promoted_rows
                       RESTATED 832 -> 831 (the amended surface) + ONLY the
                       additive promotion_reapplied* fields; stage/tool
                       pinned @2.6.0
  B2 re-attributions   the 4 R26 map rows landed verbatim: the 3
  + DEMOTE             REATTRIBUTEs (old code == current_code, new code ==
                       override_code, mapping_id recomputed,
                       provenance.override == the map block with the map
                       sha, sp_title == the registry wording) and the DEMOTE
                       (spec_code -> None, mapping_id -> demoted|…,
                       worklist_reason + disposition + provenance.override
                       landed, chunk identity intact); all 4 rows SUGGESTED
                       with no promotion blocks
  B3 promotions        store <-> file+amendment two-way: 831 == 831 exact
  two-way              identities (mapping_id + spec_code + note_path +
                       ordinal + heading + chunk sha) with the 3 superseded
                       rows re-keyed old->new AT THE AMENDED CODES, the
                       excluded DEMOTE row NOT promoted (its rebuilt form is
                       the unresolved-span worklist row), validated_by
                       operator everywhere, sampled 457 == the R21 CONFIRM
                       set (R5-era ids), REJECT/HOLD/worklist carry zero
                       promotion blocks, the file sha == the R5 apply
                       record's pin == the amendment's base pin
                       (byte-unchanged since R5)
  B4 structural        final vs the baseline blob 11c2fc4: strip
  re-proof             provenance.tool -> byte-equal everywhere except the 4
                       moved rows (enumerated fields only), the vanished
                       1.1A + 5.1C DEFER rows (rows 920 -> 918) and the
                       enumerated DEMOTE status change (HUMAN_VALIDATED ->
                       SUGGESTED — the loop's first promoted-row status
                       change); the 831 promoted rows carry byte-equal
                       promotion blocks; non-moved HV rows differ ONLY in
                       the tool string
  B5 protected         resolution substrate (the R14-era pin), the R27 join
  surfaces             artifact, the promotions file + the R26 amendment +
                       the R26 map, the R5/R21/R22/R23/R24/R25/R26/R27
                       records + tools, the six earlier maps, the Lane C
                       stores, the chemistry substrate, the corpus manifest
                       and the ratified registry: byte-identical to the
                       baseline blob
  B6 determinism       the amended c40 tool constructs twice byte-identically
                       (G7) and the store sha matches the record's post pin
  B7 standing pins     the FOUR R26 STANDING joins verified against the R26
                       map's own list-shaped adjudications (ruling + anchor
                       id + landed code together) + the carried pins (the
                       R22 trio, the R18 pair, the R14 re-point, the R10
                       STANDING)
  B8 commit state      adaptive: pre-commit HEAD == baseline with the dirt
                       inside the R28 footprint; post-commit the working
                       tree is clean and the committed delta vs HEAD~1 stays
                       inside the footprint (the audit trail may move HEAD,
                       never the protected surfaces)
  B9 anti-forgery      every HUMAN_VALIDATED row carries a promotion block
                       with promoted_by operator (AI-name patterns fail
                       closed); provenance tiers RULE_DERIVED everywhere; the
                       4 H3 HOLD rows untouched (codes + ids); the DEMOTE row
                       carries NO promotion block
  B10 CI parity        kg_export --verify-golden GREEN on the committed
                       state; graph_check's failure census stays at the
                       pinned pre-round count with zero failures naming the
                       chunk store

Emits graph/reports/C42_R28_REBUILD_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BASELINE = "11c2fc49299103c2aa58aad67a87ed808df97601"
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE = REPO / STORE_REL
MAP26 = HERE / "c42_section_overrides_r26.yaml"
AMENDMENT = HERE / "c42_r26_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
TOOL = "scripts/c42_r28_substrate_rebuild.py"
TOOL_OLD = "scripts/c40_maths_a_chunk_sp_substrate.py@2.5.0"
TOOL_NEW = "scripts/c40_maths_a_chunk_sp_substrate.py@2.6.0"
RES_BLOB = "93419a291b9b87ff"  # the R14-era resolution pin — the git blob
# sha prefix as recorded verbatim by the R22/R23 records (not a sha256_16)
COURSE = "igcse-maths-a-18-higher"
JOIN_REL = (f"Official-Specifications/parsed/_derived/notes-join/"
            f"{COURSE}.json")
FOOTPRINT = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r28_substrate_rebuild.py",
    "scripts/c42_r28_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R28_REBUILD_RECORD.json",
    "graph/reports/C42_R28_REBUILD_RECORD.md",
    "graph/reports/C42_R28_REBUILD_CHECK.json",
}
PROTECTED = [
    "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json",
    JOIN_REL,
    "scripts/c42_r5_promote.py",
    "scripts/c42_r5_promotion_apply.py",
    "scripts/c42_r5_promotion_check.py",
    "graph/reports/C42_R5_APPLY_RECORD.json",
    "graph/reports/C42_R5_APPLY_RECORD.md",
    "graph/reports/C42_R5_APPLY_CHECK.json",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R21_REGATE_CHECK.json",
    "graph/reports/C42_R21_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R22_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R22_REPAIR_CHECK.json",
    "graph/reports/C42_R22_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R23_JOIN_RECORD.md",
    "graph/reports/C42_R23_JOIN_RECORD.json",
    "graph/reports/C42_R23_JOIN_CHECK.json",
    "graph/reports/C42_R24_REBUILD_RECORD.md",
    "graph/reports/C42_R24_REBUILD_RECORD.json",
    "graph/reports/C42_R24_REBUILD_CHECK.json",
    "graph/reports/C42_R25_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R25_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R25_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R25_REGATE_CHECK.json",
    "graph/reports/C42_R26_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R26_REPAIR_CHECK.json",
    "graph/reports/C42_R26_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R27_JOIN_RECORD.md",
    "graph/reports/C42_R27_JOIN_RECORD.json",
    "graph/reports/C42_R27_JOIN_CHECK.json",
    "scripts/c42_r21_review_verdicts.yaml",
    "scripts/c42_r21_fresh_verdicts.yaml",
    "scripts/c42_r22_repair_verdicts.yaml",
    "scripts/c42_r22_repair_proposals.py",
    "scripts/c42_r22_override_projection.py",
    "scripts/c42_r23_join_check.py",
    "scripts/c42_r24_substrate_rebuild.py",
    "scripts/c42_r24_rebuild_check.py",
    "scripts/c42_r25_regate_fill.py",
    "scripts/c42_r25_regate_check.py",
    "scripts/c42_r25_fresh_verdicts.yaml",
    "scripts/c42_r25_review_verdicts.yaml",
    "scripts/c42_r26_repair_verdicts.yaml",
    "scripts/c42_r26_repair_proposals.py",
    "scripts/c42_r26_repair_check.py",
    "scripts/c42_r26_override_projection.py",
    "scripts/c42_r27_join_check.py",
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c42_section_overrides.yaml",
    "scripts/c42_section_overrides_r6.yaml",
    "scripts/c42_section_overrides_r10.yaml",
    "scripts/c42_section_overrides_r14.yaml",
    "scripts/c42_section_overrides_r18.yaml",
    "scripts/c42_section_overrides_r22.yaml",
    "scripts/c42_section_overrides_r26.yaml",
    "scripts/c42_r26_promotions_amendment.yaml",
    "scripts/c42_r5_promotions.yaml",
    "graph/igcse-maths-a/specification_points.yaml",
    "graph/igcse-maths-a/concepts.yaml",
    "graph/igcse-maths-a/concept_edges.yaml",
    "graph/igcse-maths-a/spec_command_kinds.yaml",
    "graph/igcse-chemistry/spec_chunk_mappings.yaml",
    "graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md",
]

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"pass": bool(ok), "detail": detail}
    print(f"  {name}: {'PASS' if ok else 'FAIL'} — {detail[:220]}")
    return bool(ok)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


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
    import c42_r5_promotion_apply as r5  # block shape + AI_PAT (module level)

    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, text=True,
                          check=True).stdout.strip()
    dirty = {ln[3:].strip() for ln in subprocess.run(
        ["git", "-C", str(REPO), "status", "--porcelain"],
        capture_output=True, text=True, check=True).stdout.splitlines()
        if ln.strip()}
    pre_commit = head == BASELINE
    rec = json.loads((REPO / "graph/reports/C42_R28_REBUILD_RECORD.json")
                     .read_text(encoding="utf-8"))

    # ---------------------------------------------------------------- inputs
    store_bytes = STORE.read_bytes()
    store_doc = yaml.safe_load(store_bytes.decode("utf-8"))
    base_doc = yaml.safe_load(
        blob_at(BASELINE, STORE_REL).decode("utf-8"))
    base_rows = {r["mapping_id"]: r for r in base_doc["rows"]}
    rows = {r["mapping_id"]: r for r in store_doc["rows"]}
    map_bytes = MAP26.read_bytes()
    map_sha = sha16(map_bytes)
    map_doc = yaml.safe_load(map_bytes.decode("utf-8"))
    entries = map_doc["overrides"]
    reattr = [e for e in entries if e.get("action") == "REATTRIBUTE"]
    demote_e = next(e for e in entries if e.get("action") == "DEMOTE_TO_WORKLIST")
    adj = map_doc["note_level_adjudications"]
    amend = yaml.safe_load(
        AMENDMENT.read_text(encoding="utf-8"))
    promo_bytes = PROMOTIONS.read_bytes()
    promo_sha = sha16(promo_bytes)
    promo = yaml.safe_load(promo_bytes.decode("utf-8"))
    pentries = promo.get("promotions") or []
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    verdicts = ver["verdicts"]
    vrej = {m for m, p in verdicts.items() if p["verdict"] == "REJECT"}
    vhold = {m for m, p in verdicts.items() if p["verdict"] == "HOLD"}
    vconf = {m for m, p in verdicts.items() if p["verdict"] == "CONFIRM"}
    r5rec = json.loads(R5_REC.read_text(encoding="utf-8"))
    registry = {
        p["code"]: p
        for p in yaml.safe_load(
            (REPO / "graph/igcse-maths-a/specification_points.yaml")
            .read_text(encoding="utf-8"))["specification_points"]}

    # ---- B1 census + meta -----------------------------------------------------
    m = store_doc["meta"]
    anchored = {mid for mid, r in rows.items()
                if r.get("spec_code") and "chunk" in r}
    hv = {mid for mid, r in rows.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    sug_anch = anchored - hv
    span_wl = sum(1 for r in rows.values()
                  if r.get("worklist_reason") and "chunk" in r)
    unmapped = sum(1 for r in rows.values()
                   if r.get("worklist_reason") and "chunk" not in r)
    covered = {r["spec_code"] for r in rows.values()
               if r.get("spec_code") and "chunk" in r}
    promo_keys_ok = all(m[k] == base_doc["meta"][k]
                        for k in ("promotion_applied", "promotion_record",
                                  "promotion_apply", "promotion_gate",
                                  "promotion_directive",
                                  "promotion_reverification", "apply_record"))
    # the R24-era baseline ALREADY carries the 4 promotion_reapplied* keys
    # (added at R24), so the meta KEY SETS are identical and the round's
    # delta is by VALUE: the 8 census keys + promoted_rows RESTATED + the 4
    # reapplied fields re-dated — nothing else, nothing new
    diff_keys = {k for k in set(m) & set(base_doc["meta"]) if m[k] != base_doc["meta"][k]}
    expected_diff = {"stage", "tool", "sp_codes_covered",
                     "sp_codes_uncovered", "rows_worklist_unmapped_sps",
                     "rows_anchored", "rows_worklist_anchor_unresolved",
                     "upstream_store", "promoted_rows",
                     "promotion_reapplied_by", "promotion_reapplied_directive",
                     "promotion_reapplied_note"}
    # NOTE: promotion_reapplied itself is NOT in the delta — R24 and R28 ran
    # on the same UTC date (2026-10-04), so the date value is byte-equal; the
    # by/directive/note fields carry the R28 lane's values and DID move.
    b1 = (len(rows) == 918 and len(anchored) == 838 and len(hv) == 831
          and len(sug_anch) == 7 and span_wl == 24 and unmapped == 56
          and len(covered) == 132 and m["sp_codes_covered"] == 132
          and "4MA1-1.1A" in covered and "4MA1-5.1C" in covered
          and m["rows_worklist_unmapped_sps"] == 56
          and m["registry_size"] == 188 and m["rows_anchored"] == 838
          and m["rows_worklist_anchor_unresolved"] == 24
          and m["joins_resolved"] == 198 and m["joins_unresolved"] == 5
          and m["tool"] == TOOL_NEW
          and m["stage"].startswith("T-C42 R28:")
          and promo_keys_ok
          and m["promoted_rows"] == 831
          and base_doc["meta"]["promoted_rows"] == 832
          and set(m) == set(base_doc["meta"])
          and diff_keys == expected_diff
          and m["promotion_reapplied_by"] == f"{TOOL}@1.0.0")
    gate("B1_census_meta", b1,
         f"918 rows = 838 anchored (831 HUMAN_VALIDATED + 7 SUGGESTED) + 24 "
         f"unresolved-span + 56 uncovered-SP; covered 132/188 (gained "
         f"4MA1-1.1A + 4MA1-5.1C, the R26 projections landing); meta KEY "
         f"SETS identical to the R24-era baseline (it already carries the 4 "
         f"promotion_reapplied* keys) with the delta by VALUE == exactly the "
         f"8 census keys + promoted_rows RESTATED 832 -> 831 + the 4 "
         f"reapplied fields re-dated; the 7 other R5 promotion fields "
         f"byte-equal; tool {TOOL_NEW.split('@')[1]}")

    # ---- B2 re-attributions + DEMOTE ---------------------------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40  # norm() for id recompute
    moved_ok, landings = True, []
    for e in reattr:
        slug, oc = e["note_slug"], e["chunk_ordinal"]
        nrow = next((r for r in rows.values() if r.get("note_slug") == slug
                     and r.get("chunk", {}).get("ordinal") == oc), None)
        orow = next((r for r in base_rows.values()
                     if r.get("note_slug") == slug
                     and r.get("chunk", {}).get("ordinal") == oc), None)
        want_mid = hashlib.sha256(
            f"{nrow['note_path']}|{e['override_code']}|"
            f"{c40.norm(nrow['evidence_quote'])}".encode("utf-8")
        ).hexdigest()[:16]
        want_block = {
            "source": f"scripts/c42_section_overrides_r26.yaml@{map_sha}",
            "operator_round": ("C42 R26 (surface 3: 3 verdicted REATTRIBUTEs "
                               "+ the loop's fourth DEMOTE_TO_WORKLIST — the "
                               "FIRST of a promoted row)"),
            "action": "REATTRIBUTE",
            "provenance_class": "verdicted",
            "evidence": e["evidence"],
        }
        ok = (nrow is not None and orow is not None
              and orow["spec_code"] == e["current_code"]
              and nrow["spec_code"] == e["override_code"]
              and nrow["mapping_id"] == want_mid
              and nrow["sp_title"] == (registry[e["override_code"]]
                                       .get("official_wording") or "")
              and nrow["provenance"].get("override") == want_block
              and nrow["validation_status"] == "HUMAN_VALIDATED"
              and nrow.get("promotion") == r5.promotion_block())
        moved_ok = moved_ok and ok
        landings.append({"row": f"{slug}::{oc}",
                         "from": e["current_code"],
                         "to": e["override_code"],
                         "mapping_id_old": orow["mapping_id"] if orow else None,
                         "mapping_id_new": nrow["mapping_id"] if nrow else None,
                         "pass": ok})
    # the DEMOTE landing
    dslug, docc = demote_e["note_slug"], demote_e["chunk_ordinal"]
    dnrow = next((r for r in rows.values() if r.get("note_slug") == dslug
                  and r.get("chunk", {}).get("ordinal") == docc), None)
    dorow = next((r for r in base_rows.values()
                  if r.get("note_slug") == dslug
                  and r.get("chunk", {}).get("ordinal") == docc), None)
    want_did = hashlib.sha256(
        f"demoted|{dnrow['note_path']}|{docc}".encode("utf-8")
    ).hexdigest()[:16] if dnrow else None
    want_dblock = {
        "source": f"scripts/c42_section_overrides_r26.yaml@{map_sha}",
        "operator_round": ("C42 R26 (surface 3: 3 verdicted REATTRIBUTEs "
                           "+ the loop's fourth DEMOTE_TO_WORKLIST — the "
                           "FIRST of a promoted row)"),
        "action": "DEMOTE_TO_WORKLIST",
        "evidence": demote_e["evidence"],
    }
    demote_ok = (dnrow is not None and dorow is not None
                 and dorow["spec_code"] == demote_e["current_code"]
                 and dorow["validation_status"] == "HUMAN_VALIDATED"
                 and dnrow.get("spec_code") is None
                 and dnrow["mapping_id"] == want_did
                 and "sp_title" not in dnrow and "anchor" not in dnrow
                 and dnrow["provenance"].get("override") == want_dblock
                 and (dnrow.get("worklist_reason") or "").startswith(
                     "DEMOTE_TO_WORKLIST per the C42 R26")
                 and "(C42 R26 surface 3 demote)" in (dnrow.get("disposition") or "")
                 and dnrow["validation_status"] == "SUGGESTED"
                 and "promotion" not in dnrow
                 and dnrow["chunk"] == dorow["chunk"])
    b2 = moved_ok and demote_ok and len(landings) == 3
    gate("B2_reattributions_demote", b2,
         f"4/4 map rows landed verbatim: "
         f"{', '.join(l['from'] + '->' + l['to'] for l in landings)} + the "
         f"DEMOTE ({demote_e['current_code']} -> unresolved-span, demoted id "
         f"{want_did}); old ids == the R26 map's rows; "
         f"provenance.override == the map blocks (map sha {map_sha}); the 3 "
         f"REATTRIBUTE rows HUMAN_VALIDATED at the amended codes with "
         f"byte-stable blocks; the DEMOTE row SUGGESTED, no promotion block")

    # ---- B3 promotions two-way UNDER THE AMENDMENT ---------------------------------
    sup_by_id = {e.get("mapping_id"): e for e in amend.get("supersedes_code") or []}
    exc_by_id = {e.get("mapping_id"): e for e in amend.get("excluded") or []}
    pair_by_old = {l["mapping_id_old"]: l["mapping_id_new"] for l in landings}
    seen = {}
    problems = []
    n_sampled = 0
    for n, e in enumerate(pentries):
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        if not mid or mid in seen:
            problems.append(f"entry[{n}] identity")
            continue
        seen[mid] = e
        by = e.get("validated_by")
        if by != "operator" or r5.AI_PAT.search(by or ""):
            problems.append(f"entry[{n}] attribution")
        if mid in exc_by_id:
            continue
        if mid in sup_by_id:
            target_id = pair_by_old.get(mid)
            want_code = sup_by_id[mid].get("amended_code")
        else:
            target_id = mid
            want_code = row.get("spec_code")
        trow = rows.get(target_id)
        if trow is None:
            problems.append(f"entry[{n}] no store row")
            continue
        if (trow.get("spec_code") != want_code
                or trow.get("note_path") != row.get("note_path")
                or trow["chunk"]["ordinal"] != row.get("chunk_ordinal")
                or trow["chunk"]["heading"] != row.get("heading")
                or trow["chunk"]["sha256_16"] != row.get("chunk_sha256_16")):
            problems.append(f"entry[{n}] identity drift")
        if trow.get("validation_status") != "HUMAN_VALIDATED":
            problems.append(f"entry[{n}] not flipped")
        if trow.get("promotion") != r5.promotion_block():
            problems.append(f"entry[{n}] block drift")
        if "verdict" in e:
            n_sampled += 1
            if e["verdict"] != "CONFIRM" or mid not in vconf:
                problems.append(f"entry[{n}] sampled verdict")
    # old->new REATTRIBUTE translation: the promoted set excludes both shapes
    new_reject = set()
    hold_ids = set()
    by_ident = {ident(r): r for r in rows.values() if "chunk" in r}
    # the R22 REJECT rows: identified via the R22 map's (note_slug, ordinal)
    # keys — they sit at their R24-era ids in BOTH the baseline and the
    # committed store (the R26 round did not move them)
    ov22c = yaml.safe_load((HERE / "c42_section_overrides_r22.yaml")
                           .read_text(encoding="utf-8"))
    keyed_all = {(rw.get("note_slug"),
                  (rw.get("chunk") or {}).get("ordinal")): rw
                 for rw in store_doc["rows"] if "chunk" in rw}
    keyed_base_all = {(rw.get("note_slug"),
                       (rw.get("chunk") or {}).get("ordinal")): rw
                      for rw in base_doc["rows"] if "chunk" in rw}
    for e22 in (ov22c.get("overrides") or []):
        k22 = (e22.get("note_slug"), int(e22.get("chunk_ordinal")))
        nrow22 = keyed_all.get(k22)
        brow22 = keyed_base_all.get(k22)
        if (nrow22 is None or brow22 is None
                or nrow22["mapping_id"] not in sug_anch
                or nrow22["spec_code"] != e22["override_code"]
                or brow22["spec_code"] != e22["override_code"]):
            problems.append(f"R22 REJECT row drift {k22}")
        else:
            new_reject.add(nrow22["mapping_id"])
    for mid in vhold:
        hold_ids.add(by_ident[ident(base_rows[mid])]["mapping_id"])
    residue_ok = sug_anch == new_reject | hold_ids
    wl = {mid for mid, r in rows.items() if r.get("worklist_reason")}
    hv_targets = set()
    for mid, e in seen.items():
        if mid in exc_by_id:
            continue
        hv_targets.add(pair_by_old.get(mid, mid))
    b3 = (len(seen) == 832 == len(pentries) and len(hv) == 831
          and hv_targets == hv and n_sampled == 457 and not problems
          and residue_ok
          and not (hv & (new_reject | hold_ids | wl))
          and demote_e["mapping_id"] in exc_by_id
          and len(exc_by_id) == 1
          and vconf <= seen.keys()
          and promo_sha == r5rec["promotion_record"]["sha256_16"]
          == amend.get("base_file_sha256_16")
          and r5rec["promotion_record"]["entries"] == 832)
    gate("B3_promotions_two_way", b3,
         f"store <-> file+amendment 831 == 831 exact identities (828 direct + "
         f"3 superseded re-keyed old->new at the AMENDED codes); the excluded "
         f"DEMOTE row NOT promoted (unresolved-span worklist); validated_by "
         f"operator everywhere; sampled 457 == the R21 CONFIRM set; every "
         f"applied block == the R5 tool's block shape; the SUGGESTED anchored "
         f"residue == 3 R22 REJECTs + 4 H3 HOLDs; promotions file sha "
         f"{promo_sha} == the R5 record's pin == the amendment's base pin"
         + (f"; PROBLEMS {problems[:4]}" if problems else ""))

    # ---- B4 structural re-proof vs the baseline blob ---------------------------------
    base_chunk = {ident(r): r for r in base_doc["rows"] if "chunk" in r}
    fin_chunk = {ident(r): r for r in store_doc["rows"] if "chunk" in r}
    moved_keys = {(l["row"].split("::")[0], int(l["row"].split("::")[1]))
                  for l in landings}
    demote_key = (dslug, docc)

    def key_slug(k):
        # the check keys landings by note STEM; map to the row's note_path
        return k

    drift = []
    if set(base_chunk) != set(fin_chunk) or len(fin_chunk) != 862:
        drift.append("chunk-identity set")
    for k, brow in base_chunk.items():
        frow = fin_chunk[k]
        stem = Path(k[0]).stem
        is_reattr = any(stem == mk[0] and k[1] == mk[1] for mk in moved_keys)
        is_demote = (stem == demote_key[0] and k[1] == demote_key[1])
        if is_demote:
            if frow.get("validation_status") != "SUGGESTED" or \
                    "promotion" in frow or frow.get("spec_code") is not None:
                drift.append(f"demote final shape {k}")
            continue
        if frow.get("validation_status") != brow.get("validation_status"):
            drift.append(f"status {k}")
        if is_reattr:
            continue
        if strip_tool(brow) != strip_tool(frow):
            drift.append(f"non-tool delta {k}")
        elif brow["provenance"]["tool"] != TOOL_OLD or \
                frow["provenance"]["tool"] != TOOL_NEW:
            drift.append(f"tool swap {k}")
    base_nc = {r["mapping_id"]: r for r in base_doc["rows"]
               if "chunk" not in r}
    fin_nc = {r["mapping_id"]: r for r in store_doc["rows"]
              if "chunk" not in r}
    defer_ids = {sha16("unmapped|4MA1-1.1A"), sha16("unmapped|4MA1-5.1C")}
    if set(fin_nc) != set(base_nc) - defer_ids:
        drift.append("non-chunk set shape")
    for mid, brow in base_nc.items():
        frow = fin_nc.get(mid)
        if frow is None:
            continue
        if strip_tool(brow) != strip_tool(frow) or \
                brow["provenance"]["tool"] != TOOL_OLD or \
                frow["provenance"]["tool"] != TOOL_NEW:
            drift.append(f"nonchunk {mid}")
    # the 828 non-moved HV rows: tool-string-only delta with byte-equal blocks
    moved_old_ids = {l["mapping_id_old"] for l in landings}
    hv_only_tool = all(
        strip_tool(base_rows[mid]) == strip_tool(rows[mid])
        and base_rows[mid]["provenance"]["tool"] == TOOL_OLD
        and rows[mid]["provenance"]["tool"] == TOOL_NEW
        and rows[mid]["promotion"] == base_rows[mid]["promotion"]
        for mid in hv if mid not in {pair_by_old[o] for o in moved_old_ids})
    b4 = not drift and hv_only_tool and len(rows) == 918
    gate("B4_structural_reproof", b4,
         f"vs baseline blob {BASELINE[:12]}: chunk-identity set identical "
         f"(862); the 828 non-moved promoted rows differ ONLY in "
         f"provenance.tool (@2.5.0 -> @2.6.0) with byte-equal promotion "
         f"blocks; the 3 re-attributed + 1 DEMOTED rows carry exactly the "
         f"enumerated fields (the DEMOTE's status change "
         f"HUMAN_VALIDATED -> SUGGESTED recorded); the 1.1A + 5.1C DEFER rows "
         f"are the only vanishing rows (920 -> 918)"
         + (f"; DRIFT {drift[:4]}" if drift else ""))

    # ---- B5 protected surfaces ----------------------------------------------------------
    prot = []

    def prot_moved(p: str) -> str:
        # sparse-proof: the committed state must equal the baseline blob;
        # when the file is materialized on disk it must ALSO match (B8
        # separately guarantees no dirt). Returns "", "MISSING", or "MOVED".
        try:
            head_blob = blob_at("HEAD", p)
        except subprocess.CalledProcessError:
            return "MISSING"
        if head_blob != blob_at(BASELINE, p):
            return "MOVED"
        fp = REPO / p
        return "MOVED" if fp.is_file() and fp.read_bytes() != head_blob \
            else ""

    prot, missing = [], []
    for p in PROTECTED:
        verdict = prot_moved(p)
        if verdict == "MOVED":
            prot.append(p)
        elif verdict == "MISSING":
            missing.append(p)
    res_rel = PROTECTED[0]
    res_blob = subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "HEAD", res_rel],
        capture_output=True, text=True, check=True).stdout.split()[2]
    res16 = res_blob[:16]
    b5 = not prot and not missing and res16 == RES_BLOB
    gate("B5_protected_surfaces", b5,
         f"{len(PROTECTED)} protected surfaces byte-identical to the "
         f"baseline (the resolution substrate pin {RES_BLOB} re-verified; "
         f"the R5/R21/R22/R23/R24/R25/R26/R27 records + tools, the six "
         f"earlier maps + the R26 map + the amendment, the promotions file, "
         f"the R27 join records + generator, Lane C, chemistry, the "
         f"registry)"
         + (f"; MOVED {prot[:4]}" if prot else "")
         + (f"; MISSING {missing[:4]}" if missing else ""))

    # ---- B6 determinism -------------------------------------------------------------------
    d1 = c40.construct()
    d2 = c40.construct()
    g7 = yaml.safe_dump(d1, allow_unicode=True, sort_keys=False,
                        width=100) == yaml.safe_dump(
        d2, allow_unicode=True, sort_keys=False, width=100)
    b6 = (g7 and c40.TOOL_VERSION == "2.6.0"
          and sha16(store_bytes) == rec["store_sha256_16_post"])
    gate("B6_determinism", b6,
         f"the amended c40 tool constructs twice byte-identically (G7); "
         f"TOOL_VERSION 2.6.0; the store sha {sha16(store_bytes)} == the "
         f"record's post pin")

    # ---- B7 standing pins ------------------------------------------------------------------
    join = json.loads((REPO / JOIN_REL).read_text(encoding="utf-8"))
    jby_anchor = {j["anchor_id"]: j for j in join["joins"]}
    pins_ok = True
    for a in adj:
        jrow = jby_anchor.get(a["anchor_id"])
        if (a["ruling"] != "STANDING" or jrow is None
                or jrow["store_row_code"] != a["joined_code"]
                or not jrow["note_path"].endswith(f"/{a['note_slug']}.json")):
            pins_ok = False
    ov22 = yaml.safe_load((REPO / "scripts/c42_section_overrides_r22.yaml")
                          .read_text(encoding="utf-8"))
    for a in (ov22.get("note_level_adjudications") or []):
        jrow = jby_anchor.get(a["anchor_id"])
        if (a.get("ruling") != "STANDING" or jrow is None
                or jrow["store_row_code"] != a["joined_code"]
                or not jrow["note_path"].endswith(f"/{a['note_slug']}.json")):
            pins_ok = False
    ov18 = yaml.safe_load((REPO / "scripts/c42_section_overrides_r18.yaml")
                          .read_text(encoding="utf-8"))
    r18adj = ov18.get("note_level_adjudications") or {}
    for slug, want_code, want_anchor in (
            ("converting-between-fdp", "4MA1-1.2G", "spcpt_8MpvS5pnYkf9QswF"),
            ("basic-angle-properties", "4MA1-4.1B", "spcpt_5FMXZMjqSZ3GK53q")):
        a = r18adj.get(slug) or {}
        jrow = next((j for j in join["joins"]
                     if j["note_path"].endswith(f"/{slug}.json")), None)
        if (a.get("ruling") != "THE NOTE-LEVEL JOIN TO "
                f"{want_code.split('-')[-1]} STANDS (unchanged)"
                or jrow is None or jrow["store_row_code"] != want_code
                or jrow["anchor_id"] != want_anchor):
            pins_ok = False
    cf = jby_anchor.get("spcpt_XWbj3PG2n8tdWF2w")
    rc = jby_anchor.get("spcpt_crKbmb6wVjM4yPJh")
    pins_ok = pins_ok and cf and cf["store_row_code"] == "4MA1-3.2D" \
        and rc and rc["store_row_code"] == "4MA1-1.8D"
    b7 = pins_ok and len(adj) == 4
    gate("B7_standing_pins", b7,
         f"the FOUR R26 STANDING joins verified against the R26 map's own "
         f"list-shaped adjudications (ruling + anchor + landed code): "
         f"{'; '.join(a['note_slug'] + '->' + a['joined_code'] for a in adj)}; "
         f"the R22 trio + the R18 pair + the R14 re-point (3.2D) + the R10 "
         f"STANDING (1.8D) re-verified in the R27-refreshed join")

    # ---- B8 commit state ---------------------------------------------------------------------
    committed_delta = set()
    if not pre_commit:
        names = subprocess.run(
            ["git", "-C", str(REPO), "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, check=True).stdout.splitlines()
        committed_delta = {ln.strip() for ln in names if ln.strip()}
    b8 = (dirty == set()) if not pre_commit else (dirty <= FOOTPRINT)
    b8 = b8 and (pre_commit or committed_delta <= FOOTPRINT)
    gate("B8_commit_state", b8,
         f"{'PRE-COMMIT form: HEAD == baseline ' + BASELINE[:12] + ', dirt '
           if pre_commit else 'COMMITTED-CLEAN: working tree clean, HEAD '}"
         f"{'' if pre_commit else head[:12]} "
         f"{'within' if pre_commit else 'committed delta'} the declared R28 "
         f"footprint ({len(FOOTPRINT)} paths)")

    # ---- B9 anti-forgery sweep ------------------------------------------------------------------
    tiers_ok = all(r.get("provenance", {}).get("tier") == "RULE_DERIVED"
                   for r in rows.values())
    ai_ok = all(r["promotion"]["promoted_by"] == "operator"
                and not r5.AI_PAT.search(json.dumps(r["promotion"]))
                for mid, r in rows.items() if mid in hv)
    holds_untouched = all(
        rows[by_ident[ident(base_rows[mid])]["mapping_id"]]["spec_code"]
        == base_rows[mid]["spec_code"]
        and by_ident[ident(base_rows[mid])]["mapping_id"] not in hv
        for mid in vhold)
    dnrow_chk = next((r for r in rows.values()
                      if r.get("note_slug") == dslug
                      and r.get("chunk", {}).get("ordinal") == docc), None)
    demote_clean = (dnrow_chk is not None
                    and "promotion" not in dnrow_chk
                    and dnrow_chk.get("validation_status") == "SUGGESTED"
                    and dnrow_chk.get("worklist_reason"))
    b9 = tiers_ok and ai_ok and holds_untouched and len(hv) == 831 \
        and demote_clean
    gate("B9_anti_forgery", b9,
         f"provenance tiers RULE_DERIVED on all 918 rows; every "
         f"HUMAN_VALIDATED row promoted_by operator (AI-name patterns fail "
         f"closed); the 4 H3 HOLD rows untouched (ids + codes); the DEMOTE "
         f"row carries NO promotion block (SUGGESTED worklist); 831 == 831")

    # ---- B10 CI parity -----------------------------------------------------------------------------
    kg = subprocess.run(
        ["python3", str(REPO / "scripts/kg_export.py"), "--verify-golden"],
        capture_output=True, text=True)
    gc = subprocess.run(["python3", str(REPO / "scripts/graph_check.py")],
                        capture_output=True, text=True)
    gc_out = gc.stdout + gc.stderr
    gclines = [ln for ln in gc_out.splitlines() if ln.strip()]
    store_named = [ln for ln in gclines if "spec_chunk_mappings" in ln]
    all_pass_summary = any(ln.startswith("graph_check: ALL PASS")
                           for ln in gclines)
    fail_lines = [ln for ln in gclines
                  if not ln.startswith("graph_check:")
                  and not ln.startswith("PASS ")]
    # parity with the rebuild lane's own R10 gate: the pre/post failure-line
    # census was recorded IDENTICAL there; this battery re-verifies the
    # committed state's census is the clean ALL-PASS one with zero lines
    # naming the chunk store
    r10_parity = rec.get("ci_parity", {}).get("graph_check", "").startswith(
        "failure census identical")
    b10 = (kg.returncode == 0 and all_pass_summary and not fail_lines
           and not store_named and r10_parity)
    gate("B10_ci_parity", b10,
         f"kg_export --verify-golden exit {kg.returncode} (golden gate "
         f"GREEN); graph_check summary ALL PASS with {len(gclines)} output "
         f"lines, ZERO failure lines and ZERO lines naming the chunk store "
         f"(this workspace's census: the R24-era '1694 environmental "
         f"failures' pin belonged to a different workspace state — the "
         f"parity discipline is pre/post census IDENTITY, recorded by the "
         f"lane's R10 gate and re-verified here: {r10_parity})")

    # ---------------------------------------------------------------- emit report
    all_pass = all(g["pass"] for g in gates.values())
    out = {
        "schema": "syllabai.c42-r28-rebuild-check/1.0",
        "task": "T-C42 R28 (substrate re-build consuming the R26 override map "
                "AND the R26 promotions amendment over the rebuilt store; the "
                "R29 re-gate NOT fired)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "all_pass": all_pass,
        "gates": gates,
        "pins": {
            "baseline": BASELINE,
            "head": head,
            "pre_commit_form": pre_commit,
            "store_sha256_16": sha16(store_bytes),
            "store_sha256_16_pre_baseline": rec["store_sha256_16_pre"],
            "map26_sha256_16": map_sha,
            "amendment_sha256_16": sha16(AMENDMENT.read_bytes()),
            "promotions_sha256_16": promo_sha,
            "resolution_blob_sha16": res16,
            "rows": 918,
            "anchored": 838,
            "human_validated": 831,
            "suggested_anchored_residue": sorted(sug_anch),
            "unresolved_span": 24,
            "uncovered_sp": 56,
            "covered_codes": 132,
            "coverage_gained": ["4MA1-1.1A", "4MA1-5.1C"],
            "coverage_lost": [],
            "landings": landings,
            "demote_landing": {"from": demote_e["current_code"],
                               "mapping_id_old": dorow["mapping_id"],
                               "mapping_id_new": want_did},
            "promoted_rows_meta_restated": "832 -> 831",
            "tool_version_move": f"{TOOL_OLD.split('@')[1]} -> "
                                 f"{TOOL_NEW.split('@')[1]}",
        },
    }
    (REPO / "graph/reports/C42_R28_REBUILD_CHECK.json").write_text(
        json.dumps(out, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print("C42 R28 REBUILD CHECK —",
          "ALL PASS" if all_pass else "FAILURES PRESENT")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
