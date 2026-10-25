---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9809
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9809
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9809
  old_site_id: Q1028
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
      evidence: normals to the parabola y^2 = 4ax at parameters t1, t2 with t1 t2 = 2 meeting on the parabola
        - implicit/parametric normal work with the cyclic-quadrilateral coda
      rationale: 'Canonical UGM title: When do these normals to a parabola meet on the parabola?'
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

# When do these normals to a parabola meet on the parabola?

## Question

This question should be linked to the problem "Finding circles"

Find the equation of the normal to the parabola \(y^2=4ax\) at the point \((at^2,2at)\).

The parameters of the points \(P\), \(Q\) are \(t_1\) and \(t_2\) respectively. Show that, if \(PQ\) passes through the point \((-2a,0)\), then \(t_1t_2=2\) and the normals at \(P\) and \(Q\) to the parabola meet at a point \(R\) on the parabola.

If \(O\) is the origin, show, by considering the gradients of the sides of the quadrilateral \(OPQR\) or otherwise, that the circumcircle of the triangle \(PQR\) passes through \(O\).

## Suggestion

How can we find the gradient of the parabola at a point with parameter \(t\)?

If we have the gradient of the normal through the point \((at^2,2at)\), what is the equation of the line?

The parameters of the points \(P\), \(Q\) are \(t_1\) and \(t_2\) respectively. Show that, if \(PQ\) passes through the point \((-2a,0)\), then \(t_1t_2=2\)…

What is the gradient of the line that passes through \(P\) and \(Q\)? What about its equation?

…and the normals at \(P\) and \(Q\) to the parabola meet at a point \(R\) on the parabola.

Could we write down the equations of the normals at \(P\) and \(Q\), and find where they intersect?

Aren’t we really being asked to show that \(OPQR\) is a cyclic quadrilateral? What do we know about cyclic quadrilaterals?

## Solution

Taking the derivative of the equation \(y^2=4ax\) with respect to \(x\) we find that \[2y\frac{dy}{dx}=4a \qquad \Longrightarrow \qquad \frac{dy}{dx}=\frac{2a}{y}=\frac{2a}{2at}=\frac{1}{t}.\] The gradient of normal to the parabola at the point \((at^2,2at)\) is therefore \(-t\) since \[\frac{1}{t}\times -t=-1.\] The equation of the normal is then \[y-2at=-t(x-at^2) \qquad \Longrightarrow \qquad y=-tx+2at+at^3.\]

The parameters of the points \(P\), \(Q\) are \(t_1\) and \(t_2\) respectively. Show that, if \(PQ\) passes through the point \((-2a,0)\), then \(t_1t_2=2, ...\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/JhGyhfHZ/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/JhGyhfHZ)

The gradient of the line

\(PQ\)

is

\[\frac{2at_2-2at_1}{at_2^2-at_1^1}=\frac{2(t_2-t_1)}{(t_2-t_1)(t_1+t_2)}=\frac{2}{t_1+t_2}.\]

The equation of the line through points

\(P\)

and

\(Q\)

is then

\[y-2at_1=\frac{2}{t_1+t_2}(x-at_1^2).\]

This will pass through the point

\((-2a,0)\)

if and only if

\[\begin{align*} 0-2at_1&=\frac{2}{t_1+t_2}(-2a-at_1^2) \\ &\iff t_1 = \frac{1}{t_1+t_2}(2+t_1^2) \\ &\iff t_1(t_1+t_2) = 2+t_1^2 \\ &\iff t_1 t_2 = 2, \end{align*}\]

as required.

…and the normals at \(P\) and \(Q\) to the parabola meet at a point \(R\) on the parabola.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ZQCGfjpf/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ZQCGfjpf)

The two normals passing through

\(P\)

and

\(Q\)

have the equations

\[\begin{align*} y &=-t_1x+2at_1+at_1^3 \\ y &=-t_2x+2at_2+at_2^3, \end{align*}\]

using the first part of the question. They intersect when

\[\begin{align*} -t_1x+2at_1+at_1^3 &= -t_2x+2at_2+at_2^3 \\ \Longrightarrow \qquad 2a(t_2-t_1)+a(t_2^3-t_1^3) &= x(t_2-t_1) \\ \end{align*}\]

and factorising

\((t_2^3-t_1^3)\)

gives

\[\begin{align*} \qquad 2a(t_2-t_1)+a(t_2-t_1)(t_1^2+t_1t_2+t_2^2) &= x(t_2-t_1) \end{align*}\]

Since

\(t_1\neq t_2\)

, as we are assuming

\(P\)

and

\(Q\)

are distinct, we can divide through by

\((t_2-t_1)\)

to get

\[x=a(t_1^2+t_1t_2+t_2^2+2).\]

Substituting for

\(2=t_1t_2\)

we find that

\[\begin{align*} x &=a(t_1^2+2t_1t_2+t_2^2) \\ &= a(t_1+t_2)^2. \end{align*}\]

Using this expression, we can substitute back into one of the original equations for the normal to find

\[\begin{align*} y &= -t_1a(t_1+t_2)^2+2at_1+at_1^3 \\ &=-t_1^3a-2at_1^2t_2-at_1t_2^2+2at_1+at_1^3\\ &=-2a \times 2 \times t_1 - 2 \times at_2+2at_1\\ &= -2a(t_1+t_2). \end{align*}\]

Thus \(R=\left(a(t_1+t_2)^2,-2a(t_1+t_2)\right)\), and comparing this to the general point on the parabola \((at^2,2at)\), we can see that \(R\) is clearly on the curve.

Since \(P = (at_1^2, 2at_1)\), \(Q = (at_2^2, 2at_2)\), \(R = (a(t_1+t_2)^2, -2a(t_1+t_2))\), and \(O = (0, 0)\), then:

\(OP\) has gradient \(\dfrac{2}{t_1}\), \(PQ\) has gradient \(\dfrac{2}{t_1+t_2}\), \(QR\) has gradient \(-\dfrac{2}{t_1}\), while \(RO\) has gradient \(-\dfrac{2}{t_1+t_2}\).

Thus \(OP\) and \(QR\) are reflections of each other in a vertical or horizontal line, and \(PQ\) and \(OR\) are likewise.

The diagram shows that angle \(\widehat{PQR}\) is \(180^\circ-\alpha -\beta\), and so the angles \(\widehat{POR}\) and \(\widehat{PQR}\) add to \(180^\circ\), and therefore \(OPQR\) is a cyclic quadrilateral.

Thus \(O\) lies on the circumcircle of \(PQR\), as required.
