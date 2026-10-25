---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5696
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5696
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5696
  old_site_id: null
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
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: normals to the parametric curve x = 4 - t^2, y = 4t at the y-axis intersections meeting
        on the x-axis - dy/dx = (dy/dt)/(dx/dt) with the normal equations
      rationale: 'Canonical UGM title: Can we show that these normals meet on the $x$-axis?'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we show that these normals meet on the $x$-axis?

## Question

A curve is given parametrically by the equations \[x=4-t^2,\ y=4t.\]

Find the equations of the normals to the curve at the points where the curve meets the \(y\)-axis. Show that these normals meet on the \(x\)-axis.

## Solution

A curve is given parametrically by the equations \[x=4-t^2, y=4t.\]

Find the equations of the normals to the curve at the points where the curve meets the \(y\)-axis. Show that these normals meet on the \(x\)-axis.

The curve meets the \(y\)-axis where \(x=0\), hence at \(t=\pm 2\). The corresponding points on the curve are \(P= (0,8)\) and \(Q= (0,-8)\).

Differentiating we find \(\dfrac{dy}{dt} = 4\) and \(\dfrac{dx}{dt} = -2t\). By the Chain Rule, \[\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt} = -\dfrac{2}{t} ,\] so the gradient of the normal at the point given by the parameter \(t\) is \(\dfrac{t}{2}\).

The normal at \(P\) is \(y = x + 8\), and the normal at \(Q\) is \(y = -x - 8\).

Setting the two equations equal to each other gives \(-x-8=x+8 \implies x=-8 \implies y=0\), and hence the lines meet on the \(x\)-axis.

The curve is a parabola, symmetrical about the \(x\)-axis. The symmetry of the situation guarantees that the normals will meet on the \(x\)-axis.
