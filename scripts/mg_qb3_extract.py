#!/usr/bin/env python3
"""T-MG-QB-3 run-001 — MathsGenie A-Level Maths (Edexcel, 9MA0) per-chapter
question-set extractor for MG-QuestionBank/a-level-maths-edexcel.

Lane law (README + catalog of record):
  * lane of record: mathsgenie.co.uk/a-level/maths/edexcel — 44 chapters
    (Year 1 `as-*` + Year 2 `a-level-*`), 245 subtopics. The sibling
    /as-level/maths/edexcel lane's 24 chapters are slug-identical to the Year-1
    half of this lane (verified at run time) — overlap recorded, not extracted twice.
  * question resources of record: per-chapter Question Set PDFs from the old-site
    delivery (old.mathsgenie.co.uk/newalevel.php -> a-level-*-questions-*.php),
    each `{chapter}.pdf` + `{chapter}ans.pdf` at old-asset.mathsgenie.co.uk/alevel/.
    9 chapters publish only the answers link; the sibling question PDF follows the
    site's own naming convention on the same asset host (HEAD 200 at run time) and
    is included with explicit discovery provenance.
  * SEGMENTATION LAW (this lane's parser of record): A-Level question sets embed
    question numbers inside display-math blocks, so leading-number anchoring (QB-1/2
    law) is unreliable here. Every question instead prints a right-aligned
    "(Total for question N is M marks)" boundary line. Questions are segmented by
    consecutive total lines in spatial (page, y) order; the total line travels with
    its question's crop.
  * NUMBERING LAW: the printed number is the question's identity. Non-monotonic
    dips (source typos, e.g. Q22 printed as "2") are position-derived and flagged
    `printed_as`; ascending gaps (missing print numbers) are kept as printed and
    recorded as numbering gaps. Never renumbered silently, never padded.
  * MARKS LAW (A-Level extension of the QB-1/2 printed-marks law): marks come only
    from the printed total line ("(Total for question N is M marks)"); the QB-1/2
    "(N marks)" pattern does not occur in this lane. Nothing inferred.
  * IMAGE-ONLY SETS (9 of 44): scanned question sets carry no text layer —
    question_count = 0, honest gap of record; content preserved as full-page source
    renders (assets/page-NN.png), never padded.

Source PDFs are fetched, processed and discarded; only sha256 + URLs survive.
"""
import argparse, hashlib, io, json, os, re, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import fitz
from PIL import Image

EXTRACTOR = "mg_qb3_extract.py v1 (T-MG-QB-3 run-001; total-line segmentation law)"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
WORK = "/home/z/my-project/mg_work"

TOT = re.compile(r'Total for [Qq]uestion\s+(\d{1,2})\s+is\s+(\d{1,2})\s*marks?\)?', re.I)
CHROME_TITLE = re.compile(r'^(as |a )?level [a-z]+:', re.I)
PARTS_RE = re.compile(r'^\s*\(([a-h]|[ivx]{1,4})\)', re.M)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(url, dest):
    """Download (lane-prefixed staging). Returns True on success."""
    if os.path.exists(dest) and os.path.getsize(dest) > 800:
        return True
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    import urllib.request
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"})
            with urllib.request.urlopen(req, timeout=90) as r:
                data = r.read()
            with open(dest, "wb") as f:
                f.write(data)
            if os.path.getsize(dest) > 800:
                return True
        except Exception:
            time.sleep(1.5 * (attempt + 1))
    if os.path.exists(dest):
        os.remove(dest)
    return False


def valid_pdf(path):
    try:
        doc = fitz.open(path)
        if len(doc) == 0:
            return None
        t = doc[0].get_text()
        if "Error 404" in t or "Object not found" in t:
            return None
        return doc
    except Exception:
        return None


def line_text(l):
    out = ""
    for s in l["spans"]:
        p = s["text"]
        if out and p and not out[-1].isspace() and not p[0].isspace() and out[-1].isalnum() and p[0].isalnum():
            out += " "
        out += p
    return out


def is_chrome(txt):
    t = txt.strip()
    tl = t.lower()
    return ("mathsgenie.co.uk" in tl or "do not write" in tl or CHROME_TITLE.match(tl))


def page_lines(doc, pno):
    """All text lines on a page: [(y0, y1, x0, x1, text, is_chrome)]."""
    out = []
    d = doc[pno].get_text("dict")
    for b in d["blocks"]:
        if b["type"] != 0:
            continue
        for l in b["lines"]:
            txt = line_text(l)
            if not txt.strip():
                continue
            x0, y0, x1, y1 = l["bbox"]
            out.append((y0, y1, x0, x1, txt, is_chrome(txt)))
    out.sort(key=lambda z: (z[0], z[2]))
    return out


def content_bottom(doc, pno):
    ls = page_lines(doc, pno)
    ys = [y1 for (y0, y1, x0, x1, t, ch) in ls if not ch]
    return max(ys, default=doc[pno].rect.height - 30)


def top_after_chrome(doc, pno):
    """First content y on a page (below a leading chrome/title band, if any)."""
    ls = page_lines(doc, pno)
    for (y0, y1, x0, x1, t, ch) in ls:
        if not ch:
            return max(0.0, y0 - 4)
        # keep scanning past chrome only while it is in the top band
        if y0 > 120:
            return 5.0
    return 5.0


def find_totals(doc):
    """Total lines in spatial order: [{page, y0, y1, printed, marks, text}]."""
    totals = []
    for pno in range(len(doc)):
        for (y0, y1, x0, x1, txt, ch) in page_lines(doc, pno):
            m = TOT.search(txt)
            if m:
                totals.append({"page": pno, "y0": y0, "y1": y1,
                               "printed": int(m.group(1)), "marks": int(m.group(2)),
                               "text": txt.strip()})
    totals.sort(key=lambda z: (z["page"], z["y0"]))
    return totals


def assign_numbers(totals):
    """Numbering law: printed identity; non-increasing repeats/dips position-derived
    + flagged; gaps measured against the corrected previous number, kept as printed."""
    questions, gaps, typos = [], [], []
    prev_effective = 0
    for i, t in enumerate(totals):
        pos = i + 1
        if i > 0 and t["printed"] <= totals[i - 1]["printed"]:
            # source typo (non-increasing dip/repeat): derive from position, flag it
            q = {"number": pos, "printed_as": t["printed"], "number_provenance":
                 f"position-derived; printed '{t['printed']}' is a source typo "
                 f"(previous printed number is {totals[i - 1]['printed']})"}
            typos.append({"position": pos, "printed": t["printed"]})
        else:
            q = {"number": t["printed"], "number_provenance": "printed"}
            if t["printed"] > prev_effective + 1:
                gaps.extend(range(prev_effective + 1, t["printed"]))
        q["marks"] = t["marks"]
        questions.append(q)
        prev_effective = q["number"]
    return questions, gaps, typos


def crop_png(doc, page_no, rect, out_path, zoom=2.0):
    page = doc[page_no]
    pr = page.rect
    x0, y0, x1, y1 = rect
    x0 = max(0.0, min(float(x0), pr.width - 2))
    x1 = min(pr.width, max(x0 + 4, float(x1)))
    y0 = max(0.0, min(float(y0), pr.height - 2))
    y1 = min(pr.height, max(y0 + 4, float(y1)))
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=fitz.Rect(x0, y0, x1, y1), alpha=False)
    pix.save(out_path)


def solution_pages(doc, outdir):
    """Solution scans: extract the embedded scan per page; re-encode large pages."""
    paths = []
    for pno in range(len(doc)):
        out = os.path.join(outdir, f"a-p{pno+1:02d}.png")
        embedded = None
        try:
            for img in doc[pno].get_images(full=True):
                base = doc.extract_image(img[0])
                if base["image"] and len(base["image"]) > 2000:
                    embedded = base
                    break
        except Exception:
            embedded = None
        if embedded:
            im = Image.open(io.BytesIO(embedded["image"]))
            if im.mode not in ("RGB", "L"):
                im = im.convert("RGB")
            im.save(out)
            if os.path.getsize(out) > 260_000:
                jpg = out.replace(".png", ".jpg")
                im.save(jpg, quality=78)
                os.remove(out)
                out = jpg
        else:
            pix = doc[pno].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
            pix.save(out)
        paths.append(os.path.basename(out))
    return paths


def render_md_questions(topic, qs):
    yr = f"Year {topic['year']}" if topic["year"] else "A-Level"
    lines = [f"# {topic['name']} — Question Set (A-Level Maths · Edexcel · {yr} {topic['strand']})", ""]
    if topic.get("image_only"):
        lines.append("**Scanned question set (no text layer at source)** — questions are not "
                     "individually cropped; the full source pages are preserved under `assets/` "
                     "(honest gap of record, never padded).")
        lines.append("")
        for p in topic.get("source_pages", []):
            lines.append(f"![{p}](assets/{p})")
            lines.append("")
        return "\n".join(lines) + "\n"
    lines.append(f"Chapter question set · `{topic['slug']}` · {len(qs)} questions · "
                 f"segmented by printed total lines")
    lines.append("")
    for q in qs:
        marks = f"{q['marks']} marks" if q.get("marks") else "marks not printed"
        parts = f" · parts {', '.join(q['parts'])}" if q.get("parts") else ""
        flag = f" · printed as “{q['printed_as']}” (source typo)" if q.get("printed_as") else ""
        lines.append(f"## Q{q['number']} ({marks}{parts}){flag}")
        lines.append("")
        for i, c in enumerate(q["crops"]):
            lines.append(f"![Q{q['number']}{'.' + str(i+1) if len(q['crops']) > 1 else ''}]({c})")
            lines.append("")
        if q.get("text"):
            snippet = " / ".join(q["text"].splitlines())[:400]
            lines.append(f"Text (lossy): {snippet}")
            lines.append("")
    return "\n".join(lines) + "\n"


def render_md_answers(topic, ans):
    lines = [f"# {topic['name']} — Worked Solutions (A-Level Maths · Edexcel)", ""]
    if not ans.get("present"):
        lines.append(f"**No solutions published at source** — `{ans.get('note','')}`")
        return "\n".join(lines) + "\n"
    lines.append(f"Mapping: `{ans['mapping']}` · {len(ans['crops'])} page scan(s) · "
                 f"source sha256 `{ans.get('sha','')[:16]}…`")
    lines.append("")
    for c in ans["crops"]:
        lines.append(f"![{c}](assets/{c})")
        lines.append("")
    return "\n".join(lines) + "\n"


def extract_topic(t, out_root, pdf_dir, task_id):
    slug = t["slug"]
    strand = ("Pure Mathematics" if "-pure-mathematics-" in slug
              else "Statistics" if "-statistics-" in slug
              else "Mechanics" if "-mechanics-" in slug else "Pure Mathematics")
    year = 1 if slug.startswith("as-") else 2
    mnum = re.search(r"-(?:pure-mathematics|statistics|mechanics)-(\d+)-", slug)
    number = int(mnum.group(1)) if mnum else -1
    topic = {"slug": slug, "name": t["title"], "year": year, "strand": strand,
             "chapter_number": number}

    tdir = os.path.join(out_root, slug)
    adir = os.path.join(tdir, "assets")
    if os.path.isdir(tdir):
        import shutil
        shutil.rmtree(tdir)
    os.makedirs(adir, exist_ok=True)

    qs_rec = t["question_set"]
    q_url, a_url = qs_rec["q_url"], qs_rec["a_url"]
    discovery = qs_rec.get("q_discovery", "question-set page link")
    prov = {"source_page": f"https://old.mathsgenie.co.uk/{qs_rec['page']}",
            "site_topic_page": t["site_topic_page"],
            "extracted_at": NOW, "extractor": EXTRACTOR, "task_id": task_id}

    q_path = os.path.join(pdf_dir, f"al-{slug}-q.pdf")
    a_path = os.path.join(pdf_dir, f"al-{slug}-a.pdf")
    q_ok = fetch(q_url, q_path) and bool(valid_pdf(q_path))
    a_ok = fetch(a_url, a_path) and bool(valid_pdf(a_path))
    if not q_ok:
        return {"slug": slug, "status": "question-pdf-unreadable", "q_url": q_url}

    doc = fitz.open(q_path)
    totals = find_totals(doc)
    image_only = not totals

    questions, source_pages = [], []
    if image_only:
        topic["image_only"] = True
        for pno in range(len(doc)):
            out = os.path.join(adir, f"page-{pno+1:02d}.png")
            pix = doc[pno].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
            pix.save(out)
            source_pages.append(os.path.basename(out))
        topic["source_pages"] = source_pages
    else:
        qs, gaps, typos = assign_numbers(totals)
        topic["numbering_gaps"] = gaps
        topic["printed_number_typos"] = typos
        X0, X1 = 16.0, doc[0].rect.width - 16
        for i, q in enumerate(qs):
            T = totals[i]
            # start boundary: end of previous total line (or page top)
            if i == 0:
                s_page, s_y = 0, top_after_chrome(doc, 0)
            else:
                s_page, s_y = totals[i - 1]["page"], totals[i - 1]["y1"] + 5
            rects = []
            if T["page"] == s_page:
                rects.append((s_page, s_y, T["y1"] + 7))
            else:
                cb = content_bottom(doc, s_page)
                rects.append((s_page, s_y, cb))
                for mid in range(s_page + 1, T["page"]):
                    rects.append((mid, top_after_chrome(doc, mid), content_bottom(doc, mid)))
                rects.append((T["page"], top_after_chrome(doc, T["page"]), T["y1"] + 7))
            # region text: non-chrome lines inside any rect
            rtxt_lines = []
            for (rp, ry0, ry1) in rects:
                for (y0, y1, x0, x1, txt, ch) in page_lines(doc, rp):
                    if ch:
                        continue
                    if ry0 - 2 <= y0 and y1 <= ry1 + 2:
                        rtxt_lines.append((rp, y0, x0, txt))
            rtxt_lines.sort()
            rtxt = "\n".join(x[3] for x in rtxt_lines)
            # crops
            crops = []
            for j, (rp, ry0, ry1) in enumerate(rects):
                name = f"q{q['number']:02d}.png" if j == 0 else f"q{q['number']:02d}b{j}.png"
                crop_png(doc, rp, (X0, ry0, X1, ry1), os.path.join(adir, name))
                crops.append(f"assets/{name}")
            questions.append({
                "number": q["number"], "marks": q["marks"],
                "printed_as": q.get("printed_as"), "number_provenance": q["number_provenance"],
                "parts": sorted(set(PARTS_RE.findall(rtxt))),
                "text": rtxt.strip(), "pdf_page": T["page"] + 1,
                "total_line": T["text"], "crops": crops,
            })
    q_pages = len(doc)
    q_sha = sha256(q_path)
    doc.close()

    answers = {"present": False, "reason": "not-published", "mapping": None, "crops": [],
               "sha": None, "source_url": a_url}
    a_pages = None
    if a_ok:
        sdoc = fitz.open(a_path)
        a_pages = len(sdoc)
        sp = solution_pages(sdoc, adir)
        answers = {"present": True, "reason": None, "mapping": "per-page", "crops": sp,
                   "sha": sha256(a_path), "source_url": a_url, "pages": a_pages,
                   "note": ("answer-book scans are independent of the question set in this lane "
                            "(per-page mapping; no booklet-rescan cover rule applies)")}
        sdoc.close()
    elif a_url:
        answers["note"] = f"asset missing/404 at {a_url}"

    topic_json = {
        "plane": "MG-QuestionBank", "lane": "a-level-maths-edexcel",
        "qualification": "A-Level", "subject": "Maths", "board": "Edexcel", "spec": "9MA0",
        "slug": slug, "name": t["title"],
        "year": f"Year {year}", "strand": strand, "chapter_number": number,
        "site_slug": slug, "site_topic_page": t["site_topic_page"],
        "subtopics": [{"slug": s["slug"], "title": s["title"], "site_topic_page": s["site_topic_page"]}
                      for s in t.get("subtopics", [])],
        "question_source": {
            "kind": ("image-only question set (scanned)" if image_only
                     else "chapter question set (compiled exam questions)"),
            "url": q_url, "sha256": q_sha, "pages": q_pages,
            "discovery": discovery,
            "segmentation": ("none (image-only; full-page source renders)" if image_only
                             else f"total-line boundaries ({len(totals)} lines, spatial order)"),
        },
        "solutions": {"url": a_url, "sha256": answers["sha"], "pages": a_pages},
        "question_count": len(questions),
        "numbering_gaps": topic.get("numbering_gaps", []),
        "printed_number_typos": topic.get("printed_number_typos", []),
        "provenance": prov,
    }
    qs_json = {"topic": slug, "count": len(questions), "questions": questions, "provenance": prov}
    if image_only:
        qs_json["note"] = ("scanned set without a text layer: no individually anchorable questions; "
                           "content preserved as full-page source renders (assets/page-NN.png)")
    ans_json = {"topic": slug, **answers, "provenance": prov}

    with open(os.path.join(tdir, "topic.json"), "w") as f:
        json.dump(topic_json, f, indent=1)
    with open(os.path.join(tdir, "questions.json"), "w") as f:
        json.dump(qs_json, f, indent=1)
    with open(os.path.join(tdir, "answers.json"), "w") as f:
        json.dump(ans_json, f, indent=1)
    with open(os.path.join(tdir, "questions.md"), "w") as f:
        f.write(render_md_questions(topic, questions))
    with open(os.path.join(tdir, "answers.md"), "w") as f:
        f.write(render_md_answers(topic, answers))

    return {"slug": slug, "status": "ok", "questions": len(questions),
            "image_only": image_only, "answers": answers["present"],
            "marks_sum": sum(q["marks"] for q in questions),
            "typos": topic.get("printed_number_typos", []),
            "gaps": topic.get("numbering_gaps", [])}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=f"{WORK}/catalog/alevel_edexcel_catalog.json")
    ap.add_argument("--out", default=f"{WORK}/corpus/MG-QuestionBank")
    ap.add_argument("--pdfs", default=f"{WORK}/pdfs")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--slugs", default="")
    args = ap.parse_args()

    cat = json.load(open(args.catalog))
    lane = os.path.join(args.out, "a-level-maths-edexcel")
    os.makedirs(lane, exist_ok=True)
    topics = cat["topics"]
    if args.slugs:
        want = set(args.slugs.split(","))
        topics = [t for t in topics if t["slug"] in want]
    elif args.limit:
        topics = topics[: args.limit]

    results = []

    def run(t):
        try:
            return extract_topic(t, lane, args.pdfs, "T-MG-QB-3/run-001")
        except Exception as e:
            import traceback
            return {"slug": t["slug"], "status": f"error: {type(e).__name__}: {e}",
                    "trace": traceback.format_exc()[-2000:]}

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(run, t): t for t in topics}
        for fu in as_completed(futs):
            r = fu.result()
            results.append(r)
            print(f"[{len(results)}/{len(topics)}] {r['status']:<28} q={r.get('questions','-'):>3} "
                  f"ans={r.get('answers','-')} {r['slug']}", flush=True)

    # cumulative results (chunked-run safe)
    out_path = f"{WORK}/logs/qb3_extract_results.json"
    merged = {}
    if os.path.exists(out_path):
        try:
            for r in json.load(open(out_path)).get("results", []):
                merged[r["slug"]] = r
        except Exception:
            merged = {}
    for r in results:
        merged[r["slug"]] = r
    results = sorted(merged.values(), key=lambda r: r["slug"])
    os.makedirs(f"{WORK}/logs", exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({"run": "T-MG-QB-3/run-001", "finished_at": NOW, "results": results}, f, indent=1)

    ok = [r for r in results if r["status"] == "ok"]
    imgonly = [r["slug"] for r in ok if r.get("image_only")]
    bad = [r for r in results if r["status"] != "ok"]
    zero = [r["slug"] for r in ok if not r.get("image_only") and r.get("questions") == 0]
    print(f"\nDONE: {len(ok)}/{len(results)} ok | questions={sum(r.get('questions',0) for r in ok)} "
          f"| marks={sum(r.get('marks_sum',0) for r in ok)}")
    print(f"image-only ({len(imgonly)}): {imgonly}")
    print(f"zero-question text sets: {zero}")
    print(f"failures: {[(r['slug'], r['status']) for r in bad]}")


if __name__ == "__main__":
    main()
