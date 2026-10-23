---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6463
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6463
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6463
  old_site_id: Q159
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q6
task: T-UGM-IMPORT-6
---

# How many ways to arrange the saints and liars are there?

## Question

In the questions below, the people involved make statements about each other. Each person is either a saint (S) who always tells the truth or a liar (L) who always lies.

1. Six people, \(P_1, P_2,\dots,P_6\) sit in order around a circular table with \(P_1\) sitting to \(P_6\)’s right, as shown in the diagram below.     Suppose all six people say “the person directly opposite me is telling the truth”. One possibility is that all six are lying. But, in total, how many different possibilities are there? Explain your reasoning. Suppose now that all six people say “the person to my left is lying”. In how many different ways can this happen? Explain your reasoning.

---

1. Now \(n\) people \(Q_1\), \(Q_2\), …, \(Q_n\) sit in order around a circular table with \(Q_1\) sitting to \(Q_n\)’s right.  Suppose that all \(n\) people make the statement “the person on my left is lying and the person on my right is telling the truth”. Explain why everyone is lying. Suppose now that every person makes the statement “either the people to my left and right are both lying or both are telling the truth”. If at least one person is lying, show that \(n\) is a multiple of three.

## Solution

If two people say about each other, ‘The other person is telling the truth,’ what are the possibilities?

They could both be lying, or both telling the truth.

But we can’t logically have the situation where one is truthful, but the other is not.

So we have two possible situations, one where they are both saints, and one where they are both liars.

If we have three such pairs, as in the question, then the number of possible arrangements is \(2^3 = 8\).

If \(P_1\) is a saint, then \(P_6\) to their left must be a liar.

But then the person to \(P_6\)’s left must be a saint, followed by a liar, by a saint…

So starting at \(P_1\), we have SLSLSL as a possibility moving left, where L stands for ‘liar’, and S for ‘saint’.

Alternatively \(P_1\) is a liar, which gives us LSLSLS moving left.

So there are only two ways in which this situation could occur.

Suppose that one person around the table is a saint.

The person on their right must also be a saint.

But this person is claiming our initial saint is a liar.

So we have a contradiction, and we must have no saints, and everybody is a liar.

To conclude, we need to check that the situation where everyone is a liar is consistent.

It *is* possible for everyone to be a liar, since the statement “the person on my right is telling the truth” becomes a lie for everyone.

Let’s start with a person who is lying, say \(Q_1\).

Since \(Q_1\) is lying, one of his immediate neighbours is a liar and the other, say \(Q_2\), is a saint.

The saint \(Q_2\) must have on their other side a liar, \(Q_3\). The liar \(Q_3\) is next to the saint \(Q_2\) and next to \(Q_4\) who must therefore be a liar. The next person \(Q_5\) must be a saint and so on.

So starting with a liar, the pattern LLSLLSLLS… is formed around the table.

This can only connect up to create a circle without contradiction if \(n\) is a multiple of \(3\).
