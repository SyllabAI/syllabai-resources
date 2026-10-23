---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/can-you-find-series-edition
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: can-you-find-series-edition
  station: sequences
  station_title: Sequences
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 6818
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
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: construct infinite series meeting constraints — the GP convergence condition -1<r<1
        is the central tool (general-series extensions recorded honestly)
      rationale: 'Canonical UGM title: "Can you find... series edition"'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/can-you-find-series-edition/download/teacher-notes.pdf
  kind: printable
---

# Can you find... series edition

> Excerpt: Students are asked to construct examples of infinite series that meet a set of constraints. This could consolidate understanding of convergence of series, or be used to introduce series following work on sequences.

## Problem

Can you find an infinite series where…

1. … the terms are decreasing and the series converges?

---

1. … the terms are decreasing and the series does not converge?

---

1. … the terms are increasing and the series converges?

Now try this

What if the series in (a) must converge to \(4\)?

What if the terms of the series in (b) must all be positive?

If you add the same constant to each of the terms in the series you found in (c), will your new series still meet the conditions in part (c)?

## Things you might have noticed

Since this question asks about infinite series which converge, I need to be sure that any series I suggest does converge. The series I know most about are arithmetic and geometric series. Infinite arithmetic series can’t converge except for \(0+0+0+\dotsb\), but I know conditions under which geometric series converge, so I’ll focus on geometric series for now.

I know that a geometric series will converge if the common ratio between the terms, \(r\), satisfies \(-1<r<1\), so one way to meet the required conditions is to find a convergent geometric series whose terms are decreasing (that is, where the terms satisfy \(u_{n+1}\leq u_n\) for all positive integers \(n\)).

The signs of the terms will alternate if the common ratio is negative, so I need to have a common ratio between \(0\) and \(1\). Is this enough to ensure that the terms are decreasing?

For example, I could choose the geometric series

- \(1+\tfrac{1}{2}+\tfrac{1}{4}+ \tfrac{1}{8}+\tfrac{1}{16}+\dotsb\)

- \(3+1+\tfrac{1}{3}+ \tfrac{1}{9}+\tfrac{1}{27}+\dotsb\)

- \(256+128+64+32+16+\dotsb\)

Can you find an infinite series where…

1. … the terms are decreasing and the series does not converge?

This time I want to be sure my series do not converge. Continuing from part (a), if I choose a geometric series with common ratio \(r\) where \(r\leq -1\) or \(r\geq 1\) the series will not converge. And I can ensure that the terms decrease if I choose \(r>1\) and the terms are negative. For example, the terms in the geometric series \(-1 -2 -4 -8 -\dotsb\) are decreasing and this series does not converge.

As I’m looking for a series that doesn’t converge, I could instead consider an arithmetic series with negative common difference. It doesn’t matter whether the first term is positive or negative, so for example, I could choose \(5+2-1-4 - \dotsb\)

So far I’ve considered arithmetic and geometric series, but I don’t have to restrict myself to these. For example, the terms in the series \(1+ \tfrac{1}{2}+ \tfrac{1}{3}+ \tfrac{1}{4}+ \tfrac{1}{5}+\dotsb\) are decreasing. This is known as the [harmonic series](https://undergroundmathematics.org/glossary/harmonic-series). Do you think this series converges?

What about the series \(2+\tfrac{3}{2}+\tfrac{5}{4}+\tfrac{9}{8}+\tfrac{17}{16}\dotsb\)? Does this series meet the conditions for part (b)?

Can you find an infinite series where…

1. … the terms are increasing and the series converges?

As I need a convergent series, I’ll look for a geometric series that meets the condition on increasing terms. Building on ideas from part (a), I’ll need the common ratio to be between \(0\) and \(1\), but then the terms will only increase if they are all negative. For example, I could choose the geometric series \(-1 -\tfrac{1}{3} - \tfrac{1}{9}-\tfrac{1}{27}- \dotsb\) Does this series meet the required conditions?

If the terms in a series get closer to zero as \(n\) increases, does this mean the series converges?

For (a) I chose to look for geometric series with common ratio between \(0\) and \(1\) to ensure that the sum of the terms converged and the signs of the terms didn’t alternate. If the first term is positive then all the other terms will be, and since \(0<r<1\), these terms will decrease.

I’ll keep focusing on geometric series, but to meet the extra constraint that the sum of the terms must be \(4\), I need to find first term \(a\) and common ratio \(r\) so that \(\tfrac{a}{1-r}=4.\) I could choose \(r=\tfrac{1}{2}\), which would require \(a=2.\) (This has the same common ratio as the first series I gave for (a), but the first term is different). I could also choose \(a=1\), which would then require \(r=\tfrac{3}{4}.\) How much flexibility it there over choice of \(a\) and \(r\)?

If you found a geometric series for (a), how could you modify it to make a new infinite series that converges to \(4\)?

If the terms in my series for (b) need to be positive but decreasing, I can’t have an arithmetic series.

The terms in a geometric series of positive numbers will only decrease if the common ratio is between \(0\) and \(1\), but then the sum of the terms will converge, so a geometric series cannot meet this extra condition in (b).

The harmonic series \(1+\tfrac{1}{2}+\tfrac{1}{3}+ \tfrac{1}{4}+\tfrac{1}{5}+\tfrac{1}{6}+\tfrac{1}{7}+\tfrac{1}{8}+\dotsb\) is decreasing and doesn’t converge, and all the numbers are positive, so this series already satisfies the extra constraint for (b). The series \(2+\tfrac{3}{2}+\tfrac{5}{4}+\tfrac{9}{8}+\tfrac{17}{16}\dotsb\) also meets these constraints.

For (c) I chose the geometric series \(-1 - \tfrac{1}{3}- \tfrac{1}{9}- \tfrac{1}{27}- \dotsb\), which consists of negative terms that increase to \(0\) because of the size of the common ratio. Adding \(1\) to every term gives the new series

\[0 + \tfrac{2}{3}+ \tfrac{8}{9}+ \tfrac{26}{27}+ \dotsb\]

Now instead of the terms increasing to \(0\) they increase to \(1\). But what can you say about the sum of the terms?

We have mainly focused on arithmetic and geometric series here because we already know quite a lot about how these behave. There are lots of other series that meet the conditions in this question but which require some intricate analysis to determine whether they converge.

In the final part of the problem we asked what would happen if you added a constant to every term in a series. How else could you modify geometric sequences or series and how does this affect their behaviour? For example, what happens if you multiply every term by the same constant? What if you square every term?

Here is some [Student work](https://undergroundmathematics.org/sequences/can-you-find-series-edition/student-work) for parts of this problem. How does this compare with your approach?

## Student work

One student suggested the series \(1+ \tfrac{1}{2}+ \tfrac{1}{4}+ \tfrac{1}{8}+ \tfrac{1}{16}+\dotsb\) for part (a) because she knew that its sum is \(2\). Here is some of her work for part (c).

Getting started

Here are this student’s initial notes as she tackled part (c).

Questions

- How could you use these suggestions to find a series that satisfies the constraints in part (c)?

- Can you suggest any other ways to tackle part (c)?

Using ideas

The student then used some of these ideas, leading to the following sketch graph.

Questions

- What series is this student suggesting?

- How do you think this student has used her initial thoughts to get to this series?

- What other series could she have obtained using her initial ideas?
