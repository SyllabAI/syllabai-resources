---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r7487
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r7487
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7487
  old_site_id: Q1015
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
      evidence: sum of 1/2+1/6+1/18+... (formula must be proved), sum to infinity, least n exceeding
        2999/4000
      rationale: 'Canonical UGM title: "When does the sum of this series first exceed $2999/4000$?";
        exam provenance: UCLES A level Mathematics 1, 1958, Q4'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: sum of 1/2+1/6+1/18+... (formula must be proved), sum to infinity, least n exceeding
        2999/4000
      rationale: 'Canonical UGM title: "When does the sum of this series first exceed $2999/4000$?";
        exam provenance: UCLES A level Mathematics 1, 1958, Q4'
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
  exam_reference: UCLES A level Mathematics 1, 1958, Q4
task: T-UGM-IMPORT-6
---

# When does the sum of this series first exceed $2999/4000$?

## Question

Find the sum of \(n\) terms of the geometric progression \[\frac{1}{2}+\frac{1}{6}+\frac{1}{18}+\dotsb.\] [If a general formula is used, it must first be proved.]

Deduce the sum to infinity of this series.

Find the least number of terms of the series which must be taken for their sum to exceed \(\dfrac{2999}{4000}\).

## Suggestion

What is the common ratio of this geometric series?

What is the \(n\)th term of this geometric series?

Let \(S_n\) denote the sum of the first \(n\) terms. Could we write the expansion of \(\frac{1}{3}S_n\) underneath the expression for \(S_n\)?

What do we notice? What happens if we take the two expressions away from each other?

When \(n\to \infty\), what does \(S_n\) tend towards?

Could we try to find an \(n\) such that \(S_n = \dfrac{2999}{4000}\)?

Could we write down the first few powers of \(3\)?

## Solution

This is the sum of a geometric series with first term \(a=\dfrac{1}{2}\) and common ratio \(r=\dfrac{1}{3}\). The \(n\)th term in this series is \[ar^{n-1}=\frac{1}{2}\left(\frac{1}{3}\right)^{n-1}.\]

Let the sum of the first \(n\) terms be \(S_n\), so \[S_n=\frac{1}{2}+\frac{1}{6}+\frac{1}{18}+\dotsb+\frac{1}{2}\left(\frac{1}{3}\right)^{n-1}.\]

Multiplying the above by

\(\dfrac{1}{3}\)

, we have

\[\begin{align*} \frac{1}{3}S_n&=\frac{1}{6}+\frac{1}{18}+\frac{1}{54}+\dotsb+\frac{1}{2}\left(\frac{1}{3}\right)^n,\\ \end{align*}\]

and now subtracting this equation from the one above it, since all the fractions

\(\dfrac{1}{6}, \dfrac{1}{18}, \dotsc, \dfrac{1}{2}\left(\dfrac{1}{3}\right)^{n-1}\)

cancel,

\[\begin{align*} S_n-\frac{1}{3}S_n &= \frac{1}{2}-\frac{1}{2}\left(\frac{1}{3}\right)^n\\ \Longrightarrow \quad \frac{2}{3}S_n &= \frac{1}{2}\left[1-\left(\frac{1}{3}\right)^n\right] \left(\text{ taking out a factor of } \frac{1}{2}\right),\\ \Longrightarrow \quad S_n &= \frac{3}{4}\left[1-\left(\frac{1}{3}\right)^n\right] \left(\text{ dividing both sides by }\frac{2}{3}\right). \end{align*}\]

As \(n\to\infty\), \[\left(\frac{1}{3}\right)^n \to 0.\] Therefore, the sum to infinity of this geometric series is \[S_{\infty}=\frac{3}{4}\left(1-0\right) = \frac{3}{4}.\]

We are looking for the \(n\) such that \[S_{n-1}\leq\frac{2999}{4000}\;\; \text{and}\;\; S_n>\frac{2999}{4000}.\]

So we want to solve for

\(n\)

\[\begin{align*} \frac{3}{4}\left[1-\left(\frac{1}{3}\right)^{n}\right]&=\frac{2999}{4000}=\frac{3000-1}{4000} \end{align*}\]

dividing through by

\(\dfrac{3}{4}\)

gives

\[\begin{align*} 1-\left(\frac{1}{3}\right)^{n}&=\frac{3000-1}{3000} \end{align*}\]

and this is the same as

\[\begin{align*} 1-\frac{1}{3^{n}}&= 1-\frac{1}{3000}\\ \Longrightarrow \quad \frac{1}{3000}&= \frac{1}{3^{n}} \\ \Longrightarrow \quad 3^{n} &= 3000 \\ \Longrightarrow \quad 3^{n-1} &= 1000. \end{align*}\]

Taking logs here gives \(n = 1 + \dfrac{\log(1000)}{\log 3} \approx 7.29.\) So the first \(S_n\) to exceed \(\dfrac{2999}{4000}\) is \(S_8\).
