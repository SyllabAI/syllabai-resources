---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5737
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5737
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5737
  old_site_id: Q1046
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
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Four inequalities defining a triangular region from vertex coordinates — boundary-line reading in 1.3.2 forms; inequality-region language is extension (recorded'
      rationale: 'Canonical UGM title: “Which four inequalities define this region?”; exam provenance: UCLES 1978 Q23'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1978 Q23
task: T-UGM-IMPORT-3
---

# Which four inequalities define this region?

## Question

\(O\) is the origin and \(A\), \(B\) and \(C\) are the points \((0,-1)\), \((2,-1)\) and \((1,0)\) respectively. Write down the four inequalities which define the shaded region \(ABCO\) including its boundary.

## Suggestion

Can you find the equations of the four lines that bound the shaded area? How can you use these four equations to answer the original question?

## Solution

The shaded region is bounded by four lines: \(y=0\), \(x=0\), \(y=-1\) and by the straight line through \((0,1)\), \((1,0)\) and \((2,-1)\).

Writing this straight line as \(y=mx+c\), we know that \(c=1\), since \(c\) is the \(y\)-intercept. We know the point \((1,0)\) is on the line, so \(0=m+1\), which means the fourth line segment bounding the shaded area is part of \(y=1-x\).

Since the shaded area is below the \(x\)-axis, the first inequality is \[y\le 0,\] since we wish to include the boundary of the shaded area.

Since the shaded area is to the right of the \(y\)-axis, the second inequality is \[x\ge 0.\] The shaded region is above the line \(y=-1\), so the third equation is \[y\ge-1.\]

Which side of the line \(y = 1-x\) do we want? We want the side that includes the origin. When \(x = 0\) and \(y = 0, y < 1-x\), so this is the side we want.

So the fourth and final inequality is \[y\le 1-x.\]
