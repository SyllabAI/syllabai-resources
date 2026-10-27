---
sib_protocol: SIB-1.0
artifact_id: CUR-08
artifact_version: 1.2
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: curriculum_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: false
  question_papers: false
  mark_schemes: false
  examiner_reports: false
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-28

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-016"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "1cd1b417d41e6a0dad3bc7a1e0cbe9e2dd519027"
---

# CUR-08 — Curriculum Boundaries

## Purpose

This artifact is the boundary layer of the CHEMISTRY_4CH1 curriculum-intelligence
family: the exact edges of the qualification — what Paper 1 assesses versus Paper 2,
which content is shared with the Science Double Award and which is 4CH1-only, when the
qualification is available, how the assessment objectives partition the marks, where
the twelve Core Practicals sit inside the content, and which materials are specimen
references rather than session evidence. Every downstream family that routes content
to a learner or a question needs these boundaries stated once, machine-readably, with
honest disclosure of where the boundary evidence is thin. It is a research artifact
grounded on the run's evidence pack; the canonical planes remain authoritative and
read-only to this pipeline.

## Scope

**Covers:** the paper-content boundary (core versus all content, with the bold/'C'
depth rule); the Double Award sharing boundary as carried per statement in the
applicability blocks; the series and administration boundary (availability, first
assessment, the Issue 3 forbidden-combinations change); the assessment-objective
boundary (three AOs, overall and per-paper weightings, with the graph's on-record
repair note); the practical boundary (Core Practicals anchored inside content
subtopics); and the specimen-materials boundary (SAMs as identity reference, never
session evidence). Temporal scope is CURRENT — AUTHORITATIVE; no legacy material is
used or cited.

**Does not cover:** grade-boundary or marking behavior (ASM/MS/EXM families'
ground), teaching sequencing (PED), or the legacy 4CH0 qualification (HIS family's
ground, currently blocked on unresolved legacy sources).

## Executive Summary

- Paper 1 (4CH1/1C, shared code 4SD0/1C) assesses "core content that is not in bold
  and does not have a 'C' reference"; Paper 2 (4CH1/2C) assesses "all the content,
  including content that is in bold and has a 'C' reference"; bold statements "cover
  some sub-topics in greater depth" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p13) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p14).
- The sharing law is carried per statement: non-suffixed statements "are shared with
  Science Double Award 4SD0 and assessed in both Paper 1C and Paper 2C";
  C-suffixed statements are 2C-only and not Double-Award-shared (in-pack windows:
  14 of the 60 sampled applicability blocks are 2C-only; RUN-COMPUTED: census.json,
  specification_points.c_points).
- Both papers are available in November and June, first assessment June 2019; Issue 3
  added modular International GCSEs to the forbidden combinations (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p13) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3).
- The AO boundary is threefold — AO1 and AO2 at 38–42% each, AO3 at 19–21% overall —
  with the per-paper matrix carried in the validated graph and an on-record repair
  note anchoring it to PDF p35 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p35) (SRC-GRAPH-4CH1, graph/igcse-chemistry/assessment_objectives.yaml lines 44-58).

## Main Analysis

### CUR-044 — The paper-content boundary

The official statement of the boundary is two sentences long. Paper 1 "assesses core
content that is not in bold and does not have a 'C' reference. Questions may come from
any topic area across the specification" — and the content summary lists all four
topics as in-scope for it (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p13). Paper 2 "assesses all the content,
including content that is in bold and has a 'C' reference. Questions may come from any
topic area across the specification," with the depth rule explicit: "Bold statements
cover some sub-topics in greater depth" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p14). The boundary is
therefore asymmetric by design: Paper 1 is a strict subset rule (non-bold, non-C),
Paper 2 is the complement plus depth. The mark split carrying the two papers is 110
marks (2 hours) versus 70 marks (1 hour 15 minutes), weighting 61.1% / 38.9%
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p13) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p14). Downstream routing law: any
question, explanation or practice item keyed to a bold or C-suffixed statement is
Paper 2 territory by definition; a Paper 1-labeled item touching such a statement is a
boundary violation to flag, not a style choice.

### CUR-045 — The Double Award sharing boundary, carried per statement

The applicability blocks of the statement store carry the sharing law as data: for
non-suffixed statements, "non-suffixed statements are shared with Science Double Award
4SD0 and assessed in both Paper 1C and Paper 2C", with papers [1C, 2C] and
double_award_shared: true (SRC-GRAPH-4CH1, graph/igcse-chemistry/specification_points.yaml lines 51-65); (SRC-GRAPH-4CH1, graph/igcse-chemistry/specification_points.yaml lines 93-107); (SRC-GRAPH-4CH1, graph/igcse-chemistry/specification_points.yaml lines 141-155). C-suffixed statements instead carry papers [2C] and
double_award_shared: false — the pack's 60 sampled applicability windows include 14
such 2C-only blocks (SRC-GRAPH-4CH1, graph/igcse-chemistry/specification_points.yaml lines 225-239) — context; pack specification_points windows. The run census fixes the totals: 52 of the 182 statements are C-points
(RUN-COMPUTED: census.json, specification_points.total;
census.json, specification_points.c_points). The boundary consequence is double-keyed:
a C suffix simultaneously removes a statement from Paper 1 AND from the 4SD0 route —
two different curricula edges encoded in one character, which is why CUR-02 treats
the suffix as boundary law and this artifact records its machine-readable form.

### CUR-046 — The series and administration boundary

Both papers are externally assessed, available in November and June, first assessment
June 2019 (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p13) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p14). The Issue 3 changes
summary records the boundary's recent movement: "Availability of series amended to
November and June" (pages 7-8), and — administratively decisive — "Modular
International GCSEs added to forbidden combinations" (page 31 of the specification,
listed on the changes page) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3). For a course operating under
4CH1, the forbidden-combinations rule is a hard outer boundary: the qualification
cannot be combined with modular International GCSEs, and the of-record wording for
that rule lives at the cited page. The first-teaching/first-examination anchor is
confirmed independently by the specimen materials cover ("For first teaching September 2017 First examination June 2019") (SRC-SAMS-4CH1, international-gcse-Chemistry-2017-SAM.pdf p1).

### CUR-047 — The assessment-objective boundary

The official AO table sets the outer partition of marks: AO1 "Knowledge and
understanding of chemistry" 38–42%, AO2 "Application of knowledge and understanding,
analysis and evaluation of chemistry" 38–42%, AO3 "Experimental skills, analysis and
evaluation of data and methods in chemistry" 19–21%, summing to 100%
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p35). The validated graph carries the same three objectives with
the per-paper matrix — paper 1: AO1 23.2–25.7%, AO2 23.2–25.7%, AO3 11.6–12.8%; paper
2: AO1 14.8–16.3%, AO2 14.8–16.3%, AO3 7.4–8.2% — under validation_status
RULE_DERIVED, and carries an on-record repair note ("PDF p35 verified") documenting
that the shared weighting matrix was rebuilt after an ao1/ao2 column-copy defect
(SRC-GRAPH-4CH1, graph/igcse-chemistry/assessment_objectives.yaml lines 44-58); (SRC-GRAPH-4CH1, graph/igcse-chemistry/assessment_objectives.yaml lines 71-85). The boundary law: AO3's
envelope (roughly one fifth of the qualification, split across both papers) is the
structural guarantee that experimental skills are assessed in every series — which is
the assessment-side anchor for the practical boundary below.

### CUR-048 — The practical boundary: Core Practicals live inside the content

The practicals store anchors each Core Practical to its specification point and
subtopic: PR-01 at 1.7C (S1-a, solubility of a solid at a specific temperature); PR-02
at 1.13 (S1-b, paper chromatography using inks/food colourings); PR-03 at 1.36 (S1-e,
formula of a metal oxide by combustion or reduction); PR-04 at 1.60C (S1-i,
electrolysis of aqueous solutions) — each row carrying the summary, ordering,
validation status RULE_DERIVED and the PDF page anchor (SRC-GRAPH-4CH1, graph/igcse-chemistry/practicals.yaml lines 42-56); (SRC-GRAPH-4CH1, graph/igcse-chemistry/practicals.yaml lines 64-78); (SRC-GRAPH-4CH1, graph/igcse-chemistry/practicals.yaml lines 86-100); (SRC-GRAPH-4CH1, graph/igcse-chemistry/practicals.yaml lines 109-123). The boundary reading: the twelve Core Practicals are NOT a separate
assessment segment — they are embedded at content statements inside the four topics
(here, four of the first four practicals all sit inside S1), and the statement store
flags them with the machine-readable practical flag (CUR-02's exemplar 1.7C). Two
of the sampled practicals are C-suffixed statements (1.7C, 1.60C) — practical
mastery does not respect the core/extension boundary either, and Paper 2 carries the
C-suffixed practicals.

### CUR-049 — The content-coverage boundary: what the boundary itself changed

The specification's own change log is boundary evidence of record: Issue 3's changes
were narrow and administrative — availability amendment (November and June), the
modular forbidden-combinations addition, and one command-word taxonomy addition
("“Which” added to the command word taxonomy", page 46) (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3). The
content map itself stands as four topics with printed page starts 11/16/21/23
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15). The coverage claim this licenses is precise: the CURRENT
— AUTHORITATIVE content of 4CH1 is exactly the four-topic content section between
those page anchors plus the appendices the changes page lists; anything outside that
space (legacy 4CH0 wording, other boards' topic framings, unrelated IGCSE content)
is outside the boundary and must never be presented as 4CH1 curriculum truth. The
command-word addition also dates the taxonomy CUR-07 records: the 25-word taxonomy
of record is the Issue 3 taxonomy, and its "Which" entry is an Issue 3 artifact
— CUR-07's store census (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p3).

### CUR-050 — The specimen boundary: SAMs as reference, never session evidence

The SAMs booklet is the assessment-shape reference: cover-identified as "SAMPLE ASSESSMENT MATERIALS Pearson Edexcel International GCSE in Chemistry (4CH1) For first teaching September 2017 First examination June 2019 Issue 2"
(SRC-SAMS-4CH1, international-gcse-Chemistry-2017-SAM.pdf p1), with its own Issue 2 change note describing mark-scheme
supplements for specific questions (SRC-SAMS-4CH1, international-gcse-Chemistry-2017-SAM.pdf p3). The boundary law —
restated here because it is a boundary — is that specimen material demonstrates the
intended shape of assessment at first-award standard and is never citable as live
session evidence; the evidence policy's global forbidden list makes the same point
enforceably (citing specimen/SAM material as live-session evidence is a forbidden substitution). The Getting Started Guide occupies the adjacent support boundary: it
frames the planning-and-support package for centres (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p3) (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf p4) —
official and current, but guidance rather than assessable content. Downstream
families quoting paper behavior must draw session evidence from the QP/MS/ER corpus
of record, never from these reference shelves.

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (pages 3, 13, 14, 15, 35 as paginated in the evidence pack), sha1 of record
  3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph:
  specification_points.yaml (applicability blocks), assessment_objectives.yaml (AO
  store with per-paper matrix and repair note), practicals.yaml (Core Practical
  anchors), verified at run preflight. Read-only plane for this pipeline.
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — SAMs booklet pages
  1-3 as identity and boundary evidence; never cited as session evidence.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — Getting Started Guide
  (pages 3-4) as support-package context.
- **CURRENT — AUTHORITATIVE (supplementary, identity-only):** SRC-BOOK-4CH1-SB1 —
  present as identity row; no textbook-grain claim in this artifact.
- **RUN-COMPUTED:** census.json — deterministic counts over the graph stores of
  record; verified by the run's evidence-claim QA.

## Limitations / Coverage Gaps

- The full forbidden-combinations rule text lives at the cited specification page
  (31 per the changes list); this pack carries the changes-summary row, not the full
  administration section, so the rule is quoted at summary grain.
- The AO per-paper matrix is consumed from the validated graph (RULE_DERIVED with an
  on-record repair note); this artifact inherits the graph's verdict rather than
  re-deriving the matrix from the PDF.
- The practicals store is sampled at four of twelve practicals in-pack; the complete
  anchor list rests on the store of record and the census inputs.
- Grade boundaries, marking grids and series-level difficulty are outside this
  artifact entirely (ASM/MS/EXM ground).
- The Double Award (4SD0) specification itself is not a resolved source of this
  library; the sharing law is recorded as 4CH1's own declaration of it.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN batch run SIB-CHEMISTRY_4CH1-RUN-002 under the
provider-neutral pipeline (BL-008 wave 1, protocol §4 pass 2), grounded exclusively on
the run's CUR-08 evidence pack (pack sha256 of record in the run manifest) plus the
run's deterministic census annex. Current/legacy separation: fully CURRENT; no legacy
claims. Determinism: content fingerprint of this artifact is recorded in the run
manifest; regeneration produces a new artifact_version.
