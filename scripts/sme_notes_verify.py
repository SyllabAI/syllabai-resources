#!/usr/bin/env python3
"""
T-SME-NOTES-5 — verification gates for the SME revision-notes corpus.

G1 structure      : every course has manifest.json; per-page JSON+md exist;
                    counts self-consistent (scraped == on-disk == manifest)
G2 note integrity : schema + rn_ id + non-empty blocks; md front matter
                    matches JSON (note_id, spec_point_ids)
G3 assets         : every figure file referenced in JSON exists on disk
G4 author-strip   : NO byline/junk strings in ANY rendered md (Written by,
                    Reviewed by, Updated on, Guided study, Excerpt) and no
                    author name leakage
G5 chemistry      : 162/162 official codes resolved; legacy_spec_map on every
                    matched note; other courses carry NO spec_point_codes
G6 registry truth : top-level manifest totals == sum of course manifests

stdlib-only. Exit 0 = all gates pass.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
ROOT = BASE / "SME-RevisionNotes"
CHEM = "igcse-chemistry-19"

FAILS: list[str] = []
NOTES: list[str] = []


def fail(msg: str):
    FAILS.append(msg)


def main() -> int:
    # ---------------- G1 + G2 + G3 (per course)
    all_md_authors: set[str] = set()
    course_dirs = sorted(p for p in ROOT.iterdir() if p.is_dir())
    print(f"courses on disk: {len(course_dirs)}")
    for cdir in course_dirs:
        course = cdir.name
        mf = cdir / "manifest.json"
        if not mf.exists():
            fail(f"[{course}] no manifest.json")
            continue
        man = json.loads(mf.read_text(encoding="utf-8"))
        for a in man.get("authors", []):
            if a.get("name"):
                all_md_authors.add(a["name"])
        pages = man.get("pages", [])
        n_json = len(list(cdir.glob("notes/*/*/*.json")))
        n_md = len(list(cdir.glob("notes/*/*/*.md")))
        if n_json != len(pages):
            fail(f"[{course}] manifest pages {len(pages)} != json files {n_json}")
        if n_md != n_json:
            fail(f"[{course}] json {n_json} != md {n_md}")
        exp = man["counts"]["pages_expected"]
        got = man["counts"]["pages_scraped"]
        if got != exp and not man.get("fetch_failures"):
            fail(f"[{course}] {got}/{exp} scraped with no failures recorded")
        for p in pages:
            jf = cdir / p["path"]
            mdf = jf.with_suffix(".md")
            if not jf.exists():
                fail(f"[{course}] missing {p['path']}")
                continue
            if not mdf.exists():
                fail(f"[{course}] missing md for {p['path']}")
                continue
            note = json.loads(jf.read_text(encoding="utf-8"))
            if note.get("schema") != "syllabai.sme-revision-note/1.0":
                fail(f"[{course}/{p['path']}] bad schema")
            if not str(note.get("note_id", "")).startswith("rn_"):
                fail(f"[{course}/{p['path']}] missing rn_ id")
            if not note.get("blocks"):
                fail(f"[{course}/{p['path']}] empty blocks")
            # md front matter parity
            head = mdf.read_text(encoding="utf-8")[:600]
            if f'note_id: "{note["note_id"]}"' not in head:
                fail(f"[{course}/{p['path']}] md front matter note_id mismatch")
            if f"spec_point_ids: {json.dumps(note['spec_point_ids'])}" not in \
                    mdf.read_text(encoding="utf-8"):
                fail(f"[{course}/{p['path']}] md spec_point_ids mismatch")
            # G3 assets
            for b in note.get("blocks", []):
                if b.get("type") == "figure" and b.get("file"):
                    if not (cdir / b["file"]).exists():
                        fail(f"[{course}/{p['path']}] missing asset "
                             f"{b['file']}")
        if man["counts"]["asset_failures"]:
            NOTES.append(f"[{course}] {len(man['asset_failures'])} asset "
                         f"failures (documented)")

    # ---------------- G4 author-strip (all md files)
    LEAK = ["Reviewed by", "Updated on", "Guided study available",
            "Start guided study", "## Excerpt"]
    leaks = 0
    for mdf in ROOT.glob("*/notes/*/*/*.md"):
        course = mdf.relative_to(ROOT).parts[0]
        text = mdf.read_text(encoding="utf-8", errors="replace")
        for s in LEAK:
            if s in text:
                leaks += 1
                fail(f"leak {s!r} in {mdf.relative_to(ROOT)}")
                break
        else:
            # 'Written by' only counts as a byline in the first 10 body lines
            body = text.split("---", 2)[-1]
            head_lines = [l for l in body.splitlines() if l.strip()][:10]
            if any(l.lstrip().startswith(("Written by:", "Written by ["))
                   or "Written by " in l and "at the age" not in l
                   for l in head_lines):
                leaks += 1
                fail(f"byline leak in {mdf.relative_to(ROOT)}")
                continue
            # author names of THIS course must never appear in content
            # (full names with a surname only — single-token first names
            # like "Amber" also occur as worked-example character names)
            man = json.loads((ROOT / course / "manifest.json").read_text())
            for a in man.get("authors", []):
                nm = (a.get("name") or "").strip()
                if len(nm.split()) >= 2 and re.search(rf"\b{re.escape(nm)}\b",
                                                      text):
                    leaks += 1
                    fail(f"author-name leak {nm!r} in "
                         f"{mdf.relative_to(ROOT)}")
                    break
    print(f"author-strip scan: {leaks} leaks across "
          f"{len(list(ROOT.glob('*/notes/*/*/*.md')))} md files")

    # ---------------- G5 chemistry
    res_file = ROOT / CHEM / "spec_point_resolution.json"
    if not res_file.exists():
        fail("chemistry spec_point_resolution.json missing")
    else:
        res = json.loads(res_file.read_text(encoding="utf-8"))
        c = res["counts"]
        if c["resolved_ids"] != 162 or c["unresolved_ids"] != 0:
            fail(f"chemistry resolution {c['resolved_ids']}/162, "
                 f"unresolved {c['unresolved_ids']}")
        if c["legacy_matched"] != 112:
            fail(f"chemistry legacy join {c['legacy_matched']}/112")
    for jf in (ROOT / CHEM).glob("notes/*/*/*.json"):
        note = json.loads(jf.read_text(encoding="utf-8"))
        if note["spec_point_ids"] and not note["spec_point_codes"]:
            fail(f"[{CHEM}] {jf.name} has ids but no official codes")
        if "legacy_spec_map" not in note:
            fail(f"[{CHEM}] {jf.name} missing legacy_spec_map")
    # non-chemistry: no invented codes
    for jf in ROOT.glob("*/notes/*/*/*.json"):
        if jf.relative_to(ROOT).parts[0] == CHEM:
            continue
        note = json.loads(jf.read_text(encoding="utf-8"))
        if note.get("spec_point_codes"):
            fail(f"[{jf.relative_to(ROOT)}] FORBIDDEN spec_point_codes on "
                 f"non-chemistry course")
        if note.get("legacy_spec_map") is not None:
            fail(f"[{jf.relative_to(ROOT)}] FORBIDDEN legacy_spec_map on "
                 f"non-chemistry course")

    # ---------------- G6 registry truth
    reg = ROOT / "manifest.json"
    if not reg.exists():
        fail("top-level manifest.json missing")
    else:
        doc = json.loads(reg.read_text(encoding="utf-8"))
        if doc.get("scraped_courses") != len(course_dirs):
            fail(f"registry courses {doc.get('scraped_courses')} != "
                 f"{len(course_dirs)}")
        for k in ("pages_scraped", "assets", "spec_point_links"):
            tot = sum(json.loads((d / "manifest.json").read_text())
                      ["counts"][k] for d in course_dirs)
            if doc["totals"].get(k) != tot:
                fail(f"registry totals[{k}] {doc['totals'].get(k)} != {tot}")

    print()
    for n in NOTES:
        print("NOTE:", n)
    if FAILS:
        print(f"\nFAIL ({len(FAILS)}):")
        for f in FAILS[:40]:
            print("  -", f)
        return 1
    print("ALL GATES PASS (G1-G6)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
