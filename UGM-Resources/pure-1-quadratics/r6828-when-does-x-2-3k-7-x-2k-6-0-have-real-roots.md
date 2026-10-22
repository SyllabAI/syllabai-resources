---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6828
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6828
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6828
  old_site_id: Q2023
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
      evidence: 'Real roots condition in k: discriminant >= 0.'
      rationale: 'Canonical UGM title: “When does $x^2+(3k-7)x+(2k+6)=0$ have real roots?”; exam provenance:
        UCLES 1958 Q2(ii)'
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
  exam_reference: UCLES 1958 Q2(ii)
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r6828/images/sketch2.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/Yz2c7Qqz/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When does $x^2+(3k-7)x+(2k+6)=0$ have real roots?

## Question

Find for what values of \(k\) the equation \[x^2+(3k-7)x+(2k+6)=0\] will have real roots in \(x\).

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Yz2c7Qqz/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Yz2c7Qqz)

The red curve here is \(y=x^2+(3k-7)x+(2k+6)=0\).

What tells us how many real roots a quadratic equation has?

What is the [discriminant](https://undergroundmathematics.org/glossary/discriminant) of a quadratic equation?

How does its value determine how many roots of a quadratic are real?

**Further suggestion…**

## Solution

A quadratic equation \(ax^2 + bx + c = 0\) has real roots if and only if its discriminant \(b^2-4ac \geq 0\).

Substituting in the quadratic’s coefficients, we find that for real roots here, we must have

\[\begin{align*} &&(3k-7)^2 -4(2k+6) &\geq 0 &&\quad\\ \iff\quad&& 9k^2 -42k + 49 -8k -24 &\geq 0 \\ \iff\quad&& 9k^2 -50k + 25 &\geq 0 \\ \iff\quad&& (9k-5)(k-5) &\geq 0. \end{align*}\]

The solutions of the quadratic equation \((9k-5)(k-5)=0\) are \(k=\frac{5}{9}\) and \(k=5\), so we can sketch the graph of \(y=(9k-5)(k-5)\):

> [figure: Graph showing the discriminant (9k minus 5) (k minus 5) against k. — `https://undergroundmathematics.org/quadratics/r6828/images/sketch2.png`] (image not included in the text import; path of record).

Therefore, the equation has real roots when \(y\ge0\), which is when \(k\geq 5\) or \(k \leq \dfrac{5}{9}\).
