---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/making-inverse-functions
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/scaffolded-task
- level/introducing
resource_identity:
  ugm_id: making-inverse-functions
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Introducing
  ref: 5938
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Function-machine inversion of f(x)=2x+1, then algebraic rearranging — scaffolded 1.2.3
        intro (pattern exemplar).
      rationale: 'Canonical UGM title: “Making inverse functions”'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Function-machine inversion of f(x)=2x+1, then algebraic rearranging — scaffolded 1.2.3
        intro (pattern exemplar).
      rationale: 'Canonical UGM title: “Making inverse functions”'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/function-machine.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/inverse-blank-machine.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/quadraticexamples.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/graph-g-1.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/alternative-g.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/function-machine-inverses.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/f-diagram.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/finv-diagram.svg
  kind: figure
---

# Making inverse functions

> Excerpt: Here we revisit the algebraic process of finding an inverse for a function, and explore the importance of specifying the domain and when we need to restrict the domain in order to make a function invertible.

## Function machines

Starting with a function \[f(x)=2x+1\] defined for \(x\) as any real number, we can represent it as a function machine. We put \(x\) in at the left and get \(f(x)\) out at the right.

> [figure: function machine doing times 2 then plus 1 — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/function-machine.svg`] (image not included in the text import; path of record).

The inverse function, \(f^{-1}\), is such that if we put in \(f(x)\) we’ll get out \(x\). Fill in the boxes below so that if you put in \(2x+1\) at the right, you get \(x\) out at the left.

> [figure: blank function machine converting 2x+1 into x — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/inverse-blank-machine.svg`] (image not included in the text import; path of record).

To find out what the inverse function is, use the same machine, put in \(x\) at the right and see what comes out at the left. The expression that comes out at the left is equal to \(f^{-1}(x)\).

In other words, \(f^{-1}(y)\) is what we get by rearranging \(\eqref{eq:f}\) to make \(x\) the subject. We can then simply replace each \(y\) with an \(x\) to find \(f^{-1}(x)\).

\[2x=y-1 \quad\text{so}\quad x=\frac{1}{2}(y-1). \quad\text{Therefore}\quad f^{-1}(x)=\frac{1}{2}(x-1)=\frac{1}{2}x-\frac{1}{2}.\]

**Solution**

 If we had written

\(y=2x+1\)

, then we would have

\[\begin{equation} y=f(x). \label{eq:f} \end{equation}\]

 The second function machine above tells us that putting

\(y\)

 into

\(f^{-1}\)

 we get out

\(x\)

, so

\[\begin{equation} x=f^{-1}(y). \label{eq:f-1} \end{equation}\]

 Complete the following.

\[\begin{align*} y &= 2x+1 \\ \\ 2x &= \\ \\ x &= \qquad\qquad\qquad = f^{-1}(y) \\ \\ \text{Therefore}\quad f^{-1}(x) &= \end{align*}\]

**Rearranging**

Find the inverse of each of these functions, either by drawing a function machine or by rearranging the formula.

1. \(f(x) = 3x-2,\quad x\in\mathbb{R}\)
2. \(f(x) = x^3-1,\quad x\in\mathbb{R}\)

The symbols \(x\in\mathbb{R}\) define the domain of the function and mean \(x\) can be any real number.

1. \(y=3x-2 \quad\implies\quad x=\frac{1}{3}(y+2) \quad\implies\quad f^{-1}(x)=\frac{1}{3}x+\frac{2}{3},\; x\in\mathbb{R}\)
2. \(y=x^3-1 \quad\implies\quad x=\sqrt[3]{y+1} \quad\implies\quad f^{-1}(x)=\sqrt[3]{x+1},\; x\in\mathbb{R}\)

**Solution**

**Now try these**

Note we have chosen functions that can be written as simple function machines. There are many functions which cannot be written like this and many which cannot be inverted algebraically. Can you think of some examples?

## Defining domains

What is \(x\) if \(x^2-2=7\)?

What if you also knew that \(x\geq 0\)?

If \(x^2-2=7\) then \(x\) could be \(3\) or \(-3\), but by restricting \(x\) to \(x\geq 0\), we ensure there is a single solution to the equation \(x^2-2=7\). (Of course, we could have restricted \(x\) in other ways to ensure that there was a single solution.)

**Answer**

#### The need for one-to-one

Let’s think about this quadratic problem in terms of functions and consider the function \(f(x)=x^2-2\) where \(x\) can be any real number. The [domain](https://undergroundmathematics.org/glossary/domain) of \(f\) is \(\mathbb{R}\) and the [range](https://undergroundmathematics.org/glossary/range-of-a-function) is the [interval](https://undergroundmathematics.org/glossary/interval-notation) \([-2,\infty)\) or in other words \(f(x)\ge-2\).

The function is [many-to-one](https://undergroundmathematics.org/glossary/many-to-one), which you can see from the graph of \(y=f(x)\) below. For instance, the inputs \(3\) and \(-3\) both give the same output value, namely \(7\).

The inverse function, \(f^{-1}(x)\), would be one that ‘undoes’ the effects of \(f(x)\), but what value should we get for \(f^{-1}(7)\)? We would want it to provide both values, \(3\) and \(-3\), making it a one-to-many relation but we do not consider things with more than one output to be functions.

\[y=x^2-2 \quad\implies\quad x^2=y+2 \quad\implies\quad x=\pm\sqrt{y+2}\] This seems to imply that \[f^{-1}(x)=\pm\sqrt{x+2}\] but the \(\pm\) indicates one-to-many behaviour, so \(f^{-1}\) is not actually a function.

**What happens if we try to invert the function algebraically?**

See the resource [What relation are you?](https://undergroundmathematics.org/thinking-about-functions/what-relation-are-you) for more about many-to-one and one-to-many relations.

#### Restricting the domain

If we define a new function, \(g(x)\), with the same rule as \(f(x)\) but with its domain restricted to \([0,\infty)\), then this function *is* one-to-one (also known as [injective](https://undergroundmathematics.org/glossary/injective)).

> [figure: graphs showing f of x with domain R and g of x with domain x greater than or equal to zero — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/quadraticexamples.svg`] (image not included in the text import; path of record).

This means that

\(g\)

is invertible and we can write its inverse function as

\[g^{-1}(x) = \sqrt{x+2},\quad x\ge-2.\]

How did I know to use the positive rather than the negative square root?

> [figure: graph showing g-inverse of x — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/graph-g-1.svg`] (image not included in the text import; path of record).

Notice that,

- Function \(g\) has the same range as \(f\) so any value that can be obtained as output from \(f\) can also be obtained from \(g\).
- The domain of \(g^{-1}(x)\) is \([-2,\infty)\), which is the range of \(g(x)\).
- The range of \(g^{-1}(x)\) is \([0,\infty)\), which is the domain of \(g(x)\).

We chose to restrict the domain of \(g\) to \([0,\infty)\), but we could instead have chosen to restrict it to \((-\infty,0]\). What would the graph of \(y=g(x)\) then look like? What would its range have been? Would it be invertible?

Another function is defined as \(h(x)=x^2-2, \ 1\le x\le4\). What is its range and what is its inverse function?

This alternative \(g\) has range \([-2,\infty)\), which is the same as before. It is still one-to-one, but now we see that we need to take the *negative* square root to find the inverse of \(g\), because the domain of \(g\) is \((-\infty,0]\). \[y=g(x)=x^2-2 \quad\implies\quad x^2=y+2 \quad\implies\quad x=-\sqrt{y+2}\] and therefore \[g^{-1}(x)=-\sqrt{x+2}\]

> [figure: graph of g with domain x less than or equal to zero — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/alternative-g.svg`] (image not included in the text import; path of record).

Notice that the domain of \(h^{-1}\) is the range of \(h\) and vice versa.

 For the function

\(h\)

, since it has domain

\([1,4]\)

, we will have to take the positive square root to find its inverse.

\[\begin{align*} h(x) &=x^2-2,\quad 1\le x\le4; \quad \text{range: }[-1,14] \\ h^{-1}(x) &=\sqrt{x+2},\quad-1\le x\le14; \quad \text{range: }[1,4] \end{align*}\]

**Answers**

#### Definitions

When we say that two functions, \(f\) and \(f^{-1}\), are inverses we mean that each one “undoes” the action of the other. Applying one and then the other (either way round) will take us back to our starting value.

Algebraically we can say that,

- \(f^{-1}(f(x))=x\) for all values of \(x\) in the domain of \(f\), and
- \(f(f^{-1}(y))=y\) for all values of \(y\) in the domain of \(f^{-1}\).

In order to achieve this, not only must \(f\) be one-to-one on its entire domain, but also the domain of \(f^{-1}\) must be the same as the range of \(f\) and vice-versa. Below, we shall explore why this is.

There is a concept of a one-sided inverse, where one of the above bullet points is true but not the other. However, we are only going to consider cases where they are inverses both ways round.

#### Matching domains and ranges

#### Function machines

We can represent the composition of a function and its inverse as a function machine.

> [figure: function machine diagram showing f then f inverse and another the other way round — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/function-machine-inverses.svg`] (image not included in the text import; path of record).

In the middle of the first diagram, the output of \(f\) becomes the input of \(f^{-1}\), and so the range of \(f\) must match the domain of \(f^{-1}\). The second machine shows that the domain of \(f\) must match the range of \(f^{-1}\).

#### Graphs

Another way to think about this is to consider the graph above of the function \(y=g(x)\). Starting at a value of \(x\) in the domain of \(g\) we find \(y\) by tracking vertically from the \(x\)-axis to the curve then horizontally to the \(y\)-axis.

As \(g^{-1}\) is the inverse, the same graph also represents \(x=g^{-1}(y)\). Starting at a \(y\) value on the \(y\)-axis we track the same path in reverse to find our \(x\) value. As it is the same graph, the range of possible outputs from \(g\) must be the same as the domain of possible inputs to \(g^{-1}\) and vice-versa.

#### A diagrammatic approach

We can draw a diagram to represent the function \(f\), as we did in [What relation are you?](https://undergroundmathematics.org/thinking-about-functions/what-relation-are-you).

> [figure: Two ovals each containing five dots, each dot in the left oval is joined to to a different dot in the right oval by an arrow — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/f-diagram.svg`] (image not included in the text import; path of record).

The dots on the left represent the domain of \(f\) and as \(f\) is a one-to-one function, there is at most one arrow coming into each dot on the right. We have also chosen to make the right hand set be exactly the range of \(f\), so *every* dot has an arrow coming into it.

What would the diagram for \(f^{-1}\) look like, and how does this show that the domain of \(f^{-1}\) is the range of \(f\) and vice versa?

The arrows are all reversed to get the inverse function:

> [figure: The same diagram as above, but with all of the arrows reversed — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/finv-diagram.svg`] (image not included in the text import; path of record).

It is clear from these diagrams that the domain of \(f\), which is the left set, is the range of \(f^{-1}\), while the range of \(f\), which is the right set, is the domain of \(f^{-1}\).

**Solution**

## Invertible sort

Below are graphs of twelve functions. Some are invertible on the domain shown and some are not. Can you sort them out?

You might think about…

- is the function one-to-one or many-to-one?
- how could you restrict the domain to make an invertible function?
- can you find a restricted domain that makes an invertible function with the same range as the unrestricted function?

Graph 1 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new2b.svg`] (image not included in the text import; path of record).

Graph 2 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new3a.svg`] (image not included in the text import; path of record).

Graph 3 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new5b.svg`] (image not included in the text import; path of record).

Graph 4 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new2a.svg`] (image not included in the text import; path of record).

Graph 5 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new5a.svg`] (image not included in the text import; path of record).

Graph 6 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new4b.svg`] (image not included in the text import; path of record).

Graph 7 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new6b.svg`] (image not included in the text import; path of record).

Graph 8 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new1a.svg`] (image not included in the text import; path of record).

Graph 9 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new6a.svg`] (image not included in the text import; path of record).

Graph 10 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new3b.svg`] (image not included in the text import; path of record).

Graph 11 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new4a.svg`] (image not included in the text import; path of record).

Graph 12 > [figure:  — `https://undergroundmathematics.org/combining-functions/making-inverse-functions/images/new1b.svg`] (image not included in the text import; path of record).
