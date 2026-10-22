---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6230
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6230
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6230
  old_site_id: Q84
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicular foot as midpoint — perpendicular gradients plus ax+by+c=0 fluency; MAT MCQ extension (recorded medium).'
      rationale: 'Canonical UGM title: “Can we reflect this point in this line?”; exam provenance: Oxford (MAT) None Q1C'
      validation_status: SUGGESTED
    title: find the equation of a straight line given e.g. given two points, or one point and the gradient. sufficient information
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'perpendicular foot as midpoint — perpendicular gradients plus ax+by+c=0 fluency; MAT MCQ extension (recorded medium).'
      rationale: 'Canonical UGM title: “Can we reflect this point in this line?”; exam provenance: Oxford (MAT) None Q1C'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) None Q1C
task: T-UGM-IMPORT-3
---

# Can we reflect this point in this line?

## Question

What is the reflection of the point \((3,4)\) in the line \(3x + 4y = 50\)?

1. \((9,12)\),

---

1. \((6,8)\),

---

1. \((12,16)\),

---

1. \((16,12)\).

## Suggestion

It might be helpful to sketch the situation. How are the point \((3,4)\) and its reflection related?

## Solution

Let \(L\) be the line with equation \(3x + 4y = 50\).

The point \(P(3,4)\) and its reflection \(P'\) in the line \(L\) are related in two ways: the line \(PP'\) is perpendicular to the line \(L\), and \(P\) and \(P'\) are equidistant (equal distances) from \(L\). (So in terms of vectors, \(\overrightarrow{PM}=\overrightarrow{MP'}\), where \(M\) is the point of intersection of \(PP'\) and \(L\).)

Now \(L\) has gradient \(-\frac{3}{4}\), so any line perpendicular to \(L\) will have gradient \(\frac{4}{3}\).

The perpendicular line \(PP'\) passing through \(P(3,4)\) therefore has equation \[y - 4 = \frac{4}{3}(x - 3),\] that is, \[y = \frac{4}{3}x.\]

From substituting this into the equation for \(L\), we see that \(L\) and \(PP'\) intersect at \(M\), where \[3x + 4 \times \frac{4}{3}x = 50,\] and rearranging this gives \[\frac{25}{3} x = 50,\] that is, \[x = 6.\] Then substituting this into either equation gives \(y = 8\), so \(M\) lies at \((6,8)\).

We must now use this information to find the reflected point. We can see that the difference in \(x\)-coordinates between \((3,4)\) and \((6,8)\) is \(3\), and the difference in \(y\)-coordinates is \(4\). So to get the reflected point \(P'\), we must add \(3\) to the \(x\)-coordinate and \(4\) to the \(y\)-coordinate of \(M(6,8)\), as illustrated below:

This tells us that the coordinate of the reflected point is \((9,12)\).

The answer is (a).
