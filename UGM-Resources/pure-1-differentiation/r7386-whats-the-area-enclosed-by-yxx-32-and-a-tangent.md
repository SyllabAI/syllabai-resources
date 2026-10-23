---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7386
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7386
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7386
  old_site_id: Q213
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: gradient zero at P(1,4) on y=x(x-3)^2 and the stationary-driven sketch — 1.7.2/1.7.4
        load-bearing; the tangent-revisit area carries a recorded 1.8 bearing
      rationale: 'Canonical UGM title: "What''s the area enclosed by $y=x(x-3)^2$ and a tangent?"; exam
        provenance: UCLES A level Mathematics 1, 1951, Q9'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: gradient zero at P(1,4) on y=x(x-3)^2 and the stationary-driven sketch — 1.7.2/1.7.4
        load-bearing; the tangent-revisit area carries a recorded 1.8 bearing
      rationale: 'Canonical UGM title: "What''s the area enclosed by $y=x(x-3)^2$ and a tangent?"; exam
        provenance: UCLES A level Mathematics 1, 1951, Q9'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1951, Q9
task: T-UGM-IMPORT-7
---

# What's the area enclosed by $y=x(x-3)^2$ and a tangent?

## Question

Show that the gradient of the curve \(y=x(x-3)^2\) is zero at the point \(P(1,4)\), and sketch the curve.

The tangent at \(P\) cuts the curve again at \(Q\). Calculate the area between the chord \(PQ\) and the curve.

## Suggestion

When curve sketching, good questions to ask include

- What are the stationary points?

- Where does the curve intercept the axes?

- Are there any asymptotes?

- How does the curve behave for large \(x\)?

What is the equation of the tangent?

How does this help us to find \(Q\)?

Can we see on our sketch the area we want to find? What techniques do we have for finding areas?

## Solution

Our plan is to differentiate to find the gradient of the curve. We begin by expanding

\(y=x(x-3)^2\)

, giving

\[y=x(x^2-6x+9)=x^3-6x^2+9x\]

so

\[\begin{align*} \frac{dy}{dx}&{}=3x^2-12x+9\\ &{}=3(x^2-4x+3)\\ &{}=3(x-3)(x-1). \end{align*}\]

If you know the product and chain rules, you could find the derivative using those instead.

\[\begin{align*} \frac{dy}{dx}&{}=(x-3)^2+2x(x-3) \\ &{}= (x-3)(x-3+2x) \\ &{}= 3(x-1)(x-3). \end{align*}\]

Thus \(\dfrac{dy}{dx}=0\) when \(x=1\) and when \(x=3\). At \(x=1\), \(y=4\); at \(x=3\), \(y=0\).

So the gradient of the curve is zero at \(P(1,4)\) and also at \((3,0)\).

To sketch the curve, we note that the roots occur at \(x=0\) and \(x=3\) (with the latter being a double root, and so the curve touches the \(x\)-axis here). The \(y\)-intercept is \(0\).

The equation is a cubic with \(x^3\) as the leading term. So as \(x \to\infty\), \(y\to\infty\), and as \(x\to-\infty\), \(y\to-\infty\).

So the stationary point at \(P(1,4)\) must be a maximum, and that at\((3,0)\) must be a minimum, giving

The tangent at \(P\) cuts the curve again at \(Q\). Calculate the areabetween the chord \(PQ\) and the curve.

The tangent at \(P\) has equation \(y=4\). This intersects the cubic again when \[4 = x(x-3)^2.\] We can expand this and rearrange to get \[x^3-6x^2+9x-4=0.\] We already know that \(x=1\) is a double root of this equation (as the line \(y=4\) touches the curve at \(x=1\)), so \((x-1)^2\) will be a factor. We can factorise to give \[(x-1)(x^2-5x+4)=0\] so \[(x-1)^2(x-4)=0.\]

We could have written this down immediately, since the factorisation must be \((x-1)^2(x-a)\) for some \(a\), which will expand to \(x^3+px^2+qx-a\) for some \(p\) and \(q\), and so \(a\) must be \(4\) to match the constant terms.

Thus the tangent at \(P\) intersects the curve again at \(Q(4,4)\). We can now calculate the required area, indicated by \(R\) on this sketch.

The area of

\(R\)

is equal to the area of the rectangle between

\(PQ\)

and the

\(x\)

-axis, which is

\(3\times4=12\)

, minus the area under the curve between

\(P\)

and

\(Q\)

, which is given by

\[\begin{align*} \int_1^4 x^3-6x^2+9x\,dx &{}= \left[\frac{x^4}{4}-2x^3+\frac{9x^2}{2}\right]_1^4 \\ &{}= (64-128+72)-\left(\frac{1}{4}-2+\frac{9}{2}\right) \\ &{}= 8-\frac{11}{4} = \frac{21}{4}. \end{align*}\]

Thus the area of \(R\) is \(12-\dfrac{21}{4}=\dfrac{27}{4}=6\dfrac{3}{4}\).
