---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5245
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5245
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5245
  old_site_id: Q2002
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
  exam_reference: UCLES A level Pure Mathematics 1, 1980, Q5(a)
task: T-UGM-IMPORT-6
---

# Can we find $\sum_{r=1}^n 2/(r^2+4r+3)$?

## Question

Express \[\frac{2}{r^2+4r+3}\] in partial fractions.

Hence, or otherwise, prove that \[\sum_{r=1}^n \frac{2}{r^2+4r+3}=\frac{5}{6}-\frac{2n+5}{(n+2)(n+3)}.\]

## Suggestion

We know how to rewrite the expression using partial fractions – maybe we can use this to simplify the sum?

Maybe we should try writing the sum out explicitly term by term?

## Solution

First we factorise the denominator as \[\frac{2}{r^2+4r+3}=\frac{2}{(r+1)(r+3)}.\]

Next, it makes sense to guess that there exist numbers

\(A\)

and

\(B\)

such that we have the identity

\[\begin{equation}\label{eq:partial} \frac{2}{(r+1)(r+3)}=\frac{A}{r+1}+\frac{B}{r+3}. \end{equation}\]

Forming a common denominator for the right hand side of this, we find that \[\frac{2}{(r+1)(r+3)}=\frac{A(r+3)+B(r+1)}{(r+1)(r+3)}=\frac{(A+B)r+3A+B}{(r+1)(r+3)}.\] Since the numerator must be equal to \(2\) for all values of \(r\), we obtain the system of equations \[A+B=0, \quad 3A+B=2.\] Subtracting these equations gives \(2A=2\), so \(A=1\) and therefore \(B=-1\).

Hence \[\frac{2}{r^2+4r+3}=\frac{1}{r+1}-\frac{1}{r+3}.\]

An alternative approach, starting from equation

\(\eqref{eq:partial}\)

, is to multiply both sides by

\((r+1)(r+3)\)

, giving

\[\begin{equation}\label{eq:identity} 2=A(r+3)+B(r+1). \end{equation}\]

We could proceed as before, expanding the right hand side to get the identity \(2=(A+B)r+3A+B\). Alternatively, as this identity \(\eqref{eq:identity}\) is true for all values of \(r\), we can substitute in \(r=-1\) to obtain \(2=2A\), and hence \(A=1\), and then substitute in \(r=-3\) to obtain \(2=-2B\), giving \(B=-1\).

For this part of the question, the idea is to use our partial fractions result to split the sum of interest into two simpler sums.

Substituting in the result from the previous part of the question, we obtain

\[\begin{align*} \sum_{r=1}^n \frac{2}{r^2+4r+3} &=\sum_{r=1}^n\left(\frac{1}{r+1}-\frac{1}{r+3}\right)\\ &=\sum_{r=1}^n\frac{1}{r+1}-\sum_{r=1}^n\frac{1}{r+3}, \end{align*}\]

where we have split the single sum into two separate sums on the second line.

This still looks rather intimidating, so let’s do away with the summation notation and write out the sums explicitly:

\[\begin{align*} \sum_{r=1}^n \frac{2}{r^2+4r+3}&{}=\left(\frac{1}{2}+\frac{1}{3}+\boldsymbol{\frac{1}{4}+\dotsb+\frac{1}{n+1}}\right) \\ &{}-\left(\boldsymbol{\frac{1}{4}+\frac{1}{5}+\dotsb+\frac{1}{n+1}}+\frac{1}{n+2}+\frac{1}{n+3}\right). \end{align*}\]

Now it is clear that the bold terms in the first sum are cancelled by corresponding terms in the second. Therefore, we are left with

\[\begin{align*} \sum_{r=1}^n \frac{2}{r^2+4r+3}&{}=\left(\frac{1}{2}+\frac{1}{3}\right)- \left(\frac{1}{n+2}+\frac{1}{n+3}\right)\\ &{}=\frac{5}{6}-\frac{2n+5}{(n+2)(n+3)}. \end{align*}\]
