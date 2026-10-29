---
sib_protocol: SIB-1.0
artifact_id: GAP-05
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: gap_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: true
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-009"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "6ef8c89291a6662f11fc6dc5ada151c47b172075"
---

# GAP-05 — Resource Quality Gaps

## Purpose

This artifact audits the quality of the resource corpus of record for the
Pearson Edexcel International GCSE in Chemistry (4CH1): what the issuing
body's own change-control machinery says about currency, what quality
infrastructure the student book and the teaching-and-learning corpus carry,
and where the of-record corpus is known to be damaged or absent. It is an
audit of the evidence base itself, and it discloses every quality finding the
packs can support — including the OCR-garbled examiner report that stays
excluded of record.

## Scope

**Covers:** the specification's Issue 3 change summary as the issuing body's
currency signal; the book's built-in quality infrastructure (answer sections,
significant-figure guidance, examiner-report study advice); the
teaching-and-learning terminology resource; and the disclosed quality
exclusions (garbled OCR, absent corpora, presence-only sources).

**Out of scope:** assessment-coverage arithmetic (GAP-03) and research
priorities derived from the gaps (GAP-08).

## Executive Summary

The resource corpus of record carries two kinds of quality signal: external
and internal. Externally, the specification of record publishes an Issue 3
change summary that names every changed page — the issuing body's own
currency attestation. Internally, the student book carries a full answer
infrastructure, explicit significant-figure discipline and a study-skills
page directing students to published mark schemes and examiners' reports, and
the teaching-and-learning corpus carries a dedicated practical-terminology
resource. Against those strengths the audit sets the disclosed weaknesses: a
garbled June 2024 Paper 1C examiner report excluded of record, eleven source
corpora absent at preflight, and root-level book intake copies that ride as
presence-only because their provenance is not re-verified.

## Main Analysis

### GAP-025 — The issuing body publishes a page-indexed change summary for the current specification issue, and the of-record copy is that Issue 3 document

**Claim:** the specification of record is Issue 3 (September 2024) and its
change summary enumerates the changed pages — an issuing-body currency signal
no other of-record source supplies — so currency auditing can proceed from
the document itself rather than from external claims.
**Evidence:** the of-record page reads "Summary of Pearson Edexcel
International GCSE in Chemistry (4CH1) specification Issue 3 changes Summary
of changes made between previous issue and this current issue Page number
Qualification at a glance 7, 8 Availability of series amended to November and
June Administration and general information 31 Modular International GCSEs
added to forbidden combinations Appendix 5: Command word taxonomy 46 'Which'
added to the command word taxonomy" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p3). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-026 — The book of record carries a built-in answer infrastructure that the pack can exhibit from Chapter 1 through Unit 1 questions

**Claim:** the student book's quality infrastructure includes published
answer sections — the pack exhibits answer chunks keyed to chapters and unit
question batteries — so self-checking does not depend on resources outside
the book of record.
**Evidence:** the answer chunks of record include the Chapter 1 answers —
"melting • b freezing subliming/sublimation" and particle-diagram notes
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1137)
— and the End-of-Unit-1 answers with mark-coded lines — "-255 °C (1) The
temperature is between the melting point and boiling point. Particles randomly
arranged (1) and mostly touching each other. (1)" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1169). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-027 — The book states its own numerical-quality discipline in exam-facing terms

**Claim:** the book's significant-figure guidance states a precision rule and
an exam-facing practice — quote answers to 3 significant figures, carry more
figures through the calculation and round at the end — which is a quality
standard the of-record corpus enforces internally rather than borrowing.
**Evidence:** the book's hint states "In the exam, it is usually best to quote
answers to 3 significant figures" and "carry more significant figures through
on your calculator and then round the value at the end" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 735). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-028 — The book directs students to published mark schemes and examiners' reports — surfaces that are only partially present of record

**Claim:** the book's study-skills page instructs students to check answers
"against the published mark schemes and against the comments in the Examiners'
Reports" — but of record the examiner reports are present while the mark
schemes and question papers are absent corpora, so the book's recommended
resource path is only partially satisfiable from the archive of record.
**Evidence:** the book's page reads "The very best way of revising for the
exam at the end of your course is to work through past papers set by your
examiners" and "You need to check your answers against the published mark
schemes and against the comments in the Examiners' Reports" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1104); the examiner-report
presence of record identifies as "Examiners' Report June 2025 Int GCSE
Chemistry 4CH1 1C" (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p1) while no mark
scheme is resolved in this run's preflight — a gap disclosed, not filled.
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-029 — The teaching-and-learning corpus carries a dedicated practical-terminology resource with defined variable language

**Claim:** the board's practical-terminology guide of record defines the
variable vocabulary — independent, dependent, control, fair test, valid — in
examination-facing terms, which is a quality resource the book's practical
appendix can be checked against rather than duplicated.
**Evidence:** the guide states "During an investigation, one variable is
altered (independent variable); and the effect on another variable
(dependent variable) is measured. Other variables which may affect the
results of the investigation are kept constant or controlled" and "An
investigation where variables that may affect the outcome are all controlled
– except the independent variable – is referred to as a fair test"
(SRC-TL-4CH1, practical-terminology-in-int-gcse-science.pdf p4); the book's
graph-drawing discipline — "The line should still be a best-fit curve" —
rides in the of-record corpus alongside it (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1094). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-030 — The disclosed quality exclusions: one garbled examiner report, eleven absent corpora, and presence-only intake copies

**Claim:** the corpus of record carries three disclosed quality limitations —
the June 2024 Paper 1C examiner report stays excluded of record as OCR-garbled
(a RUN-005 exclusion carried forward), eleven source corpora failed preflight
in this run, and the root-level book intake copies ride as identity-presence
only because their provenance is not re-verified — and none of the three is
repaired or substituted in this audit.
**Evidence:** the examiner-report windows of record deliberately avoid the
excluded June 2024 1C report — the clean report covers sampled in this pack
are "Examiners' Report June 2025 Int GCSE Chemistry 4CH1 1C" (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p1) and "Examiners' Report June 2023 Int GCSE Chemistry
4CH1 2C" (SRC-ER-4CH1, 2023-06/4CH1-2C/er.pdf p1); the
root-level intake copy of record identifies only as "EDEXCEL INTERNATIONAL
GCSE (9-1) Jim Clark Steve Owen Rachel Yu" (SRC-ROOT-BOOK-COPIES-4CH1,
edexcel-chemistry-igcse-book.pdf p1, identity-presence only); and the SAMs
cover rides as "INTERNATIONAL GCSE Chemistry (9-1) SAMPLE ASSESSMENT
MATERIALS Pearson Edexcel International GCSE in Chemistry (4CH1) For first
teaching September 2017 First examination June 2019" (SRC-SAMS-4CH1,
international-gcse-Chemistry-2017-SAM.pdf p1, identity-presence only).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-061 — The answer key pre-publishes marking law and accepted-variant equivalence classes — a quality dimension no other of-record surface supplies

**Claim:** The book's answer infrastructure does not stop at scores: the answer pages publish the marking law itself — for conduction answers the word ions is required and any mention of electrons scores zero — and publish accepted-variant equivalence classes for diagrams — dots, crosses or colours, and the positions of the hydrogens, do not matter — so a student self-checking against the book is checking against the board's own acceptance rules; this pre-publication of marking law is a resource-quality dimension the examiner reports corroborate only session by session.
**Evidence:** the conduction answer states the law inline — "The ions are free to move (it is important to use the word ions here; any mention of electrons will score 0 in an exam)." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1163); the diagram answer states the equivalence class — "(lt doesn't matter whether students use dots or crosses or just different colours- or what positions (N, S, E, W) the hydrogens occupy in the H2S or PH3)" (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1164; the parenthetical opens with the OCR surface lt for It — quoted verbatim from the text of record).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-062 — The answer key publishes tolerance bands for graph-dependent answers, teaching tolerance-aware self-checking

**Claim:** The solubility-curve answers publish their own tolerance bands — a solubility read from the line of best fit is marked correct across about a gram per hundred grams, a crystallisation mass within a gram, a temperature within a degree — and the key says why: the values depend on the line of best fit and the exam will always accept a range; no other of-record surface documents numeric tolerance for graph-reading, so the book is the only place a student can learn tolerance-aware self-checking of plotted answers.
**Evidence:** the key states the dependence — "The values obtained in this question and in c depend on the line of best fit. In the exam there will always be some tolerance – a range of values will be accepted." — with the bands in the answers themselves: "b 94 +/-1 g per 100 g" and "Answers of 13 ±1 g are acceptable." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1138).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-063 — The Unit 3 CHEMISTRY ONLY question battery is a graded assessment surface inside the book, with mark tariffs on the chemistry-only tier

**Claim:** The Unit 3 question battery contains a CHEMISTRY ONLY band that prices the chemistry-only tier in examination format: the dynamic-equilibrium item asks students to choose two characteristics from four options whose distractors encode the constant-versus-equal distinction, and the catalyst item demands an explained answer about equilibrium position; the battery therefore lets the chemistry-only population self-assess at exam grain inside the book of record, extending the answer-infrastructure finding of GAP-026 from answers to a full graded battery with mark tariffs.
**Evidence:** the battery frames the choice — "What are the characteristics of a reaction at dynamic equilibrium (choose two answers)?" with distractor "B The concentrations of the reactants and the products are always equal." against correct option "D The concentrations of the reactants and the products are constant." — and prices the catalyst item: "Reactions can be accelerated using a catalyst. Write down and explain the effect of a catalyst on the position of equilibrium in this reaction." — the whole battery chunk opening at its own CHEMISTRY ONLY band (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 861).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the Issue 3 change summary, p3, and the SAMs
/ experimental-skills page, p34) and SRC-BOOK-4CH1-SB1 (the book's answer
infrastructure, significant-figure discipline and study-skills page).
Supplementary: SRC-TL-4CH1 (the practical-terminology guide's variable-language
page) and SRC-ER-4CH1 (clean report covers as quality samples) are cited;
SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as one-page identity-presence
entries consumed for identity claims only. All excerpts are bounded with
locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The book's answer infrastructure is sampled at two chunks of a 42-excerpt
window; the sampling is disclosed, not exhaustive. The OCR-garbled June 2024
Paper 1C examiner report stays excluded of record and is characterized only by
its absence. Eleven source corpora failed preflight this run and are disclosed
as absent; no claim here depends on their contents.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-022 (D3 REQUIRED-core depth pass, tranche 6: GAP): +3 records (GAP-061..GAP-063), zero-append mining of the carried pack of record (origin RUN-009) — unmined-window authoring for seven artifacts and held-window authoring with fresh claims for GAP-03, whose unmined surface was exhausted (1/29 excerpts unmined pre-run); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

