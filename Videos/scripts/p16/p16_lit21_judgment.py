#!/usr/bin/env python3
"""P16 lit-21 opening lane: adjudicate the 252 RESERVED lit-0475 titles onto
cie-igcse-english-literature-21 (CIE IGCSE Literature in English 0475, spine
2023-2025, 203 spec points).

Owner decision 2026-11-20: "open lit-21" — the P12 terminal declaration is
overturned for this one course. The reserved set:
  - IGCSESUCCESS 0475 x9        (P14 RESERVED, re-derived from the committed
                                 inventory with the committed p14_judgment.py
                                 predicate: \\b0475\\b / IGCSE Literature, minus
                                 0408 World Literature)
  - Claire's Notes x243         (P15 RESERVED, scripts/p15/reserved.json ==
                                 the whole pool, ids == committed inventory)

Binding law of record (the P13/P14/P15 gate ladder adapted to a set-text
spine — new Class W, everything else unchanged):

  Class W  set-text work bind   — the title names a WORK that is a spine set
                                 text (Songs of Ourselves Vol 1 P4 / Vol 2 P3 /
                                 Vol 2 P4 poem lists, the Ted Hughes 15, the
                                 prose novels, the Stories of Ourselves Vol 2
                                 lists, the per-year drama set texts). Bind ALL
                                 spec points carrying the work (multi-year
                                 occurrences disclosed per row — the P13
                                 shared-unit precedent; a repeated set text is
                                 not a discriminative ambiguity). Confidence
                                 medium when the title carries author+work
                                 matching the spine line, low under the
                                 title-only posture (work-only or multi-work
                                 tips rows). boardMismatch true (the committed
                                 builder law for spec rows).
                                 MATCH RULE (suffix-anchored): a spine work
                                 binds a title work-span iff the span EQUALS
                                 the work or ENDS WITH it at a word boundary
                                 (marketing prefixes strip cleanly; mid-phrase
                                 coincidences like 'night sweat' inside 'the
                                 man with night sweats' do NOT bind).
  skips    honest ledger        — guidance/skills register (no work named),
                                 out-of-spine board register (AQA/Edexcel/
                                 Eduqas/WJEC/GCSE without a CIE token),
                                 works not on the 2023-2025 set-text lists
                                 (Macbeth, Kumukanda, AQA anthologies, ...),
                                 character-study titles without a set-text
                                 token (no machine-checkable bind).

Exactly-once disposition of all 252; 0 collisions machine-checked.
Outputs /home/z/my-project/work/p16/: judgment.json, keeps.json, skips.json
"""
import json, re, os
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh"
OUT = "/home/z/my-project/work/p16"
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- spine parse
spine = json.load(open(f"{HUB}/apps/hub/spines/cie-igcse-english-literature-21.json"))
HUGHES15 = ["The Thought-Fox", "The Harvest Moon", "The Jaguar", "Football at Slack",
            "The Horses", "Roe-Deer", "Wind", "A Memory", "Relic", "Telegraph Wires",
            "Hawk Roosting", "Anniversary", "Cat and Mouse", "The Other", "Snowdrop"]

def norm(s):
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def clean(t):
    return t.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')

specs = []  # {code, raw, author, works[], kind}
cur_author = None
for n in spine["curriculum"]["nodes"]:
    if n.get("family") != "SPEC_POINT":
        continue
    raw, code = n.get("title", ""), n.get("code")
    t = clean(raw)
    author, works, kind = None, [], "structural"
    m = re.match(r"^(.{2,60}?),\s*'(.+)'$", t)
    if m:  # poetry line: Author, 'Work'
        author, works, kind = m.group(1), [m.group(2)], "poem"
        if "following 15 poems" in works[0] or "may be found" in works[0]:
            author, works, kind = None, [], "structural"
    else:
        sm = re.match(r"^.*?From Stories of Ourselves Volume 2\s*,\s*the following 10 stories:(.*)$", t, re.S)
        if sm:  # stories list: no. N Author, 'Story' ...
            segs = re.split(r"no\.\s*\d+\s*", sm.group(1))
            works, authors = [], []
            for seg in segs:
                # word-internal apostrophes are content ('Dr Heidegger's Experiment',
                # 'Thank You M'am') — a quote only closes before a non-word char
                m2 = re.match(r"^(.{2,60}?),\s*'((?:[^']|'(?=\w))+?)'(?!\w)", seg.strip())
                if m2:
                    authors.append(m2.group(1)); works.append(m2.group(2))
            author, works, kind = authors or None, works, "stories-list" if works else "structural"
        elif re.match(r"^Ted Hughes,?\s+the following 15 poems", t, re.I):
            author, works, kind = "Ted Hughes", [], "hughes-header"
        elif re.match(r"^(The Thought-Fox|The Jaguar|The Horses|Wind|Relic|Hawk Roosting|Cat and Mouse|Snowdrop)\b", t.strip()):
            works = [p for p in HUGHES15 if norm(p) in " " + norm(t) + " "]
            author, works, kind = cur_author, works, "hughes-pair" if works else "structural"
        else:
            # prose/drama: "Author Work" — work = title minus a known-author prefix
            cleaned = re.sub(r"\s*(begin teaching, check the set text list.*|Requirements:.*|Resources:.*|Cambridge School Shakespeare.*|Cambridge Literature series.*|Penguin Shakespeare.*|Oxford School Shakespeare.*|Heinemann Shakespeare.*|Longman School Shakespeare.*)$", "", t, flags=re.I)
            am = re.match(r"^((?:[A-Z][\w'.-]*\s+){1,3}?)([A-Z].+)$", cleaned)
            if am and not re.match(r"^(Candidates|From|Set texts|These)", cleaned):
                author, kind = am.group(1).strip(), "prose-drama"
                # the author word-count is ambiguous — index EVERY 1..3-word
                # leading split as a work candidate (e.g. 'William Shakespeare
                # Othello' -> {'shakespeare othello', 'othello'}); exact/suffix
                # matching keeps cross-line false binds out
                words = cleaned.split()
                works = [" ".join(words[k:]) for k in range(1, min(4, len(words)))]
    if kind == "hughes-header":
        cur_author = author
    elif kind != "hughes-pair":
        cur_author = None
    specs.append({"code": code, "raw": raw, "author": author, "works": works, "kind": kind})

by_code = {s["code"]: s for s in specs}
assert len(specs) == 203, f"spec count {len(specs)} != 203"

# ---------------------------------------------------------------- pool load
cn = json.load(open(f"{RES}/Videos/inventory/channels/claires-notes-uploads.json"))
igs = json.load(open(f"{RES}/Videos/inventory/channels/igcsesuccess-uploads.json"))
p15res = json.load(open(f"{RES}/Videos/scripts/p15/reserved.json"))
cn_ids = {u["id"] for u in cn["videos"]}
assert {e["video"] for e in p15res} == cn_ids, "P15 reserved ids != claires-notes inventory ids"

pool = []
for u in cn["videos"]:
    pool.append({"id": u["id"], "title": u["title"], "provider": "claires-notes",
                 "providerLabel": "Claire's Notes", "uc": cn.get("channelId")})
igs9 = []
for u in igs["videos"]:
    t = u["title"]
    if re.search(r"\b0408\b|World\s+Literature", t, re.I):
        continue
    if re.search(r"\b0475\b", t) or re.search(r"IGCSE\s+Literature", t, re.I):
        igs9.append({"id": u["id"], "title": t, "provider": "igcsesuccess",
                     "providerLabel": "IGCSESUCCESS", "uc": igs.get("channelId")})
assert len(igs9) == 9, f"IGCSESUCCESS re-derivation {len(igs9)} != 9"
pool += igs9
assert len(pool) == 252 and len({p['id'] for p in pool}) == 252

# ---------------------------------------------------------------- extraction
CIE_TOKEN = re.compile(r"cambridge|igcse|\b0475\b|\bcie\b|literature", re.I)
AQA_BOARD = re.compile(r"\bAQA\b|\bEduqas\b|WJEC|Edexcel|\bGCSE\b(?!.*(cambridge|igcse))|English Language Paper", re.I)
GUIDANCE = re.compile(r"^(what is|top five|top tips|dos and don|the art of persuasion|analysing language|identifying and talking)|writing errors|essay skills|keep language analysis|essays? (are|is) flopping|language english vs igcse", re.I)
NOBIND_CHARS = ["Malvolio", "Caliban", "Sybil", "Eric Birling", "Mr Hyde", "Scrooge", "Cratchit", "Juliet", "Banquo", "Miranda", "Ferdinand"]

TRAIL_JUNK = re.compile(
    r"\s*(\[?part\s+\d+(\s+of\s+\d+)?\]?|part\s+\d+|analysis|detailed analysis|"
    r"detailed commentary and analysis|commentary and analysis|full analysis|"
    r"line by line analysis|line by line|detailed commentary|commentary|"
    r"study guide.*)$", re.I)

def extract_candidates(title):
    """Return (author, [spans], flags) — spans are normalized work-span candidates."""
    t = clean(title)
    low = norm(title)
    flags = {"aqaBoard": bool(AQA_BOARD.search(t) and not re.search(r"cambridge|igcse", t, re.I)),
             "multi": False}
    spans, author = [], None
    # author from " by X"
    mb = re.search(r"\bby\s+([A-Z][\w'.-]*(?:\s+[A-Z][\w'.-]+){0,3})", t)
    if mb: author = mb.group(1)
    # quoted spans (closing quote anchored before " by" / punctuation / end;
    # word-internal apostrophes are content — 'Thank You, M'am' stays whole)
    for q in re.findall(r"'((?:[^']|'(?=\w))+?)'(?!\w)(?=\s*by\b|\s*[\u2013\-:;,()]|$)", t):
        if len(norm(q)) >= 3: spans.append(q)
    # " - " segments (IGCSESUCCESS caps form + segment authors)
    segs = [s for s in re.split(r"\s+-\s+", t) if s.strip()]
    for i, seg in enumerate(segs):
        ns = norm(seg)
        if len(ns) >= 4: spans.append(seg)
        if 0 < i < len(segs) - 1 and len(ns.split()) <= 3 and not re.search(r"\d", ns) \
           and not re.search(r"igcse|literature|cambridge", ns, re.I) and author is None:
            author = seg  # "IGCSE LITERATURE - Ted Hughes - Wind": segment author
    # first colon segment (drama commentary "Othello: Act ...")
    if ":" in t:
        head = t.split(":")[0]
        if not re.search(r"insights|tips", head, re.I) and len(norm(head)) >= 4:
            spans.append(head)
    # comma lists after ':' or '(' — multi-work tips rows
    for mseg in re.findall(r"(?::|\()\s*([^:()]{10,140}?)(?:\)|$)", t):
        if "," in mseg and not re.search(r"Act\s|scene\s", mseg):
            parts = mseg.split(",")
            good = [p for p in parts if 3 <= len(norm(p)) <= 60]
            if len(good) >= 2:
                spans += good; flags["multi"] = True
    # prefix before " by " (unquoted "Work by Author" guides)
    mu = re.match(r"^(.{2,90}?)\s+by\s+[A-Z]", t)
    if mu and not re.search(r"\bAct\s+\d\b", mu.group(1)):
        spans.append(mu.group(1))
    # "Work Act N" without colon (Journey's End Act 2 scene 1; Othello Act I scene ii)
    mj = re.match(r"^([A-Z][^:]{2,60}?)\s+Act\s+(?:[IVXLC]+|\d+)", t)
    if mj: spans.append(mj.group(1))
    # Hughes poem-name spans ONLY when the name is actually in the title
    # (a mere 'Hughes' mention must not pull in all 15 poems — 'Thank You, M\'am'
    # by Langston Hughes is not a Ted Hughes set text)
    if re.search(r"hughes", low):
        for h in HUGHES15:
            nh = norm(h)
            if re.search(r"(?<![a-z0-9])" + re.escape(nh) + r"(?![a-z0-9])", low):
                spans.append(h)
    # normalize + strip trailing junk until stable + dedupe
    seen, out = set(), []
    for w in spans:
        nw = norm(w)
        while True:
            nw2 = TRAIL_JUNK.sub("", nw).strip()
            if nw2 == nw: break
            nw = nw2
        if nw and nw not in seen:
            seen.add(nw); out.append(nw)
    return author, out, flags

# ---------------------------------------------------------------- match
def spine_hits(span):
    """Suffix-anchored bind: spine work == span, or span ends with the work at a
    word boundary (marketing prefixes strip cleanly), or the title dropped a
    leading article ('city planners' vs spine 'The City Planners'). Mid-phrase
    coincidences ('night sweat' inside 'the man with night sweats') and
    cross-work subset hits ('planners' inside 'The City Planners') do NOT bind."""
    hits = []
    for s in specs:
        if not s["works"]: continue
        for w in s["works"]:
            nw = norm(w)
            if not nw: continue
            if span == nw or (len(nw) >= 4 and span.endswith(" " + nw)) \
               or nw == "the " + span or nw == "a " + span:
                hits.append(s); break
    return hits

def author_ok(title_author, spec_author):
    if not title_author: return True
    ta = set(norm(title_author).split())
    if not ta: return True
    sa_list = spec_author if isinstance(spec_author, list) else [spec_author]
    if not sa_list or all(not s for s in sa_list): return True
    for sa in sa_list:
        sa_t = set(norm(sa).split())
        if (ta & sa_t) or (ta <= sa_t) or (sa_t <= ta):
            return True
    return False

judgment, keeps, skips = {}, [], []
for p in pool:
    vid, title, prov = p["id"], p["title"], p["providerLabel"]
    author, works, flags = extract_candidates(title)
    # 1) guidance register first (no honest work bind)
    if GUIDANCE.search(title):
        skips.append({"video": vid, "title": title, "provider": p["provider"], "cls": "guidance/skills register",
                      "reason": "technique/skills title with no set-text bind (guidance register law)"})
        judgment[vid] = {"action": "skip", "cls": "guidance/skills register"}
        continue
    if flags["aqaBoard"] and not any(spine_hits(w) for w in works):
        skips.append({"video": vid, "title": title, "provider": p["provider"], "cls": "out-of-spine board register",
                      "reason": "title carries the AQA/Eduqas/WJEC/Edexcel/GCSE register without a CIE token and names no spine set text"})
        judgment[vid] = {"action": "skip", "cls": "out-of-spine board register"}
        continue
    # 2) class W: suffix-anchored set-text binds
    matched = {}  # span -> [spec]
    for w in works:
        hits = spine_hits(w)
        if hits and author_ok(author, hits[0]["author"]):
            matched[w] = hits
    if matched:
        allcodes = []
        for w, hs in matched.items():
            allcodes += [h["code"] for h in hs]
        allcodes = list(dict.fromkeys(allcodes))
        has_author = author is not None
        single = len(matched) == 1
        confidence = "medium" if (single and has_author) else "low"
        ev = ("set-text work bind (Class W): title names spine set text(s) "
              + "; ".join(f"'{w}' -> {', '.join(h['code'] for h in hs)} [{hs[0]['raw'][:60]}]" for w, hs in matched.items())
              + f"; multi-year set-text occurrence(s) disclosed (df={len(allcodes)}, the P13 shared-unit precedent — a repeated set text is not a discriminative ambiguity)"
              + ("; author cross-checked" if has_author else "; title-only posture, work-name bind")
              + ("; multi-work tips row — works' points bound as ONE multi-spec row (the four-gate topic-lecture class analog)" if flags["multi"] else "")
              + "; confidence " + confidence + " under the P13/P14 title-only posture")
        keeps.append({"video": vid, "title": title, "provider": p["provider"], "providerLabel": prov,
                      "specs": allcodes, "confidence": confidence, "cls": "set-text work bind",
                      "evidence": ev, "uc": p["uc"]})
        judgment[vid] = {"action": "keep", "cls": "set-text work bind", "specs": allcodes}
        continue
    # 3) no honest bind
    cls = "work not on the 2023-2025 set-text lists"
    reason = "the named work is not a spine set text for the 0475 2023-2025 examinations (honest no-binding)"
    if any(c.lower() in title.lower() for c in NOBIND_CHARS):
        cls = "character-study title without a set-text token"
        reason = "title names a character/theme, not a spine set text — no machine-checkable bind at the bar"
    skips.append({"video": vid, "title": title, "provider": p["provider"], "cls": cls, "reason": reason})
    judgment[vid] = {"action": "skip", "cls": cls}

# ---------------------------------------------------------------- checks
assert len(judgment) == 252, f"dispositions {len(judgment)} != 252"
assert len(keeps) + len(skips) == 252
assert len({k['video'] for k in keeps} | {s['video'] for s in skips}) == 252
bad = [k for k in keeps for c in k["specs"] if c not in by_code]
assert not bad, f"unknown spec codes: {bad[:3]}"
nocie = [k for k in keeps if k['confidence'] not in ("medium", "low")]
assert not nocie

json.dump(judgment, open(f"{OUT}/judgment.json", "w"), indent=1)
json.dump(keeps, open(f"{OUT}/keeps.json", "w"), indent=1, ensure_ascii=False)
json.dump(skips, open(f"{OUT}/skips.json", "w"), indent=1, ensure_ascii=False)

print(f"dispositions: {len(judgment)} (keeps {len(keeps)} / skips {len(skips)})")
print("skip classes:", dict(Counter(s['cls'] for s in skips)))
print("keep confidence:", dict(Counter(k['confidence'] for k in keeps)))
print("distinct spec points kept:", len({c for k in keeps for c in k['specs']}))
print("provider keep split:", dict(Counter(k['provider'] for k in keeps)))
print()
print("=== ALL KEEPS (eyeball pass) ===")
for k in sorted(keeps, key=lambda x: (x['provider'], x['title'])):
    print(f"[{k['confidence']}] {k['video']} {k['title'][:75]}")
    print(f"      -> {k['specs']}")
