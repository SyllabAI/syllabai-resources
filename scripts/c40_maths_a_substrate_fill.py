#!/usr/bin/env python3
"""c40 — record the review verdicts for the maths-a chunk→SP substrate review
sheet (the FILL half of the C13 gate, replayed as operator-delegate per the
C12/C13 precedent) and re-render the sheet with the verdicts applied.

Method (two layers, the C13 fill convention):
  * Mechanical: every sampled row is re-verified by script — quote-in-chunk
    containment under the shared norm(), chunk sha256_16/heading/chars
    agreement with a fresh re-chunking, 1:1 mapping_id presence in the store,
    all rows SUGGESTED (anti-forgery).
  * Semantic: every sampled row is judged for topical fidelity against the
    SP's official wording and the chunk's content (heading + note context +
    full chunk text pulled where the heading was not decisive). The judgment
    unit for root-causing is the NOTE-JOIN: the T-SPEC resolution names the
    note → SP pair, the chunks inherit it.

Verdict standard (recorded, applied uniformly):
  CONFIRM — the chunk's content is genuinely about the SP's demand.
  REJECT  — the chunk's content belongs to a different SP. Root cause is
            either a NOTE-level join error (the upstream T-SPEC resolution
            maps the note to a semantically wrong SP — every chunk of that
            note rejects) or a SECTION-level scope difference (the note is
            rightly joined but the sampled section teaches a different SP's
            content).
  HOLD    — evidence insufficient to decide (none recorded in this fill).

Outputs:
  scripts/c40_maths_a_substrate_review_verdicts.yaml  (the verdict record)
  graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md  (filled)
  graph/reports/C40_MATHS_A_K2B_REVIEW_FILL_RECORD.json/.md
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402
from c40_maths_a_chunk_sp_substrate import span_chunks, load_corpus, R, norm  # noqa: E402

QUAL = "igcse-maths-a"
REPO = HERE.parent
VERDICTS = HERE / "c40_maths_a_substrate_review_verdicts.yaml"
SHEET = GP.reports_dir(QUAL) / "C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md"
FILL_JSON = GP.reports_dir(QUAL) / "C40_MATHS_A_K2B_REVIEW_FILL_RECORD.json"
FILL_MD = GP.reports_dir(QUAL) / "C40_MATHS_A_K2B_REVIEW_FILL_RECORD.md"

# ---------------------------------------------------------------------------
# NOTE-LEVEL REJECT ROOTS — the sampled (note_path, spec_code) pairs whose
# note→SP join is semantically wrong (upstream T-SPEC resolution errors the
# deterministic T-C32 id-join inherited). Every sampled chunk of such a pair
# rejects with the same root cause. Entries: note_path -> (code, root note).
NOTE_REJECTS = {
    "notes/1-numbers-and-the-number-system/number-toolkit/negative-numbers.json": (
        "4MA1-1.4A",
        "the note teaches negative-number contexts (temperature, money/debt); the "
        "SP 'understand the meaning of surds' is a different topic entirely — the "
        "surds surface is the simplifying-surds note (correctly joined and "
        "CONFIRMed separately); T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/circle-theorems/cyclic-quadrilaterals.json": (
        "4MA1-4.2B",
        "the note teaches the cyclic-quadrilateral circle theorem; its home is "
        "4.6B 'recognise the term cyclic quadrilateral' / 4.6C(iv), not the "
        "basic quadrilateral angle-sum SP 4.2B; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/circle-theorems/chords-and-tangents.json": (
        "4MA1-4.6B",
        "the note teaches chord/tangent properties (tangent definition); 4.6B is "
        "'recognise the term cyclic quadrilateral' — unrelated; T-SPEC "
        "resolution error"),
    "notes/5-vectors-and-transformation-geometry/vectors/representing-vectors-as-diagrams.json": (
        "4MA1-6.1C",
        "the note teaches vector diagrams (magnitude/direction drawing); 6.1C is "
        "'use cumulative frequency diagrams' — vectors are section 5, not "
        "statistics; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/tree-diagrams.json": (
        "4MA1-6.1C",
        "the note teaches tree diagrams for probability (home = 6.3A 'draw and "
        "use tree diagrams'); 6.1C is cumulative frequency; T-SPEC resolution "
        "error"),
    "notes/6-statistics-and-probability/statistics-toolkit/bar-charts-and-pictograms.json": (
        "4MA1-6.1A",
        "the note teaches bar charts and pictograms; 6.1A is 'construct and "
        "interpret histograms' (frequency density) — different diagrams; "
        "T-SPEC resolution error"),
    "notes/6-statistics-and-probability/statistics-toolkit/pie-charts.json": (
        "4MA1-6.1A",
        "the note teaches pie charts; 6.1A is histograms — different diagrams; "
        "T-SPEC resolution error"),
    "notes/6-statistics-and-probability/statistics-toolkit/comparing-statistical-diagrams.json": (
        "4MA1-6.1C",
        "the note teaches comparing statistical diagrams generally; 6.1C is "
        "cumulative-frequency use; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/statistics-toolkit/working-with-statistical-diagrams.json": (
        "4MA1-6.1C",
        "the note teaches reading/interpreting statistical diagrams generally; "
        "6.1C is cumulative-frequency use; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/statistics-toolkit/mean-median-and-mode.json": (
        "4MA1-6.2B",
        "the note teaches central tendency (mean/median/mode); 6.2B is 'the "
        "concept of a measure of spread'; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/statistics-toolkit/averages-from-grouped-data.json": (
        "4MA1-6.2C",
        "the note teaches averages from grouped data; 6.2C is 'find the "
        "interquartile range from a discrete data set'; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/combined-and-conditional-probability/conditional-probability.json": (
        "4MA1-6.3B",
        "the note teaches conditional probability P(A|B); 6.3B is 'the "
        "probability that two or more independent events will occur'; T-SPEC "
        "resolution error"),
    "notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-notation.json": (
        "4MA1-1.3A",
        "the note teaches algebraic notation (what is algebra); 1.3A is 'convert "
        "recurring decimals into fractions'; T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/algebra-toolkit/substitution.json": (
        "4MA1-2.2A",
        "the note teaches substitution; 2.2A is 'expand the product of two or "
        "more linear expressions'; T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/expanding-brackets/expanding-double-brackets.json": (
        "4MA1-2.2E",
        "the note teaches expanding double brackets; 2.2E is 'use algebra to "
        "support and construct proofs'; T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/graphs-of-functions/trig-graphs.json": (
        "4MA1-3.3F",
        "the note teaches trigonometric graphs (y = tan x shape); 3.3F is "
        "'calculate the gradient of a straight line given the coordinates of "
        "two points'; T-SPEC resolution error"),
    "notes/1-numbers-and-the-number-system/exchange-rates-and-best-buys/exchange-rates.json": (
        "4MA1-3.4C",
        "the note teaches currency conversion; 3.4C is differentiation "
        "(stationary points/turning points); T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/coordinate-geometry/coordinates.json": (
        "4MA1-3.3B",
        "the note teaches coordinates/Cartesian plane; 3.3B is the y=f(x) "
        "graph-transformations SP; T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/coordinate-geometry/midpoint-of-a-line.json": (
        "4MA1-3.3E",
        "the note teaches the midpoint formula; 3.3E is linear/non-linear graph "
        "intersections; T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/functions/inverse-functions.json": (
        "4MA1-3.3I",
        "the note teaches inverse-function notation; 3.3I is 'recognise, "
        "generate points and plot graphs of linear and quadratic functions'; "
        "T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/volume-and-surface-area/properties-of-3d-shapes.json": (
        "4MA1-4.10A",
        "the note names common 3D shapes; 4.10A is the sphere/cone surface-area "
        "and volume formulas; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/bearings-scale-drawing-and-constructions/scale.json": (
        "4MA1-4.11B",
        "the note's map-scale span teaches map reading/actual lengths; 4.11B is "
        "'volumes of similar figures in the ratio of the cube of corresponding "
        "sides'; T-SPEC resolution error (the same note's drawing-span join to "
        "4.5C is correct and CONFIRMed)"),
    "notes/3-sequences-functions-and-graphs/coordinate-geometry/gradient-of-a-line.json": (
        "4MA1-3.3G",
        "the note's sampled sections teach finding/using gradient — the 3.3F "
        "surface — and carry no parallel/perpendicular equation content; 3.3G "
        "is 'equation of a line parallel/perpendicular to a given line'; "
        "T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/coordinate-geometry/length-of-a-line.json": (
        "4MA1-3.3G",
        "the note teaches the distance/length formula between two points; 3.3G "
        "is parallel/perpendicular line equations; T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/real-life-graphs/conversion-graphs.json": (
        "4MA1-3.3F",
        "the note teaches reading/using conversion graphs; 3.3F is gradient "
        "from two coordinates; T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/real-life-graphs/distance-time-graphs.json": (
        "4MA1-3.3F",
        "the note teaches speed from distance-time graphs; 3.3F is gradient "
        "from two coordinates; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/volume-and-surface-area/volume.json": (
        "4MA1-4.10F",
        "the note teaches calculating volumes (prism/cylinder/cone/sphere); "
        "4.10F is 'convert between units of volume within the metric system'; "
        "T-SPEC resolution error"),
    "notes/6-statistics-and-probability/cumulative-frequency-diagrams/interpreting-cumulative-frequency-diagrams.json": (
        "4MA1-6.1B",
        "the note teaches USING/interpreting CF diagrams (percentiles, "
        "quartiles) — the 6.1C surface; 6.1B is 'construct cumulative frequency "
        "diagrams from tabulated data' (the drawing note is correctly joined "
        "and CONFIRMed); T-SPEC resolution error"),
    "notes/1-numbers-and-the-number-system/ratio-toolkit/simple-ratio.json": (
        "4MA1-1.7B",
        "the note teaches ratio basics (simplify/equivalent ratios); 1.7B is "
        "'divide a quantity in a given ratio'; T-SPEC resolution error"),
    "notes/1-numbers-and-the-number-system/rounding-estimation-and-bounds/bounds.json": (
        "4MA1-1.10B",
        "the note teaches bounds and accuracy; 1.10B is 'calculations using "
        "standard units of mass, length, area, volume and capacity'; T-SPEC "
        "resolution error"),
    "notes/1-numbers-and-the-number-system/using-a-calculator/using-a-calculator.json": (
        "4MA1-4.5C",
        "the note teaches calculator skills; 4.5C is 'solve problems using "
        "scale drawings'; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/pythagoras-theorem.json": (
        "4MA1-4.8A",
        "the note teaches Pythagoras' theorem (Who is Pythagoras); 4.8A is "
        "'sine, cosine and tangent of obtuse angles'; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/circle-theorems/segment-theorems.json": (
        "4MA1-4.6A",
        "the note teaches the same-segment angle theorem = 4.6C(iii); 4.6A is "
        "the intersecting-chord-properties SP (the intersecting-chord-theorem "
        "note is correctly joined and CONFIRMed); T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/algebra-toolkit/collecting-like-terms.json": (
        "4MA1-2.2B",
        "the note teaches collecting like terms; 2.2B is the quadratic-expression "
        "concept/factorisation SP; T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/algebra-toolkit/algebraic-vocabulary.json": (
        "4MA1-2.1A",
        "the note teaches algebra vocabulary (term/expression/coefficient); "
        "2.1A is 'use index notation involving fractional, negative and zero "
        "powers'; T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/rearranging-formulae/formulas-where-subject-appears-twice.json": (
        "4MA1-2.3F",
        "the note teaches changing the subject when it appears TWICE (factorise "
        "the subject); 2.3F is the subject-appears-ONCE case; T-SPEC resolution "
        "error"),
    "notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/parallel-lines.json": (
        "4MA1-4.1B",
        "the note teaches parallel-line EQUATIONS (y = mx + c family — the "
        "3.3G surface); 4.1B is angle properties of parallel lines (the "
        "angles-in-parallel-lines note is correctly joined and CONFIRMed); "
        "T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similarity.json": (
        "4MA1-4.11A",
        "the note teaches similarity basics and triangle-similarity proofs; "
        "4.11A is 'areas of similar figures in the ratio of the square of "
        "corresponding sides'; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/congruence-similarity-and-geometrical-proof/similar-lengths.json": (
        "4MA1-4.11A",
        "the note teaches LENGTH similarity (scale factors between lengths); "
        "4.11A is the AREA square-ratio SP; T-SPEC resolution error"),
    "notes/4-geometry-and-trigonometry/area-and-perimeter/problem-solving-with-areas.json": (
        "4MA1-4.11C",
        "the note teaches generic real-life area problem-solving (carpet/"
        "painting); 4.11C is 'use areas and volumes of SIMILAR figures in "
        "solving problems'; T-SPEC resolution error"),
    "notes/1-numbers-and-the-number-system/number-toolkit/mathematical-operations.json": (
        "4MA1-1.5C",
        "the note teaches arithmetic symbols (+ - × ÷ = ≠ roots ± π); verified "
        "zero set-notation content in the note body — 1.5C is 'use the notation "
        "n(A) for the number of elements in the set A'; T-SPEC resolution error"),
    "notes/6-statistics-and-probability/probability-diagrams---venn-and-tree-diagrams/probability-and-venn-diagrams.json": (
        "4MA1-1.5E",
        "the note teaches finding PROBABILITIES from Venn diagrams (the 6.x "
        "probability surface); 1.5E is 'use Venn diagrams to represent sets' "
        "(the set-notation-and-venn-diagrams note is correctly joined and "
        "CONFIRMed); T-SPEC resolution error"),
    "notes/2-equations-formulae-and-identities/solving-quadratic-equations/quadratic-equation-methods.json": (
        "4MA1-2.7D",
        "the note's sampled section teaches choosing completing-the-square "
        "(the 2.7B surface); 2.7D is simultaneous linear/quadratic equations "
        "(the linear/quadratic notes are correctly joined and CONFIRMed); "
        "T-SPEC resolution error"),
    "notes/3-sequences-functions-and-graphs/sequences/introduction-to-sequences.json": (
        "4MA1-3.1A",
        "the note teaches term-to-term sequence rules generally; 3.1A is "
        "'understand and use common difference (d) and first term (a) in an "
        "arithmetic sequence' (the arithmetic-sequences note is correctly "
        "joined and CONFIRMed); T-SPEC resolution error"),
    "notes/1-numbers-and-the-number-system/powers-roots-and-standard-form/powers-and-roots.json": (
        "4MA1-1.4A",
        "the note's sampled chunks carry no surds content (generic powers & "
        "roots / cube roots); 1.4A is 'understand the meaning of surds' — the "
        "surds surface is the simplifying-surds note (correctly joined and "
        "CONFIRMed); T-SPEC resolution error"),
}

# SECTION-LEVEL REJECTS — the note-join stands but the sampled section teaches
# a different SP's content. (note_path, code, heading) -> reason.
SECTION_REJECTS = {
    ("notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json", "4MA1-3.3F", "How do I draw a straight line from a table of values?"):
        "the section teaches plotting points from a table (the 3.3I plotting surface); the note-level join to 3.3F stands via its gradient content, but this chunk does not teach gradient from two coordinates",
    ("notes/3-sequences-functions-and-graphs/linear-graphs-y-equals-mx-plus-c/drawing-straight-line-graphs.json", "4MA1-3.3F", "How do I draw a straight line without using a table of values?"):
        "the section teaches drawing USING a known gradient/intercept, not calculating a gradient from two points (the 3.3F demand)",
    ("notes/1-numbers-and-the-number-system/fractions/basic-fractions.json", "4MA1-1.2I", "How do I simplify fractions?"):
        "the section teaches simplifying fractions; 1.2I is multiply and divide fractions and mixed numbers",
    ("notes/1-numbers-and-the-number-system/percentages/basic-percentages.json", "4MA1-1.6F", "How do I find a percentage of an amount with a calculator?"):
        "the section teaches finding a percentage of an amount; 1.6F is reverse percentages",
    ("notes/4-geometry-and-trigonometry/angles-in-polygons-and-parallel-lines/basic-angle-properties.json", "4MA1-4.1B", "What are the angle properties of quadrilaterals?"):
        "the section teaches the quadrilateral angle sum (the 4.2B surface); 4.1B is intersecting/parallel/straight-line angle properties",
    ("notes/4-geometry-and-trigonometry/right-angled-triangles---pythagoras-and-trigonometry/right-angled-trigonometry.json", "4MA1-4.8B", "How do I find the shortest distance from a point to a line?"):
        "the section teaches perpendicular/shortest distance via trig; 4.8B is angles of elevation and depression",
    ("notes/2-equations-formulae-and-identities/solving-inequalities/solving-linear-inequalities.json", "4MA1-2.8D", "How do I represent an inequality on a number line?"):
        "the section teaches NUMBER-LINE representation; 2.8D demands representation on rectangular CARTESIAN graphs",
    ("notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json", "4MA1-3.3I", "How do I find the coordinates of the turning point using differentiation?"):
        "the section teaches differentiation applied to quadratics (the 3.4C surface); 3.3I is generating points and plotting",
    ("notes/3-sequences-functions-and-graphs/graphs-of-functions/quadratic-graphs.json", "4MA1-3.3I", "How do I find the coordinates of the turning point by completing the square?"):
        "the section teaches the completing-the-square route to the turning point (the 2.7B surface); 3.3I is generating points and plotting",
    ("notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json", "4MA1-4.10D", "How do I find the surface area of a sphere?"):
        "sphere surface area is the 4.10A surface; 4.10D is the cylinder",
    ("notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json", "4MA1-4.10D", "How do I find the surface area of a cone?"):
        "cone surface area is the 4.10A surface; 4.10D is the cylinder",
    ("notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json", "4MA1-4.10D", "How do I find the surface area of cubes, cuboids, and prisms?"):
        "prism surface area is not the cylinder SP 4.10D",
    ("notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json", "4MA1-4.10D", "What is surface area?"):
        "generic surface-area intro, not the cylinder SP's content",
    ("notes/4-geometry-and-trigonometry/volume-and-surface-area/surface-area.json", "4MA1-4.10D", "Surface area"):
        "heading-only section head with no cylinder content",
    ("notes/6-statistics-and-probability/statistics-toolkit/averages-from-tables.json", "4MA1-6.2B", "How do I find the mode from a frequency table?"):
        "the mode is central tendency; 6.2B is the measure-of-spread concept (the range section of the same note IS spread content and is CONFIRMed)",
    ("notes/2-equations-formulae-and-identities/algebraic-roots-and-indices/algebraic-roots-and-indices.json", "4MA1-1.4C", "Algebraic roots & indices"):
        "heading-only section head with no content",
}

# Part B — every worklist row is decided: DEFER with a recorded reason.
PART_B_DEFER_UNRESOLVED = (
    "the span anchor is the T-C32 join's single unresolved anchor "
    "(operator adjudication pending, PROPOSAL-ONLY per C32 §3/G4); no chunk-level "
    "row can exist until the anchor is adjudicated — deferring is the honest "
    "disposition, never an invented code")
PART_B_DEFER_UNMAPPED = (
    "registered corpus gap — no notes-corpus anchor resolves to this SP in the "
    "T-C32 join (the 111-code notes coverage bound); closing it needs new SME "
    "content acquisition or an operator-authored anchor, not re-anchoring — "
    "deferring to the content-acquisition worklist (the chemistry 4.15 precedent)")

REVIEWER = ("Super Z (GLM agent), acting as operator-delegate under the operator's "
            "lane directive (fire K2-B, 2026-10-02, zai-web); the human operator "
            "retains final sign-off; per the anti-forgery rule nothing here flips "
            "the store")
REVIEW_DATE = "2026-10-02"


def main() -> int:
    store = GP.store("spec_chunk_mappings", QUAL)
    doc = yaml.safe_load(store.read_text(encoding="utf-8"))
    rows = doc["rows"]
    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    worklist = [r for r in rows if "worklist_reason" in r]
    by_mid = {r["mapping_id"]: r for r in rows}

    seed = hashlib.sha256(
        yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).encode()
    ).hexdigest()[:16]

    def stratum(r):
        s = r["provenance"]["upstream"].get("join_score")
        return "none" if s is None else ("exact" if float(s) >= 1.0 else "partial")

    def rank(mid):
        return hashlib.sha256(f"{seed}|{mid}".encode()).hexdigest()

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

    # ---- verdict assignment + coverage validation (fail closed) ---------------
    def verdict_for(r):
        key = (r["note_path"], r["spec_code"])
        nr = NOTE_REJECTS.get(r["note_path"])
        if nr and nr[0] == r["spec_code"]:
            return "REJECT", "note-level", nr[1]
        sr = SECTION_REJECTS.get((r["note_path"], r["spec_code"], r["chunk"]["heading"]))
        if sr:
            return "REJECT", "section-level", sr
        return "CONFIRM", None, None

    verdicts = {}
    unmatched_note_keys = {k for k in NOTE_REJECTS}
    matched_note_keys = set()
    for cls, r in sample:
        v, root, why = verdict_for(r)
        if root == "note-level":
            matched_note_keys.add(r["note_path"])
        verdicts[r["mapping_id"]] = {
            "verdict": v, "root": root, "stratum": cls, "note": why,
            "spec_code": r["spec_code"], "note_path": r["note_path"],
            "chunk_ordinal": r["chunk"]["ordinal"], "heading": r["chunk"]["heading"],
        }
    unmatched = {k for k in NOTE_REJECTS if k not in matched_note_keys}
    if unmatched:
        print("UNMATCHED NOTE_REJECTS keys (not in the sample or wrong path):", file=sys.stderr)
        for k in sorted(unmatched):
            print(f"  {k} -> {NOTE_REJECTS[k][0]}", file=sys.stderr)
        return 1
    unmatched_sec = {k for k in SECTION_REJECTS
                     if k[0] not in matched_note_keys and
                     k[0] not in {r["note_path"] for _, r in sample}}
    if unmatched_sec:
        print("UNMATCHED SECTION_REJECTS paths:", file=sys.stderr)
        for k in sorted(unmatched_sec):
            print(f"  {k}", file=sys.stderr)
        return 1

    # every verdict that exists must be exercised; SECTION keys not hit = drift
    hit_sec = set()
    for cls, r in sample:
        k = (r["note_path"], r["spec_code"], r["chunk"]["heading"])
        if k in SECTION_REJECTS:
            hit_sec.add(k)
    missed_sec = set(SECTION_REJECTS) - hit_sec
    if missed_sec:
        print("SECTION_REJECTS keys NOT HIT by the sample (heading drift):", file=sys.stderr)
        for k in sorted(missed_sec):
            print(f"  {k}", file=sys.stderr)
        return 1

    # ---- mechanical layer (all sampled rows) ----------------------------------
    r_reader = R()
    _, notes = load_corpus(r_reader)
    by_note, _ = span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}
    mech_fail = 0
    for mid, v in verdicts.items():
        r = by_mid[mid]
        ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        ok = (ctext is not None
              and hashlib.sha256(ctext.encode()).hexdigest()[:16] == r["chunk"]["sha256_16"]
              and norm(r["evidence_quote"]) in norm(ctext)
              and r["validation_status"] == "SUGGESTED"
              and r["provenance"]["tier"] == "RULE_DERIVED")
        if not ok:
            mech_fail += 1
    print(f"mechanical layer: {len(verdicts) - mech_fail}/{len(verdicts)} PASS")

    # ---- Part B verdicts --------------------------------------------------------
    part_b = {}
    for r in worklist:
        is_unres = r.get("spec_code") is None
        part_b[r["mapping_id"]] = {
            "verdict": "DEFER",
            "spec_code": r.get("spec_code"),
            "note_path": r.get("note_path"),
            "why": PART_B_DEFER_UNRESOLVED if is_unres else PART_B_DEFER_UNMAPPED,
        }

    # ---- gate arithmetic ----------------------------------------------------------
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

    # ---- write the verdict record ----------------------------------------------------
    vdoc = {
        "schema": "c40-k2b-review-verdicts/1.0",
        "task": "T-C40",
        "stage": "substrate-review-fill",
        "contract": "graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md "
                    "(the C13 promotion-gate convention)",
        "reviewer": REVIEWER,
        "review_date": REVIEW_DATE,
        "method": {
            "mechanical": f"quote-in-chunk + chunk-hash + store-presence + all-SUGGESTED "
                          f"re-verification, {len(verdicts) - mech_fail}/{len(verdicts)} PASS",
            "semantic": "per-row topical fidelity against the SP's official wording and "
                        "the chunk content; root-caused at note-join level (the T-SPEC "
                        "resolution's note→SP pairs) with section-level overrides where "
                        "the note is right but the section is not",
        },
        "gate": {
            "rule": "Part A precision >= 90% per class AND every Part B row decided",
            "part_a": {"total": total, "by_stratum": rollup,
                       "classes_pass": gate_classes_pass},
            "part_b": {"rows": len(part_b), "decided": part_b_decided,
                       "defer": sum(1 for v in part_b.values() if v["verdict"] == "DEFER")},
            "outcome": "PASS" if gate_pass else "FAIL",
            "outcome_note": None if gate_pass else
                "the promotion is NOT authorized by this fill: Part A precision is "
                "below the 90% class gate on the exact and partial strata (the none "
                "stratum passes; the gate requires every class) — the REJECT rows root-cause to "
                f"{len(NOTE_REJECTS)} note-level joins + "
                f"{len(hit_sec)} section-level scope differences; the store stays "
                "SUGGESTED and the rework path (a T-SPEC resolution-repair round, "
                "then join + substrate re-runs) is the operator's call",
        },
        "verdicts": verdicts,
        "part_b_verdicts": part_b,
    }
    VERDICTS.write_text(yaml.safe_dump(vdoc, allow_unicode=True, sort_keys=False,
                                       width=100), encoding="utf-8")

    # ---- fill the sheet (deterministic re-render from store + verdicts) ----------
    # The fill re-renders the FULL sheet from the store and the verdict record
    # (never string-surgery on the previous file): the blank form's Part B boxes
    # carried a build-time template presumption ([x] DEFER pre-marked) which the
    # filled form supersedes — every mark here is on-evidence.
    title_of = {}
    for n in notes:
        title_of[n["manifest"]["path"]] = n["note"].get("title") or ""

    def chunk_text_of(r):
        return idx[(r["note_path"], r["chunk"]["ordinal"])]

    a_blocks = []
    for cls, r in sample:
        v = verdicts[r["mapping_id"]]
        c = chunk_text_of(r)
        excerpt = " ".join(c.split())[:420]
        up = r["provenance"]["upstream"]
        score_s = "n/a" if up.get("join_score") is None else str(up["join_score"])
        boxes = {
            "CONFIRM": "[x] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs rework",
            "REJECT": "[ ] CONFIRM — this chunk belongs to this SP   [x] REJECT — wrong chunk/SP   [ ] HOLD — needs rework",
            "HOLD": "[ ] CONFIRM — this chunk belongs to this SP   [ ] REJECT — wrong chunk/SP   [x] HOLD — needs rework",
        }[v["verdict"]]
        note_line = ""
        if v["verdict"] == "REJECT" and v["note"]:
            note_line = f"\n- Reviewer note (root cause: {v['root']}): {v['note']}"
        elif v["verdict"] == "CONFIRM":
            note_line = "\n- Reviewer note: CONFIRMed on topical fidelity (chunk content teaches the SP's demand; mechanical layer re-verified)."
        elif v["verdict"] == "HOLD" and v["note"]:
            note_line = f"\n- Reviewer note: {v['note']}"
        a_blocks.append(f"""### {r['spec_code']} — {r['sp_title']}
- Note: {title_of.get(r['note_path'], '')} (`{r['note_path']}`)
- Chunk: ordinal {r['chunk']['ordinal']} — heading `{r['chunk']['heading']}` — sha256_16 `{r['chunk']['sha256_16']}` — {r['chunk']['chars']} chars
- Evidence quote (verbatim self-slice, markdown-safe): "{r['evidence_quote']}"
- Chunk excerpt: «{excerpt}»
- Upstream: T-C32 join {up['join_row']} — tier {up['join_tier']} — score {score_s} — wording {up.get('wording_check')} — validation tier {up['validation_tier']}
- Rationale: {r['rationale']}
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
- Verdict: [ ] AUTHOR an anchor   [ ] REPAIR corpus/markdown   [x] DEFER (record why)
- Why DEFERred: {v['why']}

""")

    gate_note = (
        f"**Gate outcome (this fill):** Part A per-class precision — exact "
        f"{rollup['exact']['precision'] * 100:.1f}%, partial "
        f"{rollup['partial']['precision'] * 100:.1f}%, none "
        f"{rollup['none']['precision'] * 100:.1f}% — the ≥90% class gate FAILS on the "
        f"exact and partial strata (the none stratum passes but the gate requires "
        f"every class) — **the promotion is NOT authorized.** The REJECT rows "
        f"root-cause to {len(NOTE_REJECTS)} note-level joins + {len(hit_sec)} "
        f"section-level scope differences (each carries its note above). The store "
        f"stays `SUGGESTED`; the rework path — a T-SPEC resolution-repair round over "
        f"the implicated joins, then the T-C32 join re-run and the substrate "
        f"re-build — is the operator's decision. This fill records the defect "
        f"inventory; nothing is promoted, nothing is silently repaired.")

    filled = f"""# C40 — maths-a Chunk→SP Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `{seed}` (sha256 of the emitted rows — deterministic regeneration) ·
**Rows:** {len(sample)} anchored spot-checks + {len(worklist)} worklist decisions.
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the
chunk→SP substrate. Per-class rollup: any confirmed-precision < 90% on the sampled
rows → rework that class before promotion.
**Sampling:** all ambiguous rows (the span-marker construction has none by design)
+ seeded stratified anchored sample — low-assurance strata (join score <1.0 or
absent) at 100%, score == 1.0 at ceil(20%) — + every worklist row.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (gate G5);
only the verdicts recorded here — applied in a recorded deterministic apply step —
can. The upstream join is AI_VALIDATED (operator-delegated chain); the tier
difference to chemistry's T-C10-backed substrate is intentional and recorded.

**Filled:** {REVIEW_DATE} — Reviewer: {REVIEWER}.
**Fill method:** mechanical layer scripted re-verification
({len(verdicts) - mech_fail}/{len(verdicts)} PASS); semantic layer per-row
topical-fidelity judgment root-caused at note-join level.

## Part A — anchored-row spot-check ({len(sample)} rows)

{"".join(a_blocks)}## Part B — worklist decisions ({len(worklist)} rows)

{"".join(b_blocks)}## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A total (anchored spot-check) | {total['rows']} | {total['confirm']} | {total['reject']} | {total['hold']} | {total['confirm']}/{total['rows']} = {total['precision'] * 100:.1f}% |
| A stratum: join score == 1.0 (exact) | {rollup['exact']['rows']} | {rollup['exact']['confirm']} | {rollup['exact']['reject']} | {rollup['exact']['hold']} | {rollup['exact']['confirm']}/{rollup['exact']['rows']} = {rollup['exact']['precision'] * 100:.1f}% |
| A stratum: join score < 1.0 (partial) | {rollup['partial']['rows']} | {rollup['partial']['confirm']} | {rollup['partial']['reject']} | {rollup['partial']['hold']} | {rollup['partial']['confirm']}/{rollup['partial']['rows']} = {rollup['partial']['precision'] * 100:.1f}% |
| A stratum: join score n/a (none) | {rollup['none']['rows']} | {rollup['none']['confirm']} | {rollup['none']['reject']} | {rollup['none']['hold']} | {rollup['none']['confirm']}/{rollup['none']['rows']} = {rollup['none']['precision'] * 100:.1f}% |
| B (worklist) | {len(part_b)} | {sum(1 for v in part_b.values() if v['verdict'] == 'DEFER')} DEFER | | | {len(part_b)}/{len(part_b)} decided |

{gate_note}
"""
    SHEET.write_text(filled + "\n", encoding="utf-8")

    # ---- fill record --------------------------------------------------------------
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    rec = {
        "schema": "c40-k2b-review-fill-record/1.0",
        "task": "T-C40",
        "stage": "substrate-review-fill",
        "generated_utc": now,
        "baseline": baseline,
        "reviewer": REVIEWER,
        "sheet": str(SHEET.relative_to(REPO)),
        "verdicts_record": str(VERDICTS.relative_to(REPO)),
        "part_a": {"total": total, "by_stratum": rollup,
                   "note_level_rejects": len(NOTE_REJECTS),
                   "section_level_rejects": len(hit_sec)},
        "part_b": {"rows": len(part_b), "defer": len(part_b)},
        "gate": {"rule": "Part A precision >= 90% per class AND every Part B row decided",
                 "outcome": "PASS" if gate_pass else "FAIL"},
        "disposition": ("promotion NOT authorized; store stays SUGGESTED; the defect "
                        "inventory is recorded for the operator's rework decision"),
        "mechanical_layer": f"{len(verdicts) - mech_fail}/{len(verdicts)} PASS",
    }
    FILL_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
    md = f"""# C40 — K2 Lane B substrate review sheet FILLED (operator-delegate)

**Generated:** {now}  |  **Baseline:** `{baseline}`
**Reviewer:** {REVIEWER}

## Method

- **Mechanical layer:** every sampled row re-verified by script — quote-in-chunk
  containment under the shared `norm()`, chunk `sha256_16`/heading/chars agreement
  with a fresh re-chunking, 1:1 mapping-id presence in the store, all rows
  SUGGESTED — **{len(verdicts) - mech_fail}/{len(verdicts)} PASS**.
- **Semantic layer:** per-row topical fidelity against the SP's official wording
  and the chunk content, root-caused at the NOTE-JOIN level (the T-SPEC
  resolution's note→SP pairs) with section-level overrides where the note is
  right but the sampled section is not.

## Result

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A total | {total['rows']} | {total['confirm']} | {total['reject']} | {total['hold']} | {total['precision'] * 100:.1f}% |
| A stratum exact (score == 1.0) | {rollup['exact']['rows']} | {rollup['exact']['confirm']} | {rollup['exact']['reject']} | {rollup['exact']['hold']} | {rollup['exact']['precision'] * 100:.1f}% |
| A stratum partial (score < 1.0) | {rollup['partial']['rows']} | {rollup['partial']['confirm']} | {rollup['partial']['reject']} | {rollup['partial']['hold']} | {rollup['partial']['precision'] * 100:.1f}% |
| A stratum none (score n/a) | {rollup['none']['rows']} | {rollup['none']['confirm']} | {rollup['none']['reject']} | {rollup['none']['hold']} | {rollup['none']['precision'] * 100:.1f}% |
| B (worklist) | {len(part_b)} | {len(part_b)} DEFER | | | {len(part_b)}/{len(part_b)} decided |

**Gate outcome: FAILS** — Part A per-class precision is below the 90% gate on the
exact (54.1%) and partial (74.4%) strata; the none stratum passes (91.7%) but the
gate requires every class. **The promotion is NOT authorized by this fill.** The
store stays `SUGGESTED`.

## The defect inventory (the fill's product)

- **{len(NOTE_REJECTS)} note-level joins** are semantically wrong — the T-SPEC
  resolution file maps the note to an unrelated SP, and the deterministic T-C32
  id-join inherits it (examples: 'Vector Diagrams'→6.1C cumulative frequency,
  'Tree Diagrams'→6.1C, 'Bar Charts & Pictograms'→6.1A histograms,
  'Negative Numbers'→1.4A surds, 'Exchange Rates'→3.4C differentiation,
  'Coordinates'→3.3B graph transformations, 'Mean Median & Mode'→6.2B spread).
  Every sampled chunk of such a note rejects with the root cause recorded.
- **{len(hit_sec)} section-level scope differences** — the note is rightly joined
  but the sampled section teaches a different SP's content (examples: the
  number-line section under the Cartesian-graph SP 2.8D; the sphere/cone
  sections under the cylinder SP 4.10D).
- The C31 §3 wording crosscheck (202/202 EXACT) verified registry CONSISTENCY
  (resolution wording == store wording for the mapped code), not name→code
  semantics — this fill is the first gate to measure the semantics, working as
  designed.

## Disposition

Zero silent promotion; zero silent repair. The rework path — a T-SPEC
resolution-repair round over the implicated joins, then the T-C32 join re-run
and the substrate re-build — is the operator's decision. The substrate's
SUGGESTED surface, its census, and the 111-code coverage bound all stand.
"""
    FILL_MD.write_text(md + "\n", encoding="utf-8")

    print(f"C40 review fill recorded: Part A {total['confirm']}/{total['rows']} = "
          f"{total['precision'] * 100:.1f}% (exact {rollup['exact']['precision'] * 100:.1f}% / "
          f"partial {rollup['partial']['precision'] * 100:.1f}% / none {rollup['none']['precision'] * 100:.1f}%)")
    print(f"  gate outcome: {'PASS' if gate_pass else 'FAIL'} — promotion "
          f"{'authorized' if gate_pass else 'NOT authorized'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
