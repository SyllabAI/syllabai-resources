---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r6549
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r6549
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6549
  old_site_id: Q2018
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: 'stationary points of y = cot x - 8 cos x: d(cot x)/dx derived by the quotient rule on
        cos x/sin x (the in-spec 3.4.2 route - resolves the lane-11 ''beyond the 3.4.1 list'' caveat of
        record), then -cosec^2 x + 8 sin x = 0 (flips the lane-11 non-overlap row of record routed ''P3
        3.4 Differentiation'')'
      rationale: 'Canonical UGM title: Where are the stationary points on $\cot x-8\cos x$?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Where are the stationary points on $\cot x-8\cos x$?

## Question

The equation of a curve is \[y = \cot x - 8 \cos x, \quad (0 < x < \pi).\] Find the coordinates of the points on the curve where \(\dfrac{dy}{dx} = 0\).

Sketch the curve.

## Suggestion

Should we include \(\dfrac{\pi}{2}\) in the domain of this function?

If we think of \(\cot x\) as \(\dfrac{1}{\tan x}\), then as \(\tan \dfrac{\pi}{2}\) is not defined, neither is \(\cot x\) at this value.

But what if we define \(\cot x=\dfrac{\cos x}{\sin x}\) instead?

As well as the stationary points, we should consider the \(x\)-intercepts and any asymptotes.

## Solution

Using \(\cot x=\dfrac{1}{\tan x}\) will give us problems at \(x=\dfrac{\pi}{2}\), so we’ll use the alternative, \[\cot x = \frac{\cos x}{\sin x}.\]

We can differentiate \(y\): \[\frac{dy}{dx} = \frac{d}{dx}(\cot x) + 8\sin x.\] What’s the derivative of \(\cot x\)? It’s \(-\cosec^2 x\).

Finding the derivative of \(\cot x\)

Let \(u = \cos x\) and \(v = \sin x\), so that \(\cot x=\dfrac{u}{v}\), allowing us to use the [quotient rule](https://undergroundmathematics.org/glossary/quotient-rule).

Noting that

\(\dfrac{du}{dx}=-\sin x\)

and

\(\dfrac{dv}{dx}=\cos x\)

, we find

\[\begin{align*} \frac{d}{dx}(\cot x) &= \frac{\sin x(-\sin x)-\cos x(\cos x)}{(\sin x)^2}\\ &= \frac{-(\sin^2 x + \cos^2 x)}{\sin^2 x}\\ &= \frac{-1}{\sin^2 x}\\ &= -\cosec^2 x. \end{align*}\]

So we have that \[\frac{dy}{dx} = -\cosec^2 x + 8\sin x.\]

Now

\[\begin{align*} -\cosec^2 x + 8\sin x &=0\\ \iff 8 \sin x &= \cosec^2 x\\ \iff (\sin x)^3 &= \dfrac{1}{8}\\ \iff \sin x &= \dfrac{1}{2}.\\ \end{align*}\]

We’re allowed to multiply both sides by \(\sin^2 x\) in the above, since \(\sin x\) is not zero for \(0 < x < \pi\).

Solutions for \(x\) in the given range are \(\dfrac{\pi}{6}\) and \(\pi - \dfrac{\pi}{6} = \dfrac{5\pi}{6}\).

We were asked, however, to find the *coordinates* of the stationary points. The first is \[\left( \frac{\pi}{6}, \frac{\cos \tfrac{\pi}{6}}{\sin \tfrac{\pi}{6}} - 8 \cos \frac{\pi}{6} \right) = \Biggl( \frac{\pi}{6}, \frac{\tfrac{\sqrt{3}}{2}}{\tfrac{1}{2}} - 8 \frac{\sqrt{3}}{2} \Biggr) = \left( \frac{\pi}{6}, -3\sqrt{3} \right)\] and the second is \[\left( \frac{5\pi}{6}, \frac{\cos \tfrac{5\pi}{6}}{\sin \tfrac{5\pi}{6}} - 8 \cos \frac{5\pi}{6} \right) = \Biggl( \frac{5\pi}{6}, \frac{-\tfrac{\sqrt{3}}{2}}{\tfrac{1}{2}} + 8 \frac{\sqrt{3}}{2} \Biggr) = \left( \frac{5\pi}{6}, 3\sqrt{3} \right).\]

Now we have the coordinates of the stationary points, we can think about the sketch. First we should think about what happens as \(x \to 0\) and \(x \to \pi\):

As \(x \to 0\), \(\dfrac{\cos x}{\sin x} \to + \infty\), and \(- 8 \cos x \to -8\), so \(y \to + \infty\)

As \(x \to \pi\), \(\dfrac{\cos x}{\sin x} \to - \infty\), and \(- 8 \cos x \to 8\), so \(y \to - \infty\)

So since there are only two stationary points, and we have their coordinates, there is really only one shape the curve can have. So we have the beginnings of our sketch:

Now all we need to do is find the points where the graph crosses the \(x\)-axis, in the range given. We can factorise \(y\) as

\[y = \cos x \left( \dfrac{1}{\sin x} - 8 \right),\]

so \(y = 0\) if and only if either \(\cos x = 0\) or \(\sin x = \dfrac{1}{8}\), which in turn happens only when \(x\) takes one of the three values

\[\dfrac{\pi}{2}, \quad \sin^{-1}{\tfrac{1}{8}}, \quad \pi - \sin^{-1}{\tfrac{1}{8}}\]

We can see \(\dfrac{\pi}{2}\) is in the middle of the range, and if we calculate \(\sin^{-1}{\tfrac{1}{8}}\) we can see that it is less than \(\dfrac{\pi}{6}\) which is where our first turning point occurs. So the first \(x\)-intercept does indeed occur where we thought it did, looking back at our preliminary sketch. And this in turn implies that \(\pi - \sin^{-1}{\tfrac{1}{8}} > \dfrac{5 \pi}{6}\)

So we can mark on our intercepts, and our sketch is done!

A sketch of our function.

Note that the curve has rotational symmetry around the point \(\left(\dfrac{\pi}{2}, 0\right)\). This is to be expected since both \(\cos x\) and \(\cot x\) have the same symmetry.
