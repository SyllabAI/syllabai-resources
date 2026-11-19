# P16 — LIT-21 OPENING LANE

**State: SHIPPED 2026-11-20 — resources PR → `videos/p16-lit21-opening`, hub PR → `t-videomap-p16/run-001`.**
**Authorization: owner decision 2026-11-20 "**open lit-21**" — the P12 terminal declaration is overturned for `cie-igcse-english-literature-21` (that course ONLY), and the RESERVED lit-0475 sets accumulated by P14+P15 are adjudicated onto the freshly opened course.**
**Delegated self-review per owner chat 2026-11-09 "approve and review yourself".**

## The decision point this lane closes

P12 (shipped 2026-11-14) declared the honest-empty remainder TERMINAL — 11 courses with no
mapping content ever surfaced, `cie-igcse-english-literature-21` (CIE IGCSE Literature in English
0475) among them. P14 then surfaced the FIRST lit-21 content ever seen (IGCSESUCCESS 0475 ×9 —
RESERVED), and P15 grew the reserved set to 252 titles (Claire's Notes ×243, the whole pool
gated at the content-level lit register). Both lanes ledgered the sets as RESERVED pending an
owner decision that only the owner could make: open the course, or keep it terminal. The owner
ruled OPEN on 2026-11-20.

## Pool of record

| source | uploads | reserved | keeps |
| --- | --- | --- | --- |
| IGCSESUCCESS (`UCXxbJOZLFMEh304aa4rA-zg`, P14 inventory) | 279 | 9 (re-derived by the committed `p14_judgment.py` predicate) | 2 (Wind → the three Hughes pair-lines; A Streetcar Named Desire → the 2024/2025 drama specs) |
| Claire's Notes (`UCDHUKn14qPhrkV6fBpyOBtw`, P15 inventory; ids == `scripts/p15/reserved.json`) | 243 | 243 | 98 |
| **total** | **252 accounts** | **252** | **100 rows / 100 videos** |

Exactly-once disposition of all 252, 0 collisions machine-checked (`scripts/p16/judgment_summary.json`).

## Judgment law of record — Class W (set-text work bind)

The lit-21 spine is the 0475 **2023-2025 set-text syllabus**: Songs of Ourselves Vol 1 Part 4 /
Vol 2 Part 4 / Vol 2 **Part 3** poem lists, the Ted Hughes 15 (two poems per spec line), the prose
novels, the Stories of Ourselves Vol 2 per-year lists, and the per-year drama set texts — 203 spec
points (`S3.x`/`S5.x`/…/`S25.x`), three examination-year blocks.

- **Bind rule (suffix-anchored):** a spine work binds a title work-span iff the span EQUALS the
  work, ENDS WITH it at a word boundary (marketing prefixes strip cleanly: "Master The Telephone
  Call…"), or the title dropped a leading article ("City Planners" → spine "The City Planners").
  Mid-phrase coincidences ("night sweat" inside "The Man with Night Sweats") and cross-work
  subsets ("planners" inside "The City Planners") do NOT bind. Word-internal apostrophes are
  content ("Dr Heidegger's Experiment", "Thank You M'am").
- **Multi-year occurrences:** a set text repeated across the year blocks binds ALL its spec
  points, disclosed per row (df=N — the P13 shared-unit precedent: a repeated set text is not a
  discriminative ambiguity). Othello → 4 specs (2023+2024 papers), A Streetcar Named Desire → 4
  (2024+2025), SoO Vol 1 P4 / Hughes / Vol 2 P4 poems → 3 or 2, SoO Vol 2 Part 3 poems → 1 (2025
  only), Journey's End / Twelfth Night → 2 (2023 only).
- **Confidence:** medium when the title carries author+work matching the spine line; low under
  the title-only posture (work-only scene commentary; multi-work tips rows bound as ONE
  multi-spec row — the four-gate topic-lecture class analog).
- **boardMismatch true** on every spec row (the committed builder law for the title-only
  posture). No paper-code anchors — no session codes in the reserved titles.

## Result

**100 owner-reviewed rows onto the freshly opened course — 101 of 203 spec points mapped
(56 medium / 44 low), the course's first video-map file.** Coverage highlights: the full
Songs of Ourselves Vol 2 Part 3 list (2025 poetry, 15/15 of that section's poem lines incl. all
12 Claire's guides), the Ted Hughes 15 (all 8 pair-lines × 3 year blocks), Othello scene-by-scene
commentary ×23, A Midsummer Night's Dream ×5, Journey's End ×8 (2023), Twelfth Night ×2 (2023),
the Stories of Ourselves story guides ×10, the SoO Vol 1 P4 poem guides ×12 + 3 multi-work tips
rows, Ozymandias (the multi-board guide that names Cambridge iGCSE), Funeral Blues / Rain /
Night Sweat / The Capital / Plaits / Children of Wealth / an afternoon nap.

Identity: **oEmbed 100/100 author==channel-of-record** (0 mismatch, 0 dead, 0 thumbnail
fallbacks; UC ids from the committed inventories).

## Honest skips — 152, ledgered by class (`scripts/p16/skips.json`)

| class | count | examples |
| --- | --- | --- |
| work not on the 2023-2025 set-text lists | 106 | Macbeth ×~20, Kumukanda + the Kayo Chingonyi poems, AQA Power-and-Conflict / Love-and-Relationships poems, An Inspector Calls, Lord of the Flies, Jekyll & Hyde, A Christmas Carol, Romeo & Juliet, The Tempest, Sonnet 18/43/130, An Essay on Man (a NEAR-MISS against the spine's 'From An Essay on Criticism' — correctly NOT bound) |
| guidance/skills register | 15 | "Why Your Essays Are Flopping", "IGCSE FLE vs IGCSE Literature?!", the language-devices series (anaphora/epistrophe/symploce), essay-craft tips |
| out-of-spine board register | 16 | explicit AQA/Eduqas/WJEC/Edexcel/GCSE titles with no CIE token and no spine set text |
| character-study titles without a set-text token | 15 | Malvolio, Caliban, Sybil Birling, Mr Hyde, Scrooge, the Cratchits — no machine-checkable bind at the bar |

A final safety sweep re-scanned all 152 skips for any spine set-text name: **0 residual
mentions** — nothing bindable was left behind.

## Emit + gates

- Builder P16 section (fresh-create, the P12 shape; video-keyed idempotency; no P16B — lit-21
  has no containment children), placed after P15B / before P2F; flags want-array + status
  template extended (the receipt-sync law).
- **Disclosed builder fix (this lane):** the P2 main-loop method gate (line ~171) predated the
  P9+ `paper-code` row law and the P4 `inherited-external` method — the P15 Belal-Sir anchors
  shipped onto the MERGE course `igcse-biology-19` tripped it in any full replay, poisoning the
  shared errors array so every later section skipped its writes and stale shipped rows cascaded
  into downstream duplicate gates. The gate now tolerates all three committed methods; the full
  replay runs exit 0.
- **Emit: exit 0 ×2, the replay machine-checked a no-op modulo generatedUtc** (lit-21 file
  byte-identical modulo the timestamp; rows 100, specs 101/203 stable).
- Hub gates: **video-map tests 16/16 (7,191 expects)** incl. the corpus-at-rest census over all
  96 courses (0 reviewed:false); **spec-join census 96 courses / 16,298 rows / 59,095 refs /
  0 violations** (+100 rows / +299 refs = lit-21 exactly); registry 95 → 96 courses; flags 96.
- Evidence artifacts committed: `scripts/p16/skips.json` (152 by class) + `oembed-p16.json`
  (100) + `specjoin-census.json` + `judgment_summary.json` + the lane scripts
  (`p16_lit21_judgment.py` / `p16_oembed.py` / `p16_assemble.py` / `p16_specjoin_census.py`).

## Open work remaining

1. Owner: re-supply the 7 lost P14 pool names + the 3 unresolved URLs (Skip the Tutor /
   Bizcon Sessions / Dr Demina) — nothing silently dropped, the ledger holds.
2. **PAT rotation** — the classic token has transited far too many sessions; every receipts
   file of record logs it overdue. Rotate before the next push.
