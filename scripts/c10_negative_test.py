#!/usr/bin/env python3
"""
T-C10 — negative tests for the c10-notes-mapping check group in graph_check.py.

Ten corruption classes are injected into a throwaway copy of the notes tree
(markdown files only; assets are skipped by the checker anyway). Each class
MUST be caught by check_notes_mapping; a missing catch fails this script.

Classes:
  1. spec_map removed from a note
  2. invented code outside the 182-point registry (4CH1-9.99)
  3. provenance field (evidence) emptied
  4. subsection anchor corrupted
  5. spec_points list emptied
  6. foreign-curriculum code (4CH0) planted in front matter
  7. a note file deleted
  8. tier flipped to HUMAN_VALIDATED (premature authority)
  9. validation_status promoted WITHOUT the required validated_by/date
 10. stray validated_by on a still-SUGGESTED mapping

A positive control then verifies the promotion pathway: a COMPLETE
HUMAN_VALIDATED block (validated_by + ISO date, tier still AI_SUGGESTED)
must PASS the validator — otherwise the promotion pathway would be unusable.

Usage: python3 scripts/c10_negative_test.py
"""
from __future__ import annotations

import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent / "scripts"))
import graph_check as gc  # noqa: E402

REPO = gc.REPO
NOTES = REPO / "Chemistry IGCSE Revision Notes"


def clone_notes(tmp: Path) -> Path:
    root = tmp / "notes"
    for src in sorted(NOTES.rglob("*.md")):
        dst = root / src.relative_to(NOTES)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    return root


def run_check(notes_root: Path):
    data = gc.load_all(gc.GRAPH_DEFAULT)
    point_codes = gc.check_spec_points(data)[1]
    _, _, sub_codes, _ = gc.check_topics(data, point_codes)
    return gc.check_notes_mapping(data, point_codes, sub_codes, notes_root=notes_root)


def pick_note(root: Path) -> Path:
    return sorted(root.rglob("*.md"))[3]


def edit_fm(path: Path, fn) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    close = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    fm = yaml.safe_load("".join(lines[1:close]))
    fm = fn(fm)
    new_fm = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False, width=100)
    path.write_text("---\n" + new_fm + "---\n" + "".join(lines[close + 1:]),
                    encoding="utf-8")


TESTS = []


def test(name, expect_substrings):
    def deco(fn):
        TESTS.append((name, fn, expect_substrings))
        return fn
    return deco


@test("spec_map removed", ["c10.1 missing spec_map"])
def t1(root):
    edit_fm(pick_note(root), lambda fm: {k: v for k, v in fm.items() if k != "spec_map"})


@test("invented registry-foreign code", ["c10.2 code not in 182-registry"])
def t2(root):
    def corrupt(fm):
        fm["spec_map"]["spec_points"][0]["code"] = "4CH1-9.99"
        return fm
    edit_fm(pick_note(root), corrupt)


@test("evidence emptied", ["c10.3 missing evidence"])
def t3(root):
    def corrupt(fm):
        fm["spec_map"]["spec_points"][0]["provenance"]["evidence"] = ""
        return fm
    edit_fm(pick_note(root), corrupt)


@test("subsection anchor corrupted", ["c10.4"])
def t4(root):
    def corrupt(fm):
        fm["spec_map"]["subsection"] = "4CH1-S9-z"
        return fm
    edit_fm(pick_note(root), corrupt)


@test("spec_points emptied", ["c10.5 zero mappings", "c10.7 covered points"])
def t5(root):
    def corrupt(fm):
        fm["spec_map"]["spec_points"] = []
        return fm
    edit_fm(pick_note(root), corrupt)


@test("foreign 4CH0 code planted", ["c10.6 foreign curriculum code"])
def t6(root):
    def corrupt(fm):
        fm["spec_map"]["mapper"] = "4CH0 contamination probe"
        return fm
    edit_fm(pick_note(root), corrupt)


@test("note file deleted", ["note count"])
def t7(root):
    pick_note(root).unlink()


@test("tier prematurely HUMAN_VALIDATED", ["c10.3 wrong tier"])
def t8(root):
    def corrupt(fm):
        fm["spec_map"]["spec_points"][0]["provenance"]["tier"] = "HUMAN_VALIDATED"
        return fm
    edit_fm(pick_note(root), corrupt)


@test("promotion without validated_by/date", ["c10.3 HUMAN_VALIDATED missing validated_by"])
def t9(root):
    def corrupt(fm):
        prov = fm["spec_map"]["spec_points"][0]["provenance"]
        prov["validation_status"] = "HUMAN_VALIDATED"
        return fm
    edit_fm(pick_note(root), corrupt)


@test("stray validated_by on SUGGESTED mapping", ["c10.3 stray validated_by"])
def t10(root):
    def corrupt(fm):
        fm["spec_map"]["spec_points"][0]["provenance"]["validated_by"] = "operator"
        return fm
    edit_fm(pick_note(root), corrupt)


def positive_control() -> bool:
    """A COMPLETE HUMAN_VALIDATED block (tier still AI_SUGGESTED) must pass
    the validator — otherwise the promotion pathway would be unusable."""
    with tempfile.TemporaryDirectory(dir=HERE) as td:
        root = clone_notes(Path(td))

        def promote(fm):
            prov = fm["spec_map"]["spec_points"][0]["provenance"]
            prov["validation_status"] = "HUMAN_VALIDATED"
            prov["validated_by"] = "operator"
            prov["validated_date"] = "2026-09-11"
            return fm
        edit_fm(pick_note(root), promote)
        chk = run_check(root)
    if chk.ok:
        print("POSITIVE CONTROL OK: complete HUMAN_VALIDATED block passes")
        return True
    print("POSITIVE CONTROL FAILED: legitimate promotion rejected:")
    for m in chk.failures[:5]:
        print("  -", m)
    return False


def main():
    failures = []
    for name, fn, expects in TESTS:
        with tempfile.TemporaryDirectory(dir=HERE) as td:
            root = clone_notes(Path(td))
            fn(root)
            chk = run_check(root)
        msgs = chk.failures
        if chk.ok:
            failures.append(f"{name}: NOT CAUGHT (validator passed)")
            continue
        for exp in expects:
            if not any(exp in m for m in msgs):
                failures.append(f"{name}: expected {exp!r} not in failures: {msgs[:3]}")
        print(f"CAUGHT  {name}  ({len(msgs)} issue(s); e.g. {msgs[0]})")
    print()
    if failures:
        print(f"c10_negative_test: {len(failures)} PROBLEM(S):")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    if not positive_control():
        sys.exit(1)
    print(f"c10_negative_test: ALL {len(TESTS)} CORRUPTION CLASSES CAUGHT "
          f"(+ positive control passing)")


if __name__ == "__main__":
    main()
