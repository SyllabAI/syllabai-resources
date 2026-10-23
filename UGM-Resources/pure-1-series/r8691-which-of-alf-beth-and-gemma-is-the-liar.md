---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8691
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8691
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8691
  old_site_id: Q102
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q6
task: T-UGM-IMPORT-6
---

# Which of Alf, Beth and Gemma is the liar?

## Question

Three people called Alf, Beth, and Gemma, sit together in the same room.

One of them always tells the truth.
 One of them always tells a lie.
 The other one tells truth or lies at random.

In each of the following situations, your task is determine how each person acts.

1. Suppose that Alf says “I always tell lies” and Beth says “Yes, that’s true, Alf always tells lies”. Who always tells the truth? Who always lies? Briefly explain your answer.

---

1. Suppose instead that Gemma says “Beth always tells the truth” and Beth says “That’s wrong.” Who always tells the truth? Who always lies? Briefly explain your answer.

---

1. Suppose instead that Alf says “Beth is the one who behaves randomly” and Gemma says “Alf always lies”. Then Beth says “You have heard enough to determine who always tells the truth”. Who always tells the truth? Who always lies? Briefly explain your answer.

## Solution

First, if Alf is telling the truth, we have a contradiction. So Alf must be, on this occasion, lying. So either Alf always lies, or he lies at random.

If Alf always lies, he’s telling the truth on this occasion, another contradiction. So by process of elimination, Alf is the random liar.

Now Beth says that Alf always tells lies—but we’ve just figured out that this isn’t true, so Beth is lying on this occasion, and must therefore always tell lies since Alf is the random liar.

We get: Alf lies at random, Beth always lies, and Gemma always tells the truth.

There are 6 possible combinations, we could present this reasoning as a table considering each statement in turn against these. We place a cross wherever a contradiction arises.

In these tables, R stands for random-truth-and-lie-teller, L for liar, and T for truth-teller.

| A is B is G is | T R L | T L R | R T L | R L T | L T R | L R T |
|---|---|---|---|---|---|---|
| A says A=L | x | x | \(\checkmark\) | \(\checkmark\) | x | x |
| B says A=L | – | – | x (know A=R) | \(\checkmark\) | – | – |

Showing the result we argued above.

Consider Gemma’s statement, “Beth always tells the truth.” If it’s true then Gemma has spoken a truth and can’t be the liar. If it’s false then both Beth and Gemma lie at least some of the time. So either Beth is the truth-teller and Gemma is random, or Beth is random and Gemma the liar.

Beth then contradicts Gemma. If Beth is the truth-teller then Gemma’s statement is false so Beth is not the truth-teller—a contradiction.

We are left with only one option: Beth is random, Gemma is the liar and Alf the truth-teller.

Gemma cannot be the truth teller. So Gemma is lying on this occasion, and Beth is telling the truth on this occasion. Since Beth does not always tell the truth, she must lie at random, and so Gemma always lies. Beth says this isn't true, so she can't be the liar as she would be telling the truth on this occasion so she must only lie at random, but she can't always tell the truth as then contradicting Gemma would be a lie.

| A is B is G is | T R L | T L R | R T L | R L T | L T R | L R T |
|---|---|---|---|---|---|---|
| G says B=T | \(\checkmark\) (G lie) | \(\checkmark\) | x | x | \(\checkmark\) (G true) | x |
| B says B \(\neq\) T | \(\checkmark\) (B true) | x | – | – | x | – |

Using the earlier conventions we can fill in a table as before:

| A is B is G is | T R L | T L R | R T L | R L T | L T R | L R T |
|---|---|---|---|---|---|---|
| A says B=R | \(\checkmark\) | x | \(\checkmark\) (lie) | \(\checkmark\) (lie) | \(\checkmark\) | x |
| G says A=L | \(\checkmark\) | – | \(\checkmark\) | x | \(\checkmark\) | – |
| B states one solution only | \(\checkmark\) (lie: still 3) | – | x | – | x | – |

Just before Beth speaks, we have three possible combinations, so what she says is a lie. She cannot therefore be the truth-teller and this eliminates two options. Once she has spoken it, her statement in a sense becomes true!

We conclude that Alf always tells the truth, Beth lies at random and Gemma always lies.

Alf's statement could be true meaning Beth cannot be the total liar or it could be a lie ruling out the only other combination with Beth as the random truth teller, but no others. Gemma's statement then rules out Alf being the random liar since if Gemma is definitely telling the truth, Alf is definitely the liar so she must be telling the truth on this occasion, but not necessarily always, but if she's lying all other combinations are still possible. At this point in the table we have three columns still active and Beth states that we know the answer, but we don't so she is lying closing off both the options with her telling the truth and we are left with one, so although she was lying she is now paradoxically telling the truth! So

If we tried to do this by checking in turn starting with Alf being the truth teller we would verify straight away that it is a possible solution but we would need to check the other combinations to discover whether Beth's statement was true in fact and the possibility of the other combinations would reveal Beth's lie.
