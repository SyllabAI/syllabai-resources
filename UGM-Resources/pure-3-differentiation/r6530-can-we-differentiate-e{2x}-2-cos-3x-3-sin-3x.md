---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r6530
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r6530
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6530
  old_site_id: Q4057
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
      evidence: d/dx of e^(2x)(2 cos 3x + 3 sin 3x) by the product rule with the 3.4.1 composite derivatives
        inside - the exact CIE product-rule-plus-standard-derivatives showcase (flips the lane-10 non-overlap
        row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we differentiate $e^{2x}( 2 \cos (3x) + 3 \sin (3x))$?'
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

# Can we differentiate $e^{2x}( 2 \cos (3x) + 3 \sin (3x))$?

## Question

Differentiate with respect to \(x\)

\[e^{2x}\left( 2 \cos 3x + 3 \sin 3x \right).\]

## Suggestion

Can we remember the chain and product rules for differentiation?

## Solution

We’ll start by applying the [product rule](https://undergroundmathematics.org/glossary/product-rule), defining \(u=e^{2x}\) and \(v=2 \cos 3x + 3 \sin 3x\).

Their derivatives can be calculated via the [chain rule](https://undergroundmathematics.org/glossary/chain-rule), which tells us \(u'=2e^{2x}\).

The function \(v\) contains two trigonometric functions, so we need to recall that \(\dfrac{d (\sin x)}{dx} = \cos x\) and \(\dfrac{d (\cos x)}{dx} = - \sin x\).

Another application of the chain rule then gives \(v' = -6 \sin 3x + 9 \cos x\). We can now combine \(u\), \(v\), \(u'\) and \(v'\) to find

\[\begin{align*} \dfrac{d \left( e^{2x}\left( 2 \cos 3x + 3 \sin 3x \right) \right)}{dx} &= u'v + v'u\\ &= 2e^{2x} \times \left( 2 \cos 3x + 3 \sin 3x \right) + \left( -6 \sin 3x + 9 \cos x \right) \times e^{2x}\\ &= 13 e^{2x} \cos 3x. \end{align*}\]
