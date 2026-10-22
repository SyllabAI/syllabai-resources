---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8045
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8045
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8045
  old_site_id: Q1076
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'Chord of a parabola: line meets curve, then midpoint (coordinate-geometry flavour).'
      rationale: 'Canonical UGM title: “Can we find the midpoint of a chord of this parabola?”; exam provenance:
        UCLES 1982 Q13'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1982 Q13
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/Hxq7nrsY/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the midpoint of a chord of this parabola?

## Question

Given that \(x_1\) and \(x_2\) are the roots of \(ax^2 + bx + c = 0\), state in terms of some or all of \(a\), \(b\), \(c\): (i) the condition that \(x_1 = x_2\), (ii) the value of \(x_1 + x_2\).

1. Find the values of \(m\) for which the line \(y = mx\) is a tangent to the curve \(y^2 = 3x - 1\).
2. The line \(y = 2x\) meets the curve \(3y = x^2 - 10\) at the points \(A(x_1, y_1)\) and \(B(x_2, y_2)\).
  1. Obtain the quadratic equation whose roots are \(x_1\) and \(x_2\).
  2. Without solving this equation, find the \(x\) co-ordinate of the midpoint of \(AB\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Hxq7nrsY/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Hxq7nrsY)

The red curve here is \(y^2 = 3x-1\), while the blue line is \(y = mx\).

## Solution

We know that \(a \neq 0\), since otherwise the equation would only have one root.

The [discriminant](https://undergroundmathematics.org/glossary/discriminant) of the quadratic equation \(ax^2 + bx + c = 0\) is given by \(b^2 - 4ac\).

There is one repeated root (that is, \(x_1 = x_2\)) if and only if \(b^2 - 4ac = 0\), or equivalently \(b^2 = 4ac\).

Since the roots of the quadratic equation \(ax^2 + bx + c = 0\) are \(x_1\) and \(x_2\), we can rewrite the equation as \(a(x - x_1)(x - x_2) = 0\).

Expanding this expression then yields \[ax^2 - a(x_1 + x_2)x + ax_1x_2 = 0.\] Comparing these coefficients with the ones in the original equation yields \(b = -a(x_1 + x_2)\) and hence \(x_1 + x_2 = -\dfrac{b}{a}\).

By using the quadratic formula we get

\[\begin{align*} x_1 + x_2 &= \frac{-b + \sqrt{b^2 - 4ac}}{2a} + \frac{-b - \sqrt{b^2 - 4ac}}{2a}\\ &= \frac{-b + \sqrt{b^2 - 4ac} - b - \sqrt{b^2 - 4ac}}{2a}\\ &= \frac{-2b}{2a}\\ &= -\frac{b}{a} \end{align*}\]

**Alternative Solution**

The line \(y = mx\) is a tangent to the curve \(y^2 = 3x - 1\) if the line touches the curve at exactly one point.

The intersection points are found by solving the equations of the line and the curve simultaneously.

Substituting \(y=mx\) into the equation of the curve gives \(m^2 x^2 = 3x - 1\), which is equivalent to the equation \(m^2x^2 - 3x + 1 = 0\).

By part (i) above, we know that we have exactly one root if and only if \(9 = 4m^2\), so \(m = \pm \dfrac{3}{2}\).

As in part (a), the intersection points of a line with a curve are obtained by solving their equations simultaneously.

To find their \(x\)-coordinates, we substitute \(y=3x\) into the equation of the curve to give \(6x=x^2-10\), which rearranges to \(x^2 - 6x - 10 = 0\).

We know that the \(x\) coordinates of the points \(A\) and \(B\) are \(x_1\) and \(x_2\) respectively, so the midpoint of \(AB\) has \(x\)-coordinate \(\dfrac{x_1+x_2}{2}\).

By part (ii) above, we know that \(x_1 + x_2 = 6\), since they are the roots of the equation \(x^2 -6x - 10 = 0\). Thus the midpoint of \(AB\) has \(x\)-coordinate \(\dfrac{6}{2}=3\).
