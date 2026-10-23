---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7078
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7078
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7078
  old_site_id: Q3025
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
      evidence: first four terms of (1-x/2)^10 then coefficient of x^2 in (5+4x)(1-x/2)^10 — the canonical
        CIE P1 binomial question
      rationale: 'Canonical UGM title: "Can we find the coefficient of $x^2$ in $(5 + 4x)(1 - x/2)^{10}$?";
        exam provenance: UCLES O level Additional Mathematics 2, 1970, Q4(ii)'
      validation_status: SUGGESTED
      primaryPick: true
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1970, Q4(ii)
task: T-UGM-IMPORT-6
---

# Can we find the coefficient of $x^2$ in $(5 + 4x)(1 - x/2)^{10}$?

## Question

Write down and simplify the first \(4\) terms in the expansion by the binomial theorem of \(\left(1 - \tfrac{1}{2}x\right)^{10}\).

Find the coefficient of \(x^2\) in the expansion of \[(5 + 4x)\left(1 - \tfrac{1}{2}x\right)^{10}.\]

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

By applying this to the expression

\(\left(1 - \tfrac{1}{2}x\right)^{10}\)

, we have that

\[ \left(1 - \tfrac{1}{2}x\right)^{10} = \binom{10}{0} \left( -\frac{x}{2} \right)^0 + \binom{10}{1} \left( -\frac{x}{2} \right)^1 + \binom{10}{2} \left( -\frac{x}{2} \right)^2 + \binom{10}{3} \left( -\frac{x}{2} \right)^3 + \dotsb \]

We can simplify this a little.

\[\begin{align*} \binom{10}{1} &= \frac{10}{1} = 10, \\ \binom{10}{2} &= \frac{10 \times 9}{2 \times 1} = 45, \\ \binom{10}{3} &= \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120, \end{align*}\]

so that \[\left(1 - \tfrac{1}{2}x\right)^{10} = 1 - 5x + \frac{45}{4} x^2 - 15x^3 + \dotsb\]

There are only two contributing terms to the coefficient of \(x^2\).

The \(5\) from the factor \((5 + 4x)\) pairs with the \(\dfrac{45}{4}x^2\) term in the expansion of \(\left(1 - \tfrac{1}{2}x\right)^{10}\), and the \(4x\) term pairs with the \(-5x\) term. Since we have already calculated the coefficients in this expansion this is a straightforward task.

Thus, we have that the coefficient of

\(x^2\)

in the product is

\[\begin{align*} 5 \times \frac{45}{4} + 4 \times (-5) &= \frac{225}{4} - 20 \\ &= \frac{145}{4}. \end{align*}\]
