---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5344
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5344
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5344
  old_site_id: Q165
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q6
task: T-UGM-IMPORT-6
---

# Who broke the vase?

## Question

Alice, Bob, Charlie and Diane are playing together when one of them breaks a precious vase. They all know who broke the vase. When questioned they make the following statements:

**Alice**: It was Bob.
 **Bob**: It was Diane.
 **Charlie**: It was not me.
 **Diane**: What Bob says is wrong.

Each statement is either true or false.

1. Explain why at least one of the four must be lying.

---

1. Explain why at least one of them must be telling the truth.

---

1. Let us suppose that exactly one of the four is lying, so the other three are telling the truth. Who is lying? Who did break the vase? Explain your answer.

---

1. Let us now suppose that exactly one of the four is telling the truth, so the other three are lying. Who is telling the truth? Who did break the vase? Explain your answer.

---

1. Let us now suppose that two of the statements are true and two are false. List the people who might now have broken the vase. Justify your answers.

---

1. Hence show that if we don’t know how many of the four statements are true, then any one of the four could have broken the vase.

## Solution

Alice, Bob, Charlie and Diane are playing together when one of them breaks a precious vase. They all know who broke the vase. When questioned they make the following statements:

Alice: It was Bob.
 Bob: It was Diane.
 Charlie: It was not me.
 Diane: What Bob says is wrong.

Each statement is either true or false.

Let’s look at Diane. If she’s telling the truth, then Bob is lying, while if Bob is telling the truth, then she’s lying.

Therefore Diane or Bob is lying.

Let’s look at Diane again. If she’s not telling the truth, then Bob must be telling the truth, and vice versa.

Therefore Diane or Bob is telling the truth.

As we worked out above, if there is exactly one liar, it must be either Bob or Diane.

Let’s suppose first that Diane is the liar, so Bob is telling the truth. This means that Diane is the culprit.

But this means that Alice is also lying, so we have at least two liars, which is a contradiction.

However, if Bob is the liar, all the other statements are consistent.

Alice (truthfully) says that the culprit is Bob, Bob is lying when he says the culprit is Diane, Charlie is truthful in saying that he was not responsible, and Diane is truthful in saying that Bob is wrong.

So in this situation, Bob broke the vase, and is the liar.

We know either Bob or Diane must be the truth-teller.

Suppose that Bob is telling the truth, so Diane is the culprit. Then Charlie is also telling the truth - he didn’t break the vase.

So we have at least two people telling the truth, which is a contradiction.

However, if Diane is the one telling the truth, this implies that Bob is lying. Charlie must be lying, which means that he was responsible for the breakage.

Alice is also lying, so in this situation, Diane is telling the truth, and Charlie broke the vase.

Let’s introduce some notation: we’ll write, for example, TFTF if Alice tells the truth, Bob lies, Charlie tells the truth, and Diane lies.

The possible combinations are TTFF, TFTF, FTFT, FFTT, TFFT, FTTF. Let’s work out which of these are consistent.

First, exactly one of Bob and Diane must be telling the truth, while the other is lying. This eliminates TFTF and FTFT.

TTFF is not possible: Alice and Bob can’t both be telling the truth, otherwise we have two different culprits.

We can also rule out TFFT, since if Charlie is lying, he was in fact the culprit. But this contradicts Alice’s statement that Bob is responsible.

However, FFTT and FTTF are both consistent.

In the first case, it was not Bob, Diane or Charlie, so Alice was responsible.

In the second case, Bob’s statement that Diane broke the vase is true (and Charlie backs this up, as does the falsehood of Alice’s statement).

So either Alice or Diane broke the vase.

As we’ve shown above,

1. if one child is lying, Bob broke the vase,

---

1. if two children are lying, either Alice or Diane broke the vase, and

---

1. if three children are lying, then Charlie broke the vase.

So if we don’t know how many of the children are lying, it is possible that any of them could have broken the vase.
