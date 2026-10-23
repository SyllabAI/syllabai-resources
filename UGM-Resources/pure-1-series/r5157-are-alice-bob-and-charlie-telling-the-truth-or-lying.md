---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5157
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5157
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5157
  old_site_id: Q200
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q6
task: T-UGM-IMPORT-6
---

# Are Alice, Bob and Charlie telling the truth, or lying?

## Question

1. Alice, Bob, and Charlie make the following statements: Alice: Bob is lying.
 Bob: Charlie is lying.
 Charlie: 1 + 1 = 2. Who is telling the truth? Who is lying? Explain your answer.

---

1. Now Alice, Bob, and Charlie make the following statements: Alice: Bob is telling the truth.
 Bob: Alice is telling the truth.
 Charlie: Alice is lying. What are the possible numbers of people telling the truth? Explain your answer.

---

1. They now make the following statements: Alice: Bob and Charlie are both lying.
 Bob: Alice is telling the truth or Charlie is lying (or both).
 Charlie: Alice and Bob are both telling the truth. Who is telling the truth and who is lying on this occasion? Explain your answer.

## Solution

*We take ‘lying’ here as meaning, ‘saying something untrue’.*

Certainly Charlie is telling the truth.

Bob says Charlie is lying, so he must himself be lying.

Alice says that Bob is lying, which we have just shown to be true.

So Alice and Charlie are telling the truth, and Bob is lying.

A more condensed version of this could read:

Charlie is clearly telling the truth, so Bob is lying, which means Alice is telling the truth.

Let’s introduce some notation: write, for example, TFT to describe the situation where Alice is telling the truth, Bob is lying, and Charlie is telling the truth.

Looking at the statements above, Bob and Charlie contradict one another, but one of them must be telling the truth (Alice is either telling the truth or lying!).

So either Bob or Charlie is telling the truth, and the other is lying. This narrows down our possible situations to TFT,FFT, TTF, FTF.

From the first and second statements, Alice and Bob must both be telling the truth, or both lying (if, for example, Alice is telling the truth and Bob is not, we reach a contradiction).

This narrows down possible situations further to FFT and TTF. In each of these cases, all three are consistent, so either one or two people are lying.

**An alternative version without notation**

They cannot all be telling the truth, and they cannot all be lying. Bob and Charlie must be opposites.

Alice and Bob telling the truth and Charlie lying is consistent, as is Alice and Bob lying and Charlie telling the truth.

So there can be either one or two people telling the truth.

Looking at Charlie’s statement, either Charlie is telling the truth, and so everyone is telling the truth, or Charlie is lying, and either Alice or Bob (or both) is lying.

So we have narrowed down our possibilities to TTT, FTF, TFF, FFF.

Looking at Alice’s statement, if Alice is telling the truth, Bob and Charlie are not, ruling out TTT.

If Alice is lying, either Bob or Charlie (or both) are telling the truth, ruling out FFF. So we are only left with FTF and TFF.

Looking at Bob’s statement, if Bob is lying then Alice is lying **and** Charlie is telling the truth. This rules out TFF.

This leaves FTF, which is consistent with Bob’s statement, and is therefore the correct solution. Hence Bob is telling the truth, and Alice and Charlie are lying.

A condensed version of this argument could read, if Alice is telling the truth, then Bob’s statement is also true, contradicting Alice.

So Alice is lying, which makes Bob’s statement true, and Charlie’s statement a lie.

The form of “or” used in Bob’s statement here, which includes the possibility of “both”, is the usual mathematical/logical definition of the term “or”.

If we have a statement \(S\) of the form “\(A\) is true or \(C\) is true”, and we decide \(S\) is false, this is the same as saying that the statement \(T\) which says that “\(A\) is false and \(C\) is false” IS true.

If you know a little about logical notation, we can write this rule as \[\neg(A\vee C) \iff (\neg A) \wedge (\neg C),\] where \(\neg =\) NOT, and \(\wedge =\) AND, and \(\vee =\) OR.

This is known as one of de Morgan’s laws—the other is \[\neg(A \wedge C) \iff (\neg A)\vee (\neg C).\]

What this rule tells us in this case is that if Bob’s statement is false, then both Alice is not telling the truth and Charlie is not lying.
