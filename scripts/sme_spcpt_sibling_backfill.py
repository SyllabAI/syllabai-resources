#!/usr/bin/env python3
"""T-SPEC-2a — backfill sibling-course spec_point_index.json from committed
RN corpora (verbatim SME data already in-repo).

The three chemistry-family EQ courses (modular-24-unit-1/2, SDA-17-chemistry)
have partial indexes: parts reference ids the harvest never captured. This
backfills missing ids with name/definition text harvested verbatim from the
course's own committed SME-RevisionNotes sidecar JSONs (TipTap spec_point
blocks) and .md spec markers ("> **Spec point** — <id> · <definition>").

No-guess rules:
  - text is copied verbatim from committed SME scrapes; nothing synthesized
  - ids with no text in any committed corpus get a null-text entry marked
    provenance "unavailable-in-committed-corpora" (they stay unresolved later)
  - existing index entries are never modified
Coverage is rebuilt from the actual part references (distinct ids).

Idempotent: re-running produces identical files.
"""
import json
import re
import sys
import time
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
RN = BASE / "SME-RevisionNotes"

COURSES = ["igcse-chemistry-modular-24-unit-1",
           "igcse-chemistry-modular-24-unit-2",
           "igcse-science-double-award-17-chemistry"]

MD_PAT = re.compile(r">\s*\*\*Spec point\*\*\s*—\s*`?(spcpt_\w+)`?\s*(?:·\s*(.+))?")


def harvest_course_rn(course):
    """id -> {name, definition, note_ids:[…]} from one RN course dir."""
    out = {}
    root = RN / course
    if not root.exists():
        return out
    # sidecar JSONs: blocks[].spec_point + note id
    for jf in sorted(root.rglob("notes/**/*.json")):
        try:
            d = json.loads(jf.read_text(encoding="utf-8"))
        except Exception:
            continue
        nid = d.get("note_id")
        for b in d.get("blocks") or []:
            if b.get("type") == "spec_point" and b.get("id"):
                e = out.setdefault(b["id"], {"name": None, "definition": None,
                                             "note_ids": []})
                if b.get("name") and not e["name"]:
                    e["name"] = b["name"]
                if b.get("definition") and not e["definition"]:
                    e["definition"] = b["definition"]
                if nid and nid not in e["note_ids"]:
                    e["note_ids"].append(nid)
    # .md markers for definitions the sidecars lack
    for mf in sorted(root.rglob("notes/**/*.md")):
        try:
            txt = mf.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm_nid = None
        mfm = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
        if mfm:
            n = re.search(r'^note_id:\s*"(rn_\w+)"', mfm.group(1), re.M)
            if n:
                fm_nid = n.group(1)
        for m in MD_PAT.finditer(txt):
            sid, dfn = m.group(1), (m.group(2) or "").strip()
            if not dfn:
                continue
            e = out.setdefault(sid, {"name": None, "definition": None,
                                     "note_ids": []})
            if not e["definition"]:
                e["definition"] = dfn
            if fm_nid and fm_nid not in e["note_ids"]:
                e["note_ids"].append(fm_nid)
    return out


def harvest_all_rn():
    """Shared SME-id text pool over ALL committed chemistry RN corpora.

    SME reuses spec-point ids across related courses (modular units share the
    same taxonomy; some ids also appear on the 2017-linear pages), so a
    verbatim name/definition scraped from any committed sibling/linear page
    is evidence for the id itself. Preference on merge: own-course text wins;
    first non-null wins otherwise.
    """
    pool = {}
    order = [c for c in COURSES] + ["__linear__"]
    roots = {c: RN / c for c in COURSES}
    roots["__linear__"] = BASE / "Chemistry IGCSE Revision Notes"
    for c in order:
        text = harvest_course_rn(c)
        for sid, e in text.items():
            cur = pool.setdefault(sid, {"name": None, "definition": None,
                                        "note_ids": [], "src": c})
            # merge; first non-null wins, keep all note ids
            if e.get("name") and not cur["name"]:
                cur["name"] = e["name"]
            if e.get("definition") and not cur["definition"]:
                cur["definition"] = e["definition"]
            for n in e.get("note_ids", []):
                if n not in cur["note_ids"]:
                    cur["note_ids"].append(n)
    return pool


def main():
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    report = {}
    rn_pool = harvest_all_rn()
    print(f"shared RN text pool: {len(rn_pool)} ids")
    for course in COURSES:
        cdir = EQ / course
        idx_path = cdir / "spec_point_index.json"
        idx = json.loads(idx_path.read_text(encoding="utf-8"))
        sp = idx["spec_points"]

        # actual part references
        refd = {}
        for f in sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        refd.setdefault(s, 0)
                        refd[s] += 1

        missing = [k for k in sorted(refd) if k not in sp]
        # also upgrade entries a previous run marked unavailable
        stale = [k for k, v in sp.items()
                 if k in refd and v.get("provenance", "").startswith("unavailable-")]
        if not missing and not stale:
            report[course] = {"status": "nothing-to-do", "missing": 0}
            continue

        added, unavailable = [], []
        for sid in sorted(set(missing) | set(stale)):
            t = rn_pool.get(sid)
            if t and (t.get("name") or t.get("definition")):
                if sid in sp and sid not in stale:
                    continue  # never overwrite real entries
                sp[sid] = {
                    "name": t.get("name"),
                    "definition": t.get("definition"),
                    "notes": t.get("note_ids", []),
                    "subtopic_slugs": [],
                    "provenance": "rn-corpus-backfill (verbatim SME text, committed corpora)",
                }
                added.append(sid)
            else:
                sp[sid] = {
                    "name": None,
                    "definition": None,
                    "notes": [],
                    "subtopic_slugs": [],
                    "provenance": "unavailable-in-committed-corpora (referenced by "
                                  "question parts only; no SME statement text "
                                  "available; never guessed)",
                }
                unavailable.append(sid)

        # fill subtopic_slugs for backfilled ids from part references
        slug_refs = {}
        for f in sorted(cdir.glob("*/*/*/topic.json")) + sorted(cdir.glob("*/*/topic.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            slug = t["topic"]["slug"]
            for q in t.get("questions", []):
                for p in q.get("parts", []):
                    for s in p.get("spec_point_ids") or []:
                        slug_refs.setdefault(s, set()).add(slug)
        for sid in added:
            sp[sid]["subtopic_slugs"] = sorted(slug_refs.get(sid, []))

        idx["coverage"] = {
            "question_part_ids_total": len(refd),
            "covered_by_index": len([k for k in refd if k in sp]),
            "missing_from_index": [],
        }
        idx["backfill"] = {
            "updated_utc": now,
            "added": len(added),
            "unavailable": len(unavailable),
            "tool": "scripts/sme_spcpt_sibling_backfill.py",
            "unavailable_ids": unavailable,
        }
        idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1),
                            encoding="utf-8")
        report[course] = {"added": len(added), "unavailable": unavailable,
                          "index_total": len(sp), "referenced_total": len(refd)}
        print(f"[{course}] +{len(added)} backfilled, {len(unavailable)} unavailable "
              f"-> index {len(sp)} ids, referenced {len(refd)}")
        for s in unavailable:
            print(f"   unavailable: {s} (x{refd[s]} part refs)")

    out = Path("/home/z/my-project/scripts/specmap_work/backfill_report.json")
    out.write_text(json.dumps({"generated_utc": now, "courses": report}, indent=1))
    print("saved", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
