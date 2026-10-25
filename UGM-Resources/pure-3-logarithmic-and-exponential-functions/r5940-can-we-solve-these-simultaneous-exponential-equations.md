---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r5940
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r5940
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5940
  old_site_id: "Q2021"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "3(4^p)=7(6^q) and 3(8^{p+1})=25(6^q) - divide and reduce to 2^p=25/56, then 'determine, to two significant figures, the value of p' by logarithms"
      rationale: "Canonical UGM title: Can we solve these simultaneous exponential equations?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1, QP 840/1, 1975, Q2b"
  task: T-UGM-IMPORT-10
---

# Can we solve these simultaneous exponential equations?

## Question

Given that \[3(4^p) = 7(6^q)\] and \[3(8^{p+1}) = 25(6^q),\] prove that \[2^p = \frac{25}{56},\] and express \(6^q\) also as the quotient of two integers.

Determine, to two significant figures, the value of \(p\).

## Solution

We can rewrite the second equation as \[3 \times 8 \times 8^p = 25 \times 6^q\] and then rewrite \(8^p\) as \(4^p \times 2^p\), which gives us \[3 \times 8 \times 4^p \times 2^p= 25 \times 6^q.\]

Dividing this by the first equation gives \[8 \times 2^p = \frac{25}{7}.\] Therefore \(2^p = \dfrac{25}{56}\), as required.

To find an expression for \(6^q\), we can start by rewriting the \(4^p\) in the first equation in terms of \(2^p\) and substitute the value we’ve just found for \(2^p\), so \(4^p = 2^{2p} = (2^p)^2\).

Therefore the first equation can be rewritten as \[3 \times (2^p)^2 = 7 \times 6^q.\] Substituting the value \(\frac{25}{56}\) for \(2^p\) gives \[7 \times 6^q = 3 \times \Bigl(\frac{25}{56}\Bigr)^2\] and therefore \[6^q = \frac{3 \times 25^2}{7 \times 56^2} = \frac{1875}{21952}.\]

Finally, calculating

\(p\)

:

\[\begin{equation} \label{eq:log} 2^p = \frac{25}{56} \end{equation}\]

so we can take logs to any base and rearrange to find \(p\). \[p\log 2 = \log\frac{25}{56}\] and therefore, dividing both sides by \(\log 2\), \[p = -1.2 \quad \text{to 2 s.f.}\]

Here we can use log to any base, say base 10. We also need a calculator to work out the numerical value of \(p\).

If your calculator can calculate logs to any base of your choosing, then you can solve equation \(\eqref{eq:log}\) immediately by calculating \(\log_2 \left(\dfrac{25}{56}\right)\).
