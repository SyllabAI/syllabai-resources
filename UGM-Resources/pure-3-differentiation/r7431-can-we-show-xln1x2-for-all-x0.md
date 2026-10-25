---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7431
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7431
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7431
  old_site_id: Q194
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: d/dx (x - ln(1+x^2)) = 1 - 2x/(1+x^2) >= 0 by the 3.4.1 composite derivative of ln(1+x^2),
        deducing x > ln(1+x^2) for x > 0 - the increasing-function argument (flips the lane-10 non-overlap
        row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we show $x>\ln(1+x^2)$ for all $x>0$?'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we show $x>\ln(1+x^2)$ for all $x>0$?

## Question

Given that \[y=x-\ln(1+x^2),\] show that \[\frac{dy}{dx}\geq 0\ \text{for all values of $x$.}\]

Deduce that, for all \(x>0\), \[x>\ln(1+x^2).\]

## Solution

We can compute

\(\dfrac{dy}{dx}\)

using the chain rule:

\[\begin{align*} \frac{dy}{dx} &= 1-\frac{1}{1+x^2}\times\frac{d}{dx}(1+x^2)\\ &= 1-\frac{2x}{1+x^2}\\ &= \frac{1+x^2-2x}{1+x^2}\\ &= \frac{(x-1)^2}{1+x^2}. \end{align*}\]

We know that \((x-1)^2 \geq 0\) and \(1+x^2\geq 1\) for all values of \(x\), so \(\dfrac{dy}{dx} \geq 0\) for all values of \(x\).

We know that \(\dfrac{dy}{dx}\geq 0\) for all values of \(x\), so the function \(x-\ln(1+x^2)\) is an increasing function.

Substituting we find that when

\(x = 0\)

,

\(y=0\)

and

\(\dfrac{dy}{dx} = 1\)

. This means that for any value of

\(x>0\)

,

\(y\)

must be greater than zero. So

\[\begin{align*} x &- \ln(1+x^2) > 0\\ \implies\quad x &> \ln(1+x^2) \end{align*}\]

for all \(x>0\) as required.
