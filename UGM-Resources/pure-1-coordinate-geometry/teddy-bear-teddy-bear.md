---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/teddy-bear
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: teddy-bear
  station: circles
  station_title: Circles
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 6355
  old_site_id: G2_RT7_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Match 13 circles to equations in both forms ((x+10)^2+(y+15)^2=4pi^2, x^2+y^2+66x-78y+2110=0) — centre/radius fluency, standard and expanded. Pattern exemplar.'
      rationale: 'Canonical UGM title: “Teddy bear”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
---

# Teddy bear

> Excerpt: Students are invited to match some circles on a graph with their equations. The circles are drawn to scale, but the axes are not labelled. For detailed notes on this resource, please see [Teddy bear - teacher support](/circles/teddy-bear-teacher-support).

## Problem

We have thought of 13 circles. 11 of them are drawn accurately on the above graph. Here are the equations of 11 of the original 13 circles.

1. \((x+10)^2 +(y+15)^2 = 4\pi^2\)

---

1. \(x^2 + y^2 = 324\)

---

1. \((x+22)^2 + (y+36)^2 = 411\)

---

1. \((x+3\pi)^2 + (y-15)^2 = 1990\)

---

1. \(\bigl(x-21\sqrt{2}\bigr)^2 + \bigl(y-24\sqrt{3}\bigr)^2 = 131\sqrt{5}\)

---

1. \(x^2 + y^2 + 66x - 78y + 2110 = 0\)

---

1. \(x^2 + y^2 = 9\)

---

1. \((x-23)^2 +(y+42)^2 = 200\)

---

1. \(x^2 + y^2 = 81\)

---

1. \((x-18)^2 + (y+36)^2 = 1990\)

---

1. \(x^2 + y^2 - 18x + 45 = 0\)

Can you match them up, find the two missing equations and draw the two missing circles on the graph?

## Solution

Here’s a summary of the matching between equations and circles.

| Circle | Equation |
|---|---|
| \(a\) | 6 |
| \(b\) | 5 |
| \(c\) | 4 |
| \(d\) | \((x+22)^2 + (y-18)^2 = 169\) |
| \(e\) | \((x-9)^2 + (y-18)^2 = 81\) |
| \(f\) | 2 |
| \(g\) | 9 |
| \(h\) | 11 |
| \(i\) | 1 |
| \(j\) | 3 |
| \(k\) | 8 |
| \(l\) | 7 |
| \(m\) | 10 |

Here’s a description of one way in which we could have found that matching.

We begin by writing equations 6 and 11 in completed square form: equation 6 becomes \((x+33)^2+(y-39)^2=500\) and equation 11 becomes \((x-9)^2+y^2=36\).

Equation 11 therefore describes a circle with centre on the \(x\)-axis, and we might notice that circle \(h\) is such a circle. So we hope that these two match up. (In fact, one can show that we would end up with more than 13 circles if equation 11 and circle \(h\) didn’t match up.)

As circle \(g\) passes through the centre of circle \(h\), equation 9 belongs to circle \(g\).

Moreover, circle \(f\) corresponds to equation 2 and we can draw the circle corresponding to equation 7. It is circle \(l\) in the diagram below.

From the information we worked out so far, we deduce that circle \(e\) has centre \((9,18)\) and radius \(9\). So its equation is \((x-9)^2 + (y-18)^2 = 81\) (which isn’t on the given list of equations).

By further considering the centres of the circles described by the remaining equations (e.g. by looking at which quadrant they lie in), we can match up circle \(a\) and equation 6, circle \(b\) and equation 5, circle \(c\) and equation 4, circle \(i\) and equation 1, circle \(j\) and equation 3, and circle \(k\) and equation 8.

To find the equation of circle \(d\), we first work out its centre \((-22,18)\), e.g. by considering the centres of circles \(e\) and \(j\). Moreover, to obtain its radius we note that the point on circle \(d\) which has the largest \(x\)-value and the point on circle \(g\) which has the smallest \(x\)-value form a straight line parallel to the \(y\)-axis. Thus, the radius is \(13\) and the equation of circle \(d\) is \((x+22)^2 + (y-18)^2 = 169\).

Finally, to plot the circle with equation 10, we first construct its centre by using circle \(j\) and circle \(f\). Then, we could use the bisector method to find the centre of circle \(c\) and take its radius to construct circle \(m\).

The following diagram shows all 13 circles with their correct labels.
