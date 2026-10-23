---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6405
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6405
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6405
  old_site_id: Q191
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: seven terms in AP; a,x_2,b in GP; then GP series with |r|<1 — express r via S_n, S_∞
        and prove S_{2n}=S_n(2S-S_n)/S
      rationale: 'Canonical UGM title: "What can we say if $a, x_1, x_2, x_3, x_4, x_5, b$ are in arithmetic
        progression?"; exam provenance: UCLES A level Mathematics B 1, 1984, Q1'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: seven terms in AP; a,x_2,b in GP; then GP series with |r|<1 — express r via S_n, S_∞
        and prove S_{2n}=S_n(2S-S_n)/S
      rationale: 'Canonical UGM title: "What can we say if $a, x_1, x_2, x_3, x_4, x_5, b$ are in arithmetic
        progression?"; exam provenance: UCLES A level Mathematics B 1, 1984, Q1'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics B 1, 1984, Q1
task: T-UGM-IMPORT-6
---

# What can we say if $a, x_1, x_2, x_3, x_4, x_5, b$ are in arithmetic progression?

## Question

1. The seven numbers \(a, x_1, x_2, x_3, x_4, x_5, b\) are in arithmetic progression. Express \(x_2\) in terms of \(a\) and \(b\), and show that \(x_1+x_3+x_5=\dfrac{3}{2}(a+b)\). Given also that the numbers \(a, x_2, b\) are in geometric progression, and that \(b\neq a\), express \(b\) in terms of \(a\).

---

1. A geometric series has common ratio \(r,\) where \(|r|<1.\) The sum of the first \(n\) terms of the series is \(S_n\) and the sum to infinity is \(S\). Express \(r\) in terms of \(S_n, S\) and \(n,\) and prove that the sum of the first \(2n\) terms of the series is \(\dfrac{S_n(2S-S_n)}{S}\).

## Suggestion

Can we work out \(d\), the common difference in the arithmetic progression?

## Solution

Let’s call the common difference of the arithmetic progression \(d\). This means that \[x_1=a+d,\ x_2=a+2d,\ \dots,\ b=a+6d.\] Thus \(b-a=6d\), and \(d=\dfrac{b-a}{6}\).

We can now substitute this value for \(d\) into the expression for \(x_2\), yielding \[x_2=a+2\Bigl(\frac{b-a}{6}\Bigr)=\frac{b+2a}{3}.\]

We’ll now rewrite

\(x_1+x_3+x_5\)

in terms of

\(a\)

and

\(d\)

, and then substitute

\(d=\dfrac{b-a}{6}\)

, giving

\[\begin{align*} x_1+x_3+x_5&=(a+d)+(a+3d)+(a+5d)\\ &= 3a+9d\\ &= 3a+9\Bigl(\frac{b-a}{6}\Bigr)\\ &= \frac{3a+3b}{2}\\ &= \frac{3}{2}(a+b), \end{align*}\]

as required.

For the final part, since \(a, x_2, b\) are in geometric progression, they have a common ratio \(r\), so \[x_2=ar\quad\text{and}\quad b=ar^2.\]

We wish to eliminate \(r\). We have \(x_2^2=a^2r^2\), which immediately implies that \(x_2^2=ab\).

We already know that

\(x_2=\dfrac{b+2a}{3}\)

, so putting the two different expressions for

\(x_2\)

together, we have

\[x_2^2=\left(\frac{b+2a}{3}\right)^2=ab.\]

Expanding the brackets and multiplying both sides by

\(9\)

gives

\[\begin{align*} &b^2+4ab+4a^2=9ab\\ \implies\quad&b^2-5ab+4a^2=0\\ \implies\quad&(b-a)(b-4a)=0, \end{align*}\]

so either \(b=a\) or \(b=4a\). Since \(b\neq a\), we must have \(b=4a\).

1. A geometric series has common ratio \(r\), where \(|r|<1\). The sum of the first \(n\) terms of the series is \(S_n\) and the sum to infinity is \(S\). Express \(r\) in terms of \(S_n,\) \(S\) and \(n,\) and prove that the sum of the first \(2n\) terms of the series is \(\dfrac{S_n(2S-S_n)}{S}\)

Let

\(a\)

be the first term of this geometric series with common ratio

\(r\)

. Then

\[S_n=\frac{a(1-r^n)}{1-r}\]

and

\[S=\frac{a}{1-r}.\]

To find an expression for

\(r\)

in terms of

\(S_n\)

,

\(S\)

and

\(n\)

, we must first eliminate

\(a\)

. We can rearrange the second expression to get

\[a=S(1-r),\]

which we can substitute into the first expression to get

\[S_n=\frac{S(1-r)(1-r^n)}{1-r}=S(1-r^n).\]

We want an expression for

\(r\)

, so we rearrange to get

\[\begin{align*} 1-r^n =& \frac{S_n}{S}\\ \implies r^n =& 1-\frac{S_n}{S}\\ \implies r =& \left(1-\frac{S_n}{S}\right)^{\frac{1}{n}}. \end{align*}\]

To find the sum of the first

\(2n\)

terms, we substitute

\(2n\)

into the formula for the sum of the first

\(n\)

terms, giving

\[S_{2n}=\frac{a(1-r^{2n})}{1-r}.\]

We now rewrite the equation using our expressions for

\(a\)

and

\(r^n\)

, giving

\[\begin{align*} S_{2n}&=S(1-r^{2n})\\ &=S\bigl(1-(r^n)^2\bigr)\\ &=S\left(1-\left(1-\frac{S_n}{S}\right)^2\right)\\ &=S\left(1-\left(1-\frac{2S_n}{S}+\frac{S_n^2}{S^2}\right)\right)\\ &=S\left(\frac{2S_n}{S}-\frac{S_n^2}{S^2}\right)\\ &=2S_n-\frac{S_n^2}{S}\\ &= \frac{S_n(2S-S_n)}{S}. \end{align*}\]
