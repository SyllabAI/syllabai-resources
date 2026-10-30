#!/usr/bin/env python3
"""Export the ADR-037/ADR-039 official-paper corpus into the syllabai-hub question-set
format (syllabai.sme-exam-questions/1.1 compatible, contract-additive).

Reads  : <repo>/Official-ExamQuestion/igcse-chemistry-19/<series>/4CH1-<paper>/topic.json
         the CURRENT hub content/igcse-chemistry-19/questions.json (28 SME sets —
         the Exam Questions plane, SME-only since the v2 two-file split,
         IA decision commit 662654ade0)
         the CURRENT hub content/igcse-chemistry-19/official-papers.json (54
         official sets — the Past Papers plane; pass it via the REQUIRED
         --current-official-papers)
Writes : <out>/content/igcse-chemistry-19/questions.json        (SME passthrough)
         <out>/content/igcse-chemistry-19/official-papers.json  (official rebuild)
Papers : 1C + 2C (16 series each) + 1CR + 2CR (11 R-series each, the F-178
         R-VARIANT tranches). Official slugs: official-4ch1-<paper>-<series>.

Export gates (fail-closed, v4 of this script — the G-E law archived on PR #27,
landed in wave 12; F44 adds the per-paper topicSlug namespace + G-E1b identity
closure; F51 adds the data-cut stamping law G-E5):
  G-E1  every regenerated set is compared against the bundle of record.
        Default: ANY delta fails the export (the reproducibility law — running
        the exporter of record against its own bundle must be a no-op).
        A content wave passes --expected-deltas <census.json>; the printed
        census (new/gone/changed part ids per slug) must EQUAL it exactly.
  G-E2  per-question sum(parts.marks) == totalMarks; every markPoints block
        sums to the part marks; specPointCodes is a list of strings.
  G-E3  per-slice census (questions/parts/marks) must equal the recorded
        MULTI-SERIES-REPORT constants for BOTH papers (hard stop on drift).
  G-E4  the staged questions.json re-serializes byte-identically to the SME
        bundle of record (the official-papers export never touches the SME
        corpus of record — now proven on the WHOLE file, not just a prefix:
        since the two-file split the SME file IS the whole questions.json).
  G-E5  the data-cut law (F51; runs first, whenever a manifest is staged):
        the run declares --source-cut main@<40-hex> — the resources commit
        whose corpus it consumes; every consumed staging topics file must be
        content-identical to that cut's committed topic.json (modulo the
        generated_utc/generator converter header — the data plane must match
        canonicalized byte-exact), and the declared cut is then STAMPED into
        the staged manifest's importSource.ref. 'importSource.ref stays' is
        retired: the pin once under-claimed at the exporter-of-record commit
        (bf8d56c3) while the run consumed 855cddcf — the wrinkle v2
        PIN-TIGHTEN-1 (fc7a5dc2) closed by hand and filed as this follow-up.
Deterministic; no LLM in the loop.

wave-15 additions (v5, UX doctrine — best experience, non-verbatim presentation
sanctioned; values never invented):
  F-W15-1  stem restore: every upstream stem_md is restored to the question's
           first part (427 stems were silently dropped by every prior exporter
           version — the single largest official-vs-SME rendering gap). Stems
           pass through the eyeballed STEM-RESTORE.json ledger (drop-tail /
           authored rebuild / figure promotion) plus mechanical cleaning
           (control chars, bullet/step reflow). Splice-guard: a stem whose
           text is already folded into part 1 is not duplicated.
  F-W15-2  mark-scheme furniture strip: trailing "Question/Answer Notes Marks"
           MS-table header lines are stripped from solutionMd/markPoints.
  F-W15-3  RETIRED before ship (wave-15 review): the hub renders single
           newlines as soft breaks (react-markdown, no remark-breaks), so
           joining them was render-identical byte noise — and it disturbed
           the wave-14 verbatim-transcription pins (e.g. 2019-06 3(d)(ii)).
           Line breaks stay as extracted; only junk lines are removed.
  F-W15-4  honest stub note: the "pending scan / queued for human verification"
           process jargon is replaced with learner-facing copy (the wave-13
           CROP-REVIEW verdicts are settled; the queue language was stale).

Contract notes (src/lib/contracts.ts in syllabai-hub):
- QuestionPart: id/order/questionType/marks/commandWord/specPointIds/
  specPointCodes/problemMd/solutionMd/choices?/sourcePaper? — this exporter
  ADDS markPoints[] + assets[] (added to the zod contract in the same PR).
- Unknown keys are stripped by zod; every required field is emitted exactly.
- Shared figure references (assets[].shared + ref_part) resolve to the owning
  part's/stem asset's PNG (same rawUrl) — the hub pattern embeds images as
  markdown, so shared figures inline the same URL.

wave-20 additions (v6, stem-figure tranche):
  F-W20-1  stem figures inline: STEM-RESTORE.json entries may carry
           stemFigures (converter-rendered crop assets, flagged stem_figure)
           and stemFigureRef (an already-cropped asset id). Assets flagged
           stem_figure on the question's FIRST part render INSIDE the stem
           block — right after the stem prose, before the part text — instead
           of the end-of-problemMd figure slot; assets targeted at a later
           part (the 2019-06 2C bond-energy tables for 5(a)(i)) render in
           that part's normal figure slot.
  F-W20-2  flattened label-soup cuts: entry.dropSpan [from, to) removes the
           mid-stem flattened figure-label run (both anchors verbatim,
           fail-closed); entry.dropTail removes the tail from a verbatim
           anchor (the soup the crop now serves visually). These apply to
           keep-verdict stems before mechanical cleaning.

F121 additions (v7, group-stem tranche — T-OEQ-GROUPSTEM-1):
  F-W20-4  group stems restore: every question-group intro (topic.json
           groups[letter].group_stem_md — 567 corpus-wide, the largest stem
           class still unrestored after F-W15-1) is restored to the group's
           FIRST part — the printed position, after the question stem and its
           figures. Same laws as F-W15-1: the STEM-RESTORE.json group
           verdicts (keys 'Q<n>.<letter>': drop-tail cuts, dropSpan+dropTail,
           replace) then mechanical cleaning; splice-guard against the part
           text; fail-closed verbatim anchors. A group entry may declare
           figures[] (stem-figure crop ids of the question's FIRST part) that
           render AFTER the group stem so the served order matches the printed
           paper. Data tables and displayed formulae with no serving crop are
           KEPT verbatim by law — a cut needs the crop-corroboration evidence
           of record (the wave-19/20 rule), never the other way round.
  G-E7     the group-stem plane law (unit battery
           scripts/official_examq_f121_tests.py + CI): every group stem must
           reach the served set on its group's first part; a group stem can
           never vanish, be invented, or be mis-attached; group ledger keys
           are slice-scoped consumed (the F113 law); adjudicated cuts must
           actually cut (the cut tail must not survive into the served bytes).

F125 additions (v6, part-level soup tranche — T-OEQ-PARTSOUP-1):
  F-W20-5  part-level cuts: the F123 residual class — flattened figure-label
           soup living in a part's OWN problem_md (pre-existing, the group
           machinery never touches part text) — is adjudicated by the SAME
           cut law in a new ledger key space `Q<n>.<g>(<i>)` (the printed
           part label minus its leading question number and the first
           group's parens: 8(b)(i) -> Q8.b(i)). apply_part_cut() mirrors the
           stem/group ledger application (dropSpan/dropTail, fail-closed
           verbatim anchors, the same trailing-connector strip) and the
           entry's served_by must resolve to a crop asset OF THAT PART
           (machine-checked crop corroboration — a cut removes only what a
           crop of record serves, never the reverse).
  G-E7+    the plane law extends to the part-level space: part ledger keys
           are slice-scoped consumed (stale keys refuse); an adjudicated
           part cut must actually cut (the raw soup-carrying part text must
           never reach the served bytes) and the cleaned head must be
           served on the part itself.
"""
import json, glob, os, re, subprocess, sys, hashlib
from pathlib import Path

# repo-relative (F15 portability): works from any checkout of syllabai-resources
REPO_ROOT = str(Path(__file__).resolve().parents[1])
CORPUS = str(Path(__file__).resolve().parents[1] / "Official-ExamQuestion" / "igcse-chemistry-19")
HUB_CURRENT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/hub-chem-questions.json"
RAW = "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/Official-ExamQuestion/igcse-chemistry-19"
SERIES_LABEL = {"01": "January", "06": "June", "11": "November"}
OFFICIAL_SLUG_PREFIX = "official-4ch1-"
_CHEM_MANIFEST_NOTE = None   # chemistry keeps its per-wave note hardcode at the staging site
# F121 headline of record (T-OEQ-GROUPSTEM-1). The full chained note (this
# headline + the superseded pin's note kept verbatim) is assembled on the
# serving manifest in the v2 content PR; this hardcode is the exporter-side
# bump the staging law requires.
_CHEM_F121_NOTE_HEAD = (
    "ADR-037 exporter v5 at this cut (F121, the group-stem restore wave "
    "- T-OEQ-GROUPSTEM-1): the question-group intros (topic.json "
    "groups[<letter>].group_stem_md, 567 corpus-wide - the largest stem class "
    "still unrestored after the wave-15 question-stem restore) are now "
    "first-class serving content - the exporter restores each group intro to "
    "its group's FIRST part (the printed position, after the question stem and "
    "its figures), passing through the STEM-RESTORE.json group verdicts of "
    "record (36 eyeballed cuts: flattened table/graph/label soup whose printed "
    "object a crop asset of record serves - bond-energy tables, results "
    "tables, ion-formulae tables, solubility/temperature graphs, displayed "
    "formulae; everything else restores mechanically; data tables and "
    "displayed formulae with no serving crop are KEPT verbatim by law - a cut "
    "needs the crop-corroboration evidence, never the reverse). G-E7 pins the "
    "plane fail-closed both directions (a group stem can never vanish, be "
    "invented, or be mis-attached; group ledger keys are slice-scoped "
    "consumed; adjudicated cuts must actually cut). official-papers.json "
    "re-served at this cut: 567 parts carry their group intro (G-E1 census == "
    "scripts/exporter-disclosures/2026-10-30-f121-group-stem-restore-4ch1.json "
    "exactly - the group-stem class only, new=0/gone=0). Counts unchanged "
    "(54 sets / 477 questions / 2,607 parts / 4,860 marks / 4,161 markPoints); "
    "G-E4 SME passthrough byte-identical; figure crops 478 + honest stubs 7 "
    "unchanged. Wave-15 UX doctrine governs under ADR-039 fix-and-disclose: "
    "best learner experience, values never invented. The full prior-lineage "
    "chain (through the F119 label pin and the F117/F113/F108 waves it chains) "
    "is preserved verbatim on the serving manifest. 54 official sets (16x1C + "
    "16x2C + R-variants), 477 questions, 2,607 parts, all spec-tagged.")
# F123 headline of record (T-OEQ-STEMFIG-2019-06). Chains the F121 head
# verbatim (the manifest note is the full chain; this is the exporter-side
# bump the staging law requires).
_CHEM_F123_NOTE_HEAD = (
    "ADR-037 exporter v5 at this cut (F123, the 2019-06 stem-figure stub pass "
    "- T-OEQ-STEMFIG-2019-06): the thirteen un-adjudicated 2019-06 stem-figure "
    "stubs restore - every flattened figure-label soup / dropped printed figure "
    "in the June-2019 slice (1C Q4.b second chromatogram, Q8.c chloroethene, "
    "Q10.a pentane, Q15.b apparatus + mass table; 1CR Q3.c chromatogram, Q8.b "
    "and Q10.b results tables, Q9.b C60 fullerene; 2C Q3.c results table, Q4.c "
    "alloy, Q7.b gas syringe; 2CR Q3.a fractionating column as a declared group "
    "figure) is now served by an eyeballed 150 dpi manual crop (13 assets, "
    "figure crops 478 -> 491) with 12 STEM-RESTORE.json group verdicts (10 cuts "
    "crop-corroborated incl. one dropSpan+dropTail and one complete-sentence-keep, "
    "1 replace, 1 keep; 2 declared figures[] restore print order) - the wave-19/20 "
    "cut law held: every cut's printed object is served by a crop of record. "
    "official-papers.json re-served at this cut: 12 parts changed (G-E1 census == "
    "scripts/exporter-disclosures/2026-10-30-f123-stemfig-2019-06-4ch1.json "
    "exactly - the stem-figure class only, new=0/gone=0). Counts: 54 sets / 477 "
    "questions / 2,607 parts / 4,860 marks / 4,161 markPoints; figure crops 491 + "
    "honest stubs 7; G-E4 SME passthrough byte-identical. Wave-15 UX doctrine "
    "governs under ADR-039 fix-and-disclose: best learner experience, values "
    "never invented. "
    + _CHEM_F121_NOTE_HEAD
)
# F125 headline of record (T-OEQ-PARTSOUP-1). Chains the F123 head verbatim
# (the manifest note is the full chain; this is the exporter-side bump the
# staging law requires).
_CHEM_F125_NOTE_HEAD = (
    "ADR-037 exporter v6 at this cut (F125, the part-level soup pass "
    "- T-OEQ-PARTSOUP-1): the F123 residual part-level soup class adjudicates "
    "to zero - flattened figure-label soup living in a part's OWN problem_md "
    "(1 of record: 2019-06 1CR 8(b)(i), the printed plotting grid's axis "
    "block) now cuts under the same wave-19/20 cut law in a new "
    "STEM-RESTORE.json part key space (Q<n>.<g>(<i>)): the serving crop was "
    "re-cut FIRST (the converter-era auto-crop of asset_8_b_i_grid clipped "
    "the printed y-axis title; the F125 eyeballed rect [143, 192, 507.5, "
    "533.3] on qp.pdf p.19 restores it, rendered from the sha-verified QP of "
    "record) so the cut removes only what the crop serves; G-E7 extends to "
    "the part-level space (slice-scoped consumed, served_by must be a crop "
    "asset of the part, the raw soup-carrying part text must never reach the "
    "served bytes). official-papers.json re-served at this cut: 1 part "
    "changed (G-E1 census == "
    "scripts/exporter-disclosures/2026-10-31-f125-part-soup-4ch1.json "
    "exactly - the part-soup class only, new=0/gone=0). Counts: 54 sets / "
    "477 questions / 2,607 parts / 4,860 marks / 4,161 markPoints; figure "
    "crops 491 + honest stubs 7; G-E4 SME passthrough byte-identical. "
    "Wave-15 UX doctrine governs under ADR-039 fix-and-disclose: best "
    "learner experience, values never invented. "
    + _CHEM_F123_NOTE_HEAD
)
# F119 headline of record (T-OEQ-PARTLABEL-3). The full chained note (this
# headline + the superseded pin's note kept verbatim) is assembled on the
# serving manifest in the v2 content PR; this hardcode is the exporter-side
# bump the staging law requires.
_CHEM_F119_NOTE_HEAD = (
    "ADR-037 exporter v4 at this cut (F119, the printed-part-label serving wave "
    "- T-OEQ-PARTLABEL-3): sourcePaper.questionPart is now a first-class serving "
    "field on the official plane - the printed label ('(a)', '(a)(i)') derived "
    "from the corpus part_number by printed_part_label() (fail-closed grammar: "
    "1-3 parenthesized [a-z0-9]{1,5} groups) and identity-checked against the "
    "part id slug by the new G-E6 label gate (fail-closed both directions: a "
    "label can never vanish or be invented; null IFF the part is a path-less "
    "whole-question slice). official-papers.json re-served at this cut: all "
    "2,607 parts carry labels (G-E1 census == scripts/exporter-disclosures/"
    "2026-10-30-f119-part-label-serving-4ch1.json exactly - the label class "
    "only, zero content deltas, new=0/gone=0). Counts unchanged (54 sets / 477 "
    "questions / 2,607 parts / 4,860 marks / 4,161 markPoints); G-E4 SME "
    "passthrough byte-identical (2,605,409 B); figure crops 478 + honest stubs "
    "7 unchanged. The hub player consumes the field first (lib/part-label "
    "data-first branch) with the slug parse kept as fail-closed fallback; "
    "labels render inline with the part text (T-OEQ-PARTLABEL-2) at a smaller "
    "label size (T-OEQ-PARTLABEL-3 operator refinement, trace "
    "1a18a2e461266b5d). Wave-15 UX doctrine governs under ADR-039 "
    "fix-and-disclose: best learner experience, values never invented. The "
    "full prior-lineage chain (through the F117 #451 pin @2be1107f and the "
    "F113/F108 waves it chains) is preserved verbatim on the serving manifest. "
    "54 official sets (16x1C + 16x2C + R-variants), 477 questions, 2,607 parts, "
    "all spec-tagged.")
_PHYS_MANIFEST_NOTE = (
    "ADR-037 exporter v4 at this cut (F119, the printed-part-label serving wave "
    "- T-OEQ-PARTLABEL-3): sourcePaper.questionPart is now a first-class serving "
    "field on the official plane - the printed label ('(a)', '(a)(i)') derived "
    "from the corpus part_number by printed_part_label() (fail-closed grammar) "
    "and identity-checked against the part id slug by the new G-E6 label gate "
    "(fail-closed both directions: null IFF path-less). official-papers.json "
    "re-served at this cut: 2,239 of 2,254 parts carry labels (G-E1 census == "
    "scripts/exporter-disclosures/2026-10-30-f119-part-label-serving-4ph1.json "
    "exactly - the label class only, zero content deltas, new=0/gone=0); the 15 "
    "whole-question slices stay honestly null. Counts unchanged (55 sets / 540 "
    "questions / 2,254 parts / 4,970 marks / 2,254 markPoints; figure crops 520 "
    "+ honest stubs 25); G-E4 SME passthrough byte-identical (2,057,977 B). The "
    "hub player consumes the field first (lib/part-label data-first branch) "
    "with the slug parse kept as fail-closed fallback; labels render inline "
    "with the part text (T-OEQ-PARTLABEL-2) at a smaller label size "
    "(T-OEQ-PARTLABEL-3 operator refinement, trace 1a18a2e461266b5d). Wave-15 "
    "UX doctrine governs under ADR-039 fix-and-disclose: best learner "
    "experience, values never invented. Supersedes the G-E4-PHYS-STAMP-1 stamp "
    "@main@3b2ce8da700b80f51700fb34fc721c90d6654d6b; its full note (and the "
    "bootstrap lineage it chains to Task 22 / F103) is preserved verbatim on "
    "the serving manifest. 55 official sets (17x1P + 16x2P + 11x1PR + 11x2PR), "
    "540 questions, 2,254 parts, all spec-tagged.")


def series_label(series):
    year, mm = series.split("-")
    return f"{SERIES_LABEL.get(mm, mm)} {year}"


def part_slug(pn):
    return pn.replace("(", "-").replace(")", "")


def printed_part_label(part_number):
    """F119: the printed part label ("(a)", "(a)(i)") served as a first-class
    field (sourcePaper.questionPart) — the corpus part_number minus its leading
    question number. None IFF the part_number carries no printed sub-part label
    (whole-question slices: maths-B's bare "2"/"4", the 735 no-path class).
    Fail-closed grammar: 1-3 parenthesized [a-z0-9]{1,5} groups; anything else
    refuses (None) — and G-E6's id cross-check then refuses the part outright
    if its id slug disagrees, so a label can never silently vanish or be made
    up. The hub player (lib/part-label, T-OEQ-PARTLABEL-1/2/3) consumes this
    field of record first and keeps the slug parse as the fail-closed fallback."""
    m = re.match(r"^\d+(.*)$", (part_number or "").strip())
    rest = (m.group(1) if m else "").strip()
    if not rest:
        return None
    if not re.match(r"^(?:\([a-z0-9]{1,5}\)){1,3}$", rest):
        return None
    return rest


def g_e6_label_law(parts, census=None):
    """F119: every official part's sourcePaper.questionPart must BE the label
    its own identity carries — the id slug's path segments re-wrapped
    ("1-a-i" -> "(a)(i)"); null IFF the id is path-less (whole-question
    slices). Fail-closed in BOTH directions: a vanished label and an invented
    one both raise. census (optional dict) accumulates per-path-level counts."""
    label_seg_re = re.compile(r"^[a-z0-9]{1,5}$")
    for p in parts:
        bits = p["id"].split("_")
        if len(bits) != 4 or bits[0] != "offp":
            raise ExportGateError(
                f"G-E6: {p['id']} id shape off-grammar (offp_<series>_<paper>_<qn>[-<path>])")
        segs = bits[3].split("-")[1:]
        if segs and not (len(segs) <= 3 and all(label_seg_re.match(s) for s in segs)):
            raise ExportGateError(
                f"G-E6: {p['id']} path segments off-grammar: {segs!r}")
        expected = "".join(f"({s})" for s in segs) if segs else None
        actual = (p.get("sourcePaper") or {}).get("questionPart")
        if actual != expected:
            raise ExportGateError(
                f"G-E6: {p['id']} questionPart {actual!r} != the id-derived "
                f"printed label {expected!r}")
        if census is not None:
            census[len(segs)] = census.get(len(segs), 0) + 1


PAPER = os.environ.get("EXAMQ_EXPORT_PAPERS", "1C,2C")   # legacy env (unused by the v4 flow)

# Task 22 hub-export wave: the lane registry (the Task 14 converter pattern).
# 4ch1 stays the DEFAULT lane: the module constants below keep their chemistry
# values at import time, so the default behavior is byte-identical; --spec 4ph1
# rebinds the lane-scoped globals via apply_lane().
LANE_SPEC = "4ch1"
LANES = {
    "4ch1": dict(lane="igcse-chemistry-19", code="4CH1", prefix="official-4ch1-",
                 subject="Chemistry", syllabus="2017 (Issue 3)",
                 topic_seed=lambda series, paper: series,
                 manifest_note=_CHEM_MANIFEST_NOTE),
    "4ph1": dict(lane="igcse-physics-19", code="4PH1", prefix="official-4ph1-",
                 subject="Physics", syllabus="2017",
                 topic_seed=lambda series, paper: "4ph1-" + series + "-" + paper,
                 manifest_note=_PHYS_MANIFEST_NOTE),
}


def apply_lane(spec):
    """Rebind the lane-scoped globals for --spec 4ph1. The 4ch1 branch is the
    identity (the module constants are already the chemistry values)."""
    global CORPUS, RAW, OFFICIAL_SLUG_PREFIX, PAPER_SERIES, PAPERS, EXPECTED_CENSUS, LANE_SPEC
    cfg = LANES[spec]
    LANE_SPEC = spec
    if spec == "4ch1":
        return cfg
    CORPUS = str(Path(__file__).resolve().parents[1] / "Official-ExamQuestion" / cfg["lane"])
    RAW = ("https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/"
           "Official-ExamQuestion/" + cfg["lane"])
    OFFICIAL_SLUG_PREFIX = cfg["prefix"]
    PAPER_SERIES = {"1P": list(_PH_SERIES_1P), "2P": list(_PH_SERIES_2P),
                    "1PR": list(_PH_SERIES_1PR), "2PR": list(_PH_SERIES_2PR)}
    PAPERS = tuple(PAPER_SERIES)
    EXPECTED_CENSUS = _PH_EXPECTED_CENSUS
    return cfg


# physics topicId seed: lane-scoped (chemistry's of-record topicIds are
# "off_" + sha1(series)[:12] - the G-E1b identity law keeps them byte-identical;
# a physics set seeded with the bare series would COLLIDE with chemistry's in
# the hub's package-global id space - the F44 collision class, lane-wide).
# The physics law of record: "off_" + sha1("4ph1-<series>-<paper>")[:12].
# The physics frozen census of record (Task 22; generated from
# igcse-physics-19/MULTI-SERIES-REPORT.json @ converter v0.25.0 - 55 slices).
# (questions, parts, marks) per slice; a mismatch is a hard stop (G-E3).
_PH_EXPECTED_CENSUS = {
    "1P": {
        "2019-06": (12, 47, 110),
        "2020-01": (12, 50, 110),
        "2020-06": (11, 42, 110),
        "2020-11": (11, 42, 110),
        "2021-01": (11, 50, 110),
        "2021-06": (11, 48, 110),
        "2021-11": (12, 53, 110),
        "2022-01": (12, 55, 110),
        "2022-06": (12, 59, 110),
        "2023-01": (11, 50, 110),
        "2023-06": (12, 45, 110),
        "2023-11": (12, 49, 110),
        "2024-06": (12, 51, 110),
        "2024-11": (11, 53, 110),
        "2025-06": (11, 49, 110),
        "2025-11": (12, 50, 110),
        "2026-06": (11, 46, 110),
    },
    "1PR": {
        "2019-06": (11, 54, 110),
        "2020-01": (12, 52, 110),
        "2020-06": (13, 53, 110),
        "2021-01": (12, 47, 110),
        "2022-01": (12, 49, 110),
        "2022-06": (12, 49, 110),
        "2023-01": (11, 55, 110),
        "2023-06": (11, 46, 110),
        "2024-06": (12, 50, 110),
        "2025-06": (11, 43, 110),
        "2026-06": (11, 47, 110),
    },
    "2P": {
        "2019-06": (9, 31, 70),
        "2020-01": (8, 31, 70),
        "2020-06": (8, 35, 70),
        "2021-01": (8, 37, 70),
        "2021-06": (7, 32, 70),
        "2021-11": (8, 37, 70),
        "2022-01": (9, 31, 70),
        "2022-06": (7, 31, 70),
        "2023-01": (8, 28, 70),
        "2023-06": (8, 36, 70),
        "2023-11": (8, 29, 70),
        "2024-06": (8, 33, 70),
        "2024-11": (8, 35, 70),
        "2025-06": (8, 32, 70),
        "2025-11": (8, 36, 70),
        "2026-06": (8, 27, 70),
    },
    "2PR": {
        "2019-06": (8, 34, 70),
        "2020-01": (8, 33, 70),
        "2020-06": (8, 36, 70),
        "2021-01": (8, 33, 70),
        "2022-01": (8, 30, 70),
        "2022-06": (7, 30, 70),
        "2023-01": (8, 34, 70),
        "2023-06": (8, 30, 70),
        "2024-06": (9, 30, 70),
        "2025-06": (8, 31, 70),
        "2026-06": (8, 28, 70),
    },
}
# Physics paper schedules of record: 1P = all 17 series; 2P = 16 (the 2020-11
# NO-QP trio: 1PR/2P/2PR carry no qp.pdf); 1PR/2PR = 11 (the five two-variant
# sessions 2021-06/2021-11/2023-11/2024-11/2025-11 never printed R variants,
# the COVID/November pattern - same shape as the chemistry R1CR schedule).
_PH_SERIES_1P = ["2019-06", "2020-01", "2020-06", "2020-11", "2021-01", "2021-06", "2021-11", "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06", "2024-11", "2025-06", "2025-11", "2026-06"]
_PH_SERIES_2P = ["2019-06", "2020-01", "2020-06", "2021-01", "2021-06", "2021-11", "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06", "2024-11", "2025-06", "2025-11", "2026-06"]
_PH_SERIES_1PR = ["2019-06", "2020-01", "2020-06", "2021-01", "2022-01", "2022-06", "2023-01", "2023-06", "2024-06", "2025-06", "2026-06"]
_PH_SERIES_2PR = ["2019-06", "2020-01", "2020-06", "2021-01", "2022-01", "2022-06", "2023-01", "2023-06", "2024-06", "2025-06", "2026-06"]


def raw_url(series, paper, rel_path):
    return f"{RAW}/{series}/{LANES[LANE_SPEC]['code']}-{paper}/{rel_path}"


def resolve_asset_path(a, by_id):
    """Shared refs point at the owner's PNG (same file); stem ids too."""
    if a.get("path"):
        return a["path"]
    ref = a.get("ref_part")
    if ref and ref in by_id:
        return by_id[ref].get("path")
    return None


STEM_LEDGER_PATH = os.path.join(REPO_ROOT, "Official-ExamQuestion", "STEM-RESTORE.json")

# F-W15-2: a solution line made only of MS-table header furniture (the answer
# grid's column headers leak into the extracted cell text). Tokens are matched
# after stripping glue digits ("3Answer" → "Answer").
FURNITURE_WORDS = {"question", "number", "answer", "notes", "marks",
                   "additional", "guidance", "total", "for"}


def _is_furniture_line(line):
    toks = [t for t in re.split(r"[^A-Za-z]+", line) if t]
    return bool(toks) and all(t.lower().lstrip("0123456789") in FURNITURE_WORDS for t in toks)


# F87 (v0.21.1): the QP multi-page footer family — serve-time defense on ALL
# text fields (problemMd never went through strip_furniture). Redundant second
# line of defense behind the converter battery, never the only one.
_RX_CONTINUES = re.compile(r"\s*QUESTION\s*\d{0,2}\s*CONTINUES\s+ON\s+(?:THE\s+)?(?:NEXT|BACK)(?:\s*/\s*(?:NEXT|BACK))?\s+PAGE\.?", re.I)
def _strip_continues(s):
    return _RX_CONTINUES.sub("", s).rstrip() if _RX_CONTINUES.search(s) else s


def strip_furniture(sol):
    """F-W15-2: drop trailing furniture lines (up to 4) + a trailing
    'Total for Question N = M marks' line, from the end only."""
    if not sol:
        return sol
    lines = sol.rstrip().splitlines()
    n = 0
    while lines and n < 4:
        last = lines[-1].strip()
        if _is_furniture_line(last) or re.fullmatch(r"Total\s+\d+", last):
            lines.pop()
            n += 1
            continue
        if re.fullmatch(r"Total\s+for\s+Question\s+\d+\s*=\s*\d+\s*marks", last):
            lines.pop()
            n += 1
            continue
        break
    return "\n".join(lines).rstrip() if n else sol


def _bulletize(stem):
    """F-W15-1 cleaning: flattened method bullet runs (• / ●) become markdown
    bullets; 'Step N' runs become one line per step; control chars are
    stripped. Only fires on ≥2 occurrences so prose never splits."""
    s = re.sub(r"[\x00-\x08\x0b-\x1f]", "", stem).replace("\t", " ")
    for b in ("\u2022", "\u25cf"):
        if s.count(f" {b} ") >= 1:
            parts = [x.strip() for x in s.split(b) if x.strip()]
            if len(parts) >= 3:
                s = parts[0] + "\n" + "\n".join(f"- {p}" for p in parts[1:])
                break
    if len(re.findall(r"\bStep\s+\d+\b", s)) >= 2:
        s = re.sub(r"(?<!^)(?<!\n)\s*(\bStep\s+\d+\b)", r"\n\1", s)
    return s


SOLUTION_ENRICH_PATH = os.path.join(REPO_ROOT, "Official-ExamQuestion", "SOLUTION-ENRICH.json")


def load_enrichment_ledger():
    """F-W20-3: the authored worked-answer ledger (wave-20 Part C). Optional:
    an absent ledger means every part serves its MS-derived solution."""
    if not os.path.exists(SOLUTION_ENRICH_PATH):
        return {}
    doc = json.load(open(SOLUTION_ENRICH_PATH))
    return doc.get("entries", {})


def load_stem_ledger():
    if not os.path.exists(STEM_LEDGER_PATH):
        raise ExportGateError(
            f"F-W15-1: stem ledger missing at {STEM_LEDGER_PATH} — the wave-15 "
            "stem restore runs with the eyeballed ledger of record (STEM-RESTORE.json)")
    return json.load(open(STEM_LEDGER_PATH))


def restore_stem(q, series, paper, ledger, by_part_num):
    """F-W15-1: cleaned stem markdown for a question, or None. Authored ledger
    verdicts win; everything else passes mechanical cleaning. Splice-guard:
    stems already folded into part 1 by the converter are not duplicated.
    wave-20 (F-W20-2): entry.dropSpan / entry.dropTail cut the flattened
    figure-label soup BEFORE verdict handling; both anchors verbatim."""
    stem = (q.get("stem_md") or "").strip()
    if not stem:
        return None
    qnum = str(q["question_number"])
    entry = ledger.get("verdicts", {}).get(f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:Q{qnum}")
    first_md = (q["parts"][0].get("problem_md") or "") if q["parts"] else ""
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    if norm(stem)[:60] and norm(stem)[:60] in norm(first_md):
        return None  # splice-guard: converter already folded this stem into part 1
    if entry:
        span = entry.get("dropSpan")
        if span:
            a_from, a_to = span
            i, j = stem.find(a_from), stem.find(a_to)
            if i < 0 or j < 0 or j <= i:
                raise ExportGateError(
                    f"F-W20-2: dropSpan anchors not found/ordered in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {a_from[:50]!r} -> {a_to[:50]!r}")
            stem = (stem[:i].rstrip() + " " + stem[j:].lstrip()).strip()
        tail = entry.get("dropTail")
        if tail:
            if tail not in stem:
                raise ExportGateError(
                    f"F-W20-2: dropTail anchor not found in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {tail[:60]!r}")
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-\u2013\u2014.:;]?$", "", stem)
    if entry and entry.get("verdict") == "replace":
        anchor = entry.get("dropTailFrom")
        if anchor:
            if anchor not in stem:
                raise ExportGateError(
                    f"F-W15-1: dropTailFrom anchor not found in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {anchor[:60]!r}")
        md = entry["stemMd"]
        fig_part = entry.get("inlineFigureFrom")
        if fig_part:
            a = by_part_num.get(fig_part)
            crop = next((x for x in (a or {}).get("assets", [])
                         if x.get("kind") == "crop" and resolve_asset_path(x, {})), None) if a else None
            if not crop:
                raise ExportGateError(
                    f"F-W15-1: inlineFigureFrom {fig_part} on "
                    f"{series}/4CH1-{paper} Q{qnum} has no resolvable crop asset")
            url = raw_url(series, paper, resolve_asset_path(crop, {}))
            cap = f"{crop.get('mention', 'figure')} — official paper figure (qp.pdf p.{crop.get('page')})"
            md = md.replace("{{FIG:" + fig_part + "}}", f"![{cap}]({url})")
        if "{{FIG:" in md:
            raise ExportGateError(
                f"F-W15-1: unresolved FIG placeholder in authored stem of "
                f"{series}/4CH1-{paper} Q{qnum}")
        return md.strip()
    if entry and entry.get("verdict") == "drop-tail":
        tail = entry.get("tail")
        if tail and tail not in stem:
            raise ExportGateError(
                f"F-W15-1: drop-tail anchor not found in stem of "
                f"{series}/4CH1-{paper} Q{qnum}: {tail[:60]!r}")
        if tail:
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-–—.:;]?$", "", stem)
        return _bulletize(stem).strip()
    # unledgered (or keep-verdict) stems: mechanical cleaning only
    return _bulletize(stem).strip() or None


GROUP_PART_RE = re.compile(r"^(\d+)\(([a-z])\)")


def group_letter_of(part_number):
    """The group letter a part_number belongs to ('5(a)(ii)' -> 'a'), else None."""
    m = GROUP_PART_RE.match(str(part_number or ""))
    return m.group(2) if m else None


def part_ledger_key(qnum, part_number):
    """F125: the part-level verdict key suffix for a part's OWN problem_md —
    the printed part label minus its leading question number and the first
    group's parens: '8(b)(i)' -> 'b(i)', '6(a)' -> 'a', '15(b)(iv)' -> 'b(iv)'.
    Whole-question parts (no parenthesized path) carry no part-level key."""
    pn = str(part_number or "")
    q = str(qnum)
    if not pn.startswith(q + "("):
        return None
    suffix = pn[len(q) + 1:]
    if not suffix or ")" not in suffix:
        return None
    first, _, rest = suffix.partition(")")
    return f"Q{q}.{first}{rest}"


def apply_part_cut(text, entry, key):
    """F125 (F-W20-5): the part-level adjudicated cuts — the same verdict
    vocabulary, fail-closed verbatim anchors and trailing-connector strip as
    the F121 group machinery (restore_group_stem), deliberately mirrored not
    shared so the group path's served bytes stay byte-identical. Applies to
    the part's OWN problem_md only; the entry's served_by crop corroboration
    is machine-checked by the G-E7 part-level law."""
    span = entry.get("dropSpan")
    if span:
        a_from, a_to = span
        i, j = text.find(a_from), text.find(a_to)
        if i < 0 or j < 0 or j < i:
            raise ExportGateError(
                f"F125: dropSpan anchors not found/ordered in part {key}: "
                f"{a_from[:50]!r} -> {a_to[:50]!r}")
        text = (text[:i].rstrip() + " " + text[j:].lstrip()).strip()
    tail = entry.get("dropTail")
    if tail:
        if tail not in text:
            raise ExportGateError(
                f"F125: dropTail anchor not found in part {key}: {tail[:60]!r}")
        text = text[:text.index(tail)].rstrip()
        text = re.sub(r"[\s]*[-\u2013\u2014.:;]?$", "", text)
    return text


def restore_group_stem(g, series, paper, qnum, letter, ledger, first_problem_md):
    """F121 (F-W20-4): the question-group intro (groups[letter].group_stem_md)
    is restored to the group's FIRST part — the largest remaining stem class
    after F-W15-1 (question stems): 567 group intros were silently dropped by
    every prior exporter version.

    Same laws as the question stem: the eyeballed ledger verdicts (dropSpan /
    dropTail cuts, replace) then mechanical cleaning; splice-guard: a stem
    already folded into the group's first part is not duplicated. Anchors are
    verbatim and fail-closed. Ledger keys: '<series>/4CH1-<paper>:Q<n>.<letter>'.
    """
    stem = (g.get("group_stem_md") or "").strip()
    if not stem:
        return None
    key = f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:Q{qnum}.{letter}"
    entry = (ledger or {}).get("verdicts", {}).get(key)
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    if norm(stem)[:60] and norm(stem)[:60] in norm(first_problem_md or ""):
        return None  # splice-guard: the converter already folded this stem in
    if entry:
        span = entry.get("dropSpan")
        if span:
            a_from, a_to = span
            i, j = stem.find(a_from), stem.find(a_to)
            if i < 0 or j < 0 or j < i:
                raise ExportGateError(
                    f"F121: dropSpan anchors not found/ordered in group stem "
                    f"{key}: {a_from[:50]!r} -> {a_to[:50]!r}")
            stem = (stem[:i].rstrip() + " " + stem[j:].lstrip()).strip()
        tail = entry.get("dropTail")
        if tail:
            if tail not in stem:
                raise ExportGateError(
                    f"F121: dropTail anchor not found in group stem {key}: "
                    f"{tail[:60]!r}")
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-\u2013\u2014.:;]?$", "", stem)
    if entry and entry.get("verdict") == "replace":
        if "{{FIG:" in (entry.get("stemMd") or ""):
            raise ExportGateError(
                f"F121: FIG placeholders are not supported on group stems "
                f"(v1): {key}")
        return _bulletize(entry["stemMd"]).strip()
    if entry and entry.get("verdict") == "drop-tail":
        tail = entry.get("tail")
        if tail and tail not in stem:
            raise ExportGateError(
                f"F121: drop-tail anchor not found in group stem {key}: "
                f"{tail[:60]!r}")
        if tail:
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-\u2013\u2014.:;]?$", "", stem)
        return _bulletize(stem).strip() or None
    # unledgered (or keep-verdict) group stems: mechanical cleaning only
    return _bulletize(stem).strip() or None


def export_series(series, paper, topic=None, stem_ledger=None, enrich=None):
    if topic is None:
        tp = f"{CORPUS}/{series}/{LANES[LANE_SPEC]['code']}-{paper}/topic.json"
        topic = json.load(open(tp))
    tj = topic
    # asset id -> asset (for shared-ref resolution)
    by_id = {}
    for q in tj["questions"]:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                by_id[a["id"]] = a

    questions = []
    for qi, q in enumerate(tj["questions"]):
        qnum = str(q["question_number"])
        # F-W15-1: the printed stem is restored to the question's first part
        by_part_num = {p["part_number"]: p for p in q["parts"]}
        stem_md = restore_stem(q, series, paper, stem_ledger or {}, by_part_num)
        # F-W20-1: stem-level figures render inside the stem block
        stem_figs_md = []
        s_entry = (stem_ledger or {}).get("verdicts", {}).get(f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:Q{qnum}") or {}
        ref = (s_entry.get("stemFigureRef") or {}).get("asset")
        if ref:
            ra = by_id.get(ref)
            if ra is None:
                # F28 collapse: the owner record may exist only as a share-ref
                # whose ref_part names the stem asset (its path IS the owner's
                # PNG) — resolve through the share-ref's path.
                ra = next((a for a in by_id.values() if a.get("ref_part") == ref), None)
            rpath = resolve_asset_path(ra, by_id) if ra else None
            if not ra or ra.get("kind") != "crop" or not rpath:
                raise ExportGateError(
                    f"F-W20-1: stemFigureRef {ref} on {series}/4CH1-{paper} Q{qnum} "
                    f"does not resolve to a real crop asset")
            url = raw_url(series, paper, rpath)
            cap = f"{ra.get('mention', 'figure')} — official paper figure (qp.pdf p.{ra.get('page')})"
            stem_figs_md.append((ra.get("id"), f"![{cap}]({url})"))
        first_assets = (q["parts"][0].get("assets") or []) if q["parts"] else []
        for a in first_assets:
            if not a.get("stem_figure") or a.get("kind") != "crop":
                continue
            rel = resolve_asset_path(a, by_id)
            if not rel:
                raise ExportGateError(
                    f"F-W20-1: stem figure {a['id']} on {series}/4CH1-{paper} Q{qnum} "
                    f"has no resolvable path")
            url = raw_url(series, paper, rel)
            cap = f"{a.get('mention', 'figure')} — official paper figure (qp.pdf p.{a.get('page')})"
            stem_figs_md.append((a["id"], f"![{cap}]({url})"))
        # ---- F121 (F-W20-4): the group intros restore to their group's first
        # part. A group ledger entry may declare figures[] (asset ids that are
        # stem-figure crops of the question's FIRST part) — those render after
        # the group stem so the served order matches the printed paper.
        groups = q.get("groups") or {}
        g_first_pn, group_stems, g_figs_decl = {}, {}, {}
        q0_pn = q["parts"][0]["part_number"] if q["parts"] else None
        for letter, g in groups.items():
            gkey = f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:Q{qnum}.{letter}"
            g_entry = (stem_ledger or {}).get("verdicts", {}).get(gkey) or {}
            fp = next((p for p in q["parts"]
                       if group_letter_of(p["part_number"]) == letter), None)
            if fp is None:
                if (g.get("group_stem_md") or "").strip() or g_entry:
                    raise ExportGateError(
                        f"F121/G-E7: group {letter} of {series}/4CH1-{paper} "
                        f"Q{qnum} carries a stem/ledger entry but no part "
                        f"resolves to it — a group stem can neither vanish nor "
                        f"be unattachable")
                continue
            g_first_pn[fp["part_number"]] = letter
            group_stems[letter] = restore_group_stem(
                g, series, paper, qnum, letter, stem_ledger or {},
                fp.get("problem_md"))
            figs = g_entry.get("figures") or []
            if figs:
                if fp["part_number"] != q0_pn:
                    raise ExportGateError(
                        f"F121: figures[] declared on {gkey} but the group's "
                        f"first part is not the question's first part — the "
                        f"stem-figure block only exists there")
                first_ids = {a["id"] for a in first_assets
                             if a.get("stem_figure") and a.get("kind") == "crop"}
                missing = [f for f in figs if f not in first_ids]
                if missing:
                    raise ExportGateError(
                        f"F121: declared figure(s) {missing} on {gkey} are not "
                        f"stem-figure crops of the question's first part")
                g_figs_decl[letter] = list(figs)
        g0 = g_first_pn.get(q0_pn)
        decl0 = set(g_figs_decl.get(g0) or []) if g0 else set()
        stem_figs_head = [md for aid, md in stem_figs_md if aid not in decl0]
        stem_figs_group = [md for aid, md in stem_figs_md if aid in decl0]
        parts = []
        for p in q["parts"]:
            marks = int(p["marks"]) if p.get("marks") is not None else 0
            assets_out, figures_md, solution_figs_md = [], [], []
            for a in p.get("assets") or []:
                # F-W20-1: stem figures on the FIRST part render in the stem
                # block (stem_figs_md above) — their crop record still rides
                # assets[] for the metadata, but the end-of-part figure slot
                # must not duplicate the inline stem image.
                # F113: an asset whose source is the mark scheme ("ms.pdf")
                # is the PRINTED MS ANSWER (the F95 MS-answer-is-a-drawing
                # class served by the converter's MS-answer-figure crops).
                # It renders in the SOLUTION surface — solutionMd — never in
                # problemMd, and its caption names the ms.pdf page.
                is_stem_fig = a.get("stem_figure") and len(parts) == 0
                is_ms_answer = a.get("source") == "ms.pdf"
                rel = resolve_asset_path(a, by_id)
                entry = {
                    "kind": a.get("kind"),
                    "mention": a.get("mention"),
                    "page": a.get("page"),
                    "review": bool(a.get("review")),
                    "shared": bool(a.get("shared")),
                }
                if a.get("ref_part"):
                    entry["refPart"] = a["ref_part"]
                if is_ms_answer:
                    entry["source"] = "ms"
                if a.get("kind") == "crop" and rel:
                    entry["path"] = rel
                    entry["rawUrl"] = raw_url(series, paper, rel)
                    if is_ms_answer:
                        cap = (f"{a.get('mention', 'figure')} — official mark scheme "
                               f"answer figure (ms.pdf p.{a.get('page')})")
                        solution_figs_md.append(f"![{cap}]({entry['rawUrl']})")
                    else:
                        cap = f"{a.get('mention', 'figure')} — official paper figure (qp.pdf p.{a.get('page')})"
                        if a.get("shared"):
                            cap += f" (same figure as {a.get('ref_part')})"
                        if not is_stem_fig:
                            figures_md.append(f"![{cap}]({entry['rawUrl']})")
                elif a.get("kind") == "crop-required":
                    if is_ms_answer:
                        solution_figs_md.append(
                            "> *The printed mark scheme answers this part with a figure; "
                            "the eyeballed crop is pending review.*")
                    else:
                        # F-W15-4: learner-facing copy — the wave-13 CROP-REVIEW
                        # verdicts settled these as honest blank-scaffold stubs;
                        # the old 'pending scan / queued for verification' line
                        # described a queue that no longer exists.
                        figures_md.append(
                            "> *No printed figure accompanies this part — in the paper "
                            "you would draw the diagram (or label the apparatus) in the "
                            "answer space provided.*")
                assets_out.append(entry)
            problem_md = (p.get("problem_md") or "").strip()
            # F125 (F-W20-5): the part-level adjudicated cuts (the F123
            # residual class — soup in a part's OWN problem_md) apply before
            # composition, under the same fail-closed anchor law.
            pk = part_ledger_key(qnum, p["part_number"])
            if pk:
                pkey = f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:{pk}"
                p_entry = (stem_ledger or {}).get("verdicts", {}).get(pkey)
                if p_entry:
                    problem_md = apply_part_cut(problem_md, p_entry, pkey)
            head = []
            g_here = g_first_pn.get(p["part_number"])
            if len(parts) == 0 and stem_md:
                # F-W20-1: stem prose, then its (undeclared) figures
                head.append(stem_md)
                head += stem_figs_head
            if g_here:
                gmd = group_stems.get(g_here)
                if gmd:
                    # F121: the group intro renders before the part text;
                    # declared group figures render after it (print order)
                    head.append(gmd)
                    if len(parts) == 0:
                        head += stem_figs_group
            if head:
                problem_md = "\n\n".join(head + [problem_md])
            if figures_md:
                problem_md += "\n\n" + "\n\n".join(figures_md)
            sol = p.get("solution_md") or None
            if sol:
                # F-W15-2: trailing MS-grid furniture lines off (visible junk).
                # F-W15-3 retired: no reflow — single newlines render as soft
                # breaks, and the verbatim cell structure is wave-14-pinned.
                sol = strip_furniture(sol) or None
            # F-W20-3: authored worked answers replace the terse MS cell as the
            # learner-facing solutionMd; the MS text itself stays verbatim in
            # mark_points (marking is never authored). Ledger-only: a part
            # without a reviewed entry keeps its MS-derived solution.
            e_entry = (enrich or {}).get(f"{series}-{paper}:{part_slug(p['part_number'])}")
            if e_entry and e_entry.get("review") == "authored-r0" and e_entry.get("solutionMd"):
                sol = e_entry["solutionMd"]
            # F113: the printed MS answer figure rides AFTER the authored text
            # (the image is the printed answer of record; the text is the
            # authored walkthrough — both learner-facing, image last).
            if solution_figs_md:
                sol = ((sol + "\n\n") if sol else "") + "\n\n".join(solution_figs_md)
            mp = [{"id": x["id"], "marks": x["marks"],
                   "textMd": _strip_continues(strip_furniture(x["text_md"]))}
                  for x in (p.get("mark_points") or [])]
            choices = None
            if p.get("question_type") == "multiple_choice" and p.get("choices"):
                ch = p["choices"]
                if isinstance(ch, str):
                    ch = json.loads(ch)
                choices = [{"label": c["label"], "isCorrect": bool(c.get("is_correct")),
                            "textMd": c.get("text_md", "")} for c in ch]
            parts.append({
                # wave-15 id-collision fix: the paper code is part of the
                # identity — offp_<series>_<part> collided across 1C/2C/1CR/2CR
                # of the same series (631 duplicated ids), cross-wiring saved
                # MCQ answers and typed-answer drafts between papers.
                "id": f"offp_{series}_{paper.lower()}_{part_slug(p['part_number'])}",
                "order": len(parts),
                "questionType": p.get("question_type"),
                "marks": marks,
                "commandWord": None,
                "specPointIds": [],
                "specPointCodes": list(p.get("spec_point_codes") or []),
                "problemMd": _strip_continues(problem_md),
                "solutionMd": sol,
                "markPoints": mp,
                "assets": assets_out,
                "answerStatus": p.get("answer_status"),
                "choices": choices,
                "sourcePaper": {
                    "date": series_label(series),
                    "number": f"{LANES[LANE_SPEC]['code']}/{paper}",
                    "questionNumber": int(qnum) if qnum.isdigit() else None,
                    "questionPart": printed_part_label(p["part_number"]),
                },
            })
        questions.append({
            "id": f"offq_{series}_{paper.lower()}_{part_slug(qnum)}",
            "order": qi,
            "difficulty": None,
            "style": "exam_whole",
            "totalMarks": int(q["total_marks"]) if q.get("total_marks") is not None else sum(x["marks"] for x in parts),
            "parts": parts,
        })

    return {
        "topicId": "off_" + hashlib.sha1(
            LANES[LANE_SPEC]["topic_seed"](series, paper).encode()).hexdigest()[:12],
        "slug": OFFICIAL_SLUG_PREFIX + paper.lower() + "-" + series,
        "name": f"{series_label(series)} — Paper {paper} (official past paper)",
        "setName": "Official Past Paper",
        # F44: topicSlug := the set's own canonical slug (the per-paper ref
        # namespace of record — v2 0776f8dea7, operator-ordered "path 1 — fix":
        # one shared topicSlug with per-set restarting orders collided 12 base
        # refs and the frozen package-global seenRefs gate refused the bundle).
        "topicSlug": OFFICIAL_SLUG_PREFIX + paper.lower() + "-" + series,
        "section": f"Official past papers ({LANES[LANE_SPEC]['code']}/{paper})",
        "sectionSlug": "official-past-papers",
        "curriculum": {
            "board": "Pearson Edexcel",
            "level": "IGCSE",
            "subject": LANES[LANE_SPEC]["subject"],
            "code": LANES[LANE_SPEC]["code"],
            "syllabusVersion": LANES[LANE_SPEC]["syllabus"],
        },
        "source": {
            "provider": "Pearson Edexcel (operator archive, ADR-037 verbatim extraction)",
            "license": "operator-archive; extracted verbatim from the licensed archive PDFs — see syllabai-resources Official-ExamQuestion/README.md",
            "pageUrl": f"https://github.com/SyllabAI/syllabai-resources/tree/main/Official-ExamQuestion/{LANES[LANE_SPEC]['lane']}/{series}/{LANES[LANE_SPEC]['code']}-{paper}",
        },
        "schema": "syllabai.official-paper-questions/0.1",
        "relatedNoteIds": [],
        "questions": questions,
    }


# G-E3 census of record — generated from MULTI-SERIES-REPORT.json @ converter
# v0.10.0 (wave 12: 2019-06 1C recovered through the F41 OCR layer).
# (questions, parts, marks) per slice; a mismatch is a hard stop.
EXPECTED_CENSUS = {
    "1C": {
        "2019-06": (15, 64, 110),
        "2020-01": (10, 60, 110),
        "2020-11": (10, 64, 110),
        "2021-01": (11, 53, 110),
        "2021-06": (10, 54, 110),
        "2021-11": (11, 67, 110),
        "2022-01": (11, 65, 110),
        "2022-06": (10, 57, 110),
        "2023-01": (12, 60, 110),
        "2023-06": (10, 55, 110),
        "2023-11": (10, 66, 110),
        "2024-06": (10, 56, 110),
        "2024-11": (11, 56, 110),
        "2025-06": (10, 49, 110),
        "2025-11": (10, 59, 110),
        "2026-06": (9, 56, 110),
    },
    "2C": {
        "2019-06": (8, 39, 70),
        "2020-01": (7, 39, 70),
        "2020-11": (7, 35, 70),
        "2021-01": (7, 39, 70),
        "2021-06": (7, 43, 70),
        "2021-11": (7, 41, 70),
        "2022-01": (7, 41, 70),
        "2022-06": (7, 39, 70),
        "2023-01": (7, 37, 70),
        "2023-06": (7, 41, 70),
        "2023-11": (7, 37, 70),
        "2024-06": (7, 37, 70),
        "2024-11": (7, 34, 70),
        "2025-06": (6, 38, 70),
        "2025-11": (6, 31, 70),
        "2026-06": (6, 36, 70),
    },
    # 1CR tranche (converter v0.12.0 corpus; MULTI-SERIES-REPORT of record):
    # (questions, parts, marks) — every set carries its printed 110/110.
    "1CR": {
        "2019-06": (10, 55, 110),
        "2020-01": (11, 59, 110),
        "2020-11": (10, 63, 110),
        "2021-01": (10, 58, 110),
        "2022-01": (11, 59, 110),
        "2022-06": (11, 57, 110),
        "2023-01": (10, 57, 110),
        "2023-06": (11, 59, 110),
        "2024-06": (12, 57, 110),
        "2025-06": (11, 55, 110),
        "2026-06": (11, 57, 110),
    },
    # 2CR tranche (converter v0.13.0 corpus; MULTI-SERIES-REPORT of record):
    # (questions, parts, marks) — every set carries its printed 70/70.
    "2CR": {
        "2019-06": (7, 40, 70),
        "2020-01": (7, 38, 70),
        "2020-11": (7, 36, 70),
        "2021-01": (8, 45, 70),
        "2022-01": (7, 35, 70),
        "2022-06": (7, 40, 70),
        "2023-01": (8, 40, 70),
        "2023-06": (7, 38, 70),
        "2024-06": (7, 38, 70),
        "2025-06": (7, 38, 70),
        "2026-06": (7, 35, 70),
    },
}

ALL_SERIES = ["2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
              "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
              "2024-11", "2025-06", "2025-11", "2026-06"]
# F-178 R-VARIANT tranche 1 (footer-verified 22/22, tracker PR #32): the 1CR
# paper exists for exactly these 11 of the 16 series (2021-06/2021-11/2023-11/
# 2024-11/2025-11 never printed a 1CR; 2020-06 never ran at all — COVID).
R1CR_SERIES = ["2019-06", "2020-01", "2020-11", "2021-01", "2022-01", "2022-06",
               "2023-01", "2023-06", "2024-06", "2025-06", "2026-06"]
PAPER_SERIES = {"1C": ALL_SERIES, "2C": ALL_SERIES,
                "1CR": R1CR_SERIES, "2CR": R1CR_SERIES}   # same 11 series print 2CR
PAPERS = tuple(PAPER_SERIES)   # both F-178 R-variant tranches now convert


class ExportGateError(Exception):
    pass


def census(s):
    nq = len(s["questions"])
    nps = sum(len(q["parts"]) for q in s["questions"])
    mk = sum(p["marks"] for q in s["questions"] for p in q["parts"])
    return nq, nps, mk


def is_official(t):
    """F44: official sets are identified by their slug prefix, never by
    topicSlug (which is the set's own slug since the per-paper namespace
    law) — the old topicSlug=='official-past-papers' filter silently
    selected zero sets after that law landed."""
    return t.get("slug", "").startswith(OFFICIAL_SLUG_PREFIX)


# G-E1b: set-level identity fields — a law, not a wave artifact (F44). The
# part census cannot see these; the topicSlug namespace drift rode exactly
# this blind spot. Any drift fails with no disclosure path: a real namespace
# change must land in the exporter of record and the bundle in the same
# reviewed PR.
IDENTITY_FIELDS = ("topicId", "slug", "name", "setName", "topicSlug",
                   "section", "sectionSlug", "curriculum", "source",
                   "schema", "relatedNoteIds")


def part_map(s):
    return {p["id"]: p for q in s["questions"] for p in q["parts"]}


# F51 (exporter v4): the data-cut law. The hub manifest's importSource.ref is
# the pin the v2 per-course pin law serves — PIN-TIGHTEN-1 (v2 fc7a5dc2) proved
# the wrinkle class: the ref once named the exporter-of-record commit (F44's
# landing bf8d56c3) while the run actually consumed a later cut (855cddcf).
# The exporter now stamps the DECLARED data cut and proves the consumed staging
# copies ARE that cut, fail-closed, no disclosure path (identity is a law — the
# G-E1b precedent). Content-identity modulo the converter header:
# generated_utc/generator are the converter's own identity (its version law),
# not the data cut's; the data plane must match canonicalized byte-exact.
SOURCE_CUT_RE = re.compile(r"^main@[0-9a-f]{40}$")
CUT_VOLATILE_HEADER = ("generated_utc", "generator")


def parse_source_cut(value):
    if not SOURCE_CUT_RE.match(value or ""):
        raise ValueError(
            f"--source-cut must be main@<40-hex commit sha> (got {value!r}) — "
            f"the declared data cut is the resources commit whose corpus the run consumes")
    return value


def _cut_topic_bytes(source_cut, rel_path):
    # the pin of record is 'main@<40-hex>' (manifest form); git wants the bare
    # rev — 'main@<hex>' is not valid rev syntax (the '@' would start a reflog
    # expression), so translate before handing it to git.
    rev = source_cut.split("@", 1)[1] if "@" in source_cut else source_cut
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "show", f"{rev}:{rel_path}"],
        capture_output=True)
    if proc.returncode != 0:
        raise ExportGateError(
            f"G-E5: cannot read {rel_path} at the declared data cut {source_cut} "
            f"(git show failed: {proc.stderr.decode(errors='replace').strip()[:200]})")
    return proc.stdout


def _topic_data_plane(raw_bytes):
    d = json.loads(raw_bytes)
    return {k: v for k, v in d.items() if k not in CUT_VOLATILE_HEADER}


def verify_source_cut(topics_dir, source_cut):
    """G-E5: every consumed staging topics file must BE the declared data cut.
    Content-identity vs <cut>:Official-ExamQuestion/.../topic.json modulo the
    converter header. Fail-closed, no disclosure path — a runner whose staging
    copies are not the declared cut must re-stage or declare the cut the copies
    actually are; it can no longer stamp a pin the data cannot prove."""
    checked = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            staged_path = os.path.join(topics_dir, f"{series}-{paper}.json")
            if not os.path.exists(staged_path):
                raise ExportGateError(
                    f"G-E5: staging topics file missing for {series}/{paper}: "
                    f"{staged_path} (stage the declared cut's corpus topics first)")
            staged = _topic_data_plane(open(staged_path, "rb").read())
            rel = (f"Official-ExamQuestion/{LANES[LANE_SPEC]['lane']}/{series}/"
                   f"{LANES[LANE_SPEC]['code']}-{paper}/topic.json")
            at_cut = _topic_data_plane(_cut_topic_bytes(source_cut, rel))
            if json.dumps(staged, sort_keys=True) != json.dumps(at_cut, sort_keys=True):
                raise ExportGateError(
                    f"G-E5: staging topics for {series}/{paper} are NOT the declared "
                    f"data cut {source_cut} (content drift beyond the converter header; "
                    f"re-stage from {source_cut} or declare the cut the copies are)")
            checked += 1
    print(f"G-E5 ok: {checked}/{checked} staging topics content-identical to the "
          f"declared data cut {source_cut} (modulo the converter header)")



def g_e7_group_stem_law(out_sets, topics_src, stem_ledger):
    """G-E7 (F121): the group-stem plane law. Every question-group intro of
    the corpus of record must reach the served set on the group's FIRST part
    (cleaned per the STEM-RESTORE group verdicts); a group stem can never
    vanish, be invented, or be attached to the wrong part; group ledger keys
    must resolve slice-scoped (the F113 unconsumed-key law) and their
    adjudicated cuts must actually cut (the cut tail must not survive into
    the served problemMd — fail-visible in both directions). Returns the
    accounting dict; raises ExportGateError on any violation."""
    g_stats = {"groups": 0, "served": 0, "splice": 0, "cuts": 0, "keys": 0,
               "part_cuts": 0, "part_keys": 0}
    g_keys_seen = set()
    p_keys_seen = set()
    normsp = lambda s: re.sub(r"\s+", " ", s or "").strip()
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            topic = topics_src(series, paper)
            slug = f"{LANES[LANE_SPEC]['prefix']}{paper.lower()}-{series}"
            served = next(t for t in out_sets if t["slug"] == slug)
            served_by_qid = {q["id"]: q for q in served["questions"]}
            for q in topic["questions"]:
                qnum = str(q["question_number"])
                sq = served_by_qid.get(
                    f"offq_{series}_{paper.lower()}_{part_slug(qnum)}")
                if sq is None:
                    raise ExportGateError(f"G-E7: {slug} lost question {qnum}")
                for letter, g in (q.get("groups") or {}).items():
                    gs_raw = (g.get("group_stem_md") or "").strip()
                    gkey = f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:Q{qnum}.{letter}"
                    g_entry = (stem_ledger or {}).get("verdicts", {}).get(gkey)
                    if g_entry:
                        g_keys_seen.add(gkey)
                    fp = next((p for p in q["parts"]
                               if group_letter_of(p["part_number"]) == letter), None)
                    if fp is None:
                        if gs_raw or g_entry:
                            raise ExportGateError(
                                f"G-E7: {gkey} has a stem/ledger entry but no "
                                f"part resolves to the group")
                        continue
                    if not gs_raw:
                        continue
                    g_stats["groups"] += 1
                    gmd = restore_group_stem(
                        g, series, paper, qnum, letter, stem_ledger or {},
                        fp.get("problem_md"))
                    target_id = (f"offp_{series}_{paper.lower()}_"
                                 + part_slug(fp["part_number"]))
                    sp = next((x for x in sq["parts"] if x["id"] == target_id), None)
                    if sp is None:
                        raise ExportGateError(
                            f"G-E7: {slug} lost the group-first part {target_id}")
                    if gmd is None:
                        # splice-guard: the converter folded the stem into the
                        # part text — the raw head MUST still be present
                        g_stats["splice"] += 1
                    head = normsp(gmd if gmd else gs_raw)[:60]
                    if head and head not in normsp(sp["problemMd"]):
                        raise ExportGateError(
                            f"G-E7: group stem of {gkey} is not served on the "
                            f"group's first part {target_id}")
                    if gmd:
                        g_stats["served"] += 1
                    # cuts applied: the RAW (soup-carrying) stem must never
                    # reach the served bytes — the cleaned form only. (Scoping
                    # the check to the stem rather than the whole problemMd:
                    # a part's own pre-existing text may legitimately repeat
                    # soup tokens, e.g. the F94 drawing-option letter runs.)
                    had_cut = bool(g_entry and (g_entry.get("tail")
                                                or g_entry.get("dropTail")
                                                or g_entry.get("dropSpan")))
                    if had_cut and normsp(gs_raw) in normsp(sp["problemMd"]):
                        raise ExportGateError(
                            f"G-E7: the adjudicated cut of {gkey} was not "
                            f"applied — the raw soup-carrying stem survives "
                            f"verbatim in the served problemMd")
                    if g_entry and (g_entry.get("tail") or g_entry.get("dropTail")
                                    or g_entry.get("dropSpan")):
                        g_stats["cuts"] += 1
                # ---- F125: the part-level plane law — ledger verdicts over a
                # part's OWN problem_md (the F123 residual class). Consumed
                # slice-scoped (the F113 law); served_by must be a crop asset
                # OF THE PART (the wave-19/20 cut law, machine-checked); the
                # cut must actually cut (the raw soup-carrying part text must
                # never reach the served bytes) and the cleaned head must be
                # served on the part itself.
                for p in q["parts"]:
                    pk = part_ledger_key(qnum, p["part_number"])
                    if pk is None:
                        continue
                    pkey = f"{series}/{LANES[LANE_SPEC]['code']}-{paper}:{pk}"
                    p_entry = (stem_ledger or {}).get("verdicts", {}).get(pkey)
                    if not p_entry:
                        continue
                    p_keys_seen.add(pkey)
                    target_id = (f"offp_{series}_{paper.lower()}_"
                                 + part_slug(p["part_number"]))
                    sp = next((x for x in sq["parts"] if x["id"] == target_id), None)
                    if sp is None:
                        raise ExportGateError(
                            f"G-E7: {slug} lost the ledgered part {target_id}")
                    sb = p_entry.get("served_by")
                    pa = next((a for a in (p.get("assets") or [])
                               if a.get("id") == sb), None)
                    if pa is None or pa.get("kind") != "crop":
                        raise ExportGateError(
                            f"G-E7: the part-level cut of {pkey} names served_by "
                            f"{sb!r} which is not a crop asset of the part "
                            f"(a cut removes only what a crop of record serves)")
                    raw_md = (p.get("problem_md") or "").strip()
                    cleaned = apply_part_cut(raw_md, p_entry, pkey)
                    if normsp(raw_md) and normsp(raw_md) in normsp(sp["problemMd"]):
                        raise ExportGateError(
                            f"G-E7: the adjudicated part cut of {pkey} was not "
                            f"applied — the raw soup-carrying part text survives "
                            f"verbatim in the served problemMd")
                    head = normsp(cleaned)[:60]
                    if head and head not in normsp(sp["problemMd"]):
                        raise ExportGateError(
                            f"G-E7: the cleaned part text of {pkey} is not served "
                            f"on the part {target_id}")
                    if p_entry.get("dropTail") or p_entry.get("dropSpan"):
                        g_stats["part_cuts"] += 1
    lane_code = LANES[LANE_SPEC]["code"]
    hosted = {s for paper in PAPERS for s in PAPER_SERIES[paper]}
    stale = sorted(
        k for k in (stem_ledger or {}).get("verdicts", {})
        if "." in k.split(":")[-1]
        and f"/{lane_code}-" in k
        and k.split("/")[0] in hosted
        and k not in g_keys_seen
        and k not in p_keys_seen)
    if stale:
        raise ExportGateError(
            f"G-E7: {len(stale)} group ledger key(s) never resolved for this lane "
            f"(stale or misnamed — the F113 unconsumed-key law): {stale[:4]}")
    g_stats["keys"] = len(g_keys_seen)
    g_stats["part_keys"] = len(p_keys_seen)
    return g_stats


def run_gates(out_sets, raw_sme_bytes, raw_official_bytes, expected_deltas_path, topics_src, allow_new_official=False, stem_ledger=None, enrich=None):
    """G-E1..G-E4 against the two-file bundle of record (raw_sme_bytes = the
    SME-only questions.json, raw_official_bytes = official-papers.json).
    topics_src(series, paper) -> topic dict.
    allow_new_official: a legitimate append wave may add official sets absent from
    the official-papers.json of record — their full part ids are disclosed in the
    'new' census class (the exporter refuses silently-dropped new sets either way)."""
    by_slug = {t.get("slug"): t for t in json.loads(raw_official_bytes)}
    # ---- G-E3: census constants (cheap, run first) ----
    n_slices = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            s = next(t for t in out_sets if t["slug"] == f"{LANES[LANE_SPEC]['prefix']}{paper.lower()}-{series}")
            c = census(s)
            exp = EXPECTED_CENSUS[paper][series]
            if c != exp:
                raise ExportGateError(f"G-E3 {series}/{paper}: census {c} != expected {exp}")
            n_slices += 1
    print(f"G-E3 ok: {n_slices} slices match the MULTI-SERIES constants of record "
          f"({sum(census(t)[2] for t in out_sets if is_official(t))} marks)")
    # ---- G-E2: sum laws ----
    for t in out_sets:
        if not is_official(t):
            continue
        for q in t["questions"]:
            if sum(p["marks"] for p in q["parts"]) != q["totalMarks"]:
                raise ExportGateError(f"G-E2 part-sum violation in {t['slug']} {q['id']}")
            for p in q["parts"]:
                msum = sum(m["marks"] for m in (p.get("markPoints") or []))
                if p.get("markPoints") and msum != p["marks"]:
                    raise ExportGateError(f"G-E2 markPoints sum {msum} != {p['marks']} at {p['id']}")
                if not all(isinstance(c, str) for c in (p.get("specPointCodes") or [])):
                    raise ExportGateError(f"G-E2 spec codes not strings at {p['id']}")
    print("G-E2 ok: part-sum, markPoints sum-law and spec-code shapes hold on all official sets")
    # ---- G-E1: regenerate vs bundle of record ----
    census_rows = {"new": {}, "gone": {}, "changed": {}}
    ident_drift = []
    n_common = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            slug = f"{LANES[LANE_SPEC]['prefix']}{paper.lower()}-{series}"
            rebuilt = export_series(series, paper, topics_src(series, paper), stem_ledger, enrich)
            of_record = by_slug.get(slug)
            if of_record is None:
                if not allow_new_official:
                    raise ExportGateError(
                        f"G-E1: bundle of record lacks {slug} (an append wave must run "
                        f"with --allow-new-official and disclose its census)")
                census_rows["new"][slug] = sorted(p["id"] for q in rebuilt["questions"] for p in q["parts"])
                continue
            n_common += 1
            for f in IDENTITY_FIELDS:
                if json.dumps(rebuilt.get(f), sort_keys=True) != json.dumps(of_record.get(f), sort_keys=True):
                    ident_drift.append(f"{slug}: {f}")
            rp, op = part_map(rebuilt), part_map(of_record)
            new_ids = sorted(set(rp) - set(op))
            gone_ids = sorted(set(op) - set(rp))
            changed = sorted(pid for pid in set(rp) & set(op)
                             if json.dumps(rp[pid], sort_keys=True) != json.dumps(op[pid], sort_keys=True))
            if new_ids:
                census_rows["new"].setdefault(slug, []).extend(new_ids)
            if gone_ids:
                census_rows["gone"].setdefault(slug, []).extend(gone_ids)
            if changed:
                census_rows["changed"].setdefault(slug, []).extend(changed)
    flat = {k: {s: v for s, v in d.items() if v} for k, d in census_rows.items()}
    n_delta = sum(len(v) for d in flat.values() for v in d.values())
    # wave-19 rename-wave shape: a disclosure carrying idRenames explains an
    # id-identity wave — gone ids must BE the map's keys, new ids its values,
    # and the content census (keyed by the NEW ids, id key excluded) must equal
    # the disclosure's 'changed'. One disclosure of record, both tools read it
    # (the CI hands the same file to the exporter and the verify harness).
    rename_ok = False
    if n_delta and expected_deltas_path:
        expected_probe = json.load(open(expected_deltas_path))
        if "idRenames" in expected_probe:
            rename_n = content_n = 0
            for paper in PAPERS:
                for series in PAPER_SERIES[paper]:
                    slug = f"{LANES[LANE_SPEC]['prefix']}{paper.lower()}-{series}"
                    rebuilt = export_series(series, paper, topics_src(series, paper), stem_ledger, enrich)
                    of_record = by_slug[slug]
                    smap = expected_probe["idRenames"].get(slug)
                    if not smap:
                        raise ExportGateError(f"G-E1: rename disclosure lacks {slug}")
                    qmap, pmap = smap.get("questions", {}), smap.get("parts", {})
                    for oq, rq in zip(of_record["questions"], rebuilt["questions"]):
                        if len(oq["parts"]) != len(rq["parts"]):
                            raise ExportGateError(f"G-E1: {slug} {oq['id']}: part count drift under a rename disclosure")
                        if qmap.get(oq["id"]) != rq["id"]:
                            raise ExportGateError(
                                f"G-E1: {slug}: question rename mismatch {oq['id']} -> {qmap.get(oq['id'])!r} "
                                f"(regenerated {rq['id']})")
                        for oprt, rprt in zip(oq["parts"], rq["parts"]):
                            if pmap.get(oprt["id"]) != rprt["id"]:
                                raise ExportGateError(
                                    f"G-E1: {slug}: part rename mismatch {oprt['id']} -> {pmap.get(oprt['id'])!r} "
                                    f"(regenerated {rprt['id']})")
                            rename_n += 1
                            ck = {k for k in (set(oprt) | set(rprt)) - {"id"}
                                  if json.dumps(oprt.get(k), sort_keys=True) != json.dumps(rprt.get(k), sort_keys=True)}
                            if ck:
                                content_n += 1
                                if rprt["id"] not in expected_probe.get("changed", {}).get(slug, []):
                                    raise ExportGateError(
                                        f"G-E1: content delta {slug} {rprt['id']} ({sorted(ck)}) "
                                        f"missing from the rename disclosure's 'changed' census")
            disc_changed_n = sum(len(v) for v in expected_probe.get("changed", {}).values())
            if content_n != disc_changed_n:
                raise ExportGateError(
                    f"G-E1: rename-disclosure content census {disc_changed_n} != fresh {content_n} "
                    f"(regenerate the disclosure only after eyeballing every class)")
            print(f"G-E1 ok: rename disclosure verified — {rename_n} ids renamed, "
                  f"{content_n} content deltas match the disclosed 'changed' census exactly")
            rename_ok = True
            n_delta = 0
    if n_delta == 0:
        if not rename_ok:
            print("G-E1 ok: regeneration is a byte-level no-op against the bundle of record")
    else:
        if not expected_deltas_path:
            for k in ("new", "gone", "changed"):
                for slug, ids in flat[k].items():
                    for pid in ids:
                        print(f"  DELTA {k}: {slug} {pid}")
            raise ExportGateError(
                f"G-E1: {n_delta} deltas vs the bundle of record with no --expected-deltas "
                f"census (the reproducibility law: an exporter of record run against its own "
                f"bundle must be a no-op; a content wave must disclose its census)")
        expected = json.load(open(expected_deltas_path))
        if json.dumps(flat, sort_keys=True) != json.dumps(expected, sort_keys=True):
            raise ExportGateError("G-E1: delta census != --expected-deltas (the printed "
                                  "DELTA listing above shows the fresh census; regenerate "
                                  "the disclosure file only after eyeballing every class)")
        print(f"G-E1 ok: {n_delta} deltas match the disclosed wave census exactly")
    if ident_drift:
        for d in ident_drift:
            print(f"  IDENTITY DRIFT {d}")
        raise ExportGateError("G-E1b: set-level identity drift vs the bundle of record "
                              "(identity fields are a law, not a wave artifact — a real "
                              "namespace change must land in the exporter of record and the "
                              "bundle in the same reviewed PR)")
    print(f"G-E1b ok: set-level identity fields byte-equal on all {n_common} common official sets")
    # ---- G-E6: the printed part label is a first-class field (F119) ----
    # Identity is a law, not a wave artifact (the G-E1b precedent) — the
    # emitted label and the part id derive from the same corpus part_number,
    # so any disagreement here is an exporter bug and fails closed in BOTH
    # directions (a vanished label and an invented one). The check itself is
    # g_e6_label_law() (unit-batteried, scripts/official_examq_f119_tests.py).
    label_census = {}
    for t in out_sets:
        if not is_official(t):
            continue
        for q in t["questions"]:
            g_e6_label_law(q["parts"], label_census)
    print("G-E6 ok: questionPart == the id-derived printed label on all official "
          f"parts ({label_census.get(1, 0)} one-level, {label_census.get(2, 0)} "
          f"two-level, {label_census.get(3, 0)} three-level, "
          f"{label_census.get(0, 0)} path-less/null)")
    # ---- G-E4: the SME corpus of record is never touched ----
    # Two-file law (v2 IA 662654ade0): the staged questions.json must be a
    # byte-identical passthrough of the SME bundle of record — proven on the
    # WHOLE file (since the split the SME file IS the whole questions.json).
    # The official rebuild's parity is G-E1's law (census + identity fields);
    # its bytes may legitimately drift inside a disclosed content wave.
    sme_sets = [t for t in out_sets if not is_official(t)]
    out_q_bytes = json.dumps(sme_sets, indent=1, ensure_ascii=False).encode()
    if out_q_bytes != raw_sme_bytes:
        n = min(len(out_q_bytes), len(raw_sme_bytes))
        for i in range(n):
            if out_q_bytes[i] != raw_sme_bytes[i]:
                raise ExportGateError(
                    f"G-E4: staged questions.json diverges from the SME bundle of "
                    f"record at byte {i}: "
                    f"{raw_sme_bytes[max(0, i - 60):i + 60]!r} vs "
                    f"{out_q_bytes[max(0, i - 60):i + 60]!r}")
        raise ExportGateError(
            f"G-E4: staged questions.json length drift vs the SME bundle of record "
            f"(of record {len(raw_sme_bytes)} bytes vs staged {len(out_q_bytes)} bytes)")
    print(f"G-E4 ok: questions.json byte-identical passthrough ({len(raw_sme_bytes)} bytes, "
          f"{len(sme_sets)} SME sets)")
    # ---- G-E7: the group stem is a first-class serving plane law (F121) ----
    # The check itself is g_e7_group_stem_law() (unit-batteried,
    # scripts/official_examq_f121_tests.py).
    g_stats = g_e7_group_stem_law(out_sets, topics_src, stem_ledger)
    print(f"G-E7 ok: {g_stats['groups']} group stems accounted for "
          f"({g_stats['served']} restored to their group's first part, "
          f"{g_stats['splice']} splice-guarded, {g_stats['cuts']} adjudicated cuts "
          f"applied; {g_stats['keys']} group ledger keys consumed; "
          f"{g_stats['part_cuts']} part-level cuts applied on "
          f"{g_stats['part_keys']} part ledger keys)")






def _manifest_note_text():
    """Task 22: the lane-aware note of record. Chemistry returns None (the
    chemistry note above stays the per-wave hardcode of record, byte-safe);
    physics returns the bootstrap note (LANES["4ph1"]["manifest_note"])."""
    return LANES[LANE_SPEC].get("manifest_note")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("out_stage")
    ap.add_argument("current_questions")
    ap.add_argument("--current-official-papers", required=True,
                    help="official-papers.json of record (the Past Papers plane, 54 "
                         "official sets) — the split sibling of the SME-only "
                         "questions.json (v2 IA decision 662654ade0)")
    ap.add_argument("--topics-dir", default=None,
                    help="dir holding <series>-<paper>.json staging copies of the corpus topics")
    ap.add_argument("--expected-deltas", default=None,
                    help="disclosed delta census for a content wave (default: zero deltas)")
    ap.add_argument("--allow-new-official", action="store_true",
                    help="append wave: official sets absent from the bundle of record are "
                         "disclosed in the 'new' census class instead of refusing")
    ap.add_argument("--manifest", default=None,
                    help="manifest.json beside the bundle of record; staged with bumped note")
    ap.add_argument("--spec", default="4ch1", choices=sorted(LANES),
                    help="corpus lane (Task 22): 4ch1 (default, byte-identical) | 4ph1")
    ap.add_argument("--source-cut", default=None,
                    help="the data cut this run consumes, main@<40-hex> (F51: REQUIRED "
                         "with --manifest — stamped into importSource.ref and proven by "
                         "G-E5 against the staging copies)")
    args = ap.parse_args()
    apply_lane(args.spec)
    topics_dir = args.topics_dir or os.path.join(os.getcwd(), "topics")
    source_cut = None
    if args.manifest and not args.source_cut:
        ap.error("--source-cut main@<40-hex> is REQUIRED with --manifest (F51: the "
                 "manifest's importSource.ref must name the data cut the run consumes "
                 "— 'importSource.ref stays' is retired; see v2 PIN-TIGHTEN-1)")
    if args.source_cut and not args.manifest:
        ap.error("--source-cut is only meaningful with --manifest (it stamps importSource.ref)")
    if args.source_cut:
        try:
            source_cut = parse_source_cut(args.source_cut)
        except ValueError as exc:
            ap.error(str(exc))
        verify_source_cut(topics_dir, source_cut)

    def topics_src(series, paper):
        return json.load(open(os.path.join(topics_dir, f"{series}-{paper}.json")))

    raw = open(args.current_questions, "rb").read()
    hub = json.loads(raw)
    leaked = [t.get("slug") for t in hub if is_official(t)]
    if leaked:
        raise ExportGateError(
            f"input law: questions.json of record still carries {len(leaked)} official "
            f"set(s) (e.g. {leaked[:3]}) — since the two-file split (v2 IA 662654ade0) "
            f"official sets live in official-papers.json; pass that file via "
            f"--current-official-papers")
    kept = hub
    raw_op = open(args.current_official_papers, "rb").read()
    of_strays = [t.get("slug") for t in json.loads(raw_op) if not is_official(t)]
    if of_strays:
        raise ExportGateError(
            f"input law: official-papers.json of record carries non-official set(s) "
            f"(e.g. {of_strays[:3]}) — it must hold ONLY official sets")
    stem_ledger = load_stem_ledger()
    enrich = load_enrichment_ledger()
    official = [export_series(s, paper, topics_src(s, paper), stem_ledger, enrich)
                for paper in PAPERS for s in PAPER_SERIES[paper]]
    out = kept + official

    run_gates(out, raw, raw_op, args.expected_deltas, topics_src, args.allow_new_official,
              stem_ledger, enrich)

    dest = os.path.join(args.out_stage, "content", LANES[LANE_SPEC]["lane"])
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "questions.json"), "wb") as f:
        f.write(json.dumps(kept, indent=1, ensure_ascii=False).encode())
    with open(os.path.join(dest, "official-papers.json"), "wb") as f:
        f.write(json.dumps(official, indent=1, ensure_ascii=False).encode())
    n_sets = len(official)
    n_q = sum(len(t["questions"]) for t in official)
    n_p = sum(len(q["parts"]) for t in official for q in t["questions"])
    n_mp = sum(len(p["markPoints"]) for t in official for q in t["questions"] for p in q["parts"])
    n_fig = sum(1 for t in official for q in t["questions"] for p in q["parts"]
                for a in p["assets"] if a["kind"] == "crop")
    n_stub = sum(1 for t in official for q in t["questions"] for p in q["parts"]
                 for a in p["assets"] if a["kind"] == "crop-required")
    print(f"sets: {len(kept)} SME kept + {n_sets} official | questions: {n_q} | parts: {n_p} "
          f"| markPoints: {n_mp} | figure crops: {n_fig} | honest stubs: {n_stub}")
    if args.manifest and os.path.exists(args.manifest):
        manifest = json.load(open(args.manifest))
        official_n = sum(1 for t in out if is_official(t))
        # F51: the pin law — the staged manifest names the data cut the run
        # consumed (G-E5-proven above), never a stale or tool-identity ref.
        manifest["importSource"]["ref"] = source_cut
        manifest["importSource"]["note"] = _manifest_note_text() or _CHEM_F125_NOTE_HEAD
        os.makedirs(args.out_stage, exist_ok=True)
        with open(os.path.join(args.out_stage, "manifest.json"), "wb") as f:
            f.write(json.dumps(manifest, indent=1, ensure_ascii=False).encode())
        print(f"manifest staged (importSource.ref stamped to the declared data cut "
              f"{source_cut} — G-E5-proven; note text is the per-wave hardcode of "
              f"record: bump it in the same reviewed PR as the wave)")
    print(f"written: {dest}/questions.json + {dest}/official-papers.json")


if __name__ == "__main__":
    main()
