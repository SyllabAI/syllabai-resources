---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7042
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7042
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7042
  old_site_id: Q47
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: the parabola y^2 = 4ax and the ellipse 2x^2 + y^2 = c^2 cutting at right angles via the
        normal-midpoint proof - implicit/parametric derivatives of both curves
      rationale: 'Canonical UGM title: Can we show this parabola and this ellipse meet at right angles?'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we show this parabola and this ellipse meet at right angles?

## Question

The normal at a point \(P\) on the parabola \(y^2=4ax\) meets the ellipse \(2x^2+y^2=c^2\) in the points \(M\), \(N\). Prove that \(P\) is the mid-point of \(MN\).

Hence, or otherwise, prove that the conics cut at right angles.

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/hnFbS96n/width/600/height/600/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/hnFbS96n)

In this applet you can change the parameters of the parabola and the ellipse. The green line is the normal to the parabola at the point \(P = (at^2, 2at)\).

How could we find the gradient of the parabola and the equation of its normal?

We only need to show that \(P\) is the midpoint of \(MN\) – could we do this without finding M and N?

What happens when we move the points \(M\) and \(N\) near to the point of intersection?

## Solution

Let’s find the equation of the normal through P. Let the point \(P\) have the coordinates \((at^2,2at)\).

[Implicitly differentiating](https://undergroundmathematics.org/glossary/implicit-differentiation) the formula for the parabola gives \[2 y \frac{dy}{dx} = 4a \qquad\implies\qquad \frac{dy}{dx} = \frac{2a}{y} = \frac{1}{t}\] and so the normal has slope \[m = \frac{-1}{dy/dx} = -t.\]

Then the equation of the normal is \[y - 2at = -t(x - at^2)\] or \[y = (2a - x + at^2)t.\]

Substituting into \(2x^2+y^2=c^2\), we find that at the points \(M\) and \(N\) \[2x^2 + (2a - x + at^2)^2 t^2 = c^2\] which we can expand to give \[(2+t^2)x^2 - 2at^2(2+t^2) x + a^2t^2(2+t^2)^2 - c^2 = 0.\]

A quadratic equation \(Ax^2+Bx+C=0\) has roots \(x=\frac{-B}{2A}\pm\frac{\sqrt{B^2-4AC}}{2A}\) so the midpoint of its roots is at \(x=\frac{-B}{2A}\). Hence the midpoint of \(MN\) has \(x\)-coordinate \[x=\dfrac{2at^2(2+t^2)}{2(2+t^2)} = at^2,\] so \(P\) is indeed the midpoint of \(MN\).

What happens as the points $ M, P$ and \(N\) gradually approaches \(Q\), the point where the ellipse and parabola intersect?

Since \(P\) is the midpoint of \(MN\), as we take the limit, the chord \(MPN\) becomes closer and closer to being the tangent to the ellipse at \(Q\).

But all the while, the line \(MPN\) is the normal to the parabola.

This means that in the limit, \(MPN\) is both the tangent to the ellipse and the normal to the parabola, that is, the ellipse and parabola meet at right angles (they are orthogonal).
