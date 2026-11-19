#!/usr/bin/env python3
"""parse_9700.py — chunker for CIE 9700 Biology Coursebook 4th ed (text-layer lane).

Input:  cache/w-f9/text_pages/9700/page_*.json  (extract_9700.py output,
        column-aware span-pool assembly; col 0 = left band, col 1 = right band)
Output: staged parsed/ corpus for the 9700 lane.

Laws (probed, evidence cache/w-f9/probe*.json + build logs):
- markers take precedence over display headings (EOC 18pt heading is
  chapter_questions, not a body section);
- marker forms case-insensitive ('Learning outcomes' Title Case on openers);
- opener pages: blocks before the Learning-outcomes marker accumulate into an
  opener_title segment (chapter number + display title), folded into the
  following learning_outcomes chunk;
- back-matter ranges force content_type (front_matter/appendix/glossary/index/
  acknowledgements/exam_advice/answers_saqs/answers_eoc/recommended_resources);
  P1/P2 keep marker typing;
- segmentation streams col 0 fully then col 1, flushes on marker / heading /
  column / chapter change; paragraphs via y-gap; de-hyphenation at joins;
  packing 350-1600, hard max 2400.
"""
import json, os, re, sys, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_9700 import (chapter_ranges, BOOK_TITLE, AUTHOR, OFFSET,
                                 FRONT_MATTER_END, ALLCAPS_MARKERS, SOFT_MARKERS,
                                 CHAPTER_OPENERS, P1_START, P2_START,
                                 is_running_header, FOOTER_STRIP_Y)

IN = "/home/z/my-project/cache/w-f9/text_pages/9700"
OUT_DIR = "/home/z/my-project/cache/w-f9/build/9700/out"
PREFIX = "c9700"
TARGET_MIN, TARGET_MAX, HARD_MAX = 350, 1600, 2400
HEADING_SIZE = 15.5             # 18pt A-heads (probed)
SOFT_HEAD_SIZE = 11.5           # bold 12-13pt sub-heads (probed)
OPENERS = set(CHAPTER_OPENERS) | {P1_START, P2_START}

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\u201c\"'])")

FORCED = {
    "Front matter (cover, contents, how to use this book, introduction)": "front_matter",
    "P1 Practical skills for AS": None,
    "P2 Planning, analysis and evaluation": None,
    "Appendix 1: Amino acid R groups": "appendix",
    "Appendix 2: DNA and RNA triplet codes": "appendix",
    "Glossary": "glossary",
    "Index": "index",
    "Acknowledgements": "acknowledgements",
    "Advice on how to revise for and approach examinations": "exam_advice",
    "Introduction to the examination and changes to the syllabus": "exam_advice",
    "Answers to SAQs": "answers_saqs",
    "Answers to EOCQs": "answers_eocq",
    "Recommended resources": "recommended_resources",
}

_ALL = dict(ALLCAPS_MARKERS)
_LOWER = {k.lower(): v for k, v in ALLCAPS_MARKERS.items()}


def classify_marker(text):
    t = re.sub(r"\s+", " ", text.strip())
    if t in _ALL:
        return _ALL[t]
    if t.lower() in _LOWER:
        return _LOWER[t.lower()]
    for pat, ct in SOFT_MARKERS:
        if t.startswith(pat):
            return ct
    for pat, ct in SOFT_MARKERS:
        if t.lower().startswith(pat.lower()):
            return ct
    return None


def is_display_head(text, size, bold):
    t = text.strip()
    if size < HEADING_SIZE or len(t) > 80:
        return False
    return not t.endswith(('.', '?', '!', ',', ';', ':', ')'))


def is_soft_head(text, size, bold):
    t = text.strip()
    if not bold or size < SOFT_HEAD_SIZE or size >= HEADING_SIZE or len(t) > 70:
        return False
    if t.endswith(('.', '?', '!', ',', ';', ':')):
        return False
    return not t.startswith(('[', 'Figure', 'Table'))


def dehyph(a, b):
    if a.endswith("-") and len(a) > 2 and a[-2].islower() and b[:1].islower():
        return a[:-1] + b
    return a + " " + b


def build_segments():
    ranges = chapter_ranges()
    page2chap = {}
    for s, e, m in ranges:
        for p in range(s, e + 1):
            page2chap[p] = dict(m)
            page2chap[p]["forced"] = FORCED.get(m["chapter_title"])
    segs = []
    cur = None
    cur_dy = None
    for pf in sorted(glob.glob(os.path.join(IN, "page_*.json"))):
        d = json.load(open(pf, encoding="utf-8"))
        pno = d["pdf"]
        chap = page2chap.get(pno)
        if chap is None:
            continue
        prev_y = None
        prev_col = None
        opener_done = pno not in OPENERS
        for b in d["blocks"]:
            t = b["text"].strip()
            if not t or t == "images":
                continue
            y, col = b["y"], b.get("col", 0)
            if is_running_header(t, b["size"], y):
                continue
            if y > FOOTER_STRIP_Y and b["size"] < 13:
                continue
            # repeated display header of a forced range (e.g. 'Answers to SAQs'
            # at 28pt on every answers page) is a running display header
            if chap["forced"] and t == chap["chapter_title"]:
                continue
            dy = (y - prev_y) if prev_y is not None else 999
            if prev_col is not None and col != prev_col and cur:
                segs.append(dict(cur)); cur = None
            prev_y, prev_col = y, col
            mk = classify_marker(t)
            # opener page: everything before the Learning-outcomes marker is
            # the chapter head (number + display title) -> opener_title segment
            if not opener_done and mk != "learning_outcomes":
                if cur and cur["ctype"] != "opener_title":
                    segs.append(dict(cur)); cur = None
                if cur is None:
                    cur = {"chapter": chap, "section": None, "ctype": "opener_title",
                           "text": t, "pstart": pno, "pend": pno}
                else:
                    cur["text"] += "\n\n" + t
                    cur["pend"] = pno
                cur_dy = dy
                continue
            if pno in OPENERS and mk == "learning_outcomes":
                opener_done = True
            if cur and cur["ctype"] == "opener_title":
                segs.append(dict(cur)); cur = None
            if mk or is_display_head(t, b["size"], b["bold"]) or \
                    ((not mk) and is_soft_head(t, b["size"], b["bold"])):
                if cur:
                    segs.append(dict(cur)); cur = None
            if mk:
                ctype = chap["forced"] or mk
                cur = {"chapter": chap, "section": None, "ctype": ctype,
                       "text": t, "pstart": pno, "pend": pno}
            elif is_display_head(t, b["size"], b["bold"]):
                ctype = chap["forced"] or "body"
                cur = {"chapter": chap, "section": t, "ctype": ctype,
                       "text": t, "pstart": pno, "pend": pno}
            elif is_soft_head(t, b["size"], b["bold"]):
                ctype = chap["forced"] or "body"
                cur = {"chapter": chap, "section": None, "ctype": ctype,
                       "text": t, "pstart": pno, "pend": pno}
            elif cur is None:
                cur = {"chapter": chap, "section": None,
                       "ctype": chap["forced"] or "body",
                       "text": t, "pstart": pno, "pend": pno}
            else:
                if cur_dy is not None and cur_dy > 16:
                    cur["text"] += "\n\n" + t
                else:
                    cur["text"] = dehyph(cur["text"], t)
                cur["pend"] = pno
                if len(cur["text"]) > 1800 and cur_dy is not None and cur_dy > 16:
                    segs.append(dict(cur))
                    cur = {"chapter": chap, "section": cur["section"],
                           "ctype": cur["ctype"],
                           "text": "", "pstart": pno, "pend": pno}
            cur_dy = dy
        nxt = page2chap.get(pno + 1)
        if cur and (nxt is not chap or nxt != chap):
            segs.append(dict(cur)); cur = None; cur_dy = None
    if cur:
        segs.append(dict(cur))
    # fold trailing opener_title into the next segment as learning_outcomes
    cleaned = []
    hold = None
    for s in segs:
        if hold is not None:
            s = {**s, "text": (hold["text"] + "\n\n" + s["text"]).strip(),
                 "pstart": min(hold["pstart"], s["pstart"])}
            hold = None
        if s["ctype"] == "opener_title":
            hold = s
            continue
        cleaned.append(s)
    if hold:
        cleaned.append({**hold, "ctype": "learning_outcomes"})
    return cleaned


def pack(segs):
    chunks = []
    for s in segs:
        text = s["text"]
        parts, cur2 = [], ""
        for para in text.split("\n\n"):
            para = re.sub(r"\s*\n\s*", " ", para).strip()
            if not para:
                continue
            if cur2:
                cur2 += "\n\n" + para
            else:
                cur2 = para
            while len(cur2) > HARD_MAX:
                cut = cur2.rfind("\n\n", 0, HARD_MAX)
                if cut < TARGET_MIN:
                    ms = list(SENT_SPLIT.finditer(cur2[:HARD_MAX]))
                    cut = ms[-1].start() if ms else HARD_MAX
                parts.append(cur2[:cut].strip())
                cur2 = cur2[cut:].strip()
        if cur2:
            parts.append(cur2)
        for p in parts:
            chunks.append({**s, "text": p})
    merged = []
    for c in chunks:
        tiny = len(c["text"]) < 80
        if merged and (
            (tiny and len(merged[-1]["text"]) + len(c["text"]) + 2 <= TARGET_MAX
             and merged[-1]["chapter"] is c["chapter"]
             and merged[-1]["ctype"] == c["ctype"]
             and c["pstart"] - merged[-1]["pend"] <= 1)
            or (len(c["text"]) < TARGET_MIN
                and len(merged[-1]["text"]) + len(c["text"]) + 2 <= TARGET_MAX
                and merged[-1]["chapter"] is c["chapter"]
                and merged[-1]["section"] == c["section"]
                and merged[-1]["ctype"] == c["ctype"]
                and c["pstart"] - merged[-1]["pend"] <= 1)):
            m = merged[-1]
            m["text"] += "\n\n" + c["text"]
            m["pend"] = c["pend"]
        else:
            merged.append(dict(c))
    # forward-merge: tiny chunk whose NEXT chunk is same chapter+ctype and
    # page-contiguous joins forward (stranded sub-heads across column flushes)
    fwd = []
    i = 0
    while i < len(merged):
        c = merged[i]
        if (len(c["text"]) < 30 and i + 1 < len(merged)
                and merged[i + 1]["chapter"] is c["chapter"]
                and merged[i + 1]["ctype"] == c["ctype"]
                and merged[i + 1]["pstart"] - c["pend"] <= 1
                and len(merged[i + 1]["text"]) + len(c["text"]) + 2 <= TARGET_MAX):
            nxt = merged[i + 1]
            merged[i + 1] = {**nxt, "text": (c["text"] + "\n\n" + nxt["text"]).strip(),
                             "pstart": c["pstart"]}
            i += 1
            continue
        fwd.append(c)
        i += 1
    merged = fwd
    out = []
    for c in merged:
        if len(c["text"]) <= HARD_MAX:
            out.append(c)
            continue
        cur2 = ""
        for para in c["text"].split("\n\n"):
            cand = (cur2 + "\n\n" + para) if cur2 else para
            if len(cand) > HARD_MAX and cur2:
                out.append({**c, "text": cur2})
                cur2 = para
            else:
                cur2 = cand
        if cur2:
            out.append({**c, "text": cur2})
    return out


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    segs = build_segments()
    print(f"segments: {len(segs)}")
    chunks = pack(segs)
    print(f"chunks (pre-id): {len(chunks)}")
    out_path = os.path.join(OUT_DIR, "cie_a_level_biology_9700_chunks_v1.jsonl")
    n = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for c in chunks:
            n += 1
            ch = c["chapter"]
            cno = ch["chapter_no"] if ch["chapter_no"] else 0
            cid = f"{PREFIX}_v1_u0_c{cno}_pdf{c['pstart']:03d}_{n:04d}"
            if c["pstart"] <= FRONT_MATTER_END:
                bp = None
            else:
                bp = [max(1, c["pstart"] - OFFSET), c["pend"] - OFFSET]
            rec = {
                "id": cid,
                "book_title": BOOK_TITLE,
                "author": AUTHOR,
                "unit_no": ch.get("unit_no"),
                "unit_name": ch.get("unit_name"),
                "chapter_no": ch["chapter_no"],
                "chapter_title": ch["chapter_title"],
                "section": c["section"],
                "content_type": c["ctype"],
                "book_pages": bp,
                "pdf_pages": [c["pstart"], c["pend"]],
                "text": c["text"],
                "char_count": len(c["text"]),
            }
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(f"wrote {n} -> {out_path}")
    tc = collections.Counter(json.loads(l)["content_type"] for l in open(out_path, encoding="utf-8"))
    print("types:", dict(tc.most_common(24)))
    sizes = sorted(json.loads(l)["char_count"] for l in open(out_path, encoding="utf-8"))
    print(f"size min={sizes[0]} median={sizes[len(sizes)//2]} max={sizes[-1]}")


if __name__ == "__main__":
    main()
