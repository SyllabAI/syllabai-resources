---
sib_protocol: SIB-1.0
artifact_id: TUT-05
artifact_version: 1.1
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
generated_at: 2026-10-30

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-021"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "bc4740884"
    syllabai_resources: "7352d2eab0bc822a8273d8dadfbeaefe3faf45d2"
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

### TUT-073 — Accepted-variant hints define the equivalence classes the exam will tolerate

**Claim:** The HINT apparatus does not only police errors — it grants explicit permission for variants, which tells the tutor exactly where individual taste is free. Terminology is the standing example: shell and energy level are declared interchangeable, both accepted in the examination; electron drawings may show helium's two electrons paired or opposite, either form acceptable; and single-or-paired electron drawing is left to taste at this level. A tutor who knows these equivalence classes never wastes marks policing style the exam does not discriminate on, and can spend the saved attention on the conventions the book does pin down.
**Evidence:** the terminology grant: "The terms 'shell' and 'energy level' are used quite interchangeably by chemists. To make things easier, we will just use one term, shell, from now on. If, however, you prefer the term energy level, that is absolutely fine and both terms will be accepted in the examination." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 117); the drawing grants: "The helium electrons are sometimes shown as a pair (as here), and sometimes as two separate electrons on opposite sides of the circle. Either form is acceptable." and "It does not matter at this level whether you draw the electrons singly or in pairs." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 117).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-074 — Error-anticipation hints name the mistake mechanism; sanity-envelope hints bound the answer

**Claim:** Two hint families work as a pair. The forecast family names the exact mechanism of a common mistake before it happens — the hydrated-crystal counter that correctly works out ten hydrogens but then counts one oxygen instead of five, the yield multiplier that re-applies the coefficient two by using 2Fe's 112 g after the moles step already used it, and the word-ending trap in formula writing. The envelope family then bounds the answer so the mistake can be caught downstream: a percentage yield must come out below 100 per cent, with the two legitimate explanations for an over-100 value spelled out, and an Rf value must sit between 0 and 1, a violation meaning the division ran backwards. The tutor teaches the mechanism, then hands the student the detector.
**Evidence:** the named forecasts: "It is dangerous to calculate the number of hydrogens and oxygens separately. The common mistake is to work out 10 hydrogens (quite correctly!), but then only count 1 oxygen rather than 5." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 154) and "A common mistake is to multiply the number of moles by the mass of 2Fe (112 g), but we have already used the '2' when we worked out the number of moles of Fe." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 214); the yield envelope: "The percentage yield should always come out as less than 100%. If it comes out as more than 100% either you have made a mistake in the calculation or the question will continue by asking about what might have gone wrong in the experiment to give a value greater than 100%." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 223); the Rf envelope: "An Rf value must be between 0 and 1. If you get a number bigger than 1 you have probably divided the numbers the wrong way round." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 81).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-075 — Method-pluralism hints license the faster route — with a show-your-working floor beneath it

**Claim:** The calculation hints repeatedly grant pluralism: reliance on memorised formulae is discouraged in favour of proportional reasoning, the printed formula is licensed for students who feel safer with it, and two complete calculation methods for reacting masses are offered on the explicit condition that only one need be learned. The floor under the freedom is uniform: however fast the route, all calculations must be shown. The tutor therefore teaches method choice as a legitimate decision while enforcing the one non-negotiable — visible working — which is what the mark scheme actually pays for.
**Evidence:** the proportional-reasoning steer: "Don't get too reliant on learning formulae for doing simple calculations. If 1 mole weighs 100g, it should be fairly obvious to you that 2 moles will weigh twice as much, 10 moles will weigh 10 times as much and 0.2 moles will weigh 0.2 times as much." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 162) and "On the other hand, if you feel safer using a formula, use it." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 163); the floor: "Your maths may be so good that you don't need to take all these steps to find the answer. If you can do it more quickly, that's fine. However, you must still show all your calculations." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 212).
Temporal scope: CURRENT — AUTHORITATIVE.
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
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-073..TUT-075), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.
