---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8128
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8128
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8128
  old_site_id: Q2020
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
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Reciprocal simultaneous equations; hidden quadratic in 1/x and 1/y.
      rationale: 'Canonical UGM title: “Can we solve these simultaneous equations that involve reciprocals?”;
        exam provenance: UCLES 1975 Q2a'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1975 Q2a
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/yYkVZWhX/width/700/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we solve these simultaneous equations that involve reciprocals?

## Question

Find the values of

\(x\)

and

\(y\)

which satisfy the simultaneous equations

\[\begin{gather*} 2x + 3y = 1,\\ \frac{2}{x} + \frac{3}{y} = 1. \end{gather*}\]

## Suggestion

We have simultaneous equations here; what methods do we know for solving them in general? Which method is most appropriate in this case?

## Solution

Find the values of \(x\) and \(y\) which satisfy the simultaneous equations \[2x + 3y = 1,\] \[\frac{2}{x} + \frac{3}{y} = 1.\]

Substitution works well as a method here. Elimination won’t work, as subtracting (a multiple of) one equation from the other will not cancel any terms. (This is because the terms in the second equation are not multiples of \(x\) and \(y\) as in the first equation, but instead multiples of \(1/x\) and \(1/y\).)

From the first equation, \[y = \frac{1}{3} - \frac{2}{3} x.\] Multiplying the second equation by \(xy\) gives \[2y + 3x = xy,\] and substituting the value of \(y\) from above into this gives \[\frac{2}{3} - \frac{4}{3} x + 3x =x\left(\frac{1}{3} - \frac{2}{3} x\right).\] Therefore \[\frac{2}{3} - \frac{4}{3} x + 3x = \frac{1}{3} x -\frac{2}{3} x^2.\] Rearranging this gives the quadratic \[x^2 + 2x + 1 = 0.\] This can be rewritten as \((x + 1)^2 = 0,\) and therefore the only solution is \(x = -1\). Substituting this into the rearranged first equation gives \[y = \frac{1}{3} - \frac{2}{3} \times (-1) = 1.\]

We can check our answers by substituting \(x=-1\) and \(y=1\) into both equations; the first gives \(-2+3=1\) and the second also gives \(-2+3=1\), so our solution correctly solves the simultaneous equations.

We might be able to see this solution to the equations quickly by inspection (just by looking at them!).

This doesn’t, however, prove that we have found *all* possible solutions—we need to work a little harder to do this.

Notice too that we can get one equation from the other by replacing \(x\) with \(\dfrac{1}{x}\) and \(y\) with \(\dfrac{1}{y}\). Thus if \((x,y)\) is a solution, so is \(\left(\dfrac{1}{x}, \dfrac{1}{y}\right)\).

## Taking it further

What if the question had asked for the solution to the pair of equations

\[\begin{gather*} ax+by=1\\ \frac{a}{x}+ \frac{b}{y}=1 \end{gather*}\]

instead?

You could use the GeoGebra applet below to explore this. Here are some questions you might consider.

1. What curve does each equation generate?
2. How many solutions are there to this pair of simultaneous equations for different values of \(a\) and \(b\)?
3. Are the solutions always in the same quadrant?
4. If there are two solutions, can they lie on opposite parts of the curve?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/yYkVZWhX/width/700/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/yYkVZWhX)
