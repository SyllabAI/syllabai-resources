---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/factorial-fragments
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: factorial-fragments
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 6099
  old_site_id: "A4_RT11_1"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "log n! explored across values and bases - log(n!) = sum of log k generalisation and 'what happens if you change the base'; log-law fluency"
      rationale: "Canonical UGM title: Factorial fragments"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# Factorial fragments

> Excerpt: In this open task, students explore the expression $\log n!$ for different values of $n$ and thereby gain fluency in manipulation and understanding of logarithms.

## Problem

Think about this expression

\[\large{\log n!}\]

What can you say about it?

Try some values of \(n\).

Choose a base or work generally. What happens if you change the base?

What do you notice?

## Some things to think about

Think about this expression \[\log n!\]

What can you say about it?

Try some values of \(n\).

Choose a base or work generally. What happens if you change the base?

What do you notice?

For example, do you agree with these

\[\begin{align*} \log_2 3! \, &= \log_2 (1\times 2\times 3) \\ &= \log_2 1 + \log_2 2 + \log_2 3 \\ &= 1+\log_2 3 \end{align*}\]

and

\[\begin{align*} \log_3 6!\, &= \log_3 (1\times2\times3\times4\times5\times6) \\ &= \log_3 1 + \log_3 2 + \log_3 3 + \log_3 4 +\log_3 5 + \log_3 6 \\ &= 4\log_3 2 + 2 + \log_3 5 \end{align*}\]

- What do you notice about the coefficients?

- Do you always get an integer term, whatever base you use?

- If you knew \(\log_2 12!\) could you write down what \(\log_4 12!\) is?

- What could \(n\) be if \(\log_5 n!\) has integer term \(3\) when expanded as far as possible?

- What can you say about \(n\) if \(\log_6 n!\) has integer term \(4\)?

- If you know that \(p\) and \(q\) are primes larger than \(7\) and \(a\) is not prime, can you fill in the boxes in the equation below? \[\log \square! = a\log 2 + \square \log 3 + 3 \log 5 +\square \log 7 + \log p +\log q\] Note that the numbers in the boxes may or may not be the same. Can you make up a similar question?
