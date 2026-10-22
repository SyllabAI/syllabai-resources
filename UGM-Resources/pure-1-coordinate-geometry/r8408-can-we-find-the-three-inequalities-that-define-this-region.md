---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r8408
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r8408
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8408
  old_site_id: Q1047
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
      evidence: 'Line with gradient -2 through the ellipse''s positive y-intersection; three inequalities bound the region — the line work is 1.3.1/1.3.2 vocabulary; the ellipse '
      rationale: 'Canonical UGM title: “Can we find the three inequalities that define this region?”; exam provenance: O&C (Oxford & Cambridge SEG) 1969 Q7'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C (Oxford & Cambridge SEG) 1969 Q7
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/r8408/download/teacher-notes.pdf
  kind: printable
---

# Can we find the three inequalities that define this region?

## Question

In Fig. 1 (not drawn to scale) the curve has equation \(x^2+4y^2=16\). The straight line has a gradient of \(-2\) and passes through the intersection of the curve with the positive \(y\)-axis.

Write down the three inequalities which are sufficient to define the shaded area (including the three lines bounding it).

Fig. 1

## Suggestion

Should the inequalities be of the form \(y \leq f(x)\) or \(y \geq f(x)\)? Or are there other useful ways to write inequalities?

If you’re not sure which way round an inequality should go, choose a point not on the boundary; does it have coordinates that make the inequality work? If so, the point is on the side you want.

## Solution

Since the shaded area is inside the curve, the first inequality is \[x^2+4y^2\le 16.\] (We can check the direction of the inequality by testing with a point in the inside, say \((0,0)\). This gives \(0^2+4\times0^2=0\le 16\), so we have our inequality the correct way round.)

Since the shaded area is below the \(x\)-axis, the second inequality is \[y\le 0.\]

The third inequality will relate to the straight line, which we know must be of the form \(y=c-2x\). To find \(c\), we must first find where the curve crosses the positive \(y\)-axis.

When \(x=0\), \(4y^2=16\), and so \(y=\pm2\). Since we wish to know where the curve crosses the positive \(y\)-axis, this point is \((0,2)\) (so the \(y\)-intercept is 2).

Putting this point into the equation of the line (or by knowing the \(y\)-intercept), we find that \(c=2\), and so the equation of the line is \(y=2-2x\).

Since the shaded area is above the line, the third inequality is \[y\ge 2-2x.\]
