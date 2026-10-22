---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/near-miss
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: near-miss
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 7749
  old_site_id: E1_RT12_1
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
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'ill-conditioning read as nearly-parallel line geometry (KQ64).'
      rationale: 'Canonical UGM title: “Near miss”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/near-miss/download/teacher-notes.pdf
  kind: printable
---

# Near miss

> Excerpt: Students are invited to consider two very similar pairs of simultaneous linear equations and to explain why their solutions are so different.

## Problem

Solve the two pairs of simultaneous equations

\[\begin{align*} x + 0.99999y &= 2.99999 \\ 0.99999x + y &= 2.99998 \end{align*}\]

and

\[\begin{align*} x + 1.00001y &= 2.99999 \\ 0.99999x + y &= 2.99998. \end{align*}\]

Were you surprised by your answers?

Explain why the solutions are so different and yet the pairs of equations are nearly identical.

## Suggestion

Do you have any strategies for solving simultaneous equations? How will you decide which to use here?

Other than as strings of symbols, how else can we represent these equations? What does a solution to the equations correspond to in this language?

Notice that each equation specifies a line. A solution to the two equations corresponds to a point on both lines. What do the lines look like?

## Solution

Here are two possible approaches to solving the equations.

**Method 1**

For the first pair, subtract the second equation from the first to obtain \[0.00001x - 0.00001y = 0.00001.\] Dividing through by \(0.00001\) then gives \[x - y = 1.\] We can now add this to the second initial equation to eliminate \(y\); we get \[1.99999x = 3.99998.\] Now dividing through by \(1.99999\) gives \[x = 2,\] and so also \[y = 1.\]

For the second pair, we can again subtract the second equation from the first, which this time gives \[0.00001x + 0.00001y = 0.00001.\] Dividing through then gives \[x + y = 1.\] Subtracting the second initial equation from this (to eliminate \(y\)) gives \[0.00001x = -1.99998,\] and so \[x = - 199998,\] which in turn leads to \[y = 199999.\]

**Method 2**

For the first system, multiply the second equation by \(0.99999\) and subtract it from the first one. We see \[(1 - 0.99999^2)x = 2.99999 - 2.99998 \times 0.99999,\] which implies that \[x = \frac{2.99999 - 2.99998 \times 0.99999}{1 - 0.99999^2} = \frac{0.0000399998 }{0.0000199999} = 2,\] so finally substituting back into either equation we obtain \[x=2, \qquad y = 1.\]

For the second system, multiply the second equation by \(1.00001\) before subtracting it from the first. We get \[x = \frac{2.99999 - 2.99998 \times 1.00001}{1 - 1.00001\times 0.99999} = \frac{-0.0000199998}{0.0000000001} = -199998,\] and so \[y = 199999.\]

One helpful way to explain this is geometrically. We can view the problem of solving these equations as being the problem of finding the intersections of pairs of lines.

Rewriting these equations in the standard form

\(y=mx+c\)

we see the first pair of equations becomes

\[\begin{align*} y &= -\frac{1}{0.99999} x + \frac{2.99999}{0.99999} \\ & \approx \boxed{-1.00001 x} + 3.00002 \\ y &= \boxed{-0.99999 x} + 2.99998, \end{align*}\]

whilst the second gives

\[\begin{align*} y &= -\frac{1}{1.00001} x + \frac{2.99999}{1.00001} \\ & \approx \boxed{-0.9999900001 x} + 2.99996 \\ y &= \boxed{-0.99999 x} + 2.99998. \end{align*}\]

Both pairs of lines are very nearly parallel, but the second pair are much closer to being parallel—even though the difference in their offsets is only a little smaller than that for the first pair.

Because nearly parallel lines approach each other only very slowly, the pair which is much closer to being parallel takes much longer to meet when starting from the origin.

By only very slightly changing the slope (and intercept if we like) of the first line, the point at which the intersection lies can be moved enormous distances. In particular, because two distinct parallel lines never meet, we can make the intersection as far away as we like by slowly tuning the slopes to the same value!

Also, note that in both pairs of equations, the first line is steeper. That said, in the first pair the first line is higher at \(x=0\) whilst in the second pair, the second line is on top at \(x=0\). This explains the difference in the sign of the solutions \(x\).

A more algebraic approach might involve solving the system more generally. Here is such an argument.

Suppose we have

\[\begin{align*} a x + b y &= e \\ cx + d y &= f \end{align*}\]

as our system of equations. Then focusing on \(x\), we find (assuming \(d \neq 0\)) \[\left(a - \frac{b}{d} c\right) x = e - \frac{b}{d} f\] or (assuming \(ad-bc \neq 0\)) \[x = \frac{d e - b f}{ad-bc}.\] Now changing \(a\), \(b\), \(c\), \(d\), \(e\), \(f\) in the original equations a little corresponds to changing the numerator and denominator slightly. So now the question we’re interested in is simply whether \(x = \frac{p}{q}\) can change dramatically when we change \(p\) and \(q\) only a little—we are investigating the solutions to \[qx = p.\]

In fact, the solution \(x\) certainly can be very sensitive, because if \(q\) is very small then \(1/q\) is very large, and even small changes in \(q\) give rise to enormous ones in \(1/q\). For instance, we have \[\frac {1}{0.001} = 1000, \qquad \frac {1}{0.000001} = 1000000, \qquad \frac {1}{-0.001} = -1000.\]

Indeed, we can check \(ad-bc\) for the equations is very close to zero, which explains how sensitive the solution is to small changes of the parameters: we have \[ad-bc = 0.0000199999\] for the first pair, and \[ad-bc = 0.0000000001\] for the second pair.

As an aside, notice that \(q=0\) is the point around which things become very sensitive in solving \(qx=p\), which is exactly where the equation might have no solution (or infinitely many solutions).

Similarly, \(ad-bc = 0\) is exactly the point at which the original pair of equations have either no solution or infinitely many solutions. You might like to try to construct simple examples of equations with both zero and infinitely many solutions.

You might like to read [this short piece](https://undergroundmathematics.org/thinking-about-numbers/irrational-vs-rational-does-it-matter) about the butterfly effect.
