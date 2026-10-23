---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6970
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6970
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6970
  old_site_id: Q132
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q7
task: T-UGM-IMPORT-6
---

# Given this set of tiles, when can we create a match?

## Question

Suppose we have a collection of tiles, each containing two strings of letters, one above the other. A match is a list of tiles from the given collection (tiles may be used repeatedly) such that the string of letters along the top is the same as the string of letters along the bottom. For example, given the collection \[\left\{ \left[ \frac{\mathsf{AA}}{\mathsf{A}} \right], \left[ \frac{\mathsf{B}}{\mathsf{ABA}} \right], \left[ \frac{\mathsf{CCA}}{\mathsf{CA}} \right] \right\},\] the list \[\left[ \frac{\mathsf{AA}}{\mathsf{A}} \right]\quad \left[ \frac{\mathsf{B}}{\mathsf{ABA}} \right]\quad \left[ \frac{\mathsf{AA}}{\mathsf{A}} \right]\] is a match since the string \(\mathsf{AABAA}\) occurs both on the top and bottom.

Consider the following set of tiles: \[\left\{ \left[ \frac{\mathsf{X}}{\mathsf{U}} \right], \left[ \frac{\mathsf{UU}}{\mathsf{U}} \right], \left[ \frac{\mathsf{Z}}{\mathsf{X}} \right], \left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right], \left[ \frac{\mathsf{Y}}{\mathsf{U}}\right], \left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right] \right\}.\]

1. What tile must a match begin with?

---

1. Write down all the matches which use four tiles (counting any repetitions).

---

1. Suppose we replace the tile \(\left[ \dfrac{\mathsf{E}}{\mathsf{ZE}} \right]\) with \(\left[ \dfrac{\mathsf{E}}{\mathsf{ZZZE}} \right]\). What is the least number of tiles that can be used in a match? How many different matches are there using this smallest number of tiles? [Hint: you may find it easiest to construct your matches backwards from right to left.]

Consider a new set of tiles \(\left\{ \left[ \dfrac{\mathsf{XXXXXXX}}{\mathsf{X}} \right], \left[ \dfrac{\mathsf{X}}{\mathsf{XXXXXXXXXX}} \right] \right\}\). (The first tile has seven \(\mathsf{X}\)s on top, and the second tile has ten \(\mathsf{X}\)s on the bottom.)

1. For which numbers \(n\) do there exist matches using \(n\) tiles? Briefly justify your answer.

## Solution

Suppose we have a collection of tiles, each containing two strings of letters, one above the other. A match is a list of tiles from the given collection (tiles may be used repeatedly) such that the string of letters along the top is the same as the string of letters along the bottom. For example, given the collection \[\left\{ \left[ \frac{\mathsf{AA}}{\mathsf{A}} \right], \left[ \frac{\mathsf{B}}{\mathsf{ABA}} \right], \left[ \frac{\mathsf{CCA}}{\mathsf{CA}} \right] \right\},\] the list \[\left\{ \left[ \frac{\mathsf{AA}}{\mathsf{A}} \right], \left[ \frac{\mathsf{B}}{\mathsf{ABA}} \right], \left[ \frac{\mathsf{AA}}{\mathsf{A}} \right] \right\}\] is a match since the string \(\mathsf{AABAA}\) occurs both on the top and bottom.

Consider the following set of tiles: \[\left\{ \left[ \frac{\mathsf{X}}{\mathsf{U}} \right], \left[ \frac{\mathsf{UU}}{\mathsf{U}} \right], \left[ \frac{\mathsf{Z}}{\mathsf{X}} \right], \left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right], \left[ \frac{\mathsf{Y}}{\mathsf{U}}\right], \left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right] \right\}.\]

1. What tile must a match begin with?

Since a match should have the same sequence on the top and the bottom, the beginning tile must have the same start letter at the top and at the bottom.

The only tile that meets this requirement is \(\left[ \frac{\mathsf{UU}}{\mathsf{U}} \right]\), so any match must begin with this.

From (a), we need to start with \(\left[ \frac{\mathsf{UU}}{\mathsf{U}} \right]\).

In order to be a match, another \(\mathsf{U}\) is needed on bottom, therefore the next tile should be \(\left[ \frac{\mathsf{X}}{\mathsf{U}} \right]\), or \(\left[ \frac{\mathsf{Y}}{\mathsf{U}} \right]\).

If we continue with \(\left[ \frac{\mathsf{X}}{\mathsf{U}} \right]\), then the next tile must have an \(\mathsf{X}\) at the bottom, so it must be \(\left[ \frac{\mathsf{Z}}{\mathsf{X}} \right]\).

We now need a \(\mathsf{Z}\) at the bottom, so the next tile must be \(\left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right]\).

Since we’ve reached four tiles, we have a first solution, namely the list \[\left\{ \left[ \frac{\mathsf{UU}}{\mathsf{U}} \right], \left[ \frac{\mathsf{X}}{\mathsf{U}} \right], \left[ \frac{\mathsf{Z}}{\mathsf{X}} \right], \left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right] \right\}.\]

If, after \(\left[ \frac{\mathsf{UU}}{\mathsf{U}} \right]\), we instead continue with \(\left[ \frac{\mathsf{Y}}{\mathsf{U}} \right]\), the next tile must have a \(\mathsf{Y}\) at the bottom, so it should be \(\left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right]\).

Now we need a \(\mathsf{Z}\) at the bottom, so we must continue with \(\left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right]\).

Therefore we have a second solution, namely the list \[\left\{ \left[ \frac{\mathsf{UU}}{\mathsf{U}} \right], \left[ \frac{\mathsf{Y}}{\mathsf{U}} \right], \left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right], \left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right] \right\}.\]

1. Suppose we replace the tile \(\left[ \frac{\mathsf{E}}{\mathsf{ZE}} \right]\) with \(\left[ \frac{\mathsf{E}}{\mathsf{ZZZE}} \right]\). What is the least number of tiles that can be used in a match? How many different matches are there using this smallest number of tiles? [Hint: you may find it easiest to construct your matches backwards from right to left.]

Let’s do as suggested, and construct our matches backwards, from right to left.

So we start with \(\left[ \frac{\mathsf{E}}{\mathsf{ZZZE}} \right]\), and we need three \(\mathsf{Z}\)s in the left-hand side, at the top.

So we can continue with either \(\left[ \frac{\mathsf{Z}}{\mathsf{X}} \right]\) or \(\left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right]\).

Since afterwards we need to continue with \(\left[ \frac{\mathsf{X}}{\mathsf{U}} \right]\) or \(\left[ \frac{\mathsf{Y}}{\mathsf{U}} \right]\), respectively, and the only continuation will be \(\left[ \frac{\mathsf{UU}}{\mathsf{U}} \right]\), anything we choose will lead to the same number of tiles used.

We will therefore, continue with three copies of \(\left[ \frac{\mathsf{Z}}{\mathsf{X}} \right]\), and after that we need three \(\mathsf{X}\)s at the top so we add three copies of \(\left[ \frac{\mathsf{X}}{\mathsf{U}} \right]\).

Now we need three more \(\mathsf{U}\)s on the top, so we add three copies of \(\left[ \frac{\mathsf{UU}}{\mathsf{U}} \right]\).Therefore, the minimum number of tiles we need to construct a match is 10.

To the left of \(\left[ \frac{\mathsf{E}}{\mathsf{ZZZE}} \right]\) we can put any of \(\left[ \frac{\mathsf{Z}}{\mathsf{X}} \right]\) or \(\left[ \frac{\mathsf{Z}}{\mathsf{Y}} \right]\) in each of the next three positions, and, after that, we have only one way to continue (for each case), so there are \(2^3=8\) matches using the smallest number of tiles.

Consider a new set of tiles \(\left\{ \left[ \frac{\mathsf{XXXXXXX}}{\mathsf{X}} \right], \left[ \frac{\mathsf{X}}{\mathsf{XXXXXXXXXX}} \right] \right\}\).

The first tile has seven \(\mathsf{X}\)s on top, and the second tile has ten \(\mathsf{X}\)s on the bottom.

1. For which numbers \(n\) do there exist matches using \(n\) tiles? Briefly justify your answer.

If we use \(a\) tiles of the form \(\left[ \frac{\mathsf{XXXXXXX}}{\mathsf{X}} \right]\) and \(b\) tiles of the form \(\left[ \frac{\mathsf{X}}{\mathsf{XXXXXXXXXX}} \right]\) then we will have \(7a+b\) \(\mathsf{X}\)s on the top and \(10b+a\) \(\mathsf{X}\)s at the bottom.

In order to be a match, we need to have the same number of \(\mathsf{X}\)s at the top and at the bottom, which means that \(7a+b=10b+a\).

Therefore, \(6a=9b\), which implies \(2a=3b\). Since \(a\) and \(b\) are numbers of tiles, they should be natural numbers and, hence, \(a=3k\) and \(b=2k\) for some natural \(k\), and such values will work.

Thus, in order to have a match we should use \(a+b=5k\) tiles, for some natural \(k\). So there exist matches using \(n\) tiles if and only if \(n\) is a multiple of 5.
