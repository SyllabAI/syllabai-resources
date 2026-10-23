---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5848
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5848
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5848
  old_site_id: Q1048
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
  exam_reference: O&C O level MEI Additional Mathematics 1, 1969, Q15
task: T-UGM-IMPORT-6
---

# How many students took French, Latin and German?

## Question

In an examination, candidates could take any one, any two or all of Latin, French and German.

Out of \(100\) candidates \(4\) took Latin only, \(13\) took French only and \(12\) took German only. There were \(5\) who took all three languages and \(20\) who did not take French.

The average mark in French of all of the candidates who took this subject was \(50\)%. Within this group there were the following average marks in French:

\(\qquad\) Those taking French only, \(57\)%.

\(\qquad\) Those taking French and Latin, \(45\)%.

\(\qquad\) Those taking French and German, \(52\)%.

\(\qquad\) Those taking all three languages, \(35\)%.

Calculate the number who took Latin and German, the number who took French and Latin and the number who took French and German.

## Suggestion

There is a lot of information in this question. It might help to draw a Venn diagram with a Latin bubble, a French bubble, and a German bubble so that these overlap.

If we fill in the number of people in each region, can we then write down relationships between the remaining unknown numbers?

If we know the average number of marks received per candidate in French, can we find out how many marks were earned by the candidates in French in total?

## Solution

Let’s summarise with a Venn diagram.

Note that the question doesn’t allow for someone not taking any of the three languages. Everyone here takes at least one language.

The question tells us that \(20\) candidates didn’t take French. Therefore 20 candidates took only Latin, only German, or Latin and German.

From our diagram, we see that this means \[4+12+x=20,\] and so \(x=4\).

Let’s use that the total number of candidates is

\(100\)

. We find that

\[4+13+12+4+y+z+5=100,\]

which means that

\[\begin{equation}\label{eq:eqn1} y+z=62. \end{equation}\]

What about the averages? We have that \(80\) candidates took French, and their average mark was \(50\), so the total number of marks earned was \(4000\).

Note now that when the question says ‘French and German’ it means ‘French and German but not Latin’.

Since the average mark of those taking only French was \(57\), and \(13\) candidates only took French, this accounts for \(57\times 13=741\) marks.

The total marks earned by those taking French and Latin is \(45y\).

The total number of marks earned by those taking French and German is \(52z\).

Finally, the number of marks earned by those taking all three languages is \(35\times 5=175\).

This tells us that \[4000=741+45y+52z+175.\]

Rearranging \(\eqref{eq:eqn1}\), we find that \(z=62-y\), and on substituting this in, we have \[4000=741+45y+52(62-y)+175,\] which yields \[7y=140,\] and so \(y\) is \(20\), and \(z\) is \(62-20=42\).

Our completed Venn diagram looks like this:

So the number who took Latin and German is \(4\), the number who took French and Latin is \(20\), and the number who took French and German is \(42\).
