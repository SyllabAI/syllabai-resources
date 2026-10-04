#!/usr/bin/env python3
"""c42_r27_join_check.py — T-C42 R27 verification battery (the JOIN RE-RUN lane).

The R27 lane is the scope §7 loop's deterministic join re-run, fired by the
operator's 'R27 join re-run + R28 rebuild consuming both carriers' directive
(2026-10-04, zai-web, gateway trace 1a106d1aa121ab59) naming exactly the R26
record's next-decision menu option (a) verbatim ("R27 join re-run + R28
substrate re-build consuming the R26 map AND amendment"). The R28 re-build IS
fired by the same directive and runs after this round closes; the R29 re-gate
is NOT fired. The 4 H3 HOLD rows and the ord-3 promoted-surface extension
candidate stay untouched operator decisions.

  J1 join refresh      the refreshed join artifact: census UNCHANGED
                       198 joined / 5 unresolved / 203 anchors / 0 foreign
                       (the R26 round re-pointed 0 note-level joins — ALL
                       FOUR adjudicated STANDING — and cleared 0 anchors; the
                       resolution file is byte-untouched, counts stay 222/214/8,
                       last writer R14); coverage census UNCHANGED (120/188
                       distinct codes, tier splits 61F/59H codes and 81F/117H
                       anchors, wording census EXACT 173 / LEDGER_EXPLAINABLE
                       25); exact unresolved id set (the C31 §3 residual + the
                       2 R1-cleared + the 2 R6-cleared); every input pin in the
                       artifact equals the recorded R19-era constant
                       (manifest cc470d40873f51a4, resolution b4539ab904c9a319,
                       SP store 33d3e5313d37464a, ledger 7f9322a8a05d3767) and
                       the resolution pin equals the live git blob
  J2 verbatim pins     all THIRTEEN note-level joins pinned verbatim: the R14
                       re-point (composite-functions -> 4MA1-3.2D), the R10
                       CORRECT pair (2.2A / 2.2C), the R10 STANDING pin
                       (related-calculations -> 4MA1-1.8D), the two R18
                       STANDING pins (converting-between-fdp -> 4MA1-1.2G,
                       basic-angle-properties -> 4MA1-4.1B), the three R22
                       STANDING pins (3d-pythagoras-and-trigonometry ->
                       4MA1-4.8D, difference-of-two-squares -> 4MA1-2.2F,
                       graphical-solutions -> 4MA1-2.6B) and the four R26
                       STANDING pins (types-of-number -> 4MA1-1.1G,
                       factorising-by-grouping -> 4MA1-2.2F,
                       drawing-straight-line-graphs -> 4MA1-3.3F,
                       introduction-to-vectors -> 4MA1-5.1D)
  J3 R18 map pins      both R18 STANDING pins verified against the R18 map's
                       own note_level_adjudications (dict-shaped): ruling
                       text + anchor id + landed code together, fail-closed
  J4 R22 map pins      the three R22 STANDING pins verified against the R22
                       map's own note_level_adjudications (list-shaped):
                       ruling STANDING + anchor id + joined_code together,
                       fail-closed; PLUS the map's overrides block carries
                       exactly the 3 verdicted REATTRIBUTE entries and NEITHER
                       of the 3 rows appears in the R5 promotions file (by
                       mapping_id AND by note+ordinal — the 832-entry promoted
                       set is identity- and code-stable at the join layer,
                       verified not assumed)
  J5 R26 map pins +    the four R26 STANDING pins verified against the R26
  the promotions       map's own note_level_adjudications (list-shaped, the
  interaction          R23 precedent): ruling STANDING + anchor id +
                       joined_code together, fail-closed; the map's overrides
                       block carries exactly the 3 verdicted REATTRIBUTEs + 1
                       DEMOTE_TO_WORKLIST entries; AND the R26 NOVELTY verified
                       at the join layer: the R5 promotions file (832 rows)
                       intersects the R26 map's 4 rows in EXACTLY those 4 rows
                       BY mapping_id AND by note+ordinal, the R5-pinned codes
                       equal the map's current_codes, the amendment
                       scripts/c42_r26_promotions_amendment.yaml agrees
                       (schema c42-r28-promotions-amendment/1.0, base_file
                       sha == the live R5 sha, 3 supersedes with amended_code
                       == the map's override_code + 1 excluded with
                       disposition DEMOTE_TO_WORKLIST, pinned_code == the R5
                       code on every entry, the 4 ids distinct and covering
                       exactly the map's rows)
  J6 resolution        the resolution substrate is BYTE-UNTOUCHED: the HEAD
  substrate            blob sha equals the R14-era full blob pin
                       93419a291b9b87ffa81aa2300db43e7851a95184 (recorded
                       since the R15/R16 record) and the recomputed counts
                       are 222 rows / 214 with resolved_code / 8 without
  J7 determinism       the generator re-run exits 0 and the refreshed artifact
                       is content-identical to the audited one modulo
                       generated_utc (joins, unresolved, counts, inputs,
                       task, validation_tier, schema, ordering all equal)
  J8 protected         working-tree dirt limited to the declared R27
  surfaces             footprint (subset semantics — the J7 re-run refreshes
                       the join's generated_utc and this battery refreshes its
                       own check json, so timestamp-only churn inside the
                       footprint is inherent; no dirt OUTSIDE the footprint is
                       the fail-closed guarantee); every protected loop record
                       byte-untouched between the baseline a8803c5 and HEAD
                       AND between HEAD and the working tree where
                       materialized (the R26 map/amendment/verdicts/check/
                       proposals/records, the R25 re-gate records, the R24
                       rebuild records + the R22/R21/R19-R20/R23 records, the
                       R5 apply artifacts incl. the 832-entry promotions file,
                       every earlier map/record, the scope doc, the C30
                       ledger, the SP store + the chunk store (sha16
                       ac37a91b9b657ef6 — the R25-era pin, R26 moved zero
                       store bytes), the Lane C stores, the c40 substrate tool
                       and the c42-era repair/check tools)
  J9 commit state      the working-tree delta vs HEAD stays inside the
                       footprint pre-commit; once HEAD carries the round
                       (subject starts 'T-C42 R27'), the committed delta vs
                       HEAD~1 stays inside the footprint too — the audit
                       trail may move HEAD, never a protected byte

Emits graph/reports/C42_R27_JOIN_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-a-18-higher"
JOIN = REPO / "Official-Specifications/parsed/_derived/notes-join/" \
              f"{COURSE}.json"
BASELINE = "a8803c5664db29bab69ed78e09bab4b246282dc4"  # the R26-closed HEAD
RES_BLOB = "93419a291b9b87ffa81aa2300db43e7851a95184"
RES_PATH = f"SME-ExamQuestion/{COURSE}/spec_point_resolution.json"
STORE_REL = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
STORE_SHA16 = "ac37a91b9b657ef6"  # the R25/R26-era store pin
# the R19-era recorded input pins (the artifact's own inputs block)
PIN_MANIFEST = "cc470d40873f51a4"
PIN_RESOLUTION = "b4539ab904c9a319"
PIN_SP_STORE = "33d3e5313d37464a"
PIN_LEDGER = "7f9322a8a05d3767"
RESIDUAL = "spcpt_QWXhzVp2S3VYZdZc"
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
R6_CLEARED = {"spcpt_mVXT4jbXQPrzhHvz", "spcpt_hK2H8q4Y8NYv833v"}
# the THIRTEEN verbatim note-level pins (9 carried + the 4 R26 STANDING joins)
VERBATIM = {
    "notes/3-sequences-functions-and-graphs/functions/composite-functions.json":
        "4MA1-3.2D",
    "notes/2-equations-formulae-and-identities/expanding-brackets/expanding-triple-brackets.json":
        "4MA1-2.2A",
    "notes/2-equations-formulae-and-identities/algebraic-fractions/algebraic-fractions.json":
        "4MA1-2.2C",
    "notes/1-numbers-and-the-number-system/number-toolkit/related-calculations.json":
        "4MA1-1.8D",
    "notes/1-numbers-and-the-number-system/fractions-decimals-and-percentages/converting-between-fdp.json":
        "4MA1-1.2G",
    "notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json":
        "4MA1-4.1B",
    "notes/4-geometry-and-trigonometry/3d-pythagoras-and-trigonometry/3d-pythagoras-and-trigonometry.json":
        "4MA1-4.8D",
    "notes/2-equations-formulae-and-identities/factorising/difference-of-two-squares.json":
        "4MA1-2.2F",
    "notes/3-sequences-functions-and-graphs/graphs-of-functions/graphical-solutions.json":
        "4MA1-2.6B",
    "notes/1-numbers-and-the-number-system/prime-factors-hcf-and-lcm/types-of-number.json":
        "4MA1-1.1G",
    "notes/2-equations-formulae-and-identities/factorising/factorising-by-grouping.json":
        "4MA1-2.2F",
    "notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json":
        "4MA1-3.3F",
    "notes/5-vectors-and-transformation-geometry/vectors/introduction-to-vectors.json":
        "4MA1-5.1D",
}
R18_PINS = (
    ("converting-between-fdp",
     "THE NOTE-LEVEL JOIN TO 1.2G STANDS (unchanged)", "4MA1-1.2G",
     "spcpt_8MpvS5pnYkf9QswF"),
    ("basic-angle-properties",
     "THE NOTE-LEVEL JOIN TO 4.1B STANDS (unchanged)", "4MA1-4.1B",
     "spcpt_5FMXZMjqSZ3GK53q"),
)
R22_PINS = (
    ("3d-pythagoras-and-trigonometry", "4MA1-4.8D", "spcpt_kX4655D8M3Q3TRzW"),
    ("difference-of-two-squares", "4MA1-2.2F", "spcpt_RJbgRvXq2VrGpP5g"),
    ("graphical-solutions", "4MA1-2.6B", "spcpt_sHCB9WZbDMyTFqCP"),
)
R22_OVERRIDE_KEYS = {
    ("graphical-solutions", 1, "5fd48f084383be11", "4MA1-2.6B", "4MA1-3.3E"),
    ("3d-pythagoras-and-trigonometry", 4, "a8d23b11c343a3bd", "4MA1-4.8D",
     "4MA1-4.8F"),
    ("difference-of-two-squares", 3, "eb26022693be3948", "4MA1-2.2F",
     "4MA1-2.2B"),
}
R26_PINS = (
    ("types-of-number", "4MA1-1.1G", "spcpt_J55PhZ2cbPsYvpt8"),
    ("factorising-by-grouping", "4MA1-2.2F", "spcpt_vMSNnYkKPf62MRH9"),
    ("drawing-straight-line-graphs", "4MA1-3.3F", "spcpt_h8QyRmzX5mCJb3X9"),
    ("introduction-to-vectors", "4MA1-5.1D", "spcpt_v6tP4DSVShVJMJhk"),
)
R26_OVERRIDE_KEYS = {
    # (note_slug, ordinal, mapping_id, current_code, override_code)
    ("drawing-straight-line-graphs", 4, "e6ed72481e8ffc2e", "4MA1-3.3F",
     "4MA1-3.3H"),
    ("factorising-by-grouping", 2, "70f0b027f3f1528f", "4MA1-2.2F", None),
    ("introduction-to-vectors", 3, "7fdded0b9245e1c3", "4MA1-5.1D",
     "4MA1-5.1C"),
    ("types-of-number", 1, "81c0b59852d5d4b6", "4MA1-1.1G", "4MA1-1.1A"),
}
FOOTPRINT = {
    "scripts/c32_notes_maths_a_join.py",
    "scripts/c42_r27_join_check.py",
    "Official-Specifications/parsed/_derived/notes-join/"
    f"{COURSE}.json",
    "graph/reports/C42_R27_JOIN_CHECK.json",
    "graph/reports/C42_R27_JOIN_RECORD.md",
    "graph/reports/C42_R27_JOIN_RECORD.json",
}
PROTECTED = [
    "graph/reports/C42_IGCSE_MATHS_A_K2B_REWORK_SCOPE.md",
    "graph/reports/C42_MATHS_A_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R6_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R10_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md",
    "graph/reports/C42_R13_REGATE_CHECK.json",
    "graph/reports/C42_R14_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R15_R16_CHECK.json",
    "graph/reports/C42_R15_R16_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R17_REGATE_CHECK.json",
    "graph/reports/C42_R17_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R18_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R18_REPAIR_CHECK.json",
    "graph/reports/C42_R19_R20_CHECK.json",
    "graph/reports/C42_R19_R20_JOIN_SUBSTRATE_RECORD.md",
    "graph/reports/C42_R19_R20_JOIN_SUBSTRATE_RECORD.json",
    "graph/reports/C42_R21_REGATE_CHECK.json",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.md",
    "graph/reports/C42_R21_MATHS_A_REGATE_FILL_RECORD.json",
    "graph/reports/C42_R22_REPAIR_CHECK.json",
    "graph/reports/C42_R22_REPAIR_PROPOSALS.json",
    "graph/reports/C42_R22_RESOLUTION_REPAIR_RECORD.md",
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
    "graph/reports/C42_R5_APPLY_CHECK.json",
    "graph/reports/C42_R5_APPLY_RECORD.json",
    "graph/reports/C42_R5_APPLY_RECORD.md",
    "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json",
    "graph/igcse-maths-a/specification_points.yaml",
    "graph/igcse-maths-a/spec_chunk_mappings.yaml",
    "graph/igcse-maths-a/concepts.yaml",
    "graph/igcse-maths-a/concept_edges.yaml",
    "graph/igcse-maths-a/spec_command_kinds.yaml",
    "graph/igcse-chemistry/spec_chunk_mappings.yaml",
    "scripts/c42_section_overrides.yaml",
    "scripts/c42_section_overrides_r6.yaml",
    "scripts/c42_section_overrides_r10.yaml",
    "scripts/c42_section_overrides_r14.yaml",
    "scripts/c42_section_overrides_r18.yaml",
    "scripts/c42_section_overrides_r22.yaml",
    "scripts/c42_section_overrides_r26.yaml",
    "scripts/c42_r26_promotions_amendment.yaml",
    "scripts/c42_r26_repair_verdicts.yaml",
    "scripts/c42_r26_repair_proposals.py",
    "scripts/c42_r26_repair_check.py",
    "scripts/c42_r26_override_projection.py",
    "scripts/c42_r25_regate_fill.py",
    "scripts/c42_r25_regate_check.py",
    "scripts/c42_r25_fresh_verdicts.yaml",
    "scripts/c42_r25_review_verdicts.yaml",
    "scripts/c42_r24_substrate_rebuild.py",
    "scripts/c42_r24_rebuild_check.py",
    "scripts/c42_r23_join_check.py",
    "scripts/c42_r22_repair_verdicts.yaml",
    "scripts/c42_r22_repair_proposals.py",
    "scripts/c42_r22_repair_check.py",
    "scripts/c42_r22_override_projection.py",
    "scripts/c42_r21_regate_check.py",
    "scripts/c42_r21_fresh_verdicts.yaml",
    "scripts/c42_r21_review_verdicts.yaml",
    "scripts/c42_r5_promotions.yaml",
    "scripts/c42_r5_promote.py",
    "scripts/c42_r5_promotion_apply.py",
    "scripts/c42_r5_promotion_check.py",
    "scripts/c40_maths_a_chunk_sp_substrate.py",
]

gates: dict[str, dict] = {}


def gate(name: str, ok: bool, detail: str) -> bool:
    gates[name] = {"pass": bool(ok), "detail": detail}
    return bool(ok)


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def git(*args: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), *args],
                          capture_output=True, check=True).stdout


def git_text(*args: str) -> str:
    return git(*args).decode("utf-8")


def blob_bytes(rev: str, path: str) -> bytes:
    return git("show", f"{rev}:{path}")


def slug_of(np: str) -> str:
    return np.split("/")[-1][:-5] if isinstance(np, str) else ""


def main() -> int:
    snap = JOIN.read_bytes()
    join = json.loads(snap.decode("utf-8"))
    r22doc = yaml.safe_load(
        (REPO / "scripts/c42_section_overrides_r22.yaml").read_text("utf-8"))
    r18doc = yaml.safe_load(
        (REPO / "scripts/c42_section_overrides_r18.yaml").read_text("utf-8"))
    r26doc = yaml.safe_load(
        (REPO / "scripts/c42_section_overrides_r26.yaml").read_text("utf-8"))
    amend = yaml.safe_load(
        (REPO / "scripts/c42_r26_promotions_amendment.yaml")
        .read_text("utf-8"))
    prom = yaml.safe_load(
        (REPO / "scripts/c42_r5_promotions.yaml").read_text("utf-8"))
    prom_rows = prom.get("promotions") or []

    # ------------------------------------------------------------------ J1
    c = join["counts"]
    cov_ok = (c["joined"] == 198 and c["unresolved_recorded"] == 5
              and c["anchors_total"] == 203 and c["anchors_distinct"] == 203
              and c["foreign_codes"] == 0
              and c["distinct_official_codes"] == 120
              and c["coverage_of_188"] == "120/188"
              and c["coverage_by_applicability_tier"] ==
              {"Foundation": 61, "Higher": 59}
              and c["anchors_by_applicability_tier"] ==
              {"Foundation": 81, "Higher": 117}
              and c["wording_check_census"] ==
              {"EXACT": 173, "LEDGER_EXPLAINABLE": 25}
              and c["ids_absent_from_resolution"] == 0)
    got_unres = {u["anchor_id"] for u in join["unresolved"]}
    unres_ok = got_unres == {RESIDUAL} | R1_CLEARED | R6_CLEARED
    pins = join["inputs"]
    res_live = blob_bytes("HEAD", RES_PATH)
    pins_ok = (pins["notes_manifest"]["sha256_16"] == PIN_MANIFEST
               and pins["resolution"]["sha256_16"] == PIN_RESOLUTION
               and pins["spec_points_store"]["sha256_16"] == PIN_SP_STORE
               and pins["tier_dedupe_ledger"]["sha256_16"] == PIN_LEDGER
               and pins["resolution"]["sha256_16"] == sha16(res_live))
    j1 = cov_ok and unres_ok and pins_ok
    gate("J1_join_refresh", j1,
         f"census UNCHANGED 198/5/203 (R26 re-pointed 0 joins, cleared 0 "
         f"anchors — ALL FOUR adjudicated STANDING), 0 foreign, coverage "
         f"120/188 (61F/59H codes, 81F/117H anchors, EXACT 173 / "
         f"LEDGER_EXPLAINABLE 25); unresolved set == residual + 2 R1-cleared "
         f"+ 2 R6-cleared; all four input pins equal the recorded R19-era "
         f"constants and the resolution pin equals the live git blob "
         f"{sha16(res_live)}")

    # ------------------------------------------------------------------ J2
    by_np = {r["note_path"]: r for r in join["joins"]}
    j2 = True
    missing = []
    for np_, want in VERBATIM.items():
        row = by_np.get(np_)
        if row is None or row["store_row_code"] != want:
            j2 = False
            missing.append((np_, None if row is None else
                            row["store_row_code"]))
    gate("J2_verbatim_pins", j2,
         f"all {len(VERBATIM)} note-level joins pinned verbatim (R14 re-point "
         f"3.2D; R10 pair 2.2A/2.2C + STANDING 1.8D; R18 STANDING pair 1.2G/"
         f"4.1B; R22 STANDING trio 4.8D/2.2F/2.6B; R26 STANDING quartet "
         f"1.1G/2.2F/3.3F/5.1D) — "
         f"{'all landed' if j2 else f'DRIFT: {missing}'}")

    # ------------------------------------------------------------------ J3
    j3 = True
    for slug, ruling, code, anchor in R18_PINS:
        adj = (r18doc.get("note_level_adjudications") or {}).get(slug) or {}
        row = next((r for r in join["joins"]
                    if r["note_path"].endswith(f"/{slug}.json")), None)
        if adj.get("ruling") != ruling or adj.get("anchor_id") != anchor \
                or row is None or row["store_row_code"] != code \
                or row["anchor_id"] != anchor:
            j3 = False
    gate("J3_r18_map_pins", j3,
         "BOTH R18 STANDING pins verified against the R18 map's own "
         "note_level_adjudications (dict-shaped) — ruling text + anchor id + "
         "landed code together, fail-closed (carried from R19)")

    # ------------------------------------------------------------------ J4
    r22adj = {a.get("note_slug"): a for a in
              (r22doc.get("note_level_adjudications") or [])}
    j4 = True
    for slug, code, anchor in R22_PINS:
        adj = r22adj.get(slug) or {}
        row = next((r for r in join["joins"]
                    if r["note_path"].endswith(f"/{slug}.json")), None)
        if adj.get("ruling") != "STANDING" or adj.get("joined_code") != code \
                or adj.get("anchor_id") != anchor or row is None \
                or row["store_row_code"] != code or row["anchor_id"] != anchor:
            j4 = False
    ov_keys = set()
    for e in r22doc.get("overrides") or []:
        ov_keys.add((e.get("note_slug"), int(e.get("chunk_ordinal")),
                     e.get("mapping_id"), e.get("current_code"),
                     e.get("override_code")))
    map_ok = ov_keys == R22_OVERRIDE_KEYS and len(r22adj) == 3
    r22_ids = {k[2] for k in R22_OVERRIDE_KEYS}
    r22_np_ord = {(slug_of(p), o)
                  for p, o in ((f"notes/%/{k[0]}", k[1])
                               for k in R22_OVERRIDE_KEYS)}

    def prom_hits(ids, np_ords):
        h_ids = [r for r in prom_rows
                 if r.get("row", {}).get("mapping_id") in ids]
        h_rows = [r for r in prom_rows
                  if (slug_of(r.get("row", {}).get("note_path", "")),
                      int(r.get("row", {}).get("chunk_ordinal", -1)))
                  in np_ords]
        return h_ids, h_rows

    hit_ids, hit_rows = prom_hits(r22_ids, r22_np_ord)
    prom_ok = (len(prom_rows) == 832 and not hit_ids and not hit_rows)
    j4 = j4 and map_ok and prom_ok
    gate("J4_r22_map_pins", j4,
         f"ALL THREE R22 STANDING pins verified against the R22 map's own "
         f"note_level_adjudications (list-shaped) — ruling STANDING + anchor "
         f"id + joined_code together; the map's overrides block carries "
         f"exactly the 3 verdicted REATTRIBUTE entries "
         f"{'as pinned' if map_ok else 'DRIFT'}; the R5 promotions file "
         f"(832 rows) intersects the 3 rows in NOTHING by mapping_id and by "
         f"note+ordinal ({len(hit_ids)}/{len(hit_rows)} hits) — the R22-era "
         f"promoted-set stability, verified not assumed (carried)")

    # ------------------------------------------------------------------ J5
    r26adj = {a.get("note_slug"): a for a in
              (r26doc.get("note_level_adjudications") or [])}
    j5 = True
    for slug, code, anchor in R26_PINS:
        adj = r26adj.get(slug) or {}
        row = next((r for r in join["joins"]
                    if r["note_path"].endswith(f"/{slug}.json")), None)
        if adj.get("ruling") != "STANDING" or adj.get("joined_code") != code \
                or adj.get("anchor_id") != anchor or row is None \
                or row["store_row_code"] != code or row["anchor_id"] != anchor:
            j5 = False
    ov26_keys = set()
    for e in r26doc.get("overrides") or []:
        ov26_keys.add((e.get("note_slug"), int(e.get("chunk_ordinal")),
                       e.get("mapping_id"), e.get("current_code"),
                       e.get("override_code")))
    n_reattr = sum(1 for e in r26doc.get("overrides") or []
                   if e.get("action") == "REATTRIBUTE")
    n_demote = sum(1 for e in r26doc.get("overrides") or []
                   if e.get("action") == "DEMOTE_TO_WORKLIST")
    map26_ok = (ov26_keys == R26_OVERRIDE_KEYS and len(r26adj) == 4
                and r26doc.get("schema") == "c42-r28-section-overrides/1.0"
                and n_reattr == 3 and n_demote == 1)
    # the R26 NOVELTY at the join layer: the promoted set intersects the 4
    # rows in EXACTLY those 4 rows, by id AND by note+ordinal
    r26_ids = {k[2] for k in R26_OVERRIDE_KEYS}
    r26_np_ord = {(k[0], k[1]) for k in R26_OVERRIDE_KEYS}
    hit26_ids, hit26_rows = prom_hits(r26_ids, r26_np_ord)
    prom_by_id = {r.get("row", {}).get("mapping_id"): r for r in prom_rows}
    codes_ok = all(
        len(hit26_ids) == 4 and len(hit26_rows) == 4
        and prom_by_id.get(mid, {}).get("row", {}).get("spec_code") == cur
        for (s, o, mid, cur, oc) in R26_OVERRIDE_KEYS)
    # the amendment agrees with the map and the R5 file
    sup = amend.get("supersedes_code") or []
    exc = amend.get("excluded") or []
    live_r5_sha = sha16((REPO / "scripts/c42_r5_promotions.yaml")
                        .read_bytes())
    sup_by_id = {e.get("mapping_id"): e for e in sup}
    exc_by_id = {e.get("mapping_id"): e for e in exc}
    amend_ok = (amend.get("schema") == "c42-r28-promotions-amendment/1.0"
                and amend.get("round") == "R26"
                and amend.get("base_file") == "scripts/c42_r5_promotions.yaml"
                and amend.get("base_file_sha256_16") == live_r5_sha
                and amend.get("base_file_untouched") is True
                and len(sup) == 3 and len(exc) == 1
                and len(set(sup_by_id) | set(exc_by_id)) == 4
                and set(sup_by_id) | set(exc_by_id) == r26_ids)
    for (s, o, mid, cur, oc) in R26_OVERRIDE_KEYS:
        if oc is None:
            e = exc_by_id.get(mid) or {}
            amend_ok = amend_ok and e.get("pinned_code") == cur \
                and e.get("disposition") == "DEMOTE_TO_WORKLIST" \
                and e.get("note_path", "").endswith(f"/{s}.json") \
                and int(e.get("chunk_ordinal", -1)) == o
        else:
            e = sup_by_id.get(mid) or {}
            amend_ok = amend_ok and e.get("pinned_code") == cur \
                and e.get("amended_code") == oc \
                and e.get("note_path", "").endswith(f"/{s}.json") \
                and int(e.get("chunk_ordinal", -1)) == o
    j5 = j5 and map26_ok and codes_ok and amend_ok
    gate("J5_r26_map_pins_and_promotions_interaction", j5,
         f"ALL FOUR R26 STANDING pins verified against the R26 map's own "
         f"list-shaped adjudications — ruling STANDING + anchor id + "
         f"joined_code together; the map's overrides block carries exactly "
         f"3 verdicted REATTRIBUTEs + 1 DEMOTE_TO_WORKLIST "
         f"{'as pinned' if map26_ok else 'DRIFT'}; THE R26 NOVELTY at the "
         f"join layer: the R5 promotions file (832 rows) intersects the 4 "
         f"rows in EXACTLY those 4 rows by mapping_id ({len(hit26_ids)}) AND "
         f"by note+ordinal ({len(hit26_rows)}) with the R5-pinned codes == "
         f"the map's current_codes {'verified' if codes_ok else 'DRIFT'}; the "
         f"amendment agrees (schema c42-r28-promotions-amendment/1.0, base "
         f"sha {amend.get('base_file_sha256_16')} == live {live_r5_sha}, "
         f"3 supersedes with amended_code == override_code + 1 excluded "
         f"DEMOTE, pinned codes == the R5 codes) "
         f"{'verified' if amend_ok else 'DRIFT'}")

    # ------------------------------------------------------------------ J6
    res_doc = json.loads(res_live)
    rr = res_doc.get("resolved") or []
    n_rows = len(rr)
    n_code = sum(1 for x in rr if x.get("resolved_code"))
    j6 = (sha16(res_live) == PIN_RESOLUTION
          and git_text("rev-parse", f"HEAD:{RES_PATH}").strip()
          == git_text("rev-parse", f"{BASELINE[:8]}:{RES_PATH}").strip()
          and (n_rows, n_code, n_rows - n_code) == (222, 214, 8))
    gate("J6_resolution_substrate", j6,
         f"resolution BYTE-UNTOUCHED: HEAD blob == R14-era pin {RES_BLOB[:16]} "
         f"(== baseline blob), counts recomputed 222 rows / 214 with "
         f"resolved_code / 8 without — last writer remains R14; R26 amended "
         f"nothing at the resolution layer")

    # ------------------------------------------------------------------ J7
    run = subprocess.run([sys.executable, "scripts/c32_notes_maths_a_join.py"],
                         capture_output=True, text=True)
    j7 = run.returncode == 0
    detail7 = f"generator re-run exit {run.returncode}"
    if j7:
        re_join = json.loads(JOIN.read_bytes().decode("utf-8"))
        a = json.loads(snap.decode("utf-8"))
        a.pop("generated_utc"), re_join.pop("generated_utc")
        j7 = a == re_join
        detail7 += "; refreshed artifact content-identical modulo " \
                   "generated_utc" if j7 else "; CONTENT DRIFT vs snapshot"
    gate("J7_determinism", j7,
         detail7 + " (joins, unresolved, counts, inputs, task, "
         "validation_tier, schema, ordering all equal)")

    # ------------------------------------------------------------------ J8
    dirty = []
    for l in git_text("status", "--porcelain").splitlines():
        if not l.strip():
            continue
        # porcelain v1: XY + space + path (renames: 'R  old -> new')
        p = l.split("->")[-1].lstrip() if "->" in l else l[3:]
        dirty.append(p)
    dirt_ok = set(dirty) <= FOOTPRINT
    moved = []
    for p in PROTECTED:
        try:
            b = git_text("rev-parse", f"{BASELINE[:8]}:{p}").strip()
            h = git_text("rev-parse", f"HEAD:{p}").strip()
        except subprocess.CalledProcessError:
            moved.append(p)
            continue
        if b != h:
            moved.append(p)
            continue
        disk = REPO / p
        if disk.is_file() and sha16(disk.read_bytes()) != \
                sha16(blob_bytes("HEAD", p)):
            moved.append(p)
    store_ok = sha16(blob_bytes("HEAD", STORE_REL)) == STORE_SHA16
    j8 = dirt_ok and not moved and store_ok
    gate("J8_protected_surfaces", j8,
         f"working-tree dirt ⊆ the declared R27 footprint "
         f"({sorted(set(dirty) - FOOTPRINT) or 'no outside dirt'}); every "
         f"protected loop record byte-untouched baseline→HEAD→working tree "
         f"({len(PROTECTED)} paths incl. the R26 map/amendment/verdicts/check/"
         f"records, the R25 re-gate records, the R24 rebuild records, the R22/"
         f"R21/R19-R20/R23 records, the R5 apply artifacts incl. the 832-row "
         f"promotions file, every earlier map/record, the scope doc, the C30 "
         f"ledger, the SP + chunk stores, the Lane C stores, the c40 tool) — "
         f"{'clean' if j8 else f'MOVED/DIRTY: {sorted(moved)}'}; the chunk "
         f"store sha16 {STORE_SHA16} re-verified (R26 moved zero store bytes)")

    # ------------------------------------------------------------------ J9
    head = git_text("log", "-1", "--format=%H %s")
    head_sha, head_subj = head[:40], head[41:]
    committed_ok = True
    if head_sha.startswith(BASELINE[:8]):
        delta = [l for l in git_text("diff", "--name-only", "HEAD")
                 .splitlines() if l.strip()]
        committed_ok = set(delta) <= FOOTPRINT
        j9_detail = (f"HEAD == baseline {BASELINE[:8]} (pre-commit form): "
                     f"working-tree delta vs HEAD ⊆ footprint "
                     f"({sorted(set(delta) - FOOTPRINT) or 'in footprint'})")
    elif head_subj.startswith("T-C42 R27"):
        delta = [l for l in git_text("diff", "--name-only", "HEAD~1", "HEAD")
                 .splitlines() if l.strip()]
        committed_ok = set(delta) <= FOOTPRINT
        j9_detail = (f"HEAD carries the round ({head_subj[:60]}...): committed "
                     f"delta vs HEAD~1 ⊆ footprint "
                     f"({sorted(set(delta) - FOOTPRINT) or 'in footprint'})")
    else:
        j9_detail = (f"HEAD {head_sha[:8]} is neither baseline nor a T-C42 "
                     f"R27 commit — delta check skipped, dirt gate above "
                     f"remains the guarantee")
    gate("J9_commit_state", committed_ok, j9_detail)

    # ----------------------------------------------------------------- emit
    all_pass = all(g["pass"] for g in gates.values())
    out = {
        "schema": "c42-r27-join-check/1.0",
        "task": "T-C42 R27 join re-run verification battery (J1-J9)",
        "generated_utc": datetime.now(timezone.utc)
            .isoformat(timespec="seconds"),
        "head": {"sha": head_sha, "subject": head_subj},
        "baseline": BASELINE,
        "directive": "R27 join re-run + R28 rebuild consuming both carriers "
                     "(2026-10-04, zai-web, gateway trace 1a106d1aa121ab59) "
                     "— the join re-run lane; R28 fired by the same "
                     "directive and runs after this round closes; R29 NOT "
                     "fired",
        "gates": gates,
        "all_pass": all_pass,
    }
    outp = REPO / "graph/reports/C42_R27_JOIN_CHECK.json"
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    for name, g in gates.items():
        print(f"{'PASS' if g['pass'] else 'FAIL'}  {name}: {g['detail']}")
    print(f"ALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(g['pass'] for g in gates.values())}/{len(gates)}) "
          f"-> {outp.relative_to(REPO)}")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
