#!/usr/bin/env python3
"""T-MG-QB-2 run-001 — build the igcse-maths-edexcel question-bank catalog.

Law applied (MG-QuestionBank README):
  * mode presence re-verified against the live lane at run time; drift vs
    T-MG-VERIFY-1 run-000 recorded, never silently reconciled.
  * resources read off each topic's /booklet page (entriesByTab RSC payload):
    free (premium:false) entries -> questions_ws_url / booklet_url / solutions_url;
    premium Sets counted as gated, never downloaded (license law).
  * site-native slug grammar preserved: grade-{band}-{g}-{n}-{name};
    grade/tier stay data, never directories.

Output: mg_work/catalog/igcse_edexcel_catalog.json + logs/qb2_catalog_log.json
"""
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mg_rsc import fetch, flight  # noqa: E402

WORK = "/home/z/my-project/mg_work"
LANE = "igcse-maths-edexcel"
PATH = "/igcse/maths/edexcel"
RUN000 = "/home/z/my-project/scripts/mg_run000_main/verification.json"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

GRADE_RE = re.compile(r"^grade-\d+-\d+-\d+-[a-z0-9-]+$")
NON_TOPICS = {"papers", "worksheets", "revision-guides", "lessons", "flashcards", "question-rush",
              "daily-greens", "videos", "questions", "mock-exam-builder", "mini-tests", "45-min-tests",
              "predicted-papers", "grade-boundaries"}


def parse_slug(slug):
    """Site-native slug grammar (validated against the GCSE QB-1 catalog codes):
    grade-{g}-{g}-{n}-{name}            -> band=g, code g.n        (single bands 1..7)
    grade-8-9-{g}-{n}-{name}            -> band='8-9', g=8, code 8.n
    Returns (band, g, n, name)."""
    m89 = re.match(r"^grade-8-9-(\d+)-(\d+)-([a-z0-9-]+)$", slug)
    if m89:
        return "8-9", 8, int(m89.group(2)), m89.group(3)
    m = re.match(r"^grade-(\d+)-(\d+)-(\d+)-([a-z0-9-]+)$", slug)
    if m and m.group(1) == m.group(2):
        g = int(m.group(1))
        return str(g), g, int(m.group(3)), m.group(4)
    raise ValueError(f"unparseable topic slug: {slug}")


def harvest_lane_slugs(html, path_prefix):
    """Topic slugs from lane-page anchor hrefs (same grammar as mg_run000.py)."""
    slugs = {}
    for m in re.finditer(r'href="' + re.escape(path_prefix) + r'/([a-z0-9-]+)"', html):
        slug = m.group(1)
        if slug in NON_TOPICS or not GRADE_RE.match(slug):
            continue
        slugs.setdefault(slug, None)
    return sorted(slugs)


def anchor_titles(html, path_prefix):
    """href -> anchor text for topic links."""
    titles = {}
    for m in re.finditer(r'<a[^>]+href="' + re.escape(path_prefix) + r'/([a-z0-9-]+)"[^>]*>(.*?)</a>',
                         html, re.S):
        slug, text = m.group(1), re.sub(r"<[^>]+>", " ", m.group(2))
        text = " ".join(text.split())
        if text and slug not in titles:
            titles[slug] = text
    return titles


def entries_by_tab(payload):
    dec = json.JSONDecoder()
    blocks = []
    for m in re.finditer(r'"entriesByTab":', payload):
        i = payload.find("{", m.end())
        try:
            obj, _ = dec.raw_decode(payload, i)
            blocks.append(obj)
        except Exception:
            pass
    return blocks[0] if blocks else {}


def main():
    started = NOW
    # --- 1) live lane page: re-verify topic set vs run-000 -------------------
    lane_html = fetch(f"https://www.mathsgenie.co.uk{PATH}", cache_key=f"lane2_{LANE}.html")
    live_slugs = harvest_lane_slugs(lane_html, PATH)
    titles = anchor_titles(lane_html, PATH)
    v000 = json.load(open(RUN000))
    r000_slugs = sorted(v000["lanes"][LANE]["topics"].keys())
    added = sorted(set(live_slugs) - set(r000_slugs))
    removed = sorted(set(r000_slugs) - set(live_slugs))
    drift = {"live_topic_count": len(live_slugs), "run000_topic_count": len(r000_slugs),
             "added_since_run000": added, "removed_since_run000": removed}
    print("lane drift:", json.dumps(drift))

    # --- 2) per-topic booklet pages -> free PDF URLs -------------------------
    cat_topics = []
    log = []
    for idx, slug in enumerate(live_slugs):
        band, g, n, _name = parse_slug(slug)
        title = titles.get(slug) or v000["lanes"][LANE]["topics"].get(slug, {}).get("title") or slug
        rec = {"slug": slug, "title": title, "grade_band": band, "grade": g, "code": f"{g}.{n}",
               "ordinal": n, "premium_gated": 0}
        try:
            html = fetch(f"https://www.mathsgenie.co.uk{PATH}/{slug}/booklet",
                         cache_key=f"booklet_{LANE}_{slug}.html")
            tabs = entries_by_tab(flight(html))
        except Exception as e:
            log.append({"slug": slug, "error": f"booklet page: {e}"})
            rec["error"] = str(e)
            cat_topics.append(rec)
            continue
        free = {}
        for tab in ("worksheet", "booklet", "solutions"):
            entries = tabs.get(tab, [])
            fr = [e for e in entries if e.get("premium") is False
                  and str(e.get("originalUrl", "")).lower().endswith(".pdf")]
            gated = [e for e in entries if e.get("premium") is True]
            rec["premium_gated"] += len(gated)
            if fr:
                free[tab] = fr[0]["originalUrl"]
            else:
                free[tab] = None
        rec["questions_ws_url"] = free["worksheet"]
        rec["booklet_url"] = free["booklet"]
        rec["solutions_url"] = free["solutions"]
        rec["exam_questions_published"] = bool(free["worksheet"] or free["booklet"])
        cat_topics.append(rec)
        if (idx + 1) % 20 == 0:
            print(f"  {idx+1}/{len(live_slugs)} booklet pages read", flush=True)

    # title -> name (title case as printed on lane page)
    for t in cat_topics:
        t["name"] = t.pop("title")

    catalog = {
        "source_page": f"https://www.mathsgenie.co.uk{PATH}",
        "site_lane": f"https://mathsgenie.co.uk{PATH}",
        "scraped_at": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "qualification": "IGCSE", "subject": "Maths", "board": "Edexcel",
        "topic_count": len(cat_topics),
        "grade_bands": sorted({t["grade_band"] for t in cat_topics}, key=str),
        "drift_vs_run000": drift,
        "topics": cat_topics,
    }
    os.makedirs(f"{WORK}/catalog", exist_ok=True)
    with open(f"{WORK}/catalog/igcse_edexcel_catalog.json", "w") as f:
        json.dump(catalog, f, indent=1, ensure_ascii=False)
    with open(f"{WORK}/logs/qb2_catalog_log.json", "w") as f:
        json.dump({"run": "T-MG-QB-2/run-001", "started": started, "finished": NOW,
                   "log": log, "drift": drift}, f, indent=1)

    # summary
    ws = sum(1 for t in cat_topics if t["questions_ws_url"])
    bk = sum(1 for t in cat_topics if t["booklet_url"])
    so = sum(1 for t in cat_topics if t["solutions_url"])
    errs = [t["slug"] for t in cat_topics if t.get("error")]
    print(f"\ncatalog: {len(cat_topics)} topics | ws={ws} booklet={bk} solutions={so} | errors={errs}")
    print("premium gated total:", sum(t["premium_gated"] for t in cat_topics))
    print("bands:", catalog["grade_bands"])


if __name__ == "__main__":
    main()
