#!/usr/bin/env python3
"""
T-C10 — batch promotion helper for the PR front-matter review.

Marks reviewed note->spec-point mappings as HUMAN_VALIDATED in the decisions
JSON (the source of truth) and re-runs the gated applier so the note front
matter carries the promotion.

Promotions MUST live in the decisions files, never as hand-edits on note
front matter: `c10_map_notes.py` regenerates front matter from decisions on
every run and would silently revert hand edits on the next rework re-run
(the applier's G7 gate and the validator's c10.3 enforce the block shape).

Spec syntax (repeatable --map):
    CODE               promote every mapping with this code; only allowed
                       when the code lives on exactly one note
    CODE@FRAGMENT      required when the code is mapped on several notes;
                       FRAGMENT is matched case-insensitively against the
                       note's repo-relative path and must match exactly
                       one note carrying the code

Options:
    --by NAME          validator identity recorded (default: operator)
    --date YYYY-MM-DD  promotion date (default: today)
    --no-apply         edit the decisions only; skip the applier re-run

Idempotent: promoting an already-promoted mapping is a reported no-op; the
decisions file style (compact mapping objects, indent 2) is preserved.

Usage:
    python3 scripts/c10_promote.py --map 4CH1-4.15 --map '4CH1-1.10@chromatography'
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DECISION_DIR = HERE / "c10_decisions"
RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def dump_decisions(data: dict) -> str:
    """Match the existing decisions-file style exactly: indent 2/4 for the
    note/mappings structure, each mapping object compact on a single line."""
    out = ["{"]
    keys = list(data.keys())
    for i, k in enumerate(keys):
        out.append(f"  {json.dumps(k, ensure_ascii=False)}: {{")
        out.append('    "mappings": [')
        maps = data[k]["mappings"]
        for j, m in enumerate(maps):
            comma = "," if j < len(maps) - 1 else ""
            out.append(f"      {json.dumps(m, ensure_ascii=False)}{comma}")
        out.append("    ]")
        out.append("  }" + ("," if i < len(keys) - 1 else ""))
    out.append("}")
    return "\n".join(out) + "\n"


def load_all() -> dict:
    """note-rel -> {"file": Path, "file_data": dict, "mappings": [...]}.
    Verifies cross-file key uniqueness while loading; mutations to the
    mapping dicts are reflected in file_data (same objects), so writing
    file_data back to disk preserves them."""
    decisions, seen = {}, {}
    for f in sorted(DECISION_DIR.glob("S*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for note, d in data.items():
            if note in seen:
                sys.exit(f"FAIL: note key in two decision files: {note} "
                         f"({seen[note].name} and {f.name})")
            seen[note] = f
            decisions[note] = {"file": f, "file_data": data,
                               "mappings": d["mappings"]}
    return decisions


def resolve_targets(decisions: dict, specs: list[str]) -> list[tuple[str, dict]]:
    """Resolve --map specs to (note-rel, mapping) pairs with ambiguity errors."""
    targets = []
    for spec in specs:
        if "@" in spec:
            code, frag = spec.split("@", 1)
            hits = [(n, d) for n, d in decisions.items()
                    if any(m["code"] == code for m in d["mappings"])
                    and frag.lower() in n.lower()]
        else:
            code, frag = spec, None
            hits = [(n, d) for n, d in decisions.items()
                    if any(m["code"] == code for m in d["mappings"])]
        if not hits:
            sys.exit(f"FAIL: no mapping found for {spec!r}")
        if len(hits) > 1:
            cand = "\n  ".join(n for n, _ in hits)
            sys.exit(f"FAIL: {spec!r} is ambiguous across {len(hits)} notes — "
                     f"disambiguate with CODE@FRAGMENT:\n  {cand}")
        note, d = hits[0]
        m = next(m for m in d["mappings"] if m["code"] == code)
        targets.append((note, m))
    return targets


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--map", action="append", required=True, metavar="SPEC",
                    help="CODE or CODE@FRAGMENT (repeatable)")
    ap.add_argument("--by", default="operator", help="validator identity")
    ap.add_argument("--date", default=datetime.date.today().isoformat(),
                    help="promotion date (YYYY-MM-DD)")
    ap.add_argument("--no-apply", action="store_true",
                    help="edit decisions only; skip the applier re-run")
    args = ap.parse_args()

    if not RE_ISO_DATE.match(args.date):
        sys.exit(f"FAIL: --date must be YYYY-MM-DD, got {args.date!r}")

    decisions = load_all()
    targets = resolve_targets(decisions, args.map)

    changed_files, promoted, noop = set(), [], []
    for note, m in targets:
        val = m.get("validation")
        if isinstance(val, dict) and val.get("validation_status") == "HUMAN_VALIDATED":
            noop.append(f"{m['code']} @{Path(note).name} (already promoted by "
                        f"{val.get('validated_by')} on {val.get('validated_date')})")
            continue
        m["validation"] = {
            "validation_status": "HUMAN_VALIDATED",
            "validated_by": args.by,
            "validated_date": args.date,
        }
        # keep key order stable: code, confidence, evidence, rationale,
        # then validation
        ordered = {k: m[k] for k in m if k != "validation"}
        ordered["validation"] = m["validation"]
        m.clear()
        m.update(ordered)
        changed_files.add(decisions[note]["file"])
        promoted.append(f"{m['code']} @{Path(note).name}")

    for msg in noop:
        print("-", msg)
    for msg in promoted:
        print("PROMOTED", msg)
    if not promoted and not noop:
        print("nothing to do")
        return 0

    # write back the in-memory file data (mutations included), preserving
    # each file's note ordering and the compact decisions style
    for f in sorted(changed_files):
        data = next(d["file_data"] for d in decisions.values()
                    if d["file"] == f)
        f.write_text(dump_decisions(data), encoding="utf-8")
        print("decisions updated:", f.name)
    print("next: front matter carries the promotion after the gated applier "
          "re-run (G7 validates every validation block)")

    if args.no_apply:
        return 0
    r = subprocess.run([sys.executable, str(HERE / "c10_map_notes.py")])
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
