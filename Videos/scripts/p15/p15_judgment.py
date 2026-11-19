#!/usr/bin/env python3
"""P15 judgment: route the 18 judgment pools (T1 x14 + T2 x4, 5,348 uploads) onto the
residual-gap spine. claires-notes (243 uploads) is RESERVED (0475 lit register — the
lit-21 owner decision point, folds into the IGCSESUCCESS 9). The P13/P14 gate ladder:

  Tier B   paper-code anchors   — machine-checkable session/paper codes in titles
                                 (method paper-code, confidence high, specs [], kind
                                 past-paper-walkthrough). P15 registers: 0610/0620/0625
                                 CIE IGCSE sciences; 0654/0653 co-ordinated/combined
                                 (shared-paper anchors bind all three sciences of the
                                 family — the P13 shared-unit double-binding precedent);
                                 0417 / 4IT0 ICT; 4MA1 maths A H/F + modular-24 units;
                                 0606 add-maths; 0452 / 0455 / 0680 / 8291 / 0460 /
                                 4GE0 / 0500; IAL WPH/WBI "Unit N <session>" unit-paper
                                 anchors (the P14 Assil law analog); 9708 econ.
  Class M  section markers      — "N.M" titles bind that subtopic's points, confidence low
  Class S  section-name binding — verbatim pipe/dash field equality (P13 gate)
  Tier A   distinctive-token    — df<=3 token binds, confidence medium/low
  Class L  topic lectures       — four-gate topic-lecture class (P12/P13)
  skips    honest ledger        — guidance/advice/marketing, O-Level register, out-of-spine
                                 boards (AQA/OCR/IB/GCSE-UK/NCERT), Edexcel UK-GCSE CS
                                 (no spine course), no-binding remainder.
  reserved lit-0475             — Claire's Notes: 243 accounts, owner decision point.

Outputs work/p15/: tier-b.json, judgment.json, skips.json, reserved.json
"""
import json, os, re, datetime
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub"
WORK = "/home/z/my-project/work/p15"
UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs(WORK, exist_ok=True)

JUDGMENT_POOLS = ["chem-bio-hosni", "caie-made-easier", "learn-today-igcse", "nicos-paphitis",
                  "everything-em", "taughtly", "dr-maria-emam", "mark-harrison", "the-math-pad",
                  "science-and-stuff", "belal-sir-chem-bio", "geo-hacks", "libra-maths",
                  "gilbert-phoon", "shawn-hew", "doctor-no-science", "keen-mindz", "learn-econ-anjuli"]
RESERVED_POOLS = {"claires-notes": "0475 English Literature register at content level (Cambridge iGCSE poem/prose study guides) — the lit-21 owner decision point (folds into the IGCSESUCCESS 9 RESERVED titles; P12 terminal declaration vs the first lit-21 content)"}

pool = []
_seen = set()
for slug in JUDGMENT_POOLS:
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        if v["id"] in _seen:
            continue
        _seen.add(v["id"])
        pool.append({"id": v["id"], "title": v["title"], "provider": slug})

reserved = []
for slug, note in RESERVED_POOLS.items():
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        reserved.append({"video": v["id"], "title": v["title"][:160], "provider": slug, "note": note})

# ---------------------------------------------------------------- spine
TARGETS = ["cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
           "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
           "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
           "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
           "cie-igcse-science-combined-science-23-biology",
           "cie-igcse-science-combined-science-23-physics",
           "cie-igcse-science-combined-science-23-chemistry",
           "cie-igcse-ict-21", "igcse-ict-17",
           "igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
           "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2",
           "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
           "cie-igcse-further-maths-additional-maths-25",
           "cie-igcse-accounting-25", "cie-igcse-accounting-21",
           "cie-igcse-economics-20", "cie-igcse-economics-25", "cie-a-level-economics-23",
           "cie-igcse-environmental-management-25", "cie-as-environmental-management-20",
           "cie-igcse-geography-20", "cie-igcse-geography-25", "igcse-geography-19",
           "cie-igcse-english-language-20", "cie-igcse-english-language-25",
           "ial-physics-19", "ial-biology-18", "ial-chemistry-17",
           "igcse-chemistry-19", "igcse-biology-19"]

P4_CHILDREN = set(json.load(open(f"{RES}/Videos/drafts/_p4/inheritance-map.json"))["parents"].keys())
P15B = [c for c in TARGETS if c in P4_CHILDREN]

specs = {}
for course in TARGETS:
    nodes = json.load(open(f"{HUB}/content/{course}/curriculum.json"))["nodes"]
    topic_of, cur = {}, None
    for n in nodes:
        if n["family"] == "TOPIC":
            cur = n["title"]
        topic_of[n["code"]] = cur
    specs[course] = {"nodes": nodes, "topic_of": topic_of}

STOP = set("""the a an of and or to in on for with your how what why when from as is are be
you i we they it its their our my this that these those at by not no do does using use
explained simply vs versus part guide tips tricks answer answering level levels as a2 igcse
cambridge international caie complete full everything need know revision exam exams
prepare preparation skill skills study lesson lectures lecture course class class-watcher
watch before september october november may june feb march oct nov jun jan uk etc new
updated best top must topics topic questions question paper papers past as-level solved
solution walkthrough selected crash practice problems problem basics intro introduction
introduction-to overview basic further maths math physics chemistry biology economics
economic business accounting accounts computer science 9701 9708 9709 9702 9700 9706 9609
9618 0478 0580 0606 0500 0455 9608 0620 0625 0610 2281 4024 5070 5090 5124 2210 0452 0455
0680 8291 0417 4it0 4ge0 4ma1 0475 0653 0654 0460 9231 4037 4040 0450 0413
p1 p2 p3 p4 p5 p6 m1 m2 s1 s2 fp1 fp2 fp3 c1 c2 c3 c4 c12 c34 edexcel ocr aqa gcse
urdu hindi archived lesson lect tutorial tutorials revision-worksheet worksheet daily
dose olevels olevel predicted predictions predicted-papers tricky made easy exam-exam
review questions questionwise workbook workbook sneak preview reality teaching online""".split())

def toks14(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2]

for course in TARGETS:
    df = Counter()
    for n in specs[course]["nodes"]:
        for w in set(toks14(n["title"] or "")):
            df[w] += 1
    specs[course]["df"] = df
    specs[course]["pts"] = [n for n in specs[course]["nodes"] if n["family"] == "SPEC_POINT"]
    specs[course]["subs"] = [n for n in specs[course]["nodes"] if n["family"] == "SUBTOPIC"]

TDF = {}
for course in TARGETS:
    c = Counter()
    for n in specs[course]["nodes"]:
        if n["family"] in ("TOPIC", "SUBTOPIC"):
            for w in set(toks14(n["title"] or "")):
                c[w] += 1
    TDF[course] = c

def sub_points(course, subcode):
    num = subcode.split(":")[-1].replace("SUB", "")
    return [p for p in specs[course]["pts"] if re.match(rf"^{re.escape(num)}\.\d+$", p["code"])]

def topic_points(course, topic_title):
    return [p for p in specs[course]["pts"] if specs[course]["topic_of"].get(p["code"]) == topic_title]

def best_point(course, title, max_df=3):
    vt = set(toks14(title))
    best, best_score = None, 0
    for p in specs[course]["pts"]:
        pt = set(toks14(p["title"] or ""))
        if not pt:
            continue
        hits = vt & pt
        if not hits:
            continue
        dmax = max(specs[course]["df"].get(w, 99) for w in hits)
        distinctive = [w for w in hits if specs[course]["df"].get(w, 99) <= max_df]
        score = len(distinctive) * 10 + len(hits)
        if len(distinctive) >= 2 or (len(hits) >= 3 and dmax <= 6):
            if score > best_score:
                best, best_score = (p, sorted(hits), dmax, len(hits)), score
    return best

def norm_stop(s):
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return " " + " ".join(w for w in s.split() if w not in STOP and len(w) > 2) + " "

def split_fields(title):
    f = [x.strip() for x in re.split(r"\|| - | — ", title) if x.strip()]
    return f

def section_by_field(course, title):
    fields = [norm_stop(re.sub(r"\([^)]*\)", " ", f)) for f in split_fields(title)]
    best = None
    for n in specs[course]["nodes"]:
        if n["family"] not in ("TOPIC", "SUBTOPIC"):
            continue
        nt = norm_stop(n.get("title") or "")
        if len(nt.strip()) >= 8 and any(nt == f for f in fields):
            if best is None or (n["family"] == "SUBTOPIC" and best["family"] != "SUBTOPIC"):
                best = n
    if not best:
        return None
    if best["family"] == "TOPIC":
        pts = topic_points(course, best.get("title"))
    else:
        pts = sub_points(course, best["code"])
    return (best, pts) if pts else None

def topic_by_unique_token(course, title):
    vt = set(toks14(title))
    vt_stripped = " " + " ".join(re.findall(r"[a-z0-9]+", title.lower())) + " "
    best = None
    for n in specs[course]["nodes"]:
        if n["family"] != "TOPIC":
            continue
        tset = set(toks14(n["title"] or ""))
        subtoks, seen = set(), False
        for m in specs[course]["nodes"]:
            if m is n:
                seen = True
                continue
            if seen and m["family"] == "TOPIC":
                break
            if seen and m["family"] == "SUBTOPIC":
                subtoks |= set(toks14(m["title"] or ""))
        scope = tset | subtoks
        hits = vt & scope
        uniq = [w for w in hits if TDF[course].get(w, 99) <= 1]
        tpair = sorted(w for w in hits if w in tset and TDF[course].get(w, 99) <= 1)
        cls = None
        tt = re.sub(r"[^a-z0-9 ]+", " ", (n["title"] or "").lower())
        tt = " " + " ".join(w for w in tt.split() if w not in STOP and len(w) > 2) + " "
        if len(tt.strip()) >= 8 and tt in vt_stripped:
            cls = "verbatim"
        elif len(uniq) >= 2:
            cls = "multi-uniq"
        elif len(uniq) == 1 and uniq[0] in tset:
            cls = "title-token"
        elif len(tpair) >= 2:
            cls = "title-pair"
        if cls and (best is None or len(uniq) + len(tpair) > len(best[1]) + len(best[2])):
            best = (n["title"], uniq or tpair, sorted(hits), cls)
    return best

def section_marker(course, title):
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\s", title + " ")
    if not m:
        return None
    num = f"{m.group(1)}.{m.group(2)}"
    subs = [s for s in specs[course]["subs"] if s["code"].split(":")[-1].replace("SUB", "") == num]
    if subs:
        pts = sub_points(course, subs[0]["code"])
        if pts:
            return (num, subs[0], pts)
    return None

# ---------------------------------------------------------------- registers
RE_SESSION = re.compile(
    r"(may\s*[/ ]?\s*june|oct(?:ober)?\s*[/ -]?\s*nov(?:ember)?|feb(?:ruar)?y?\s*[/ -]?\s*mar(ch)?\.?"
    r"|\b(jan|jun|nov|feb|mar)\w*\s+20\d\d|20\d\d\s+(jan|jun|nov|feb|mar)|\b(jan|jun|nov|feb|mar)\s*20\d\d"
    r"|\b(?:ON|MJ|FM|F/M|M/J|O/N)[ ]?20?\d\d\b|_(?:s|w|q)\d{2}_|/M/J/\d{2}|/O/N/\d{2}|/F/M/\d{2}"
    r"|\b(?:may|june|oct|nov)\s*20\d\d|\bm/j\b|\bo/n\b|\bqp\b)", re.I)
RE_SOLVED = re.compile(r"solved|solution|walkthrough|past[- ]?paper|qp\s*_?\d|mark scheme|\bQ\s?\d|\bQ\(|question\s*\d|exam questions?|predictions?!? paper|\bcomplete\b|paper\s*\d", re.I)
RE_GUIDE = re.compile(
    r"tips|tricks?\b|ace your|how to (ace|finish|overcome|stop|prepare|revise|get full|write|score)|how (do i|this student|did paper)|"
    r"survival guide|preparation course|orientation|watch (this|before)|podcast|success|result day|"
    r"interview|vision|challenge|parents? of|update|tour|platform|worried|nervous|resit|message|"
    r"days? left|30 days|60 days|join now|score an a\*|a\* in|game.?chang|blended|covid|"
    r"studysmart|aitutor|revision in|month left|marking schemes|what you (need|can)|can't miss|"
    r"paper breakdown|important topics|fix of|lifesaver|one thing|stress|focus on what|predictions?!"
    r"|sneak preview|live class|whatsapp|daily dose|the reality of|full marks|made easy|sneak peek", re.I)
RE_OLEVEL = re.compile(r"\bO\s?-?\s?Levels?\b|\bOL\b|\b4024\b|\b2281\b|\b5070\b|\b5090\b|\b5124\b|\b2210\b|\b4037\b|\b4040\b", re.I)
RE_NT_BOARD = re.compile(r"\bAQA\b|\bOCR\b|\bIB\b|\bNCERT\b|\bCBSE\b|\bJEE\b|\bNEET\b|\bKS[1-4]\b|\bAP\b|\bSAT\b|\bMEI\b|\bMYP\b")
RE_UK_GCSE = re.compile(r"\bGCSE\b(?!\s*\(?\s*i\s*\)?|\s*International)", re.I)
RE_ED_IG = re.compile(r"Edexcel\s+IGCSE|IGCSE.{0,40}Edexcel|\b4MA1\b|\b4PH1?\b|\b4CH1?\b|\b4BI1?\b|\b4IT0\b|\b4GE0\b", re.I)
RE_IAL_UNIT = re.compile(r"Unit\s*([1-6]).{0,60}?(AS|A2|IAS|IA2|A[- ]?Level|International).{0,40}?(Physic|Biolog|Chem)|((Physic|Biolog|Chem).{0,40}?(AS|A2|IAS|IA2).{0,40}?Unit\s*([1-6]))|(IAS|IA2)\s*(Physics|Biology|Chemistry)", re.I)
RE_MOD_UNIT = re.compile(r"Modular.{0,30}?Unit\s*([12])", re.I)
RE_COORDD = re.compile(r"\b0654\b|[Cc]o-?ordinated|[Dd]ouble\s*[Aa]ward", re.I)
RE_COMBINED = re.compile(r"\b0653\b|[Cc]ombined\s*[Ss]cience", re.I)

RE_0610 = re.compile(r"\b0?610\b|\b0973\b", re.I)
RE_0620 = re.compile(r"\b0620\b|\b0971\b", re.I)
RE_0625 = re.compile(r"\b0625\b|\b0972\b", re.I)
RE_0417 = re.compile(r"\b0417\b", re.I)
RE_4IT0 = re.compile(r"\b4IT0\b|Edexcel\s+i?GCSE\s+ICT|ICT\s+Paper\s*\d", re.I)
RE_ED_CS = re.compile(r"Edexcel\s+(i)?GCSE\s+Computer\s+Science", re.I)
RE_4MA1 = re.compile(r"\b4MA1\b|\b4MB\b|IGCSE\s+Math|IGCSE\s+Further\s+Maths?\b.{0,30}Edexcel", re.I)
RE_0606 = re.compile(r"\b0606\b|[Aa]dd(itional)?\s*[Mm]aths", re.I)
RE_0452 = re.compile(r"\b0452\b|IGCSE\s+Account", re.I)
RE_0455 = re.compile(r"\b0455\b|IGCSE\s+Economics|IGCSE\s+Econ", re.I)
RE_0680 = re.compile(r"\b0680\b|[Ee]nvironmental\s+[Mm]anagement|\bE\.?M\.?\b\s*(paper|revision|topic)", re.I)
RE_8291 = re.compile(r"\b8291\b|AS\s+Environmental", re.I)
RE_0460 = re.compile(r"\b0460\b|\b0976\b|IGCSE\s+Geography", re.I)
RE_4GE0 = re.compile(r"\b4GE0\b|Edexcel\s+i?GCSE\s+Geography", re.I)
RE_0500 = re.compile(r"\b0500\b|[Ff]irst\s+[Ll]anguage\s+[Ee]nglish|directed\s+writing", re.I)
RE_WPH = re.compile(r"\bWPH\d?\d?\b|IAL\s+[Pp]hysics|IAS\s+[Pp]hysics|IA2\s+[Pp]hysics", re.I)
RE_WBI = re.compile(r"\bWBI\d?\d?\b|IAL\s+[Bb]iology|IAS\s+[Bb]iology|IA2\s+[Bb]iology", re.I)
RE_WCH = re.compile(r"\bWCH\d?\d?\b|IAL\s+[Cc]hemistry|IAS\s+[Cc]hemistry|IA2\s+[Cc]hemistry", re.I)
RE_9708 = re.compile(r"\b9708\b", re.I)
RE_0475 = re.compile(r"\b0475\b|Study\s+Guide\s+for\s+Cambridge|Songs\s+of\s+Ourselves", re.I)

def paper_num(title):
    cands = []
    m = re.search(r"\bPaper\s*(\d{1,2})\b", title, re.I)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"\bP(\d{1,2})\b(?=[\sQ,(]|$)", title)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"_qp[_ ]?(\d{1,2})\b", title, re.I)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"\b0?(610|620|625|653|654|417|452|455|460|500|606|680|8291|460)/(\d{1,2})\d?/", title)
    if m:
        cands.append(int(m.group(2)))
    for raw in cands:
        if 1 <= raw <= 6:
            return raw
        if 11 <= raw <= 66 and raw % 10 in (1, 2, 3):
            return raw // 10
    return None

tier_b, skips = [], []
judgment = {c: [] for c in TARGETS}

def skip(prov, vid, title, reason):
    skips.append({"video": vid, "title": title[:160], "provider": prov, "reason": reason})

def route(course, vid, prov, specs_list, confidence, reason, p15b=False, board=False):
    judgment[course].append({"id": vid, "provider": prov, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p15b": p15b, "crossReg": board})

def tb(course_list, vid, prov, title, code, cross=False):
    for course in course_list:
        tier_b.append({"id": vid, "title": title, "provider": prov, "courses": [course],
                       "code": code, "kind": "past-paper-walkthrough",
                       "p15b": course in P15B, "crossReg": cross})

# ---------------------------------------------------------------- guidance gate
def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|Q\s?\d|paper\s*\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

# ---------------------------------------------------------------- bind ladder
def bind_course(course, vid, prov, t, p15b=None):
    if p15b is None:
        p15b = course in P15B
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p15b)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p15b)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p15b)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p15b)
            return True
    return False

# ---------------------------------------------------------------- P15 pool laws
COORD_TRIO = ["cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
              "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
              "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry"]
COMBO_TRIO = ["cie-igcse-science-combined-science-23-biology",
              "cie-igcse-science-combined-science-23-physics",
              "cie-igcse-science-combined-science-23-chemistry"]

def ig_science_anchor(pools_codes, vid, prov, t):
    """CIE IGCSE single-science session-paper anchors."""
    out = []
    if RE_0610.search(t):
        out.append("cie-igcse-biology-23")
    if RE_0620.search(t):
        out.append("cie-igcse-chemistry-23")
    if RE_0625.search(t):
        out.append("cie-igcse-physics-23")
    return out

def ma_routes(t):
    """4MA1 register routing: higher/foundation/modular-24."""
    out = []
    mm = RE_MOD_UNIT.search(t)
    if mm:
        lvl = "higher" if re.search(r"higher", t, re.I) else ("foundation" if re.search(r"foundation", t, re.I) else None)
        if lvl:
            out.append(f"igcse-maths-a-modular-24-{lvl}-unit-{mm.group(1)}")
            return out
        out += [f"igcse-maths-a-modular-24-higher-unit-{mm.group(1)}",
                f"igcse-maths-a-modular-24-foundation-unit-{mm.group(1)}"]
        return out
    hf = None
    if re.search(r"\b[12]H\b|\bHigher\b", t, re.I):
        hf = "igcse-maths-a-18-higher"
    elif re.search(r"\b[12]F\b|\bFoundation\b", t, re.I):
        hf = "igcse-maths-a-18-foundation"
    if hf:
        out.append(hf)
    else:
        out += ["igcse-maths-a-18-higher", "igcse-maths-a-18-foundation"]
    return out

def judge_pool(slug, laws):
    for v in pool:
        if v["provider"] != slug:
            continue
        vid, t = v["id"], v["title"]
        # universal honesty gates
        if RE_OLEVEL.search(t):
            skip(slug, vid, t, "O-Level register (4024/2281/... code) — no O-Level course in the spine")
            continue
        if RE_ED_CS.search(t):
            skip(slug, vid, t, "Edexcel UK-GCSE Computer Science — no spine course (the spine carries CIE 0478, not the UK GCSE CS)")
            continue
        laws(vid, t)

def with_ladder(vid, t, courses, anchor_tests, prov):
    """anchor_tests: list of (regex_tests, course_list_fn) — first hit anchors; else ladder."""
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    for label, test, courses_fn in anchor_tests:
        if test(t):
            cl = courses_fn(t)
            if cl:
                pn = paper_num(t)
                sm = RE_SESSION.search(t)
                for c in cl:
                    tb([c], vid, prov, t,
                       f"session/paper register anchor: {label}" + (f", paper {pn}" if pn else "") +
                       (f", session '{sm.group(0)[:24]}'" if sm else ""))
                return
    for c in courses:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

# ---- chem bio by Hosni: 0610 + 0620 + WBI/WCH IAL units + Ed-IGCSE? (his register: CIE IGCSE sciences + IAL bio/chem)
def law_hosni(vid, t):
    prov = "chem-bio-hosni"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WBI.search(t) or RE_WCH.search(t):
        un = re.search(r"Unit\s*([1-6])", t)
        sess = RE_SESSION.search(t)
        if un and (sess or re.search(r"past|paper|solved|walkthrough", t, re.I)):
            if RE_WBI.search(t) or re.search(r"biolog", t, re.I):
                tb(["ial-biology-18"], vid, prov, t,
                   f"IAL biology Unit {un.group(1)} + session/paper reference — unit-paper review anchor (the P14 Assil law analog)")
            else:
                tb(["ial-chemistry-17"], vid, prov, t,
                   f"IAL chemistry Unit {un.group(1)} + session/paper reference — unit-paper review anchor (the P14 Assil law analog)")
            return
        course = "ial-biology-18" if (RE_WBI.search(t) or re.search(r"biolog", t, re.I)) else "ial-chemistry-17"
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, f"IAL unit title with no distinctive match in {course} at the df<=3 bar")
        return
    cl = ig_science_anchor(None, vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in ["cie-igcse-biology-23", "cie-igcse-chemistry-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_cie_trio(vid, t):
    prov = None
    # generic CIE IGCSE sciences law (caie-made-easier / learn-today-igcse)
    with_ladder(vid, t, ["cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23"],
                [("0610", lambda x: bool(RE_0610.search(x) and (RE_SESSION.search(x) or RE_SOLVED.search(x))), lambda x: ["cie-igcse-biology-23"]),
                 ("0620", lambda x: bool(RE_0620.search(x) and (RE_SESSION.search(x) or RE_SOLVED.search(x))), lambda x: ["cie-igcse-chemistry-23"]),
                 ("0625", lambda x: bool(RE_0625.search(x) and (RE_SESSION.search(x) or RE_SOLVED.search(x))), lambda x: ["cie-igcse-physics-23"])],
                CURRENT_PROV[0])

def law_science_and_stuff(vid, t):
    prov = "science-and-stuff"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_COORDD.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        # shared-paper anchor: one 0654 paper covers all three sciences (the P13 shared-unit precedent)
        tb(COORD_TRIO, vid, prov, t, "0654 co-ordinated sciences session/paper anchor — shared-paper binding to all three sciences (disclosed)")
        return
    if RE_COMBINED.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        tb(COMBO_TRIO, vid, prov, t, "0653 combined science session/paper anchor — shared-paper binding to all three sciences (disclosed)")
        return
    cl = ig_science_anchor(None, vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in COORD_TRIO + ["cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_ict_nicos(vid, t):
    prov = "nicos-paphitis"
    with_ladder(vid, t, ["cie-igcse-ict-21"],
                [("0417", lambda x: bool(RE_0417.search(x) and (RE_SESSION.search(x) or RE_SOLVED.search(x) or re.search(r"paper\s*\d", x, re.I))), lambda x: ["cie-igcse-ict-21"])],
                prov)

def law_ict_harrison(vid, t):
    prov = "mark-harrison"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4IT0.search(t) or re.search(r"ICT\s+Paper", t, re.I):
        tb(["igcse-ict-17"], vid, prov, t, "Edexcel IGCSE ICT paper register anchor")
        return
    if RE_0417.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
        return
    for c in ["igcse-ict-17", "cie-igcse-ict-21"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_maths_pad(vid, t):
    prov = CURRENT_PROV[0]
    has_code = bool(RE_SESSION.search(t) or re.search(r"\b[12][HF]\b", t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4MA1.search(t) or re.search(r"IGCSE\s+Math", t, re.I):
        cl = ma_routes(t)
        pn = paper_num(t)
        sm = RE_SESSION.search(t)
        for c in cl:
            tb([c], vid, prov, t, "4MA1 maths-A paper anchor" +
               (f" ({'higher' if 'higher' in c else ('foundation' if 'foundation' in c else 'modular')})" if len(cl) == 1 else " — register not stated in title, both tiers bound (disclosed)") +
               (f", paper {pn}" if pn else "") + (f", session '{sm.group(0)[:24]}'" if sm else ""))
        return
    for c in ["igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
              "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
              "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_0606(vid, t):
    prov = CURRENT_PROV[0]
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0606.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 additional maths session/paper register anchor")
        return
    targets = ["cie-igcse-further-maths-additional-maths-25"]
    if RE_0620.search(t):
        targets = ["cie-igcse-chemistry-23", "cie-igcse-further-maths-additional-maths-25"]
    for c in targets:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_ial_phys_doctorno(vid, t):
    prov = "doctor-no-science"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WPH.search(t):
        un = re.search(r"Unit\s*([1-6])", t)
        sess = RE_SESSION.search(t)
        if un and (sess or re.search(r"past|paper|solved|walkthrough", t, re.I)):
            tb(["ial-physics-19"], vid, prov, t,
               f"IAL physics Unit {un.group(1)} + session/paper reference — unit-paper review anchor (the P14 Assil law analog)")
            return
        if bind_course("ial-physics-19", vid, prov, t):
            return
        skip(prov, vid, t, "IAL physics title with no distinctive match in ial-physics-19 at the df<=3 bar")
        return
    if RE_0625.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        tb(["cie-igcse-physics-23"], vid, prov, t, "CIE IGCSE physics session/paper register anchor")
        return
    for c in ["ial-physics-19", "cie-igcse-physics-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_taughtly(vid, t):
    prov = "taughtly"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0500.search(t) and (RE_SESSION.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-english-language-20", "cie-igcse-english-language-25"]:
            tb([c], vid, prov, t, "0500 First Language English paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-igcse-english-language-20", "cie-igcse-english-language-25"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_em(vid, t):
    prov = CURRENT_PROV[0]
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_8291.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-as-environmental-management-20"], vid, prov, t, "8291 AS environmental management paper register anchor")
        return
    if RE_0680.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-igcse-environmental-management-25"], vid, prov, t, "0680 environmental management paper register anchor")
        return
    for c in ["cie-igcse-environmental-management-25", "cie-as-environmental-management-20"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_geohacks(vid, t):
    prov = "geo-hacks"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4GE0.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["igcse-geography-19"], vid, prov, t, "Edexcel 4GE0 IGCSE geography paper register anchor")
        return
    if RE_0460.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-geography-20", "cie-igcse-geography-25"]:
            tb([c], vid, prov, t, "0460 IGCSE geography paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-igcse-geography-20", "cie-igcse-geography-25", "igcse-geography-19"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_keenmindz(vid, t):
    prov = "keen-mindz"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0452.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_anjuli(vid, t):
    prov = "learn-econ-anjuli"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9708.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-a-level-economics-23"], vid, prov, t, "9708 A-level economics paper register anchor")
        return
    if RE_0455.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
            tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-igcse-economics-20", "cie-igcse-economics-25", "cie-a-level-economics-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_belal(vid, t):
    prov = "belal-sir-chem-bio"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "AQA/OCR/IB-board register — out-of-spine board (channel is a mixed-register chemistry/biology channel)")
        return
    if RE_ED_IG.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        course = "igcse-biology-19" if re.search(r"biolog", t, re.I) else "igcse-chemistry-19"
        tb([course], vid, prov, t, "Edexcel IGCSE science paper register anchor")
        return
    if RE_0620.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        tb(["cie-igcse-chemistry-23"], vid, prov, t, "CIE 0620 session/paper register anchor")
        return
    for c in ["igcse-chemistry-19", "cie-igcse-chemistry-23", "igcse-biology-19"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

CURRENT_PROV = [None]

def main():
    LAWS = {
        "chem-bio-hosni": law_hosni,
        "caie-made-easier": law_cie_trio,
        "learn-today-igcse": law_cie_trio,
        "science-and-stuff": law_science_and_stuff,
        "nicos-paphitis": law_ict_nicos,
        "mark-harrison": law_ict_harrison,
        "the-math-pad": law_maths_pad,
        "libra-maths": law_both_maths,
        "gilbert-phoon": law_both_maths,
        "shawn-hew": law_0606,
        "doctor-no-science": law_ial_phys_doctorno,
        "taughtly": law_taughtly,
        "everything-em": law_em,
        "dr-maria-emam": law_em,
        "geo-hacks": law_geohacks,
        "keen-mindz": law_keenmindz,
        "learn-econ-anjuli": law_anjuli,
        "belal-sir-chem-bio": law_belal,
    }
    for slug, law in LAWS.items():
        CURRENT_PROV[0] = slug
        n0_t, n0_a, n0_s = len(tier_b), sum(len(x) for x in judgment.values()), len(skips)
        for v in pool:
            if v["provider"] == slug:
                law(v["id"], v["title"])
        print(f"[{slug}] anchors +{len(tier_b)-n0_t}, routed +{sum(len(x) for x in judgment.values())-n0_a}, skips +{len(skips)-n0_s}", flush=True)

    # NT/UK-GCSE honesty pass (any title slipping through pools' laws is already skip-ledgered;
    # a final sanity pass asserts no NT-board titles routed)
    nt_leak = [r for vs in judgment.values() for r in vs if RE_NT_BOARD.search(TITLE_OF[r['id']])]
    for r in nt_leak:
        r["action"] = "skip"
        r["reason"] = "NT-board register caught on the final sanity pass — re-adjudicated to skip"
        skips.append({"video": r["id"], "title": TITLE_OF[r["id"]][:160], "provider": r["provider"], "reason": r["reason"]})

    json.dump(tier_b, open(f"{WORK}/tier-b.json", "w"), indent=1)
    json.dump(judgment, open(f"{WORK}/judgment.json", "w"), indent=1)
    json.dump(skips, open(f"{WORK}/skips.json", "w"), indent=1)
    json.dump(reserved, open(f"{WORK}/reserved.json", "w"), indent=1)
    routed = {p["id"] for p in tier_b} | {r["id"] for vs in judgment.values() for r in vs if r["action"] == "keep"}
    print(f"\ntier B anchors: {len(tier_b)} rows over {len({p['id'] for p in tier_b})} videos")
    print(f"tier A keeps: {sum(1 for vs in judgment.values() for r in vs if r['action']=='keep')}")
    print(f"skips: {len(skips)} | reserved: {len(reserved)}")
    print(f"routed+skips+reserved = {len(routed) + len(skips) + len(reserved)} of {len(pool) + len(reserved)} accounts (target exactly-once)")
    json.dump({"tierBRows": len(tier_b), "tierBVideos": len({p['id'] for p in tier_b}),
               "tierAKeeps": sum(1 for vs in judgment.values() for r in vs if r['action'] == 'keep'),
               "skips": len(skips), "reserved": len(reserved), "poolUploads": len(pool) + len(reserved),
               "p15bCourses": P15B}, open(f"{WORK}/judgment_summary.json", "w"), indent=1)

# libra/gilbert: 4MA1 + 0606 dual register — maths-pad law then 0606 law
def law_both_maths(vid, t):
    prov = CURRENT_PROV[0]
    has_code = bool(RE_SESSION.search(t) or re.search(r"\b[12][HF]\b", t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0606.search(t):
        law_0606_inner(vid, t, prov)
        return
    if RE_4MA1.search(t) or re.search(r"IGCSE\s+Math", t, re.I):
        law_maths_inner(vid, t, prov)
        return
    for c in ["cie-igcse-further-maths-additional-maths-25", "igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
              "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
              "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_0606_inner(vid, t, prov):
    if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I):
        tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 additional maths session/paper register anchor")
        return
    if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
        return
    skip(prov, vid, t, "0606 title with no distinctive match at the df<=3 bar")

def law_maths_inner(vid, t, prov):
    cl = ma_routes(t)
    pn = paper_num(t)
    sm = RE_SESSION.search(t)
    for c in cl:
        tb([c], vid, prov, t, "4MA1 maths-A paper anchor" +
           (f" ({'higher' if 'higher' in c else ('foundation' if 'foundation' in c else 'modular')})" if len(cl) == 1 else " — register not stated in title, both tiers bound (disclosed)") +
           (f", paper {pn}" if pn else "") + (f", session '{sm.group(0)[:24]}'" if sm else ""))

TITLE_OF = {}

if __name__ == "__main__":
    for v in pool:
        TITLE_OF[v["id"]] = v["title"]
    for r in reserved:
        TITLE_OF.setdefault(r["video"], r["title"])
    main()
