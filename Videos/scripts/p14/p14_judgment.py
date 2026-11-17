#!/usr/bin/env python3
"""P14 judgment: route the 12 judgment pools (T1 x10 + T2 x2, 18,005 uploads) onto the
covered spine + the 5 NT pools' pool-level skip ledger + the Allery-CIE re-adjudication
group (41 candidates over the P2F pool of record). The P13 gate ladder extended:

  Tier B   paper-code anchors   — machine-checkable session/paper codes in titles
                                 (method paper-code, confidence high, specs [], kind
                                 past-paper-walkthrough). CIE paper-number routing per
                                 subject (P13 law); 0580 papers 2/4 -> extended, 1/3 ->
                                 core (P9 law); WMA01 C12 / WMA02 C34 IAL-legacy composites
                                 -> two units each (P9 law); 9702/41/M/J/10 slash form.
  Class M  section markers      — "N.M" titles bind that subtopic's points, confidence low
  Class S  section-name binding — verbatim pipe/dash field equality (P13 gate; node norm
                                 >= 8 chars, SUBTOPIC preferred)
  Tier A   distinctive-token    — df<=3 token binds, confidence medium/low
  Class L  topic lectures       — four-gate topic-lecture class (P12/P13)
  skips    honest ledger        — guidance/advice/marketing, O-Level register, out-of-spine
                                 boards (AQA/OCR/IB/NCERT/GCSE/9MA0), bare GCE session
                                 walkthroughs (ANCHOR-GRANULARITY §6 — a GCE paper is
                                 evidence about the GCE qualification; no GCE course in the
                                 spine; the P9 precedent), FP2/FP3/S3/S4/M3-5 (no course),
                                 no-binding, no-cluster.
  reserved lit-21               — IGCSESUCCESS 0475 titles: owner decision point (P12
                                 terminal declaration vs first-ever lit-21 content); ledgered
                                 separately, NOT silently skipped.

Cross-register teaching binds (ExamSolutions old-GCE module tokens -> IAL unit courses;
the P10 Arnolds S1/S2 precedent) land at boardMismatch true, confidence low.

AS sciences (cie-as-{physics,chemistry,biology}-25) are inherit CHILDREN (P4 map) — their
direct rows carry p14b=True (builder post-inherit section, the P11B/P13B shape). AS maths
unit courses and cie-as-computer-science-19 are NOT inherit children — pre-inherit.

Outputs work/p14/: tier-b.json, tier-a.json, judgment.json, skips.json, reserved-lit21.json
"""
import json, os, re, datetime
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub"
WORK = "/home/z/my-project/work/p14"
UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs(WORK, exist_ok=True)

# ---------------------------------------------------------------- pools
JUDGMENT_POOLS = ["etphysics", "prosperity-academy", "dr-hanaa-assil", "zainematics",
                  "craigndave", "science-with-hazel", "mega-lecture", "examsolutions",
                  "sir-faizan-pasha", "ck-a-level-physics", "igcsesuccess", "mr-astbury-maths"]
NT_POOLS = {"tlmaths": "OCR/AQA A-level maths register — no spine qualification (recon NT)",
            "physics-by-m-anwar": "NCERT (India) physics register — no spine qualification (recon NT)",
            "takingthebiz": "business guidance register — no spine qualification (recon NT)",
            "accounting-lecture": "accounting register outside the spine's qualifications (recon NT)",
            "the-econ-show": "channel EMPTY at re-verification (recon NT; honest zero)"}

pool = []
_seen = set()
for slug in JUDGMENT_POOLS:
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        if v["id"] in _seen:
            continue
        _seen.add(v["id"])
        pool.append({"id": v["id"], "title": v["title"], "provider": slug})

# ---------------------------------------------------------------- spine
TARGETS = ["cie-a-level-physics-25", "cie-as-physics-25",
           "cie-a-level-chemistry-25", "cie-as-chemistry-25",
           "cie-a-level-biology-25", "cie-as-biology-25",
           "cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics",
           "cie-a-level-maths-20-probability-and-statistics-1", "cie-as-maths-20-probability-and-statistics-1",
           "cie-a-level-maths-20-probability-and-statistics-2",
           "cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1",
           "cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2",
           "cie-a-level-maths-20-pure-3",
           "cie-a-level-economics-23", "cie-a-level-accounting-21", "cie-as-accounting-21",
           "cie-a-level-computer-science-19", "cie-as-computer-science-19",
           "cie-igcse-maths-25-core", "cie-igcse-maths-25-extended",
           "cie-igcse-further-maths-additional-maths-25",
           "cie-igcse-computer-science-23",
           "cie-igcse-english-language-20", "cie-igcse-english-language-25",
           "igcse-maths-a-18-higher",
           "igcse-biology-19", "igcse-chemistry-19", "igcse-physics-19",
           "cie-igcse-chemistry-23", "cie-igcse-physics-23", "cie-igcse-biology-23",
           "igcse-chemistry-modular-24-unit-1", "igcse-chemistry-modular-24-unit-2",
           "ial-chemistry-17",
           "ial-maths-20-pure-1", "ial-maths-20-pure-2", "ial-maths-20-pure-3", "ial-maths-20-pure-4",
           "ial-maths-20-mechanics-1", "ial-maths-20-mechanics-2",
           "ial-maths-20-statistics-1", "ial-maths-20-statistics-2",
           "ial-maths-20-decision-1", "ial-further-maths-18-further-pure-1"]
P4_CHILDREN = set(json.load(open(f"{RES}/Videos/drafts/_p4/inheritance-map.json"))["parents"].keys())

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
9618 0478 0580 0606 0500 0455 9608 0620 0625 0610 2281 4024 5070 5090 5124 2210
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
    r"|\b(?:ON|MJ|FM|F/M|M/J|O/N)[ ]?20?\d\d\b|_(?:s|w|q)\d{2}_|/M/J/\d{2}|/O/N/\d{2}"
    r"|\b(?:may|june|oct|nov)\s*20\d\d|\bm/j\b|\bo/n\b|\bqp\b)", re.I)
RE_SOLVED = re.compile(r"solved|solution|walkthrough|past[- ]?paper|qp\s*_?\d|mark scheme|\bQ\s?\d|\bQ\(|question\s*\d|exam questions?|predictions?!? paper|\bcomplete\b", re.I)
RE_GUIDE = re.compile(
    r"tips|tricks?\b|ace your|how to (ace|finish|overcome|stop|prepare|revise|get full|write|score)|how (do i|this student|did paper)|"
    r"survival guide|preparation course|orientation|watch (this|before)|podcast|success|result day|"
    r"interview|vision|challenge|parents? of|update|tour|platform|worried|nervous|resit|message|"
    r"days? left|30 days|60 days|join now|score an a\*|a\* in|game.?chang|blended|covid|"
    r"studysmart|aitutor|revision in|month left|marking schemes|what you (need|can)|can't miss|"
    r"paper breakdown|important topics|fix of|lifesaver|one thing|stress|focus on what|predictions?!"
    r"|sneak preview|live class|whatsapp|daily dose|the reality of|full marks|made easy|sneak peek", re.I)
RE_OLEVEL = re.compile(r"\bO\s?-?\s?Levels?\b|\bOL\b|\b4024\b|\b2281\b|\b5070\b|\b5090\b|\b5124\b|\b2210\b|\b4037\b", re.I)
RE_NT_BOARD = re.compile(r"\bAQA\b|\bOCR\b|\bIB\b|\bNCERT\b|\bCBSE\b|\bJEE\b|\bNEET\b|\bGCSE\b|\bKey Stage\b|\bKS[1-4]\b|\bAP\b|\bSAT\b|\bMEI\b")
RE_AS_REG = re.compile(r"\bAS\s+Level\b|\bAS\s+Chem\b|\bAS\s+Physic|\bAS\s+Biolog|\bAS\s+Account|\bAS\s+Econom|\bAS\s+Math|\bIAS\b|\bAS\s*[-|]|\(\s*AS\s*\)|\bAS\b\s*$", re.I)
RE_A2_REG = re.compile(r"\bA2\b|\bA[- ]?Level\b|\bIAL\b|\bA2s?\b|\(\s*A2\s*\)", re.I)
RE_REG_FALLBACK = re.compile(r"\b(AS|A2)\s+(Chemistry|Physics|Biology)\b|\b(Chemistry|Physics|Biology)\s+(AS|A2)\b", re.I)
REG_FALLBACK_CLUSTER = {("AS", "Chemistry"): "chem9701", ("A2", "Chemistry"): "chem9701",
                        ("AS", "Physics"): "phys9702", ("A2", "Physics"): "phys9702",
                        ("AS", "Biology"): "bio9700", ("A2", "Biology"): "bio9700"}
PHYSICS_POOLS = ("ck-a-level-physics", "sir-faizan-pasha")
RE_ED_IG = re.compile(r"Edexcel\s+IGCSE|IGCSE.{0,40}Edexcel|\b4MA1\b|\b4PH1\b|\b4CH1\b|\b4BI1\b", re.I)
RE_IAL_CHEM_UNIT = re.compile(r"Unit\s*([1-6]).{0,60}?(AS|A2|IAS|IA2|A[- ]?Level).{0,30}?Chem(istry)?|Chem(istry)?.{0,30}?(AS|A2|IAS|IA2).{0,40}?Unit\s*([1-6])", re.I)
RE_MOD_UNIT = re.compile(r"Modular\s+Unit\s*([12])", re.I)
RE_IG_CHEM_PAPER = re.compile(r"Paper\s*([12])\s*(CR|HR|C|H)?\b|1CR|2CR|1HR|2HR", re.I)
OLD_GCE_UNIT = {"C1": "ial-maths-20-pure-1", "C2": "ial-maths-20-pure-2", "C3": "ial-maths-20-pure-3",
                "C4": "ial-maths-20-pure-4", "M1": "ial-maths-20-mechanics-1", "M2": "ial-maths-20-mechanics-2",
                "S1": "ial-maths-20-statistics-1", "S2": "ial-maths-20-statistics-2",
                "FP1": "ial-further-maths-18-further-pure-1", "D1": "ial-maths-20-decision-1"}
RE_C12_C34 = re.compile(r"\bC12\b|\bC34\b|International\s+Core\s+Maths|WMA01|WMA02", re.I)
RE_BARE_GCE_UNIT = re.compile(r"\b(C[1-4]|M[1-5]|S[1-4]|FP[1-3]|D1)\b")
RE_9MA0 = re.compile(r"\b9MA0\b|\b9FM0\b|A[- ]?Level\s+Maths?\b.*Paper|Paper\s+[12]\s.*A[- ]?Level|Edexcel\s+A[- ]?Level", re.I)
RE_0475 = re.compile(r"\b0475\b|Literature", re.I)
RE_0500 = re.compile(r"\b0500\b|First\s+Language\s+English", re.I)
RE_CIE_TOPIC = re.compile(r"CIE\s+Topic\s*(\d+)", re.I)

RE_CODE_9702 = re.compile(r"\b9702\b")
RE_CODE_9701 = re.compile(r"\b9701\b")
RE_CODE_9700 = re.compile(r"\b9700\b")
RE_CODE_9709 = re.compile(r"\b9709\b")
RE_CODE_9708 = re.compile(r"\b9708\b")
RE_CODE_9706 = re.compile(r"\b9706\b")
RE_CODE_9609 = re.compile(r"\b9609\b")
RE_CODE_9618 = re.compile(r"\b9618\b")
RE_CODE_0580 = re.compile(r"\b0580\b")
RE_CODE_0606 = re.compile(r"\b0606\b")
RE_CODE_0478 = re.compile(r"\b0478\b|0478-0984")
RE_CODE_0620 = re.compile(r"\b0620\b")
RE_CODE_0625 = re.compile(r"\b0625\b")
RE_CODE_0610 = re.compile(r"\b0610\b")

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
    m = re.search(r"\b9(?:702|701|700|709|708|706|609|618)/(\d{1,2})\d?/", title)
    if m:
        cands.append(int(m.group(1)))
    for raw in cands:
        if 1 <= raw <= 6:
            return raw
        if 11 <= raw <= 66 and raw % 10 in (1, 2, 3):
            return raw // 10
    return None

def unit_token(title):
    m = RE_BARE_GCE_UNIT.search(title)
    return m.group(1) if m else None

tier_b, skips, reserved = [], [], []
judgment = {c: [] for c in TARGETS}

def skip(prov, vid, title, reason):
    skips.append({"video": vid, "title": title[:160], "provider": prov, "reason": reason})

def route(course, vid, prov, specs_list, confidence, reason, p14b=False, board=False):
    judgment[course].append({"id": vid, "provider": prov, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p14b": p14b, "crossReg": board})

def tb(course_list, vid, prov, title, code, cross=False):
    for course in course_list:
        tier_b.append({"id": vid, "title": title, "provider": prov, "courses": [course],
                       "code": code, "kind": "past-paper-walkthrough",
                       "p14b": course in P4_CHILDREN, "crossReg": cross})

# ---------------------------------------------------------------- per-cluster Tier B routes
def tb_science(cluster, n, title):
    if cluster == "phys9702":
        return [("cie-as-physics-25", True)] if n in (1, 2, 3) else ([("cie-a-level-physics-25", False)] if n in (4, 5) else [])
    if cluster == "chem9701":
        return [("cie-as-chemistry-25", True)] if n in (1, 2) else ([("cie-a-level-chemistry-25", False)] if n in (4, 5) else [])
    if cluster == "bio9700":
        return [("cie-as-biology-25", True)] if n in (1, 2, 3) else ([("cie-a-level-biology-25", False)] if n in (4, 5) else [])
    return []

def tb_maths(n):
    return {1: ["cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1"],
            2: ["cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2"],
            3: ["cie-a-level-maths-20-pure-3"],
            4: ["cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics"],
            5: ["cie-a-level-maths-20-probability-and-statistics-1", "cie-as-maths-20-probability-and-statistics-1"],
            6: ["cie-a-level-maths-20-probability-and-statistics-2"]}.get(n, [])

def tb_ig_maths(n):
    return ["cie-igcse-maths-25-extended"] if n in (2, 4) else (["cie-igcse-maths-25-core"] if n in (1, 3) else [])

def tb_cs(n):
    return ["cie-as-computer-science-19"] if n in (1, 2) else (["cie-a-level-computer-science-19"] if n in (3, 4) else [])

# ---------------------------------------------------------------- guidance gate
def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|Q\s?\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

# ---------------------------------------------------------------- bind ladder
def bind_course(course, vid, prov, t, p14b=None, cross=False):
    if p14b is None:
        p14b = course in P4_CHILDREN  # inherit children take direct rows POST-inherit
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p14b, cross)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p14b, cross)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p14b, cross)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p14b, cross)
            return True
    return False

# ---------------------------------------------------------------- ExamSolutions law
def examsolutions(vid, prov, t):
    ut = unit_token(t)
    intl_legacy = bool(re.search(r"\bC12\b|\bC34\b|WMA01|WMA02", t))
    sess = bool(RE_SESSION.search(t))
    ocr_aqa = bool(re.search(r"\bOCR\b|\bAQA\b|\bMEI\b", t, re.I))
    if intl_legacy and sess:
        # P9 law: WMA01 C12 / WMA02 C34 IAL-legacy composites -> two units each
        pairs = {"C12": ["ial-maths-20-pure-1", "ial-maths-20-pure-2"],
                 "C34": ["ial-maths-20-pure-3", "ial-maths-20-pure-4"]}
        m = re.search(r"\b(C12|C34)\b", t)
        units = pairs[m.group(1)] if m else ["ial-maths-20-pure-1", "ial-maths-20-pure-2"]
        sm = RE_SESSION.search(t)
        tb(units, vid, prov, t, f"IAL-legacy composite {m.group(1) if m else 'C12'} + session '{sm.group(0) if sm else '?'}' (P9 law)", cross=False)
        return
    if ut and ocr_aqa:
        skip(prov, vid, t, f"OCR/AQA/MEI-board GCE {ut} title — out-of-spine board (P9 precedent: OCR/AQA/MEI skipped)")
        return
    if ut and ut in ("FP2", "FP3", "S3", "S4", "M3", "M4", "M5"):
        skip(prov, vid, t, f"old-GCE {ut} — no corresponding IAL unit course in the spine (the P10 FP2 owner note class)")
        return
    if ut and ut in OLD_GCE_UNIT and sess and RE_SOLVED.search(t):
        skip(prov, vid, t, f"bare GCE {ut} session walkthrough — ANCHOR-GRANULARITY §6: a GCE paper is evidence about the GCE qualification, no GCE course in the spine (P9 precedent)")
        return
    if ut and ut in OLD_GCE_UNIT:
        # teaching title with module token -> cross-register bind (P10 Arnolds S1/S2 precedent)
        course = OLD_GCE_UNIT[ut]
        if bind_course(course, vid, prov, t, False, cross=True):
            return
        skip(prov, vid, t, f"old-GCE {ut} teaching title with no distinctive match in {course} at the df<=3 bar")
        return
    if RE_9MA0.search(t) or (sess and RE_SOLVED.search(t)):
        skip(prov, vid, t, "new-GCE (9MA0) or session-paper title without a module token — no spine course (ANCHOR-GRANULARITY §6)")
        return
    skip(prov, vid, t, "ExamSolutions title without a module register — no honest unit-course route")

# ---------------------------------------------------------------- Assil law
def assil(vid, prov, t):
    mm = RE_MOD_UNIT.search(t)
    if mm:
        course = f"igcse-chemistry-modular-24-unit-{mm.group(1)}"
        if bind_course(course, vid, prov, t, p14b=course in P4_CHILDREN):
            return
        skip(prov, vid, t, f"'Modular Unit {mm.group(1)}' review title with no distinctive match in {course} at the df<=3 bar")
        return
    ial_unit = bool(RE_IAL_CHEM_UNIT.search(t) or (re.search(r"Unit\s*[1-6]\b", t) and re.search(r"(AS|A2|IAS|IA2)", t) and re.search(r"Chem", t, re.I)))
    if ial_unit and RE_SESSION.search(t):
        # the IAL analog of the P11 W-code law: "Unit N <session>" IS the machine-checkable
        # unit-paper reference (Unit 3 Oct 2022 = WCH13 session paper review; the channel's
        # "Unit N <session> AS/A2 Chemistry Edexcel" series is its unit-paper review register)
        sm = RE_SESSION.search(t)
        un = re.search(r"Unit\s*([1-6])", t)
        tb(["ial-chemistry-17"], vid, prov, t,
           f"IAL chemistry Unit {un.group(1) if un else '?'} + session '{sm.group(0)}' — unit-paper review anchor (P11 W-code law analog)")
        return
    if ial_unit:
        if bind_course("ial-chemistry-17", vid, prov, t):
            return
        skip(prov, vid, t, "IAL chemistry unit title (no session) with no distinctive match in ial-chemistry-17 at the df<=3 bar")
        return
    if re.search(r"IGCSE", t, re.I):
        m = RE_IG_CHEM_PAPER.search(t)
        if m and sess_ok(t):
            tb(["igcse-chemistry-19"], vid, prov, t, f"Edexcel IGCSE chemistry paper ref '{m.group(0)}' + session")
            return
        if bind_course("igcse-chemistry-19", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE chemistry title with no distinctive match in igcse-chemistry-19 at the df<=3 bar")
        return
    if bind_course("ial-chemistry-17", vid, prov, t):
        return
    skip(prov, vid, t, "chemistry title with no unit/IGCSE register and no distinctive match")

def sess_ok(t):
    return bool(RE_SESSION.search(t))

# ---------------------------------------------------------------- Hazel law (Ed-IG register)
def ed_ig_subject(t):
    tl = t.lower()
    if re.search(r"math", tl):
        return "igcse-maths-a-18-higher"
    if re.search(r"biolog", tl):
        return "igcse-biology-19"
    if re.search(r"chem", tl):
        return "igcse-chemistry-19"
    if re.search(r"physic", tl):
        return "igcse-physics-19"
    return None

def hazel(vid, prov, t):
    subj = ed_ig_subject(t)
    if not subj:
        skip(prov, vid, t, "no Edexcel-IGCSE subject register (GCSE/IB/A-level/other register) — out of lane")
        return
    if RE_OLEVEL.search(t):
        skip(prov, vid, t, "O-Level register — no O-Level course in the spine")
        return
    if bind_course(subj, vid, prov, t):
        return
    skip(prov, vid, t, f"Ed-IG {subj} register title with no distinctive match at the df<=3 bar and no topic-unique token")

# ---------------------------------------------------------------- Astbury law
def astbury(vid, prov, t):
    if RE_OLEVEL.search(t):
        skip(prov, vid, t, "O-Level register — no O-Level course in the spine")
        return
    if re.search(r"A[- ]?Level|\bAS\b", t, re.I):
        skip(prov, vid, t, "Edexcel GCE A-level/AS maths register — no GCE maths course in the spine (ANCHOR-GRANULARITY §6)")
        return
    if ed_ig_subject(t) == "igcse-maths-a-18-higher" or RE_ED_IG.search(t):
        if bind_course("igcse-maths-a-18-higher", vid, prov, t):
            return
        skip(prov, vid, t, "Ed-IG maths register title with no distinctive match in igcse-maths-a-18-higher at the df<=3 bar")
        return
    skip(prov, vid, t, "no Ed-IG maths register — out of lane")

# ---------------------------------------------------------------- IGCSESUCCESS law
def igcsesuccess(vid, prov, t):
    if re.search(r"\b0408\b|World\s+Literature", t, re.I):
        skip(prov, vid, t, "CIE World Literature 0408 — no spine course (honest no-target)")
        return
    if re.search(r"\b0475\b", t) or re.search(r"IGCSE\s+Literature", t, re.I):
        reserved.append({"video": vid, "title": t[:160], "provider": prov,
                         "reason": "cie-igcse-english-literature-21 owner decision point (P12 terminal declaration vs the first lit-21 content ever surfaced — recon default: keep terminal) — reserved pending owner decision, not silently dropped"})
        return
    if RE_0500.search(t) or re.search(r"First Language English", t, re.I):
        ok = False
        for course in ("cie-igcse-english-language-20", "cie-igcse-english-language-25"):
            if bind_course(course, vid, prov, t):
                ok = True
        if ok:
            return
        skip(prov, vid, t, "First Language English register title with no distinctive match in either english-language course at the df<=3 bar")
        return
    skip(prov, vid, t, "no 0500/0475 register — channel meta/teaching-business register (out of lane)")

# ---------------------------------------------------------------- Craig'n'Dave law
def craigndave(vid, prov, t):
    if RE_CODE_0478.search(t):
        if bind_course("cie-igcse-computer-science-23", vid, prov, t):
            return
        skip(prov, vid, t, "0478 title with no distinctive match in cie-igcse-computer-science-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "out-of-spine qualification register (AQA 8525/7517, OCR J277/H446 GCSE/A-level CS) — honest no-target")

# ---------------------------------------------------------------- Zainematics law
def zainematics(vid, prov, t):
    # spine qualification codes take precedence over O-Level branding — the 0580/0606/9618
    # token is machine-checkable spine evidence even when the title ALSO carries 4024/2281
    # dual-qualification branding (the Zainematics umbrella format)
    has_spine_code = bool(re.search(r"\b(9618|0606|0580|9709)\b", t))
    if not has_spine_code and RE_OLEVEL.search(t):
        skip(prov, vid, t, "O-Level register (4024/2281/5070/2210) — no O-Level course in the spine")
        return
    if RE_CODE_9618.search(t):
        n = paper_num(t)
        if n and sess_ok(t) and RE_SOLVED.search(t):
            tb(tb_cs(n), vid, prov, t, f"9618 paper {n} + session")
            return
        ok = False
        for course in ("cie-a-level-computer-science-19", "cie-as-computer-science-19"):
            if bind_course(course, vid, prov, t):
                ok = True
        if ok:
            return
        skip(prov, vid, t, "9618 title with no distinctive match in either CS course at the df<=3 bar")
        return
    if RE_CODE_0606.search(t):
        n = paper_num(t)
        if n and sess_ok(t) and RE_SOLVED.search(t):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, f"0606 paper {n} + session")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in further-maths-additional-25 at the df<=3 bar")
        return
    if RE_CODE_0580.search(t):
        n = paper_num(t)
        if n and sess_ok(t) and RE_SOLVED.search(t):
            tb(tb_ig_maths(n), vid, prov, t, f"0580 paper {n} + session (P9 law: papers 2/4 extended, 1/3 core)")
            return
        ext = bool(re.search(r"extended|paper\s*[24]\b|p[24]\b", t, re.I))
        core = bool(re.search(r"core|paper\s*[13]\b|p[13]\b", t, re.I))
        course = "cie-igcse-maths-25-extended" if ext else ("cie-igcse-maths-25-core" if core else "cie-igcse-maths-25-extended")
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, f"0580 title with no distinctive match in {course} at the df<=3 bar")
        return
    if RE_CODE_9709.search(t):
        n = paper_num(t)
        if n and sess_ok(t) and RE_SOLVED.search(t):
            tb(tb_maths(n), vid, prov, t, f"9709 paper {n} + session")
            return
        unit_map = {"P1": ["cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1"],
                    "P2": ["cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2"],
                    "P3": ["cie-a-level-maths-20-pure-3"],
                    "M1": ["cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics"],
                    "S1": ["cie-a-level-maths-20-probability-and-statistics-1", "cie-as-maths-20-probability-and-statistics-1"],
                    "S2": ["cie-a-level-maths-20-probability-and-statistics-2"]}
        for u, courses in unit_map.items():
            if re.search(rf"\b{u}\b", t):
                ok = False
                for course in courses:
                    if bind_course(course, vid, prov, t):
                        ok = True
                if ok:
                    return
        skip(prov, vid, t, "9709 title with no unit token and no distinctive cross-course match at the df<=3 bar")
        return
    if RE_CODE_9618.search(t):
        return
    skip(prov, vid, t, "no spine qualification code and no register (Zainematics umbrella remainder — gaming/other/O-Level content)")
# ---------------------------------------------------------------- CIE science/maths/econ pools law
CIE_CODE_MAP = [(RE_CODE_9702, "phys9702"), (RE_CODE_9701, "chem9701"), (RE_CODE_9700, "bio9700"),
                (RE_CODE_9709, "maths9709"), (RE_CODE_9708, "econ9708"), (RE_CODE_9706, "acct9706"),
                (RE_CODE_9609, "biz9609"), (RE_CODE_9618, "cs9618"),
                (RE_CODE_0580, "ig-maths"), (RE_CODE_0606, "ig-further"), (RE_CODE_0478, "ig-cs"),
                (RE_CODE_0620, "ig-chem"), (RE_CODE_0625, "ig-phys"), (RE_CODE_0610, "ig-bio")]

def cie_generic(vid, prov, t):
    for rx, cluster in CIE_CODE_MAP:
        if rx.search(t):
            break
    else:
        cluster = None
    if cluster is None:
        # the P13 register law without a code: explicit "AS/A2 <subject>" registers route
        # (Mega Lecture's class series; CK/Faizan's 9702 teaching register by pool context)
        mreg = RE_REG_FALLBACK.search(t)
        if mreg:
            key = (mreg.group(1) or mreg.group(3), mreg.group(2) or mreg.group(4))
            cluster = REG_FALLBACK_CLUSTER.get(key)
        elif prov in PHYSICS_POOLS and re.search(r"\b(AS|A2)\b|\bPhysics\b", t):
            cluster = "phys9702"
    if cluster is None:
        skip(prov, vid, t, "no spine qualification code and no CIE level-register (CIE aggregator remainder)")
        return
    n = paper_num(t)
    solved = sess_ok(t) and RE_SOLVED.search(t)
    if cluster in ("phys9702", "chem9701", "bio9700"):
        if n and solved:
            courses = tb_science(cluster, n, t)
            if courses:
                tb([c for c, _ in courses], vid, prov, t, f"paper {n} + session (CIE paper-number routing)")
                return
        as_reg = bool(RE_AS_REG.search(t))
        course = {"phys9702": ("cie-as-physics-25", "cie-a-level-physics-25"),
                  "chem9701": ("cie-as-chemistry-25", "cie-a-level-chemistry-25"),
                  "bio9700": ("cie-as-biology-25", "cie-a-level-biology-25")}[cluster]
        target = course[0] if as_reg else course[1]
        if bind_course(target, vid, prov, t, p14b=(target in P4_CHILDREN)):
            return
        skip(prov, vid, t, f"no distinctive match in {target} at the df<=3 bar and no topic-unique token")
        return
    if cluster == "maths9709":
        if n and solved:
            courses = tb_maths(n)
            if courses:
                tb(courses, vid, prov, t, f"9709 paper {n} + session")
                return
        unit_map = {"P1": ["cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1"],
                    "P2": ["cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2"],
                    "P3": ["cie-a-level-maths-20-pure-3"],
                    "M1": ["cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics"],
                    "S1": ["cie-a-level-maths-20-probability-and-statistics-1", "cie-as-maths-20-probability-and-statistics-1"],
                    "S2": ["cie-a-level-maths-20-probability-and-statistics-2"]}
        for u, courses in unit_map.items():
            if re.search(rf"\b{u}\b", t):
                ok = False
                for course in courses:
                    if bind_course(course, vid, prov, t):
                        ok = True
                if ok:
                    return
        best = None
        for course in [c for cs in unit_map.values() for c in cs]:
            sg = section_by_field(course, t)
            if sg:
                node, pts = sg
                route(course, vid, prov, [p["code"] for p in pts], "low",
                      f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar")
                return
            b = best_point(course, t)
            if b:
                p, hits, dmax, nh = b
                dist = sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3)
                cand = (dist, -dmax, course)
                if best is None or cand > best[0]:
                    best = (cand, course, p, hits, dmax)
        if best and best[0][0] >= 2:
            _, course, p, hits, dmax = best
            conf = "medium" if best[0][0] >= 2 else "low"
            route(course, vid, prov, [p["code"]], conf,
                  f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); unit inferred cross-course")
            return
        skip(prov, vid, t, "maths title without unit tokens and no cross-course distinctive match at the df<=3 bar")
        return
    if cluster == "econ9708":
        if n and solved:
            tb(["cie-a-level-economics-23"], vid, prov, t, f"9708 paper {n} + session")
            return
        if bind_course("cie-a-level-economics-23", vid, prov, t):
            return
        skip(prov, vid, t, "no distinctive economics match at the df<=3 bar and no topic-unique token")
        return
    if cluster == "acct9706":
        as_reg = bool(RE_AS_REG.search(t))
        course = "cie-as-accounting-21" if as_reg else "cie-a-level-accounting-21"
        if n and solved:
            tb([course], vid, prov, t, f"9706 paper {n} + session")
            return
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, "no distinctive accounting match at the df<=3 bar and no topic-unique token")
        return
    if cluster == "biz9609":
        al_c, as_c = "cie-a-level-business-23", "cie-as-business-23"
        sg = section_by_field(al_c, t)
        if sg:
            node, pts = sg
            tnum = 0
            for nd in specs[al_c]["nodes"]:
                if nd["family"] == "TOPIC":
                    tnum += 1
                if nd["code"] == node["code"]:
                    break
            course = al_c if tnum > 5 else as_c
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar")
            return
        if bind_course(al_c, vid, prov, t):
            return
        if bind_course(as_c, vid, prov, t):
            return
        skip(prov, vid, t, "no distinctive business match at the df<=3 bar")
        return
    if cluster == "cs9618":
        zainematics(vid, prov, t)
        return
    if cluster == "ig-maths":
        zainematics(vid, prov, t)
        return
    if cluster == "ig-further":
        zainematics(vid, prov, t)
        return
    if cluster == "ig-cs":
        craigndave(vid, prov, t)
        return
    ig_course = {"ig-chem": "cie-igcse-chemistry-23", "ig-phys": "cie-igcse-physics-23", "ig-bio": "cie-igcse-biology-23"}[cluster]
    if n and solved:
        tb([ig_course], vid, prov, t, f"IGCSE paper {n} + session")
        return
    if bind_course(ig_course, vid, prov, t):
        return
    skip(prov, vid, t, f"no distinctive match in {ig_course} at the df<=3 bar")

# ---------------------------------------------------------------- CK / Faizan / ETphysics / Prosperity / Mega
def cie_pool(vid, prov, t):
    if RE_OLEVEL.search(t):
        skip(prov, vid, t, "O-Level register — no O-Level course in the spine")
        return
    cie_generic(vid, prov, t)

# ---------------------------------------------------------------- Allery re-adjudication group
def allery_cie(vid, prov, t):
    n = paper_num(t)
    if n and sess_ok(t) and RE_SOLVED.search(t):
        courses = tb_science("chem9701", n, t)
        if courses:
            tb([c for c, _ in courses], vid, prov, t, f"9701 paper {n} + session (re-adjudication group)")
            return
    as_reg = bool(RE_AS_REG.search(t))
    target = "cie-as-chemistry-25" if as_reg else "cie-a-level-chemistry-25"
    if bind_course(target, vid, prov, t, p14b=(target in P4_CHILDREN)):
        return
    skip(prov, vid, t, "CIE-Topic chemistry title with no distinctive match at the df<=3 bar (re-adjudication group)")

POOL_LAW = {"etphysics": cie_pool, "prosperity-academy": cie_pool, "mega-lecture": cie_pool,
            "sir-faizan-pasha": cie_pool, "ck-a-level-physics": cie_pool,
            "zainematics": zainematics, "craigndave": craigndave, "science-with-hazel": hazel,
            "dr-hanaa-assil": assil, "examsolutions": examsolutions,
            "igcsesuccess": igcsesuccess, "mr-astbury-maths": astbury}

print("=== judgment pass ===", flush=True)
for v in pool:
    vid, t, prov = v["id"], v["title"], v["provider"]
    has_code = bool(re.search(r"\b(9702|9701|9700|9709|9708|9706|9609|9618|0580|0606|0478|0500|0620|0625|0610|4MA1|4CH1|4BI1|4PH1)\b", t))
    has_reg = bool(RE_REG_FALLBACK.search(t)) or (prov in PHYSICS_POOLS and bool(re.search(r"\b(AS|A2)\b", t)))
    # the P13 guidance gate (teacher-guidance/advice/marketing excluded as bind targets;
    # code-bearing walkthroughs keep their machine-checkable route; titles carrying the
    # explicit CIE level register are teaching content even when promo strings ride along)
    if prov not in ("examsolutions", "dr-hanaa-assil") and is_guidance(t, has_code or has_reg):
        skip(prov, vid, t, "teacher-guidance/advice/marketing register — excluded as bind target")
        continue
    if prov == "examsolutions":
        examsolutions(vid, prov, t)
    elif prov == "dr-hanaa-assil":
        assil(vid, prov, t)
    elif prov == "science-with-hazel":
        hazel(vid, prov, t)
    elif prov == "mr-astbury-maths":
        astbury(vid, prov, t)
    elif prov == "igcsesuccess":
        igcsesuccess(vid, prov, t)
    elif prov == "craigndave":
        craigndave(vid, prov, t)
    elif prov == "zainematics":
        zainematics(vid, prov, t)
    else:
        cie_pool(vid, prov, t)

# Allery re-adjudication group (41 candidates over the P2F pool of record)
ra = json.load(open(f"{RES}/Videos/scripts/p14/p14_readjudication.json"))
allery_cands = ra.get("allery-chemistry-cie", {}).get("cieCandidates", [])
for c in allery_cands:
    allery_cie(c["id"], "allery-chemistry-p2f", c["title"])

# ---------------------------------------------------------------- NT pools (pool-level skip ledger)
nt_skipped = 0
for slug, reason in NT_POOLS.items():
    try:
        vs = json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]
    except FileNotFoundError:
        continue
    for v in vs:
        if v["id"] in _seen:
            continue  # already dispositioned in a judgment pool (shouldn't happen: 0 overlap verified)
        _seen.add(v["id"])
        skip(slug, v["id"], v["title"], reason)
        nt_skipped += 1

# ---------------------------------------------------------------- exactly-once check
tb_vids = {x["id"] for x in tier_b}
routed_vids = set()
for course, rows in judgment.items():
    for r in rows:
        routed_vids.add(r["id"])
all_judged = tb_vids | routed_vids
skipped_ids = {s["video"] for s in skips}
overlap_rs = all_judged & skipped_ids
pool_ids = {v["id"] for v in pool} | {c["id"] for c in allery_cands}
total_accounts = len(all_judged | skipped_ids)
print(f"\n=== disposition ===")
print(f"judgment pools: {len(pool)} uploads + Allery re-adjudication group {len(allery_cands)} candidates")
print(f"tier-b videos: {len(tb_vids)} | tier-a routed videos: {len(routed_vids) - len(tb_vids & routed_vids)}")
print(f"skips: {len(skips)} (NT pool-level {nt_skipped}) | reserved lit-21: {len(reserved)}")
print(f"exactly-once: dispositioned {total_accounts} vs pools {len(pool_ids)} + NT {nt_skipped} = {len(pool_ids) + nt_skipped}")
print(f"routed-vs-skip collisions: {len(overlap_rs)} {list(overlap_rs)[:3]}")

rows_total = sum(len(x) for x in judgment.values())
print(f"\n=== per-course routed rows ===")
for course in TARGETS:
    rows = judgment[course]
    if not rows:
        continue
    conf = Counter(r["confidence"] for r in rows)
    b = sum(1 for r in rows if r.get("p14b"))
    cross = sum(1 for r in rows if r.get("crossReg"))
    print(f"{course}: {len(rows)} rows {dict(conf)} p14b {b} crossReg {cross}")
print(f"\nTOTAL routed rows {rows_total} + tier-b rows {len(tier_b)}; skips {len(skips)}; reserved {len(reserved)}")

json.dump(tier_b, open(f"{WORK}/tier-b.json", "w"), indent=1, ensure_ascii=False)
json.dump(skips, open(f"{WORK}/skips.json", "w"), indent=1, ensure_ascii=False)
json.dump(reserved, open(f"{WORK}/reserved-lit21.json", "w"), indent=1, ensure_ascii=False)
ta = {}
for course, rows in judgment.items():
    for r in rows:
        ta[f"{course}::{r['id']}"] = r
json.dump(ta, open(f"{WORK}/tier-a.json", "w"), indent=1, ensure_ascii=False)
json.dump(judgment, open(f"{WORK}/judgment.json", "w"), indent=1, ensure_ascii=False)
json.dump({"utc": UTC, "poolCounts": {p: sum(1 for v in pool if v["provider"] == p) for p in JUDGMENT_POOLS}},
          open(f"{WORK}/judgment-meta.json", "w"), indent=1)
print("\noutputs written to", WORK)
