---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7031
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7031
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7031
  old_site_id: Q215
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
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: worst case at n=1 then arithmetic-series sum 2+3+⋯+101 = 100(2+101)/2 = 5150 — the AP
        sum is the load-bearing computation in a STEP-style MC
      rationale: 'Canonical UGM title: "If $f(n) > k$ for all $n \geq 1$, what can we say about $k$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2007, Q1J'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q1J
task: T-UGM-IMPORT-6
---

# If $f(n) > k$ for all $n \geq 1$, what can we say about $k$?

## Question

*[Choose the one correct answer and explain your reasoning.]*

The inequality \[(n+1) + \bigl(n^4+2\bigr) + \bigl(n^9+3\bigr) + \bigl(n^{16}+4\bigr) + \cdots + \bigl(n^{10000}+100\bigr) > k\] is true for all \(n\ge 1\). It follows that

1. \(k < 1300\),

---

1. \(k^2<101\),

---

1. \(k \ge 101^{10000}\),

---

1. \(k < 5150\).

## Suggestion

What happens when \(n=1\)?

What happens to the LHS when \(n=2\)? Is it bigger or smaller than for the case \(n=1\)?

## Solution

To make this a lot simpler, note that the expression

\[(n+1) + \bigl(n^4+2\bigr) + \bigl(n^9+3\bigr) + \bigl(n^{16}+4\bigr) + \cdots + \bigl(n^{10000}+100\bigr)\]

increases as

\(n\)

increases, so the inequality holds for all

\(n \ge 1\)

if it holds for

\(n = 1\)

. So we need

\[\begin{align*} &(1+1)+(1+2)+(1+3)+(1+4)+\cdots +(1+100) > k\\ \iff\quad& 2+3+4+5+\cdots +101 > k\\ \iff\quad& \frac{100}{2}(2+101) > k\\ \iff\quad& 5150 > k. \end{align*}\]

Hence the answer is (d).

Alternatively, we could have broken up the sum here as \[(1+1+\cdots+1)+(1+2+\cdots+100)=100+\tfrac{1}{2}\times100\times101.\]
