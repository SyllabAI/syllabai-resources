---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/parabella
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: parabella
  station: quadratics
  station_title: Quadratics
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 9637
  old_site_id: E1_RT12_3
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
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: NRICH
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/parabella/images/diagram.png
  kind: figure
---

# Parabella

> Excerpt: An opportunity for students to engage with problem solving using accessible algebra and geometry. This shows a beautiful result about parabolas.

## Problem

Take any two points \(A\) and \(B\) on the parabola \(y = x^2\).

Draw the line \(OC\) through the origin, parallel to \(AB\), cutting the parabola again at \(C\).

Let \(A\) have coordinates \((a,a^2)\), let \(B\) have coordinates \((b,b^2)\) and let \(C\) have coordinates \((c,c^2)\).

Prove that \(a+b = c\).

> [figure: A parabolla with points A, O, C, B on it. — `https://undergroundmathematics.org/quadratics/parabella/images/diagram.png`] (image not included in the text import; path of record).

*The parabella*

Imagine drawing another parallel line \(DE\), where \(D\) and \(E\) are two other points on the parabola. Extend the ideas of the previous result to prove that the midpoints of each of the three parallel lines lie on a straight line.

## Solution

We know that

\(A=(a,a^2)\),

\(B=(b,b^2)\),

\(C=(c,c^2)\).

We can calculate the gradient of a straight line between two points \((x_1,y_1)\) and \((x_2,y_2)\) as \(\frac{y_1-y_2}{x_1-x_2}\).

So the gradient of line \(AB\) is equal to \(\frac{a^2-b^2}{a-b}=a+b\).

Also, the gradient of line \(OC\) is equal to \(\frac{0-c^2}{0-c}=c\).

However, we know from the question that these two lines are parallel. Two lines are parallel if and only if they have the same gradient, which means that we must have \(a+b=c\).

---

Now, suppose that we have two points \(D=(d,d^2)\) and \(E=(e,e^2)\) on the parabola making another line parallel to \(OC\).

The gradient of line \(DE\) is equal to \(\frac{d^2-e^2}{d-e}=d+e\). As \(DE\) is parallel to \(OC\), we also have \(d+e=c\).

We can calculate the midpoint of a straight line between two points \((x_1,y_1)\) and \((x_2,y_2)\) as \((\frac{x_1+x_2}{2},\frac{y_1+y_2}{2})\).

So the midpoint of line \(OC\) is \[\left(\frac{0+c}{2},\frac{0+c^2}{2}\right) = \left(\frac{c}{2},\frac{c^2}{2}\right).\]

The midpoint of line \(AB\) is \[\left(\frac{a+b}{2},\frac{a^2+b^2}{2}\right) = \left(\frac{c}{2},\frac{a^2+b^2}{2}\right).\]

The midpoint of line \(DE\) is \[\left(\frac{d+e}{2},\frac{d^2+e^2}{2}\right) = \left(\frac{c}{2},\frac{d^2+e^2}{2}\right).\]

All three of these points have an \(x\)-coordinate of \(\frac{c}{2}\). This means that the line \(x=\frac{c}{2}\) passes through the midpoints of the lines \(OC\), \(AB\) and \(DE\).
