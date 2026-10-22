---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7533
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7533
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7533
  old_site_id: Q183
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Inequality proof with two square roots — beyond routine, but discriminant/sign reasoning.
      rationale: 'Canonical UGM title: “Can we prove this inequality involving two square roots?”; exam
        provenance: UCLES 1981 Q6(i)'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1981 Q6(i)
task: T-UGM-IMPORT-1
---

# Can we prove this inequality involving two square roots?

## Question

Given that \(0<x<1\), prove that \[\sqrt{1+x}+\sqrt{1-x}<2.\]

## Suggestion

Given that \(0<x<1\), prove that \(\sqrt{1+x}+\sqrt{1-x}<2\).

Can we get rid of those square roots? Would squaring both sides be helpful? Are we allowed to do this?

## Solution

Given that \(0<x<1\), prove that \(\sqrt{1+x}+\sqrt{1-x}<2\).

We need to be careful when squaring inequalities. For example, \(-3 < 2\), but \((-3)^2 > 2^2.\)

But if \(0 < a < b\), then we can definitely say that \(0 < a^2 < b^2\) and \(0 < \sqrt{a} < \sqrt{b}\).

We will use this idea to help us answer this question.

It’s true here that \(0 < \sqrt{1+x}+\sqrt{1-x}\).

So \(0 < \sqrt{1+x}+\sqrt{1-x}<2\) if and only if \(0 < \bigl(\sqrt{1+x}+\sqrt{1-x}\bigr)^2<4\).

Therefore, to prove the inequality we require, we only need to show that \(0 < \bigl(\sqrt{1+x}+\sqrt{1-x}\bigr)^2<4\).

The left hand inequality is clear.

Expanding the central expression, we have

\[\begin{align*} \bigl(\sqrt{1+x}+\sqrt{1-x}\bigr)^2&=(1+x) + 2\sqrt{(1+x)(1-x)} + (1-x)\\ &=2+2\sqrt{1-x^2}. \end{align*}\]

Since \(\sqrt{1-x^2}<1\), the right hand side is less than \(4\), as we wanted.

So we have \(\sqrt{1+x}+\sqrt{1-x}<2\).
