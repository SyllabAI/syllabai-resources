---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/can-you-find-cubic-edition
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: can-you-find-cubic-edition
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 6487
  old_site_id: "F1_RT6_2a"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "cubics built from root/touch conditions: 'if α is a root, x−α is a factor' used across all five parts incl. repeated-root touch cases and y-intercept constraints"
      rationale: "Canonical UGM title: Can you find... cubic edition"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# Can you find... cubic edition

> Excerpt: Students are given constraints on where some cubic curves cross the axes and are asked to come up with possible equations for these curves.

## Problem

Can you find a cubic curve that…

1. … passes through the \(x\)-axis at \(x=1\) and \(x=-1\)?

---

1. … passes through the origin and touches the \(x\)-axis at \(x=-3\)?

---

1. … touches the \(x\)-axis at \(x=2\) and crosses the \(y\)-axis at \(12\)?

---

1. … crosses the \(y\)-axis at \(-6\) and has three integer roots?

---

1. … crosses the \(y\)-axis at \(y=5\) and touches the \(x\)-axis at \(x=1\)?

## Explore

In this section we have provided some tools to help you explore cubic curves. You should try to get as far as you can with the problem *before* using the tools. For example,

- If you have found examples of cubic curves that satisfy the criteria, can you generalise your examples?

- If you haven’t managed to come up with an equation for an example, have you tried to sketch one or more examples of cubic curves that satisfy the criteria?

- If you have been able to express the criteria in algebra, have you thought about what else you need to know to find an example that meets these criteria?

**Thinking about cubics**

- If you know \(f(x)\) is a cubic function of \(x\), what can you say algebraically about \(f(x)\)?

- What do you know geometrically about the graph of \(f(x)\)? Sketch some different shapes that can cubic graphs be.

- How many pieces of information do we need to define a cubic curve? In what form might this information be given?

**Exploring coefficients and graphs**

One of the standard ways to write a cubic in one variable is \(ax^3+bx^2+cx+d.\) Use the sliders for \(a,b,c\) and \(d\) to explore what happens when you vary the coefficients.

- What different shapes the can the graph of \(y=ax^3+bx^2+cx+d\) be?

- How many roots can a cubic have?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/EQ3MagEq/width/602/height/426/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/EQ3MagEq)

Things to think about

- What happens if \(a=0\)?

- Can you convince yourself that the graph of a cubic must cross the \(x\)-axis at least once?

- Which of the following shapes did you manage to make using the GeoGebra file?

You might like to have a look at [Curvy Cubics](https://undergroundmathematics.org/calculus-meets-functions/curvy-cubics) to explore different cubic curves further.

Any cubic can be written in the form \(ax^3+bx^2+cx+d,\) so we have four values that we can vary to give us different cubics. You may have noticed from the graphical work above, every cubic must have at least one root. If \(\alpha\) is a root, this means that \(x-\alpha\) is a factor of the cubic, so we can write our cubic as the product of \(x-\alpha\) and a quadratic, i.e. \(a(x-\alpha)(x^2+bx+c).\)

- Why does having a root \(\alpha\) mean that \((x-\alpha)\) is a factor of the cubic?

- What determines whether the cubic has any other roots?

Here is another GeoGebra file. You can use it to explore cubics written in a form with \(x-\alpha\) as a factor. Can you recreate the shape of the curves in the diagram above?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ysf5NKZy/width/602/height/437/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ysf5NKZy)

## Things you might have tried

We will describe geometric and algebraic approaches to this problem, but you should try to combine these, rather than selecting only one of the approaches.

The question tells us that the graph passes through the \(x\)-axis in two places. Try to sketch a few curves that satisfy these conditions.

Possible curves

What other possibilities are there?

How many times does the graph have to cross the \(x\)-axis?

An algebraic point of view

Algebraically, we know \(1\) and \(-1\) are roots, so we know the cubic must have factors \((x-1)\) and \((x+1).\) Therefore we need a cubic curve of the form \(y = a(x-1)(x+1)(x-b)\).

- What are the possibilities for the cubic?

- What is the relationship between features of \(y = a(x-1)(x+1)(x-b)\) and features of the sketch graphs?

- How would varying \(a\) or \(b\) affect the type of curve you get?

Try to sketch some cubic curves that *touch* the \(x\)-axis at \(x=-3.\) How much flexibility is there if the curve also has to pass through the origin?

Possible curves

Here are two sketches of cubic curves which fit the given criteria. Can you sketch any that are noticeably different from these?

An algebraic point of view

- If the equations of these curves are written in the form \(y=a(x-\alpha)(x^2+bx+c),\) what can \(\alpha\) be? What about \(a\), \(b\), or \(c\)?

- If instead the equations of these curves are written in the form \(y=a(x-\alpha)(x-\beta)(x-\gamma)\), what can you say?

Parts (a) and (b) both gave information about two roots, but how did the form of this information affect the range of curves that met the criteria?

Now that we’ve discussed a way of tackling a couple of these questions, we can ask “How is this question different from parts (a) and (b)?” This may help you to anticipate how much choice there will be for the cubic.

We know there is a repeated root at \(x=2\), so this is a bit like part (b). But in part (b), the \(y\)-intercept was \((0,0)\) whereas in this question the \(y\)-intercept is \((0,12)\). Which \(y\)-intercept do you think gives more flexibility?

In part \((a)\) we could choose where the third root was and whether the coefficient of \(x^3\) was positive or negative. Do we have more or less freedom here?

How would your answer to part (a) have been different if we had asked for a curve that "touched" the $x$-axis where, say, $x=1$?

Possible curves

What could the equations for these cubics be?

The distinction between "touching" the $x$-axis and "crossing" the $x$-axis at particular points may have affected your choice of cubics in this problem, but how different are these cubics?

How would your cubics for (c) be different if we had asked for a curve that *crosses* the \(x\)-axis at \(2\)?

- What does the \(y\)-intercept tell us about the roots of the equation?

- How much does having to have integer roots limit the possibilities?

Relationship between roots and the \(y\)-intercept

- A general equation of a cubic with roots \(\alpha\), \(\beta\) and \(\gamma\), is \(y = a (x-\alpha)(x-\beta)(x-\gamma)\). How does this give you information about the \(y\)-intercept?

- Could the cubic have a repeated root?

Possible cubics?

Which of the following satisfy the conditions in the question?

\[\begin{align*} y &= -3(x-1)(x+1)(x-2), \\ y &= 2(x+1)^2 (x-3), \\ y &= \frac{1}{2} (x-1)(x-2)(x+6) \end{align*}\]

\[\begin{align*} y &= \frac{1}{20} (x-8)(x-5)(x-3), \\ y &= \frac{2}{3} (x-1)(x-3)^2 \end{align*}\]

What are the roots in each case?

Once again, it is worth asking how this question is similar to or different from the previous parts. Do you think there will be lots of different types of cubic curve that satisfy these conditions or only a few different types?

Given that there are infinitely many possibilities for the cubics in these questions, it is helpful to talk about different ‘types’ of cubics, so that we can try to classify the possibilities. We can choose how to define the types, depending on what the question is asking. Sometimes it may be easier to see possible groups by looking at sketches and in other cases the algebra may be more helpful.

We might say that cubics are the same type if their sketch graphs look essentially the same, perhaps in terms of shape, number of roots, or whether the coefficient of \(x^3\) is positive or negative. For example, what’s the same and what’s different about these two cubics?

If you have been told something about some roots, you might also be interested in whether other roots exist, and if they do, are they less than, greater than, between, or the same as, the roots that you know about. These possibilities could all give you different types of cubics, but it would still be possible to write down or sketch examples of all the possible types.

Looking back, the distinction between “touching” the \(x\)-axis and “crossing” it at particular points was an important idea in this problem. But if we classify cubics based on the shape of their curve, this distinction may become less important. You can explore cubics with different shaped graphs at [Curvy cubics](https://undergroundmathematics.org/calculus-meets-functions/curvy-cubics).
