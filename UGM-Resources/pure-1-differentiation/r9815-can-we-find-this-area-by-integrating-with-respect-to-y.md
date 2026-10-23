---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9815
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9815
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9815
  old_site_id: Q207
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent to 27y^2=x^3 at (12,8) via y=x^(3/2)/(3sqrt3) — rational-index power rule; the
        integration-wrt-y part carries bearings beyond P1 1.8 (recorded)
      rationale: 'Canonical UGM title: "Can we find this area by integrating with respect to $y$?";
        exam provenance: UCLES A level Mathematics 1, 1953, Q12'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1953, Q12
task: T-UGM-IMPORT-7
---

# Can we find this area by integrating with respect to $y$?

## Question

Sketch the form of the curve \(27y^2=x^3\), and find the equation of the tangent at the point \(P(12,8)\) on the curve.

Verify this tangent cuts the curve again at the point \(Q(3,-1)\).

If \(O\) is the origin, find by integration the area enclosed by the arcs \(OP\), \(OQ\) of the curve and the line \(PQ\). [Integration with respect to \(y\) is recommended.]

## Solution

Sketch the form of the curve \(27y^2=x^3\), …

The graph passes through the point \((0,0)\), and at no other point crosses the \(x\)- or \(y\)-axis.

The graph does not exist for negative \(x\).

The curve will be symmetric about the \(x\)-axis, due to the \(y^2\) term.

We can rearrange the equation for positive \(y\) values as \(y=\frac{1}{\sqrt{27}}x^{3/2}\).

Since \(\dfrac{3}{2}>1\), this will be between the graph of \(y=x\) and \(y=x^2\), so it will look something like this…

… and find the equation of the tangent at the point \(P(12,8)\) on the curve.

[Differentiating implicitly](https://undergroundmathematics.org/glossary/implicit-differentiation), we find that \[54y\frac{dy}{dx}=3x^2,\] and so \[\frac{dy}{dx}=\frac{1}{18}\frac{x^2}{y}.\] Evaluating this at \(P(12,8)\), the gradient of the tangent is \[\frac{1}{18}\frac{12^2}{8}=\frac{144}{144}=1.\] So the tangent has the form \[y=x+c.\]

Since we know that the tangent passes through \((12,8)\), we find that \[8=12+c \Longrightarrow c=-4.\] So the equation of the tangent to the curve at \(P\) is \[y=x-4.\]

For the line \(y=x-4\), we have \[-1=3-4=-1\] and so the line passes through \(Q\).

For the curve, we have \[27y^2=27\times (-1)^2=27\ \text{and}\ x^3=3^3=27.\]

So the curve and the line intersect again at \(Q(3,-1)\).

Here’s the area we want to find:

To find the shaded area, we find the area of the trapezium bounded by the lines \(x=0, y=8\), \(y=-1\) and \(PQ\) and then subtract the area under the curve \(x=3y^{2/3}\) between \(y=-1\) and \(y=8\).

The area of the trapezium is \[\frac{12+3}{2}\times 9=\frac{135}{2}.\]

The area under the curve is

\[\begin{align*} \int_{-1}^8 3y^{2/3}\, dy &=\left[\frac{9}{5}y^{5/3}\right]^8_{-1}\\ &=\frac{9\times32}{5}+\frac{9}{5}\\ &=\frac{297}{5}. \end{align*}\]

So the area we want is \[\frac{135}{2}-\frac{297}{5}=\frac{81}{10}.\]
