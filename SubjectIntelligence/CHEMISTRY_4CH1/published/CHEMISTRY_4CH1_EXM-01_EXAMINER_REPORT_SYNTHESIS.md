---
sib_protocol: SIB-1.0
artifact_id: EXM-01
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: examiner_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: false
  question_papers: true
  mark_schemes: false
  examiner_reports: true
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-27

provenance:
  source_manifest: "SRC-ER-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-012"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "0261a2b908751ac5c0a4331c1f7463c4956ec664"
---

# EXM-01 — Examiner Report Synthesis

## Purpose

This artifact synthesises the structure and voice of the official 4CH1 examiner
reports held in the corpus of record: what a report contains, how it speaks about performance, and
which recurring commentary forms it uses. Every claim is carried on a bounded,
page-located excerpt from the run's evidence pack, with paper/session identity
preserved per the EXM family's citation law. Research artifact; canonical planes
untouched.

## Scope

**Covers:** report structure; overall-performance statements; question-by-question
commentary; the not-creditworthy ruling class; general-reminder passages;
legacy-transition notes.

**Grounding:** SRC-ER-4CH1 (the 2019-06 1C/1CR/2C/2CR reports of the pack, pages
3-4 of each — the commentary zone after cover and boilerplate) and SRC-QPMS-4CH1
(paper identity headers).

**Out of scope:** warning/reward/penalty catalogues (EXM-02..EXM-04),
question-specific insights (EXM-05).

## Executive Summary

Each report runs cover → publisher boilerplate → an introduction with an
overall-performance statement → question-by-question commentary. The voice is
operational: it says what was well answered, what was not, and — most valuably for
teaching — why answers failed (repeating the stem is "not creditworthy"; an
observation must be an observation). The 2019 reports also carry a historic frame:
first examination of the new specification, with paper-length notes against the
legacy model. The corpus's session coverage is partial by design (no public ER for
COVID-era and some January/November sittings — disclosed in the source manifest of
record), so synthesis here stays within the held sessions.

## Main Analysis

### EXM-001 — The report corpus and its page structure

**Claim:** the held reports follow a stable structure — cover, boilerplate,
introduction, then question-by-question commentary from page 3 onward.
**Evidence:** the 2019-06 1C report's page 3 opens the "Introduction" and its page 4
runs "Question 2 (b)" commentary (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p3, p4); the
1CR report's page 3 opens directly with "Question 1" commentary after its title
block (SRC-ER-4CH1, 2019-06/4CH1-1CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-002 — Overall-performance statements in the introduction

**Claim:** reports open with an overall performance judgement that frames the
question commentary.
**Evidence:** "Introduction This is the first time the new specification for
International GCSE has been examined. Taking this into account candidates generally
performed well on this paper. The first four questions were answered well by the
majority of candidates, but the later questions proved more challenging."
(SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-003 — The question-by-question commentary form

**Claim:** commentary is organised per question part with a performance verdict plus
failure analysis.
**Evidence:** "Question 2 (b) This question was well answered by the majority of
candidates. Those who did not score here often just stated that the elements were in
the same group..." (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p4); the 2CR report's
Question 1 note on the oxygen test (SRC-ER-4CH1, 2019-06/4CH1-2CR/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-004 — The not-creditworthy ruling class

**Claim:** reports rule named answer types non-creditworthy explicitly.
**Evidence:** "...often just stated that the elements were in the same group, which
was just a repeat of the stem of the question and is, therefore, not creditworthy."
(SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-005 — General-reminder passages

**Claim:** reports embed general candidate reminders (presentation, terminology)
alongside question commentary.
**Evidence:** "In general, candidates should be reminded that clear handwriting is
important, and it should be absolutely clear which letter they mean..." (SRC-ER-4CH1, 2019-06/4CH1-1CR/er.pdf p4).
Temporal scope: CURRENT — AUTHORITATIVE.

### EXM-006 — Legacy-transition notes

**Claim:** the first-session reports carry transition framing against the legacy
specification, including paper-length change.
**Evidence:** "This was the first time candidates had sat this new specification
paper. The style of this paper is very similar to that of the legacy specification
but has increased from 60 to 70 marks." (SRC-ER-4CH1, 2019-06/4CH1-2C/er.pdf p3).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-ER-4CH1 — the 2019-06 1C/1CR/2C/2CR examiner-report PDFs
(page-located excerpts from the commentary zone; per-file identity carried by the
paper-dir paths, per-file sha256 recorded in the source manifest of record).
SRC-QPMS-4CH1 provides paper-identity headers in the pack. Reports are commentary on
the official papers — paper identity cites ride on SRC-QPMS-4CH1 per the source
manifest's own limitation note. Session coverage limits (8/16 held sessions; the
garbled 2024-06 1C ER excluded of record) are disclosed in the run receipts.

## Limitations / Coverage Gaps

The synthesis anchors on the four 2019-06 reports of the pack; later held sessions
(2022-2025) are analysed in the sibling EXM artifacts whose packs hold them. Sessions
without public ERs (COVID-era, some January/November sittings) and the silver-tier
Nov-2025/June-2026 PEFs are source gaps of record — disclosed, never filled. No
canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-005 (BL-008 pass 5) from the run's evidence
pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 bound all citations
to pack excerpts. Research artifact — evidence-backed, not canonical educational
truth.
