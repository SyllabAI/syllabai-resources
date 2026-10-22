---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r9368
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r9368
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9368
  old_site_id: Q3045
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Circle through (2,0) and (8,0) touching the y-axis; furthest point from (2,0) — circle-from-conditions.'
      rationale: 'Canonical UGM title: “Given three clues, can we find the equation of this circle?”; exam provenance: UCLES 1968 Q7'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1968 Q7
task: T-UGM-IMPORT-3
---

# Given three clues, can we find the equation of this circle?

## Question

Find the equation of the circle which passes through the points \((2,0)\) and \((8,0)\) and touches the \(y\)-axis on the positive side of the origin.

Find the coordinates of the point on the circle which is furthest from the point \((2,0)\).

## Suggestion

A sketch of the circle would help to visualise the problem.

Are there any circle theorems that could help you?

## Solution

The vertical line of symmetry of the circle is \(x = 5\), and so the centre of the circle must be a point of the form \((5,q)\).

As the circle touches the \(y\)-axis, the radius of the circle is therefore \(5\).

The distance between \((2,0)\) and \((5,q)\) must be \(5\), so \(\sqrt{(2-5)^2 + q^2} = 5\). Solving for \(q\) gives \(q = 4\), and so the centre of the circle is \((5,4)\).

Therefore the equation of the circle is \[(x - 5)^2 + (y - 4)^2 = 25.\]

The point on the circle furthest from this point lies on the opposite end of the diameter that contains \((2,0)\).

By symmetry around the centre \((5,4)\), this point is \((8,8)\).
