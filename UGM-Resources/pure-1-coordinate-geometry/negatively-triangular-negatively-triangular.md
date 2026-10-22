---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/negatively-triangular
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: negatively-triangular
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 8455
  old_site_id: G2_RT6_1
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
      evidence: 'Which three of four given lines enclose a triangle with negative coordinates — intersections from line forms; create-your-own extension.'
      rationale: 'Canonical UGM title: “Negatively triangular”'
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
- path: https://undergroundmathematics.org/geometry-of-equations/negatively-triangular/download/teacher-notes.pdf
  kind: printable
---

# Negatively triangular

> Excerpt: Given four straight line equations, which three enclose a triangle with negative coordinates? Students are asked to create a similar problem for themselves.

## Warm-up

Four straight lines have the following equations

1. \(3x+8y=59\)

---

1. \(x-2y=1\)

---

1. \(y-4x=3\)

---

1. \(3y+2x=-19\)

How many intersections do you expect?

**Some more points…**

Three of the four lines above will enclose a triangle where each point on the triangle has negative coordinates.

Which three lines?

Once you have answered these, you will be ready to move to the [main problem](https://undergroundmathematics.org/geometry-of-equations/negatively-triangular/main-problem).

## Warm-up solutions

**Approach 1**

These equations represent straight lines and can therefore be written in the form \(y=mx+c\).

The four equations can be written as:

\[\begin{align} y &=-\frac{3x}{8}-\frac{59}{8} \label{eq:a'}\tag{$a'$}\\ y &=\frac{x}{2}-\frac{1}{2} \label{eq:b'}\tag{$b'$} \\ y &=4x+3 \label{eq:c'}\tag{$c'$}\\ y &=-\frac{2x}{3}-{19}{3} \label{eq:d'}\tag{$d'$} \end{align}\]

This shows that none of the lines are parallel. Any two lines that are not parallel will intersect at some point. This means that each of the four lines will intersect with the other three.

Therefore there could be up to six intersections.

**Approach 2**

If two lines intersect then we can solve their equations simultaneously to find the coordinates of the intersection.

\[\begin{align} 3x+8y &=59 \label{eq:1}\tag{$a$}\\ x-2y &=1 \label{eq:2}\tag{$b$}\\ y-4x &=3 \label{eq:3}\tag{$c$}\\ 3y+2x &=-19 \label{eq:4}\tag{$d$} \end{align}\]

Subtracting three times equation \(\eqref{eq:2}\) from equation \(\eqref{eq:1}\) gives \(14y=56\), so \(y=4\). We can find \(x\) by substituting this into equation \(\eqref{eq:2}\): we have \(x-8=1\) and so \(x=9\). We can easily check that the point \((9,4)\) does indeed lie on both lines.

Therefore the coordinates of intersection between lines \(\eqref{eq:1}\) and \(\eqref{eq:2}\) are: \((4,9)\)

Repeating this process for each of the other five pairs yields the following solutions:

Lines \(\eqref{eq:1}\) and \(\eqref{eq:3}\) intersect at: \((1,7)\)

Lines \(\eqref{eq:1}\) and \(\eqref{eq:4}\) intersect at: \((-47,25)\)

Lines \(\eqref{eq:2}\) and \(\eqref{eq:3}\) intersect at: \((-1,-1)\)

Lines \(\eqref{eq:2}\) and \(\eqref{eq:4}\) intersect at: \((-5,-3)\)

Lines \(\eqref{eq:3}\) and \(\eqref{eq:4}\) intersect at: \((-2,-6)\)

Therefore there are six intersections.

This approach has the benefit of providing information useful in answering the next part of the problem.

**Some more points…**

Three of the four lines above will enclose a triangle where each point on the triangle has negative coordinates.

Which three lines?

From approach 2 above we can immediately see that the triangle must have vertices at: \((-1,-1)\), \((-5,-3)\), and \((-2,-6)\). These are the points of intersection between lines \(\eqref{eq:2}\), \(\eqref{eq:3}\) and \(\eqref{eq:4}\).

Therefore, the three lines that will enclose a triangle where each point on the triangle has negative coordinates are:

\(x-2y=1\)

\(y-4x=3\)

\(3y+2x=-19\)

## Main problem

You are going to consider how the warm-up problem was created. You will need to create a similar problem with a different set of four straight lines.

- How can you guarantee that your four lines will intersect to form a triangle where each point on the triangle has negative coordinates?

- How can you ensure that just one triangle is created with these conditions?

- How many approaches can you find to create a similar problem?

- Which of your approaches to this problem is the most effective?

Once you have completed this problem you may like to consider the questions below to extend your thinking:

Question 1

What conditions are there for four straight lines to enclose a square which has only negative coordinates for any point on that square?

Question 2

How do these conditions vary if we wish to enclose other quadrilaterals?

You might like to try a graphical approach to this problem, perhaps using [Desmos](https://www.desmos.com/calculator).

## Main solutions

How can you guarantee that your four lines will intersect to form a triangle where each point on the triangle has negative coordinates?

**Approach 1**

We know that all of the vertices of the triangle need to be located in the bottom left quadrant. If we specify the coordinates of the vertices then we can work out the equations of the lines from there.

We could select any three points in the bottom left quadrant. Let’s take \(A(-5,-2)\), \(B(-4,-9)\) and \(C(-0.4,-0.5)\) as an example. To find the equation of the straight line passing through two points we can use the general form of the equation \(y-y_{1}=m(x-x_{1})\).

Let’s start with coordinates \(A\) and \(B\). The gradient of the line is \(\frac{y-y_{1}}{x-x_{1}}=\frac{-2+9}{-5+4}=-7\).

Then the equation of the line is \(y+2=-7(x+5)\), or \(y+7x+37=0\).

Now if we repeat the process with coordinates \(B\) and \(C\) we get a gradient of \(\frac{-9+0.5}{-4+0.4}\), or \(\frac{85}{36}\). Then the equation of the line is \(y+9=\frac{85}{36}(x+4)\), or \(36y=85x+16\).

And finally we repeat the process with coordinates \(A\) and \(C\) giving a gradient of \(\frac{-2+0.5}{-5+0.4}=\frac{15}{46}\). Then the equation of the line is \(y+2=\frac{15}{46}(x+5)\) \(46y=15x-17\).

That gives us three equations that will intersect to enclose a triangle where each point on the triangle has negative coordinates. We now just need to specify a fourth equation that will not intersect to create another triangle in the bottom left quadrant. This could be done by choosing any line that is restricted to the other three quadrants. For example, \(y+x=5\).

**Approach 2**

We could solve this problem algebraically by considering the constraints on the values of the gradient, m and \(y\)-intercept, c.

If we start by assuming that we have two straight lines \[y=m_{1}x+c_{1}\] and \[y=m_{2}x+c_{2}.\] Then solving these two equations simultaneously gives us the coordinates of the point of intersection of the two lines as \[\left(\frac{c_{2}-c_{1}}{m_{1}-m_{2}},\frac{m_{2}c_{1}-m_{1}c_{2}}{m_{2}-m_{1}}\right).\]

Now, we want the coordinates to be negative. If we first consider the \(x\)-coordinate then we require that either \(c_{1}>c_{2}\) and \(m_{1}>m_{2}\), or \(c_{2}>c_{1}\) and \(m_{2}>m_{1}\).

Considering the \(y\)-coordinate we require that either \(m_{2}c_{1}>m_{1}c_{2}\) and \(m_{1}>m_{2}\), or \(m_{1}c_{2}>m_{2}c_{1}\).

Combining the conditions for both coordinates we have the following:

\(c_{1}>c_{2}\) and \(m_{1}>m_{2}\) and \(m_{2}c_{1}>m_{1}c_{2}\)

or

\(c_{2}>c_{1}\) and \(m_{2}>m_{1}\) and \(m_{1}c_{2}>m_{2}c_{1}\).

If we can select two lines that meet these conditions then they will intersect in the third quadrant.

We could then repeat the process to select a third line to intersect with the first two, also in the third quadrant.

Making use of a spreadsheet to select values of \(m\) and \(c\) that fit the conditions can be helpful.
