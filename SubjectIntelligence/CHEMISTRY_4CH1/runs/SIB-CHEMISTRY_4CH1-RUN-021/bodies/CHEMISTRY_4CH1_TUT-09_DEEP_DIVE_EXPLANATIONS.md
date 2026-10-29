---
sib_protocol: SIB-1.0
artifact_id: TUT-09
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
  examiner_reports: false
  supplementary: true

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

# TUT-09 — Deep-Dive Explanations

## Purpose

This artifact assembles the 4CH1 explanations that go beneath the one-line
rule: the book's electrolysis chapter as the model of a chemistry-only deep
explanation, built layer by layer from the conduction model to the reactivity
rule, with the board's topic guides supplying the teaching-depth perspective
and the boundary discipline. Every claim is carried on a bounded,
locator-addressed excerpt from this artifact's own evidence pack.

## Scope

**Covers:** the conduction precondition; the electrolysis/electrolyte
definitions; the molten lead(II) bromide mechanism; the redox framing and
half-equations; the aqueous-versus-molten product switch; the reactivity-series
selection rule; and the topic guides' depth notes (multi-bond boundaries,
equilibrium in flow reactors).

**Out of scope:** the comparison pairs these explanations rest on (TUT-08) and
the practical questioning repertoire (TUT-04).

## Executive Summary

The electrolysis chapter demonstrates the course's deep-explanation pattern:
start from the general conduction precondition (charged particles, free to
move), define the process, walk one complete mechanism (molten lead(II)
bromide), name the redox bookkeeping (OILRIG, half-equations), then explain the
aqueous switch (water as a weak electrolyte) and close with the portable rule
(reactivity series decides the cathode product). The topic guides add the
depth markers: where GCSE deliberately draws boundaries (halogens forming one
bond), and where a common explanation is disqualified by reality (the Haber
chamber never reaches equilibrium).

## Main Analysis

### TUT-049 — The deep explanation starts from the conduction precondition, not from electrolysis

**Claim:** the chapter's foundation is the general precondition for conduction —
charged particles that are free to move, electrons or ions — which a tutor
should establish before any electrode chemistry.
**Evidence:** the book states "In order for things to conduct electricity,
there must be charged particles present and these charged particles must be free
to move. The chargedparticles will be either electrons or ions; it is important
that you are clear which one you are talking about."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 355).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-050 — Electrolysis is defined as a chemical change, and the electrolyte carries the ions

**Claim:** the book defines electrolysis as "a chemical change caused by passing
an electric current through a compound which is either molten or in solution."
and the electrolyte as the liquid or solution that undergoes it, with the ion
movement doing both the conducting and the chemistry — the definition pair a
tutor should quote exactly.
**Evidence:** the book states "Electrolysis is a chemical change caused by
passing an electric current through a compound which is either molten or in
solution." and "An electrolyte is a liquid or solution that undergoes
electrolysis. Electrolytes all contain ions." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 357). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-051 — The molten lead(II) bromide mechanism shows the full ion story end to end

**Claim:** the chapter's worked mechanism runs: solid ions locked in the
lattice and unable to conduct; on melting the ions become free; the power
source drives electrons to one electrode; cations pick up electrons at the
cathode (Pb²⁺ + 2e⁻ → Pb) while anions surrender electrons at the anode —
the complete causal chain a tutor can rehearse.
**Evidence:** the book states "The ions are locked tightly in the lattice and
aren't free to move. The solid lead(II) bromide doesn't conduct electricity. As
soon as the solid melts, the ions become free to move around."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 361);
at the cathode "each lead(Il) ion picks up two electrons from the electrode and
forms neutral lead atoms", represented by the half-equation
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 362);
and the key point warns "Do not confuse bromide and bromine."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 364).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-052 — Redox bookkeeping frames the electrodes: OILRIG, half-equations, simultaneous processes

**Claim:** the chapter grounds electrode reactions in the electron-transfer
definitions — oxidation is loss, reduction is gain, memorised as OILRIG — and
explains why the equations are called half-equations: each shows one of the two
simultaneous processes.
**Evidence:** the book states "Oxidation occurs when something loses electrons."
and "Reduction occurs when something gains electrons.", "A way of remembering
this is the mnemonic OILRIG.", and "oxidation and reduction always occur at the
same time: we talk about redox reactions" with each electrode equation showing
"one of the processes occurring" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 367). Temporal scope:
CURRENT — AUTHORITATIVE.

### TUT-053 — The aqueous switch is explained by water's own weak ionisation

**Claim:** the chapter explains why sodium chloride solution gives hydrogen
rather than sodium at the cathode: water ionises slightly ("Water is called a
weak electrolyte"), its H⁺ ions are easier to reduce than the sodium ions
because "sodium is a very reactive metal", and the hydroxide build-up makes the
cathode region alkaline — the mechanistic answer to the course's most common
product-rule surprise.
**Evidence:** the book states "Although chlorine is still formed at the anode,
hydrogen is produced at the cathode rather than sodium. The hydrogen at the
cathode comes from the water." and "Water is called a weak electrolyte. It
ionises very slightly to give hydrogen ions and hydroxide ions"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 377).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-054 — The portable rules and the depth boundary close the explanation

**Claim:** the chapter compresses the mechanism into portable rules — high
reactivity-series metals stay as hydrogen at the cathode, metals below hydrogen
come out, halides give the halogen at the anode — while the topic guides mark
where depth stops: at GCSE the halogens are confined to single bonds, and the
Haber chamber's 15% pass yield shows why answers cannot be linked to the
equilibrium yield.
**Evidence:** the book states "If the metal is high in the reactivity series,
you get hydrogen produced at the cathode instead of the metal." and "If you
have solutions of halides (chlorides, bromides or iodides), you obtain the
halogen (chlorine, bromine or iodine) at the anode."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 385);
the bonding guide notes "at GCSE level the molecules met will be confined to
those in which they form only one bond, a single covalent bond."
(SRC-TL-4CH1, teaching-and-learning-materials/Chemical-bonding---FINAL.pdf p9);
the equilibrium guide states "At a temperature of 450 °C and a pressure of 200
atm, the equilibrium yield of ammonia is 40 %." while the industrial pass yield
"is only about 15 %" and "The answer cannot be linked to the equilibrium yield
of ammonia." (SRC-TL-4CH1,
teaching-and-learning-materials/Chemical-equilibrium---FINAL.pdf p7). Temporal
scope: CURRENT — AUTHORITATIVE.

### TUT-085 — The conduction deep-dive splits the circuit into two carriers and derives the electrode names from the split

**Claim:** The electrolysis deep-dive rests on one structural sentence: electrons flow in the external circuit but ions flow in the electrolyte — two charge carriers exchanging charge at the electrode surfaces. From that split the chapter derives the naming system rather than asserting it: cations are the ions attracted to the cathode, anions those attracted to the anode, and the mnemonic kit (PANiC) exists only to stabilise the electrode polarities that make the derivation bite. The two invariants a tutor can then state without qualification are that reduction always occurs at the cathode and oxidation always occurs at the anode, and that a molten two-element ionic compound yields its metal at the cathode and its non-metal at the anode.
**Evidence:** the carrier split: "Electrons flow in the external circuit but ions flow in the electrolyte." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 365); the polarity mnemonic: "Remember PANiC: positive anode, negative (is) cathode." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 356); the derived names and invariants: "You can probably see now that positive ions are known as cations because they are attracted to the cathode (negative electrode). Negative ions are known as anions because they are attracted to the anode (positive electrode)." and "Reduction always occurs at the cathode and oxidation always occurs at the anode." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 370).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-086 — The deep-dive explains why aqueous products differ from molten products — and names the compound that cannot even be melted

**Claim:** The chapter prices the molten-versus-aqueous difference with a mechanism, not a rule: reactivity is ion-formation tendency, so the more reactive an element the harder its ion is to discharge — which is exactly why hydrogen, not sodium, comes off concentrated brine. The selective discharge then feeds back on the water equilibrium itself: once the hydrogen ions are removed as gas they cannot reform water, and the ionisation becomes a one-way process. The molten route has its own boundary case the tutor can quote verbatim: some compounds decompose before melting, and copper(II) carbonate — breaking to oxide and carbon dioxide on gentle heating — is impossible to melt, so molten electrolysis is simply unavailable for it.
**Evidence:** the selectivity mechanism: "The more reactive something is, the greater tendency it has to form an ion. This means that the more reactive something is, the more difficult it is to turn it back into an atom." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 375); the one-way feedback: "Because the hydrogen ions are discharged (removed from the solution as hydrogen gas), they can no longer react with the hydroxide ions and reform water. The ionisation of the water becomes a one-way process." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 375); the boundary case: "When aqueous solutions are electrolysed the products are not always the same as when molten salts are electrolysed." and "Some break up into simpler substances before their melting point. For example, copper(Il) carbonate breaks into copper(Il) oxide and carbon dioxide, even on gentle heating. It is impossible to melt it." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 372).
Temporal scope: CURRENT — AUTHORITATIVE.

### TUT-087 — The competition and volume-ratio deep-dives show theory meeting its own experimental corrections

**Claim:** Two deep-dives model honest confrontation between the ideal account and the observed one. At the anode of brine, the hydroxide ion is marginally easier to oxidise than the chloride ion — yet chloride dominates because there are so many more of its ions present, a concentration-beats-incentive result the book states without embarrassment, and the chapter then balances the ledger by tracking which ions remain: sodium and hydroxide, so the solution ends as sodium hydroxide. The water electrolysis ratio shows the same honesty: the half-equations fix hydrogen at twice the oxygen's volume, the experiment returns more than double, and the discrepancy is assigned to oxygen's higher solubility — with the pre-saturation run that repairs the measurement. The tutor inherits explanation-plus-fix as one move.
**Evidence:** the competition: "It is slightly easier to remove electrons from (oxidise) the hydroxide ion than from the chloride ion, but there isn't much difference. There are, however, many, many more chloride ions present in the solution, and so it is mainly these that are oxidised at the anode:" with the endgame: "Cl- and H⁺ ions were removed from the solution by being discharged at the electrodes, so we are left with Na+ and OH-, sodium hydroxide solution." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 380); the ratio and its fix: "Twice as much hydrogen is produced as oxygen." and "Actually, when we do this experiment the amount of hydrogen we obtain is more than twice as much as the oxygen. This is because oxygen is more soluble in water than hydrogen." with the repair: "What we sometimes do to stop this happening is to carry out the electrolysis experiment for a few minutes first in order to saturate the water with oxygen and then start to collect the gases; this gives much better results." (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 384).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-BOOK-4CH1-SB1 (the parse v3 corpus — the electrolysis
chapter's conduction introduction, definitions, lead(II) bromide mechanism,
redox framing, sodium chloride solution and other-solutions pages).
Supplementary: SRC-TL-4CH1 (the bonding topic guide's Period-2 extrapolation
page and the equilibrium topic guide's Haber-process page). SRC-SPEC-4CH1
(change-summary page) and SRC-ER-4CH1 (June 2019 1C report cover page) are held
as single-page identity-presence entries and consumed for no claim. All excerpts
are bounded with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

The pack window holds the electrolysis chapter (41 excerpts) and five topic-guide
pages; energetics and equilibrium deep explanations from the book are outside
this artifact's window (the equilibrium guide's pages excepted) and no claim is
made about them. The OCR layer garbles some subscripts and a fraction-notation
passage; quotes are taken from clean spans only. The electrolysis chapter's
quantitative electrolysis section is packed but not claimed here. No canonical
planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-008 (BL-008 pass 8) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-021 (D3 REQUIRED-core depth pass, tranche 5: TUT): +3 records (TUT-085..TUT-087), zero-append mining of the carried pack of record on the OCR text-of-record basis resolved by operator ruling (gate_resolution_sb1_ebook.json); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

