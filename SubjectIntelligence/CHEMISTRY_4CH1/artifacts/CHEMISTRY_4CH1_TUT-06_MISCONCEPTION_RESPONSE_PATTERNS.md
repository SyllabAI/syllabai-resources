---
sib_protocol: SIB-1.0
artifact_id: TUT-06
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
  supplementary: true

status: GENERATED
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

# TUT-06 — Misconception Response Patterns

## Purpose

This artifact assembles the 4CH1 misconception corpus a tutor needs to respond,
not just to correct: the book's own "common mistake" warnings, the board's
topic-guide diagnosis of anthropomorphism, and the examiner-attested
misconceptions from the reports of record. Each record pairs the misconception
with the response formulation the evidence of record itself supplies. Every
claim is carried on a bounded, locator-addressed excerpt from this artifact's
own evidence pack.

## Scope

**Covers:** word-ending and symbol confusions in formulae; the moles-times-two
arithmetic trap; half-equation electron placement; displacement and observation
wording; the equilibrium constant-versus-equal error; the colourless-versus-clear
observation ban; the anthropomorphism diagnosis; and the mass-loss and
activation-energy misreadings attested in the reports.

**Out of scope:** the general hint repertoire (TUT-05) and examiner feedback
beyond misconception attestations (TUT-07).

## Executive Summary

Three layers agree on where 4CH1 students go wrong: the book flags its common
mistakes inline (word endings, moles arithmetic, electron sides), the board's
topic guide names the deepest one (anthropomorphism — atoms that "want"), and
the examiners attest the cost (marble-chip mass-loss misreadings, activation-
energy answers replaced by "solids must melt", colourless called clear). The
response pattern is consistent across all three layers: name the wrong form,
state the correct form, and bind the correct wording to the mark consequence.

## Main Analysis

### TUT-031 — Word endings in formulae are the book's own named most-common mistake

**Claim:** the book identifies careless word endings as the most common
formulae-writing error and responds with a bare caution — the response pattern
for fluency errors is a short, direct warning, not re-teaching.
**Evidence:** the HINT box states "Not looking carefully at word endings is one
of the most common mistakes students make when they start to write formulae. Be
careful!" (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl
line 284). Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-032 — The moles arithmetic trap is corrected by explaining where the coefficient was already used

**Claim:** the book's response to the double-counting error (multiplying by the
mass of 2Fe after the coefficient already entered the mole calculation) is to
show why the step is redundant — the response pattern for arithmetic
misconceptions is a reason, not just a rule.
**Evidence:** the HINT box states "To find the mass of Fe we multiply the number
of moles of Fe by the mass of 1 mole of Fe (56 g). A common mistake is to
multiply the number of moles by the mass of 2Fe (112 g), but we have already
used the '2' when we worked out the number of moles of Fe."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 214).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-033 — Half-equation errors are met with a self-check routine

**Claim:** for the electrons-on-the-wrong-side error the book prescribes a
verification habit — check the charge balance — turning the misconception
response into a routine the student can run unsupervised.
**Evidence:** the HINT box states "A common mistake is to put the electrons on
the wrong side of the halfequation. Check the charges to make sure you have the
same total charge on both sides." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 368). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-034 — Observation and displacement wordings are policed by the book and the examiners together

**Claim:** wording misconceptions — "displaces bromide" instead of "displaces
bromine", "clear" instead of "colourless" — are corrected by stating the
permitted form and the meaning of the banned word, and the equilibrium wording
error ("equal" for "constant") receives the same treatment.
**Evidence:** the book's HINT box states "In the exam you must write 'chlorine
displaces bromine' not 'chlorine displaces bromide'."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 446);
on equilibrium wording: "Be careful with the wording of your answer in the exam
- the concentrations of the reactants and products at equilibrium are constant,
they are not equal." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 833); on observations: "You
must be careful with the words you use here: the final mixture is colourless and
not clear. Do not use the word clear."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 965).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-035 — The board's topic guide names anthropomorphism as the deepest bonding misconception

**Claim:** the bonding topic guide diagnoses the "atoms want" family of
statements as anthropomorphism, explicitly rejects the four statements
candidates should avoid, and supplies the mechanistic replacement — atoms lose
electrons when the environment makes it possible, not because of desire.
**Evidence:** the guide records that "Statements such as 'The sodium atom wants
to lose one electron' are very common." and that "This example of
anthropomorphism (i.e. giving inanimate objects human characteristics) is not
justified.", listing among the statements to avoid "Chemical bonding involves
transferring or sharing electrons in order to achieve the electronic structure
of a noble gas." (SRC-TL-4CH1,
teaching-and-learning-materials/Chemical-bonding---FINAL.pdf p4). Temporal
scope: CURRENT — AUTHORITATIVE.

### TUT-036 — The examiner reports attest the cost of the misconceptions the book warns about

**Claim:** the reports of record confirm the misconception classes with mark
consequences: the marble-chip size misreading and the "acid escaped" response
scored zero, and the activation-energy question was answered with a
"solids must melt" model — demonstrating to a tutor why the book's warnings are
mark-bearing.
**Evidence:** the November 2024 report states "a common misconception was that
the reduction in size of the marble chips caused the reading on the balance to
decrease" and that "Another frequent incorrect response was the suggestion that
hydrochloric acid escaped the flask, which scored zero marks."
(SRC-ER-4CH1, chemistry/4ch1/past-papers/2024-11/4CH1-1C/er.pdf p5); the June
2024 report states "This was a common answer which scored 0 marks. Many
candidates focused on the reactants being solids and the need to melt them
rather than on the high activation energy associated with the chemical
reaction." (SRC-ER-4CH1,
chemistry/4ch1/past-papers/2024-06/4CH1-2CR/er.pdf p5). Temporal scope:
CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — the book's
mistake-flagging HINT boxes across chapters 5, 7, 10, 12, 21 and 25) and
SRC-TL-4CH1 (the bonding topic guide's anthropomorphism page — board-authored
diagnosis). Supplementary: SRC-ER-4CH1 (November 2024 1C and June 2024 2CR
misconception attestations). SRC-SPEC-4CH1 (change-summary page) is held as a
single-page identity-presence entry and consumed for no claim. All excerpts are
bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The book window holds the 26 matches of the mistake-flagging queries; other
misconception carriers (the answer sections, end-of-unit commentary) are outside
the window. The examiner attestation is limited to the two report pages packed;
the broader error census is the MIS family's territory and is not re-claimed
here. The anthropomorphism page's replacement statements are quoted only within
the excerpt window. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
