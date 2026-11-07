#!/usr/bin/env python3
"""T-MG-QB-1 run-001 — extract gcse-maths-edexcel question bank (free tier of record).
Per topic: /booklet page → entriesByTab → premium:false PDFs (booklet / exam-questions / solutions)
→ download, sha256, topic.json + lane manifest + receipt. Premium entries recorded as gated."""
import sys, os, json, time, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mg_rsc import fetch, flight, sha256_file, pool_map

WORK = "/tmp/mg_work"
OUT = f"{WORK}/mg-qb/gcse-maths-edexcel"
RUN000 = f"{WORK}/run000/verification.json"
LANE = "gcse-maths-edexcel"
PATH = "/gcse/maths/edexcel"
TASK = "T-MG-QB-1"
RUN = "run-001"
EXTRACTOR = "mg_qb_run001.py v1 (mg_rsc.py v1)"

TAB_TO_FILE = {"booklet": "booklet.pdf", "worksheet": "exam-questions.pdf", "solutions": "solutions.pdf"}

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

def grade_tab(slug):
    m = re.match(r"grade-(\d+)-", slug)
    return m.group(1) if m else None

def process_topic(topic):
    title = TOPICS[topic]
    rec = {"slug": topic, "title": title, "grade_tab": grade_tab(topic), "resources": {},
           "premium_gated": 0, "modes_present": MODES_BY_TOPIC.get(topic, [])}
    if "booklet" not in rec["modes_present"]:
        rec["note"] = "no booklet card on topic page of record"
        return topic, rec
    url = f"https://www.mathsgenie.co.uk{PATH}/{topic}/booklet"
    html = fetch(url, cache_key=f"booklet_{LANE}_{topic}.html")
    tabs = entries_by_tab(flight(html))
    tdir = f"{OUT}/{topic}"
    os.makedirs(tdir, exist_ok=True)
    for tab, entries in tabs.items():
        fname = TAB_TO_FILE.get(tab)
        if not fname:
            continue
        free = [e for e in entries if e.get("premium") is False and e.get("originalUrl", "").lower().endswith(".pdf")]
        gated = [e for e in entries if e.get("premium") is True]
        rec["premium_gated"] += len(gated)
        if not free:
            rec["resources"][tab] = {"status": "not-published", "reason": "no free-tier entry on booklet page"}
            continue
        e = free[0]
        pdf_path = f"{tdir}/{fname}"
        fetch(e["originalUrl"], cache_key=f"pdf_{LANE}_{topic}_{tab}.pdf", binary=True, timeout=60)
        # copy from cache to staging
        with open(f"/tmp/mg_cache/pdf_{LANE}_{topic}_{tab}.pdf", "rb") as f:
            data = f.read()
        with open(pdf_path, "wb") as f:
            f.write(data)
        rec["resources"][tab] = {
            "file": fname, "title": e.get("title"), "url": e["originalUrl"],
            "sha256": sha256_file(pdf_path), "bytes": len(data),
        }
    return topic, rec

def main():
    global TOPICS, MODES_BY_TOPIC
    os.makedirs(OUT, exist_ok=True)
    v = json.load(open(RUN000))
    lane_v = v["lanes"][LANE]
    MODES_BY_TOPIC = {slug: info.get("modes", []) for slug, info in lane_v["topics"].items()}
    TOPICS = {slug: info.get("title", slug) for slug, info in lane_v["topics"].items()}
    print(f"topics: {len(TOPICS)}")
    started = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    results = pool_map(process_topic, sorted(TOPICS), workers=6)
    topics_out, errors = {}, []
    dl_bytes = 0
    for topic, (ok, ret) in results.items():
        if not ok:
            errors.append({"topic": topic, "error": ret})
            continue
        rec = ret[1] if isinstance(ret, tuple) else ret
        topics_out[topic] = rec
        for r in rec["resources"].values():
            dl_bytes += r.get("bytes", 0)

    # write topic.json files
    for topic, rec in topics_out.items():
        os.makedirs(f"{OUT}/{topic}", exist_ok=True)
        rec_out = dict(rec)
        rec_out.update({
            "lane": LANE, "qualification": "GCSE", "subject": "Maths", "board": "edexcel",
            "spec": "1MA1", "href": f"{PATH}/{topic}",
            "source_page": f"https://www.mathsgenie.co.uk{PATH}/{topic}/booklet",
            "extracted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "task_id": TASK, "run": RUN, "extractor": EXTRACTOR,
            "license": "free-tier of record per LICENSE-DATA.md entry; premium-gated items recorded, not downloaded",
            "pending": {"questions_structured_parse": "run-002"},
        })
        with open(f"{OUT}/{topic}/topic.json", "w") as f:
            json.dump(rec_out, f, indent=1, ensure_ascii=False)

    cov = {}
    for tab in TAB_TO_FILE.values():
        cov[tab] = sum(1 for r in topics_out.values() if any(x.get("file") == tab for x in r["resources"].values()))
    manifest = {
        "lane": LANE, "qualification": "GCSE", "subject": "Maths", "board": "edexcel", "spec": "1MA1",
        "plane": "MG-QuestionBank", "task_id": TASK, "run": RUN,
        "extracted_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_chain": "mathsgenie.co.uk topic /booklet pages (RSC flight payloads) → this plane",
        "topic_count": len(topics_out),
        "coverage": cov,
        "premium_gated_total": sum(r["premium_gated"] for r in topics_out.values()),
        "bytes_total": dl_bytes,
        "modes_absent": {"premium-worksheet-sets": "premium-gated, of record but not extracted (license law)"},
        "pending": {"questions_structured_parse": "run-002 (PDF → structured parts)",
                    "papers_bank": "run-003 (past/predicted/mini-tests per papers-*.json)"},
        "extractor": EXTRACTOR,
        "errors": errors,
    }
    with open(f"{OUT}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)
    receipt = {"task_id": TASK, "run": RUN, "lane": LANE, "started_utc": started,
               "finished_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
               "topics": len(topics_out), "pdf_bytes": dl_bytes, "errors": len(errors),
               "coverage": cov}
    with open(f"{WORK}/mg-qb/receipt.json", "w") as f:
        json.dump(receipt, f, indent=1)
    print(json.dumps(receipt, indent=1))
    if errors:
        print("ERRORS:", json.dumps(errors[:5], indent=1))

if __name__ == "__main__":
    main()
