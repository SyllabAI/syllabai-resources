---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7212
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7212
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7212
  old_site_id: Q1042
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: minimum area of triangle OXY in the unit square as x varies — calculus optimisation
        (an algebraic-inequality route is also recorded)
      rationale: 'Canonical UGM title: "What''s the minimum area of this variable triangle?"; exam provenance:
        UCLES O level Additional Mathematics 2, 1966, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1966, Q3
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/j46H5ZGN/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# What's the minimum area of this variable triangle?

## Question

\(OABC\) is a square of side \(\quantity{1}{ft.}\). A point \(X\) in \(AB\) and a point \(Y\) in \(BC\) are such that \(AX=\quantity{x}{ft.}\), \(BY=\quantity{kx}{ft.}\) and \(BY\) is longer than \(AX\). For a given value of \(k\), show that the minimum area of the triangle \(OXY\) is \[\quantity{\frac{4k-1}{8k}}{sq.ft.}\]

## Suggestion

Could we draw a picture of the problem?

Can we write the area of the triangle \(OXY\) as a function of \(x\)?

Interactive diagram

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/j46H5ZGN/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/j46H5ZGN)

The bar labelled ‘Area’ has a height that measures the area of triangle \(OXY\).

The bar labelled ‘Bound’ shows the value of \(\dfrac{4k-1}{8k}\).

For a given \(k\), how does the area vary with \(x\)?

## Solution

*Don’t get distracted by the choice of feet for units here, the question works perfectly well whatever the units given for length.*

From the picture, we can see that the easiest way to find the area of the triangle \(OXY\) is to subtract the areas of the triangles \(OAX\), \(BXY\) and \(OCY\) from the area of the square \(OABC\).

Writing the area as a function of \(x\), \(A(x)\), we find that \[A(x)=1-\frac{x}{2}-\frac{1}{2}kx(1-x)-\frac{1}{2}(1-kx)=\frac{1}{2}-\frac{x}{2}+\frac{kx^2}{2}.\]

Taking the derivative with respect to \(x\), we find that \[\frac{dA}{dx}=-\frac{1}{2}+kx,\] which is equal to zero when \(x=\dfrac{1}{2k}\). Since \(A(x)\) has a positive \(x^2\) coefficient, this must be a ‘vertex-down’ parabola, and we have a minimum.

Alternatively, since \(A(x)\) is a quadratic, we could have found the minimum point by completing the square.

So we have a minimum value of \[A\left(\dfrac{1}{2k}\right)=\frac{1}{2}-\frac{1}{4k}+\frac{1}{8k}=\frac{1}{2}-\frac{1}{8k}=\frac{4k-1}{8k}.\]

Therefore, for fixed \(k\), the minimum area of the triangle \(OXY\) is \[\quantity{\frac{4k-1}{8k}}{sq.ft.}\]

How does this expression behave as \(k\) varies?
