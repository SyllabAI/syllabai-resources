---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8033
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8033
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8033
  old_site_id: Q160
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q2
task: T-UGM-IMPORT-6
---

# Can we find a sequence of solutions to the equation $x^2 - 2y^2 = 1?$

## Question

1. Find a pair of positive integers, \(x_1\) and \(y_1\), that solve the equation \[(x_1)^2 - 2(y_1)^2 = 1.\]

---

1. Given integers \(a\), \(b\), we define two sequences \(x_1\), \(x_2\), \(x_3\), \(\dots\) and \(y_1\), \(y_2\), \(y_3\), \(\dots\) by setting \[x_{n+1} = 3x_n + 4y_n, \quad y_{n+1} = ax_n + by_n, \quad \text{for $n \ge 1$}.\] Find *positive* values for \(a\), \(b\) such that \[(x_{n+1})^2 - 2(y_{n+1})^2 = (x_n)^2 - 2(y_n)^2.\]

---

1. Find a pair of integers \(X\), \(Y\) which satisfy \(X^2 - 2Y^2 = 1\) such that \(X > Y > 50\).

---

1. (Using the values of \(a\) and \(b\) found in the second part) what is the approximate value of \(x_n/y_n\) as \(n\) increases?

## Suggestion

Can you combine what we know to form an equation involving \(a\) and \(b\)?

How can we use what we have learnt from (i) and (ii)?

## Solution

By inspection or by trying a few small values, we can find the solution \(x_1 = 3\), \(y_1 = 2\).

Substituting the expressions for \(x_n\) and \(y_n\) into this equation, we get \[(3x_n + 4y_n)^2 - 2(ax_n + by_n)^2 = (x_n)^2 - 2(y_n)^2\] that is, \[(8 - 2a^2)(x_n)^2 + (24 - 4ab)x_ny_n + (18-2b^2)(y_n)^2 = 0.\]

This equation will certainly hold if all three coefficients are zero. In this case, we have

\[2a^2 = 8, \quad 4ab = 24, \quad 2b^2 = 18.\]

These equations DO solve, to give \(a = \pm 2, b = \pm 3\). Since we also require that \(a\) and \(b\) are positive, we have \(a = 2\) and \(b = 3\).

We start with our previously found small solution, \(x_1 = 3\) and \(y_1 = 2\).

Now we can use the sequences defined above with \(a=2, b=3\) to generate new solutions. We have \[x_1 = 3, \quad y_1 = 2;\] \[x_2 = 3 \times 3 + 4 \times 2 = 17, \quad y_2 = 2 \times 3 + 3 \times 2 = 12;\] \[x_3 = 3 \times 17 + 4 \times 12 = 99, \quad y_3 = 2 \times 17 + 3 \times 12 = 70.\] So \(X = 99\) and \(Y = 70\) are such a pair.

Let’s suppose that \(\dfrac{x_n}{y_n}\) tends to a limit \(L\) as \(n\) tends to infinity.

Then for large \(n,\) \[L \approx \dfrac{x_{n+1}}{y_{n+1}} = \dfrac{3x_{n}+4y_n}{2x_n+3y_{n}}\] \[=\dfrac{3\dfrac{x_{n}}{y_{n}}+4}{2\dfrac{x_{n}}{y_{n}}+3}\] \[\approx \dfrac{3L+4}{2L+3}.\]

Thus \(L \approx \dfrac{3L+4}{2L+3}\), which becomes equality when we allow \(n\) to tend to infinity. Thus by solving the equation, \(L = \sqrt{2}.\)

Alternatively, we could argue like this:

For all the pairs \((x_n,y_n)\), we have \[(x_n)^2 - 2(y_n)^2 = 1.\]

Also, because of the way \(x_n\) and \(y_n\) are constructed, both form increasing sequences.

So if we divide through by \((y_n)^2\), we see that \[\left(\frac{x_n}{y_n}\right)^2 - 2 = \frac{1}{(y_n)^2} \approx 0 \quad \text{for large $n$},\] so \(x_n/y_n \approx \sqrt{2}\), since \(x_n\) and \(y_n\) are both positive.

This question may remind you of [Staircase sequences](https://undergroundmathematics.org/thinking-about-numbers/staircase-sequences).
