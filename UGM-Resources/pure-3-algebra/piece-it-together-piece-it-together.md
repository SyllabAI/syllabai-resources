---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/piece-it-together
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/problem-requiring-decisions
- level/introducing
resource_identity:
  ugm_id: piece-it-together
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 6
  resource_type_label: Problem requiring decisions
  level: Introducing
  ref: 6041
  old_site_id: "F1_RT8_1"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "Graph 2 is built from y=2x and y=−2x with 'another way you could describe it' as the modulus function y=|2x|; Taking it further writes the four cards' equations incl. modulus forms"
      rationale: "Canonical UGM title: Piece it together"
      validation_status: SUGGESTED
    title: "understand the meaning of | x |, sketch the graph of y = | ax + b | and use relations such as"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# Piece it together

> Excerpt: Students are asked to describe four piecewise graphs for others to sketch. This may encourage informal discussion about the domains of different sections and help students to develop ideas of how we might write equations of piecewise functions. To take the task further, a set of equations that match to some of the graphs is provided.

## Problem

We often describe graphs using an equation or algebraic property, for example ‘this is the graph of \(y = x^2\)’, or ‘this is the graph of a quadratic’.

Underneath are some unusual looking graphs. Try to describe each graph in words. What features do you notice?

If you are in a group, one person should try and describe the graph to others, who try to draw it as accurately as possible. You may want to download the printable version so you can cut the cards out.

Graph 1

Graph 3

Graph 2

Graph 4

## Things you might have noticed

How did you describe the features of the graphs? Did you use mathematical language to help you?

Did you use shapes or equations to describe different sections?

If you did this in a group, were certain graphs drawn more accurately than others? If so, what was different about the way they were described?

Graph 1

This function is made up of sections of the form \(y=a\). Were equations used in the description?

What is the value of the function when \(x=1\)? How did you interpret the closed and open circles at the end of the sections? Where have you seen these used before?

Graph 2

The middle section of this function is interesting. It is made of sections of \(y=2x\) and \(y=−2x\), but can you think of another way you could describe it?

Graph 3

What happens at the points (3,0) and (8,0)? Which line would you define as them being part of?

Graph 4

There are two features here that have not occured in the other graphs. We have a non-linear section, and our function continues as \(x\) gets larger.

These are all graphs of piecewise functions. The whole function \(f(x)\) is made up of differing sections (or pieces).

Now you have described and sketched the functions, can you write their equations? The way they were described might help you with this. You can check your answers in the [taking it further](https://undergroundmathematics.org/thinking-about-functions/piece-it-together/taking-it-further) section.

## Taking it further

Now we have described the graphs in words, we want to see if we can describe the graphs using mathematical notation. How can we write the equations of these graphs?

You may wish to use the [equation cards](https://undergroundmathematics.org/thinking-about-functions/piece-it-together/components/equation-cards.pdf) to help you. Try to match the graphs to their equations. You may find that you need to draw some extra graphs, and write some more equations to complete the set.

**Graph 1**

Each section of the function is made up of equations in the form \(y=a\).

The open and closed circles should have reminded us of representing inequalities on a number line.

Equation

The equation of this graph was not given by any of the cards.

\[f(x) = \begin{cases}3 & \text{if } -1 ≤ x ≤ 1 \\ 1 & \text{if } 1 < x < 2 \\ -1 & \text{if } 2≤ x ≤ 4 \\ 2 & \text{if } 4 < x ≤ 7 \end{cases}\]

Notice that this function given for this graph is only defined for \(x\) between \(-1\) and \(7\), so the domain of the function is \(-1≤x≤7\). You can work more with domains of functions in [Domain and Range dominoes](https://undergroundmathematics.org/combining-functions/domain-and-range-dominoes).

You may have noticed that

\[f(x) = \begin{cases}3 & \text{if } x ≤ 1 \\ 1 & \text{if } 1 < x < 2 \\ -1 & \text{if } 2≤ x ≤ 4 \\ 2 & \text{if } 4 < x ≤ 7 \end{cases}\]

was similar, but required a different graph to be drawn.

What is the difference between the two graphs? What is the domain of this function?

**Graph 2**

The middle section of the graph might have reminded us of a modulus function, as it could be part of the graph of \(y=|2x|\).

But the modulus (or absolute value) function is a piecewise function itself, and can be written,

\[f(x) = \begin{cases}-2x & \text{if } x<0 \\ 2x & \text{if } x≥0 \end{cases}.\]

Equation

Two of the equations given in the cards are correct for this graph.

\[f(x) = \begin{cases}4 & \text{if } -3 ≤ x < -1 \\ -2x & \text{if } -1 ≤ x < 0 \\ 2x & \text{if } 0≤ x < 2 \\ 2 & \text{if } 2≤x< 6 \end{cases}\]

and

\[f(x) = \begin{cases}4 & \text{if } -3 ≤ x < -1 \\ -2x & \text{if } -1 ≤ x ≤ 0 \\ 2x & \text{if } 0 < x < 2 \\ 2 & \text{if } 2≤x< 6 \end{cases}\]

By convention we include \(x = 0\) in the right-hand part of the absolute value function, as shown in the first of the equations, but the graphs are the same for both of the functions given above.

**Graph 3**

Points \((3,0)\) and \((8,0)\) could be part of two different sections. Have we seen this before?

Equation

One equation is

\[f(x) = \begin{cases}2x & \text{if } 0 ≤ x < 1 \\ 0 & \text{if } 1 ≤ x < 3 \\ 2x-6 & \text{if } 3≤ x < 5 \\ 0 & \text{if } 5≤x< 8 \\ 2x-16 & \text{if } 8≤x≤10 \end{cases}\]

which wasn’t included in the equation cards.

The equation that does appear includes \(x = 3\) and \(x = 8\) as part of the flat sections, written as

\[f(x) = \begin{cases}2x & \text{if } 0 ≤ x < 1 \\ 0 & \text{if } 1 ≤ x ≤ 3 \\ 2x-6 & \text{if } 3< x < 5 \\ 0 & \text{if } 5≤x≤ 8 \\ 2x-16 & \text{if } 8<x≤10 \end{cases}\]

Are both of these correct?

The equation

\[f(x) = \begin{cases}2x & \text{if } 0 ≤ x < 1 \\ 0 & \text{if } 1 ≤ x ≤ 3 \\ 2x-6 & \text{if } 3 ≤ x < 5 \\ 0 & \text{if } 5≤x≤ 8 \\ 2x-16 & \text{if } 8≤x≤10 \end{cases}\]

also appears. What is the difference between this equation and the other two? Is this still a function?

**Graph 4**

Piecewise functions do not have to be linear, so having a quadratic as one of the sections is not a problem. Note that the final section continues as \(x\) increases and doesn’t have an end point.

Equation

The cards include the equation

\[f(x) = \begin{cases}1 & \text{if }-3≤x≤0 \\ x^2 & \text{if } 0≤x≤2 \\ 0 & \text{if } x≥2 \end{cases}\]

Why is this not correct? How would you write a correct function for graph \(4\)?

**Extra equations**

There are two cards left that we haven’t looked at yet. Can you draw the graphs for them? Are they both functions?

Graphs

\[f(x) = \begin{cases}2 & \text{if } -3 ≤ x < -1 \\ -2x & \text{if } -1 ≤ x < 0 \\ 2x & \text{if } 0≤ x < 2 \\ 4 & \text{if } x≥2 \end{cases}\]

This function is similar to a function given for graph \(2\), but what is different about this function compared to any of the others we have looked at here?

This also has the same property as the function above. There are no jumps between different pieces of the graph.

\[f(x) = \begin{cases}x^2 & \text{if } x ≥ 0 \\ -x^2 & \text{if } x < 0 \end{cases}\]

These two graphs are known as *continuous* piecewise functions, whereas the earlier functions are all *discontinuous* piecewise functions.
