---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7471
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7471
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7471
  old_site_id: "Q4018"
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
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "log(4/9) - log(9/125) + 2log(9/5) simplified by the quotient and power laws 'where all logarithms are to base 10' to find x and y without tables"
      rationale: "Canonical UGM title: Can we use the laws of logs to find $x$ and $y$?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Additional Mathematics 2, QP 420/2, 1960, Q6 (ii)"
  task: T-UGM-IMPORT-10
---

# Can we use the laws of logs to find $x$ and $y$?

## Question

If \[\log{x} = 2 + \log{y} = \log{\frac{4}{9}} - \log{\frac{9}{125}} + 2\log{\frac{9}{5}},\] where all logarithms are to base \(10\), find \(x\) and \(y\) without using tables.

## Suggestion

Which rules do you know to simplify expressions with logarithms? Can you use them to simplify the above equation?

## Solution

We will simplify the right hand side of the above equation as far as possible. By using the logarithm quotient rule we get

\[\begin{align*} \log{\frac{4}{9}} - \log{\frac{9}{125}} + 2\log{\frac{9}{5}} & = \log{4} - \log{9} - \log{9} + \log{125} + 2\log{9} - 2\log{5} \\ & = \log{4} + \log{125} - 2\log{5}. \end{align*}\]

Now as \(125 = 5^3\) we can use the logarithm power rule to get \[\log{4} + \log{5^3} - 2\log{5} = \log{4} + 3\log{5} - 2\log{5} = \log{4}+\log{5}=\log{20}.\] Therefore, we get \(\log{x} = \log{20}\) and thus \(x = 20\).

Now for

\(y\)

we get the equation

\(2 + \log{y} = \log{20}\)

. As all logarithms are to base

\(10\)

we can write

\(2 = \log{100}\)

and therefore

\[\begin{align*} \log{y} & = \log{20} - \log{100} \\ & = \log{\frac{20}{100}} \\ & = \log{\frac{1}{5}}. \end{align*}\]

Hence \(y = \frac{1}{5}\).
