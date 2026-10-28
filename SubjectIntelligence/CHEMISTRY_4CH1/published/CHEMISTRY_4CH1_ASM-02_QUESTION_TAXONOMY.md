---
sib_protocol: SIB-1.0
artifact_id: ASM-02
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: assessment_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: true
  mark_schemes: true
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-29

provenance:
  source_manifest: "SRC-QPMS-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-019"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "e4c1960be234beb0406b9218f4fbb2a95b1e3f28"
    syllabai_resources: "e3d648a195a13e3713b4b14a3095518e4a0d24e5"
---

# ASM-02 — Question Taxonomy

## Purpose

This artifact classifies the question types that appear on the 4CH1 examination papers
as parsed in the official exam corpus of record (SRC-QPMS-4CH1). It is the second
artifact of the Assessment Intelligence (ASM) family, grounded on the paper corpus
itself rather than on the specification's description of question styles. Every
item-class claim is carried on bounded, locator-addressed excerpts from the run's
evidence pack, and the classification is observational: it names the item forms the
papers actually use, with one worked anchor per class. This is a research artifact for
teaching and revision design; it writes nothing to the canonical assessment planes.

## Scope

**Covers:** the item classes observable in the parsed papers — four-option
multiple-choice items; structured short-answer items; two-point linked explanations;
calculation items; equation construction/completion items; and the grading annotations
that ride inside the parsed mark-scheme text.

**Grounding:** SRC-QPMS-4CH1 (official paper extractions with embedded mark-scheme
text, schema syllabai.official-paper-questions/0.2).

**Out of scope:** mark-allocation statistics (ASM-05), difficulty (ASM-06), examiner
sentiment (EXM family — the forbidden substitution).

## Executive Summary

The 4CH1 papers mix a small, stable set of item classes. Four-option multiple-choice
items (A–D, single response, marked with a tick in the parsed corpus) open most
questions; structured short-answer items dominate the remainder, tagged per part with
a bracketed mark tariff; two-mark items are frequently two-point linked explanations
whose mark scheme names M1/M2 explicitly; calculations appear as "show that" tasks
anchored to a printed answer; and chemistry equations are tested by completion or
full construction. The parsed mark-scheme text carries its own grading annotations
(ACCEPT/ALLOW/IGNORE/REJECT) that make the corpus self-describing for later MS-family
analysis.

## Main Analysis

### ASM-007 — Four-option multiple-choice items

**Claim:** the papers use four-option single-response multiple-choice items labelled
(A)–(D), with the correct option marked by a tick in the parsed corpus.
**Evidence:** a Paper 1 opening item asks "Which statement explains this observation?"
with options "- **(A)** the crystal condenses in the water" through (D)
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 9-23), and its sibling item marks
the correct row with a tick: "- **(A)** all of the liquid is purple ✔"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 28-42).
**Taxonomy note:** MCQs carry a 1-mark tariff inside the question body (the embedded
mark scheme reads "- **(1)** Answer B: the crystal dissolves in the water",
SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 49-63), so the class is diagnostic
of AO1 recall at fixed tariff.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-008 — Structured short-answer items with per-part tariffs

**Claim:** the dominant item class is structured short-answer, split into lettered
parts whose headers carry the part tariff in square brackets.
**Evidence:** part headers appear throughout the parsed papers, e.g. "### 1(b)(i) [1]"
with the stem "Which statement describes the final appearance of the liquid?"
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 49-63) and "### 2(b) [1]" with
"State why they have similar chemical reactions." (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 111-125).
**Taxonomy note:** the bracketed tariff is visible in the question text itself, which
is what makes the corpus machine-auditable for the ASM-05 mark-allocation analysis.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-009 — Two-point linked explanations with M1/M2 marking

**Claim:** two-mark explanation items are frequently structured as linked two-point
arguments whose mark scheme names the points M1 and M2 explicitly.
**Evidence:** the mark-scheme text for a graphite-conductivity item reads "An
explanation that links together the following two points" with "M1 (graphite has)
delocalised electron(s)" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 512-526);
the same linked form governs a chromatography item (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 305-319) and an intermolecular-forces item
(SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 702-716).
**Taxonomy note:** this is the papers' signature reasoning class — candidates must
supply cause AND consequence, which is where partial credit structure becomes visible
(see MS-06).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-010 — Calculation items anchored to a printed answer

**Claim:** numerical work appears as "show that" calculations whose stem prints the
target answer, plus standard mole/percentage items, marked in working steps.
**Evidence:** an empirical-formula item reads "Show, by calculation, that the empirical
formula of this compound is CBrF3" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 655-669), and its mark scheme allocates M1 to the division step — "M1 C 8.05 ÷ 12 OR
0.671" — with M2 dependent (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 683-697).
**Taxonomy note:** the printed target makes method the assessed object; the
error-carried-forward allowance visible in the mark scheme ("ALLOW ECF from M1") is
the marking-side signature of this class ( analysed further in MS-07).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-011 — Equation construction and completion items

**Claim:** chemical equations are assessed both by completion (balancing a skeleton
equation) and by full construction from a described reaction.
**Evidence:** an organic item instructs "Complete the chemical equation for this
reaction" over the skeleton "C2H4 + HCl + O2 → C2H4Cl2 + H2O" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 567-581), and the ammonia synthesis item asks
"Give a chemical equation for this reaction" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 369-383).
**Taxonomy note:** both forms accept alternative correct multiples (the mark scheme
reads "ACCEPT multiples and" — SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines
579-593), a class-level marking property, not a per-item one.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-012 — Grading annotations riding inside the parsed items

**Claim:** the parsed mark-scheme text carries its own grading annotations —
ACCEPT/ALLOW for alternatives, IGNORE for non-penalised noise, REJECT for forbidden
answers — making the corpus self-describing for downstream mark-scheme analysis.
**Evidence:** "Li+ ALLOW Sr2+" on a flame-test ion item (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 165-179), "IGNORE Fe if added to both sides of the
equation" on the ammonia equation (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 369-383) and "REJECT elements for c" on the isomers definition (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 743-757).
**Boundary note:** these annotations are recorded here purely as item-class markers;
their mark-scheme semantics are the MS family's ground and are not analysed here.
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-064 — The plotted-point tolerance band

**Claim:** graph-plotting marks carry a printed spatial tolerance: every point must be plotted correctly to within half a square, the same envelope later reused for reading levelling-off values off the expected curves. The assessment thus fixes its graphical precision at the square-grid level and applies the envelope to both plotting and reading.
**Evidence:** the plot instruction is marked "all points plotted" "correctly to + or – half a square" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1003-1017), and the curve-reading point reuses it as "M2 levelling off at 42 cm3 to + or – half a square" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1031-1045).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-065 — The expected-curve drawing method with printed anchors

**Claim:** predicting a curve is marked against printed anchors: the scheme names the start point, the curve's position relative to the original, and the level-off volume each with its own mark — so the sketch method is specified as three checkable features rather than judged holistically. A second expected curve repeats the structure with its own anchor volume.
**Evidence:** the scheme prints "M1 curve Y starting at origin and below original" "curve" and "M2 levelling off at 42 cm3 to + or – half a square" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1031-1045); the higher-temperature curve prints "M1 curve Z starting at origin and above original" "curve" with "M2 levelling off at 84 cm3 to + or – half a square" and "ACCEPT curves" (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1047-1061).
Temporal scope: CURRENT — AUTHORITATIVE.

### ASM-066 — The any-one-from pool with per-branch ignore riders

**Claim:** the volume-deficit suggestion is marked as a pool — any one from two printed explanations — and each branch carries its own ignore rider policing unqualified wording: gas escaping unqualified is ignored, and the impurity branch ignores a bare mention of magnesium. The pool structure plus per-branch riders means the markable space is two named mechanisms, each with its own wording fence.
**Evidence:** the scheme prints "Any one from:" with "M1 some gas escapes before the bung is" "replaced/ before the syringe is connected" carrying the rider fragments "IGNORE gas" and "escapes unqualified", and "M2 the magnesium is impure/ the magnesium" "ribbon has an oxide coating" with its own ignore rider on a bare mention (SRC-QPMS-4CH1, 2019-06/4CH1-1C/questions.md lines 1068-1082).
Temporal scope: CURRENT — AUTHORITATIVE.


## Evidence / Source Basis

Primary evidence: SRC-QPMS-4CH1 (the official 4CH1 paper extractions of record — the
2019-06 4CH1/1C paper supplies the worked anchors, with the interleaved session spread
in the pack confirming the item classes recur across sessions). All excerpts are
bounded line-window excerpts with line locators preserved. The pack's supplementary
sources (SRC-TL-4CH1) were not consumed; no ER evidence was used (EXM family ground),
and no specimen material was cited.

## Limitations / Coverage Gaps

The worked anchors come principally from the 2019-06 1C paper of the pack; the class
inventory is observational and does not claim to enumerate every rare item form on
every session. Frequency statistics per class belong to ASM-05/ASM-09, not here. The
taxonomy names what the parsed corpus shows; it does not infer examiner intent
(that is EXM ground and would be the forbidden substitution if drawn from mark
schemes). No canonical assessment-identity plane was read or written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Deepened under SIB-CHEMISTRY_4CH1-RUN-019 (D3 tranche 3): +3 records (ASM-064..066), zero-append mining of the carried pack of record; every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations. Research artifact — evidence-backed, not canonical educational
truth.
