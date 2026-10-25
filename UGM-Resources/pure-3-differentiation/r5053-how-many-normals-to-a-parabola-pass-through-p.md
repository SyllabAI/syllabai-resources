---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5053
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5053
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5053
  old_site_id: Q26
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
      evidence: normal to the parabola y^2 = 4ax at (at^2, 2at) and the two-normals-through-P proof -
        implicit/parametric differentiation of the standard parabola with the fixed-point geometry
      rationale: 'Canonical UGM title: How many normals to a parabola pass through $P$?'
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

# How many normals to a parabola pass through $P$?

## Question

Find the equation of the normal to the parabola \(y^2=4ax\) at the point \((at^2,2at)\).

Prove that, if \(p^2>8\), two chords can be drawn through the point \((ap^2,2ap)\) which are normal to the parabola at their second points of intersection, and that the line joining these points of intersection meets the axis of the parabola in a fixed point, independent of \(p\).

## Suggestion

We need to find the gradient of the normal at this point. How could we find the gradient of the curve itself?

Can we find values of \(t\) such that \((ap^2,2ap)\) lies on the normal at \(T\)? Can we get a cubic equation for \(t\) in terms of \(p\)? Do we know any of its roots?

You might find the following applet helpful in visualising the normals to the curve.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/xryG3d7n/width/700/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/xryG3d7n)

As we vary \(p\) using the slider, the point \(P = (ap^2, 2ap)\) moves around the curve. All possible normals through \(P\) are shown, in green and purple.

## Solution

**Approach 1: differentiate with respect to the parameter \(t\).**

Differentiating with respect to \(t\), we see \(\dfrac{dy}{dx} = \dfrac{dy/dt}{dx/dt}= \dfrac{2a}{2at}= \dfrac{1}{t}\).

So the gradient of the normal at \(T\) is \(-t\).

The point \((at^2,2at)\) is on the line which gives us its equation as \(y = -tx +at^3+2at\).

**Approach 2: find \(y\) directly**

We have \(y=2\sqrt{ax}\) (taking the positive square root for the top half of the curve).

Now we can differentiate to find \(\dfrac{dy}{dx} = 2\cdot\dfrac{1}{2}(ax)^{-1/2}a= \sqrt{\dfrac{a}{x}}\), and at \(x=at^2\) (noting that \(t\) is positive), this gives us \(\dfrac{dy}{dx} = \dfrac{1}{t}\). As above, we conclude the normal has gradient \(-t\).

We get the same result for the bottom half of the curve.

**Approach 3: implicit differentiation**

Differentiating \(y^2=4ax\) with respect to \(x\) gives, using the chain rule, \[2y \dfrac{dy}{dx} = 4a\] and therefore the gradient at \((at^2,2at)\) is \(\dfrac{4a}{2y} = \dfrac{4a}{4at}=\dfrac{1}{t}\).

We seek points \(T = (at^2, 2at)\) where the normal at \(T\) passes through \(P = (ap^2, 2ap)\).

So we need \((ap^2,2ap)\) to lie on the line \(y = at^3+2at-xt\).

Substituting in these values of \((x,y)\) we obtain \[2ap = at^3 + 2at-ap^2t\] or (cancelling the \(a\)) \[t^3 + (2-p^2)t - 2p = 0.\]

We already know one solution: \(p=t\) (because the normal at the point given by \(p\) passes through the curve at this same point.)

So we can take out from this cubic a factor of \((p-t)\) to give \[t^2 + pt + 2 = 0.\]

A quadratic has two roots if and only if its discriminant is positive, or “\(b^2-4ac>0\)”, which here gives simply \(p^2-8>0\), as required.

Finally, we consider the line joining \(T_1=(at_1^2,2at_1)\) and \(T_2=(at_2^2,2at_2)\) on the parabola (where \(t_1\) and \(t_2\) denote the two roots of the quadratic).

We want to find where this intersects the axis of the parabola, the line \(y=0\).

The gradient of the line is given by ‘the difference in \(y\) coordinates divided by the difference in \(x\) coordinates’, which is \[\frac{2a(t_2-t_1)}{a(t_2^2-t_1^2)} = \frac{2}{t_1+t_2}.\]

Hence the equation of the line is \[y - 2at_1 = \frac{2}{t_1+t_2} (x - a t_1^2),\] and by setting \(y=0\) we find \[x = at_1^2 + \frac{1}{2} (t_1+t_2)(-2at_1) = -at_1t_2.\]

We can recall now that the product of the roots of the quadratic \(x^2 + ax + b = 0\) is given by \(b\), the constant term.

But in \(t^2+pt+2=0\) the constant term is simply \(2\), giving the \(x\)-intercept to be \(x = -2a\), which is indeed independent of \(p\).
