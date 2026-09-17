#!/usr/bin/env python3
"""
T-SME-EQ-2 — multi-course SME spec-point harvest (exam-questions corpus).

For each course slug, fetches that course's SME revision-note pages (URLs
discovered from sitemaps by scripts/sme_notes_discover.py, cached at
.cache/sme_notes_urls.json) and extracts every embedded TipTap `specPoint`
block, writing <course>/spec_point_index.json with the same schema as the
chemistry v1 index (syllabai.sme-spec-point-index/1.0) plus additive
provenance fields.

Per-course cache: .cache/sme_spcpt/<course-slug>/<page-slug>.json — re-runs
skip cached pages unless --force. stdlib-only; secrets never printed.

Note: unlike igcse-chemistry-19 (resolved to official 4CH1 codes), this
harvest intentionally stops at the SME-native index (spcpt_ id -> name /
definition / note linkage). No official codes are invented for other
subjects — they have no registry here.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
CORPUS = BASE / "SME-ExamQuestion"
CACHE = Path("/home/z/my-project/.cache/sme_spcpt")
DISCOVER = Path("/home/z/my-project/.cache/sme_notes_urls.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

SINGLE_SEGMENT = [
    "ial-biology-18",
    "ial-chemistry-17",
    "ial-further-maths-18-further-pure-1",
    "ial-physics-19",
    "igcse-business-19",
    "igcse-economics-17",
    "igcse-english-literature-16",
    "igcse-further-maths-19",
    "igcse-geography-19",
    "igcse-ict-17",
]


def fetch(url: str, timeout: int = 45) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def next_data(html: bytes):
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html.decode("utf-8", errors="replace"), re.S)
    return json.loads(m.group(1)) if m else None


def extract_spec_points(html: bytes) -> list[dict]:
    data = next_data(html)
    if data is None:
        raise ValueError("no __NEXT_DATA__")
    blocks = {}

    def walk(node):
        if isinstance(node, dict):
            if node.get("type") == "specPoint":
                a = node.get("attrs") or {}
                sid = a.get("id")
                if sid and sid not in blocks:
                    blocks[sid] = {"id": sid,
                                   "name": a.get("name") or "",
                                   "definition": a.get("definition") or ""}
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    return list(blocks.values())


def extract_rn_ids(html: bytes) -> list[str]:
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html.decode("utf-8", errors="replace"), re.S)
    if not m:
        return []
    return sorted(set(re.findall(r"\brn_[A-Za-z0-9]+", m.group(1))))


def harvest_one(course: str, url: str, force: bool) -> dict:
    slug = url.rstrip("/").split("/")[-1]
    cdir = CACHE / course
    cpath = cdir / (slug + ".json")
    if cpath.exists() and not force:
        return json.loads(cpath.read_text(encoding="utf-8"))
    last_err = None
    for attempt in range(3):
        try:
            html = fetch(url)
            out = {"slug": slug, "url": url,
                   "rn_ids": extract_rn_ids(html),
                   "spec_points": extract_spec_points(html)}
            cdir.mkdir(parents=True, exist_ok=True)
            cpath.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            return out
        except Exception as exc:  # noqa: BLE001 — retry any fetch/parse error
            last_err = exc
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"fetch failed x3: {url} ({last_err})")


def course_note_urls(course: str) -> tuple[str, list[str]]:
    disc = json.loads(DISCOVER.read_text(encoding="utf-8"))
    info = disc["courses"][course]
    base = info["notes_base"]
    urls = set()
    for u in disc["notes_urls"]:
        if not u.startswith(base):
            continue
        u = u.rstrip("/")
        rest = u[len(base):].strip("/").split("/") if u[len(base):] else []
        if len(rest) >= 2:          # leaf pages: section/topic/leaf (or deeper)
            urls.add(u)
    return base, sorted(urls)


def question_ids(course: str) -> set[str]:
    root = CORPUS / course
    files = sorted(root.glob("*/*/*/topic.json")) + \
            sorted(root.glob("*/*/topic.json"))
    ids = set()
    for f in files:
        t = json.loads(f.read_text(encoding="utf-8"))
        for q in t.get("questions", []):
            for part in q.get("parts", []):
                for sid in part.get("spec_point_ids", []) or []:
                    ids.add(sid)
    return ids


def harvest_course(course: str, workers: int, force: bool) -> int:
    base, urls = course_note_urls(course)
    print(f"[{course}] notes_base {base}")
    print(f"[{course}] leaf pages: {len(urls)}")
    results, failures = [], []
    with cf.ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(harvest_one, course, u, force): u for u in urls}
        done = 0
        for fut in cf.as_completed(futs):
            u = futs[fut]
            try:
                results.append(fut.result())
            except Exception as exc:  # noqa: BLE001
                failures.append({"url": u, "error": str(exc)[:200]})
            done += 1
            if done % 25 == 0 or done == len(urls):
                print(f"[{course}]   fetched {done}/{len(urls)} "
                      f"(failures: {len(failures)})")

    spec: dict[str, dict] = {}
    for res in results:
        for sp in res["spec_points"]:
            entry = spec.setdefault(sp["id"], {
                "name": sp["name"], "definition": sp["definition"],
                "notes": [], "subtopic_slugs": []})
            if not entry["definition"] and sp["definition"]:
                entry["definition"] = sp["definition"]
            entry["notes"].extend(res["rn_ids"][:1])  # primary rn id
            entry["subtopic_slugs"].append(res["slug"])
    for e in spec.values():
        e["notes"] = sorted(set(e["notes"]))
        e["subtopic_slugs"] = sorted(set(e["subtopic_slugs"]))

    qids = question_ids(course)
    covered = qids & set(spec)
    missing = sorted(qids - set(spec))

    doc = {
        "schema": "syllabai.sme-spec-point-index/1.0",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "course_slug": course,
        "notes_base": base,
        "source_pages": len(results),
        "fetch_failures": failures,
        "spec_points": dict(sorted(spec.items())),
        "coverage": {
            "question_part_ids_total": len(qids),
            "covered_by_index": len(covered),
            "missing_from_index": missing,
        },
    }
    out = CORPUS / course / "spec_point_index.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                   encoding="utf-8")

    pct = (f"{100 * len(covered) / len(qids):.1f}%" if qids else "n/a")
    print(f"[{course}] spec points: {len(spec)} | part ids {len(qids)} "
          f"covered {len(covered)} ({pct}) missing {len(missing)} "
          f"| fetch failures {len(failures)}")
    if qids and len(covered) < 0.5 * len(qids):
        print(f"[{course}] WARNING: coverage below 50% — inspect before use")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--courses", help="comma-separated course slugs")
    g.add_argument("--class-single", action="store_true",
                   help="the 10 single-segment courses")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    courses = (SINGLE_SEGMENT if args.class_single
               else [c.strip() for c in args.courses.split(",") if c.strip()])

    rc = 0
    for course in courses:
        if not (CORPUS / course).is_dir():
            print(f"[{course}] ERROR: no corpus folder", file=sys.stderr)
            rc = 2
            continue
        try:
            harvest_course(course, args.workers, args.force)
        except Exception as exc:  # noqa: BLE001
            print(f"[{course}] FAILED: {exc}", file=sys.stderr)
            rc = 2
    return rc


if __name__ == "__main__":
    sys.exit(main())
