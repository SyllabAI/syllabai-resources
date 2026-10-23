---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r7581
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r7581
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7581
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 2, QP 840/2, 1970, Q17a
task: T-UGM-IMPORT-5
---

# Can we sketch the curve $y = \cos x - \sin x +2$?

## Question

Give a sketch for \(-\pi \leq x \leq \pi\) of the curve \[y = \cos x - \sin x +2.\]

## Solution

Firstly we can rewrite the right hand side using one of the compound angle identities, such as \[R\cos(x+\theta)=R\cos x\cos \theta- R\sin x \sin \theta.\]

If we put \(R\cos \theta = 1\) and \(R \sin \theta = 1\), where \(R > 0\) and \(\theta\) is acute, we have (on dividing these equations) \(\tan \theta = 1 \implies \theta = \dfrac{\pi}{4}\).

On squaring and adding these equations, we have \[R^2 = 2 \implies R = \sqrt{2}.\]

This gives us that \(\sqrt{2}\cos\left(x+\dfrac{\pi}{4}\right) = \cos x - \sin x\), so the curve we are asked to sketch is \[y = \sqrt{2}\cos\left(x+\dfrac{\pi}{4}\right) +2.\]

So this is our standard cosine curve, stretched in the \(y\)-direction by a scale factor of \(\sqrt{2}\), translated by \(\dfrac{\pi}{4}\) to the left, and upwards by \(2\).
