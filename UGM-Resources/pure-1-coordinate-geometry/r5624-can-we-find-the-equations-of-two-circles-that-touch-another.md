---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r5624
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r5624
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5624
  old_site_id: Q6
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
      evidence: 'Point inside x^2+y^2+4x-8y-80=0; two radius-5 circles through P touching it — centre/radius from the expanded form plus tangency conditions.'
      rationale: 'Canonical UGM title: “Can we find the equations of two circles that touch another?”; exam provenance: UCLES 1958 Q2'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1958 Q2
task: T-UGM-IMPORT-3
---

# Can we find the equations of two circles that touch another?

## Question

Show by calculation that the point \(P(-9,-3)\) lies inside the circle \[x^2+y^2+4x-8y-80=0.\]

Find the equations of the two circles which pass through \(P\), touch the given circle, and have radii of 5 units.

## Suggestion

Can we find the centre and the radius of the circle? How far is \(P\) from the centre of the circle?

We know these circles pass through \(P\) — can we find another point that these circles must go through?

## Solution

Let’s call this circle \(D\). Firstly, we rewrite the equation of \(D\) in the form \((x-a)^2+(y-b)^2=r^2\), so that we can easily work out its centre and radius.

We have

\[\begin{align*} &x^2+y^2+4x-8y-80=0\\ \iff\quad& (x+2)^2 - 4 + (y-4)^2-16 - 80 =0\\ \iff\quad& (x+2)^2 + (y-4)^2 = 100. \end{align*}\]

\(D\) has centre \((-2,4)\) and radius \(10\). This means that a point \(Q\) lies inside \(D\) if and only if the distance between \(Q\) and the point \((-2,4)\) is less than \(10\).

Let

\(d\)

be the distance between

\((-9,-3)\)

and

\((-2,4)\)

. Then

\[\begin{align*} d &= \sqrt{(-9-(-2))^2+(-3-4)^2}\\ &= \sqrt{(-7)^2+(-7)^2}\\ &= \sqrt{49+49}\\ &= \sqrt{98} \end{align*}\]

Now \(\sqrt{98} < 10\), so the distance between P and \((-2,4)\) is less than \(10\), and \(P\) lies inside \(D\).

The normal to the circle \(C_1\) at \(T_1\) is also normal to \(D\).

It must go through the centre of \(C_1\), but it must go through the centre of \(D\) too.

Now \(D\) has radius \(10\), and \(C_1\) has diameter \(10\), so we can deduce \(C_1\), and similarly \(C_2\), goes through \((-2,4)\), the centre of \(D\).

Now suppose one of the smaller circles \(C\) has centre \((a,b)\).

The circle \(C\) passes through \((-9,-3)\), so the distance between \((a,b)\) and \((-9,-3)\) is \(5\). So \[(a+9)^2 + (b+3)^2 = 25,\] by Pythagoras’ theorem.

But also \(C\) passes through \((-2,4)\), so the distance between \((a,b)\) and \((-2,4)\) is \(5\). So \[(a+2)^2 + (b-4)^2 = 25,\] by Pythagoras’ theorem.

So we have the two equations \[a^2+b^2+18a+6b+65=0\] and \[a^2+b^2+4a-8b-5=0.\]

Subtracting these gives \(14a+14b+70=0\), so \[70=-14a-14b\] and \[b=-5-a.\]

Substituting this into \((a+9)^2+(b+3)^2=25\) gives us \[a^2+18a+81+4+4a+a^2=25,\] that is, \[a^2+11a+30=0.\]

This quadratic factorises into \((a+5)(a+6)=0\), so \(a = -5\) or \(a=-6\).

Substituting these values into \(b=-5-a\), we get two possibilities for \((a,b)\), \((-5,0)\) and \((-6,1)\).

It’s easy to check that these points are viable ones for the centre of \(C\) (they do satisfy both equations).

So as the circles have radius \(5\), we get that the equations for these two circles are \[(x+5)^2+y^2=25,\] and \[(x+6)^2+(y-1)^2=25.\]
