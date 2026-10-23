---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r5642
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r5642
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5642
  old_site_id: Q4008
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q1F
task: T-UGM-IMPORT-7
---

# When does the trapezium rule give the exact answer here?

## Question

*[Choose the one correct answer and explain your reasoning.]*

The graph \(y=f(x)\) of a function is drawn below for \(0 \le x \le 1\).

The trapezium rule is then used to estimate

\[\displaystyle\int_0^1 \! f(x) \, \mathrm{d}x\]

by dividing \(0 \le x \le 1\) into \(n\) equal intervals. The estimate calculated will equal the actual integral when

1. \(n\) is a multiple of \(4\);

---

1. \(n\) is a multiple of \(6\);

---

1. \(n\) is a multiple of \(8\);

---

1. \(n\) is a multiple of \(12\).

## Suggestion

The notation \[\displaystyle\int_0^1 \! f(x) \, \mathrm{d}x\] means the area between the \(f(x)\) and the \(x\)-axis, from \(x=0\) to \(x=1\).

## Solution

The function \(f(x)\) is linear on the intervals

\[0 \le x \le \frac{1}{3},\]

\[\frac{1}{3} \le x \le \frac{1}{2} ,\]

\[\frac{1}{2} \le x \le \frac{3}{4},\]

\[\frac{3}{4} \le x \le 1,\]

and in order to use the trapezium rule, we need to divide the interval \(0 \le x \le 1\) into \(n\) equal intervals.

However, if the values \(x = \dfrac{1}{3}, \dfrac{1}{2}, \dfrac{3}{4}\) aren’t at the end of an interval, then the trapezium rule will overestimate the value of the integral.

For example, if we took \(\dfrac{1}{4} \le x \le \dfrac{1}{2}\) as one of the intervals (\(n=4\)), then we would be overestimating the value of the integral, because we would also be including the area of triangle A, as shown below.

Therefore we need to choose a value of \(n\) such that \(x = \dfrac{1}{3}, \dfrac{1}{2}, \dfrac{3}{4}\) lie at the end of intervals.

The largest such interval would be of width \(\dfrac{1}{12}\), that is, \(n=12\), and similarly, \(n\) can be any multiple of \(12\).

Hence the answer is (d).
