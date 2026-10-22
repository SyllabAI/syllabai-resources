---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7455
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7455
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7455
  old_site_id: Q1067
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
  - code: 1.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'Repeated root with parameter: discriminant = 0.'
      rationale: 'Canonical UGM title: “When does $(p+1)x^2+4px+9=0$ have a repeated root?”; exam provenance:
        UCLES 1986 Q5(a)'
      validation_status: SUGGESTED
    title: find the discriminant of a quadratic polynomial ax + bx + c and use the discriminant ‘repeated
      root’ is included.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1986 Q5(a)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/XnjucJEw/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $(p+1)x^2+4px+9=0$ have a repeated root?

## Question

Find the values of \(p\) for which the equation \[ (p+1)x^2+4px+9=0\] has equal roots.

## Suggestion

Find the values of \(p\) for which the equation \[(p+1)x^2+4px+9=0\] has equal roots.

When does the quadratic equation \(ax^2 + bx + c = 0\) have equal roots?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/XnjucJEw/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/XnjucJEw)

The red curve here is \(y = (p+1)x^2+4px +9\).

What will the curve look like when the equation has equal roots?

Can you find the required values of \(p\)?

## Solution

A quadratic equation has equal roots if and only if its [discriminant](https://undergroundmathematics.org/glossary/discriminant) is zero.

So here we require

\((4p)^2 - 4(9(p+1)) = 0\)

. Dividing by

\(4\)

gives

\[\begin{align*} 4p^2 - 9(p+1) &=0 &\iff\quad&&4p^2 - 9p - 9 = 0 \\ &&\iff\quad&&(p - 3)(4p + 3) = 0 \\ &&\iff\quad&&p = 3 \ \text{or} \ p=-\tfrac{3}{4}. \end{align*}\]

So for these two values of \(p\) (and no other values), the quadratic equation has equal roots.
