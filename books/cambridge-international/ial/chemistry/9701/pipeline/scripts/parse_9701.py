#!/usr/bin/env python3
"""parse_9701.py — chunker for CIE 9701 Coursebook 3rd ed (text-layer lane).

Input: data/9701/text_pages/page_*.json (extract_9701.py output)
Output: download/rag_9701/cie_a_level_chemistry_9701_chunks_v1.jsonl

Segmentation: stream blocks page by page; flush segment on chapter / section /
content-type change. Paragraphs via y-gap heuristic (dy>16pt -> blank line,
dy>7pt -> space join). De-hyphenation at segment joins. Packing 350-1600,
hard max 2400, sentence-boundary splits. Junk: standalone 'images' alt-text.
"""
import json, os, re, sys, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9701 import (chapter_ranges, BOOK_TITLE, AUTHOR, SECTION_RE,
                                 PSECTION_RE)

IN = "/home/z/my-project/data/9701/text_pages"
OUT_DIR = "/home/z/my-project/download/rag_9701"
PREFIX = "c9701"
TARGET_MIN, TARGET_MAX, HARD_MAX = 350, 1600, 2400

ALLCAPS_MARKERS = {
    "LEARNING INTENTIONS": "learning_objectives",
    "BEFORE YOU START": "before_you_start",
    "WORKED EXAMPLE": "worked_example",
    "ACTIVITY": "activity",
    "REFLECTION": "reflection",
    "KEY POINTS": "key_points",
    "EXAM-STYLE QUESTIONS": "chapter_questions",
    "SUMMARY": "summary",
    "SELF-EVALUATION": "self_evaluation",
    "SCIENCE IN CONTEXT": "science_in_context",
    "STUDY TIP": "tip",
    "TIP": "tip",
    "EXTENSION": "extension_work",
    "LINK": "cross_link",
}
SOFT_MARKERS = [
    ("Science in context", "science_in_context"),
    ("Study tip", "tip"),
    ("Questions for discussion", "activity"),
]
# markers that END a previous box (heading-like, their own type)
RESET_TO_BODY = set()
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(‟\"'])")


def classify_marker(text):
    t = text.strip()
    if t in ALLCAPS_MARKERS:
        return ALLCAPS_MARKERS[t]
    for pat, ct in SOFT_MARKERS:
        if t.startswith(pat) and len(t) < len(pat) + 4:
            return ct
    return None


def is_section_heading(text, size, bold):
    t = text.strip()
    if SECTION_RE.match(t) or PSECTION_RE.match(t):
        return size >= 9.5
    return False


def is_soft_heading(text, size, bold):
    """Unnumbered display headings (bold, >=9.6pt, short, no terminal punct)."""
    t = text.strip()
    if not bold or size < 9.6 or len(t) > 60:
        return False
    if t.endswith(('.', '?', '!', ',', ';', ':')):
        return False
    return not t.startswith(('[', 'Figure', 'Table', '1 ', '2 ', '3 '))


def para_join(prev, cur, dy):
    if prev is None:
        return cur
    if dy > 16:
        sep = "\n\n"
    elif dy > 7:
        sep = "\n"
    else:
        sep = " "
    return prev + sep + cur


def dehyph(a, b):
    """merge line-wrap hyphen: 'oxi-' + 'dation' -> 'oxidation'."""
    if a.endswith("-") and len(a) > 2 and a[-2].islower() and b[:1].islower():
        return a[:-1] + b
    return a + " " + b


def flush_segment(segs, chapter, section, ctype, text, pstart, pend):
    if text and len(text.strip()) > 0:
        segs.append({"chapter": chapter, "section": section, "ctype": ctype,
                     "text": text.strip(), "pstart": pstart, "pend": pend})


def build_segments():
    ranges = chapter_ranges()
    page2chap = {}
    for s, e, m in ranges:
        for p in range(s, e + 1):
            page2chap[p] = m
    segs = []
    cur = None      # running segment dict
    cur_dy = None   # pending dy for next join
    for pf in sorted(glob.glob(os.path.join(IN, "page_*.json"))):
        d = json.load(open(pf))
        pno = d["pdf"]
        chap = page2chap.get(pno)
        if chap is None:
            continue
        prev_y = None
        for b in d["blocks"]:
            t = b["text"].strip()
            if not t or t == "images":
                continue
            y = b["y"]
            dy = (y - prev_y) if prev_y is not None else 999
            prev_y = y
            mk = classify_marker(t)
            soft = (not mk) and is_soft_heading(t, b["size"], b["bold"])
            sec = t if is_section_heading(t, b["size"], b["bold"]) else None
            if mk or sec or soft:
                if cur:
                    flush_segment(segs, **_args(cur))
                    cur = None
            if soft:
                cur = {"chapter": chap, "section": None, "ctype": "body",
                       "text": t, "pstart": pno, "pend": pno}
                cur_dy = None
                continue
            if sec:
                cur = {"chapter": chap, "section": sec, "ctype": "body",
                       "text": t, "pstart": pno, "pend": pno}
                cur_dy = None
                continue
            if mk:
                cur = {"chapter": chap, "section": None, "ctype": mk,
                       "text": t, "pstart": pno, "pend": pno}
                cur_dy = None
                continue
            if cur is None:
                cur = {"chapter": chap, "section": None, "ctype": "body",
                       "text": t, "pstart": pno, "pend": pno}
            else:
                if cur_dy is not None and cur_dy > 16:
                    cur["text"] += "\n\n" + t
                else:
                    cur["text"] = dehyph(cur["text"], t)
                cur["pend"] = pno
                # bound runaway segments at a paragraph boundary
                if len(cur["text"]) > 1800 and cur_dy is not None and cur_dy > 16:
                    flush_segment(segs, **_args(cur))
                    cur = {"chapter": chap, "section": None, "ctype": cur["ctype"],
                           "text": "", "pstart": pno, "pend": pno}
            cur_dy = dy
        # page end: flush on chapter boundary only (text flows across pages)
        if cur and page2chap.get(pno + 1) is not chap:
            flush_segment(segs, **_args(cur))
            cur = None
            cur_dy = None
    if cur:
        flush_segment(segs, **_args(cur))
    return segs


def _args(c):
    return {"chapter": c["chapter"], "section": c["section"], "ctype": c["ctype"],
            "text": c["text"], "pstart": c["pstart"], "pend": c["pend"]}




def pack(segs):
    """segment -> chunks (350-1600 target, 2400 hard max)."""
    # merge 'Chapter N\n\nTitle' title slivers into the FOLLOWING segment
    cleaned = []
    hold = None
    for s in segs:
        t = s["text"]
        if hold is not None:
            s = {**s, "text": hold["text"] + "\n\n" + t if t else hold["text"]}
            hold = None
        if re.fullmatch(r"Chapter \d{1,2}\s*\n\n[\s\S]{3,70}", t) and s["ctype"] == "body":
            hold = s
            continue
        cleaned.append(s)
    if hold is not None:
        cleaned.append(hold)
    segs = cleaned
    chunks = []
    for s in segs:
        text = s["text"]
        # paragraph-normalize
        parts, cur = [], ""
        for para in text.split("\n\n"):
            para = re.sub(r"\s*\n\s*", " ", para).strip()
            if not para:
                continue
            if cur:
                cur += "\n\n" + para
            else:
                cur = para
            while len(cur) > HARD_MAX:
                cut = cur.rfind("\n\n", 0, HARD_MAX)
                if cut < TARGET_MIN:
                    ms = list(SENT_SPLIT.finditer(cur[:HARD_MAX]))
                    cut = ms[-1].start() if ms else HARD_MAX
                parts.append(cur[:cut].strip())
                cur = cur[cut:].strip()
        if cur:
            parts.append(cur)
        for p in parts:
            chunks.append({**s, "text": p})
    # merge undersized into neighbours with same (chapter, section, ctype)
    merged = []
    for c in chunks:
        tiny = len(c["text"]) < 80
        if merged and ((tiny and len(merged[-1]["text"]) + len(c["text"]) + 2 <= TARGET_MAX
                        and merged[-1]["chapter"] is c["chapter"]
                        and merged[-1]["ctype"] == c["ctype"]
                        and c["pstart"] - merged[-1]["pend"] <= 1)
                       or (len(c["text"]) < TARGET_MIN and len(merged[-1]["text"]) + len(c["text"]) + 2 <= TARGET_MAX
                           and merged[-1]["chapter"] is c["chapter"] and merged[-1]["section"] == c["section"]
                           and merged[-1]["ctype"] == c["ctype"] and c["pstart"] - merged[-1]["pend"] <= 1)):
            m = merged[-1]
            m["text"] += "\n\n" + c["text"]
            m["pend"] = c["pend"]
        else:
            merged.append(dict(c))
    # split remaining oversize (paranoid; pack() already split)
    out = []
    for c in merged:
        if len(c["text"]) <= HARD_MAX:
            out.append(c)
            continue
        cur = ""
        for para in c["text"].split("\n\n"):
            cand = (cur + "\n\n" + para) if cur else para
            if len(cand) > HARD_MAX and cur:
                out.append({**c, "text": cur})
                cur = para
            else:
                cur = cand
        if cur:
            out.append({**c, "text": cur})
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    segs = build_segments()
    print(f"segments: {len(segs)}")
    chunks = pack(segs)
    print(f"chunks (pre-id): {len(chunks)}")
    # id assignment + schema
    out_path = os.path.join(OUT_DIR, "cie_a_level_chemistry_9701_chunks_v1.jsonl")
    n = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for c in chunks:
            n += 1
            ch = c["chapter"]
            cno = ch["chapter_no"] if ch["chapter_no"] else 0
            cid = f"{PREFIX}_v1_u0_c{cno}_pdf{c['pstart']:03d}_{n:04d}"
            rec = {
                "id": cid,
                "book_title": BOOK_TITLE,
                "author": AUTHOR,
                "unit_no": None,
                "unit_name": None,
                "chapter_no": ch["chapter_no"],
                "chapter_title": ch["chapter_title"],
                "section": c["section"],
                "content_type": c["ctype"],
                "book_pages": None,
                "pdf_pages": [c["pstart"], c["pend"]],
                "text": c["text"],
                "char_count": len(c["text"]),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {n} -> {out_path}")
    # census
    import collections
    tc = collections.Counter(json.loads(l)["content_type"] for l in open(out_path, encoding="utf-8"))
    print("types:", dict(tc.most_common(20)))
    sizes = sorted(json.loads(l)["char_count"] for l in open(out_path, encoding="utf-8"))
    print(f"size min={sizes[0]} median={sizes[len(sizes)//2]} max={sizes[-1]}")


if __name__ == "__main__":
    main()
