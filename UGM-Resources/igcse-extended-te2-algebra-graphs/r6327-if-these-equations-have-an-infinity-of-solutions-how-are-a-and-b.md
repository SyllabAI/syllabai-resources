---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r6327
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r6327
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6327
  old_site_id: null
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.5.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: If these linear equations have an infinity of solutions, how are a and b related — the
        solution-structure arm of E2.5.4.
      rationale: 'Canonical UGM title: “If these equations have an infinity of solutions, how are $a$
        and $b$ related?”; exam provenance: UCLES AO level Additional Mathematics 1, QP 8175/1, 1985,
        Q30 (a)

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'UCLES AO level Additional Mathematics 1, QP 8175/1, 1985, Q30 (a)

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# If these equations have an infinity of solutions, how are $a$ and $b$ related?

## Question

Given that \(a\) and \(b\) are non-zero constants, and that the equations

\[\begin{align*} a^2x+aby&=a+4b\\ abx+b^2y&=a+b \end{align*}\]

have an infinite number of solutions for \(x\) and \(y\), express \(a\) in terms of \(b\).

## Suggestion

Given \(a\) and \(b\), what will the two equations look like when plotted as graphs on \(x\) and \(y\) axes? When will there be an infinite number of solutions for \(x\) and \(y\)?

## Solution

For given values of \(a\) and \(b\), \(a^2x+aby=a+4b\) and \(abx+b^2y=a+b\) represent straight lines in the \(x-y\) plane.

#### Approach 1

Multiply the first equation by \(b\), and the second equation by \(a\). Now subtract — we find that

\[ ba^2x + ab^2y - a^2bx -ab^2y = ab+4b^2 - a^2 - ba. \]

So all the \(x\) and \(y\) terms cancel, giving us that (if the equations are to be consistent) \(4b^2-a^2=0\).

So the set of equations has either no solutions (the lines are parallel, and the equations are inconsistent) or an infinite number of solutions (the lines are on top of each other, and the equations are consistent).

So for an infinite number of solutions we need \(0=4b^2 - a^2\) to be true, which leads us to \[a=\pm2b.\]

#### Approach 2

We can re-write each equation in the form \(y = mx + c\) ( dividing by \(a\) and \(b\) is not a problem, since they are non-zero). We have

\[y = -\frac{ax}{b}+\frac{4}{a}+\frac{1}{b}, \quad y=-\frac{ax}{b}+\frac{a}{b^2}+\frac{1}{b}.\]

We require these straight lines to coincide (be on top of each other). Their gradients are equal, so this can only happen if their \(y\)-intercepts are the same.

This means we need \[\frac{4}{a}+\frac{1}{b}=\frac{a}{b^2}+\frac{1}{b},\]

which yields \[ a=\pm2b. \]
