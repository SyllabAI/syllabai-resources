---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9800
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9800
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9800
  old_site_id: Q179
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2012, Q1B
task: T-UGM-IMPORT-6
---

# When will  $N$ definitely be a square number?

## Question

*[Choose the one correct answer and explain your reasoning.]*

Let \(N=2^k\times4^m\times8^n\)where \(k,m,n\) are positive whole numbers. Then \(N\) will definitely be a square number whenever

1. \(k\) is even;

---

1. \(k+n\) is odd;

---

1. \(k\) is odd but \(m+n\) is even;

---

1. \(k+n\) is even.

## Suggestion

When is a number a square? How else can we write the factors to help us?

## Solution

We’ll start by rewriting all the terms as powers of \(2\).

By doing this, we will get \[N=2^k\times2^{2m}\times 2^{3n}\Longrightarrow N=2^{k+2m+3n}.\]

Since square numbers are all of the form \(x^{y}\), where \(y\) is an even number, \(N\) will be a square number when \(k+2m+3n\) is even.

That is, as \(2m+2n\) is always even, when \(k+n\) is even so the answer is (d).

Alternatively, we could have noticed that \(4^m\) is already a square, as \(4^m=\left(2^m\right)^2\), and rewrite \(8^n\) as \(4^n\times2^n\).

Since \(4^n\) is also a square, for \(N\) to be a square we will need only \(2^k\times 2^n=2^{k+n}\) to be a square, and, therefore, \(k+n\) to be even.
