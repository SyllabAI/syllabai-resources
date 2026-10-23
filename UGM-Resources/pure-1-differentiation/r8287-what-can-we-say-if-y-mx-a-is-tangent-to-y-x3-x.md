---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r8287
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r8287
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8287
  old_site_id: Q253
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
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: line y=m(x-a) tangent to y=x^3-x — the derivative supplies the tangency gradient with
        a double-root condition
      rationale: 'Canonical UGM title: "What can we say if $y = m(x-a)$ is tangent to $y = x^3 - x$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2011, Q3'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q3
task: T-UGM-IMPORT-7
---

# What can we say if $y = m(x-a)$ is tangent to $y = x^3 - x$?

## Question

The graphs of \(y = x^3 - x\) and \(y = m(x-a)\) are drawn on the axes below. Here \(m>0\) and \(a \le -1\).

The line \(y=m(x-a)\) meets the \(x\)-axis at \(A = (a,0)\), *touches* the cubic \(y=x^3 -x\) at \(B\) and intersects again with the cubic at \(C\). The \(x\)-coordinates of \(B\) and \(C\) are respectively \(b\) and \(c\).

1. Use the fact that the line and cubic *touch* when \(x=b\), to show that \(m=3b^2-1\).

---

1. Show further that \[a = \frac{2b^3}{3b^2 - 1}.\]

---

1. If \(a=-10^6\), what is the approximate value of \(b\)?

---

1. Using the fact that \[x^3 - x - m(x-a) = (x-b)^2 (x-c)\] (which you need not prove), show that \(c=-2b\).

---

1. \(R\) is the finite region bounded above by the line \(y=m(x-a)\) and bounded below by the cubic \(y = x^3 - x\). For what value of \(a\) is the area of \(R\) largest? Show that the largest possible area of \(R\) is \(\dfrac{27}{4}\).

## Suggestion

What do we know about curves and lines which touch at some point? How can that help us to answer this question?

Can we find \(m\) simply in terms of \(a\) and \(b\)? Could we drop a vertical from \(B\)?

Can you sketch a graph to show this situation?

Why is this true? For which values of x is this true? So this tells us that …

How does the area of \(R\) change as \(a\) changes?

Or… can we find a formula for the area? When we’ve done so, how can we maximise this?

## Solution

For the line and the cubic to touch at \(x=b\), the gradients must be equal at this point.

The gradient of the cubic is given by \[\frac{dy}{dx} = 3x^2 - 1,\] and the gradient of the line is \(m\).

Therefore, equating these expressions at \(x=b\) gives \[m = 3b^2 - 1.\]

The value of \(y\) must be the same for each graph at \(x=b\). Hence we have \[b^3 - b = m(b-a).\]

Now from part (i) we know that \(m=3b^2 - 1\), so substituting this into the above expression gives \[b^3 - b = (3b^2 - 1)(b-a).\]

We can rearrange this to get

\(a\)

by dividing by

\(3b^2-1\)

to give

\[b-a=\frac{b^3 - b}{3b^2 - 1}\]

and then finding

\[\begin{align*} a &{}= b - \frac{b^3 - b}{3b^2 - 1}\\ &{}= \frac{b(3b^2-1) -(b^3 - b)}{3b^2 -1}\\ &{}= \frac{2b^3}{3b^2 - 1}. \end{align*}\]

If \(a\) is large and negative, the line \(y=m(x-a)\) (which is still a tangent to the curve somewhere between \(-1\) and \(0\)) will be almost horizontal.

So the point \(B\) will lie almost at the maximum point of the curve, which is where \(3x^2-1=0\), so \(b\approx-\dfrac{1}{\sqrt{3}}\).

Another way of thinking about this is that the fraction in (ii) must be very large and negative.

For this, either \(b\) must be very large and negative, or the denominator must be very close to zero.

But \(b\) lies between \(-1\) and \(0\), so it must be the latter, and \(3b^2-1\approx0\), giving \(b \approx - \dfrac{1}{\sqrt{3}}\) (taking the negative square root).

We can put both sides in a polynomial form, so that we can see the coefficients of \(x^3\), \(x^2\) etc. on each side. Doing this gives \[x^3-(m+1)x +ma = x^3 -(2b + c)x^2 +(b^2 + 2bc)x -b^2 c.\]

Since the statement is true for all \(x\), it must be true that the coefficient of any power of \(x\) must be the same on both sides.

In particular the coefficient of \(x^2\) on the left side, \(0\), must be equal to the coefficient on the right side, \(-(2b + c)\). Therefore \(2b+c=0\), and hence \(c=-2b\).

If \(a\) increases (getting closer to \(-1\)), then \(b\) decreases and the line \(y=m(x-a)\) rises, making the area of \(R\) larger.

Therefore we want to choose the largest possible value of \(a\) in order to make the area the largest. So as \(a \le -1\), the area of \(R\) is largest when \(a=-1\).

And when \(a=-1\), the line \(y=m(x-a)\) must be tangent to the curve at the point \((-1,0)\) since this is a point on both the line and the curve for this value of \(a\).

So \(B\) coincides with \(A\) and \(b=-1\).

We can also deduce this algebraically using the earlier results, as follows. By part (ii), we see that \[-1 = \frac{2b^3}{3b^2 - 1}.\]

Rearranging this gives \(2b^3 + 3b^2 - 1 = 0\), which can be factorised as \((b+1)^2 (2b-1) = 0\). Since \(b\) can’t be positive, we conclude that \(b=-1\).

Then using part (iv), we obtain \(c=2\), and from part (i), we see that \(m=3b^2 - 1 = 2\).

So we can now calculate

\[\begin{align*} \text{Area of $R$} &{}= \int_b^c (m(x+1) - (x^3 - x)) \, dx \\ &{}= \int_{-1}^2 -x^3 + 3x + 2 \, dx \\ &{}= \left[ -\frac{x^4}{4} + \frac{3x^2}{2} + 2x \right]_{-1}^2 \\ &{}= 6-\left(-\frac{3}{4}\right)\\ &{}= \frac{27}{4}. \end{align*}\]
