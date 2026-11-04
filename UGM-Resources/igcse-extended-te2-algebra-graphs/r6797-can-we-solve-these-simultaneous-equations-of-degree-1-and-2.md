---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r6797
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r6797
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6797
  old_site_id: Q4017
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
  - code: E2.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Simultaneous equations of degree 1 and 2 — the E2.5.5 register verbatim.
      rationale: 'Canonical UGM title: “Can we solve these simultaneous equations of degree 1 and 2?”;
        exam provenance: UCLES O level Additional Mathematics 2, QP 420/2, 1960, Q6 (i)

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
  exam_reference: 'UCLES O level Additional Mathematics 2, QP 420/2, 1960, Q6 (i)

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-algebra/r6797/images/r6797.svg
  kind: figure
---

# Can we solve these simultaneous equations of degree 1 and 2?

## Question

Solve the simultaneous equations \[\frac{x}{3} - \frac{y}{10} = \frac{5}{6}, \quad x(y-2) = 2y + 3.\]

## Suggestion

One way we could approach this problem is by substituting one equation into the other. How could we do this?

Perhaps, though, we could make our lives easier by making the first equation look more like the second one, as the second equation only has one \(x\) in it?

Whatever we do, it might be nice to get rid of some of these fractions before we go too far!

## Solution

Let’s start by multiplying the first equation by \(30\), which is the [lowest common multiple](https://undergroundmathematics.org/glossary/lowest-common-multiple) of the denominators; in this way, we will have no more fractions. The equation thus becomes \[10x-3y=25.\]

We could rearrange this to find \(x = \dfrac{3y+25}{10}\) and substitute this into the second equation, but this reintroduces the fractions and so seems somewhat ugly.

Alternatively, we could rearrange the second equation to get \(x=\dfrac{2y+3}{y-2}\) and substitute this into the first equation, which we can then rearrange and solve to find \(y\). This, though, also has fractions in it, and this time they are algebraic.

A somewhat nicer approach is to multiply the first equation by \(y-2\), to get \[10x(y-2)-3y(y-2)=25(y-2).\] Since we know \(x(y-2)=2y+3\), this now becomes \(10(2y+3)-3y(y-2)=25(y-2)\), which we can rearrange to get \[3y^2-y-80=0.\]

This equation factorises into \((y+5)(3y-16)=0\), thus \(y = -5\) or \(y=\dfrac{16}{3}\). (Alternatively, we could use the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) to obtain these solutions.)

The corresponding values for \(x\) (using either of the original equations or their rearranged variants) are \(x=1\) and \(x=\dfrac{41}{10}\). We check that our answers are correct by substituting these \((x,y)\) pairs into the other equation.

Therefore there are two solutions: \((x,y) = (1, -5)\) or \((x,y)= \left(\dfrac{41}{10}, \dfrac{16}{3}\right)\).

Looking at this geometrically, \(10x-3y=25\) is a straight line which intersects the axes at \((\frac52,0)\) and \((0,-\frac{25}{3})\), while we can rearrange \(x(y-2) = 2y + 3\) to get \[y=\frac{2x+3}{x-2}=\frac{2(x-2)+7}{x-2}=2+\frac{7}{x-2}\] so this is a stretched and translated \(y=\frac{1}{x}\) graph (which is a rectangular hyperbola).

The straight line and other graph intersect twice, as we have discovered:

> [figure: the line crosses the hyperbola in the solution points — `https://undergroundmathematics.org/thinking-about-algebra/r6797/images/r6797.svg`] (image not included in the text import; path of record).
