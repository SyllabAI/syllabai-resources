---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6093
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6093
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6093
  old_site_id: Q143
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
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q6
task: T-UGM-IMPORT-6
---

# Does Alice like wine or beer?

## Question

1. Alice, Bob, Charlie and Dianne each make the following statements: **Alice**: I am telling the truth. **Bob**: Alice is telling the truth. **Charlie**: Bob is telling the truth. **Dianne**: Charlie is lying. Only one of the four people is telling the truth. Which one? Explain your answer.

---

1. They now make the following statements: **Alice**: Bob is lying. **Bob**: Charlie is lying. **Charlie**: I like beer. **Dianne**: 2+2=4. Now two of the four people are telling the truth. Which two? Explain your answer.

---

1. They are now joined by Egbert. They each make the following statements: **Alice**: I like wine. **Bob**: Charlie is lying. **Charlie**: Alice is lying. **Dianne**: Alice likes beer. **Egbert**: Alice likes beer. Now three of the five people are telling the truth. Which ones? Explain your answer.

## Solution

If Alice is telling the truth then so is Bob. But we are told that only one person is telling the truth, so this is a contradiction.

If Bob is telling the truth, then so is Alice—again, a contradiction.

If Charlie is telling the truth, then so are Bob and Alice.

But if Dianne is telling the truth, then the others are lying, which is consistent. So Dianne is the one telling the truth.

Dianne is clearly telling the truth.

Does Charlie like beer? If he does, then he is telling the truth, so Bob is lying and Alice is telling the truth. But this gives three people telling the truth which is not allowed.

If Charlie doesn’t like beer, then he’s lying, Bob is telling the truth, and Alice is lying, so just Bob and Dianne are telling the truth. This is our answer.

Dianne and Egbert are either both telling the truth or both lying.

If they are both lying, then the other three must all be telling the truth. But if Charlie tells the truth, Alice must be lying, so we have a contradiction.

Therefore Dianne and Egbert are both telling the truth. Now one of Alice, Bob and Charlie must be telling the truth, and the other two must be lying.

If Charlie is lying, then both Alice and Bob must be telling the truth. But altogether this would give four people telling the truth, a contradiction.

So Charlie must be telling the truth, which means Alice and Bob are both lying.

Alternatively, we can draw up a table for the various cases. Clearly we have exactly three truthful people only when Alice likes beer but not wine.

| Alice… | does not like wine or beer | likes wine but not beer | likes beer but not wine | likes wine and beer |
|---|---|---|---|---|
| A truthful? | No | Yes | No | Yes |
| B truthful? | No | Yes | No | Yes |
| C truthful? | Yes | No | Yes | No |
| D truthful? | No | No | Yes | Yes |
| E truthful? | No | No | Yes | Yes |
