---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r9325
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r9325
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9325
  old_site_id: Q4023
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
      evidence: tangent to the ellipse at P meeting the y-axis at Q and the line x = a at T, with the
        chord A'P construction - parametric differentiation and the tangent equation
      rationale: 'Canonical UGM title: Where does this tangent to this ellipse meet $x=a$?'
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

# Where does this tangent to this ellipse meet $x=a$?

## Question

The point \(P\) in the first quadrant lies on the ellipse \(\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1\). The points \(A^{\prime} \ (-a, 0)\) and \(A \ (a, 0)\) are the extremities of the major axis of the ellipse, and \(O\) is the origin. The tangent to the ellipse at \(P\) meets the axis of \(y\) at \(Q\) and meets the line \(x = a\) at \(T\). The chord \(A^{\prime} P\) meets the axis of \(y\) at \(M\), and when produced meets the line \(x=a\) at \(R\).

Prove that

1. \(AT=TR\),

---

1. \(OQ^2 - MQ^2 = b^2\).

## Suggestion

How can we find the tangent to the ellipse? Be careful when you differentiate the equation of the ellipse!

Do not forget that we know that the point \(P\) lies on the ellipse.

## Solution

Let us denote the coordinates of \(P\) by \((p, q)\).

Since

\(P\)

is in the first quadrant we have

\(p, q > 0\)

, and since

\(P\)

lies on the ellipse we know that

\[\begin{equation} \frac{p^2}{a^2} + \frac{q^2}{b^2} = 1. \label{eq:ellipse-eqn-eval-at-P} \end{equation}\]

Let us first work out the equation for the tangent to the ellipse at

\(P\)

in the form

\(y = mx + c\)

.

Differentiating implicitly

we have

\[\frac{2x}{a^2} + \frac{2y}{b^2} \frac{dy}{dx} = 0\]

and hence

\(\dfrac{dy}{dx} = - \dfrac{x b^2}{y a^2}\)

. The value of

\(m\)

is the value of this derivative at the point

\((p, q)\)

, which is

\(m = - \dfrac{p b^2}{q a^2}\)

. We also know that the point

\(P\)

lies on the tangent and hence we have the condition

\[q = - \frac{p^2 b^2}{q a^2} + c\]

which is equivalent to

\[c = \frac{q^2 a^2 + p^2 b^2}{q a^2}.\]

Using

\(q^2 a^2 + p^2 b^2 = a^2 b^2\)

, which follows directly from the above equation

\(\eqref{eq:ellipse-eqn-eval-at-P}\)

, the tangent is described by

\[\begin{equation} y = - \frac{p b^2}{q a^2} x + \frac{b^2}{q}. \label{eq:equation-of-tangent-at-P} \end{equation}\]

Let us now work out the coordinates of the point \(T\) shown in the following picture.

We can get the \(y\)-coordinate by inserting \(x = a\) into the equation of the tangent at \(P\). We get \[y = - \frac{p b^2}{q a^2}a + \frac{b^2}{q} = \frac{a b^2 - p b^2}{q a}\] and hence \(T\) has the coordinates \(\left(a, \dfrac{a b^2 - p b^2}{q a}\right)\).

We will now calculate the coordinates of the point \(R\) drawn in the following picture.

We start off by computing the equation for the line

\(A^{\prime} P\)

. Since the coordinates of

\(P\)

are

\((p, q)\)

, the slope of the line is given by

\(\dfrac{q}{p + a}\)

and hence the line is of the form

\(y = \dfrac{q}{p + a} x + c\)

for the

\(y\)

-axis intercept

\(c\)

. Using that the point

\(A^{\prime}\)

lies on the line we get the condition

\(- \dfrac{q a}{p + a} + c = 0\)

and hence

\(c = \dfrac{q a}{p + a}\)

. Thus the line

\(A^{\prime} P\)

has the equation

\[\begin{equation} y = \frac{q}{p + a} x + \frac{q a}{p + a}. \label{eq:equation-Aprime-P} \end{equation}\]

Since the \(x\)-coordinate for \(R\) is \(a\) we can compute the \(y\)-coordinate via \[y = \frac{q a}{p + a} + \frac{q a}{p + a}.\] and hence the point \(R\) has the coordinates \(\left(a, 2\dfrac{q a}{p + a}\right)\).

Since the points

\(A\)

,

\(T\)

, and

\(R\)

all lie on the same vertical line

\(x = a\)

it suffices to show that

\(T\)

lies exactly in the middle of

\(A\)

and

\(R\)

, i.e. that the

\(y\)

-coordinate of

\(T\)

is half the

\(y\)

-coordinate of

\(R\)

. From equation

\(\eqref{eq:ellipse-eqn-eval-at-P}\)

we get

\(b^2 = \dfrac{q^2 a^2}{a^2 - p^2}\)

. Thus we have

\[\begin{align*} b^2 \frac{a - p}{q a} &= \dfrac{q^2 a^2}{a^2 - p^2} \frac{a - p}{q a} \\ &= \frac{qa(a-p)}{a^2 - p^2} \\ &= \frac{qa(a-p)}{(a+p)(a-p)} \\ &= \frac{qa}{a+p} \end{align*}\]

and hence \(AT = TR\).

Let us now compute the coordinates of the points \(Q\) and \(M\) shown in the following drawing.

The

\(y\)

-coordinate of

\(Q\)

is given by the

\(y\)

-axis intercept of the tangent to the ellipse at

\(P\)

. We have already found the intercept as part of equation

\(\eqref{eq:equation-of-tangent-at-P}\)

, so we already know that the point

\(Q\)

has the coordinates

\(\left(0, \dfrac{b^2}{q}\right)\)

. Similarly, the

\(y\)

-coordinate of

\(M\)

is just the

\(y\)

-axis intercept of the line

\(A^{\prime} P\)

, i.e. the line given by equation

\(\eqref{eq:equation-Aprime-P}\)

, and hence

\(M\)

is given by

\(\left(0, \dfrac{q a}{p + a}\right)\)

. Using this we get

\[\begin{align*} OQ^2 - MQ^2 &= \left( \frac{b^2}{q} \right) ^2 - \left( \frac{b^2}{q} - \frac{q a}{p + a} \right)^2 \\ &= \left( \frac{b^2(p + a)}{q (p + a)} \right)^2 - \left( \frac{b^2(p + a) - q^2 a}{q (p + a)} \right)^2 \\ &= \frac{2q^2 a b^2 (p + a) - q^4 a^2}{q^2 (p + a)^2} \\ &= \frac{2a b^2 (p + a) - q^2 a^2}{(p + a)^2} \end{align*}\]

Equation

\(\eqref{eq:ellipse-eqn-eval-at-P}\)

implies that

\(q^2 = b^2 \left(1 - \dfrac{p^2}{a^2}\right)\)

and using this for our calculation gives

\[\begin{align*} OQ^2 - MQ^2 &= \frac{2a b^2 (p + a) - b^2 \left(1 - \frac{p^2}{a^2}\right) a^2}{(p + a)^2} \\ &= b^2 \frac{2a (p + a) - a^2 + p^2}{(p + a)^2} \\ &= b^2 \frac{2ap + 2a^2 - a^2 + p^2}{(p + a)^2} \\ &= b^2 \underbrace{\frac{p^2 + 2p a + a^2}{(p + a)^2}}_{= 1}. \end{align*}\]

Thus \(OQ^2 - MQ^2 = b^2\).
