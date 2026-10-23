---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r5416
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r5416
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5416
  old_site_id: Q203
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
  exam_reference: UCLES A level Mathematics 1, 1955, Q4
task: T-UGM-IMPORT-6
---

# Can we sum the first $2n$ terms of $1^2-3^2+5^2-7^2+\cdots$?

## Question

By bracketing the terms in pairs, or otherwise, find the sum of \(2n\) terms of the series \[1^2-3^2+5^2-7^2+\cdots.\]

Hence show that the sum of \(2n+1\) terms is \(8n^2+8n+1\).

## Suggestion

Can we find an expression for a general term in the series?

What is the sign of the \(2k^{th}\) term?

Can we find expressions for the two terms in the \(k^{th}\) pair?

Can we factorise \(a^2-b^2\)?

Can we check our formula by substituting in a couple of values for \(n\)?

## Solution

We’ll simplify this sum by pairing the terms, as the question suggests. We know how to factorise the difference of two squares:

\[a^2-b^2=(a+b)(a-b).\]

We have here

\[\begin{align*} 1^2-3^2&=(1-3)(1+3)=-2\times 4, \\ 5^2-7^2&=(5-7)(5+7)=-2\times12, \\ 9^2-11^2&=(9-11)(9+11)=-2\times20, \\ \dots. \end{align*}\]

The \(k^{th}\) pair of terms is \[(4k-3)^2-(4k-1)^2=\bigl((4k-3)-(4k-1)\bigr)\bigl((4k-3)+(4k-1)\bigr) =-2(8k-4).\]

How did we work out the \(4k-3\) and \(4k-1\)?

The first terms of each pair form the sequence \(1\), \(5\), \(9\), …, which is the sequence \(4k-3\).

The second term of each pair is two greater, and so is \(4k-1\).

So the sum of the first \(2n\) terms, which is the first \(n\) pairs, is \[(-2)[4+12+20+... +(8n-4)]\] \[=(-2)\dfrac{n}{2}[8+(n-1)8]\] \[= -8n^2.\]

We are using here that the sum of \(n\) terms of an arithmetic sequence with first term \(a\) and common difference \(d\) is \[\dfrac{n}{2}[2a+(n-1)d].\]

We can check this: the sum of the first two terms is\(1^2-3^2=-8=-8\times1^2\).

The sum of the first four terms is \(1^2-3^2+5^2-7^2=-8+25-49=-32=-8\times 2^2\).

So it looks as if we have the correct formula.

Now we wish to find the sum of the first \(2n+1\) terms.

The sum of the first \(2n\) terms is \(-8n^2\), and the \((2n+1)^{st}\) term is \((4(n+1)-3)^2=(4n+1)^2\).

Thus the sum of the first \(2n+1\) terms is \((4n+1)^2-8n^2 = 8n^2+8n+1\), as required.
