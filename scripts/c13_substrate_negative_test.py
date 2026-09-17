#!/usr/bin/env python3
"""c13 — negative tests for the chunk→SP substrate (corruption classes must fail the RIGHT gate).

Positive control: the pristine emitted store passes verify_store.
Every tampered store must fail with the exact gate id. Zero-LLM, deterministic.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from c13_chunk_sp_substrate import load_registry, load_store, verify_store  # noqa: E402
from c13_chunk_sp_substrate import chunk_note, front_matter_split  # noqa: E402


def build_env(base: Path, in_repo: bool):
    registry = load_registry(base)
    notes_root = (base / "Chemistry IGCSE Revision Notes") if in_repo else (base / "notes")
    graph_dir = base / "graph"
    notes, store, _ = load_store(notes_root)
    idx = {}
    for n in notes:
        _, body = front_matter_split((notes_root / n["path"]).read_text(encoding="utf-8"))
        for c in chunk_note(body):
            idx[(n["path"], c["ordinal"])] = c["text"]
    doc = yaml.safe_load((graph_dir / "spec_chunk_mappings.yaml").read_text(encoding="utf-8"))
    return registry, idx, doc


def expect_fail(name, gate, doc, registry, idx):
    try:
        verify_store(doc, registry, idx)
    except SystemExit as e:
        msg = str(e)
        if gate in msg:
            print(f"  PASS {name}: {msg.splitlines()[0][:90]}")
            return
        raise SystemExit(f"NEGATIVE TEST FAIL [{name}]: expected {gate}, got: {msg}")
    raise SystemExit(f"NEGATIVE TEST FAIL [{name}]: no failure raised (gate {gate} did not fire)")


def main():
    if len(sys.argv) > 1:
        base, in_repo = Path(sys.argv[1]), False
    else:
        base, in_repo = Path(__file__).resolve().parent.parent, True
    registry, idx, pristine = build_env(base, in_repo)

    # positive control
    verify_store(copy.deepcopy(pristine), registry, idx)
    print("  PASS positive control: pristine store verifies clean")

    anchored_rows = [i for i, r in enumerate(pristine["rows"]) if "chunk" in r]
    worklist_rows = [i for i, r in enumerate(pristine["rows"]) if "worklist_reason" in r]
    assert anchored_rows and worklist_rows, "fixture rows missing"

    # 1. corrupted evidence quote (edited wording) -> G4
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[0]]["evidence_quote"] = d["rows"][anchored_rows[0]]["evidence_quote"] + " and an invented tail"
    expect_fail("corrupted evidence quote", "G4", d, registry, idx)

    # 2. mutated chunk content hash -> G4
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[0]]["chunk"]["sha256_16"] = "0" * 16
    expect_fail("mutated chunk hash", "G4", d, registry, idx)

    # 3. re-pointed chunk ordinal (quote not in that chunk) -> G4
    d = copy.deepcopy(pristine)
    r = d["rows"][anchored_rows[0]]
    other = next(o for o in range(0, 40) if o != r["chunk"]["ordinal"] and (r["note_path"], o) in idx)
    r["chunk"]["ordinal"] = other
    expect_fail("chunk re-pointed", "G4", d, registry, idx)

    # 4. forged self-claimed HUMAN_VALIDATED -> G5
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[0]]["validation_status"] = "HUMAN_VALIDATED"
    expect_fail("forged HUMAN_VALIDATED row", "G5", d, registry, idx)

    # 5. forged HUMAN_VALIDATED tier -> G5
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[0]]["provenance"]["tier"] = "HUMAN_VALIDATED"
    expect_fail("forged HUMAN_VALIDATED tier", "G5", d, registry, idx)

    # 6. upstream anchor de-validated (SUGGESTED upstream) -> G5
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[0]]["provenance"]["upstream"]["validation_status"] = "SUGGESTED"
    expect_fail("upstream de-validated", "G5", d, registry, idx)

    # 7. worklist suppression (an uncovered SP loses its row) -> G6
    d = copy.deepcopy(pristine)
    d["rows"] = [r for i, r in enumerate(d["rows"]) if i != worklist_rows[0]]
    expect_fail("worklist row suppressed", "G6", d, registry, idx)

    # 8. foreign curriculum code injected -> G3 (outside the ratified registry)
    d = copy.deepcopy(pristine)
    r = copy.deepcopy(d["rows"][anchored_rows[0]])
    r["spec_code"] = "4CH1-9.99"
    r["mapping_id"] = "forged00000000000"
    d["rows"].append(r)
    expect_fail("foreign SP code", "G3", d, registry, idx)

    # 9. foreign code that REPLACES a real code on an anchored row -> G3
    d = copy.deepcopy(pristine)
    d["rows"][anchored_rows[1]]["spec_code"] = "9999-1.1"
    expect_fail("real code swapped to foreign", "G3", d, registry, idx)

    print("NEGATIVE TESTS: 9/9 green (positive control + 9 corruption classes)")


if __name__ == "__main__":
    main()
