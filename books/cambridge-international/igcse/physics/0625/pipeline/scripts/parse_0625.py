#!/usr/bin/env python3
"""parse_0625.py — chunker for Hodder Cambridge IGCSE Physics 3rd ed (0625).

Input:  cache/w-f9/text_pages/0625/page_*.json (extract_0625.py output; fixed
        gutter x=307 column law, col 0 = left band, col 1 = right band)
Output: staged parsed/ corpus for the 0625 lane.

Laws (probed, evidence cache/w-f9/probe*.json + build logs):
- display headings are the '●● Title' bullet lines (>=18pt); prefix stripped;
- openers: 26pt title + 35pt chapter number accumulate into an opener_title
  segment (folded into the following chunk); the 9pt symbol-font bullet list
  ('l ...' lines) is the at-a-glance LO box -> learning_outcomes;
- 5 section dividers = unit law: chapters carry unit_no/unit_name;
- back-matter banks force content_type (revision_bank/exam_bank/mathematics/
  investigations/practical_test_bank/alt_practical_bank/answers/index/
  acknowledgements); repeated display headers of forced ranges dropped;
- marker forms case-insensitive + whitespace-normalized (probed 'Worked
  examples' / 'Worked example' / 'Practical work:' / 'Checklist');
- 'l'-bullet prefix stripped; fi/fl ligature-loss damage NOT repaired in body
  text (v1 damage class, polish pending).
"""
import json, os, re, sys, glob, collections

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_structure_0625 import (chapter_ranges, BOOK_TITLE, AUTHOR, OFFSET,
                                 FRONT_MATTER_END, ALLCAPS_MARKERS, SOFT_MARKERS,
                                 BULLET_HEAD, OPENER_BULLET, CHAPTER_OPENERS,
                                 SECTION_DIVIDERS, BACK_STARTS, BACK_TYPES,
                                 is_running_header, FOOTER_STRIP_Y)

IN = "/home/z/my-project/cache/w-f9/text_pages/0625"
OUT_DIR = "/home/z/my-project/cache/w-f9/build/0625/out"
PREFIX = "c0625"
TARGET_MIN, TARGET_MAX, HARD_MAX = 350, 1600, 2400
HEADING_SIZE = 15.0             # ●● heads are 18-20pt; a)/b) sub-heads 14pt
SUBHEAD_SIZE = 13.0
OPENERS = set(CHAPTER_OPENERS)
DIV_PAGES = {s: (no, name) for s, no, name in SECTION_DIVIDERS}
BACK_RANGE = {s: (key, title) for s, key, title in BACK_STARTS}

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\u201c\"'])")

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


def is_bullet_head(text, size):
    return bool(BULLET_HEAD.match(text.strip())) and size >= HEADING_SIZE


def bullet_head_type(sec):
    """●● heads that carry their own content_type (probed: Worked example /
    Practical boxes). Everything else is a plain body section."""
    s = re.sub(r"\s+", " ", sec.strip().lower())
    if s.startswith("worked example"):
        return "worked_example"
    if s.startswith("practical"):
        return "practical"
    return None


def is_subhead(text, size, bold):
    t = text.strip()
    if size < SUBHEAD_SIZE or size >= HEADING_SIZE + 3 or len(t) > 70:
        return False
    return bool(re.match(r"^[a-e]\)\s+\S", t)) or (bold and not t.endswith(('.', ',', ';', ':'))
                                                   and len(t) < 44
                                                   and not t.startswith(('[', 'Figure', 'Table')))


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
            key = None
            for st, k, title in BACK_STARTS:
                if p >= st:
                    key = k
            page2chap[p]["back_key"] = key
            page2chap[p]["forced"] = BACK_TYPES.get(key) if key else None
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
        opener_phase = None       # None | 'head' | 'box' (openers only)
        if pno in OPENERS:
            opener_phase = "head"
        for b in d["blocks"]:
            t = b["text"].strip()
            # strip symbol-font control glyphs (opener box bullets render \x07)
            t = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", t).strip()
            if not t or t == "images":
                continue
            y, col = b["y"], b.get("col", 0)
            if is_running_header(t, b["size"], y):
                continue
            if y > FOOTER_STRIP_Y and b["size"] < 13:
                continue
            if chap["forced"] and t == chap["chapter_title"]:
                continue
            dy = (y - prev_y) if prev_y is not None else 999
            if prev_col is not None and col != prev_col and cur:
                segs.append(dict(cur)); cur = None
            prev_y, prev_col = y, col
            forced = chap["forced"]
            # opener page phase law: 'head' (>=20pt title+number) -> 'box'
            # (9pt at-a-glance bullets) -> 'body' (>=10.5pt content)
            if opener_phase == "head":
                if b["size"] >= 20:
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
                opener_phase = "box"
            if opener_phase == "box":
                if b["size"] < 10.5 and OPENER_BULLET.match(t):
                    if cur and cur["ctype"] == "opener_title":
                        segs.append(dict(cur)); cur = None
                    mk = "learning_outcomes"
                else:
                    opener_phase = "body"
                    # the transition block starts body typing: flush the box
                    if cur:
                        segs.append(dict(cur)); cur = None
                    mk = classify_marker(t)
            else:
                mk = classify_marker(t)
            bullet = is_bullet_head(t, b["size"])
            sub = (not mk) and (not bullet) and is_subhead(t, b["size"], b["bold"])
            if cur and cur["ctype"] == "opener_title":
                segs.append(dict(cur)); cur = None
            if mk or bullet or sub:
                if cur:
                    segs.append(dict(cur)); cur = None
            if bullet:
                sec = BULLET_HEAD.sub("", t).strip()
                btype = bullet_head_type(sec)
                cur = {"chapter": chap, "section": sec if not btype else None,
                       "ctype": forced or btype or "body",
                       "text": sec, "pstart": pno, "pend": pno}
            elif mk:
                cur = {"chapter": chap, "section": None,
                       "ctype": forced or mk,
                       "text": t, "pstart": pno, "pend": pno}
            elif sub:
                cur = {"chapter": chap, "section": None,
                       "ctype": forced or "body",
                       "text": t, "pstart": pno, "pend": pno}
            elif cur is None:
                cur = {"chapter": chap, "section": None,
                       "ctype": forced or "body",
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
        if cur and nxt != chap:
            segs.append(dict(cur)); cur = None; cur_dy = None
    if cur:
        segs.append(dict(cur))
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
    # strip the 'l' bullet prefix in learning_outcomes text
    for s in cleaned:
        if s["ctype"] == "learning_outcomes":
            s["text"] = "\n\n".join(OPENER_BULLET.sub("", ln) if OPENER_BULLET.match(ln) else ln
                                    for ln in s["text"].split("\n\n"))
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
    out_path = os.path.join(OUT_DIR, "cie_igcse_physics_0625_chunks_v1.jsonl")
    n = 0
    with open(out_path, "w", encoding="utf-8") as f:
        for c in chunks:
            n += 1
            ch = c["chapter"]
            cno = ch["chapter_no"] if ch["chapter_no"] else 0
            uno = ch.get("unit_no") or 0
            cid = f"{PREFIX}_v1_u{uno}_c{cno}_pdf{c['pstart']:03d}_{n:04d}"
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
