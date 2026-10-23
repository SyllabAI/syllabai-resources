---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8399
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8399
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8399
  old_site_id: Q3018
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent to y=(x+k)^2 at x=2k (expand-then-differentiate; the chain-rule alternative
        is named in the solution) plus the midpoint locus
      rationale: 'Canonical UGM title: "Can we find the locus of a midpoint created by a parabola?";
        exam provenance: UCLES O level Additional Mathematics 2, 1977, Q14'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent to y=(x+k)^2 at x=2k (expand-then-differentiate; the chain-rule alternative
        is named in the solution) plus the midpoint locus
      rationale: 'Canonical UGM title: "Can we find the locus of a midpoint created by a parabola?";
        exam provenance: UCLES O level Additional Mathematics 2, 1977, Q14'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1977, Q14
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/dDg5zVQh/width/513/height/620/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the locus of a midpoint created by a parabola?

## Question

Show that the tangent to the curve \(y = (x+k)^2\) at the point where \(x = 2k\) is \[y + 3k^2 = 6kx.\]

This tangent meets the \(x\)-axis at \(P\) and the \(y\)-axis at \(Q\). The mid-point of \(PQ\) is \(M\).

Find the co-ordinates of \(M\) in terms of \(k\) and hence deduce the equation of the locus of \(M\) as \(k\) varies.

## Suggestion

To find the gradient, it might help to expand the bracket.

Given two points in the plane whose coordinates are \((x_1,y_1)\) and \((x_2,y_2)\), can we write down the coordinates of their midpoint?

## Solution

We have \(y = (x+k)^2 = x^2+2kx+k^2\), and so \(\dfrac{dy}{dx}= y' = 2x + 2k\). (If you know the [chain rule](https://undergroundmathematics.org/glossary/chain-rule), you can alternatively use this here.)

This tells us that when \(x = 2k, y = 9k^2\), and \(y' = 6k\). So the gradient of the tangent is \(6k\).

We can write the equation of the tangent as \(y = 6kx+c\), and we know that the point \((2k, 9k^2)\) is on the line, so \[9k^2 = 12k^2 +c \implies c = -3k^2 .\]

Thus the equation is

\(y = 6kx - 3k^2\)

or, after rearranging,

\[\begin{equation}\label{eq:given-form-for-tangent} y + 3k^2 = 6kx, \end{equation}\]

as required.

From \(\eqref{eq:given-form-for-tangent}\), the coordinates of \(Q\) are just \((0,-3k^2)\). Similarly, the \(x\)-coordinate of \(P\) is given by \[0 = 6kx - 3k^2,\] and so \(x = \dfrac{k}{2}\). Thus, the coordinates of \(P\) are \(\left( \dfrac{k}{2}, 0 \right)\).

The midpoint of the line segment \(PQ\) is thus \[\left(\dfrac{0+k/2}{2}, \dfrac{-3k^2+0}{2} \right) = \left( \dfrac{k}{4}, -\dfrac{3k^2}{2} \right).\]

To find the locus of \(M\), we need to eliminate \(k\) here. So if \((x,y)\) is on the locus of \(M\), \[x = \dfrac{k}{4} \implies k = 4x,\quad y = -\dfrac{3k^2}{2} \implies y = -24x^2.\]

Now we have the locus of \(M\) as \(k\) varies; a vertex-up parabola, with its maximum at the origin. You can observe the locus in the following applet by varying \(k\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/dDg5zVQh/width/513/height/620/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/dDg5zVQh)
