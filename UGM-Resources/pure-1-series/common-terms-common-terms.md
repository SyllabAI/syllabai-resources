---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/common-terms
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: common-terms
  station: sequences
  station_title: Sequences
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 8700
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: construct an AP and a GP sharing u_2=6, u_4=54 — d=(54-6)/2=24 vs r^2=9; nth-term formulae
        of both progressions load-bearing
      rationale: 'Canonical UGM title: "Common terms"'
      validation_status: SUGGESTED
    title: recognise arithmetic and geometric progressions
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: construct an AP and a GP sharing u_2=6, u_4=54 — d=(54-6)/2=24 vs r^2=9; nth-term formulae
        of both progressions load-bearing
      rationale: 'Canonical UGM title: "Common terms"'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/common-terms/download/teacher-notes.pdf
  kind: printable
---

# Common terms

> Excerpt: A set of four related questions about geometric and arithmetic sequences which have matching terms. How many common terms can they have?

## Problem

1. Can you find an arithmetic and a geometric sequence which each have second and fourth terms \[u_2=6 \quad\text{and}\quad u_4=54 \text{ ?}\]

---

1. Can you find an arithmetic and a geometric sequence which each have \[u_2=-2, \quad u_3=4 \quad\text{and}\quad u_5=16 \text{ ?}\]

---

1. A geometric sequence \(G\) has first term \(8\) and common ratio \(-\frac{1}{2}\). Can you find an arithmetic sequence that has the same first term and two other terms the same as the corresponding terms of \(G\)?

---

1. Can you find an arithmetic and a geometric sequence that have four terms in common?

## Solution

Let’s start by looking for an arithmetic sequence. We are given the second and fourth terms so the common difference must be \[d=\frac{1}{2}(54-6) = 24\] and the first term is \(d\) less than the second, so \[a=6-24 = -18.\]

The arithmetic sequence is \((-18,6,30,54,78,...)\).

The geometric sequence has common ratio, \(r\), such that \[r^2=\frac{54}{6}=9 \quad\text{and so}\quad r=3.\] Its first term is \(6\div3\) and the sequence is \((2,6,18,54,162,...)\).

We can illustrate these two sequences as sets of points on a graph.

We have drawn in lines on which the points lie. Can you describe the shape of the two lines?

Notice that when solving for \(r\) above we could also have had \(r=-3\). What would our geometric sequence have looked like then?

Having thought about how arithmetic and geometric sequences behave, your first reaction might be that it is impossible to have three terms in common. Let’s have a look at the numbers anyway…

Comparing \(u_2\) and \(u_3\), the arithmetic sequence must have \(d=4-(-2)=6\) and this does fit with \(u_5\). The first term, \(a=u_2-d=-8\) and the arithmetic sequence is \((-8,-2,4,10,16,22,...)\).

For the geometric sequence, the common ratio must be \(r=\frac{u_3}{u_2}=-2\). As a check, \(\frac{u_5}{u_3}=4=r^2\) so this does work. The first term will be \(\frac{u_2}{r}=1\) and the sequence is \((1,-2,4,-8,16,-32,...)\).

The reason this works is the negative common ratio. This is an example of an *oscillating* sequence where the values of the terms go above and below a central value, in this case zero.

As before, we can illustrate these sequences with a graph.

The terms of the arithmetic sequence lie along a straight line again, but this time we have had to draw a *pair* of exponential curves for the geometric sequence – one for the positive terms and one for the negative.

This is similar to the previous example in that \(G\) has a negative common ratio and is therefore oscillating. Let’s write out the first few terms. \[G=\left(8,-4,2,-1,\frac{1}{2},-\frac{1}{4},...\right)\]

We want an arithmetic sequence that has \(a=8\) and that meets \(G\) again at two other terms. We could try matching some of the early terms and see what happens.

- Try matching the first two terms. Then we have \(d=-12\) and the sequence would go \((8,-4,-16,-28,...)\). This is clearly not going to meet \(G\) a third time.

- Try the first and third terms. \(2d=-6\) so \(d=-3\) and the sequence goes \((8,5,2,-1,-4,...)\). This is what we want because its first, third and fourth terms match with \(G\).

What does this solution have in common with the solution to (2)? How are they related?

We have found a sequence with the first, third and fourth terms in common with \(G\). Do you think that it is possible to find other arithmetic sequences with different sets of three terms in common with \(G\)?

The only way we can get four terms of a geometric sequence to be linearly spaced is if all its terms are identical. A geometric sequence with common ratio \(r=1\) and an arithmetic sequence with common difference \(d=0\) will have identical terms if their first terms are the same.

You might argue that the sequence \((1,1,1,1,1,...)\) is neither arithmetic nor geometric, but it is generally considered to be both, as it satisfies the definition of both.
