---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r6710
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r6710
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6710
  old_site_id: Q120
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
      evidence: tangent and normal at the point P above the focus of an ellipse meeting the y-axis, with
        QR = HP - parametric differentiation on the standard parametrisation
      rationale: 'Canonical UGM title: What can we say if a point $P$ on an ellipse is directly above
        the focus?'
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

# What can we say if a point $P$ on an ellipse is directly above the focus?

## Question

The point \(S\) is a focus of the ellipse \(\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1\), and \(P\) is a point on the ellipse such that \(PS\) is perpendicular to the axis of \(x\). The tangent and normal to the ellipse at \(P\) meet the axis of \(y\) in \(Q\) and \(R\) respectively. If \(H\) is the other focus of the ellipse prove that \(QR=HP\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/mSqSVCQr/width/700/height/550/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/mSqSVCQr)

The lengths \(QR\) and \(HP\) are measured on the diagram.

As we vary \(a\) and \(b\), how do the two lengths compare? Can we now turn this into a proof?

What are the [foci](https://undergroundmathematics.org/glossary/focus-of-an-ellipse) of an ellipse? What are their coordinates on the \(x\)-axis (if the \(x\)-axis contains the [semi major axis](https://undergroundmathematics.org/glossary/semi-major-axis))?

Assume that the focus \(S\) is on the positive \(x\)-axis, without any loss of generality. Once we know the coordinates of \(S\), how can we find the coordinates of \(P\)? (Again, let this point be in the first quadrant.)

What is the gradient of the ellipse at an arbitrary point of the ellipse?

We now have \(P\) and a general form for the gradient. What are the equations of the normal and tangent to the curve at this point? What then are the two intercepts \(Q\) and \(R\)?

## Solution

Firstly, we can work out the coordinates of \(P\).

It is a standard property of ellipses that the distance from the centre

\(O\)

to either

focus

is

\(f=\sqrt{a^2-b^2}\)

(with the convention that

\(a>b\)

). Thus at points

\(S\)

and

\(P\)

we have

\(x=\sqrt{a^2-b^2}\)

. Thus the

\(y\)

-coordinate of

\(P\)

is

\[\begin{align*} \frac{y^2}{b^2} &= 1-\frac{a^2-b^2}{a^2} \\ &= \frac{b^2}{a^2}, \end{align*}\]

so \[y^2 = \frac{b^4}{a^2}\] and so \[y = \frac{b^2}{a},\] since we have picked \(P\) to be in the top right quadrant. Thus \(P\) has coordinates \(\left(\sqrt{a^2-b^2},\dfrac{b^2}{a}\right)\).

Now let’s work out the equation of the tangent to the ellipse at \(P\).

We differentiate the equation of the ellipse implicitly to find the gradient of the tangent at

\(P\)

: we have

\[\frac{2x}{a^2}+\frac{2y}{b^2}\frac{dy}{dx}=0,\]

and so

\[ \frac{dy}{dx} = -\frac{2x}{a^2}\times \frac{b^2}{2y} = -\frac{x}{y}\times\frac{b^2}{a^2}. \]

Thus at point

\(P\)

the derivative is

\[\begin{align*} \frac{dy}{dx} &= -\frac{\sqrt{a^2-b^2}}{b^2/a}\times\frac{b^2}{a^2} \\ &= -\frac{\sqrt{a^2-b^2}}{a}. \end{align*}\]

The equation of the tangent to the ellipse through \(P\) therefore has the equation \[y-\frac{b^2}{a}=-\frac{\sqrt{a^2-b^2}}{a}\left(x-\sqrt{a^2-b^2}\right).\]

We can use this equation to work out the coordinates of \(Q\).

When

\(x=0\)

we get point

\(Q\)

, where

\[\begin{align*} y &= \frac{b^2}{a}-\frac{\sqrt{a^2-b^2}}{a}\left(-\sqrt{a^2-b^2}\right)\\ &= \frac{b^2+(a^2-b^2)}{a}=a, \end{align*}\]

so \(Q\) has coordinates \((0,a)\). (Without loss of generality we are assuming \(a>b>0\).)

Now let’s work out the equation of the normal at \(P\) and the coordinates of \(R\).

Similarly, the equation of the normal at

\(P\)

is

\[y-\frac{b^2}{a}=\frac{a}{\sqrt{a^2-b^2}}\left(x-\sqrt{a^2-b^2}\right).\]

When

\(x=0\)

we get the point

\(R\)

, where

\[\begin{align*} y&=\frac{b^2}{a}+\frac{a}{\sqrt{a^2-b^2}}\left(-\sqrt{a^2-b^2}\right)\\ y&=\frac{b^2}{a}-a=\frac{b^2-a^2}{a}, \end{align*}\]

so \(R\) has coordinates \(\left(0,\dfrac{b^2-a^2}{a}\right)\).

Now we want to prove that \(QR = HP\).

The other focus of the ellipse, \(H\), has coordinates \(\left(-\sqrt{a^2-b^2},0\right)\).

Therefore we have

\[\begin{align*} HP &= \sqrt{(2\sqrt{a^2-b^2})^2+\left(\frac{b^2}{a}\right)^2} \\ &= \sqrt{4(a^2-b^2)+\frac{b^4}{a^2}}\\ &= \frac{1}{a}\sqrt{4a^4-4a^2b^2+b^4} \\ &= \frac{1}{a}\sqrt{(2a^2-b^2)^2}=\frac{2a^2-b^2}{a}. \end{align*}\]

Similarly, \[QR = a+\frac{a^2-b^2}{a}=\frac{2a^2-b^2}{a}\] since we know that \(Q\) is above the \(x\)-axis and \(R\) is below it (had we chosen the other focus as \(S\) this would be reversed.)

Thus \(QR = HP\) as required.

For an alternative solution using the geometry of the ellipse, look at [Solution 2](https://undergroundmathematics.org/chain-rule/r6710/solution-2).

## Solution 2

We’ve added points \(Q'\) and \(R'\), where \(Q'\) and \(R'\) are the points at which the tangent and normal intersect the \(x\) axis.

We’ll use the reflection property of the ellipse. This states that any light beam sent from one focus will always reflect back to the other focus.

In our diagram, this is equivalent to the statement that \(\angle HPQ = \angle Q'PS\).

Let this angle be \(\alpha\) and let \(\beta=90^\circ-\alpha\), so that any right-angled triangle for which one angle is either \(\alpha\) or \(\beta\) must have angles \(\alpha\), \(\beta\) and \(90^\circ\) (as they must sum to \(180^\circ\)).

We can now find most of the angles in the diagram.

We can see that \(\triangle QTP\) and \(\triangle PTR\) are both isosceles. This tells us that \(QT=TP\) and \(TP=TR\) and so \(QT=TP=TR\).

As the foci are equidistant from the minor axis, we know that the \(x\)-axis bisects \(HS\), and so must also bisect \(HP\).

Hence \(HT=TP\), which gives us that \(QR=QT+TR=2TP = HT+TP=HP\), as required.

What can we deduce about the quadrilateral \(PQHR\)?

As an extension, show that \(TS=TP\). What can we deduce about the polygon \(PQHRS\)?

Does this result still hold when \(P\) is any point on the ellipse?
