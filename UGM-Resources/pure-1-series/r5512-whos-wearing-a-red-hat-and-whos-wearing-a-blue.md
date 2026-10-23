---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5512
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5512
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5512
  old_site_id: Q188
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2012, Q6
task: T-UGM-IMPORT-6
---

# Who's wearing a red hat and who's wearing a blue?

## Question

Alice, Bob and Charlie are well-known expert logicians; they always tell the truth.

They are sat in a row, as illustrated above. In each of the scenarios below, their father puts a red or blue hat on each of their heads. Alice can see Bob’s and Charlie’s hats, but not her own; Bob can see only Charlie’s hat; Charlie can see none of the hats. All three of them are aware of this arrangement.

1. Their father puts a hat on each of their heads and says: “Each of your hats is either red or blue. At least one of you has a red hat.” Alice then says “I know the colour of my hat.” What colour is each person’s hat? Explain your answer.

---

1. Their father puts a new hat on each of their heads and again says: “Each of your hats is either red or blue. At least one of you has a red hat.” Alice then says “I don’t know the colour of my hat.” Bob then says “I don’t know the colour of my hat.” What colour is Charlie’s hat? Explain your answer.

---

1. Their father puts a new hat on each of their heads and says: “Each of your hats is either red or blue. At least one of you has a red hat, and at least one of you has a blue hat.” Alice says “I know the colour of my hat.” Bob then says “Mine is red.” What colour is each person’s hat? Explain your answer.

---

1. Their father puts a new hat on each of their heads and says: “Each of your hats is either red or blue. At least one of you has a red hat, and at least one of you has a blue hat.” Alice then says “I don’t know the colour of my hat.” Bob then says “My hat is red.” What colour is Charlie’s hat? Explain your answer.

---

1. Their father puts a new hat on each of their heads and says: “Each of your hats is either red or blue. Two of you who are seated adjacently both have red hats.” Alice then says “I don’t know the colour of my hat.” What colour is Charlie’s hat? Explain your answer.

## Solution

Alice only knows the colours of the other two hats, and that at least one hat is red.

From this she has deduced the colour of her own hat, so Bob and Charlie’s hats must be BB (both blue) - if Bob and Charlie are RR or RB or BR, this won’t help Alice enough to be sure of her own hat.

Therefore she must have deduced that she was wearing the one red hat.

Alice doesn’t know the colour of her hat, and so either Bob, Charlie or both has a red hat.

Bob, knowing this, and knowing the colour of Charlie’s hat, still doesn’t know the colour of his own hat.

This means that Charlie must have a red hat - if he has a blue one, Bob can deduce his own hat is red.

Alice knows the colours of Bob and Charlie’s hats, and that there’s at least one hat of each colour.

From this she has deduced the colour of her own hat, so Bob and Charlie must have the same colour hats, and Alice has the other colour.

Bob knows this, and knows the colour of Charlie’s hat, which must be red, allowing Bob to deduce his own hat is red.

Therefore Alice’s hat is blue, Bob’s is red, and Charlie’s is also red.

1. Their father puts a new hat on each of their heads and says: " Each of your hats is either red or blue. At least one of you has a red hat, and at least one of you has a blue hat." Alice then says “I don’t know the colour of my hat.” Bob then says “My hat is red.” What colour is Charlie’s hat? Explain your answer.

Alice knows that there is at least one hat of each colour, and she can see the colours of Bob’s and Charlie’s hats.

She can’t deduce the colour of her own hat, so Bob and Charlie must have different coloured hats.

Bob knows this, and can see the colour of Charlie’s hat.

Therefore Charlie’s hat must be blue, allowing Bob to deduce that his own hat is red.

The only possibilities are RRB, BRR, and RRR.

The first of these enables Alice to deduce she has a red hat, so this can’t happen.

Therefore Bob and Charlie must both have red hats.
