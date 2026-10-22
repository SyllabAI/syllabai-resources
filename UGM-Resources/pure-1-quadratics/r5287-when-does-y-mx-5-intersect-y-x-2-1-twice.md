---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r5287
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r5287
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5287
  old_site_id: Q2025
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
      evidence: 'y = mx - 5 cuts y = x^2 - 1 twice: discriminant in m.'
      rationale: 'Canonical UGM title: “When does $y=mx-5$ intersect $y=x^2-1$  twice?”; exam provenance:
        UCLES 1986 Q5(b)'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1986 Q5(b)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/mJq6WcZR/width/500/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $y=mx-5$ intersect $y=x^2-1$  twice?

## Question

Find the range of values of \(m\) for which the straight line \(y=mx-5\) intersects the curve \(y=x^2-1\) in two distinct points.

## Suggestion

What effect will changing \(m\) have on the line and the curve?

Use this applet to confirm your prediction and estimate an answer to the question.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/mJq6WcZR/width/500/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/mJq6WcZR)

## Solution

The line meets the curve where

\[ mx-5=x^2-1,\]

which rearranges to

\[x^2-mx+4 = 0.\]

This has two distinct roots if the discriminant \(m^2 -16\) is positive, that is if \(m < -4\) or \(m > 4\).

This can be written as \(\big|m\big|>4\), using the modulus function.
