#!/usr/bin/env python3
"""
T-SME-EQ-1 — harvest SME spec-point index from revision-note pages.

Fetches all 112 SME revision-note pages (source URLs from the notes corpus
front matter) and extracts every embedded TipTap `specPoint` block:

    {"type": "specPoint", "attrs": {"id": "spcpt_...", "name": ...,
                                    "definition": ...}}

Output: SME-ExamQuestion/spec_point_index.json
    spec_points: {spcpt_id: {name, definition, notes: [rn ids],
                             subtopic_slugs: [...]}}
plus coverage report vs the spcpt ids referenced by SME-ExamQuestion parts.

Resumable: per-note extraction cached under .cache/sme_spcpt/ (repo-external);
re-runs skip cached pages unless --force. stdlib-only; secrets never printed.
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
REPO_OUT = BASE / "SME-ExamQuestion"
CACHE = Path("/home/z/my-project/.cache/sme_spcpt")
NOTES_ROOT = BASE / "Chemistry IGCSE Revision Notes"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")


def note_records() -> list[dict]:
    """Walk notes corpus; return [{file, url, slug}] from front-matter source:."""
    recs = []
    for dirpath, _dirs, fnames in sorted(NOTES_ROOT.walk()):
        for fn in sorted(fnames):
            if not fn.endswith(".md"):
                continue
            p = dirpath / fn
            head = p.read_text(encoding="utf-8", errors="replace")[:2000]
            m = re.search(r"^source: (https://\S+)", head, re.M)
            if not m:
                continue
            url = m.group(1).rstrip("/")
            recs.append({"file": str(p.relative_to(BASE)), "url": url,
                         "slug": url.split("/")[-1]})
    return recs


def fetch(url: str, timeout: int = 45) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def extract_spec_points(html: bytes) -> list[dict]:
    m = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">(.*?)</script>',
        html.decode("utf-8", errors="replace"), re.S)
    if not m:
        raise ValueError("no __NEXT_DATA__")
    data = json.loads(m.group(1))
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


def harvest_one(rec: dict, force: bool) -> dict:
    cpath = CACHE / (rec["slug"] + ".json")
    if cpath.exists() and not force:
        return json.loads(cpath.read_text(encoding="utf-8"))
    last_err = None
    for attempt in range(3):
        try:
            html = fetch(rec["url"])
            out = {"slug": rec["slug"], "url": rec["url"],
                   "file": rec["file"],
                   "rn_ids": extract_rn_ids(html),
                   "spec_points": extract_spec_points(html)}
            cpath.write_text(json.dumps(out, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            return out
        except Exception as exc:  # noqa: BLE001 — retry any fetch/parse error
            last_err = exc
            time.sleep(2.0 * (attempt + 1))
    raise RuntimeError(f"fetch failed x3: {rec['url']} ({last_err})")


def question_ids() -> set[str]:
    ids = set()
    for f in sorted(set(
            glob_topic_files())):
        t = json.loads(f.read_text(encoding="utf-8"))
        for q in t.get("questions", []):
            for part in q.get("parts", []):
                for sid in part.get("spec_point_ids", []) or []:
                    ids.add(sid)
    return ids


def glob_topic_files() -> list[Path]:
    return sorted(p for p in REPO_OUT.glob("*/*/*/topic.json")) + \
           sorted(p for p in REPO_OUT.glob("*/*/topic.json"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    CACHE.mkdir(parents=True, exist_ok=True)
    recs = note_records()
    print(f"notes with source URL: {len(recs)}")

    results, failures = [], []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(harvest_one, r, args.force): r for r in recs}
        done = 0
        for fut in cf.as_completed(futs):
            r = futs[fut]
            try:
                res = fut.result()
                results.append(res)
            except Exception as exc:  # noqa: BLE001
                failures.append((r["url"], str(exc)))
            done += 1
            if done % 20 == 0 or done == len(recs):
                print(f"  fetched {done}/{len(recs)} "
                      f"(failures: {len(failures)})")

    if failures:
        for url, err in failures:
            print(f"FAIL: {url} :: {err}", file=sys.stderr)
        return 2

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

    qids = question_ids()
    covered = qids & set(spec)
    missing = sorted(qids - set(spec))

    doc = {
        "schema": "syllabai.sme-spec-point-index/1.0",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_pages": len(results),
        "spec_points": dict(sorted(spec.items())),
        "coverage": {
            "question_part_ids_total": len(qids),
            "covered_by_index": len(covered),
            "missing_from_index": missing,
        },
    }
    REPO_OUT.mkdir(parents=True, exist_ok=True)
    out = REPO_OUT / "spec_point_index.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                   encoding="utf-8")

    print(f"distinct spec points in index: {len(spec)}")
    print(f"question ids: {len(qids)} covered: {len(covered)} "
          f"missing: {len(missing)}")
    for sid in missing:
        print(f"  MISSING {sid}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
