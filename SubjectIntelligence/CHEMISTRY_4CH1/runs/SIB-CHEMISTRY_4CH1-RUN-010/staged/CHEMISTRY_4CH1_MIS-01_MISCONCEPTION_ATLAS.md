---
sib_protocol: SIB-1.0
artifact_id: MIS-01
artifact_version: 1.1
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: misconception_intelligence
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

status: GENERATED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-ER-4CH1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-010"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "2cb92fe5f56d22f1b231c129a7e0dbc27bf86007"
    syllabai_resources: "295fb5b698b37026417e4100551b025579c5f90f"
---

# MIS-01 — Misconception Atlas

## Purpose

This artifact maps the misconception and error landscape of Pearson Edexcel
International GCSE Chemistry (4CH1) as it is visible in the official examiner
corpus: what candidates actually get wrong, why they get it wrong, and what examiners
say distinguishes credit-worthy answers from near-misses. Every record is grounded on
an official Pearson examiner report for a named session and paper, carried in the
run's evidence pack with page identity. The atlas exists to feed diagnostics,
interventions and examiner-intelligence artifacts downstream — never to replace the
mark-scheme or canonical planes. It is a research artifact: it does not promote these
observations into canonical educational truth (Subject Intelligence Build v1, §5).

## Scope

**Covers:** current assessment evidence only (official examiner corpus). Twelve misconception records
(MIS-001 … MIS-012) grounded on the official 4CH1 examiner reports of record —
the 23 clean reports across the seven sessions with public ERs (2019-06, 2022-06,
2023-06, 2023-11, 2024-06, 2024-11, 2025-06), covering papers 1C/2C/1CR/2CR as
held; the June 2024 Paper 1C report is excluded of record as OCR-garbled.
Each record states the concept, the misconception, why it occurs, the correct
understanding, the typical manifestation and the diagnostic/intervention signals, with
the examiner-report citation(s) that ground it.

**Does not cover:** mark-scheme internals (MS family), question-by-question examiner
synthesis beyond the misconception grain (EXM family), legacy 4CH0 sentiment (out of
temporal scope here), and any claim about sessions for which no public ER exists —
those are publishing gaps, disclosed in the library manifest, never filled by
invention.

## Executive Summary

- The examiner corpus shows a consistent set of high-frequency misconception clusters
  across 2019–2025: particle-model language (vibration is movement), halogens vs
  halide ions terminology, bonds vs intermolecular forces, stoichiometric-ratio
  handling, premature rounding, and practical-work under-preparation.
- Terminology precision is the single most repeated examiner complaint: candidates
  "lose unnecessary marks" for vague prose, imprecise bonding vocabulary, and
  element/ion naming confusions that are knowledge-adjacent but not knowledge failures.
- Practical chemistry is the weakest strand in the corpus: examiner introductions
  repeatedly identify practical-context questions as the most challenging, with one
  series noting "many candidates had done very little practical work".
- Calculation technique is comparatively strong but carries two systematic failure
  modes examiners name explicitly: neglecting or double-counting the stoichiometric
  ratio, and premature rounding/truncation.

## Main Analysis

### MIS-001 — Particle movement in solids: "particles do not move"

**Concepts:** states of matter; particle model
**Specification Points:** 1.6
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1 territory (core statements); description-style items.
**Misconception:** Candidates describe the particles in a solid as not moving, treating
vibration as distinct from movement; others answer a question about arrangement and
movement with descriptions of inter-particle forces or particle energy instead.
**Why it occurs:** The everyday meaning of "not moving" (no translation) collides with
the kinetic model, where vibration about fixed positions IS movement; candidates also
pattern-match "describe the particles" to whichever particle facts they rehearsed
(forces/energy) rather than the two axes the question names.
**Correct understanding:** In a solid, particles vibrate about fixed positions in a
regular arrangement — vibration is a type of movement; "arrangement" and "movement"
are the two axes a description question demands.
**Typical manifestation:** "The particles do not move" without "…around/vibrate"; or a
correct-energy description where arrangement+movement was asked (examiners: answers
"did not address the question").
**Diagnostic signals:** Ask for arrangement AND movement of particles in a solid/liquid/
gas; watch for force- or energy-language substitutions; ask whether vibration counts as
movement.
**Intervention ideas:** Three-column drill (arrangement / movement / energy) per state;
explicitly name vibration as movement; mark-scheme-language practice ("vibrate about
fixed positions", "move around freely").
**Evidence:** Pearson examiner report June 2019 4CH1/1CR, Question 1 (SRC-ER-4CH1, 2019-06/4CH1-1CR/er.pdf p3): candidates "gave the impression they did not appreciate that vibration is
a type of movement"; some "described the forces between particles… or referred to the
amount of energy" where arrangement+movement was asked.

### MIS-002 — Evaporation explained as more frequent collisions

**Concepts:** states of matter; evaporation; kinetic theory
**Specification Points:** 1.6
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1; explain-style one/two-mark items.
**Misconception:** On heating, candidates explain evaporation as "greater frequency of
collisions" — importing reaction-kinetics vocabulary into a physical change.
**Why it occurs:** The collision-frequency explanation is heavily rehearsed for rates
of reaction and over-applies to any "what happens when you heat" question.
**Correct understanding:** Heating raises particle (kinetic) energy; evaporation
involves the more energetic particles at the surface escaping the liquid.
**Typical manifestation:** "Particles collide more often so more evaporate."
**Diagnostic signals:** Ask why heating increases evaporation rate; flag any
collision-frequency answer as the kinetics frame mis-applied.
**Intervention ideas:** Contrast pair drill: rate-of-reaction explanation vs
evaporation explanation, same stimulus (heating); require the words "more energetic
particles escape".
**Evidence:** Pearson examiner report November 2023 4CH1/1C, Q1b (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p3):
"Far fewer went on to explain that evaporation involves the more energetic particles
escaping the liquid. Some confused this process with reactions by talking about greater
frequency of collisions."

### MIS-003 — Change of state written as a chemical reaction

**Concepts:** condensation; physical vs chemical change; state symbols
**Specification Points:** 1.5, 1.6
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1; equation-writing items on state changes.
**Misconception:** Candidates write a chemical equation (e.g. forming water) for a
change of state such as condensation, not realising the molecules themselves are
unchanged.
**Why it occurs:** Equation-writing is rehearsed as "always make a new substance
equation"; the cue "write an equation" overrides the change-of-state context.
**Correct understanding:** A change of state alters arrangement and energy, not the
molecules: H2O(g) → H2O(l), with state symbols carrying the meaning.
**Typical manifestation:** An equation for the formation of water where condensation
was asked.
**Diagnostic signals:** Any state-change item that asks for an equation; check whether
the molecular formula changes across the arrow.
**Intervention ideas:** Physical-vs-chemical change sort with equations; drill
state-symbol equations for melting/boiling/condensing/freezing.
**Evidence:** Pearson examiner report November 2023 4CH1/1C, Q1c(ii) (SRC-ER-4CH1, 2023-11/4CH1-1C/er.pdf p3):
"A few incorrectly wrote an equation for the formation of water. They did
not realise that a change of state does not alter the molecules themselves."

### MIS-004 — Halogens vs halide ions (and -ine/-ide naming)

**Concepts:** Group 7; halogens; halide ions; displacement
**Specification Points:** 2.20, 2.21
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1 and Paper 2; displacement and test-for items.
**Misconception:** Candidates use "halogens" and "halide ions" interchangeably, and
write displacement products with the wrong suffix class — "chlorine displaces bromide
and iodide" instead of "displaces bromine and iodine".
**Why it occurs:** The -ine (element) vs -ide (ion) distinction is a naming-layer rule
sitting on top of genuinely-understood chemistry; examiners note it recurs year on year.
**Correct understanding:** Halogens are the elements (Cl2, Br2, I2); halide ions are
their anions (Cl−, Br−, I−). A more reactive halogen displaces a less reactive halogen
(the element) from its halide solution.
**Typical manifestation:** "Chlorine displaces bromide"; "halide ions" where the
element is meant; confusion flagged by examiners in two different questions of the same
series.
**Diagnostic signals:** Displacement equations and word equations; ask candidates to
label every species as element or ion before writing.
**Intervention ideas:** -ine/-ide suffix table drill; insist on species-type labelling
in displacement answers; examiners' own advice: "use the correct terminology when
describing these reactions".
**Evidence:** Pearson examiner reports June 2023 4CH1/1C, Q07(d) (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p3) and
4CH1/2CR, Introduction (SRC-ER-4CH1, 2023-06/4CH1-2CR/er.pdf p3): "confusion between halogens and
halide ions… an on-going issue"; and November 2023 4CH1/2C, Question 1 (SRC-ER-4CH1, 2023-11/4CH1-2C/er.pdf p3):
"stating that chlorine displaces bromide and iodide is incorrect rather than displaces
bromine and iodine."

### MIS-005 — Bonds vs intermolecular forces

**Concepts:** covalent bonding; intermolecular forces; physical properties
**Specification Points:** 1.38, 1.39
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1 and Paper 2; explain-the-property items; long-answer.
**Misconception:** Candidates attribute differences in melting/boiling behaviour — and
more generally any property difference between molecular substances — to breaking the
covalent bonds between atoms, or reach for "intermolecular forces" as an incantation
where the question needs precise, correct use.
**Why it occurs:** Two distinct concepts (intra-molecular bonds vs inter-molecular
forces) share one word in everyday speech ("bonds hold it together") and both live in
the same topic neighbourhood.
**Correct understanding:** Simple molecular substances are separated at melting/boiling
by overcoming intermolecular forces, not the covalent bonds; the covalent bonds within
molecules remain intact through a state change.
**Typical manifestation:** "The covalent bonds break when it melts"; or "intermolecular
forces" used vaguely/incorrectly in long answers — examiners flag "incorrect use of
intermolecular forces" as a terminology failure in extended responses.
**Diagnostic signals:** Ask "what breaks when X melts/boils"; audit long answers for
the exact phrase usage.
**Intervention ideas:** Diagram drill: two molecules with a bond inside each and a
force between them — label what is overcome at the boiling point; examiner-worded model
sentences.
**Evidence:** Pearson examiner reports June 2023 4CH1/1C, Introduction (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p3):
"Some candidates also do not fully understand the difference between a
bond between two atoms in a molecule, and an intermolecular force between molecules";
and June 2025 4CH1/1C, Introduction (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p3) — long-response candidates "lacked a
firm grasp of key terminology (eg incorrect use of intermolecular forces)".

### MIS-006 — Premature rounding and truncation in calculations

**Concepts:** relative atomic mass; moles; significant figures
**Specification Points:** 1.26, 1.31
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Both papers; calculation chains (RAM from isotopes, mole
calculations).
**Misconception:** Candidates round or truncate intermediate values (e.g. displaying
0.36 as 0.3) and carry the damage forward; in RAM-from-isotopes items, some round the
answer to the most abundant isotope's mass number — defeating the purpose of the
calculation.
**Why it occurs:** Calculator-display habits and a belief that "one decimal place"
applies throughout rather than to the final reported answer.
**Correct understanding:** Carry at least the significant figures of the question data
through all intermediates; round only the final answer (to the requested precision).
**Typical manifestation:** 0.36 shown as 0.3; an average atomic mass "rounded" to the
mass number of the dominant isotope.
**Diagnostic signals:** Multi-step calculation items; inspect intermediate values on
the script.
**Intervention ideas:** "Round once, at the end" rule; examiner advice verbatim:
"work to at least the same number of significant figures as the data in the question".
**Evidence:** Pearson examiner report June 2023 4CH1/1C, Introduction (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p3):
"lost marks through rounding their answer too early, or by truncating the
answer on their calculator screen eg by showing 0.36 as 0.3"; and June 2019 4CH1/2CR,
Question 2 (SRC-ER-4CH1, 2019-06/4CH1-2CR/er.pdf p3) — rounding the RAM answer "defeats the purpose of doing the
calculation"; and June 2025 4CH1/2CR, Introduction (SRC-ER-4CH1, 2025-06/4CH1-2CR/er.pdf p3) — "a significant number
of candidates lost marks through simple rounding errors".

### MIS-007 — Stoichiometric ratio: neglected or double-counted

**Concepts:** mole calculations; stoichiometry; reacting ratios
**Specification Points:** 1.31, 1.42
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Both papers; mole and mass calculation chains.
**Misconception:** Two mirror-image failure modes: (a) ignoring the equation's
stoichiometric ratio entirely and using a 1:1 mole relationship; (b) applying the ratio
twice — once inside the Mr and again in the mole conversion.
**Why it occurs:** The ratio lives in the equation, not the arithmetic habit; candidates
who memorised a "divide by Mr, multiply by ratio" recipe mis-file which step carries it.
**Correct understanding:** Convert mass → moles with plain Mr; apply the equation's
ratio ONCE at the mole stage; convert back.
**Typical manifestation:** Correct method, wrong factor of 2/3; or Mr "adjusted" by the
ratio and the ratio applied again later.
**Diagnostic signals:** Any multi-step mole question; check where the ratio entered
the working.
**Intervention ideas:** Mole-map (mass ↔ moles ↔ ratio ↔ moles ↔ mass) with the ratio
labelled at exactly one step; error-carried-forward awareness so a ratio slip costs one
mark, not the chain.
**Evidence:** Pearson examiner reports June 2022 4CH1/1C, Introduction (SRC-ER-4CH1, 2022-06/4CH1-1C/er.pdf p3) —
"Ratios in equations were a problem for some candidates and this was often
missed"; June 2023 4CH1/2CR, Introduction (SRC-ER-4CH1, 2023-06/4CH1-2CR/er.pdf p3) — "consider the ratio only once…
but then consider it again later"; June 2024 4CH1/2CR, Introduction (SRC-ER-4CH1, 2024-06/4CH1-2CR/er.pdf p3) —
"the stoichiometric ratio was neglected".

### MIS-008 — Practical chemistry under-preparation (AO3 strand)

**Concepts:** practical techniques; observations; method evaluation
**Specification Points:** 1.7C, 1.13, 2.44C (Core Practical strand)
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Both papers; practical-context questions in unfamiliar settings.
**Misconception (cluster):** Candidates underperform on practical-grounded questions —
not from single wrong ideas but from thin laboratory experience: unfamiliar contexts
defeat them even when the underlying chemistry is known, qualitative answers lack
specific detail, and method-improvement reasoning fails on error direction.
**Why it occurs:** Exam questions assess practical skills on paper; candidates with
little hands-on work cannot import the sensory and procedural detail the answers need.
**Correct understanding:** Core Practical experience transfers to unfamiliar contexts
when the technique's purpose, key observations and error sources are explicitly
connected.
**Typical manifestation:** Strong theory scores beside weak practical-context scores in
the same script; vague observations; missing direction-of-error reasoning.
**Diagnostic signals:** Practical-context items answered below the same candidate's
theory average; examiner flag "questions involving practical work… tended to score
lower marks than more theoretical questions".
**Intervention ideas:** Map every Core Practical to its likely unfamiliar-context
variant; require direction-of-error statements in evaluation practice; examiners'
advice: "candidates need plenty of experience in doing chemistry experiments".
**Evidence:** Pearson examiner reports June 2019 4CH1/1C, Introduction (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p3);
June 2023 4CH1/1CR, Introduction (SRC-ER-4CH1, 2023-06/4CH1-1CR/er.pdf p3) — "many candidates had done very little
practical work"; June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1, 2024-06/4CH1-1CR/er.pdf p3); June 2025 4CH1/1C,
Introduction (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf p3) — practical questions "showed the greatest variation in
performance… qualitative analysis as a key area for improvement within AO3".

### MIS-009 — Extended-response answers: unlinked chains and vague prose

**Concepts:** extended writing; explanation quality
**Specification Points:** (assessment-skill strand; AO1/AO2 long-answer items)
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** 4–6 mark explanation questions on both papers.
**Misconception (cluster):** Candidates produce correct chemistry fragments that are
not linked into the causal chain the marks demand, answer beside the question actually
asked, or write too vaguely to earn precision marks.
**Why it occurs:** Long answers are drafted as fact dumps; linking words and
question-mapping are not rehearsed as skills.
**Correct understanding:** Each mark is a linked step: identify → because → so →
therefore; the answer must walk the chain the question names.
**Typical manifestation:** All facts present, few marks awarded; examiners: candidates
"did not answer the question given", "were often too vague", "needed to link the
statements to gain all the marks".
**Diagnostic signals:** 4+ mark explanations; compare script content against mark-scheme
chain steps.
**Intervention ideas:** Draft-then-tick practice (examiners' own advice: "draft their
ideas first or tick parts of the question off when they appear in the answer"); chain
scaffolds.
**Evidence:** Pearson examiner reports June 2022 4CH1/1C, Introduction (SRC-ER-4CH1, 2022-06/4CH1-1C/er.pdf p3);
June 2022 4CH1/2C, Introduction (SRC-ER-4CH1, 2022-06/4CH1-2C/er.pdf p3); June 2024 4CH1/1CR, Introduction (SRC-ER-4CH1, 2024-06/4CH1-1CR/er.pdf
p3).

### MIS-010 — Metallic/ionic conduction and "the ions move"

**Concepts:** metallic bonding; ionic bonding; electrical conductivity
**Specification Points:** 1.37, 1.38
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1 (core bonding statements); Paper 2 conductivity items.
**Misconception:** In conduction explanations, candidates say "the ions move" (or just
"electrons carry charge") instead of naming the correct mobile species and structure:
metallic layers slide (malleability) and delocalised electrons move (conduction); in
ionic conduction the ions move, in metallic conduction the electrons do.
**Why it occurs:** "Charged things move" is over-generalised; the structure→property
chain is memorised per-material rather than reasoned from the model.
**Correct understanding:** Metal: fixed positive ions in layers + delocalised electrons
that move and carry charge; molten/aqueous ionic compound: the ions themselves move.
Layers sliding (not ions or electrons) explains malleability.
**Typical manifestation:** "The ions slide over each other" for malleability; "ions
move" for metallic conduction; "electrons carried charge" without movement.
**Diagnostic signals:** Ask conduction and malleability in one item and cross-check the
mobile species named in each answer.
**Intervention ideas:** Species-table drill (which particles move where); examiner
wording as model answers ("layers moved and slid over each other"; "delocalised
electrons" moving).
**Evidence:** Pearson examiner report November 2024 4CH1/2C, Question 2 (SRC-ER-4CH1, 2024-11/4CH1-2C/er.pdf p3) —
marks lost "for stating that the ions moved"; malleability answers
"started saying that electrons moved or slid"; and June 2025 4CH1/2CR, Introduction
(SRC-ER-4CH1, 2025-06/4CH1-2CR/er.pdf p3) — "imprecise terminology related to metallic and ionic bonding led to lower
average marks".

### MIS-011 — Naming rust: oxidation states omitted

**Concepts:** rusting; oxidation states; nomenclature
**Specification Points:** 2.17, 2.18
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1; recall/naming items in corrosion contexts.
**Misconception:** Candidates name rust as "iron oxide", "iron hydroxide", or give a
process word ("oxidation") where the chemical name with oxidation state is required;
others know the oxide idea but omit the (III) state and score zero.
**Why it occurs:** Everyday word "rust" carries no oxidation-state information;
candidates under-rehearse the naming convention as an examinable fact.
**Correct understanding:** Rust is hydrated iron(III) oxide — the chemical name must
carry the oxidation state (iron(III) oxide).
**Typical manifestation:** "iron(II) oxide", "iron hydroxide", "iron oxide" with no
state, or "oxidation" as the name.
**Diagnostic signals:** Any corrosion question; require the full chemical name.
**Intervention ideas:** Naming-with-oxidation-state drill on common compounds; contrast
iron(II) vs iron(III) oxide formulas.
**Evidence:** Pearson examiner reports June 2023 4CH1/1C, Q2(a)(i) (SRC-ER-4CH1, 2023-06/4CH1-1C/er.pdf p6) —
"the oxidation state was frequently missing and so no mark was scored";
November 2024 4CH1/1C, Q3(a)(ii) (SRC-ER-4CH1, 2024-11/4CH1-1C/er.pdf p3) — errors "iron(II) oxide, iron hydroxide,
and iron oxide with no oxidation state given".

### MIS-012 — Atomic-structure arithmetic: labels, masses and electron shells

**Concepts:** atomic structure; isotopes; relative atomic mass; electron configuration
**Specification Points:** 1.17, 1.18, 1.19, 1.20
Temporal scope: CURRENT — AUTHORITATIVE
**Assessment context:** Paper 1; subatomic-particle and configuration items.
**Misconception (cluster):** Slips around the atom model: proton/neutron labels
switched on diagrams; total electron count given where configuration is asked; shell
count not mapped to period; isotope-mass calculations done by adding masses without
multiplying by abundances; electron configuration written for the wrong term.
**Why it occurs:** The atom's number vocabulary (protons/neutrons/mass number/
configuration) is dense and label-dependent; under time pressure adjacent labels swap.
**Correct understanding:** Proton number defines identity and period (via shells);
mass number = protons + neutrons; RAM = Σ(isotope mass × fractional abundance);
configuration lists electrons per shell (2,3 for boron — not 5).
**Typical manifestation:** Switched labels still earning partial credit; "5" where
"2,3" was asked; sums instead of weighted means.
**Diagnostic signals:** Particle-diagram items; isotope-table items; period/group
inference items.
**Intervention ideas:** Label-locked diagrams; weighted-mean template; shells↔period
flash questions.
**Intervention note:** spelling of particle names is itself a flagged loss source —
examiners applied "benefit of doubt" but warn on illegibility.
**Evidence:** Pearson examiner reports June 2019 4CH1/2CR, Question 2 (SRC-ER-4CH1, 2019-06/4CH1-2CR/er.pdf p3);
November 2024 4CH1/2C, Question 1 (SRC-ER-4CH1, 2024-11/4CH1-2C/er.pdf p3); June 2025 4CH1/1C, Q1(a)/Q1(b) (SRC-ER-4CH1, 2025-06/4CH1-1C/er.pdf
pp4–5).

## Evidence / Source Basis

- **Primary evidence:** SRC-ER-4CH1 — the official Pearson examiner
  reports of record: 23 clean reports across seven sessions (2019-06, 2022-06,
  2023-06, 2023-11, 2024-06, 2024-11, 2025-06; papers 1C/2C/1CR/2CR as held),
  bounded page excerpts with page locators in the run's evidence pack (pack sha256
  of record in the run manifest); paper/session identity per the ER titles.
- **Paper/session identity:** SRC-QPMS-4CH1 — the official QP/MS
  corpus of record; cited for paper/session identity context (each ER is commentary on
  its own paper), identity row in the pack.
- **SUPPLEMENTARY (identity):** SRC-TL-4CH1 — official teaching-and-learning corpus;
  identity row only (no prose claims grounded on it here).

## Limitations / Coverage Gaps

- **No public ER exists** for 4CH1 sessions 2020-01, 2020-11, 2021-01, 2021-11,
  2022-01, 2023-01 (COVID-era + January/November publishing; zero Pearson catalog
  rows) and 2021-06 (cancelled series); Nov-2025/June-2026 PEFs sit behind Pearson's
  silver tier. The atlas covers exactly the seven clean sessions of record — nothing
  is extrapolated across the gaps.
- **Extraction-quality disclosure:** the June 2024 Paper 1C report is excluded of
  record as OCR-garbled (embedded-font text-extraction failure observed at intake;
  exclusion carried forward from RUN-001 and consistent with the RUN-009
  examiner-report census of record), so no record grounds on it; that session's
  1CR/2C/2CR introductions ground their records normally.
- The pack carries bounded excerpts (identity covers and page-3 introductions for the
  23 clean reports of record; deeper question-level pages for June 2023 1C (p6) and
  June 2025 1C (pp4–5)), so records reflect the granularity the pack holds;
  question-level nuance beyond those pages is not claimed.
- Examiner sentiment is session-specific commentary, not a controlled study; recurrence
  across series (stated where examiners say so) is the atlas's only trend evidence.
- Mark-scheme-side error patterns belong to the MS family and are deliberately not
  asserted here (no examiner sentiment synthesized from mark schemes).

## Research Status

status: GENERATED (research artifact; not educational truth). v1.1 remediation
generated under SIB-CHEMISTRY_4CH1-RUN-010 (operator order trace 1a178e533eaa1b81),
grounded exclusively on the run's MIS-01 evidence pack. Remediation of record: the
corpus statement aligned to the examiner-report census of record — 23 clean reports
across the seven sessions with public ERs, the garbled June 2024 Paper 1C report
excluded (v1.0 stated "24 reports across the 8 sessions" while listing seven sessions
and counting the garbled file); evidence citations upgraded to the r4 binding grammar
(same sources, pages and quotes). Current/legacy separation: fully CURRENT assessment
evidence; no legacy claims (legacy ER corpus exists separately for HIS/EXM).
Determinism: content fingerprint recorded in the run manifest; regeneration produces a
new artifact_version.
