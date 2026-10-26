#!/usr/bin/env python3
"""tracker_check.py — V10 tracker-rollup gate (T-BOOK-065 r0, f-0035 system change).

Catches the phase-row drift class of record before it can land again:
  - c25 left the Unit-4 row headline at 3/8 while 4 packs were published
    (repaired in-lane by c27, disclosed 3/8 -> 5/8);
  - c29 flip a2005a16 updated row 29 + the c29 pack entry but left
    TRACKER.md row 66 at 'UNIT-4 LANES 6/8 ... next lane u4:c29' and
    tracker.yaml phases.unit-4 'in-progress' (repaired in 295fb5b6).

Checks (exit code = number of ERRORS, mirroring the lint convention; WARNs are
advisory and never block):
  1. Phase rollup   — phases.<unit>.status equals the rollup of member
                      pack_status values (all published => complete;
                      complete => all published).
  2. Pack truth     — tracker.yaml pack_status vs qa/lessonPackV1.json status.
  3. Phase rows     — TRACKER.md Unit-N row vs the yaml phase status
                      ('**open' headline or a stale 'LANES n/m' without
                      COMPLETE while yaml says complete => error).
  4. Lesson rows    — TRACKER.md 'pack PUBLISHED/DRAFT' cell vs pack_status.

Usage: python3 scripts/tracker_check.py [--course chemistry-4ch1] [--root DIR]
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml


def parse_chapter(dir_name: str):
    m = re.match(r"u(\d+)-c(\d+)-", dir_name)
    return (int(m.group(1)), int(m.group(2))) if m else None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", default="chemistry-4ch1")
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args()
    root = Path(args.root)

    tr = yaml.safe_load((root / "tracker.yaml").read_text(encoding="utf-8"))
    course = tr["courses"][args.course]
    cdir = root / course["path"]
    lessons = course.get("lessons") or {}
    md = (root / "TRACKER.md").read_text(encoding="utf-8")
    md_lines = md.splitlines()

    errors: list[str] = []
    warns: list[str] = []

    # chapter tuple -> (dir_name, entry)
    by_chapter = {}
    for name, e in lessons.items():
        ch = parse_chapter(name)
        ck = e.get("chapter_key")
        if ck:
            m = re.match(r"u(\d+):c(\d+)$", str(ck))
            if m and (int(m.group(1)), int(m.group(2))) != ch:
                errors.append(f"[C2] {name}: chapter_key {ck} contradicts dir name")
        if ch:
            by_chapter[ch] = (name, e)

    # ── C1: phase rollup vs member pack statuses ─────────────────────────────
    phase_rows = {}
    for key, ph in (course.get("phases") or {}).items():
        members = []
        for ref in ph.get("lessons") or []:
            m = re.match(r"u(\d+):c(\d+)$", str(ref))
            if not m:
                errors.append(f"[C1] phases.{key}: unparsable lesson ref {ref!r}")
                continue
            hit = by_chapter.get((int(m.group(1)), int(m.group(2))))
            if hit is None:
                errors.append(f"[C1] phases.{key}: ref {ref} has no tracker entry")
                continue
            members.append(hit[1].get("pack_status", "unknown"))
        status = ph.get("status")
        n_pub = sum(1 for s in members if s == "published")
        if members and n_pub == len(members) and status != "complete":
            errors.append(
                f"[C1] phases.{key}={status!r} but all {len(members)} member packs "
                f"are published — the f-0035 drift class (expected: complete)")
        elif status == "complete" and members and n_pub != len(members):
            errors.append(
                f"[C1] phases.{key}='complete' but only {n_pub}/{len(members)} "
                "member packs are published")
        elif 0 < n_pub < len(members) and status == "not-started":
            warns.append(f"[C1] phases.{key}='not-started' but {n_pub}/{len(members)} published (stale)")
        # ── C3: phase row in TRACKER.md vs yaml status ────────────────────────
        label = {"pilot-gate": "Pilot gate", "unit-1-rest": "Unit 1 rest"}.get(
            key, key.replace("-", " ").title())
        row = next((l for l in md_lines if l.startswith(f"| {label} |")), None)
        if row is None:
            warns.append(f"[C3] no TRACKER.md row found for phase {key} ({label!r})")
            continue
        cell = row.split("|")[3] if row.count("|") >= 3 else ""
        if status == "complete":
            # headline = the cell's lead segment before the first ':', ';' or
            # em-dash — the tail narrative may legitimately contain 'COMPLETE'
            # from a closure statement, so only the headline can contradict.
            headline = re.split(r"[:;—]", cell, 1)[0]
            if re.match(r"\s*\*\*open\b", headline):
                errors.append(f"[C3] phases.{key}='complete' but its TRACKER.md row still opens with '**open' — f-0035 class")
            m = re.search(r"LANES (\d+)/(\d+)", headline)
            if m and int(m.group(1)) < int(m.group(2)):
                errors.append(f"[C3] phases.{key}='complete' but its TRACKER.md row headline reads 'LANES {m.group(1)}/{m.group(2)}' — f-0035 class (c25/c29 signature)")
            if "COMPLETE" not in headline and "closed" not in headline:
                warns.append(f"[C3] phases.{key}='complete' but its row headline carries neither 'COMPLETE' nor 'closed' (pre-convention row — consider re-stamping)")
        elif re.search(r"LANES COMPLETE|UNIT-\d COMPLETE", cell):
            warns.append(f"[C3] TRACKER.md row for phases.{key} declares COMPLETE but yaml status is {status!r} (md ahead of yaml)")

    # ── C2: pack ground truth (qa/lessonPackV1.json vs pack_status) ──────────
    for name, e in lessons.items():
        ps = e.get("pack_status")
        jf = cdir / "lessons" / name / "qa" / "lessonPackV1.json"
        if not jf.exists():
            if ps == "published":
                errors.append(f"[C2] {name}: pack_status='published' but {jf.relative_to(root)} is missing")
            continue
        jstatus = json.loads(jf.read_text(encoding="utf-8")).get("status")
        if ps == "published" and jstatus != "published":
            errors.append(f"[C2] {name}: tracker says 'published' but lessonPackV1.json status={jstatus!r}")
        elif jstatus == "published" and ps != "published":
            errors.append(f"[C2] {name}: lessonPackV1.json is published but tracker pack_status={ps!r} (yaml behind json)")

    # ── C4: per-lesson TRACKER.md rows vs pack_status ────────────────────────
    for name, e in lessons.items():
        ch = parse_chapter(name)
        if not ch:
            continue
        pat = re.compile(rf"^\| \d+ \| u{ch[0]}:c{ch[1]:02d} ")
        row = next((l for l in md_lines if pat.match(l)), None)
        if row is None:
            warns.append(f"[C4] no TRACKER.md lesson row for {name}")
            continue
        ps = e.get("pack_status")
        if ps == "published":
            if "pack PUBLISHED" not in row:
                errors.append(f"[C4] {name}: tracker says 'published' but its TRACKER.md row lacks 'pack PUBLISHED'")
            if "pack DRAFT" in row:
                errors.append(f"[C4] {name}: tracker says 'published' but its TRACKER.md row still says 'pack DRAFT'")
        elif ps == "draft":
            if "pack DRAFT" not in row:
                errors.append(f"[C4] {name}: tracker says 'draft' but its TRACKER.md row lacks 'pack DRAFT'")

    # ── report ────────────────────────────────────────────────────────────────
    for w in warns:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"tracker_check: {len(lessons)} lessons, {len(course.get('phases') or {})} phases — "
          f"{len(errors)} error(s), {len(warns)} warn(s)")
    return len(errors)


if __name__ == "__main__":
    sys.exit(main())
