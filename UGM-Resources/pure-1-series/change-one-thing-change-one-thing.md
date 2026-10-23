---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/change-one-thing
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/rich-example
- level/introducing
resource_identity:
  ugm_id: change-one-thing
  station: sequences
  station_title: Sequences
  resource_type_id: 2
  resource_type_label: Rich example
  level: Introducing
  ref: 6517
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: last term of the AP 3, 3.5, 4, ... with 25 terms, solved several ways — a_n = a_1+(n-1)d
        consolidation (acknowledged capture)
      rationale: 'Canonical UGM title: "Change one thing"; exam provenance: , None'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: ', None'
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/change-one-thing/download/teacher-notes.pdf
  kind: printable
---

# Change one thing

> Excerpt: Students are asked to think carefully about the different ways they can solve an arithmetic sequences question, and about what happens when they change one aspect of an arithmetic sequence.

## Problem

Find the last term of the sequence that starts with \(3\), has a [common difference](https://undergroundmathematics.org/glossary/common-difference) of \(\frac{1}{2}\) and has \(25\) terms.

- In what ways can this problem be solved?

Change only one aspect of the sequence in order to make the last term \(100\).

- What aspects can be changed?

- What would they change to?

## Solution

Let’s write the sequence numerically: \(3, 3\frac{1}{2}, 4, 4\frac{1}{2},...\)

The first term is \(3\), and after that there will be \(24\) other terms. \(\frac{1}{2}\) is being added for each term, so over \(24\) terms, \(12\) will be added. Therefore the \(25\)th term will be \(3 + 12 = 15\).

How does this example help us explain why the nth term of an arithmetic sequence is \(a_n = a_1 + (n-1)d\)? Why is it \(n-1\) rather than \(n\)?

We could also plot the points of the sequence on a graph.

The sequence is a linear relationship, so we can draw a linear graph through the points with gradient of \(\frac{1}{2}\). The equation of the line is \(y = \frac{1}{2}x + c\).

What is the value of \(c\)?

The equation of the line is

\(y = \frac{1}{2}x + 2\frac{1}{2}\)

, and so the

\(25\)

th term will be,

\[\begin{align*} y &= \frac{1}{2} \times 25 + 2\frac{1}{2} \\ &= 15. \end{align*}\]

How does thinking about the sequence graphically and the equation \(y = \frac{1}{2}x + 2\frac{1}{2}\), link to \(a_n = a_1 + (n-1)d\), the formula for the nth term of an arithmetic sequence?

We are told about three aspects of the sequence: the first term, the number of terms, and the common difference.

**The first term**

If we change the first term, then we still have a common difference of \(\frac{1}{2}\) and \(25\) terms, so difference between the first and last term will still be \(12\). Therefore, to make the last term \(100\) the first term would be \(88\).

If we think about the old and new sequences as linear graphs then we have a translation of \(85\) units in the \(y\) direction.

**The number of terms**

If we change the number of terms then we have the same intitial sequence, with a first term of \(3\) and a common difference of \(\frac{1}{2}\). This means that we can look at the original graph of \(y = \frac{1}{2}x + 2\frac{1}{2}\), and we want to know when \(y = 100\). Solving for \(x\) gives us \(x = 195\), i.e. there would be \(195\) terms in this sequence.

**The common difference**

If we change the common difference we want a sequence that starts at \(3\) and gets to \(100\) by the \(25\)th term. This means we are adding on \(97\) in 24 terms. Therefore the common difference will be \(\frac{97}{24}\). Graphically we have a line that still passes through the point \((1,3)\), but also passes through \((25, 100)\) giving the equation \(y = \frac{97}{24}x-\frac{25}{24}\).

We might have tried to change the common difference in a different way. We could make it a common *ratio*, and change the sequence from arithmetic to geometric. Why can’t a geometric sequence with a first term of \(3\), and common ratio of \(\frac{1}{2}\) ever have a nth term of \(100\)?

Is it possible to have other sequences that have a first term of \(3\), and a \(25\)th term of \(100\)?
