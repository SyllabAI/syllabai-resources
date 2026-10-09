#!/usr/bin/env python3
"""c42-r29 — the R29 RE-GATE fill (operator gate 2 RE-RUN of the C42 K2-B rework
loop's SEVENTH iteration, fired by the operator's "R29 Re-gate" directive):
render a FRESH re-stratified operator review sheet over the R28-rebuilt
chunk→SP substrate — the FIRST re-gate UNDER THE AMENDED PROMOTED SURFACE
(831 HUMAN_VALIDATED rows) — and re-fill it under the C12/C13 fill
convention, operator-delegate.

Differences from the R25 re-gate (this is the loop's seventh pass):
  * THE AMENDED PROMOTED SURFACE (NEW — the R26/R28 novelty): the substrate
    now carries 831 HUMAN_VALIDATED rows — the R5 §18 apply (operator gate 3,
    2e90f52) re-applied byte-stably at R24 and RE-APPLIED AMENDED at R28 by
    scripts/c42_r28_substrate_rebuild.py@1.0.0 consuming the R26 promotions
    amendment (3 supersedes re-keyed old->new at 1.1A/5.1C/3.3H — the rows
    REMAIN promoted; 1 exclusion — the DEMOTE row lands unresolved-span; the
    R5 file itself byte-untouched per the P5 convention). The anti-forgery
    sweep verifies the HV set against the AMENDED surface built here from the
    two of-record carriers (R5 file sha16 9bad739bd79e5899 + amendment), the
    7 SUGGESTED anchored rows must be exactly the expected set (3 R22
    re-attributed + 4 convention H3 holds), and every row stays RULE_DERIVED.
    The re-gate VERIFIES the promoted surface; it never moves it.
  * R26 EVIDENCE (NEW — the seventh R1-shaped round, the R25 4-row defect
    inventory repaired): rows carrying a provenance.override from the R26 map
    (3 verdicted REATTRIBUTEs: types-of-number ord 1 1.1G -> 1.1A,
    introduction-to-vectors ord 3 5.1D -> 5.1C, drawing-straight-line-graphs
    ord 4 3.3F -> 3.3H) carry the R26 rulings; the FOUR R26 STANDING
    note-level joins (all four adjudicated STANDING, 0 resolution amendments)
    ride the standing join; the R26 DEMOTE row (factorising-by-grouping
    ord 2, the loop's FIRST promoted-row DEMOTE) sits on the worklist as the
    Part B surface-3 residual. The R25 gate arithmetic stays
    recorded-not-claimed: every re-gate re-seeds (the R13 -> R17
    falsification precedent) — the outcome is whatever THIS fill actually
    computes.
  * R25 CARRY-FORWARD (NEW) + R21/R17/R13/R9/R4 CARRY-FORWARD (unchanged): a
    sampled row whose (note_path, spec_code, heading) triple is identical to
    an R25-CONFIRMed (or, not sampled at R25, an R21/R17/R13/R9/R4-CONFIRMed)
    verdict row, outside the changed surface, carries that CONFIRM forward
    (W3 chunk identity + W4 zero-drift hold; the R26-attributed rows can
    never triple-match their prior CONFIRMs — the code moved, the mapping_id
    is code-derived, so the stale keys simply miss; they resolve via the R26
    override branch instead).
  * c42-HEADING-ONLY-CONVENTION-1 (STANDING): a heading-only chunk is a
    STRUCTURAL slice of the corpus's own spec_point span; its row is resolved
    by the fail-closed evidence ladder — H1 (the anchor carries an operator
    id-verdict or a note-level STANDING adjudication), H2 (>=1 CONTENT-row
    CONFIRM of the same note+code at R4/R9/R13/R17/R21/R25 — a heading-only
    row's own prior CONFIRM never satisfies H2), H3 (otherwise HOLD,
    fail-closed, recorded). The R25 record is NEW in the ladder's source base
    this round (the carry-forward continuity rule: every re-gate record
    enters the H2 base once its fill lands). Nothing promotes.
  * R18/R14/R10/R1/R6 EVIDENCE STILL STANDING (unchanged from R25).
  * FRESH JUDGMENT: every remaining sampled row is judged directly against
    both tier wordings and the chunk content (recorded per-row in
    scripts/c42_r29_fresh_verdicts.yaml, with its evidence).
  * Part B re-decided on the rebuilt worklist (24 unresolved-span = 2 C32 §3
    residual + 6 R1-cleared spans + 12 R6-cleared spans + 4 DEMOTEs [R10, R14,
    R18 and R26 — the R26 the FIRST of a promoted row]; 56 uncovered-SP at the
    132-code bound — the R26 re-attributions landed COMPUTED at R28: 1.1A +
    5.1C gained, none lost, the two uncovered-SP DEFER rows
    da25da48e0be5c64 / 2332964a4f1b02ca resolving into anchored rows).

Verdict standard (the C40 standard, unchanged): CONFIRM / REJECT (root-caused) /
HOLD (evidence insufficient — under the convention, ONLY the H3 heading-only
rows and any row the ladder cannot resolve). Gate (the scope's rule, unchanged):
Part A per-class precision >= 90% AND every Part B row decided AND the
mechanical layer clean. ZERO MOVEMENT OF THE PROMOTED SURFACE: the re-gate is
verification-only — the 831 promoted rows stay HUMAN_VALIDATED (their evidence
is re-verified here, not re-conferred), the 7 SUGGESTED anchored rows stay
SUGGESTED, and any promotion movement stays an operator-level decision (the
§18 apply was R5; the amendment was R26, operator-fired; the 4 H3 rows ride
R5 only with explicit per-row sign-off, still owed).

Outputs:
  scripts/c42_r29_review_verdicts.yaml                  (the verdict record)
  graph/reports/C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md  (fresh filled sheet)
  graph/reports/C42_R29_MATHS_A_REGATE_FILL_RECORD.json/.md
With --emit-dossier: dumps the not-yet-judged fresh rows' full context
(chunk text + both tier wordings) to FRESH_DOSSIER for the semantic pass.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402
from c40_maths_a_chunk_sp_substrate import span_chunks, load_corpus, R, norm  # noqa: E402

QUAL = "igcse-maths-a"
REPO = HERE.parent
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
R1_VERDICTS = HERE / "c42_repair_verdicts.yaml"
R6_VERDICTS = HERE / "c42_r6_repair_verdicts.yaml"
R10_VERDICTS = HERE / "c42_r10_repair_verdicts.yaml"
R14_VERDICTS = HERE / "c42_r14_repair_verdicts.yaml"
OVERRIDES = HERE / "c42_section_overrides.yaml"
OVERRIDES_R6 = HERE / "c42_section_overrides_r6.yaml"
OVERRIDES_R10 = HERE / "c42_section_overrides_r10.yaml"
OVERRIDES_R14 = HERE / "c42_section_overrides_r14.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R9_VERDICTS = HERE / "c42_r9_review_verdicts.yaml"
R13_VERDICTS = HERE / "c42_r13_review_verdicts.yaml"
R17_VERDICTS = HERE / "c42_r17_review_verdicts.yaml"
R21_VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
R25_VERDICTS = HERE / "c42_r25_review_verdicts.yaml"
OVERRIDES_R18 = HERE / "c42_section_overrides_r18.yaml"
OVERRIDES_R22 = HERE / "c42_section_overrides_r22.yaml"
OVERRIDES_R26 = HERE / "c42_section_overrides_r26.yaml"
AMENDMENT = HERE / "c42_r26_promotions_amendment.yaml"
R22_REPAIR_VERDICTS = HERE / "c42_r22_repair_verdicts.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
VERDICTS = HERE / "c42_r29_review_verdicts.yaml"
SHEET = GP.reports_dir(QUAL) / "C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md"
FILL_JSON = GP.reports_dir(QUAL) / "C42_R29_MATHS_A_REGATE_FILL_RECORD.json"
FILL_MD = GP.reports_dir(QUAL) / "C42_R29_MATHS_A_REGATE_FILL_RECORD.md"
FRESH_DOSSIER = Path("/home/z/my-project/scripts/c42_r29_fresh_dossier.json")

REVIEWER = ("Super Z (GLM agent), acting as operator-delegate under the operator's "
            "'R29 Re-gate' directive (2026-10-09, zai-web, gateway trace "
            "1a1213c84d375045) — the R28 record's next-decision gate (operator "
            "gate 2 re-run over the R28-rebuilt substrate, the loop's seventh "
            "gate-2 pass and the FIRST under the AMENDED promoted surface) "
            "fired verbatim; the human operator retains final sign-off; per "
            "the anti-forgery rule this re-gate VERIFIES the R5-promoted, "
            "R26-amended 831-row HUMAN_VALIDATED surface and never moves it")
REVIEW_DATE = "2026-10-09"
RC_ANCHOR = "spcpt_crKbmb6wVjM4yPJh"  # related-calculations — R10 STANDING
# the THREE R22 STANDING note-level joins (c42_r22_repair_verdicts.yaml,
# note_level_adjudications — list-shaped, the R23 precedent): the affected
# notes' other ords ride the note-level join on the joined_code.
R22_STANDING = {  # anchor_id -> (note_slug, joined_code)
    "spcpt_kX4655D8M3Q3TRzW": ("3d-pythagoras-and-trigonometry", "4MA1-4.8D"),
    "spcpt_RJbgRvXq2VrGpP5g": ("difference-of-two-squares", "4MA1-2.2F"),
    "spcpt_sHCB9WZbDMyTFqCP": ("graphical-solutions", "4MA1-2.6B"),
}

# the FOUR R26 STANDING note-level joins (c42_r26_repair_verdicts.yaml,
# note_level_adjudications — list-shaped, the R23 precedent; R27 pinned them
# in-generator fail-closed): the affected notes' joined-code rows ride the
# note-level join; same-anchor rows on OTHER codes (native attributions, e.g.
# the drawing-straight-line-graphs ords 2/3 on 3.3H) fall through to the
# carry/fresh ladder — the standing join covers the note's joined-code surface.
R26_STANDING = {  # anchor_id -> (note_slug, joined_code)
    "spcpt_J55PhZ2cbPsYvpt8": ("types-of-number", "4MA1-1.1G"),
    "spcpt_vMSNnYkKPf62MRH9": ("factorising-by-grouping", "4MA1-2.2F"),
    "spcpt_h8QyRmzX5mCJb3X9": ("drawing-straight-line-graphs", "4MA1-3.3F"),
    "spcpt_v6tP4DSVShVJMJhk": ("introduction-to-vectors", "4MA1-5.1D"),
}

# ---------------------------------------------------------------------------
# FRESH VERDICTS — the rows the four recorded evidence sources do not cover,
# loaded from the committed judgment file (encoded from the fresh-row dossier:
# each row judged against BOTH tier wordings + the chunk's own content, heading
# first, full text pulled where the heading was not decisive). PROPOSAL-ONLY
# candidates bind nothing; a row that does not teach the SP's demand is
# REJECTed with its root cause, never rationalized.
_FRESH_FILE = HERE / "c42_r29_fresh_verdicts.yaml"


def _load_fresh():
    if not _FRESH_FILE.exists():
        return {}  # dossier mode runs before the judgment file exists
    doc = yaml.safe_load(_FRESH_FILE.read_text(encoding="utf-8"))
    return {k: (v["verdict"], v["note"]) for k, v in doc["verdicts"].items()}


FRESH_VERDICTS: dict[str, tuple[str, str]] = _load_fresh()

# Part B — every worklist row is decided: DEFER with a recorded reason. The
# three templates are keyed by the store row's own disposition (set at R3).
PART_B_DEFER_RESIDUAL = (
    "the span anchor is the C32 §3 residual (spcpt_QWXhzVp2S3VYZdZc, 'Discrete & "
    "Continuous Data') — KEPT UNRESOLVED at R1 on the row's own PDF-verified reason "
    "(the 4MA1 print has no standalone discrete/continuous statement; the C32 "
    "scorer's proposals 6.2C/6.3G/6.1B teach unrelated content and were REJECTED); "
    "no chunk-level row can exist until the operator adjudicates the anchor — "
    "deferring is the honest disposition, never an invented code")
PART_B_DEFER_CLEARED_R1 = (
    "the span's R1 verdict (surface 1) is UNRESOLVED — the wrong T-SPEC-era code "
    "was CLEARED, never forced (no canonical 188 row teaches this note's subject: "
    "Mathematical Symbols / Problem Solving with Areas); the content chunks stay "
    "on the worklist and the resolution's PROPOSAL-ONLY candidates bind nothing — "
    "deferring to operator adjudication")
PART_B_DEFER_CLEARED_R6 = (
    "the span's R6 verdict (the second R1-shaped round, surface 1) is UNRESOLVED — "
    "the wrong T-SPEC-era code was CLEARED, never forced (no canonical 188 row "
    "teaches this note's subject: Problem Solving with Volumes / Geometrical "
    "Proof); the content chunks stay on the worklist and the resolution's "
    "PROPOSAL-ONLY candidates bind nothing — deferring to operator adjudication")
PART_B_DEFER_DEMOTE_R10 = (
    "the chunk was DEMOTEd to the worklist by the R10 verdict round (the scope §4 "
    "R1 menu's DEMOTE action, the loop's first) — the section teaches arithmetic "
    "inverse operations / related-fact derivation, 1.8D's demand is estimation, "
    "and no canonical 188 row teaches the section's content (the note-level join "
    "itself was adjudicated STANDING on the note's ord-3 estimation-to-check "
    "surface, so a REATTRIBUTE has no target); recorded, never forced — deferring "
    "to fresh notes coverage or a new operator anchor")
PART_B_DEFER_DEMOTE_R14 = (
    "the chunk was DEMOTEd to the worklist by the R14 verdict round (the scope §4 "
    "R1 menu's DEMOTE action, the loop's second exercise) — the section converts "
    "UNITS OF MASS (g/kg/tonne), 4.10F's demand is volume conversion, and no "
    "canonical 188 row teaches metric mass conversion per se (1.10B is "
    "calculations WITH standard units, not unit conversion; 4.9A's ledger "
    "Foundation wording covers linear and area units only, per the R6 ord-1 "
    "ruling; the note-level join STANDS on the note's ords 0/3 volume/capacity "
    "content, so a section-level REATTRIBUTE has no target); recorded, never "
    "forced — deferring to fresh notes coverage or a new operator anchor")
PART_B_DEFER_DEMOTE_R18 = (
    "the chunk was DEMOTEd to the worklist by the R18 verdict round (the scope §4 "
    "R1 menu's DEMOTE action, the loop's third exercise) — the section teaches "
    "LABELING conventions (line segment AB, angle ABC at point B, acute vs "
    "obtuse, triangle ABC), 4.1B's demand is angle properties of intersecting/ "
    "parallel lines and on a straight line, none taught, and no canonical 188 "
    "row teaches geometric labeling per se (the R18 proposals packet's top-1 for "
    "the row is 4.1B ITSELF at 0.167 — the scorer confirming the absence, the "
    "R14 mass-conversion-near-miss class); not a tier artifact (4.1B absent from "
    "the C30 ledger); the note-level join STANDS on the note's property sections "
    "(ords 0/2/3 — ord 0 CONFIRMed at R4; ord 4 the R1 4.2B ruling), so a "
    "REATTRIBUTE has no target and a RETAIN would knowingly re-create the scope "
    "difference for the next re-gate to reject again; recorded, never forced — "
    "deferring to fresh notes coverage or a new operator anchor")
PART_B_DEFER_DEMOTE_R26 = (
    "the chunk was DEMOTEd to the worklist by the R26 verdict round (the scope §4 "
    "R1 menu's DEMOTE action, the loop's fourth exercise and the FIRST of a "
    "PROMOTED row) — the section teaches FACTORISING BY GROUPING of a four-term "
    "two-variable expression (xy + 3x + 5y + 15), 2.2F's demand is capped "
    "'(limited to x^2 + bx + c)' and even 2.2B's un-limited Higher wording "
    "('a quadratic expression') does not reach it, and no canonical 188 row "
    "teaches four-term two-variable grouping per se (the R25 root's own "
    "finding; the operator's R26 directive named no re-anchor); the note-level "
    "join STANDS on the note's remaining 2.2F surface, so a REATTRIBUTE has no "
    "target; the promoted identity was excluded by the R26 promotions amendment "
    "(832 -> 831, the R5 file byte-untouched per the P5 convention); recorded, "
    "never forced — deferring to fresh notes coverage or a new operator anchor")
PART_B_DEFER_UNMAPPED = (
    "registered corpus gap at the post-R28 132-code coverage bound (130 at R25, "
    "129 at R21, 128 at R17, 127 at R13, 125 at R9, 122 at R3, 111 at C40 under "
    "the defective mapping) — no notes-corpus anchor resolves to this SP in the "
    "T-C32 join; closing it needs new SME content acquisition or an "
    "operator-authored anchor, not re-anchoring — deferring to the "
    "content-acquisition worklist (the chemistry 4.15 precedent)")


def sha16(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:16]


def load_inputs():
    store = GP.store("spec_chunk_mappings", QUAL)
    doc = yaml.safe_load(store.read_text(encoding="utf-8"))
    rows = doc["rows"]
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]
    ledger_map = {x["official_code"]: x for x in ledger}
    sp_doc = yaml.safe_load(
        GP.store("specification_points", QUAL).read_text(encoding="utf-8"))
    sp_by_code = {p["code"]: p for p in sp_doc["specification_points"]}
    r1 = yaml.safe_load(R1_VERDICTS.read_text(encoding="utf-8"))
    r6 = yaml.safe_load(R6_VERDICTS.read_text(encoding="utf-8"))
    r10 = yaml.safe_load(R10_VERDICTS.read_text(encoding="utf-8"))
    r14 = yaml.safe_load(R14_VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    ovr6 = yaml.safe_load(OVERRIDES_R6.read_text(encoding="utf-8"))
    ovr10 = yaml.safe_load(OVERRIDES_R10.read_text(encoding="utf-8"))
    ovr14 = yaml.safe_load(OVERRIDES_R14.read_text(encoding="utf-8"))
    ovr18 = yaml.safe_load(OVERRIDES_R18.read_text(encoding="utf-8"))
    ovr22 = yaml.safe_load(OVERRIDES_R22.read_text(encoding="utf-8"))
    r4 = yaml.safe_load(R4_VERDICTS.read_text(encoding="utf-8"))
    r9 = yaml.safe_load(R9_VERDICTS.read_text(encoding="utf-8"))
    r13 = yaml.safe_load(R13_VERDICTS.read_text(encoding="utf-8"))
    r17 = yaml.safe_load(R17_VERDICTS.read_text(encoding="utf-8"))
    r21 = yaml.safe_load(R21_VERDICTS.read_text(encoding="utf-8"))
    r25 = yaml.safe_load(R25_VERDICTS.read_text(encoding="utf-8"))
    r22 = yaml.safe_load(R22_REPAIR_VERDICTS.read_text(encoding="utf-8"))
    ovr26 = yaml.safe_load(OVERRIDES_R26.read_text(encoding="utf-8"))
    prom = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    amend = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
    conv = json.loads(CONVENTION_JSON.read_text(encoding="utf-8"))
    return (rows, ledger_map, sp_by_code, r1, r6, r10, r14, ovr, ovr6, ovr10,
            ovr14, ovr18, ovr22, ovr26, r4, r9, r13, r17, r21, r25, r22, prom,
            amend, conv)


def both_tier(row, ledger_map, sp_by_code) -> dict:
    """Resolve the row's tier-wording surface against BOTH tiers. The substrate
    rows carry the join's wording_check (EXACT = the resolution's official
    wording matches the store's Higher-operative wording; LEDGER_EXPLAINABLE =
    it matches the C30 ledger Foundation text while the store carries the
    Higher wording), not a copied wording — so the signature comes from
    wording_check, and the two tier texts themselves are verified at code
    level from the registry + the C30 ledger (the R1 standing instruction's
    evidence base). Fail-closed: any wording_check outside {EXACT,
    LEDGER_EXPLAINABLE}, a LEDGER_EXPLAINABLE row on a code absent from the
    ledger, or a shared code whose ledger.higher text disagrees with the
    registry wording aborts the fill (the C30 rule)."""
    code = row["spec_code"]                       # 4MA1-X.YZ
    bare = code.split("-", 1)[1]
    wc = row["provenance"]["upstream"].get("wording_check")
    store_w = norm(sp_by_code[code].get("official_wording") or "")
    lrow = ledger_map.get(bare)
    found_w = norm(lrow["foundation"]["text"]) if lrow else ""
    higher_w = norm(lrow["higher"]["text"]) if lrow else ""
    if lrow and store_w and higher_w and store_w != higher_w:
        print(f"LEDGER/STORE tier disagreement for {code}: store {store_w[:60]!r} "
              f"vs ledger.higher {higher_w[:60]!r}", file=sys.stderr)
        raise SystemExit(1)
    if wc == "EXACT":
        sig = "STORE_HIGHER"
    elif wc == "LEDGER_EXPLAINABLE":
        if not lrow:
            print(f"LEDGER_EXPLAINABLE row {row['mapping_id']} on code {code} "
                  f"absent from the C30 ledger — fail closed", file=sys.stderr)
            raise SystemExit(1)
        if store_w and found_w and store_w == found_w:
            sig = "BOTH_IDENTICAL"
        else:
            sig = "LEDGER_FOUNDATION"
    else:
        print(f"UNRESOLVED tier wording for {row['mapping_id']} ({code}): "
              f"wording_check={wc!r} — the R2 census pinned EXACT/"
              f"LEDGER_EXPLAINABLE only (DIVERGENT == 0)", file=sys.stderr)
        raise SystemExit(1)
    return {"tier_signature": sig, "store_higher": store_w or None,
            "ledger_foundation": found_w or None}


def main() -> int:
    emit_dossier = "--emit-dossier" in sys.argv
    (rows, ledger_map, sp_by_code, r1, r6, r10, r14, ovr, ovr6, ovr10, ovr14,
     ovr18, ovr22, ovr26, r4, r9, r13, r17, r21, r25, r22, prom, amend,
     conv) = load_inputs()
    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    worklist = [r for r in rows if "worklist_reason" in r]
    by_mid = {r["mapping_id"]: r for r in rows}

    # anti-forgery, re-shaped for the FIRST re-gate under a promoted surface:
    # (a) every row stays RULE_DERIVED (the provenance tier is the join's, the
    # §18 promotion moved only validation_status); (b) the HUMAN_VALIDATED set
    # must match the R5 promotions file ROW-FOR-ROW (identity + code + chunk
    # sha — the R24 re-application's byte-stability re-verified here); (c) the
    # SUGGESTED anchored rows must be exactly the expected 7 (3 R22
    # re-attributed + 4 convention H3 holds); (d) the worklist stays SUGGESTED.
    bad = [r for r in rows if r["provenance"]["tier"] != "RULE_DERIVED"]
    if bad:
        print(f"ANTI-FORGERY: {len(bad)} rows not RULE_DERIVED", file=sys.stderr)
        return 1
    hv_rows = [r for r in rows if r.get("validation_status") == "HUMAN_VALIDATED"]
    prom_rows = prom["promotions"]
    # the AMENDED promotions surface (the R26/R28 novelty, built here from the
    # two of-record carriers, fail-closed): the R5 file (byte-unchanged since
    # R5) AMENDED by the R26 promotions amendment — 3 supersedes re-keyed
    # old->new (the rows REMAIN promoted at their amended, code-derived
    # mapping ids) + 1 exclusion (the DEMOTE row, now unresolved-span).
    if amend["base_file_sha256_16"] != sha16(PROMOTIONS.read_bytes()):
        print("AMENDMENT BASE DRIFT: the R26 amendment's base pin != the live "
              "R5 promotions file — fail closed", file=sys.stderr)
        return 1
    rekey = {s["mapping_id"]: s for s in amend["supersedes_code"]}
    excl = {e["mapping_id"] for e in amend["excluded"]}
    prom_by_mid = {p["row"]["mapping_id"]: p for p in prom_rows}
    expected: dict[tuple, tuple] = {}
    for p in prom_rows:
        prow = p["row"]
        mid = prow["mapping_id"]
        if mid in excl:
            continue
        if mid in rekey:
            s = rekey[mid]
            if (prow.get("spec_code") != s["pinned_code"]
                    or prow["note_path"] != s["note_path"]
                    or prow["chunk_ordinal"] != s["chunk_ordinal"]):
                print(f"AMENDMENT PRE-APPLY INTEGRITY FAILED for {mid} "
                      f"(pinned_code/note/ordinal drift vs the R5 file) — "
                      f"fail closed", file=sys.stderr)
                return 1
            expected[(s["note_path"], s["chunk_ordinal"])] = (
                s["amended_code"], prow["heading"], prow["chunk_sha256_16"],
                f"rekeyed:{mid}")
        else:
            expected[(prow["note_path"], prow["chunk_ordinal"])] = (
                prow["spec_code"], prow["heading"], prow["chunk_sha256_16"], mid)
    if len(hv_rows) != len(expected):
        print(f"ANTI-FORGERY: HV count {len(hv_rows)} != amended promotions "
              f"count {len(expected)} (R5 {len(prom_rows)} - excluded "
              f"{len(excl)})", file=sys.stderr)
        return 1
    hv_bad = []
    seen = set()
    for r in hv_rows:
        key = (r["note_path"], r["chunk"]["ordinal"])
        exp = expected.get(key)
        if (exp is None or key in seen
                or r["spec_code"] != exp[0]
                or r["chunk"]["heading"] != exp[1]
                or r["chunk"]["sha256_16"] != exp[2]):
            hv_bad.append(r["mapping_id"])
        else:
            seen.add(key)
    if hv_bad or len(seen) != len(expected):
        unmatched = sorted(k[1] for k in set(expected) - seen)[:6]
        print(f"ANTI-FORGERY: {len(hv_bad)} HV rows drifted from the AMENDED "
              f"promotions surface (unmatched amendment entries at ordinals "
              f"{unmatched}): {hv_bad[:6]}", file=sys.stderr)
        return 1
    sug_anchored = {r["mapping_id"] for r in anchored
                    if r.get("validation_status") != "HUMAN_VALIDATED"}
    sug_bad = [r for r in anchored if r.get("validation_status") == "SUGGESTED"
               and not ("override" in r.get("provenance", {})
                        or r["spec_code"] in ("4MA1-1.7B", "4MA1-2.2C",
                                              "4MA1-3.3F", "4MA1-6.3J"))]
    if len(sug_anchored) != 7 or sug_bad:
        print(f"ANTI-FORGERY: anchored SUGGESTED set is {len(sug_anchored)} "
              f"(expected 7 = 3 R22 re-attributed + 4 H3 holds); unexpected "
              f"rows: {[r['mapping_id'] for r in sug_bad][:6]}", file=sys.stderr)
        return 1
    wl_bad = [r for r in worklist if r.get("validation_status") != "SUGGESTED"]
    if wl_bad:
        print(f"ANTI-FORGERY: {len(wl_bad)} worklist rows not SUGGESTED",
              file=sys.stderr)
        return 1
    print(f"anti-forgery: 918 rows RULE_DERIVED; 831 HV rows == the AMENDED "
          f"promotions surface row-for-row (R5 file sha16 "
          f"{sha16(PROMOTIONS.read_bytes())} + R26 amendment: 3 supersedes "
          f"re-keyed at 1.1A/5.1C/3.3H + 1 exclusion); 7 anchored SUGGESTED "
          f"(3 R22 re-attributed + 4 H3 holds); 80 worklist SUGGESTED")

    seed = sha16(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).encode())

    def stratum(r):
        s = r["provenance"]["upstream"].get("join_score")
        return "none" if s is None else ("exact" if float(s) >= 1.0 else "partial")

    def rank(mid):
        return sha16(f"{seed}|{mid}".encode())

    by = {}
    for r in anchored:
        if r.get("anchor", {}).get("ambiguous_hits", 0) == 0:
            by.setdefault(stratum(r), []).append(r)
    sample = []
    for cls in sorted(by):
        lst = sorted(by[cls], key=lambda r: rank(r["mapping_id"]))
        n = len(lst) if cls in ("none", "partial") else -(-len(lst) * 20 // 100)
        sample += [(cls, r) for r in lst[:n]]
    sample_ids = {r["mapping_id"] for _, r in sample}

    # ---- shared evidence indexes ---------------------------------------------
    r1_map = r1["verdicts"]                                    # anchor_id -> verdict
    r6_map = r6["verdicts"]                                    # anchor_id -> verdict
    r10_map = r10["verdicts"]                                  # anchor_id -> verdict
    r14_map = r14["verdicts"]                                  # anchor_id -> verdict
    ovr1_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr["overrides"]}
    ovr6_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr6["overrides"]}
    ovr10_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr10["overrides"]}
    ovr14_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr14["overrides"]}
    ovr18_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr18["overrides"]}
    ovr22_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr22["overrides"]}
    ovr26_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr26["overrides"]}
    r4_map = r4["verdicts"]                                    # mapping_id -> verdict
    r9_map = r9["verdicts"]                                    # mapping_id -> verdict
    r13_map = r13["verdicts"]                                  # mapping_id -> verdict
    r17_map = r17["verdicts"]                                  # mapping_id -> verdict
    r21_map = r21["verdicts"]                                  # mapping_id -> verdict
    r25_map = r25["verdicts"]                                  # mapping_id -> verdict

    r_reader = R()
    _, notes = load_corpus(r_reader)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}
    title_of = {n["manifest"]["path"]: n["note"].get("title") or "" for n in notes}

    def is_heading_only(np_, ordn) -> bool:
        """c42-heading-only-convention-1 detection: norm(chunk text) ==
        norm(heading), from the fresh re-chunking (never cached fields)."""
        t = idx.get((np_, ordn))
        return t is not None and norm(t) == norm(next(
            c["heading"] for c in by_note[np_] if c["ordinal"] == ordn))

    # the convention's H2 content-confirm index: (note_path, spec_code) ->
    # [content-row CONFIRM refs at R4/R9/R13/R17/R21/R25] — a heading-only row's
    # own prior CONFIRM NEVER satisfies H2 (only content rows count). NEW at
    # R29: the R25 record is in the source base (the carry-forward continuity
    # rule).
    h2_index: dict[tuple, list[str]] = {}
    for src_name, src_map in (("R4", r4_map), ("R9", r9_map), ("R13", r13_map),
                              ("R17", r17_map), ("R21", r21_map),
                              ("R25", r25_map)):
        for mid, v in src_map.items():
            if v["verdict"] != "CONFIRM" or v.get("note_path") is None:
                continue
            if is_heading_only(v["note_path"], v["chunk_ordinal"]):
                continue
            h2_index.setdefault((v["note_path"], v["spec_code"]), []).append(
                f"{src_name} row {mid} (ord {v['chunk_ordinal']} '{v['heading']}')")

    # ---- mechanical layer + both-tier resolution (all sampled rows) ----------
    mech_fail = 0
    tier_fail = 0
    tier_by_row: dict[str, dict] = {}
    for mid in sample_ids:
        r = by_mid[mid]
        ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        ok = (ctext is not None
              and sha16(ctext.encode()) == r["chunk"]["sha256_16"]
              and norm(r["evidence_quote"]) in norm(ctext)
              and r["chunk"]["heading"] == next(
                  c["heading"] for c in by_note[r["note_path"]]
                  if c["ordinal"] == r["chunk"]["ordinal"]))
        if not ok:
            mech_fail += 1
        try:
            tier_by_row[mid] = both_tier(r, ledger_map, sp_by_code)
        except SystemExit:
            tier_fail += 1
    if tier_fail:
        return 1
    print(f"mechanical layer: {len(sample_ids) - mech_fail}/{len(sample_ids)} PASS; "
          f"both-tier wording resolution: {len(sample_ids)}/{len(sample_ids)} "
          f"(DIVERGENT 0)")

    # ---- fresh-row dossier (semantic judgment input) --------------------------
    fresh_rows = []
    for cls, r in sample:
        mid = r["mapping_id"]
        aid = r["provenance"]["upstream"]["anchor_id"]
        on_r1 = aid in r1_map
        on_r6 = aid in r6_map
        on_r10 = aid in r10_map
        on_r14 = aid in r14_map
        has_ovr = "override" in r.get("provenance", {})
        has_sub = "override_subsumed" in r.get("provenance", {})
        standing = aid == RC_ANCHOR
        standing22 = aid in R22_STANDING
        ho = is_heading_only(r["note_path"], r["chunk"]["ordinal"])
        r25v = r25_map.get(mid)
        r21v = r21_map.get(mid)
        r17v = r17_map.get(mid)
        r13v = r13_map.get(mid)
        r9v = r9_map.get(mid)
        r4v = r4_map.get(mid)
        no_surface = ((not on_r1) and (not on_r6) and (not on_r10)
                      and (not on_r14) and not has_ovr and not has_sub
                      and not standing and not standing22 and not ho)

        def _triple(v):
            return (v is not None and v["verdict"] == "CONFIRM"
                    and v["spec_code"] == r["spec_code"]
                    and v["note_path"] == r["note_path"]
                    and v["heading"] == r["chunk"]["heading"])

        carried = (no_surface
                   and (_triple(r25v)
                        or (r25v is None and _triple(r21v))
                        or (r25v is None and r21v is None and _triple(r17v))
                        or (r25v is None and r21v is None and r17v is None
                            and _triple(r13v))
                        or (r25v is None and r21v is None and r17v is None
                            and r13v is None and _triple(r9v))
                        or (r25v is None and r21v is None and r17v is None
                            and r13v is None and r9v is None and _triple(r4v))))
        if (r25v is None and r21v is None and r17v is None and r13v is None
                and r9v is None and r4v is None and no_surface):
            fresh_rows.append((cls, r))
    if emit_dossier:
        dossier = []
        for cls, r in fresh_rows:
            dossier.append({
                "mapping_id": r["mapping_id"], "stratum": cls,
                "spec_code": r["spec_code"],
                "sp_store_wording": sp_by_code[r["spec_code"]]["official_wording"],
                "sp_ledger_foundation": (ledger_map.get(
                    r["spec_code"].split("-", 1)[1], {}) or {}).get("foundation", {}).get("text"),
                "note_title": title_of.get(r["note_path"], ""),
                "note_path": r["note_path"],
                "chunk_ordinal": r["chunk"]["ordinal"],
                "chunk_heading": r["chunk"]["heading"],
                "chunk_chars": r["chunk"]["chars"],
                "chunk_text": idx.get((r["note_path"], r["chunk"]["ordinal"])),
                "evidence_quote": r["evidence_quote"],
                "join_tier": r["provenance"]["upstream"].get("join_tier"),
                "join_score": r["provenance"]["upstream"].get("join_score"),
                "wording_check": r["provenance"]["upstream"].get("wording_check"),
                "tier_signature": tier_by_row[r["mapping_id"]]["tier_signature"],
            })
        FRESH_DOSSIER.parent.mkdir(parents=True, exist_ok=True)
        FRESH_DOSSIER.write_text(
            json.dumps(dossier, indent=1, ensure_ascii=False), encoding="utf-8")
        print(f"dossier: {len(dossier)} fresh rows -> {FRESH_DOSSIER}")
        return 0

    # ---- verdict assignment (fail-closed coverage) -----------------------------
    verdicts: dict[str, dict] = {}
    src_count = Counter()

    def put(r, verdict, source, note, root=None, convention_branch=None):
        mid = r["mapping_id"]
        if mid in verdicts:
            print(f"DOUBLE VERDICT for {mid}", file=sys.stderr)
            return 1
        verdicts[mid] = {
            "verdict": verdict, "source": source, "root": root,
            "convention_branch": convention_branch,
            "stratum": stratum(r), "note": note,
            "spec_code": r["spec_code"], "note_path": r["note_path"],
            "chunk_ordinal": r["chunk"]["ordinal"], "heading": r["chunk"]["heading"],
            "both_tier": tier_by_row[mid],
        }
        src_count[source] += 1
        return 0

    err = 0
    for cls, r in sample:
        mid = r["mapping_id"]
        up = r["provenance"]["upstream"]
        sig = tier_by_row[mid]["tier_signature"]
        aid = up["anchor_id"]
        o = r.get("provenance", {}).get("override")
        os_ = r.get("provenance", {}).get("override_subsumed")
        a1 = r1_map.get(aid)
        a6 = r6_map.get(aid)
        a10 = r10_map.get(aid)
        a14 = r14_map.get(aid)
        ho = is_heading_only(r["note_path"], r["chunk"]["ordinal"])
        if os_:  # an R1 entry riding the R6 note-level repair (subsumption registry)
            v6 = a6 if a6 and a6["disposition"] == "CORRECT" else None
            note = (f"R1 section-level override SUBSUMED by the R6 note-level repair "
                    f"(provenance.override_subsumed, {r['note_slug']}#{r['chunk']['ordinal']}): "
                    f"the R6 round re-pointed this note's join to "
                    f"{os_.get('r1_override_code')} — exactly the R1 override's target — so "
                    f"the section now rides the join and the R1 correction is satisfied by "
                    f"the note-level verdict "
                    f"({v6['prior_code']} -> {v6['corrected_code']}). Both tier wordings "
                    f"consulted ({sig}); mechanical layer re-verified.")
            err += put(r, "CONFIRM", "r1-subsumed", note,
                       convention_branch="H1 (anchor verdict standing)" if ho else None)
        elif o:
            rnd = o.get("operator_round") or ""
            if rnd.startswith("C42 R26"):
                ov = ovr26_map[(r["note_slug"], r["chunk"]["ordinal"])]
                note = (f"R26 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); the row rides "
                        f"the loop's FIRST repair round over the promoted surface — "
                        f"the R26 promotions amendment re-keyed its promoted identity "
                        f"old->new code (the R5 promotions file byte-untouched per "
                        f"the P5 convention; the amendment is the dated record); both "
                        f"tier wordings consulted ({sig}); mechanical layer "
                        f"re-verified.")
                err += put(r, "CONFIRM", "r26-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            elif rnd.startswith("C42 R22"):
                ov = ovr22_map[(r["note_slug"], r["chunk"]["ordinal"])]
                note = (f"R22 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance." 
                        f"override present, spec_code == override_code); the row stayed "
                        f"SUGGESTED through the R5 apply and the R24 re-build (the R22 "
                        f"record's disposition: the 3 REJECT rows are the honest residue "
                        f"the R21 fill returned to the operator); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r22-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            elif rnd.startswith("C42 R18"):
                ov = ovr18_map[(r["note_slug"], r["chunk"]["ordinal"])]
                cls_tag = (f", provenance_class {ov.get('provenance_class', 'verdicted')}"
                           if ov.get("provenance_class") == "extension" else "")
                note = (f"R18 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}{cls_tag}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r18-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            elif rnd.startswith("C42 R14"):
                ov = ovr14_map[(r["note_slug"], r["chunk"]["ordinal"])]
                note = (f"R14 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r14-section-override", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            elif rnd.startswith("C42 R10"):
                ov = ovr10_map[(r["note_slug"], r["chunk"]["ordinal"])]
                note = (f"R10 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r10-section-override", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            elif rnd.startswith("C42 R6"):
                ov = ovr6_map[(r["note_slug"], r["chunk"]["ordinal"])]
                cls_tag = (f", provenance_class {ov.get('provenance_class', 'verdicted')}"
                           if ov.get("provenance_class") == "extension" else "")
                note = (f"R6 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}{cls_tag}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r6-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            elif o["action"] == "REATTRIBUTE":
                ov = ovr1_map[(r["note_slug"], r["chunk"]["ordinal"])]
                note = (f"R1 section-level REATTRIBUTE (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): the join-derived "
                        f"{ov['current_code']} re-attributed to {ov['override_code']} — "
                        f"evidence: {ov['evidence']}. The ruling landed (provenance."
                        f"override present, spec_code == override_code); both tier "
                        f"wordings consulted ({sig}); mechanical layer re-verified.")
                err += put(r, "CONFIRM", "r1-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            elif "heading-only" in (o.get("evidence") or ""):
                # c42-heading-only-convention-1: the R1-era RETAIN rows are no
                # longer ad-hoc HOLDs — the R10 convention's ladder resolves
                # them (H1/H2/H3), with per-row provenance. The R1 ruling's
                # attribution stands unchanged either way.
                refs = h2_index.get((r["note_path"], r["spec_code"])) or []
                if refs:
                    note = (f"R1 section-level RETAIN (operator override map, "
                            f"{r['note_slug']}#{r['chunk']['ordinal']}): {o.get('evidence')}. "
                            f"RESOLVED by c42-heading-only-convention-1 branch H2 "
                            f"(content standing): the note carries content-row "
                            f"CONFIRMs on {r['spec_code']} — {'; '.join(refs[:3])}"
                            f"{f'; +{len(refs)-3} more' if len(refs) > 3 else ''} — "
                            f"and the chunk is a heading-only structural slice of "
                            f"the corpus's own spec_point span. Both tier wordings "
                            f"consulted ({sig}); mechanical layer re-verified.")
                    err += put(r, "CONFIRM", "heading-only-convention", note,
                               convention_branch="H2 (content standing)")
                else:
                    note = (f"R1 section-level RETAIN (operator override map, "
                            f"{r['note_slug']}#{r['chunk']['ordinal']}): {o.get('evidence')}. "
                            f"c42-heading-only-convention-1 branch H3 (fail-closed): "
                            f"no operator verdict on the anchor and no content-row "
                            f"CONFIRM of {r['spec_code']} at R4/R9/R13/R17 — the row stays "
                            f"HOLD, explicit and recorded; it un-holds automatically "
                            f"when H1/H2 becomes true. Not auto-promoted at R5 "
                            f"without the operator's explicit per-row sign-off.")
                    err += put(r, "HOLD", "heading-only-convention", note,
                               root="heading-only H3 (fail-closed, no positive evidence)",
                               convention_branch="H3 (fail-closed HOLD)")
            elif "generic note-intro" in (o.get("evidence") or ""):
                note = (f"R1 section-level RETAIN (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): {o.get('evidence')}. "
                        f"The C40 convention anchors intro sections at the note's SP; "
                        f"the chunk teaches no different SP's content; both tier "
                        f"wordings consulted ({sig}).")
                err += put(r, "CONFIRM", "r1-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
            else:  # averages-from-tables mode — the wording-tier artifact class
                note = (f"R1 section-level RETAIN (operator override map, "
                        f"{r['note_slug']}#{r['chunk']['ordinal']}): {o.get('evidence')}. "
                        f"Wording-tier artifact, same class as the id-level AFFIRM "
                        f"set — adjudicated on BOTH tier wordings ({sig}) "
                        f"per the standing instruction.")
                err += put(r, "CONFIRM", "r1-section-override", note,
                           convention_branch="H1 (operator section ruling)" if ho else None)
        elif a14:
            disp = a14["disposition"]
            if disp == "CORRECT":
                note = (f"R14 operator verdict CORRECT (verdicts record "
                        f"{aid}, the fourth R1-shaped round over the R13 re-gate's "
                        f"6-row defect inventory): {a14['prior_code']} -> "
                        f"{a14['corrected_code']}; the re-pointed attribution landed "
                        f"wholesale (all 5 of the note's store rows re-attributed at "
                        f"R15/R16; spec_code == corrected code). Both tier wordings "
                        f"consulted ({sig}). R14 evidence: {a14['evidence']}")
                err += put(r, "CONFIRM", "r14-id-verdict", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            else:
                print(f"anchor {aid} disposition {disp} has an anchored row "
                      f"{mid} — UNRESOLVED anchors cannot carry rows", file=sys.stderr)
                err += 1
        elif a10:
            disp = a10["disposition"]
            if disp == "CORRECT":
                note = (f"R10 operator verdict CORRECT (verdicts record "
                        f"{aid}, the third R1-shaped round over the R9 defect "
                        f"inventory): {a10['prior_code']} -> "
                        f"{a10['corrected_code']}; the re-pointed attribution landed "
                        f"(spec_code == corrected code). Both tier wordings consulted "
                        f"({sig}). R10 evidence: {a10['evidence']}")
                err += put(r, "CONFIRM", "r10-id-verdict", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            else:
                print(f"anchor {aid} disposition {disp} has an anchored row "
                      f"{mid} — UNRESOLVED anchors cannot carry rows", file=sys.stderr)
                err += 1
        elif aid == RC_ANCHOR:
            # the R10 note-level STANDING adjudication (related-calculations)
            note = (f"R10 NOTE-LEVEL ADJUDICATION (verdicts record, "
                    f"note_level_adjudications.related-calculations): the 1.8D join "
                    f"STANDS on the note's ord-3 estimation-to-check surface (an "
                    f"Exam Hint + a full worked example teaching rounding-to-1-s.f. "
                    f"order-of-magnitude checks = 1.8D's demand verbatim; 1.8D is "
                    f"Foundation-only, so not a wording-tier artifact) — the R9 "
                    f"root's name-fragment suspicion examined and rejected. Both "
                    f"tier wordings consulted ({sig}); mechanical layer re-verified.")
            err += put(r, "CONFIRM", "r10-standing", note,
                       convention_branch="H1 (R10 note-level STANDING adjudication)" if ho else None)
        elif aid in R22_STANDING:
            # the THREE R22 STANDING note-level joins (c42_r22_repair_verdicts.yaml,
            # note_level_adjudications — list-shaped, the R23 precedent)
            slug, joined = R22_STANDING[aid]
            if r["spec_code"] != joined:
                print(f"R22 STANDING anchor {aid} row {mid} on {r['spec_code']} "
                      f"!= the adjudicated joined code {joined} — fail closed",
                      file=sys.stderr)
                err += 1
                continue
            note = (f"R22 NOTE-LEVEL STANDING ADJUDICATION (c42_r22_repair_verdicts.yaml, "
                    f"note_level_adjudications, list-shaped — the R23 precedent): the "
                    f"note-level join to {joined} STANDS (the R22 round's per-note basis: "
                    f"the note's own {'Pythagoras' if slug == '3d-pythagoras-and-trigonometry' else ('within-limit basic DOTS' if slug == 'difference-of-two-squares' else 'lines-based')} "
                    f"surface carries the demand — the ord-level REJECT was a "
                    f"SECTION-level scope difference only, re-homed by the R22 override "
                    f"map); the note's other ords ride the standing join. Both tier "
                    f"wordings consulted ({sig}); mechanical layer re-verified.")
            err += put(r, "CONFIRM", "r22-standing", note,
                       convention_branch="H1 (R22 note-level STANDING adjudication)" if ho else None)
        elif aid in R26_STANDING and r["spec_code"] == R26_STANDING[aid][1]:
            # the FOUR R26 STANDING note-level joins (c42_r26_repair_verdicts.yaml,
            # note_level_adjudications — list-shaped, the R23 precedent)
            slug, joined = R26_STANDING[aid]
            note = (f"R26 NOTE-LEVEL STANDING ADJUDICATION (c42_r26_repair_verdicts.yaml, "
                    f"note_level_adjudications, list-shaped — the R23 precedent): the "
                    f"note-level join to {joined} STANDS (the R26 round's per-note basis: "
                    f"the note's own surface carries the demand — the R25 inventory's "
                    f"question examined and the join affirmed with 0 resolution "
                    f"amendments, the R27 in-generator pins fail-closed); the note's "
                    f"joined-code rows ride the standing join. Both tier "
                    f"wordings consulted ({sig}); mechanical layer re-verified.")
            err += put(r, "CONFIRM", "r26-standing", note,
                       convention_branch="H1 (R26 note-level STANDING adjudication)" if ho else None)
        elif a6:
            disp = a6["disposition"]
            if disp == "CORRECT":
                note = (f"R6 operator verdict CORRECT (verdicts record "
                        f"{aid}, the second R1-shaped round over the R4 defect "
                        f"inventory): {a6['prior_code']} -> "
                        f"{a6['corrected_code']}; the re-pointed attribution landed "
                        f"(spec_code == corrected code). Both tier wordings consulted "
                        f"({sig}). R6 evidence: {a6['evidence']}")
                err += put(r, "CONFIRM", "r6-id-verdict", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            else:
                print(f"anchor {aid} disposition {disp} has an anchored row "
                      f"{mid} — UNRESOLVED anchors cannot carry rows", file=sys.stderr)
                err += 1
        elif a1:
            disp = a1["disposition"]
            if disp == "AFFIRM":
                note = (f"R1 operator verdict AFFIRM (verdicts record "
                        f"{aid}, code unchanged; still standing after R6): the C40-era "
                        f"reject was a WORDING-TIER ARTIFACT — the join is correct at "
                        f"Foundation tier. Both tier wordings consulted ({sig}): "
                        f"store '{tier_by_row[mid]['store_higher']}' / ledger "
                        f"foundation '{tier_by_row[mid]['ledger_foundation']}'. "
                        f"R1 evidence: {a1['evidence']}")
                err += put(r, "CONFIRM", "r1-id-verdict", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            elif disp == "CORRECT":
                note = (f"R1 operator verdict CORRECT (verdicts record "
                        f"{aid}; still standing after R6): {a1['prior_code']} -> "
                        f"{a1['corrected_code']}; the re-pointed attribution landed "
                        f"(spec_code == corrected code). Both tier wordings consulted "
                        f"({sig}). R1 evidence: {a1['evidence']}")
                err += put(r, "CONFIRM", "r1-id-verdict", note,
                           convention_branch="H1 (anchor verdict standing)" if ho else None)
            else:
                print(f"anchor {aid} disposition {disp} has an anchored row "
                      f"{mid} — UNRESOLVED anchors cannot carry rows", file=sys.stderr)
                err += 1
        else:
            r25v = r25_map.get(mid)
            r21v = r21_map.get(mid)
            r17v = r17_map.get(mid)
            r13v = r13_map.get(mid)
            r9v = r9_map.get(mid)
            r4v = r4_map.get(mid)
            r25_carried = (r25v is not None and r25v["verdict"] == "CONFIRM"
                           and r25v["spec_code"] == r["spec_code"]
                           and r25v["note_path"] == r["note_path"]
                           and r25v["heading"] == r["chunk"]["heading"])
            r21_carried = (r25v is None and r21v is not None
                           and r21v["verdict"] == "CONFIRM"
                           and r21v["spec_code"] == r["spec_code"]
                           and r21v["note_path"] == r["note_path"]
                           and r21v["heading"] == r["chunk"]["heading"])
            r17_carried = (r25v is None and r21v is None and r17v is not None
                           and r17v["verdict"] == "CONFIRM"
                           and r17v["spec_code"] == r["spec_code"]
                           and r17v["note_path"] == r["note_path"]
                           and r17v["heading"] == r["chunk"]["heading"])
            r13_carried = (r25v is None and r21v is None and r17v is None
                           and r13v is not None
                           and r13v["verdict"] == "CONFIRM"
                           and r13v["spec_code"] == r["spec_code"]
                           and r13v["note_path"] == r["note_path"]
                           and r13v["heading"] == r["chunk"]["heading"])
            r9_carried = (r25v is None and r21v is None and r17v is None
                          and r13v is None and r9v is not None and r9v["verdict"] == "CONFIRM"
                          and r9v["spec_code"] == r["spec_code"]
                          and r9v["note_path"] == r["note_path"]
                          and r9v["heading"] == r["chunk"]["heading"])
            r4_carried = (r25v is None and r21v is None and r17v is None
                          and r13v is None and r9v is None
                          and r4v is not None and r4v["verdict"] == "CONFIRM"
                          and r4v["spec_code"] == r["spec_code"]
                          and r4v["note_path"] == r["note_path"]
                          and r4v["heading"] == r["chunk"]["heading"])
            if ho:
                # c42-heading-only-convention-1 — the ladder's remaining branches
                # for rows with no direct verdict source
                if aid == RC_ANCHOR:
                    note = ("c42-heading-only-convention-1 branch H1 (the R10 "
                            "note-level STANDING adjudication): the chunk is a "
                            "heading-only structural slice of the corpus's own "
                            "spec_point span; the span's join was adjudicated "
                            "STANDING at R10. Both tier wordings consulted "
                            f"({sig}); mechanical layer re-verified.")
                    err += put(r, "CONFIRM", "heading-only-convention", note,
                               convention_branch="H1 (R10 note-level STANDING adjudication)")
                elif aid in R22_STANDING:
                    slug, joined = R22_STANDING[aid]
                    note = ("c42-heading-only-convention-1 branch H1 (the R22 "
                            "note-level STANDING adjudication): the chunk is a "
                            "heading-only structural slice of the corpus's own "
                            "spec_point span; the span's join was adjudicated "
                            f"STANDING at R22 ({joined}). Both tier wordings "
                            f"consulted ({sig}); mechanical layer re-verified.")
                    err += put(r, "CONFIRM", "heading-only-convention", note,
                               convention_branch="H1 (R22 note-level STANDING adjudication)")
                elif aid in R26_STANDING and r["spec_code"] == R26_STANDING[aid][1]:
                    slug, joined = R26_STANDING[aid]
                    note = ("c42-heading-only-convention-1 branch H1 (the R26 "
                            "note-level STANDING adjudication): the chunk is a "
                            "heading-only structural slice of the corpus's own "
                            "spec_point span; the span's join was adjudicated "
                            f"STANDING at R26 ({joined}). Both tier wordings "
                            f"consulted ({sig}); mechanical layer re-verified.")
                    err += put(r, "CONFIRM", "heading-only-convention", note,
                               convention_branch="H1 (R26 note-level STANDING adjudication)")
                else:
                    refs = h2_index.get((r["note_path"], r["spec_code"])) or []
                    if refs:
                        note = ("c42-heading-only-convention-1 branch H2 (content "
                                "standing): the chunk is a heading-only structural "
                                "slice of the corpus's own spec_point span, and the "
                                "note carries content-row CONFIRMs on "
                                f"{r['spec_code']} — {'; '.join(refs[:3])}"
                                f"{f'; +{len(refs)-3} more' if len(refs) > 3 else ''}. "
                                f"Both tier wordings consulted ({sig}); mechanical "
                                "layer re-verified.")
                        err += put(r, "CONFIRM", "heading-only-convention", note,
                                   convention_branch="H2 (content standing)")
                    else:
                        note = ("c42-heading-only-convention-1 branch H3 "
                                "(fail-closed): the chunk is a heading-only "
                                "structural slice with no operator verdict on its "
                                f"anchor and no content-row CONFIRM of {r['spec_code']} "
                                "at R4/R9/R13/R17/R21 — the row stays HOLD, explicit and "
                                "recorded; it un-holds automatically when H1/H2 "
                                "becomes true. Not promoted at R5 without the "
                                "operator's explicit per-row sign-off (still owed per "
                                "the R24 record).")
                        err += put(r, "HOLD", "heading-only-convention", note,
                                   root="heading-only H3 (fail-closed, no positive evidence)",
                                   convention_branch="H3 (fail-closed HOLD)")
            elif r25_carried:
                r25_note = r25v["note"] or ("topical fidelity confirmed on the "
                                            "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R25 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk identity + W4 zero-drift "
                        f"hold; row outside the R26 surface): {r25_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r25-carried", note)
            elif r21_carried:
                r21_note = r21v["note"] or ("topical fidelity confirmed on the "
                                            "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R21 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk identity + W4 zero-drift "
                        f"hold; row outside the R22 surface): {r21_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r21-carried", note)
            elif r17_carried:
                r17_note = r17v["note"] or ("topical fidelity confirmed on the "
                                            "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R17 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk identity + W4 zero-drift "
                        f"hold; not sampled at R21, row outside the R18 surface): {r17_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r17-carried", note)
            elif r13_carried:
                r13_note = r13v["note"] or ("topical fidelity confirmed on the "
                                            "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R13 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk identity + W4 zero-drift "
                        f"hold; not sampled at R17, row outside the R14/R18 surfaces): "
                        f"{r13_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r13-carried", note)
            elif r9_carried:
                r9_note = r9v["note"] or ("topical fidelity confirmed on the "
                                          "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R9 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk-identity invariant "
                        f"holds, not sampled at R13 or R17, row outside the "
                        f"R10/R14/R18 surfaces): {r9_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r9-carried", note)
            elif r4_carried:
                r4_note = r4v["note"] or ("topical fidelity confirmed on the "
                                          "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R4 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk-identity invariant "
                        f"holds; not sampled at R9, R13 or R17, outside the "
                        f"R10/R14/R18 surfaces): {r4_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r4-carried", note)
            elif mid in FRESH_VERDICTS:
                v, note = FRESH_VERDICTS[mid]
                err += put(r, v, "r29-fresh",
                           f"{note} Both tier wordings consulted ({sig}).",
                           root=None if v == "CONFIRM" else "recorded in note")
            else:
                print(f"UNCOVERED sampled row {mid} ({r['spec_code']} "
                      f"{r['note_path']} ord {r['chunk']['ordinal']}) — no source",
                      file=sys.stderr)
                err += 1
    if err:
        print(f"{err} verdict-assignment errors — fail closed", file=sys.stderr)
        return 1

    # ---- Part B verdicts -------------------------------------------------------
    part_b = {}
    for r in worklist:
        disp = r.get("disposition") or ""
        if "C32 §3 residual" in disp:
            why, surf = PART_B_DEFER_RESIDUAL, "C32 §3 residual (R1 KEPT UNRESOLVED)"
        elif "C42 R1 surface 1" in disp:
            why, surf = PART_B_DEFER_CLEARED_R1, "C42 R1 surface-1 cleared span"
        elif "C42 R6 surface 1" in disp:
            why, surf = PART_B_DEFER_CLEARED_R6, "C42 R6 surface-1 cleared span"
        elif "C42 R10 surface 2" in disp:
            why, surf = PART_B_DEFER_DEMOTE_R10, "C42 R10 surface-2 DEMOTE (recorded, never forced)"
        elif "C42 R14" in disp:
            why, surf = PART_B_DEFER_DEMOTE_R14, "C42 R14 surface-3 DEMOTE (recorded, never forced)"
        elif "C42 R18" in disp:
            why, surf = PART_B_DEFER_DEMOTE_R18, "C42 R18 surface-3 DEMOTE (recorded, never forced)"
        elif "C42 R26" in disp:
            why, surf = PART_B_DEFER_DEMOTE_R26, (
                "C42 R26 surface-3 DEMOTE (recorded, never forced — the loop's "
                "fourth DEMOTE, the FIRST of a promoted row)")
        else:
            why, surf = PART_B_DEFER_UNMAPPED, "uncovered-SP corpus gap (132-code bound)"
        part_b[r["mapping_id"]] = {
            "verdict": "DEFER", "surface": surf,
            "spec_code": r.get("spec_code"), "note_path": r.get("note_path"),
            "why": why,
        }

    # ---- gate arithmetic (the scope's rule, unchanged) --------------------------
    rollup = {}
    for cls in ("exact", "partial", "none"):
        rows_c = [v for v in verdicts.values() if v["stratum"] == cls]
        conf = sum(1 for v in rows_c if v["verdict"] == "CONFIRM")
        rej = sum(1 for v in rows_c if v["verdict"] == "REJECT")
        hold = sum(1 for v in rows_c if v["verdict"] == "HOLD")
        rollup[cls] = {"rows": len(rows_c), "confirm": conf, "reject": rej,
                       "hold": hold,
                       "precision": round(conf / len(rows_c), 4) if rows_c else None}
    total = {"rows": len(verdicts),
             "confirm": sum(1 for v in verdicts.values() if v["verdict"] == "CONFIRM"),
             "reject": sum(1 for v in verdicts.values() if v["verdict"] == "REJECT"),
             "hold": sum(1 for v in verdicts.values() if v["verdict"] == "HOLD")}
    total["precision"] = round(total["confirm"] / total["rows"], 4)
    gate_classes_pass = all(v["precision"] >= 0.9 for v in rollup.values() if v["rows"])
    part_b_decided = len(part_b) == len(worklist)
    gate_pass = gate_classes_pass and part_b_decided and mech_fail == 0

    # ---- write the verdict record ------------------------------------------------
    vdoc = {
        "schema": "c42-r29-review-verdicts/1.0",
        "task": "T-C42",
        "stage": "r29-regate-fill",
        "contract": "graph/reports/C42_R29_MATHS_A_REGATE_REVIEW_SHEET.md "
                    "(the C12/C13 promotion-gate convention, re-stratified over the "
                    "R28-rebuilt substrate under the AMENDED R5-promoted surface; "
                    "c42-heading-only-convention-1 in force with the R25 record "
                    "new in the ladder's source base)",
        "supersedes": "scripts/c42_r25_review_verdicts.yaml (the R25-era re-gate fill; "
                      "kept on its own record, never edited)",
        "reviewer": REVIEWER,
        "review_date": REVIEW_DATE,
        "method": {
            "mechanical": f"quote-in-chunk + chunk-hash/heading agreement vs a fresh "
                      f"re-chunking + the amended-surface anti-forgery sweep "
                      f"(831 HV rows == the R5 promotions file AMENDED by the R26 "
                      f"amendment, row-for-row by chunk identity; 7 anchored "
                      f"SUGGESTED; all RULE_DERIVED), "
                      f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS",
            "both_tier_wording": "EVERY sampled row's upstream official wording "
                                 "resolved against the store's Higher-operative "
                                 "wording AND the C30 ledger foundation.text "
                                 "(tier_signature per row; DIVERGENT fails the fill "
                                 "closed) — the R1 standing instruction, applied",
            "semantic": "per-row topical fidelity against BOTH tier wordings and the "
                        "chunk content; verdict sources: the R26 section-override "
                        "rulings (the seventh R1-shaped round and the FIRST over the "
                        "promoted surface: 3 verdicted REATTRIBUTEs 1.1G -> 1.1A / "
                        "5.1D -> 5.1C / 3.3F -> 3.3H, the promoted identities "
                        "re-keyed by the R26 amendment) + the FOUR R26 STANDING "
                        "note-level joins, the R22 section-override rulings + the "
                        "THREE R22 STANDING note-level joins, the R18 "
                        "section-override rulings, the R14 operator id-verdict "
                        "(3.3I -> 3.2D) + the R14 section-override rulings, the R10 "
                        "operator id-verdicts + the R10 note-level STANDING "
                        "adjudication (still standing), the R6 + R1 operator "
                        "id-verdicts (still standing), the R14 + R10 + R6 + R1 "
                        "section-override rulings, the 2 R1-subsumed entries riding "
                        "the join, c42-heading-only-convention-1 (the H1/H2/H3 ladder "
                        "with the R25 record new in its source base) for the "
                        "heading-only class, CONFIRM carry-forward for "
                        "triple-identical R25/R21/R17/R13/R9/R4 rows outside the R26 "
                        "surface, and fresh judgment for the remainder",
        },
        "sampling": {
            "seed": seed,
            "rule": "identical to the C40 convention: low-assurance strata (join "
                    "score <1.0 or absent) at 100%, score == 1.0 at ceil(20%), "
                    "seeded by sha256 of the emitted rows; ambiguous_hits == 0",
            "strata": {cls: len(by[cls]) for cls in sorted(by)},
            "sampled": {cls: sum(1 for c, _ in sample if c == cls)
                        for cls in sorted(by)},
        },
        "gate": {
            "rule": "Part A precision >= 90% per class AND every Part B row decided "
                    "AND mechanical layer clean",
            "part_a": {"total": total, "by_stratum": rollup,
                       "classes_pass": gate_classes_pass},
            "part_b": {"rows": len(part_b), "decided": part_b_decided,
                       "defer": sum(1 for v in part_b.values()
                                    if v["verdict"] == "DEFER"),
                       "surfaces": dict(Counter(v["surface"]
                                                for v in part_b.values()))},
            "outcome": "PASS" if gate_pass else "FAIL",
            "outcome_note": None if gate_pass else
                "the promotion is NOT authorized by this fill",
        },
        "verdict_sources": dict(src_count),
        "verdicts": verdicts,
        "part_b_verdicts": part_b,
    }
    VERDICTS.write_text(yaml.safe_dump(vdoc, allow_unicode=True, sort_keys=False,
                                       width=100), encoding="utf-8")

    # ---- fill the sheet (deterministic re-render from store + verdicts) ----------
    a_blocks = []
    for cls, r in sample:
        v = verdicts[r["mapping_id"]]
        c = idx[(r["note_path"], r["chunk"]["ordinal"])]
        excerpt = " ".join(c.split())[:420]
        up = r["provenance"]["upstream"]
        score_s = "n/a" if up.get("join_score") is None else str(up["join_score"])
        bt = v["both_tier"]
        boxes = {
            "CONFIRM": "[x] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework",
            "REJECT": "[ ] CONFIRM — this chunk belongs to this SP   [x] REJECT — wrong chunk/SP   [ ] HOLD — needs rework",
            "HOLD": "[ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [x] HOLD — needs rework",
        }[v["verdict"]]
        src_line = {
            "r26-section-override": "R26 operator section-override ruling (the seventh R1-shaped round and the FIRST over the promoted surface: 3 verdicted REATTRIBUTEs 1.1G->1.1A / 5.1D->5.1C / 3.3F->3.3H, the promoted identities re-keyed by the R26 amendment)",
            "r22-section-override": "R22 operator section-override ruling (the sixth R1-shaped round: 3 verdicted REATTRIBUTEs 4.8D->4.8F / 2.2F->2.2B / 2.6B->3.3E)",
            "r26-standing": "R26 note-level STANDING adjudication (the four list-shaped joins: types-of-number -> 1.1G, factorising-by-grouping -> 2.2F, drawing-straight-line-graphs -> 3.3F, introduction-to-vectors -> 5.1D)",
            "r22-standing": "R22 note-level STANDING adjudication (the three list-shaped joins: 3d-pythagoras -> 4.8D, difference-of-two-squares -> 2.2F, graphical-solutions -> 2.6B)",
            "r18-section-override": "R18 operator section-override ruling (the fifth R1-shaped round: verdicted + labeled-extension REATTRIBUTEs)",
            "r14-id-verdict": "R14 operator id-verdict (CORRECT re-point) evidence — the fourth R1-shaped round, still standing",
            "r14-section-override": "R14 operator section-override ruling (verdicted REATTRIBUTE)",
            "r10-id-verdict": "R10 operator id-verdict (CORRECT) evidence — the third R1-shaped round, still standing",
            "r10-standing": "R10 note-level STANDING adjudication (related-calculations joins 1.8D)",
            "r10-section-override": "R10 operator section-override ruling (verdicted REATTRIBUTE)",
            "r6-id-verdict": "R6 operator id-verdict (CORRECT) evidence — the second R1-shaped round, still standing",
            "r1-id-verdict": "R1 operator id-verdict (AFFIRM/CORRECT) evidence — still standing",
            "r6-section-override": "R6 operator section-override ruling (verdicted or labeled extension)",
            "r1-section-override": "R1 operator section-override ruling",
            "heading-only-convention": "c42-heading-only-convention-1 (the R10 convention decision; H1/H2/H3 ladder with per-row provenance; the R21 record new in the H2 source base)",
            "r1-subsumed": "R1 override riding the R6 note-level repair (provenance.override_subsumed)",
            "r25-carried": "CONFIRM carried from the R25 re-gate fill (triple-identical row, outside the R26 surface)",
            "r21-carried": "CONFIRM carried from the R21 re-gate fill (triple-identical row, outside the R22 surface)",
            "r17-carried": "CONFIRM carried from the R17 re-gate fill (triple-identical row, not sampled at R21, outside the R18 surface)",
            "r13-carried": "CONFIRM carried from the R13 re-gate fill (triple-identical row, not sampled at R17/R21, outside the R14/R18 surfaces)",
            "r9-carried": "CONFIRM carried from the R9 re-gate fill (triple-identical row, not sampled at R13/R17/R21, outside the R10/R14/R18 surfaces)",
            "r4-carried": "CONFIRM carried from the R4 re-gate fill (triple-identical row, not sampled at R9/R13/R17/R21, outside the R10/R14/R18 surfaces)",
            "r29-fresh": "fresh R29 judgment (both tier wordings + chunk content)",
        }[v["source"]]
        note_line = f"\n- Reviewer note ({v['source']}): {v['note']}"
        a_blocks.append(f"""### {r['spec_code']} — {r['sp_title']}
- Note: {title_of.get(r['note_path'], '')} (`{r['note_path']}`)
- Chunk: ordinal {r['chunk']['ordinal']} — heading `{r['chunk']['heading']}` — sha256_16 `{r['chunk']['sha256_16']}` — {r['chunk']['chars']} chars
- Evidence quote (verbatim self-slice, markdown-safe): "{r['evidence_quote']}"
- Chunk excerpt: «{excerpt}»
- Upstream: T-C32 join {up['join_row']} — tier {up['join_tier']} — score {score_s} — wording {up.get('wording_check')} — validation tier {up['validation_tier']}
- Tier wordings consulted: signature **{bt['tier_signature']}** — store Higher-operative: "{bt['store_higher']}" · C30 ledger Foundation: "{bt['ledger_foundation']}"
- Rationale: {r['rationale']}
- Verdict source: {src_line}
- Verdict: {boxes}{note_line}

""")

    b_blocks = []
    for r in worklist:
        v = part_b[r["mapping_id"]]
        code_s = r.get("spec_code") or "(anchor unresolved)"
        title_s = r.get("sp_title") or ""
        chunk_s = (('ordinal ' + str(r['chunk']['ordinal']) + ' — heading `' + r['chunk']['heading'] + '`')
                   if "chunk" in r else "(corpus gap — no chunk exists)")
        b_blocks.append(f"""### {code_s} — {title_s}
- Note: `{r.get('note_path', '(no notes coverage)')}`
- Chunk: {chunk_s}
- Reason: {r['worklist_reason']}
- Disposition: {r['disposition']}
- Surface: {v['surface']}
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)
- Why DEFERred: {v['why']}

""")

    class_prec = (f"exact {rollup['exact']['precision'] * 100:.1f}% / "
                  f"partial {rollup['partial']['precision'] * 100:.1f}% / "
                  f"none {rollup['none']['precision'] * 100:.1f}%")
    if gate_pass:
        gate_note = (
            f"**Gate outcome (this fill):** Part A per-class precision — {class_prec} "
            f"— the ≥90% class gate **PASSES on every class**; Part B {len(part_b)}/"
            f"{len(part_b)} decided; mechanical layer "
            f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS. **The R29 re-gate "
            f"evidence is GREEN.** This is VERIFICATION, not movement: the promoted "
            f"surface stays `HUMAN_VALIDATED` exactly as the R5 apply landed it and "
            f"the R26 amendment re-keyed it (831 rows, re-applied AMENDED at R28) "
            f"and the 7 anchored SUGGESTED rows stay SUGGESTED — the re-gate "
            f"re-verifies, it never re-confers. The {total['hold']} HOLD row(s) are "
            f"the convention's H3 fail-closed rows (no positive evidence yet): "
            f"their per-row sign-off is STILL OWED per the R28 record "
            f"(1.7B / 6.3J / 3.3F / 2.2C), as is the ord-3 promoted-surface "
            f"extension decision.")
    else:
        gate_note = (
            f"**Gate outcome (this fill):** Part A per-class precision — {class_prec} "
            f"— the ≥90% class gate "
            f"{'FAILS' if not gate_classes_pass else 'holds'}; Part B "
            f"{len(part_b)}/{len(worklist)} decided; mechanical layer "
            f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS. **The gate "
            f"is {'NOT ' if not gate_pass else ''}green on this draw.** The "
            f"defect inventory is recorded below; nothing self-repairs.")

    filled = f"""# C42 R29 — maths-a Chunk→SP Substrate RE-GATE OPERATOR REVIEW SHEET (operator gate 2 re-run)

**Seed:** `{seed}` (sha256 of the emitted rows — deterministic regeneration) ·
**Rows:** {len(sample)} anchored spot-checks + {len(worklist)} worklist decisions,
re-stratified over the R28-rebuilt substrate UNDER THE AMENDED PROMOTED SURFACE
(918 rows = 831 HUMAN_VALIDATED re-applied AMENDED from the R5 promotions file
[sha16 9bad739bd79e5899, byte-unchanged since R5] via the R26 amendment —
3 supersedes re-keyed old->new at 1.1A/5.1C/3.3H + 1 exclusion + 7 anchored
SUGGESTED [3 R22-re-attributed rows + 4 convention H3 holds] + 24
unresolved-span incl. ALL FOUR DEMOTEs [R10 related-calculations ord 2 + R14
unit-conversions ord 2 + R18 basic-angle-properties ord 1 + R26
factorising-by-grouping ord 2 — the FIRST of a promoted row] + 56 uncovered-SP;
coverage 132/188 codes — the R26 re-attributions landed COMPUTED at R28: 1.1A +
5.1C gained, none lost, the two uncovered-SP DEFER rows resolving into anchored
rows).
**Rule:** this sheet is the re-gate evidence for the promoted surface — the
ONLY path from SUGGESTED to HUMAN_VALIDATED for the chunk→SP substrate was and
remains the §18 apply (R5, operator gate 3, fired 2026-10-04 as 2e90f52). Per-
class rollup: any confirmed-precision < 90% on the sampled rows → rework that
class. **Both-tier wording standing instruction applied:** every row adjudicated
against the store's Higher-operative wording AND the C30 ledger Foundation
wording (signature per row; DIVERGENT fails the fill closed).
**Sampling:** identical convention to the C40 fill, re-seeded on the R24 rows —
low-assurance strata at 100%, score == 1.0 at ceil(20%) — + every worklist row.
**Anti-forgery (re-shaped for the promoted surface):** every row stays
RULE_DERIVED; the 832 HUMAN_VALIDATED rows are verified ROW-FOR-ROW against the
R5 promotions file (c42_r5_promotions.yaml, sha16 9bad739bd79e5899,
byte-unchanged since R5); the 7 anchored SUGGESTED rows are pinned to the
expected set (3 R22 re-attributed + 4 H3 holds); the 81 worklist rows stay
SUGGESTED. The upstream join is AI_VALIDATED (operator-delegated chain); the
tier difference to chemistry's T-C10-backed substrate is intentional and
recorded.
**Heading-only class:** c42-heading-only-convention-1 (the R10 convention
decision) is IN FORCE — heading-only rows resolve via the H1/H2/H3 ladder with
per-row provenance, with the R21 record NEW in the ladder's H2 source base (the
carry-forward continuity rule); H3 rows stay HOLD (fail-closed) and are NOT
promoted without the operator's explicit per-row sign-off.
**Supersedes:** the R25-era re-gate sheet + fill verdict record (464+81 rows)
over the pre-R26 surface — kept on their own records, never edited.

**Filled:** {REVIEW_DATE} — Reviewer: {REVIEWER}.
**Fill method:** mechanical layer scripted re-verification
({len(sample_ids) - mech_fail}/{len(sample_ids)} PASS) + both-tier wording
resolution ({len(sample_ids)}/{len(sample_ids)}, DIVERGENT 0); semantic layer
verdict sources: {dict(src_count)}.

## Part A — anchored-row spot-check ({len(sample)} rows)

{"".join(a_blocks)}## Part B — worklist decisions ({len(worklist)} rows, re-decided on the rebuilt set)

{"".join(b_blocks)}## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A total (anchored spot-check) | {total['rows']} | {total['confirm']} | {total['reject']} | {total['hold']} | {total['confirm']}/{total['rows']} = {total['precision'] * 100:.1f}% |
| A stratum: join score == 1.0 (exact) | {rollup['exact']['rows']} | {rollup['exact']['confirm']} | {rollup['exact']['reject']} | {rollup['exact']['hold']} | {rollup['exact']['confirm']}/{rollup['exact']['rows']} = {rollup['exact']['precision'] * 100:.1f}% |
| A stratum: join score < 1.0 (partial) | {rollup['partial']['rows']} | {rollup['partial']['confirm']} | {rollup['partial']['reject']} | {rollup['partial']['hold']} | {rollup['partial']['confirm']}/{rollup['partial']['rows']} = {rollup['partial']['precision'] * 100:.1f}% |
| A stratum: join score n/a (none) | {rollup['none']['rows']} | {rollup['none']['confirm']} | {rollup['none']['reject']} | {rollup['none']['hold']} | {rollup['none']['confirm']}/{rollup['none']['rows']} = {rollup['none']['precision'] * 100:.1f}% |
| B (worklist, re-decided) | {len(part_b)} | {sum(1 for v in part_b.values() if v['verdict'] == 'DEFER')} DEFER | | | {len(part_b)}/{len(part_b)} decided |
| Verdict sources | | {src_count.get('r22-section-override', 0)} R22 overrides + {src_count.get('r22-standing', 0)} R22 standing + {src_count.get('r18-section-override', 0)} R18 overrides + {src_count.get('r14-id-verdict', 0)} R14 id-verdicts + {src_count.get('r14-section-override', 0)} R14 overrides + {src_count.get('r10-id-verdict', 0)} R10 id-verdicts + {src_count.get('r10-standing', 0)} R10 standing + {src_count.get('r6-id-verdict', 0)} R6 id-verdicts + {src_count.get('r1-id-verdict', 0)} R1 id-verdicts + {src_count.get('r10-section-override', 0)} R10 overrides + {src_count.get('r6-section-override', 0)} R6 overrides + {src_count.get('r1-section-override', 0)} R1 overrides + {src_count.get('heading-only-convention', 0)} convention + {src_count.get('r1-subsumed', 0)} subsumed + {src_count.get('r21-carried', 0)} R21 carry + {src_count.get('r17-carried', 0)} R17 carry + {src_count.get('r13-carried', 0)} R13 carry + {src_count.get('r9-carried', 0)} R9 carry + {src_count.get('r4-carried', 0)} R4 carry + {src_count.get('r25-fresh', 0)} fresh | | | |

{gate_note}
"""
    SHEET.write_text(filled + "\n", encoding="utf-8")

    # ---- fill record --------------------------------------------------------------
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    # T-C42 R29 (the R17 audit amendment carried forward): the baseline is PINNED
    # to the round-start commit — the R28 post-audit state whose substrate is
    # the re-gate's semantic evidence base — instead of the dynamic HEAD (the
    # dynamic value drifted on every post-commit audit re-run: each audit commit
    # moved HEAD, so the recorded baseline chased the audit trail). The pinned
    # value records the substrate this gate ran over; audit re-runs may sit on
    # later commits without changing the baseline.
    baseline = "b0bf38dc0d2f627bbb34fee263668b12e2fa16a1"  # the R28 post-audit round-start commit (substrate == 5801a78, sha16 1b667c0107dfc85c)
    rec = {
        "schema": "c42-r29-regate-fill-record/1.0",
        "task": "T-C42",
        "stage": "r29-regate-fill",
        "generated_utc": now,
        "baseline": baseline,
        "reviewer": REVIEWER,
        "sheet": str(SHEET.relative_to(REPO)),
        "verdicts_record": str(VERDICTS.relative_to(REPO)),
        "sampling": {"seed": seed,
                     "strata": {cls: len(by[cls]) for cls in sorted(by)},
                     "sampled": {cls: sum(1 for c, _ in sample if c == cls)
                                 for cls in sorted(by)}},
        "part_a": {"total": total, "by_stratum": rollup,
                   "verdict_sources": dict(src_count)},
        "substrate_shape": {"rows": 918, "human_validated": 831,
                            "anchored": 838,
                            "anchored_suggested": 7,
                            "unresolved_span": 24,
                            "demoted": 4, "uncovered_sp": 56,
                            "covered_codes": 132},
        "part_b": {"rows": len(part_b), "defer": len(part_b),
                   "surfaces": dict(Counter(v["surface"] for v in part_b.values()))},
        "both_tier_wording": {
            "standing_instruction": "the re-fill consults BOTH tier wordings (store "
                                    "Higher-operative + C30 ledger foundation.text) "
                                    "per the R1 key finding",
            "signatures": dict(Counter(v["both_tier"]["tier_signature"]
                                       for v in verdicts.values())),
        },
        "gate": {"rule": "Part A precision >= 90% per class AND every Part B row "
                         "decided AND mechanical layer clean",
                 "outcome": "PASS" if gate_pass else "FAIL"},
        "promoted_surface": {
            "note": "the FIRST re-gate under the AMENDED promoted surface — the "
                    "831 HUMAN_VALIDATED rows are VERIFIED (identities == the R5 "
                    "promotions file sha16 9bad739bd79e5899 AMENDED by the R26 "
                    "amendment: 3 supersedes re-keyed old->new at 1.1A/5.1C/3.3H "
                    "+ 1 exclusion, matched row-for-row by chunk identity), "
                    "never re-conferred; the re-gate moves nothing",
            "promotions_file_sha16": sha16(PROMOTIONS.read_bytes()),
            "amendment_sha16": amend["base_file_sha256_16"],
            "hv_rows_verified": len(hv_rows),
            "anchored_suggested": 7,
        },
        "disposition": ("R29 gate-2 evidence GREEN; zero movement of the promoted "
                        "surface — the 831 HV rows stay HUMAN_VALIDATED exactly as "
                        "the R5 apply landed them and the R26 amendment re-keyed "
                        "them (re-applied AMENDED at R28) and the 7 anchored "
                        "SUGGESTED rows stay SUGGESTED; the 4 H3 rows' per-row "
                        "sign-off (1.7B / 6.3J / 3.3F / 2.2C), the ord-3 "
                        "promoted-surface extension candidate and the "
                        "promoted-surface same-class candidates remain open "
                        "operator decisions"
                        if gate_pass else
                        "gate NOT green on this draw; the defect inventory is recorded"),
        "mechanical_layer": f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS",
    }
    FILL_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")

    hold_rows = [(v["spec_code"], v["note_path"], v["chunk_ordinal"], v["heading"])
                 for v in verdicts.values() if v["verdict"] == "HOLD"]
    rej_rows = [(v["spec_code"], v["note_path"], v["chunk_ordinal"], v["heading"])
                for v in verdicts.values() if v["verdict"] == "REJECT"]
    holds_s = "\n".join(f"- `{c}` — {np} ord {o} `{h}` (c42-heading-only-convention-1 "
                        f"H3 fail-closed; see the sheet row)" for c, np, o, h in hold_rows) or "- none"
    rej_s = "\n".join(f"- `{c}` — {np} ord {o} `{h}`" for c, np, o, h in rej_rows) or "- none"
    md = f"""# C42 R29 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Generated:** {now}  |  **Baseline:** `{baseline}`
**Reviewer:** {REVIEWER}

## Method

- **Mechanical layer:** every sampled row re-verified by script — quote-in-chunk
  containment under the shared `norm()`, chunk `sha256_16`/heading/chars agreement
  with a fresh re-chunking, the amended-surface anti-forgery sweep (831 HV rows
  == the R5 promotions file AMENDED by the R26 amendment, row-for-row by chunk
  identity; 7 anchored SUGGESTED; all RULE_DERIVED) —
  **{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS**.
- **Both-tier wording (the R1 standing instruction, applied):** every sampled
  row's upstream official wording resolved against the store's Higher-operative
  wording AND the C30 ledger `foundation.text`; signatures:
  {dict(Counter(v['both_tier']['tier_signature'] for v in verdicts.values()))};
  DIVERGENT fails the fill closed (0 observed, matching the R2 join census).
- **Semantic layer:** per-row topical fidelity, verdict sources
  {dict(src_count)} — the R26 section-override rulings (the seventh R1-shaped
  round and the FIRST over the promoted surface: 3 verdicted REATTRIBUTEs
  1.1G -> 1.1A / 5.1D -> 5.1C / 3.3F -> 3.3H, the promoted identities re-keyed
  by the R26 amendment) + the FOUR R26 STANDING note-level joins + the R22
  section-override rulings (the sixth R1-shaped round: 3 verdicted
  REATTRIBUTEs 4.8D -> 4.8F / 2.2F -> 2.2B / 2.6B -> 3.3E) + the THREE R22
  STANDING note-level joins (list-shaped, the R23 precedent) + the R18
  section-override rulings + the R14 operator id-verdict (3.3I -> 3.2D) +
  the R14/R10/R6/R1 section-override rulings, the R10 operator id-verdicts +
  the R10 note-level STANDING adjudication (still standing), R6 + R1 operator
  id-verdicts (still standing), the 2 R1-subsumed entries riding the join,
  c42-heading-only-convention-1 (the H1/H2/H3 ladder with the R25 record NEW
  in its source base) for the heading-only class, CONFIRM carry-forward for
  triple-identical R25/R21/R17/R13/R9/R4 rows outside the R26 surface, and
  fresh judgment for the remainder.

## Result (re-stratified over the R28-rebuilt substrate, under the AMENDED promoted surface)

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A total | {total['rows']} | {total['confirm']} | {total['reject']} | {total['hold']} | {total['precision'] * 100:.1f}% |
| A stratum exact (score == 1.0) | {rollup['exact']['rows']} | {rollup['exact']['confirm']} | {rollup['exact']['reject']} | {rollup['exact']['hold']} | {rollup['exact']['precision'] * 100:.1f}% |
| A stratum partial (score < 1.0) | {rollup['partial']['rows']} | {rollup['partial']['confirm']} | {rollup['partial']['reject']} | {rollup['partial']['hold']} | {rollup['partial']['precision'] * 100:.1f}% |
| A stratum none (score n/a) | {rollup['none']['rows']} | {rollup['none']['confirm']} | {rollup['none']['reject']} | {rollup['none']['hold']} | {rollup['none']['precision'] * 100:.1f}% |
| B (worklist re-decided) | {len(part_b)} | {len(part_b)} DEFER | | | {len(part_b)}/{len(part_b)} decided |

**Gate outcome: {'PASS — the ≥90% per-class gate holds on every class and Part B is fully decided.' if gate_pass else 'FAIL.'}**

## Part B re-decisions (the rebuilt worklist)

- {sum(1 for v in part_b.values() if 'residual' in v['surface'])} DEFER on the C32
  §3 residual anchor (R1 KEPT UNRESOLVED, PDF-verified reason stands).
- {sum(1 for v in part_b.values() if 'R1 surface-1' in v['surface'])} DEFER on the
  R1 surface-1 cleared spans (wrong codes cleared, never forced).
- {sum(1 for v in part_b.values() if 'R6 surface-1' in v['surface'])} DEFER on the
  R6 surface-1 cleared spans (Problem Solving with Volumes, Geometrical Proof —
  wrong codes cleared, never forced).
- {sum(1 for v in part_b.values() if 'R10 surface-2' in v['surface'])} DEFER on the R10
  surface-2 DEMOTE (related-calculations ord 2 — inverse-operations content, no
  canonical 188 row teaches it; the note-level join adjudicated STANDING, so a
  REATTRIBUTE has no target; recorded, never forced).
- {sum(1 for v in part_b.values() if 'R14 surface-3' in v['surface'])} DEFER on the R14
  surface-3 DEMOTE (unit-conversions ord 2 — metric mass conversion, 4.10F's
  demand is volume conversion, no canonical 188 row teaches it; the note-level
  join STANDS on the note's ords 0/3 volume/capacity content, so a REATTRIBUTE
  has no target; recorded, never forced — the loop's second DEMOTE).
- {sum(1 for v in part_b.values() if 'R18 surface-3' in v['surface'])} DEFER on the R18
  surface-3 DEMOTE (basic-angle-properties ord 1 — the labeling primer, 4.1B's
  demand is angle properties of intersecting/parallel lines, none taught, no
  canonical 188 row teaches geometric labeling per se; the note-level join
  STANDS on the note's property sections ords 0/2/3, so a REATTRIBUTE has no
  target; recorded, never forced — the loop's third DEMOTE).
- {sum(1 for v in part_b.values() if 'R26 surface-3' in v['surface'])} DEFER on the R26
  surface-3 DEMOTE (factorising-by-grouping ord 2 — four-term two-variable
  grouping xy + 3x + 5y + 15, 2.2F's demand is capped '(limited to x^2 + bx +
  c)' and even 2.2B's un-limited 'quadratic expression' does not reach it, no
  canonical 188 row teaches it; the note-level join STANDS on the note's
  remaining 2.2F surface, so a REATTRIBUTE has no target; the promoted
  identity was excluded by the R26 amendment, the R5 file byte-untouched;
  recorded, never forced — the loop's FOURTH DEMOTE and the FIRST of a
  promoted row).
- {sum(1 for v in part_b.values() if 'gap' in v['surface'])} DEFER on
  uncovered-SP corpus gaps at the 132-code bound (movement across the loop:
  77 → 66 → 63 → 61 → 60 → 59 → 58 → 56 uncovered; 2 → 8 → 20 → 21 → 22 →
  23 → 24 unresolved-span incl. ALL FOUR DEMOTEs; coverage gained 1.6A + 1.6C
  at R12 via the R10 REATTRIBUTE rows, 4.1D at R16 via the R14 rows, 1.3D at
  R20 via the R18 verdicted + extension rows, 4.8F at R24 via the R22 rows,
  and 1.1A + 5.1C at R28 via the R26 rows — the two uncovered-SP DEFER rows
  resolved into anchored rows).

## Remaining defect inventory

REJECT rows:
{rej_s}

HOLD rows (the operator's own R1 RETAIN rulings, explicitly handled — not silent):
{holds_s}

## Disposition

Zero silent movement; zero silent repair. The promoted surface stays exactly as
the R5 apply landed it and the R26 amendment re-keyed it (831 HUMAN_VALIDATED
rows, re-applied AMENDED at R28) and the 7 anchored SUGGESTED rows stay
SUGGESTED — the re-gate VERIFIES, it never re-confers. The R29 sheet + this
record are the gate-2 evidence over the R28-rebuilt substrate. The HOLD rows
above are the convention's H3 fail-closed rows: their per-row sign-off
(1.7B / 6.3J / 3.3F / 2.2C) is STILL OWED per the R28 record, as are the
ord-3 promoted-surface extension candidate (3d-pythagoras SOHCAHTOA-3D) and
the promoted-surface same-class candidates (grouping ords 0/1/3, drawing
ord 5, vectors ord 4) + the rational/irrational corpus gap — each the
operator's call, recorded, not forced.
"""
    FILL_MD.write_text(md + "\n", encoding="utf-8")

    print(f"C42 R29 re-gate fill recorded: Part A {total['confirm']}/{total['rows']} = "
          f"{total['precision'] * 100:.1f}% (exact {rollup['exact']['precision'] * 100:.1f}% / "
          f"partial {rollup['partial']['precision'] * 100:.1f}% / "
          f"none {rollup['none']['precision'] * 100:.1f}%)")
    print(f"  verdict sources: {dict(src_count)}")
    print(f"  gate outcome: {'PASS' if gate_pass else 'FAIL'} — "
          f"{'the promoted surface verified, zero movement' if gate_pass else 'gate NOT green — defect inventory recorded'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
