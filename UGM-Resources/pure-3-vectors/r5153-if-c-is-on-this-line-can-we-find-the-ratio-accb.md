---
created: 2026-10-26T04:13:07 (UTC +06:00)
source: https://undergroundmathematics.org/vector-geometry/r5153
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- vector-geometry
- type/review-question
resource_identity:
  ugm_id: r5153
  station: vector-geometry
  station_title: Vector Geometry
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5153
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: vector-geometry
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: vector-geometry
    validation_status: SUGGESTED
  spec_points:
  - code: 3.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-15 cross-map (cross-map-p3-vectors.json (P3c
        lane 15) @ syllabai-experimental 16c5f80)
      evidence: '''If C is on this line, can we find the ratio AC:CB?'' — section division of a line by
        a point expressed in position vectors; the spec''s 3.7.2 text explicitly excepts only the GENERAL
        ratio theorem while requiring ''understanding that the midpoint of a line segment...'' — specific-ratio
        division of a line by vector addition is the included core.'
      rationale: 'Canonical UGM title: If $C$ is on this line, can we find the ratio $AC:CB$?'
      validation_status: SUGGESTED
    title: carry out addition and subtraction of vectors and multiplication of a vector by a scalar, and
      interpret these operations in geometrical terms The general form of the ratio theorem is not included,
      but understanding that the midpoint of
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-vectors.json (P3c lane 15) @ syllabai-experimental 16c5f80
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-15
---

# If $C$ is on this line, can we find the ratio $AC:CB$?

## Question

Relative to an origin \(O\), the position vectors of two points, \(A\) and \(B\), are \(\begin{pmatrix}2\\5\end{pmatrix}\) and \(\begin{pmatrix}4\\1\end{pmatrix}\) respectively. The point \(C\) is on \(AB\). Given that the position of \(C\) is \(\begin{pmatrix}2t\\t\end{pmatrix}\), find the ratio \(AC:CB\).

The point \(D\) is on \(OC\), between \(O\) and \(C\), and \(\widehat{ADB}\) is a right angle. Given that the position vector of \(D\) is \(\begin{pmatrix}2s\\s\end{pmatrix}\), find the value of \(s\).

## Suggestion

A diagram will help. How can we express the fact that \(C\) is on \(AB\)?

If \(AD\) is perpendicular to \(DB\), what can we say about the gradients of \(AD\) and \(DB\)?

## Solution

Since \(C\) lies on the line \(AB\), we can write its position vector as \[\lambda\begin{pmatrix}2\\5\end{pmatrix} + (1-\lambda)\begin{pmatrix}4\\1\end{pmatrix} =\begin{pmatrix}4-2\lambda\\4\lambda +1\end{pmatrix}.\]

Equating the coefficients, we have \(2t= 4-2\lambda\) and \(t = 4\lambda +1\). Solving these simultaneous equations gives \(t = \dfrac{9}{5}\) and \(\lambda = \dfrac{1}{5}\).

The ratio \(AC:CB = (1-\lambda):\lambda = 4:1\).

**Approach 1: gradients multiply to \(-1\)**

We can see that the gradient of \(AD\) is \(\dfrac{5-s}{2-2s}\), while the gradient of \(DB\) is \(\dfrac{1-s}{4-2s}\), and since \(AD\) and \(BD\) are perpendicular,

\[\dfrac{5-s}{2-2s}\times\dfrac{1-s}{4-2s} = -1\]

which gives us that \[5s^2-18s+13=0.\]

This factorises into \[(5s-13)(s-1) = 0 \implies s = 1, \dfrac{13}{5}.\]

The value \(\dfrac{13}{5}\) gives \(D\) to be further from the origin than \(C\), so we can discard this, and \[D=(2,1).\]

The value of \(s\) we seek is \(1\).

**Approach 2: using the angle in a semicircle**

If \(A\),\(B\) and \(D\) are points on a circle with \(AB\) a diameter of that circle, then \(\widehat{ADB}\) is a right angle.

The converse is also true; if \(\widehat{ADB}=\dfrac{\pi}{2}\), then \(AB\) has to be a diameter of the circle.

Thus \(D\) is on the circle with diameter \(AB\). The midpoint of \(AB\) is \((3,3)\) and the length of \(AB\) is \(2\sqrt{5}\), and so the circle has centre \((3,3)\) and radius \(\sqrt{5}\).

Thus the equation of the circle is \((x-3)^2+(y-3)^2=5\). The point \(D\) is on this, so \((2s-3)^2 +(s-3)^2 = 5\), or \(5s^2-18s+13=0\).

The solution then proceeds as before.

**Approach 3: using the scalar product**

We know that the lines \(DA\) and \(DB\) have to be perpendicular.

Thus \((\mathbf{d}-\mathbf{a})\cdot(\mathbf{d}-\mathbf{b})=0,\) where \(\mathbf{d}\) is the position vector of \(D\), and where \(\cdot\) represents the [scalar product](https://undergroundmathematics.org/glossary/dot-product).

Now \(\mathbf{d} = \begin{pmatrix}2s\\s\end{pmatrix},\) so \(\mathbf{d}-\mathbf{a} =\begin{pmatrix}2s-2\\s-5\end{pmatrix} , \mathbf{d}-\mathbf{b}= \begin{pmatrix}2s-4\\s-1\end{pmatrix}.\)

Thus we have

\[\begin{align*} (\mathbf{d}-\mathbf{a})\cdot(\mathbf{d}-\mathbf{b})&=\begin{pmatrix}2s-2\\s-5\end{pmatrix} \cdot \begin{pmatrix}2s-4\\s-1\end{pmatrix}\\ &=(2s-2)(2s-4)+(s-5)(s-1)\\ &=5s^2-18s+13=0, \end{align*}\]

as before, and so \[\mathbf{d}=\begin{pmatrix}2\\1\end{pmatrix}, s = 1.\]
