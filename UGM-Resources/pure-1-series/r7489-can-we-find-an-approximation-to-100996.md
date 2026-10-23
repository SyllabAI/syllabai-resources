---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7489
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7489
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7489
  old_site_id: Q3004
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
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: expand (1+p)^6, substitute p=x-x^2, then choose x to evaluate (1.0099)^6 — expansion
        with substitution and numerical use
      rationale: 'Canonical UGM title: "Can we find an approximation to $(1.0099)^6$?"; exam provenance:
        UCLES AO level Additional Mathematics 1, 1983, Q6'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 1, 1983, Q6
task: T-UGM-IMPORT-6
---

# Can we find an approximation to $(1.0099)^6$?

## Question

Obtain the first \(4\) terms in the expansion of \((1 + p)^6\) in ascending powers of \(p\).

By substituting \(p = x - x^2\) obtain the expansion of \((1 + x - x^2)^6\) as far as the term in \(x^2\).

Find a value for \(x\) which would enable you to calculate \((1.0099)^6\).

## Suggestion

How can we use our expansion from the first part of the question?

We want to use an expansion of \((1 + x - x^2)^6\) - can we find an equation that \(x\) must satisfy?

Or can we see straight away what \(x\) must be?

## Solution

The

binomial theorem

says that, if

\(x\)

is a real number and

\(n\)

is a positive integer, then

\[ (1+x)^n = \sum_{i=0}^n \binom{n}{i} x^i \]

where

\[\begin{align*} \binom{n}{0} &= 1, \\ \binom{n}{i} &= \frac{n(n-1) \dotsm (n-(i-1))}{i(i-1) \dotsm 1} \quad\text{for each integer $1 \le i \le n$.} \end{align*}\]

By applying this to expression

\((1+p)^6\)

and ignoring terms beyond the fourth, we see that

\[\begin{align*} (1+p)^6 &= \binom{6}{0} p^0 + \binom{6}{1} p^1 + \binom{6}{2} p^2 + \binom{6}{3} p^3 + \dotsb \\ &= 1 + \frac{6}{1} p + \frac{6 \times 5}{2 \times 1} p^2 + \frac{6 \times 5 \times 4}{3 \times 2 \times 1} p^3 + \dotsb \\ &= 1 + 6p + 15p^2 + 20p^3 + \dotsb. \end{align*}\]

By taking

\(p = x - x^2\)

in the above expansion, we have that

\[ (1+x-x^2)^6 = 1 + 6(x-x^2) + 15(x-x^2)^2 + 20(x-x^2)^3 + \dotsb. \]

Ignoring the terms corresponding to

\(p^3\)

,

\(p^4\)

,… we have, up to and including the term featuring

\(x^2\)

,

\[\begin{align*} (1+x-x^2)^6 &= 1 + 6(x-x^2) + 15x^2 + \dotsb \\ &= 1 + 6x - 6x^2 + 15x^2 + \dotsb \\ &= 1 + 6x + 9x^2 + \dotsb. \end{align*}\]

If we intend to use a binomial expansion of \((1+x-x^2)^6\), it would be sensible to find some \(x\) such that \[1+x-x^2 = 1.0099.\] That is, \(x\) must be such that \[x - x^2 = 0.0099.\] However, as \[0.0099 = 0.01 - 0.0001 = 0.01 - (0.01)^2,\] we can simply take \(x = 0.01\).

Alternatively, we could solve the quadratic equation \(x^2 - x + 0.0099 = 0\).

By applying this solution \(x=0.01\) to the approximation from the previous part \[(1+x-x^2)^6 \approx 1 + 6x + 9x^2\] which improves as \(x\) tends to zero, we get \[(1.0099)^6 \approx 1 + 6 \times 0.01 + 9 \times (0.01)^2 = 1 + 0.06 + 0.0009 = 1.0609.\] In fact, \[(1.0099)^6 = 1.0608897,\] and so the error in the approximation is tiny: it is less than \(0.001\)%.
