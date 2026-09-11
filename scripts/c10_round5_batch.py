#!/usr/bin/env python3
"""
T-C10 round-5 staging (2026-09-11) — derive the 150-spec promotion batch
command mechanically from C10_ROUND5_REVIEW.json and stage it as sheet §13.

Operator instruction (2026-09-11): "Ratify the 59 and promote 150" — the
round-5 §11 option (b) resolved as ONE controlled promotion of all 150
round-5 CONFIRMs (no risk/section split). This script derives that command
exactly as PHASE2_PR_REVIEW_SHEET.md §12 did for the 59: same promoter,
same resolver, same spec syntax:

    CODE               promote every mapping with this code; only allowed
                       when the code lives on exactly one note
    CODE@FRAGMENT      required when the code is mapped on several notes;
                       FRAGMENT is matched case-insensitively against the
                       note's repo-relative path and must match exactly
                       one note carrying the code

Fragment ladder: full note STEM first (matching §12's readable style), then
"parent-dir/STEM" (needed where one carrier's stem is a case-insensitive
substring of a sibling carrier's path, e.g. 'Solubility - IGCSE…' is
contained in 'Investigating solubility - IGCSE…'), then the full
repo-relative path. Every spec is verified against the PRODUCTION resolver
(c10_promote.resolve_targets) before it is written.

Hard asserts before writing anything:
  - C10_ROUND5_REVIEW.json: exactly 150 reviewed pairs, all verdict CONFIRM
  - every pair resolves by exact (note-key, code) identity in the store
  - the store is exactly 209 mappings (112 notes), 0 promoted
  - the 150 derived specs are distinct and resolve via the production
    resolver to exactly the 150 round-5 pairs (no ambiguity, no drift)
  - §13 targets are disjoint from the staged §12 59-spec batch and their
    union is the whole 209-mapping store (each mapping ratified exactly
    once across the two batches)

Idempotent: re-running replaces the machine-generated §13 region (from the
'## 13.' heading to the END marker) and preserves any execution record
appended after the marker.

Usage: python3 scripts/c10_round5_batch.py
"""
from __future__ import annotations

import json
import shlex
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import c10_promote  # noqa: E402  (production promoter: resolver + loader)

REPORTS = HERE.parent / "graph" / "reports"
REVIEW = REPORTS / "C10_ROUND5_REVIEW.json"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
BY = "operator"
DATE = "2026-09-11"
END_MARKER = "<!-- c10-round5-batch-end -->"
SECTION_HEADING = "## 13. Round 5 — the 150-spec staged batch (2026-09-11)"


def fragment_for(code: str, note: str, store: dict) -> str:
    """Shortest unambiguous FRAGMENT for CODE@FRAGMENT specs. The ladder:
    full stem -> 'parent/STEM' -> full repo-relative path. Returns a
    fragment that matches exactly one note among the code's carriers
    (case-insensitive substring, exactly the production resolver's rule)."""
    carriers = [n for n, d in store.items()
                if any(m["code"] == code for m in d["mappings"])]
    if len(carriers) == 1:
        return ""  # bare code
    rel = Path(note)
    for frag in (rel.stem, f"{rel.parent.name}/{rel.stem}", str(rel)):
        hits = [n for n in carriers if frag.lower() in n.lower()]
        if len(hits) == 1:
            return frag
    sys.exit(f"FAIL: no unambiguous fragment for {code} @ {note}")


def spec_for(code: str, note: str, store: dict) -> str:
    frag = fragment_for(code, note, store)
    return code if not frag else f"{code}@{frag}"


def parse_sheet_specs(text: str, heading: str) -> list[str]:
    """Extract the --map specs from a staged sheet section's bash block."""
    sec = text.split(heading, 1)[1]
    bash = sec.split("```bash", 1)[1].split("```", 1)[0]
    tokens = shlex.split(bash.replace("\\\n", " "))
    return [t for i, t in enumerate(tokens) if i > 0 and tokens[i - 1] == "--map"]


def wrap_command(specs: list[str]) -> str:
    """Render the promoter invocation: 3 --map flags per continuation line,
    exactly the §12 layout the audit's shlex parser expects."""
    lines = ["cd work/syllabai-resources && \\"]
    for i in range(0, len(specs), 3):
        chunk = specs[i:i + 3]
        lines.append("    " + " ".join(f"--map {shlex.quote(s)}" for s in chunk)
                     + " \\")
    lines.append(f"    --by {BY} --date {DATE}")
    return "\n".join(lines)


def main() -> int:
    review = json.loads(REVIEW.read_text(encoding="utf-8"))
    pairs = review["reviewed_pairs"]
    if not (len(pairs) == 150
            and all(p["verdict"] == "CONFIRM" for p in pairs)):
        sys.exit("FAIL: review record is not 150x CONFIRM")
    if review["verdict_counts"] != {"CONFIRM": 150, "REJECT": 0, "HOLD": 0}:
        sys.exit(f"FAIL: unexpected verdict counts "
                 f"{review['verdict_counts']}")

    store = c10_promote.load_all()
    all_pairs = {(m["code"], n) for n, d in store.items()
                 for m in d["mappings"]}
    promoted = [1 for n, d in store.items() for m in d["mappings"]
                if m.get("validation", {}).get("validation_status")
                == "HUMAN_VALIDATED"]
    if len(all_pairs) != 209:
        sys.exit(f"FAIL: store is {len(all_pairs)} mappings, expected 209")
    if promoted:
        sys.exit(f"FAIL: store already carries {len(promoted)} promoted "
                 f"mappings — the staged batch is pre-execution")

    # every round-5 pair must exist in the store by exact identity
    r5_pairs = [(p["code"], p["note"]) for p in pairs]
    missing = [k for k in r5_pairs if k not in all_pairs]
    if missing:
        sys.exit(f"FAIL: round-5 pairs not in store: {missing[:3]}")

    # derive the specs and prove them against the production resolver
    specs = [spec_for(c, n, store) for c, n in r5_pairs]
    if len(set(specs)) != 150:
        sys.exit("FAIL: derived specs are not 150 distinct strings")
    targets = c10_promote.resolve_targets(store, specs)  # refuses on ambiguity
    staged = [(m["code"], n) for n, m in targets]
    if sorted(staged) != sorted(r5_pairs):
        sys.exit("FAIL: resolver drifted from the round-5 pairs")

    # reconcile against the staged §12 batch: disjoint + union = store
    sheet = SHEET.read_text(encoding="utf-8")
    s12 = parse_sheet_specs(sheet, "## 12. Round 4")
    t12 = c10_promote.resolve_targets(store, s12)
    staged12 = {(m["code"], n) for n, m in t12}
    if len(staged12) != 59:
        sys.exit(f"FAIL: §12 stages {len(staged12)} targets, expected 59")
    inter = staged12 & set(staged)
    if inter:
        sys.exit(f"FAIL: §12/§13 overlap: {sorted(inter)[:3]}")
    union = staged12 | set(staged)
    if union != all_pairs:
        gap = all_pairs - union
        extra = union - all_pairs
        sys.exit(f"FAIL: batches do not cover the store exactly once "
                 f"(missing {sorted(gap)[:3]}, extra {sorted(extra)[:3]})")

    n_bare = sum(1 for s in specs if "@" not in s)
    n_frag = 150 - n_bare
    sec_counts = {}
    for p in pairs:
        sec = f"S{p['note'].split('/')[1][0]}"
        sec_counts[sec] = sec_counts.get(sec, 0) + 1

    # ---- render §13 -------------------------------------------------------
    section = f"""
{SECTION_HEADING}

The round-5 exhaustive review (`graph/reports/C10_ROUND5_REVIEW.json` + `PHASE2_ROUND5_REVIEW_SHEET.md`, pre-review SHA `c6454c9`, artifacts committed at `c90f5ae`) reviewed the remaining 150 mappings — 209 store minus the 59 §12 ratification targets, both round-4 REJECT pairs excluded — and returned **150 CONFIRM / 0 REJECT / 0 HOLD** under the frozen guide §0.0 contributory contract + §8 command-kind rule. The operator has now resolved §11's option (b) with the instruction **"Ratify the 59 and promote 150"** (2026-09-11): one controlled promotion of all 150, no risk/section split. This section stages that command, derived mechanically from the machine record (nothing hand-typed).

```bash
{wrap_command(specs)}
```

({n_bare} bare `CODE` specs — each code on exactly one note — and {n_frag} `CODE@FRAGMENT` disambiguations, the fragment ladder preferring the note stem and falling back to `parent/stem` where one carrier's stem is a case-insensitive substring of a sibling's path. Section spread S1:{sec_counts.get('S1', 0)} / S2:{sec_counts.get('S2', 0)} / S3:{sec_counts.get('S3', 0)} / S4:{sec_counts.get('S4', 0)}. After the command: gates re-run automatically — applier ALL GREEN with `promoted HUMAN_VALIDATED: 209`, `graph_check.py` 9/9, `c10_negative_test.py` 10 classes + positive control. The pre-execution reconciliation audit `scripts/c10_ratify_audit.py` (round-5 edition) must PASS on both staged batches BEFORE either command runs; re-run with `--phase post` after execution to verify the final state.)

{END_MARKER}
"""

    # idempotent replacement of the machine region; anything after the
    # END marker (an execution record) is preserved
    body = sheet.rstrip("\n")
    if SECTION_HEADING in body:
        head, rest = body.split(SECTION_HEADING, 1)
        after = rest.split(END_MARKER, 1)
        tail = after[1] if len(after) > 1 else ""
        body = head.rstrip("\n") + "\n" + section.rstrip("\n") + tail
    else:
        body = body + "\n" + section.rstrip("\n") + "\n"
    SHEET.write_text(body + "\n", encoding="utf-8")

    print(f"staged §13: 150 specs ({n_bare} bare / {n_frag} fragment), "
          f"--by {BY} --date {DATE}")
    print(f"reconciled: §12 (59) ∩ §13 (150) = ∅; union = 209 = whole store")
    print(f"sections: {sec_counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
