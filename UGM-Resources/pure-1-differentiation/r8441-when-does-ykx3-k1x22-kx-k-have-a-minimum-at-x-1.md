---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8441
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8441
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8441
  old_site_id: null
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
      evidence: cubic kx^3-(k+1)x^2+(2-k)x-k has its minimum at x=1 precisely for k>1/2 — dy/dx(1)=0
        plus nature conditions on k
      rationale: 'Canonical UGM title: "When does $y=kx^3-(k+1)x^2+(2-k)x-k$ have a minimum at $x =1$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2014, Q1C'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: cubic kx^3-(k+1)x^2+(2-k)x-k has its minimum at x=1 precisely for k>1/2 — dy/dx(1)=0
        plus nature conditions on k
      rationale: 'Canonical UGM title: "When does $y=kx^3-(k+1)x^2+(2-k)x-k$ have a minimum at $x =1$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2014, Q1C'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2014, Q1C
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/kbTxRppv/width/463/height/469/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $y=kx^3-(k+1)x^2+(2-k)x-k$ have a minimum at $x =1$?

## Question

The cubic \[y=kx^3-(k+1)x^2+(2-k)x-k\]

has a turning point, that is a minimum, when \(x = 1\) precisely for

\[\text{(a)} \quad k>0, \quad \text{(b)} \quad 0<k<1, \quad \text{(c)} \quad k > \dfrac{1}{2}, \quad \text{(d)} \quad k < 3, \quad \text{(e) all values of } x.\]

## Suggestion

How can we find the turning points on a graph?

How can we find out what kind of turning points they are?

## Solution

What happens if we differentiate \(y\)? We find \(\dfrac{dy}{dx} = 3kx^2-2(k+1)x+2-k\).

If we substitute \(x = 1\) into this, we find

\[\dfrac{dy}{dx} = 3k -2k -2 +2 -k = 0.\]

Thus we have a stationary point at \(x = 1\) whatever the value of \(k\). But when is this a minimum?

Differentiating again, we find that \(\dfrac{d^2y}{dx^2} = 6kx -2k -2\). At \(x = 1\), this gives \(\dfrac{d^2y}{dx^2}= 4k-2\).

The turning point will be a minimum if \(\dfrac{d^2y}{dx^2} > 0 \iff k > \dfrac{1}{2}\).

Thus the answer is (c).

Since our curve is a cubic, \(\dfrac{d^2y}{dx^2} = 0\) would always mean a point of inflection so is excluded from the inequality.

For higher order curves this isn’t always the case – consider \(y=(x-1)^4\) at the point \(x=1\), for instance.

This applet illustrates the shape of our cubic as \(k\) varies.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/kbTxRppv/width/463/height/469/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/kbTxRppv)
