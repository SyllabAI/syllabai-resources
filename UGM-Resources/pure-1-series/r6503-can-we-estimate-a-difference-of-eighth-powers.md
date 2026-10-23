---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6503
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6503
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6503
  old_site_id: Q29
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
      evidence: expand (1+x)^8, then evaluate (1.001)^8-(0.999)^8 by combining the (1±x)^8 expansions
        — canonical numerical binomial question
      rationale: 'Canonical UGM title: "Can we estimate a difference of eighth powers?"; exam provenance:
        UCLES O level Mathematics Alternative C, 1951, Q5'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Mathematics Alternative C, 1951, Q5
task: T-UGM-IMPORT-6
---

# Can we estimate a difference of eighth powers?

## Question

Write down the first four terms in the expansion of \((1+x)^8\) in ascending powers of \(x\).

Evaluate \((1.001)^8-(0.999)^8\) to eight significant figures.

[*Try to do this without touching your calculator!*]

## Suggestion

How do we expand \((1+x)^n\)?

Can we also find the expansion of \((1-x)^8\)?

How can we be sure our answer is correct to eight significant figures?

## Solution

We can use the binomial theorem for

\(n\)

a positive integer,

\[(a+b)^n=\sum\limits_{k=0}^n \binom{n}{k}a^{n-k}b^k,\]

with

\(n=8\)

,

\(a=1\)

and

\(b=x\)

, to get

\[\begin{align*} (1+x)^8 &= \binom{8}{0}x^0+\binom{8}{1}x^1+\binom{8}{2}x^2+\binom{8}{3}x^3 + \dotsb + x^8 \\ &= 1 + \frac{8}{1} x^0 + \frac{8 \cdot 7}{2 \cdot 1} x^2 + \frac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} x^3 + \dotsb x^8 \\ &= 1 + 8x + 28x^2 + 56x^3 + \dotsb + x^8. \end{align*}\]

Alternatively, we can just use the fact that the 9th line of Pascal’s triangle starts 1, 8, 28, 56, … and just write the final line down.

We can expand to get \[(1-x)^8 = 1 - 8x + 28x^2 - 56x^3 + \dotsb + x^8.\] Thus \[(1+x)^8-(1-x)^8=16x+112x^3+ 112x^5 + 16x^7,\] with the even powers of \(x\) all cancelling out.

If we pick

\(x=0.001\)

and substitute it into the above equation we get precisely what we need:

\[\begin{align} (1.001)^8-(0.999)^8&\approx16\times 0.001+112\times(0.001)^3 \\ &=0.016 + 0.000\,000\,112=0.016\,000\,112 . \end{align}\]

So to eight significant figures \((1.001)^8-(0.999)^8\approx0.016\,000\,11\).

Do the higher-order terms make a contribution that we need to consider?

The \(x^5\) term does not contribute because \((0.001)^5=0.000000000000001\) and the coefficient is not of the order \(10^6\) that would be needed to bring it within 8 significant figures. The other terms are even smaller.
