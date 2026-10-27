---
sib_protocol: SIB-1.0
artifact_id: PED-07
artifact_version: 1.0
subject: Chemistry
qualification: International GCSE
specification: 4CH1
curriculum_version: "2017"

research_family: learning_pedagogy_intelligence
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
  supplementary: true

# lifecycle: GENERATED -> QA_PASSED -> STAGED
status: PUBLISHED
generated_by: zai_agent
generated_at: 2026-10-26

provenance:
  source_manifest: "SRC-BOOK-4CH1-SB1"
  generation_run_id: "SIB-CHEMISTRY_4CH1-RUN-006"
  generator:
    provider: "z.ai"
    model: "GLM"
    agent_version: "SIB-GEN-r0"
  source_revisions:
    syllabai: "357ace0a230f5e0095ad230320af587dca6bb71f"
    syllabai_pastpapers: "3b6a443d4e3643f461a1cca12c6e1ad47ab6b596"
    syllabai_resources: "8b5a64f1b18724208ff19969b002028d3ed41bed"
---

# PED-07 — Interleaving Opportunities

## Purpose

This artifact identifies the interleaving opportunities the 4CH1 evidence of
record builds in: where the materials deliberately re-mix topics, families, and
practical threads rather than teaching them in isolation — the book's
cross-chapter organic threads, LOOKING AHEAD boxes, recurring practical
machinery, and reused rules (SRC-BOOK-4CH1-SB1); the board's side-by-side
mapping guides that expose the same content across qualifications
(SRC-TL-4CH1); and the experimental-skills statements that recur across the
course (SRC-TL-4CH1 Getting Started Guide). Claims ride only on this artifact's
own bounded pack excerpts. Canonical planes are untouched.

## Scope

**Covers:** cross-qualification mapping guides; organic-family thread reuse;
nomenclature decoding as transferable skill; forward-looking boxes; practical
threads recurring across units; reused bond-counting rules; model-kit
manipulation; error-aware practical links; recurring experimental-skills
statements.

**Out of scope:** sequencing order itself (PED-01) and prerequisite repair
(PED-02).

## Executive Summary

Interleaving in the evidence of record runs on two scales. Inside the book,
threads are deliberately re-mixed: the organic family chapters open by recalling
the previous family's reactions, nomenclature is taught as a decodable system
that transfers across every family member, LOOKING AHEAD boxes name the precise
vocabulary of the next level, bond-counting rules learned in bonding reappear as
REMINDERs inside organic drawing tasks, and practical machinery (electrolysis
investigations, oxygen-consumption experiments) recurs with quantitative
upgrades. At board level, two official mapping guides expose the same content
side-by-side — Science (Single/Double) against the separate sciences, and
Cambridge 0620 against 4CH1 — making cross-specification interleaving a planned,
inspectable structure rather than an accident of authorship. The Getting Started
Guide's experimental-skills statements (variables, analysis, communication,
reliability) describe skills that recur across every practical thread.

## Main Analysis

### PED-042 — Side-by-side mapping guides expose cross-qualification structure

**Claim:** the teaching corpus ships two mapping guides that lay content out
side-by-side across specifications, so departments can interleave deliberately
across science courses and entry routes.
**Evidence:** the sciences mapping guide introduces itself as showing
"side-by-side – the content of the Science (Single Award) and the Science (Double
Award) specifications against those for the three separate sciences"
(SRC-TL-4CH1, International-GCSE-Sciences_Mapping-Guide.pdf p 3); the Cambridge
guide is titled as a mapping "from Cambridge International Examinations to
Pearson Edexcel (0620 to 4CH1)" with a qualification-at-a-glance content summary
(SRC-TL-4CH1, Cambridge.IGCSE.Chemistry.Mapped.Against.Edexcel.iG-Final.pdf
p 1, p 2). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-043 — Organic-family threads are taught as one interleaved story

**Claim:** the organic chapters open by explicitly recalling the previous family,
so Unit 4 interleaves families instead of siloing them.
**Evidence:** the carboxylic-acids chapter opens "Previously you have seen how
alcohols can be oxidised to form a class of organic compounds called carboxylic
acids" (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 996);
the alkanes chapter's decode hint shows the naming system as transferable —
"'eth' shows a two-carbon chain. 'ane' shows only carbon-carbon single bonds"
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 964).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-044 — LOOKING AHEAD boxes name the next level precisely

**Claim:** forward-looking boxes sharpen the current topic's vocabulary by naming
what the concept will be called in later study — an interleave with the learner's
future rather than only their past.
**Evidence:** the isomers section's LOOKING AHEAD box states that the isomerism
discussed "should be called structural isomerism" with the same-formula
different-structure definition (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 898). Temporal scope: CURRENT —
AUTHORITATIVE.

### PED-045 — Practical machinery recurs across units

**Claim:** practical threads interleave across the course: electrolysis
investigations return in quantitative form, and oxygen-consumption apparatus
reappears for rusting — the same skills re-mixed with new chemistry.
**Evidence:** the electrolysis chapter carries "PRACTICAL: INVESTIGATING THE
ELECTROLYSIS OF AQUEOUS SOLUTIONS" (SRC-BOOK-4CH1-SB1,
edexcel_igcse_chemistry_chunks_v3.jsonl line 373) and later "PRACTICAL:
QUANTITATIVE ELECTROLYSIS" investigating how much product is obtained
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 390); the
atmosphere chapter reuses gas-volume apparatus to determine oxygen content via
iron rusting (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line
471, line 472). Temporal scope: CURRENT — AUTHORITATIVE.

### PED-046 — Reused rules carry old topics into new ones

**Claim:** a single rule learned early (carbon forms four bonds) is re-delivered
as a REMINDER inside later organic drawing tasks — an interleave of bonding into
organic work.
**Evidence:** the organic structures section REMINDERs that "C always forms four
bonds and H always forms one bond" with oxygen and nitrogen counts added
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 873).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-047 — Model-kit manipulation links structure across topics

**Claim:** the book invites physical manipulation of the same atom set to reveal
structural variety — isomers built by re-joining the same five carbons and twelve
hydrogens — interleaving bonding geometry with organic family structure.
**Evidence:** the isomers section asks learners to pick out five carbon atoms and
twelve hydrogen atoms in a molecular-model set and find the distinct ways to join
them (SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 897).
Temporal scope: CURRENT — AUTHORITATIVE.

### PED-048 — Experimental-skills statements recur across every practical thread

**Claim:** the board's delivery guidance frames a recurring experimental-skills
band — variables, analysis, communication, reliability — that every practical
thread exercises, giving interleaved practice a common skill spine.
**Evidence:** the Getting Started Guide lists the experimental-skill demands
including "identify independent, dependent and control variables" and analysing
data "consistent with the evidence" (SRC-TL-4CH1, gstt-int-gcse-chemistry.pdf
p 10); the book's own enthalpy practical names its error sources — heat loss to
air and vessel — instantiating that reliability band inside a specific thread
(SRC-BOOK-4CH1-SB1, edexcel_igcse_chemistry_chunks_v3.jsonl line 738).
Temporal scope: CURRENT — AUTHORITATIVE.

## Evidence / Source Basis

Primary evidence: SRC-TL-4CH1 (the two mapping guides and the Getting Started
Guide experimental-skills page, plus the identity-pinned scheme of work) and
SRC-BOOK-4CH1-SB1 (organic-thread, LOOKING AHEAD, practical, REMINDER, model-kit
and error chunks at line+chunk-id locators). Supplementary: SRC-SPEC-4CH1
progression pages; SRC-SME-NOTES-4CH1 structured notes; SRC-ER-4CH1 and
SRC-ER-4CH0-LEGACY as identity-presence pages only, consumed for no claim here.
Bounded excerpts with locators preserved; caps enforced by the pack builder.

## Limitations / Coverage Gaps

Interleaving claims are bounded by this pack's query windows; the complete
LOOKING AHEAD and PRACTICAL inventories are neither enumerated nor denied. The
Cambridge mapping guide's row-level equivalences are cited at the
qualification-at-a-glance level its excerpted pages show. OCR-era quirks of the
book parse (doubled skill tags, stray glyphs) are quoted as parsed or
paraphrased, never repaired. The legacy examiner-report entry is present for
identity only; no legacy claim is made. No canonical planes were written.

## Research Status

GENERATED under SIB-CHEMISTRY_4CH1-RUN-006 (BL-008 pass 6) from this artifact's
evidence pack alone; validator of record tools/sib @ 357ace0a; claim QA r3 binds
every citation to a pack excerpt. Research artifact — evidence-backed, not
canonical educational truth.
