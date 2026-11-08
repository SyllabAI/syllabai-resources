#!/usr/bin/env python3
"""T-MG-LS-2 run-001 extractor — MG-Lessons igcse-maths-edexcel.

Reads cached lessons pages, extracts the `lesson` envelope (cards: content
cards with markdown blocks + verbatim math; mcq cards with isCorrect options
+ explanation), downloads inline figure assets, and writes per-topic
lesson.json + lesson.md per the plane law (video links of record only).
"""
import json
import os
import re
import sys

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import envelope as env  # noqa: E402
import mg_common as C  # noqa: E402
import rsc  # noqa: E402

LANE = "igcse-maths-edexcel"
TASK = "T-MG-LS-2"
RUN = "run-001"
EXTRACTOR = f"mg_ls1_extract.py ({TASK} {RUN})"
CORP = f"{C.CORPUS}/MG-Lessons/{LANE}"

cat = json.load(open(f"{C.LOGS}/rgls_catalog.json"))[LANE]
LANE_DIR = cat["lane_dir"]


class ImgSink:
    def __init__(self, assets_dir):
        self.dir = assets_dir
        self.n = 0
        self.blob = os.path.join(C.CACHE, "imgs")
        os.makedirs(self.dir, exist_ok=True)
        os.makedirs(self.blob, exist_ok=True)
        self.excluded = []

    def ref_for(self, url):
        ext = os.path.splitext(url.split("?")[0])[1].lower() or ".png"
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
            self.excluded.append(url)
            return None
        self.n += 1
        name = f"{self.n:03d}-{os.path.basename(url.split('?')[0])}"
        dest = os.path.join(self.dir, name)
        if not os.path.exists(dest):
            import hashlib
            blob = os.path.join(self.blob, hashlib.sha256(url.encode()).hexdigest() + ext)
            if not os.path.exists(blob):
                data = C.http_get(url, binary=True, tries=3)
                open(blob, "wb").write(data)
                import time
                time.sleep(0.1)
            import shutil
            shutil.copyfile(blob, dest)
        return f"assets/{name}"


def extract_topic(slug):
    html_path = C.cache_path(LANE_DIR, slug, "lessons")
    html = open(html_path, encoding="utf-8", errors="ignore").read()
    payload = rsc.flight_payload(html)
    table = env.t_table(payload)
    lesson = env.find_key(payload, "lesson", table)
    if not isinstance(lesson, dict) or "cards" not in lesson:
        return None
    return html, lesson


def build_lesson(slug, lesson, tdir):
    sink = ImgSink(os.path.join(tdir, "assets"))
    steps, quiz, videos = [], [], []

    def process_content(text):
        """Download images in a content block; return body with local refs."""
        def rep(m):
            ref = sink.ref_for(m.group(2))
            if ref:
                return f"![{m.group(1)}](../{ref})"
            return ""
        return re.sub(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)", rep, text)

    for card in sorted(lesson.get("cards", []), key=lambda c: c.get("order", 0)):
        ctype = card.get("type")
        if ctype == "content":
            body_parts = []
            for b in card.get("blocks", []):
                body_parts.append(process_content(b.get("content", "")).strip())
            body = "\n\n".join(p for p in body_parts if p)
            figs = sorted(set(re.findall(r"\.\./(assets/[^\)]+)", body)))
            step = {"heading": card.get("title"), "body": body or None}
            if figs:
                step["figure_refs"] = figs
            steps.append(step)
        elif ctype == "mcq":
            quiz.append({
                "id": card.get("id"),
                "question": card.get("question"),
                "options": [{
                    "id": o.get("id"),
                    "text": o.get("text"),
                    "is_correct": bool(o.get("isCorrect")),
                } for o in card.get("options", [])],
                "explanation": card.get("explanation"),
            })
    return steps, quiz, videos, sink


def render_md(slug, grade, steps, quiz, lesson_meta):
    out = [f"# {slug} — lesson", ""]
    out += [f"_Lane: `{LANE}` · grade {grade or '—'} · "
            f"{len(steps)} content steps · {len(quiz)} check questions "
            f"(source: MathsGenie lessons)_", ""]
    for s in steps:
        if s.get("heading"):
            out += [f"## {s['heading']}", ""]
        if s.get("body"):
            out += [s["body"], ""]
    if quiz:
        out += ["## Check yourself", ""]
        for i, q in enumerate(quiz, 1):
            out += [f"{i}. {q.get('question')}", ""]
            for o in q.get("options", []):
                mark = " ✔" if o.get("is_correct") else ""
                out += [f"   - {o.get('text')}{mark}", ""]
            if q.get("explanation"):
                out += [f"   _Explanation:_ {q['explanation']}", ""]
    return "\n".join(out)


def main():
    os.makedirs(CORP, exist_ok=True)
    results = {"lane": LANE, "task": TASK, "run": RUN, "started": C.now_iso(),
               "lessons": {}, "gaps": []}
    topics = sorted(s for s, m in cat["topics"].items() if "lessons" in m["modes"])
    print(f"topics with lessons: {len(topics)}")
    for idx, slug in enumerate(topics):
        tdir = os.path.join(CORP, slug)
        os.makedirs(tdir, exist_ok=True)
        try:
            html, lesson = extract_topic(slug)
        except Exception as e:
            results["gaps"].append({"topic": slug, "reason": f"extract-error: {str(e)[:100]}"})
            print(f"  [{idx+1}/{len(topics)}] {slug}: ERROR {str(e)[:60]}")
            continue
        if not lesson:
            results["gaps"].append({"topic": slug, "reason": "no-lesson-envelope"})
            continue
        steps, quiz, videos, sink = build_lesson(slug, lesson, tdir)
        grade = C.slug_grade(slug)
        doc = {
            "topic": slug,
            "lane": LANE,
            "grade": grade,
            "tier": None,
            "steps": steps,
            "quiz": quiz,
            "videos": videos,
            "is_published": lesson.get("isPublished"),
            "source_url": f"https://www.mathsgenie.co.uk/{LANE_DIR}/{slug}/lessons",
            "source_sha256": C.sha256_str(html),
            "extracted_at": C.now_iso(),
            "extractor": EXTRACTOR,
            "task_id": TASK,
            "source_meta": {
                "lesson_id": lesson.get("id"),
                "topic_id": lesson.get("topicId"),
                "created_at": lesson.get("createdAt"),
                "updated_at": lesson.get("updatedAt"),
                "figures": sink.n,
                "grammar_note": "quiz[] is a documented amendment; steps[].figure_refs may list multiple figures",
            },
        }
        if sink.excluded:
            doc["source_meta"]["excluded_non_image_refs"] = sink.excluded
        json.dump(doc, open(os.path.join(tdir, "lesson.json"), "w"),
                  indent=1, ensure_ascii=False)
        open(os.path.join(tdir, "lesson.md"), "w").write(
            render_md(slug, grade, steps, quiz, doc["source_meta"]))
        results["lessons"][slug] = {"steps": len(steps), "quiz": len(quiz),
                                    "figures": sink.n}
        if (idx + 1) % 25 == 0:
            print(f"  {idx+1}/{len(topics)}", flush=True)
    results["finished"] = C.now_iso()
    json.dump(results, open(f"{C.LOGS}/ls2_extract_results.json", "w"), indent=1)
    tot_s = sum(m["steps"] for m in results["lessons"].values())
    tot_q = sum(m["quiz"] for m in results["lessons"].values())
    print(f"saved; lessons={len(results['lessons'])} steps={tot_s} quiz={tot_q} gaps={len(results['gaps'])}")


if __name__ == "__main__":
    main()
