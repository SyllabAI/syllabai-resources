---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9614
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9614
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9614
  old_site_id: Q172
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
      evidence: 'y = kx meets y = (x-1)^2: intersection conditions (MAT).'
      rationale: 'Canonical UGM title: “When does $y=kx$ intersect the parabola $y=(x-1)^2$?”; exam provenance:
        Oxford (MAT) 2010 Q1A'
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
  exam_reference: Oxford (MAT) 2010 Q1A
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r9614/images/parabola172.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/Tu6DZjV2/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $y=kx$ intersect the parabola $y=(x-1)^2$?

## Question

The values of \(k\) for which the line \(y=kx\) intersects the parabola \(y=(x-1)^2\) are precisely

1. \(k\le0\),
2. \(k\ge-4\),
3. \(k\ge0 \hspace{2mm} \textrm{or} \hspace{2mm} k\le-4\),
4. \(-4\le k\le0\).

## Suggestion

The values of \(k\) for which the line \(y=kx\) intersects the parabola \(y=(x-1)^2\) are precisely…

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Tu6DZjV2/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Tu6DZjV2)

## Solution

The line \(y=kx\) intersects the parabola \(y=(x-1)^2\) when the equation

\[(x-1)^2 = kx\]

has real solutions.

Rearranging this equation gives

\[x^2 - (k+2)x + 1 =0,\]

which has [discriminant](https://undergroundmathematics.org/glossary/discriminant) \((k+2)^2-4\).

For the quadratic to have real solutions we need the discriminant to be non-negative, that is \((k+2)^2 \geq 4\), so we need either

\[\begin{align*} k+2 &\ge 2 \\ \textrm{or}\quad k+2 &\le -2, \end{align*}\]

i.e., \(k \ge 0\) or \(k \le -4\).

So the answer is (c).

Alternatively a sketch shows us what is happening.

> [figure: The parabola with tangents through the origin, gradients 0 and minus 4. — `https://undergroundmathematics.org/quadratics/r9614/images/parabola172.png`] (image not included in the text import; path of record).

It’s clear from the sketch that any line with positive gradient cuts the parabola, and that \(y = -0.01x\) certainly does not. So the only possible option is (c).
