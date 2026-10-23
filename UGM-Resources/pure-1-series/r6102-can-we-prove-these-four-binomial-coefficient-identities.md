---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6102
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6102
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6102
  old_site_id: Q4047
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: binomial-coefficient identities (ΣC=2^n, kΣ, ΣC/(k+1), k²Σ) proved by substituting x=1/x=-1-style
        values into (1+x)^n
      rationale: 'Canonical UGM title: "Can we prove these four binomial coefficient identities?"; exam
        provenance: UCLES STEP Mathematics I, 2010, Q5'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics I, 2010, Q5
task: T-UGM-IMPORT-6
---

# Can we prove these four binomial coefficient identities?

## Question

By considering the expansion of \((1+x)^n\) where \(n\) is a positive integer, or otherwise, show that:

1. \(\dbinom{n}{0}+\dbinom{n}{1}+\dbinom{n}{2}+\dotsb+\dbinom{n}{n}=2^n\);

---

1. \(\dbinom{n}{1}+2\dbinom{n}{2}+3\dbinom{n}{3}+\dotsb+n\dbinom{n}{n}=n2^{n-1}\);

---

1. \(\dbinom{n}{0}+\dfrac{1}{2}\dbinom{n}{1}+\dfrac{1}{3}\dbinom{n}{2}+\dotsb+\dfrac{1}{n+1}\dbinom{n}{n}=\dfrac{1}{n+1}(2^{n+1}-1)\);

---

1. \(\dbinom{n}{1}+2^2\dbinom{n}{2}+3^2\dbinom{n}{3}+\dotsb+n^2\dbinom{n}{n}=n(n+1)2^{n-2}\).

## Solution

By the binomial theorem, we know that we can write

\[\begin{equation} (1+x)^n=\sum_{k=0}^n \dbinom{n}{k}x^k=\dbinom{n}{0}+\dbinom{n}{1}x+\dotsb+\dbinom{n}{n}x^n. \label{eq:1} \end{equation}\]

To answer part (i), we put \(x=1\) into \(\eqref{eq:1}\), which tells us that \[2^n=\sum_{k=0}^n\dbinom{n}{k}.\]

By considering the expansion of \((1+x)^n\) where \(n\) is a positive integer, or otherwise, show that:

1. \(\dbinom{n}{1}+2\dbinom{n}{2}+3\dbinom{n}{3}+\dotsb+n\dbinom{n}{n}=n2^{n-1}\);

Let’s start by using the expansion. This time we want \[\sum_{k=1}^n k\dbinom{n}{k}.\]

We know that \(\dbinom{n}{k} = \dfrac{n!}{(n-k)!k!}\) so let’s try rearranging this expression to something more helpful.

We can rewrite \(\dfrac{n!}{(n-k)!k!}\) as \(\dfrac{n!}{k\times(n-k)!(k-1)!}=\dfrac{1}{k}\times \dfrac{n!}{(n-k)!(k-1)!}\).

This is helpful because we could substitute it for the binomial terms and then the \(k\) in the summation will cancel, but at the moment the rest isn’t very helpful, so let’s have another play!

Using the very common “trick” of adding and subtracting the same value we can rearrange \(\dfrac{n!}{(n-k)!(k-1)!}=\dfrac{n!}{((n-1)-(k-1))!(k-1)!}\) which is very helpful because the denominator now looks like it comes from a binomial coefficient, and we know we can just separate out the \(n\) in the numerator as we did before with \(k\) thus giving us \(\dbinom{n}{k}=\dfrac{n}{k}\times \dbinom{n-1}{k-1}\).

We can now rewrite \[\sum_{k=1}^n k\dbinom{n}{k} = \sum_{k=1}^n k \dfrac{n}{k}\dbinom{n-1}{k-1}=\sum_{k=1}^n n\dbinom{n-1}{k-1}=n\sum_{k=1}^n \dbinom{n-1}{k-1}.\]

Comparing to part (i) \[\sum_{k=0}^n\dbinom{n}{k}=2^n\] we note that we want \(k\) to run through from \(1\) to \(n\) which means \(k-1\) runs from \(0\) to \(n-1\) so we can use the result from (i) if we change the summation to finish at \(n-1\)

Note that we know \(n \ge 1\) and this time \(k\) runs from \(1\) to \(n\) so \(n-1\) and \(k-1\) do not cause any issues.

\[n\sum_{k=1}^n \dbinom{n-1}{k-1}=n\sum_{k=0}^{n-1}\dbinom{n-1}{k}=n2^{(n-1)}\]

Let’s continue to work through using manipulations of the binomial coefficients.

This time we note that we are asked for

\[\begin{equation}\sum_{k=0}^n \dfrac{1}{k+1} \dbinom{n}{k}. \label{eq:2} \end{equation}\]

We would like to pull out a factor of \(k+1\) to cancel in \(\eqref{eq:2}\). So we write \[\frac{n!}{(n-k)!k!}=(k+1)\frac{n!}{(n-k)!(k+1)!},\] and to make this of the right form, we write \[(k+1)\frac{n!}{(n-k)!(k+1)!}=\frac{k+1}{n+1}\frac{(n+1)!}{(n-k)!(k+1)!}=\frac{k+1}{n+1}{n+1\choose k+1}.\] Using this in \(\eqref{eq:2}\), we have \[\sum_{k=0}^n\frac{1}{k+1}\dbinom{n}{k}=\sum_{k=0}^n\frac{1}{n+1}{n+1\choose k+1}=\frac{1}{n+1}\sum_{k=1}^{n+1}{n+1\choose k}.\] This is really close to being able to apply part (i), but \(k\) starts at \(1\) in the sum rather than \(0\). Since \({n+1\choose 0}=1\), we run the sum from \(0\) but compensate by subtracting \(1\), that is, \[\frac{1}{n+1}\sum_{k=1}^{n+1}{n+1\choose k}=\frac{1}{n+1}\left(\sum_{k=0}^{n+1}{n+1\choose k}-1\right).\] So we can now apply (i), and we find that \[\sum_{k=0}^n\frac{1}{k+1}\dbinom{n}{k}=\frac{1}{n+1}(2^{n+1}-1),\] as required.

We can straight away apply that \(\dbinom{n}{k}=\dfrac{n}{k}\dbinom{n-1}{k-1}\), as we deduced in part (ii), to find that \[\sum_{k=1}^nk^2\dbinom{n}{k}=\sum_{k=1}^n nk\dbinom{n-1}{k-1}=n\sum_{k=0}^{n-1} (k+1)\dbinom{n-1}{k}.\] We are really close to being able to apply (ii) again, but we have \(k+1\) and not \(k\) as the coefficient of \(\binom{n-1}{k}\). However, we can write \[n\sum_{k=0}^{n-1}(k+1){n-1\choose k}=n\sum_{k=0}^{n-1}\left(k{n-1\choose k}+{n-1\choose k}\right).\] Now the first term we can find from part (ii) (\(k\) runs from zero rather than one, but the first term is zero anyway), and moreover we can find the second term by part (i). Therefore, we have that \[\sum_{k=1}^nk^2\dbinom{n}{k}=n((n-1)2^{n-2}+2^{n-1})=n2^{n-2}(n-1+2)=n(n+1)2^{n-2},\] as required.

Alternative calculus solutions

What happens if we simply [differentiate](https://undergroundmathematics.org/glossary/differentiate) \(\eqref{eq:1}\) with respect to \(x\), and then put \(x = 1\)?

The right-hand side becomes exactly as desired, and the left-hand side is \(n(1+x)^{n-1}\) evaluated at \(x = 1\), which is indeed \(n2^{n-1}\).

Taking our cue from part (ii), we can integrate both sides of \(\eqref{eq:1}\) now. The sensible limits are 0 and 1.

So we have \[\int_0^1(1+x)^n \:dx = \left[x\dbinom{n}{0}+\dfrac{1}{2}\dbinom{n}{1}x^2+\dotsb+\dfrac{1}{n+1}\dbinom{n}{n}x^{n+1}\right]_0^1.\]

The left hand side is \[\left[\dfrac{(1+x)^{n+1}}{n+1}\right]_0^1 = \left(\dfrac{2^{n+1}}{n+1}\right)-\left(\dfrac{1}{n+1}\right) = \dfrac{2^{n+1}-1}{n+1},\]

while the right hand side is also exactly what we need.

Our plan this time is to

1. start with equation \(\eqref{eq:1}\),

---

1. differentiate once,

---

1. multiply by \(x\), and then

---

1. differentiate a second time.

Now if we put \(x = 1\), as before, this should prove our identity.

So we have

\[\begin{align*} (1+x)^n&=\dbinom{n}{0}+\dbinom{n}{1}x+\dotsb+\dbinom{n}{n}x^n \\ \implies n(1+x)^{n-1} &= \dbinom{n}{1}+2x\dbinom{n}{2}+3x^2\dbinom{n}{3} + \dotsb+nx^{n-1}\dbinom{n}{n} \\ \implies nx(1+x)^{n-1} &= x\dbinom{n}{1}+2x^2\dbinom{n}{2}+3x^3\dbinom{n}{3} + \dotsb+nx^{n}\dbinom{n}{n} \\ \implies \dfrac{d}{dx}\left(nx(1+x)^{n-1}\right) &= \dbinom{n}{1}+2^2x\dbinom{n}{2}+3^2x^2\dbinom{n}{3} + \dotsb+n^2x^{n-1}\dbinom{n}{n}. \end{align*}\]

Using the [product rule](https://undergroundmathematics.org/glossary/product-rule) on the LHS, we have

\[\dfrac{d}{dx}\left(nx(1+x)^{n-1}\right) = n(1+x)^{n-1}+nx(n-1)(1+x)^{n-2},\]

which is, when we evaluate at \(x = 1, \, n(n+1)2^{n-2}\,\) as desired.

The RHS is also exactly what we want when evaluated at \(x = 1\), and so the given identity for part (iv) is true.
