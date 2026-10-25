---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/trig-gradient-match
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/building-blocks
resource_identity:
  ugm_id: trig-gradient-match
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 8321
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: 'pairing trig functions with their gradient functions incl. the scaled composites - builds
        d/dx(sin x) = cos x and the chain-rule cases graphically; excerpt-capture disclosure: no solution
        well of record, matched on the provider task statement'
      rationale: 'Canonical UGM title: Trig gradient match'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Trig gradient match

> Excerpt: Students are asked to pair up graphs of certain trig functions and their gradient functions and sketch some missing graphs.  The graphs are not labelled, so students will have to focus on the shapes of the graphs.

## Problem

Take a look at these graphs. The numbered graphs show the gradient functions of ones with letters, but some are missing…

- Try to pair up a function with its gradient function. Which features of the graphs will you use to justify your reasoning?

- If a graph can’t be paired up with anything, try to sketch a graph that would complete its pair.

The graphs are available as [cards](https://undergroundmathematics.org/calculus-trig-log/trig-gradient-match/components/cards.pdf) to cut out and sort, including some blank cards for the missing graphs.

Once you have sorted the graphs into pairs of functions \(f(x)\) and \(f'(x)\) and sketched any missing graphs, try to sketch the graphs of the second derivatives.

Also try to sketch graphs of functions whose derivative is \(f(x).\) What do you notice?

## Suggestion

Take a look at these [graphs](https://undergroundmathematics.org/calculus-trig-log/trig-gradient-match/). The numbered graphs show the gradient functions of ones with letters, but some are missing…

- Try to pair up a function with its gradient function. Which features of the graphs will you use to justify your reasoning?

- If a graph can’t be paired up with anything, try to sketch a graph that would complete its pair.

One way to approach this is to group the graphs with letters into different “families” and match these groups with gradient function graphs with appropriate features. Can you explain why this approach could lead to the following groups?

Why these groups?

- Graphs A and E are both continuous and their gradients appear to vary smoothly.

- Graphs D and F have turning points so their gradient function graphs must meet the \(x\)-axis. Or we could say that \(D\) and \(F\) have both positive and negative gradients.

- Graphs B and C have no turning points. Their gradients are either always positive or always negative.

Now think about how to pair these cards up within the groups.

Ideas for matching and sketching

Aligning cards vertically can help with spotting related features. What feature of a gradient function will need to be aligned with

- … a stationary point?

- … an asymptote?

What feature will a function exhibit if the gradient function

- … is above the horizontal axis?

- … cuts the horizontal axis?

- … has a stationary point?

## Things you might have noticed

Take a look at these [graphs](https://undergroundmathematics.org/calculus-trig-log/trig-gradient-match/). The numbered graphs show the gradient functions of ones with letters, but some are missing…

- Try to pair up a function with its gradient function. Which features of the graphs will you use to justify your reasoning?

- If a graph can’t be paired up with anything, try to sketch a graph that would complete its pair.

Following on from the groups of cards in the [Suggestion](https://undergroundmathematics.org/calculus-trig-log/trig-gradient-match/suggestion), I now need to consider how these cards can be paired up.

**First group**

I notice graph A has a stationary point at \(x=0\) and its gradient is positive before and negative afterwards. Graph E has stationary points to the right and left of the origin.

- Does graph 5 match A or E? How can I tell?

- How could I use transformations to sketch the missing graph?

- How could I use features to sketch the missing graph?

First group graph pairs

**Second group**

Graph D has an asymptote along the vertical axis whereas graph F has a turning point at \(x=0\).

- What do I look for in the gradient function for each of these features?

- What transformation can I use to sketch the missing graph easily?

Second group graph pairs

**Third group**

I can use the asymptotes to help find a first pair, and I can also think about transformations, since some of these graphs are transformations of each other.  <cm-cards include-source="components/colouredcards-content" display="B|1" markers="B,1" card-padding="5" card-spacing="5 0" card-width="180" />

- What feature can I use to choose between graphs 3 and 4 to match with graph C?

- How can I use transformations again to sketch the missing graph?

- Can I be certain what the missing graph should look like?

Third group graph pairs

Since graph 3 is a vertical reflection of graph 4, my missing graph could be a vertical reflection of graph C, but it could also show the gradient function of any vertical translation of this, so I sketch a family of curves.

(The black graph is the one that was obtained by reflecting graph C in the \(y\)-axis.)

I could continue to base my reasoning on transformations. Alternatively, I could consider the behaviour of the graphs. How does this affect the second derivative, \(f''(x)\), or the antiderivatives (the family of functions whose derivatives are \(f(x)\))? I’ll take the second approach and consider a few examples.

I’ll say graph A is \(y=f(x)\), so graph 5 is \(y=f'(x)\) and I can consider the gradient of graph 5 to help me sketch \(y=f''(x).\) The gradient of graph 5 is negative as it passes through the origin, so \(f''(0)\) must be negative. Graph 5 has alternating maxima and minima with sections of either positive or negative gradient in between, so \(y=f''(x)\) crosses the \(x\)-axis whenever graph 5 has a stationary point and alternates between being positive and negative. I notice that the \(x\)-intercepts of \(y=f''(x)\) correspond to [points of inflection](https://undergroundmathematics.org/glossary/point-of-inflection) in graph A.

This type of thinking also helps me to sketch the antiderivatives of the function shown in graph A. What will these functions look like when graph A crosses the \(x\)-axis? What about when graph 5 crosses the \(x\)-axis?

In graphs F and 2, I notice that graph 2 also alternates between positive and negative gradient, but this time there are no stationary points. How must my approach to sketching the second derivative of graph F differ from how I sketched the second derivative of graph A? How does this reflect the differences between graphs F and A or graphs 2 and 5?

If I apply the same type of thinking to graphs B and 1, how could I use the other graphs to confirm my ideas?

Thinking about transformations helps with the pair A and 5. Graph 5 is a reflection in the horizontal axis of graph E and I have already sketched the gradient function of E. Therefore the second derivative of A is actually a reflection of A in the horizontal axis. I also noticed that the gradient function of E was in fact A, so I already know what the antiderivatives of graph A will look like. Graph 2 isn't a transformation of a graph whose derivative I have a sketch for, so I'll need to think about what its behaviour tells me about its gradient function, which will be the second derivative of the function on card F. The gradient of the section passing through the origin is always positive, but is least steep when $x=0$, so I would expect its gradient function to have a minimum at a point with coordinates $(0,k)$ for some $k>0.$ The graph gets steeper and steeper as it approaches its asymptotes, so I expect the graph of the gradient function also to have these asymptotes. The section of the graph to the right of this central section behaves in a similar way, but always has negative gradient, so I'd expect the gradient function of this section to have a local maximum. Then I can use the periodicity of the graph to complete my sketch. This type of thinking also helps me to sketch the antiderivatives of the function shown in graph F - each section of this graph is either positive or negative, and if its Thinking about my second group I could try to sketch what is happening from the gradient function using features and symmetry, but in matching my final group of graphs I have already seen what the gradient functions of shapes like this look like. I will therefore look at how individual sections of B and C behaved and alternate them in my sketch. In this way I seem to have redrawn something similar to the original function graphs F and D.

My sketches of some second derivatives look very similar to the original functions. How could I tell if these are actually the same?
