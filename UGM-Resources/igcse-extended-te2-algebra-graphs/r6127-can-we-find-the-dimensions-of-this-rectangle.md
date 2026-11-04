---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r6127
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r6127
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6127
  old_site_id: Q1037
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Find the dimensions of this rectangle — construct equations from area/perimeter clues;
        E2.5.1 register.
      rationale: 'Canonical UGM title: “Can we find the dimensions of this rectangle?”; exam provenance:
        UCLES AO level Additional Mathematics 1, QP 986/1, 1978, Q5

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'UCLES AO level Additional Mathematics 1, QP 986/1, 1978, Q5

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-algebra/r6127/images/rectangle.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/uusEWXaf/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the dimensions of this rectangle?

## Question

Find the dimensions of the rectangle whose perimeter is \(\quantity{36}{m}\) and which is such that the square of the length of the diagonal is \(\quantity{170}{m^2}\).

## Suggestion

Could we draw a helpful picture of the rectangle, with the two side lengths as \(x\) and \(y\)?

Can we use the information in the question to write down two equations in \(x\) and \(y\)?

## Solution

> [figure: Rectangle with side lengths x and y, and diagonal marked. — `https://undergroundmathematics.org/thinking-about-algebra/r6127/images/rectangle.png`] (image not included in the text import; path of record).

Let the sides of the rectangle be of length

\(x\)

and

\(y\)

metres. Then the question tells us that the perimeter of the rectangle is

\(\quantity{36}{m}\)

, so

\[\begin{equation}\label{eq:per} 2x+2y=36, \end{equation}\]

and that the square of the length of the diagonal is \(\quantity{170}{m^2}\), and so

\[\begin{equation}\label{eq:diag} x^2+y^2=170, \end{equation}\]

by Pythagoras’ theorem.

Rearranging equation \(\eqref{eq:per}\), we find that \(y=18-x\), and so equation \(\eqref{eq:diag}\) becomes \[x^2+(18-x)^2=170,\] which when we multiply out the brackets becomes \[x^2+324-36x+x^2=170,\] and so the quadratic we must solve is \[2x^2-36x+154=0.\] We can divide this equation through by two and solve \[x^2-18x+77=0.\] We can factorise the equation \[(x-7)(x-11)=0.\] If \(x=7\), we must have \(y=11\), and \(x=11\) gives us that \(y = 7\).

Therefore the dimensions of the rectangle are \(\quantity{7}{m}\) by \(\quantity{11}{m}\).

This applet might help you visualise how the square on the diagonal varies with \(x\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/uusEWXaf/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/uusEWXaf)

The red rectangle has perimeter \(36\).

When does the area of the square have its minimum value?

Notice how the two solutions for \(x\) and \(y\) are symmetrical.
