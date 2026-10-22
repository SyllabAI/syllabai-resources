---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r5887
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r5887
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5887
  old_site_id: Q3029
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Sum/product of two numbers -> plot the corresponding graphs and read the intersection as the solution — the graph-equation relationship verbatim (hyperbola is c'
      rationale: 'Canonical UGM title: “If we know the sum and product of two numbers, what are they?”; exam provenance: UCLES 1970 Q1'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1970 Q1
task: T-UGM-IMPORT-3
---

# If we know the sum and product of two numbers, what are they?

## Question

The sum and product of two numbers, \(x\) and \(y\), are \(10\) and \(12\) respectively. Form appropriate equations, plot [*on graph paper*] the corresponding graphs and hence obtain approximate values for \(x\) and \(y\).

## Interactive diagram

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/p8UAQ3Pm)

The red rectangle has a horizontal side of length \(x\).

The vertical side has length \(y\), and the perimeter is fixed at \(20\). The area of the red rectangle is shown.

## Solution

The information given in the question tells us that

\[\begin{align*} x + y &= 10, \\ xy &= 12. \end{align*}\]

By rearranging these equations to make

\(y\)

the subject, we get

\[\begin{align*} y &= 10 - x, \\ y &= \frac{12}{x}. \end{align*}\]

The following graph shows both the line (corresponding to the first equation) and the hyperbola (corresponding to the second equation).

The graph shows that there is an approximate solution with \(x \approx 1.4\) and \(y \approx 8.6\) and another one with \(x \approx 8.6\) and \(y \approx 1.4\). These give essentially the same solution, as we are looking for two numbers with a given sum and given product.

The equations can be solved exactly, and without much difficulty. By substituting the equation

\(y = 10 - x\)

into the equation

\(xy = 12\)

, we have

\[x(10 - x) = 12\]

so that

\[x^2 - 10x + 12 = 0.\]

By the

quadratic formula

, we have that

\[\begin{align*} x &= \frac{10 \pm \sqrt{(-10)^2 - 4 \cdot 1 \cdot 12}}{2 \cdot 1} \\ &= \frac{10 \pm \sqrt{100 - 48}}{2} \\ &= \frac{10 \pm \sqrt{52}}{2}. \end{align*}\]

The smaller of these values is \(1.394448\!\ldots\), which is close to our visual estimate.
