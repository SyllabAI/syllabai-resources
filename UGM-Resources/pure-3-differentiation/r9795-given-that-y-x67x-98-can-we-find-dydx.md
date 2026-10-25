---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9795
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9795
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9795
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: dy/dx of y = (x+6)^7 (x-9)^8 by the product rule and the zeros of dy/dx - the canonical
        3.4.2 product-rule exercise
      rationale: 'Canonical UGM title: Given that $y = (x+6)^7(x-9)^8$, can we find $dy/dx$?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Given that $y = (x+6)^7(x-9)^8$, can we find $dy/dx$?

## Question

Given that \(y = (x+6)^7(x-9)^8\), find \(\dfrac{dy}{dx}\) and the values of \(x\) for which \(\dfrac{dy}{dx}\) is zero.

## Solution

Let

\(u = (x+6)^7\)

and

\(v = (x-9)^8\)

. By the

chain rule

\[\begin{equation*} u' = 7(x+6)^6 \frac{d}{dx}(x+6) = 7(x+6)^6 \end{equation*}\]

and

\[\begin{equation*} v' = 8(x-9)^7 \frac{d}{dx}(x-9) = 8(x-9)^7 \end{equation*}\]

By the

product rule

\[\begin{align*} \frac{dy}{dx} = uv' + u'v &= 8(x+6)^7(x-9)^7 + 7(x+6)^6(x-9)^8 \\ &= (x+6)^6(x-9)^7 \left( 8(x+6) + 7(x-9) \right) \\ &= (x+6)^6(x-9)^7(15x - 15) \\ &= 15(x+6)^6(x-9)^7(x-1). \end{align*}\]

Consequently,

\[\begin{equation*} \frac{dy}{dx} = 0 \end{equation*}\]

if and only if

\[\begin{equation*} x = -6 \quad\text{or}\quad x = 9 \quad\text{or}\quad x = 1. \end{equation*}\]
