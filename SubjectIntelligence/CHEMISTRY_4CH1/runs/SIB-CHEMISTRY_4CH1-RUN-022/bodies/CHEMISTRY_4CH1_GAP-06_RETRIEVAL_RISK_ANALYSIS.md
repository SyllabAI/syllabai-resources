---
sib_protocol: SIB-1.0
artifact_id: GAP-06
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
  examiner_reports: false
  supplementary: false

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

# GAP-06 — Retrieval Risk Analysis

## Purpose

This artifact analyzes retrieval risk for the Pearson Edexcel International
GCSE in Chemistry (4CH1): the places where a student's or a retrieval system's
recall of the course is most likely to fail — content that is examined only on
one paper, book scaffolding that is unevenly distributed, and surfaces that
exist only on one side of the specification/book pair. Every risk claim is
carried on a bounded, locator-addressed excerpt from this artifact's own
evidence pack; risks the pack cannot verify are disclosed as unverified rather
than asserted. Canonical planes are untouched.

## Scope

**Covers:** the paper-split rule as the primary structural risk; the
chemistry-only content concentration on Paper 2C; the distribution of the
book's retrieval surfaces (did-you-know hooks and unit question batteries)
across the four units; and the specification-only suggested-practicals
surface.

**Out of scope:** curriculum mapping detail (GAP-01), assessment-session
census (GAP-03), and misconception response patterns (GAP-04).

## Executive Summary

The specification's own paper rule is the dominant retrieval risk: Paper 1C
assesses only content that is neither bold nor C-referenced, while Paper 2C
assesses all the content — so chemistry-only statements carry examination
consequences on exactly one paper. The book's retrieval surfaces do span all
four units — did-you-know hooks and unit question batteries are present from
States of matter to crude oil — but the batteries carry no paper-level labels,
so a retrieval system keyed on them cannot route questions to the correct
paper without the specification's rule. The specification's Appendix 6
suggested practicals are a further specification-only surface whose book-side
coverage is unaudited in this pack and disclosed as such.

## Main Analysis

### GAP-031 — The paper-split rule is the primary structural retrieval risk: chemistry-only content is examined on exactly one paper

**Claim:** the specification's assessment rule concentrates bold and
C-referenced content onto Paper 2C alone — Paper 1C assesses "the content
that is not in bold and does not have a 'C' reference" while Paper 2C assesses
"all the content, including content that is in bold and has a 'C' reference"
— so retrieval for chemistry-only statements is all-or-nothing by paper, the
highest-leverage risk the of-record corpus documents.
**Evidence:** the specification's assessment page states the Paper 1C rule —
"Assesses the content that is not in bold and does not have a 'C' reference.
Questions may come from any topic area across the specification" — and the
Paper 2C rule — "Assesses all the content, including content that is in bold
and has a 'C' reference" with the note "Bold statements cover some sub-topics
in greater depth" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-032 — The chemistry-only statement surface concentrates in identifiable sub-topics, giving the paper-split rule concrete coordinates

**Claim:** the chemistry-only statements are not diffusely spread: the
specification prints them as C-suffixed clusters in named sub-topics —
metallic bonding (1.52C–1.54C) and electrolysis (1.55C–1.60C) in Topic 1 — so
the paper-split risk resolves to specific teachable coordinates rather than a
general warning.
**Evidence:** the specification's Topic 1 page prints the cluster — "1.52C
know how to represent a metallic lattice by a 2-D diagram 1.53C understand
metallic bonding in terms of electrostatic attractions 1.54C explain typical
physical properties of metals, including electrical conductivity and
malleability" followed by the electrolysis cluster "1.55C understand why
covalent compounds do not conduct electricity" through "1.60C practical:
investigate the electrolysis of aqueous solutions" (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p21). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-033 — The book's did-you-know hook surface spans all four units, but the hooks are context notes, not examined statements

**Claim:** the book carries a did-you-know surface in every unit — from
Periodic Table numbering in Unit 1 to ester smells in Unit 4 — and the hooks
are framed as context — "You will sometimes see Group 0 labelled as Group 8"
and "The old name for ethanoic acid was acetic acid" — rather than as
assessable statements, so a retrieval system must not rank them as core
content; the risk is misclassification, not absence.
**Evidence:** the hooks of record include "DID YOU KNOW? You will sometimes
see Group 0 labelled as Group 8. In more advanced Periodic Tables the groups
are numbered from 1 to 18, including the transition metals."
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 110),
"DID YOU KNOW? Historically alkali metals were put in the same group because
of similarities in properties, before anyone knew anything about electrons!"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 412),
"DID YOU KNOW? Calcium oxide is known as quicklime. Adding water to it is
described as slaking it." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 714) and "DID YOU KNOW?
The old name for ethanoic acid was acetic acid." (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 982). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-034 — The unit question batteries are strong retrieval checkpoints that span all four units but carry no paper-level routing labels

**Claim:** every unit of the book closes with a unit question battery in
examination format — the pack exhibits batteries for Units 1 through 4, with
mark allocations and skill tags — yet none of the batteries of record labels
its questions by paper (1C or 2C), so paper routing cannot be recovered from
the book's own checkpoints and must come from the specification's rule.
**Evidence:** the Unit 1 battery opens "UNIT QUESTIONS You may need to refer
to the Periodic Table on page 320." and runs to "(Total 10 marks)"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 394);
the Unit 2 battery opens with Group 1 storage — "Lithium, sodium and potassium
are three elements in Group 1 of the Periodic Table. All these elements are
stored under oil so that they cannot react with air and water"
(SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 686);
the Unit 3 battery works the hydrogen bromide equilibrium — "Hydrogen, H2, and
bromine, Br2, react vigorously to form hydrogen bromide, HBr" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 849); the Unit 4 battery
opens "Crude oil is a complex mixture of hydrocarbons" (SRC-BOOK-4CH1-SB1,
parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 1057). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-035 — The specification's suggested practicals are a specification-only retrieval surface in this pack

**Claim:** the specification's Appendix 6 lists suggested practical
investigations that are explicitly additional to the main-body practicals —
"additional practical investigations that exemplify the scientific process"
— and this artifact's pack does not include the book pages that would show
whether each suggested practical is worked in the book of record, so their
book-side retrieval coverage is disclosed as unaudited rather than assumed.
**Evidence:** the specification's appendix reads "The following suggestions
are additional practical investigations that exemplify the scientific process.
They can be used to supplement students' understanding of chemistry in
addition to the practical investigations found within the main body of the
content" and lists items — "Investigate the ease of thermal decomposition of
carbonates, including calcium carbonate, zinc carbonate and copper carbonate",
"Investigate the rusting of iron" and "Carry out electrolysis of sea
water/acidified water" among them (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p53). Temporal scope:
CURRENT — AUTHORITATIVE.

### GAP-036 — The risk analysis boundary: book-and-spec grounding only, with the garbled session's feedback unavailable to the analysis

**Claim:** this artifact's risk claims are grounded on the book and
specification alone — the examiner-report and topic-guide sources of record
ride as identity-presence only — and the OCR-garbled June 2024 Paper 1C report
stays excluded of record, so no retrieval-risk finding in this artifact leans
on examiner feedback from that session; both boundaries are disclosed rather
than silently crossed.
**Evidence:** the presence sources identify as "Examiners' Report June 2019
IGCSE Chemistry 4CH1 1C" (SRC-ER-4CH1, 2019-06/4CH1-1C/er.pdf p1) and "TOPIC
GUIDE: Chemical bonding Pearson Edexcel International GCSE in Chemistry (4CH1)
and Science (4SD0 and 4SS0) First teaching 2017" (SRC-TL-4CH1,
Chemical-bonding---FINAL.pdf p1), neither cited for risk content above; the
paper-model page that grounds the structural risk is the specification's
assessment page (SRC-SPEC-4CH1,
international-gcse-chemistry-2017-specification.pdf p33); the June 2024 1C
report is absent from the pack of record consistent with its garbled-OCR
exclusion carried forward from the earlier run. Temporal scope: CURRENT —
AUTHORITATIVE.

### GAP-064 — The Unit 3 battery carries question-block-level CHEMISTRY ONLY bands, giving indirect paper routing that refines the no-labels finding

**Claim:** The Unit 3 question battery is internally banded — a CHEMISTRY ONLY marker opens the bond-energy block, END OF CHEMISTRY ONLY closes it, and a second CHEMISTRY ONLY marker opens the equilibrium block — so while GAP-034's finding stands that no battery question is labelled 1C or 2C, the chemistry-only routing is recoverable indirectly at question-block granularity: combined with the specification's paper-split rule, a C-banded block is examinable on Paper 2C only, which is routing information no other unit battery in the pack exhibits.
**Evidence:** the battery bands — CHEMISTRY ONLY at the bond-energy block (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 850) and END OF CHEMISTRY ONLY two chunks later (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 852); the routing rule that converts the band to paper coordinates — "Assesses all the content, including content that is in bold and has a 'C' reference" (SRC-SPEC-4CH1, international-gcse-chemistry-2017-specification.pdf p33).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-065 — The did-you-know surface extends past the four sampled hooks to stance-carrying and terminology hooks, widening the misclassification risk

**Claim:** Beyond the four hooks sampled at GAP-033, the pack exhibits hooks that carry a contested-claims stance and non-examinable terminology: the climate hook frames a live scientific disagreement, and the hydrogen-peroxide hook introduces the non-SI vol concentration scale used in commerce; a retrieval system that ranks the hook surface as core content would not merely misclassify context as content — it would surface contested framing and commercial units as if they were settled, assessable statements, so the misclassification risk extends from labels to stance.
**Evidence:** the stance hook reads "Although most scientists believe that increases in carbon dioxide will cause devastating climate change, there are others who reject this." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 483); the terminology hooks read "'vol', meaning volume, is a measurement for concentration for hydrogen peroxide." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 813) and "Intermolecular literally means between molecules." (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 323).
Temporal scope: CURRENT — AUTHORITATIVE.

### GAP-066 — The unit batteries carry a book-native skill taxonomy — executive function and decision making among them — with no printed mapping to the assessment objectives

**Claim:** The unit question batteries tag their questions with a book-native skill taxonomy — INTERPRETATION, REASONING, PROBLEM SOLVING, CRITICAL THINKING, ANALYSIS, EXECUTIVE FUNCTION and DECISION MAKING — a skill-dimension retrieval surface that neither the specification's assessment-objective model nor any paper label supplies; the pack prints no mapping between the book's skill tags and the AO classes, so a retrieval system can route by skill but cannot ground that routing in the assessment model, and the mapping is disclosed as unmapped of record.
**Evidence:** the Unit 1 battery tags its questions with the SKILLS line INTERPRETATION, REASONING (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 395); the Unit 2 battery carries the EXECUTIVE FUNCTION tag (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 689) and the DECISION MAKING tag (SRC-BOOK-4CH1-SB1, parsed/edexcel_igcse_chemistry_chunks_v3.jsonl line 694).
Temporal scope: CURRENT — AUTHORITATIVE.
## Evidence / Source Basis

Primary evidence: SRC-SPEC-4CH1 (the chemistry-only statement cluster, p21;
the assessment-information page, p33; the suggested-practicals appendix, p53)
and SRC-BOOK-4CH1-SB1 (the did-you-know hooks and unit question batteries
across all four units). Supplementary: SRC-ER-4CH1 and SRC-TL-4CH1 ride as
one-page identity-presence entries consumed for no risk claim; SRC-ROOT-BOOK-COPIES-4CH1
and SRC-SAMS-4CH1 likewise. All excerpts are bounded with locators preserved;
caps enforced by the pack builder.

## Limitations / Coverage Gaps

Retrieval risk is grounded on the paper-split rule and the book's own
surfaces; no search-log, telemetry or user-behavior corpus exists of record,
so all risk findings are structural, not behavioral. The unit question
batteries are sampled at one battery per unit; inter-unit batteries are
unsampled. Book-side coverage of the Appendix 6 suggested practicals is
unaudited in this pack and disclosed as such.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-009 (BL-009 pass 9) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth. Deepened under SIB-CHEMISTRY_4CH1-RUN-022 (D3 REQUIRED-core depth pass, tranche 6: GAP): +3 records (GAP-064..GAP-066), zero-append mining of the carried pack of record (origin RUN-009) — unmined-window authoring for seven artifacts and held-window authoring with fresh claims for GAP-03, whose unmined surface was exhausted (1/29 excerpts unmined pre-run); every quote self-bound to raw excerpt text before the official gate; claim QA re-bound all citations.

