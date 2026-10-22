---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r6234
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r6234
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6234
  old_site_id: Q8
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'AP=2BP locus derived to (x+7)^2+y^2=100 — distance-ratio locus in circle standard form; the folded 1.3.2 circle statement verbatim; STEP I depth is extension.'
      rationale: 'Canonical UGM title: “Can we show that this point moves on a circle?”; exam provenance: UCLES 2005 Q6'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2005 Q6
task: T-UGM-IMPORT-3
---

# Can we show that this point moves on a circle?

## Question

1. The point \(A\) has coordinates \((5,16)\) and the point \(B\) has coordinates \((-4,4)\). The variable point \(P\) has coordinates \((x,y)\) and moves on a path such that \(AP = 2BP\). Show that the Cartesian equation of the path of \(P\) is \[(x + 7)^2 + y^2 = 100.\]

---

1. The point \(C\) has coordinates \((a,0)\) and the point \(D\) has coordinates \((b,0)\). The variable point \(Q\) moves on a path such that \[QC = k \times QD,\] where \(k > 1\). Given that the path of \(Q\) is the same as the path of \(P\), show that \[\frac{a + 7}{b + 7} = \frac{a^2 + 51}{b^2 + 51}.\] Show further that \((a + 7)(b + 7) = 100\), in the case \(a \neq b\).

## Suggestion

In this applet, as you move \(P\), the two bars show the relative sizes of \(AP\) and \(2\times BP\). When are they equal?

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/x8nHWyAK)

Can we find the lengths \(AP\) and \(BP\) in terms of \(x\) and \(y\)?

… Given that the path of \(Q\) is the same as the path of \(P\)…

What do we know about the equations of the paths of \(P\) and \(Q\) in this case? Must they be the same?

## Solution

We are told that \(AP = 2BP\), which is the same as \((AP)^2 = 4(BP)^2\).

We use the formula for the distance \(d\) between two points \((x_1,y_1)\) and \((x_2,y_2)\), which is \(d^2 = (x_2-x_1)^2 + (y_2-y_1)^2\).

So the above expression becomes

\[\begin{align*} &&(x - 5)^2 + (y - 16)^2 &= 4((x + 4)^2 + (y - 4)^2)&&\quad\\ \iff\quad&& x^2 + y^2 - 10x - 32y + 281 &= 4x^2 + 4y^2 + 32x - 32y + 128\\ \iff\quad&& 3x^2 + 3y^2 + 42x - 153 &= 0\\ \iff\quad&& x^2 + y^2 + 14x - 51 &= 0. \end{align*}\]

Completing the square for

\(x\)

gives us

\[\begin{align*} &&(x + 7)^2 - 49 + y^2 - 51 &= 0&&\quad\\ \iff\quad&& (x + 7)^2 + y^2 &= 100. \end{align*}\]

This is the equation of a circle with centre \((-7,0)\) and radius \(10\).

Using the same approach as in part (i), with

\(Q=(x,y)\)

, we have

\[\begin{align*} &&(QC)^2 &= k^2 \times (QD)^2&&\quad\\ \iff\quad&& (x - a)^2 + y^2 &= k^2(x - b)^2 + k^2y^2\\ \iff\quad&& x^2 - 2ax + a^2 + y^2 &= k^2 x^2 - 2bk^2 x + b^2 k^2 + k^2 y^2\\ \iff\quad&& x^2(k^2 - 1) + y^2(k^2 - 1) &+ x(2a - 2b k^2) + (b^2 k^2 - a^2) = 0. \end{align*}\]

If this [locus](https://undergroundmathematics.org/glossary/locus) is the same as the locus of \(P\), which had equation \(x^2+y^2+14x-51=0\), then we must be able to rewrite our equation in this form. (Alternatively, we can say that the ratios of corresponding coefficients must be the same.)

Note that \(k^2 - 1 \neq 0\), so we can divide by it to make the coefficients of the \(x^2\) and \(y^2\) terms equal to \(1\).

Dividing by \(k^2-1\) gives the locus of \(Q\) as \[x^2 + y^2 + \frac{2a - 2b k^2}{k^2 - 1}x + \frac{b^2 k^2 - a^2}{k^2 - 1} = 0.\]

If this locus is the same as the locus of \(P\), then we must have \[\frac{2a - 2b k^2}{k^2 - 1} = 14\] and \[\frac{b^2 k^2 - a^2}{k^2 - 1} = -51.\]

The first of these gives \[2a - 2b k^2 = 14k^2 - 14,\] so \[k^2 = \frac{a + 7}{b + 7}.\]

Similarly, the second rearranges to

\[b^2 k^2 - a^2 = -51k^2 + 51,\] so \[k^2 = \frac{a^2 + 51}{b^2 + 51}.\]

Thus \[\frac{a + 7}{b + 7} = \frac{a^2 + 51}{b^2 + 51}.\]

Now we can rearrange this to

\[\begin{align*} &&(a + 7)(b^2 + 51) &= (b + 7)(a^2 + 51)&&\quad\\ \iff\quad&& ab^2 + 7b^2 + 51a &= a^2b + 7a^2 + 51b\\ \iff\quad&& ab^2 - a^2b &= 7(a^2 - b^2) + 51(b - a)\\ \iff\quad&& ab(b - a) &= 7(a - b)(a + b) + 51(b - a). \end{align*}\]

Since \(a \neq b\), we may divide by \(b-a\) to obtain \[ab = 51 - 7(a + b).\]

That is,

\[\begin{align*} &&ab + 7(a + b) &= 51&&\quad\\ \Longrightarrow \quad&& ab + 7a + 7b + 49 &= 51 + 49\\ \Longrightarrow \quad&& (a + 7)(b + 7) &= 100. \end{align*}\]
