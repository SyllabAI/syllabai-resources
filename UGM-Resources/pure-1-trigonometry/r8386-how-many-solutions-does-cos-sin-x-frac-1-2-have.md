---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r8386
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r8386
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8386
  old_site_id: Q129
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: cos(sin x) = 1/2 solution count — composite range reasoning over sin and cos
      rationale: 'Canonical UGM title: “How many solutions does $\cos (\sin x)=\frac{1}{2}$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, Specimen 2, Q1E'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: cos(sin x) = 1/2 solution count — composite range reasoning over sin and cos
      rationale: 'Canonical UGM title: “How many solutions does $\cos (\sin x)=\frac{1}{2}$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, Specimen 2, Q1E'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, Specimen 2, Q1E
task: T-UGM-IMPORT-5
---

# How many solutions does $\cos (\sin x)=\frac{1}{2}$ have?

## Question

In the range \(0 \le x < 2\pi\) the equation \[\cos(\sin x) = \frac{1}{2}\] has

1. no solutions;

---

1. one solution;

---

1. two solutions;

---

1. three solutions.

## Suggestion

First consider \[\cos y = \frac{1}{2};\] what are the solutions of this equation?

From this, can you find the values of \(\sin x\) that satisfy \[\cos(\sin x) = \frac{1}{2}?\]

Do all or any of these values of \(\sin x\) give a solution for \(x\)?

## Solution

The equation \(\cos y = \dfrac{1}{2}\) has solutions \[y = \pm \frac{\pi}{3}, \pm \frac{5\pi}{3}, \pm \frac{7\pi}{3}, \pm \frac{11\pi}{3}, \dotsc .\]

So if \(\cos(\sin x) = \dfrac{1}{2}\) then \[\sin x = \pm \frac{\pi}{3}, \pm \frac{5\pi}{3}, \pm \frac{7\pi}{3}, \pm \frac{11\pi}{3}, \dotsc .\]

Now as \(\pi > 3\), we have \(\dfrac{\pi}{3} > 1\).

Therefore, all numbers on this list have magnitude greater than \(1\), and so lie outside the range of sine (\(-1 \le \sin x \le 1\)).

This means that \(\sin x\) cannot equal any of the numbers on this list, so there are no solutions.

The answer is (a).
