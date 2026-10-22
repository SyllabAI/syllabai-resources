---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6804
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6804
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6804
  old_site_id: Q4
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Tangents from a point to a circle — sits with P1 coordinate geometry (1.3); tangency via
        discriminant is the shared skill.
      rationale: 'Canonical UGM title: “Can we find the tangents to a circle from a point?”; exam provenance:
        UCLES 1964 Q2'
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
  exam_reference: UCLES 1964 Q2
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/GmAARe8H/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the tangents to a circle from a point?

## Question

Prove that the line \(y=mx+c\) will touch the circle \(x^2+y^2=25\) if \(c^2=25(1+m^2).\)

Hence or otherwise find the equations of the two tangents to this circle from the point \((2,11)\).

## Suggestion

Prove that the line \(y=mx+c\) will touch the circle \(x^2+y^2=25\) if \(c^2=25(1+m^2)\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/GmAARe8H/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/GmAARe8H)

The blue circle here is \(x^2 + y^2 = 25,\) while the green line is \(y = mx + c\).

When a line and a circle touch, what can we say about their equations?

What else can we write down about \(c\) and \(m\) if we know a point on the line?

## Solution

For the line to touch the circle there must be exactly one point of intersection between them—the line must be a tangent to the circle.

To find the points of intersection of the line and circle we need to solve their equations for \(x\) and \(y\).

Substituting

\(y = mx + c\)

into

\(x^2 + y^2 = 25\)

gives

\[\begin{align*} &x^2 + (mx+c)^2 = 25\\ \iff\quad& x^2 + m^2x^2 + 2mcx + c^2 = 25\\ \iff\quad& (1+m^2)x^2 + 2mcx + c^2 - 25 = 0 \end{align*}\]

This is a quadratic equation in \(x\), and so to have exactly one point of intersection, we require the [discriminant](https://undergroundmathematics.org/glossary/discriminant) to be zero. The discriminant here is \[(2mc)^2 - 4 (1+m^2) (c^2-25)= 4 (25 (1+m^2) - c^2),\] where we have expanded, rearranged and taken out a factor of \(4\).

So if \(c^2 = 25(1+m^2)\) then the discriminant is \(0\). Therefore the line and circle intersect at exactly one point, and so the line touches the circle.

We can, in fact, prove more than this; we also have that the line touches the circle if \(c^2=25(1+m^2)\).

We were asked to prove that **if** \(c^2=25(1+m^2)\), **then** the line touches the circle; in fact, we see that \(c^2=25(1+m^2)\) **if and only if** the line touches the circle.

We can save time by using the first part of the question to solve the next part.

We want to find straight lines of the form \(y=mx+c\) which go through the point \((2,11)\) and are tangent to the circle.

Substituting the coordinates \((2,11)\) into \(y=mx+c\) gives \(11 = 2m + c\), and from the first part we must have \(c^2 = 25(1+m^2)\).

Now we have simultaneous equations for \(m\) and \(c\) which we can solve.

Substituting for \(c\) gives \[(11-2m)^2 = 25(1+m^2),\] which rearranges to give \[21m^2 + 44m - 96 = 0.\] This can be factorised to give \[(3m-4) (7m+24) = 0.\] So \(m = \dfrac{4}{3}\) or \(m = - \dfrac{24}{7}\).

If \(m = \dfrac{4}{3}\), then \(c = 11 - 2\left(\dfrac{4}{3}\right) = \dfrac{25}{3}\), and if \(m = - \dfrac{24}{7}\) then \(c = 11 - 2 \left(-\dfrac{24}{7}\right) = \dfrac{125}{7}\).

So the two tangents are \[y= \dfrac{4}{3} x + \dfrac{25}{3}\] and \[y= - \dfrac{24}{7} x + \dfrac{125}{7}.\]

We could write these equations in the form \(ay+bx+c = 0\), giving \[3y-4x-25=0 \] and \[7y+24x-125=0.\]
