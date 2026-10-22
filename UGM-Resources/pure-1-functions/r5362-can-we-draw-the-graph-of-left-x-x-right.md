---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5362
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5362
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5362
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
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Range of |x+[x]|; one-one question; inverse of a restricted mapping. Floor function is
        an extension beyond P1 "simple cases".
      rationale: 'Canonical UGM title: “Can we draw the graph of  $\left| x + [x] \right|$?”; exam provenance:
        UCLES 1979 Q[''Q1''] [848/0]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Range of |x+[x]|; one-one question; inverse of a restricted mapping. Floor function is
        an extension beyond P1 "simple cases".
      rationale: 'Canonical UGM title: “Can we draw the graph of  $\left| x + [x] \right|$?”; exam provenance:
        UCLES 1979 Q[''Q1''] [848/0]'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Range of |x+[x]|; one-one question; inverse of a restricted mapping. Floor function is
        an extension beyond P1 "simple cases".
      rationale: 'Canonical UGM title: “Can we draw the graph of  $\left| x + [x] \right|$?”; exam provenance:
        UCLES 1979 Q[''Q1''] [848/0]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1979 Q['Q1'] [848/0]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r5362/images/sketch-labelled.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5362/images/g-machine.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5362/images/g-1-machine.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r5362/images/sketch-reflection-labelled.png
  kind: figure
---

# Can we draw the graph of  $\left| x + [x] \right|$?

## Question

A function

\(f\)

is defined on

\(\mathbb{R}\)

by

\[\begin{equation*} f \colon x \to \left| x + [x] \right| \end{equation*}\]

where \([x]\) indicates the greatest integer less than or equal to \(x\), e.g. \([3] = 3\), \([2.4] = 2\), \([-3.6] = -4\). Sketch the graph of the function for \(-3 \le x \le 3\). What is the range of \(f\)? Is the mapping one-one?

The function \(g\) is defined by \(g \colon x \to \left| x + [x] \right|\), \(x \in \mathbb{R}_+\), \(x \notin \mathbb{Z}_+\). Find the rule and domain of the inverse function \(g^{-1}\).

## Solution

The function \([x]\) defined here is called the [floor function](https://undergroundmathematics.org/glossary/floor-function).

Note that the value of our function \(f(x)\) will change abruptly at each integer value of \(x\). Let’s look at the behaviour of \(f\) on [intervals](https://undergroundmathematics.org/glossary/interval-notation) like \([0,1)\), \([1,2)\), etc.

When

\(0 \le x < 1\)

, we have that

\([x] = 0\)

and so

\[\begin{equation*} f(x) = \left| x + [x] \right| = |x| = x. \end{equation*}\]

When

\(1 \le x < 2\)

, we have

\([x] = 1\)

so

\[\begin{equation*} f(x) = \left| x + [x] \right| = |x+1| = x + 1 \end{equation*}\]

and similarly for all other intervals of the form

\([n,n+1)\)

where

\(n\)

is a positive integer,

\[\begin{equation*} f(x) = x + n . \end{equation*}\]

On the other hand, when

\(-1 \le x < 0\)

, we have

\([x] = -1\)

and so

\[\begin{equation*} f(x) = \left| x + [x] \right| = |x-1| = -x + 1. \end{equation*}\]

Similarly, for all intervals of the form

\([n,n+1)\)

with

\(n < 0\)

,

\[\begin{equation*} f(x) = -x - n . \end{equation*}\]

These considerations lead to the following graph.

> [figure: graph of the function f — `https://undergroundmathematics.org/combining-functions/r5362/images/sketch-labelled.png`] (image not included in the text import; path of record).

As can be seen from the graph, the range of \(f\) is \[f(x)\geq 0, f(x)\neq 1,3,5,\ldots.\]

Notice that \(f(-1)=f(1)=2\) and similarly for other non-zero integer values of \(x\). Hence the mapping is not one-to-one.

The notation \(x \in \mathbb{R}_+\), \(x \notin \mathbb{Z}_+\) means that the domain of \(g\) is the real numbers greater than zero but excluding all the positive integers. Where the question asks for the ‘rule’ it means an algebraic definition of the function.

Remember that an inverse function does not exist for a function such as \(f\) that is not one-to-one. The restricted domain of \(g\) means that it is one-to-one and does have an inverse.

Notice also that with the restricted domain, \(x+[x]\) is always positive, so the definition of \(g\) can (more conveniently) be written without the modulus sign.

By definition, the domain of \(g^{-1}\) is the same as the range of \(g\). From the graph, we can see that this is \[0<x<1\text{ and }2<x<3\text{ and }\ldots\text{ and }2n<x<2n+1\ldots\] where \(n\) is a positive integer. This can be written as \[(0,1) \cup (2,3) \cup (4,5) \ldots \cup (2n,2n+1) \cup \ldots .\]

To find the rule that defines \(g^{-1}\), let’s first think about what \(g\) is doing. We can consider the number \(x\) as being made up of two parts – the whole number part \([x]\) and its fractional part which we call \(a\) (such that \(0<a<1\)). Then \[x=[x]+a\] and \[g(x)=x+[x] = 2[x]+a.\] In other words, the function \(g\) doubles the whole number part and keeps the fractional part the same. We can think about \(g\) as a function machine.

> [figure: g as a function machine — `https://undergroundmathematics.org/combining-functions/r5362/images/g-machine.png`] (image not included in the text import; path of record).

We have defined the operation ‘split’ to mean turn \(x\) into a whole number and a fractional part between \(0\) and \(1\). The operation ‘join’ is its inverse which is actually just addition.

Now we can draw the inverse function machine.

> [figure: g inverse as a function machine — `https://undergroundmathematics.org/combining-functions/r5362/images/g-1-machine.png`] (image not included in the text import; path of record).

So now we see that \[g^{-1}(x)=\frac{1}{2}[x]+a = \frac{1}{2}[x]+x-[x] = x-\frac{1}{2}[x].\]

Alternatively, we are to find the function \(g^{-1}\) such that \(g^{-1}(x + [x]) = x\) whenever \(x\) is in the domain of \(g\). So we want to write \(x\) as a function of \((x+[x])\).

Thus, the required rule is \(g^{-1}(x) = x - \dfrac{[x]}{2}\), as before.

 We note that

\([x + [x]] = 2[x]\)

, so we can write

\[\begin{equation*} x = x + [x] - [x] = (x + [x]) - \frac{[x + [x]]}{2}. \end{equation*}\]

> [figure: A graph of g and its reflection in the line y = x — `https://undergroundmathematics.org/combining-functions/r5362/images/sketch-reflection-labelled.png`] (image not included in the text import; path of record).

The graph of \(y = g(x)\) is in blue, the line \(y = x\) is a dashed line, and \(y=g^{-1}(x)\) is in red.

We can reply by pointing out that \(5.75\) does not lie in the domain of \(g^{-1}\), even though the rule that defines \(g^{-1}\) can be applied, in principle, to any real number.

 Suppose someone objects that

\(g^{-1}(x) = x - \dfrac{[x]}{2}\)

 is not the inverse of

\(g\)

 as, for example,

\[\begin{equation*} g(g^{-1}(5.75)) = g\left( 5.75 - \frac{[5.75]}{2} \right) = g(5.75 - 2.5) = g(3.25) = 3.25 + [3.25] = 6.25. \end{equation*}\]
