---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/can-you-find-asymptote-edition
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
  ugm_id: can-you-find-asymptote-edition
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 5530
  old_site_id: F5_RT6_1
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: E2.11.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Given a graph, produce a function whose graph has those features — asymptote features
        front and centre; the E2.11.3 register verbatim.
      rationale: 'Canonical UGM title: “Can you find... asymptote edition”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/polynomials/can-you-find-asymptote-edition/images/obliqueasymptote.svg
  kind: figure
- path: https://undergroundmathematics.org/polynomials/can-you-find-asymptote-edition/images/subgraphs.png
  kind: figure
---

# Can you find... asymptote edition

> Excerpt: The graph of a function is provided. Students are asked to come up with a function that would have a graph like it by considering the important features of the graph.

## Problem

Can you find a function that gives the following graph?

> [figure: Curve with 3 components with 2 vertical and one oblique asymptote. — `https://undergroundmathematics.org/polynomials/can-you-find-asymptote-edition/images/obliqueasymptote.svg`] (image not included in the text import; path of record).

You can use [Desmos](https://www.desmos.com/calculator) to help you construct your function.

## Suggestion

Here are some questions you could ask about this graph.

- What are the main features of the graph? How can we represent these algebraically?
- Where does the curve cross the axes? How can we represent this information algebraically?
- What happens to the \(y\)-values when the \(x\)-values are large, either positive or negative?

## Things you might have tried

There are many ways to approach this problem. We suggest three possibilities below. These are complementary: we could use parts of each of them to reach a conclusion.

- What are the main features of the graph? How can we represent these algebraically?

If we take a step back and look at the graph from a distance, we see that it looks roughly like \(y=x\) when \(x\) is not near zero.

This gives us some hope that we might be able to draw this graph using a function based around polynomials.

Two main features of the graph are the asymptotes (two vertical and one oblique) and the axis crossings, including at the origin. A third key feature is that the function is odd: the graph has rotational symmetry about the origin.

As we have no scale on the graph, we have a certain amount of freedom to choose values for these, as long as they are reasonably consistent with what we see in the graph.

We often need to decide where to focus our attention and how to rework the problem: this is one of the choice points we face when working on a piece of mathematics. Our three approaches each start with the above observations, but take different routes from there.

#### Approach 1

In this approach, we will focus on the asymptotes.

We will take the asymptotes to be \(x=1\), \(x=-1\) and \(y=x\). (We could have used other numbers, such as \(y=2x\) or \(x=\pm3\), for example.)

Looking at the \(x=1\) asymptote, we see that the graph tends to \(+\infty\) on the left of it and to \(-\infty\) on its right. We can think through our repertoire of graphs related to polynomials: which graphs have a single asymptote with this sort of behaviour?

The graph of \(y=\dfrac{1}{x}\) comes to mind, though we will have to transform it to get it to the right place; something like \(y=\dfrac{1}{x-1}\), or perhaps it is \(y=-\dfrac{1}{x-1}\), should give us the asymptotes we want. We can do something similar near the asymptote \(x=-1\).

These two graphs both tend to \(0\) as \(x\) gets large, though, and we want our graph to tend to \(y=x\) for large \(x\). So maybe we also need to think about the graph of \(y=x\) itself?

Here are the graphs of these three functions:

> [figure: three graphs, the first showing y = minus 1 over x minus 1, the second showing y = minus one over x plus one and the third showing y = x — `https://undergroundmathematics.org/polynomials/can-you-find-asymptote-edition/images/subgraphs.png`] (image not included in the text import; path of record).

We now have three functions, each of which displays a piece of the behaviour we want from the whole graph. Now all that we need to do is to figure some way of putting these three functions together…

What happens if we add two of these functions together?

**Suggestion for the next step**

How can you convince yourself that your final answer does have the properties of the graph in the problem?

#### Approach 2

In this approach, we begin with our initial observation that once

\(x\)

is large (either positive or negative), the graph looks roughly like

\(y=x\)

. So we can try representing the function as

\[\begin{equation} \label{eq:xtimes} y=x\cdot\dfrac{\text{polynomial}}{\text{polynomial}}, \end{equation}\]

where the fraction part tends to \(1\) as \(x\) gets large. For this to happen, we need the two polynomials to have the same [degree](https://undergroundmathematics.org/glossary/degree-of-a-polynomial) and also the same [leading term](https://undergroundmathematics.org/glossary/leading-term).

The denominator has to be zero at the vertical asymptotes, which we will take to be \(x=1\) and \(x=-1\), so the polynomial \((x-1)(x+1)=x^2-1\) will do.

This means that the numerator would have to be a quadratic of the form \(x^2+\text{something}\) if this approach works.

Let us now reflect on another question asked in the suggestion:

- Where does the curve cross the axes? How can we represent this information algebraically?

What does this tell us about the quadratic in the numerator?

There are three \(x\)-axis intercepts, but we have already accounted for \(x=0\) in the overall equation \(\eqref{eq:xtimes}\).

**Suggestion**

What will the resulting equation of the graph be? Does this work when you plot it with graph-plotting software?

#### Approach 3

Similarly to the previous approach, we note that the graph looks like

\(y=x\)

when

\(x\)

is large. So we can write the equation of the graph as

\[\begin{equation} y=x+\dfrac{\text{polynomial}}{\text{polynomial}}, \end{equation}\]

where this time the fraction part tends to zero as \(x\) gets large. For this to happen, the degree of the numerator needs to be less than the degree of the denominator.

To get the asymptotes, we need the denominator to be zero at \(x=\pm1\) as before, so we can again take the denominator to be \(x^2-1\).

We could go two ways from here.

Firstly, we could add the \(x\) and the fraction parts together. This will give us \[y=\dfrac{x(x^2-1)+g(x)}{x^2-1}=\dfrac{x^3-x+g(x)}{x^2-1}\] for some polynomial \(g(x)\) of degree \(0\) or \(1\), so \(y\) will be a cubic divided by \(x^2-1\).

If we can work out the roots of this cubic, we can then write down the whole equation of the graph, and we should be done.

When the cubic equals zero, what can we say about \(y\)?

**Finding the roots of the cubic**

Alternatively, we can think about the fraction part in isolation. Its numerator must be a polynomial of degree \(0\) or \(1\), and the denominator is \(x^2-1\). Also, the whole function is odd, and the initial \(x\) is odd, so the fraction must also be odd.

The denominator is \(x^2-1\), which is an even function; what does this tell us about the numerator?

Does this give us enough information to find an equation for the graph?

---

- How do these approaches illuminate different aspects of the graph?
- Which aspects are most easily generalised?
