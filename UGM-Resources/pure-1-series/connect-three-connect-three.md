---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/connect-three
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: connect-three
  station: sequences
  station_title: Sequences
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 5401
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
  - code: 1.6.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: find an arithmetic progression containing any three given numbers — AP structure recognition
        and construction
      rationale: 'Canonical UGM title: "Connect three?"; exam provenance: NRICH, None'
      validation_status: SUGGESTED
    title: recognise arithmetic and geometric progressions
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: NRICH, None
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/connect-three/components/cards.pdf
  kind: printable
- path: https://undergroundmathematics.org/sequences/connect-three/download/teacher-notes.pdf
  kind: printable
---

# Connect three?

> Excerpt: Can we find an arithmetic progression containing any three given numbers (in some order)? What if one or more of those numbers were irrational? There are opportunities to further develop students thinking with discussions about proof by contradiction.

## Problem

Write down three numbers. Can you find an arithmetic progression containing all three of these numbers (in some order)?

Is it always possible to find an arithmetic progression containing any three numbers chosen (in some order)?

An arithmetic progression, or AP, is the same as an arithmetic sequence.

## Suggestion

What do you think right now (i.e. before diving in and doing any in-depth thinking)?

You might like to consider the sets of three numbers on each of the cards below.

\(\sqrt{2}\), \(\sqrt{3}\), \(\sqrt{5}\)

\(1\), \(\sqrt{2}\), \(2\)

\(4\), \(8\), \(14\)

\(78\), \(39\), \(169\)

\(-11\), \(-3\), \(19\)

\(\frac{1}{2}\), \(\pi\), \(5\pi - 2\)

\(1\), \(\frac{\pi}{2}\), \(\pi\)

\(4\sqrt{3} - 5\), \(-3\), \(-6\sqrt{3}\)

\(2\), \(5\), \(5\)

- Can you find an arithmetic progression containing all three of the numbers in each case?

- If you can find an arithmetic progression containing the three numbers on a card, is it unique?

- Are there any similarities or differences between cards?

- Can you apply a similar approach or line of reasoning to think about more than one card?

## Things you might have noticed

Write down three numbers. Can you find an arithmetic progression containing all three of these numbers (in ANY order)?

Is it always possible to find an arithmetic progression containing any three numbers chosen (in ANY order)?

We will consider these questions in the context of the cards given in the [Suggestion](https://undergroundmathematics.org/sequences/connect-three/suggestion).

**Cards C, D, E and I**

\(4\), \(8\), \(14\)

\(78\), \(39\), \(169\)

\(-11\), \(-3\), \(19\)

\(2\), \(5\), \(5\)

If we want them to belong to an arithmetic progression (from now on referred to as an AP), we need to identify a common difference for each set of three numbers.

- How might you do this for card C?

- Can the same approach be applied to cards D, E & I?

- Is it possible to find an AP that contains the numbers in card D in their given order?

- What is different about card I? Is there ever an occasion where an AP could contain a repeated value?

Let’s say we suggest the following AP for card C, \[2, 4, 6, 8, \dots\] Are there any other, different APs that could have been suggested?

**Cards F and G**

\(\frac{1}{2}\), \(\pi\), \(5\pi - 2\)

\(1\), \(\frac{\pi}{2}\), \(\pi\)

We might choose to look at card F first. Beginning as for cards C, D and E, by looking for a common difference we find that the difference between the first two values is \(\pi-\frac{1}{2}\) and the second two values is \(4\pi - 2\). Now, for us to find an AP we require that \[p\left(\pi - \frac{1}{2}\right) = q(4\pi - 2)\] where \(p\) and \(q\) are integers.

Can you see any values for \(p\) and \(q\) that could work here?

- What about if \(q=1\) (i.e. \(4\pi - 2\) is a multiple of \(\pi - \frac{1}{2}\))?

Now let’s think about card G. As before, looking for a common difference we find that the difference between the first two values is \(\frac{\pi}{2} - 1\) and the second two values is \(\frac{\pi}{2}\). But what do we do with this information now?

As above, if we have an AP then we can write \[p\left(\frac{\pi}{2} - 1\right) = q\left(\frac{\pi}{2}\right)\] where \(p\) and \(q\) are integers.

Expanding the brackets and rearranging we have \[\pi=\frac{2p}{p-q}.\]

Why did we choose to rearrange the equation to make \(\pi\) the subject?

- Why might this be useful? What do we know about \(\pi\)?

Could \(p\) ever be equal to \(q\)?

- What would this mean for the progression?

- What would it mean algebraically?

What does this tell us?

\[\pi=\frac{2p}{p-q}\]

As \(\pi\) is irrational and all the other terms in the expression are integers, this is impossible and we have reached a contradiction. So it is NOT possible to find an AP containing all three of the terms on card G.

**Cards A, B and H**

\(\sqrt{2}\), \(\sqrt{3}\), \(\sqrt{5}\)

\(1\), \(\sqrt{2}\), \(2\)

\(4\sqrt{3} - 5\), \(-3\), \(-6\sqrt{3}\)

Based on your thinking so far, or otherwise, do you have any feeling about whether or not it will be possible to find APs for the numbers on these cards?

Below is a way to think about card A. It proves that it is impossible to find an AP containing all three of the values.

Does this mean that it is impossible to find an AP for cards B and H too?

Card A

The difference between the first two values is \(\sqrt{3} - \sqrt{2}\) and between the second two values is \(\sqrt{5} - \sqrt{3}\).

As for cards F and G, if we have an AP then we can write \[p\left(\sqrt{3} - \sqrt{2}\right) = q\left(\sqrt{5} - \sqrt{3}\right)\] where \(p\) and \(q\) are integers.

There are not ‘obvious’ values of \(p\) and \(q\) that will work here so let’s continue as we did for card G.

Expanding the expression and rearranging we have \[(p+q)\sqrt{3} = p\sqrt{2} + q\sqrt{5}.\]

At this point we have three different irrational terms in our equation. This is different to what happened with card G.

What happens if we square both sides?

Squaring both sides we get \[3(p+q)^2 = 2p^2 + 5q^2 + (p+q)\sqrt{10}.\]

Rearranging to make \(\sqrt{10}\) the subject gives us \[\sqrt{10} = \frac{3(p+q)^2 - 2p^2 - 5q^2}{p+q}.\] As \(\sqrt{10}\) is irrational, but all of the terms on the right-hand side are integers, we have a contradiction. So it is NOT possible to find an AP containing all three of the values on card A.

You might like to think about cards B and H in a similar way before looking at the suggestions below for card H.

Card H

The difference between the first two values is \(4\sqrt{3}-2\) and between the second two values is \(6\sqrt{3}-3\).

As previously, if we have an AP then we can write \[p\left(4\sqrt{3}-2\right) = q\left(6\sqrt{3}-3\right)\] where \(p\) and \(q\) are integers.

We might now notice that the expressions within the brackets here can be factorised to give \[2p\left(2\sqrt{3}-1\right) = 3q\left(2\sqrt{3}-1\right)\] and then simplified to show that \[2p=3q.\]

This tells us that we can find values of \(p\) and \(q\), and therefore that we can identify a common difference and then an AP that contains the values on this card.

What might have happened if we had continued without factorising the expression \[p\left(4\sqrt{3}-2\right) = q\left(6\sqrt{3}-3\right)?\]

If we had continued as for card A, we might have expanded the brackets and rearranged to get \[\left(4p - 6q\right)\sqrt{3} = 2p - 3q\] but this suggests that \[\sqrt{3} = \frac{2p-3q}{2(2p-3q)} = \frac{1}{2}.\] This is a contradiction and suggests that we cannot find an AP containing the values on this card.

Can you identify what has gone wrong with our line of reasoning here?

In summary

| Card | Is it possible to find an AP? | A possible AP |
|---|---|---|
| A | No |  |
| B | No |  |
| C | Yes | \(2, 4, 6, 8, \dots\) |
| D | Yes | \(13, 26, 39, 52, \dots\) |
| E | Yes | \(-11,-9,-7,-5,\dots\) |
| F | Yes | \(\left(\frac{1}{2}\right), \pi, \left(2\pi-\frac{1}{2}\right), \left(3\pi - 1\right), \dots\) |
| G | No |  |
| H | Yes | \(\left(4 \sqrt{3}-5\right), \left(2 \sqrt{3} - 4\right), -3, \left(-2 \sqrt{3} - 2\right), \dots\) |
| I | No |  |
