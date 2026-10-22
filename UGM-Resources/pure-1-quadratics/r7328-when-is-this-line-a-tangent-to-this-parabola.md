---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7328
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7328
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7328
  old_site_id: Q3020
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
  - code: 1.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Tangency of line to parabola via discriminant = 0.
      rationale: 'Canonical UGM title: “When is this line a tangent to this parabola?”; exam provenance:
        UCLES 1977 Q13(b); cross-mapped primary pick of record (UGM-Enrichment perSpecPoint primaryPick,
        syllabai-resources#55)'
      validation_status: SUGGESTED
      primaryPick: true
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1977 Q13(b)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/bVZ7uYtj/width/600/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When is this line a tangent to this parabola?

## Question

Calculate the value of \(k\) for which the line \(y = 2x + k\) is a tangent to the curve \(y = 2x^2 - 4x + 5\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/bVZ7uYtj/width/600/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/bVZ7uYtj)

The blue parabola here is \(y = 2x^2 - 4x + 5\), while the red line is \(y = 2x + k\).

## Solution

Note that \(y=2x+k\) is a line, while \(y=2x^2 -4x + 5\) is a parabola, so they meet in \(0\), \(1\) or \(2\) points.

If \(y=2x+k\) is a tangent to \(y=2x^2 -4x + 5\), then they meet in exactly one point, so when we solve the two equations simultaneously, we must get just one solution.

Let’s do this: putting \(2x+k = 2x^2-4x+5\) gives \(2x^2 -6x + 5-k = 0\).

For this quadratic equation to have exactly one root, the [discriminant](https://undergroundmathematics.org/glossary/discriminant) \(b^2-4ac\) must be zero. So \((-6)^2-4\times 2(5-k) = 0\), which gives \(k = \dfrac{1}{2}\).
