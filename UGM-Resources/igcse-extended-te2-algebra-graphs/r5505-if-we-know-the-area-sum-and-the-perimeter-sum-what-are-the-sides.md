---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r5505
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r5505
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5505
  old_site_id: Q1073
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
      evidence: Given the area-sum and perimeter-sum, find the sides — construct equations from geometric
        conditions; the E2.5.1 register verbatim.
      rationale: 'Canonical UGM title: “If we know the area-sum and the perimeter-sum, what are the sides?”;
        exam provenance: UCLES O level Mathematics Alternative A Algebra, QP 411/3, 1960, Q9

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
  exam_reference: 'UCLES O level Mathematics Alternative A Algebra, QP 411/3, 1960, Q9

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-algebra/r5505/images/img-5505.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/kRFKSEFV/width/600/height/300/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# If we know the area-sum and the perimeter-sum, what are the sides?

## Question

There are four separate square enclosures, three of side \(\quantity{x}{yd.}\) and one of side \(\quantity{y}{yd.}\) The sum of the areas of the enclosures is \(\quantity{147}{sq. yd.}\) and the sum of their perimeters is \(\quantity{96}{yd.}\) Obtain two equations containing \(x\) and \(y\) and solve them.

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/kRFKSEFV/width/600/height/300/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/kRFKSEFV)

The three green squares here each have side length \(x\).

The side of the blue square is chosen to make the sum of the perimeters of the four squares \(96\).

Can you find the \(x\) value the question requires?

When is the area smallest?

Why is the width of the green and blue squares together constant?

## Solution

The area of a square of side \(x\) is \(x^2\), so the sum of the areas of the enclosures is \(3x^2 + y^2\).

Hence, our first equation is \(3x^2 + y^2 = 147\).

Now a square of side \(x\) has perimeter \(4x\), and so the sum of the perimeter of the enclosures is \((3 \times 4x) + 4y\).

Our second equation therefore is \(12x + 4y = 96\).

In order to solve these, we’ll now use the second equation to express \(y\) in terms of \(x\). Rearranging, we get

\[\begin{align*} 3x + y &= 24 \\ \implies y &= 24 - 3x. \end{align*}\]

If we substitute this into the area equation above, we have

\[\begin{align*} 3x^2 + (24 - 3x)^2 &= 147 \\ \implies 3x^2 + 576 - 144x + 9x^2 &= 147 \\ \implies 12x^2 - 144x + 429 &= 0\\ \implies 4x^2-48x+143=0\\ \implies (2x-13)(2x-11)=0\\ \implies x = 5.5, 6.5. \end{align*}\]

Alternatively we could use the [quadratic equation formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) to solve here, to get the two solutions for \(x\) given by

So we again get \(x_1 = 6.5\) and \(x_2 = 5.5\).

\[\begin{align*} x & = \frac{144 \pm \sqrt{144^2 - 4 \times 12 \times 429}}{24}\\ & = \frac{144 \pm \sqrt{144}}{24}\\ & = \frac{144 \pm 12}{24}. \end{align*}\]

Now by using the perimeter equation above, we find

\[\begin{align*} x_1 = 6.5, \quad \rightarrow \quad y_1 &= 24 - 3 \times 6.5 \\ &= 4.5 \\ x_2 = 5.5, \quad \rightarrow \quad y_2 &= 24 - 3 \times 5.5 \\ &= 7.5. \end{align*}\]

Thus there are two solutions, namely \(x_1 = 6.5\) yd., \(y_1 = 4.5\) yd. and \(x_2 = 5.5\) yd., \(y_2 = 7.5\) yd.

How ‘likely’ is this, that we find two viable solutions for \((x,y)\) here?

If we sketch the graphs of \(3x^2 + y^2 = 147\) (an ellipse) and \(3x + y = 24\) (a straight line), we are asking the line to cut the ellipse in two places, both in the first quadrant.

> [figure: the ellipse and the line intersecting twice in the first quadrant — `https://undergroundmathematics.org/thinking-about-algebra/r5505/images/img-5505.png`] (image not included in the text import; path of record).

If the perimeter was \(100\) yd. instead of \(96\) yd. do we still get two solutions?
