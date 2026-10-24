---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7384
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7384
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7384
  old_site_id: "Q145"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "9^x - 3^{x+1} = k has 'one or more real solutions precisely when' the y=3^x quadratic y^2-3y-k=0 has a positive root - k >= -9/4"
      rationale: "Canonical UGM title: When does $9^x - 3^{x+1} = k$ have one or more real solutions?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2008, Q1H"
  task: T-UGM-IMPORT-10
---

# When does $9^x - 3^{x+1} = k$ have one or more real solutions?

## Question

The equation \[9^x - 3^{x+1} = k\] has one or more real solutions precisely when

1. \(k \geq -9/4\),

---

1. \(k > 0\),

---

1. \(k \leq -1\),

---

1. \(k \geq 5/8\).

## Suggestion

Maybe we can change variable so that we are working with an equation of a more familiar form? Would the substitution \(y = 3^x\) help?

## Solution

If we write \(y = 3^x\) and use the fact that \(9^x = (3^2)^x = (3^x)^2\), the equation can be written as \[y^2 -3y - k = 0.\]

This has solutions \[y = \frac{3 \pm \sqrt{9 + 4k}}{2}\] which are real when \(k \geq -9/4\). Since \(y = 3^x\), we need at least one of these solutions to be positive for \(x\) to be real, but the larger root is clearly always positive, so this is not a problem. Hence the answer is (a).

Interactive check

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/TDQ9jTyn/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/TDQ9jTyn)

The green curve is \(y=9^x - 3^{x+1} -k\).
