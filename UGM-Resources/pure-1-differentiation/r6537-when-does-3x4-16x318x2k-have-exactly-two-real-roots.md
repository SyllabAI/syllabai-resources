---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r6537
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r6537
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6537
  old_site_id: Q144
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: turning points of 3x^4-16x^3+18x^2 with nature, sketch, and the k-set for exactly two
        real roots
      rationale: 'Canonical UGM title: "When does $3x^4-16x^3+18x^2=k$ have exactly two real roots?";
        exam provenance: UCLES A level Mathematics B 1, 1983, Q6'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: turning points of 3x^4-16x^3+18x^2 with nature, sketch, and the k-set for exactly two
        real roots
      rationale: 'Canonical UGM title: "When does $3x^4-16x^3+18x^2=k$ have exactly two real roots?";
        exam provenance: UCLES A level Mathematics B 1, 1983, Q6'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics B 1, 1983, Q6
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/SSm64SXN/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $3x^4-16x^3+18x^2=k$ have exactly two real roots?

## Question

Find the coordinates of each turning point on the graph of \(y=3x^4-16x^3+18x^2\) and determine in each case whether it is a maximum point or a minimum point.

Sketch the graph of \(y=3x^4-16x^3+18x^2\), and state the set of values of \(k\) for which the equation \(3x^4-16x^3+18x^2=k\) has precisely two real roots for \(x\).

## Suggestion

How can we determine if a turning point is a minimum or a maximum?

What does the line \(y=k\) look like on the graph?

We could try using a ruler as \(y=k\), and explore what happens when we add this to the graph of \(y=3x^4-16x^3+18x^2\) as we vary \(k\).

## Solution

We find that \(\dfrac{dy}{dx}=12x^3-48x^2+36x=12x(x^2-4x+3)=12x(x-1)(x-3)\).

Since turning points occur where \(\dfrac{dy}{dx}=0\), the turning points are at \(x=0,1\) or \(3\).

When \(x=0\) we have that \(y=0\), when \(x=1\) we find that \(y=5\), and when \(x=3\), \(y=-27\).

Therefore the turning points are \((0,0),\) \((1,5)\) and \((3,-27)\).

We can consider \(y'=\dfrac{dy}{dx}\) at different values of \(x\) to identify if a point is a minimum or a maximum.

At \(x=-\dfrac{1}{2}\) we observe that \(\dfrac{dy}{dx}<0\) and, at \(x=\dfrac{1}{2}, \dfrac{dy}{dx}>0\). This shows us that \((0,0)\) is a minimum point.

At \(x=\dfrac{3}{2}\) we can see that \(\dfrac{dy}{dx}>0\), so considering the result above at \(x=\dfrac{1}{2}\) this shows that \((1,5)\) is a maximum.

It is evident that for all \(x>3\), \(\dfrac{dy}{dx}>0\), implying that \((3,-27)\) is a minimum point.

Or else we could say that \(y'' = 36x^2-96x+36 = 12(3x^2-8x+3)\).

So \(y''(0)\) is positive, \(y''(1)\) is negative and \(y''(3)\) is positive.

This means \((0,0),\) is a minimum, \((1,5)\) is a maximum, and \((3,-27)\) is a minimum.

From the information that we have, we can sketch the graph of \(y=3x^4-16x^3+18x^2\) as follows.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/SSm64SXN/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/SSm64SXN)

By considering the values of \(k\) for which there are exactly two intersections between the graph we have just sketched and \(y=k\), we find that the values required are \[-27<k<0, \quad \text{and} \quad 5<k.\]
