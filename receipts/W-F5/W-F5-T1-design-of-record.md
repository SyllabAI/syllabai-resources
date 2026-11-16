# W-F5-T1 — Design of record: presentation layer for the canonical bundles
(LaTeX render lane + geometry-driven source re-recovery lane)

```yaml
wave: W-F5
task: W-F5-T1 (design of record — transform inventory, damage-class census, lane
      architecture, gate law, T2 execution plan)
order_trace: 1a1e5bfa1854103d   # bare operator order "W-F5"
directive_traces:               # the operator's preceding plain-language directive
  - 1a1e5b85438a9a11            # "the parsed outputs can be better than the original"
  - 1a1e5be7c17de8f1            # "LaTeX, better formatting etc. We don't have to be verbatim"
executed_utc: 2026-11-15
inputs_of_record:
  - the 68 landed CIE canonical bundles at commit d926be489c016d55b6d5bd3c9210b4d19b5acaf4
    (blob oids pinned in cache/w-exec/manifest-wf3t2-land.json; records commit 3c8c2515…)
  - cache/w-f5/audit-of-record.json — the T1 audit of record (pattern inventory P01..P15
    + refined damage classes, per-qual counts + examples, pinned at the manifest oids)
  - the 13-field contract of record (staged W-F2-T2 outputs; bundle shape law W-F3-T1)
  - flag classes of record (8 kinds carried verbatim from SOURCE; W-F3-T1 §2)
  - reparse precedent — spec-reparse-1.0 (W-F2): deterministic source re-extraction,
    flag recorded, never silently repaired
  - per-row provenance pins (pdf filename + pdf_sha1 + page + oy) inside every bundle row
status: DESIGN COMPLETE — T2 (build + land) PENDING OPERATOR ORDER
write_surface: tasks/W-F5-presentation-layer.md + receipts/W-F5/ + worklog append +
  cache/w-f5/. Zero repo writes; census stays 0.5; bundles stay at issue 1.
```

## 1. Operator order and interpretation

Order (trace `1a1e5bfa1854103d`): **"W-F5"** — the presentation-layer wave the operator
described in the two preceding directive traces: the parsed outputs can be *better than
the original* (LaTeX, better formatting; "we don't have to be verbatim"). Interpretation
of record: W-F5 = presentation/repair wave over the 34 landed CIE canonical bundles, in
three deterministic lanes (§3). T1 is the design; the T2 build + land fires by separate
operator order (W-F3 precedent).

## 2. What the audit found (facts of record — cache/w-f5/audit-of-record.json)

Scanned all 34 `spec_points.json` blobs at the pinned oids (6,920 rows).

**Pattern inventory (P01..P15):** the corpus is typographically healthy overall —
327 rows already carry proper unicode math (α, β, →, ×, °, –) and need no repair;
only 1 caret, 1 ASCII fraction, 2 ordinals. The `chem-bare` and `ion-charge` regexes
produce mostly FALSE positives (genetics "F1, F2", rubric codes "(W2)", "A4", suspended
hyphens "di- and tripeptides") — cosmetic regex transformation is the WRONG tool for
them (adjudicated §5).

**Refined damage classes (the real defects, candidate sets):**

| class | rows | quals | example (verbatim from the pinned blob) |
|---|---|---|---|
| subscript-loss | 41 | 12 | `SO , PC l , SF` (SO₃, PCl₅, SF₆); `H (aq) and OH (aq) form H O(l)` |
| hyphen-split | 24 | 12 | `file- based`, `light- independent` |
| math-garble | 22 | 5 | `r ^ cos i + i sin i h / r e`; two-column text interleaved mid-sentence |
| footer-continued | 28 | 7 | trailing page-break marker `… continued` |
| exponent-loss | 11 | 6 | `6.02 × 10 particles` (the ²³ is GONE); `E = 1/2 mv` (the ² is gone) |
| orphan-digit-prefix | 2 | 2 | leading orphan tokens `2 3 P O ` |

**Key finding:** the flags of record undercount the loss class — only 5 rows carry
`possible-superscript-loss`, but pattern evidence shows 41 + 11 + 2 rows in the
sub/super/orphan classes across ~15 quals. Flags stay untouched (they are of-record);
the repair set is derived from evidence, and every repair is receipted.

**Feasibility fact:** every row carries provenance (pdf + pdf_sha1 + page + oy), so the
pinned source PDF page region is addressable for each damaged row. The CIE syllabus
PDFs are NOT in the durable cache (only 2 IAL Pearson PDFs + 2 Pearson books are) — the
re-recovery lane therefore needs a fetch step at T2 with sha1 verification against the
parse_report pins (fetch-manifest pattern of record, W-F1/W-F4 precedent).

## 3. Lane architecture (three deterministic lanes, zero LLM everywhere)

- **R1 — render layer (`text_render`):** every spec_points row gains a
  `text_render` field: display-ready text with KaTeX-compatible `$…$` math spans and
  safe spacing normalizations, derived from `text` by an ORDERED, PURE transform table
  (§5). `text` is never modified by R1. Uniform across all 34 quals; rows with no
  applicable transform get `text_render == text`.
- **R2 — geometry-driven source re-recovery:** for the sub/super/orphan/math-garble
  candidate rows (~95 rows), re-extract the pinned PDF page region (provenance page/oy)
  with column-aware, sub/superscript-aware span geometry. Recovered truth re-derives
  the row `text` at issue 2 with flag `reparse-2.0` (W-F2 reparse precedent: recorded,
  never silent) + a per-row recovery receipt (before/after bytes + geometry evidence +
  pdf_sha1 match). Rows the PDF cannot adjudicate (glyph truly absent) stay verbatim at
  issue 1 semantics with a `render-gap` note in the recovery receipt — honest, no
  invention (constants like 10²³ are NOT restored from domain knowledge; they are
  recovered from the PDF or left absent).
- **R3 — presentation polish (render-side):** footer-continued stripping, degree/prime
  spacing normalization, hyphenation rejoin ONLY where the source PDF line layout proves
  the split was a line wrap (geometry check) — otherwise verbatim. All R3 edits happen
  inside `text_render`, never in `text`; each is reversible (§5).

## 4. Field and issue law

- Bundles re-issued at `issue: "2"` for the 34 `spec_points.json` files; `topics.json`
  UNTOUCHED (byte-identical to issue-1 blobs). 34 modifications, one revertible commit.
- Row shape grows by ONE field: `text_render` (inserted after `text`, keeping the
  13-field order otherwise intact — 14 fields of record at issue 2).
- `id`, `ordering`, `topic`, `subsection`, `sub_items`, `practical`, `applicability`,
  `leading_verb`, `provenance` untouched. `flags`: issue-1 flags never dropped;
  `reparse-2.0` may be APPENDED on R2-recovered rows (additive only).
- `counts` recomputed honestly if row text changes; `schema` string unchanged
  (`syllabai.spec-points/1.0`).
- Census decision rule: census 0.5 stays agent-side; at T2 a 0.6 rider (issue bump +
  `text_render` field noted in the bundle manifest fields, changelog seq 8,
  additivity deep-compare) is applied ONLY if the census schema actually describes the
  fields the bump touches — same propose-then-apply pattern as the W-F3 0.5 rider.

## 5. Transform tables (adjudicated from real examples)

ACCEPTED for R1/R3 (each with its deterministic inverse; de-render must reproduce
`text` byte-for-byte):

| # | transform | guard | inverse |
|---|---|---|---|
| T1 | `N °C` → `N°C` inside `$…$`-wrapped temperature span | only `\d+\s°` | insert the space back |
| T2 | `d ′` spacing → `d′` (primes) | `\s′` | insert the space back |
| T3 | clean math spans wrapped `$…$`: fractions `\d+/\d+`, `θ`, ≤/≥ expressions | span must contain ONLY the adjudicated math charset | remove `$` delimiters |
| T4 | fraction → `$\frac{a}{b}$` | `\b\d+/\d+\b` inside a T3 span | `\frac{a}{b}` → `a/b` |
| T5 | trailing ` continued` stripped (footer artifact, never legitimate) | `continued\s*$` | re-append (allow-listed by recovery receipt) |
| T6 | hyphen-split rejoin `file- based` → `file-based` | ONLY with PDF line-wrap geometry proof (R3-R2 joint evidence) | re-split at recorded wrap point |

REJECTED as cosmetic regex (stay verbatim; handled only via R2 evidence):
`chem-bare` (F1/W2/A4 false positives), `ion-charge` suspended hyphens, `ordinal`
superscripting, whole-text LaTeXification (percent signs, `<address>` pseudo-code and
`_`/`^` artifacts stay plain text), caret math (`r ^ cos i…` is garbled source, not
notation — R2 lane).

**Ambiguity law:** any instance the transform table cannot adjudicate with its recorded
guard stays verbatim. Uncertainty is recorded, never guessed.

## 6. Gates

| gate | task | pass condition |
|---|---|---|
| G-F5-D1 | T1 | every transform, guard and lane rule cites a real artifact of record (path + pinned blob oid or audit JSON pointer) — no invented shapes |
| G-F5-D2 | T1 | the audit of record covers all 34 quals at the pinned oids (pattern inventory + refined damage classes + examples); every class names its detector regex |
| G-F5-D3 | T1 | zero writes outside `tasks/W-F5-*.md` + `receipts/W-F5/` + worklog append + `cache/w-f5/`; zero repo writes; bundles stay at issue 1; census stays 0.5 |
| G-F5-C1 | T2 | reversal gate: de-render(`text_render`) == `text` byte-for-byte on 100% of rows, EXCEPT allow-listed rows (T5/T6/R2) each carrying a per-row receipt |
| G-F5-C2 | T2 | determinism gate: the emitter is pure code (transform tables + geometry checks); zero LLM anywhere; re-run on the same inputs reproduces byte-identical outputs |
| G-F5-C3 | T2 | flag preservation: issue-1 flag sets are subsets of issue-2 flag sets; `reparse-2.0` appended only on R2-recovered rows |
| G-F5-C4 | T2 | issue bump honesty: `issue: "2"`, topics.json byte-identical to issue-1 oids, counts recomputed, 13+1 field order intact |
| G-F5-C5 | T2 | swap discipline: `git diff --stat` shows ONLY the 34 modified `spec_points.json`; single revertible commit; SWAP.md with sha256 pins |
| G-F5-C6 | T2 | R2 recovery receipts: per-row before/after + page/oy + pdf_sha1 match against the pinned parse_report; unrecoverable rows documented, not guessed |

## 7. Scope

| set | rows/quals | lane |
|---|---|---|
| all rows | 6,920 / 34 | R1 `text_render` + R3 polish |
| sub/super/orphan candidates | 41+11+2 / ~15 | R2 re-recovery (per-row adjudication) |
| hyphen-split candidates | 24 / 12 | R3 with geometry proof, else verbatim |
| math-garble candidates | 22 / 5 | R2 column-aware reparse |
| footer-continued | 28 / 7 | R3 (T5) |

## 8. Non-goals

- No LLM anywhere (transform tables + geometry code only).
- No in-place mutation of landed files; nothing touches `topics.json`, ids, ordering,
  provenance, or issue-1 flags.
- No whole-text LaTeXification; no semantic rewriting; no domain-knowledge constant
  restoration (10²³ comes from the PDF or not at all).
- No graph YAMLs, no notes-join, no book-lane work, no Pearson-side changes.

## 9. Receipts and operator actions

Receipt of record: `receipts/W-F5/W-F5-T1-design-receipt.json` (schema
`syllabai.task-receipt/1`, `origin_trace: 1a1e5bfa1854103d`) + this design +
append-ready worklog block `receipts/W-F5/W-F5-T1-worklog-entry.md`. Evidence of
record cached at `cache/w-f5/audit-of-record.json`.

Operator actions:
1. Fire W-F5-T2 (build + land) by separate order — the build needs a fetch step for the
   CIE syllabus PDFs (sha1-verified against parse_report pins) before the R2 lane runs.
2. Rotate the delegated PAT (still outstanding; 4 chat-channel exposures).
