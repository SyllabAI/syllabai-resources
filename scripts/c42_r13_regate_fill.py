#!/usr/bin/env python3
"""c42-r13 — the R13 RE-GATE fill (operator gate 2 RE-RUN of the C42 K2-B rework
loop's third iteration): render a FRESH re-stratified operator review sheet over
the R12-rebuilt chunk→SP substrate and re-fill it under the C12/C13 fill
convention, operator-delegate.

Differences from the R9 re-gate (this is the loop's third pass):
  * BOTH-TIER WORDING (the R1 standing instruction, unchanged): every sampled
    row's upstream official wording is resolved against the store's
    Higher-operative wording AND the C30 tier-dedupe ledger's foundation.text.
  * R10 VERDICT EVIDENCE: rows on the 2 R10 CORRECT anchors carry the R10
    verdict round's id-level evidence; the 3 related-calculations rows carry
    the R10 NOTE-LEVEL STANDING adjudication; rows carrying a
    provenance.override from the R10 map (7 verdicted REATTRIBUTEs) carry the
    R10 rulings; the DEMOTE row left the anchored surface at R12 and is decided
    in Part B.
  * R1/R6 EVIDENCE STILL STANDING: rows on the R1/R6 AFFIRM/CORRECT anchors and
    the non-subsumed R1/R6 section overrides carry those rulings exactly as at
    R9; the 2 R1-subsumed entries ride the join.
  * c42-HEADING-ONLY-CONVENTION-1 (NEW — the R10 round's convention decision,
    graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md): a heading-only chunk
    (norm(chunk text) == norm(heading), detected mechanically from a fresh
    re-chunking) is a STRUCTURAL slice of the corpus's own spec_point span; its
    row is resolved by the fail-closed evidence ladder — H1 (the anchor carries
    an operator id-verdict or the R10 note-level STANDING adjudication), H2
    (>=1 CONTENT-row CONFIRM of the same note+code at R4/R9 — a heading-only
    row's own prior CONFIRM never satisfies H2), H3 (otherwise HOLD,
    fail-closed, recorded). Every convention verdict carries per-row provenance
    naming the branch and the evidence reference(s). Nothing promotes.
  * R9 CARRY-FORWARD (NEW) + R4 CARRY-FORWARD (unchanged): a sampled row whose
    (note_path, spec_code, heading) triple is identical to an R9-CONFIRMed (or,
    not sampled at R9, an R4-CONFIRMed) verdict row, outside the changed
    surface, carries that CONFIRM forward (W3 chunk identity + W4 zero-drift
    make the prior judgment's evidence unchanged).
  * FRESH JUDGMENT: every remaining sampled row is judged directly against
    both tier wordings and the chunk content (recorded per-row in
    scripts/c42_r13_fresh_verdicts.yaml, with its evidence).
  * Part B re-decided on the rebuilt worklist (21 unresolved-span = 2 C32 §3
    residual + 6 R1-cleared spans + 12 R6-cleared spans + 1 R10 DEMOTE; 61
    uncovered-SP at the 127-code bound).

Verdict standard (the C40 standard, unchanged): CONFIRM / REJECT (root-caused) /
HOLD (evidence insufficient — under the convention, ONLY the H3 heading-only
rows and any row the ladder cannot resolve). Gate (the scope's rule, unchanged):
Part A per-class precision >= 90% AND every Part B row decided AND the
mechanical layer clean. ZERO promotion: the substrate stays SUGGESTED;
SUGGESTED -> HUMAN_VALIDATED happens only at R5 (operator gate 3, the §18
promotions-file convention).

Outputs:
  scripts/c42_r13_review_verdicts.yaml                  (the verdict record)
  graph/reports/C42_R13_MATHS_A_REGATE_REVIEW_SHEET.md  (fresh filled sheet)
  graph/reports/C42_R13_MATHS_A_REGATE_FILL_RECORD.json/.md
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
OVERRIDES = HERE / "c42_section_overrides.yaml"
OVERRIDES_R6 = HERE / "c42_section_overrides_r6.yaml"
OVERRIDES_R10 = HERE / "c42_section_overrides_r10.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R9_VERDICTS = HERE / "c42_r9_review_verdicts.yaml"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
VERDICTS = HERE / "c42_r13_review_verdicts.yaml"
SHEET = GP.reports_dir(QUAL) / "C42_R13_MATHS_A_REGATE_REVIEW_SHEET.md"
FILL_JSON = GP.reports_dir(QUAL) / "C42_R13_MATHS_A_REGATE_FILL_RECORD.json"
FILL_MD = GP.reports_dir(QUAL) / "C42_R13_MATHS_A_REGATE_FILL_RECORD.md"
FRESH_DOSSIER = Path("/home/z/my-project/scripts/c42_r13_fresh_dossier.json")

REVIEWER = ("Super Z (GLM agent), acting as operator-delegate under the operator's "
            "'an R1-shaped round over the R9 inventory (then R7/R8/R9 again), the "
            "heading-only-chunk convention decision' directive (2026-10-03, "
            "zai-web); the human operator retains final sign-off; per the "
            "anti-forgery rule nothing here flips the store (the §18 apply is "
            "R5, operator gate 3)")
REVIEW_DATE = "2026-10-03"
RC_ANCHOR = "spcpt_crKbmb6wVjM4yPJh"  # related-calculations — R10 STANDING

# ---------------------------------------------------------------------------
# FRESH VERDICTS — the rows the four recorded evidence sources do not cover,
# loaded from the committed judgment file (encoded from the fresh-row dossier:
# each row judged against BOTH tier wordings + the chunk's own content, heading
# first, full text pulled where the heading was not decisive). PROPOSAL-ONLY
# candidates bind nothing; a row that does not teach the SP's demand is
# REJECTed with its root cause, never rationalized.
_FRESH_FILE = HERE / "c42_r13_fresh_verdicts.yaml"


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
PART_B_DEFER_UNMAPPED = (
    "registered corpus gap at the post-R12 127-code coverage bound (125 at R9, "
    "122 at R3, 111 at C40 under the defective mapping) — no notes-corpus anchor "
    "resolves to this SP in the T-C32 join; closing it needs new SME content "
    "acquisition or an operator-authored anchor, not re-anchoring — deferring to "
    "the content-acquisition worklist (the chemistry 4.15 precedent)")


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
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    ovr6 = yaml.safe_load(OVERRIDES_R6.read_text(encoding="utf-8"))
    ovr10 = yaml.safe_load(OVERRIDES_R10.read_text(encoding="utf-8"))
    r4 = yaml.safe_load(R4_VERDICTS.read_text(encoding="utf-8"))
    r9 = yaml.safe_load(R9_VERDICTS.read_text(encoding="utf-8"))
    conv = json.loads(CONVENTION_JSON.read_text(encoding="utf-8"))
    return rows, ledger_map, sp_by_code, r1, r6, r10, ovr, ovr6, ovr10, r4, r9, conv


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
    (rows, ledger_map, sp_by_code, r1, r6, r10, ovr, ovr6, ovr10, r4, r9,
     conv) = load_inputs()
    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    worklist = [r for r in rows if "worklist_reason" in r]
    by_mid = {r["mapping_id"]: r for r in rows}

    # anti-forgery: nothing in the store may be past SUGGESTED / RULE_DERIVED
    bad = [r for r in rows if r.get("validation_status") != "SUGGESTED"
           or r["provenance"]["tier"] != "RULE_DERIVED"]
    if bad:
        print(f"ANTI-FORGERY: {len(bad)} rows not SUGGESTED/RULE_DERIVED", file=sys.stderr)
        return 1

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
    ovr1_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr["overrides"]}
    ovr6_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr6["overrides"]}
    ovr10_map = {(o["note_slug"], o["chunk_ordinal"]): o for o in ovr10["overrides"]}
    r4_map = r4["verdicts"]                                    # mapping_id -> verdict
    r9_map = r9["verdicts"]                                    # mapping_id -> verdict

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
    # [content-row CONFIRM refs at R4/R9] — a heading-only row's own prior
    # CONFIRM NEVER satisfies H2 (only content rows count)
    h2_index: dict[tuple, list[str]] = {}
    for src_name, src_map in (("R4", r4_map), ("R9", r9_map)):
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
        has_ovr = "override" in r.get("provenance", {})
        has_sub = "override_subsumed" in r.get("provenance", {})
        standing = aid == RC_ANCHOR
        ho = is_heading_only(r["note_path"], r["chunk"]["ordinal"])
        r4v = r4_map.get(mid)
        r9v = r9_map.get(mid)
        carried = ((not on_r1) and (not on_r6) and (not on_r10)
                   and not has_ovr and not has_sub and not standing and not ho
                   and ((r9v is not None and r9v["verdict"] == "CONFIRM"
                         and r9v["spec_code"] == r["spec_code"]
                         and r9v["note_path"] == r["note_path"]
                         and r9v["heading"] == r["chunk"]["heading"])
                        or (r9v is None and r4v is not None
                            and r4v["verdict"] == "CONFIRM"
                            and r4v["spec_code"] == r["spec_code"]
                            and r4v["note_path"] == r["note_path"]
                            and r4v["heading"] == r["chunk"]["heading"])))
        if r4v is None and r9v is None and not on_r1 and not on_r6 \
                and not on_r10 and not has_ovr and not has_sub \
                and not standing and not ho:
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
            if rnd.startswith("C42 R10"):
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
                            f"CONFIRM of {r['spec_code']} at R4/R9 — the row stays "
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
            r9v = r9_map.get(mid)
            r4v = r4_map.get(mid)
            r9_carried = (r9v is not None and r9v["verdict"] == "CONFIRM"
                          and r9v["spec_code"] == r["spec_code"]
                          and r9v["note_path"] == r["note_path"]
                          and r9v["heading"] == r["chunk"]["heading"])
            r4_carried = (r4v is not None and r4v["verdict"] == "CONFIRM"
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
                                "at R4/R9 — the row stays HOLD, explicit and "
                                "recorded; it un-holds automatically when H1/H2 "
                                "becomes true. Not auto-promoted at R5 without the "
                                "operator's explicit per-row sign-off.")
                        err += put(r, "HOLD", "heading-only-convention", note,
                                   root="heading-only H3 (fail-closed, no positive evidence)",
                                   convention_branch="H3 (fail-closed HOLD)")
            elif r9_carried:
                r9_note = r9v["note"] or ("topical fidelity confirmed on the "
                                          "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R9 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk-identity invariant "
                        f"holds, row outside the R10 surface): {r9_note[:400]}. "
                        f"Mechanical layer re-verified; both tier wordings "
                        f"consistent ({sig}).")
                err += put(r, "CONFIRM", "r9-carried", note)
            elif r4_carried:
                r4_note = r4v["note"] or ("topical fidelity confirmed on the "
                                          "chunk content vs the SP demand")
                note = (f"CONFIRM carried from the R4 re-gate fill (same chunk identity "
                        f"and same code attribution — W3 chunk-identity invariant "
                        f"holds; not sampled at R9, outside the R10 surface): "
                        f"{r4_note[:400]}. Mechanical layer re-verified; both tier "
                        f"wordings consistent ({sig}).")
                err += put(r, "CONFIRM", "r4-carried", note)
            elif mid in FRESH_VERDICTS:
                v, note = FRESH_VERDICTS[mid]
                err += put(r, v, "r13-fresh",
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
        else:
            why, surf = PART_B_DEFER_UNMAPPED, "uncovered-SP corpus gap (127-code bound)"
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
        "schema": "c42-r13-review-verdicts/1.0",
        "task": "T-C42",
        "stage": "r13-regate-fill",
        "contract": "graph/reports/C42_R13_MATHS_A_REGATE_REVIEW_SHEET.md "
                    "(the C12/C13 promotion-gate convention, re-stratified over the "
                    "R12-rebuilt substrate; c42-heading-only-convention-1 in force)",
        "supersedes": "scripts/c42_r9_review_verdicts.yaml (the R9-era re-gate fill; "
                      "kept on its own record, never edited)",
        "reviewer": REVIEWER,
        "review_date": REVIEW_DATE,
        "method": {
            "mechanical": f"quote-in-chunk + chunk-hash/heading agreement vs a fresh "
                          f"re-chunking + all-SUGGESTED/RULE_DERIVED re-verification, "
                          f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS",
            "both_tier_wording": "EVERY sampled row's upstream official wording "
                                 "resolved against the store's Higher-operative "
                                 "wording AND the C30 ledger foundation.text "
                                 "(tier_signature per row; DIVERGENT fails the fill "
                                 "closed) — the R1 standing instruction, applied",
            "semantic": "per-row topical fidelity against BOTH tier wordings and the "
                        "chunk content; verdict sources: the R10 operator id-verdicts "
                        "+ the R10 note-level STANDING adjudication (the third "
                        "R1-shaped round), the R6 + R1 operator id-verdicts (still "
                        "standing), the R10 + R6 + R1 section-override rulings, the "
                        "2 R1-subsumed entries riding the join, c42-heading-only-"
                        "convention-1 (the H1/H2/H3 ladder) for the heading-only "
                        "class, CONFIRM carry-forward for triple-identical R9/R4 "
                        "rows outside the R10 surface, and fresh judgment for the "
                        "remainder",
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
            "r10-id-verdict": "R10 operator id-verdict (CORRECT) evidence — the third R1-shaped round",
            "r10-standing": "R10 note-level STANDING adjudication (related-calculations joins 1.8D)",
            "r10-section-override": "R10 operator section-override ruling (verdicted REATTRIBUTE)",
            "r6-id-verdict": "R6 operator id-verdict (CORRECT) evidence — the second R1-shaped round, still standing",
            "r1-id-verdict": "R1 operator id-verdict (AFFIRM/CORRECT) evidence — still standing",
            "r6-section-override": "R6 operator section-override ruling (verdicted or labeled extension)",
            "r1-section-override": "R1 operator section-override ruling",
            "heading-only-convention": "c42-heading-only-convention-1 (the R10 convention decision; H1/H2/H3 ladder with per-row provenance)",
            "r1-subsumed": "R1 override riding the R6 note-level repair (provenance.override_subsumed)",
            "r9-carried": "CONFIRM carried from the R9 re-gate fill (triple-identical row, outside the R10 surface)",
            "r4-carried": "CONFIRM carried from the R4 re-gate fill (triple-identical row, not sampled at R9, outside the R10 surface)",
            "r13-fresh": "fresh R13 judgment (both tier wordings + chunk content)",
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
            f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS. **The R13 re-gate "
            f"evidence is GREEN.** This is EVIDENCE, not promotion: the store stays "
            f"`SUGGESTED` and the §18 apply (SUGGESTED → HUMAN_VALIDATED, exact row "
            f"identities, structural diff zero on the non-validation delta) is R5 — "
            f"operator gate 3, the operator's choice to fire. The "
            f"{total['hold']} HOLD row(s) are the convention's H3 fail-closed rows "
            f"(no positive evidence yet) and are recorded for R5's attention: they "
            f"promote only with the operator's explicit per-row sign-off.")
    else:
        gate_note = (
            f"**Gate outcome (this fill):** Part A per-class precision — {class_prec} "
            f"— the ≥90% class gate "
            f"{'FAILS' if not gate_classes_pass else 'holds'}; Part B "
            f"{len(part_b)}/{len(worklist)} decided; mechanical layer "
            f"{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS. **The promotion "
            f"is {'NOT ' if not gate_pass else ''}authorized by this fill.** The "
            f"defect inventory is recorded below; nothing self-repairs.")

    filled = f"""# C42 R13 — maths-a Chunk→SP Substrate RE-GATE OPERATOR REVIEW SHEET (operator gate 2 re-run)

**Seed:** `{seed}` (sha256 of the emitted rows — deterministic regeneration) ·
**Rows:** {len(sample)} anchored spot-checks + {len(worklist)} worklist decisions,
re-stratified over the R12-rebuilt substrate (923 rows = 841 anchored + 21
unresolved-span incl. the loop's first DEMOTE + 61 uncovered-SP; coverage
127/188 codes).
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the
chunk→SP substrate. Per-class rollup: any confirmed-precision < 90% on the sampled
rows → rework that class before promotion. **Both-tier wording standing
instruction applied:** every row adjudicated against the store's Higher-operative
wording AND the C30 ledger Foundation wording (signature per row; DIVERGENT fails
the fill closed).
**Sampling:** identical convention to the C40 fill, re-seeded on the rebuilt
rows — low-assurance strata at 100%, score == 1.0 at ceil(20%) — + every worklist
row.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows; nothing here
flips the store (all 923 rows re-verified SUGGESTED / RULE_DERIVED). The §18 apply
is R5, operator gate 3. The upstream join is AI_VALIDATED (operator-delegated
chain); the tier difference to chemistry's T-C10-backed substrate is intentional
and recorded.
**Heading-only class:** c42-heading-only-convention-1 (the R10 convention
decision) is IN FORCE — heading-only rows resolve via the H1/H2/H3 ladder with
per-row provenance; H3 rows stay HOLD (fail-closed) and are NOT auto-promoted.
**Supersedes:** the R9-era re-gate sheet + fill verdict record (465+83 rows) over
the pre-R10 surface — kept on their own records, never edited.

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
| Verdict sources | | {src_count.get('r10-id-verdict', 0)} R10 id-verdicts + {src_count.get('r10-standing', 0)} R10 standing + {src_count.get('r6-id-verdict', 0)} R6 id-verdicts + {src_count.get('r1-id-verdict', 0)} R1 id-verdicts + {src_count.get('r10-section-override', 0)} R10 overrides + {src_count.get('r6-section-override', 0)} R6 overrides + {src_count.get('r1-section-override', 0)} R1 overrides + {src_count.get('heading-only-convention', 0)} convention + {src_count.get('r1-subsumed', 0)} subsumed + {src_count.get('r9-carried', 0)} R9 carry + {src_count.get('r4-carried', 0)} R4 carry + {src_count.get('r13-fresh', 0)} fresh | | | |

{gate_note}
"""
    SHEET.write_text(filled + "\n", encoding="utf-8")

    # ---- fill record --------------------------------------------------------------
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    rec = {
        "schema": "c42-r13-regate-fill-record/1.0",
        "task": "T-C42",
        "stage": "r13-regate-fill",
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
        "substrate_shape": {"rows": 923, "anchored": 841, "unresolved_span": 21,
                            "demoted": 1, "uncovered_sp": 61, "covered_codes": 127},
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
        "disposition": ("R13 gate-2 evidence GREEN; zero promotion — the store stays "
                        "SUGGESTED and the §18 apply is R5 (operator gate 3), the "
                        "operator's choice to fire; the convention's H3 rows promote "
                        "only with explicit per-row operator sign-off"
                        if gate_pass else
                        "promotion NOT authorized; the defect inventory is recorded"),
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
    md = f"""# C42 R13 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Generated:** {now}  |  **Baseline:** `{baseline}`
**Reviewer:** {REVIEWER}

## Method

- **Mechanical layer:** every sampled row re-verified by script — quote-in-chunk
  containment under the shared `norm()`, chunk `sha256_16`/heading/chars agreement
  with a fresh re-chunking, all rows SUGGESTED / RULE_DERIVED —
  **{len(sample_ids) - mech_fail}/{len(sample_ids)} PASS**.
- **Both-tier wording (the R1 standing instruction, applied):** every sampled
  row's upstream official wording resolved against the store's Higher-operative
  wording AND the C30 ledger `foundation.text`; signatures:
  {dict(Counter(v['both_tier']['tier_signature'] for v in verdicts.values()))};
  DIVERGENT fails the fill closed (0 observed, matching the R2 join census).
- **Semantic layer:** per-row topical fidelity, verdict sources
  {dict(src_count)} — R10 operator id-verdicts + the R10 note-level STANDING
  adjudication (the third R1-shaped round), R6 + R1 operator id-verdicts (still
  standing), R10 + R6 + R1 section-override rulings, c42-heading-only-
  convention-1 (the H1/H2/H3 ladder) for the heading-only class, the 2
  R1-subsumed entries riding the join, CONFIRM carry-forward for
  triple-identical R9/R4 rows outside the R10 surface, and fresh judgment for
  the remainder.

## Result (re-stratified over the R12-rebuilt substrate)

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
- {sum(1 for v in part_b.values() if 'DEMOTE' in v['surface'])} DEFER on the R10
  surface-2 DEMOTE (related-calculations ord 2 — inverse-operations content, no
  canonical 188 row teaches it; the note-level join adjudicated STANDING, so a
  REATTRIBUTE has no target; recorded, never forced).
- {sum(1 for v in part_b.values() if 'gap' in v['surface'])} DEFER on
  uncovered-SP corpus gaps at the 127-code bound (movement across the loop:
  77 → 66 → 63 → 61 uncovered; 2 → 8 → 20 → 21 unresolved-span incl. the R10
  DEMOTE; coverage gained 1.6A + 1.6C at R12 via the R10 REATTRIBUTE rows).

## Remaining defect inventory

REJECT rows:
{rej_s}

HOLD rows (the operator's own R1 RETAIN rulings, explicitly handled — not silent):
{holds_s}

## Disposition

Zero silent promotion; zero silent repair. The substrate stays `SUGGESTED`
(all 923 rows re-verified). The R13 sheet + this record are the gate-2 evidence;
the §18 apply (SUGGESTED → HUMAN_VALIDATED, exact row identities, structural-diff
zero on the non-validation delta, two-way audit) is R5 — operator gate 3, the
operator's choice to fire. The HOLD rows above are the convention's H3
fail-closed rows: they ride R5 only with the operator's explicit per-row sign-off
(plus the convention decision itself), or stay SUGGESTED — recorded, not forced.
"""
    FILL_MD.write_text(md + "\n", encoding="utf-8")

    print(f"C42 R13 re-gate fill recorded: Part A {total['confirm']}/{total['rows']} = "
          f"{total['precision'] * 100:.1f}% (exact {rollup['exact']['precision'] * 100:.1f}% / "
          f"partial {rollup['partial']['precision'] * 100:.1f}% / "
          f"none {rollup['none']['precision'] * 100:.1f}%)")
    print(f"  verdict sources: {dict(src_count)}")
    print(f"  gate outcome: {'PASS' if gate_pass else 'FAIL'} — "
          f"{'R5 (operator gate 3) is armed; the store stays SUGGESTED here' if gate_pass else 'promotion NOT authorized'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
