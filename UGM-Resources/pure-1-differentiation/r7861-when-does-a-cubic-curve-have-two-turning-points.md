---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r7861
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r7861
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7861
  old_site_id: Q211
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
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: cubic with two distinct turning points — the discriminant condition on f'=3x^2+2ax+b
        is the load-bearing argument
      rationale: 'Canonical UGM title: "When does a cubic curve have two turning points?"; exam provenance:
        Oxford University Mathematics Aptitude Test, 2012, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2012, Q3
task: T-UGM-IMPORT-7
---

# When does a cubic curve have two turning points?

## Question

Let \(f(x) = x^3 + ax^2 + bx + c\), where the coefficients \(a\), \(b\) and \(c\) are real numbers. The figure below shows a section of the graph of \(y=f(x)\). The curve has two distinct turning points; these are located at \(A\) and \(B\), as shown. (Note that the axes have been omitted deliberately.)

1. Find a condition on the coefficients \(a\), \(b\), \(c\) such that the curve has two distinct turning points if, and only if, this condition is satisfied.

*It may be assumed from now on that the condition on the coefficients in (i) is satisfied.*

1. Let \(x_1\) and \(x_2\) denote the \(x\) coordinates of \(A\) and \(B\), respectively. Show that \[x_2 - x_1 = \frac{2}{3} \sqrt{a^2 - 3b}.\]

---

1. Suppose now that the graph of \(y=f(x)\) is translated so that the turning point at \(A\) now lies at the origin. Let \(g(x)\) be the cubic function such that \(y=g(x)\) has the translated graph. Show that \[g(x) = x^2 \left(x - \sqrt{a^2 - 3b}\right).\]

---

1. Let \(R\) be the area of the region enclosed by the \(x\)-axis and the graph \(y=g(x)\). Show that if \(a\) and \(b\) are rational then \(R\) is also rational.

---

1. Is it possible for \(R\) to be a non-zero rational number when \(a\) and \(b\) are both irrational? Justify your answer.

## Solution

The curve has two distinct turning points if and only if the derivative, \(f'(x)\), has two distinct real roots.

Now

\[\begin{equation} f'(x) = 3x^2 +2ax + b,\label{eq:1} \end{equation}\]

which has two distinct real roots when the discriminant is greater than \(0\). That is, \[(2a)^2 - 4(3)(b) > 0,\] and hence \[a^2 - 3b > 0.\]

The coordinates of the turning points satisfy the quadratic \(\eqref{eq:1}\), so \[x = \frac{-2a \pm \sqrt{4a^2 - 12b}}{6} = \frac{-a \pm \sqrt{a^2 - 3b}}{3}.\] As \(x_1 < x_2\), we have \[x_1 = \frac{-a - \sqrt{a^2 - 3b}}{3}\quad\text{and}\quad x_2 = \frac{-a + \sqrt{a^2 - 3b}}{3}.\] (We know that both of these are real as \(a^2 - 3b > 0\).)

Therefore \[x_2 - x_1 = \frac{1}{3} \left(-a + \sqrt{a^2 - 3b} + a + \sqrt{a^2 - 3b} \right) = \frac{2}{3} \sqrt{a^2 - 3b}.\]

The translated graph now has a repeated root at the origin, and a third root at \(t\), say, where \(t>0\). Therefore the graph has equation of the form \[g(x) = x^2 (x-t) = x^3 - tx^2.\] Hence \[g'(x) = 3x^2 - 2tx = x(3x-2t),\] and so \(g(x)\) has turning points at \(x=0\) and \(x=\frac{2}{3}t\).

From part (ii), we have \[\frac{2}{3}t - 0 = \frac{2}{3} \sqrt{a^2 - 3b},\] and so \[t=\sqrt{a^2 - 3b}.\] This gives \[g(x) = x^2 \left(x-\sqrt{a^2 - 3b}\right).\]

Alternatively, we could use the result from part (ii) again. Our cubic \(g(x)=x^3-tx^2\) is just like the original cubic in the question, with \(a=-t\), \(b=0\) and \(c=0\).

Therefore the difference between the \(x\)-coordinates of the turning points for \(g(x)\) is \[\frac{2}{3}\sqrt{a^2-3b}=\frac{2}{3}\sqrt{t^2-0}=\frac{2}{3}t\] as \(t>0\). We can immediately deduce that \(t=\sqrt{a^2-3b}\), as in the first approach.

We use integration to determine

\(R\)

. As the region is below the

\(x\)

-axis, we take the negative of the integral, so we get

\[\begin{align*} R &{} = - \int_0^t g(x) \, dx \\ &{} = - \int_0^t (x^3 - tx^2) \, dx\\ &{} = - \left[ \frac{x^4}{4} - \frac{tx^3}{3} \right]_0^t \\ &{} = - t^4( \frac{1}{4}-\frac{1}{3}) \\ &{} = \frac{1}{12} t^4\\ &{} = \frac{1}{12} (a^2 - 3b)^2. \end{align*}\]

So if \(a\) and \(b\) are rational, then \(R\) must also be rational.

Yes, it is possible for \(R\) to be a non-zero rational number when \(a\) and \(b\) are both irrational.

For example, by choosing \(a = 2\sqrt{\sqrt{2}}\) and \(b = \sqrt{2}\), we have \(a^2-3b=\sqrt{2}\), and hence \(R=\dfrac{2}{12}= \dfrac{1}{6}\) which is rational.
