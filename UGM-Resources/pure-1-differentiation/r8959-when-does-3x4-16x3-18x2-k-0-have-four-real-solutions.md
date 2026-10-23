---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r8959
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r8959
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8959
  old_site_id: Q117
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
      evidence: 3x^4-16x^3+18x^2+k=0 has four real solutions exactly when -27<k<-5 — stationary-value
        structure is decisive
      rationale: 'Canonical UGM title: "When does $3x^4 - 16x^3 +18x^2 + k = 0$ have four real solutions?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2009, Q1F'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q1F
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/ZUJ6hAz4/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $3x^4 - 16x^3 +18x^2 + k = 0$ have four real solutions?

## Question

The equation in \(x\), \[3x^4 - 16x^3 +18x^2 + k = 0\] has four real solutions

1. when \(-27 < k < 5\);

---

1. when \(5< k <27\);

---

1. when \(-27< k <-5\);

---

1. when \(-5 < k <0\).

## Suggestion

The equation in \(x\), \[3x^4 - 16x^3 +18x^2 + k = 0\] has four real solutions

1. when \(-27 < k < 5\);

---

1. when \(5< k <27\);

---

1. when \(-27< k <-5\);

---

1. when \(-5< k <0\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ZUJ6hAz4/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ZUJ6hAz4)

The curve is the function \(y = 3x^4 - 16x^3 +18x^2 + k\).

## Solution

The equation in \(x\), \[3x^4 - 16x^3 +18x^2 + k = 0\] has four real solutions

1. when \(-27 < k < 5\);

---

1. when \(5< k <27\);

---

1. when \(-27< k <-5\);

---

1. when \(-5< k <0\).

*The understanding here is that the solutions are distinct.*

The number of distinct solutions to \(f(x)=3x^4 - 16x^3 +18x^2 + k = 0\) equals the number of times the graph \(y=f(x)\) crosses the \(x\)-axis, so it’ll be helpful to sketch the graph of \(y = f(x)\).

We can use differentiation to learn about the stationary points and therefore the shape of this graph. So we write

\[y=3x^4-16x^3+18x^2+k,\]

and then we differentiate to find

\[\begin{align*} y' &= 12x^3-48x^2+36x \\ &= 12x(x^2 - 4x + 3) \\ &= 12x(x-3)(x-1). \end{align*}\]

To find the stationary points, we solve \(y'= 0\). We see that the stationary points of the graph occur at \(x=0\), \(x=1\) and \(x=3\).

To classify these stationary points, we can use the second derivative. We have

\[\begin{align*} y'' &= 36x^2-96x+36 \\ &= 12(3x^2-8x+3). \end{align*}\]

Substituting,

\[\begin{align*} y''(0) &= 36 > 0, \\ y''(1) &= -24 < 0, \\ y''(3) &= 72 > 0, \end{align*}\]

so we find that the stationary points at \(x=0\) and \(x=3\) are minima, and the stationary point at \(x=1\) is a maximum.

If we now substitute \(x=0\), \(1\) and \(3\) into the equation, we find that the coordinates of our minima are \((0,k)\) and \((3,k-27)\), and the coordinates of the maximum are \((1,k+5)\).

Or alternatively, we can say we know the rough shape of the curve (see below) so we know which turning points are maxima, and which are minima.

This information about the curve is summarised in the sketch of \(y=f(x)\) given below.

The equation has four real solutions when the graph crosses the \(x\)-axis four times.

This occurs when the \(x\)-axis is in the position of the dotted line in the diagram above.

That is, it’s in a position such that the minima at \((0,k)\) and \((3,k-27)\) are below it, and the maximum at \((1,k+5)\) is above it.

In terms of inequalities, this is when \(k < 0\), \(k-27 < 0\) and \(k+5 > 0\).

So combining these, our final inequality is \(-5 < k < 0\), so the answer is (d).
