---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r8471
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r8471
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8471
  old_site_id: Q42
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
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UKMT 2012 Q16
task: T-UGM-IMPORT-3
---

# Can we find the area of this inscribed quadrilateral?

## Question

The diagram shows the ellipse whose equation is \(x^2+y^2-xy+x-4y=12\). The curve cuts the \(y\)-axis at points \(A\) and \(C\) and cuts the \(x\)-axis at points \(B\) and \(D\). What is the area of the inscribed quadrilateral \(ABCD\)?

## Solution

If we know the coordinates of the four points \(A\), \(B\), \(C\) and \(D\), then we can split the quadrilateral into two triangles, \(ABD\) and \(BCD\). Using the coordinates, we can find the base (\(BD\)) of these triangles and their heights (\(OA\) and \(OC\), where \(O\) is the origin). We can therefore find their areas and add them to obtain the area of \(ABCD\).

The areas of the triangles are \(\frac12 BD\times OA\) and \(\frac12 BD\times OC\); if we add these together, we obtain \(\frac12 BD(OA+OC)=\frac12 BD\times AC\) for the area of the quadrilateral, that is, half of the product of the diagonals.

This formula is true for any quadrilateral with perpendicular diagonals. Can you see why? Is it true even if the quadrilateral is not [convex](https://undergroundmathematics.org/glossary/convex-shape)?

At the points \(A\) and \(C\) we have \(x=0\), so the \(y\)-coordinate must satisfy \(y^2-4y-12=0\), that is, \(y=6\) or \(y=-2\). So from the diagram, we see that \(A=(0,6)\) and \(C=(0,-2)\).

Similarly, we have \(y=0\) at the points \(B\) and \(D\) and so \(x^2+x-12=0\), that is, \(x=3\) or \(x=-4\). Therefore using the diagram, we get \(B=(3,0)\) and \(D=(-4,0)\).

Therefore the triangle \(ABD\) has area \(\frac12\times7\times6=21\) and \(BCD\) has area \(\frac12\times7\times2=7\), and so the quadrilateral has area \(21+7=28\).
