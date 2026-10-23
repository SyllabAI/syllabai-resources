---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7507
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7507
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7507
  old_site_id: Q157
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q5
task: T-UGM-IMPORT-6
---

# Can we show $g(n)$ is equal to the recursion depth of $f(n)$?

## Question

Let \(f(n)\) be a function defined, for any integer \(n \ge0\), as follows: \[f(n)= \begin{cases} 1 & \text{if $n=0$,}\\ (f(n/2))^2 & \text{if $n>0$ and $n$ even,}\\ 2f(n-1) & \text{if $n>0$ and $n$ odd.} \end{cases}\]

1. What is the value of \(f(5)\)?

The recursion depth of \(f(n)\) is deﬁned to be the number of other integers \(m\) such that the value of \(f(m)\) is calculated whilst computing the value of \(f(n).\) For example, the recursion depth of \(f(4)\) is \(3\), because the values of \(f(2)\), \(f(1)\), and \(f(0)\) need to be calculated on the way to computing the value of \(f(4)\).

1. What is the recursion depth of \(f(5)\)?

Now let \(g(n)\) be a function, defined for all integers \(n \ge 0\), as follows: \[g(n)= \begin{cases} 0 & \text{if } n=0,\\ 1+g(n/2) & \text{if $n>0$ and $n$ is even,}\\ 1+g(n-1) & \text{if $n>0$ and $n$ is odd.} \end{cases}\]

1. What is \(g(5)\)?

---

1. What is \(g(2^k)\), where \(k \ge 0\) is an integer? Briefly explain your answer.

---

1. What is \(g(2^l+2^k)\), where \(l> k \ge 0\) are integers? Briefly explain your answers.

---

1. Explain briefly why the value of \(g(n)\) is equal to the recursion depth of \(f(n)\).

## Solution

Let \(f(n)\) be a function defined, for any integer \(n \ge0\), as follows: \[f(n)= \begin{cases} 1 & \text{if } n=0,\\ (f(n/2))^2 & \text{if $n>0$ and $n$ even,}\\ 2f(n-1) & \text{if $n>0$ and $n$ odd.} \end{cases}\]

1. What is the value of \(f(5)\)?

Working backwards, we have

\[\begin{align*} f(5)&=2f(4)\\ &=2(f(2))^2\\ &=2(f(1))^4\\ &=2(2f(0))^4\\ &=2\times 2^4\\ &=32. \end{align*}\]

The recursion depth of \(f(n)\) is deﬁned to be the number of other integers \(m\) such that the value of \(f(m)\) is calculated whilst computing the value of \(f(n)\). For example, the recursion depth of \(f(4)\) is \(3\), because the values of \(f(2)\), \(f(1)\), and \(f(0)\) need to be calculated on the way to computing the value of \(f(4)\).

1. What is the recursion depth of \(f(5)\)?

On our way to calculating \(f(5)\), we also had to calculate \(f(4)\), \(f(2)\), \(f(1)\) and \(f(0)\), so the recursion depth is \(4\).

If we write down the first few terms of the sequence \(f(n)\), it appears that \(f(n) = 2^n.\)

We have the sequence defined by \(u_{2n} = (u_n)^2, u_{2n-1} = 2u_n, u_0 = 1,\) and it is easy to show using induction that \(u_n = 2^n\).

So we could get this sequence more simply by defining \(u_n = 2u_{n-1}\) for all \(n\), \(u_0 =1.\)

This definition, however, has a larger recursion depth than the one in the question.

\[\begin{align*} g(5) &=1+g(4)\\ &=1+(1+g(2))\\ &=1+(1+(1+g(1)))\\ &=1+(1+(1+(1+g(0))))\\ &=4. \end{align*}\]

\(2^k\) is even for all \(k>0\), and \(2^0=1\), which is odd, therefore:

\[\begin{align*} g(2^k) &= 1+g(2^{k-1})\\ &=1+(1+g(2^{k-2}))\\ &=\\ &\qquad\vdots\\ &=k+g(2^0)\\ &=k+g(1)\\ &=k+1. \end{align*}\]

As above, \(2^l\) and \(2^k\) are both even for \(l,k>0\), so

\[\begin{align*} g(2^l+2^k)&=1+g(2^{l-1}+2^{k-1})\\ &=\\ &\qquad \vdots\\ &=k+g(2^{l-k}+1)\\ &=k+1+g(2^{l-k})\\ &=k+1+(l-k+1)\\ &=l+2. \end{align*}\]

To explain the above; when \(k=0\), \(2^k=1\) so we need to calculate \(g(2^{l-k}+1)\). This has an odd input, so the output is \(1+g(2^{l-k})\). We can then use our answer from (iv), finding \(g(2^{l-k})=(l-k)+1\) and simplify our expression.

It is interesting to reflect on how \(g(n)\) works if \(n\) is written in binary.

The rule for \(g\) tells us that if \(n\) is even, \(g(n)\) is \(1 + g(n/2)\), that is, \(1\) + the binary number given by removing the \(0\) at the end of \(n\).

If \(n\) is odd, \(g(n)\) is \(1 + g(n-1)\), that is, \(1 +\) the binary number given by changing the final \(1\) to a \(0\).

Suppose \(n\) in binary has \(j\) 1s and \(k\) 0s. It is easy to see, therefore, that \(g(n)\) is \(2j + k - 1\) (the \(-1\) comes in because we don’t remove the final \(0\)).

Imagine calculating \(f(n)\) and \(g(n)\) at the same time, so we take it in turns to carry out one step in the calculation.

With every step we carry out on \(f(n)\) we create an expression in terms of \(f(c)\) where \(c\) is an integer less than \(n\).

With each corresponding step for \(g(n)\), we make \(g(n)\) the sum of \(g(c)\) and the total number of steps we’ve taken so far (this is equal to the number of different \(c\) values we’ve used so far).

Eventually we’ll reach an expression for \(f(n)\) in terms of \(f(0)\), and \(g(n)=g(0)+\text{(number of values of c used)}=0+\text{(number of values of c used)}\).

That is, \(g(n)\) is the recursion depth of \(f(n)\).
