---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6707
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6707
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6707
  old_site_id: Q4025
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
  exam_reference: O&C O level Elementary Mathematics 1 (St Dunstan's College), 1964, Q6
task: T-UGM-IMPORT-6
---

# Can we find how many boys study French, Latin and German?

## Question

In a certain school there are \(127\) boys in one particular year. They may study one or more (or none) of the languages Latin, French, and German. No boys study both Latin and German; \(18\) study both French and German, half as many French and Latin; \(21\) study Latin only; \(70\) study a language but not German; \(82\) study one or more of the two modern languages. By using Venn diagrams, or otherwise, find how many boys study each language and how many study none.

## Suggestion

Which of the areas in the Venn diagram can you fill in straight away from the information above?

How can we manage the remaining areas?

## Solution

Let us start with writing all numbers into a Venn diagram which we get immediately from the question.

Now we also know that \(70\) study a language but not German, which means that \(40\) study French alone.

Now if \(82\) study one or more of the two modern languages, \(15\) must study German alone.

Adding up, that leaves \(24\) out of \(127\) studying no languages at all.

Thus \(67\) study French, \(33\) study German, \(30\) study Latin, and \(24\) study no languages at all.
