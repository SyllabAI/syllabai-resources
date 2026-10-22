---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9659
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9659
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9659
  old_site_id: Q225
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
      evidence: 'Distinct real roots: discriminant > 0 (MAT).'
      rationale: 'Canonical UGM title: “When does $x^2 + ax + a = 1$ have distinct real roots?”; exam
        provenance: Oxford (MAT) 2013 Q1A'
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
  exam_reference: Oxford (MAT) 2013 Q1A
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/UCGHBKJ2/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $x^2 + ax + a = 1$ have distinct real roots?

## Question

For what values of the real number \(a\) does the quadratic equation \[x^2 + ax + a = 1\] have distinct real roots?

1. \(a \neq 2\);
2. \(a > 2\);
3. \(a=2\);
4. all values of \(a\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/UCGHBKJ2/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/UCGHBKJ2)

The red curve here is \(y = x^2 + ax + a\), while the blue line is \(y = 1\).

What can we say about the curve and the line when the quadratic equation has distinct real roots?

## Solution

We can find out about the roots of this quadratic by considering its [discriminant](https://undergroundmathematics.org/glossary/discriminant).

Before we do this, we must rearrange the equation into the form “\(ax^2+bx+c=0\)”, so \[x^2 + ax + (a-1) = 0.\] Thus the discriminant is equal to \[a^2 - 4\times 1 \times (a-1) = a^2 - 4a + 4 = (a-2)^2.\]

For the quadratic to have two distinct real roots we need this to be positive and so we need \(a \ne 2\).

The answer is (a).
