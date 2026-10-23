---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9884
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9884
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9884
  old_site_id: Q181
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
  exam_reference: UCLES A level Pure Mathematics 1, 1981, Q1
task: T-UGM-IMPORT-6
---

# Can we prove that $\sum_{i=1}^n H_i=n^3?$

## Question

A sequence of numbers \(H_1\), \(H_2\), \(H_3\), … is defined as follows: \(H_1=1\) and \(H_n=H_{n-1}+6(n-1)\) for \(n \ge 2\).

1. Write down the numerical values of \(H_2\), \(H_3\) and \(H_4\).

---

1. Find an expression for \(H_n\) in terms of \(n\).

---

1. Prove that \[\sum_{i=1}^n H_i=n^3.\]

## Suggestion

Can we write \(H_n\) in terms of the previous \(H_i\)?

## Solution

\[\begin{align*} H_2&=H_1+6\times 1=1+6=7.\\ H_3&=H_2+6\times2=7+12=19.\\ H_4&=H_3+6\times 3=19+18=37. \end{align*}\]

We begin by working out what \(H_n\) is in terms of the earlier \(H_i\) values, and then use the formula for the sum of the integers from \(1\) to \(n-1\):

\[\begin{align*} H_n&=H_{n-1}+6(n-1)\\ &=H_{n-2}+6(n-2)+6(n-1)\\ &=\cdots\\ &=H_1+6\times1+6\times2+\cdots+6(n-2)+6(n-1)\\ &=H_1+6\sum_{i=1}^{n-1}i\\ &=1+6\times\frac{1}{2}n(n-1)\\ &=3n^2-3n+1. \end{align*}\]

We have

\[\begin{align*} \sum_{i=1}^n H_i&=\sum_{i=1}^n (3i^2-3i+1)\\ &=3\sum_{i=1}^n i^2 -3\sum_{i=1}^n i +\sum_{i=1}^n1\\ &=3\times \tfrac{1}{6}n(n+1)(2n+1)-3\times\tfrac{1}{2}n(n+1)+n\\ &=\tfrac{1}{2} n\bigl((n+1)(2n+1)-3(n+1)+2\bigr)\\ &=\tfrac{1}{2} n(2n^2+3n+1-3n-3+2)\\ &=\tfrac{1}{2} n(2n^2)\\ &=n^3 \end{align*}\]

as required.
