---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6137
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6137
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6137
  old_site_id: Q189
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
      evidence: P(q-r)+Q(r-p)+R(p-q)=0 for AP terms and the log analogue for GP terms — nth-term formulae
        of both progressions
      rationale: 'Canonical UGM title: "How are the $p$th, $q$th and $r$th terms of an AP related?";
        exam provenance: UCLES A level Mathematics 1, 1951, Q1'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 1, 1951, Q1
task: T-UGM-IMPORT-6
---

# How are the $p$th, $q$th and $r$th terms of an AP related?

## Question

The \(p\)th term of a progression is \(P\), the \(q\)th term is \(Q\), and the \(r\)th term is \(R\). Show that, if the progression is arithmetical, \[P(q-r)+Q(r-p)+R(p-q)=0\] and that, if it is geometrical, \[(q-r)\log P+(r-p)\log Q+(p-q)\log R=0.\]

## Solution

Let \(a\) be the first term of the progression and \(d\) be the common difference. Then \[P=a+(p-1)d, \quad Q=a+(q-1)d\quad\text{and }R=a+(r-1)d.\]

Therefore,

\[\begin{align*} P(q-r)+&Q(r-p)+R(p-q)\\ &=\bigl(a+(p-1)d\bigr)(q-r)+\bigl(a+(q-1)d\bigr)(r-p)+\bigl(a+(r-1)d\bigr)(p-q)\\ &=a(q-r+r-p+p-q)+d\bigl((p-1)(q-r)+(q-1)(r-p)+(r-1)(p-q)\bigr)\\ &=d(pq-pr-q+r+qr-qp-r+p+rp-qr-p+q)\\ &=0. \end{align*}\]

Alternatively, \(P-Q = (p-q)d\), and \(P-R = (p-r)d\). We can divide these to eliminate \(d\), and then rearrange to get the same result.

…and that, if it is geometrical, \[(q-r)\log P+(r-p)\log Q+(p-q)\log R=0.\]

Let \(a\) be the first term of the progression and \(r\) be the common ratio.
 Then, \[P=ar^{p-1},\quad Q=ar^{q-1}\quad\text{and}\quad R=ar^{r-1}.\]

Therefore, taking logs,

\[\begin{align*} \log P&=\log a+(p-1)\log r,\\ \log Q&=\log a+(q-1)\log r,\\ \log R&=\log a+(r-1)\log r. \end{align*}\]

We can now see that \(\log P, \log Q\) and \(\log R\) are the \(p^{th}\), \(q^{th}\) and \(r^{th}\) terms in an arithmetic progression with common difference \(\log r\).

So using the first part of the question, \((q-r)\log P+(r-p)\log Q+(p-q)\log R = 0\).
