#!/usr/bin/env python3
"""T-MG-RG-1 run-001 extractor — MG-RevisionGuides gcse-maths-edexcel.

Reads cached revision-guides pages, extracts the `note` envelope, parses the
faithful markdown into typed blocks (heading | paragraph | formula |
worked-example | exam-tip | mcq-set[amendment]), downloads figure assets
(numbered, images only — PDFs are never stored), and writes per-topic
revision-guide.json + revision-guide.md into the staging corpus.
"""
import json
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, "/home/z/my-project/scripts/mg_rgls_work")
import envelope as env  # noqa: E402
import mg_common as C  # noqa: E402
import rsc  # noqa: E402

LANE = "gcse-maths-edexcel"
TASK = "T-MG-RG-1"
RUN = "run-001"
EXTRACTOR = f"mg_rg1_extract.py ({TASK} {RUN})"
CORP = f"{C.CORPUS}/MG-RevisionGuides/{LANE}"

cat = json.load(open(f"{C.LOGS}/rgls_catalog.json"))[LANE]
LANE_DIR = cat["lane_dir"]
catalog_src = cat.get("catalog_source", "sitemap-derived")

# ---------------------------------------------------------------- parsing


def parse_mcq_set(block: str) -> dict:
    """Parse one <mcq-set>...</mcq-set> into a typed block."""
    items = []
    for mq in re.finditer(r"<mcq id=\"([^\"]*)\">(.*?)</mcq>", block, re.S):
        mid, body = mq.group(1), mq.group(2)

        def tag(name):
            m = re.search(rf"<{name}>(.*?)</{name}>", body, re.S)
            return re.sub(r"\s+", " ", m.group(1)).strip() if m else None

        options = []
        for om in re.finditer(r'<mcq-option(\s+correct)?\s*>(.*?)</mcq-option>', body, re.S):
            options.append({
                "text": re.sub(r"\s+", " ", om.group(2)).strip(),
                "correct": bool(om.group(1)),
            })
        items.append({
            "id": mid,
            "prompt": tag("mcq-prompt"),
            "options": options,
            "explanation": tag("mcq-explanation"),
        })
    return {"kind": "mcq-set", "items": items}


class ImgSink:
    """Downloads guide images into assets/ with provenance; PDFs refused."""

    def __init__(self, assets_dir):
        self.dir = assets_dir
        self.n = 0
        self.map = {}          # url -> assets/NNN-name
        self.excluded = []     # non-image refs (e.g. pdf) — recorded, not stored
        os.makedirs(assets_dir, exist_ok=True)
        self._blob = os.path.join(C.CACHE, "imgs")
        os.makedirs(self._blob, exist_ok=True)

    def ref_for(self, url):
        if url in self.map:
            return self.map[url]
        ext = os.path.splitext(url.split("?")[0])[1].lower() or ".png"
        if ext not in (".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"):
            self.excluded.append(url)
            return None
        self.n += 1
        base = os.path.basename(url.split("?")[0])
        name = f"{self.n:03d}-{base}"
        dest = os.path.join(self.dir, name)
        if not os.path.exists(dest):
            import hashlib
            blob = os.path.join(self._blob, hashlib.sha256(url.encode()).hexdigest() + ext)
            if not os.path.exists(blob):
                data = C.http_get(url, binary=True, tries=3)
                with open(blob, "wb") as f:
                    f.write(data)
                time.sleep(0.1)
            import shutil as _sh
            _sh.copyfile(blob, dest)
        rel = f"assets/{name}"
        self.map[url] = rel
        return rel


def sub_images(text, sink):
    """Replace ![](url) with [](#fig) markers returning figure list."""
    figs = []

    def rep(m):
        ref = sink.ref_for(m.group(2))
        if ref:
            figs.append({"alt": m.group(1), "figure_ref": ref})
            return f"\x00FIG:{ref}\x00"
        return ""

    return re.sub(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)", rep, text), figs


def flush_paragraph(buf, sink, blocks):
    """Turn a plain-text chunk into paragraph/formula/figure blocks."""
    text = buf.strip()
    if not text:
        return
    text, figs = sub_images(text, sink)
    alt_by_ref = {f["figure_ref"]: f["alt"] for f in figs}
    for p in [q.strip() for q in re.split(r"\n\s*\n", text) if q.strip()]:
        segs = re.split(r"\x00FIG:([^\x00]*)\x00", p)
        lead = segs[0].strip()
        if lead:
            _push_text_block(lead, blocks)
        for k in range(1, len(segs), 2):
            ref = segs[k]
            nxt = (segs[k + 1] if k + 1 < len(segs) else "").replace("\x00", "").strip()
            blocks.append({"kind": "figure", "figure_ref": ref,
                           "alt": alt_by_ref.get(ref, "")})
            if nxt:
                _push_text_block(nxt, blocks)


def _push_text_block(text, blocks):
    t = text.strip()
    if not t or re.fullmatch(r"-{3,}|\x00", t):
        return
    # pure display-math -> formula block
    m = re.fullmatch(r"\$\$(.+)\$\$", t, re.S)
    if m:
        blocks.append({"kind": "formula", "math": m.group(1).strip(),
                       "math_format": "latex"})
        return
    # bold-only line -> heading
    if re.fullmatch(r"\*\*[^*]+\*\*", t) and "\n" not in t:
        blocks.append({"kind": "heading", "text": t.strip("*").strip()})
        return
    # tip patterns -> exam-tip
    if re.match(r"^(?:\*\*)?tip\b", t, re.I):
        t = re.sub(r"^\*\*Tip:?\*\*\s*", "", t, flags=re.I)
        t = re.sub(r"^Tip:?\s*", "", t, flags=re.I)
        blocks.append({"kind": "exam-tip", "text": t})
        return
    blocks.append({"kind": "paragraph", "text": t})


def parse_section(sec, sink, blocks):
    """One ---delimited section into blocks (examples may start mid-section)."""
    sec = sec.strip()
    if not sec:
        return
    pieces = re.split(r"(?=\*\*Example\s*\d+)", sec)
    for piece in pieces:
        piece = piece.strip()
        if not piece:
            continue
        em = re.match(r"\*\*Example\s*(\d+[^*]*?)\*\*", piece, re.S)
        if not em:
            flush_paragraph(piece, sink, blocks)
            continue
        title = re.sub(r"\s+", " ", "Example " + em.group(1)).strip().strip(":")
        rest = piece[em.end():].strip()
        step_parts = re.split(r"\*\*(Step\s*\d+)[:.]?\*\*\s*", rest)
        steps = []
        pre = step_parts[0].strip()
        if pre:
            pre, figs = sub_images(pre, sink)
            lead = re.sub(r"\x00FIG:([^\x00]*)\x00", "", pre).replace("\x00", "").strip()
            if lead:
                steps.append({"heading": None, "body": lead, "figure_refs": []})
        for k in range(1, len(step_parts), 2):
            shead = step_parts[k].strip()
            sbody = step_parts[k + 1] if k + 1 < len(step_parts) else ""
            sbody, figs = sub_images(sbody, sink)
            body = re.sub(r"\x00FIG:([^\x00]*)\x00", "", sbody).replace("\x00", "").strip()
            body = re.sub(r"[ \t]+\n", "\n", body).strip()
            steps.append({"heading": shead, "body": body or None,
                          "figure_refs": [f["figure_ref"] for f in figs]})
        blocks.append({"kind": "worked-example", "title": title, "steps": steps})


def parse_guide_ordered(md, sink):
    """Order-preserving parse: walk the markdown once."""
    blocks, videos = [], []
    md = re.sub(r"<iframe[^>]*>.*?</iframe>",
                lambda m: videos.append(re.search(r'src=\"([^\"]+)\"', m.group(0)).group(1)) or "\n\n",
                md, flags=re.S)
    pieces = re.split(r"(<mcq-set>.*?</mcq-set>)", md, flags=re.S)
    chunks = []  # (type, text) preserving order; mcq appended at its position
    for p in pieces:
        if p.strip().startswith("<mcq-set>"):
            chunks.append(("mcq", p))
        else:
            chunks.append(("md", p))
    # parse md sections into blocks, mcq into mcq-set blocks, in order
    for typ, text in chunks:
        if typ == "mcq":
            blocks.append(parse_mcq_set(text))
        else:
            for sec in re.split(r"\n+---\n+", text):
                parse_section(sec, sink, blocks)
    return blocks, videos


# ---------------------------------------------------------------- main

def main():
    os.makedirs(CORP, exist_ok=True)
    results = {"lane": LANE, "task": TASK, "run": RUN, "started": C.now_iso(),
               "guides": {}, "gaps": [], "exclusions": []}
    topics = [s for s, m in cat["topics"].items() if "revision-guides" in m["modes"]]
    print(f"topics with revision-guides: {len(topics)}")

    for idx, slug in enumerate(sorted(topics)):
        tdir = os.path.join(CORP, slug)
        os.makedirs(tdir, exist_ok=True)
        html_path = C.cache_path(LANE_DIR, slug, "revision-guides")
        html = open(html_path, encoding="utf-8", errors="ignore").read()
        payload = rsc.flight_payload(html)
        table = env.t_table(payload)
        note = env.find_key(payload, "note", table)
        if not isinstance(note, dict) or not note.get("markdown"):
            results["gaps"].append({"topic": slug, "reason": "note-envelope-missing"})
            print(f"  [{idx+1}/{len(topics)}] {slug}: GAP note-missing")
            continue
        md = note["markdown"]
        sink = ImgSink(os.path.join(tdir, "assets"))
        blocks, videos = parse_guide_ordered(md, sink)
        n_fig = sink.n
        guide = {
            "topic": slug,
            "lane": LANE,
            "grade": C.slug_grade(slug),
            "tier": None,
            "title": note.get("title"),
            "summary": note.get("summary"),
            "blocks": blocks,
            "videos": [{"embed_url": v} for v in videos],
            "source_url": f"https://www.mathsgenie.co.uk/{C.LANES[LANE]}/{slug}/revision-guides",
            "source_sha256": C.sha256_str(html),
            "extracted_at": C.now_iso(),
            "extractor": EXTRACTOR,
            "task_id": TASK,
            "source_meta": {
                "note_id": note.get("id"),
                "upstream_source_url": note.get("sourceUrl"),
                "published_at": note.get("publishedAt"),
                "updated_at": note.get("updatedAt"),
                "figure_count": n_fig,
                "block_counts": {},
            },
        }
        for b in blocks:
            guide["source_meta"]["block_counts"][b["kind"]] = \
                guide["source_meta"]["block_counts"].get(b["kind"], 0) + 1
        if sink.excluded:
            guide["source_meta"]["excluded_non_image_refs"] = sink.excluded
            results["exclusions"] += [{"topic": slug, "url": u} for u in sink.excluded]
        json.dump(guide, open(os.path.join(tdir, "revision-guide.json"), "w"),
                  indent=1, ensure_ascii=False)
        # md render
        open(os.path.join(tdir, "revision-guide.md"), "w").write(
            render_md(guide))
        results["guides"][slug] = {
            "title": note.get("title"), "blocks": len(blocks),
            "figures": n_fig, "mcq_sets": guide["source_meta"]["block_counts"].get("mcq-set", 0),
            "worked_examples": guide["source_meta"]["block_counts"].get("worked-example", 0),
        }
        print(f"  [{idx+1}/{len(topics)}] {slug}: {len(blocks)} blocks, {n_fig} figs")

    results["finished"] = C.now_iso()
    json.dump(results, open(f"{C.LOGS}/rg1_extract_results.json", "w"), indent=1)
    print("saved results;", len(results["guides"]), "guides,", len(results["gaps"]), "gaps")


def render_md(g):
    out = [f"# {g.get('title') or g['topic']}", ""]
    if g.get("summary"):
        out += [g["summary"], ""]
    for b in g["blocks"]:
        k = b["kind"]
        if k == "heading":
            out += [f"## {b['text']}", ""]
        elif k == "paragraph":
            out += [b["text"], ""]
        elif k == "formula":
            out += [f"$${b['math']}$$", ""]
        elif k == "figure":
            out += [f"![{b.get('alt','')}](../{b['figure_ref']})", ""]
        elif k == "exam-tip":
            out += [f"> **Exam tip.** {b['text']}", ""]
        elif k == "worked-example":
            out += [f"**{b['title']}**", ""]
            for s in b["steps"]:
                if s.get("heading"):
                    out += [f"**{s['heading']}**", ""]
                if s.get("body"):
                    out += [s["body"], ""]
                for fr in s.get("figure_refs", []):
                    out += [f"![](../{fr})", ""]
            out += [""]
        elif k == "mcq-set":
            out += ["**Practice questions**", ""]
            for i, it in enumerate(b["items"], 1):
                out += [f"{i}. {it['prompt']}", ""]
                for o in it["options"]:
                    mark = " ✔" if o["correct"] else ""
                    out += [f"   - {o['text']}{mark}", ""]
                if it.get("explanation"):
                    out += [f"   _Explanation:_ {it['explanation']}", ""]
            out += [""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
