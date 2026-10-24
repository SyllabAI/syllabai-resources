---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/absolutely
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/investigation
- level/introducing
resource_identity:
  ugm_id: absolutely
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 7
  resource_type_label: Investigation
  level: Introducing
  ref: 7065
  old_site_id: "F1_RT1_1"
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
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "the modulus function scaffolded from its graph: the V-shape read as piecewise y=±x, 'this function is known as the modulus function. It is often written as |x|' — the canonical meaning-of-|x| task"
      rationale: "Canonical UGM title: Absolutely!"
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

# Absolutely!

> Excerpt: Students are shown the graph of the modulus function and asked what they can say about it. Questions about various features are suggested to support classroom discussion and prompt thinking about defining the modulus function as a piecewise linear function, transformations of the graph and applications of the function.

## Problem

Take a look at the graph below.

How would you describe it?

What questions might you ask yourself about this graph?

## Possible questions

Here are some questions that you might like to think about, if you have not already considered them.

- Is this a proper function?

- Does it matter that it has two different parts?

- Is there a formula for this?

- Are there other functions that look similar to this?

- How could I move the ‘corner’?

- How would a function like this occur?

- How could it be used?

- What could a function like this model?

## Things you might have noticed

- Is this a proper function?

- Does it matter that it has two different parts?

- Is there a formula for this?

Broadly speaking, a function gives a single output for each input. If you choose any \(x\)-value and use the graph to give you the corresponding \(y\)-value, you will get only one \(y\)-value, so this graph does represent a function.

It is important not to confuse the fact that every \(x\)-value has a single \(y\)-value with the fact that there may be more than one value of \(x\) that gives the same value of \(y\).

The two different parts of the graph don’t stop it being a function, but they do mean that we may need a different rule for different inputs. In the case of this graph, for positive values of \(x\) and \(0\) the graph is \(y=x,\) i.e. the output is equal to the input. For negative values of \(x,\) the graph is \(y=-x,\) i.e. the function multiplies the input by \(-1\). These rules cover all possibilities for input values, so our function is the rule \[f(x)=x \,\,\text{if } x \geq 0 \,\, \text{and } f(x)=-x \,\, \text{if } x<0.\] This is sometimes written more compactly as \(f(x) = \begin{cases}x & \text{if } x \geq 0 \\ -x & \text{if } x <0. \end{cases}\)

We could have attached \(f(0)=0\) to the left-hand section of the graph instead, but the convention is to include it in the right-hand section.

This function is known as the modulus function. It is often written as \(\vert x \vert\) and pronounced ‘mod \(x\)’. It is also called the absolute value function. It is worth noting that the name ‘modulus function’ is not universal and modulus has several different meanings in mathematics.

- Are there other functions that look similar to this?

- How could I move the ‘corner’?

What would the function \(f(x)=\vert x-2\vert\) look like? What about \(f(x)= \vert 3x\vert\)?

The sections of the original graph meet at \(x=0\), which is why there appears to be a ‘corner’ at \((0,0)\). What would happen if the sections met somewhere else? What similar functions would have sections meeting at \((3,0)\) or at \((-2,0)\)? What about sections meeting at \((3,5)\)?

The original function is symmetric about the \(y\)-axis. Can you define a function like this which doesn’t have a vertical line of symmetry?

The original function doesn’t output any negative values, but can you define a function like this that does output negative values?

- How would a function like this occur?

- How could it be used?

- What could a function like this model?

What is the difference between \(3\) and \(5\)? What about \(5\) and \(3\)? In some situations, you might not be interested in which number is bigger, but in the size of the gap between them. For example, if you are trying to solve an equation using trial and improvement, you might decide to stop once successive answers are closer together than \(0.01\).

If a car is driving at constant speed past you, the graph of the distance of the car from you, plotted against time, would look like the graph of a modulus function.

The amount of force in a stretched or compressed spring is proportional to how much the spring has been compressed or extended, i.e. the modulus of the difference between the original and new lengths.
