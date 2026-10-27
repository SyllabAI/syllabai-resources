#!/usr/bin/env python3
"""
c19_promote_test.py — negative tests for the T-C19 attachment-promotion pathway.
No network, no keys, no repo mutation: exercises the sheet parser, the gate
arithmetic re-computation, and the attribution gate with synthetic inputs, plus
fail-closed behavior on drifted/absent identities (c12_review_test.py spirit).

Run: python3 scripts/c19_promote_test.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import c19_promote as promote  # noqa: E402

FAILS = []


def expect_fail(fn, label):
    try:
        fn()
    except SystemExit:
        print(f"  PASS (fail-closed): {label}")
        return
    FAILS.append(label)
    print(f"  FAIL (did not abort): {label}")


def expect_ok(fn, label):
    try:
        fn()
    except SystemExit as e:
        FAILS.append(label)
        print(f"  FAIL (aborted: {e}): {label}")
        return
    print(f"  PASS: {label}")


def sheet_text(rollup_rows, gate="gate arithmetic **PASSES**", filled=True, verdict="x"):
    rows = "\n".join(rollup_rows)
    return f"""# C19 sheet
{"**Filled:** 2026-09-19" if filled else "unfilled"}
- Verdict: [{verdict}] CONFIRM — ok   [ ] REJECT — ok   [ ] HOLD — ok
## Rollup (filled at gate time)
| Class (role|section) | stratum rows | sampled | CONFIRM | REJECT | HOLD | precision |
|---|---:|---:|---:|---:|---:|---:|
{rows}
{gate}
"""


ROW = "### 1. `4CH1-CON-ACTIVATION-ENERGY` PART_OF `4CH1-3.14C` — mapping_id `x`\n- Verdict: [{v}] CONFIRM — the concept genuinely subsumes this SP's demand   [ ] REJECT — wrong concept/SP pairing   [ ] HOLD — needs better evidence (state what)\n"
GOOD = ("| CORE|S1 | 1 | 1 | 1 | 0 | 0 | 1/1 = 100% |")


def t_sheet_parsing():
    # happy path parses
    text = sheet_text([GOOD]).replace("- Verdict:", ROW.split("- Verdict:")[0] + "- Verdict:")
    text = sheet_text([GOOD]) + "\n" + ROW.format(v="x")
    verdicts, claimed, partb = promote.parse_sheet(text)
    assert verdicts == {("4CH1-CON-ACTIVATION-ENERGY", "4CH1-3.14C"): "CONFIRM"}, verdicts
    assert claimed[0]["cls"] == "CORE|S1"
    print("  PASS: happy-path sheet parses (verdicts + rollup)")
    # two boxes ticked
    def bad_two():
        bad = ROW.format(v="x").replace("[ ] REJECT", "[x] REJECT")
        promote.parse_sheet(sheet_text([GOOD]) + "\n" + bad)
    expect_fail(bad_two, "two verdict boxes ticked")
    # zero boxes ticked
    def bad_zero():
        promote.parse_sheet(sheet_text([GOOD]) + "\n" + ROW.format(v=" "))
    expect_fail(bad_zero, "no verdict box ticked")
    # unfilled sheet
    def bad_unfilled():
        promote.parse_sheet(sheet_text([GOOD], filled=False) + "\n" + ROW.format(v="x"))
    expect_fail(bad_unfilled, "unfilled sheet")
    # gate line not a PASS
    def bad_gate():
        promote.parse_sheet(sheet_text([GOOD], gate="gate arithmetic **PENDING**") + "\n" + ROW.format(v="x"))
    expect_fail(bad_gate, "gate line PENDING")


def t_gate_arithmetic():
    rows_by = {("A", "B"): {"role": "CORE", "section": "S1"},
               ("C", "D"): {"role": "CORE", "section": "S1"}}
    # happy path: 2/2 CONFIRM = 100% >= gate, arithmetic matches the claim
    verdicts_ok = {("A", "B"): "CONFIRM", ("C", "D"): "CONFIRM"}
    claimed_ok = [{"cls": "CORE|S1", "stratum": 2, "sampled": 2,
                   "confirm": 2, "reject": 0, "hold": 0}]
    expect_ok(lambda: promote.verify_gate(verdicts_ok, claimed_ok, rows_by),
              "arithmetic matches claim (100% >= gate)")
    # arithmetic mismatch: claim inflates CONFIRM
    verdicts_mix = {("A", "B"): "CONFIRM", ("C", "D"): "REJECT"}
    expect_fail(lambda: promote.verify_gate(
        verdicts_mix, [{"cls": "CORE|S1", "stratum": 2, "sampled": 2, "confirm": 2,
                        "reject": 0, "hold": 0}], rows_by),
        "arithmetic mismatch (claim inflates CONFIRM)")
    # precision below gate: arithmetic matches (1 CONFIRM + 1 REJECT) but 1/2 = 50% < 90%
    claimed_mix = [{"cls": "CORE|S1", "stratum": 2, "sampled": 2,
                    "confirm": 1, "reject": 1, "hold": 0}]
    expect_fail(lambda: promote.verify_gate(verdicts_mix, claimed_mix, rows_by),
                "precision below gate (1/2 = 50%)")


def t_attribution():
    def bad_by():
        if promote.AI_NAME_RE.search("Super-Z-agent"):
            raise SystemExit("attribution gate")
    expect_fail(bad_by, "AI-name attribution rejected")
    def good_by():
        if promote.AI_NAME_RE.search("operator-directive-session-106"):
            raise SystemExit("attribution gate fired on a clean identity")
    expect_ok(good_by, "operator-directive identity accepted")


def t_drift():
    # an identity absent from the live rows must fail verify_gate's lookup
    def absent():
        promote.verify_gate({("NO", "SUCH"): "CONFIRM"},
                            [{"cls": "CORE|S1", "stratum": 1, "sampled": 1,
                              "confirm": 1, "reject": 0, "hold": 0}], {})
    expect_fail(absent, "sheet identity not in live store (drift)")


def main():
    print("c19_promote_test: negative tests")
    t_sheet_parsing()
    t_gate_arithmetic()
    t_attribution()
    t_drift()
    # the real sheet must parse + verify against the live store (read-only)
    sheet = HERE.parent / "graph" / "reports" / "C19_CONCEPT_SP_SUBSTRATE_REVIEW_SHEET.md"
    if sheet.exists():
        import c19_substrate_verify as sub
        rows, problems, counts = sub.build_rows(HERE.parent)
        assert not problems
        live = {(r["edge"]["source"], r["edge"]["target"]): r for r in rows}
        verdicts, claimed, _ = promote.parse_sheet(sheet.read_text(encoding="utf-8"))
        promote.verify_gate(verdicts, claimed, live)
        print(f"  PASS: real sheet verifies against the live store "
              f"({len(verdicts)} sampled rows, {counts['part_of']} attachments)")
    else:
        print("  (real sheet absent — sandbox environment; skipped)")
    if FAILS:
        print(f"FAIL: {len(FAILS)} test(s): {FAILS}", file=sys.stderr)
        return 1
    print("c19_promote_test: ALL PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
