---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r9184
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r9184
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9184
  old_site_id: Q3030
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: 'area between sin x and sin 2x: A = INT sin 2x - INT sin x = 1/2[-cos x] - [-cos x] =
        1/4 with a second implicit-substitution method of record - the 3.5.1 standard antiderivatives
        are the engine (flips the lane-11 non-overlap row of record routed ''P3 3.5 Integration'')'
      rationale: 'Canonical UGM title: Can we find the area between $\sin x$ and $\sin 2x$?'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Can we find the area between $\sin x$ and $\sin 2x$?

## Question

Using the same axes, *sketch* the curves \(y = \sin x\) and \(y = \sin 2x\) from \(x = 0\) to \(\tfrac{1}{2}\pi\), where \(x\) is in radians.

Prove that the curves intersect at the points \[(0,0) \quad\text{and}\quad \left(\frac{\pi}{3}, \frac{\sqrt{3}}{2} \right).\]

Calculate the area of the region bounded by the parts of the curves between these two points.

## Solution

The curve \(y = \sin 2x\) has the same shape as \(y = \sin x\), but twice the frequency; we thus have the following sketch.

The curves intersect exactly when \(\sin x = \sin 2x\), or \(\sin x = 2 \sin x \cos x\).

This gives us that either \(\sin x = 0\) or \(\cos x = \dfrac{1}{2}\). Within our region this means \(x = 0\) or \(x=\dfrac{\pi}{3}\).

So the curves intersect at \((0,0)\) and at \(\left(\dfrac{\pi}{3}, \dfrac{\sqrt{3}}{2}\right)\).

The area we are to calculate is the yellow area indicated in the following diagram.

**Thinking about scaling**

We are looking for the area

\[\begin{align*} A &= \int_0^{\dfrac{\pi}{3}} \sin 2x\:dx - \int_0^{\dfrac{\pi}{3}}\sin x\:dx\\ &= \frac{1}{2}\int_0^{\dfrac{2\pi}{3}} \sin x\:dx - \int_0^{\dfrac{\pi}{3}}\sin x\:dx\\ &= \frac{1}{2}\biggl[-\cos x\biggr]_0^{\dfrac{2\pi}{3}} - \biggl[-\cos x\biggr]_0^{\dfrac{\pi}{3}}\\ &= \frac{1}{2}\left(\frac{1}{2}+1\right) - \left(-\frac{1}{2}+1\right)\\ &= \frac{1}{4}. \end{align*}\]

**Using an implicit substitution**

We are looking for the area

\[\begin{align*} A &= \int_0^{\dfrac{\pi}{3}} \sin 2x -\sin x\:dx \\ &= \biggl[ -\frac{\cos 2x}{2}+\cos x \biggr]_0^{\dfrac{\pi}{3}} \\ &= \frac{1}{4} + \frac{1}{2} + \frac{1}{2}-1\\ &= \frac{1}{4}. \end{align*}\]
