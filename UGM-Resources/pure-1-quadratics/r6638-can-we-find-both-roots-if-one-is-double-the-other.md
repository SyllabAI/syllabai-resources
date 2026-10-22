---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6638
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6638
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6638
  old_site_id: Q2013
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
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Roots related by an integer factor; factorise or use root relationships.
      rationale: 'Canonical UGM title: “Can we find both roots if one is double the other?”; exam provenance:
        UCLES 1985 Q1'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1985 Q1
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/C3PhbhcB/width/800/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find both roots if one is double the other?

## Question

Given that one of the values of \(x\) satisfying the quadratic equation \[x^2-(2a+1)x+(a^2+2)=0\] is twice the other, find \(a\).

## Suggestion

If we know the values of \(x\) that satisfy a quadratic equation, how can we use this to write the equation down?

Could we now compare our equation with the one given?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/C3PhbhcB/width/800/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/C3PhbhcB)

The green curve here is \(y=x^2-(2a+1)x+(a^2+2)\).

The blue line segment \(OP\) represents the smaller root, and the length \(OP'\) is double \(OP\).

## Solution

If \(x^2-(2a+1)x+a^2+2 = 0\) has one root double the other, then we can call the roots \(b\) and \(2b\), and write \[x^2-(2a+1)x+a^2+2 \equiv (x-b)(x-2b),\] as the quadratic on the right hand side has roots \(b\) and \(2b\).

Multiplying out we have \[x^2-(2a+1)x+a^2+2 \equiv x^2-3bx+2b^2.\]

Since this holds for all \(x\) (it is an identity), we can equate coefficients, giving us \(2a+1=3b\) and \(a^2 + 2 =2b^2\).

The first equation gives \(b = \dfrac{2a+1}{3}\), so we can substitute this into the second equation to obtain \[a^2 + 2 = 2\left(\dfrac{2a+1}{3}\right)^2.\]

Expanding the brackets and rearranging yields \(a^2 - 8a + 16 = 0\), or \((a-4)^2=0\), so \(a = 4\).

Checking this in the original equation: \(x^2-(2 \times 4+1)x+4^2+2 = (x-3)(x-6)\).
