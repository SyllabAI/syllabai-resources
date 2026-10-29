---
sib_protocol: SIB-1.0
artifact_id: GAP-03
artifact_version: 1.1
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
  textbook: false
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: false

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-30

provenance:
  source_manifest: "SRC-SPEC-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-022"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "bc4740884"
    syllabai_resources: "1a5c37bcecf379cd98e83aa74aa9472920092428"
---

# GAP-03 — Assessment Coverage Gaps

## Purpose

This artifact audits assessment coverage for the Pearson Edexcel International
GCSE in Chemistry (4CH1): what the specification's assessment model demands,
what examiner-report coverage the archive of record actually supplies, and
where the two do not meet. It enumerates the examiner-report census of record
session by session and paper by paper, and discloses every assessment surface
the of-record corpus cannot cover. Gaps are disclosed, never filled — no
session, paper or mark-scheme surface is inferred into existence.

## Scope

**Covers:** the two-paper assessment model and its weighting split; the
assessment-objective weightings; the examiner-report census of record (23
clean reports across seven sessions, 2019–2025); the session, series and
paper-variant gaps disclosed by that census.

**Out of scope:** curriculum content coverage (GAP-01), misconception-content
of the reports (GAP-04), and question-paper/mark-scheme surfaces, which are
absent of record and disclosed here rather than audited.

## Executive Summary

The specification of record assesses the qualification through Paper 1C
(110 marks, 61.1%) and Paper 2C (70 marks, 38.9%), totalling 180 marks, with
assessment-objective weightings printed as ranges rather than point values.
Against that model, the archive of record carries 23 clean examiner reports
spanning seven sessions from June 2019 to June 2025. The census discloses
structural gaps: no 2020 or 2021 sessions of record, a November series present
only from November 2023 onward and never with regional (R) variants, and the
June 2024 Paper 1C report excluded of record as OCR-garbled. Question papers
and mark schemes as corpora are absent of record entirely, and the sample
assessment materials ride as identity-presence only.

## Main Analysis

### GAP-013 — The assessment model of record is a two-paper structure with a fixed mark and weighting split

**Claim:** the specification assesses the qualification through exactly two
papers with fixed marks and weightings — Paper 1C at 110 marks and 61.1%,
Paper 2C at 70 marks and 38.9%, 180 in total — and the two papers differ
systematically in the content they may draw on, which makes any assessment
corpus gap asymmetric between the papers.
**Evidence:** the specification's assessment page states Paper 1C is
"Assessed through a 2-hour written examination set and marked by Pearson" and
"The paper is weighted at 61.1% of the qualification", assessing "the content
that is not in bold and does not have a 'C' reference" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33); Paper 2C is
"Assessed through a 1-hour and 15-minute written examination" weighted at
"38.9% of the qualification", assessing "all the content, including content
that is in bold and has a 'C' reference" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33); the page totals
them — "The total number of marks for this qualification is 180" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-014 — Assessment-objective weightings are printed as ranges, and the of-record page carries a parsing asymmetry that the audit discloses

**Claim:** the specification prints its assessment-objective weightings as
ranges — AO1 and AO2 at 38–42% each, AO3 at 19–21% — and the of-record page
renders the AO2 weighting without its en-dash, an extraction artifact the
audit records rather than repairs; no point-value weighting exists anywhere in
the pack of record.
**Evidence:** the assessment-objectives table reads "AO1 Knowledge and
understanding of chemistry 38–42% AO2 Application of knowledge and
understanding, analysis and evaluation of chemistry 38 42% AO3 Experimental
skills, analysis and evaluation of data and methods in chemistry 19–21%"
(SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p35); the
per-unit table beneath it splits the same ranges by paper — "Chemistry Paper 1
23.2–25.7% 23.2–25.7% 11.6–12.8%" and "Chemistry Paper 2 14.8–16.3%
14.8–16.3% 7.4–8.2%" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p35). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-015 — The examiner-report census of record comprises 23 clean reports across seven sessions, June 2019 to June 2025

**Claim:** the archive of record supplies exactly 23 clean examiner reports
for 4CH1, spanning the sessions June 2019, June 2022, June 2023, November
2023, June 2024, November 2024 and June 2025 — a census the audit enumerates
from the reports' own cover pages of record.
**Evidence:** the covers identify themselves — "Examiners' Report June 2019
IGCSE Chemistry 4CH1 1C", "Examiners' Report Principal Examiner Feedback
Summer 2019 Pearson Edexcel International GCSE in Chemistry (4CH1) Paper 1CR",
"Examiners' Report June 2022 International GCSE Chemistry 4CH1 2C", "Examiners'
Report June 2023 Int GCSE Chemistry 4CH1 1CR", "Examiners' Report Principal
Examiner Feedback November 2023 Pearson Edexcel International GCSE In
Chemistry (4CH1) Paper 1C and Science Double Award (4SD0) Paper 1C", "Examiners'
Report June 2024 Int GCSE Chemistry 4CH1 2CR", "Examiners' Report Principal
Examiner Feedback November 2024 Pearson Edexcel International GCSE In
Chemistry (4CH1) Paper 2C" and "Examiners' Report June 2025 Int GCSE Chemistry
4CH1 1C" (SRC-ER-4CH1, er.pdf p1, covers of record). Temporal scope: CURRENT —
AUTHORITATIVE.

### GAP-016 — No 2020 or 2021 session exists of record, and the November series enters only from November 2023

**Claim:** the of-record examiner-report census contains no 2020 session and
no 2021 session, and its November coverage begins only at November 2023 —
two full years of sessions and all earlier Novembers are assessment-coverage
gaps that the archive of record cannot illuminate, and this audit discloses
them rather than approximating them.
**Evidence:** the census of record enumerates June 2019, June 2022, June 2023,
November 2023, June 2024, November 2024 and June 2025 covers — "Examiners'
Report June 2019 IGCSE Chemistry 4CH1 1C", "Examiners' Report June 2022
International GCSE Chemistry 4CH1 1CR", "Examiners' Report June 2023 Int GCSE
Chemistry 4CH1 2C", "Examiners' Report Principal Examiner Feedback November
2023 Pearson Edexcel International GCSE In Chemistry (4CH1) Paper 2C" and
"Examiners' Report Principal Examiner Feedback November 2024 Pearson Edexcel
International GCSE In Chemistry (4CH1) Paper 1C" (SRC-ER-4CH1, er.pdf p1,
covers of record) — with no 2020 or 2021 cover among them. Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-017 — November sessions carry no regional (R) paper variants, and June 2024 is missing its Paper 1C report of record

**Claim:** the June sessions of record each carry four paper variants (1C,
1CR, 2C, 2CR) while the November sessions of record carry only 1C and 2C — no
R variants — and June 2024 enters the census with only three clean reports
because its Paper 1C examiner report is excluded of record as OCR-garbled, a
disclosure carried forward from the earlier run rather than repaired.
**Evidence:** the June 2025 covers run "Examiners' Report June 2025 Int GCSE
Chemistry 4CH1 1C", "…4CH1 1CR", "…4CH1 2C" and "…4CH1 2CR" while the November
covers of record are only "Examiners' Report Principal Examiner Feedback
November 2023 Pearson Edexcel International GCSE In Chemistry (4CH1) Paper 1C
and Science Double Award (4SD0) Paper 1C", "…Paper 2C", "Examiners' Report
Principal Examiner Feedback November 2024 Pearson Edexcel International GCSE
In Chemistry (4CH1) Paper 1C" and "…Paper 2C" (SRC-ER-4CH1, er.pdf p1, covers
of record); the June 2024 covers of record are "Examiners' Report June 2024
Int GCSE Chemistry 4CH1 1CR", "…4CH1 2C" and "…4CH1 2CR" with no 1C cover
(SRC-ER-4CH1, er.pdf p1, covers of record). Temporal scope: CURRENT —
AUTHORITATIVE.

### GAP-018 — Mark schemes and question papers are absent of record, and the practical-assessment surface is disclosed as italic specification points the pack cannot enumerate

**Claim:** the archive of record contains no question-paper or mark-scheme
corpus for 4CH1 — those sources failed preflight and stay disclosed — so
assessment coverage can be audited only from the specification's model and the
examiner-report census; the specification's experimental-skills machinery
points to italic specification points and to a SAMs document that rides in
this pack as identity-presence only, and neither surface is itemized of
record.
**Evidence:** the specification states "Sample papers and mark schemes can be
found in the Pearson Edexcel International GCSE in Chemistry Sample Assessment
Materials (SAMs) document" and "Our practical investigations are embedded
within 2: Chemistry content as specification points in italics" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p34); the SAMs cover of
record is "INTERNATIONAL GCSE Chemistry (9-1) SAMPLE ASSESSMENT MATERIALS
Pearson Edexcel International GCSE in Chemistry (4CH1) For first teaching
September 2017 First examination June 2019" (SRC-SAMS-4CH1,
international-gcse-Chemistry-2017-SAM.pdf p1, identity-presence only). The
topic-guide presence source is "TOPIC GUIDE: Chemical bonding Pearson Edexcel
International GCSE in Chemistry (4CH1) and Science (4SD0 and 4SS0) First
teaching 2017" (SRC-TL-4CH1, Chemical-bonding---FINAL.pdf p1). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-055 — The two-paper mark ledger closes arithmetically of record and the page rules out scaling, so no hidden normalisation layer exists to reconcile

**Claim:** The assessment model's own arithmetic closes on the page of record: 110 plus 70 marks is the stated 180 total, the stated weightings 61.1 and 38.9 percent sum to exactly 100, and the page states the marks for the papers are not scaled, with grades 9 to 1 awarded on the overall mark; assessment-coverage risk therefore lives in the absent question-paper and mark-scheme corpora disclosed at GAP-018, not in the mark ledger itself, which needs no reconciliation surface beyond the two papers. (Authored from held windows with fresh claims: this artifact's unmined excerpt surface was exhausted pre-run.)
**Evidence:** the page totals and closes the ledger — "The total number of marks for this qualification is 180. This total is obtained by adding the mark for Paper 1C (out of 110 marks) to the mark for Paper 2C (out of 70 marks). The marks for the papers are not scaled." — and fixes the award rule: "Based on the overall mark, students will be awarded a grade. The grades available range from 9 to 1" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p33).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-056 — The experimental-skills list is the finest-grained experimental-assessment surface of record, and it carries no per-skill weighting

**Claim:** The specification's experimental-skills page enumerates the ability classes the written papers may test — from solving problems in a practical context through identifying independent, dependent and control variables — but the pack carries no per-skill weighting: the only quantitative surface for experimental skills is the AO3 band of 19 to 21 percent, so skill-level assessment coverage cannot be audited from the of-record corpus and is disclosed as a granularity gap. (Authored from held windows with fresh claims: this artifact's unmined excerpt surface was exhausted pre-run.)
**Evidence:** the skills list opens "solve problems set in a practical context" and includes "make observations and measurements with appropriate precision, record these methodically and present them in appropriate ways" and "identify independent, dependent and control variables" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p34); the only weighting surface of record is "AO3 Experimental skills, analysis and evaluation of data and methods in chemistry 19–21%" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p35).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-057 — Exactly one cover in the 23-report census names a second qualification: the November 2023 Paper 1C report is jointly issued for 4CH1 and 4SD0

**Claim:** The November 2023 Paper 1C examiner report identifies itself as covering both the Chemistry Paper 1C and the Science Double Award 4SD0 Paper 1C in a single document — the only such joint-qualification cover in the census of record — so the 4CH1 November-2023 1C commentary is partially shared with the Double Award population; no standalone 4SD0 report corpus exists of record, and no other session cover names a second qualification. (Authored from held windows with fresh claims: this artifact's unmined excerpt surface was exhausted pre-run.)
**Evidence:** the joint cover of record reads "Pearson Edexcel International GCSE In Chemistry (4CH1) Paper 1C and Science Double Award (4SD0) Paper 1C" under the November 2023 heading (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p1); the other 22 covers of record identify 4CH1 papers only, e.g. "Examiners' Report June 2025 Int GCSE Chemistry 4CH1 1C" (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p1).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the assessment-information page, the SAMs /
experimental-skills page and the assessment-objectives page) and SRC-ER-4CH1
(23 clean examiner-report cover pages of record, one per report, 2019-2025).
Supplementary: SRC-ROOT-BOOK-COPIES-4CH1 and SRC-SAMS-4CH1 ride as one-page
identity-presence entries; the SRC-BOOK-4CH1-SB1 entry resolved identity-only
(this artifact's query matched no chunk text) and is consumed for no claim.
All excerpts are bounded with locators preserved; caps enforced by the pack
builder.

## Limitations / Coverage Gaps

No question-paper or mark-scheme corpus is resolved of record, so no
item-level assessment demand can be audited. The June 2024 Paper 1C examiner
report stays excluded of record as OCR-garbled (RUN-005 exclusion carried
forward) and is deliberately absent from the census. The examiner-report
census is a cover-page census — report interiors are not sampled here and no
claim is made about them.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-022 (D3 REQUIRED-core depth pass, tranche 6: GAP): +3 records (GAP-055..GAP-057), zero-append mining of the carried pack of record (origin RUN-009) — unmined-window authoring for seven artifacts and held-window authoring with fresh claims for GAP-03, whose unmined surface was exhausted (1/29 excerpts unmined pre-run); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
