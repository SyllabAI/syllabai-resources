---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r7258
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r7258
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7258
  old_site_id: Q3015
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
      evidence: 27, x, y in GP with sum 21 — common-ratio quadratic with two solution pairs
      rationale: 'Canonical UGM title: "If $27$, $x$, $y$ are in GP, with sum $21$, what are $x$ and
        $y$?"; exam provenance: UCLES AO level Additional Mathematics 1, 1980, Q12(a)'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 1, 1980, Q12(a)
task: T-UGM-IMPORT-6
---

# If $27$, $x$, $y$ are in GP, with sum $21$, what are $x$ and $y$?

## Question

The numbers \(27\), \(x\), \(y\) are in geometric progression. If the sum of these three numbers is \(21\) calculate the possible values of \(x\) and \(y\).

## Solution

As the numbers

\(27\)

,

\(x\)

and

\(y\)

are in

geometric progression

, there is a

common ratio

\(r\)

such that

\[\begin{align*} x &= 27 r, \\ y &= xr = 27r^2. \end{align*}\]

We are also given that the sum of the three numbers is

\(21\)

, i.e.

\[ 27 + x + y = 21. \]

By substituting the values for

\(x\)

and

\(y\)

into this, we see that

\[\begin{align*} 27 + 27r + 27r^2 = 21 &\implies 27r^2 + 27r + 6 = 0 \\ &\implies 9r^2 + 9r + 2 = 0 \\ &\implies (3r + 2)(3r + 1) = 0. \end{align*}\]

Hence, the two possibilities for the common ratio are \[r = -\frac{2}{3} \quad\text{or}\quad r = -\frac{1}{3}.\]

Alternatively, one could use the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) to find the possible values of \(r\).

As the question asked us to find the possible values of \(x\) and \(y\), we are not yet done.

**Case 1: \(r = -\frac{2}{3}\)**

In this case, \[x = 27r = 27 \times \left( -\frac{2}{3} \right) = -18 \quad\text{and}\quad y = xr = (-18) \times \left( -\frac{2}{3} \right) = 12.\]

**Case 2: \(r = -\frac{1}{3}\)**

In this case, \[x = 27r = 27 \times \left( -\frac{1}{3} \right) = -9 \quad\text{and}\quad y = xr = (-9) \times \left( -\frac{1}{3} \right) = 3.\]

It’s possible to do the question without mentioning \(r\).

Three numbers \(a,b\) and \(c\) are in geometric progression if and only if \(ac=b^2\).

So here we have \(27y=x^2\), and also \(27+x+y=21\), or \(y = -x-6\).

So we have \(27(-x-6)=x^2\), and solving this quadratic equation gives us the same answers as above.
