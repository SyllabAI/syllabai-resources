#!/usr/bin/env python3
"""
T-SME-CAMBRIDGE — SME exam-questions scraper for the Cambridge (CAIE) lanes.

Cambridge topic-questions use the COMPILED page model (each
/topic-questions/{section}/{topic}/{leaf-type}/ page embeds that page's
question set in full, like the pre-2026-09 Edexcel pages), but the corpus
conventions are the v1.1 ones committed with the 49-course Edexcel corpus
(question_sets[] + per-question set_slug + scrape.sets_completed/asset_map).

Per topic, every leaf-type page (exam-questions, structured-questions,
multiple-choice-questions, theory-questions, paper-1, ...) becomes one
entry of question_sets[] with set_slug = the leaf-type URL segment — the
same convention the IAL courses use for their MC/structured split
(ial-biology-18: question_sets[0].slug == "exam-questions").

curriculum is taken from the page (course.attributes + syllabusVersion),
never invented: {board: "Cambridge (CIE)", level, subject, exam_code,
sme_course_id, syllabus_version, sme_alias_path, course_name}.

Operator authorization: see LICENSE-DATA.md ("Amendment 2026-09-17 — Save
My Exams authorization (operator attestation)"); the 2026-10-17 operator
directive extends the attested SME corpora to the Cambridge lanes.
Public pages only; no credentials; stdlib only.

Usage:
  python3 scripts/sme_cambridge_examq_scrape.py --courses cie-a-level-chemistry-25 [--limit N]
  python3 scripts/sme_cambridge_examq_scrape.py --all [--delay S]
  python3 scripts/sme_cambridge_examq_scrape.py --manifest-only --courses <slug>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import sme_examq_scrape as eq  # noqa: E402 (http_get, parse_next_data, AssetManager)
import sme_examq_setpage_scrape as sp  # noqa: E402 (atomize_question, LICENSE)
import sme_cambridge_courses as cc  # noqa: E402

BASE = "https://www.savemyexams.com"
REPO = Path("/home/z/my-project/download/syllabai-resources")
OUT = REPO / "SME-ExamQuestion"
SCHEMA = "syllabai.sme-exam-questions/1.1"
LICENSE = sp.LICENSE


def leaf_urls_from_landing(html: str, tq_prefix: str) -> list[str]:
    """All depth-3 leaf pages under the course's /topic-questions/ tree,
    any leaf type (exam-questions, structured-questions, mcq, paper-1...)."""
    urls = sorted(set(re.findall(
        r'href="(' + re.escape(tq_prefix) +
        r'/[a-z0-9-]+/[a-z0-9-]+/[a-z0-9-]+/?)"', html)))
    return [u if u.endswith("/") else u + "/" for u in urls]


def fetch_curriculum(pp: dict, level: str, subject: str, mid: str) -> dict:
    """Board/level/subject/exam_code/syllabus_version — page-sourced."""
    course = pp.get("course") or {}
    attrs = course.get("attributes") or {}
    sv = (pp.get("syllabusVersion") or {}).get("attributes") or {}
    name = attrs.get("name") or ""
    board = ("Cambridge (CIE)" if "Cambridge" in name
             else (name.split(" ")[0] or "Cambridge (CIE)"))
    return {
        "board": board,
        "level": level,
        "subject": subject,
        "exam_code": attrs.get("exam_code"),
        "sme_course_id": course.get("id"),
        "syllabus_version": sv.get("name"),
        "sme_alias_path": mid,
        "course_name": name,
    }


def scrape_topic(course: dict, grouped: dict, sec_slug: str,
                 topic_slug: str, delay: float) -> dict:
    """One topic dir from its leaf-type set pages -> summary dict."""
    path = course["sme_path"]
    tq_prefix = f"/{path}/topic-questions"
    out_dir = OUT / course["slug"] / sec_slug / topic_slug
    assets_dir = out_dir / "assets"
    assets = eq.AssetManager(assets_dir, delay=0.3)

    questions_out: list[dict] = []
    sets_out: list[dict] = []
    missing_all: list[str] = []
    sets_completed: list[str] = []
    subtopics: list[dict] = []
    topic_obj = None
    section_obj = None
    curriculum = None

    for set_url in grouped[(sec_slug, topic_slug)]:
        leaf_type = set_url.rstrip("/").split("/")[-1]
        full_url = set_url if set_url.startswith("http") else BASE + set_url
        html = eq.http_get(full_url)
        pp = eq.parse_next_data(html)
        if curriculum is None:
            curriculum = fetch_curriculum(pp, course["level"],
                                          course["subject"], course["mid"])
        # canonical topic/section objects (first successful page)
        if topic_obj is None:
            t = next((t for t in (pp.get("topics") or [])
                      if (t.get("attributes") or {}).get("slug") == topic_slug), None)
            if t is None:
                raise RuntimeError(f"topic {topic_slug} not on page {set_url}")
            sec_by_id = {s["id"]: s for s in (pp.get("sections") or [])}
            topic_obj = t
            section_obj = sec_by_id[t["relationships"]["section"]["data"]["id"]]
            for st in (pp.get("subtopics") or []):
                if (((st.get("relationships") or {}).get("topic") or {})
                        .get("data", {}) or {}).get("id") == t["id"]:
                    rn = ((st.get("relationships") or {})
                          .get("revision_note") or {}).get("data") or {}
                    subtopics.append({
                        "slug": (st.get("attributes") or {}).get("slug"),
                        "name": (st.get("attributes") or {}).get("name"),
                        "revision_note_id": rn.get("id")})

        qsets = pp.get("questionSets") or []
        q_ids = {q["id"] for q in (pp.get("questions") or [])}

        def _refs(c: dict) -> list[str]:
            return [r["id"] for r in
                    ((c.get("relationships") or {}).get("questions")
                     .get("data") or [])] if c.get("relationships") else []

        # Session-split pages (a-level maths: 10 same-slug session sets,
        # page embeds ONE session) — match by max overlap with the
        # embedded question ids, exactly the convention the 49-course
        # Edexcel corpus uses for its session-split maths topics (one
        # question_sets[] entry = the embedded session). Slug match first
        # for the MC/structured split; overlap decides among same-slug sets.
        cands = [c for c in qsets
                 if (c.get("attributes") or {}).get("slug") == leaf_type] \
            or list(qsets)
        set_obj, best = None, -1
        for c in cands:
            ov = len(q_ids.intersection(_refs(c)))
            if ov > best:
                best, set_obj = ov, c
        if set_obj is None:
            print(f"    !! no questionSet at all: {full_url}", flush=True)
            continue
        set_slug = (set_obj.get("attributes") or {}).get("slug") or leaf_type

        q_by_id = {q["id"]: q for q in (pp.get("questions") or [])}
        set_order_ids = _refs(set_obj)
        missing = [qid for qid in set_order_ids if qid not in q_by_id]
        missing_all.extend(missing)
        ctx = {"asset_fn": None, "equations": []}

        def asset_fn(fig_attrs, _assets=assets):
            src = eq.normalize_cdn_url(fig_attrs.get("src") or "")
            if not src:
                return None, None
            name = _assets.filename_for(src, fig_attrs.get("alt"))
            return src, name

        ctx["asset_fn"] = asset_fn

        n_before = len(questions_out)
        for qid in set_order_ids:
            q = q_by_id.get(qid)
            if q is None:
                continue
            entry = sp.atomize_question(q, ctx, set_slug)
            if entry:
                questions_out.append(entry)
        sets_completed.append(set_slug)
        sets_out.append({
            "id": set_obj.get("id"), "slug": set_slug,
            "name": (set_obj.get("attributes") or {}).get("name"),
            "order": (set_obj.get("attributes") or {}).get("order"),
            "difficulties": (set_obj.get("attributes") or {})
            .get("question_difficulties"),
            "question_count": len(set_order_ids),
            "questions_embedded": len(questions_out) - n_before,
            "page_url": full_url,
        })
        time.sleep(delay)

    assets.fetch_all()

    topic_doc = {
        "schema": SCHEMA,
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams",
                   "landing_url": f"{BASE}/{path}/topic-questions/",
                   "registry": "scripts/sme_cambridge_examq_scrape.py",
                   "license": LICENSE},
        "curriculum": curriculum,
        "section": {"slug": sec_slug,
                    "name": (section_obj.get("attributes") or {}).get("name")},
        "topic": {"id": topic_obj.get("id"), "slug": topic_slug,
                  "name": (topic_obj.get("attributes") or {}).get("name"),
                  "order": (topic_obj.get("attributes") or {}).get("order")},
        "subtopics": subtopics,
        "question_sets": sets_out,
        "scrape": {"questions_embedded": len(questions_out),
                   "questions_missing": missing_all,
                   "asset_failures": assets.failures,
                   "sets_completed": sets_completed,
                   "asset_map": dict(assets.map)},
        "questions": questions_out,
    }
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "topic.json").write_text(
        json.dumps(topic_doc, indent=1, ensure_ascii=False), encoding="utf-8")

    # ------- questions.md / mark-schemes.md (setpage renderer conventions)
    cur = curriculum or {}
    code = cur.get("exam_code") or ""
    label = (f"{cur.get('board')} {cur.get('level').upper()} "
             f"{cur.get('subject')}{f' ({code})' if code else ''}")
    qmd = [f"# Exam Questions — {(topic_obj['attributes'] or {}).get('name')}",
           f"**{(section_obj['attributes'] or {}).get('name')}** · {label}",
           f"> Source: [{BASE}/{path}/topic-questions/]"
           f"({BASE}/{path}/topic-questions/) · "
           f"{len(questions_out)} questions across {len(sets_out)} sets\n"]
    smd = [f"# Mark Schemes — {(topic_obj['attributes'] or {}).get('name')}",
           f"**{(section_obj['attributes'] or {}).get('name')}** · {label}\n"]
    by_set: dict[str, list[dict]] = {}
    for q in questions_out:
        by_set.setdefault(q["set_slug"], []).append(q)
    for s in sets_out:
        qs = by_set.get(s["slug"], [])
        head = f"## {(s.get('name') or s['slug']).title()} ({s['question_count']} questions)"
        qmd.append(f"\n{head}\n")
        smd.append(f"\n{head}\n")
        for qi, q in enumerate(qs, 1):
            diff = q.get("difficulty") or "?"
            qmd.append(f"\n### Q{qi} — {diff} — {q['total_marks']} marks")
            for p in q["parts"]:
                marks = p.get("marks")
                mark_s = (f" [{marks} mark{'s' if marks != 1 else ''}]"
                          if marks is not None else "")
                qmd.append(f"\n**Q{qi}**{mark_s}\n")
                qmd.append(p["problem_md"].strip())
                spq = p.get("source_paper") or {}
                if spq.get("number"):
                    qmd.append(f"\n*Source: {spq.get('date') or ''} "
                               f"{spq['number']} Q{spq.get('question_number') or ''}"
                               f"{str(spq.get('question_part') or '').upper()}*\n")
            smd.append(f"\n### Q{qi}")
            for p in q["parts"]:
                if p["solution_md"].strip():
                    smd.append(p["solution_md"].strip())
    (out_dir / "questions.md").write_text("\n".join(qmd) + "\n", encoding="utf-8")
    (out_dir / "mark-schemes.md").write_text("\n".join(smd) + "\n", encoding="utf-8")

    n_parts = sum(len(q["parts"]) for q in questions_out)
    return {
        "url": sets_out[0]["page_url"] if sets_out else None,
        "section_slug": sec_slug,
        "section_name": (section_obj["attributes"] or {}).get("name"),
        "topic_slug": topic_slug,
        "topic_name": (topic_obj["attributes"] or {}).get("name"),
        "questions": len(questions_out), "parts": n_parts,
        "total_marks": sum(q["total_marks"] for q in questions_out),
        "assets": len(assets.map),
        "asset_failures": assets.failures,
        "missing_questions": missing_all,
        "equations": sum(len(p.get("equations") or [])
                         for q in questions_out for p in q["parts"]),
        "sets": len(sets_out),
        "files": ["topic.json", "questions.md", "mark-schemes.md"],
    }


def disk_summary(course_slug: str) -> list[dict]:
    """Per-topic summaries from topic.json already on disk (resume)."""
    root = OUT / course_slug
    out = []
    if not root.is_dir():
        return out
    for tj in sorted(root.glob("*/*/topic.json")):
        try:
            t = json.loads(tj.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            continue
        qs = t.get("questions") or []
        sc = t.get("scrape") or {}
        out.append({
            "url": (t.get("question_sets") or [{}])[0].get("page_url"),
            "section_slug": t.get("section", {}).get("slug"),
            "section_name": t.get("section", {}).get("name"),
            "topic_slug": t.get("topic", {}).get("slug"),
            "topic_name": t.get("topic", {}).get("name"),
            "questions": len(qs),
            "parts": sum(len(q.get("parts") or []) for q in qs),
            "total_marks": sum(q.get("total_marks") or 0 for q in qs),
            "assets": len(sc.get("asset_map") or {}),
            "asset_failures": sc.get("asset_failures") or [],
            "missing_questions": sc.get("questions_missing") or [],
            "equations": sum(len(p.get("equations") or [])
                             for q in qs for p in q.get("parts") or []),
            "sets": len(t.get("question_sets") or []),
            "files": ["topic.json", "questions.md", "mark-schemes.md"],
            "reused": True,
        })
    return out


def write_course_manifest(course: dict, topics: list[dict],
                          leaf_types: dict, no_tq: bool) -> dict:
    totals = {
        "topics": len(topics),
        "questions": sum(t["questions"] for t in topics),
        "parts": sum(t["parts"] for t in topics),
        "marks": sum(t["total_marks"] for t in topics),
        "assets": sum(t["assets"] for t in topics),
        "asset_failures": sum(len(t["asset_failures"]) for t in topics),
        "missing_questions": sum(len(t["missing_questions"]) for t in topics),
        "equations": sum(t["equations"] for t in topics),
    }
    man = {
        "schema": SCHEMA,
        "course_slug": course["slug"],
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source": {"provider": "Save My Exams",
                   "landing_url": f"{BASE}/{course['sme_path']}/topic-questions/",
                   "registry": "scripts/sme_cambridge_examq_scrape.py",
                   "license": LICENSE},
        "status": ("no_topic_questions_on_sme" if no_tq else "scraped"),
        "course": {"slug": course["slug"], "level": course["level"],
                   "subject": course["subject"], "mid": course["mid"],
                   "leaf_types": leaf_types},
        "totals": totals,
        "topics": sorted(topics, key=lambda t: (t["section_slug"] or "",
                                                t["topic_slug"] or "")),
    }
    (OUT / course["slug"]).mkdir(parents=True, exist_ok=True)
    (OUT / course["slug"] / "manifest.json").write_text(
        json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    return man


def scrape_course(course: dict, delay: float, force: bool,
                  limit: int | None) -> dict:
    path = course["sme_path"]
    tq_prefix = f"/{path}/topic-questions"
    print(f"[{course['slug']}] landing {BASE}{tq_prefix}/", flush=True)
    landing_html = eq.http_get(f"{BASE}{tq_prefix}/")
    leaf_urls = leaf_urls_from_landing(landing_html, tq_prefix)
    if limit:
        leaf_urls = leaf_urls[:limit]
    leaf_types: dict[str, int] = {}
    grouped: dict[tuple[str, str], list[str]] = {}
    for u in leaf_urls:
        sec, top, leaf = u.rstrip("/").split("/topic-questions/", 1)[1].split("/")
        grouped.setdefault((sec, top), []).append(u)
        leaf_types[leaf] = leaf_types.get(leaf, 0) + 1
    print(f"[{course['slug']}] {len(leaf_urls)} leaf pages, "
          f"{len(grouped)} topics, leaf_types={leaf_types}", flush=True)

    reused = {t["topic_slug"]: t for t in disk_summary(course["slug"])}
    topics: list[dict] = []
    if not grouped:
        man = write_course_manifest(course, [], leaf_types, no_tq=True)
        print(f"[{course['slug']}] NO topic questions on SME — recorded",
              flush=True)
        return man
    for i, (sec, top) in enumerate(sorted(grouped), 1):
        if top in reused and not force:
            topics.append(reused[top])
            print(f"[{course['slug']}] [{i}/{len(grouped)}] {top}: reused "
                  f"(q={reused[top]['questions']})", flush=True)
            continue
        t0 = time.time()
        try:
            r = scrape_topic(course, grouped, sec, top, delay)
            topics.append(r)
            print(f"[{course['slug']}] [{i}/{len(grouped)}] {top}: "
                  f"q={r['questions']} parts={r['parts']} marks={r['total_marks']} "
                  f"assets={r['assets']} eq={r['equations']} sets={r['sets']} "
                  f"({time.time() - t0:.1f}s)", flush=True)
        except Exception as exc:  # noqa: BLE001
            print(f"[{course['slug']}] [{i}/{len(grouped)}] !! FAIL {top}: "
                  f"{exc}", flush=True)
    man = write_course_manifest(course, topics, leaf_types, no_tq=False)
    print(f"[{course['slug']}] DONE topics={man['totals']['topics']} "
          f"questions={man['totals']['questions']} "
          f"assets={man['totals']['assets']}", flush=True)
    return man


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--courses", help="comma-separated Cambridge course slugs")
    g.add_argument("--all", action="store_true", help="all 34 Cambridge lanes")
    g.add_argument("--manifest-only", action="store_true",
                   help="rebuild per-course manifests from disk and exit")
    ap.add_argument("--delay", type=float, default=0.8)
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=None,
                    help="cap leaf pages per course (smoke test)")
    args = ap.parse_args()

    all_courses = cc.courses()
    if args.all:
        sel = all_courses
    else:
        want = [c.strip() for c in args.courses.split(",") if c.strip()]
        sel = [c for c in all_courses if c["slug"] in want]
        missing = set(want) - {c["slug"] for c in sel}
        if missing:
            raise SystemExit(f"unknown Cambridge slugs: {sorted(missing)}")

    if args.manifest_only:
        for course in sel:
            reused = disk_summary(course["slug"])
            leaf_types: dict[str, int] = {}
            root = OUT / course["slug"]
            for tj in sorted(root.glob("*/*/topic.json")):
                try:
                    t = json.loads(tj.read_text(encoding="utf-8"))
                except Exception:  # noqa: BLE001
                    continue
                for s in t.get("question_sets") or []:
                    lt = (s.get("page_url") or "").rstrip("/").split("/")[-1]
                    if lt:
                        leaf_types[lt] = leaf_types.get(lt, 0) + 1
            no_tq = not reused
            write_course_manifest(course, reused, leaf_types, no_tq)
            print(f"[{course['slug']}] manifest rebuilt "
                  f"({len(reused)} topics, no_tq={no_tq})")
        return 0

    rc = 0
    for course in sel:
        try:
            scrape_course(course, args.delay, args.force, args.limit)
        except Exception as exc:  # noqa: BLE001
            print(f"[{course['slug']}] FAILED: {exc}", file=sys.stderr)
            rc = 2
    return rc


if __name__ == "__main__":
    sys.exit(main())
