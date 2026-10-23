---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r7424
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r7424
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7424
  old_site_id: null
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
      evidence: prove the AP range-sum formula, sum 1000..2000 excluding multiples of 5; GP r=0.95 least
        n with S-S_n<1
      rationale: 'Canonical UGM title: "Can we sum from $1000$ to $2000$ excluding multiples of 5?";
        exam provenance: UCLES A level Mathematics B 1, 1978, Q1'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: prove the AP range-sum formula, sum 1000..2000 excluding multiples of 5; GP r=0.95 least
        n with S-S_n<1
      rationale: 'Canonical UGM title: "Can we sum from $1000$ to $2000$ excluding multiples of 5?";
        exam provenance: UCLES A level Mathematics B 1, 1978, Q1'
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
  exam_reference: UCLES A level Mathematics B 1, 1978, Q1
task: T-UGM-IMPORT-6
---

# Can we sum from $1000$ to $2000$ excluding multiples of 5?

## Question

1. Prove that the sum of all the integers between \(m\) and \(n\) inclusive (\(m, n \in \mathbb{Z}_+\), \(n > m\)) is \(\tfrac{1}{2}(m+n)(n-m+1)\). Find the sum of all the integers between \(1000\) and \(2000\) which are *not* divisible by \(5\).

---

1. A geometric series has first term \(2\) and common ratio \(0.95\). The sum of the first \(n\) terms of the series is denoted by \(S_n\) and the sum to infinity is denoted by \(S\). Calculate the least value of \(n\) for which \(S - S_n < 1\).

## Solution

We know that

\(1 + 2 + \ldots + n = \dfrac{n(n+1)}{2}\)

. So we can write

\[\begin{align*} m+(m+1) + (m+2) + \ldots + n &= (1 + 2 + \ldots + n)-(1 + 2 + \ldots + (m-1))\\ &= \frac{n(n+1)}{2} - \frac{(m-1)m}{2} \\ &= \frac{n^2 + n - m^2 + m}{2} \\ &= \frac{(m+n)(n-m+1)}{2}. \end{align*}\]

We can calculate this by summing all the integers between

\(1000\)

and

\(2000\)

, and then subtracting the sum of all those divisible by

\(5\)

. By the above formula,

\[\begin{equation*} \sum_{i=1000}^{2000} i = \frac{(1000 + 2000)(2000 - 1000 + 1)}{2} = \frac{3000 \times 1001}{2} = 1\,501\,500. \end{equation*}\]

The sum of all numbers between

\(1000\)

and

\(2000\)

that

are

divisible by

\(5\)

can be written as

\[\begin{align*} 1000 + 1005 + \dotsb + 1995 + 2000 &= 5 \times 200 + 5 \times 201 + \dotsb + 5 \times 400 \\ &= 5 \times \left( 200 + 201 + \dotsb + 400 \right) \\ &= 5 \sum_{i=200}^{400} i \\ &= \frac{5 \times (200+400) \times (400 - 200 + 1)}{2} \\ &= \frac{5 \times 600 \times 201}{2} \\ &= 301\,500. \end{align*}\]

Hence, the desired sum is

\[\begin{equation*} 1\,501\,500 - 301\,500 = 1\,200\,000. \end{equation*}\]

We have

\[\begin{equation*} S_n = a \frac{1 - r^n}{1-r}, \end{equation*}\]

where

\(a = 2\)

and

\(r = 0.95\)

, and

\[\begin{equation*} S = \lim_{n \to \infty} S_n = \frac{a}{1-r} = \dfrac{2}{0.05} = 40. \end{equation*}\]

We are to find the least value of \(n\) for which \(S - S_n < 1\); let’s try to solve \(S - S_n = 1\).

This gives us \(40 - 2\dfrac{1 - 0.95^n}{1-0.95}=40 - 40(1-0.95^n)=1\), and multiplying out and rearranging gives \[0.95^n=\dfrac{1}{40} \implies n = \dfrac{\ln(1/40)}{\ln 0.95} = 71.9...\]

Thus the value of \(n\) that we require is \(72\).

Alternatively, we could solve \(0.95^n=\dfrac{1}{40}\) by taking logs to base \(0.95\).
