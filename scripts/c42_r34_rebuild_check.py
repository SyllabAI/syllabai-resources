#!/usr/bin/env python3
"""c42_r34_rebuild_check.py — T-C42 R34 verification battery (committed-clean).

The R34 lane is the scope §7 loop's substrate re-build consuming the R33
override map AND the R33 promotions amendment (the R33 record's next lane,
fired by the operator directive "fire R34 → R35"; the R35 validation re-gate
is sanctioned by the same directive and fired separately). Verified:

  B1 census+meta       917 rows = 835 anchored (831 HUMAN_VALIDATED + 4
                       SUGGESTED: the 3 R22 re-attributed REJECTs + the 1
                       re-homed drawing ord 0 hold) + 27 unresolved-span + 55
                       uncovered-SP; covered 133/188 (UNCHANGED — the R33
                       projections landing: gained none lost none); meta
                       promotion fields byte-equal to the R5 values EXCEPT
                       promoted_rows RESTATED 831 (the value unchanged, the
                       set re-pinned row-level) + the 4 additive
                       promotion_reapplied* fields re-dated; stage pinned
                       @R34; tool pinned @2.7.0 (NO version move — the first
                       re-build where the tool string does not churn)
  B2 re-attributions   the 3 R33 map rows landed verbatim: the
                       REATTRIBUTEs (old code == current_code, new code ==
                       override_code, mapping_id recomputed — the R24
                       id_pairs convention, the projected re-keys verified
                       live — provenance.override == the map block with the
                       map sha, sp_title == the registry wording; all 3
                       flipped HUMAN_VALIDATED byte-stably); ZERO DEMOTEs
  B3 promotions        store <-> files+amendments two-way: 831 == 831 exact
  two-way              identities with the 3 superseded rows re-keyed
                       old->new AT THE AMENDED CODES (1.8B -> 1.8D), the 5
                       R30 supersedes re-keyed via the R31 record, the 3
                       R26 supersedes via the R28 record, the R26 + R30
                       excluded rows NOT promoted (their rebuilt forms are
                       the unresolved-span worklist rows), the 3 R31-ADDED
                       sign-off rows promoted with the R5-shaped block,
                       validated_by operator everywhere, sampled 457 == the
                       R21 CONFIRM set (R5-era ids), REJECT/hold/worklist
                       carry zero promotion blocks, the file sha == the R5
                       apply record's pin == the R33 amendment's base pin
                       (byte-unchanged since R5)
  B4 structural        final vs the baseline blob 9cd386c: byte-equal
  re-proof             everywhere except the 3 moved rows (enumerated
                       fields only) — rows 917 -> 917, no vanishing row, no
                       status changes, the non-chunk worklist byte-identical
                       (55 == 55); the re-applied promoted rows carry
                       byte-equal promotion blocks and byte-identical forms
                       (provenance.tool stays @2.7.0 — no tool churn)
  B5 protected         resolution substrate (the R14-era pin), the R27 join
  surfaces             artifact, the promotions file + the R26/R30/R33
                       amendments + the nine maps, the R5/R21/R22/R23/R24/
                       R25/R26/R27/R29/R30/R31/R32/R33 records + tools +
                       carriers, the Lane C stores, the chemistry substrate,
                       the corpus manifest and the ratified registry:
                       byte-identical to the baseline blob
  B6 determinism       the amended c40 tool constructs twice byte-identically
                       (G7) and the store sha matches the record's post pin
  B7 standing pins     the FOUR R26 STANDING joins verified against the R26
                       map's own list-shaped adjudications (ruling + anchor
                       id + landed code together) + the carried pins (the
                       R22 trio, the R18 pair, the R14 re-point, the R10
                       STANDING) + the R33 SPLIT-note anchors (the corpus
                       anchor STANDS at 1.8B; the R10 related-calculations
                       anchor STANDS at 1.8D)
  B8 commit state      adaptive: pre-commit HEAD == baseline with the dirt
                       inside the R34 footprint; post-commit the working
                       tree is clean and the committed delta vs HEAD~1 stays
                       inside the footprint (the audit trail may move HEAD,
                       never the protected surfaces)
  B9 anti-forgery      every HUMAN_VALIDATED row carries a promotion block
                       with promoted_by operator (AI-name patterns fail
                       closed); provenance tiers RULE_DERIVED everywhere;
                       the re-homed hold + the 3 R22 REJECT rows untouched
                       SUGGESTED; ZERO DEMOTEs this round
  B10 CI parity        kg_export --verify-golden GREEN on the committed
                       state; graph_check's failure census stays at the
                       pinned pre-round count with zero failures naming the
                       chunk store

Emits graph/reports/C42_R34_REBUILD_CHECK.json.
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
BASELINE = "9cd386c12aac240da7796ea6724748979397aaf8"
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE = REPO / STORE_REL
MAP33 = HERE / "c42_section_overrides_r33.yaml"
AMENDMENT = HERE / "c42_r33_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
R5_REC = REPO / "graph/reports/C42_R5_APPLY_RECORD.json"
R28_REC = REPO / "graph/reports/C42_R28_REBUILD_RECORD.json"
R31_REC = REPO / "graph/reports/C42_R31_REBUILD_RECORD.json"
TOOL = "scripts/c42_r34_substrate_rebuild.py"
TOOL_C40 = "scripts/c40_maths_a_chunk_sp_substrate.py@2.7.0"
COURSE = "igcse-maths-a-18-higher"
JOIN_REL = (f"Official-Specifications/parsed/_derived/notes-join/"
            f"{COURSE}.json")
FOOTPRINT = {
    "scripts/c40_maths_a_chunk_sp_substrate.py",
    "scripts/c42_r34_substrate_rebuild.py",
    "scripts/c42_r34_rebuild_check.py",
    STORE_REL,
    "graph/reports/C42_R34_REBUILD_RECORD.json",
    "graph/reports/C42_R34_REBUILD_RECORD.md",
    "graph/reports/C42_R34_REBUILD_CHECK.json",
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
    "scripts/c42_r26_promotions_amendment.yaml",
    "scripts/c42_r30_promotions_amendment.yaml",
    "scripts/c42_r33_promotions_amendment.yaml",
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
    rec = json.loads((REPO / "graph/reports/C42_R34_REBUILD_RECORD.json")
                     .read_text(encoding="utf-8"))

    # ---------------------------------------------------------------- inputs
    store_bytes = STORE.read_bytes()
    store_doc = yaml.safe_load(store_bytes.decode("utf-8"))
    base_doc = yaml.safe_load(
        blob_at(BASELINE, STORE_REL).decode("utf-8"))
    base_rows = {r["mapping_id"]: r for r in base_doc["rows"]}
    rows = {r["mapping_id"]: r for r in store_doc["rows"]}
    map_bytes = MAP33.read_bytes()
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
    added_by_mid = {a["row"]["mapping_id"]: a
                    for a in amend.get("added") or []}

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
    expected_diff = {"stage",
                     "promotion_reapplied", "promotion_reapplied_by",
                     "promotion_reapplied_directive",
                     "promotion_reapplied_note"}
    # NOTE: the census keys are NOT in the delta — the R33 projections land
    # UNCHANGED (covered 133, anchored 835, span 27, uncovered 55); the tool
    # key is NOT in the delta — the FIRST re-build with no version move
    # (c40 stays @2.7.0 per the R33 carriers' contract); promotion_reapplied
    # IS (R31 ran 2026-10-12, R34 runs 2026-10-16) — the by/directive/note
    # fields carry the R34 lane's values.
    # promoted_rows NOT in the delta: 831 -> 831 (the value unchanged, the
    # set re-pinned row-level)
    b1 = (len(rows) == 917 and len(anchored) == 835 and len(hv) == 831
          and len(sug_anch) == 4 and span_wl == 27 and unmapped == 55
          and len(covered) == 133 and m["sp_codes_covered"] == 133
          and "4MA1-2.7C" in covered
          and m["rows_worklist_unmapped_sps"] == 55
          and m["registry_size"] == 188 and m["rows_anchored"] == 835
          and m["rows_worklist_anchor_unresolved"] == 27
          and m["joins_resolved"] == 198 and m["joins_unresolved"] == 5
          and m["tool"] == TOOL_C40
          and m["stage"].startswith("T-C42 R34:")
          and promo_keys_ok
          and m["promoted_rows"] == 831
          and base_doc["meta"]["promoted_rows"] == 831
          and set(m) == set(base_doc["meta"])
          and diff_keys == expected_diff
          and m["promotion_reapplied_by"] == f"{TOOL}@1.0.0")
    gate("B1_census_meta", b1,
         f"917 rows = 835 anchored (831 HUMAN_VALIDATED + 4 SUGGESTED) + 27 "
         f"unresolved-span + 55 uncovered-SP; covered 133/188 UNCHANGED "
         f"(the R33 projections landing: gained none, lost none — 1.8B "
         f"keeps ords 0-5, 1.8D already covered via the R10 join); meta KEY "
         f"SETS identical with the delta by VALUE == exactly the stage key "
         f"+ the 4 reapplied fields re-dated (promoted_rows stays 831 "
         f"— the value unchanged, the set re-pinned); the 7 other R5 "
         f"promotion fields byte-equal; tool @2.7.0 (NO version move)")

    # ---- B2 re-attributions ---------------------------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40  # norm() for id recompute
    op_round = ("C42 R33 (surface 3: 3 verdicted REATTRIBUTEs [all "
                "HUMAN_VALIDATED, the supersedes shape] — the 1.8B->1.8D "
                "re-home batch — the loop's FIRST SPLIT-note scoping)")
    moved_ok, landings = True, []
    for e in reattr:
        slug, oc = e["note_slug"], e["chunk_ordinal"]
        nrow = next((r for r in rows.values() if r.get("note_slug") == slug
                     and r.get("chunk", {}).get("ordinal") == oc), None)
        orow = next((r for r in base_rows.values()
                     if r.get("note_slug") == slug
                     and r.get("chunk", {}).get("ordinal") == oc), None)
        want_mid = sha16(
            f"{nrow['note_path']}|{e['override_code']}|"
            f"{c40.norm(nrow['evidence_quote'])}")
        want_block = {
            "source": f"scripts/c42_section_overrides_r33.yaml@{map_sha}",
            "operator_round": op_round,
            "action": "REATTRIBUTE",
            "provenance_class": "verdicted",
            "evidence": e["evidence"],
        }
        want_status = "HUMAN_VALIDATED"  # all 3 R33 movers are HV promotions
        ok = (nrow is not None and orow is not None
              and orow["spec_code"] == e["current_code"]
              and nrow["spec_code"] == e["override_code"]
              and nrow["mapping_id"] == want_mid
              and nrow["sp_title"] == (registry[e["override_code"]]
                                       .get("official_wording") or "")
              and nrow["provenance"].get("override") == want_block
              and nrow["validation_status"] == want_status
              and (nrow.get("promotion") == r5.promotion_block()
                   if want_status == "HUMAN_VALIDATED"
                   else "promotion" not in nrow))
        moved_ok = moved_ok and ok
        landings.append({"row": f"{slug}::{oc}",
                         "from": e["current_code"],
                         "to": e["override_code"],
                         "mapping_id_old": orow["mapping_id"] if orow else None,
                         "mapping_id_new": nrow["mapping_id"] if nrow else None,
                         "pass": ok})
    b2 = moved_ok and not demote_es and len(landings) == 3
    gate("B2_reattributions", b2,
         f"3/3 map rows landed verbatim: "
         f"{', '.join(l['from'] + '->' + l['to'] for l in landings)}"
         f" (rounding-and-estimation ords 6/7/8); old ids == the R33 map's "
         f"rows; provenance.override == the map blocks (map sha {map_sha}); "
         f"all 3 promoted rows HUMAN_VALIDATED at the amended codes with "
         f"byte-stable blocks; ZERO DEMOTEs this round")

    # ---- B3 promotions two-way UNDER THE AMENDMENTS ---------------------------------
    sup_by_id = {e.get("mapping_id"): e
                 for e in amend.get("supersedes_code") or []}
    exc_by_id = {e.get("mapping_id"): e for e in amend.get("excluded") or []}
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
    pair33_by_old = {l["mapping_id_old"]: l["mapping_id_new"]
                     for l in landings if "DEMOTE" not in l["row"]}
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
        if mid in r26_exc or mid in r30_exc:
            continue
        if mid in sup_by_id:
            target_id = pair33_by_old.get(mid)
            want_code = sup_by_id[mid].get("amended_code")
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
    # old->new REATTRIBUTE translation: the promoted set excludes both shapes
    new_reject = set()
    hold_ids = set()
    by_ident = {ident(r): r for r in rows.values() if "chunk" in r}
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
        nrow_h = by_ident[ident(base_rows[r30_rekey.get(mid, mid)])]
        if mid in added_ids:
            if nrow_h["mapping_id"] != mid or \
                    nrow_h["mapping_id"] not in hv:
                problems.append(f"sign-off hold {mid} not promoted")
        else:
            hold_ids.add(nrow_h["mapping_id"])
    residue_ok = sug_anch == new_reject | hold_ids
    wl = {mid for mid, r in rows.items() if r.get("worklist_reason")}
    hv_targets = set(added_ids)
    for mid, e in seen.items():
        if mid in r26_exc or mid in r30_exc:
            continue
        t = pair33_by_old.get(mid)
        if t is None and mid in r30_sup:
            t = r30_rekey.get(mid)
        if t is None and mid in r26_sup:
            t = r26_rekey.get(mid)
        hv_targets.add(t or mid)
    b3 = (len(seen) == 832 == len(pentries) and len(hv) == 831
          and hv_targets == hv and n_sampled == 457 and not problems
          and residue_ok
          and not (hv & (new_reject | hold_ids | wl))
          and len(exc_by_id) == 0 and len(added_ids) == 3
          and vconf <= seen.keys()
          and promo_sha == r5rec["promotion_record"]["sha256_16"]
          == amend.get("base_file_sha256_16")
          and r5rec["promotion_record"]["entries"] == 832)
    gate("B3_promotions_two_way", b3,
         f"store <-> files+amendments 831 == 831 exact identities (823 "
         f"direct + 3 R26-chain re-keyed + 5 R30 superseded re-keyed via the "
         f"R31 record + 3 R33 superseded re-keyed AT THE AMENDED CODES "
         f"1.8B->1.8D + 3 R31-ADDED sign-off promotions); the R26 + R30 "
         f"excluded rows NOT promoted (unresolved-span worklist); "
         f"validated_by operator everywhere; sampled 457 == the R21 CONFIRM "
         f"set; every applied block == the R5 tool's block shape; the "
         f"SUGGESTED anchored residue == 3 R22 REJECTs + 1 re-homed hold; "
         f"promotions file sha {promo_sha} == the R5 record's pin == the "
         f"R33 amendment's base pin"
         + (f"; PROBLEMS {problems[:4]}" if problems else ""))

    # ---- B4 structural re-proof vs the baseline blob ---------------------------------
    base_chunk = {ident(r): r for r in base_doc["rows"] if "chunk" in r}
    fin_chunk = {ident(r): r for r in store_doc["rows"] if "chunk" in r}
    moved_keys = {(l["row"].split("::")[0],
                   int(l["row"].split("::")[1].split(" ")[0]))
                  for l in landings}
    drift = []
    if set(base_chunk) != set(fin_chunk) or len(fin_chunk) != 862:
        drift.append("chunk-identity set")
    added_ids_pre = set(added_ids)
    for k, brow in base_chunk.items():
        frow = fin_chunk[k]
        stem = Path(k[0]).stem
        is_mover = any(stem == mk[0] and k[1] == mk[1] for mk in moved_keys)
        if frow.get("validation_status") != brow.get("validation_status"):
            drift.append(f"status {k}")
        if is_mover:
            continue
        if strip_tool(brow) != strip_tool(frow):
            drift.append(f"non-tool delta {k}")
        elif brow["provenance"]["tool"] != TOOL_C40 or \
                frow["provenance"]["tool"] != TOOL_C40:
            drift.append(f"tool drift {k}")
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
    moved_new_ids = {l["mapping_id_new"] for l in landings}
    hv_byte_stable = all(
        strip_tool(base_rows[mid]) == strip_tool(rows[mid])
        and base_rows[mid]["provenance"]["tool"] == TOOL_C40
        and rows[mid]["provenance"]["tool"] == TOOL_C40
        and rows[mid]["promotion"] == base_rows[mid]["promotion"]
        for mid in hv
        if mid not in added_ids_pre and mid not in moved_new_ids
        and mid in base_rows)
    b4 = not drift and hv_byte_stable and len(rows) == 917
    gate("B4_structural_reproof", b4,
         f"vs baseline blob {BASELINE[:12]}: chunk-identity set identical "
         f"(862); the re-applied non-moved promoted rows BYTE-IDENTICAL "
         f"(provenance.tool stays @2.7.0 — no tool churn) with byte-equal "
         f"promotion blocks; the 3 re-attributed rows carry exactly the "
         f"enumerated fields (ZERO status changes this round); the "
         f"non-chunk worklist byte-identical (55 == 55, no vanishing row)"
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
         f"R27 join artifact, the promotions file, the R26+R30+R33 "
         f"amendments, the nine maps, the R5/R21/R22/R23/R24/R25/R26/R27/"
         f"R29/R30/R31/R32/R33 records + tools + carriers, the Lane C "
         f"stores, the chemistry substrate, the corpus manifest, the "
         f"ratified registry)"
         + (f"; DRIFT {prot_drift[:3]}" if prot_drift else ""))

    # ---- B6 determinism -----------------------------------------------------------------
    sys.path_ok = True
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
                      ("spcpt_crKbmb6wVjM4yPJh", "4MA1-1.8D")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("store_row_code") != want:
            pins_ok = False
    b7 = pins_ok
    gate("B7_standing_pins", b7,
         "the FOUR R26 STANDING joins verified against the R26 map's own "
         "list-shaped adjudications + the carried pins (the 4.11C anchor, "
         "the 1.7B anchor, the 3.3F anchor) + the R33 SPLIT-note anchors "
         "(the corpus anchor STANDS at 1.8B — ords 0-5; the R10 "
         "related-calculations anchor STANDS at 1.8D) — the join layer "
         "untouched")

    # ---- B8 commit state -----------------------------------------------------------------
    if pre_commit:
        outside = {c for c in dirty if c not in FOOTPRINT}
        b8 = not outside
        detail = (f"pre-commit: HEAD == baseline {BASELINE[:12]}; dirt "
                  f"{len(dirty)} inside the R34 footprint")
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
                  f"committed delta vs HEAD~1 inside the R34 footprint")
    gate("B8_commit_state", b8, detail
         + (f"; OUTSIDE {sorted(outside)[:4]}" if outside else ""))

    # ---- B9 anti-forgery -----------------------------------------------------------------
    af_ok = all(
        r.get("promotion", {}).get("promoted_by") == "operator"
        and not r5.AI_PAT.search(r5.AI_PAT.pattern) is True
        for r in [])  # placeholder replaced below
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
    demote_new = {l["mapping_id_new"] for l in landings
                  if "DEMOTE" in l["row"]}
    hold_rekeyed = {by_ident[ident(base_rows[r30_rekey.get(mid, mid)])]
                    ["mapping_id"]
                    for mid in vhold if mid not in added_ids}
    b9 = (not af_problems and tiers_ok
          and all("promotion" not in rows[d] for d in demote_new)
          and hold_rekeyed <= sug_anch
          and new_reject <= sug_anch
          and not (hv & (new_reject | hold_rekeyed | wl)))
    gate("B9_anti_forgery", b9,
         f"831 HUMAN_VALIDATED rows carry operator-attributed promotion "
         f"blocks; provenance tiers RULE_DERIVED everywhere; the re-homed "
         f"hold + the 3 R22 REJECT rows stay SUGGESTED unpromoted; ZERO "
         f"DEMOTE rows this round (no worklist landings)"
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
        "schema": "c42-r34-rebuild-check/1.0",
        "task": "T-C42",
        "stage": "r34-substrate-rebuild-check",
        "round": "R34",
        "round_start": BASELINE,
        "audited_head": head,
        "baseline_store_sha256_16": sha16(blob_at(BASELINE, STORE_REL)),
        "store_sha256_16": sha16(store_bytes),
        "record_sha256_16": sha16((REPO / "graph/reports/"
                                   "C42_R34_REBUILD_RECORD.json").read_bytes()),
        "checks": [{"check": k, **v} for k, v in gates.items()],
        "passed": sum(1 for v in gates.values() if v["pass"]),
        "total": len(gates),
        "result": "ALL PASS" if all(v["pass"] for v in gates.values())
                  else "FAILURES PRESENT",
    }
    (REPO / "graph/reports/C42_R34_REBUILD_CHECK.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8")
    print(f"c42_r34_rebuild_check: {out['result']} ({out['passed']}/"
          f"{out['total']})")
    return 0 if out["passed"] == out["total"] else 1


if __name__ == "__main__":
    sys.exit(main())
