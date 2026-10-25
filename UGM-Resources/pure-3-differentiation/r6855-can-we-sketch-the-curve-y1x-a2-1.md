---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r6855
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r6855
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6855
  old_site_id: Q61
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
      evidence: stationary points of g(x) = 1/(((x-a)^2-1)((x-b)^2-1)) found by differentiating the product
        of reciprocal quadratics - the product/quotient-rule work is load-bearing for the three stationary
        abscissae
      rationale: 'Canonical UGM title: Can we sketch the curve $y=1/((x-a)^2-1)$?'
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

# Can we sketch the curve $y=1/((x-a)^2-1)$?

## Question

1. Sketch the curve \(y=f(x)\) where \[f(x)=\frac{1}{(x-a)^2-1} \qquad \qquad (x\neq a\pm 1),\] and \(a\) is a constant.

---

1. The function \(g(x)\) is defined by \[g(x)=\frac{1}{((x-a)^2-1)((x-b)^2-1)} \qquad \qquad (x\neq a\pm 1,\,x\neq b \pm 1),\] where \(a\) and \(b\) are constants, and \(b>a\). Sketch the curves \(y=g(x)\) in the two cases \(b>a+2\) and \(b=a+2\), finding the values of \(x\) at the stationary points.

## Suggestion

*These suggestions apply to both parts of this question.*

How can we determine the vertical asymptotes of a curve? The horizontal ones?

Can the curve cross an asymptote? Does the function change sign here or not?

Are there any roots to the equation \(f(x)=0\) or \(g(x)=0\)? In other words, what are the \(x\) intercepts? What are the \(y\)-intercepts?

How do the curves behave as \(x\rightarrow\infty\)?

These curves are each symmetrical about a line \(x=c\). What is this \(c\) in each case?

How can we find the stationary points of the curve?

In the second part of the question, how do the two different conditions \(b > a+2\) and \(b = a+2\) affect the asymptotes?

## Solution

Using the difference of two squares, \((x-a)^2 - 1 = ((x-a)-1)(x-a)+1) = (x-(a+1))(x-(a-1))\).

Thus \(f(x) = \dfrac{1}{(x-(a+1))(x-(a-1))}\), and we have the vertical asymptotes \(x = a-1\) and \(x = a+1\).

Near the asymptote \(x=a-1\) as \(x \rightarrow a-1\) from below \((x-a)^2 \rightarrow 0\) from above so \(f(x) \rightarrow \infty\), whereas above \(x=a-1, \: \: f(x) \rightarrow -\infty\).

Similarly near the asymptote \(x=a+1\) as \(x \rightarrow a+1\) from below \((x-a)^2 \rightarrow 0\) from below so \(f(x) \rightarrow -\infty\), whereas above \(x=a+1, \: \: f(x) \rightarrow \infty\).

As \(x \rightarrow \infty, \: \: f(x)\) is positive and tending to zero, and as \(x \rightarrow -\infty, \: \: f(x)\) is also positive and tending to zero.

We have the \(y\)-intercept when \(x=0\): \[f(0)=\frac{1}{a^2-1}.\]

There are no roots to the equation \(f(x)=0\), and we can see that the curve will be symmetrical about the line \(x=a\).

We can use the symmetry about \(x=a\) to find the maximum point of the central branch by evaluating the curve at \(x=a\) giving \(f(a)=-1\).

We could look for turning points by setting the first derivative equal to zero. To find the first derivative we will need to use [quotient rule](https://undergroundmathematics.org/glossary/quotient-rule): \[0=f'(x)=-\frac{2(x-a)}{((x-a)^2-1)^2}\] \[\iff \quad 2(x-a)=0.\] So the only stationary point is at \(x = a\), and \(f(a) = -1\).

We have \(g(x) = \dfrac{1}{(x-(a+1))(x-(a-1))(x-(b-1))(x-(b+1))}\), as before.

Thus we have the vertical asymptotes \(x = a-1, x = a+1, x = b-1\) and x = \(b+1\).

If \(b > a+2\), these will be distinct, with \(x = b-1\) and x = \(b+1\) being to the right of the first two.

As \(x \rightarrow \infty, \: \: f(x)\) is positive and tending to zero, and as \(x \rightarrow -\infty, \: \: f(x)\) is also positive and tending to zero.

The \(y\)-intercept is \[g(0)=\frac{1}{(a^2-1)(b^2-1)},\] and again there are no roots of \(g(x)=0\). This time, the curve will be symmetric about \(x=\frac{1}{2}(a+b)\).

Stationary points occur when

\(g'(x)=0\)

so

\[0=g'(x)=\frac{-2(x-a)}{((x-a)^2-1)^2((x-b)^2-1)}+\frac{-2(x-b)}{((x-a)^2-1)((x-b)^2-1)^2}\]

\[\begin{align*} \iff 0&= (x-a)[(x-b)^2-1]+(x-b)[(x-a)^2-1]\\ &=(x-a)^2(x-b)-(x-b)+(x-a)(x-b)^2-(x-a)\\ &=(x-a)(x-b)\left[(x-a)+(x-b)\right]-\left[(x-a)+(x-b)\right] \\ &=\left((x-a)(x-b)-1\right)(2x-a-b) \end{align*}\]

\[\iff [x^2-(a+b)x+(ab-1)](2x-a-b)=0.\]

The roots of this are therefore

\[\begin{align*} x&=\frac{1}{2}(a+b)\\ \text{and } x &= \frac{(a+b)\pm\sqrt{(a+b)^2-4(ab-1)}}{2}\\ &=\frac{(a+b)\pm\sqrt{a^2-2ab+b^2+4}}{2}\\ &=\frac{1}{2}(a+b)\pm\frac{1}{2}\sqrt{(a-b)^2+4}. \end{align*}\]

The discriminant of this is always positive so these two roots are found equally spaced either side of the first root \(x=\frac{1}{2}(a+b)\).

We can see that \[g\left(\frac{1}{2}(a+b)\right)=\frac{1}{\left(\frac{1}{4}(b-a)^2-1\right)\left(\frac{1}{4}(a-b)^2-1\right)}=\frac{1}{\left(\frac{1}{4}(b-a)^2-1\right)^2}>0.\]

When \(b>a+2\), we have \(b-1>a+1\) so there are four distinct asymptotes and the sketch is

Graph of \(y=g(x)\) in the case \(b>a+2\)

When \(b=a+2\), we have \(b-1=a+1\) so we lose the middle branch and the sketch is

Graph of \(y=g(x)\) in the case \(b=a+2\)
