---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/name-that-graph
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: name-that-graph
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 8067
  old_site_id: E1_RT7_6
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
  - code: 1.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Match parabola equations to graphs (vertex form, translations).
      rationale: 'Canonical UGM title: “Name that graph”; cross-mapped primary pick of record (UGM-Enrichment
        perSpecPoint primaryPick, syllabai-resources#55)'
      validation_status: SUGGESTED
      primaryPick: true
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/name-that-graph/images/graph1.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/name-that-graph/images/graph2.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/name-that-graph/images/graph2.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/name-that-graph/images/graph3.png
  kind: figure
---

# Name that graph

> Excerpt: Students are encouraged to think about the different forms of a quadratic equation and how they are related to a quadratic graph.

## Problem

> [figure: Plot of a parabola. — `https://undergroundmathematics.org/quadratics/name-that-graph/images/graph1.png`] (image not included in the text import; path of record).

Can you find an equation for this parabola?

- In how many ways can you choose to show this equation?
- Which format did you initially choose and why?

What is the same and what is different about your approach to finding an equation of the two parabolas below, compared to the example above?

> [figure: Plot of two parabolas. — `https://undergroundmathematics.org/quadratics/name-that-graph/images/graph2.png`] (image not included in the text import; path of record).

- What properties do the three parabolas have in common?
- Is there an approach to finding the equation that works for all three of these parabolas, and indeed for any parabola you could be given?
- Which approach to finding the equation was the most efficient? Is it the same approach for each example?

## Solutions

Given that the diagram shows a parabola, I know that I am looking for a quadratic equation.

There are three forms in which I could choose to write a quadratic equation:

\[\begin{equation} y=ax^2 + bx + c\label{eq:1} \end{equation}\]

\[\begin{equation} y=a(x-d)(x-e)\label{eq:2} \end{equation}\]

\[\begin{equation} y=a(x-f)^2+g\label{eq:3} \end{equation}\]

In order to write the equation in form \(\eqref{eq:1}\) I need to know three pieces of information (because there are three unknowns). Any three different coordinate points on the parabola would work as this would enable me to write three equations in \(a, b, c\) which I could then solve simultaneously.

To write the equation directly in form \(\eqref{eq:2}\) (fully factorised form) I also need to know three pieces of information. This time however I specifically need to know the location of the \(x\)-intercepts (assuming that there are any), which will give me the values of \(d\) and \(e\). Given another point on the parabola I can then identify the value of \(a\).

Form \(\eqref{eq:3}\) (completed square form) will require a different three pieces of information. The location of the minimum or maximum point (the vertex) of the parabola, \((f, g)\), plus one additional point on the parabola to identify the value of \(a\).

I can now consider the specific case of the red parabola presented above. Attempting to identify the equation of this parabola in each of the three forms described will allow me to compare efficiency.

If I want to find the equation in the form \(y=ax^2 + bx + c,\) then I will need to make use of three pairs of coordinates on the parabola. If I substitute each pair in turn into the general form of the equation then I will be able to solve these simultaneously to find the values of \(a, b\) and \(c\).

Let’s say I substitute each of \((0, -3)\), \((1, -4)\) and \((3, 0)\) into the equation so that I get the three equations:

Substituting equation the value of \(c\) from \(\eqref{eq:4}\) into \(\eqref{eq:5}\) and \(\eqref{eq:6}\) I get

and

which simplify to give

If I now eliminate \(b\) by doing \(\eqref{eq:10} - 3 \times \eqref{eq:9}\) I get \[6 = 6a\] or \[a = 1.\] Substituting this back into any one of the equations I find that \(b= -2\).

So the equation of the parabola is \[y=x^2 -2x -3.\]

It’s worth noting that this is a fairly laborious process! Perhaps a different approach will be more efficient.

\[\begin{equation} -3=c\label{eq:4} \end{equation}\]

\[\begin{equation} -4 = a + b + c\label{eq:5} \end{equation}\]

\[\begin{equation} 0= 9a + 3b + c\label{eq:6} \end{equation}\]

\[\begin{equation} -4 = a + b - 3\label{eq:7} \end{equation}\]

\[\begin{equation} 0 = 9a + 3b - 3 \label{eq:8} \end{equation}\]

\[\begin{equation} -1 = a + b \label{eq:9} \end{equation}\]

\[\begin{equation} 3 = 9a + 3b\label{eq:10} \end{equation}\]

**Form (1)**

Instead, I could have tried to find the equation in factorised form, \(y=a(x-d)(x-e)\), where \(d\) and \(e\) are the \(x\)-intercepts of the parabola.

I can read these from the graph as \(x=-1\) and \(x=3\) and so I can write down the equation of the parabola \[y=a(x+1)(x-3).\]

Using a third point on the curve, say \((0, -3)\), I can now find that \(a=1\) and hence the equation of the parabola is \[y=(x+1)(x-3).\]

I could expand this equation to check that it agrees with my previous answer: \[y=x^2 + x - 3x - 3,\] which simplifies to \[y=x^2-2x-3\] as expected.

**Form (2)**

Finally, I could have tried to find the equation in completed square form, \(y=a(x-f)^2 + g\).

From the graph I can see that the minium point as has coordinates \((1, -4)\) so the completed square form of the equation will be \[y=a(x-1)^2 - 4.\]

Using an additional point on the parabola, say \((0, -3)\) again, I find that \(a=1\) and so the equation of the parabola is \[y=(x-1)^2 -4.\]

Once again, I could expand this to check that it agrees with the equations found above via other methods: \[y = x^2 - 2x + 1 - 4\] which simplifies to \[y=x^2 - 2x - 3\] as expected.

**Form (3)**

For this particular parabola form \(\eqref{eq:2}\), factorised form, is probably the most efficient form to aim for. The \(x\)-intercepts are clear from the graph and there are several other integer coordinates visible that can be used to identify the scaling factor, \(a\).

What is the same and what is different about your approach to finding the equation of the two parabolas below, compared to the example above?

> [figure: Plot of two parabolas. — `https://undergroundmathematics.org/quadratics/name-that-graph/images/graph2.png`] (image not included in the text import; path of record).

First I will consider the blue parabola.

As before I can take three pairs of coordinates located on the parabola and substitute them into the general equation of the form \(y=ax^2 + bx + c\), solving simultaneously to find \(a, b\) and \(c\).

Let’s say I choose \((0, 8)\) \((4, 8)\), and \((2, -4)\), giving me three equations: \[8 = c\] \[8 = 16a + 4b + c\] \[-4 = 4a + 2b + c.\]

Solving simultaneously I obtain the quadratic equation \[y=3x^2 - 12x + 8.\]

**Form (1)**

I cannot accurately read the positions of the \(x\)-intercepts from the graph. This means that I cannot write this equation directly in factorised form.

Perhaps it is worth noting however, that whilst I cannot directly write the equation in factorised form, I can use an extension of this approach to identify the equation in form \(\eqref{eq:1}\).

I know the location of the two points on the parabola on the line \(y=8\). If I call the blue parabola \(y=f(x)\) and consider the translation \(y=f(x) - 8\) I can write down \[f(x) - 8 = a(x - 0)(x - 4).\] Rearranging and simplifying I find that \[f(x) = ax(x - 4) + 8 = ax^2 - 4ax + 8.\] Using a third point on either \(y=f(x)\) or \(y=f(x)-8\), I can establish that \(a=3\) and hence that the equation of the blue parabola is \[y=3x^2 - 12x + 8.\]

(I could similarly have used the location of the two points on the line \(y=-1\) to get the same result.)

> [figure: Plot of two parabolas f of x and f of x minus 8. — `https://undergroundmathematics.org/quadratics/name-that-graph/images/graph3.png`] (image not included in the text import; path of record).

**Form (2)**

Finding the equation in completed square form is fairly straight forward as I can read the coordinates of the minimum point from the graph as \((2, -4)\).

I now know the equation is of the form \[y=a(x-2)^2 - 4.\]

Using an additional point on the parabola, say \((0,8)\), I find that \(a=3\) and so the equation is \[y=3(x-2)^2 - 4.\]

Expanding this equation to check that this agrees with previous result I get \[y = 3x^2 - 12x + 8\] as expected.

**Form (3)**

For this parabola form \(\eqref{eq:3}\), completed square form, is the more efficient form. The coordinates of the minimum point can be read directly from the graph and an integer \(y\)-intercept makes for a more straight-forward calculation to confirm the scaling factor, \(a\). It is worth noting that the method of translating the parabola discussed in form \(\eqref{eq:2}\) is also an efficient approach here.

Now I will consider the purple parabola.

Taking the first approach as before I select three coordinates: \((0, -6)\), \((-3, 0)\) and \((-6, -6)\) to substitute into the general form of the equation. This gives the three equations \[-6 = c\] \[0 = 9a - 3b + c\] \[-6 = 36a - 6b + c.\] Solving simultaneously I find the equation of the parabola to be \[y=-\frac{2}{3}x^2 - 4x - 6.\]

**Form (1)**

I can see from the graph that this parabola touches the \(x\)-axis at \(x=-3\). This means that I can write the equation in the form \[y=a(x+3)^2.\] Using the point \((0, -6)\) I find that \(a=-\frac{2}{3}\) and so the equation is \[y=-\frac{2}{3}(x+3)^2.\]

Expanding this equation to check that it agrees with my previous answer I have \[y = -\frac{2}{3}x^2 - 4x - 6\] as expected.

**Form (2)**

From the graph I know that the maximum point on the parabola is at \((-3, 0)\). This means that the equation is of the form \[y=a(x+ 3)^2.\] I am now in exactly the same position as in form \(\eqref{eq:2}\) so using the same method I know that \(a=-\frac{2}{3}\) and the equation is \[y=-\frac{2}{3}(x+3)^2\] as before.

**Form (3)**

For this parabola form \(\eqref{eq:2}\) and form \(\eqref{eq:3}\) are equivalent and more efficient that the approach used in form \(\eqref{eq:1}\).

The three parabolas have the following properties in common:

- A vertical line of symmetry passing through the maximum or minimum point.
- Real roots - two of the parabolas cross the \(x\)-axis in two places, one touches the \(x\)-axis.
- A \(y\)-intercept that can be read from the diagram.
- At least three points that pass through integer coordinates that can be read from the graph.

In general all of the approaches discussed here rely on the ability to read information directly from the graph.

It is possible to use three simultaneous equations to find the equation of each parabola in form \(\eqref{eq:1}\). However, this is a laborious approach and consequently there are plenty of opportunities for “silly” arithmetical errors! This is certainly not the most efficient approach!

Form \(\eqref{eq:2}\), factorised form, is a very efficient approach for the red and purple parabolas. Although it may seem that this approach cannot work for the blue parabola (and indeed any parabola which doesn’t cross the \(x\)-axis), it may be possible to consider a translation of the parabola and to obtain the equation from there, as demonstrated in the approach to form \(\eqref{eq:2}\) (for the blue parabola). This is still more efficient than attempting the original approach for form \(\eqref{eq:1}\).

Form \(\eqref{eq:3}\), completed square form, is a very efficient approach for all three parabolas as the coordinates of the minimum or maximum point (the vertex) of each parabola can be read directly from the graph.
