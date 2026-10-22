---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r7607
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r7607
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7607
  old_site_id: Q198
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
      evidence: Ranges of log_a x and 1/x; f∘g with h(x)+f(x)=0; why g∘f needs a restricted domain (the
        composite-formation condition); define both inverses fully. log/exp vocabulary sits in 9709 P2/P3
        — the range/composition/inverse skills are exactly 1.2.x.
      rationale: 'Canonical UGM title: “Can we find the ranges of $f$ and $g$, and the function $f \circ
        g$?”; exam provenance: UCLES 1981 Q[''Q4''] [9202/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Ranges of log_a x and 1/x; f∘g with h(x)+f(x)=0; why g∘f needs a restricted domain (the
        composite-formation condition); define both inverses fully. log/exp vocabulary sits in 9709 P2/P3
        — the range/composition/inverse skills are exactly 1.2.x.
      rationale: 'Canonical UGM title: “Can we find the ranges of $f$ and $g$, and the function $f \circ
        g$?”; exam provenance: UCLES 1981 Q[''Q4''] [9202/1]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Ranges of log_a x and 1/x; f∘g with h(x)+f(x)=0; why g∘f needs a restricted domain (the
        composite-formation condition); define both inverses fully. log/exp vocabulary sits in 9709 P2/P3
        — the range/composition/inverse skills are exactly 1.2.x.
      rationale: 'Canonical UGM title: “Can we find the ranges of $f$ and $g$, and the function $f \circ
        g$?”; exam provenance: UCLES 1981 Q[''Q4''] [9202/1]'
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
  exam_reference: UCLES 1981 Q['Q4'] [9202/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r7607/images/logx.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r7607/images/reciprocalx.png
  kind: figure
---

# Can we find the ranges of $f$ and $g$, and the function $f \circ g$?

## Question

Functions

\(f\)

and

\(g\)

are defined by

\[\begin{align*} f:{}&x \to \log_a x,\quad&&(x \in \mathbb{R}_+, a>1),\\ g:{}&x\to \frac{1}{x},&&(x \in \mathbb{R}_+). \end{align*}\]

State the ranges of \(f\) and \(g\), and show that if \(h\) denotes the composite function \(f \circ g\), then \[h(x)+f(x)=0.\]

Explain briefly why the composite function \(g \circ f\) cannot be properly defined unless the domain is restricted to a subset of \(\mathbb{R}_+\), and state a possible subset which would be suitable.

Define fully the inverses of \(f\) and \(g\), and determine whether or not \(h^{-1}(x)+f^{-1}(x)=0\).

## Notational note

Note that the symbol \(\mathbb{R}\) refers to the set of all real numbers, that is, all the numbers on the number line.

Similarly, we denote the integers \((...,-2,-1,0,1,2,...)\) by \(\mathbb{Z}\), and the rationals (numbers \(a/b\), where \(a\) and \(b\) are whole numbers, \(b \neq 0\)) by \(\mathbb{Q}\).

Adding a small subscript “\(+\)” after any of these symbols means we only include the positive members of the relevant set. So, for example, \(\mathbb{R}_+\) refers to the *positive* real numbers. Similarly, a small subscript “\(-\)” would mean include only the negative numbers in this set.

An alternative notation which is also quite common is to use a superscript “\(+\)” instead, for example \(\mathbb{R}^+\).

## Solution

The range of \(f\) is \(\mathbb{R}\) and the range of \(g\) is \(\mathbb{R}_+\).

It is often helpful for domain and range questions to think about the graph of the relevant functions; here is the graph of \(y=f(x)\):

> [figure: Graph of f of x. The function is only defined for positive x. It tends to minus infinity as x tends to 0, and to infinity as x tends to infinity, with decreasing gradient. — `https://undergroundmathematics.org/combining-functions/r7607/images/logx.png`] (image not included in the text import; path of record).

We can see that the graph gives every \(y\) value for some \(x\) value, so the range is the whole of \(\mathbb{R}\).

Here is the graph of \(y=g(x)\) (confining the domain to only \(\mathbb{R}_+\)):

> [figure: Graph of g of x for positive x. It tends to infinity as x tends to 0, and tends to 0 as x tends to infinity. — `https://undergroundmathematics.org/combining-functions/r7607/images/reciprocalx.png`] (image not included in the text import; path of record).

Then it’s clear that the values of \(y\) which the graph passes through are those greater than zero, so the range of \(g\) is \(\mathbb{R}_+\).

We have

\[\begin{align*} h(x)&=(f\circ g)(x)\\ &=f(g(x))\\ &=\log_a\left(\frac{1}{x}\right)\\ &=\log_a(x^{-1})\\ &=-\log_a x \end{align*}\]

So \(h(x)+f(x)=-\log_a x+\log_a x=0\).

For the composition \(f_2 \circ f_1\) of two functions, \(f_1\) and \(f_2\), to be properly defined, we must have the range of \(f_1\) contained within the domain of \(f_2\). (Otherwise, for some \(x\) in the domain of \(f_1\), we would have \(f_1(x)\) not in the domain of \(f_2\), so \(f_2(f_1(x))\) will not be defined.)

In this case, we are considering \(g\circ f\) so \(f_2=g\) and \(f_1=f\). Therefore we require the range of \(f\) to be contained within the domain of \(g\).

But the domain of \(g\) is \(\mathbb{R}_+\) while the range of \(f\) is \(\mathbb{R}\). So the range of \(f\) is *not* contained within the domain of \(g\), thus \(g \circ f\) is not properly defined unless we restrict the domain to a subset of \(\mathbb{R}_+\).

For a suitable subset, we need the range of \(f\) with this restricted domain to be a subset of \(\mathbb{R}_+\). We see that \(f(x)>0\) when \(x>1\), so any subset of \(\{x:x>1\}\) (the real numbers greater than \(1\)) would suffice.

When defining a function, it is vital to specify the domain.

Recall that for any function \(f\), the domain of \(f^{-1}\) is the range of \(f\): every possible output of \(f\) has to be an allowable input to \(f^{-1}\) to get back to the original value.

As \(f(x)=\log_a x\), to find the inverse, we can write \(x=f(y)\) and rearrange to find \(y\) in terms of \(x\).

What we’re really doing is saying that \(f\bigl(f^{-1}(x)\bigr)=x\) and then writing \(y=f^{-1}(x)\). So we are using the result that \(f\circ f^{-1}\) and \(f^{-1}\circ f\) are both the identity function.

So in our case,

\[\begin{align*} &&x&=f(y)&&\quad\\ \implies&&x&=\log_a y\\ \implies&&a^x&=y \end{align*}\]

So \(f^{-1}(x)=a^x\) for \(x\) in \(\mathbb{R}\).

For

\(g(x)\)

, we have

\[\begin{align*} &&x&=g(y)&&\quad\\ \implies&&x&=\frac{1}{y}\\ \implies&&y&=\frac{1}{x} \end{align*}\]

So \(g^{-1}(x)=1/x\) for \(x\) in \(\mathbb{R}_+\).

For the final part, we start by finding

\(h(x)\)

:

\[\begin{align*} &&x&=h(y)&&\quad\\ \implies&&x&=-\log_a y\\ \implies&&-x&=\log_a y\\ \implies&&a^{-x}&=y \end{align*}\]

so \(h^{-1}(x)=a^{-x}\).

Thus \(h^{-1}(x)+f^{-1}(x)=a^{-x}+a^x>0\) for all \(x\), so \(h^{-1}(x)+f^{-1}(x)\ne 0\).
