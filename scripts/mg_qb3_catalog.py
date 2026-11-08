#!/usr/bin/env python3
"""T-MG-QB-3 run-001 — build the a-level-maths-edexcel question-bank catalog.

Law applied (MG-QuestionBank README):
  * lane of record: mathsgenie.co.uk/a-level/maths/edexcel (new site) — 44 chapters
    (Year 1 `as-*` + Year 2 `a-level-*` slugs), 245 subtopics; hierarchy decoded
    live from the RSC flight payload; drift vs T-MG-VERIFY-1 run-000 recorded.
  * question resources of record: the old-site per-chapter Question Set pages
    (old.mathsgenie.co.uk/newalevel.php -> a-level-*-questions-*.php), each carrying
    a {chapter}.pdf exam-question paper + {chapter}ans.pdf solutions paper at
    old-asset.mathsgenie.co.uk/alevel/. Subtopic pages carry no question PDFs
    (video/lesson only); the new-site subtopic question bank is interactive-only,
    recorded as link-of-record, never scraped.
  * join: old-site question-set chapter <-> new-site chapter slug via the chapter
    name + numbering crosswalk built from both sides at run time.

Output: /home/z/my-project/mg_work/catalog/alevel_edexcel_catalog.json
"""
import json
import os
import re
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mg_rsc import fetch  # noqa: E402

WORK = "/home/z/my-project/mg_work"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lane_hierarchy():
    """Decode the new-site lane payload into chapters + subtopics."""
    html = fetch("https://www.mathsgenie.co.uk/a-level/maths/edexcel",
                 cache_key="lane3_a-level-maths-edexcel.html")
    payload = fetch.__globals__["flight"](html)
    dec = json.JSONDecoder()
    chapters, subtopics = [], {}
    for m in re.finditer(r'\{"id":"', payload):
        try:
            obj, end = dec.raw_decode(payload, m.start())
        except Exception:
            continue
        if not (isinstance(obj, dict) and str(obj.get("href") or "").startswith("/a-level/maths/edexcel/")):
            continue
        if "topics" in obj:  # chapter with children
            subs = []
            for s in obj["topics"]:
                s = dict(s)
                s["_chapter_slug"] = obj["slug"]
                subs.append(s)
                subtopics[s["slug"]] = s
            chapters.append({"id": obj["id"], "slug": obj["slug"], "title": obj["title"],
                             "href": obj["href"], "topicId": obj.get("topicId"),
                             "subtopics": subs})
    return chapters, subtopics


def old_site_structure():
    """Parse newalevel.php sidebar into sections -> entries (topics + question sets)."""
    html = fetch("https://old.mathsgenie.co.uk/newalevel.php", cache_key="al3_old_newalevel.html")
    sections = []  # [{title, entries:[{kind, num, name, href}]}]
    cur = None
    # walk the sidebar list items in order; section headers are <h4>/<h5>/<strong>/li without numbered links
    for m in re.finditer(r'<h([2-5])[^>]*>(.*?)</h\1>|<li><a[^>]+href="([a-z0-9-]+\.php)"[^>]*>(.*?)</a>', html, re.S):
        if m.group(1):  # section header
            title = re.sub(r"<[^>]+>", " ", m.group(2))
            title = " ".join(title.split())
            cur = {"title": title, "entries": []}
            sections.append(cur)
        else:
            href, text = m.group(3), m.group(4)
            text = " ".join(re.sub(r"<[^>]+>", " ", text).split()).replace("&nbsp;", " ")
            if cur is None:
                cur = {"title": "(front)", "entries": []}
                sections.append(cur)
            kind = "question-set" if "-questions-" in href else "topic"
            num = None
            mn = re.match(r"^(\d+)\.(\d+)\s*(.*)$", text)
            if mn:
                num = f"{mn.group(1)}.{mn.group(2)}"
                text = mn.group(3)
            cur["entries"].append({"kind": kind, "num": num, "name": text, "href": href})
    return sections


def question_set_pdfs(qs_href):
    """Fetch a question-set page; return {name, q_url, a_url, label_q, label_a}.
    Classification law: the ans URL's stem must equal the other stem + 'ans'
    (handles chapter names that themselves end in 'ans', e.g. radians.pdf)."""
    html = fetch("https://old.mathsgenie.co.uk/" + qs_href, cache_key="al3_old_" + qs_href)
    links = re.findall(r'<a[^>]+href="([^"]+\.pdf)"[^>]*>(.*?)</a>', html, re.S)
    urls = []
    for h, t in links:
        t = " ".join(re.sub(r"<[^>]+>", " ", t).split())
        urls.append((h, t))
    # dedupe, keep order
    seen, uniq = set(), []
    for h, t in urls:
        if h not in seen:
            seen.add(h)
            uniq.append((h, t))
    stems = {h: h.rsplit("/", 1)[-1][:-4] for h, _ in uniq}
    q_url = a_url = None
    label_q = label_a = None
    for h, t in uniq:
        st = stems[h]
        if st.endswith("ans") and st[:-3] + ".pdf" in {u.rsplit("/", 1)[-1] for u, _ in uniq}:
            a_url, label_a = h, t
        else:
            q_url, label_q = h, t
    return {"page": qs_href, "q_url": q_url, "a_url": a_url,
            "label_q": label_q, "label_a": label_a}


def main():
    started = NOW
    chapters, subtopics = lane_hierarchy()
    print(f"new-site lane: {len(chapters)} chapters, {len(subtopics)} subtopics")

    sections = old_site_structure()
    n_topics = sum(1 for s in sections for e in s["entries"] if e["kind"] == "topic")
    qs_pages = [e for s in sections for e in s["entries"] if e["kind"] == "question-set"]
    print(f"old-site sidebar: {len(sections)} sections, {n_topics} topic pages, {len(qs_pages)} question sets")

    # fetch every question-set page for its PDF pair
    qs_records = []
    for e in qs_pages:
        rec = dict(e)
        try:
            rec.update(question_set_pdfs(e["href"]))
        except Exception as ex:
            rec["error"] = str(ex)
        qs_records.append(rec)
    missing = [r["href"] for r in qs_records if r.get("error") or not r.get("q_url")]
    print(f"question-set pages fetched: {len(qs_records)}, without q pdf: {missing}")

    # ---- join old question sets -> new chapters ----
    # normalise a chapter display name for matching
    def norm(s):
        return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()

    join = []
    for ch in chapters:
        # new-site chapter slug: {qual}-{strand}-{n}-{name}; title carries the display name
        ch_key = norm(ch["title"])
        cand = None
        for r in qs_records:
            # question-set href: a-level-{y}-questions-{name}.php ; entry name "Question Set N: Title"
            rname = re.sub(r"^question set \d+:\s*", "", r["name"], flags=re.I)
            if norm(rname) == ch_key:
                cand = r
                break
        join.append({"chapter": ch, "question_set": cand})

    joined = sum(1 for j in join if j["question_set"])
    print(f"join by title: {joined}/{len(chapters)}")
    unmatched = [j["chapter"]["slug"] for j in join if not j["question_set"]]
    if unmatched:
        print("unmatched chapters:", unmatched)
        # fallback: match by chapter number embedded in slug
        for j in join:
            if j["question_set"]:
                continue
            m = re.search(r"-(\d+)-[^-]+$", j["chapter"]["slug"])
            if not m:
                continue
            n = m.group(1)
            for r in qs_records:
                if re.search(rf"questions-{n}-|questions-{n}\b", r["href"]):
                    j["question_set"] = r
                    break
        joined = sum(1 for j in join if j["question_set"])
        print(f"join after slug-number fallback: {joined}/{len(chapters)}")

    catalog = {
        "source_lane": "https://www.mathsgenie.co.uk/a-level/maths/edexcel",
        "classic_source": "https://old.mathsgenie.co.uk/newalevel.php",
        "asset_host": "old-asset.mathsgenie.co.uk/alevel/",
        "scraped_at": NOW,
        "qualification": "A-Level", "subject": "Maths", "board": "Edexcel", "spec": "9MA0",
        "chapter_count": len(chapters),
        "subtopic_count": len(subtopics),
        "sections": [{"title": s["title"],
                      "chapters": [e["name"] for e in s["entries"] if e["kind"] == "question-set"]}
                     for s in sections],
        "topics": [
            {
                "slug": j["chapter"]["slug"],
                "title": j["chapter"]["title"],
                "chapter_id": j["chapter"]["id"],
                "topicId": j["chapter"].get("topicId"),
                "site_topic_page": "https://mathsgenie.co.uk" + j["chapter"]["href"],
                "subtopics": [{"slug": s["slug"], "title": s["title"],
                               "site_topic_page": "https://mathsgenie.co.uk" + s["href"]}
                              for s in j["chapter"]["subtopics"]],
                "question_set": j["question_set"],
            } for j in join
        ],
    }
    os.makedirs(f"{WORK}/catalog", exist_ok=True)
    with open(f"{WORK}/catalog/alevel_edexcel_catalog.json", "w") as f:
        json.dump(catalog, f, indent=1, ensure_ascii=False)
    os.makedirs(f"{WORK}/logs", exist_ok=True)
    with open(f"{WORK}/logs/qb3_catalog_log.json", "w") as f:
        json.dump({"run": "T-MG-QB-3/run-001", "started": started, "finished": NOW,
                   "chapters": len(chapters), "subtopics": len(subtopics),
                   "question_sets": len(qs_records),
                   "qs_without_pdf": missing,
                   "joined": joined}, f, indent=1)

    with_pdf = sum(1 for t in catalog["topics"] if t["question_set"] and t["question_set"].get("q_url"))
    with_ans = sum(1 for t in catalog["topics"] if t["question_set"] and t["question_set"].get("a_url"))
    print(f"\ncatalog: {len(catalog['topics'])} chapters | with q pdf={with_pdf} | with ans pdf={with_ans}")
    print("sections:", json.dumps(catalog["sections"], indent=1)[:800])


if __name__ == "__main__":
    main()
