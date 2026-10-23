---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8279
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8279
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8279
  old_site_id: Q173
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q6
task: T-UGM-IMPORT-6
---

# The liar, the switcher and the truth-teller; who's who?

## Question

1. A, B and C are three people. One of them is a liar who always tells lies, another is a saint who always tells the truth, and the third is a switcher who sometimes tells the truth and sometimes lies. They make the following statements: A: I am the liar.
 B: A is the liar.
 C: I am not the liar. Who is the liar among A, B and C? Briefly explain your answer.

---

1. P, Q and R are three more people, one a liar, one a saint, and the third a contrarian who tells a lie if he is the first to speak or if the preceding speaker told the truth, but otherwise tells the truth. They make the following statements: P: Q is the liar.
 Q: R is the liar.
 R: P is the liar. Who is the liar among P, Q and R? Briefly explain your answer.

---

1. X, Y and Z are three more people, one a liar, one a switcher and one a contrarian. They make the following statements: X: Y is the liar.
 Y: Z is the liar.
 Z: X is the liar.
 X: Y is the liar.
 Y: X is the liar. Who is the liar among X, Y and Z? Briefly explain your answer.

## Solution

A cannot be the liar, since then he would have told the truth, and A cannot be the saint because then he would have lied. Therefore A must be the switcher.

B is therefore lying, so is the liar. C is telling the truth and is the saint.

We can show this reasoning in a table. The top half of the table shows the six possible combinations of T (truth-telling saint), L (liar) and S (switcher). The bottom half shows which combinations become impossible at each step in the conversation.

| A is B is C is | T L S | T S L | L T S | L S T | S T L | S L T |
|---|---|---|---|---|---|---|
| A says A=L | x | x | x | x | \(\checkmark\) | \(\checkmark\) |
| B says A=L | – | – | – | – | x | \(\checkmark\) |
| C says C \(\neq\) L | – | – | – | – | – | \(\checkmark\) |

Again, we draw up a table, this time using C to mean contrarian.

| P is Q is R is | T L C | T C L | L T C | L C T | C T L | C L T |
|---|---|---|---|---|---|---|
| P says Q=L | \(\checkmark\) | x | \(\checkmark\) | \(\checkmark\) | \(\checkmark\) | x |
| Q says R=L | \(\checkmark\) | – | x | x | \(\checkmark\) | – |
| R says P=L | x | – | – | – | \(\checkmark\) | – |

The only possible combination is PQR=CTL. Let’s check that this is consistent with the statements.

P: Q is the liar. (FALSE. Consistent with P=contrarian, so lies if speaks first.)
 Q: R is the liar. (TRUE. Consistent with Q=saint.)
 R: P is the liar. (FALSE. Consistent with R=liar.)

So R is the liar.

| X is Y is Z is | L S C | L C S | S L C | S C L | C S L | C L S |
|---|---|---|---|---|---|---|
| X says Y=L | \(\checkmark\) | \(\checkmark\) | \(\checkmark\) (truth) | \(\checkmark\) (lie) | \(\checkmark\) | x |
| Y says Z=L | \(\checkmark\) (lie) | x | \(\checkmark\) | \(\checkmark\) | \(\checkmark\) (truth) | – |
| Z says X=L | \(\checkmark\) | – | x | \(\checkmark\) | \(\checkmark\) | – |
| X says Y=L | \(\checkmark\) | – | – | \(\checkmark\) (lie) | x | – |
| Y says X=L | \(\checkmark\) | – | – | x | – | – |

Let’s check LSC is consistent.

X: Y is the liar. (FALSE, consistent with X=liar).
 Y: Z is the liar. (FALSE, consistent with Y=switcher).
 Z: X is the liar. (TRUE, consistent with Z=contrarian, previous statement was false).
 X: Y is the liar. (FALSE, consistent with X=liar).
 Y: X is the liar. (TRUE, consistent with Y=switcher).

So X is the liar.
