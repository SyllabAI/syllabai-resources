#!/usr/bin/env python3
"""P19 judgment: route the 25 admitted gap-profile pools (7,098 uploads) onto the
fresh post-P18 residual spine. Owner order this session: "run P19 judgment"
(the P19 filing PR #364 admitted as filed per the P15/P17/P18 convention: the
owner order admits the pools and opens the judgment gate).

The P15/P17/P18 gate ladder unchanged, with the registers the P19 profile filed:

  Tier B   paper-code anchors   — 0610/0620/0625 CIE IGCSE sciences (+ 0971/0972/
                                 0973 + the 5090 dual); 0417/0983 ICT; 4IT1+4IT0 +
                                 the International-GCSE-ICT register text; 4MA1 maths-A
                                 H/F + modular-24 4WM codes; 4MB1 maths-B (incl. the
                                 'IGCSE (9-1) Maths B' P19 infix form); 0580/0980
                                 papers 2/4 extended vs 1/3 core (the P9/P14 law,
                                 code-required); 0607 International Maths (the NEW
                                 P19 register, the 0606 dual-branding posture);
                                 0606 (+ the disclosed 4037 dual); 0452/0985 (+ the
                                 disclosed 7707 dual) incl. the 'O level/ IGCSE
                                 Accounting' P19 form; 0455 (+ the disclosed 2281
                                 dual); 0450 (+ the disclosed 7115 O-Level dual; the
                                 NEW P19 register -> cie-igcse-business-25); 0680;
                                 9708 incl. the 'Cambridge AS/A2 Economics' P19 form;
                                 9609 incl. the 'AS/A Level Business' unit-series
                                 forms (pool-scoped: only the CIE-declared 9609
                                 pools); 4BS1/4BI1/4CH1/4PH1/4SD0 Edexcel IGCSE
                                 registers; IAL WPH (incl. the P19 spaced 'WPH 16'
                                 form = unit 6) + the Pearson-pipe family; 0475
                                 Class W set-text titles.
  NEW P19   topic-number anchor — the igbiocomplete '(topic N.M[.K])' form binds the
                                 exact spec point / subtopic points of the CIE trio
                                 course, PLUS the co-ordinated P/B/C-prefixed twin
                                 point where the 2025-2027 co-ord spine carries the
                                 same number (the shared-0625-structure law; the
                                 combined-23 numbering diverges and is NOT bound);
                                 the study-buddy leading/pipe 'N. {Topic}' form binds
                                 the trio topic at index N with stem token-agreement;
                                 the sciencewithchun 0654 section-scoped 'B9/P5/C3'
                                 form binds the co-ordinated same-science topic at
                                 that index with stem token-agreement (the combined
                                 numbering diverges; NOT bound).
  Class W  set-text work binds  — the P16 committed predicate (P17/P18 amendments).
  Class M/S/Tier A/Class L     — section markers, verbatim section-name binding,
                                 distinctive-token (df<=3), four-gate topic lectures.

  skips    honest ledger        — tuition-marketing/meta registers (grade thresholds,
                                 timetables, teacher profiles, lives/graduations/
                                 campus events), the guidance/advice register, NT
                                 boards (AQA/OCR/IB/NCERT/CBSE/JEE/NEET), the
                                 Anna-university 'GE8291 EVS' register (the P19
                                 false-density call of record: the gate's '8291 x13'
                                 family read was the Indian GE8291 paper, NOT
                                 Cambridge AS Environmental Management — 0 binds,
                                 the P17 nevdoes/indigo precedent), the edutainment
                                 shorts series ('Explaining X using video games/
                                 fiction'), the UK-GCSE register without an
                                 International token (the corbettmaths exclusion
                                 class), CIE AS/A Level IT 9626, bare maths titles
                                 with no syllabus code, the O-Level register unless
                                 a spine-code token is present (the disclosed
                                 4037/2281/7707/5090/7115 duals), IAL/CIE maths 9709
                                 bare walkthroughs (ANCHOR-GRANULARITY section 6, the
                                 P9/P17/P18 precedent), and the no-binding remainder.

P19 disclosed register re-adjudications of record (the profile's density reads are
register-level; the language/read stays with the judgment — the gate's own law):
  1. ginger-mathematician: the gate's '4MA1 x159' family read keyed on the P18
     RE_4MA1 'IGCSE Math' generic alternation; the channel is Cambridge-branded
     ('That Cambridge Made', 0580/0607 paper forms 'Paper 2 & 4') — the honest
     register is CIE 0580 (papers 2/4 extended vs 1/3 core, the P9/P14 law) +
     0607 + 0606; the 4MA1 deficits stay open (re-sweepable next lane).
  2. benzakademi: 'GE 8291' is the Anna University EVS paper — 0 honest binds.
  3. igbiocomplete/precool-skillz/save-my-exams carry no syllabus codes on the
     science/ICT subset — the CIE subject-name register ('IGCSE Physics -',
     'iGCSE Physics #N', 'IGCSE Chemistry-') binds at the title-only posture per
     the gate's own classification (disclosed per pool).

Exactly-once disposition of all 7,098 accounts, 0 collisions machine-checked.
Outputs work/p19/: tier-b.json, judgment.json, skips.json, judgment_summary.json
"""
import json, os, re, datetime
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub"
WORK = "/home/z/my-project/work/p19"
UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs(WORK, exist_ok=True)

JUDGMENT_POOLS = ["igbiocomplete", "maths-with-mohaiminul", "mr-khan-ict-solutions",
                  "miss-tech-teacher", "ict-with-tatchen", "rapid-revision-with-shayan",
                  "the-visible-hand", "muzammil-ameer-acma", "saifullah-ajaz",
                  "bookkeepers-journal", "your-igcse-tutors", "igcse-study-buddy",
                  "ginger-mathematician", "sciencewithchun", "the-physics-examiner",
                  "education-for-success", "edubbey", "precool-skillz", "save-my-exams",
                  "accounting-celebrity", "revwise", "benzakademi", "academic-plus",
                  "easy-edu", "the-revision-notebook"]

pool = []
_seen = set()
for slug in JUDGMENT_POOLS:
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        if v["id"] in _seen:
            continue
        _seen.add(v["id"])
        pool.append({"id": v["id"], "title": v["title"], "provider": slug})
assert len(pool) == 7098, f"pool {len(pool)} != 7098"

# ---------------------------------------------------------------- spine
TARGETS = [
    # maths (Edexcel IGCSE)
    "igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
    "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
    "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2",
    "igcse-maths-b-16",
    # maths (CIE)
    "cie-igcse-maths-25-extended", "cie-igcse-maths-25-core",
    "cie-igcse-maths-international-maths-23-extended", "cie-igcse-maths-international-maths-23-core",
    "cie-igcse-further-maths-additional-maths-25",
    # accounting
    "cie-igcse-accounting-25", "cie-igcse-accounting-21",
    # economics
    "cie-igcse-economics-20", "cie-igcse-economics-25", "cie-a-level-economics-23",
    # business
    "igcse-business-19", "cie-igcse-business-25", "cie-as-business-23", "cie-a-level-business-23",
    # environmental management
    "cie-igcse-environmental-management-25", "cie-as-environmental-management-20",
    # ICT + CS
    "igcse-ict-17", "cie-igcse-ict-21", "cie-igcse-computer-science-23",
    # CIE IGCSE sciences trio
    "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
    # co-ordinated trio (P4 children; the shared-structure twin binds)
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
    # Edexcel IGCSE sciences trio
    "igcse-chemistry-19", "igcse-biology-19", "igcse-physics-19",
    # IAL physics (the-physics-examiner WPH)
    "ial-physics-19",
]

P4_CHILDREN = set(json.load(open(f"{RES}/Videos/drafts/_p4/inheritance-map.json"))["parents"].keys())
P19B = [c for c in TARGETS if c in P4_CHILDREN]

for course in TARGETS:
    assert os.path.exists(f"{HUB}/content/{course}/curriculum.json"), f"missing {course}"

specs_spine = {}
for course in TARGETS:
    nodes = json.load(open(f"{HUB}/content/{course}/curriculum.json"))["nodes"]
    topic_of, cur = {}, None
    for n in nodes:
        if n["family"] == "TOPIC":
            cur = n["title"]
        topic_of[n["code"]] = cur
    specs_spine[course] = {"nodes": nodes, "topic_of": topic_of}

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
0680 8291 0417 4it0 4it1 4ge0 4ge1 4ma1 4mb1 4bs1 4xm 0475 0653 0654 0460 9231 4037 4040
0450 0413 0607 4ch1 4bi1 4ph1 4sd0 4wch1 4wch2 4wm1 4wm2 wph wbi wch wit wec
p1 p2 p3 p4 p5 p6 m1 m2 s1 s2 fp1 fp2 fp3 c1 c2 c3 c4 c12 c34 edexcel ocr aqa gcse
urdu hindi archived lesson lect tutorial tutorials revision-worksheet worksheet daily
dose olevels olevel predicted predictions predicted-papers tricky made easy exam-exam
review questions questionwise workbook workbook sneak preview reality teaching online
8021 0985 7707 4pm0 4pm1 0980 0983 0971 0972 0973 4wm shorts 7115 olevel""".split())

def toks14(s):
    # P19 disclosed amendment: tokens stem to singular (trailing 's'/'ies') so
    # plural-form title tokens agree with spine point tokens ('probability' vs
    # 'probabilities') — applied to BOTH the spine tables and the titles, so the
    # df tables and the binding rule stay consistent (the P18 RE_GUIDE amendment
    # precedent: a shared-helper regex/tokenizer fix disclosed, not re-opened).
    out = []
    for w in re.findall(r"[a-z0-9]+", s.lower()):
        if w in STOP or len(w) <= 2:
            continue
        if w.endswith("ies") and len(w) > 5:
            w = w[:-3] + "y"
        elif w.endswith("s") and not w.endswith("ss") and len(w) > 3:
            w = w[:-1]
        out.append(w)
    return out

for course in TARGETS:
    df = Counter()
    for n in specs_spine[course]["nodes"]:
        for w in set(toks14(n["title"] or "")):
            df[w] += 1
    specs_spine[course]["df"] = df
    specs_spine[course]["pts"] = [n for n in specs_spine[course]["nodes"] if n["family"] == "SPEC_POINT"]
    specs_spine[course]["subs"] = [n for n in specs_spine[course]["nodes"] if n["family"] == "SUBTOPIC"]
    specs_spine[course]["topics"] = [n for n in specs_spine[course]["nodes"] if n["family"] == "TOPIC"]

TDF = {}
for course in TARGETS:
    c = Counter()
    for n in specs_spine[course]["nodes"]:
        if n["family"] in ("TOPIC", "SUBTOPIC"):
            for w in set(toks14(n["title"] or "")):
                c[w] += 1
    TDF[course] = c

def sub_points(course, subcode):
    num = subcode.split(":")[-1].replace("SUB", "")
    return [p for p in specs_spine[course]["pts"] if re.match(rf"^{re.escape(num)}\.\d+$", p["code"])]

def topic_points(course, topic_title):
    return [p for p in specs_spine[course]["pts"] if specs_spine[course]["topic_of"].get(p["code"]) == topic_title]

def best_point(course, title, max_df=3):
    vt = set(toks14(title))
    best, best_score = None, 0
    for p in specs_spine[course]["pts"]:
        pt = set(toks14(p["title"] or ""))
        if not pt:
            continue
        hits = vt & pt
        if not hits:
            continue
        dmax = max(specs_spine[course]["df"].get(w, 99) for w in hits)
        distinctive = [w for w in hits if specs_spine[course]["df"].get(w, 99) <= max_df]
        score = len(distinctive) * 10 + len(hits)
        if len(distinctive) >= 2 or (len(hits) >= 3 and dmax <= 6):
            if score > best_score:
                best, best_score = (p, sorted(hits), dmax, len(hits)), score
    return best

def norm_stop(s):
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return " " + " ".join(w for w in s.split() if w not in STOP and len(w) > 2) + " "

def split_fields(title):
    # P19 disclosed amendment: dash-run separators (the 'Biology- {topic}' forms)
    # split fields too — the P18 law only split on the spaced ' - ' form, which
    # lost the verbatim-field matches on the P19 pools.
    return [x.strip() for x in re.split(r"\|+|[-\u2013\u2014]+", title) if x.strip()]

def section_by_field(course, title):
    fields = [norm_stop(re.sub(r"\([^)]*\)", " ", f)) for f in split_fields(title)]
    best = None
    for n in specs_spine[course]["nodes"]:
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
    for n in specs_spine[course]["nodes"]:
        if n["family"] != "TOPIC":
            continue
        tset = set(toks14(n["title"] or ""))
        subtoks, seen = set(), False
        for m in specs_spine[course]["nodes"]:
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
    subs = [s for s in specs_spine[course]["subs"] if s["code"].split(":")[-1].replace("SUB", "") == num]
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
    r"|\b(?:may|june|oct|nov)\s*20\d\d|\b(Winter|Summer)\s+(session\s+)?20\d\d\b|\bm/j\b|\bo/n\b|\bqp\b|\bW1[1-9]\b|\bS1[1-9]\b|\bM1[1-9]\b)", re.I)
RE_SOLVED = re.compile(r"solved|solution|walkthrough|past[- ]?paper|qp\s*_?\d|mark scheme|\bQ\s?\d|\bQ\(|question\s*\d|exam questions?|predictions?!? paper|\bcomplete\b|paper\s*\d", re.I)
RE_GUIDE = re.compile(
    r"tips|tricks?\b|ace your|how to (ace|finish|overcome|stop|prepare|revise|get full|write|score|answer|pass)|how (do i|this student|did paper)|"
    r"survival guide|preparation course|orientation|watch (this|before)|podcast|success|result day|"
    r"interview|\bvision\b|challenge|parents? of|\bupdates?\b(?!\s*(?:&|and|to)\s+(?:software|devices|systems))|tour|platform|worried|nervous|resit|message|"
    r"days? left|30 days|60 days|join now|score an a\*|a\* in|game.?chang|blended|covid|"
    r"studysmart|aitutor|revision in|month left|marking schemes|what you (need|can)|can't miss|"
    r"paper breakdown|important topics|fix of|lifesaver|one thing|stress|focus on what|predictions?!"
    r"|sneak preview|live class|whatsapp|daily dose|the reality of|full marks|made easy|sneak peek"
    r"|you (need to|must) know|don't let|i won't let|checklist|shortcuts?\b|exam saving|mock exams?\b", re.I)
RE_OLEVEL = re.compile(r"\bO\s?-?\s?Levels?\b|\bOL\b|\b4024\b|\b2281\b|\b5070\b|\b5090\b|\b5124\b|\b2210\b|\b4037\b|\b4040\b|\b7707\b|\b7115\b", re.I)
RE_NT_BOARD = re.compile(r"\bAQA\b|\bOCR\b|\bIB\b|\bNCERT\b|\bCBSE\b|\bISC\b|\bJEE\b|\bNEET\b|\bKS[1-4]\b|\bAP\b|\bSAT\b|\bMEI\b|\bMYP\b|\bH2\b", re.I)
RE_UK_GCSE = re.compile(r"\bGCSE\b(?!\s*\(?\s*i\s*\)?|\s*International)", re.I)
RE_IGCSE_TOK = re.compile(r"\bIGCSE\b|international\s+GCSE", re.I)
RE_ED_IG = re.compile(r"Edexcel\s+IGCSE|IGCSE.{0,40}Edexcel|\b4MA1\b|\b4PH1?\b|\b4CH1?\b|\b4BI1?\b|\b4IT0\b|\b4IT1\b|\b4GE0\b|\b4GE1\b|\b4MB1\b|\b4BS1\b|\b4SD0\b", re.I)
RE_IAL_UNIT = re.compile(r"Unit\s*([1-6]).{0,60}?(AS|A2|IAS|IA2|A[- ]?Level|International).{0,40}?(Physic|Biolog|Chem)|((Physic|Biolog|Chem).{0,40}?(AS|A2|IAS|IA2).{0,40}?Unit\s*([1-6]))|(IAS|IA2)\s*(Physics|Biology|Chemistry)", re.I)
RE_PEARSON_PIPE = re.compile(r"[Aa]\s*[Ll]evel\s*\|?\s*(Biology|Chemistry|Physics)\s*\|?\s*(?:Unit\s*([1-6])|Scientific\s+article)", re.I)
RE_MOD_UNIT = re.compile(r"Modular.{0,30}?Unit\s*([12])", re.I)
RE_COORDD = re.compile(r"\b0654\b|[Cc]o-?ordinated|[Dd]ouble\s*[Aa]ward", re.I)
RE_COMBINED = re.compile(r"\b0653\b|[Cc]ombined\s*[Ss]cience", re.I)

RE_0610 = re.compile(r"\b0?610\b|\b0973\b|\b5090\b", re.I)
RE_0620 = re.compile(r"\b0620\b|\b0971\b", re.I)
RE_0625 = re.compile(r"\b0625\b|\b0972\b", re.I)
RE_0417 = re.compile(r"\b0417\b|\b0983\b", re.I)
RE_4IT0 = re.compile(r"\b4IT0\b|\b4IT1\b|Edexcel\s+i?GCSE\s+ICT|[Ii]nternational\s+GCSE\s+ICT|IGCSE\s+ICT\s+Paper\s*\d|Edexcel\s+IGCSE\s+ICT.{0,30}Paper|Edexcel\s+GCSE\s+ICT", re.I)
RE_ED_CS = re.compile(r"Edexcel\s+(i)?GCSE\s+Computer\s+Science", re.I)
RE_4MA1 = re.compile(r"\b4MA1\b|IGCSE\s+Math|IGCSE\s+Further\s+Maths?\b.{0,30}Edexcel", re.I)
RE_4MB1 = re.compile(r"\b4MB1\b|IGCSE\s*\(9-1\)\s*Maths?\s+B\b|IGCSE\s+Maths?\s+B\b|Maths?\s+B\s+(Exam|Paper|Past)|Specification\s+B\s*\(4MB1\)", re.I)
RE_4WM = re.compile(r"\b4WM([12])\w*/", re.I)
RE_4XM = re.compile(r"\b4XM\d?\b", re.I)
RE_0606 = re.compile(r"\b0606\b|[Aa]dd(itional)?\s*[Mm]aths", re.I)
RE_0607 = re.compile(r"\b0607\b|international\s+maths?\b", re.I)
RE_0580 = re.compile(r"\b0580\b|\b0980\b", re.I)
RE_0452 = re.compile(r"\b0452\b|\b0985\b|IGCSE\s+Account|O\s?[Ll]evels?/?\s*(&\s*)?(i?GCSE\s+)?Accounting", re.I)
RE_0455 = re.compile(r"\b0455\b|IGCSE\s+Economics|IGCSE\s+Econ|O\s?[Ll]evels?/?\s*(&\s*)?(i?GCSE\s+)?Economics", re.I)
RE_0680 = re.compile(r"\b0680\b|[Ee]nvironmental\s+[Mm]anagement|\bE\.?M\.?\b\s*(paper|revision|topic)", re.I)
RE_0450 = re.compile(r"\b0450\b|\b7115\b|Business\s+Studies", re.I)
RE_0460 = re.compile(r"\b0460\b|\b0976\b|IGCSE\s+Geography", re.I)
RE_4GE1 = re.compile(r"\b4GE1\b|International\s+GCSE\s+Geography|Edexcel\s+i?GCSE\s+Geography", re.I)
RE_WPH = re.compile(r"\bWPH\s?\d?\d?\b|IAL\s+[Pp]hysics|IAS\s+[Pp]hysics|IA2\s+[Pp]hysics", re.I)
RE_WBI = re.compile(r"\bWBI\s?\d?\d?\b|IAL\s+[Bb]iology|IAS\s+[Bb]iology|IA2\s+[Bb]iology", re.I)
RE_WCH = re.compile(r"\bWCH\s?\d?\d?\b|IAL\s+[Cc]hemistry|IAS\s+[Cc]hemistry|IA2\s+[Cc]hemistry", re.I)
RE_WIT = re.compile(r"\bWIT\d?\d?\b|IAL\s+Information\s+Technology", re.I)
RE_WEC = re.compile(r"\bWEC\d?\d?\b|IAL\s+Economics", re.I)
RE_9708 = re.compile(r"\b9708\b|A\s?[- ]?\s?[Ll]evel\s*[Ee]conomics|Cambridge\s+(AS|A2)\s+[Ee]conomics", re.I)
RE_9609 = re.compile(r"\b9609\b|A\s?[Ll]evel\s*[Bb]usiness|(?:\bAS|\bA2)\s*[Ll]evel\s*[Bb]usiness", re.I)
RE_9700 = re.compile(r"\b9700\b|A\s?[- ]?\s?[Ll]evel\s*[Bb]iology", re.I)
RE_9701 = re.compile(r"\b9701\b|A\s?[- ]?\s?[Ll]evel\s*[Cc]hemistry", re.I)
RE_9702 = re.compile(r"\b9702\b|A\s?[- ]?\s?[Ll]evel\s*[Pp]hysics", re.I)
RE_8021 = re.compile(r"\b8021\b|[Gg]eneral\s+[Pp]aper", re.I)
RE_4PM = re.compile(r"\b4PM[01]\b|[Ff]urther\s+[Pp]ure\s+[Mm]aths|[Ff]urther\s+[Pp]ure\s+.{0,24}(IGCSE|Edexcel)", re.I)
RE_4BS1 = re.compile(r"\b4BS1\b|\b4BS0\b|Edexcel\s+i?GCSE\s+Business|IGCSE\s+Business\s+Studies", re.I)
RE_4CH1 = re.compile(r"\b4CH1\b", re.I)
RE_4BI1 = re.compile(r"\b4BI1\b", re.I)
RE_4PH1 = re.compile(r"\b4PH1\b", re.I)
RE_4SD0 = re.compile(r"\b4SD0\b", re.I)
RE_4WCHMOD = re.compile(r"\b4WCH([12])\b", re.I)
RE_4XB = re.compile(r"\b4XB\d?\b", re.I)
RE_4XP = re.compile(r"\b4XP\d?\b", re.I)
RE_0475 = re.compile(r"\b0475\b|Study\s+Guide\s+for\s+Cambridge|Songs\s+of\s+Ourselves|Stories\s+of\s+Ourselves", re.I)
RE_GCSE_LIT = re.compile(r"GCSE\s+English\s+Lit", re.I)
RE_2012_MOD = re.compile(r"Modular.{0,30}?Unit\s*([1-4]).{0,40}?20(0\d|1[0-6])|20(0\d|1[0-6]).{0,40}?Modular", re.I)
RE_IAL_MATHS = re.compile(r"IAL\s+Math|Edexcel\s+Maths?\s*[-\u2013]\s*(Pure|Mechanics|Statistics)|\b9709\b|A\s?[Ll]evel\s+Maths?\s+(Pure|Mechanics|Statistics)", re.I)
RE_PROMO = re.compile(r"register now|onsite classes|onsite class|money well spent|subscribe|follow (me|us)|visit (our|my)|\bemotional\b|new (course|batch)|enrol|admissions? open|tuition|#GP\w*|is live!|batch registration|are (live|open)|join (now|business|the)|workshop highlights|campus", re.I)
RE_META = re.compile(r"grade boundar|threshold|timetable|teacher profile|birthday|thanks for (all|your)|2000 subs|celebrat|speedrun|farewell|teacher'?s day|graduation|good bye session", re.I)
RE_CERT = re.compile(r"\bIC3\b|Certiport|\bMOS\b|Microsoft Office Specialist", re.I)
RE_CIE_IT = re.compile(r"(AS|A)\s?[Ll]evel\s+IT\b", re.I)
RE_0500tok = re.compile(r"\b0500\b|first\s+language\s+english", re.I)

# ---- P19 new register machinery ----
RE_TNUM_PAREN = re.compile(r"\btopic\s+(\d{1,2})\.(\d{1,2})(?:\.(\d{1,2}))?", re.I)
RE_TNUM_LEAD = re.compile(r"(?:^|\|\s*)(\d{1,2})\.\s+(?=[A-Za-z])")
RE_0654_SEC = re.compile(r"(?<![A-Za-z0-9])([BPC])(\d{1,2})(?![A-Za-z0-9])")
RE_CHAPTER = re.compile(r"[Cc]hapter\s+(\d{1,2})")
RE_ANNA8291 = re.compile(r"GE\s?8291|\bEVS\b|\+1\s*,?\s*\+2|CBSE|\bISC\b", re.I)
RE_EDUTAIN = re.compile(r"Explaining \w+ using (video games|fiction|movies|films)", re.I)
RE_LIVE = re.compile(r"is live!|live stream|livestream", re.I)

COORD = {"bio": "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
         "chem": "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
         "phys": "cie-igcse-science-co-ordinated-sciences-double-award-23-physics"}
TRIO = {"bio": "cie-igcse-biology-23", "chem": "cie-igcse-chemistry-23", "phys": "cie-igcse-physics-23"}
COORD_PREFIX = {"bio": "B", "chem": "C", "phys": "P"}
SUBJ_RE = {"bio": re.compile(r"IGCSE\s*Biology", re.I), "chem": re.compile(r"IGCSE\s*Chemistry", re.I),
           "phys": re.compile(r"IGCSE\s*Physics", re.I)}

def _stem(w):
    for suf in ("ies", "es", "s"):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            return w[: -len(suf)]
    return w

def topic_at_index(course, n):
    for t in specs_spine[course]["topics"]:
        m = re.search(r"-T[A-Z]?(\d+)$", t["code"])
        if m and int(m.group(1)) == n:
            return t
    return None

def token_agreement(title, node_title):
    a = set(_stem(w) for w in toks14(title))
    b = set(_stem(w) for w in toks14(node_title or ""))
    if not a or not b:
        return 0.0, 0
    inter = a & b
    return len(inter) / len(a), len(inter)

def point_by_code(course, a, b, c=None):
    code = f"{a}.{b}.{c}" if c else f"{a}.{b}"
    return next((p for p in specs_spine[course]["pts"] if p["code"] == code), None)

def sub_by_num(course, a, b):
    num = f"{a}.{b}"
    return next((s for s in specs_spine[course]["subs"] if s["code"].split(":")[-1].replace("SUB", "") == num), None)

def tnum_anchor(vid, prov, t, subj):
    """(topic N.M[.K]) / leading 'N.' register -> trio course exact point/subtopic,
    + co-ordinated P/B/C twin where the co-ord spine carries the same number.
    Returns True if any bind landed."""
    landed = False
    trio = TRIO[subj]
    m3 = RE_TNUM_PAREN.search(t)
    m_lead = None if m3 else RE_TNUM_LEAD.search(t)
    if m3:
        a, b = m3.group(1), m3.group(2)
        c3 = m3.group(3)
        if c3:
            p = point_by_code(trio, a, b, c3)
            if p:
                route(trio, vid, prov, [p["code"]], "medium",
                      f"topic-number register: title names point {a}.{b}.{c3} '{p['title'][:60]}' — exact code match "
                      f"(the CIE 2023-2025 {subj} numbering); oEmbed author verified", None)
                landed = True
        else:
            s = sub_by_num(trio, a, b)
            if s:
                pts = sub_points(trio, s["code"])
                if pts:
                    route(trio, vid, prov, [p["code"] for p in pts], "low",
                          f"topic-number register: title names section {a}.{b} '{s['title'][:60]}' — subtopic points bound "
                          f"at the disclosed title-only bar (the CIE 2023-2025 {subj} numbering)", None)
                    landed = True
        if c3:
            co = point_by_code(COORD[subj], f"{COORD_PREFIX[subj]}{a}", b, c3)
            if co:
                route(COORD[subj], vid, prov, [co["code"]], "medium",
                      f"topic-number register (shared-structure twin bind): title names {a}.{b}.{c3} and the co-ordinated "
                      f"2025-2027 {subj} spine carries {co['code']} '{co['title'][:50]}' — the 0625/0654 shared content "
                      f"structure (disclosed)", True)
                landed = True
    elif m_lead:
        n = int(m_lead.group(1))
        tp = topic_at_index(trio, n)
        if tp:
            frac, ninter = token_agreement(t, tp["title"])
            if frac >= 0.5 and ninter >= 1:
                pts = topic_points(trio, tp["title"])
                if pts:
                    route(trio, vid, prov, [p["code"] for p in pts], "low",
                          f"topic-number register: title names topic {n} '{tp['title'][:60]}' (stem agreement {ninter} token(s)) "
                          f"— topic points bound at the disclosed title-only bar (the CIE 2023-2025 {subj} numbering)", None)
                    landed = True
    return landed

def sec0654_anchor(vid, prov, t):
    """0654 section-scoped 'B9/P5/C3' register -> co-ordinated same-science topic
    at that index with stem token-agreement. Returns True if a bind landed."""
    m = RE_0654_SEC.search(t)
    if not m:
        return False
    letter, n = m.group(1).upper(), int(m.group(2))
    subj = {"B": "bio", "P": "phys", "C": "chem"}[letter]
    co = COORD[subj]
    tp = topic_at_index(co, n)
    if not tp:
        return False
    rest = t[m.end():]
    frac, ninter = token_agreement(rest or t, tp["title"])
    if frac < 0.5 or ninter < 1:
        return False
    pts = topic_points(co, tp["title"])
    if not pts:
        return False
    route(co, vid, prov, [p["code"] for p in pts], "low",
          f"0654 section-scoped register: title names section {letter}{n} '{tp['title'][:60]}' (stem agreement "
          f"{ninter} token(s)) — co-ordinated topic points bound at the disclosed title-only bar (the shared "
          f"0654 section numbering)", True)
    return True

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
    m = re.search(r"\b0?(610|620|625|653|654|417|452|455|460|500|606|607|680|8291|460)/(\d{1,2})\d?/", title)
    if m:
        cands.append(int(m.group(2)))
    m = re.search(r"\b(?:9700|9701|9702|9708|9609|0580|4024)[/ ]?(\d{1,2})\b", title)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"\bQP\s?(\d{1,2})\b", title, re.I)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"\b04(?:17|52|55)\s*Paper\s*(\d)", title, re.I)
    if m:
        cands.append(int(m.group(1)))
    for raw in cands:
        if 1 <= raw <= 6:
            return raw
        if 11 <= raw <= 66 and raw % 10 in (1, 2, 3):
            return raw // 10
    return None

tier_b, skips = [], []
judgment = {c: [] for c in TARGETS}
LIT = "cie-igcse-english-literature-21"
judgment[LIT] = []  # Class W column (the lit spine is NOT in the generic TARGETS ladder)

def skip(prov, vid, title, reason):
    skips.append({"video": vid, "title": title[:160], "provider": prov, "reason": reason})

def route(course, vid, prov, specs_list, confidence, reason, p19b=False, cross=False):
    judgment[course].append({"id": vid, "provider": prov, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p19b": p19b if p19b else course in P19B, "crossReg": cross})

def tb(course_list, vid, prov, title, code, cross=False):
    for course in course_list:
        tier_b.append({"id": vid, "title": title, "provider": prov, "courses": [course],
                       "code": code, "kind": "past-paper-walkthrough",
                       "p19b": course in P19B, "crossReg": cross})

def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|Q\s?\d|paper\s*\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

def bind_course(course, vid, prov, t, p19b=None):
    if p19b is None:
        p19b = course in P19B
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p19b)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p19b)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs_spine[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p19b)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p19b)
            return True
    return False

COORD_TRIO = [COORD["bio"], COORD["phys"], COORD["chem"]]
DA_TRIO = ["igcse-science-double-award-17-biology",
           "igcse-science-double-award-17-chemistry",
           "igcse-science-double-award-17-physics"]

def ig_science_anchor(vid, prov, t):
    out = []
    if RE_0610.search(t):
        out.append("cie-igcse-biology-23")
    if RE_0620.search(t):
        out.append("cie-igcse-chemistry-23")
    if RE_0625.search(t):
        out.append("cie-igcse-physics-23")
    return out

def ed_science_anchor(t):
    """Edexcel IGCSE sciences 4CH1/4BI1/4PH1/4SD0 — specific-code routing."""
    out = []
    if RE_4CH1.search(t):
        out.append("igcse-chemistry-19")
    if RE_4BI1.search(t):
        out.append("igcse-biology-19")
    if RE_4PH1.search(t):
        out.append("igcse-physics-19")
    if RE_4SD0.search(t):
        out += DA_TRIO
    return out

def ma_routes(t):
    """4MA1/4MB1/4WM/4XM register routing: higher/foundation/modular-24 + maths-B."""
    out = []
    mw = RE_4WM.search(t)
    if mw:
        lvl = "higher" if re.search(r"\bH\b|higher", t, re.I) else ("foundation" if re.search(r"\bF\b|foundation", t, re.I) else None)
        if lvl:
            out.append(f"igcse-maths-a-modular-24-{lvl}-unit-{mw.group(1)}")
            return out
        out += [f"igcse-maths-a-modular-24-higher-unit-{mw.group(1)}",
                f"igcse-maths-a-modular-24-foundation-unit-{mw.group(1)}"]
        return out
    mm = RE_MOD_UNIT.search(t) or (RE_4XM.search(t) and re.search(r"unit\s*[12]", t, re.I))
    if mm:
        g = mm.group(1) if mm.lastindex and mm.lastindex >= 1 else None
        um = re.search(r"unit\s*([12])", t, re.I)
        g = g or (um.group(1) if um else None)
        lvl = "higher" if re.search(r"higher", t, re.I) else ("foundation" if re.search(r"foundation", t, re.I) else None)
        if g and lvl:
            out.append(f"igcse-maths-a-modular-24-{lvl}-unit-{g}")
            return out
        if g:
            out += [f"igcse-maths-a-modular-24-higher-unit-{g}",
                    f"igcse-maths-a-modular-24-foundation-unit-{g}"]
            return out
        if lvl:
            out += [f"igcse-maths-a-modular-24-{lvl}-unit-1", f"igcse-maths-a-modular-24-{lvl}-unit-2"]
            return out
    if RE_4MB1.search(t) and not (RE_4MA1.search(t) or RE_4WM.search(t)):
        out.append("igcse-maths-b-16")
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

CURRENT_PROV = [None]

def judge_pool(slug, law, olevel_exempt=None):
    for v in pool:
        if v["provider"] != slug:
            continue
        vid, t = v["id"], v["title"]
        if RE_PROMO.search(t) or RE_LIVE.search(t) or len(re.sub(r"\W+", "", t)) < 6:
            skip(slug, vid, t, "channel promo/meta content (no qualification register)")
            continue
        if RE_META.search(t):
            skip(slug, vid, t, "meta announcement (grade thresholds/timetable/results/celebration/graduation) — no qualification register")
            continue
        if RE_EDUTAIN.search(t):
            skip(slug, vid, t, "edutainment shorts register (the 'Explaining X using video games/fiction' series) — no spec-structured lecture")
            continue
        if RE_IAL_MATHS.search(t):
            skip(slug, vid, t, "IAL/CIE maths register (P1-M2/S1/9709/A-level Pure) — bare unit/session walkthroughs skip per ANCHOR-GRANULARITY §6 (P9 precedent)")
            continue
        exempt = olevel_exempt and olevel_exempt(t)
        has_spine_code = bool(RE_0606.search(t) or RE_0607.search(t) or RE_0452.search(t)
                              or RE_0455.search(t) or RE_0610.search(t) or RE_0620.search(t)
                              or RE_0625.search(t) or RE_0580.search(t) or RE_0417.search(t)
                              or RE_9708.search(t) or RE_9609.search(t) or RE_9700.search(t)
                              or RE_9701.search(t) or RE_9702.search(t) or RE_8021.search(t)
                              or RE_0460.search(t) or RE_0680.search(t) or RE_0475.search(t)
                              or RE_4MA1.search(t) or RE_4MB1.search(t) or RE_4PM.search(t)
                              or RE_4BS1.search(t) or RE_0500tok.search(t) or RE_0450.search(t))
        if not exempt and RE_OLEVEL.search(t) and not has_spine_code:
            skip(slug, vid, t, "O-Level register (4024/2281/5090/7707/7115/...) with no IGCSE spine-code token — no O-Level course in the spine")
            continue
        if RE_ED_CS.search(t):
            skip(slug, vid, t, "Edexcel UK-GCSE Computer Science — no spine course (the spine carries CIE 0478)")
            continue
        law(vid, t)

def with_ladder(vid, t, courses, anchor_tests, prov):
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

def ial_unit_anchor(vid, prov, t, subject=None):
    """Unit N + session/paper reference -> unit-paper review anchor (P14 Assil law)."""
    un = re.search(r"unit\s*([1-6])", t, re.I)
    sess = RE_SESSION.search(t)
    pipe = RE_PEARSON_PIPE.search(t)
    subj = subject
    if subj is None:
        if pipe:
            subj = {"biology": "bio", "chemistry": "chem", "physics": "phys"}[pipe.group(1).lower()]
        elif RE_WBI.search(t) or re.search(r"biolog", t, re.I):
            subj = "bio"
        elif RE_WCH.search(t) or re.search(r"chem", t, re.I):
            subj = "chem"
        elif RE_WPH.search(t) or re.search(r"physic", t, re.I):
            subj = "phys"
    course = {"bio": "ial-biology-18", "chem": "ial-chemistry-17", "phys": "ial-physics-19"}[subj]
    is_article = bool(pipe and pipe.group(2) is None and re.search(r"scientific\s+article", t, re.I))
    # the P19 spaced 'WPH 16' form: WPH + paper NN (unit = tens digit)
    mw = re.search(r"\bWPH\s?(\d{2})\b", t, re.I)
    if mw and (sess or re.search(r"past|paper|solved|walkthrough|part \d of \d", t, re.I)):
        tb([course], vid, prov, t,
           f"IAL physics WPH {mw.group(1)} paper register anchor (unit {mw.group(1)[0]}, the P19 spaced form of the P14 Assil law)")
        return True
    if un and (sess or re.search(r"past|paper|solved|walkthrough", t, re.I)):
        tb([course], vid, prov, t,
           f"IAL {'biology' if subj=='bio' else ('chemistry' if subj=='chem' else 'physics')} Unit {un.group(1)} + session/paper reference — unit-paper review anchor (the P14 Assil law analog)")
        return True
    if is_article:
        tb([course], vid, prov, t,
           "IAL scientific-article paper register anchor (Unit 5 article — Pearson Edexcel A-level named)")
        return True
    return False

def cie_alevel_sci_anchor(vid, prov, t):
    subj = None
    if RE_9700.search(t): subj = ("bio", "cie-as-biology-25", "cie-a-level-biology-25")
    elif RE_9701.search(t): subj = ("chem", "cie-as-chemistry-25", "cie-a-level-chemistry-25")
    elif RE_9702.search(t): subj = ("phys", "cie-as-physics-25", "cie-a-level-physics-25")
    if not subj:
        return False
    n = paper_num(t)
    if RE_SESSION.search(t) or RE_SOLVED.search(t):
        if n in (4, 5):
            tb([subj[2]], vid, prov, t, f"CIE A-level {subj[0]} paper {n} session/paper register anchor (papers 4-5 -> A2)")
        elif n in (1, 2, 3):
            tb([subj[1]], vid, prov, t, f"CIE AS {subj[0]} paper {n} session/paper register anchor (papers 1-3 -> AS)")
        elif re.search(r"\bAS\b", t) and not re.search(r"\bA2?\b", t):
            tb([subj[1]], vid, prov, t, f"CIE AS {subj[0]} session/paper register anchor (AS named, paper not stated)")
        elif re.search(r"\bA2?\b|\bA\s?[Ll]evel\b", t):
            tb([subj[2]], vid, prov, t, f"CIE A-level {subj[0]} session/paper register anchor (A-level named, paper not stated)")
        else:
            tb([subj[1], subj[2]], vid, prov, t, f"CIE {subj[0]} session/paper register anchor — AS/A2 not stated, both bound (disclosed)")
        return True
    return False

def maths058_anchor(vid, prov, t):
    """0580/0980 paper routing (the P9/P14 law: papers 2/4 extended, 1/3 core).
    Code-required — bare 'IGCSE Maths' titles never reach here unless the pool
    law routes them (the ginger Cambridge-context amendment)."""
    n = paper_num(t)
    if n and RE_SESSION.search(t) and RE_SOLVED.search(t):
        course = "cie-igcse-maths-25-extended" if n in (2, 4) else "cie-igcse-maths-25-core"
        tb([course], vid, prov, t, f"0580 paper {n} + session (P9 law: papers 2/4 extended, 1/3 core)")
        return True
    ext = bool(re.search(r"extended|paper\s*[24]\b|p[24]\b", t, re.I))
    core = bool(re.search(r"core|paper\s*[13]\b|p[13]\b", t, re.I))
    course = "cie-igcse-maths-25-extended" if ext else ("cie-igcse-maths-25-core" if core else "cie-igcse-maths-25-extended")
    if bind_course(course, vid, prov, t):
        return True
    skip(CURRENT_PROV[0], vid, t, f"0580 title with no distinctive match in {course} at the df<=3 bar")
    return True

def maths0607_anchor(vid, prov, t):
    """0607 International Maths (the NEW P19 register): papers 2/4/6 extended,
    1/3/5 core (the 0607 paper scheme); unstated -> both, disclosed."""
    n = paper_num(t)
    pair = ["cie-igcse-maths-international-maths-23-extended", "cie-igcse-maths-international-maths-23-core"]
    if n and RE_SESSION.search(t) and RE_SOLVED.search(t):
        tb([pair[0] if n in (2, 4, 6) else pair[1]], vid, prov, t,
           f"0607 International Maths paper {n} + session register anchor (the NEW P19 register; papers 2/4/6 extended, 1/3/5 core)")
        return True
    if n and RE_SOLVED.search(t):
        tb([pair[0] if n in (2, 4, 6) else pair[1]], vid, prov, t,
           f"0607 International Maths paper {n} register anchor (the NEW P19 register)")
        return True
    ext = bool(re.search(r"extended", t, re.I))
    core = bool(re.search(r"core", t, re.I))
    if ext or core:
        if bind_course(pair[0] if ext else pair[1], vid, prov, t):
            return True
        skip(CURRENT_PROV[0], vid, t, "0607 title with no distinctive match at the df<=3 bar")
        return True
    for c in pair:
        if bind_course(c, vid, prov, t):
            return True
    skip(CURRENT_PROV[0], vid, t, "0607 title with no distinctive match in the international-maths pair at the df<=3 bar")
    return True

def em_anchor(vid, prov, t):
    """0680 Environmental Management."""
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb(["cie-igcse-environmental-management-25"], vid, prov, t, "0680 session/paper register anchor")
        return True
    if bind_course("cie-igcse-environmental-management-25", vid, prov, t):
        return True
    skip(CURRENT_PROV[0], vid, t, "0680 title with no distinctive match in cie-igcse-environmental-management-25 at the df<=3 bar")
    return True

# ---------------------------------------------------------------- P19 pool laws

def law_igbiocomplete(vid, t):
    prov = "igbiocomplete"
    subj = None
    if SUBJ_RE["bio"].search(t): subj = "bio"
    elif SUBJ_RE["chem"].search(t): subj = "chem"
    elif SUBJ_RE["phys"].search(t): subj = "phys"
    if not subj:
        skip(prov, vid, t, "no CIE IGCSE science subject register (the pool's register is the CIE trio)")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if tnum_anchor(vid, prov, t, subj):
        return
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb([TRIO[subj]], vid, prov, t, f"CIE IGCSE {subj} session/paper register anchor (subject-name register, disclosed)")
        return
    if bind_course(TRIO[subj], vid, prov, t):
        return
    skip(prov, vid, t, f"no honest binding at the df<=3 bar in cie-igcse-{subj}-23 (the CIE subject-name register binds at the ladder bar only)")

def law_studybuddy(vid, t):
    prov = "igcse-study-buddy"
    code_subj = None
    if RE_0610.search(t): code_subj = "bio"
    elif RE_0620.search(t): code_subj = "chem"
    elif RE_0625.search(t): code_subj = "phys"
    if not code_subj:
        skip(prov, vid, t, "no CIE IGCSE science code register (the pool's register is the coded CIE trio)")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if tnum_anchor(vid, prov, t, code_subj):
        return
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb([TRIO[code_subj]], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    if bind_course(TRIO[code_subj], vid, prov, t):
        return
    skip(prov, vid, t, f"no honest binding at the df<=3 bar in cie-igcse-{code_subj}-23")

def law_edubbey(vid, t):
    prov = "edubbey"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0417.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
            return
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
        skip(prov, vid, t, "0417 title with no distinctive match in cie-igcse-ict-21 at the df<=3 bar")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_0455.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
                tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        for c in ["cie-igcse-economics-25", "cie-igcse-economics-20"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0455 title with no distinctive match in the economics pair at the df<=3 bar")
        return
    if RE_0450.search(t) or re.search(r"Business\s+Studies", t, re.I):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-business-25"], vid, prov, t, "0450/7115 business paper register anchor (the NEW P19 register; the 7115 token is the O-Level dual branding, disclosed)")
            return
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
        skip(prov, vid, t, "0450 title with no distinctive match in cie-igcse-business-25 at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in cl:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_precool(vid, t):
    prov = "precool-skillz"
    subj = None
    if re.search(r"i?GCSE\s*\|?\s*ICT|i?GCSE\s+ICT", t, re.I): subj = "ict"
    elif SUBJ_RE["phys"].search(t): subj = "phys"
    elif SUBJ_RE["chem"].search(t): subj = "chem"
    elif re.search(r"i?GCSE\s*\|?\s*Economics|Economics\s*#\d", t, re.I): subj = "econ"
    elif re.search(r"i?GCSE\s*\|?\s*Business", t, re.I): subj = "business"
    if not subj:
        skip(prov, vid, t, "no subject-name register (the pool's register is the iGCSE subject series)")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    course_map = {"ict": "cie-igcse-ict-21", "phys": "cie-igcse-physics-23",
                  "chem": "cie-igcse-chemistry-23", "econ": "cie-igcse-economics-25",
                  "business": "cie-igcse-business-25"}
    if bind_course(course_map[subj], vid, prov, t):
        return
    skip(prov, vid, t, f"no honest binding at the df<=3 bar in {course_map[subj]} (subject-name register binds at the ladder bar only)")

def law_savemyexams(vid, t):
    prov = "save-my-exams"
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board register (AQA/OCR/IB/...) — the mixed-board remainder, disclosed")
        return
    if RE_GCSE_LIT.search(t) or re.search(r"GCSE\s+English\s+Lit", t, re.I):
        lit_law(vid, t, prov)
        return
    if re.search(r"GCSE\s+Computer\s+Science", t, re.I):
        skip(prov, vid, t, "GCSE Computer Science (OCR/UK register) — no spine course")
        return
    if RE_ED_CS.search(t):
        skip(prov, vid, t, "Edexcel UK-GCSE Computer Science — no spine course")
        return
    # UK-GCSE board-tagged form ('GCSE Physics (Edexcel)') without an IGCSE token
    if re.search(r"GCSE\s+[\w ]+\(Edexcel\)", t, re.I) and not RE_IGCSE_TOK.search(t):
        skip(prov, vid, t, "UK-GCSE Edexcel register (GCSE X (Edexcel) form, no International token) — the corbettmaths exclusion class")
        return
    if re.search(r"GCSE\s*&\s*IGCSE\s*Maths|GCSE\s*/\s*IGCSE\s*Maths", t, re.I):
        skip(prov, vid, t, "generic GCSE/IGCSE maths exam-tips register — no syllabus code, guidance")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_ED_IG.search(t) and re.search(r"Chemistry|Biology|Physics", t, re.I):
        ecl = ed_science_anchor(t)
        if ecl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
            for c in ecl:
                tb([c], vid, prov, t, "Edexcel IGCSE science paper register anchor (4CH1/4BI1/4PH1/4SD0)")
            return
        for c in ecl or ["igcse-chemistry-19", "igcse-biology-19", "igcse-physics-19"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "Edexcel IGCSE science title with no distinctive match at the df<=3 bar")
        return
    # CIE subject-name register (the T2 disclosed posture: 'IGCSE {Subject}' = the CIE IGCSE catalogue form)
    if re.search(r"CIE\s+IGCSE\s+Computer\s+Science|\b0478\b", t, re.I):
        if bind_course("cie-igcse-computer-science-23", vid, prov, t):
            return
        skip(prov, vid, t, "CIE 0478 title with no distinctive match in cie-igcse-computer-science-23 at the df<=3 bar")
        return
    for subj, course in [("Biology", "cie-igcse-biology-23"), ("Chemistry", "cie-igcse-chemistry-23"),
                         ("Physics", "cie-igcse-physics-23"), ("Economics", "cie-igcse-economics-25"),
                         ("Business", "cie-igcse-business-25"), ("ICT", "cie-igcse-ict-21")]:
        if re.search(rf"IGCSE\s*[- ]?\s*{subj}\b|\b{subj}\s*[- ]\s*(IGCSE|Exam Question)", t, re.I):
            if bind_course(course, vid, prov, t):
                return
            skip(prov, vid, t, f"IGCSE {subj} title with no distinctive match in {course} at the df<=3 bar")
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_ginger(vid, t):
    prov = "ginger-mathematician"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the Cambridge-branded advice/motivation/news remainder)")
        return
    if RE_0607.search(t):
        maths0607_anchor(vid, prov, t)
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the 4037 token is the O-Level dual branding)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match at the df<=3 bar")
        return
    # bare 'iGCSE Maths' topic lectures — the Cambridge-context amendment (disclosed):
    # this pool's register read of record is CIE 0580, NOT the P18 RE_4MA1 generic form
    if re.search(r"i?GCSE\s+Maths?\b", t, re.I) and not re.search(r"GCSE\s+Maths?\b", t, re.I):
        maths058_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (the pool's maths registers are CIE 0580/0607/0606; bare-IGCSE form only)")

def law_sciencewithchun(vid, t):
    prov = "sciencewithchun"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0654_SEC.search(t) and RE_COORDD.search(t):
        if sec0654_anchor(vid, prov, t):
            return
    if RE_COORDD.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or paper_num(t)):
        tb(COORD_TRIO, vid, prov, t, "0654 co-ordinated sciences session/paper anchor — shared-paper binding to all three sciences (disclosed)")
        return
    if re.search(r"IGCSE\s+Chemistry", t, re.I):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE chemistry title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is 0654 section-scoped questions-by-topic)")

def law_ict_pools(vid, t, prov):
    # the P18 fiifi pattern: ICT code/register anchors adjudicate BEFORE the
    # guidance gate (the 0417 token is machine-checkable; skills-video titles
    # like 'Using the slide master in PowerPoint' are content, not guidance)
    it1 = bool(RE_4IT0.search(t))
    it0417 = bool(RE_0417.search(t))
    if it1 and it0417:
        tb(["igcse-ict-17"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — Edexcel side anchor")
        tb(["cie-igcse-ict-21"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — CIE side anchor (dual-coded, disclosed)")
        return
    if it1:
        tb(["igcse-ict-17"], vid, prov, t, "Edexcel International GCSE ICT (4IT1) register anchor")
        return
    if it0417 and (RE_SESSION.search(t) or RE_SOLVED.search(t) or paper_num(t)):
        tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if it0417:
        # the skills-video subset ('(0417) Using X in spreadsheets (Excel)'):
        # the code register is established, the ladder binds where the skill
        # tokens are distinctive in the 0417 spine
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
        skip(prov, vid, t, "0417 title with no distinctive match in cie-igcse-ict-21 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 0417 session/paper form; channel promos skip)")

def law_misstech(vid, t):
    law_ict_pools(vid, t, "miss-tech-teacher")

def law_mrkhan(vid, t):
    law_ict_pools(vid, t, "mr-khan-ict-solutions")

def law_tatchen(vid, t):
    prov = "ict-with-tatchen"
    # the P18 fiifi pattern: the 0417 code register adjudicates before the
    # guidance gate (the series' clickbait suffixes ride on real content)
    it1 = bool(RE_4IT0.search(t))
    it0417 = bool(RE_0417.search(t))
    if it1 and it0417:
        tb(["igcse-ict-17"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — Edexcel side anchor")
        tb(["cie-igcse-ict-21"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — CIE side anchor (dual-coded, disclosed)")
        return
    if it1:
        tb(["igcse-ict-17"], vid, prov, t, "Edexcel International GCSE ICT (4IT1) register anchor")
        return
    if it0417 and (RE_SESSION.search(t) or RE_SOLVED.search(t) or paper_num(t)):
        tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
        return
    if it0417:
        # the chapter-scoped lecture series: the pool's own chapter-structured
        # 0417 series names chapter N — the chapter index is the bind evidence
        # (the series' paren concept labels self-verify the scheme, e.g.
        # 'Chapter 2 Full Revision Video (Input & Output Devices)'); the
        # token-agreement fast path binds at low, the index-only path at the
        # disclosed title-only bar
        m = RE_CHAPTER.search(t)
        if m:
            n = int(m.group(1))
            tp = topic_at_index("cie-igcse-ict-21", n)
            if tp:
                pts = topic_points("cie-igcse-ict-21", tp["title"])
                if pts:
                    frac, ninter = token_agreement(t, tp["title"])
                    route("cie-igcse-ict-21", vid, prov, [p["code"] for p in pts], "low",
                          f"chapter-scoped register: the pool's chapter-structured 0417 series names chapter {n} "
                          f"'{tp['title'][:60]}'" + (f" (stem agreement {ninter} token(s))" if frac >= 0.5 and ninter >= 1 else
                          " (index-consistent with the 0417 theory-chapter scheme, the disclosed chapter-index bind)") +
                          " — topic points bound at the disclosed title-only bar", None)
                    return
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
        skip(prov, vid, t, "0417 title with no distinctive match in cie-igcse-ict-21 at the df<=3 bar")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 0417 lecture series)")

def law_shayan(vid, t):
    prov = "rapid-revision-with-shayan"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/exam-technique register (P12 gate; the 'Day N' technique series)")
        return
    if RE_0452.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
                tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — the 'O level/' form is the disclosed 7707 O-Level dual branding")
            return
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0452 title with no distinctive match in the accounting pair at the df<=3 bar")
        return
    if RE_0455.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
                tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        for c in ["cie-igcse-economics-25", "cie-igcse-economics-20"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0455 title with no distinctive match in the economics pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are the 0452/0455 'O level/ IGCSE' forms)")

def law_bookkeepers(vid, t):
    prov = "bookkeepers-journal"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"Edexcel\s+(AS|A2?|IAS|IA2)\s+[Ll]evel", t, re.I) or re.search(r"Edexcel\s+I?AS\s+Accounting", t, re.I):
        skip(prov, vid, t, "Edexcel AS/IAL Accounting & Business register (WBS/WAC) — no spine course (the spine carries CIE 0452/9609)")
        return
    if RE_4BS1.search(t) or re.search(r"Edexcel\s+IGCSE\s+Business", t, re.I):
        if bind_course("igcse-business-19", vid, prov, t):
            return
        skip(prov, vid, t, "4BS1 title with no distinctive match in igcse-business-19 at the df<=3 bar")
        return
    if RE_0452.search(t):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0452/IGCSE-accounting title with no distinctive match in the accounting pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_accountingcelebrity(vid, t):
    prov = "accounting-celebrity"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"A\s?[Ll]evel\s+Accounting|9706", t, re.I):
        skip(prov, vid, t, "A-level accounting register (9706) — no spine course")
        return
    if RE_0452.search(t):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0452/IGCSE-accounting title with no distinctive match in the accounting pair at the df<=3 bar (the generic accounting-shorts remainder)")
        return
    skip(prov, vid, t, "no syllabus register on the title (the generic accounting-shorts remainder, 7% density disclosed)")

def law_muzammil(vid, t):
    prov = "muzammil-ameer-acma"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9609.search(t):
        # the CIE-declared 9609 pool: 'Business AS/A Level' unit-series form binds
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-as-business-23", "cie-a-level-business-23"]:
                tb([c], vid, prov, t, "9609 business paper register anchor — bound to both AS and A-level courses (shared code, disclosed)")
            return
        as_first = bool(re.search(r"\bAS\b|Business\s+AS|unit\s*[1-5]", t, re.I))
        for c in (["cie-as-business-23", "cie-a-level-business-23"] if as_first else ["cie-a-level-business-23", "cie-as-business-23"]):
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "9609 title with no distinctive match in the business pair at the df<=3 bar")
        return
    if RE_0450.search(t) or re.search(r"Business\s+Studies", t, re.I):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-business-25"], vid, prov, t, "0450/7115 business paper register anchor (the NEW P19 register)")
            return
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
        skip(prov, vid, t, "0450 title with no distinctive match in cie-igcse-business-25 at the df<=3 bar")
        return
    if RE_0452.search(t):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0452 title with no distinctive match in the accounting pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (bare 'AS/AL' forms without a syllabus register skip honestly)")

def law_saifullah(vid, t):
    prov = "saifullah-ajaz"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0450.search(t) or re.search(r"7115|O\s?[Ll]evels?\s+Business", t, re.I):
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
        skip(prov, vid, t, "0450/7115 title with no distinctive match in cie-igcse-business-25 at the df<=3 bar")
        return
    if RE_9609.search(t):
        as_first = bool(re.search(r"\bAS\b|As\s+[Ll]evel|unit\s*[1-5]", t, re.I))
        for c in (["cie-as-business-23", "cie-a-level-business-23"] if as_first else ["cie-a-level-business-23", "cie-as-business-23"]):
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "9609 title with no distinctive match in the business pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (registration/promo remainder skipped by the promo gate)")

def law_visiblehand(vid, t):
    prov = "the-visible-hand"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9708.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-a-level-economics-23"], vid, prov, t, "9708 A-level economics paper register anchor (incl. the 'Cambridge AS/A2 Economics' P19 form)")
            return
        if bind_course("cie-a-level-economics-23", vid, prov, t):
            return
        skip(prov, vid, t, "9708 title with no distinctive match in cie-a-level-economics-23 at the df<=3 bar")
        return
    if RE_0455.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
                tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        for c in ["cie-igcse-economics-25", "cie-igcse-economics-20"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0455 title with no distinctive match in the economics pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 9708/0455 session-QP forms)")

def law_yourtutors(vid, t):
    prov = "your-igcse-tutors"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"\b0523\b|Chinese\s+as\s+a\s+Second\s+Language", t, re.I):
        skip(prov, vid, t, "0523 Chinese as a Second Language register — no spine course")
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the 4037 token is the O-Level dual branding)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match at the df<=3 bar")
        return
    if RE_0455.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
                tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        for c in ["cie-igcse-economics-25", "cie-igcse-economics-20"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0455 title with no distinctive match in the economics pair at the df<=3 bar")
        return
    if RE_0452.search(t):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "0452 title with no distinctive match in the accounting pair at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor (the disclosed 0972 dual)")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_efsuccess(vid, t):
    prov = "education-for-success"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"STP\s+Mathematics|Grade\s*[1-8]\b|Primary|Grade\s*[1-8]\s*Mathematics", t, re.I):
        skip(prov, vid, t, "school-internal maths register (STP/Grade 6 textbooks) — not the International spine")
        return
    if RE_0680.search(t):
        em_anchor(vid, prov, t)
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    skip(prov, vid, t, "no honest binding (the school channel's non-International remainder)")

def law_physicsexaminer(vid, t):
    prov = "the-physics-examiner"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_WPH.search(t) or re.search(r"IAL\s+Physics", t, re.I):
        if ial_unit_anchor(vid, prov, t, subject="phys"):
            return
        if bind_course("ial-physics-19", vid, prov, t):
            return
        skip(prov, vid, t, "IAL physics title with no distinctive match in ial-physics-19 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the WPH paper walkthrough series)")

def law_benzakademi(vid, t):
    prov = "benzakademi"
    if RE_ANNA8291.search(t):
        skip(prov, vid, t, "Anna-university GE8291 EVS register (the P19 false-density call of record: 'GE 8291' is the Indian university EVS paper, NOT Cambridge AS Environmental Management — the P17 nevdoes/indigo precedent)")
        return
    skip(prov, vid, t, "no honest binding (the CBSE/ISC/+1,+2 Indian-board remainder)")

def law_academicplus(vid, t):
    prov = "academic-plus"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"\b9609\b", t):
        if bind_course("cie-as-business-23", vid, prov, t) or bind_course("cie-a-level-business-23", vid, prov, t):
            return
        skip(prov, vid, t, "9609 title with no distinctive match in the business pair at the df<=3 bar")
        return
    if RE_4BS1.search(t) or re.search(r"Edexcel\s+i?GCSE\s+Business", t, re.I):
        if bind_course("igcse-business-19", vid, prov, t):
            return
        skip(prov, vid, t, "4BS1 title with no distinctive match in igcse-business-19 at the df<=3 bar")
        return
    skip(prov, vid, t, "bare 'A-Level Business' form with no board register (the thin-multi T2 disclosure: the gate's 'A-Level Business' family read was board-agnostic — the indigo false-density precedent)")

def law_revisionnotebook(vid, t):
    prov = "the-revision-notebook"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9609.search(t):
        if bind_course("cie-as-business-23", vid, prov, t) or bind_course("cie-a-level-business-23", vid, prov, t):
            return
        skip(prov, vid, t, "9609 title with no distinctive match in the business pair at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 9609 short-notes series)")

def law_mohaiminul(vid, t):
    prov = "maths-with-mohaiminul"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4MB1.search(t):
        if bind_course("igcse-maths-b-16", vid, prov, t):
            return
        skip(prov, vid, t, "4MB1 title with no distinctive match in igcse-maths-b-16 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 4MB1 maths-B series)")

def law_easyedu(vid, t):
    prov = "easy-edu"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4MB1.search(t):
        if bind_course("igcse-maths-b-16", vid, prov, t):
            return
        skip(prov, vid, t, "4MB1 title with no distinctive match in igcse-maths-b-16 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 4MB1 lecture series)")

def law_revwise(vid, t):
    prov = "revwise"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    ecl = ed_science_anchor(t)
    if ecl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in ecl:
            tb([c], vid, prov, t, "Edexcel IGCSE science paper register anchor (4CH1/4BI1/4PH1/4SD0)")
        return
    if ecl:
        for c in ecl:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "Edexcel IGCSE science title with no distinctive match at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in cl:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses (the mixed NT x34 remainder, disclosed)")

def law_easy(vid, t):
    law_easyedu(vid, t)

# ---------------------------------------------------------------- Class W (P16 predicate, P17/P18 amendments)
LIT_SPINE = json.load(open(f"{HUB}/spines/cie-igcse-english-literature-21.json"))
HUGHES15 = ["The Thought-Fox", "The Harvest Moon", "The Jaguar", "Football at Slack",
            "The Horses", "Roe-Deer", "Wind", "A Memory", "Relic", "Telegraph Wires",
            "Hawk Roosting", "Anniversary", "Cat and Mouse", "The Other", "Snowdrop"]

def lw_norm(s):
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def lw_clean(t):
    return t.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')

lit_specs = []
_cur_author = None
for n in LIT_SPINE["curriculum"]["nodes"]:
    if n.get("family") != "SPEC_POINT":
        continue
    raw, code = n.get("title", ""), n.get("code")
    t = lw_clean(raw)
    author, works, kind = None, [], "structural"
    m = re.match(r"^(.{2,60}?),\s*'(.+)'$", t)
    if m:
        author, works, kind = m.group(1), [m.group(2)], "poem"
        if "following 15 poems" in works[0] or "may be found" in works[0]:
            author, works, kind = None, [], "structural"
    else:
        sm = re.match(r"^.*?From Stories of Ourselves Volume 2\s*,\s*the following 10 stories:(.*)$", t, re.S)
        if sm:
            segs = re.split(r"no\.\s*\d+\s*", sm.group(1))
            works, authors = [], []
            for seg in segs:
                m2 = re.match(r"^(.{2,60}?),\s*'((?:[^']|'(?=\w))+?)'(?!\w)", seg.strip())
                if m2:
                    authors.append(m2.group(1)); works.append(m2.group(2))
            author, works, kind = authors or None, works, "stories-list" if works else "structural"
        elif re.match(r"^Ted Hughes,?\s+the following 15 poems", t, re.I):
            author, works, kind = "Ted Hughes", [], "hughes-header"
        elif re.match(r"^(The Thought-Fox|The Jaguar|The Horses|Wind|Relic|Hawk Roosting|Cat and Mouse|Snowdrop)\b", t.strip()):
            works = [p for p in HUGHES15 if lw_norm(p) in " " + lw_norm(t) + " "]
            author, works, kind = _cur_author, works, "hughes-pair" if works else "structural"
        else:
            cleaned = re.sub(r"\s*(begin teaching, check the set text list.*|Requirements:.*|Resources:.*|Cambridge School Shakespeare.*|Cambridge Literature series.*|Penguin Shakespeare.*|Oxford School Shakespeare.*|Heinemann Shakespeare.*|Longman School Shakespeare.*)$", "", t, flags=re.I)
            am = re.match(r"^((?:[A-Z][\w'.-]*\s+){1,3}?)([A-Z].+)$", cleaned)
            if am and not re.match(r"^(Candidates|From|Set texts|These)", cleaned):
                author, kind = am.group(1).strip(), "prose-drama"
                words = cleaned.split()
                works = [" ".join(words[k:]) for k in range(1, min(4, len(words)))]
    if kind == "hughes-header":
        _cur_author = author
    elif kind != "hughes-pair":
        _cur_author = None
    lit_specs.append({"code": code, "raw": raw, "author": author, "works": works, "kind": kind})
assert len(lit_specs) == 203, f"lit spec count {len(lit_specs)} != 203"

CIE_TOKEN = re.compile(r"cambridge|igcse|\b0475\b|\bcie\b|literature", re.I)
AQA_BOARD = re.compile(r"\bAQA\b|\bEduqas\b|WJEC|Edexcel|\bGCSE\b(?!.*(cambridge|igcse))|English Language Paper", re.I)
GUIDANCE = re.compile(r"^(what is|top five|top tips|dos and don|the art of persuasion|analysing language|identifying and talking)|writing errors|essay skills|keep language analysis|essays? (are|is) flopping|language english vs igcse", re.I)
NOBIND_CHARS = ["Malvolio", "Caliban", "Sybil", "Eric Birling", "Mr Hyde", "Scrooge", "Cratchit", "Juliet", "Banquo", "Miranda", "Ferdinand", "Macbeth", "Lady Macbeth"]
LW_SUFFIX_COLLISIONS = {"singh song": "song"}
TRAIL_JUNK = re.compile(
    r"\s*(\[?part\s+\d+(\s+of\s+\d+)?\]?|part\s+\d+|analysis|detailed analysis|"
    r"detailed commentary and analysis|commentary and analysis|full analysis|"
    r"line by line analysis|line by line|detailed commentary|commentary|"
    r"study guide.*)$", re.I)

def lw_extract(title):
    t = lw_clean(title)
    low = lw_norm(title)
    flags = {"aqaBoard": bool(AQA_BOARD.search(t) and not re.search(r"cambridge|igcse", t, re.I)),
             "multi": False}
    spans, author = [], None
    mb = re.search(r"\bby\s+([A-Z][\w'.-]*(?:\s+[A-Z][\w'.-]+){0,3})", t)
    if mb: author = mb.group(1)
    mp = re.search(r"\b(?:by|of)\s+([A-Z][\w'.-]*(?:'s)?)\s*'", t)
    if mp and author is None: author = mp.group(1)
    for q in re.findall(r"'((?:[^']|'(?=\w))+?)'(?!\w)(?=\s*by\b|\s*[\u2013\-:;,()]|\s*#|$)", t):
        if len(lw_norm(q)) >= 3: spans.append(q)
    segs = [s for s in re.split(r"\s+-\s+", t) if s.strip()]
    for i, seg in enumerate(segs):
        ns = lw_norm(seg)
        if len(ns) >= 4: spans.append(seg)
        if 0 < i < len(segs) - 1 and len(ns.split()) <= 3 and not re.search(r"\d", ns) \
           and not re.search(r"igcse|literature|cambridge", ns, re.I) and author is None:
            author = seg
    if ":" in t:
        head = t.split(":")[0]
        if not re.search(r"insights|tips", head, re.I) and len(lw_norm(head)) >= 4:
            spans.append(head)
    for mseg in re.findall(r"(?::|\()\s*([^:()]{10,140}?)(?:\)|$)", t):
        if "," in mseg and not re.search(r"Act\s|scene\s", mseg):
            parts = mseg.split(",")
            good = [p for p in parts if 3 <= len(lw_norm(p)) <= 60]
            if len(good) >= 2:
                spans += good; flags["multi"] = True
    mu = re.match(r"^(.{2,90}?)\s+by\s+[A-Z]", t)
    if mu and not re.search(r"\bAct\s+\d\b", mu.group(1)):
        spans.append(mu.group(1))
    mj = re.match(r"^([A-Z][^:]{2,60}?)\s+Act\s+(?:[IVXLC]+|\d+)", t)
    if mj: spans.append(mj.group(1))
    if re.search(r"hughes", low):
        for h in HUGHES15:
            nh = lw_norm(h)
            if re.search(r"(?<![a-z0-9])" + re.escape(nh) + r"(?![a-z0-9])", low):
                spans.append(h)
    seen, out = set(), []
    for w in spans:
        nw = lw_norm(w)
        while True:
            nw2 = TRAIL_JUNK.sub("", nw).strip()
            if nw2 == nw: break
            nw = nw2
        if nw and nw not in seen:
            seen.add(nw); out.append(nw)
    return author, out, flags

def lw_spine_hits(span):
    hits = []
    tail2 = " ".join(span.split()[-2:]) if len(span.split()) >= 2 else ""
    for s in lit_specs:
        if not s["works"]: continue
        for w in s["works"]:
            nw = lw_norm(w)
            if not nw: continue
            if span == nw or (len(nw) >= 4 and span.endswith(" " + nw)) \
               or nw == "the " + span or nw == "a " + span:
                if tail2 in LW_SUFFIX_COLLISIONS and LW_SUFFIX_COLLISIONS[tail2] == nw \
                   and span != nw:
                    continue
                hits.append(s); break
    return hits

def lw_author_ok(title_author, spec_author):
    if not title_author: return True
    ta = set(lw_norm(title_author).split())
    if not ta: return True
    sa_list = spec_author if isinstance(spec_author, list) else [spec_author]
    if not sa_list or all(not s for s in sa_list): return True
    for sa in sa_list:
        sa_t = set(lw_norm(sa).split())
        if (ta & sa_t) or (ta <= sa_t) or (sa_t <= ta):
            return True
    return False

LIT_KEEPS = []
def lit_law(vid, t, prov):
    author, works, flags = lw_extract(t)
    if GUIDANCE.search(t):
        skip(prov, vid, t, "guidance/skills register with no set-text bind (guidance register law)")
        return
    if flags["aqaBoard"] and not any(lw_spine_hits(w) for w in works):
        skip(prov, vid, t, "title carries the AQA/Eduqas/WJEC/Edexcel/GCSE register without a CIE token and names no spine set text")
        return
    matched = {}
    for w in works:
        hits = lw_spine_hits(w)
        if hits and lw_author_ok(author, hits[0]["author"]):
            matched[w] = hits
    if matched:
        allcodes = []
        for w, hs in matched.items():
            allcodes += [h["code"] for h in hs]
        allcodes = list(dict.fromkeys(allcodes))
        has_author = author is not None
        single = len(matched) == 1
        confidence = "medium" if (single and has_author) else "low"
        reason = ("set-text work bind (Class W): title names spine set text(s) "
                  + "; ".join(f"'{w}' -> {', '.join(h['code'] for h in hs)}" for w, hs in list(matched.items())[:3])
                  + f"; multi-year occurrence(s) disclosed (the P13 shared-unit precedent)"
                  + ("; author cross-checked" if has_author else "; title-only posture, work-name bind"))
        route(LIT, vid, prov, allcodes, confidence, reason)
        LIT_KEEPS.append(vid)
        return
    cls = "work not on the 2023-2025 set-text lists"
    if any(c.lower() in t.lower() for c in NOBIND_CHARS):
        cls = "character-study title without a set-text token"
    skip(prov, vid, t, cls + " (lit register, no honest Class W bind)")

# ---------------------------------------------------------------- run
LAWS = {
    "igbiocomplete": law_igbiocomplete,
    "maths-with-mohaiminul": law_mohaiminul,
    "mr-khan-ict-solutions": law_mrkhan,
    "miss-tech-teacher": law_misstech,
    "ict-with-tatchen": law_tatchen,
    "rapid-revision-with-shayan": law_shayan,
    "the-visible-hand": law_visiblehand,
    "muzammil-ameer-acma": law_muzammil,
    "saifullah-ajaz": law_saifullah,
    "bookkeepers-journal": law_bookkeepers,
    "your-igcse-tutors": law_yourtutors,
    "igcse-study-buddy": law_studybuddy,
    "ginger-mathematician": law_ginger,
    "sciencewithchun": law_sciencewithchun,
    "the-physics-examiner": law_physicsexaminer,
    "education-for-success": law_efsuccess,
    "edubbey": law_edubbey,
    "precool-skillz": law_precool,
    "save-my-exams": law_savemyexams,
    "accounting-celebrity": law_accountingcelebrity,
    "revwise": law_revwise,
    "benzakademi": law_benzakademi,
    "academic-plus": law_academicplus,
    "easy-edu": law_easy,
    "the-revision-notebook": law_revisionnotebook,
}
assert set(LAWS) == set(JUDGMENT_POOLS)

OLEVEL_EXEMPT = {}

TITLE_OF = {v["id"]: v["title"] for v in pool}

def main():
    for slug, law in LAWS.items():
        CURRENT_PROV[0] = slug
        n0_t, n0_a, n0_s = len(tier_b), sum(len(x) for x in judgment.values()), len(skips)
        judge_pool(slug, law, OLEVEL_EXEMPT.get(slug))
        print(f"[{slug}] anchors +{len(tier_b)-n0_t}, routed +{sum(len(x) for x in judgment.values())-n0_a}, skips +{len(skips)-n0_s}", flush=True)

    # NT/UK-GCSE final sanity pass
    nt_leak = [r for vs in judgment.values() for r in vs if r['action'] == 'keep' and RE_NT_BOARD.search(TITLE_OF[r['id']])]
    for r in nt_leak:
        r["action"] = "skip"
        r["reason"] = "NT-board register caught on the final sanity pass — re-adjudicated to skip"
        skips.append({"video": r["id"], "title": TITLE_OF[r["id"]][:160], "provider": r["provider"], "reason": r["reason"]})

    json.dump(tier_b, open(f"{WORK}/tier-b.json", "w"), indent=1)
    json.dump(judgment, open(f"{WORK}/judgment.json", "w"), indent=1)
    json.dump(skips, open(f"{WORK}/skips.json", "w"), indent=1)

    routed = {p["id"] for p in tier_b} | {r["id"] for vs in judgment.values() for r in vs if r["action"] == "keep"}
    skip_ids = {s["video"] for s in skips}
    overlap_rs = routed & skip_ids
    assert not overlap_rs, f"collisions routed/skipped: {list(overlap_rs)[:5]}"
    allacct = routed | skip_ids
    missing = [v["id"] for v in pool if v["id"] not in allacct]
    print(f"\ntier B anchors: {len(tier_b)} rows over {len({p['id'] for p in tier_b})} videos")
    print(f"tier A keeps: {sum(1 for vs in judgment.values() for r in vs if r['action']=='keep')} (lit keeps: {len(LIT_KEEPS)})")
    print(f"skips: {len(skips)}")
    print(f"disposition: {len(allacct)} of {len(pool)} accounts exactly-once; missing {len(missing)}")
    assert not missing, f"un-dispositioned: {missing[:5]}"
    by_course = {c: sum(1 for r in vs if r["action"] == "keep") for c, vs in judgment.items() if vs}
    print("keeps by course:", by_course)
    json.dump({"tierBRows": len(tier_b), "tierBVideos": len({p['id'] for p in tier_b}),
               "tierAKeeps": sum(1 for vs in judgment.values() for r in vs if r['action'] == 'keep'),
               "litKeeps": len(LIT_KEEPS), "skips": len(skips), "poolUploads": len(pool),
               "p19bCourses": P19B, "keepsByCourse": by_course},
              open(f"{WORK}/judgment_summary.json", "w"), indent=1)

if __name__ == "__main__":
    main()
