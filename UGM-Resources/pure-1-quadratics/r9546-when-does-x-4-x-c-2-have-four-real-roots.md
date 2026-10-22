---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9546
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9546
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9546
  old_site_id: Q80
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'x^4 = (x-c)^2: quadratic in x^2; count four real roots (MAT).'
      rationale: 'Canonical UGM title: “When does $x^4=(x-c)^2$ have four real roots?”; exam provenance:
        Oxford (MAT) 2009 Q1C'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2009 Q1C
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/EFTgpQun/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $x^4=(x-c)^2$ have four real roots?

## Question

Given a real constant, \(c\), the equation \[x^4=(x-c)^2\] has four real solutions (including possible repeated roots) for

1. \(c\leq \frac{1}{4}\),
2. \(-\frac{1}{4} \leq c \leq \frac{1}{4}\),
3. \(c \leq -\frac{1}{4}\),
4. all values of \(c\).

## Suggestion

How could we turn this question into a question about quadratics?

Remember that there are two possible solutions when we solve an equation of the form \(y^2=a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/EFTgpQun/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/EFTgpQun)

The blue curve is \(y = x^4 - (x-c)^2\).

What could we say about this curve when the above equation has “four real solutions”?

## Solution

If we square root both sides of the equation \(x^4=(x-c)^2\), we find that this holds if and only if \[x^2=x-c\quad\text{or}\quad x^2=-(x-c).\]

Rearranging these gives \[x^2-x+c=0\quad\text{or}\quad x^2+x-c=0,\]

These will have two real roots (or one repeated real root) if the [discriminant](https://undergroundmathematics.org/glossary/discriminant) is non-negative, so we require \[1-4c\ge0\quad\text{and}\quad 1+4c\ge0\] respectively.

Combining these two requirements we get the result that \[-\frac{1}{4} \leq c \leq \frac{1}{4}.\]

Alternatively, we can think of the original equation as a difference of two squares. Moving both terms to one side of the equation we get \[x^4-(x-c)^2 = (x^2)^2-(x-c)^2 = (x^2+x-c)(x^2-x+c)=0\] and so \(x^2+x-c=0\) or \(x^2-x+c=0\), as before.

So the answer is (b).
