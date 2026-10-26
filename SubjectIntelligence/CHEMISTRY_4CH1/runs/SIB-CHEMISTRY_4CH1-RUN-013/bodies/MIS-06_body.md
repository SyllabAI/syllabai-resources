
# MIS-06 — Terminology Errors

## Purpose

This artifact catalogs the terminology errors that the official Pearson examiner corpus
records for Pearson Edexcel International GCSE Chemistry (4CH1): the naming-vocabulary,
suffix-class, formula-writing and label-precision failures that examiners repeatedly
flag as costing marks independently of chemistry knowledge — "knowledge-adjacent but not
knowledge failures". Every record is grounded on an official Pearson examiner report for
a named session and paper, carried in the run's evidence pack with page identity. It is
a research artifact: it does not promote these observations into canonical educational
truth (Subject Intelligence Build v1, §5).

**Claim-type labeling (BL-011, RUN-011):** records separate what the official
examiner corpus says from what SyllabAI infers from it and proposes for the classroom.
`[OBSERVED_IN_SOURCE]` marks fields whose content quotes or directly paraphrases the
cited official evidence (Evidence / Motivating evidence / Examiner guidance fields).
`[SIB_INFERENCE]` marks SyllabAI's own explanatory and diagnostic reasoning, grounded
on but not stated by that evidence (Why it occurs / Why the reasoning fails /
Diagnostic signals / Signal tested / Fail pattern / Pass pattern). `[PROPOSED_INTERVENTION]`
marks proposed classroom actions, not observed facts (Intervention ideas / Intervention /
Intervention note / Drill design / Success signal / Probe). The remaining record fields
(Concepts, Specification Points, Temporal scope, Assessment context, Misconception /
Error / The confusion, Correct understanding / distinction / reasoning / technique /
usage, Typical manifestation, Credit-worthy form) are record descriptors whose grounding
is the record's cited evidence. The per-record `Temporal scope: CURRENT — AUTHORITATIVE`
stamp carries the source-classification vocabulary defined in SOURCE_REQUIREMENTS.md
§4.1 (definitions of record).

## Scope

**Covers:** seven terminology-error records (MIS-043 … MIS-049) grounded on the official
4CH1 examiner reports held by the library (8 held sessions; papers 1C/2C/1CR/2CR),
extracted into the run's evidence pack with bounded page excerpts and page locators.
Each record states the term or convention misused, why it occurs, the correct usage, the
typical manifestation, and the examiner guidance that addresses it.

**Does not cover:** concept-level confusions behind the vocabulary (MIS-02), examiner
reward/penalty patterns beyond terminology (EXM family), legacy 4CH0 sentiment, and
sessions without a public ER (disclosed gaps, never filled).

## Executive Summary

- Terminology precision is the corpus's single most repeated examiner complaint —
  "candidates need to take care on the use of terminology… As in previous series".
- The -ine/-ide suffix class, intermolecular-force usage, and oxidation-state naming are
  the three named repeat offenders.
- Bonding terminology ("ions moved" for metallic conduction; imprecise metallic/ionic
  vocabulary) measurably lowers average marks on extended items.
- Formula-writing mechanics (subscripts, charges, species names) and even handwriting of
  particle names are named loss sources.

## Main Analysis

### MIS-043 — '-ine' vs '-ide': halogen displacement wording

**Concepts:** Group 7; halogens; halide ions; nomenclature
**Specification Points:** 2.20, 2.21
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** displacement products get the wrong suffix class — "stating that chlorine
displaces bromide and iodide is incorrect rather than displaces bromine and iodine."
**Why it occurs [SIB_INFERENCE]:** the -ine/-ide rule is a naming-layer convention on top of understood
reactivity; the labels swap under pressure.
**Correct usage:** products of displacement are the displaced ELEMENTS (bromine, iodine);
'halide' names the ion in solution.
**Typical manifestation:** -ide products in otherwise-correct displacement orders.
**Examiner guidance [OBSERVED_IN_SOURCE]:** "Teachers need to encourage them to use the correct terminology
when describing these reactions."
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/2C, Question 1 (SRC-ER-4CH1,
2023-11/4CH1-2C/er.pdf p3); June 2023 4CH1/1C, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p3).

### MIS-044 — 'Intermolecular forces' used imprecisely

**Concepts:** covalent bonding; intermolecular forces
**Specification Points:** 1.38, 1.39
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the phrase is used as an incantation or applied to the wrong scale —
"Some candidates also do not fully understand the difference between a bond between two
atoms in a molecule, and an intermolecular force between molecules"; long-response
candidates "lacked a firm grasp of key terminology (eg incorrect use of intermolecular
forces)".
**Why it occurs [SIB_INFERENCE]:** both scales are called 'bonds' in everyday speech; the technical
distinction is unpractised.
**Correct usage:** intermolecular forces act BETWEEN molecules and are overcome at
melting/boiling; covalent bonds act WITHIN molecules and survive state changes.
**Typical manifestation:** 'bonds break' at boiling; IMF cited where bonds were meant.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners name the exact phrase as the terminology failure.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/1C, Introduction (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p3); June 2025 4CH1/1C, Introduction (SRC-ER-4CH1,
2025-06/4CH1-1C/er.pdf p3).

### MIS-045 — Oxidation states omitted from compound names

**Concepts:** rusting; oxidation states; nomenclature
**Specification Points:** 2.17, 2.18
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "the oxidation state was frequently missing and so no mark was scored";
common wrong names "iron(II) oxide, iron hydroxide, and iron oxide with no oxidation
state given"; some "named a process such as oxidation rather than giving the chemical
name".
**Why it occurs [SIB_INFERENCE]:** everyday 'rust' carries no state information; the (III) feels optional.
**Correct usage:** rust is hydrated iron(III) oxide — variable-oxidation compounds need
the Roman numeral.
**Typical manifestation:** zero scored despite knowing rust is an iron oxide.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the name, not the process word, is the markable object.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2023 4CH1/1C, Q2(a)(i) (SRC-ER-4CH1,
2023-06/4CH1-1C/er.pdf p6); November 2024 4CH1/1C, Q3(a)(ii) (SRC-ER-4CH1,
2024-11/4CH1-1C/er.pdf p3).

### MIS-046 — 'Ions moved' and imprecise metallic/ionic bonding vocabulary

**Concepts:** metallic bonding; ionic bonding; conduction
**Specification Points:** 1.37, 1.38
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "some lost both marks for stating that the ions moved" (metallic conduction);
electrons said to "move or slid" for malleability; and generally "the use of imprecise
terminology related to metallic and ionic bonding led to lower average marks in this
section compared to others."
**Why it occurs [SIB_INFERENCE]:** 'charged things move' is over-generalised across structures.
**Correct usage:** metals: delocalised electrons move (conduction), layers slide
(malleability); molten/aqueous ionic compounds: the ions move.
**Typical manifestation:** both-mark losses on structure→property items; lower section
averages.
**Examiner guidance [OBSERVED_IN_SOURCE]:** examiners' wording ("layers moved and slid over each other",
"delocalised electrons") is the model vocabulary.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/2C, Question 2 (SRC-ER-4CH1,
2024-11/4CH1-2C/er.pdf p3); June 2025 4CH1/2CR, Introduction (SRC-ER-4CH1,
2025-06/4CH1-2CR/er.pdf p3).

### MIS-047 — Movement vocabulary: vibration unnamed

**Concepts:** states of matter; particle model
**Specification Points:** 1.1
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** "it was quite common to see the statement the particles do not move, without
adding the key word around or freely" — the word 'vibrate' absent where it is the
markable term.
**Why it occurs [SIB_INFERENCE]:** everyday 'moving' means translating; the kinetic model's sense is
unpractised in words.
**Correct usage:** particles in a solid vibrate about fixed positions; in liquids they
move around; in gases they move freely.
**Typical manifestation:** 'do not move' statements; vague movement prose.
**Examiner guidance [OBSERVED_IN_SOURCE]:** mark-scheme language — vibrate about fixed positions — should be
rehearsed verbatim.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report June 2019 4CH1/1CR, Question 1 (SRC-ER-4CH1,
2019-06/4CH1-1CR/er.pdf p3).

### MIS-048 — Method terminology: 'covering/coating' vs 'barrier'

**Concepts:** corrosion protection; method description
**Specification Points:** 2.17, 2.18
Temporal scope: CURRENT — AUTHORITATIVE
**Error:** the protective mechanism is described with the everyday phrase where the
mark-scheme concept was demanded — "candidates often used the term covering/coating
rather than barrier losing them M1 but they were able to continue and achieve M2."
**Why it occurs [SIB_INFERENCE]:** the physical act (covering) is described instead of the chemical
function (excluding oxygen/water as a barrier).
**Correct usage:** name the function — a barrier excluding the reactants of rusting.
**Typical manifestation:** first marking point lost; partial credit pattern.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the M1/M2 split shows exactly which word carried the mark.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2024 4CH1/1C, Q3(b)(i) (SRC-ER-4CH1,
2024-11/4CH1-1C/er.pdf p3).

### MIS-049 — Formula-writing mechanics: subscripts, charges, spelling

**Concepts:** formulae; ionic charges; scientific spelling
**Specification Points:** 1.19, 1.21, 1.22
Temporal scope: CURRENT — AUTHORITATIVE
**Error (cluster):** "Common mistakes included failing to balance the equation, the
formulae being MgO2, Mg2 or O as a single atom rather than O2"; label switches on
particle diagrams ("proton and neutron labels being switched… the spelling of the
subatomic particles was often poor"); name/suffix slips in organic formulae ("confusion
between ene and ane in Q09(c)").
**Why it occurs [SIB_INFERENCE]:** formulae are written from memory of sounds, not from valency rules;
handwriting pressure degrades labels.
**Correct usage:** valency-derived formulae with correct subscripts; complete, legible
particle names; -ene/-ane suffixes checked against the structure.
**Typical manifestation:** otherwise-correct chemistry losing formula marks.
**Examiner guidance [OBSERVED_IN_SOURCE]:** the formulae errors are itemized by the examiners themselves; at
this level the relative mass of protons and neutrons is taken as 1.
**Evidence [OBSERVED_IN_SOURCE]:** Pearson examiner report November 2023 4CH1/2C, Question 2 (SRC-ER-4CH1,
2023-11/4CH1-2C/er.pdf p3); June 2025 4CH1/1C, Questions 1(a) and Introduction
(SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p4 and p3).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — official Pearson examiner reports; bounded page
  excerpts with page locators in this run's MIS-06 evidence pack
  (evidence/MIS-06/evidence_pack.json, sha256 of record in the run manifest and
  (census.json, artifacts.MIS-06.pack_sha256)); 10 report files, 13 excerpts extracted.
- **Paper/session identity:** SRC-QPMS-4CH1 (SRC-QPMS-4CH1, identity) — the official
  QP/MS corpus of record; identities preserved.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 (SRC-TL-4CH1, identity);
  SRC-BOOK-4CH1-SB1 (SRC-BOOK-4CH1-SB1, identity) — image-only scan, identity-only.

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11, 2022-01,
  2023-01 and 2021-06; Nov-2025/June-2026 PEFs sit behind Pearson's silver tier. Nothing
  is extrapolated across the gaps.
- **Extraction disclosure:** the 2024-06 4CH1/1C ER is glyph-garbled on extraction and is
  EXCLUDED from this pack, not cited by any record.
- The pack carries bounded excerpts (first ~1,600 characters per cited page); records
  reflect the granularity the pack holds.
- Examiner sentiment is session-specific commentary, not a controlled study.

## Research Status

status: GENERATED (research artifact; not educational truth). Generated by SIB-GEN run
SIB-CHEMISTRY_4CH1-RUN-003 under the provider-neutral pipeline, grounded exclusively on
the run's MIS-06 evidence pack. Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims. Determinism: content fingerprint recorded in the run
manifest; regeneration produces a new artifact_version.
