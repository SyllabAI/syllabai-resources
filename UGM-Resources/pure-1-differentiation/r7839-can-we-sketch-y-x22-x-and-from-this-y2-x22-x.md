---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7839
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7839
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7839
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: sketch y=x^2(2-x) via dy/dx=-3x^2+4x stationary structure, then the y^2 symmetry extension
      rationale: 'Canonical UGM title: "Can we sketch $y = x^2(2-x)$, and from this, $y^2 = x^2(2-x)$?";
        exam provenance: UCLES A level Mathematics A 1, 1973, Q10'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: sketch y=x^2(2-x) via dy/dx=-3x^2+4x stationary structure, then the y^2 symmetry extension
      rationale: 'Canonical UGM title: "Can we sketch $y = x^2(2-x)$, and from this, $y^2 = x^2(2-x)$?";
        exam provenance: UCLES A level Mathematics A 1, 1973, Q10'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1, 1973, Q10
task: T-UGM-IMPORT-7
---

# Can we sketch $y = x^2(2-x)$, and from this, $y^2 = x^2(2-x)$?

## Question

Draw a sketch-graph of the curve whose equation is

\[\begin{equation*} y = x^2(2-x). \end{equation*}\]

Hence, or otherwise, draw a sketch-graph of the curve whose equation is

\[\begin{equation*} y^2 = x^2(2-x) \end{equation*}\]

indicating *briefly* how the form of the curve has been derived.

## Solution

The polynomial on the right-hand side has a double zero at the origin and a zero at \(x = 2\).

Further,

\[\begin{equation*} \frac{dy}{dx} = -3x^2 + 4x = x(4-3x) \end{equation*}\]

so the curve has two stationary points, at \(x = 0\) and \(x = \dfrac{4}{3}\).

Since the leading term of the polynomial is \(-x^3\), \(y \to \infty\) as \(x \to -\infty\), and \(y \to -\infty\) as \(x \to \infty\).

Consequently, the first stationary point must be a local minimum and the second stationary point must be a local maximum.

This information, when put together, leads to the following sketch.

Firstly, note that this curve does not exist where the right hand side is negative, that is when \(x>2\). This corresponds to where the curve in the first part of the question is below the \(x\)-axis.

For other values of \(x\), the curve has two branches, \(y=\pm x\sqrt{2-x}\).

The curve cuts or touches the \(x\)-axis at \(x=0\) and at \(x=2\).

So we have some kind of loop above and below the \(x\)-axis between \(x=0\) and \(x=2\), while for \(x<0\) the curve is in two branches, one increasing and the other decreasing.

In order to discover the nature of the axis crossings, we could think about how \(y=\sqrt{2-x}\) behaves and what happens when we multiply it by \(x\). Alternatively, we can do some calculus.

Differentiating implicitly

we find

\[\begin{align*} y^2 &=2x^2-x^3 \\ \implies\quad 2y\frac{dy}{dx} &= 4x-3x^2 \\ \iff\quad \frac{dy}{dx} &=\frac{4x-3x^2}{2y} \end{align*}\]

As \(x\) approaches \(2\), \(y\to 0\) and \(\frac{dy}{dx}\to\frac{8-12}{2y}\to\pm\infty\). So a tangent to the curve at \(x=2\) would be vertical.

We can’t evaluate \(\frac{dy}{dx}\) at the origin, but nearby \(x\) is very small so \(y^2\approx2x^2\). This means that \(y\approx\pm\sqrt{2}x\) and we have \[\frac{dy}{dx}\approx\frac{4x-3x^2}{\pm 2\sqrt{2}x} \approx \pm\sqrt{2}.\] Hence the curve passes through the origin with gradient \(\pm\sqrt{2}\).

The curve whose equation is \begin{equation*} y^2 = x^2(2-x) \end{equation*} has two parts, each the reflection of the other in the $x$-axis: \begin{equation*} y = \pm \sqrt{x^2(2-x)} \quad\text{where $x \le 2$.} \end{equation*} The restriction that $x \le 2$ is necessary, since $x^2(2-x) \ge 0$ if and only if $x \le 2$. We have a graph of the function $y = x^2(2-x)$, so we need to think how a graph is transformed by the map $y \mapsto \sqrt{y}$. The three points where $y = 1$ are invariant; both the old curve and the new curve go through all three points. The new curve will be ABOVE the old curve for $0

1$, since in this region, $y^2 > y$. But the map $x \mapsto \sqrt{x}$ is reasonably well-behaved; as $x$ increases, $\sqrt{x}$ increases, and as $x$ decreases, $\sqrt{x}$ decreases. In particular, the stationary points remain stationary points as, by the

, \begin{equation*} \frac{d}{dx} \left( \sqrt{f(x)} \right) = \frac{f'(x)}{2\sqrt{f(x)}} \end{equation*} when $f(x)$ is a function such that $f(x) > 0$.

We are led, then, to the following sketch.

*** Both curves are plotted together below.
