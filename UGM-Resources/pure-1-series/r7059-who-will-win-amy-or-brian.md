---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7059
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7059
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7059
  old_site_id: Q228
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2012, Q7
task: T-UGM-IMPORT-6
---

# Who will win, Amy or Brian?

## Question

Amy and Brian play a game together, as follows. They take it in turns to write down a number from the set \(\{ 0,1,2 \}\), with Amy playing first. On each turn (except Amy’s first turn), the player must not repeat the number just played by the previous player.

In their first version of the game, Brian wins if, after he plays, the sum of all the numbers played so far is a multiple of \(3\). For example, Brian will win after the sequence \[(2,0)\; (1,2)\; (1,0)\] (where we draw a bracket around each round) because the sum of the numbers is \(6\). Amy wins if Brian has not won within five rounds; for example, Amy wins after the sequence \[(2,0)\; (1,2)\; (1,2)\; (0,2)\; (1,2)\]

1. Show that if Amy starts by playing either \(1\) or \(2\), then Brian can immediately win.

---

1. Suppose, instead, Amy starts by playing \(0\). Show that Brian can always win within two rounds.

They now decide to change the rules so that Brian wins if, after he plays, the sum of all the numbers played so far is *one less than a multiple of \(3\)*. Again, Amy wins if Brian has not won within five rounds. It is still the case that a player must not repeat the number just played previously.

1. Show that if Amy starts by playing either \(0\) or \(2\), then Brian can immediately win.

---

1. Suppose, instead, Amy starts by playing \(1\). Explain why it cannot benefit Brian to play \(2\), assuming Amy plays with the best strategy.

---

1. So suppose Amy starts by playing \(1\), and Brian then plays \(0\). How should Amy play next?

---

1. Assuming both play with the best strategies, who will win the game? Explain your answer.

## Solution

If Amy plays \(1\), Brian can play \(2\) and win; similarly if Amy plays \(2\), Brian can play \(1\) and win.

If Amy starts with \(0\), Brian can play \(1\).

Then Amy can play \(0\) or \(2\). If she plays \(0\), Brian plays \(2\) and wins; if she plays \(2\), Brian plays \(0\) and wins.

If Amy starts with \(0\), and Brian plays \(2\), then Amy can play \(1\), in which case Brian plays \(0\) and wins; if she plays \(0\), then Brian plays \(1\) and wins.

If Amy plays \(0\), Brian plays \(2\) and wins; if Amy plays \(2\), Brian plays \(0\) and wins.

If Amy plays \(1\) and Brian plays \(2\), the game is essentially reset to \(0\) (as \(1+2\) is a multiple of \(3\)).

Amy can then play \(1\) again, leaving Brian in the same position but now with fewer turns to win.

If Amy plays \(1\), Brian can play \(0\) and win, so Amy should play \(2\).

As shown in the previous parts, the game will start with \((1,0)\; (2,\dots)\;\).

If Brian plays \(0\), the game is essentially reset, with no advantage to him. So Brian’s only chance is to play \(1\).

We then have \((1,0)\; (2,1)\). If Amy plays \(0\), Brian can play \(1\) and win. So Amy’s only chance is to play \(2\).

But we’re now in a cycle, leading to \((1,0)\;(2,1)\;(2,1)\;(2,1)\;(2,1)\), giving a win for Amy; Brian is powerless to stop this.

Our conclusion is that if Amy plays with her best strategy, she’ll win.
