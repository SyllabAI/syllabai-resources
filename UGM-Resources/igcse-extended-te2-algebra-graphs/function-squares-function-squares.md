---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/function-squares
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: function-squares
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 7445
  old_site_id: F1_RT2_2
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.10.1a
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: The reciprocal-form cards (a/x^n family) ride the same library — the E2.10.1a synthetic-suffix
        fragment row (parse continuation of E2.10.1’s forms list) closes on the same substrate.
      rationale: 'Canonical UGM title: “Function squares”'
      validation_status: SUGGESTED
  - code: E2.11.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: The reciprocal-form cards (a/x^n family) ride the same library — the E2.10.1a synthetic-suffix
        fragment row (parse continuation of E2.10.1’s forms list) closes on the same substrate.
      rationale: 'Canonical UGM title: “Function squares”'
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
- path: https://undergroundmathematics.org/thinking-about-functions/function-squares/images/newcubesmall.png
  kind: figure
---

# Function squares

> Excerpt: Students can start to build familiarity with a basic library of functions and their properties using this resource. The functions are available as graphs or equations on cards.

## Warm-up

Can you arrange the functions \(f(x)=x^2\), \(f(x)=-1\), \(f(x)=x\) and \(f(x)=x^3\) in the table below so that they have the properties stated in each cell?

| Graph is straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph is straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |
| --- | --- |
| Graph is not straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph is not straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |

Can you explain why each function is in each cell?

Which other functions could fit in the cells of this table?

## Warm-up ideas

We need to think about what is meant by the two properties. They both describe properties of the graph of a function, but can be interpreted algebraically too. For example, the \(y\)-axis is a line of symmetry if the graph would look the same when reflected in the \(y\)- axis, but what would this mean for the input and output values of the function?

The only way of arranging the four given functions in the table is shown here.

| Graph is straight \(y\)-axis is a line of symmetry \[f(x)=1\] | Graph is straight \(y\)-axis is not a line of symmetry \[f(x)=x\] |
| --- | --- |
| Graph is not straight \(y\)-axis is a line of symmetry \[f(x)=x^2\] | Graph is not straight \(y\)-axis is not a line of symmetry \[f(x)=x^3\] |

There are several ways to explain why these functions have the properties in the corresponding row and column. Here are some suggestions.

- The graph of \(f(x)=-1\) has gradient \(0\), so it is parallel to the \(x\)-axis. Therefore it is straight and the \(y\)-axis is a line of symmetry. Another way to see the symmetry is to note that all input values of \(x\) give the same output value, so in particular, \(f(2)=f(-2)\), \(f(3)=f(-3)\), and in general \(f(x)=f(-x).\) Therefore the function behaves the same way on either side of the \(y\)-axis.
- The graph of \(f(x)=x\) has gradient 1, so it is straight, but it does not look the same when reflected in the \(y\)-axis.
- The graph of \(f(x)=x^2\) gets steeper and steeper as \(x\)-values move further away from \(0\), so it is not straight, but \((-x)^2=x^2\), so the \(y\)-axis is a line of symmetry.
- The graph of \(f(x)=x^3\) gets steeper and steeper as \(x\)-values move further away from \(0\), so it is not straight. However, \(f(-2)=(-2)^3=-8,\) and \(f(2)=2^3=8\), so the graph of \(f(x)=x^3\) does not look the same when reflected in the \(y\)-axis.

---

Which other functions could fit in the cells of this table?

Which straight lines are symmetric about the \(y\)-axis? Are all straight lines the graphs of functions of \(x\)?

The line \(x=0\) is straight and symmetric about the \(y\)-axis, but a function of \(x\) has to give a single output for any valid input value of \(x\). If a line such as \(x=3\) were the graph of a function of \(x\), what could the output value, \(f(3),\) be?

For the other cells, you might find it helpful to make a list of the functions you know about and try to sketch their graphs. Here is an alternative way to complete this function square.

| Graph is straight \(y\)-axis is a line of symmetry \[f(x)=1\] | Graph is straight \(y\)-axis is not a line of symmetry \[f(x)=-x\] |
| --- | --- |
| Graph is not straight \(y\)-axis is a line of symmetry \[f(x)=x^2+1\] | Graph is not straight \(y\)-axis is not a line of symmetry \[f(x)=\frac{1}{x} \text{ for } x\neq 0\] |

We have to specify that \(x\) is not zero when we write \(f(x)=\dfrac{1}{x}\) because \(\dfrac{1}{x}\) isn’t defined if \(x=0.\) It is important to think about which inputs are valid when you write down a formula for a function.

Here is an alternative way to complete this function square.

## Main problem

Can you arrange functions in these \(2 \times 2\) tables?

Once you have completed a function square, can you find other functions which also fit?

We have provided some functions on printed [cards](https://undergroundmathematics.org/thinking-about-functions/function-squares/components/functions-cards2.pdf) and you can either work with the equations of the functions or with their graphs. *(Please note that we haven’t excluded any input values for \(x\) on the cards because one of the properties to be considered is whether these functions are defined for all real values of \(x.\))*

| Graph passes through \((0,0)\) Graph has rotational symmetry about \((0,0)\) \[f(x)= \cdots\] | Graph passes through \((0,0)\) Graph does not have rotational symmetry about \((0,0)\) \[f(x)= \cdots\] |
| --- | --- |
| Graph does not pass through \((0,0)\) Graph has rotational symmetry about \((0,0)\) \[f(x)= \cdots\] | Graph does not pass through \((0,0)\) Graph does not have rotational symmetry about \((0,0)\) \[f(x)= \cdots\] |

| Function is defined for all real \(x\) Different values of \(x\) always give different values of \(f(x)\) \[f(x)= \cdots\] | Function is defined for all real \(x\) Different values of \(x\) may give the same value of \(f(x)\) \[f(x)= \cdots\] |
| --- | --- |
| Function is not defined for some real \(x\) Different values of \(x\) always give different values of \(f(x)\) \[f(x)= \cdots\] | Function is not defined for some real \(x\) Different values of \(x\) may give the same value of \(f(x)\) \[f(x)= \cdots\] |

Could you try to form a function square for other properties of functions?

Take a look at some of the functions you have used and at any other functions you have thought about. What is the same and what is different about these functions?

- the graph of the function is straight, i.e. the graph has constant gradient
- the graph of the function passes through the origin, i.e. \(f(0)=0\)
- different input values (values of \(x\)) all give different output values (values of \(f(x)\))
- the graph has asymptotes (lines which the graph of the function gets arbitrarily close to)
- the \(y\)-axis is a line of symmetry (the function is even)
- rotational symmetry about the origin (the function is odd)
- the function could be defined for all real values of \(x\), i.e. all real values of \(x\) are suitable as inputs

**Some properties**

From a completed function square, can you work out which properties might have been used?

Are there properties that can never be combined to make a function square?

## Taking it further

In the main problem you arranged four functions in a \(2 \times 2\) square according to two properties that the functions did or did not have. Now we will think about arranging eight functions in a \(2 \times 2 \times 2\) ‘cube’ based on whether or not the functions have three properties.

For example, can you complete this function cube for the following properties?

- Where the function is well defined, two different input values give two different output values
- The graph of function has asymptotes
- The graph of function has rotational symmetry about \((0,0)\)

> [figure: 2 by 2 by 2 cube with 4 functions drawn on; The functions x + (1 over x) and x cubed minus x are drawn on adjacent cells and the functions x + 1 and 1 over (x + 1) on the opposite cells respectively — `https://undergroundmathematics.org/thinking-about-functions/function-squares/images/newcubesmall.png`] (image not included in the text import; path of record).

There are many ways to represent a cube and if you wanted to use the functions cards, you might find it simpler to arrange them in a \(4 \times 2\) table, i.e. two ‘layers’ of four functions.

For example, the table below could represent a function cube for the properties

- The graph passes through \((0,0)\)
- The graph is straight
- The \(y\)-axis is a line of symmetry for the graph

| Graph passes through \((0,0)\) Graph is straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph passes through \((0,0)\) Graph is straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |
| --- | --- |
| Graph passes through \((0,0)\) Graph is not straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph passes through \((0,0)\) Graph is not straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |
| Graph does not pass through \((0,0)\) Graph is straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph does not pass through \((0,0)\) Graph is straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |
| Graph does not pass through \((0,0)\) Graph is not straight \(y\)-axis is a line of symmetry \[f(x)= \cdots\] | Graph does not pass through \((0,0)\) Graph is not straight \(y\)-axis is not a line of symmetry \[f(x)= \cdots\] |

Try to complete this function cube or make a different one.

You might need to make some extra function cards.

Make a note of any cells that you can’t think of functions for.

Make a note of properties that are difficult to combine in a function cube.
