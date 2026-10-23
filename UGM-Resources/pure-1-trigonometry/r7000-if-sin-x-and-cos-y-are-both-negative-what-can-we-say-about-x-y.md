---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7000
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7000
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7000
  old_site_id: Q3032
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: count values of z with sin 3z° = k in 0–360; quadrant signs of sin X and cos Y — graph/behaviour
        reasoning
      rationale: 'Canonical UGM title: “If $\sin X$ and $\cos Y$ are both negative, what can we say about
        $X + Y$?”; exam provenance: UCLES O level Additional Mathematics 1, QP 471/1, 1972, Q3(iii,iv)'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: count values of z with sin 3z° = k in 0–360; quadrant signs of sin X and cos Y — graph/behaviour
        reasoning
      rationale: 'Canonical UGM title: “If $\sin X$ and $\cos Y$ are both negative, what can we say about
        $X + Y$?”; exam provenance: UCLES O level Additional Mathematics 1, QP 471/1, 1972, Q3(iii,iv)'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 1, QP 471/1, 1972, Q3(iii,iv)
task: T-UGM-IMPORT-5
---

# If $\sin X$ and $\cos Y$ are both negative, what can we say about $X + Y$?

## Question

1. Given that \(\sin 3z^\circ = k\), where \(0 < k < 1\), how many values of \(z\) lie between \(0\) and \(360\)?

---

1. Given that \(X\) and \(Y\) both lie between \(0\) and \(360\), and that \(\sin X^\circ\) and \(\cos Y^\circ\) are both negative, find the values between which \(X + Y\) must lie.

## Suggestion

How does \(\sin 3z^\circ\) relate to the function \(\sin z^\circ\)?

Could drawing a graph of \(y = \sin (3z)\) help us here?

## Solution

The function \(y=\sin 3z\) is a stretch of \(y=\sin z\:\), scale factor \(\dfrac{1}{3}\), in the \(x\)-direction.

Thus, instead of one ‘complete wave’ between \(0\) and \(360\), we have three, giving this graph:

So while we would have two intersections between \(y = k\) and \(y = \sin z\) for \(0 < z < 360\), we’ll instead have six in the same interval.

If \(\sin X< 0\) and \(0 < X < 360\), then \(180 < X < 360\), while if \(\cos Y< 0\) and \(0 < Y < 360\), then \(90 < Y < 270\).

So for \(\sin X\) and \(\cos Y\) to both be negative, \(270 < X+Y < 630\).

Note that if \(270 < X+Y < 630\), this is no guarantee that \(\sin X\) and \(\cos Y\) are both negative (for example, \(X = 170, Y = 110\)).
