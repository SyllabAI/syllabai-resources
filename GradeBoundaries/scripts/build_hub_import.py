#!/usr/bin/env python3
"""Build hub-import/grade-boundaries-1.0/bundle.json — the hub serving bundle.

Joins mapping/course-map.yaml to parsed/<family>/<Session>.json and emits one
namespace-complete bundle the v2 hub mechanically imports to
apps/hub/content/grade-boundaries/bundle.v1.json. Only sessions whose source
PDF has a recorded sha256 may enter the bundle (provenance law); any map
entry whose family parsed nothing is emitted with an empty series list —
an honest absence the hub renders as the roadmap state, never a stub.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

from gb_common import HUB_IMPORT, LANE, MAPPING, PARSED, fail, now_utc

BUNDLE = HUB_IMPORT / "bundle.json"


def sha16(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def read_map() -> list[dict]:
    """Minimal YAML read — the map is machine-generated with a fixed shape."""
    text = (MAPPING / "course-map.yaml").read_text()
    courses: list[dict] = []
    cur: dict | None = None
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("- slug:"):
            cur = {"slug": s.split(":", 1)[1].strip()}
            courses.append(cur)
        elif cur is not None and ":" in s and not s.startswith("#"):
            k, v = s.split(":", 1)
            cur[k.strip()] = v.strip().strip('"')
    return courses


def load_family(family: str) -> dict[str, dict]:
    """session -> parsed doc for a family"""
    out: dict[str, dict] = {}
    d = PARSED / family
    if not d.exists():
        return out
    for p in sorted(d.glob("*.json")):
        out[p.stem] = json.loads(p.read_text())
    return out


def linear_course_entry(row: dict, docs: dict[str, dict]) -> dict | None:
    code = row["code"]
    # tiered subjects (Maths A Foundation/Higher): the hub slug selects the
    # tier — a "-foundation"/"-higher" slug only ever serves its own rows
    tier = ("foundation" if row["slug"].endswith("-foundation")
            else "higher" if row["slug"].endswith("-higher") else None)
    series = []
    review = False
    for session, doc in docs.items():
        rows = [s for s in doc["subjects"]
                if s.get("code") == code and s.get("overall")
                and s.get("tier") == tier]
        if not rows:
            continue
        for subj in rows:
            if subj.get("reviewRequired") or doc.get("parse_warnings"):
                review = True
            series.append({
                "session": session,
                "year": int(session.split()[-1]),
                "scale": subj["overall"]["scale"],
                "maxMark": subj["overall"]["maxMark"],
                "boundaries": subj["overall"]["boundaries"],
                "gradeLadder": subj["gradeLadder"],
                "papersNote": subj.get("papersNote"),
                "tier": subj.get("tier"),
                "source": {"family": doc["family"],
                           "sha256_16": (doc["source"].get("sha256")
                                         or "")[:16]},
            })
    if not series:
        return None
    series.sort(key=lambda s: (s["year"], s["session"]))
    ladder = series[-1]["gradeLadder"]
    return {
        "code": code,
        "board": row.get("board", "Edexcel"),
        "level": row.get("level"),
        "title": row.get("subject"),
        "gradeLadder": ladder,
        "tier": tier,
        "calculator": {"mode": "linear-total",
                       "maxMark": series[-1]["maxMark"]},
        "reviewRequired": review,
        "series": series,
    }


def modular_ial_course_entry(row: dict, docs: dict[str, dict],
                             family: str) -> dict | None:
    code = row["code"]
    unit_stem = None
    cashin = row.get("ialCashIn") or code
    series = []
    review = False
    if family == "pearson-ial":
        # unit codes W<XX><n>.. join via subject stem, cash-in by exact code
        m = re.match(r"^Y([A-Z]{2,4}\d+)$", code)
        unit_stem = m.group(1) if m else None
    for session, doc in docs.items():
        subj = None
        if family == "pearson-int-gcse-modular":
            subj = next((s for s in doc["subjects"]
                         if any(u.get("code", "").startswith(code)
                                for u in s.get("units", []))
                         or any(c.get("code") == code
                                for c in s.get("cashIns", []))), None)
        else:
            subj = next((s for s in doc["subjects"]
                         if any(c.get("code") == code
                                for c in s.get("cashIns", []))), None)
        if not subj:
            continue
        entry: dict = {
            "session": session,
            "year": int(session.split()[-1]),
            "gradeLadder": subj.get("gradeLadder"),
            "source": {"family": doc["family"],
                       "sha256_16": (doc["source"].get("sha256") or "")[:16]},
        }
        if family == "pearson-int-gcse-modular":
            # suite join: units 4W<key><n> belong to the cash-in 4X<key><n>
            # (4WCH1/4WCH2 -> 4XCH1); a "-unit-N" hub slug keeps only that
            # unit's rows
            unit_no = None
            m_un = re.search(r"-unit-(\d)$", row["slug"])
            if m_un:
                unit_no = m_un.group(1)
            suite = code[2:-1] if len(code) >= 4 else code
            units = [u for u in subj.get("units", [])
                     if u.get("code", "").startswith("4W")
                     and u["code"][2:-1] == suite
                     and (unit_no is None or u["code"][-1] == unit_no)]
            cashins = [c for c in subj.get("cashIns", [])
                       if c.get("code") == code]
        else:
            units = [u for u in subj.get("units", [])
                     if unit_stem and re.match(
                         rf"^[WX]{unit_stem[:2]}\d", u.get("code", ""))
                     and u.get("code", "").endswith(tuple("0123456789"))
                     and unit_stem[:2] in u.get("code", "")]
            cashins = [c for c in subj.get("cashIns", [])
                       if c.get("code") == code]
        entry["units"] = [
            {"code": u["code"], "title": u["title"], "maxMark": u["maxMark"],
             "boundaries": u["boundaries"],
             "ums": u.get("ums")}
            for u in units if u.get("boundaries")]
        entry["cashIns"] = [
            {"code": c["code"], "title": c["title"], "maxMark": c["maxMark"],
             "boundaries": c["boundaries"]}
            for c in cashins if c.get("boundaries")]
        if not entry["units"] and not entry["cashIns"]:
            continue
        if subj.get("reviewRequired") or doc.get("parse_warnings"):
            review = True
        series.append(entry)
    if not series:
        return None
    series.sort(key=lambda s: (s["year"], s["session"]))
    return {
        "code": code,
        "board": row.get("board", "Edexcel"),
        "level": row.get("level"),
        "title": row.get("subject"),
        "gradeLadder": series[-1].get("gradeLadder"),
        "calculator": {"mode": "display-only", "maxMark": None},
        "reviewRequired": review,
        "series": series,
    }


def cie_course_entry(row: dict) -> dict | None:
    code = row.get("cieSyllabus")
    d = PARSED / "cie" / str(code)
    if not d.exists():
        return None
    series = []
    review = False
    for p in sorted(d.glob("*.json")):
        doc = json.loads(p.read_text())
        if not doc.get("routes") and not doc.get("components"):
            continue
        if doc.get("parse_warnings"):
            review = True
        series.append({
            "session": doc["session"],
            "year": int(doc["session"].split()[-1]),
            "gradeLadder": doc.get("gradeLadder"),
            "components": [
                {"code": c["code"], "maxMark": c["maxMark"],
                 "boundaries": c["boundaries"]}
                for c in doc.get("components", []) if c.get("boundaries")],
            "routes": [
                {"combination": r["combination"],
                 "maxWeightedMark": r["maxWeightedMark"],
                 "boundaries": r["boundaries"]}
                for r in doc.get("routes", []) if r.get("boundaries")],
            "source": {"family": doc["family"],
                       "sha256_16": (doc["source"].get("sha256") or "")[:16]},
        })
    if not series:
        return None
    series.sort(key=lambda s: (s["year"], s["session"]))
    return {
        "code": str(code),
        "board": row.get("board", "Cambridge International"),
        "level": row.get("level"),
        "title": row.get("subject"),
        "gradeLadder": series[-1].get("gradeLadder"),
        "calculator": {"mode": "display-only", "maxMark": None},
        "reviewRequired": review,
        "series": series,
    }


def main() -> None:
    courses = read_map()
    docs = {fam: load_family(fam) for fam in (
        "pearson-int-gcse-linear", "pearson-int-gcse-modular", "pearson-ial")}
    out_courses: dict[str, dict] = {}
    served = roadmap = 0
    for row in courses:
        fam = row["family"]
        entry = None
        if fam == "pearson-int-gcse-linear":
            entry = linear_course_entry(row, docs[fam])
        elif fam in ("pearson-int-gcse-modular", "pearson-ial"):
            entry = modular_ial_course_entry(row, docs[fam], fam)
        elif fam == "cie":
            entry = cie_course_entry(row)
        if entry:
            out_courses[row["slug"]] = entry
            served += 1
        else:
            out_courses[row["slug"]] = {
                "code": row["code"], "board": row.get("board", "Edexcel"),
                "level": row.get("level"), "title": row.get("subject"),
                "gradeLadder": None, "calculator": None,
                "reviewRequired": False, "series": [],
            }
            roadmap += 1

    manifest_rows = []
    man = LANE / "raw" / "MANIFEST.jsonl"
    if man.exists():
        manifest_rows = [json.loads(ln) for ln in
                         man.read_text().splitlines() if ln.strip()]
    bundle = {
        "schema": "syllabai.grade-boundaries/1.0",
        "generated": now_utc(),
        "generator": "GradeBoundaries/scripts/build_hub_import.py v1",
        "source": {
            "lane": "SyllabAI/syllabai-resources GradeBoundaries",
            "documents": len(manifest_rows),
            "manifest_sha16": sha16(man.read_text()) if man.exists() else None,
        },
        "counts": {"courses_served": served, "courses_roadmap": roadmap,
                   "courses_total": len(out_courses)},
        "courses": dict(sorted(out_courses.items())),
    }
    HUB_IMPORT.mkdir(parents=True, exist_ok=True)
    BUNDLE.write_text(json.dumps(bundle, indent=1, ensure_ascii=False) + "\n")
    size = BUNDLE.stat().st_size
    print(f"BUNDLE: {BUNDLE} ({size} bytes) — {served} served, "
          f"{roadmap} roadmap, {len(out_courses)} total")
    sys.exit(0 if served > 0 else 2)


if __name__ == "__main__":
    main()
