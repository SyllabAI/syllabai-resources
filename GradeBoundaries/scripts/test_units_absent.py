#!/usr/bin/env python3
"""T-GRADE-8 run-003 self-check — the units-absent emission law.

The run-014 upstream note (receipt R0-AUTO-110, PR #622 chain):
build_hub_import.py should not emit a series row whose only content is a
cash-in — or should emit units-absent instead of `units: []`. run-003
ratifies the units-absent shape generator-wide: a present-but-empty
optional array (units/cashIns/components/routes/calculatorUnits) is never
emitted — that is precisely the shape the hub prebuild validator rejects.

Synthetic fixtures only — zero network, zero corpus reads, zero invention.
The October-2022..2025 FP1 incident shape (row code YFM01, cash-in only)
is reproduced exactly.

Run:  python3 test_units_absent.py    (exit 0 = law holds)
"""
from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_hub_import as b  # noqa: E402

FAILURES: list[str] = []


def check(name: str, cond: bool) -> None:
    print(("PASS " if cond else "FAIL ") + name)
    if not cond:
        FAILURES.append(name)


def ial_doc(session: str, units: list[dict], cashins: list[dict]) -> dict:
    ladder = ["A", "B", "C", "D", "E", "U"]
    return {"family": "pearson-ial", "session": session,
            "parse_warnings": [], "source": {"sha256": "ab" * 32},
            "gradeLadder": ladder,
            "subjects": [{"code": "YFM01", "gradeLadder": ladder,
                          "units": units, "cashIns": cashins}]}


CASH_IN = {"code": "YFM01", "title": "Further Pure Mathematics 1",
           "maxMark": 600,
           "boundaries": {"A": 480, "B": 420, "C": 360, "D": 300,
                          "E": 240, "U": 0}}
CASH_IN_NO_BOUNDARIES = {**CASH_IN, "boundaries": {}}
UNIT = {"code": "WFM11", "title": "Further Pure Mathematics 1",
        "maxMark": 100, "ums": {"maxMark": 100},
        "boundaries": {"A": 80, "B": 70, "C": 60, "D": 50, "E": 40, "U": 0}}

# mirrors mapping/course-map.yaml's ial-further-maths-18-further-pure-1 row
ROW = {"slug": "ial-further-maths-18-further-pure-1", "code": "YFM01",
       "board": "Edexcel", "level": "IAL", "subject": "Further Maths",
       "family": "pearson-ial", "ialCashIn": "YFM01"}


def series_of(entry: dict | None) -> dict:
    assert entry is not None and len(entry["series"]) == 1, entry
    return entry["series"][0]


def main() -> None:
    # 1. the of-record incident shape: cash-in only (October FP1 sessions)
    docs = {"October 2025": ial_doc("October 2025", [], [CASH_IN])}
    s = series_of(b.modular_ial_course_entry(ROW, docs, "pearson-ial", {}))
    check("cash-in-only session still emitted", True)
    check("units key ABSENT (not [])", "units" not in s)
    check("cashIns preserved", [c["code"] for c in s["cashIns"]] == ["YFM01"])
    check("no present-empty arrays on the row",
          all(k not in s or s[k] for k in b.OPTIONAL_ARRAY_KEYS))

    # 2. unit-bearing session whose cash-in carries no boundaries:
    #    units survive, the cashIns key stays absent
    docs = {"June 2026": ial_doc("June 2026", [UNIT], [CASH_IN_NO_BOUNDARIES])}
    s = series_of(b.modular_ial_course_entry(ROW, docs, "pearson-ial", {}))
    check("units preserved", [u["code"] for u in s["units"]] == ["WFM11"])
    check("cashIns key ABSENT", "cashIns" not in s)

    # 3. both present: both keys survive
    docs = {"June 2026": ial_doc("June 2026", [UNIT], [CASH_IN])}
    s = series_of(b.modular_ial_course_entry(ROW, docs, "pearson-ial", {}))
    check("both keys present when both have rows",
          bool(s["units"]) and bool(s["cashIns"]))

    # 4. neither has rows: session skipped entirely (unchanged law)
    docs = {"June 2026": ial_doc("June 2026", [], [CASH_IN_NO_BOUNDARIES])}
    check("row-less session skipped",
          b.modular_ial_course_entry(ROW, docs, "pearson-ial", {}) is None)

    # 5. CIE: an AS page whose routes all fail the award filter drops the
    #    routes key (components survive)
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        cie_doc = {"family": "cie", "session": "June 2025",
                   "parse_warnings": [], "source": {"sha256": "cd" * 16},
                   "gradeLadder": ["A", "B", "C", "D", "E", "U"],
                   "components": [{"code": "1", "maxMark": 75,
                                   "boundaries": {"A": 60, "C": 40, "U": 0}}],
                   "routes": [{"combination": "Components 1,2",
                               "option": "AY", "award": "A-Level",
                               "maxWeightedMark": 250,
                               "boundaries": {"A": 200, "C": 130, "U": 0}}]}
        (root / "cie" / "0606").mkdir(parents=True)
        (root / "cie" / "0606" / "June 2025.json").write_text(
            json.dumps(cie_doc))
        b.PARSED = root
        entry = b.cie_course_entry({"slug": "cie-add-maths-16",
                                    "cieSyllabus": "0606", "level": "AS",
                                    "board": "Cambridge International",
                                    "subject": "Additional Maths"})
        s = series_of(entry)
        check("components present", bool(s.get("components")))
        check("routes key ABSENT after AS award filter", "routes" not in s)

    # 6. negative control: the post-build guard refuses a law-violating bundle
    bad = {"courses": {"x": {"series": [{"session": "October 2025",
                                         "units": [], "cashIns": []}]}}}
    try:
        b.assert_no_present_empty_arrays(bad)
        check("guard raises on present-empty bundle", False)
    except SystemExit:
        check("guard raises on present-empty bundle", True)

    # 7. linear path: optional-array keys are never added there either
    lin_ladder = ["9", "8", "7", "6", "5", "4", "3", "2", "1", "U"]
    lin_doc = {"family": "pearson-int-gcse-linear", "session": "June 2026",
               "parse_warnings": [], "source": {"sha256": "ef" * 32},
               "gradeLadder": lin_ladder,
               "subjects": [{"code": "4CH1", "tier": None,
                             "gradeLadder": lin_ladder,
                             "overall": {"scale": "9-1", "maxMark": 180,
                                         "boundaries": {"9": 141, "U": 0}}}]}
    entry = b.linear_course_entry(
        {"slug": "igcse-chemistry-19", "code": "4CH1", "board": "Edexcel",
         "level": "IGCSE", "subject": "Chemistry",
         "family": "pearson-int-gcse-linear"}, {"June 2026": lin_doc})
    s = series_of(entry)
    check("linear rows carry no optional-array keys",
          all(k not in s for k in b.OPTIONAL_ARRAY_KEYS))

    print("ALL GREEN" if not FAILURES else f"FAILURES: {FAILURES}")
    sys.exit(0 if not FAILURES else 1)


if __name__ == "__main__":
    main()
