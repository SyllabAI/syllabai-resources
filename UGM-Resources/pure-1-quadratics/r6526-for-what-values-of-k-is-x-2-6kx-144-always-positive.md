---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6526
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6526
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6526
  old_site_id: Q1061
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
      evidence: 'Always-positive quadratic: discriminant + completing the square.'
      rationale: 'Canonical UGM title: “For what values of $k$ is $x^2 + 6kx +144$ always positive?”;
        exam provenance: UCLES 1981 Q12(b)'
      validation_status: SUGGESTED
    title: find the discriminant of a quadratic polynomial ax + bx + c and use the discriminant ‘repeated
      root’ is included.
  - code: 1.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'Always-positive quadratic: discriminant + completing the square.'
      rationale: 'Canonical UGM title: “For what values of $k$ is $x^2 + 6kx +144$ always positive?”;
        exam provenance: UCLES 1981 Q12(b)'
      validation_status: SUGGESTED
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1981 Q12(b)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/zSZ9EfDk/width/700/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# For what values of $k$ is $x^2 + 6kx +144$ always positive?

## Question

Write \(x^2 + 6kx +144\) in the form \((x+p)^2+q\) and thus obtain expressions for \(p\) and \(q\) in terms of \(k\). Hence find the range of values for \(k^2\) such that \(x^2+6kx+144\) is positive for all values of \(x\), and deduce the corresponding range of values of \(k\).

## Suggestion

Write \(x^2 + 6kx +144\) in the form \((x+p)^2+q\) and thus obtain expressions for \(p\) and \(q\) in terms of \(k\).

Hence find the range of values for \(k^2\) such that \(x^2+6kx+144\) is positive for all values of \(x\), and deduce the corresponding range of values for \(k\).

When drawing the graph of \(y = (x+p)^2+q\), what do \(p\) and \(q\) represent?

How does knowing \(p\) and \(q\) help us to determine whether the quadratic function is always positive?

Here is the graph of \(y = x^2+6kx+144\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/zSZ9EfDk/width/700/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/zSZ9EfDk)

## Solution

We have been asked to [complete the square](https://undergroundmathematics.org/glossary/completing-the-square).

In this case, we have

\[\begin{align*} x^2 + 6kx +144 &= x^2 + 6kx +9k^2-9k^2 +144\\ &= (x+3k)^2-9k^2 +144.\\ \end{align*}\]

Comparing this expression with \((x+p)^2+q\), we find

\[\begin{align*} p&=3k \\ \text{and}\quad q&=-9k^2+144. \end{align*}\]

Hence find the range of values for \(k^2\) such that \(x^2+6kx+144\) is positive for all values of \(x\), and deduce the corresponding range of values for \(k\).

The smallest value a quadratic of the form \((x+p)^2+q\) takes is \(q\), since \((x+p)^2\ge0\) for all \(p\). This minimum happens when \(x=-p\), which is when \((x+p)^2=0\).

Thus for the quadratic to be positive everywhere, we require \(q>0\). Using the expression for \(q\) obtained above, we have \[-9k^2+144>0\] which rearranges to \[k^2<16.\] Hence \(-4 < k < 4\), which can be also be written as \(\big |k\big |<4\).
