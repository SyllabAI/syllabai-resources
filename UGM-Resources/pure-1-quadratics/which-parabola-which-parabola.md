---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/which-parabola
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
  ugm_id: which-parabola
  station: quadratics
  station_title: Quadratics
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 6672
  old_site_id: E1_RT7_2
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
      evidence: Identify the parabola from graph features (NRICH).
      rationale: 'Canonical UGM title: “Which parabola?”; exam provenance: NRICH'
      validation_status: SUGGESTED
    title: carry out the process of completing the square for a quadratic polynomial ax + bx + c and use
      y a completed square form
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: NRICH
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis1thick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis2thick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis3thick.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis4thick.png
  kind: figure
import_note: question well prepended (was not among crawled sections)
---

# Which parabola?

> Excerpt: This problem is good for thinking about how the equation of a parabola relates to its appearance on the graph, and for starting to think about transformations of graphs.

## Question

This would also like sourceUrl http://nrich.maths.org/791

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png`] (image not included in the text import; path of record).

Given that two of the parabolas have the equations \[y = x^2 - 12x + 27\] and \[y = -x^2 + 12x - 36,\] can you find the equations of the other parabolas?

---

You might like to design your own pattern of parabolas, perhaps using [Desmos](https://www.desmos.com/calculator). You could start from [our design](https://www.desmos.com/calculator/vc5ngspqdx), if you like.

## Problem

This would also like sourceUrl http://nrich.maths.org/791

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png`] (image not included in the text import; path of record).

Given that two of the parabolas have the equations \[y = x^2 - 12x + 27\] and \[y = -x^2 + 12x - 36,\] can you find the equations of the other parabolas?

---

You might like to design your own pattern of parabolas, perhaps using [Desmos](https://www.desmos.com/calculator). You could start from [our design](https://www.desmos.com/calculator/vc5ngspqdx), if you like.

## Suggestion

Can you factorise these equations? What does this tell you about the graphs of these two functions?

What is the difference between the graphs of \(y=x^2+bx+c\) and y=\(-x^2-bx-c\)? Can you spot any graphs in the picture that might satisfy such a relation?

If you know that a graph has equation \(y=ax^2+bx+c\), what is the equation of its reflection in the \(y\)-axis?

## Solution

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledthick.png`] (image not included in the text import; path of record).

Given that two of the parabolas have the equations \[y=x^2-12x+27\] and \[y=-x^2+12x-36,\] can you find the equations of the other parabolas?

Here is a summary of the equations that you should have found.

| Parabola | Equation |
| --- | --- |
| A | \(y=x^2+12x+36\) |
| B | \(y=-x^2-12x-27\) |
| C | \(y=-x^2-12x-36\) |
| D | \(y=x^2+12x+27\) |
| E | \(y=-x^2+9\) |
| F | \(y=x^2\) |
| G | \(y=-x^2\) |
| H | \(y=x^2-9\) |
| I | \(y=-x^2+12x-27\) |
| J | \(y=x^2-12x+36\) |
| K | \(y=-x^2+12x-36\) |
| L | \(y=x^2-12x+27\) |

Here is a way to find the equations of the parabolas.

We will first look at the equation

\[\begin{equation} y=x^2-12x+27=(x-3)(x-9).\label{eq:1} \end{equation}\]

The graph of this equation will intersect the \(x\)-axis at \(x=3\) and \(x=9\). The are only two parabolas in the picture that intersect the positive \(x\)-axis twice: parabolas I and L, which are symmetrical about the \(x\)-axis, which corresponds to the map \(y\mapsto -y\). Since the coefficient of \(x^2\) is positive, we know the parabola must look like \(\cup\) rather than \(\cap\), so the equation \(\eqref{eq:1}\) must correspond to parabola L. But we now also know what the equation of parabola I is: \(y=-x^2+12x-27\).

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis1thick.png`] (image not included in the text import; path of record).

*We can now mark some points on the \(x\)-axis*

We can also see from the picture that parabola B corresponds to parabola I reflected in they \(y\)-axis. This reflection corresponds to the map \(x\mapsto -x\), so we can see that the equation of parabola B is \(y=-(-x)^2+12(-x)-27=-x^2-12x-27\). Similarly, parabola D is parabola L reflected in the \(y\)-axis, so parabola D has the equation \(y=x^2+12x+27\).

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis2thick.png`] (image not included in the text import; path of record).

*We can now mark more points on the \(x\)-axis*

Now let’s think about the equation

\[\begin{equation} y=-x^2-12x-36=-(x+6)^2.\label{eq:2} \end{equation}\]

The parabola corresponding to \(\eqref{eq:2}\) has a double root at \(x=-6\), so the top of the parabola must just touch the \(x\)-axis (the coefficient of \(x^2\) is \(-1\) so it looks like \(\cap\) rather than \(\cup\)). We know where \((-3,0)\) and \((-9,0)\) are on the picture because we know that parabola B and D intersect the \(x\)-axis at these points. Parabola A and C both have a double root at \(x=-6\), so from their shapes we see that equation \(\eqref{eq:2}\) must be the equation of parabola C, and that the equation of parabola A, its reflection in the \(x\)-axis, must have the equation \(y=(x+6)^2=x^2+12x+36\).

We can see from the picture that parabolas J and K are parabolas A and C reflected in the \(y\)-axis respectively. So parabola J must have the equation corresponding to parabola A under the transformation \(x\mapsto -x\), which is \(y=x^2-12x+36\). Similarly, parabola K has the equation \(y=-x^2+12x-36\).

> [figure: 12 parabolas — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis3thick.png`] (image not included in the text import; path of record).

*We can now mark all of the important points on the \(x\)-axis*

We still need to find the equations of parabolas E, F, G and H. From the picture, we see that E and H both intersect the \(x\)-axis at the points \((3,0)\) and \((-3,0)\), so they look like \(y=\pm\alpha(x+3)(x-3)\), for some \(\alpha>0\). From their shapes, we see that parabola E has equation \(y=-\alpha(x+3)(x-3)=-\alpha x^2+9\alpha\) and parabola H has equation \(y=\alpha x^2-9\alpha\). To find the value of \(\alpha\), we compare to parabola I, which has the same height. The peak of parabola I is in the middle of its two roots, since a parabola is symmetrical. So the height of parabola I, and therefore of E, is \(9\). Since the peak of parabola E is at \(x=0\), we require that \(9=0^2\alpha+9\alpha\), and so \(\alpha=1\).

> [figure:  — `https://undergroundmathematics.org/quadratics/which-parabola/images/parabolalabelledaxis4thick.png`] (image not included in the text import; path of record).

*We now know the heights of the parabolas*

Finally, parabolas F and G both have a double root at \(x=0\), which means they have the form \(y=\pm \alpha x^2\), for some \(\alpha>0\). Again looking at their shapes, we see that parabola F has equation \(y=\alpha x^2\) and parabola G has equation \(y=-\alpha x^2\). To find the value of \(\alpha\), notice that parabola F is a translation of parabola J along the \(x\)-axis by \(6\) in the negative direction. So the equation of parabola F must be that of parabola J evaluated at \((x+6)\) instead of \(x\), and so is \(y=(x+6)^2-12(x+6)+36=x^2+12x+36-12x-72+36=x^2\). So \(\alpha=1\).
