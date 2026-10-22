---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9658
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9658
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9658
  old_site_id: Q3031
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
      evidence: No real solutions of a line-quadratic system = discriminant condition.
      rationale: 'Canonical UGM title: “When do these simultaneous equations have no real solutions?”;
        exam provenance: UCLES 1972 Q5(ii)'
      validation_status: SUGGESTED
    title: solve by substitution a pair of simultaneous e.g. equations of which one is linear and one
      is 2 quadratic
  - code: 1.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: No real solutions of a line-quadratic system = discriminant condition.
      rationale: 'Canonical UGM title: “When do these simultaneous equations have no real solutions?”;
        exam provenance: UCLES 1972 Q5(ii)'
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
  exam_reference: UCLES 1972 Q5(ii)
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/MWvUfdmy/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When do these simultaneous equations have no real solutions?

## Question

From the equations

\[\begin{align*} 3x + 2y &= 5, \\ 3x^2 + 2y^2 &= k \end{align*}\]

derive an equation relating \(x\) and \(k\). Show that there are no real values of \(x\) if \(k < 5\).

## Suggestion

When we think about the equation we found from the first part, what tells us about the number of real solutions it has?

## Solution

By rearranging the first equation, we have that

\[ y = \frac{5 - 3x}{2}. \]

By substituting this into the second equation, we see that

\[\begin{align*} 3x^2 + 2 \left( \frac{5 - 3x}{2} \right)^2 = k &\iff 3x^2 + \frac{(5 - 3x)^2}{2} = k \\ &\iff 3x^2 + \frac{25}{2} - 15x + \frac{9}{2} x^2 = k \\ &\iff \frac{15}{2} x^2 - 15x + \frac{25}{2} = k\\ &\iff 15x^2 - 30x + 25 = 2k. \end{align*}\]

Recall that for a quadratic equation \(ax^2 + bx + c = 0\), the [discriminant](https://undergroundmathematics.org/glossary/discriminant) is the expression \(b^2 - 4ac\), and that the quadratic has no real solutions if and only if \(\Delta < 0\).

The previous part of the question led to the quadratic equation \(15x^2-30x+25=2k\), which we can rewrite as \(15x^2-30x+(25-2k)=0\).

The associated discriminant is then

\[\begin{align*} (-30)^2 - 4 \times 15(25-2k) &= 900-60(25-2k)\\ &= -600+120k. \end{align*}\]

Therefore there are no real values of \(x\) if and only if \(-600+120k<0\), or \(120k<600\). Dividing by \(120\) gives us \(k<5\) as required.

Geometrically, the two equations represent a fixed straight line and an ellipse of size determined by \(k\). When the ellipse is small enough, the line will not intersect it, as can be seen in this interactivity.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/MWvUfdmy/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/MWvUfdmy)
