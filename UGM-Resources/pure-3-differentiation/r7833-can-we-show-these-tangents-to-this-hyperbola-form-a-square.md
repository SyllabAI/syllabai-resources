---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7833
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7833
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7833
  old_site_id: Q115
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
      evidence: tangents to xy = 1 and x^2 - y^2 = 2 at P and Q forming the square PMQN - gradients from
        implicit differentiation (dy/dx = x/y on the hyperbola), the perpendicularity and the equal sides
      rationale: 'Canonical UGM title: Can we show these tangents to this hyperbola form a square?'
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

# Can we show these tangents to this hyperbola form a square?

## Question

Sketch on the same axes the two curves

\(C_1\)

and

\(C_2\)

, given by

\[\begin{align*} C_1&: xy &= 1, \\ C_2&: x^2-y^2 &= 2. \end{align*}\]

The curves intersect at \(P\) and \(Q\). Given that the coordinates of \(P\) are \((a,b)\) (which you need not evaluate), write down the coordinates of \(Q\) in terms of \(a\) and \(b\).

The tangent to \(C_1\) through \(P\) meets the tangent to \(C_2\) through \(Q\) at the point \(M\), and the tangent to \(C_2\) through \(P\) meets the tangent to \(C_1\) through \(Q\) at \(N\). Show that the coordinates of \(M\) are \((-b,a)\) and write down the coordinates of \(N\).

Show that \(PMQN\) is square.

## Suggestion

Sketch on the same axes the two curves

\(C_1\)

and

\(C_2\)

, given by

\[\begin{align*} C_1&: xy &=1, \\ C_2&: x^2-y^2&=2. \end{align*}\]

Can we sketch the hyperbola \(xy=1\)?

Can we sketch the hyperbola \(x^2-y^2=2\)?

Does our sketch tell us what the coordinates of \(Q\) are?

Could we find the equations of the tangents and then try to solve them together?

Along the way, we could need to use the information that \((a,b)\) lies on both \(C_1\) and \(C_2\). That is, we know that \(ab = 1\) and \(a^2 - b^2 = 2\).

Show that \(PMQN\) is a square.

What will the gradients of the tangents have to multiply to?

What must be true for the sides of the quadrilateral?

## Solution

Sketch on the same axes the two curves

\(C_1\)

and

\(C_2\)

, given by

\[\begin{align*} C_1&: xy &=1, \\ C_2&: x^2-y^2&=2. \end{align*}\]

Note that \(C_2\) does not intersect the \(y\)-axis.

If \(P\) has coordinates \((a,b)\), then \(Q\) has coordinates \((-a,-b)\).

This is easily checked by substituting back into the equations for \(C_1\) and \(C_2\).

The gradient of \(C_1\) at any point is given by: \[y+x\frac{dy}{dx}=0 \quad \Longrightarrow \quad \frac{dy}{dx}=-\frac{y}{x}.\] Similarly, the gradient of \(C_2\) at any point is given by \[2x-2y\frac{dy}{dx}=0 \quad \Longrightarrow \quad \frac{dy}{dx}=\frac{x}{y}.\] Thus the tangent to \(C_1\) at \(P(a,b)\) has equation \[y-b=-\frac{b}{a}(x-a),\] while the tangent to \(C_2\) at \(Q(-a,-b)\) has equation \[y+b=\frac{a}{b}(x+a).\]

The intersection of these two lines is at \(M\), so we solve the equations simultaneously to find the coordinates of \(M\).

In the process of doing this, we need to use the information that

\((a,b)\)

are the coordinates of point

\(P\)

, that is,

\((a,b)\)

lies on both

\(C_1\)

and

\(C_2\)

. So we should expect to use the equations

\[\begin{align*} ab &= 1 \\ a^2 - b^2 &= 2 \end{align*}\]

at some point.

We want to solve \[\frac{a}{b}x + \frac{a^2 - b^2}{b} = -\frac{b}{a}x + 2b.\] Multiplying through by \(ab\), we can eliminate denominators, and since \(ab = 1\) we do not need to change the last term. We can also replace \(a^2 - b^2\) by \(2\). We get \[a^2 x + 2a = -b^2 x + 2b,\] so \[(a^2 + b^2)x = 2(b-a).\]

We want to deal with \(a^2 + b^2\). We could try to write it in terms of \(b-a\), since that’s on the right-hand side.

We have \[a^2 + b^2 = (a - b)^2 + 2ab = (a-b)^2 + 2,\] so the above equation becomes \[[(a-b)^2 + 2]x = 2(b-a).\]

We can divide through by \(a-b\) (it cannot be zero because \(a^2 - b^2 = 2\)), and use \(a^2 - b^2 = 2\) to give \(\frac{2}{a-b} = a+b\), using the familiar difference of two squares.

Thus the equation becomes \[\left((a-b) + \frac{2}{a-b}\right) x = -2,\] that is, \[(a - b + a + b) x = -2.\] Now we can tidy up to get \[x = -\frac{1}{a} = -b,\] and using either of the equations of the tangents, say the first one, then gives \[y = \frac{b^2}{a} + 2b = \frac{b^2 + 2ab}{a} = \frac{b^2 + 2}{a} = a.\]

So \(M\) has coordinates \((-b,a)\), as required.

Then we see immediately that \(N\) has the coordinates \((b,-a)\).

Consider the two tangents through point

\(P\)

:

\[\begin{align*} y-b &= -\frac{b}{a}(x-a) \\ y-b &= \frac{a}{b}(x-a), \end{align*}\]

and note that \[-\frac{b}{a}\times\frac{a}{b}=-1.\] The tangent of \(C_2\) at \(P\) is therefore also the normal of \(C_1\) at \(P\). By an analogous argument around \(PMQN\) all intersecting straight lines meet at right angles.

All we then need to do is show that one of the side lengths is equal to any one of the others, and indeed we have \[\vert PM \vert = \sqrt{(a--b)^2+(b-a)^2}=\sqrt{2(a^2+b^2)}\] and \[\vert QN \vert = \sqrt{(-a-b)^2+(-b--a)^2}=\sqrt{2(a^2+b^2)}.\]

Thus \(PMQN\) is a square.
