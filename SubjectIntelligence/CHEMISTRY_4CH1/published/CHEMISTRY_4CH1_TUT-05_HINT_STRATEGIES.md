---
sib_protocol: SIB-1.0
artifact_id: TUT-05
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: tutor_intelligence
applicability: REQUIRED

temporal_scope:
  current: true
  legacy: false

source_scope:
  specification: false
  textbook: true
  question_papers: false
  mark_schemes: false
  examiner_reports: true
  supplementary: false

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-008"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "7ff30654d9a256bab02b9371b658ad9b9e589959"
---

# TUT-05 — Hint Strategies

## Purpose

This artifact extracts the hint strategy the validated student book itself
models: how its HINT boxes are built, what hint types recur, and how the
examiner's voice confirms the same disciplines. A tutor can copy these forms
when a student needs a nudge rather than an explanation. Every claim is carried
on a bounded, locator-addressed excerpt from this artifact's own evidence pack.

## Scope

**Covers:** the book's HINT boxes in the pack window — terminology-precision
hints, never-do rules, mnemonic devices, numerical-discipline hints and
reassurance hints — plus the examiner-side echo of presentation advice.

**Out of scope:** misconception diagnosis and response sequences (TUT-06) and
the book's key-point teaching boxes (TUT-01).

## Executive Summary

The book's hints fall into a small number of reusable types: precision guards
("you must not talk about molecules of an ionic compound"), capital-letter
discipline (CO versus Co), absolute rules (never change a formula when
balancing), memory devices (PANiC, AN OX RED CAT), numerical discipline
(significant figures, rounding), and reassurance ("Don't worry if you don't
know…"). The examiner's report voice matches the precision type — rewarding
methods shown as bullet points — so hint-giving and feedback-giving converge on
the same habits.

## Main Analysis

### TUT-025 — Precision hints mark the words that lose marks

**Claim:** the book's hints single out the exact wordings that will be marked
wrong — the ionic-compound molecules ban is stated as an exam-critical precision
rule, the archetype of the mark-protecting hint.
**Evidence:** a HINT box states "This is really important: you must not talk
about molecules of an ionic compound. This will be marked wrong in the exam and
you could lose all the marks for a question!"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 293).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-026 — Symbol-writing hints guard the capitalisation convention

**Claim:** two-letter element symbols carry a capitalisation discipline the
book teaches through a hint anchored on a real confusion — CO (carbon monoxide)
versus Co (cobalt).
**Evidence:** the HINT box states "Be careful! When you are writing symbols with
two letters, the first is a capital letter and the second must be lower case. If
you write CO you are talking about carbon monoxide, not cobalt."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 94).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-027 — Never-do hints state absolute rules without exception clauses

**Claim:** the book's most emphatic hints are absolute prohibitions — the
balancing rule forbids formula changes outright — showing that hint-giving for
irreversible errors uses imperative, unqualified form.
**Evidence:** the HINT box states "This is really important! You must never,
never change a formula when balancing an equation. All you are allowed to do is
to write big numbers in front of the formula."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 139).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-028 — Mnemonic hints compress electrode rules into memorable form

**Claim:** the electrolysis hints use mnemonics — PANiC ("positive anode,
negative (is) cathode") and AN OX RED CAT — paired immediately with the
substantive half-equation work, modelling the pattern: device first, then the
chemistry it indexes.
**Evidence:** the HINT box states "Remember PANiC: positive anode, negative
(is) cathode." before the conduction discussion
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 356);
the electrode-reaction hint opens "A way of remembering this is AN OX RED CAT or
AN OILRIG CAT." and then works the molten-sodium-chloride half-equations with
the charge-balance rule "the total charge must be the same on both sides"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 369).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-029 — Numerical hints enforce significant-figure and rounding discipline in calculations

**Claim:** the calculation hints set the numeric conventions precisely —
significant figures matching the data, and rounding of intermediate ratios —
formulating them as what is allowed versus what is forbidden.
**Evidence:** the ratio hint states "it is fine to round 2.51 to 2.5 or 1.01 to 1
but what you must not do is round 2.51 to 3!"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 197);
the moles hint states "The original masses were measured to 2 significant
figures so the number of moles should also be given to 2 significant figures
(0.010)." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 180). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-030 — Reassurance hints de-escalate early-course anxiety, and the examiner's voice confirms the presentation discipline

**Claim:** the book's hints also manage confidence — telling a student what they
do not yet need to know — while the examiner's report supplies the matching
presentation advice, so the hint repertoire spans content reassurance to
answer presentation.
**Evidence:** an early HINT box states "Don't worry if you don't know how to
write symbol equations. This one is included here so that you can refer to it
again in later revision." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 36); the June 2022 report's
model-answer commentary advises "Consider using bullet points or a numbered list
to show a method clearly." (SRC-ER-4CH1,
chemistry/4ch1/past-papers/2022-06/4CH1-1C/er.pdf p6). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — HINT boxes from
chapters 1, 3, 5, 7 and 10 in the pack window). Supplementary: SRC-ER-4CH1 (the
June 2022 1C report's model-answer advice page, quoted once). SRC-TL-4CH1
(topic-guide cover page) and SRC-SPEC-4CH1 (change-summary page) are held as
single-page identity-presence entries and consumed for no claim. All excerpts
are bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack window holds the first 60 hint matches in book order, so hint style in
Units 3 and 4 is outside the window and no claim is made about it. The examiner
corroboration is a single presentation-advice page; the feedback pattern set is
developed in TUT-07 with its own pack. Hint frequency per chapter is not
counted here — the artifact characterises types, not rates. No canonical planes
were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
