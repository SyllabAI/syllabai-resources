---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8812
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8812
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8812
  old_site_id: Q3012
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
      evidence: Show a quadratic always has real roots — discriminant condition.
      rationale: 'Canonical UGM title: “Can we show $(b^2 - 2ac)x^2 + 4(a + c)x = 8$ always has real roots?”;
        exam provenance: UCLES 1980 Q12(b)'
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
  exam_reference: UCLES 1980 Q12(b)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/zXpND8SE/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we show $(b^2 - 2ac)x^2 + 4(a + c)x = 8$ always has real roots?

## Question

Prove that the roots of \((b^2 - 2ac)x^2 + 4(a + c)x = 8\) are real if \(a\), \(b\), \(c\) are real. Find the conditions that the roots are equal.

## Suggestion

Would the [discriminant](https://undergroundmathematics.org/glossary/discriminant) be helpful here?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/zXpND8SE/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/zXpND8SE)

The curve here is \(y=(b^2 - 2ac)x^2 + 4(a + c)x -8\).

What can we say about the curve if the roots of the equation are real?

What would the curve look like if the roots of the equation are equal?

## Solution

The roots of a quadratic equation are real if the [discriminant](https://undergroundmathematics.org/glossary/discriminant) is greater than or equal to zero.

We will assume throughout this question that \(b^2-2ac\), the coefficient of \(x^2\), is non-zero. If it were zero, we would not have a quadratic equation any longer!

The quadratic equation here is

\[ (b^2 - 2ac)x^2 + 4(a + c)x - 8=0, \]

and so its discriminant (denoted by

\(\Delta\)

) is

\[\begin{align*} \Delta &= 16(a + c)^2 - 4(b^2 - 2ac)(-8) \\ &= 16(a + c)^2 + 32(b^2 - 2ac). \end{align*}\]

There is a common factor of \(16\), which it would be helpful to take out. By expanding and simplifying, we then see that

\[\begin{align*} \Delta &= 16\bigl((a+c)^2+2(b^2-2ac)\bigr) \\ &= 16(a^2 + 2ac + c^2 + 2b^2 - 4ac) \\ &= 16(a^2 - 2ac + c^2 + 2b^2) \\ &= 16\bigl((a - c)^2 + 2b^2\bigr), \end{align*}\]

which is nonnegative for all real \(a\), \(b\), and \(c\), as it is a sum of squares, and a square cannot be negative.

The two roots are equal when the discriminant, \(\Delta\), is zero. This occurs precisely when both of the squares \((a-c)^2\) and \(b^2\) are zero, that is, when \(a = c\) and \(b = 0\).
