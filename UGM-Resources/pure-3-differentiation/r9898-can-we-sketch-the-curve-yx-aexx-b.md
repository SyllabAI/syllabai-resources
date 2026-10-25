---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9898
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9898
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9898
  old_site_id: Q1001
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
      evidence: stationary points of y = ((x-a)/(x-b)) e^x by the product and quotient rules giving the
        (a-b) < 0 or (a-b) > 4 condition, then the two case sketches (flips the lane-10 non-overlap row
        of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we sketch the curve $y=(x-a)e^x/(x-b)$?'
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

# Can we sketch the curve $y=(x-a)e^x/(x-b)$?

## Question

The curve \(y=\left(\dfrac{x-a}{x-b}\right)e^x,\) where \(a\) and \(b\) are constants, has two stationary points. Show that \[a-b<0 \quad \text{ or } \quad a-b>4.\]

1. Show that, in the case \(a=0\) and \(b=\dfrac{1}{2}\), there is one stationary point on either side of the curve’s vertical asymptote, and sketch the curve.

---

1. Sketch the curve in the case \(a=\dfrac{9}{2}\) and \(b=0\).

## Solution

Let’s find the stationary points of \[y=\left(\frac{x-a}{x-b}\right)e^x.\]

We plan to differentiate using the product rule here, so it helps us to find the derivative of \(\dfrac{x-a}{x-b}\) first.

If \(z = \dfrac{x-a}{x-b}\), then by the quotient rule, \(z' = \dfrac{a-b}{(x-b)^2}\). Returning to our original problem, we have \(y'=0\) when \[\frac{dy}{dx}=\left(\frac{x-a}{x-b}\right)e^x+\left[\dfrac{a-b}{(x-b)^2}\right]e^x=0\] \[\implies \frac{e^x(x^2-(a+b)x+(a+ab-b))}{(x-b)^2}=0.\]

We know that \(e^x > 0\) for any \(x\), so we need \(x^2-(a+b)x+(a+ab-b)=0.\)

This has two solutions as long as the discriminant is positive, which happens if and only if \((a+b)^2 -4(a+ab-b) > 0.\)

Multiplying out and rearranging here gives \[(a-b)(a-b-4)>0,\] which holds when \[a-b<0 \quad \text{ or } \quad a-b>4.\]

The vertical asymptote to the curve is at

\(x=\dfrac{1}{2}\)

. Now let’s substitute in the values of

\(a\)

and

\(b\)

to find the stationary points:

\[x^2-(a+b)x+ab-b+a=x^2-\frac{1}{2}x-\frac{1}{2}=0.\]

Solving this, we find that

\[\begin{align*} &x^2-\frac{1}{2}x-\frac{1}{2}=0 \\ &\implies 2x^2-x-1=0\\ &\implies (2x+1)(x-1)=0\\ &\implies x = 1, -\dfrac{1}{2}, &\end{align*}\]

which lie on either side of the asymptote \(x=\dfrac{1}{2}\).

We can now sketch the graph. We know two stationary points, \(\left(-\dfrac{1}{2},\dfrac{e^{-1/2}}{2}\right)\) and \((1,2e)\), and by inspection we can see that it also passes through \((0,0)\).

We also have that \(y\to\infty\) as \(x\to+\infty\), and \(y\to 0\) as \(x\to -\infty\).

Also, as \(x\to \dfrac{1}{2}\) from the right, \(y\to+\infty\) and as \(x \to \dfrac{1}{2}\) from the left \(y \to -\infty\).

We may now give an approximate sketch of the graph.

Note that the curve is close to \(y = e^x\) when \(\vert x \vert\) is large.

We again find the stationary points of the curve, this time solving

\[\begin{align*} &x^2-\frac{9}{2}x+\frac{9}{2}=0 \\ &\implies 2x^2-9x+9=0\\ &\implies (2x-3)(x-3)=0\\ &\implies x = 3, \dfrac{3}{2}. \end{align*}\]

So our two stationary points are \(\left(\frac{3}{2},-2e^{3/2}\right)\) and \(\left(3,-2e^3\right)\).

The vertical asymptote is at \(x=0\). As \(x\to 0\) from the right, we have that \(y\to-\infty\), since in this case \(x-\tfrac{9}{2} < 0\) and the denominator \(x\) is positive, so \(y\) is negative. As \(x\to 0\) from the left, we have \(y\to +\infty\) as \(x-\tfrac{9}{2} < 0\) again, but this time the denominator \(x\) is negative.

The graph crosses the \(x\)-axis once, at \(x=\dfrac{9}{2}\), and as \(x \to +\infty\), \(y \to +\infty\) and as \(x \to -\infty\), \(y\to 0\).

GeoGebra applet

This applet shows the curve for different values of \(a\) and \(b\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/gVxEqSMt/width/627/height/432/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/gVxEqSMt)
