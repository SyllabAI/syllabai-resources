---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5640
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5640
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5640
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: 'part 1 is the binomial expansion: coefficient of x^7 in (x^2+2/x)^8 (parts 2-3 are
        calculus — 1.7/1.8 bearings recorded in the cross-map)'
      rationale: 'Canonical UGM title: "Can we find the minimum value of $x^2+2/x$ for $x$ positive?";
        exam provenance: UCLES O level Additional Mathematics 2, 1967, Q4'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1967, Q4
task: T-UGM-IMPORT-6
---

# Can we find the minimum value of $x^2+2/x$ for $x$ positive?

## Question

1. Find and simplify the coefficient of \(x^7\) in the binomial expansion of \(\left( x^2 + \dfrac{2}{x} \right)^8\).

---

1. Calculate the minimum value of \(x^2 + \dfrac{2}{x}\) for positive values of \(x\).

---

1. Given that \(y = \left( x^2 + \dfrac{2}{x} \right)^8\), find the value of \(\dfrac{dy}{dx}\) when \(x = -1\).

## Solution

The

binomial theorem

says that, if

\(n\)

is a positive integer, then

\[\begin{equation*} (x+y)^n = \sum_{r=0}^n \binom{n}{r} x^r y^{n-r} \end{equation*}\]

where

\[\begin{equation*} \binom{n}{r} = \frac{n!}{r!(n-r)!} \end{equation*}\]

So \(\left(x^2+\dfrac{2}{x}\right)^8\) is made up of terms of the form \(\dbinom{8}{r}x^{2r}\left(\dfrac{2}{x}\right)^{8-r}\).

To find the value of \(r\) that gives the term in \(x^7\), we require \(2r-(8-r)=7\), which gives \(r = 5\).

So the coefficient of \(x^7\) is \(\dbinom{8}{5}2^3\), or \(448\).

If we let

\[\begin{equation*} y = x^2 + \frac{2}{x} = x^2 + 2x^{-1} \end{equation*}\]

then we have that

\[\begin{equation*} \frac{dy}{dx} = 2x - 2x^{-2}. \end{equation*}\]

Hence,

\[\begin{equation*} \frac{dy}{dx} = 0 \iff x = x^{-2} \iff x^3 = 1 \iff x = 1. \end{equation*}\]

Is this stationary point a minimum? Yes: as \(x \to 0\) or \(x \to \infty\), \(y \to \infty\), so this stationary point has to be a minimum.

The minimum value of the expression is then \(1^2+\dfrac{2}{1} = 3\).

By the

Chain Rule

we have that

\[\begin{align*} \frac{dy}{dx} &= 8 \left( x^2 + \frac{2}{x} \right)^7 \times \frac{d}{dx} \left( x^2 + \frac{2}{x} \right) \\ &= 8 \left( x^2 + \frac{2}{x} \right)^7 \left( 2x - 2x^{-2} \right). \end{align*}\]

So we have

\[\begin{align*} \frac{dy}{dx}(-1) &= 8 \left( (-1)^2 + \frac{2}{-1} \right)^7 \left( 2(-1) - 2(-1)^{-2} \right) \\ &= 8 (1-2)^7 (-2-2) \\ &= 8 (-1)^7 (-4) \\ &= 32. \end{align*}\]
