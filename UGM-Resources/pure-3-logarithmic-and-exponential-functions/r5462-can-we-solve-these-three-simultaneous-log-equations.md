---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r5462
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r5462
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5462
  old_site_id: "Q241"
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
      evidence: "log_b a=2, log_b(c-3)=3, log_a(c+5)=2 written in exponential form (a=b^2, c-3=b^3, c+5=a^2); b^4=b^3+8 discriminates the two values of a"
      rationale: "Canonical UGM title: Can we solve these three simultaneous log equations?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2013, Q1F"
  task: T-UGM-IMPORT-10
---

# Can we solve these three simultaneous log equations?

## Question

Three *positive* numbers \(a\), \(b\), \(c\) satisfy \[\log_b a = 2, \qquad \log_b (c-3) = 3, \qquad \log_a (c+5) = 2.\] This information

1. specifies \(a\) uniquely.

---

1. is satisfied by two values of \(a\).

---

1. is satisfied by infinitely many values of \(a\).

---

1. is contradictory.

## Suggestion

Could we rewrite the equations using powers rather than logarithms?

## Solution

If we write the three equations in exponential form, we get \[a=b^2, \qquad c-3 = b^3, \qquad c+5 = a^2.\] We can then eliminate \(a\) and \(c\) by substituting the first and second equations into the third, to get \[b^3 + 3 + 5 = b^4,\] which rearranges to \[b^3(b-1)=8.\]

We require \(b\) to be positive, so we are only interested in positive solutions of this equation.

We note that \(b^3(b-1)\) is negative for \(0<b<1\), and then for \(b>1\), both \(b^3\) and \(b-1\) are positive and increasing (without bound).

So there is only one positive solution to this equation (in fact by looking at it we can easily spot that \(b=2\)), so there is only one possible value for \(a\) and for \(c\) (namely \(a=4\) and \(c=11\)).

The answer is (a).
