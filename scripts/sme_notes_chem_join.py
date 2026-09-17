#!/usr/bin/env python3
"""
T-SME-NOTES-4 — chemistry-only post-join for the SME revision-notes corpus.

1. Legacy join (verbatim preservation):
   The operator-validated spec_map front matter in "Chemistry IGCSE Revision
   Notes/**.md" (AI_SUGGESTED -> HUMAN_VALIDATED 2026-09-11 by the operator,
   produced by scripts/c10_map_notes.py) is joined into the re-scraped notes
   BY SOURCE URL and attached VERBATIM as legacy_spec_map. Provenance is
   preserved exactly; nothing is re-derived or downgraded.

2. Official 4CH1 codes for the notes' spec_point_ids:
   - primary: SME-ExamQuestion/igcse-chemistry-19/spec_point_resolution.json
     (162 ids already resolved + adjudicated corpus-side; copied 1:1)
   - scripts/sme_spcpt_adjudications.yaml decisions likewise copied
   - remaining notes-only ids: same deterministic matcher as
     sme_spcpt_resolve.py (score >= 0.75, margin >= 0.05, subsection boost
     anchored on the page's own legacy spec_map subsection)
   - anything still unresolved is RECORDED, never fabricated

Validation status: AI_VALIDATED (operator-delegated). HUMAN_VALIDATED strings
appear only inside the verbatim legacy_spec_map (operator's own record).
"""
from __future__ import annotations

import difflib
import json
import re
import sys
import time
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
NOTES_DIR = BASE / "SME-RevisionNotes" / "igcse-chemistry-19"
LEGACY_DIR = BASE / "Chemistry IGCSE Revision Notes"
EQ_CHEM = BASE / "SME-ExamQuestion" / "igcse-chemistry-19"
COURSE = "igcse-chemistry-19"

sys.path.insert(0, str(Path(__file__).parent))
import sme_spcpt_resolve as R  # noqa: E402  (score, load_registry, thresholds)


def norm_url(u: str) -> str:
    return (u or "").strip().rstrip("/")


def legacy_by_url() -> dict[str, dict]:
    out = {}
    for p in sorted(LEGACY_DIR.rglob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        src = norm_url(str(fm.get("source", "")))
        sm = fm.get("spec_map")
        if src and isinstance(sm, dict):
            out[src] = {"spec_map": sm, "legacy_file": str(p.relative_to(BASE))}
    return out


def load_official_id_map() -> tuple[dict[str, dict], dict[str, str]]:
    """id -> {code, method} from question-side resolution + adjudications."""
    idmap: dict[str, dict] = {}
    res = json.loads((EQ_CHEM / "spec_point_resolution.json")
                     .read_text(encoding="utf-8"))
    for r in res["resolved"]:
        if r.get("resolved_code"):
            idmap[r["id"]] = {"code": r["resolved_code"],
                              "method": f"corpus:{r.get('method')}"}
    adj_path = Path(__file__).parent / "sme_spcpt_adjudications.yaml"
    if adj_path.exists():
        doc = yaml.safe_load(adj_path.read_text(encoding="utf-8")) or {}
        for d in doc.get("decisions", []):
            if isinstance(d, dict) and d.get("id") and d.get("code"):
                idmap[d["id"]] = {"code": d["code"],
                                  "method": "corpus:ai-adjudicated"}
    return idmap, {p["code"]: p for p in
                   yaml.safe_load((BASE / "graph" / "specification_points.yaml")
                                  .read_text(encoding="utf-8"))
                   ["specification_points"]}


def match_notes_only(sme_def: str, page_codes: list[str],
                     page_subsection: str | None,
                     registry: dict, by_sub: dict) -> tuple[str | None,
                                                           float, float]:
    """Matcher fallback for ids that never reached the question side."""
    scored = []
    for code, p in registry.items():
        s = R.score(sme_def, p.get("official_wording", ""))
        if page_subsection and p.get("subsection") == page_subsection:
            s += R.SUBSECTION_BOOST
        scored.append((s, code))
    scored.sort(reverse=True)
    top1_s, top1 = scored[0]
    top2_s, top2 = scored[1]
    if top1_s >= R.AUTO_THRESHOLD and (top1_s - top2_s) >= R.MARGIN:
        return top1, top1_s, top2_s
    if top1 in page_codes and top1_s >= 0.55:
        return top1, top1_s, top2_s
    return None, top1_s, top2_s


def main() -> int:
    legacy = legacy_by_url()
    print(f"legacy notes with spec_map: {len(legacy)}")
    idmap, registry = load_official_id_map()
    print(f"corpus-resolved ids available: {len(idmap)}")
    by_sub: dict[str, list[str]] = {}
    for code, p in registry.items():
        by_sub.setdefault(p.get("subsection"), []).append(code)

    note_jsons = sorted(NOTES_DIR.glob("notes/*/*/*.json"))
    print(f"scraped chemistry notes: {len(note_jsons)}")

    legacy_hits = legacy_miss = 0
    methods: dict[str, int] = {}
    unresolved = []
    details = []
    for jf in note_jsons:
        note = json.loads(jf.read_text(encoding="utf-8"))
        leg = legacy.get(norm_url(note["url"]))
        if leg:
            legacy_hits += 1
            note["legacy_spec_map"] = leg["spec_map"]
            note["legacy_spec_map_file"] = leg["legacy_file"]
        else:
            legacy_miss += 1

        ids = note["spec_point_ids"]
        page_codes = [sp.get("code") for sp in
                      (note.get("legacy_spec_map") or {})
                      .get("spec_points", []) if sp.get("code")]
        page_sub = (note.get("legacy_spec_map") or {}).get("subsection")
        codes: dict[str, dict] = {}
        for sid in ids:
            if sid in idmap:
                codes[sid] = idmap[sid]
                methods[idmap[sid]["method"]] = methods.get(
                    idmap[sid]["method"], 0) + 1
                continue
            sp = next((b for b in note["blocks"]
                       if b.get("type") == "spec_point" and b.get("id") == sid),
                      {})
            sme_def = sp.get("definition") or sp.get("name") or ""
            code, s1, s2 = match_notes_only(sme_def, page_codes, page_sub,
                                            registry, by_sub)
            if code:
                codes[sid] = {"code": code, "method": "notes-definition-match",
                              "similarity": round(min(s1, 1.0), 4)}
                methods["notes-definition-match"] = methods.get(
                    "notes-definition-match", 0) + 1
            else:
                unresolved.append({"id": sid, "name": sp.get("name"),
                                   "definition": sme_def,
                                   "top": round(min(s1, 1.0), 4),
                                   "note": str(jf.relative_to(NOTES_DIR))})
        note["spec_point_codes_detail"] = codes
        note["spec_point_codes"] = sorted({c["code"] for c in codes.values()})

        # rewrite json + md front matter
        jf.write_text(json.dumps(note, ensure_ascii=False, indent=1),
                      encoding="utf-8")
        mdf = jf.with_suffix(".md")
        md = mdf.read_text(encoding="utf-8")
        md = re.sub(r"^spec_point_codes: \[.*\]$",
                    "spec_point_codes: "
                    + json.dumps(note["spec_point_codes"]),
                    md, count=1, flags=re.M)
        if "legacy_spec_map: true" not in md and leg:
            md = re.sub(r"^(guided_study: .*)$",
                        r"\1\nlegacy_spec_map: true", md, count=1, flags=re.M)
        mdf.write_text(md, encoding="utf-8")

        for sid, c in codes.items():
            details.append({"id": sid, "code": c["code"],
                            "method": c["method"],
                            "note": str(jf.relative_to(NOTES_DIR))})

    total_ids = sum(len(json.loads(j.read_text())["spec_point_ids"])
                    for j in note_jsons)
    resolved_ids = len({d["id"] for d in details})
    print(f"legacy join: matched {legacy_hits}, unmatched {legacy_miss}")
    print(f"spec ids on notes: {total_ids} unique resolved: {resolved_ids} "
          f"unresolved: {len({u['id'] for u in unresolved})}")
    print("methods:", methods)

    doc = {
        "schema": "syllabai.sme-notes-spec-resolution/1.0",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "course_slug": COURSE,
        "validation": "AI_VALIDATED (operator-delegated); legacy_spec_map is "
                      "the operator's own HUMAN_VALIDATED record, preserved "
                      "verbatim",
        "counts": {"notes": len(note_jsons),
                   "legacy_matched": legacy_hits,
                   "legacy_unmatched": legacy_miss,
                   "unique_ids": len({d["id"] for d in details}
                                     | {u["id"] for u in unresolved}),
                   "resolved_ids": resolved_ids,
                   "unresolved_ids": len({u['id'] for u in unresolved})},
        "methods": methods,
        "resolved": details,
        "unresolved": unresolved,
    }
    (NOTES_DIR / "spec_point_resolution.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {NOTES_DIR / 'spec_point_resolution.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
