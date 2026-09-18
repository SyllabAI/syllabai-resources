#!/usr/bin/env python3
"""
T-C19 — c19_promote.py: operator-side promotion of concept→SP attachment rows
(the expansion round c11_promote.py names; c10/c11/c12 promotions-file family).

Promotion path (CONCEPT_SPEC_POINT_MAPPING_VALIDATION_LANE.md §7, RATIFIED v1.1):

  filled operator review sheet  ->  scripts/c19_promotions.yaml (this tool,
  the only writer)  ->  gated generator re-run (c11_concept_pilot.py G19)  ->
  graph/concept_edges.yaml PART_OF rows carry HUMAN_VALIDATED + validated_by/date.

Hard properties (fail closed):
  * the filled sheet is the ONLY input verdict authority; the tool re-computes
    the gate arithmetic from the verdict boxes and asserts it against the
    sheet's claimed rollup before anything is written;
  * class-licensing per the ratified C13 model: a class that passes at >= 90%
    confirmed-precision licenses ALL of its rows; rows the sheet marks
    REJECT/HOLD are never promoted; Part B gap rows are never promoted;
  * every promoted identity must resolve to an existing store attachment
    (drift check: the live store rows are re-derived and must match the sheet
    substrate exactly);
  * attribution gate: AI self-attribution is forbidden (same as c11_promote);
  * idempotent: re-recording an identity is a reported no-op;
  * the store is NEVER hand-edited: the generator is the only writer.

Usage:
  python3 scripts/c19_promote.py --sheet graph/reports/C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md
  python3 scripts/c19_promote.py --sheet ... --check   # verify sheet + drift only
"""
from __future__ import annotations

import argparse
import datetime
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PROMOTIONS = HERE / "c19_promotions.yaml"
SHEET_DEFAULT = "graph/reports/C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md"
GATE_MIN_PRECISION = 0.90

RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)


def die(msg: str):
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        die(f"{path.name} does not parse: {e}")


def parse_sheet(text: str):
    """Extract per-identity verdicts + claimed rollup + gate line from the sheet."""
    if "**Filled:**" not in text:
        die("sheet is not filled (no **Filled:** header)")
    # per-row verdicts: '### N. `SRC` PART_OF `TGT` — mapping_id `MID`' then a verdict line
    verdicts = {}   # (src, tgt) -> 'CONFIRM'|'REJECT'|'HOLD'
    for block in re.split(r"\n### ", text)[1:]:
        head = block.split("\n", 1)[0]
        m = re.match(r"\d+\. `([4A-Z0-9-]+)` PART_OF `([4A-Z0-9.C-]+)`", head)
        if not m:
            continue
        src, tgt = m.group(1), m.group(2)
        vm = re.search(r"- Verdict: \[([ x])\] CONFIRM[^\n]*\[([ x])\] REJECT[^\n]*\[([ x])\] HOLD", block)
        if not vm:
            die(f"row {src} PART_OF {tgt}: verdict line missing/unticked-format")
        marks = [vm.group(1), vm.group(2), vm.group(3)]
        if marks.count("x") != 1:
            die(f"row {src} PART_OF {tgt}: exactly one verdict box must be ticked")
        verdicts[(src, tgt)] = ["CONFIRM", "REJECT", "HOLD"][marks.index("x")]
    # claimed class rollup rows: | CLASS | stratum | sampled | CONFIRM | REJECT | HOLD | precision |
    claimed = []
    for ln in text.splitlines():
        m = re.match(r"\| (CORE\|S\d|ENRICHMENT\|S\d|SUPPORTING\|S\d|FAIL\|S\d) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| ([^|]+) \|", ln)
        if m:
            claimed.append({"cls": m.group(1), "stratum": int(m.group(2)),
                            "sampled": int(m.group(3)), "confirm": int(m.group(4)),
                            "reject": int(m.group(5)), "hold": int(m.group(6))})
    if not claimed:
        die("sheet rollup table missing or unfilled")
    if "gate arithmetic **PASSES**" not in text:
        die("sheet gate line is not a recorded PASS")
    # Part B decisions
    partb = len(re.findall(r"- Verdict: \[x\] DEFER", text))
    return verdicts, claimed, partb


def verify_gate(verdicts, claimed, rows_by_id_all):
    """Re-compute per-class arithmetic from verdict boxes; assert vs claimed rollup."""
    sampled_ids = set(verdicts)
    per = {}
    for (src, tgt), v in verdicts.items():
        r = rows_by_id_all.get((src, tgt))
        if r is None:
            die(f"sheet row {src} PART_OF {tgt} is not a live store attachment (drift)")
        cls = f"{r['role']}|{r['section']}"
        per.setdefault(cls, {"sampled": 0, "confirm": 0, "reject": 0, "hold": 0})
        per[cls]["sampled"] += 1
        per[cls][v.lower()] += 1
    if set(per) != {c["cls"] for c in claimed}:
        die(f"rollup classes {sorted({c['cls'] for c in claimed})} != verdict classes {sorted(per)}")
    for c in claimed:
        got = per[c["cls"]]
        if (got["sampled"], got["confirm"], got["reject"], got["hold"]) != \
           (c["sampled"], c["confirm"], c["reject"], c["hold"]):
            die(f"rollup mismatch for {c['cls']}: sheet claims "
                f"{(c['sampled'], c['confirm'], c['reject'], c['hold'])}, verdict boxes give "
                f"{(got['sampled'], got['confirm'], got['reject'], got['hold'])}")
        prec = got["confirm"] / got["sampled"] if got["sampled"] else 0.0
        if prec < GATE_MIN_PRECISION:
            die(f"gate FAIL for {c['cls']}: confirmed-precision {prec:.3f} < {GATE_MIN_PRECISION}")
        print(f"  class {c['cls']}: {got['confirm']}/{got['sampled']} = {prec:.0%} >= {GATE_MIN_PRECISION:.0%}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sheet", default=SHEET_DEFAULT)
    ap.add_argument("--by", default="operator-directive-session-106")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--check", action="store_true",
                    help="verify sheet + drift + record plan; write nothing")
    args = ap.parse_args()

    if not RE_ISO_DATE.match(args.date):
        die(f"--date must be YYYY-MM-DD, got {args.date!r}")
    if not args.by or AI_NAME_RE.search(args.by):
        die(f"--by {args.by!r} fails the attribution gate: promotion is "
            f"operator-only and AI self-attribution is forbidden (fail closed)")

    sheet_path = REPO / args.sheet
    if not sheet_path.is_file():
        die(f"review sheet not found: {args.sheet}")
    text = sheet_path.read_text(encoding="utf-8")
    verdicts, claimed, partb = parse_sheet(text)
    n_confirm = sum(1 for v in verdicts.values() if v == "CONFIRM")
    n_reject = sum(1 for v in verdicts.values() if v == "REJECT")
    n_hold = sum(1 for v in verdicts.values() if v == "HOLD")
    print(f"sheet: {len(verdicts)} sampled rows decided "
          f"({n_confirm} CONFIRM / {n_reject} REJECT / {n_hold} HOLD); Part B DEFERs: {partb}")

    # drift check: re-derive the live store attachment rows and require exact match
    sys.path.insert(0, str(HERE))
    import c19_substrate_verify as sub
    mirror = REPO
    rows, problems, counts = sub.build_rows(mirror)
    if problems:
        die(f"live store structural problems: {problems[:3]}")
    live = {(r["edge"]["source"], r["edge"]["target"]): r for r in rows}
    if counts["part_of"] != 117:
        die(f"live store PART_OF count {counts['part_of']} != the sheet substrate's 117 "
            f"(store drift since the sheet was emitted; re-run c19_substrate_verify.py and re-gate)")
    for key in verdicts:
        if key not in live:
            die(f"sheet identity {key} absent from the live store (drift)")

    # class rollup over the LIVE rows for sampled strata
    verify_gate(verdicts, claimed, live)

    # class-licensed promotion set: all live rows of every passing class,
    # minus any row the sheet individually REJECTed or HOLDed
    rejected = {k for k, v in verdicts.items() if v in ("REJECT", "HOLD")}
    promote = [k for k in live if k not in rejected]
    print(f"promotion plan: {len(promote)}/{len(live)} attachment rows "
          f"(class-licensed; {len(rejected)} individually excluded)")

    existing = {}
    if PROMOTIONS.exists():
        rec = load_yaml(PROMOTIONS)
        for p in (rec.get("promotions") or []):
            a = p["attachment"]
            existing[(a["concept"], a["spec_point"])] = p
    todo = [k for k in promote if k not in existing]
    noop = [k for k in promote if k in existing]
    for k in noop:
        print("-", f"{k[0]} PART_OF {k[1]} (already promoted by {existing[k]['validated_by']})")
    if not todo:
        print("nothing to record")
        return 0

    ref = (f"{args.sheet} (Part A class rollup; sampled rows individually marked; "
           f"seed + method on the sheet)")
    if args.check:
        print(f"CHECK mode: {len(todo)} entries would be recorded; no files written")
        return 0

    entries = []
    for k in sorted(todo):
        entries.append({
            "attachment": {"concept": k[0], "spec_point": k[1]},
            "validated_by": args.by,
            "validated_date": args.date,
            "review_reference": ref,
        })
    promo = {
        "meta": {
            "task": "T-C19",
            "stage": "attachment-promotion",
            "contract": "CONCEPT_SPEC_POINT_MAPPING_VALIDATION_LANE.md §7 (RATIFIED v1.1)",
            "decision_record": "graph/reports/C19_SUBSTRATE_ROWS.yaml + filled review sheet",
            "tool": "scripts/c19_promote.py",
            "generated_date": args.date,
        },
        "promotions": sorted(
            (list(existing.values())
             + entries),
            key=lambda p: (p["attachment"]["concept"], p["attachment"]["spec_point"])),
    }
    promo_text = (
        "# T-C19 attachment promotion record — operator ratifications of concept→SP\n"
        "# PART_OF attachment identities (the expansion round named by c11_promote.py).\n"
        "# Written ONLY by scripts/c19_promote.py; see the lane spec §7.\n"
        "# Hand-editing is forbidden.\n"
        + yaml.safe_dump(promo, allow_unicode=True, sort_keys=False, width=100))
    yaml.safe_load(promo_text)  # fail-closed: parse before replacing the record
    tmp = PROMOTIONS.with_suffix(".yaml.tmp")
    tmp.write_text(promo_text, encoding="utf-8")
    os.replace(tmp, PROMOTIONS)  # atomic
    print(f"promotions recorded: {PROMOTIONS.name} ({len(todo)} new, {len(existing)} existing)")
    for k in todo[:5]:
        print("PROMOTED", f"{k[0]} PART_OF {k[1]}")
    if len(todo) > 5:
        print(f"  ... and {len(todo) - 5} more")

    r = subprocess.run([sys.executable, str(HERE / "c11_concept_pilot.py")], cwd=REPO)
    if r.returncode != 0:
        print("NOTE: the generator rejected the state — the promotions file "
              "retains the entries above and graph_check will flag any "
              "graph/promotions mismatch; fix the underlying evidence or "
              "revert the promotions file via git.", file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
