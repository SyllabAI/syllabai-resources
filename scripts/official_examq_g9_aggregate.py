#!/usr/bin/env python3
"""
official_examq_g9_aggregate.py — the OVERALL G9 learner-surface gate.

Reads the leg receipts of record and computes the overall learner-surface
disposition under the F105 aggregation law (official_examq_g9_semantics.py):

  the overall gate may be PASS only when EVERY mandatory validation leg
  (static-corpus, static-bundles, rendered) and every required check has been
  completed successfully — missing evidence must not be masked by successful
  unrelated checks, and delegated (NOT_APPLICABLE) checks are only lawful
  while the legs their contract names are themselves green.

  FAIL     any mandatory leg FAILs
  REVIEW   any leg REVIEWs, or any mandatory leg is NOT_RUN/missing, or any
           delegated check names responsible legs that are not green
  NOT_RUN  nothing ran at all
  PASS     every mandatory leg PASSed and every delegation is covered

A leg receipt whose "overall" is absent is recomputed from its cases; a leg
with no receipt at all is NOT_RUN (and therefore blocks PASS).

Usage:
  python3 scripts/official_examq_g9_aggregate.py \
    --static-corpus  Official-ExamQuestion/benchmark/receipts/<run>/g9-static-corpus.receipt.json \
    --static-bundles Official-ExamQuestion/benchmark/receipts/<run>/g9-static-bundles.receipt.json \
    --render         Official-ExamQuestion/benchmark/receipts/<run>/g9-render.receipt.json \
    --out Official-ExamQuestion/benchmark/receipts/<run>/g9-aggregate.receipt.json
Exit code: 0 iff the overall gate is PASS.
"""
import argparse
import datetime
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from official_examq_g9_semantics import (  # noqa: E402
    MANDATORY_LEGS, LEG_STATIC_CORPUS, LEG_STATIC_BUNDLES, LEG_RENDERED,
    overall_gate, leg_disposition_from_receipt,
)

VALIDATOR_VERSION = "g9-aggregate/0.1"


def main():
    ap = argparse.ArgumentParser(description="overall G9 learner-surface gate (F105 law)")
    ap.add_argument("--static-corpus", default=None, help="static corpus-leg receipt JSON")
    ap.add_argument("--static-bundles", default=None, help="static bundles-leg receipt JSON")
    ap.add_argument("--render", default=None, help="rendered-leg receipt JSON")
    ap.add_argument("--out", default=None, help="write the aggregate receipt JSON here")
    args = ap.parse_args()

    paths = {LEG_STATIC_CORPUS: args.static_corpus,
             LEG_STATIC_BUNDLES: args.static_bundles,
             LEG_RENDERED: args.render}
    receipts, load_notes = {}, []
    for leg in MANDATORY_LEGS:
        p = paths.get(leg)
        if not p:
            receipts[leg] = None
            load_notes.append(f"{leg}: no receipt supplied -> NOT_RUN (blocks PASS)")
            continue
        f = Path(p)
        if not f.exists():
            receipts[leg] = None
            load_notes.append(f"{leg}: receipt missing at {p} -> NOT_RUN (blocks PASS)")
            continue
        try:
            receipts[leg] = json.loads(f.read_text())
        except Exception as exc:
            receipts[leg] = None
            load_notes.append(f"{leg}: receipt unreadable at {p} ({exc}) -> NOT_RUN (blocks PASS)")

    disposition, reasons = overall_gate(receipts)

    leg_summary = {}
    for leg in MANDATORY_LEGS:
        r = receipts[leg]
        leg_summary[leg] = {
            "receipt": paths.get(leg),
            "present": r is not None,
            "leg_overall": leg_disposition_from_receipt(r),
            "validator_version": (r or {}).get("validator_version"),
            "benchmark_version": (r or {}).get("benchmark_version"),
        }

    receipt = {
        "receipt_schema": "syllabai.g9-aggregate-receipt/0.1",
        "validator_version": VALIDATOR_VERSION,
        "law": "F105 — overall PASS only when every mandatory leg and every "
               "required check completed successfully; NOT_RUN never promotes; "
               "delegated checks must be covered by green responsible legs",
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "legs": leg_summary,
        "load_notes": load_notes,
        "blocking_reasons": reasons,
        "overall": disposition,
    }
    if args.out:
        Path(args.out).write_text(json.dumps(receipt, indent=1))
    print(f"G9 OVERALL: {disposition}")
    for n in load_notes:
        print(f"  note: {n}")
    for r in reasons:
        print(f"  blocked-by: {r}")
    if args.out:
        print(f"  receipt -> {args.out}")
    sys.exit(0 if disposition == "PASS" else 1)


if __name__ == "__main__":
    main()
