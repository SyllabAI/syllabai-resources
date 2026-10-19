#!/usr/bin/env python3
"""c13 — build the revision-notes corpus package for the SyllabAI backend.

Reads the `Chemistry IGCSE Revision Notes` tree (one .md per note with
c10 spec_map front-matter + relative `../../assets/...` image refs) and
emits a versioned ZIP package:

    package.json   — tree (topics -> subtopics -> notes) + note bodies +
                     spec maps + asset manifests
    assets/<file>  — every referenced diagram image

The backend (syllabai-core RevisionNoteIngestService, package_version 1.0)
ingests this ZIP replace-all; note bodies keep image refs rewritten to the
flattened `assets/<filename>` form. Ordering reproduces the canonical
Save-My-Exams sequence from each note's source-URL slug
(`2-8-1-tests-for-gases` -> topic 2, subtopic 8, note 1) with a
directory-letter fallback.

Usage:
    python3 scripts/c13_build_note_package.py [--out dist/revision-notes-package.zip]

Operator flow after generation (admin JWT required):
    curl -X POST "$BASE/api/v1/admin/revision-notes/ingest" \
         -H "Authorization: Bearer $ADMIN_JWT" \
         -F "file=@dist/revision-notes-package.zip"
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import yaml  # same dependency the c09/c10 corpus tooling already uses

REPO_ROOT = Path(__file__).resolve().parent.parent
NOTES_ROOT = REPO_ROOT / "Chemistry IGCSE Revision Notes"
PACKAGE_VERSION = "1.0"

# refs whose file is absent from assets/ are pruned from the body (the backend
# rejects dangling references fail-closed); reported at the end of the run.
PRUNED_REFS: list[str] = []

IMG_REF = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
SLUG_TAIL = re.compile(r"^(\d+)-(\d+)-(\d+)-")
DIR_TOPIC = re.compile(r"^(\d+)\.")
DIR_LETTER = re.compile(r"^([a-z]+)\.")
SPEC_CODE = re.compile(r"4CH1-\d+(?:\.\d+)?[A-Za-z]?")


def frontmatter(text: str) -> dict:
    """Parse the leading YAML front-matter block with the corpus tooling's
    yaml dependency (c10 wrote these blocks with ruamel/pyyaml shapes)."""
    if not text.startswith("---"):
        return {}
    head = text.split("\n---", 1)[0][3:]
    try:
        parsed = yaml.safe_load(head)
    except yaml.YAMLError:
        return {}
    return parsed if isinstance(parsed, dict) else {}


def normalize_asset_name(name: str, taken: set[str]) -> str:
    """ASCII-safe asset filename: the backend rejects anything outside
    [A-Za-z0-9 .()-] (fail-closed containment), so fold exotic characters
    (en-dashes, ~, _) to '-' and guarantee uniqueness."""
    stem, dot, ext = name.rpartition(".")
    if not dot:
        stem, ext = name, ""
    clean = unicodedata.normalize("NFKD", stem)
    clean = re.sub(r"[^A-Za-z0-9 ().-]", "-", clean).strip("- .") or "asset"
    candidate = f"{clean}.{ext}" if ext else clean
    base = candidate
    n = 2
    while candidate in taken:
        candidate = f"{base}-{n}"
        n += 1
    taken.add(candidate)
    return candidate


def list_of(value) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def spec_codes(fm: dict) -> list[str]:
    codes: list[str] = []
    spec_map = fm.get("spec_map") or {}
    for point in list_of(spec_map.get("spec_points")):
        if isinstance(point, dict):
            code = str(point.get("code", "")).strip()
            if SPEC_CODE.fullmatch(code):
                codes.append(code)
    seen: set[str] = set()
    return [c for c in codes if not (c in seen or seen.add(c))]


def asset_filename(url: str, referenced: dict[str, str], taken: set[str]) -> str:
    """Flatten a relative asset ref to a normalized unique basename."""
    if url in referenced:
        return referenced[url]
    name = normalize_asset_name(Path(url).name, taken)
    referenced[url] = name
    return name


def rewrite_body(text: str, referenced: dict[str, str], taken: set[str]) -> tuple[str, list[str]]:
    """Rewrite relative image refs to `assets/<filename>`; drop refs whose
    file is missing on disk (uncaptured diagrams, empty placeholder refs)."""
    used: list[str] = []

    def sub(match: re.Match) -> str:
        alt, url = match.group(1), match.group(2)
        if url.startswith(("http://", "https://", "data:")):
            return match.group(0)
        # existence check against the ORIGINAL disk name, then normalize
        if not (NOTES_ROOT / "assets" / Path(url).name).is_file():
            if url not in PRUNED_REFS:
                PRUNED_REFS.append(url)
            return ""
        filename = asset_filename(url, referenced, taken)
        if filename not in used:
            used.append(filename)
        return f"![{alt}](assets/{filename})"

    return IMG_REF.sub(sub, text), used


def topic_order_of(dir_name: str) -> int:
    match = DIR_TOPIC.match(dir_name)
    if not match:
        raise SystemExit(f"cannot derive topic order from {dir_name!r}")
    return int(match.group(1))


def slug_of(source: str) -> str:
    """SME canonical slug = the last path segment of the source URL
    (e.g. '2-8-1-tests-for-gases'); '' when the URL is not SME-shaped."""
    if "/revision-notes/" not in source:
        return ""
    tail = source.rstrip("/").rsplit("/", 1)[-1]
    return tail if SLUG_TAIL.match(tail) else ""


def build() -> dict:
    if not NOTES_ROOT.is_dir():
        raise SystemExit(f"notes tree not found: {NOTES_ROOT}")

    referenced: dict[str, str] = {}
    taken_names: set[str] = set()
    taken_ids: set[str] = set()
    topics: dict[int, dict] = {}

    for topic_dir in sorted(p for p in NOTES_ROOT.iterdir() if p.is_dir()):
        if not DIR_TOPIC.match(topic_dir.name):
            continue  # assets/ and other non-topic dirs
        topic_order = topic_order_of(topic_dir.name)
        topic = topics.setdefault(
            topic_order,
            {"order": topic_order, "title": topic_dir.name, "subtopics": {}},
        )
        for sub_dir in sorted(p for p in topic_dir.iterdir() if p.is_dir()):
            for note_path in sorted(sub_dir.glob("*.md")):
                raw = note_path.read_text(encoding="utf-8", errors="replace")
                fm = frontmatter(raw)
                body = raw.split("\n---", 1)[1].lstrip("-\n").strip() if "\n---" in raw else raw

                # canonical ordering: SME source-URL slug first, dir letters fallback
                source = str(fm.get("source") or "")
                slug = slug_of(source)
                if slug:
                    t_order, s_order, n_order = (
                        int(SLUG_TAIL.match(slug).group(1)),
                        int(SLUG_TAIL.match(slug).group(2)),
                        int(SLUG_TAIL.match(slug).group(3)),
                    )
                else:
                    sub_letter = DIR_LETTER.match(sub_dir.name)
                    s_order = (ord(sub_letter.group(1)) - ord("a") + 1) if sub_letter else 99
                    n_order = len(topic["subtopics"].get(sub_dir.name, {}).get("notes", [])) + 1
                    t_order = topic_order

                note_id = re.sub(r"[^A-Za-z0-9._-]", "-", slug or note_path.stem)[:256]
                while note_id in taken_ids:
                    note_id = f"{note_id}-x"
                taken_ids.add(note_id)

                body_md, assets = rewrite_body(body, referenced, taken_names)
                note = {
                    "noteId": note_id,
                    "title": note_path.stem.replace(" - IGCSE Chemistry Revision Notes", "")
                    .replace("  Edexcel IGCSE Chemistry Revision Notes 2017", " ")
                    .strip(),
                    "order": n_order,
                    "bodyMd": body_md,
                    "specMapJson": json.dumps(fm.get("spec_map") or {}, ensure_ascii=False),
                    "specPointCodes": ",".join(spec_codes(fm)),
                    "sourceUrl": source or None,
                    "assets": assets,
                }
                sub = topic["subtopics"].setdefault(
                    sub_dir.name,
                    {"order": s_order, "title": sub_dir.name, "notes": []},
                )
                sub["notes"].append(note)

    package = {
        "packageVersion": PACKAGE_VERSION,
        "corpusVersion": f"4ch1-notes-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}",
        "generatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "topics": [],
        "assets": [],
    }
    # normalized packaged name -> original file on disk (names may differ after
    # ASCII-normalization); only files referenced by at least one note ship.
    asset_sources: dict[str, Path] = {
        norm: NOTES_ROOT / "assets" / Path(orig).name
        for orig, norm in referenced.items()
    }
    for topic_order in sorted(topics):
        topic = topics[topic_order]
        subtopics = []
        for sub_name in sorted(topic["subtopics"]):
            sub = topic["subtopics"][sub_name]
            sub["notes"].sort(key=lambda n: n["order"])
            subtopics.append({
                "order": sub["order"],
                "title": sub["title"],
                "notes": sub["notes"],
            })
        package["topics"].append({
            "order": topic["order"],
            "title": topic["title"],
            "subtopics": subtopics,
        })
    shipped = {
        name for t in package["topics"] for s in t["subtopics"]
        for n in s["notes"] for name in n["assets"]
        if asset_sources.get(name, Path()).is_file()
    }
    package["assets"] = [
        {"filename": name, "contentType": "image/png"}
        for name in sorted(shipped)
    ]
    return package, asset_sources


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out", default="dist/revision-notes-package.zip", help="output ZIP path")
    args = parser.parse_args()

    package, asset_sources = build()
    out_path = REPO_ROOT / args.out
    out_path.parent.mkdir(parents=True, exist_ok=True)

    notes = sum(len(s["notes"]) for t in package["topics"] for s in t["subtopics"])
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("package.json", json.dumps(package, ensure_ascii=False, indent=1))
        for asset in package["assets"]:
            zf.write(asset_sources[asset["filename"]], f"assets/{asset['filename']}")

    size_mb = out_path.stat().st_size / 1_048_576
    print(f"package: {out_path} ({size_mb:.1f} MB)")
    print(f"topics={len(package['topics'])} notes={notes} assets={len(package['assets'])}")
    print(f"corpus_version={package['corpusVersion']}")
    if PRUNED_REFS:
        print(f"pruned {len(PRUNED_REFS)} broken image ref(s) not present in assets/:")
        for url in PRUNED_REFS:
            print(f"  - {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
