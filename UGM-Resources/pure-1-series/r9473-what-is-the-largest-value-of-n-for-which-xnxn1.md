---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9473
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9473
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9473
  old_site_id: Q90
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q1C
task: T-UGM-IMPORT-6
---

# What is the largest value of $n$ for which $x_n>x_{n+1}$?

## Question

The sequence \(x_n\) is given by the formula \[x_n=n^3-9n^2+631.\]

The largest value of \(n\) for which \(x_n>x_{n+1}\) is

1. 5;

---

1. 7;

---

1. 11;

---

1. 17.

## Suggestion

How else could we write \(x_n>x_{n+1}\)? Can we use this to form an inequality in \(n\)?

## Solution

We see that \(x_n>x_{n+1}\) is equivalent to saying \(x_n-x_{n+1}>0\).

So we solve this inequality for

\(n\)

: we have

\[\begin{align*} & n^3-9n^2+631-[(n+1)^3-9(n+1)^2+631] > 0 \\ & \iff n^3-9n^2+631-(n^3+3n^2+3n+1-9n^2-18n-9+631) > 0 \\ & \iff -3n^2+15n+8 > 0 \\ & \iff 3n^2-15n-8 < 0. \end{align*}\]

Using the quadratic formula, the solution to

\(3n^2-15n-8=0\)

is

\[\begin{align*} n &= \frac{15\pm\sqrt{15^2-4\times 3\times(-8)}}{6} \\ &= \frac{15\pm\sqrt{225+96}}{6} \\ &= \frac{15\pm\sqrt{321}}{6}. \end{align*}\]

So the values of \(n\) satisfying the inequality are \[\frac{15-\sqrt{321}}{6} < n < \frac{15+\sqrt{321}}{6} \approx 5.49.\] This implies that \(n=5\) is the largest integer in the range.

Hence the answer required is (a).

Check: \(x_4 =551, x_5 =531 , x_6 = 523, x_7= 533.\)
