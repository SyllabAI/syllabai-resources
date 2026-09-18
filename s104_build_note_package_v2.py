#!/usr/bin/env python3
"""s104 — build the SME RevisionNotes corpus package (v2 source, same v1.0
backend format as c13_build_note_package.py).

Source: SME-RevisionNotes/igcse-chemistry-19 (structured re-scrape:
.md body + .json metadata per note, course assets/).

Differences from the v1 builder (all documented in ADR-026):
  * noteId  = the SME rn_* id (real corpus identity, stable across re-scrapes)
  * spec_map = UNION of the human-validated c10 legacy map (HUMAN_VALIDATED,
    operator 2026-09-11) and the SME resolution codes (AI_VALIDATED,
    operator-delegated 2026-09-17); per-code provenance preserved, the
    human-validated provenance wins when both apply (verified: the two
    sources agree 161/162 at code level)
  * tree     = SME sections (4) -> SME topics (28) -> notes (112), orders
    derived from slug segments

Output format: revision-notes package 1.0 (RevisionNoteIngestService):
  package.json {topics[{order,title,subtopics[{order,title,notes[...]}]}],
               assets[]} + assets/<file>
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml

SRC = Path("/home/z/my-project/work/sme-sparse/SME-RevisionNotes/igcse-chemistry-19")
OUT = Path("/home/z/my-project/work/sme-igcse-corpus/dist/sme-revision-notes-package.zip")
PACKAGE_VERSION = "1.0"

IMG = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
SLUG = re.compile(r"^(\d+)-(\d+)-(\d+)-")
SPEC_CODE = re.compile(r"4CH1-\d+(?:\.\d+)?[A-Za-z]?")
SECTION_DIR = re.compile(r"^(\d)-")


def normalize_asset_name(name: str, taken: set[str]) -> str:
    stem, dot, ext = name.rpartition(".")
    if not dot:
        stem, ext = name, ""
    clean = unicodedata.normalize("NFKD", stem)
    clean = re.sub(r"[^A-Za-z0-9 ().-]", "-", clean).strip("- .") or "asset"
    candidate = f"{clean}.{ext}" if ext else clean
    base, n = candidate, 2
    while candidate in taken:
        candidate = f"{base}-{n}"
        n += 1
    taken.add(candidate)
    return candidate


def build():
    notes_root = SRC / "notes"
    referenced: dict[str, str] = {}       # original basename -> packaged name
    taken_names: set[str] = set()
    topics: dict[int, dict] = {}
    stats = {"notes": 0, "hv_codes": 0, "ai_only_codes": 0, "pruned_refs": 0}

    for md_path in sorted(notes_root.glob("*/*/*.md")):
        raw = md_path.read_text(encoding="utf-8", errors="replace")
        fm = {}
        if raw.startswith("---"):
            head = raw.split("\n---", 1)[0][3:]
            try:
                fm = yaml.safe_load(head) or {}
            except yaml.YAMLError:
                fm = {}
        body = raw.split("\n---", 1)[1].lstrip("-\n").strip() if "\n---" in raw else raw
        meta = json.loads(md_path.with_suffix(".json").read_text())

        slug = md_path.stem
        m = SLUG.match(slug)
        if not m:
            print(f"skipping non-slug note {md_path}", file=sys.stderr)
            continue
        t_order, s_order, n_order = int(m.group(1)), int(m.group(2)), int(m.group(3))

        # ---- union spec map ----
        legacy = (meta.get("legacy_spec_map") or {})
        legacy_points = legacy.get("spec_points") or []
        legacy_codes = {e["code"]: e for e in legacy_points
                        if isinstance(e, dict) and e.get("code")}
        new_codes = list(dict.fromkeys(meta.get("spec_point_codes") or []))
        union: dict[str, dict] = {}
        for code, entry in legacy_codes.items():
            if SPEC_CODE.fullmatch(code):
                union[code] = entry          # HUMAN_VALIDATED provenance wins
                stats["hv_codes"] += 1
        for code in new_codes:
            if code not in union and SPEC_CODE.fullmatch(code):
                union[code] = {"code": code, "provenance": {
                    "tier": "AI_SUGGESTED",
                    "model_version": "sme-definition-resolution",
                    "validation_status": "AI_VALIDATED",
                    "validated_by": "operator-delegation-2026-09-17",
                }}
                stats["ai_only_codes"] += 1
        spec_map = {
            "curriculum_code": legacy.get("curriculum_code", "4CH1-2017"),
            "phase": legacy.get("phase", 2),
            "subsection": legacy.get("subsection"),
            "spec_points": [union[c] for c in sorted(union)],
            "mapped_date": legacy.get("mapped_date"),
            "mapper": "s104 union policy (c10 HUMAN_VALIDATED ∪ SME resolution AI_VALIDATED)",
        }

        # ---- body asset rewrite ----
        used: list[str] = []
        def sub(match: re.Match) -> str:
            alt, url = match.group(1), match.group(2)
            if url.startswith(("http://", "https://", "data:")):
                return match.group(0)
            orig = Path(url).name
            if not (SRC / "assets" / orig).is_file():
                stats["pruned_refs"] += 1
                return ""
            if orig in referenced:
                filename = referenced[orig]
            else:
                filename = normalize_asset_name(orig, taken_names)
                referenced[orig] = filename
            if filename not in used:
                used.append(filename)
            return f"![{alt}](assets/{filename})"
        body_md = IMG.sub(sub, body)

        note = {
            "noteId": meta.get("note_id") or slug[:256],
            "title": meta.get("title") or fm.get("title") or slug,
            "order": n_order,
            "bodyMd": body_md,
            "specMapJson": json.dumps(spec_map, ensure_ascii=False),
            "specPointCodes": ",".join(sorted(union)),
            "sourceUrl": meta.get("url"),
            "assets": used,
        }
        titles = meta.get("titles") or {}
        topic = topics.setdefault(t_order, {
            "order": t_order,
            "title": titles.get("section") or f"Section {t_order}",
            "subtopics": {}})
        sub = topic["subtopics"].setdefault(s_order, {
            "order": s_order,
            "title": titles.get("topic") or f"Topic {s_order}",
            "notes": []})
        sub["notes"].append(note)
        stats["notes"] += 1

    package = {
        "packageVersion": PACKAGE_VERSION,
        "corpusVersion": "sme-revision-notes-igcse-chemistry-19-2026-09-18",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "topics": [],
        "assets": [],
    }
    for t_order in sorted(topics):
        topic = topics[t_order]
        package["topics"].append({
            "order": topic["order"], "title": topic["title"],
            "subtopics": [topic["subtopics"][s] for s in sorted(topic["subtopics"])],
        })
    asset_sources = {norm: SRC / "assets" / orig for orig, norm in referenced.items()}
    shipped = sorted({n for t in package["topics"] for s in t["subtopics"]
                      for n in s["notes"] for n in n["assets"]})
    package["assets"] = [{"filename": n, "contentType": "image/png"} for n in shipped]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("package.json", json.dumps(package, ensure_ascii=False, indent=1))
        for a in package["assets"]:
            zf.write(asset_sources[a["filename"]], f"assets/{a['filename']}")

    print(json.dumps(stats, indent=1))
    print(f"package: {OUT} ({OUT.stat().st_size/1e6:.1f} MB)")
    print(f"topics={len(package['topics'])} subtopics="
          f"{sum(len(t['subtopics']) for t in package['topics'])} "
          f"assets={len(package['assets'])}")
    return package


if __name__ == "__main__":
    build()
