---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r8130
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r8130
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8130
  old_site_id: Q1052
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
  - code: 1.8.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "area between a cubic and the x-axis written as a difference of two definite integrals with the sign split at the interior root — area-as-signed-integrals is the tested 1.8.4 skill"
      rationale: "Canonical UGM title: \"What's the area between $f_k(x) = x(x-k)(x-2)$ and the $x$-axis?\""
      validation_status: SUGGESTED
    title: "use definite integration to find lines parallel to the axes, or between a curve and a line or between two curves: • the area of a region bounded by a curve and • a volume of revolution about one of the axes."
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# What's the area between $f_k(x) = x(x-k)(x-2)$ and the $x$-axis?

## Question

Let \(0< k <2\). Below is sketched a graph of \(y=f_k(x)\) where \(f_k(x) = x(x-k)(x-2)\). Let \(A(k)\) denote the area of the shaded region.

1. Without evaluating them, write down an expression for \(A(k)\) in terms of two integrals.

---

1. Explain why \(A(k)\) is a polynomial in \(k\) of degree \(4\) or less. [You are not required to calculate \(A(k)\) explicitly.]

---

1. Verify that \(f_k (1+t) = -f_{2-k}(1-t)\) for any \(t\).

---

1. How can the graph of \(y=f_k(x)\) be transformed to the graph of \(y = f_{2-k}(x)\)? Deduce that \(A(k)=A(2-k)\).

---

1. Explain why there are constants \(a, b, c\) such that \[A(k) = a(k-1)^4 + b(k-1)^2 + c.\] [You are not required to calculate \(a,b, c\) explicitly.]

## Suggestion

How is the value of an integral affected if a function gives negative values (is below the \(x\)-axis)?

What is the highest of power of \(k\) we can get by integrating \(f\), with the limits given?

What happens if we use part (iii), replacing \(1+t\) with \(x\)?

Can we compare \(f_{2-k}(x)\) to \(f_k (x)\)? What do the transformations from part iv) do to the area \(A(k)\)?

1. Explain why there are constants \(a, b, c\) such that \[A(k) = a(k-1)^4 + b(k-1)^2 + c.\] [You are not required to calculate \(a,b,c\) explicitly.]

Can we show \(A(1+k) = A(1-k)\)? What implications for symmetry does this have?

## Solution

We need to consider the two shaded regions separately, because one is above the \(x\)-axis (giving a positive area), and one is below the \(x\)-axis (giving a negative area), so we can’t just take the integral \(\displaystyle\int_0^2 \! f_k(x) \, \mathrm{d}x\).

Instead, we have

\[A(k) = \displaystyle\int_0^k \! f_k(x) \, \mathrm{d}x - \displaystyle\int_k^2 \! f_k(x) \, \mathrm{d}x,\]

as the negative sign in front of the second integral cancels out the negative sign of the area between \(x=k\) and \(x=2\).

Therefore,

\[A(k) = \displaystyle\int_0^k \! x(x-k)(x-2) \, \mathrm{d}x - \displaystyle\int_k^2 \! x(x-k)(x-2) \, \mathrm{d}x.\]

\(A(k)\) is certainly a polynomial in \(k\). Could it include a \(k^5\) term?

Only if you have an \(x^5\) term or a \(kx^4\) term after integrating, which means having an \(x^4\) term or a \(kx^3\) term before integrating.

Neither is possible, by looking at \(x(x-k)(x-2)\), and the same argument works for powers of \(k\) higher than \(5\).

Hence \(A(k)\) is a polynomial in \(k\) of degree at most \(4\).

Let’s start by thinking about what \(f_k(1+t)\) and \(f_{2-k}(1-t)\) are, given that \(f_{k}(x)=x(x-k)(x-2)\).

To find \(f_{k}(1+t)\), we need to substitute \(1+t\) for \(x\) in the formula for \(f_{k}(x).\) This gives us \[f_k(1+t) = (1+t)(1+t-k)(1+t-2).\]

To find \(f_{2-k}(1-t)\), we need to substitute \(1-t\) for \(x\), but we also need to substitute \(2-k\) for \(k.\) Therefore \[f_{2-k}(1-t) = (1-t)(1-t-(2-k))(1-t-2).\]

Now we can manipulate

\(-f_{2-k}(1-t)\)

to try to obtain

\(f_k(1+t).\)

\[\begin{align*} -f_{2-k}(1-t) \hspace{2mm} & =-(1-t)(1-t-(2-k))(1-t-2) \\ & = -(1-t)(-1-t+k)(-1-t) \\ & = (t-1)(1+t-k)(1+t) \quad \text{by taking a factor of $-1$ from each bracket} \\ & = (1+t)(1+t-k)(t-1) \quad \text{by rearranging the order of the brackets.} \\ \end{align*}\]

If we think about what we are aiming for, we can see that the first two brackets involve \(1+t\), which is a good sign. It would be helpful to rewrite the last bracket in a way that also involves \(1+t.\) We can write \(t-1\) as \(1+t-2\) which means that

\[\begin{align*} -f_{2-k}(1-t) \hspace{2mm} & =(1+t)(1+t-k)(1+t-2) \\ & = f_{k}(1+t) \quad \text{as required.}\\ \end{align*}\]

We started from the RHS because it looks messier and we wanted to get it to a simpler expression. We could have started with the LHS.

From part (iii), we have that

\[f_k(1+t) = -f_{2-k}(1-t).\]

If we substitute \(t\) with \(1-x\), the above equation becomes equivalent to

\[-f_k(2-x) =f_{2-k}(x).\]

Now, \(f_k(2-x)\) is the reflection of \(f_k(x)\) in the line \(x=1\).

A second transformation is now required because of the minus sign in front of \(f_{k}\). This is a reflection in the \(x\)-axis.

Together these transformations are the same as a rotation \(180^{\circ}\) around the point \((1,0)\).

In fact, combining two reflections always gives you a rotation about the point where the two mirror lines intersect.

As we can see in the sketch above, since we’re rotating \(180^\circ\) around a point on the x axis, the area between the graph and the \(x\)-axis remains the same for \(f_k\) and \(f_{2-k}\), i.e. \(A(k) = A(2-k)\).

Or else we could say that since both of the reflections preserve the shaded area, combining them does too.

We know that \(A(k) = A(2-k)\), so \(A(1-k) = A(2-(1-k)) = A(1+k)\), and so \(y = A(k)\) is symmetrical about the line \(k = 1\).

So if we translate \(y = A(k)\) by \(1\) to the left, then it is even, so if we express \(A(k)\) as powers of \((x-1)\), only even powers are possible.

Therefore we have \(A(k) = a(k-1)^4 + b(k-1)^2 + c\) for some constants \(a, b, c\).
