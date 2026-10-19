#!/usr/bin/env python3
"""
T-C10 (Phase 2) — worksheet generator.

Deterministic, zero-LLM. Produces per-subsection mapping worksheets for the
AI point-level mapping pass:

  1. Walk the 112 SME notes; parse front matter `source:` URLs.
  2. Map each URL's SME topic-group slug (e.g. 1-5-chemical-formulae-…)
     to the 4CH1 subsection registry (4CH1-S1-e) — the PROVIDER-tier anchor.
  3. HARD-verify the 28 SME groups align 1:1 with the 28 spec subsections
     (both count and ordering) before emitting anything.
  4. Emit scripts/c10_worksheets/<SUB>.md: the subsection's spec points
     (full statements) + each note's title, slug tail, excerpt, headings and
     a body excerpt — the raw material for the AI_SUGGESTED mapping pass.
  5. Emit scripts/c10_worksheets/_ALL_POINTS.md (full 182-point registry,
     one line each) for cross-subsection mapping reference.

Nothing here decides point-level mappings: that is the AI pass (recorded in
scripts/c10_decisions/). This script only prepares and gates the inputs.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NOTES_ROOT = REPO / "Chemistry IGCSE Revision Notes"
GRAPH = REPO / "graph"
OUT_DIR = REPO / "scripts" / "c10_worksheets"

SECTION_LETTERS = "abcdefghi"          # subsection letters a..i
EXCERPT_CHARS = 900


# ---------------------------------------------------------------- registry --
def load_registry() -> dict:
    points = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
    topics = yaml.safe_load((GRAPH / "topics.yaml").read_text(encoding="utf-8"))
    subs = {}
    section_of = {t["code"]: t["code"] for t in topics["topics"]}
    for st in topics.get("subtopics", []):
        sec_code = "-".join(st["code"].split("-")[:2])  # 4CH1-S1
        subs[st["code"]] = {
            "title": st.get("title") or st.get("title_md"),
            "ordering": st.get("ordering"),
            "section": section_of.get(sec_code, sec_code),
        }
    by_sub: dict[str, list] = {}
    for p in points["specification_points"]:
        by_sub.setdefault(p["subsection"], []).append(p)
    for lst in by_sub.values():
        lst.sort(key=lambda p: p.get("global_order", 0))
    return {
        "points_by_sub": by_sub,
        "subtopics": subs,
        "all_points": points["specification_points"],
        "meta": points["meta"],
    }


# ------------------------------------------------------------------- notes --
def front_matter_split(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            fm_text = "\n".join(lines[1:i])
            body = "\n".join(lines[i + 1:])
            return yaml.safe_load(fm_text) or {}, body
    return {}, text


def parse_slug(url: str):
    """Return (section_no, group_no, group_slug, note_slug) from an SME URL."""
    parts = [p for p in url.rstrip("/").split("/") if p]
    if len(parts) < 2:
        return None
    group_slug, note_slug = parts[-2], parts[-1]
    m = re.match(r"^(\d)-(\d+)-", group_slug)
    if not m:
        return None
    sec_m = re.match(r"^(\d)-", parts[-3] if len(parts) >= 3 else group_slug)
    section_from_path = int(sec_m.group(1)) if sec_m else None
    return int(m.group(1)), int(m.group(2)), group_slug, note_slug, section_from_path


def note_material(path: Path):
    text = path.read_text(encoding="utf-8")
    fm, body = front_matter_split(text)
    url = fm.get("source") or ""
    lines = body.splitlines()
    title = ""
    headings = []
    for ln in lines:
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif re.match(r"^#{2,4} ", ln):
            h = re.sub(r"[*_`]", "", ln).strip()
            if h and h.lower() != "excerpt":
                headings.append(h)
    # excerpt blockquote
    excerpt = ""
    in_quote = False
    qbuf = []
    for ln in lines:
        if ln.startswith(">"):
            in_quote = True
            qbuf.append(re.sub(r"^>+\s?", "", ln))
        elif in_quote:
            break
    excerpt = " ".join(qbuf).strip()
    excerpt = re.sub(r"[#*`>]", "", excerpt)
    # body excerpt: strip headings/blank lines noise, keep prose order
    prose = []
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith(">"):
            continue
        prose.append(re.sub(r"[*_`]", "", s))
    body_excerpt = " ".join(prose)[:EXCERPT_CHARS]
    return {
        "path": str(path.relative_to(REPO)),
        "title": title or path.stem,
        "url": url,
        "headings": headings,
        "excerpt": " ".join(excerpt.split())[:300],
        "body_excerpt": " ".join(body_excerpt.split()),
        "fm_keys": sorted(fm.keys()),
    }


def walk_notes() -> list[dict]:
    notes = []
    for p in sorted(NOTES_ROOT.rglob("*.md")):
        if "assets" in p.parts:
            continue
        notes.append(note_material(p))
    return notes


# ------------------------------------------------------------------- gates --
def main():
    reg = load_registry()
    notes = walk_notes()
    subtopics = reg["subtopics"]

    # ---- gate 1: every note has a parseable source URL slug
    grouped: dict[str, list[dict]] = {}
    failures = []
    for n in notes:
        parsed = parse_slug(n["url"]) if n["url"] else None
        if not parsed:
            failures.append(f"note without parseable source URL: {n['path']} ({n['url']!r})")
            continue
        sec, grp, group_slug, note_slug, sec_from_path = parsed
        if sec_from_path is not None and sec_from_path != sec:
            failures.append(f"section mismatch in URL: {n['path']}")
        if not (1 <= sec <= 4) or not (1 <= grp <= 9):
            failures.append(f"group number out of range: {n['path']}")
            continue
        letter = SECTION_LETTERS[grp - 1]
        sub_code = f"4CH1-S{sec}-{letter}"
        if sub_code not in subtopics:
            failures.append(f"slug maps to unknown subsection {sub_code}: {n['path']}")
            continue
        n["sub_code"] = sub_code
        n["group_slug"] = group_slug
        n["note_slug"] = note_slug
        grouped.setdefault(sub_code, []).append(n)

    # ---- gate 2: 28 SME groups <-> 28 spec subsections, 1:1
    sme_groups = sorted(
        {(n["sub_code"], n["group_slug"]) for lst in grouped.values() for n in lst}
    )
    if len(grouped) != 28:
        failures.append(f"subsection coverage {len(grouped)} != 28")
    if len(sme_groups) != 28:
        failures.append(f"SME group count {len(sme_groups)} != 28")

    # group ordering must match subtopic ordering (slug 1-5 -> 5th subsection of S1)
    for sub_code, group_slug in sme_groups:
        sec = int(sub_code.split("-")[1][1])
        grp = SECTION_LETTERS.index(sub_code.split("-")[2]) + 1
        m = re.match(r"^(\d)-(\d+)-", group_slug)
        if not m or int(m.group(1)) != sec or int(m.group(2)) != grp:
            failures.append(f"ordering mismatch: {sub_code} vs {group_slug}")

    if failures:
        print("WORKSHEET GENERATION FAILED — alignment gates:")
        for f in failures:
            print("  -", f)
        sys.exit(1)

    # ---------------------------------------------------------------- emit --
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = {"notes": len(notes), "subsections": {}}
    for sub_code in sorted(grouped, key=lambda c: (int(c.split("-")[1][1]), c.split("-")[2])):
        lst = grouped[sub_code]
        pts = reg["points_by_sub"].get(sub_code, [])
        st = subtopics[sub_code]
        summary["subsections"][sub_code] = {
            "title": st["title"], "sme_group": lst[0]["group_slug"],
            "notes": len(lst), "spec_points": len(pts),
        }
        out = [f"# Worksheet {sub_code} — {st['title']}",
               f"SME group `{lst[0]['group_slug']}` · notes: {len(lst)} · spec points: {len(pts)}",
               "",
               "## Spec points in this subsection",
               ""]
        for p in pts:
            flags = []
            if p.get("c_point"):
                flags.append("C")
            if p.get("practical"):
                flags.append("PRACTICAL")
            fl = f" [{','.join(flags)}]" if flags else ""
            dmg = " · DAMAGE" if p.get("damage_flags") else ""
            out.append(f"- **{p['code']}** ({p['official_code']}){fl}{dmg}: {p['official_wording']}")
        out += ["", "## Notes", ""]
        for i, n in enumerate(lst, 1):
            out.append(f"### N{i}. {n['title']}")
            out.append(f"- path: `{n['path']}`")
            out.append(f"- slug: `{n['note_slug']}`")
            if n["excerpt"]:
                out.append(f"- excerpt: {n['excerpt']}")
            if n["headings"]:
                out.append("- headings:")
                for h in n["headings"][:30]:
                    out.append(f"  - {h}")
            if n["body_excerpt"]:
                out.append(f"- body: {n['body_excerpt']}")
            out.append("")
        (OUT_DIR / f"{sub_code.replace('4CH1-S', 'S')}.md").write_text(
            "\n".join(out), encoding="utf-8")

    # full registry appendix for cross-subsection mapping
    lines = ["# Full 4CH1 spec-point registry (182) — cross-reference for mapping", ""]
    for p in sorted(reg["all_points"], key=lambda p: p.get("global_order", 0)):
        flags = []
        if p.get("c_point"):
            flags.append("C")
        if p.get("practical"):
            flags.append("PRACTICAL")
        fl = f" [{','.join(flags)}]" if flags else ""
        lines.append(f"- **{p['code']}** ({p['official_code']}){fl} ({p['subsection']}): {p['official_wording']}")
    (OUT_DIR / "_ALL_POINTS.md").write_text("\n".join(lines), encoding="utf-8")

    (OUT_DIR / "_summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")

    total_pts = sum(len(v) for v in reg["points_by_sub"].values())
    print(f"WORKSHEETS OK — {len(notes)} notes, {len(grouped)} subsections, "
          f"{total_pts} registry points")
    for k, v in summary["subsections"].items():
        print(f"  {k}  notes={v['notes']:2d}  points={v['spec_points']:2d}  {v['title']}")


if __name__ == "__main__":
    main()
