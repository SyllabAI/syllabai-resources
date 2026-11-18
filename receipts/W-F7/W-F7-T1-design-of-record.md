# W-F7-T1 — Book-alignment lane design of record
# the ial-chemistry V-lane corroboration join (the last open Lane B item)

```yaml
schema: syllabai.book-alignment-design/1.0
task: W-F7-T1 (book-alignment lane design of record)
wave: W-F7
origin_trace: 1a1ef43dcfda2a59
trace_id: 1a1ef43dcfda2a59
executed_utc: 2026-11-18
operator: SyllabAI operator (zai-web 1a1ef43dcfda2a59)
order: "book-alignment lane"
tree_of_record: syllabai-resources @ HEAD 5608e2e1ccb34945036b26c23275488e3a0e43ff
design_authority: W-F4-T1 book-join design of record (receipts/W-F4/W-F4-T1-book-join-design.md, gates G-F4-D1..D3 PASS) — schema, ladder and verdict classes adopted UNCHANGED; this document adds only the ial-chemistry build-time laws the T1 design left as build-time probes
status: DESIGN_OF_RECORD — artifacts NOT emitted (W-F7-T2 same order, per the W-F6 T1+T2 precedent)
```

## 1. Scope: what the lane is, and what it can and cannot fire on

The operator order **"book-alignment lane"** (trace `1a1ef43dcfda2a59`) fires the remaining
Lane B backlog named in the Wave-43/46 push-confirm reports. Per the W-F4-T1 eligibility
ledger (§8) and the W-F4-T2 wave report (§5 finding 5: "the V-lane corroboration join waits
for the W-F2-T2 swap to land"), exactly ONE item is actionable:

- **ial-chemistry `book-join.json`** — deferred at Wave 37 as `BUILT_NOT_JOINED` for two
  reasons of record, BOTH now resolved: (a) the spec side was mid-swap — the W-F2-T2 Stage R
  sub-item layers landed as Waves 35-36 (`0111c9c1` era) and are pushed; (b) the point-level
  route was unprobed — this design pins it (§3).

Everything else stays honest-blocked, unchanged: 10 NO_BOOK F4 quals (books rollout queue,
operator purchases — never agent-fetches), ial-biology (YBI11 row `—`), the 4 modular/SDA
quals (NO_BOOK receipts of record), CIE coursebooks (SOURCE_ONLY = Lane C follow-on, not
Lane B scope). ial-physics/4BI1/4PH1/4CH1 joins are landed and pushed; this lane touches
none of them.

## 2. Probes of record (evidence: cache/w-f7/probe.json + probe2.json, zero repo writes)

Ran the W-F4-T1 ladder J1-J5 against the ial-chemistry spec side at the pinned HEAD
(`5608e2e1` blobs; 319 points, all `official_code` present, unique, `1.1`-`20.5`, zero null)
and the two pinned YCH corpora (blob `5924f3d9` SB1 1571 chunks + blob `7a22b6b9` SB2 1406
chunks, both verified present in the object store):

| key | probe result | adjudication |
|---|---|---|
| J1 printed code list | front matter carries ONE anchored course-structure entry: printed heading `1 COMPARING MASSES OF SUBSTANCES` + `SPECIFICATION REFERENCE` + printed list `1.1 1.2 1.4` (chunk `ych1_v1_u0_c0_pdf009_0039`, all 3 resolve); scattered front-matter tokens are OCR noise + numeric constants (`6.02`, `12.0`, `16.0`) and unanchored cross-refs (unit-mismatched) | **J1 ANCHORED-ONLY, topic-level**: the printed heading is a SECTION title (not the manifest chapter title `1A Atoms, elements and molecules`), so the list is recorded verbatim as Topic-1 evidence, never attributed to a chapter row (L-2); scattered tokens are findings, not rows |
| J2 LO code chips | 7 tokens / 6 distinct codes (`10.8`, `10.9`, `17.26`, `17.27`, `17.28`, `17.29(i)`, `17.29(ii)`), 100% unit-consistent, printed as chip runs in LO boxes (`PART 17.26 17.27 17.28 17.29(i) 17.29(ii)`) | **J2 ACTIVE** (the W-F4-T2 probe said "≈ empty" with a looser regex; the full run finds a small real chip set — recorded as a W-F4-T2 errata candidate, not a contradiction: both agree the chips are sparse) |
| J3 body code chips | the IAL books print **margin spec-reference chips**: OCR interleaves the margin column into chunk text; unit-consistent resolved tokens 265 raw → 69 under the conservative admission law (§3), 48 distinct codes, 18 of 54 manifest chapters; false-positive classes identified and excluded deterministically (ratio notation `1.2: 1.2:1.9`, unit-glued `1.4dm3`/`3.8dm?`, arithmetic `63.5 + 32.1`, formula subscripts `CuSO4.5H2O`) | **J3 ACTIVE, conservative** — weaker key per L-1, never contradicting J1/J2 |
| J4 LO text equality | 0 / 714 LO bullet lines exact-match any spec text (incl. sub_items) under the normalisation map; 0 even space-free (diagnostic only) | **honest 0** — the book paraphrases; recorded in `route_tried` (the ial-physics P-F4-2 precedent) |
| J5 title adjudication | after the printed `Topic N:` prefix-strip: 16/20 topics EQUAL verbatim; 3 topics CONTAINS (the book title = spec title + printed tail: T10 `...and Spectra`, T15 `...and Chirality`, T19 whose spec-side title of record ends in a trailing comma); T11 `Kinetics II` vs `Kinetics` (book disambiguator); T18 printed punctuation variant (`:` vs `–`) | **J5 ACTIVE, three-tier per M-6** — EQUAL / CONTAINS (the W-F4-T1 law verbatim) / printed NUMBER_IDENTITY with the variant pair as-printed; all 54 rows topic-mapped at build time (gate) |
| J6 page-span adjacency | chapter page frames and spec provenance pages live in different PDFs (book vs specification) | **NOT_APPLICABLE** (the ial-physics J6 refinement, adopted verbatim) |

## 3. The ial-chemistry build-time laws (delta over W-F4-T1 — nothing else changes)

- **M-1 margin-chip admission (J2/J3, deterministic, zero LLM).** A code token is admitted
  iff: (a) it resolves against the pinned `official_code` set, bare or in the printed
  sub-item suffix form `N.M(i..x)`; (b) it is NOT ratio-adjacent (immediately preceded or
  followed by `:`), NOT letter-glued (a letter directly adjacent outside the token — kills
  `1.4dm3`, `3.8dm?`, `CuSO4.5H2O`); and (c) it appears in one of three printed-chip
  positions: **RUN** = member of a run of >= 2 consecutive whitespace-separated admitted
  tokens (the OCR image of a margin chip block); **SUFFIXED** = carries the printed
  `(i..x)` sub-item suffix (ordinary prose numbers never do); **TAIL** = the final token of
  the chunk. Everything else stays unadmitted — conservative by design (L-2: a false chip
  is invention; a missed chip is honest sparsity).
- **M-2 unit-consistency.** A chip attributes to its chapter only when the book unit
  (`ych[12]_u<t>`) equals the code's topic number (`N.M` -> topic `N`). Unit-mismatched
  tokens are cross-references, excluded per L-2 (the ial-physics J3 refinement).
- **M-3 sub-item resolution.** Printed `17.29(i)` resolves to point `17.29` + sub_item
  ordinal i (the Stage-R `sub_items` of record); the as-printed form rides the row (the
  W-F1-T1 as-printed law; the 4BI1 `2.57`->`2.57B` L-4 precedent generalized to ordinals).
- **M-4 CP chips.** Printed `CP<n>` markers and the 63 practical-suggestion markers ride
  rows as `practicals_lane` flags/reasons (W-F4-T1 §8.2 routing adopted; the Lab Book owns
  Core Practicals — CATALOG §3.5/§3.6 Notes).
- **M-5 J1 anchor law.** Anchor-adjacent lists only: the printed `SPECIFICATION REFERENCE`
  heading + following code tokens within the same chunk. The single anchored entry of record
  (printed section heading `1 COMPARING MASSES OF SUBSTANCES`, codes `1.1 1.2 1.4`) is
  **topic-level evidence, recorded verbatim, not attributed to a chapter row**: the printed
  heading is a SECTION title, not the manifest chapter title (`u1:c1` = `1A Atoms, elements
  and molecules`), and positional chapter attribution would be the fuzzy guessing L-2
  forbids. Its codes ride rows only where the margin chips print them too (1.1 does; 1.2/1.4
  stay honest-unkeyed unless otherwise printed).
- **M-6 J5 topic law (three-tier, printed-evidence only).** The unit-to-topic map is the
  printed Topic numbering (manifest unit index N <-> spec `T-N`; the books' own "ABOUT THIS
  BOOK" claim: "Each unit has five Topic areas that match the titles and order of those in
  the specification"). Per-row basis, deterministic:
  (1) `J5_EQUAL_AFTER_PREFIX_STRIP` — strip the printed `Topic <N>:` prefix, normalised
  equality (16/20 topics expected); (2) `J5_CONTAINS_AFTER_PREFIX_STRIP` — the spec title
  is a verbatim substring of the printed book title (T10 `...and Spectra`, T11 `Kinetics II`
  vs `Kinetics`, T15 `...and Chirality`, T19 whose spec-side title of record itself ends in
  a trailing comma — see errata) — the W-F4-T1 J5 law admits CONTAINS verbatim; (3)
  `J5_NUMBER_IDENTITY_TITLE_VARIANT` — printed title variant with the number identity
  (T18: book `Organic Chemistry: Arenes` vs spec `Organic Chemistry \u2013 Arenes`); the
  printed pair rides the row as-printed, never silently normalised. Every row carries the
  printed pair; `J5_UNMATCHED` rows (none expected) would stay `UNJOINED` unless chips.
  Gate: all 54 rows carry a topic ref with one of the three bases.
- **M-7 row grain.** One row per manifest lesson chapter (35 SB1 + 19 SB2 = 54 rows, keys
  `u{t}:c{n}` from the landed structures), each carrying `book_key`, chapter title, the
  unit's `spec_refs.topic` (M-6), and `spec_refs.points` (J1/J2/J3 chips merged,
  strongest-first, printed form + resolution + admission mode + chunk evidence). Verdicts:
  `JOIN_POINT` where point chips exist, else `JOIN_TOPIC`; `UNJOINED` rows (not expected)
  would carry keys-tried. Divider chunks (`c0`) carry no rows; any chips found there are
  recorded in the receipt, not invented into rows.

## 4. Wave-37 errata of record (found by the probe, corrected by this lane)

The landed `ial-chemistry/book-layer-index.json` carries `no_book_units: [unit 3, unit 6]
NO_BOOK_PRACTICAL_UNIT` — a **namespace conflation copied from the ial-physics builder**.
Evidence: CATALOG §4.2 prints "Units 3/6 are practicals, no SB" in the **Physics** row only;
the chemistry spec `topics.json` numbers CONTENT topics 1-20 (topic 3 = `Bonding and
Structure`, topic 6 = `Energetics`), and the SB1 manifest + corpus cover BOTH: 5 chapters
(3A-3D) and 7 chapters (6A-6G), 254 chunks (98 body, 18 LO), topic dividers present. The
exam practical units (WCH13/WCH16) carry no content topics and no student book — the honest
statement, recorded by the corrected index in this lane. The old state stays in git history;
the correction is confined to the ial-chemistry index file (no other index, structure file,
spec-side file or census file is touched).

### 4.1 Further findings of record (routed, not repaired — write surface closed)

- **Spec-side title truncation (T19):** `topics.json` of record prints topic 19 as
  `Organic Nitrogen Compounds: Amines, Amides,` — the printed spec title continues
  (`Amino Acids and Proteins`, as the book unit title prints). Spec-side errata candidate
  for the Lane C owners; NOT edited here.
- **W-F4-T2 J2 probe count:** "≈ empty" under the looser T2 regex vs 7 chips / 6 codes
  under the full run — both agree the chips are sparse; recorded as a W-F4-T2 errata
  candidate, no retro-edit.

## 5. Artifacts of the build (W-F7-T2)

| file | change | content |
|---|---|---|
| `_derived/book_layer/ial-chemistry/book-join.json` | NEW | schema `syllabai.book-spec-join/1.0` per W-F4-T1 §5 (the 4CH1/ial-physics row shapes); `spec_side` pins the HEAD blobs; `join_keys` block records every regime's route_tried incl. the honest zeros; `coverage` block complete with per-row reasons |
| `_derived/book_layer/ial-chemistry/book-layer-index.json` | M | `join_status` -> `JOINED` + the route summary; `no_book_units` -> the exam-unit note of record (§4); `generated_utc`/`generator` updated; the Wave-37 state preserved in history |

Zero changes to: the two book-structure files, any spec-side file, any other book_layer
file, the census (0.4 stays as landed agent-side of record), the books lanes.

## 6. Build gates (defined now, for W-F7-T2)

| gate | pass condition |
|---|---|
| G-F7-B1 | every join row cites chunk ids + as-printed forms + admission mode; zero LLM; laws M-1..M-7 honoured (re-derived by the gate script from the pinned blobs, not trusted from the emitter) |
| G-F7-B2 | every spec ref resolves against the pinned spec blob at `5608e2e1`; id-set invariance: the landing surface is EXACTLY `book-join.json` (A) + `book-layer-index.json` (M), nothing else |
| G-F7-B3 | coverage block complete: chapters 54/54 accounted, all 54 rows carry a topic ref with a verifiable M-6 basis, points 319/319 accounted (keyed / topic-only with `no_printed_key` / practicals-routed); honest rows never dropped |
| G-F7-B4 | multi-book law: one qual-level join, rows carry `book_key`; the §4 errata confined to the ial-chemistry index; structure files byte-untouched (blob equality asserted) |
| G-F7-B5 | determinism: `generated_utc` pinned; the emitter re-run reproduces both files byte-identically (sha256) |
| G-F7-B6 | the index rewrite keeps every pre-existing field honest: `books`/`no_book_units`-correction/`join_status` are the only edited regions; all other keys byte-preserved |

## 7. Non-goals

No books-lane writes (modules/manifests/CATALOG untouched; the CATALOG drift candidates of
W-F4-T1 §11 stay routed to the books-lane owners). No spec-side edits. No census writes. No
book acquisition or fetches. No LLM anywhere. No new lanes fired (the 10 NO_BOOK quals stay
queued on the books rollout; CIE joins stay Lane C follow-on).

## 8. Definition of done

- Design of record + JSON receipt + worklog filed under `receipts/W-F7/`; task file
  `tasks/W-F7-book-alignment.md` drafted (lands with the records commit of this order).
- Probes of record cached (`cache/w-f7/probe.json`, `probe2.json`).
- W-F7-T2 executes in the same order (W-F6 precedent): emitter + gates + swap staging +
  one revertible commit; records landing (task file + receipts + the pending Wave-46/47
  ride-alongs + LEDGER) follows as the next commit of the same order; push by separate
  operator order.
