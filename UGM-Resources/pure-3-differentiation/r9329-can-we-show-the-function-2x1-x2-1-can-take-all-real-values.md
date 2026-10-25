---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r9329
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r9329
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9329
  old_site_id: Q1082
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: f'(x) = -2(x^2+x+1)/(x^2-1)^2 by the quotient rule, always negative, with the inflection
        argued from the behaviour of f' between the asymptotes - the range part is the recorded discriminant
        method
      rationale: 'Canonical UGM title: Can we show the function $(2x+1)/(x^2-1)$ can take all real values?'
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

# Can we show the function $(2x+1)/(x^2-1)$ can take all real values?

## Question

Prove that, for real values of \(x\), the function \[\frac{2x+1}{x^2-1}\] can take all real values. Sketch the graph of the function, and prove that it has a point of inflection between \(x=-1\) and \(x=+1\).

## Suggestion

We want to show that as we travel from \(-\infty\) to \(\infty\) along the \(x\)-axis, \(f(x)\) at some point takes each real value.

Suppose that \(y=\dfrac{2x+1}{x^2-1}\). Given a \(y\), can we find an \(x\)?

Things to look out for when curve sketching:

- asymptotes;

- intercepts;

- stationary points and their nature;

- behaviour as \(x\rightarrow \pm \infty\).

What is the definition of a point of inflection?

## Solution

Let

\(y=\dfrac{2x+1}{x^{2}-1}\)

(

\(x \neq \pm 1\)

). Rearranging, we have that

\[yx^2-2x-(1+y)=0.\]

We can solve this quadratic for

\(x\)

to find that (if

\(y \neq 0\)

),

\[\begin{align*} x &= \frac{2\pm\sqrt{4+4y(y+1)}}{2y}\\ &= \frac{1 \pm \sqrt{y^2 + y + 1}}{y}\\ &=\frac{1 \pm \sqrt{\left(y+\frac{1}{2}\right)^2 + \frac{3}{4}}}{y}. \end{align*}\]

So for any value of \(y\neq 0\), this gives real values for \(x\), and so for these \(x\)-values, \[f(x)=\frac{2x+1}{x^2-1} = y.\]

If

\(y = 0\)

, then

\(x = -\dfrac{1}{2}\)

gives

\(f(x) = y\)

. So the function takes all real values.

There are vertical asymptotes at \(x=\pm 1\), and the curve behaves like \(y=\dfrac{2}{x}\) for large \(x\).

Also \(f(0)=-1\) and the only root for \(f(x) = 0\) is \(-\frac{1}{2}\).

We can find the gradient of the curve by using the

quotient rule

(

\(x \neq \pm 1\)

):

\[\begin{align*} f'(x) &= \frac{2(x^2-1)-(2x+1)(2x)}{(x^2-1)^2}\\ &= \frac{-2x^2-2x-2}{(x^2-1)^2}\\ &= \frac{-2(x^2+x+1)}{(x^2-1)^2}\\ &= \frac{-2\left(\left(x+\frac{1}{2}\right)^2+\frac{3}{4}\right)}{(x^2-1)^2},\\ \end{align*}\]

which is always negative.

A point of inflection on a curve occurs where the gradient function has a maximum or a minimum.

As a point moves around the curve, a point of inflection happens where the tangent at that point changes from being on one side of the curve to the other.

Informally, our curve must change from being concave upwards to concave downwards in between the two asymptotes \(x\pm1\), and so it has a point of inflection somewhere there.

To be sure of this, we note that \(f'(-0.5) = -\dfrac{24}{9}\), \(f'(0) = -2\), \(f'(0.5) = -\dfrac{56}{9}\), and that \(-\dfrac{24}{9} < -2 > -\dfrac{56}{9}\).

This means, if we imagine the graph of \(y=f'(x)\), a continuous function between \(-1\) and \(1\), that \(f'(x)\) must have a local maximum between \(-0.5\) and \(0.5\).
