---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/proving-quad-formula
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/scaffolded-task
- level/developing
resource_identity:
  ugm_id: proving-quad-formula
  station: quadratics
  station_title: Quadratics
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 8731
  old_site_id: E1_RT5_1
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
      evidence: Derive the quadratic formula (completing the square) — CIE hands the formula, derivation
        is enrichment.
      rationale: 'Canonical UGM title: “Proving the quadratic formula”; exam provenance: NRICH'
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
  exam_reference: NRICH
task: T-UGM-IMPORT-1
---

# Proving the quadratic formula

> Excerpt: This resource provides a route for students to understand the derivation of the quadratic formula. Students are asked to arrange the steps of an argument into the correct order.

## Problem

The quadratic equation \[ax^2 + bx + c = 0\] has the solution(s) \[x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}\] assuming that \(a\neq 0\).

This result looks quite strange the first time you come across it. Until you have seen a proof of it, it might seem a bit magical that it works at all.

In fact, the proof is not very much more than one tool we use in solving quadratic equations anyway—completing the square.

---

The statements below can be sorted into a proof of the quadratic formula. You might want to print them out and cut them up to rearrange them.

This shows that the original equation is equivalent to \[\left(x + \frac{b}{2a} \right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0.\]

Since \(a \neq 0\), we can divide by \(a\) to get \[x^2 + \frac{b}{a} x + \frac{c}{a} = 0.\]

We complete the square.

We can rewrite the right-hand side by putting it over a common denominator: \[\left(x + \frac{b}{2a} \right)^2 = \frac{b^2 - 4ac}{4a^2}.\]

Consider \(ax^2 + bx + c = 0\), where \(a \neq 0\).

Get the squared term on one side of the equation: \[\left(x + \frac{b}{2a} \right)^2 = \frac{b^2}{4a^2} - \frac{c}{a}.\]

Subtracting \(\frac{b}{2a}\) from both sides and putting the right-hand side over a common denominator gives \[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.\]

We can take the square root of both sides.

Since \(x\) appears only once in the equation, we can rearrange this to solve for \(x\).

Taking account of the possibility of positive and negative square roots, we see \[x + \frac{b}{2a} = \frac{\pm\sqrt{b^2 - 4ac}}{2a}.\]

## Solution

The quadratic equation \[ax^2 + bx + c = 0\] has the solution(s) \[x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}\] assuming that \(a\neq 0\).

Consider \(ax^2 + bx + c = 0\), where \(a \neq 0\).

Since \(a \neq 0\), we can divide by \(a\) to get \[x^2 + \frac{b}{a} x + \frac{c}{a} = 0.\]

We complete the square.

This shows that the original equation is equivalent to \[\left(x + \frac{b}{2a} \right)^2 - \frac{b^2}{4a^2} + \frac{c}{a} = 0.\]

Since \(x\) appears only once in the equation, we can rearrange this to solve for \(x\).

Get the squared term on one side of the equation: \[\left(x + \frac{b}{2a} \right)^2 = \frac{b^2}{4a^2} - \frac{c}{a}.\]

We can rewrite the right-hand side by putting it over a common denominator: \[\left(x + \frac{b}{2a} \right)^2 = \frac{b^2 - 4ac}{4a^2}.\]

We can take the square root of both sides.

Taking account of the possibility of positive and negative square roots, we see \[x + \frac{b}{2a} = \frac{\pm\sqrt{b^2 - 4ac}}{2a}.\]

Subtracting \(\frac{b}{2a}\) from both sides and putting the right-hand side over a common denominator gives \[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}.\]
