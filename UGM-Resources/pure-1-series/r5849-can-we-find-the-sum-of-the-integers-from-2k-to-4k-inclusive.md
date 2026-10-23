---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r5849
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r5849
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5849
  old_site_id: Q94
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
      evidence: sums over 2k..4k; prove the GP sum formula a(1-r^n)/(1-r); recurring decimal 0.075075...
        as an infinite GP — AP sum + GP sum + sum to infinity
      rationale: 'Canonical UGM title: "Can we find the sum of the integers from $2k$ to $4k$ inclusive?";
        exam provenance: UCLES A level Mathematics A 1, 1981, Q3'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: sums over 2k..4k; prove the GP sum formula a(1-r^n)/(1-r); recurring decimal 0.075075...
        as an infinite GP — AP sum + GP sum + sum to infinity
      rationale: 'Canonical UGM title: "Can we find the sum of the integers from $2k$ to $4k$ inclusive?";
        exam provenance: UCLES A level Mathematics A 1, 1981, Q3'
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
  exam_reference: UCLES A level Mathematics A 1, 1981, Q3
task: T-UGM-IMPORT-6
---

# Can we find the sum of the integers from $2k$ to $4k$ inclusive?

## Question

1. The positive integer \(k\) is given.  Find, in terms of \(k\), an expression for \(S_1\), the sum of the integers from \(2k\) to \(4k\) inclusive. Find, in terms of \(k\), an expression for \(S_2\), the sum of the *odd* integers lying between \(2k\) and \(4k\). Show that \(\dfrac{S_1}{S_2} = 2+\dfrac{1}{k}\).

---

1. Prove that the sum of the first \(n\) terms of the geometric progression having first term \(a\) and common ratio \(r\) (\(r \neq 1\)) is \[a \left( \frac{1-r^n}{1-r} \right).\] By regarding the recurring decimal \(0.\dot{0}7\dot{5}\) (\(=0.075075\dotsc\), where the figures \(075\) repeat) as an infinite geometric progression, or otherwise, obtain the value of the decimal as a fraction in its lowest terms.

## Suggestion

Is there a convenient way of dividing up these sums into smaller sums that are easier to deal with?

Can we use the fact that the \(k\)th term in this geometric progression has the form \(a\times r^{k-1}\)?

If we call the sum of the first n terms \(T_n\), do you notice anything about the terms in \(r\times T_n\)?

What’s the first term of the geometric progression? What’s the common ratio?

## Solution

**Approach 1**

We could add together the integers

\(2k\)

,

\(2k+1\)

,

\(\dotsc\)

,

\(4k\)

excluding

\(3k\)

in pairs as follows:

\[\begin{align*} 2k+4k &= 6k \\ (2k+1)+(4k-1) &= 6k \\ \vdots \quad & \\ (3k-1)+(3k+1) &= 6k. \end{align*}\]

And there are \(k\) of these pairs in total.

So to add the numbers between \(2k\) and \(4k\) inclusive, we can add \(k\) pairs that add to \(6k\), together with \(3k\), that is, \[S_1=6k^2+3k.\]

**Approach 2**

We could use the fact that the sum of the integers from \(1\) to \(n\) is \(P_n=\dfrac{n(n+1)}{2}\).

So we want to find \(P_{4k}-P_{2k-1}\).

We have

\[\begin{align*} S_1 &= P_{4k}-P_{2k-1} \\ &=\frac{1}{2} (4k)(4k+1) - \frac{1}{2} (2k-1)(2k)\\ &=6k^2+3k. \end{align*}\]

The idea behind the first approach above can be used again for (a)(ii).

**Approach 1**

If

\(k\)

is even, we can add the odd integers between

\(2k\)

and

\(4k\)

in

\(k/2\)

pairs that add to

\(6k\)

:

\[\begin{align*} (2k+1)+(4k-1) &= 6k \\ (2k+3)+(4k-3) &= 6k \\ \vdots \quad & \\ (3k-1)+(3k+1) &= 6k. \end{align*}\]

So

\[\begin{align*} S_2 &= 6k\times\frac{k}{2}\\ &=3k^2. \end{align*}\]

We can use exactly the same approach if \(k\) is odd, only this time the odd integers between \(2k\) and \(4k\) consist of \((k-1)/2\) pairs that add to \(6k\), together with \(3k=6k/2.\)

So once again \[S_2=3k^2.\]

**Approach 2**

We need \((2k+1) + (2k+3) + \cdots + (4k-1)\), or \((2k+1) + (2k+3) + \cdots + (2k+(2k-1))\).

This is an arithmetic sequence with \(k\) terms, so for the formula, \(n = k\), \(d = 2\) and \(a = 2k+1\).

The sum is therefore \(\dfrac{n}{2}(2a+(n-1)d) = \dfrac{k}{2}(4k+2+2(k-1)) = k(3k ) =3k^2\).

We have

\[\begin{align*} \frac{S_1}{S_2} &= \frac{6k^2+3k}{3k^2}\\ &=2+\frac{1}{k}. \end{align*}\]

The sum of the first \(n\) terms of a geometric progression is \[T_n=a+ar+ar^2+\cdots+ar^{n-1}.\]

Now notice that \[r\times T_n = ar+ar^2+\cdots+ar^{n-1}+ar^n.\]

Subtracting, most of the terms cancel out so that

\[\begin{align*} (1-r)T_n &= a-ar^n\\ \implies\quad T_n &= \frac{a(1-r^n)}{(1-r)}. \end{align*}\]

By regarding the recurring decimal \(0.\dot{0}7\dot{5}\) (\(=0.075075\ldots\), where the figures \(075\) repeat) as an infinite geometric progression, or otherwise, obtain the value of the decimal as a fraction in its lowest terms.

Now \(0.075075\ldots\) can be written as the sum of a geometric progression with first term \(0.075\) and common ratio \(0.001\).

Using the expression above for the sum of the first \(n\) terms, and taking the limit as \(n\to \infty\), we have \[T_n\to a \left( \frac{1}{1-r} \right)\] (since \(|r|<1\), and \(r^n \to 0\) as \(n\to\infty\)).

Substituting in our values of \(a\) and \(r\) gives \[0.\dot{0}7\dot{5}=\frac{0.075}{1-0.001}=\frac{0.075}{0.999}=\frac{25}{333}.\]

Alternatively, let \(x = 0.075075\ldots\), so \(1000x = 75.075075\ldots\).

Subtracting, we get \(999x = 75\), so \(x=\dfrac{75}{999} = \dfrac{25}{333}\).
