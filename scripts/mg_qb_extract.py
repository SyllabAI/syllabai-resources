#!/usr/bin/env python3
"""T-MG-QB-1 run-001 — MathsGenie GCSE Maths (Edexcel) per-topic question-bank extractor.

Reads the catalog JSON (fetch_catalog.py), downloads ws/booklet/solutions PDFs,
splits questions (2-column aware, sequential-number anchors), renders crops,
writes the MG-QuestionBank lane corpus + extraction log.

PDFs are validated then discarded after processing; sha256 + URLs recorded.
"""
import argparse, hashlib, json, os, re, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

import fitz
from PIL import Image
import io

EXTRACTOR = "mg_qb_extract.py v1 (T-MG-QB-1 run-001)"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

WORK = "/home/z/my-project/mg_work"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def fetch(url, dest):
    """Download with curl -f; returns True on success."""
    if os.path.exists(dest) and os.path.getsize(dest) > 800:
        return True
    for attempt in range(3):
        r = subprocess.run(["curl", "-sf", "-A", "Mozilla/5.0 (X11; Linux x86_64)", "--max-time", "90",
                            "-o", dest, url], capture_output=True)
        if r.returncode == 0 and os.path.getsize(dest) > 800:
            return True
        time.sleep(1.5 * (attempt + 1))
    if os.path.exists(dest):
        os.remove(dest)
    return False


def valid_pdf(path):
    """Open + reject MathsGenie asset-404 error PDFs."""
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


def is_2col(page, blocks):
    return page.rect.width > 700


def column_split(page, text_blocks):
    """Return (columns, col_x_ranges). Columns = left then right when 2-col layout detected."""
    w = page.rect.width
    if is_2col(page, text_blocks):
        xs = [b["bbox"][0] for b in text_blocks]
        rights = [x for x in xs if x > w * 0.45]
        lefts = [x for x in xs if x <= w * 0.45]
        if rights and lefts:
            mid = (max(lefts) + min(rights)) / 2 if max(lefts) < min(rights) else w / 2
            return 2, [(20, mid - 4), (mid - 4, w - 15)]
    return 1, [(20, w - 15)]


NUM_RE = re.compile(r"^(\d{1,2})\s*[\.\)]?\s+(\D.*)$|^(\d{1,2})\s*$", re.S)


def anchor_number(txt):
    """Question-number anchor: block starts with expected-style number followed by non-digit."""
    t = txt.strip()
    m = re.match(r"^(\d{1,2})(?:\s+([^\d].*)|\s*$|\.\s|\)\s)", t, re.S)
    if m:
        return int(m.group(1))
    return None


def block_text(b):
    """Readable text of a PyMuPDF block: spans space-joined when alnum boundaries collide, lines newline-joined."""
    lines = []
    for l in b["lines"]:
        out = ""
        for s in l["spans"]:
            p = s["text"]
            if out and p and not out[-1].isspace() and not p[0].isspace() and out[-1].isalnum() and p[0].isalnum():
                out += " "
            out += p
        lines.append(out)
    return "\n".join(lines)


def parse_questions(doc, log):
    """Split ws/booklet PDF into questions. Returns list of dicts."""
    questions = []
    expected = 1
    prev_open_ended = False  # previous question ran to page bottom
    for pno in range(len(doc)):
        page = doc[pno]
        d = page.get_text("dict")
        tb = [b for b in d["blocks"] if b["type"] == 0]
        ib = [b for b in d["blocks"] if b["type"] == 1]
        if not tb and not ib:
            continue
        ncols, ranges = column_split(page, tb)
        for ci in range(ncols):
            x0c, x1c = ranges[ci]
            cb = [b for b in tb if x0c - 2 <= (b["bbox"][0] + b["bbox"][2]) / 2 < x1c]
            cb.sort(key=lambda b: (b["bbox"][1], b["bbox"][0]))
            ci_blocks = [b for b in ib if x0c - 2 <= (b["bbox"][0] + b["bbox"][2]) / 2 < x1c]
            # header/footer bands: mathsgenie.co.uk, Grade lines, "Please do not write..."
            def is_chrome(b):
                t = block_text(b).strip().lower()
                return ("mathsgenie.co.uk" in t or "do not write" in t
                        or t.startswith("grade") or t.startswith("gcse (1"))
            cb = [b for b in cb if not is_chrome(b)]
            if not cb and not ci_blocks:
                continue
            # effective crop bounds hug actual content (marks blocks straddle the column split)
            all_col = cb + ci_blocks
            eff_x0 = min(b["bbox"][0] for b in all_col) - 6
            eff_x1 = max([b["bbox"][2] for b in all_col] + [x1c]) + 4
            # continuation segment from page top (previous question continued)
            anchors = []
            for b in cb:
                txt = block_text(b)
                n = anchor_number(txt)
                if n is not None:
                    anchors.append((n, b, txt))
            col_top = min((b["bbox"][1] for b in cb), default=None)
            col_bottom = max((b["bbox"][3] for b in cb), default=page.rect.height)
            col_img_bottom = max((b["bbox"][3] for b in ci_blocks), default=0)
            col_bottom = max(col_bottom, col_img_bottom)

            if prev_open_ended and questions:
                # content above the first anchor in this column continues previous question
                first_anchor_y = min((b["bbox"][1] for _, b, _ in anchors), default=col_bottom + 1)
                seg_bottom = min(first_anchor_y, col_bottom)
                if seg_bottom > col_top + 4:
                    questions[-1]["extra_pages"].append({
                        "page": pno, "y0": round(col_top), "y1": round(seg_bottom), "x0": round(eff_x0), "x1": round(eff_x1)})
                    prev_open_ended = False

            for idx, (n, b, txt) in enumerate(anchors):
                if n != expected:
                    log and log.append(f"page {pno} col {ci}: anchor {n} != expected {expected} -> skipped")
                    continue
                y0 = b["bbox"][1]
                nxt = anchors[idx + 1][1]["bbox"][1] if idx + 1 < len(anchors) else None
                y1 = nxt - 4 if nxt else col_bottom
                # region text
                rtxt_blocks = [bb for bb in cb if y0 - 2 <= bb["bbox"][1] < y1]
                rtxt = "\n".join(block_text(bb)
                                 for bb in sorted(rtxt_blocks, key=lambda z: (z["bbox"][1], z["bbox"][0])))
                marks = sum(int(m) for m in re.findall(r"\((\d+)\s*marks?\)", rtxt, re.I))
                parts = re.findall(r"^\s*\(([a-h])\)", rtxt, re.M)
                questions.append({
                    "number": n, "marks": marks or None, "parts": parts,
                    "text": rtxt.strip(), "pdf_page": pno + 1,
                    "bbox": [round(eff_x0), round(y0 - 3), round(eff_x1), round(y1)],
                    "extra_pages": [],
                })
                expected += 1
                prev_open_ended = nxt is None
    return questions


def crop_png(doc, page_no, rect, out_path, zoom=2.0):
    page = doc[page_no]
    pr = page.rect
    x0, y0, x1, y1 = rect
    x0 = max(0.0, min(float(x0), pr.width - 2))
    x1 = min(pr.width, max(x0 + 4, float(x1)))
    y0 = max(0.0, min(float(y0), pr.height - 2))
    y1 = min(pr.height, max(y0 + 4, float(y1)))
    mat = fitz.Matrix(zoom, zoom)
    pix = page.get_pixmap(matrix=mat, clip=fitz.Rect(x0, y0, x1, y1), alpha=False)
    pix.save(out_path)


def solution_pages(doc, outdir, skip_pages=frozenset()):
    """Solutions PDFs are scanned image pages: extract the embedded image per page."""
    paths = []
    for pno in range(len(doc)):
        if pno in skip_pages:
            continue
        out = os.path.join(outdir, f"a-p{pno+1:02d}.png")
        embedded = None
        try:
            for img in doc[pno].get_images(full=True):
                xref = img[0]
                base = doc.extract_image(xref)
                if base["image"] and len(base["image"]) > 2000:
                    embedded = base
                    break
        except Exception:
            embedded = None
        if embedded:
            im = Image.open(io.BytesIO(embedded["image"]))
            if im.mode not in ("RGB", "L"):
                im = im.convert("RGB")
            # keep PNG if small, else re-encode JPEG for size
            tmp_png = out
            im.save(tmp_png)
            if os.path.getsize(tmp_png) > 260_000:
                jpg = out.replace(".png", ".jpg")
                im.save(jpg, quality=78)
                os.remove(tmp_png)
                out = jpg
            paths.append(os.path.basename(out))
        else:
            pix = doc[pno].get_pixmap(matrix=fitz.Matrix(1.6, 1.6), alpha=False)
            pix.save(out)
            paths.append(os.path.basename(out))
    return paths


def render_md_questions(topic, qs):
    lines = [f"# {topic['name']} — Exam Questions (GCSE Maths · Edexcel · Grade {topic['grade_band']})",
             "",
             f"Topic code `{topic['code']}` · slug `{topic['site_slug']}` · source sheet sha256 `{topic.get('ws_sha', topic.get('booklet_sha',''))[:16]}…`",
             ""]
    for q in qs:
        marks = f"{q['marks']} marks" if q["marks"] else "marks not printed"
        parts = f" · parts {', '.join(q['parts'])}" if q["parts"] else ""
        lines.append(f"## Q{q['number']} ({marks}{parts})")
        lines.append("")
        for i, c in enumerate(q["crops"]):
            lines.append(f"![Q{q['number']}{'.'+str(i+1) if len(q['crops'])>1 else ''}]({c})")
            lines.append("")
        if q.get("text"):
            snippet = " / ".join(q["text"].splitlines())[:400]
            lines.append(f"Text (lossy): {snippet}")
            lines.append("")
    return "\n".join(lines) + "\n"


def render_md_answers(topic, ans):
    lines = [f"# {topic['name']} — Worked Solutions (GCSE Maths · Edexcel · Grade {topic['grade_band']})", ""]
    if not ans.get("present"):
        lines.append(f"**No solutions published at source** — `{ans.get('note','')}`")
        return "\n".join(lines) + "\n"
    lines.append(f"Mapping: `{ans['mapping']}` · {len(ans['crops'])} image(s) · source sha256 `{ans.get('sha','')[:16]}…`")
    lines.append("")
    for c in ans["crops"]:
        lines.append(f"![{c}](assets/{c})")
        lines.append("")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--catalog", default=f"{WORK}/catalog/gcse_edexcel_catalog.json")
    ap.add_argument("--out", default=f"{WORK}/corpus/MG-QuestionBank")
    ap.add_argument("--pdfs", default=f"{WORK}/pdfs")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--codes", default="")
    args = ap.parse_args()

    cat = json.load(open(args.catalog))
    lane = os.path.join(args.out, "gcse-maths-edexcel")
    os.makedirs(lane, exist_ok=True)
    log = []

    topics = cat["topics"]
    if args.codes:
        want = set(args.codes.split(","))
        topics = [t for t in topics if t["code"] in want]
    else:
        topics = topics[: args.limit or None]
    results = []

    def process(t):
        try:
            return _process_body(t)
        except Exception as e:
            return {"code": t["code"], "slug": t["site_slug"], "name": t["name"],
                    "status": f"error: {type(e).__name__}: {e}"}

    def _process_body(t):
        res = {"code": t["code"], "slug": t["site_slug"], "name": t["name"], "status": "ok"}
        tdir = os.path.join(lane, t["site_slug"])
        adir = os.path.join(tdir, "assets")
        if os.path.isdir(tdir):
            import shutil
            shutil.rmtree(tdir)
        os.makedirs(adir, exist_ok=True)
        prov = {"source_page": t["source_page"], "site_topic_page": f"{cat['site_lane']}/{t['site_slug']}",
                "extracted_at": NOW, "extractor": EXTRACTOR, "task_id": "T-MG-QB-1/run-001"}

        ws_ok = book_ok = sol_ok = False
        ws_doc = book_doc = sol_doc = None
        ws_path = book_path = sol_path = None
        if t["questions_ws_url"]:
            ws_path = os.path.join(args.pdfs, f"{t['code']}-ws.pdf")
            ws_ok = fetch(t["questions_ws_url"], ws_path) and bool(valid_pdf(ws_path))
        if t["booklet_url"]:
            book_path = os.path.join(args.pdfs, f"{t['code']}.pdf")
            book_ok = fetch(t["booklet_url"], book_path) and bool(valid_pdf(book_path))
        if t["solutions_url"]:
            sol_path = os.path.join(args.pdfs, f"{t['code']}ans.pdf")
            sol_ok = fetch(t["solutions_url"], sol_path) and bool(valid_pdf(sol_path))

        if not ws_ok and not book_ok:
            res["status"] = "no-question-source"
            return res
        doc = (ws_doc := valid_pdf(ws_path)) if ws_ok else None
        src_pdf_url = t["questions_ws_url"]
        if not ws_ok:
            doc = valid_pdf(book_path)
            src_pdf_url = t["booklet_url"]
        if doc is None:
            res["status"] = "pdf-unreadable"
            return res

        qs = parse_questions(doc, log)
        src_kind = "ws-sheet" if ws_ok else "booklet"
        src_pdf_url = t["questions_ws_url"] if ws_ok else t["booklet_url"]
        if ws_ok and len(qs) < 2 and book_ok:
            # image-only ws generation (questions inside page images, no text anchors):
            # fall back to the booklet, which carries text anchors
            bdoc = valid_pdf(book_path)
            if bdoc is not None:
                bqs = parse_questions(bdoc, log)
                if len(bqs) > len(qs):
                    qs = bqs
                    doc = bdoc
                    src_kind = "booklet-fallback (ws has no text anchors)"
                    src_pdf_url = t["booklet_url"]
                    ws_ok = False
                    res["booklet_fallback"] = True
        src_sha = sha256(ws_path if ws_ok else book_path)
        book_sha = sha256(book_path) if book_ok else None
        for q in qs:
            crops = []
            pno = q["pdf_page"] - 1
            cp = os.path.join(adir, f"q{q['number']:02d}.png")
            crop_png(doc, pno, q["bbox"], cp)
            crops.append(f"assets/q{q['number']:02d}.png")
            for j, extra in enumerate(q["extra_pages"]):
                cp2 = os.path.join(adir, f"q{q['number']:02d}b{j+1}.png")
                crop_png(doc, extra["page"], (extra["x0"], extra["y0"], extra["x1"], extra["y1"]), cp2)
                crops.append(f"assets/q{q['number']:02d}b{j+1}.png")
            q["crops"] = crops
            for k in ("bbox", "extra_pages"):
                q.pop(k, None)

        answers = {"present": False, "reason": "not-published", "mapping": None, "crops": [], "sha": None,
                   "source_url": t["solutions_url"]}
        if sol_ok:
            sdoc = valid_pdf(sol_path)
            skip_pages = set()
            note = None
            # ans PDFs of the booklet generation are the booklet scanned with solutions:
            # when page counts match, page 1 is the booklet cover — drop it
            if book_ok and len(sdoc) == len(valid_pdf(book_path)):
                skip_pages = {0}
                note = "page 1 dropped: booklet cover scan (ans = booklet with solutions)"
            sp = solution_pages(sdoc, adir, skip_pages)
            answers = {"present": True, "reason": None, "mapping": "per-page",
                       "crops": sp, "sha": sha256(sol_path), "source_url": t["solutions_url"],
                       "pages": len(sdoc), "note": note}
        elif t["solutions_url"]:
            answers["note"] = f"asset missing/404 at {t['solutions_url']}"

        topic_json = {
            "plane": "MG-QuestionBank", "lane": "gcse-maths-edexcel",
            "qualification": "GCSE", "subject": "Maths", "board": "Edexcel",
            "slug": t["site_slug"], "name": t["name"], "code": t["code"],
            "grade_band": t["grade_band"], "grade": t["grade"], "ordinal": t["ordinal"],
            "question_source": {"kind": src_kind, "url": src_pdf_url, "sha256": src_sha},
            "booklet": {"url": t["booklet_url"], "sha256": sha256(book_path) if book_ok else None} if t["booklet_url"] else None,
            "question_count": len(qs),
            "provenance": prov,
        }
        qs_json = {"topic": t["site_slug"], "count": len(qs), "questions": qs, "provenance": prov}
        ans_json = {"topic": t["site_slug"], **answers, "provenance": prov}

        with open(os.path.join(tdir, "topic.json"), "w") as f:
            json.dump(topic_json, f, indent=1)
        with open(os.path.join(tdir, "questions.json"), "w") as f:
            json.dump(qs_json, f, indent=1)
        with open(os.path.join(tdir, "answers.json"), "w") as f:
            json.dump(ans_json, f, indent=1)
        with open(os.path.join(tdir, "questions.md"), "w") as f:
            f.write(render_md_questions({**t, "ws_sha": src_sha}, qs))
        with open(os.path.join(tdir, "answers.md"), "w") as f:
            f.write(render_md_answers(t, answers))

        res.update({"questions": len(qs), "answers": answers["present"]})
        return res

    with ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(process, t): t for t in topics}
        for fu in as_completed(futs):
            r = fu.result()
            results.append(r)
            print(f"[{len(results)}/{len(topics)}] {r['code']:>5} {r['status']:<20} "
                  f"q={r.get('questions','-'):>3} ans={r.get('answers','-')} {r['slug']}")

    results.sort(key=lambda r: r["code"])
    with open(f"{WORK}/logs/qb_extract_results.json", "w") as f:
        json.dump({"run": "T-MG-QB-1/run-001", "finished_at": NOW, "results": results, "log": log}, f, indent=1)

    ok = [r for r in results if r["status"] == "ok"]
    zero = [r["code"] for r in ok if r.get("questions") == 0]
    bad = [r for r in results if r["status"] != "ok"]
    print(f"\nDONE: {len(ok)} ok / {len(results)}; zero-question topics: {zero}; failures: {[ (r['code'], r['status']) for r in bad ]}")


if __name__ == "__main__":
    main()
