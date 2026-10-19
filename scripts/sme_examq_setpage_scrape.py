#!/usr/bin/env python3
"""
T-SME-11 — SME exam-questions scraper for the NEW set-page model (2026-09 site).

SME restructured its frontend after the Sep-17 harvest: topic-questions are no
longer compiled per topic on one leaf page; each exam-session "question set"
is its own page embedding that set's questions (full TipTap parts, mark
schemes, source-paper provenance, spec-point refs).

This scraper reproduces the committed corpus conventions EXACTLY (same
topic.json schema syllabai.sme-exam-questions/1.1, same part atomization,
same markdown renderers) with set-page orchestration:

  SME-ExamQuestion/<lane>/<section-slug>/<topic-slug>/
    topic.json        question_sets[] = session sets; questions[] flattened
                      with per-question set_slug (schema already supports it)
    questions.md      grouped per set
    mark-schemes.md   grouped per set
    assets/           question images

Only used for lanes whose SME course uses the new model (ELA 4EA1 modules).
Lanes with NO published topic questions are recorded honestly in the course
registry as no_topic_questions_on_sme — never synthesized.

Usage:
  python3 scripts/sme_examq_setpage_scrape.py --lanes igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing,...
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_examq_scrape as eq  # noqa: E402 (http_get, parse_next_data, renderers, AssetManager)

BASE = "https://www.savemyexams.com"
REPO = Path("/home/z/my-project/download/syllabai-resources")
OUT = REPO / "SME-ExamQuestion"
SCHEMA = "syllabai.sme-exam-questions/1.1"
LICENSE = ("operator-authorized; see repo LICENSE-DATA.md (SME attestation "
           "2026-09-17)")

# lane slug -> (course path after savemyexams.com/, curriculum dict minus ids
# fetched live from the page)
LANES = {
    "igcse-english-language-a-16-paper-1-non-fiction-texts-and-transactional-writing": {
        "path": "igcse/english-language/edexcel/a/16/paper-1-non-fiction-texts-and-transactional-writing",
        "level": "igcse", "subject": "english-language", "mid": "a/16/paper-1-non-fiction-texts-and-transactional-writing",
        "display_subject": "English Language A", "module_name": "Paper 1: Non-fiction Texts and Transactional Writing",
    },
    "igcse-english-language-a-16-paper-2-poetry-and-prose-texts-and-imaginative-writing": {
        "path": "igcse/english-language/edexcel/a/16/paper-2-poetry-and-prose-texts-and-imaginative-writing",
        "level": "igcse", "subject": "english-language", "mid": "a/16/paper-2-poetry-and-prose-texts-and-imaginative-writing",
        "display_subject": "English Language A", "module_name": "Paper 2: Poetry and Prose Texts and Imaginative Writing",
    },
}


def atomize_question(q: dict, ctx: dict, set_slug: str) -> dict | None:
    """Atomize one embedded question into the corpus question entry."""
    a = q["attributes"]
    parts_out = []
    for pi, part in enumerate(a.get("parts") or []):
        ctx["equations"] = []
        problem_md = eq.render_blocks(part.get("problem"), ctx)
        mc = part.get("marking_context") or {}
        solution_blocks = part.get("solution")
        if not solution_blocks and mc.get("mark_scheme"):
            solution_blocks = mc["mark_scheme"]
        solution_md = eq.render_blocks(solution_blocks, ctx)
        extract = mc.get("extract")
        if extract:
            extract_md = eq.render_blocks(extract, ctx)
            if extract_md:
                problem_md = f"**Extract:**\n\n{extract_md}\n\n{problem_md}"
        sd = part.get("source_data") or {}
        ptype = part.get("question_type") or "structured"
        choices = None
        if ptype == "multiple_choice" and part.get("choices"):
            choices = []
            for ci, ch in enumerate(sorted(part["choices"], key=lambda c: c.get("order", 0))):
                choices.append({"label": chr(ord("A") + ci),
                                "is_correct": bool(ch.get("is_correct")),
                                "text_md": eq.render_inline(ch.get("content"), ctx).strip()})
        entry = {
            "id": part.get("id"), "order": part.get("order", pi),
            "question_type": ptype,
            "marks": part.get("marks"),
            "command_word": mc.get("command_word"),
            "source_paper": {"date": sd.get("paper_date"),
                             "number": sd.get("paper_number"),
                             "question_number": sd.get("question_number"),
                             "question_part": sd.get("question_part")},
            "spec_point_ids": part.get("spec_point_ids") or [],
            "part_tier": part.get("tier"),
            "problem_md": problem_md,
            "solution_md": solution_md,
        }
        if choices is not None:
            entry["choices"] = choices
        if ctx["equations"]:
            entry["equations"] = ctx["equations"]
        parts_out.append(entry)
    if not parts_out:
        return None
    return {
        "id": q["id"], "set_slug": set_slug, "order": a.get("order"),
        "difficulty": a.get("difficulty"), "style": a.get("style"),
        "total_marks": sum(p.get("marks") or 0 for p in parts_out),
        "parts": parts_out,
    }


def scrape_topic(lane: str, meta: dict, topic: dict, section: dict,
                 sets: list[dict], delay: float) -> dict:
    """Scrape one topic (all its session sets) -> topic dir + returns summary."""
    topic_slug = topic["attributes"]["slug"]
    section_slug = section["attributes"]["slug"]
    out_dir = OUT / lane / section_slug / topic_slug
    assets_dir = out_dir / "assets"
    assets = eq.AssetManager(assets_dir, delay=0.3)

    questions_out: list[dict] = []
    sets_out: list[dict] = []
    missing_all: list[str] = []

    tq_prefix = f"/{meta['path']}/topic-questions/{section_slug}/{topic_slug}"
    for s in sets:
        sattrs = s["attributes"]
        set_slug = sattrs["slug"]
        set_url = f"{BASE}{tq_prefix}/{set_slug}/"
        html = eq.http_get(set_url)
        pp = eq.parse_next_data(html)
        set_obj = next((c for c in (pp.get("questionSets") or [])
                        if c["attributes"]["slug"] == set_slug), None)
        if set_obj is None:
            # fall back: match by id
            set_obj = next((c for c in (pp.get("questionSets") or [])
                            if c["id"] == s["id"]), None)
        if set_obj is None:
            print(f"    !! set page missing set object: {set_url}")
            continue
        q_by_id = {q["id"]: q for q in (pp.get("questions") or [])}
        set_order_ids = [r["id"] for r in set_obj["relationships"]["questions"]["data"]]
        missing = [qid for qid in set_order_ids if qid not in q_by_id]
        missing_all.extend(missing)
        ctx = {"asset_fn": None, "equations": []}

        def asset_fn(fig_attrs, _ctx=None):
            src = eq.normalize_cdn_url(fig_attrs.get("src") or "")
            if not src:
                return None, None
            name = assets.filename_for(src, fig_attrs.get("alt"))
            return src, name

        ctx["asset_fn"] = asset_fn

        n_before = len(questions_out)
        for qid in set_order_ids:
            q = q_by_id.get(qid)
            if q is None:
                continue
            entry = atomize_question(q, ctx, set_slug)
            if entry:
                questions_out.append(entry)

        sets_out.append({
            "id": s["id"], "slug": set_slug,
            "name": sattrs.get("name"), "order": sattrs.get("order"),
            "difficulties": sattrs.get("question_difficulties"),
            "question_count": len(set_order_ids),
            "questions_embedded": len(questions_out) - n_before,
            "page_url": set_url,
        })
        time.sleep(delay)

    assets.fetch_all()

    topic_doc = {
        "schema": SCHEMA,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams",
                   "landing_url": f"{BASE}/{meta['path']}/topic-questions/",
                   "registry": "scripts/sme_examq_setpage_scrape.py",
                   "license": LICENSE},
        "curriculum": meta["curriculum"],
        "section": {"slug": section_slug, "name": section["attributes"]["name"]},
        "topic": {"id": topic["id"], "slug": topic_slug,
                  "name": topic["attributes"]["name"],
                  "order": topic["attributes"]["order"]},
        "subtopics": [],
        "question_sets": sets_out,
        "scrape": {"questions_embedded": len(questions_out),
                   "questions_missing": missing_all,
                   "asset_failures": assets.failures},
        "questions": questions_out,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "topic.json").write_text(
        json.dumps(topic_doc, indent=1, ensure_ascii=False), encoding="utf-8")

    # ------- questions.md / mark-schemes.md grouped per set
    label = (f"Edexcel IGCSE {meta['display_subject']} "
             f"({meta['curriculum']['exam_code']})")
    qmd = [f"# Exam Questions — {topic['attributes']['name']}",
           f"**{section['attributes']['name']}** · {label}",
           f"> Source: [{BASE}/{meta['path']}/topic-questions/]"
           f"({BASE}/{meta['path']}/topic-questions/) · "
           f"{len(questions_out)} questions across {len(sets_out)} session sets\n"]
    smd = [f"# Mark Schemes — {topic['attributes']['name']}",
           f"**{section['attributes']['name']}** · {label}\n"]
    by_set: dict[str, list[dict]] = {}
    for q in questions_out:
        by_set.setdefault(q["set_slug"], []).append(q)
    for s in sets_out:
        qs = by_set.get(s["slug"], [])
        head = f"## {s.get('name') or s['slug']} ({s['question_count']} questions)"
        qmd.append(f"\n{head}\n")
        smd.append(f"\n{head}\n")
        for qi, q in enumerate(qs, 1):
            diff = q.get("difficulty") or "?"
            qmd.append(f"\n### Q{qi} — {diff} — {q['total_marks']} marks")
            for p in q["parts"]:
                marks = p.get("marks")
                mark_s = f" [{marks} mark{'s' if marks != 1 else ''}]" if marks is not None else ""
                qmd.append(f"\n**Q{qi}**{mark_s}\n")
                qmd.append(p["problem_md"].strip())
                sp = p.get("source_paper") or {}
                if sp.get("number"):
                    qmd.append(f"\n*Source: {sp.get('date') or ''} {sp['number']} "
                               f"Q{sp.get('question_number') or ''}"
                               f"{str(sp.get('question_part') or '').upper()}*\n")
            smd.append(f"\n### Q{qi}")
            for p in q["parts"]:
                if p["solution_md"].strip():
                    smd.append(p["solution_md"].strip())
    (out_dir / "questions.md").write_text("\n".join(qmd) + "\n", encoding="utf-8")
    (out_dir / "mark-schemes.md").write_text("\n".join(smd) + "\n", encoding="utf-8")

    return {
        "section_slug": section_slug,
        "section_name": section["attributes"]["name"],
        "topic_slug": topic_slug,
        "topic_name": topic["attributes"]["name"],
        "sets_completed": [s["slug"] for s in sets_out],
        "questions": len(questions_out),
        "parts": sum(len(q["parts"]) for q in questions_out),
        "total_marks": sum(q["total_marks"] for q in questions_out),
        "assets": len(list(assets_dir.glob("*"))) if assets_dir.is_dir() else 0,
        "asset_failures": assets.failures,
        "missing_questions": missing_all,
        "equations": sum(len(p.get("equations") or [])
                         for q in questions_out for p in q["parts"]),
        "page_urls": [s["page_url"] for s in sets_out],
    }


def scrape_lane(lane: str, delay: float) -> dict:
    meta = LANES[lane]
    tq_url = f"{BASE}/{meta['path']}/topic-questions/"
    pp = eq.parse_next_data(eq.http_get(tq_url))
    course = pp.get("course") or {}
    sv = pp.get("syllabusVersion") or {}
    ca = course.get("attributes") or {}
    meta["curriculum"] = {
        "board": "Edexcel", "level": meta["level"].upper(),
        "subject": meta["display_subject"],
        "exam_code": ca.get("exam_code"),
        "sme_course_id": course.get("id"),
        "syllabus_version": (sv.get("attributes") or {}).get("name"),
        "sme_alias_path": (sv.get("attributes") or {}).get("slug"),
    }
    secs = {s["id"]: s for s in (pp.get("sections") or [])}
    topics = sorted(pp.get("topics") or [],
                    key=lambda t: (t["attributes"].get("order") or 0))
    all_sets = pp.get("questionSets") or []

    results = []
    for t in topics:
        sets = sorted([s for s in all_sets
                       if (s["relationships"]["topic"]["data"] or {}).get("id") == t["id"]],
                      key=lambda s: (s["attributes"].get("order") or 0))
        if not sets:
            print(f"  [{t['attributes']['slug']}] no question sets — skipped")
            continue
        sec = secs[t["relationships"]["section"]["data"]["id"]]
        print(f"  [{t['attributes']['slug']}] {len(sets)} session sets ...")
        results.append(scrape_topic(lane, meta, t, sec, sets, delay))

    # ------- per-course manifest (v1.1)
    topics_summary = sorted(results, key=lambda r: (r["section_slug"], r["topic_slug"]))
    totals = {
        "topics": len(topics_summary),
        "questions": sum(r["questions"] for r in topics_summary),
        "parts": sum(r["parts"] for r in topics_summary),
        "marks": sum(r["total_marks"] for r in topics_summary),
        "assets": sum(r["assets"] for r in topics_summary),
        "asset_failures": sum(len(r["asset_failures"]) for r in topics_summary),
        "missing_questions": sum(len(r["missing_questions"]) for r in topics_summary),
        "equations": sum(r["equations"] for r in topics_summary),
    }
    leaf_census = {}
    for r in topics_summary:
        leaf_census["exam-questions"] = leaf_census.get("exam-questions", 0) + len(r["sets_completed"])
    manifest = {
        "schema": SCHEMA,
        "course_slug": lane,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams", "landing_url": tq_url,
                   "registry": "scripts/sme_examq_setpage_scrape.py",
                   "license": LICENSE},
        "course": {"slug": lane, "level": meta["level"],
                   "subject": meta["subject"], "mid": meta["mid"],
                   "leaf_types": leaf_census},
        "totals": totals,
        "topics": topics_summary,
    }
    (OUT / lane).mkdir(parents=True, exist_ok=True)
    (OUT / lane / "manifest.json").write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"  lane totals: {json.dumps(totals)}")
    return totals


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lanes", help="comma-separated lane slugs (default: all)")
    ap.add_argument("--delay", type=float, default=0.8)
    args = ap.parse_args()
    lanes = ([s.strip() for s in args.lanes.split(",") if s.strip()]
             if args.lanes else list(LANES))
    bad = [s for s in lanes if s not in LANES]
    if bad:
        print("unknown lanes:", bad)
        return 2
    for lane in lanes:
        print(f"[{lane}]")
        scrape_lane(lane, args.delay)
    return 0


if __name__ == "__main__":
    sys.exit(main())
