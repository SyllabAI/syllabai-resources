---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r6592
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r6592
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6592
  old_site_id: Q1058
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
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: the trapezium-rule MC resolves by summing the GP 2^{1/N}+...+2^{(N-1)/N} — the GP sum
        formula is the decisive step
      rationale: 'Canonical UGM title: "Can we use the trapezium rule to estimate this integral?"; exam
        provenance: Oxford University Mathematics Aptitude Test, 2009, Q1H'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q1H
task: T-UGM-IMPORT-6
---

# Can we use the trapezium rule to estimate this integral?

## Question

When the trapezium rule is used to estimate the integral

\[\displaystyle\int_0^1 \! 2^x \, \mathrm{d}x\]

by dividing the interval \(0 \le x \le 1\) into \(N\) subintervals the answer achieved is

1. \(\dfrac{1}{2N} \left(1+\dfrac{1}{2^{1/N}+1} \right)\),

---

1. \(\dfrac{1}{2N} \left(1+\dfrac{2}{2^{1/N}-1} \right)\),

---

1. \(\dfrac{1}{N} \left(1-\dfrac{1}{2^{1/N}-1} \right)\),

---

1. \(\dfrac{1}{2N} \left(\dfrac{5}{2^{1/N}+1} -1\right)\).

## Suggestion

The notation \[\displaystyle\int_0^1 \! 2^x \, \mathrm{d}x\] means the area between the curve \(y = 2^x\) and the \(x\)-axis, from \(x=0\) to \(x = 1\).

Using the trapezium rule will give us a long sum that will have to be rewritten as a fraction. Can you think of another situation where we know how to rewrite a finite sum of numbers in fractional form?

## Solution

When the trapezium rule is used to estimate the integral

\[\int_0^1 \! 2^x \, \mathrm{d}x\]

by dividing the interval \(0 \le x \le 1\) into \(N\) subintervals the answer achieved is

1. \(\dfrac{1}{2N} \left(1+\dfrac{1}{2^{1/N}+1} \right)\),

---

1. \(\dfrac{1}{2N} \left(1+\dfrac{2}{2^{1/N}-1} \right)\),

---

1. \(\dfrac{1}{N} \left(1-\dfrac{1}{2^{1/N}-1} \right)\),

---

1. \(\dfrac{1}{2N} \left(\dfrac{5}{2^{1/N}+1} -1\right)\).

The trapezium rule says this:

The area under the curve \(f(x)\) between the points \(x_0\) and \(x_n\), with this interval divided into \(n\) smaller intervals of width \(h = \dfrac{(x_n - x_0)}{n}\) is given by

\[\displaystyle\int_{x_0}^{x_n} \! f(x) \, \mathrm{d}x \approx \dfrac{1}{2} h \left[ (y_0 + y_n) + 2(y_1 + y_2 + \dotsb + y_{n-1} ) \right],\]

where \(y_i = f(x_i)\).

So dividing the interval \(0 \le x \le 1\) into \(N\) subintervals for our problem gives \(h=\dfrac{1}{N}\), and the trapezium rule gives

\[\begin{align*} \displaystyle\int_0^1 \! 2^x \, \mathrm{d}x \hspace{2mm} & \approx \dfrac{1}{2} \dfrac{1}{N} \left[ (2^0 + 2^1) + 2(2^{\frac{1}{N}}+2^{\frac{2}{N}}+ ... + 2^{\frac{N-1}{N}}) \right] \\ \end{align*}\]

We have what looks like a series inside the brackets. Do we know any ways of simplifying series?

\[2^{\frac{1}{N}}+2^{\frac{2}{N}}+ ... + 2^{\frac{N-1}{N}}\]

is a geometric series with a first term of \(2^{\frac{1}{N}}\), a common ratio of \(2^{\frac{1}{N}}\), and \(N-1\) terms so we can write it as,

\[\dfrac{2^{\frac{1}{N}}(1 - 2^{\frac{N-1}{N}})}{1-2^{\frac{1}{N}}}\]

using the formula for the sum of a geometric progression.

The whole expression can now be written as

\[\dfrac{1}{2N} \left[3 + 2 \left( \dfrac{2^\frac{1}{N}(1-2^{\frac{N-1}{N}})}{1-2^{\frac{1}{N}}}\right )\right].\]

There are many ways to rearrange this expression, but three answers have a \(1\) in them, so we can use that as a starting point.

\[\begin{align*} \dfrac{1}{2N} \left[3 + 2 \left( \dfrac{2^\frac{1}{N}(1-2^{\frac{N-1}{N}})}{1-2^{\frac{1}{N}}}\right )\right] &= \dfrac{1}{2N} \left[1 + 2\left(\dfrac{1-2^{\frac{1}{N}}}{1-2^{\frac{1}{N}}}\right) + 2 \left( \dfrac{2^\frac{1}{N}(1-2^{\frac{N-1}{N}})}{1-2^{\frac{1}{N}}}\right )\right]\\ &= \dfrac{1}{2N} \left[1 + \dfrac{2(1-2^{\frac{1}{N}}) + 2(2^{\frac{1}{N}}-2)}{1-2^{\frac{N-1}{N}}}\right]\\ &= \dfrac{1}{2N} \left(1+\dfrac{2}{2^{\frac{1}{N}}-1} \right) \end{align*}\]

So the answer is (b).
