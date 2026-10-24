---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r9976
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r9976
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9976
  old_site_id: "Q4026"
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
      evidence: "'Using the logarithm laws, we can rewrite the first two terms' - 2lg5 - (1/2)lg9 + lg0.12 evaluated without calculators from lg2=0.30103, lg3=0.47712 (lg x = log_10 x)"
      rationale: "Canonical UGM title: Can we evaluate  these log expressions without using a calculator?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Mathematics Alternative A Algebra, QP 450/3, 1973, Q6(i,iii)"
  task: T-UGM-IMPORT-10
---

# Can we evaluate  these log expressions without using a calculator?

## Question

1. Without using tables [or calculators], find the value of \[\begin{align*} 2 \lg 5 - \frac{1}{2} &\lg 9 + \lg 0.12.\\ [\lg x &= \log_{10} x] \end{align*}\]

---

1. If \(\lg 2 = 0.30103\) and \(\lg 3 = 0.47712\), find, without using tables [or calculators], the values of \(\lg 6\) and \(\lg 15\).

## Suggestion

If we can’t use calculators, we have to simplify this expression. So what rules and identities do we know for [logarithms](https://undergroundmathematics.org/glossary/logarithm-laws)?

How could we rewrite the required logarithms in terms of the logarithms we are given? Remember that all logarithms are to base 10!

## Solution

Using the [logarithm laws](https://undergroundmathematics.org/glossary/logarithm-laws), we can rewrite the first two terms as

\[\begin{align*} 2 \lg 5 &= \lg 5^2 = \lg 25\\ - \frac{1}{2}\lg 9 &= \lg 9^{-\frac{1}{2}} = \lg \frac{1}{\sqrt{9}} = \lg \frac{1}{3}. \end{align*}\]

Now we can evaluate the original expression

\[\begin{align*} \lg 25+\lg \frac{1}{3}+\lg \frac{12}{10} &= \lg \left( \frac{25\times12}{3\times10}\right)\\ &=\lg \left( 10\right)\\ &=1. \end{align*}\]

Following the logarithm laws we can rewrite the logarithm of six as \[\lg 6 = \lg 2\times3 = \left(\lg 2\right)+\left(\lg 3\right).\]

Inserting the given values for \(\lg 2\) and \(\lg 3\) we therefore obtain \[\lg 6 = 0.30103 + 0.47712 \approx 0.7782.\]

Since both given values have a precision of 5 decimal places, we can approximate the solution to 4 decimal places.

Fifteen can be expressed as \[15=\frac{10\times3}{2}.\]

Since we know the base-10 logarithm of 2, 3 and 10 we can write

\[\begin{align*} \lg 15 &= \lg \frac{10\times3}{2}\\ &= \left( \lg 10 \right) + \left( \lg 3 \right) - \left( \lg 2 \right)\\ &\approx 1 + 0.47712 - 0.30103\\ &= 1.1761. \end{align*}\]
