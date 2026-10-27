---
sib_protocol: SIB-1.0
artifact_id: CUR-01
artifact_version: 1.1
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

# CUR-01 — Curriculum Overview

## Purpose

This artifact is the entry point of the CHEMISTRY_4CH1 curriculum-intelligence family: a
grounded overview of the Pearson Edexcel International GCSE in Chemistry (4CH1),
Issue 3, as a qualification and as an assessment object. It exists so that every later
SIB artifact, chunk and tutor interaction can inherit one consistent statement of what
this qualification is, how it is examined, and how its content is organised. It fixes
the vocabulary of the course (topic codes, subtopic codes, paper codes, practical codes)
against the operator's validated curriculum graph, and it states clearly which parts of
that vocabulary come from official wording and which come from the validated internal
plane. It is a research artifact, not canonical curriculum truth: the canonical planes
of SyllabAI remain authoritative (Subject Intelligence Build v1, §5).

## Scope

**Covers:** the qualification-level structure of 4CH1 (Issue 3): qualification identity
and aims, the two-paper assessment model and weightings, the assessment objectives and
their weightings, the four topic areas with their 28 subtopics, and the twelve Core
Practicals. Temporal scope is CURRENT — AUTHORITATIVE throughout: everything here is
grounded on the current specification (Issue 3) and current official teaching-and-learning
material. No legacy material is used or cited.

**Does not cover:** the wording of individual specification statements (that is
CUR-02 Specification Interpretation's ground), concept-level relationships (CUR-03/04),
prerequisite structure (CUR-05), or the assessment-detail families (ASM, MS, EXM). This
artifact names the structure; it does not interpret it.

## Executive Summary

- The Pearson Edexcel International GCSE in Chemistry (4CH1) is a linear, untiered
  qualification first taught September 2017, first examined June 2019, currently at
  specification Issue 3, assessed through two externally-assessed written papers.
- Paper 1 (4CH1/1C, shared code 4SD0/1C) is worth 61.1% of the International GCSE:
  2 hours, 110 marks, core content only (statements not in bold and without a 'C'
  reference). Paper 2 (4CH1/2C) is worth 38.9%: 1 hour 15 minutes, 70 marks, all content
  including the bold/'C' extension statements. Both papers are available in November
  and June.
- Three assessment objectives structure the assessment: AO1 and AO2 are each weighted
  38–42% overall, AO3 is weighted 19–21% overall; the validated graph carries the
  per-paper AO weighting matrix.
- Content is organised as four topics — 4CH1-S1 Principles of chemistry, 4CH1-S2
  Inorganic chemistry, 4CH1-S3 Physical chemistry, 4CH1-S4 Organic chemistry —
  subdivided into 28 subtopics (S1: 9, S2: 8, S3: 3, S4: 8), plus 12 Core Practicals
  (4CH1-PR-01 … 4CH1-PR-12) embedded at specific specification points.

## Main Analysis

### Qualification identity and position

The qualification is the Pearson Edexcel International GCSE in Chemistry, specification
code 4CH1, first teaching September 2017, first examination June 2019, Issue 3
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p1). The course introduction states it "is designed for use in
schools and colleges" and "is part of a suite of International GCSE qualifications
offered by Pearson" (spec p8/PDF). The suite diagram on the same page shows the
qualification's position: Chemistry Paper 1 + Chemistry Paper 2 (both untiered) lead to
the International GCSE in Chemistry, and the same paper pattern across the sciences
composes the International GCSE in Science (Double Award) — which is why the Paper 1
code is shared with 4SD0 (spec p8/PDF, p13/PDF). The official Getting Started Guide
(Issue 2, October 2024) presents the qualification overview and the support package for
planning and implementation (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf pp3-4).

The stated aims are that students should: learn about unifying patterns and themes in
chemistry and use them in new and changing situations; acquire knowledge and
understanding of chemical facts, terminology, concepts, principles and practical
techniques; apply the principles and concepts of chemistry, including those related to
the applications of chemistry, to different contexts; evaluate chemical information,
making judgements on the basis of this information; appreciate the practical nature of
chemistry, developing experimental and investigative skills based on correct and safe
laboratory techniques; and analyse, interpret and evaluate data and experimental methods,
drawing conclusions from experimental evidence (spec p9/PDF, verbatim bullets).

### Assessment model

The qualification comprises two externally-assessed papers (spec p13/PDF
"Qualification at a glance"):

| Paper | Code | Duration | Marks | Weighting | Content assessed |
|---|---|---|---|---|---|
| Chemistry Paper 1 | 4CH1/1C (and 4SD0/1C) | 2 hours | 110 | 61.1% | Core content only: statements not in bold and without a 'C' reference; questions may come from any topic area |
| Chemistry Paper 2 | 4CH1/2C | 1 hour 15 min | 70 | 38.9% | All content, including bold/'C' statements; bold statements cover some sub-topics in greater depth |

Both papers are untiered, available in November and June, with first assessment June
2019, and are "set and marked by Pearson" with "a mixture of different question styles,
including multiple-choice questions, short-answer questions, calculations and extended
writing questions" (spec pp13–14/PDF). The paper weighting split (61.1% / 38.9%) and the
paper content rule (core vs all content) are the load-bearing facts for every later
assessment-family artifact: any question drawn from a bold or 'C'-referenced statement
belongs to Paper 2 territory by definition.

### Assessment objectives

The validated curriculum graph (SRC-GRAPH-4CH1, assessment_objectives.yaml — wording
authority the official spec PDF, weightings extracted deterministically from the PDF
weighting tables) records three assessment objectives:

| AO | Title (verbatim from graph, wording authority spec PDF) | Weighting overall |
|---|---|---|
| 4CH1-AO1 | Knowledge and understanding of chemistry | 38–42% |
| 4CH1-AO2 | Application of knowledge and understanding, analysis and evaluation of chemistry | 38–42% |
| 4CH1-AO3 | Experimental skills, analysis and evaluation of data and methods in chemistry | 19–21% |

The graph also carries the per-paper weighting matrix (paper 1: AO1 23.2–25.7%,
AO2 23.2–25.7%, AO3 11.6–12.8%; paper 2: AO1 14.8–16.3%, AO2 14.8–16.3%, AO3
7.4–8.2%), with an on-record repair note that the shared weighting matrix was rebuilt
from the canonical unit weightings after an ao1/ao2 column-copy defect was found and
PDF p35 verified. The AO3 envelope (roughly one fifth of the qualification) is the
structural reason practical-grounded intelligence (PRA family) and examiner-reported
practical weakness (MIS/EXM families) matter at qualification scale.

### Content structure: topics and subtopics

The specification's chemistry content is organised in four topics (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p15); codes, titles and ordering follow the validated graph topics.yaml (SRC-GRAPH-4CH1, graph/igcse-chemistry/topics.yaml lines 42-56), whose titles and subsection headers are the canonical PDF-direct parse with ratified structure overlay:

- **4CH1-S1 Principles of chemistry** — 9 subtopics: S1-a States of matter; S1-b
  Elements, compounds and mixtures; S1-c Atomic structure; S1-d The Periodic Table;
  S1-e Chemical formulae, equations and calculations; S1-f Ionic bonding; S1-g
  Covalent bonding; S1-h Metallic bonding; S1-i Electrolysis.
- **4CH1-S2 Inorganic chemistry** — 8 subtopics: S2-a Group 1 (alkali metals) –
  lithium, sodium and potassium; S2-b Group 7 (halogens) – chlorine, bromine and
  iodine; S2-c Gases in the atmosphere; S2-d Reactivity series; S2-e Extraction and
  uses of metals; S2-f Acids, alkalis and titrations; S2-g Acids, bases and salt
  preparations; S2-h Chemical tests.
- **4CH1-S3 Physical chemistry** — 3 subtopics: S3-a Energetics; S3-b Rates of
  reaction; S3-c Reversible reactions and equilibria.
- **4CH1-S4 Organic chemistry** — 8 subtopics: S4-a Introduction; S4-b Crude oil;
  S4-c Alkanes; S4-d Alkenes; S4-e Alcohols; S4-f Carboxylic acids; S4-g Esters;
  S4-h Synthetic polymers.

That is 28 subtopics in total, matching the graph's own census (182 spec points,
52 'C' points, 4 topics, 28 subtopics, 12 practicals, 25 command words). S1 is the
largest and most load-bearing topic: it carries the language models (particles, atoms,
bonding, formulae) on which S2–S4 draw.

### Core Practicals

Twelve Core Practicals are embedded at specific specification points (SRC-GRAPH-4CH1,
practicals.yaml, summaries verbatim from the canonical PDF-direct parse): PR-01
investigate the solubility of a solid in water at a specific temperature (at
specification point 1.7C); PR-02 investigate paper chromatography using inks/food
colourings (1.13); PR-03 determine the formula of a metal oxide by combustion (e.g.
magnesium oxide) or reduction (e.g. copper(II) oxide); PR-04 investigate the
electrolysis of aqueous solutions; PR-05 determine the approximate percentage by volume
of oxygen in air using a metal or a non-metal; PR-06 investigate reactions between
dilute hydrochloric and sulfuric acids and metals; PR-07 prepare a sample of pure, dry
hydrated copper(II) sulfate crystals starting from copper(II) oxide; PR-08 prepare a
sample of pure, dry lead(II) sulfate; PR-09 investigate temperature changes accompanying
salt dissolution, neutralisation, and displacement reactions; PR-10 investigate the
effect of changing the surface area of marble chips and of changing the concentration
of acid on the rate of reaction; PR-11 investigate the effect of different solids on
the catalytic decomposition of hydrogen peroxide solution; PR-12 prepare a sample of an
ester such as ethyl ethanoate. Note for downstream families: the 'C'-suffixed anchor
forms (e.g. 1.7C) mark Paper 2 territory; the practicals' official codes are kept in
the graph's own code space (4CH1-PR-nn).

### Course-shape signals from the official teaching corpus

The official Getting Started Guide (Issue 2, October 2024) frames the qualification's
planning-and-support package for centres (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf pp3-5); the scheme of work,
the linear course planner and the two topic teaching guides (Chemical bonding; Chemical
equilibrium) are the board's own sequencing layer over the same four-topic structure
(identity rows in the evidence pack; content interpretation belongs to CUR-02/PED
family, not here). The SAMs booklet (88pp, specimen papers + mark schemes at
first-award standard) is the assessment-shape reference point — specimen material,
never citeable as session evidence (SRC-SAMS-4CH1, identity).

## Evidence / Source Basis

- **CURRENT — AUTHORITATIVE:** SRC-SPEC-4CH1 — official specification PDF, Issue 3
  (pp1, 8, 9, 10, 13, 14, 15 of the PDF as paginated), sha1 of record
  3ad641b7c60b314fa3b10680feda30bf56280a53, verified at run preflight.
- **CURRENT — AUTHORITATIVE:** SRC-GRAPH-4CH1 — validated curriculum graph
  (topics.yaml, assessment_objectives.yaml, practicals.yaml, command_words.yaml),
  wording authority = the official spec PDF (sha1 3ad641b7…), structure = ratified
  overlay; read-only plane for this pipeline.
- **CURRENT — AUTHORITATIVE / SUPPLEMENTARY:** SRC-TL-4CH1 — official
  teaching-and-learning corpus (Getting Started Guide pp3–5, topic guides, scheme of
  work, course planner, command words; sha256s verified at preflight after the
  v1.2.1 identifier repair).
- **CURRENT — ASSESSMENT EVIDENCE (specimen):** SRC-SAMS-4CH1 — official SAMs booklet
  + series-structure notice; structural/identity evidence only in this artifact.

## Limitations / Coverage Gaps

- This artifact states the qualification skeleton; it does not interpret individual
  specification statements (CUR-02), does not assert concept relationships or
  prerequisites (CUR-03/04/05), and does not characterise question behaviour (ASM/MS).
- The evidence pack carries DOCX/PPTX members (scheme of work, course planner, command
  words) as identity-only rows: their text was not extracted in this run, so any claim
  here about their internal sequencing is a pointer to the files, not grounded prose.
- The per-paper AO weighting matrix is taken from the validated graph, which itself
  records an on-record repair of that matrix; the artifact inherits the graph's
  verdict rather than re-deriving it from the PDF.
- Session-level assessment behaviour (how the papers actually behaved) is out of scope
  here and belongs to the ASM/EXM/MIS families, grounded on the official QP/MS corpus
  and the official examiner-report corpus in their own runs' evidence packs.
- 2024-era teaching-corpus rows: the Getting Started Guide is the modular-suite issue
  of the document (running header) applied to the linear 4CH1 course; treated as
  official and current, cited only at overview grain.

## Research Status

status: GENERATED (research artifact; not educational truth, not canonical curriculum
truth). Generated by the SIB-GEN pilot run SIB-CHEMISTRY_4CH1-RUN-001 under the
provider-neutral pipeline; grounded exclusively on the run's CUR-01 evidence pack
(pack sha256 of record in the run manifest). Current/legacy separation: fully CURRENT;
no legacy claims. Determinism: content fingerprint of this artifact is recorded in the
run manifest; regeneration produces a new artifact_version.
