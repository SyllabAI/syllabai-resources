---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/power-series/r6601
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- power-series
- type/review-question
resource_identity:
  ugm_id: r6601
  station: power-series
  station_title: Power Series
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6601
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: power-series
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: power-series
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "(1+ax)^{−2} expanded by the |x|<1 binomial series to x³; the vanishing x-coefficient pins a=3/2 and the expansion is completed"
      rationale: "Canonical UGM title: What is this algebraic fraction if its expansion has no $x$ term?"
      validation_status: SUGGESTED
    title: "use the expansion of (1 + x)ⁿ, where n is a rational number and | x | < 1"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1, QP 9200/1, 1980, Q2(b)(ii)"
  task: T-UGM-IMPORT-9
---

# What is this algebraic fraction if its expansion has no $x$ term?

## Question

In the expansion of \[\frac{1+3x}{(1+ax)^2}\] in ascending powers of \(x\), the coefficient of \(x\) is zero. Find the value of the constant \(a\), and, when \(a\) has this value, obtain the expansion up to and including the term in \(x^3\).

## Solution

We first need to find an expansion for the denominator using the standard binomial expansion.

The [binomial theorem](https://undergroundmathematics.org/glossary/binomial-theorem) says that, if \(|x| < 1\), then \[(1+x)^r = 1 + rx + \frac{r(r-1)}{2!} x^2 + \frac{r(r-1)(r-2)}{3!} x^3 + \dotsb\]

In our case,

\(r=-2\)

and we have

\(ax\)

in place of

\(x\)

, so

\[\begin{align*} (1+ax)^{-2} &= 1 -2ax + \frac{-2(-3)}{2!}(ax)^2 + \frac{-2(-3)(-4)}{3!} (ax)^3 + \dotsb \\ &=1-2ax+3a^2x^2-4a^3x^3 +\dotsb \end{align*}\]

The term in \(x\) of the expansion of \(\dfrac{1+3x}{(1+ax)^2}\) comes from \(1 \times (-2ax) + 3x \times 1\). If the coefficient is zero then we know that \(3-2a=0\) so \(a=\dfrac{3}{2}\).

…and, when \(a\) has this value, obtain the expansion up to and including the term in \(x^3\).

Multiplying by the numerator we get \[\frac{1+3x}{(1+ax)^2} = 1 + (3-2a)x+(3a^2-6a)x^2+(9a^2-4a^3)x^3+ \dotsb\] and substituting for \(a\) we get \[\frac{1+3x}{(1+\frac{3}{2}x)^2}=1-\frac{9}{4}x^2+\frac{27}{4}x^3 \quad\text{ up to and including the term in } x^3.\]

Note that the condition for the expansion to be valid is \(\big|ax\big|<1\) which means that \(\big|x\big|<\frac{2}{3}\).
