---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r6703
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r6703
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6703
  old_site_id: Q1081
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: x^3-3a^2x+b has three distinct real roots implies 4a^6>b^2 — turning-point condition
        is the load-bearing argument
      rationale: 'Canonical UGM title: "When does this cubic equation have three distinct real roots?";
        exam provenance: UCLES A level Further Mathematics 2, 1958, Q3(ii)'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Further Mathematics 2, 1958, Q3(ii)
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/dfSZ4gqk/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does this cubic equation have three distinct real roots?

## Question

Prove, by considering the turning points on the graph \(y=x^3-3a^2x+b\) or otherwise, that if the equation \(x^3-3a^2x+b=0\) has three distinct real roots, then \(4a^6>b^2\).

## Suggestion

Where are the turning points of \(y=x^3-3a^2x+b\), and how many are there?

What is the effect of \(a\) being negative rather than positive? What happens when \(a=0\)?

What happens to the number of roots as we translate the curve in the \(y\)-direction?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/dfSZ4gqk/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/dfSZ4gqk)

## Solution

The stationary points of \(y=x^3-3a^2x+b\) occur when \[\frac{\mathrm{d}y}{\mathrm{d}x}=3x^2-3a^2=0.\] We therefore have two stationary points, at \(x=\pm a\), where \(a\neq 0\).

If \(a=0\), there is a single stationary point at \(x=0\), and it’s impossible to get three distinct roots in this case. You could try to sketch some graphs of cubic functions to see this.

Therefore, taking

\(a\neq 0\)

, we find that the two stationary points are at

\[\begin{align*} x=a, y &= a^3-3a^3 + b = -2a^3+b \\ x=-a, y &= -a^3+3a^3 + b = 2a^3+b. \end{align*}\]

If the curve is to have three distinct roots, then the \(y\)-values of the stationary points must have opposite signs.

So EITHER \[-2a^3+b >0\,\, \text{and} \,\, 2a^3+b < 0, \,\, \text{which gives} \,\, 2a^3 < b < -2a^3,\] OR \[-2a^3+b < 0\,\, \text{and} \,\, 2a^3+b > 0, \,\, \text{which gives}\,\, -2a^3 < b < 2a^3.\]

The first of these is only possible if \(a\) is negative, while the second is only possible if \(a\) is positive. In either case, we can combine these inequalities to get \(b^2 < 4a^6\).

The graph below shows the situation if \(a\) is positive.

Three different possibilities for the number of roots of \(y=x^3-3a^2x+b\).
