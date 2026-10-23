---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6257
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6257
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6257
  old_site_id: Q136
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: sum of first 2n terms of 1,1,2,1/2,4,1/4,... by separating the two interleaved GPs —
        GP sum formula twice
      rationale: 'Canonical UGM title: "Can we sum the first $2n$ terms of $1,1,2,\frac{1}{2},4,\frac{1}{4},8,\frac{1}{8},..$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2010, Q1B'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q1B
task: T-UGM-IMPORT-6
---

# Can we sum the first $2n$ terms of $1,1,2,\frac{1}{2},4,\frac{1}{4},8,\frac{1}{8},..$?

## Question

The sum of the first \(2n\) terms of \[1,1,2,\frac{1}{2},4,\frac{1}{4},8,\frac{1}{8},16,\frac{1}{16},..\] is

1. \(2^n+1-2^{1-n}\),

---

1. \(2^n+2^{-n}\),

---

1. \(2^{2n}-2^{3-2n}\),

---

1. \(\frac{2^n-2^{-n}}{3}\).

## Suggestion

Could we separate the sequence into two sub-sequences?

What kind of sequences do we have here?

Do we know a formula that helps us sum these sequences?

## Solution

Firstly, we notice we can separate the terms of this sequence into

\[[1,2,4,8,16,..]+\left[1,\frac{1}{2},\frac{1}{4},\frac{1}{8},\frac{1}{16},..\right].\]

We can safely do this because we are asked only to find the sum of the first \(2n\) terms.

If we’d been asked to find the sum to infinity of a sequence like this, than separating the sequence into brackets can sometimes give some strange answers!

For example, look what happens if we try to find the sum to infinity of the sequence \[1 -1 + 1-1+1-1+1....\]

We have

\[(1 -1) + (1-1)+(1-1)+(1-1)+...= 0,\] while \[1 +(-1 + 1)+(-1+1)+(-1+1)...= 1.\]

Which is right?

So the sum of \(2n\) terms of the sequence is the combined sum of the first \(n\) terms of each of these two geometric progressions.

We know that given a geometric sequence with first term \(a\) and common ratio \(r\), the sum of the first \(n\) terms \(S_n = \dfrac{a(r^n-1)}{r-1} = \dfrac{a(1-r^n)}{1-r}\).

So the sum of \(2n\) terms is \[\dfrac{1(2^n-1)}{2-1}+\dfrac{1\left(1-\left(\dfrac{1}{2}\right)^n\right)}{1-\dfrac{1}{2}} = 2^n -1+2-2^{1-n} = 2^n +1-2^{1-n}.\]

So the answer is (a).
