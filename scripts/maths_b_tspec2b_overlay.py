#!/usr/bin/env python3
"""maths_b_tspec2b_overlay.py — T-SPECS-MATHSB-2B-OVERLAY-1 engine (r2 overlay).

Resolves the 13 unmapped generic lessons of the maths-b content-join lane
(queue of record: T-SPECS-MATHSB-REVIEW-1 run-001 receipt followup #2: "the
13 unmapped: T-SPEC-2b operator-verdict overlay lane is the sanctioned path
for plausible semantic homes ... NOT landed here") under the operator order
"apply the T-SPEC-2b precedent ... for the 13 unmapped generic lessons"
(trace 1a183901ab68b9fd).

THE T-SPEC-2b LANE (precedent of record, sda-chem / sda-bio / acct chains):
  - operator-verdict overlay, evidence-quoted, no-guess; PMT excluded as
    source per operator instruction 2026-09-18
  - SIDE-CAR LANE LAW (scripts/build_learner_spec_links.py verdict_overlay):
    the verdicts live in spec_point_resolution.json resolved[] rows whose
    method starts with "operator-verdict"; they fill ONLY ids the map itself
    left unmapped (map lane wins). spec_point_map.json is NOT modified.

VERDICT LAW (every basis quotes statements READ + note text + grouping):
  T_SPEC_2B_ATTACH  term-identity (note's own name/title prints the
                    statement's distinctive content term verbatim) or a
                    topic-plane semantic home corroborated by of-record
                    grouping consistency (the run-001 Speed-Time->4N
                    evidence class); tier C1_content_join for term
                    identities, C3_topic_anchored for semantic homes.
  T_SPEC_2B_STAY    no statement-plane home exists in the 98-statement
                    spine (pool READ in full, quoted in the basis);
                    attaching would be a guess (the sda-bio 2.54 class).

No-guess discipline: 13/13 accounted; nothing manufactured; the two stays
carry structured quoted reasons; the map lane remains byte-untouched
(asserted); idempotence via the sheet r2 pass marker (re-run = no-op
unless --force).

Usage: python3 scripts/maths_b_tspec2b_overlay.py [--dry-run] [--force]
"""
from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-b-16"
EQ = REPO / "SME-ExamQuestion" / COURSE
RN = REPO / "SME-RevisionNotes" / COURSE
PARSED = REPO / "Official-Specifications" / "parsed" / "igcse-maths-b"

METHOD2B = ("operator-verdict lane (T-SPEC-2b; PMT excluded as source per "
            "operator instruction 2026-09-18)")
OPERATOR_ORDER = ("apply the T-SPEC-2b precedent ... for the 13 unmapped "
                  "generic lessons (trace 1a183901ab68b9fd)")
TOOL = "scripts/maths_b_tspec2b_overlay.py"

# ---------------------------------------------------------------- verdicts
# of record: evidence-quoted operator verdicts (see module docstring law).
# quote fields carry the note's own text; stmt fields quote the official
# statement READ; grouping fields cite of-record rows (all verifiable in
# spec_point_map.json / the parsed bank).
VERDICTS = [
    {
        "sid": "spcpt_6Tdy5SV9gzyC8BSw", "name": "Repeated percentage change",
        "verdict": "T_SPEC_2B_ATTACH", "code": "1H", "tier": "C1_content_join",
        "class": "term_identity",
        "stmt_read": "1H 'Fractions, decimals, ratio, proportion and percentage'",
        "quote": ("note title/name prints 'percentage' verbatim; text: 'The multiplier "
                  "for a 5% decrease is 0.95 ... So multiply 8000 by 0.95^3' "
                  "(percentage multipliers applied repeatedly)"),
        "grouping": ("1H already of-record for the sibling percentage lessons "
                     "(Basic Percentages spcpt_FHRjdMc6tvRR553q, Reverse Percentages "
                     "spcpt_5CHMgxBWhBwxh5Y6)"),
        "rejected": ("r1 refined in-topic best is 1H itself (0.299, margin 0.101 — the "
                     "top scorer of the 13); below the r1 mechanical bar (score < 0.50), "
                     "which is exactly the bar the operator-verdict lane exists to "
                     "adjudicate past"),
    },
    {
        "sid": "spcpt_84hZy4pDd8nBGN3r", "name": "Midpoint of a Line",
        "verdict": "T_SPEC_2B_ATTACH", "code": "4H", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "4H 'Rectangular Cartesian co-ordinates'",
        "quote": ("text: 'The coordinates of A are (-4, 3) and the coordinates of B are "
                  "(8, -12). Find the coordinates of the midpoint of AB' — worked with "
                  "((x1+x2)/2, (y1+y2)/2)"),
        "grouping": ("4H already of-record for the sibling '2D Coordinates' "
                     "(spcpt_Jw35TTKhvXxmGGfP, same Coordinate Geometry subtopic); "
                     "run-001 receipt names 'Midpoint of a Line->4H' as a candidate of "
                     "note"),
        "rejected": ("4M 'Determination of gradients, rates of change, maxima and minima, "
                     "stationary points and turning points' — differentiation content "
                     "the note does not teach"),
    },
    {
        "sid": "spcpt_8GsFXwdQTJymxXw8", "name": "Expected Frequency",
        "verdict": "T_SPEC_2B_ATTACH", "code": "10K", "tier": "C1_content_join",
        "class": "term_identity",
        "stmt_read": "10K 'Understand and use the term 'expected frequency''",
        "quote": ("TERM IDENTITY — the statement exists precisely for this term; text: "
                  "'Expected frequency refers to the number of times you would expect a "
                  "particular outcome to occur — It is found by multiplying the "
                  "probability by the number of trials'"),
        "grouping": ("10K carries 0 of-record mappings — this lesson is the term's home "
                     "in the corpus"),
        "rejected": ("r1 tie 10C/10K (both 0.252, margin 0.000) broken by the eyes-on "
                     "read: 10C = 'Calculation of an estimate of the mean of a larger "
                     "number of quantities given in grouped frequencies' — grouped-mean "
                     "statistics, not probability-frequency"),
    },
    {
        "sid": "spcpt_bPTTmJSGkKv2PDc5", "name": "Relative Frequency",
        "verdict": "T_SPEC_2B_ATTACH", "code": "10E", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "10E 'Understand the language and basic concepts of probability'",
        "quote": ("text: 'What is relative frequency? Number of successful outcomes / "
                  "Total number of trials ... Use Johan's results to estimate the "
                  "probability' — relative frequency IS the experimental-probability "
                  "estimate, a basic concept of probability"),
        "grouping": ("10E already of-record for 'Basic Probability' "
                     "(spcpt_FVX7YRftjhnwYHQF)"),
        "rejected": ("10K belongs to the sibling spcpt of the same note (Expected "
                     "Frequency, term identity); 10C rejected = grouped mean"),
    },
    {
        "sid": "spcpt_qRytkYVHXTQBJdSq", "name": "Best Buys",
        "verdict": "T_SPEC_2B_ATTACH", "code": "1G", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "1G 'Weights, measures and money'",
        "quote": ("text: 'Two deals for buying caps are given below: 3 caps for GBP22.50 "
                  "... 5 caps for GBP36 ... At which shop are the caps better value?' — "
                  "value-for-money comparison, the spine's money plane"),
        "grouping": ("1G already of-record for the sibling money lesson 'Money "
                     "Calculations' (spcpt_bMYrxtVc2SZgt8mX); run-001 receipt names "
                     "'Best Buys->1G' as a candidate of note"),
        "rejected": ("1I/1J (r1 in-topic bests 0.150/0.149) READ as accuracy/bounds "
                     "statements — not the content plane of this lesson"),
    },
    {
        "sid": "spcpt_pFVDbZgQGCHHRDtc", "name": "Converting Units",
        "verdict": "T_SPEC_2B_ATTACH", "code": "1G", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "1G 'Weights, measures and money'",
        "quote": ("text: 'How do I convert units of lengths? ... 1 cm = 10 mm ... 485 g "
                  "to kg' — unit conversion of lengths/mass/volumes, the measures plane"),
        "grouping": ("1G already of-record for 'Compound Measures' "
                     "(spcpt_4ZdHtGPdDjYdR6rK) and 'Speed, Density & Pressure' "
                     "(spcpt_wRw6rKqPdVmS986W) — the measures family"),
        "rejected": ("1K (r1 in-topic best 0.125) READ 'Numbers in standard form' — a "
                     "different number-plane topic"),
    },
    {
        "sid": "spcpt_trxtpbq9c342p3qw", "name": "Squared & Cubic Units",
        "verdict": "T_SPEC_2B_ATTACH", "code": "1G", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "1G 'Weights, measures and money'",
        "quote": ("text: 'How do I convert between squared units (areas)? ... 1 cm^2 = "
                  "10^2 mm^2 = 100 mm^2' — area/volume unit conversions, the measures "
                  "plane"),
        "grouping": ("same 1G measures family (Compound Measures, Speed Density & "
                     "Pressure of record); sibling subtopic 'Standard & Compound Units' "
                     "rows land here"),
        "rejected": ("1K (r1 in-topic best 0.086) rejected as for Converting Units"),
    },
    {
        "sid": "spcpt_PzyS22R9jMg3y3sZ", "name": "Expanding One Bracket",
        "verdict": "T_SPEC_2B_ATTACH", "code": "3C", "tier": "C3_topic_anchored",
        "class": "family_grouping_consistent",
        "stmt_read": "3C 'The factorisation of simple algebraic expressions'",
        "quote": ("text: 'Multiply the 4x term outside the brackets by both terms inside "
                  "the brackets ... 8x^2 - 12x'"),
        "grouping": ("FAMILY GROUPING DECISIVE: the of-record rows for the same SME "
                     "'Expanding Brackets' subtopic — Expanding Two Brackets "
                     "(spcpt_S2dfVTzRhCh7pRzW), Expanding Three Brackets "
                     "(spcpt_GVgyB5BVfNDYGf8M), Expanding Squared Brackets "
                     "(spcpt_F8nMMNHkgCNBjb5G) — all sit on 3C (r0 C1 content joins); "
                     "single-bracket expansion joins its own family"),
        "rejected": ("3A 'The basic processes of algebra' holds only 'Algebraic "
                     "Notation' of record — not the expanding-brackets family plane"),
    },
    {
        "sid": "spcpt_W5bHgsHCyJ4jpkYz", "name": "Expand & Simplify",
        "verdict": "T_SPEC_2B_ATTACH", "code": "3C", "tier": "C3_topic_anchored",
        "class": "family_grouping_consistent",
        "stmt_read": "3C 'The factorisation of simple algebraic expressions'",
        "quote": ("same note as Expanding One Bracket (single-brackets lesson, second "
                  "section): expand then simplify the result"),
        "grouping": ("same family grouping as Expanding One Bracket (Two/Three/Squared "
                     "Brackets all of-record on 3C)"),
        "rejected": ("3A rejected for family consistency (as above)"),
    },
    {
        "sid": "spcpt_rsCdKqXKjhfmkyqT", "name": "Collecting Like Terms",
        "verdict": "T_SPEC_2B_ATTACH", "code": "3A", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "3A 'The basic processes of algebra'",
        "quote": ("text: 'Collect the a terms first 8a - 6a = 2a ... Then collect the b "
                  "terms ... 2a - b' — collecting like terms is the canonical basic "
                  "algebraic process"),
        "grouping": ("3A already of-record for 'Algebraic Notation' "
                     "(spcpt_gzQvnKpxPvTqzzBp) — the sibling Algebra Toolkit lesson"),
        "rejected": ("3C rejected — factorisation is a different technique the note "
                     "does not teach (the run-001 3D-rejection evidence class)"),
    },
    {
        "sid": "spcpt_rxmWrBrc2s2q45wF", "name": "Pie Charts",
        "verdict": "T_SPEC_2B_ATTACH", "code": "10A", "tier": "C3_topic_anchored",
        "class": "semantic_home_grouping_consistent",
        "stmt_read": "10A 'Graphical representation of numerical data'",
        "quote": ("text: 'What is a pie chart? How do I draw a pie chart?' with the "
                  "students -> fractions -> angles worked table (132, 48, ...) — a pie "
                  "chart is a graphical representation of numerical data"),
        "grouping": ("10A already of-record for the statistical-diagrams family: "
                     "'Reading & Interpreting Statistical Diagrams' "
                     "(spcpt_bGtx4SMcX6BRS6KP), 'Comparing Statistical Diagrams' "
                     "(spcpt_nXY9n4Vt3cVTmKcR), 'Discrete & Continuous Data' "
                     "(spcpt_QWXhzVp2S3VYZdZc)"),
        "rejected": ("10J (r1 in-topic best 0.198) READ 'Finding very simple conditional "
                     "probability' — not the content plane of this lesson"),
    },
    {
        "sid": "spcpt_8Wtthy9gt8B5xsVW", "name": "Mathematical Symbols",
        "verdict": "T_SPEC_2B_STAY", "code": None, "tier": None,
        "class": "no_statement_plane_home",
        "stmt_read": ("T1 pool READ in full (1A 'The ordinary processes of number "
                      "manipulation', 1B 'Prime numbers, factors, multiples', 1C-1K)"),
        "quote": ("note: 'Mathematical symbols What mathematical symbols do I need to "
                  "know?' — a symbols/notation glossary"),
        "grouping": ("no T1 statement is a notation/symbols statement; cov_w = 0.0 "
                     "against every T1 candidate"),
        "rejected": ("attaching any T1 statement would be a guess (the sda-bio 2.54 "
                     "no-guess class: re-anchoring without a statement-plane home is "
                     "forbidden)"),
    },
    {
        "sid": "spcpt_SQqKCGwRcv6gj5h3", "name": "Systematic Lists",
        "verdict": "T_SPEC_2B_STAY", "code": None, "tier": None,
        "class": "no_statement_plane_home",
        "stmt_read": ("T10 pool READ in full (10E-10K probability statements; no "
                      "listing/outcomes statement exists)"),
        "quote": ("note 'Listing Outcomes', section: 'Write out all the ways to arrange "
                  "the letters A, B and C ... The six arrangements are ABC, ACB, BAC, "
                  "BCA, CAB and CBA' — a systematic-listing method lesson"),
        "grouping": ("no T10 statement covers outcome listing; 10I already of-record "
                     "for the conditional-probability lessons (Combined Conditional "
                     "Probabilities, Combined Probability, Tree Diagrams)"),
        "rejected": ("10I rejected = 'Using simple conditional probability for combined "
                     "events' — a conditional technique the note does not teach; 10E "
                     "rejected = concept language, not a listing method"),
    },
]


def now() -> str:
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="re-apply even if the r2 pass marker is present")
    args = ap.parse_args()

    res_path = EQ / "spec_point_resolution.json"
    sheet_path = EQ / "review_adjudication.json"
    map_path = EQ / "spec_point_map.json"
    map_sha_before = hashlib.sha256(map_path.read_bytes()).hexdigest()

    res = json.loads(res_path.read_text(encoding="utf-8"))
    sheet = json.loads(sheet_path.read_text(encoding="utf-8"))
    idx = json.loads((EQ / "spec_point_index.json").read_text(encoding="utf-8"))["spec_points"]
    pool = {p["official_code"]: p for p in
            json.loads((PARSED / "spec_points.json").read_text(encoding="utf-8"))["spec_points"]}
    spm = json.loads(map_path.read_text(encoding="utf-8"))

    marker = (sheet.get("r2_overlay") or {}).get("pass", "")
    if marker.startswith("r2") and not args.force:
        print("already applied (r2 overlay of record) — no-op; use --force")
        return 0

    resolved_by_id = {r["id"]: r for r in res["resolved"]}
    mapped_ids = set(spm["mappings"])
    notes_loose_after = []

    # ---- battery prechecks
    sids = [v["sid"] for v in VERDICTS]
    assert len(sids) == 13 and len(set(sids)) == 13, "verdict table must cover 13 unique sids"
    unmapped_ids = {u["spcpt_id"] for u in spm["unmapped"]}
    assert unmapped_ids == set(sids), f"queue drift: {unmapped_ids ^ set(sids)}"
    for v in VERDICTS:
        assert v["sid"] not in mapped_ids, f"{v['sid']} already mapped — map lane wins"
        if v["verdict"] == "T_SPEC_2B_ATTACH":
            p = pool[v["code"]]
            assert p["id"] == f"IGCSE_MATHS_B:{v['code']}"
            gate = spm_probe_gate(RN, idx, v["sid"])
            code_gate = re.match(r"^(\d+)", v["code"]).group(1)
            assert code_gate == gate, f"{v['sid']} topic gate {gate} != code {v['code']}"
        assert all(k in v and v[k] for k in ("stmt_read", "quote", "grouping", "rejected")), \
            f"{v['sid']} basis incomplete (evidence-quoted law)"

    # ---- apply to the resolution sidecar (map lane untouched)
    counts = {"T_SPEC_2B_ATTACH": 0, "T_SPEC_2B_STAY": 0}
    for v in VERDICTS:
        row = resolved_by_id[v["sid"]]
        basis = (f"{v['verdict']} ({v['class']}): statement READ {v['stmt_read']}; "
                 f"evidence: {v['quote']}; grouping: {v['grouping']}; "
                 f"rejected: {v['rejected']}")
        if v["verdict"] == "T_SPEC_2B_ATTACH":
            row["resolved_code"] = v["code"]
            row["official_id"] = pool[v["code"]]["id"]
            row["tier"] = v["tier"]
            row["score"] = None
            row["method"] = METHOD2B
            row["reason"] = basis + f" — operator order: {OPERATOR_ORDER}"
        else:
            row["resolved_code"] = None
            row["official_id"] = None
            row["tier"] = None
            row["score"] = None
            row["method"] = None
            row["reason"] = basis + f" — operator order: {OPERATOR_ORDER}"
        counts[v["verdict"]] += 1

    res["generated_utc"] = now()
    res["validation"] = (res["validation"].rstrip()) + (
        "; r2 T-SPEC-2b operator-verdict overlay 2026-10-28 by "
        "scripts/maths_b_tspec2b_overlay.py — T-SPECS-MATHSB-2B-OVERLAY-1: the 13 "
        "unmapped adjudicated 11 attaches + 2 honest stays, evidence-quoted, PMT "
        "excluded as source, map lane byte-untouched (side-car lane law)")

    # ---- sheet: r2 block (r1 rows preserved byte-semantically)
    loose = loose_notes_after(RN, resolved_by_id, METHOD2B)
    sheet["r2_overlay"] = {
        "tool": TOOL,
        "pass": (f"r2 (2026-10-28; T-SPECS-MATHSB-2B-OVERLAY-1; operator order "
                 f"{OPERATOR_ORDER})"),
        "lane_law": ("T-SPEC-2b side-car overlay: verdicts recorded on the resolution "
                     "sidecar rows (method 'operator-verdict lane (T-SPEC-2b; PMT "
                     "excluded as source per operator instruction 2026-09-18)') and "
                     "filled into learner spec-links ONLY for ids the map itself left "
                     "unmapped (build_learner_spec_links.verdict_overlay); the "
                     "spec_point_map.json lane remains byte-untouched"),
        "verdict_law": ("T_SPEC_2B_ATTACH = term-identity or grouping-consistent "
                        "topic-plane semantic home with statements READ quoted; "
                        "T_SPEC_2B_STAY = no statement-plane home in the 98-statement "
                        "spine, attaching would be a guess; no-guess discipline "
                        "preserved, 13/13 accounted"),
        "operator_order": OPERATOR_ORDER,
        "verdicts": counts,
        "rows": [{"spcpt_id": v["sid"], "name": v["name"], "r1_verdict": "UNMAPPED_STAY",
                  "verdict": v["verdict"], "code": v["code"], "tier": v["tier"],
                  "class": v["class"], "stmt_read": v["stmt_read"], "quote": v["quote"],
                  "grouping": v["grouping"], "rejected": v["rejected"]} for v in VERDICTS],
        "hub_effect": {"notes_coded_after_overlay": f"{199 - len(loose)}/199",
                       "notes_still_loose": loose,
                       "flashcard_effect": "none expected (zero cards link the 13 spcpts)"},
    }
    sheet["summary"]["r2_overlay"] = counts
    sheet["summary"]["notes_coded_after_r2"] = f"{199 - len(loose)}/199"

    # ---- post battery
    map_sha_after = hashlib.sha256(map_path.read_bytes()).hexdigest()
    assert map_sha_before == map_sha_after, "MAP LANE MUST STAY BYTE-UNTOUCHED"
    att = [v for v in VERDICTS if v["verdict"] == "T_SPEC_2B_ATTACH"]
    assert all(resolved_by_id[v["sid"]]["resolved_code"] for v in att)
    assert all(resolved_by_id[v["sid"]]["method"].startswith("operator-verdict") for v in att)
    stays = [v for v in VERDICTS if v["verdict"] == "T_SPEC_2B_STAY"]
    assert all(resolved_by_id[v["sid"]]["resolved_code"] is None for v in stays)

    if args.dry_run:
        print("DRY RUN — no files written")
        print(json.dumps({"verdicts": counts, "notes_loose_after": loose}, indent=1))
        return 0

    res_path.write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    sheet_path.write_text(json.dumps(sheet, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"written: {res_path.name}, {sheet_path.name}")
    print(f"verdicts: {counts}  notes loose after: {loose}")
    return 0


def spm_probe_gate(rn_dir: Path, idx, sid: str) -> str:
    """The note's SME IA topic number (the engine's topic gate)."""
    SLUG2NUM = {'number': '1', 'sets': '2', 'algebra': '3', 'functions': '4',
                'matrices': '5', 'geometry': '6', 'mensuration': '7',
                'vectors-and-transformation-geometry': '8', 'trigonometry': '9',
                'statistics-and-probability': '10'}
    want = idx[sid].get("name")
    for path in sorted(rn_dir.glob("notes/**/*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        if sid in (d.get("spec_point_ids") or []):
            segs = (d.get("path") or {}).get("segs") or []
            return SLUG2NUM.get(segs[0] if segs else "", "?")
    raise AssertionError(f"no note found for {sid} ({want})")


def loose_notes_after(rn_dir: Path, resolved_by_id, method2b: str) -> list:
    """Notes still uncoded after the overlay (expected: exactly 2)."""
    loose = []
    for path in sorted(rn_dir.glob("notes/**/*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        spids = d.get("spec_point_ids") or []
        if not spids:
            continue
        coded = any(
            (resolved_by_id.get(s, {}).get("resolved_code")
             or (resolved_by_id.get(s, {}).get("method") or "").startswith("operator-verdict"))
            for s in spids)
        if not coded:
            loose.append(d.get("title") or d.get("page_title") or d.get("note_id"))
    return loose


if __name__ == "__main__":
    raise SystemExit(main())
