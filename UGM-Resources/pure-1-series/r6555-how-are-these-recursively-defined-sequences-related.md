---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6555
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6555
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6555
  old_site_id: Q170
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q2
task: T-UGM-IMPORT-6
---

# How are these recursively defined sequences related?

## Question

A list of real numbers \(x_1\), \(x_2\), \(x_3\), … is defined by \(x_1 = 1\), \(x_2 = 3\) and then for \(n\geq3\) by \[x_n = 2x_{n−1} −x_{n−2} + 1.\]

So, for example, \(x_3 = 2x_2 −x_1 +1=2\times3−1+1=6\).

1. Find the values of \(x_4\) and \(x_5\).

---

1. Find values of real constants \(A\), \(B\), \(C\) such that for \(n = 1\), \(2\), \(3\), \[\begin{equation*} x_n = A+Bn+Cn^2. \label{eq:star}\tag{$*$} \end{equation*}\]

---

1. Assuming that equation \(\eqref{eq:star}\) holds true for all \(n\geq1\), find the smallest \(n\) such that \(x_n\geq800\).

---

1. A second list of real numbers \(y_1\), \(y_2\), \(y_3\), … is defined by \(y_1 = 1\) and \[y_n = y_{n−1} + 2n.\] Find, explaining your reasoning, a formula for \(y_n\) which holds for \(n\geq2\). What is the approximate value of \(\dfrac{x_n}{y_n}\) for large values of \(n\)?

## Suggestion

Write out the first few terms of \(y_n\) – what kind of sequence is this? Are there any familiar patterns in the \(n\)th term?

Could we write \(y_n\) in terms of \(x_n\)? Or \(x_n\) in terms of \(y_n\)?

## Solution

Using the given formula,

\[\begin{align*} x_4&=2x_3-x_2+1=2\times6-3+1=10,\\ x_5&=2x_4-x_3+1=2\times10-6+1=15. \end{align*}\]

1. Find values of real constants \(A\), \(B\), \(C\) such that for \(n = 1\), \(2\), \(3\), \[\begin{equation*} x_n = A+Bn+Cn^2. \label{eq:starrepeat}\tag{$*$} \end{equation*}\]

Putting \(n = 1\), \(2\), \(3\), we have that \(A\), \(B\) and \(C\) must satisfy \[A+B+C=1,\] \[A+2B+4C=3,\] and \[A+3B+9C=6.\]

Subtracting the second equation from the third gives us \(B+5C=3\), and taking the first equation from the second gives \(B+3C=2\).

These give us that \(C=\tfrac{1}{2}\), \(B=\tfrac{1}{2}\) and \(A=0\).

So equation \(\eqref{eq:starrepeat}\) becomes \[x_n=\frac{1}{2}n(n+1).\]

This is the formula for the sum of the first \(n\) natural numbers.

1. Assuming that equation \(\eqref{eq:starrepeat}\) holds true for all \(n\geq1\), find the smallest \(n\) such that \(x_n\geq800\).

From above we know that \(x_n\geq800\) requires \(n(n+1)\geq1600\).

We know that \(40^2=1600\), which means that \(n=40\) will give us \(n(n+1)=40\times41>1600\). To be sure it is the smallest \(n\) we should check \(n=39\). This leads to \(n(n+1)=39\times40\) which is less than \(1600\). So \(n=40\) is the smallest value that gives \(x_n\geq800\).

Alternatively we can solve \(n(n+1) = 1600\), or \(n^2+n-1600=0\).

Using the quadratic formula gives \(n \approx 39.5\), and so \(n(n+1)\geq1600\) for the first time when \(n = 40\).

Let’s start by writing out the first few equations to deduce the

\(n\)

th term:

\[\begin{align*} y_1&=1\\ y_2&=1+4\\ y_3&=1+4+6\\ \dots\\ y_n&=1+4+6+\cdots +2n. \end{align*}\]

Taking a closer look at the \(n\)th term, what we have is \[y_n=1+2(2+3+4+\cdots+(n-1)+n) = 2(1+2+3+\cdots +n)-1.\]

Looking at the right hand side of this, we see the sum of all the consecutive numbers from \(1\) to \(n\).

We know that this sum is equal to \(\tfrac{1}{2}n(n+1)\), so our equation reads \[y_n=n(n+1)-1.\]

We have \[x_n=\frac{1}{2}n(n+1)\] and \[y_n=n(n+1)-1.\] Notice that \(y_n=2x_n-1\).

So the ratio becomes \[\frac{x_n}{y_n} = \frac{2x_n}{2y_n} = \frac{y_n+1}{2y_n} = \frac{1}{2}+\frac{1}{2y_n}.\]

For large values of \(n\), \(y_n\) is large, and so \(\dfrac{1}{2y_n}\) is close to \(0\).

This means that the ratio \(\dfrac{x_n}{y_n}\) is approximately \(\dfrac{1}{2}\).
