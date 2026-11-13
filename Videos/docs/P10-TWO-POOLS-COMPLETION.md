# P10 — two-pool maths completion (MrArnoldsMaths + Maths Deity)

Status: **landed** (owner chat 2026-11-13: "Mr Arnolds Maths, and MAths Deity" → recon → "lane P10").
Lane: `T-VIDEOMAP-P10 (two-pool maths completion)`.

## 1. What shipped

**358 owner-reviewed rows onto 10 maths courses** from two channels in one lane (the P7 multi-pool precedent):

- **35 course anchors** (Tier B): bound by machine-checkable IAL module codes in titles — `method: paper-code`, `confidence: high`, `boardMismatch: false`, `specs: []` + `anchor{level: course, ref: course}` + `kind: past-paper-walkthrough` — zero spec weight per docs/ANCHOR-GRANULARITY.md §4/5/8. Sources: "Edexcel IAL P1..P4 <session> Exam Paper", "Practise Paper n (Edexcel IAL Pn)", "Edexcel style Pn Practise paper", "hardest questions (on|from) (Edexcel IAL) Pn/Mn/Sn".
- **323 spec rows** (Tier A): Maths Deity's unit.section marker tutorials (`(Edexcel IAL P1 3.7)` forms, lenient regex incl. `( Edexcel`, `E dexcel`, `(IAL P4`, `Chapter 4`, `(Edexcel IA S1)`) routed P1-P4 → pure-1..4, M1/M2 → mechanics-1/2, S1/S2 → statistics-1/2, FP1 → further-pure-1, bound by explicit-code class tables over the distinctive-token pre-pass (df ≤ 3 → medium; marker-structured rows permitted the disclosed P4 cross-subject-style higher title-only bar → low, per-row disclosure, because the small dense module spines — 16-25 specs — make df≤3 structurally unable to discriminate: `poisson` has df 5 across 16 S2 specs); Arnolds' 22 GCSE topic rows onto `igcse-maths-a-18-higher` at the tightened bar (all medium); Arnolds' module-named S1/S2 tutorial series (29) bound cross-register onto ial statistics-1/2 at boardMismatch:true.
- **2 maths courses leave the honest-empty set via fresh creation**: `ial-maths-20-statistics-2` (14/16 specs) and `ial-further-maths-18-further-pure-1` (17/25 specs). `ial-maths-20-mechanics-2` gains its first **native** rows (11/13 specs; the 41 P4 cross-subject rows remain). Maths honest-empty after P10: `ial-maths-20-decision-1` (no D1 content in either pool), `cie-igcse-maths-25-core` (Tier B — Arnolds walks extended papers only... no core papers in either pool).

## 2. Pools

- `inventory/channels/mrarnoldsmaths-uploads.json`: **437 public uploads** of `MrArnoldsMaths` (`UCwa84m5RqSJEkP9pYdeDYnw`, verified by page-HTML `externalId` grep), yt-dlp flat, 0 dupes.
- `inventory/channels/mathsdeity-uploads.json`: **353 public uploads** of `Maths Deity` (`UCODyYjai6abd1N5KGc1KacQ`, same verification), 0 dupes.
- **0 overlap** with the 4,373-video shipped union (route-time corpus exclusion + emit-time census).

## 3. Routing (deterministic, `scripts/p10/p10_route.py`)

| Disposition | Count | Detail |
| --- | --- | --- |
| Tier B anchors | 35 videos → 35 rows | md B pure-1..4 26, mech-1 2, mech-2 1, stats-1 3, stats-2 3 |
| Tier A marker/module rows | 316 | md unit.section tutorials: P1 46 / P2 45 / P3 38 / P4 31 / M1 39 / M2 17 / S1 8 / S2 26 / FP1 33; Arnolds S1 23 + S2 6 module-named tutorials |
| Tier A topic rows (Arnolds) | 41 routed → 22 kept | distinctive-token binds onto a-18-higher (primes, HCF, fractions, probability, averages, ratio, percents, equations); 17 unmapped + 2 drops honest |
| Honest skips | 399 | legacy Edexcel GCSE linear 1MA0 papers 260 (§6 — qualification not in the spine); Arnolds "Core Maths" GCE pure-core series 44 (§6, module unnumbered); GCE C1-C4/applied 26; FP2 27 (**no further-pure-2 course in the spine — owner note: adding one would be a spine change**); other-board 10 (AQA L2 FCSE 4); no-vocab 30; community/calculator 2 |

Every video in both pools is dispositioned exactly once (790 = 35 + 356 + 399).

## 4. Identity + judgment

- **oEmbed sweep 358/358** (`scripts/p10/p10_oembed.py`): every video entering a P10 draft verified live; author == channel of record (`MrArnoldsMaths` / `Maths Deity`), 0 mismatches, 0 dead, 0 thumb-fallbacks.
- **Judgment pass over every routed row** (`p10_candidates.py` → `p10_judgment.py`): explicit-code class tables per course (9 IAL + a-18-higher); rules refine the pre-pass, never invent — a table bind draws its spec from the pre-pass scored candidate list, or (direct rules, marker/module rows only) binds a spine-validated code when the title names the topic unambiguously and the textbook phrasing leaves zero token overlap (`Integrating x^n` → pure-1 5.2, `Inverting a 2x2 Matrix` → FP1 5.5). Explicit rebind: `Geometric proof of Addition formulae` → pure-3 2.3 (the spec text names sin(A±B)/cos(A±B)); degenerate vocabulary binds dropped (`Do I even need to learn the Factor formulae?` → the pre-pass's pure-1 3.2 radian-measure bind is word-adjacency — honest drop).
- Final: 322 keep (medium 189 / low 133) + 1 rebind / 23 routed-unmapped / 10 drops — every decision explicit in `owner-review-verdicts.p10.json` per course.

## 5. Builder + emit

- `build-content-map-external.mjs`: **P10 section** (10 courses; fresh-create for statistics-2 + further-pure-1, P5-shape append for the 8 existing) placed after P9 and **before the P4 inherit loop** — `igcse-maths-a-18-higher` is an inherit PARENT whose five children (a-18-foundation + modular-24 u1/u2 ×2) cascade at build time. **Idempotency law applied to BOTH the P9 and P10 loops** (the P2B law, video-keyed): each lane's draft is the sole source for its rows — prior lane rows drop by video id and the prior lane entry drops from `review.lanes` before re-append, so the full replay is a no-op from post-P9 state (the P9 loop previously assumed a fresh-course base; this lane generalizes it).
- Full emit **exit 0**. Registry **68 courses**; flags `videoMap.courses` 68; status template `P3+P4+P5+P6+P7+P8+P9+P10` machine-checked against the emitter template pre-flight.

## 6. Gates

| Gate | Result |
| --- | --- |
| Full emit exit 0 | PASS (10 P10 courses, cascade, flags 68) |
| Hub `bun test src/lib/video-map.test.ts` | **16/16 pass, 4,268 expect() calls** (corpus-at-rest zod census over all 68 flagged courses; was 4,227 over 66) |
| Independent spec-join census (`scripts/p8/p8_spec_join_census.py`) | **68 courses, 8,026 mapping rows, 6,365 spec refs, 0 violations** (was 66 / 7,622 / 5,996) |

## 7. Honest-empty after P10

- Maths: `ial-maths-20-decision-1` (no D1 content in either pool) and `cie-igcse-maths-25-core` at Tier B (no core-paper content in either pool; its P9 Tier A topic rows remain).
- `ial-further-maths-18-further-pure-2`: content exists (Maths Deity FP2, 27 tutorials) but **no spine course** — recorded as honest no-target with an owner note; adding the course is a spine change, not a mapping decision.
- Edexcel GCE (C1-C4, 9MA0-era, legacy applied) and AQA L2 FCSE content: no qualification courses exist in the spine — honest no-target skips per §6.
