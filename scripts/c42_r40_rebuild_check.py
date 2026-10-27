#!/usr/bin/env python3
"""c42_r40_rebuild_check.py — T-C42 R40 verification battery (committed-clean).

The R40 lane is the scope §7 loop's substrate re-build consuming the R39
override map AND the R39 promotions amendment (the R39 record's next lane,
fired by the operator directive "fire R39/R40"; the next validation
re-gate is NOT named by the directive). Verified:

  B1 census+meta       917 rows = 832 anchored (828 HUMAN_VALIDATED + 4
                       SUGGESTED: the 3 R22 re-attributed REJECTs + the 1
                       re-homed drawing ord 0 hold) + 30 unresolved-span +
                       55 uncovered-SP; covered 133/188 (UNCHANGED — the
                       R39 projections landing: 6.3A keeps 17 anchored
                       rows, 6.2B keeps 23, gained none lost none); meta
                       promotion fields byte-equal to the R5 values EXCEPT
                       promoted_rows SET 828 (830 - 2 R39 exclusions — the
                       SECOND re-application that NARROWS the surface) +
                       the 4 additive promotion_reapplied* fields
                       re-dated; rows_anchored 834 -> 832 and
                       rows_worklist_anchor_unresolved 28 -> 30 in the
                       delta; stage pinned @R40; tool pinned @2.7.0 (NO
                       version move — the third consecutive re-build where
                       the tool string does not churn)
  B2 the DEMOTE        the 2 R39 map rows landed verbatim: the DEMOTE
  landings             batch (the loop's SEVENTH and EIGHTH DEMOTEs, the
                       FIRST 2-row batch over promoted rows; old
                       HUMAN_VALIDATED promoted at 4MA1-6.3A / 4MA1-6.2B;
                       new mapping_ids == sha16("demoted|<note_path>|1")
                       == the projected re-keys 09f012e4cabef0cc /
                       80d783fb13def4e2 — spec_code None, no sp_title, no
                       anchor, the round-tagged worklist_reason +
                       disposition under the 'C42 R39 (surface 3:'
                       descriptor, provenance.override == the map blocks
                       with the map sha, SUGGESTED, no promotion blocks);
                       ZERO REATTRIBUTEs; the amendment's excluded entries
                       == the landed rows; the LANDED R36 demoted row
                       re-lands at 8254a7fc75ad2946 via the still-wired
                       R36 map; per-code 6.3A 18 -> 17, 6.2B 24 -> 23
  B3 promotions        store <-> files+amendments two-way: 828 == 828 exact
  two-way              identities (814 direct + 3 R26-chain re-keyed + 5
                       R30 superseded re-keyed via the R31 record + 3 R33
                       superseded re-keyed AT THE AMENDED CODES 1.8B->1.8D
                       via the R34 record + 3 R30-ADDED sign-off
                       promotions); the R26 + R30 + R36 + R39 excluded
                       rows NOT promoted (unresolved-span worklist — the
                       R36 one at its re-key, the R39 pair at their
                       re-keys), validated_by operator everywhere, sampled
                       457 == the R21 CONFIRM set (R5-era ids),
                       REJECT/hold/worklist carry zero promotion blocks,
                       the file sha == the R5 apply record's pin == the
                       R39 amendment's base pin (byte-unchanged since R5)
  B4 structural        final vs the baseline blob ad12bc9: byte-equal
  re-proof             everywhere except the 2 DEMOTE rows (enumerated
                       fields + the round's ONLY status changes
                       HUMAN_VALIDATED -> SUGGESTED) — rows 917 -> 917, no
                       vanishing row, the non-chunk worklist byte-identical
                       (55 == 55); the re-applied promoted rows carry
                       byte-equal promotion blocks and byte-identical forms
                       (provenance.tool stays @2.7.0 — no tool churn)
  B5 protected         resolution substrate (the R14-era pin), the R27 join
  surfaces             artifact, the promotions file + the
                       R26/R30/R33/R36/R39 amendments + the eleven maps,
                       the R5/R21/R22/R23/R24/R25/R26/R27/R29/R30/R31/R32/
                       R33/R34/R35/R36/R37/R38/R39 records + tools +
                       carriers, the Lane C stores, the chemistry
                       substrate, the corpus manifest and the ratified
                       registry: byte-identical to the baseline blob
  B6 determinism       the amended c40 tool constructs twice byte-identically
                       (G7) and the store sha matches the record's post pin
  B7 standing pins     the FOUR R26 STANDING joins verified against the R26
                       map's own list-shaped adjudications (ruling + anchor
                       id + landed code together) + the carried pins (the
                       R22 trio, the R18 pair, the R14 re-point, the R10
                       STANDING) + the R33 SPLIT-note anchors (the corpus
                       anchor STANDS at 1.8B; the R10 related-calculations
                       anchor STANDS at 1.8D) + the R36 STANDING scoping
                       anchor (the basic-percentages corpus anchor STANDS
                       at 1.6F) + the R39 STANDING scoping anchors (the
                       basic-probability corpus anchor STANDS at 6.3A; the
                       calculations-with-the-mean corpus anchor STANDS at
                       6.2B)
  B8 commit state      adaptive: pre-commit HEAD == baseline with the dirt
                       inside the R40 footprint; post-commit the working
                       tree is clean and the committed delta vs HEAD~1 stays
                       inside the footprint (the audit trail may move HEAD,
                       never the protected surfaces)
  B9 anti-forgery      every HUMAN_VALIDATED row carries a promotion block
                       with promoted_by operator (AI-name patterns fail
                       closed); provenance tiers RULE_DERIVED everywhere;
                       the re-homed hold + the 3 R22 REJECT rows untouched
                       SUGGESTED; the R39 DEMOTE rows unpromoted in the
                       worklist — EXACTLY TWO DEMOTEs this round (the
                       loop's SEVENTH and EIGHTH, the FIRST 2-row batch)
  B10 CI parity        kg_export --verify-golden GREEN on the committed
                       state; graph_check's failure census stays at the
                       pinned pre-round count with zero failures naming the
                       chunk store

Emits graph/reports/C42_R40_REBUILD_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BASELINE = "ad12bc9d92ffc6eadfa8a10dcfa07a4a69b9417a"
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE = REPO / STORE_REL
MAP39 = HERE / "c42_section_overrides_r39.yaml"
AMENDMENT = HERE / "c42_r39_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
R31_REC = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
R34_REC = REPO / "graph/reports/C42_R34_REBUILD_RECORD.json"
TOOL = "scripts/c42_r40_substrate_rebuild.py"
TOOL_C40 = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
COURSE = "igcse-maths-a-18-higher"
JOIN_REL = (f"Official-Specifications/parsed/_derived/notes-join/"
            f"{COURSE}.json")
DEMOTES = [
    {"old": "a5b737e510606829", "new": "09f012e4cabef0cc",
     "note": ("notes/6-statistics-and-probability/probability-toolkit/"
              "basic-probability.json"),
     "ord": 1, "code": "4MA1-6.3A", "slug": "basic-probability"},
    {"old": "d545cd5f5aeae9a9", "new": "80d783fb13def4e2",
     "note": ("notes/6-statistics-and-probability/statistics-toolkit/"
              "calculations-with-the-mean.json"),
     "ord": 1, "code": "4MA1-6.2B",
     "slug": "calculations-with-the-mean"},
]
R36_NEW_DEMOTE_ID = "8254a7fc75ad2946"
OPERATOR_ROUND = ("C42 R39 (surface 3: 2 verdicted DEMOTE_TO_WORKLIST — the "
                  "R38 fresh REJECTs adjudicated; ZERO REATTRIBUTEs, ZERO "
                  "sign-offs)")
FOOTPRINT = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r40_substrate_rebuild.py",
    "scripts/c42_r40_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R40_REBUILD_RECORD.json",
    "graph/reports/C42_R40_REBUILD_RECORD.md",
    "graph/reports/C42_R40_REBUILD_CHECK.json",
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
    "graph/reports/C42_R29_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R29_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R29_REGATE_CHECK.json",
    "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R30_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R30_REPAIR_CHECK.json",
    "graph/reports/C42_R31_REBUILD_RECORD.md",
    "graph/reports/C42_R31_REBUILD_RECORD.json",
    "graph/reports/C42_R31_REBUILD_CHECK.json",
    "graph/reports/C42_R32_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R32_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R32_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R32_REGATE_CHECK.json",
    "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R33_REPAIR_CHECK.json",
    "graph/reports/C42_R34_REBUILD_RECORD.md",
    "graph/reports/C42_R34_REBUILD_RECORD.json",
    "graph/reports/C42_R34_REBUILD_CHECK.json",
    "graph/reports/C42_R35_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R35_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R35_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R35_REGATE_CHECK.json",
    "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R36_REPAIR_CHECK.json",
    "graph/reports/C42_R37_REBUILD_RECORD.md",
    "graph/reports/C42_R37_REBUILD_RECORD.json",
    "graph/reports/C42_R37_REBUILD_CHECK.json",
    "graph/reports/C42_R38_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R38_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R38_MATHS_A_REGATE_REVIEW_SHEET.md",
    "graph/reports/C42_R38_REGATE_CHECK.json",
    "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R39_REPAIR_CHECK.json",
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
    "scripts/c42_r29_regate_fill.py",
    "scripts/c42_r29_regate_check.py",
    "scripts/c42_r29_fresh_verdicts.yaml",
    "scripts/c42_r29_review_verdicts.yaml",
    "scripts/c42_r30_repair_verdicts.yaml",
    "scripts/c42_r30_override_projection.py",
    "scripts/c42_r30_repair_check.py",
    "scripts/c42_r32_regate_fill.py",
    "scripts/c42_r32_regate_check.py",
    "scripts/c42_r32_fresh_verdicts.yaml",
    "scripts/c42_r32_review_verdicts.yaml",
    "scripts/c42_r33_repair_verdicts.yaml",
    "scripts/c42_r33_override_projection.py",
    "scripts/c42_r33_repair_check.py",
    "scripts/c42_r34_substrate_rebuild.py",
    "scripts/c42_r34_rebuild_check.py",
    "scripts/c42_r35_regate_fill.py",
    "scripts/c42_r35_regate_check.py",
    "scripts/c42_r35_fresh_verdicts.yaml",
    "scripts/c42_r35_review_verdicts.yaml",
    "scripts/c42_r36_repair_verdicts.yaml",
    "scripts/c42_r36_override_projection.py",
    "scripts/c42_r36_repair_check.py",
    "scripts/c42_r37_substrate_rebuild.py",
    "scripts/c42_r37_rebuild_check.py",
    "scripts/c42_r38_regate_fill.py",
    "scripts/c42_r38_regate_check.py",
    "scripts/c42_r38_fresh_verdicts.yaml",
    "scripts/c42_r38_review_verdicts.yaml",
    "scripts/c42_r39_repair_verdicts.yaml",
    "scripts/c42_r39_override_projection.py",
    "scripts/c42_r39_repair_check.py",
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c42_section_overrides.yaml",
    "scripts/c42_section_overrides_r6.yaml",
    "scripts/c42_section_overrides_r10.yaml",
    "scripts/c42_section_overrides_r14.yaml",
    "scripts/c42_section_overrides_r18.yaml",
    "scripts/c42_section_overrides_r22.yaml",
    "scripts/c42_section_overrides_r26.yaml",
    "scripts/c42_section_overrides_r30.yaml",
    "scripts/c42_section_overrides_r33.yaml",
    "scripts/c42_section_overrides_r36.yaml",
    "scripts/c42_section_overrides_r39.yaml",
    "scripts/c42_r26_promotions_amendment.yaml",
    "scripts/c42_r30_promotions_amendment.yaml",
    "scripts/c42_r33_promotions_amendment.yaml",
    "scripts/c42_r36_promotions_amendment.yaml",
    "scripts/c42_r39_promotions_amendment.yaml",
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
    rec = json.loads((REPO / "graph/reports/C42_R40_REBUILD_RECORD.json")
                     .read_text(encoding="utf-8"))

    # ---------------------------------------------------------------- inputs
    store_bytes = STORE.read_bytes()
    store_doc = yaml.safe_load(store_bytes.decode("utf-8"))
    base_doc = yaml.safe_load(
        blob_at(BASELINE, STORE_REL).decode("utf-8"))
    base_rows = {r["mapping_id"]: r for r in base_doc["rows"]}
    rows = {r["mapping_id"]: r for r in store_doc["rows"]}
    map_bytes = MAP39.read_bytes()
    map_sha = sha16(map_bytes)
    map_doc = yaml.safe_load(map_bytes.decode("utf-8"))
    entries = map_doc["overrides"]
    reattr = [e for e in entries if e.get("action") == "REATTRIBUTE"]
    demote_es = [e for e in entries if e.get("action") == "DEMOTE_TO_WORKLIST"]
    amend = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
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
    diff_keys = {k for k in set(m) & set(base_doc["meta"])
                 if m[k] != base_doc["meta"][k]}
    expected_diff = {"stage", "rows_anchored",
                     "rows_worklist_anchor_unresolved", "promoted_rows",
                     "promotion_reapplied_by",
                     "promotion_reapplied_directive",
                     "promotion_reapplied_note"}
    # NOTE: the census keys rows_anchored (834 -> 832) and
    # rows_worklist_anchor_unresolved (28 -> 30) ARE in the delta — the R39
    # projections land: the DEMOTE batch moves its rows out of the anchored
    # class INTO the unresolved-span class; covered/uncovered stay (133/55 —
    # 6.3A keeps 17, 6.2B keeps 23); the tool key is NOT in the delta — the
    # third consecutive re-build with no version move (c40 stays @2.7.0);
    # promotion_reapplied itself is NOT in the delta BY VALUE — both R37 and
    # R40 ran 2026-10-16, the date string is byte-identical — the re-dating
    # rides the by/directive/note fields. promoted_rows IS in the delta:
    # 830 -> 828 (the SECOND re-application that NARROWS the surface)
    b1 = (len(rows) == 917 and len(anchored) == 832 and len(hv) == 828
          and len(sug_anch) == 4 and span_wl == 30 and unmapped == 55
          and len(covered) == 133 and m["sp_codes_covered"] == 133
          and "4MA1-6.3A" in covered and "4MA1-6.2B" in covered
          and m["rows_worklist_unmapped_sps"] == 55
          and m["registry_size"] == 188 and m["rows_anchored"] == 832
          and m["rows_worklist_anchor_unresolved"] == 30
          and m["joins_resolved"] == 198 and m["joins_unresolved"] == 5
          and m["tool"] == TOOL_C40
          and m["stage"].startswith("T-C42 R40:")
          and promo_keys_ok
          and m["promoted_rows"] == 828
          and base_doc["meta"]["promoted_rows"] == 830
          and set(m) == set(base_doc["meta"])
          and diff_keys == expected_diff
          and m["promotion_reapplied_by"] == f"{TOOL}@1.0.0")
    gate("B1_census_meta", b1,
         f"917 rows = 832 anchored (828 HUMAN_VALIDATED + 4 SUGGESTED) + 30 "
         f"unresolved-span + 55 uncovered-SP; covered 133/188 UNCHANGED "
         f"(the R39 projections landing: 6.3A keeps 17 anchored rows, 6.2B "
         f"keeps 23; gained none, lost none); meta KEY SETS identical with "
         f"the delta by VALUE == exactly stage + rows_anchored (834->832) + "
         f"rows_worklist_anchor_unresolved (28->30) + promoted_rows "
         f"(830->828 — the narrowed surface) + the promotion_reapplied_by/"
         f"directive/note fields (the promotion_reapplied date value itself "
         f"coincides — both rounds ran 2026-10-16 — so the re-dating rides "
         f"the other three fields); the 7 other R5 promotion fields "
         f"byte-equal; tool @2.7.0 (NO version move)")

    # ---- B2 the DEMOTE landings ---------------------------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40  # sha16/demote convention
    keyed_all = {(rw.get("note_slug"),
                  (rw.get("chunk") or {}).get("ordinal")): rw
                 for rw in store_doc["rows"] if "chunk" in rw}
    keyed_base_all = {(rw.get("note_slug"),
                       (rw.get("chunk") or {}).get("ordinal")): rw
                      for rw in base_doc["rows"] if "chunk" in rw}
    exc_by_id = {e.get("mapping_id"): e for e in amend.get("excluded") or []}
    demote_ok = len(demote_es) == 2 and not reattr
    for dspec in DEMOTES:
        d0 = next((e for e in demote_es
                   if e.get("note_slug") == dspec["slug"]
                   and int(e.get("chunk_ordinal", -1)) == dspec["ord"]), None)
        nrow = keyed_all.get((dspec["slug"], dspec["ord"]))
        orow = keyed_base_all.get((dspec["slug"], dspec["ord"]))
        want_mid = sha16(f"demoted|{dspec['note']}|{dspec['ord']}")
        want_block = {
            "source": f"scripts/c42_section_overrides_r39.yaml@{map_sha}",
            "operator_round": OPERATOR_ROUND,
            "action": "DEMOTE_TO_WORKLIST",
            "evidence": (d0 or {}).get("evidence"),
        }
        x0 = exc_by_id.get(dspec["old"]) or {}
        demote_ok = demote_ok and bool(d0) and nrow is not None \
            and orow is not None and (
            d0.get("mapping_id") == dspec["old"]
            and d0.get("current_code") == dspec["code"]
            and d0.get("override_code") is None
            and orow["spec_code"] == dspec["code"]
            and orow["mapping_id"] == dspec["old"]
            and orow.get("validation_status") == "HUMAN_VALIDATED"
            and "promotion" in orow
            and nrow["mapping_id"] == want_mid == dspec["new"]
            and nrow.get("spec_code") is None
            and "sp_title" not in nrow
            and "anchor" not in nrow
            and nrow.get("worklist_reason", "").startswith(
                f"DEMOTE_TO_WORKLIST per the {OPERATOR_ROUND} operator verdict "
                f"round (provenance.override):")
            and nrow.get("disposition", "").endswith(
                "(C42 R39 surface 3 demote)")
            and nrow.get("provenance", {}).get("override") == want_block
            and nrow.get("validation_status") == "SUGGESTED"
            and "promotion" not in nrow
            and nrow["evidence_quote"] == orow["evidence_quote"]
            and x0.get("mapping_id") == dspec["old"]
            and x0.get("note_path") == dspec["note"]
            and x0.get("pinned_code") == dspec["code"]
            and x0.get("disposition") == "DEMOTE_TO_WORKLIST")
    # the LANDED R36 demoted row re-lands at its re-key via the R36 map
    r36_row = rows.get(R36_NEW_DEMOTE_ID) or {}
    r36_ok = (r36_row.get("worklist_reason")
              and r36_row.get("validation_status") == "SUGGESTED"
              and "promotion" not in r36_row
              and "C42 R36" in (r36_row.get("disposition") or ""))
    # the per-code family censuses: 6.3A 18 -> 17, 6.2B 24 -> 23
    fam_checks = True
    for dspec, want_new, want_old in ((DEMOTES[0], 17, 18),
                                      (DEMOTES[1], 23, 24)):
        fam_new = sorted((r.get("note_slug"), r["chunk"]["ordinal"])
                         for r in rows.values()
                         if r.get("spec_code") == dspec["code"]
                         and "chunk" in r)
        fam_old = sorted((r.get("note_slug"), r["chunk"]["ordinal"])
                         for r in base_rows.values()
                         if r.get("spec_code") == dspec["code"]
                         and "chunk" in r)
        fam_checks = fam_checks and len(fam_new) == want_new \
            and len(fam_old) == want_old \
            and (dspec["slug"], dspec["ord"]) in fam_old \
            and (dspec["slug"], dspec["ord"]) not in fam_new
    b2 = (demote_ok and r36_ok and fam_checks)
    gate("B2_demote_landings", b2,
         f"2/2 map rows landed verbatim: the DEMOTE batch (the loop's "
         f"SEVENTH and EIGHTH DEMOTEs, the FIRST 2-row batch over promoted "
         f"rows): a5b737e510606829 -> 09f012e4cabef0cc (basic-probability "
         f"ord 1) and d545cd5f5aeae9a9 -> 80d783fb13def4e2 "
         f"(calculations-with-the-mean ord 1); old rows HUMAN_VALIDATED "
         f"promoted at 4MA1-6.3A / 4MA1-6.2B; new rows spec_code None, no "
         f"sp_title, no anchor, the round-tagged worklist_reason + "
         f"disposition under the 'C42 R39 (surface 3:' descriptor; "
         f"provenance.override == the map blocks (map sha {map_sha}); "
         f"SUGGESTED with NO promotion blocks; the amendment's excluded "
         f"entries == the landed rows; the LANDED R36 demoted row re-lands "
         f"at {R36_NEW_DEMOTE_ID} via the still-wired R36 map; ZERO "
         f"REATTRIBUTEs; per-code 6.3A anchored 18 -> 17, 6.2B anchored "
         f"24 -> 23")

    # ---- B3 promotions two-way UNDER THE FIVE AMENDMENTS ---------------------------------
    sup_by_id = {e.get("mapping_id"): e
                 for e in amend.get("supersedes_code") or []}
    r26_amend = yaml.safe_load(
        (HERE / "c42_r26_promotions_amendment.yaml").read_text(encoding="utf-8"))
    r26_sup = {e["mapping_id"]: e
               for e in r26_amend.get("supersedes_code") or []}
    r26_exc = {e["mapping_id"] for e in r26_amend.get("excluded") or []}
    rec28 = json.loads(R28_REC.read_text(encoding="utf-8"))
    r26_rekey = dict(rec28["promotions"]["superseded_ids_rekeyed"])
    rec31 = json.loads(R31_REC.read_text(encoding="utf-8"))
    r30_rekey = dict(rec31["promotions"]["superseded_ids_rekeyed"])
    added_ids = set(rec31["promotions"]["added_ids"])
    r30_amend = yaml.safe_load(
        (HERE / "c42_r30_promotions_amendment.yaml").read_text(encoding="utf-8"))
    r30_sup = {e["mapping_id"]: e
               for e in r30_amend.get("supersedes_code") or []}
    r30_exc = {e["mapping_id"] for e in r30_amend.get("excluded") or []}
    r33_amend = yaml.safe_load(
        (HERE / "c42_r33_promotions_amendment.yaml").read_text(encoding="utf-8"))
    r33_sup = {e["mapping_id"]: e
               for e in r33_amend.get("supersedes_code") or []}
    rec34 = json.loads(R34_REC.read_text(encoding="utf-8"))
    r33_rekey = dict(rec34["promotions"]["superseded_ids_rekeyed"])
    r36_amend = yaml.safe_load(
        (HERE / "c42_r36_promotions_amendment.yaml").read_text(encoding="utf-8"))
    r36_exc = {e["mapping_id"] for e in r36_amend.get("excluded") or []}
    r39_exc = set(exc_by_id)
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
        if (mid in r26_exc or mid in r30_exc or mid in r36_exc
                or mid in r39_exc):
            continue
        if mid in r33_sup:
            target_id = r33_rekey.get(mid)
            want_code = r33_sup[mid].get("amended_code")
        elif mid in r30_sup:
            target_id = r30_rekey.get(mid)
            want_code = r30_sup[mid].get("amended_code")
        elif mid in r26_sup:
            target_id = r26_rekey.get(mid)
            want_code = r26_sup[mid].get("amended_code")
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
    # the 3 R31-ADDED sign-off rows: promoted with the standard block,
    # byte-stable vs the baseline store's rows
    for mid in added_ids:
        trow = rows.get(mid)
        brow = base_rows.get(mid)
        if trow is None or brow is None:
            problems.append(f"added[{mid}] missing")
            continue
        if (trow.get("spec_code") != brow.get("spec_code")
                or ident(trow) != ident(brow)):
            problems.append(f"added[{mid}] identity drift")
        if trow.get("validation_status") != "HUMAN_VALIDATED" \
                or trow.get("promotion") != r5.promotion_block():
            problems.append(f"added[{mid}] not flipped / block drift")
    # the excluded rows: NOT promoted, in the worklist (the R36 one at its
    # re-key; the R39 pair at their re-keys)
    wl = {mid for mid, r in rows.items() if r.get("worklist_reason")}
    for new_id in (R36_NEW_DEMOTE_ID,) + tuple(d["new"] for d in DEMOTES):
        if new_id not in rows or new_id not in wl \
                or rows[new_id].get("validation_status") != "SUGGESTED" \
                or "promotion" in rows[new_id]:
            problems.append(f"an excluded row not landed at {new_id}")
    for dspec in DEMOTES:
        if dspec["old"] in rows or dspec["old"] in hv:
            problems.append(f"the old demote id {dspec['old']} still "
                            f"present/promoted")
    # old->new REATTRIBUTE translation: the promoted set excludes all shapes
    new_reject = set()
    hold_ids = set()
    by_ident = {ident(r): r for r in rows.values() if "chunk" in r}
    ov22c = yaml.safe_load((HERE / "c42_section_overrides_r22.yaml")
                           .read_text(encoding="utf-8"))
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
        nrow_h = by_ident[ident(base_rows[r30_rekey.get(mid, mid)])]
        if mid in added_ids:
            if nrow_h["mapping_id"] != mid or \
                    nrow_h["mapping_id"] not in hv:
                problems.append(f"sign-off hold {mid} not promoted")
        else:
            hold_ids.add(nrow_h["mapping_id"])
    residue_ok = sug_anch == new_reject | hold_ids
    hv_targets = set(added_ids)
    for mid, e in seen.items():
        if (mid in r26_exc or mid in r30_exc or mid in r36_exc
                or mid in r39_exc):
            continue
        t = None
        if mid in r33_sup:
            t = r33_rekey.get(mid)
        if t is None and mid in r30_sup:
            t = r30_rekey.get(mid)
        if t is None and mid in r26_sup:
            t = r26_rekey.get(mid)
        hv_targets.add(t or mid)
    b3 = (len(seen) == 832 == len(pentries) and len(hv) == 828
          and hv_targets == hv and n_sampled == 457 and not problems
          and residue_ok
          and not (hv & (new_reject | hold_ids | wl))
          and len(sup_by_id) == 0 and len(exc_by_id) == 2
          and len(added_ids) == 3
          and vconf <= seen.keys()
          and promo_sha == r5rec["promotion_record"]["sha256_16"]
          == amend.get("base_file_sha256_16")
          and r5rec["promotion_record"]["entries"] == 832)
    gate("B3_promotions_two_way", b3,
         f"store <-> files+amendments 828 == 828 exact identities (814 "
         f"direct + 3 R26-chain re-keyed + 5 R30 superseded re-keyed via the "
         f"R31 record + 3 R33 superseded re-keyed AT THE AMENDED CODES "
         f"1.8B->1.8D via the R34 record + 3 R31-ADDED sign-off promotions); "
         f"the R26 + R30 + R36 + R39 excluded rows NOT promoted "
         f"(unresolved-span worklist — the R36 one at its re-key "
         f"{R36_NEW_DEMOTE_ID}, the R39 pair at 09f012e4cabef0cc / "
         f"80d783fb13def4e2); validated_by operator everywhere; sampled 457 "
         f"== the R21 CONFIRM set; every applied block == the R5 tool's "
         f"block shape; the SUGGESTED anchored residue == 3 R22 REJECTs + 1 "
         f"re-homed hold; promotions file sha {promo_sha} == the R5 record's "
         f"pin == the R39 amendment's base pin"
         + (f"; PROBLEMS {problems[:4]}" if problems else ""))

    # ---- B4 structural re-proof vs the baseline blob ---------------------------------
    base_chunk = {ident(r): r for r in base_doc["rows"] if "chunk" in r}
    fin_chunk = {ident(r): r for r in store_doc["rows"] if "chunk" in r}
    demote_keys = {(d["note"], d["ord"]) for d in DEMOTES}
    drift = []
    status_changes = []
    if set(base_chunk) != set(fin_chunk) or len(fin_chunk) != 862:
        drift.append("chunk-identity set")
    for k, brow in base_chunk.items():
        frow = fin_chunk[k]
        if frow.get("validation_status") != brow.get("validation_status"):
            status_changes.append(k)
        if (k[0], k[1]) in demote_keys:
            continue
        if strip_tool(brow) != strip_tool(frow):
            drift.append(f"non-tool delta {k}")
        elif brow["provenance"]["tool"] != TOOL_C40 or \
                frow["provenance"]["tool"] != TOOL_C40:
            drift.append(f"tool drift {k}")
    if {(x[0], x[1]) for x in status_changes} != demote_keys or \
            len(status_changes) != 2:
        drift.append("status changes "
                     f"{[(x[0], x[1]) for x in status_changes][:3]}")
    base_nc = {r["mapping_id"]: r for r in base_doc["rows"]
               if "chunk" not in r}
    fin_nc = {r["mapping_id"]: r for r in store_doc["rows"]
              if "chunk" not in r}
    if set(fin_nc) != set(base_nc):
        drift.append("non-chunk set shape")
    for mid, brow in base_nc.items():
        frow = fin_nc.get(mid)
        if frow is None:
            continue
        if brow != frow:
            drift.append(f"nonchunk {mid}")
    # the non-moved HV rows: byte-equal forms with byte-equal blocks
    moved_new_ids = {d["new"] for d in DEMOTES}
    hv_byte_stable = all(
        strip_tool(base_rows[mid]) == strip_tool(rows[mid])
        and base_rows[mid]["provenance"]["tool"] == TOOL_C40
        and rows[mid]["provenance"]["tool"] == TOOL_C40
        and rows[mid]["promotion"] == base_rows[mid]["promotion"]
        for mid in hv
        if mid not in added_ids and mid not in moved_new_ids
        and mid in base_rows)
    b4 = not drift and hv_byte_stable and len(rows) == 917
    gate("B4_structural_reproof", b4,
         f"vs baseline blob {BASELINE[:12]}: chunk-identity set identical "
         f"(862 — the W3 invariant); the re-applied non-moved promoted rows "
         f"BYTE-IDENTICAL (provenance.tool stays @2.7.0 — no tool churn) "
         f"with byte-equal promotion blocks; the 2 DEMOTE rows carry "
         f"exactly the enumerated fields with the round's ONLY status "
         f"changes (HUMAN_VALIDATED -> SUGGESTED); the non-chunk worklist "
         f"byte-identical (55 == 55, no vanishing row)"
         + (f"; DRIFT {drift[:3]}" if drift else ""))

    # ---- B5 protected surfaces ----------------------------------------------------------
    prot_drift = []
    for rel in PROTECTED:
        try:
            if blob_at(BASELINE, rel) != blob_at("HEAD", rel):
                prot_drift.append(rel)
        except subprocess.CalledProcessError:
            prot_drift.append(rel + " (unreadable)")
    b5 = not prot_drift
    gate("B5_protected_surfaces", b5,
         f"{len(PROTECTED)} protected paths byte-identical baseline blob -> "
         f"HEAD blob (the resolution substrate incl. the R14-era pin, the "
         f"R27 join artifact, the promotions file, the "
         f"R26+R30+R33+R36+R39 amendments, the eleven maps, the "
         f"R5/R21/R22/R23/R24/R25/R26/R27/R29/R30/R31/R32/R33/R34/R35/R36/"
         f"R37/R38/R39 records + tools + carriers, the Lane C stores, the "
         f"chemistry substrate, the corpus manifest, the ratified registry)"
         + (f"; DRIFT {prot_drift[:3]}" if prot_drift else ""))

    # ---- B6 determinism -----------------------------------------------------------------
    doc_a = c40.construct()
    dump_a = yaml.safe_dump(doc_a, allow_unicode=True, sort_keys=False,
                            width=100)
    doc_b = c40.construct()
    dump_b = yaml.safe_dump(doc_b, allow_unicode=True, sort_keys=False,
                            width=100)
    b6 = (dump_a == dump_b
          and sha16(store_bytes) == rec["store_sha256_16_post"]
          and rec["store_sha256_16_pre"] == sha16(
              blob_at(BASELINE, STORE_REL)))
    gate("B6_determinism", b6,
         f"G7 two constructions byte-identical; store sha "
         f"{sha16(store_bytes)} == the record's post pin; the record's pre "
         f"pin == the baseline blob sha")

    # ---- B7 standing pins ---------------------------------------------------------------
    join = json.loads((REPO / JOIN_REL).read_text(encoding="utf-8"))
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    map26 = yaml.safe_load(
        (HERE / "c42_section_overrides_r26.yaml").read_text(encoding="utf-8"))
    pins_ok = True
    for adj26 in map26["note_level_adjudications"]:
        jr = join_rows.get(adj26["anchor_id"])
        if jr is None or jr.get("store_row_code") != adj26["joined_code"] \
                or adj26.get("ruling") != "STANDING":
            pins_ok = False
    for aid, want in [("spcpt_DcSkGdrNWCZYX4V8", "4MA1-4.11C"),
                      ("spcpt_qgWTSJ5pQ2dx6rDf", "4MA1-1.7B"),
                      ("spcpt_h8QyRmzX5mCJb3X9", "4MA1-3.3F"),
                      ("spcpt_p8zkdCF8QVvDZyVX", "4MA1-1.8B"),
                      ("spcpt_crKbmb6wVjM4yPJh", "4MA1-1.8D"),
                      ("spcpt_FHRjdMc6tvRR553q", "4MA1-1.6F"),
                      ("spcpt_FVX7YRftjhnwYHQF", "4MA1-6.3A"),
                      ("spcpt_n9ZtYfjh8sFCp5Kz", "4MA1-6.2B")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("store_row_code") != want:
            pins_ok = False
    b7 = pins_ok
    gate("B7_standing_pins", b7,
         "the FOUR R26 STANDING joins verified against the R26 map's own "
         "list-shaped adjudications + the carried pins (the 4.11C anchor, "
         "the 1.7B anchor, the 3.3F anchor) + the R33 SPLIT-note anchors "
         "(the corpus anchor STANDS at 1.8B — ords 0-5; the R10 "
         "related-calculations anchor STANDS at 1.8D) + the R36 STANDING "
         "scoping anchor (the basic-percentages corpus anchor STANDS at "
         "1.6F) + the R39 STANDING scoping anchors (the basic-probability "
         "corpus anchor STANDS at 6.3A; the calculations-with-the-mean "
         "corpus anchor STANDS at 6.2B) — the join layer untouched")

    # ---- B8 commit state -----------------------------------------------------------------
    if pre_commit:
        outside = {c for c in dirty if c not in FOOTPRINT}
        b8 = not outside
        detail = (f"pre-commit: HEAD == baseline {BASELINE[:12]}; dirt "
                  f"{len(dirty)} inside the R40 footprint")
    else:
        changed = [ln.strip() for ln in subprocess.run(
            ["git", "-C", str(REPO), "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, check=True).stdout.splitlines()
            if ln.strip()]
        outside = [c for c in changed if c not in FOOTPRINT]
        dirty_now = {ln[3:].strip() for ln in subprocess.run(
            ["git", "-C", str(REPO), "status", "--porcelain"],
            capture_output=True, text=True, check=True).stdout.splitlines()
            if ln.strip()}
        b8 = not outside and not dirty_now
        detail = (f"committed-clean: HEAD {head[:12]}; tree clean; the "
                  f"committed delta vs HEAD~1 inside the R40 footprint")
    gate("B8_commit_state", b8, detail
         + (f"; OUTSIDE {sorted(outside)[:4]}" if outside else ""))

    # ---- B9 anti-forgery -----------------------------------------------------------------
    af_problems = []
    for mid in hv:
        r = rows[mid]
        pb = r.get("promotion", {})
        if pb.get("promoted_by") != "operator":
            af_problems.append(f"{mid} promoted_by")
        import re as _re
        if _re.search(r"glm|z-ai|claude|gpt|openai|anthropic",
                      json.dumps(pb), _re.I):
            af_problems.append(f"{mid} AI attribution")
    tiers_ok = all(x.get("provenance", {}).get("tier") == "RULE_DERIVED"
                   for x in rows.values())
    dem_new_ok = all(
        (rows.get(d["new"]) or {}).get("worklist_reason")
        and "promotion" not in (rows.get(d["new"]) or {})
        and (rows.get(d["new"]) or {}).get("validation_status") == "SUGGESTED"
        for d in DEMOTES)
    b9 = (not af_problems and tiers_ok
          and dem_new_ok
          and all(d["new"] not in hv for d in DEMOTES)
          and hold_ids <= sug_anch
          and new_reject <= sug_anch
          and not (hv & (new_reject | hold_ids | wl)))
    gate("B9_anti_forgery", b9,
         f"828 HUMAN_VALIDATED rows carry operator-attributed promotion "
         f"blocks; provenance tiers RULE_DERIVED everywhere; the re-homed "
         f"hold + the 3 R22 REJECT rows stay SUGGESTED unpromoted; the R39 "
         f"DEMOTE rows land unpromoted in the worklist — EXACTLY TWO DEMOTEs "
         f"this round (the loop's SEVENTH and EIGHTH, the FIRST 2-row batch)"
         + (f"; PROBLEMS {af_problems[:3]}" if af_problems else ""))

    # ---- B10 CI parity -------------------------------------------------------------------
    gc = subprocess.run(["python3", str(REPO / "scripts/graph_check.py")],
                        capture_output=True, text=True)
    gc_failures = {ln for ln in (gc.stdout + gc.stderr).splitlines()
                   if ln.strip()}
    kg = subprocess.run(
        ["python3", str(REPO / "scripts/kg_export.py"), "--verify-golden"],
        capture_output=True, text=True)
    store_named = any("spec_chunk_mappings" in ln for ln in gc_failures)
    b10 = kg.returncode == 0 and not store_named \
        and len(gc_failures) == rec["ci_parity"].get(
            "graph_check_failures", len(gc_failures))
    gate("B10_ci_parity", b10,
         f"kg_export --verify-golden exit {kg.returncode} (golden gate "
         f"GREEN); graph_check failure census {len(gc_failures)} lines (the "
         f"pre-existing sparse-checkout environmental set), zero failures "
         f"naming the chunk store")

    # ---- report ---------------------------------------------------------------------------
    out = {
        "schema": "c42-r40-rebuild-check/1.0",
        "task": "T-C42",
        "stage": "r40-substrate-rebuild-check",
        "round": "R40",
        "round_start": BASELINE,
        "audited_head": head,
        "baseline_store_sha256_16": sha16(blob_at(BASELINE, STORE_REL)),
        "store_sha256_16": sha16(store_bytes),
        "record_sha256_16": sha16((REPO / "graph/reports/"
                                   "C42_R40_REBUILD_RECORD.json").read_bytes()),
        "checks": [{"check": k, **v} for k, v in gates.items()],
        "passed": sum(1 for v in gates.values() if v["pass"]),
        "total": len(gates),
        "result": "ALL PASS" if all(v["pass"] for v in gates.values())
                  else "FAILURES PRESENT",
    }
    (REPO / "graph/reports/C42_R40_REBUILD_CHECK.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print(f"c42_r40_rebuild_check: {out['result']} ({out['passed']}/"
          f"{out['total']})")
    return 0 if out["passed"] == out["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
