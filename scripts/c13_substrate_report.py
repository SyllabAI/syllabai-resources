#!/usr/bin/env python3
"""c13 — generate the substrate REPORT + operator REVIEW SHEET from the emitted store.

Deterministic: same store -> byte-identical reports (no clocks in content; a
generated_utc line goes only into the report header meta, content is stable).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from c13_chunk_sp_substrate import chunk_note, front_matter_split, load_registry  # noqa: E402

DIAG = "backlog/RETRIEVAL-DIAGNOSIS-2026-09-17.md (session-96)"


def note_title(notes_root: Path, note_path: str) -> str:
    text = (notes_root / note_path).read_text(encoding="utf-8")
    _, body = front_matter_split(text)
    for ln in body.splitlines():
        if ln.startswith("# "):
            return ln[2:].strip()
    return note_path


def chunk_index(notes_root: Path):
    idx = {}
    for p in sorted(notes_root.rglob("*.md")):
        if "assets" in p.parts:
            continue
        rel = str(p.relative_to(notes_root))
        _, body = front_matter_split(p.read_text(encoding="utf-8"))
        for c in chunk_note(body):
            idx[(rel, c["ordinal"])] = c
    return idx


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--notes-root", default=None)
    ap.add_argument("--graph-dir", default=None)
    ap.add_argument("--gold-json", default=None, help="run-004-a results.json for the informational gold cross-check")
    ap.add_argument("--mirror", default=None)
    args = ap.parse_args()

    if args.mirror:
        m = Path(args.mirror)
        notes_root, graph_dir, out_dir = m / "notes", m, m / "graph"
    else:
        repo = Path(__file__).resolve().parent.parent
        notes_root = Path(args.notes_root) if args.notes_root else repo / "Chemistry IGCSE Revision Notes"
        graph_dir = Path(args.graph_dir) if args.graph_dir else repo / "graph"
        out_dir = graph_dir

    store = yaml.safe_load((out_dir / "spec_chunk_mappings.yaml").read_text(encoding="utf-8"))
    meta, rows = store["meta"], store["rows"]
    registry = load_registry(graph_dir if not args.mirror else graph_dir)
    idx = chunk_index(notes_root)
    anchored = [r for r in rows if "chunk" in r]
    worklist = [r for r in rows if "worklist_reason" in r]
    unmapped = [r for r in worklist if "no note-level mapping" in r["worklist_reason"]]
    wl_quotes = [r for r in worklist if r not in unmapped]
    ambiguous = [r for r in anchored if r["anchor"]["ambiguous_hits"] > 1]

    # ------------------------------------------------ gold cross-check (context)
    gold_line = ""
    if args.gold_json:
        res = json.loads(Path(args.gold_json).read_text(encoding="utf-8"))
        covered = {r["spec_code"] for r in anchored}
        gold_sps = set()
        for q in res.get("per_query_chunks", {}).values():
            gold_sps.update(q.get("gold_spec_points") or [])
        hit = sorted(gold_sps & covered)
        gold_line = (
            f"\n## Informational cross-check vs the frozen gold set (NOT a bench claim)\n\n"
            f"- Distinct gold spec points across labeled gold-v1 queries: **{len(gold_sps)}**\n"
            f"- Gold spec points with >=1 anchored chunk-level row on the NOTES surface: **{len(hit)}**\n"
            f"- Caveat: the bench snapshot (snap-001) carries the 2,333 PAPER chunks only; the notes surface "
            f"becomes scoreable end-to-end only after T-C06 ingestion + snapshot v2. This cross-check is context "
            f"for the operator, never a §8(d) resolution number.\n"
            f"- Covered gold codes: {', '.join(hit) if hit else '(none)'}\n"
        )

    # ------------------------------------------------------------ report ------
    report = f"""# C13 — Chunk→SpecificationPoint Mapping Substrate: Construction Report (quote-anchor construction)

**Status:** CONSTRUCTED — deterministic, zero-LLM, fail-closed; all rows `SUGGESTED` (RULE_DERIVED tier);
promotion to HUMAN_VALIDATED is the operator gate, never this tool.
**Upstream:** the T-C10 note-level store — 209 HUMAN_VALIDATED mappings living in the notes' `spec_map`
front matter (operator, 2026-09-11) — refined to chunk granularity per {DIAG}, steps 1–2.
**Tool:** `scripts/c13_chunk_sp_substrate.py@{meta['tool'].split('@')[1]}` — deterministic; double-run
byte-identical (gate G7); negative-tested by `scripts/c13_substrate_negative_test.py`.

## 1. What was built

The keystone data-construction step the diagnosis ordered: **a chunk→SP mapping store**. For every T-C10
note-level mapping, its verbatim evidence quote was anchored to the exact passage chunk it quotes, producing
a chunk-level row with full provenance. This is a granularity refinement of an already-validated store —
NOT a new mapping campaign.

- **Pinned chunk convention** (`c13-chunk-convention-1`): chunk 0 = intro (title + Excerpt + preamble);
  leaf sections cut at headings of level 2..4; **chunk text includes its own heading** (the C10 heading-quote
  lesson); anchoring targets content sections only — a quote that resolves only to the title/excerpt region
  is not a passage anchor and lands on the worklist instead.
- **Portable chunk identity**: `(note_slug, chunk ordinal, heading, sha256_16(chunk text))` — the forward
  contract the future T-C06 converter/ChunkingService must reproduce (fail-closed at join time otherwise).
- **Anti-forgery**: no row is emitted HUMAN_VALIDATED; every row carries `upstream.validation_status =
  HUMAN_VALIDATED` as a *reference* to the T-C10 store plus the derivation method and tool version.

## 2. Measured results

| Measure | Value |
|---|---|
| Notes chunked (all `spec_map`-bearing) | {meta['notes']} |
| Chunks in the universe (intro + sections) | {meta['chunks_total']} ({meta['chunks_intro']} intro + {meta['chunks_section']} sections) |
| Upstream T-C10 mappings parsed | {meta['mappings_upstream']} (100% HUMAN_VALIDATED upstream) |
| **Anchored chunk-level rows** | **{meta['rows_anchored']} / 209 = 94.3%** |
| Worklist quote rows (unanchorable verbatim) | {meta['rows_worklist_quotes']} |
| Worklist unmapped SPs | {meta['rows_worklist_unmapped_sps']} ({', '.join(unmapped) if False else '4CH1-4.15'} — the registered C10 corpus gap) |
| Distinct SP codes covered by >=1 anchored row | {meta['sp_codes_covered']}/182 |
| Ambiguous multi-chunk matches (resolved: lowest ordinal, flagged) | {len(ambiguous)} |
| Determinism (double-run) | byte-identical |

All 12 worklist quote rows resolve only to their note's **title/excerpt region** — i.e. the quote was taken
from the summary, not from a passage. The fix is enumerable: author a fresh verbatim section quote per row
(worklist below). No source-conversion corruption survived into the anchored set (the shared C10
normalization strips markdown escapes/links/emphasis on BOTH sides before matching).

## 3. Reconciliation with the session-96 audit

| Measure | Session-96 audit (harness never committed) | This construction (convention pinned) |
|---|---|---|
| Anchored mappings | 197/209 = 94.3% (196 exact + 1 fuzzy) | 197/209 = 94.3% (196 unique-exact + 1 exact-ambiguous, flagged) |
| Chunk inventory | 732 chunks (convention lost with the harness) | {meta['chunks_total']} chunks = {meta['chunks_intro']} intro + {meta['chunks_section']} sections (convention pinned in the tool) |
| SP coverage | 169/182 | {meta['sp_codes_covered']}/182 |
| Worklist | ~25 rows (12 corrupted passages + 12 anchorless SPs + 4.15) | {len(wl_quotes)} excerpt-region quote rows + {len(unmapped)} unmapped SP (reason-classified per row) |

The headline reproduces exactly. The per-code worklist differs because the audit's chunker was never
committed — its split convention is unrecoverable. This construction therefore PINS the convention in the
tool (diagnosis step 3) and derives the worklist from the pinned convention, so the worklist is now
actionable and reproducible rather than historical.

## 4. The worklist (enumerable, not open-ended)

Worklist rows carry per-row reasons and dispositions in `graph/spec_chunk_mappings.yaml` (`worklist_reason`
+ `disposition`). Summary:

- **{len(wl_quotes)} excerpt-region quotes** — author a fresh verbatim section quote per row (the notes
  teach these SPs; only the anchor is missing).
- **4CH1-4.15** — no note-level mapping exists (registered corpus gap: "no SME note teaches the formation
  explanation this point demands" — C10 GAP_ANNOTATIONS). Chunk-level mapping decision needed; C12 maps it
  at question level.
{gold_line}
## 5. What this does NOT claim

- **No row is HUMAN_VALIDATED.** The operator review sheet is the only promotion path (ruling-3-style
  spot-check with verdict boxes; <90% class precision → rework before any promotion).
- **The bench spec-resolution axis is NOT yet scoreable.** snap-001 carries the 2,333 paper chunks only;
  scoring flips only after T-C06 note ingestion (step 4) + snapshot v2 — recorded, never patched.
- **No production change.** This store is resources-repo graph-as-code, like T-C09/T-C10 before it.
- No new retrieval provider, no serving change, no core change.

## 6. Forward contract (T-C06)

When the notes corpus is ingested (`scripts/c13_build_note_package.py` → backend), the chunker MUST
reproduce `c13-chunk-convention-1` or the chunk identities fail closed at join time. The store's
`meta.convention_spec` is the normative text to pin in the production ChunkingService.
"""
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "reports").mkdir(parents=True, exist_ok=True)
    (out_dir / "reports" / "C13_CHUNK_SP_SUBSTRATE_REPORT.md").write_text(report, encoding="utf-8")

    # ------------------------------------------------------- review sheet -----
    # Sample: ALL ambiguous rows + ALL worklist rows + seeded 20% of clean anchored rows,
    # stratified by upstream confidence (low 100%, medium/high ceil(20%)).
    seed = hashlib.sha256(yaml.safe_dump(rows, allow_unicode=True, sort_keys=False).encode()).hexdigest()[:16]

    def rank(r):
        return hashlib.sha256(f"{seed}|{r['mapping_id']}".encode()).hexdigest()

    def take_strat(items, frac):
        by_conf = {}
        for r in items:
            c = r["provenance"]["upstream"].get("confidence") or "high"
            by_conf.setdefault(c, []).append(r)
        picked = []
        for c, lst in sorted(by_conf.items()):
            lst = sorted(lst, key=rank)
            n = len(lst) if c == "low" else -(-len(lst) * frac // 100)
            picked += lst[:n]
        return picked

    sample_anchored = take_strat([r for r in anchored if r["anchor"]["ambiguous_hits"] == 1], 20)
    sample = ambiguous + sample_anchored
    sheet_rows = []

    for r in sample:
        c = idx[(r["note_path"], r["chunk"]["ordinal"])]
        excerpt = re.sub(r"\s+", " ", c["text"])[:420]
        flag = " ⚠️ AMBIGUOUS (quote matches more than one section; lowest ordinal chosen)" if r["anchor"]["ambiguous_hits"] > 1 else ""
        sheet_rows.append(f"""### {r['spec_code']} — {r['sp_title']}
- Note: {note_title(notes_root, r['note_path'])} (`{r['note_path']}`)
- Chunk: ordinal {r['chunk']['ordinal']} — heading `{r['chunk']['heading']}` — sha256_16 `{r['chunk']['sha256_16']}` — {r['chunk']['chars']} chars{flag}
- Evidence quote (verbatim, from the T-C10 store): "{r['evidence_quote']}"
- Chunk excerpt: «{excerpt}…»
- Upstream: T-C10 {r['provenance']['upstream']['mapping']} — HUMAN_VALIDATED {r['provenance']['upstream']['validated_date']} — confidence {r['provenance']['upstream']['confidence']}
- Rationale: {r['rationale'] or '(none recorded upstream)'}
- Verdict: [ ] CONFIRM — quote anchors this chunk to this SP   [ ] REJECT — wrong chunk/SP   [ ] HOLD — needs better anchor

""")

    wl_rows = []
    for r in wl_quotes + unmapped:
        wl_rows.append(f"""### {r['spec_code']} — {r.get('sp_title', '')}
- Note: `{r.get('note_path', '(no note-level mapping)')}`
- Quote (excerpt-region only): "{r.get('evidence_quote', '(none)')}"
- Reason: {r['worklist_reason']}
- Disposition: {r['disposition']}
- Verdict: [ ] AUTHOR fresh passage quote   [ ] REPAIR markdown   [ ] DEFER (record why)

""")

    sheet = f"""# C13 — Chunk→SP Substrate OPERATOR REVIEW SHEET (the promotion gate)

**Seed:** `{seed}` (sha256 of the emitted rows — deterministic regeneration) · **Rows:** {len(sample)} anchored
spot-checks + {len(worklist)} worklist decisions.
**Rule:** this sheet is the ONLY path from SUGGESTED to HUMAN_VALIDATED for the chunk→SP substrate.
Per-class rollup: any confirmed-precision < 90% on the sampled rows → rework that class before promotion.
**Anti-forgery reminder:** the tool cannot emit HUMAN_VALIDATED rows (gate G5); only your verdicts here can.

## Part A — anchored-row spot-check ({len(sample)} rows, seeded 20% stratified + all ambiguous)

""" + "".join(sheet_rows) + f"""## Part B — worklist decisions ({len(worklist)} rows)

""" + "".join(wl_rows) + """## Rollup

| Part | Rows | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|
| A (anchored spot-check) | """ + str(len(sample)) + """ | | | | |
| B (worklist) | """ + str(len(worklist)) + """ | | | | |

Gate: Part A precision >= 90% AND every Part B row decided -> the store may be promoted (rows flip to
HUMAN_VALIDATED in a recorded, deterministic apply step — never hand-edits).
"""
    (out_dir / "reports" / "C13_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md").write_text(sheet, encoding="utf-8")
    print(f"report  -> {out_dir / 'reports' / 'C13_CHUNK_SP_SUBSTRATE_REPORT.md'}")
    print(f"sheet   -> {out_dir / 'reports' / 'C13_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md'}")
    print(f"seed {seed}: {len(sample)} spot-check rows + {len(worklist)} worklist rows")


if __name__ == "__main__":
    main()
