---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r5847
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r5847
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5847
  old_site_id: Q3026
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
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Three square roots; squaring chain reduces to a quadratic.
      rationale: 'Canonical UGM title: “How do we solve an equation containing three square roots?”; exam
        provenance: UCLES 1970 Q5(ii)'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1970 Q5(ii)
task: T-UGM-IMPORT-1
---

# How do we solve an equation containing three square roots?

## Question

Solve the equation \[ \sqrt{x+4} + \sqrt{x+10} = \sqrt{8x + 18}. \]

## Suggestion

Do we know a way of ‘undoing’ square roots?

What happens if we try squaring both sides? Can things be simplified?

**A further suggestion**

## Solution

By squaring both sides and rearranging, the equation becomes

\[\begin{align*} \left( \sqrt{x+4} + \sqrt{x+10} \right)^2 = \left( \sqrt{8x + 18} \right)^2 &\implies \left( \sqrt{x+4}\right)^2 + 2\sqrt{x+4}\sqrt{x+10} + \left( \sqrt{x+10} \right)^2 = \left( \sqrt{8x + 18} \right)^2 \\ &\implies(x+4) + 2\sqrt{x+4}\sqrt{x+10} + (x+10) = 8x + 18 \\ &\implies 2\sqrt{x+4}\sqrt{x+10} = 6x + 4 \\ &\implies \sqrt{x+4}\sqrt{x+10} = 3x + 2. \end{align*}\]

Again squaring both sides, we have

\[\begin{align*} \left( \sqrt{x+4}\sqrt{x+10} \right)^2 = \left(3x + 2\right)^2 &\implies (x+4)(x+10) = (3x + 2)^2 \\ &\implies x^2 + 14x + 40 = 9x^2 + 12x + 4 \\ &\implies 8x^2 - 2x - 36 = 0 \\ &\implies 4x^2 - x - 18 = 0 \\ &\implies (4x - 9)(x + 2) = 0. \end{align*}\]

The solutions to this final equation are

\[ x = \dfrac{9}{4} \quad\text{and}\quad x = -2. \]

But we need to be cautious here; our squaring may have introduced “false” solutions.

For example, the equation \(x+1 = 2\) clearly has the unique solution \(x = 1\). But if we square both sides, we get \((x+1)^2 = 4\), which has the solution \(x = 1\) and the “false” solution \(x = -3\).

So we need to check our answers by substituting back into our original equation.

If we do this, we see that \(\dfrac{9}{4}\) is a solution, but \(-2\) is not.
