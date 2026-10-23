---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7878
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7878
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7878
  old_site_id: Q177
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2011, Q7
task: T-UGM-IMPORT-6
---

# Who should win the game HT-2?

## Question

Alice and Bob have a large bag of coins which they use to play a game called HT-2. In this game, Alice and Bob take turns placing one coin at a time on the table, each to the right of the previous one; thus they build a row of coins that grows to the right. Alice always places the first coin. Each coin is placed head-up (H) or tail-up (T), and cannot be flipped or moved once it has been placed.

A player loses the game if he or she places a coin that results in two adjacent coins having the same pattern of heads and tails as another adjacent pair somewhere in the row (reading a pattern from left to right). For example, Bob has lost this game by producing a second instance of HT (where \(a\) and \(b\) denote coins placed by Alice and Bob respectively): \[\begin{array}{cccccc} a&b&a&b&a&b\\ H&H&T&T&H&T \end{array}\] and Alice has lost this game by producing a second instance of TT (overlapping pairs can count as repeats): \[\begin{array}{ccccc} a&b&a&b&a\\ T&H&T&T&T \end{array}\]

1. What is the smallest number of coins that might be placed in a game of HT-2 (including the final coin that causes a player to lose)? What is the largest number? Justify each answer.

---

1. Bob can always win a game of HT-2 by adopting a particular strategy. Describe the strategy.

For any positive integer \(n\), there is a game HT-\(n\) with the same rules as HT-2, except that the game is lost by a player who creates an unbroken sequence of \(n\) heads and tails that appears elsewhere in the row. For example, Bob has lost this game of HT-3 by producing a second instance of THT: \[\begin{array}{cccccccc} a&b&a&b&a&b&a&b\\ H&H&T&T&H&T&H&T \end{array}\]

1. Suppose \(n\) is odd, and Bob chooses to play by always duplicating Alice’s previous play (and Alice knows that this is Bob’s strategy). Show that Alice can always win.

In these games, a maximum time of one minute is allowed for each turn.

1. Can we be certain that a game of HT-6 will be finished within two hours? Justify your answer.

## Solution

Let’s start with the shortest game. Certainly a game of HT-2 will never end after two or fewer moves (since then we’ve only had at most one pair).

Could a game end after three moves? Then we have two consecutive pairs, coins 1 and 2, and coins 2 and 3.

For the game to end, we need both pairs to be the same. If all three coins match - HHH or TTT - this happens.

So the smallest number of coins in a game is three.

Now the longest game. There are four possible consecutive pairs, HH, HT, TH, TT.

So the longest possible game has at most five consecutive pairs (this is because of the [pigeonhole principle](https://undergroundmathematics.org/glossary/pigeonhole-principle)).

A game with five consecutive pairs has length 6. So all games have a length of at most 6.

But is a game of length 6 possible? The game HHTTHT would be an example (the first four pairs, HH, HT, TT, TH, are all different, and the fifth is a repeat of HT).

So the largest number of coins in a game is 6.

On both his first two turns (if the game gets that far), Bob should pick the same coin that Alice does on her first turn.

Let’s assume Alice picked heads first (exactly the same argument works for tails); so far we have HH.

If Alice plays heads next, she loses. If Alice plays tails next, we have HHT, and Bob plays heads again, giving HHTH.

Then if Alice plays tails, we have HHTHT, so HT is duplicated and Alice loses.

If Alice plays heads, we have HHTHH, so HH is duplicated and Alice loses.

So regardless of Alice’s strategy, Bob always wins.

One way to guarantee a win for Alice is for her to pick heads on every turn (or tails on every turn).

After \(n\) turns in the game, Alice will have just completed an unbroken sequence of \(n\) heads.

Then on Bob’s turn, he will copy Alice and play another head, creating a second unbroken sequence of \(n\) heads, from the second to the \((n+1)^{th}\) coin.

So Bob will always lose.

The total number of different ways we can have a sequence of \(6\) coins is \(2^6\), since there are two choices, heads or tails, for the first coin, two for the second, and so on.

So a game cannot have more than \(2^6+1\) sequences of \(6\) coins, again by the pigeonhole principle.

This means that a game cannot have more than \(2^6+6=70\) moves (the first sequence of six coins appears after the sixth move, and thereafter a new sequence is generated on every move).

Hence the game will not take more than \(70\) minutes, and will certainly be finished within two hours.
