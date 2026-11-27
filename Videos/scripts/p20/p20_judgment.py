#!/usr/bin/env python3
"""P20 judgment: route the 35 admitted gap-profile pools (10,611 uploads) onto the
fresh post-P19 residual spine. Owner order this session: "run P20 judgment" (the
P20 filing PR #366 admitted as filed per the P15/P17/P18/P19 convention: the owner
order admits the pools and opens the judgment gate).

The P15/P17/P18/P19 gate ladder unchanged, with the registers the P20 profile filed:

  Tier B   paper-code anchors   — CIE A-level sciences 9700/9701/9702 papers 1-3 AS /
                                 4-5 A2 (the P13/P14 paper-number law); CIE A-level
                                 accounting 9706 papers 1-2 AS / 3-4 A2 (the P13
                                 accounting paper-level law); CIE A-level maths 9709
                                 components P1/P2/P3 pure + P4/M1 mechanics + P5/S1 +
                                 P6/S2 p&s (the P9 component law refined — the P20
                                 component routing of record; bare component-less
                                 walkthroughs still skip per ANCHOR-GRANULARITY section 6,
                                 the P9/P17/P18 precedent); 9618 papers 1-2 AS / 3-4 A2;
                                 0478/0984; 0606 (+ the disclosed 4037/4024 duals, incl.
                                 the '#additionalmathematics' hashtag session class);
                                 0580 papers 2/4 extended vs 1/3 core (the P9/P14 law);
                                 0610/0620/0625 (+ 0971/0972/0973 duals); 0653 combined
                                 (the shared-paper law: session walkthroughs bind all
                                 three combined faces); 0417/0983; 4IT1/4IT0 Ed-ICT;
                                 0452/0985 (+ the disclosed 7707 dual); 0455; 0450
                                 (+ the disclosed 7115/0264 new-code duals); 0680;
                                 0460 (both geo faces — the 2020/2025 shared-register
                                 pair); 9708; 9609 (pool-scoped); 4CH1/4BI1/4PH1/4SD0
                                 Ed-IGCSE (+ 4WCH1/2/4WPH1/2/4WB1/2 modular-24);
                                 WCH/WPH IAL unit-content + session anchors (the P14
                                 Assil law).

P20 disclosed register re-adjudications of record (the profile's density reads are
register-level; the language/read stays with the judgment — the gate's own law):
  1. mathlete-by-saad: the gate's '4MA1 x78' family read re-adjudicated as the generic
     IGCSE/O-Level 0580 class per the ginger law (disclosed false density) — the
     honest register is 0606/9709/0580; the 4MA1 deficits stay open.
  2. hendrik-academy: the IBDP 'Analysis and Approaches / Applications and
     Interpretation / Time Zone' register skips (no spine course); the explicit
     9709 component subset ('9709-s26-qp-33. Paper 3 Pure Mathematics 3') and the
     9702 paper subset bind honestly; bare maths content rides the IBDP class.
  3. walter-maths-tutoring: the 9231 further-maths register has NO spine course —
     skips honest (the P18 4PM0-analog terminal call); the t-test/confidence-interval
     series rides the 9231 class.
  4. the-lightup-hub: the lit adjudication rides the committed P16 Class W predicate
     (the P17/P18 amendments) — the AQA/UK-GCSE-branded remainder skips unless a
     spine set text is named; the unseen-poetry shorts are guidance-register (the
     lit-21 spine carries no unseen spec points — the profile's 'unseen 96' is the
     unmapped set-text structure, not a literal unseen register).
  5. umara-ratnayake: the IAL ICT (WIT) subset has NO spine course — skips honest;
     Edexcel IGCSE CS skips (the spine carries CIE 0478).

Exactly-once disposition of all 10,611 accounts, 0 collisions machine-checked.
Outputs work/p20/: tier-b.json, judgment.json, skips.json, judgment_summary.json
"""
import json, os, re, datetime
from collections import Counter

RES = "/home/z/my-project/worktrees/p20-judgment"
HUB = "/home/z/my-project/worktrees/p20-hub/apps/hub"
WORK = "/home/z/my-project/work/p20"
UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs(WORK, exist_ok=True)

JUDGMENT_POOLS = ["otterbiotutor", "ptet-chemistry", "study-with-prashna", "adam-viceroy",
                  "miss-natalie-chemistry", "mathlete-by-saad", "cswithmrg", "haguin-school",
                  "mr-lee-business-econ", "mr-mathew", "pla-academy-igcse-and-a-level-buddy",
                  "refactor-lab", "mathprep-with-ahmad-bilal", "salihath-syed-basheer",
                  "edex-world", "biochemlogy", "umara-ratnayake", "aslaug-eggertsdottir",
                  "s-q", "the-lightup-hub", "e-geo", "ilm-online-academy", "y-mx-c",
                  "miss-estruch-biology", "wimzee-cambridge-academy", "mysecondteacher",
                  "the-future-professionals", "chembase-school-of-chemistry",
                  "sayo-enoch-aluko", "hendrik-academy", "walter-maths-tutoring",
                  "maths-camp", "ishan", "biology-box", "the-cs-classroom"]

pool = []
_seen = set()
for slug in JUDGMENT_POOLS:
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        if v["id"] in _seen:
            continue
        _seen.add(v["id"])
        pool.append({"id": v["id"], "title": v["title"], "provider": slug})
TARGETS = [
    # CIE IGCSE sciences trio + combined + co-ordinated (0610/0620/0625/0653 families)
    "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
    "cie-igcse-science-combined-science-23-biology",
    "cie-igcse-science-combined-science-23-chemistry",
    "cie-igcse-science-combined-science-23-physics",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
    # Edexcel IGCSE sciences + DA-17 + modular-24 faces
    "igcse-chemistry-19", "igcse-biology-19", "igcse-physics-19",
    "igcse-science-double-award-17-biology",
    "igcse-science-double-award-17-chemistry",
    "igcse-science-double-award-17-physics",
    "igcse-biology-modular-24-unit-1", "igcse-biology-modular-24-unit-2",
    "igcse-chemistry-modular-24-unit-1", "igcse-chemistry-modular-24-unit-2",
    "igcse-physics-modular-24-unit-1", "igcse-physics-modular-24-unit-2",
    # CIE A-level sciences (9700/9701/9702) + IAL chem/phys (WCH/WPH)
    "cie-a-level-biology-25", "cie-as-biology-25",
    "cie-a-level-chemistry-25", "cie-as-chemistry-25",
    "cie-a-level-physics-25", "cie-as-physics-25",
    "ial-chemistry-17", "ial-physics-19",
    # accounting (9706 + 0452), business (9609 + 0450), economics (9708 + 0455)
    "cie-a-level-accounting-21", "cie-as-accounting-21",
    "cie-igcse-accounting-25", "cie-igcse-accounting-21",
    "cie-a-level-business-23", "cie-as-business-23", "cie-igcse-business-25",
    "cie-a-level-economics-23", "cie-igcse-economics-20",
    # CS (9618 + 0478) + ICT (4IT1 + 0417)
    "cie-a-level-computer-science-19", "cie-igcse-computer-science-23",
    "igcse-ict-17", "cie-igcse-ict-21",
    # geography (0460) + EM (0680)
    "cie-igcse-geography-25", "cie-igcse-geography-20",
    "cie-igcse-environmental-management-25",
    # maths (0580/0606/9709)
    "cie-igcse-maths-25-extended", "cie-igcse-maths-25-core",
    "cie-igcse-further-maths-additional-maths-25",
    "cie-a-level-maths-20-pure-1", "cie-a-level-maths-20-pure-2", "cie-a-level-maths-20-pure-3",
    "cie-as-maths-20-pure-1", "cie-as-maths-20-pure-2",
    "cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics",
    "cie-a-level-maths-20-probability-and-statistics-1",
    "cie-a-level-maths-20-probability-and-statistics-2",
]

P4_CHILDREN = set(json.load(open(f"{RES}/Videos/drafts/_p4/inheritance-map.json"))["parents"].keys())
P20B = [c for c in TARGETS if c in P4_CHILDREN]
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
        # P20 disclosed amendment: the dash-run chapter form ("13-3: ...") of the
        # otterbiotutor/biochemlogy 9700 lesson series — dash->dot, gated by stem
        # token agreement so playlist indices and qp-forms cannot false-bind.
        m2 = re.search(r"(?<!\d)(\d{1,2})[-\u2013](\d{1,2})(?![\d.])", title)
        if m2:
            s2 = sub_by_num(course, m2.group(1), m2.group(2))
            if s2:
                frac, ninter = token_agreement(title, s2["title"])
                if frac >= 0.3 and ninter >= 1:
                    pts = sub_points(course, s2["code"])
                    if pts:
                        return (f"{m2.group(1)}.{m2.group(2)}", s2, pts)
        return None
    num = f"{m.group(1)}.{m.group(2)}"
    subs = [s for s in specs_spine[course]["subs"] if s["code"].split(":")[-1].replace("SUB", "") == num]
    if subs:
        # P20 disclosed amendment (the biochemlogy law of record): when the marker is
        # followed by a content label ('2.3 - LIPIDS'), the label must agree with the
        # sub's own title — several channels renumber by playlist index, not by the
        # syllabus numbers; a disagreeing label demotes the number to noise.
        tail = title[m.end():].strip(" -:|–	")
        if tail and re.search(r"[A-Za-z]{3}", tail):
            frac, ninter = token_agreement(tail, subs[0]["title"])
            if frac < 0.3 or ninter < 1:
                subs = []
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
RE_0450 = re.compile(r"\b0450\b|\b7115\b|\b0264\b|Business\s+Studies", re.I)
RE_0460 = re.compile(r"\b0460\b|\b0976\b|IGCSE\s+Geography", re.I)
RE_4GE1 = re.compile(r"\b4GE1\b|International\s+GCSE\s+Geography|Edexcel\s+i?GCSE\s+Geography", re.I)
RE_WPH = re.compile(r"\bWPH\s?\d?\d?\b|IAL\s+[Pp]hysics|IAS\s+[Pp]hysics|IA2\s+[Pp]hysics", re.I)
RE_WBI = re.compile(r"\bWBI\s?\d?\d?\b|IAL\s+[Bb]iology|IAS\s+[Bb]iology|IA2\s+[Bb]iology", re.I)
RE_WCH = re.compile(r"\bWCH\s?\d?\d?\b|IAL\s+[Cc]hemistry|IAS\s+[Cc]hemistry|IA2\s+[Cc]hemistry", re.I)
RE_WIT = re.compile(r"\bWIT\d?\d?\b|IAL\s+Information\s+Technology|IAL\s+ICT\b", re.I)
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

# ---- P20 new register machinery (on top of the P15-P19 set) ----
# ================================================================ P20 new register machinery =====
RE_9618 = re.compile(r"\b9618\b|A\s?[-/&]?\s?(?:AS\s?&\s?A\s?)?[Ll]evel\s*[Cc]omputer\s+[Ss]cience|(?:AS|A2)\s?-?\s?[Ll]evel\s+[Cc]omputer\s+[Ss]cience", re.I)
RE_0478 = re.compile(r"\b0478\b|\b0984\b|i?GCSE\s+Computer\s+Science", re.I)
RE_9706 = re.compile(r"\b9706\b|A\s?[-/&]?\s?[Ll]evel\s*[Aa]ccounting|(?:AS|A2)\s?[Ll]evel\s*[Aa]ccounting|Cambridge\s+(?:AS|A2)\s+[Aa]ccounting", re.I)
RE_9709 = re.compile(r"\b9709\b|(?:AS\s?&\s?A|A\s?/\s?AS|AS\s?-?A2?)\s?[Ll]evel\s*[Mm]athematics?\b.{0,40}(Pure|Mechanics|Probability|Statistics)|[Mm]athematics?\s+(?:AS\s?&\s?A\s?[Ll]evel|A\s?[/&]\s?AS\s?[Ll]evel)", re.I)
RE_9231 = re.compile(r"\b9231\b|[Ff]urther\s+[Mm]aths?\b.{0,30}(9231|Cambridge|CIE)|Cambridge.{0,30}Further\s+[Mm]aths|Hypothes[ie]s\s+[Tt]est|Confidence\s+interval\s+for\s+the\s+population\s+mean", re.I)
RE_IBDP = re.compile(r"IBDP|\bIB\s+(?:Math|Computer|Physics|Chemistry|Biology|Economics|Business|Psychology)|Time\s+Zone|Analysis\s+and\s+Approaches|Applications\s+and\s+Interpretation", re.I)
RE_0264 = re.compile(r"\b0264\b", re.I)
RE_0653 = re.compile(r"\b0653\b", re.I)
RE_4WPHMOD = re.compile(r"\b4WPH([12])\b", re.I)
RE_4WBIMOD = re.compile(r"\b4WB([12])\b", re.I)
RE_UNIT0625 = re.compile(r"\bUNIT\s*([1-6])\b", re.I)
COMBINED = {"bio": "cie-igcse-science-combined-science-23-biology",
            "chem": "cie-igcse-science-combined-science-23-chemistry",
            "phys": "cie-igcse-science-combined-science-23-physics"}
PURE = {"P1": ["cie-a-level-maths-20-pure-1", "cie-as-maths-20-pure-1"],
        "P2": ["cie-a-level-maths-20-pure-2", "cie-as-maths-20-pure-2"],
        "P3": ["cie-a-level-maths-20-pure-3"]}
MECH = ["cie-a-level-maths-20-mechanics", "cie-as-maths-20-mechanics"]
PS1 = ["cie-a-level-maths-20-probability-and-statistics-1"]
PS2 = ["cie-a-level-maths-20-probability-and-statistics-2"]

def paper9709(t):
    """9709 component routing of record: P1/P2/P3 pure (AS twins P1/P2), P4/M1
    mechanics (AS twin), P5/S1 p&s-1, P6/S2 p&s-2 (a-level only — no AS p&s face).
    Returns the course list, or [] when no honest component evidence."""
    n = paper_num(t)
    comp = None
    if re.search(r"Pure\s+Mathematics\s*1|Pure\s*1\b|\bP1\b", t, re.I) and not re.search(r"Pure\s*(Mathematics\s*)?[23]|Pure\s*[23]\b|\bP[23]\b", t, re.I):
        comp = "P1"
    elif re.search(r"Pure\s+Mathematics\s*2|Pure\s*2\b|\bP2\b", t, re.I):
        comp = "P2"
    elif re.search(r"Pure\s+Mathematics\s*3|Pure\s*3\b|\bP3\b", t, re.I):
        comp = "P3"
    elif re.search(r"\bMechanics\b|\bM1\b", t, re.I):
        comp = "M1"
    elif re.search(r"Probability\s*&?\s*[Ss]tatistics\s*1|\bS1\b", t, re.I):
        comp = "S1"
    elif re.search(r"Probability\s*&?\s*[Ss]tatistics\s*2|\bS2\b", t, re.I):
        comp = "S2"
    if comp is None and n:
        comp = {1: "P1", 2: "P2", 3: "P3", 4: "M1", 5: "S1", 6: "S2"}.get(n)
    if comp is None:
        return []
    return {"P1": PURE["P1"], "P2": PURE["P2"], "P3": PURE["P3"], "M1": MECH, "S1": PS1, "S2": PS2}[comp]

def math9709_anchor(vid, prov, t, allow_bare=False):
    """The P20 9709 register of record (the P9 component law refined): explicit
    component/paper evidence routes Tier B session walkthroughs and Tier A content
    binds onto the component faces (the P11 shared-unit law: AS+A-level twins).
    Bare component-less content binds only for CAIE-branded pools (allow_bare,
    the ginger-context amendment, disclosed); everything else returns False so the
    caller skips honestly (the P17 mathman / P18 examcrack §6 precedent)."""
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        cl = paper9709(t)
        if cl:
            n = paper_num(t)
            tb(cl, vid, prov, t, f"9709 component/paper register anchor (paper {n}, the P20 component routing)")
            return True
    comp = paper9709(t)
    if comp and not (RE_SESSION.search(t) and RE_SOLVED.search(t)):
        for c in comp:
            if bind_course(c, vid, prov, t):
                return True
        if RE_9709.search(t):
            skip(CURRENT_PROV[0], vid, t, "9709 component title with no distinctive match in the component faces at the df<=3 bar")
            return True
        return False
    if allow_bare and RE_9709.search(t):
        for c in PURE["P1"] + PURE["P2"] + PURE["P3"] + MECH + PS1 + PS2:
            if bind_course(c, vid, prov, t):
                return True
        skip(CURRENT_PROV[0], vid, t, "9709-class title with no distinctive match in the maths faces at the df<=3 bar")
        return True
    return False

def acc9706_anchor(vid, prov, t):
    """The P20 9706 register: papers 1-2 AS / 3-4 A2 (the P13 accounting paper-level
    law) + explicit AS/A2 tokens; session walkthroughs -> Tier B, content -> the
    accounting faces' spec points (the AS face shares the A-level spine nodes)."""
    faces_a = ["cie-a-level-accounting-21"]
    faces_as = ["cie-as-accounting-21"]
    # the P20 9706 specimen/question class ('2023 Specimen Paper 4 Question 2 | 9706/04')
    # anchors on question-set/paper evidence too (the P20 amendment, disclosed)
    if RE_SESSION.search(t) or RE_SOLVED.search(t) or paper_num(t):
        n = paper_num(t)
        if re.search(r"\bAS\b", t) and not re.search(r"\bA2?\b|\bA\s?[Ll]evel\b", t):
            tb(faces_as, vid, prov, t, "9706 AS session/paper register anchor (AS named)")
        elif n in (1, 2):
            tb(faces_as, vid, prov, t, f"9706 paper {n} session/paper register anchor (papers 1-2 -> AS)")
        elif n in (3, 4):
            tb(faces_a, vid, prov, t, f"9706 paper {n} session/paper register anchor (papers 3-4 -> A2)")
        elif re.search(r"\bA2\b|\bA\s?[Ll]evel\b", t):
            tb(faces_a, vid, prov, t, "9706 A-level session/paper register anchor (A-level named)")
        else:
            tb(faces_as + faces_a, vid, prov, t, "9706 session/paper register anchor — AS/A2 not stated, both bound (disclosed)")
        return True
    a2 = bool(re.search(r"\bA2\b|A\s?[Ll]evel\b|Advanced\s+Level", t, re.I))
    as_ = bool(re.search(r"\bAS\b|Advanced\s+Subsidiary", t, re.I))
    faces = faces_a if a2 and not as_ else (faces_as if as_ and not a2 else faces_a + faces_as)
    for c in faces:
        if bind_course(c, vid, prov, t):
            return True
    return False

def cs9618_anchor(vid, prov, t):
    """9618: papers 1-2 AS / 3-4 A2 session/paper anchors + content binds onto
    cie-a-level-computer-science-19."""
    course = "cie-a-level-computer-science-19"
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t) or re.search(r"\bW\d{2}\b|\bS\d{2}\b|\bM\d{2}\b|\bpaper\b", t, re.I)):
        n = paper_num(t)
        if n in (1, 2) or re.search(r"\bAS\b", t):
            tb([course], vid, prov, t, "9618 AS session/paper register anchor (papers 1-2 -> AS)")
        elif n in (3, 4):
            tb([course], vid, prov, t, "9618 A2 session/paper register anchor (papers 3-4 -> A2)")
        else:
            tb([course], vid, prov, t, "9618 session/paper register anchor (single A-level CS course)")
        return True
    if bind_course(course, vid, prov, t):
        return True
    return False

def igcse0478_anchor(vid, prov, t):
    """0478/0984 IGCSE Computer Science -> cie-igcse-computer-science-23
    (session/paper Tier B + content binds)."""
    course = "cie-igcse-computer-science-23"
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb([course], vid, prov, t, "0478/0984 session/paper register anchor")
        return True
    if bind_course(course, vid, prov, t):
        return True
    return False

def combined0653_anchor(vid, prov, t):
    """0653 combined science: session/paper -> all three combined faces (the
    shared-paper law); content -> the subject-named combined face at the token
    bar (the P19 combined-numbering divergence law — no cross-family point binds)."""
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb(list(COMBINED.values()), vid, prov, t, "0653 combined-science session/paper anchor — shared-paper binding to all three sciences (disclosed)")
        return True
    subj = None
    if re.search(r"biolog", t, re.I): subj = "bio"
    elif re.search(r"chem", t, re.I): subj = "chem"
    elif re.search(r"physic", t, re.I): subj = "phys"
    if subj:
        if bind_course(COMBINED[subj], vid, prov, t):
            return True
        skip(CURRENT_PROV[0], vid, t, "0653 combined title with no distinctive match in the combined course at the df<=3 bar")
        return True
    for c in COMBINED.values():
        if bind_course(c, vid, prov, t):
            return True
    return False

def geo0460_anchor(vid, prov, t):
    """0460/IGCSE Geography: session/paper -> both geo faces (the 2020/2025
    shared-register pair); content -> geo-25 then geo-20 at the token bar."""
    pair = ["cie-igcse-geography-25", "cie-igcse-geography-20"]
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb(pair, vid, prov, t, "0460 session/paper register anchor — the 2020/2025 geo faces share the 0460 register (disclosed)")
        return True
    for c in pair:
        if bind_course(c, vid, prov, t):
            return True
    return False

def ial_unit_anchor20(vid, prov, t, subject=None):
    """P20 amendment of the P14 Assil law analog: the unit + question-set/specimen
    evidence class ('Unit 3 Sample - Question 4 (Edexcel IAS Chemistry)',
    'WCH15 October 2022 Paper 05 | Fully Solved') also anchors — RE_SOLVED and the
    spaced WCH/WBI/WPH NN paper form (unit via the 11-16/21-26 pair law, the P19
    spaced-WPH law generalized to the chemistry/biology faces, disclosed)."""
    un = re.search(r"unit\s*([1-6])", t, re.I)
    mw = re.search(r"\bW(CH|BI|PH)\s?(\d{2})\b", t, re.I)
    sess = RE_SESSION.search(t)
    solved = RE_SOLVED.search(t)
    paperish = re.search(r"past|paper|solved|walkthrough|specimen|question", t, re.I)
    course = None
    subj = subject
    if mw:
        subj = {"CH": "chem", "BI": "bio", "PH": "phys"}[mw.group(1).upper()]
        n = int(mw.group(2))
        if 11 <= n <= 26 and n % 10 in (1, 2, 3, 4, 5, 6):
            unit = (n // 10 - 1) * 3 + (n % 10 - 1) // 2 + 1
        else:
            unit = None
        if unit:
            course = {"bio": "ial-biology-18", "chem": "ial-chemistry-17", "phys": "ial-physics-19"}[subj]
            tb([course], vid, prov, t,
               f"IAL {subj} W{mw.group(1).upper()}{n} paper register anchor (unit {unit}, the spaced NN form of the P14 Assil law — the P20 chemistry/biology generalization)")
            return True
    if course is None:
        if subj is None:
            if re.search(r"biolog", t, re.I):
                subj = "bio"
            elif re.search(r"chem", t, re.I):
                subj = "chem"
            elif re.search(r"physic", t, re.I):
                subj = "phys"
        if subj is None:
            return False
        course = {"bio": "ial-biology-18", "chem": "ial-chemistry-17", "phys": "ial-physics-19"}[subj]
    if un and (sess or solved or paperish):
        tb([course], vid, prov, t,
           f"IAL {subj} Unit {un.group(1)} + session/paper/question evidence — unit-paper review anchor "
           f"(the P14 Assil law analog, the P20 question-set/specimen amendment)")
        return True
    return False

def bio9700_content(vid, prov, t):
    """The CIE 9700 numbered lesson register of record (otterbiotutor/biochemlogy/
    miss-estruch): leading 'N-M: {topic}' binds the A2/AS face subtopic points where
    the stem tokens agree (the P19 topic-number register, generalized to the A-level
    faces); 'CHAPTER N' / bare topic titles bind at the df<=3 token bar.
    Leading playlist indices (bare 'N - Title') are NOT topic numbers — no bind."""
    m = re.search(r"(?:^|s\s)(\d{1,2})[-\u2013](\d{1,2})(?=[\s:,]|$)", t)
    if m:
        a, b = m.group(1), m.group(2)
        face = "cie-a-level-biology-25" if (int(a) >= 12 or re.search(r"\bA2\b", t)) else "cie-as-biology-25"
        s = sub_by_num(face, a, b)
        if s:
            frac, ninter = token_agreement(t, s["title"])
            if frac >= 0.3 and ninter >= 1:
                pts = sub_points(face, s["code"])
                if pts:
                    route(face, vid, prov, [p["code"] for p in pts], "low",
                          f"9700 numbered-lesson register: title names section {a}.{b} '{s['title'][:60]}' (stem agreement "
                          f"{ninter} token(s)) — subtopic points bound at the disclosed title-only bar", None)
                    return True
    for face in (["cie-a-level-biology-25"] if re.search(r"\bA2\b", t) else ["cie-a-level-biology-25", "cie-as-biology-25"]):
        if bind_course(face, vid, prov, t):
            return True
    return False

def estruch_cie_topic(vid, prov, t):
    """'Topic N ENTIRE topic for CIE A-level' register: topic index + stem token
    agreement binds the topic points (the P19 study-buddy leading-number law)."""
    m = re.search(r"Topic\s+(\d{1,2})\b", t, re.I)
    if not m:
        return False
    n = int(m.group(1))
    face = "cie-a-level-biology-25" if n >= 12 else "cie-as-biology-25"
    tp = topic_at_index(face, n)
    if not tp:
        return False
    frac, ninter = token_agreement(t, tp["title"])
    if frac < 0.4 or ninter < 1:
        return False
    pts = topic_points(face, tp["title"])
    if not pts:
        return False
    route(face, vid, prov, [p["code"] for p in pts], "low",
          f"CIE topic-number register: title names Topic {n} '{tp['title'][:60]}' (stem agreement {ninter} token(s)) "
          f"— topic points bound at the disclosed title-only bar", None)
    return True

def unit0625_anchor(vid, prov, t, subj="phys"):
    """'UNIT N {topic}' register (pla/ilm 0625): trio topic at index N with stem
    token agreement + the co-ordinated P/B/C twin where the co-ord spine carries
    the same index (the shared-0625-structure law; combined NOT bound — the P19
    numbering-divergence law)."""
    m = RE_UNIT0625.search(t)
    if not m:
        return False
    n = int(m.group(1))
    trio = TRIO[subj]
    tp = topic_at_index(trio, n)
    landed = False
    if tp:
        frac, ninter = token_agreement(t, tp["title"])
        if frac >= 0.2 and ninter >= 1:
            pts = topic_points(trio, tp["title"])
            if pts:
                route(trio, vid, prov, [p["code"] for p in pts], "low",
                      f"0625 unit register: title names UNIT {n} '{tp['title'][:60]}' (stem agreement {ninter} token(s)) "
                      f"— topic points bound at the disclosed title-only bar", None)
                landed = True
    co = topic_at_index(COORD[subj], n)
    if co:
        frac, ninter = token_agreement(t, co["title"])
        if frac >= 0.2 and ninter >= 1:
            pts = topic_points(COORD[subj], co["title"])
            if pts:
                route(COORD[subj], vid, prov, [p["code"] for p in pts], "low",
                      f"0625 unit register (shared-structure twin bind): UNIT {n} and the co-ordinated spine carries "
                      f"'{co['title'][:50]}' at the same index (disclosed)", True)
                landed = True
    return landed

def modsci_route(t):
    """Edexcel modular science routing (4WCH1/2, 4WPH1/2, 4WB1/2, 4XB/4XP +
    'Modular ... Unit N'): the modular-24 unit faces. The explicit 'Unit N'
    token outranks the qualification-code digit (the P20 pla title law:
    'Unit 2: ... (Modular) 4WPH1' routes unit 2, disclosed)."""
    out = []
    um = re.search(r"unit\s*([12])", t, re.I)
    if um:
        if re.search(r"chem", t, re.I):
            out.append(f"igcse-chemistry-modular-24-unit-{um.group(1)}")
        elif re.search(r"biolog", t, re.I):
            out.append(f"igcse-biology-modular-24-unit-{um.group(1)}")
        elif re.search(r"physic", t, re.I):
            out.append(f"igcse-physics-modular-24-unit-{um.group(1)}")
        if out:
            return out
    for rx, base in ((RE_4WCHMOD, "igcse-chemistry-modular-24-unit-"),
                     (RE_4WBIMOD, "igcse-biology-modular-24-unit-"),
                     (RE_4WPHMOD, "igcse-physics-modular-24-unit-"),
                     (RE_4XB, "igcse-biology-modular-24-unit-"),
                     (RE_4XP, "igcse-physics-modular-24-unit-")):
        mm = rx.search(t)
        if mm:
            g = mm.group(1)
            if g in ("1", "2"):
                out.append(f"{base}{g}")
                return out
    return out

def subtopic_bind(course, vid, prov, t):
    """P20 subtopic-scoped lecture gate (the four-gate topic-lecture class at
    SUBTOPIC granularity): a title token that is UNIQUE across the spine's
    topic/subtopic titles (TDF df<=1) and lands INSIDE a subtopic's own title
    binds that subtopic's points at low confidence (the title-token class,
    subtopic-scoped — disclosed)."""
    vt = set(toks14(t))
    best = None
    for n in specs_spine[course]["nodes"]:
        if n["family"] != "SUBTOPIC":
            continue
        st = set(toks14(n.get("title") or ""))
        hits = vt & st
        uniq = [w for w in hits if TDF[course].get(w, 99) <= 1]
        if uniq:
            if best is None or len(uniq) > len(best[1]):
                best = (n, uniq)
    if not best:
        return False
    n, uniq = best
    pts = sub_points(course, n["code"])
    if not pts:
        return False
    route(course, vid, prov, [p["code"] for p in pts], "low",
          f"subtopic-scoped lecture bind: title names {n['title'][:60]} via topic-unique token(s) {uniq[:5]} "
          f"— subtopic points bound at the disclosed title-only bar", None)
    return True

def series_section_bind(course, clean_title):
    """P20 numbered-lesson-series law (the tatchen chapter-index precedent,
    generalized): after stripping the series' lesson-code prefix and the
    Triple/Single/Double tag, a verbatim field match against a TOPIC/SUBTOPIC
    binds the section's points by ORDER-BASED containment (the points between
    this node and the next TOPIC/SUBTOPIC — the code-scheme-independent
    containment law, disclosed). Returns (node, [codes]) or None."""
    fields = [norm_stop(re.sub(r"\([^)]*\)", " ", f)) for f in split_fields(clean_title)]
    nodes = specs_spine[course]["nodes"]
    for i, n in enumerate(nodes):
        if n["family"] not in ("TOPIC", "SUBTOPIC"):
            continue
        nt = norm_stop(n.get("title") or "")
        if len(nt.strip()) >= 8 and any(nt == f for f in fields):
            pts = []
            for m2 in nodes[i + 1:]:
                if m2["family"] in ("TOPIC", "SUBTOPIC"):
                    break
                if m2["family"] == "SPEC_POINT":
                    pts.append(m2["code"])
            if pts:
                return (n, pts)
    return None
# ---- P19 register machinery retained verbatim ----
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
    m = re.search(r"[_\- ]qp[_\- ]?(\d{1,2})\b", title, re.I)
    if m:
        cands.append(int(m.group(1)))
    m = re.search(r"\b0?(610|620|625|653|654|417|452|455|460|500|606|607|680|8291|460)/(\d{1,2})\d?/", title)
    if m:
        cands.append(int(m.group(2)))
    m = re.search(r"\b(?:9700|9701|9702|9706|9708|9709|9609|0580|4024)[/ ]?(\d{1,2})\b", title)
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

def route(course, vid, prov, specs_list, confidence, reason, p20b=False, cross=False):
    judgment[course].append({"id": vid, "provider": prov, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p20b": p20b if p20b else course in P20B, "crossReg": cross})

def tb(course_list, vid, prov, title, code, cross=False):
    for course in course_list:
        tier_b.append({"id": vid, "title": title, "provider": prov, "courses": [course],
                       "code": code, "kind": "past-paper-walkthrough",
                       "p20b": course in P20B, "crossReg": cross})

def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|Q\s?\d|paper\s*\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

def _marker_live(course, t):
    """P20 helper: does the title's N.M(/dash) marker name a spine sub whose own
    title agrees with the marker's content label? False = channel-own index or
    disagreeing label (the biochemlogy law of record)."""
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\s", t + " ")
    m2 = None if m else re.search(r"(?<!\d)(\d{1,2})[-\u2013](\d{1,2})(?![\d.])", t)
    if not m and not m2:
        return False
    mm = m or m2
    sub = sub_by_num(course, mm.group(1), mm.group(2))
    if not sub:
        return False
    tail = t[mm.end():].strip(" -:|\u2013\t")
    if tail and re.search(r"[A-Za-z]{3}", tail):
        frac, ninter = token_agreement(tail, sub["title"])
        if frac < 0.3 or ninter < 1:
            return False
    return True

def bind_course(course, vid, prov, t, p20b=None):
    if p20b is None:
        p20b = course in P20B
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p20b)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        # P20 amendment (the biochemlogy re-adjudication law of record): a TOPIC-level
        # verbatim bind is dishonest for a SUBTOPIC-scoped lecture — when the title also
        # carries an N.M(/dash) marker that is absent from the spine OR whose label
        # disagrees with the matching sub's own title, the number is the channel's own
        # index and the lecture is subtopic-scoped; fall through to the token evidence
        # instead of binding the whole topic.
        _mp = re.search(r"\b\d{1,2}\.\d{1,2}\b", t) or re.search(r"(?<!\d)\d{1,2}[-\u2013]\d{1,2}(?![\d.])", t)
        if node["family"] == "TOPIC" and _mp and not _marker_live(course, t):
            sg = None
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p20b)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs_spine[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p20b)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p20b)
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
        if RE_IAL_MATHS.search(t) and slug not in IALMATHS_EXEMPT:
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

# ================================================================ P20 pool laws =====

def law_otterbiotutor(vid, t):
    prov = "otterbiotutor"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if cie_alevel_sci_anchor(vid, prov, t):
        return
    if bio9700_content(vid, prov, t):
        return
    skip(prov, vid, t, "9700 title with no honest binding at the df<=3 bar over the a-level/AS biology faces (the 9700 lesson series)")

def law_ptet(vid, t):
    prov = "ptet-chemistry"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9701.search(t):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        for c in ("cie-a-level-chemistry-25", "cie-as-chemistry-25"):
            if bind_course(c, vid, prov, t):
                return
    if RE_COMBINED.search(t) or RE_0653.search(t):
        if combined0653_anchor(vid, prov, t):
            return
    if RE_0620.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or paper_num(t)):
        tb(["cie-igcse-chemistry-23"], vid, prov, t, "0620 session/paper register anchor")
        return
    if RE_0620.search(t):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "0620 title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    if RE_4CH1.search(t) or re.search(r"Edexcel\s+i?GCSE\s+Chemistry|IGCSE\s+Chemistry.{0,30}Edexcel", t, re.I):
        if bind_course("igcse-chemistry-19", vid, prov, t):
            return
        skip(prov, vid, t, "Edexcel IGCSE chemistry title with no distinctive match in igcse-chemistry-19 at the df<=3 bar")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board titles (AQA/OCR/IB/...) — out-of-spine board")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 9701/0620/0653/Ed-IGCSE chemistry; the 5070 O-Level chemistry register has no spine course)")

def law_studywithprashna(vid, t):
    prov = "study-with-prashna"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9706.search(t):
        if acc9706_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9706 title with no distinctive match in the accounting faces at the df<=3 bar")
        return
    if RE_9709.search(t):
        if math9709_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9709 session title without an honest component route (the ANCHOR-GRANULARITY §6 bare-walkthrough law)")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 9706 accounting session-solution class)")

def law_adamviceroy(vid, t):
    prov = "adam-viceroy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9706.search(t):
        if acc9706_anchor(vid, prov, t):
            return
    if RE_0452.search(t) or RE_0264.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-accounting-25", "cie-igcse-accounting-21"], vid, prov, t, "0452/0985 session/paper register anchor (the disclosed 7707 dual exempt per the P14 precedence law)")
            return
        for c in ("cie-igcse-accounting-25", "cie-igcse-accounting-21"):
            if bind_course(c, vid, prov, t):
                return
            if subtopic_bind(c, vid, prov, t):
                return
    for c in ("cie-igcse-accounting-25", "cie-igcse-accounting-21", "cie-a-level-accounting-21", "cie-as-accounting-21"):
        if bind_course(c, vid, prov, t):
            return
        if subtopic_bind(c, vid, prov, t):
            return
    skip(prov, vid, t, "accounting title with no distinctive match in the accounting faces at the df<=3 bar (the promo/motivation remainder is not a qualification register)")

def law_missnatalie(vid, t):
    prov = "miss-natalie-chemistry"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_WCH.search(t) or re.search(r"Edexcel\s+(IAS|IAL)\s+Chemistry", t, re.I):
        if ial_unit_anchor20(vid, prov, t, subject="chem"):
            return
        if bind_course("ial-chemistry-17", vid, prov, t):
            return
        skip(prov, vid, t, "WCH title with no distinctive match in ial-chemistry-17 at the df<=3 bar")
        return
    ed_chem = RE_4CH1.search(t) or re.search(r"Edexcel\s+i?GCSE\s+Chemistry", t, re.I) or re.match(r"^\s*\d{1,2}[A-Z]?\s{1,3}", t)
    if ed_chem:
        # the P20 numbered-lesson-series law (the tatchen chapter-index precedent):
        # the series' leading lesson code ('1I') and the Triple/Single/Double tag are
        # stripped before the concept label re-binds — the concept label self-verifies
        clean = re.sub(r"^\s*\d{1,2}[A-Z]?\s+", "", t)
        clean = re.sub(r"\s*\((?:Triple|Single|Double|Single\s*/\s*Double)\)\s*", " ", clean, flags=re.I)
        if bind_course("igcse-chemistry-19", vid, prov, t):
            if re.search(r"Single\s*/\s*Double|Double\s+[Aa]ward|4SD0", t, re.I):
                bind_course("igcse-science-double-award-17-chemistry", vid, prov, t)
            return
        if clean != t:
            sb = series_section_bind("igcse-chemistry-19", clean)
            if sb:
                node, pts = sb
                route("igcse-chemistry-19", vid, prov, pts, "low",
                      f"Ed-IGCSE numbered-lesson series (the tatchen chapter-index precedent): the series' concept label "
                      f"'{node['title'][:60]}' matches verbatim after the lesson-code/tag strip — section points bound by "
                      f"order-based containment (the P20 series law, disclosed)", None)
                if re.search(r"Single\s*/\s*Double|Double\s+[Aa]ward|4SD0", t, re.I):
                    bind_course("igcse-science-double-award-17-chemistry", vid, prov, clean)
                return
            if bind_course("igcse-chemistry-19", vid, prov, clean):
                if re.search(r"Single\s*/\s*Double|Double\s+[Aa]ward|4SD0", t, re.I):
                    bind_course("igcse-science-double-award-17-chemistry", vid, prov, clean)
                return
        skip(prov, vid, t, "Ed-IGCSE chemistry series title with no distinctive match in igcse-chemistry-19 at the df<=3 bar")
        return
    if RE_0620.search(t):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "0620 title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are WCH unit content, the Ed-IGCSE chemistry series and 0620)")

def law_mathlete(vid, t):
    prov = "mathlete-by-saad"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the expected-topics/prediction register)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board register (SAT/entry-test/mislabelled matric content)")
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the disclosed 4037 dual exempt)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in cie-igcse-further-maths-additional-maths-25 at the df<=3 bar")
        return
    if RE_9709.search(t):
        if math9709_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9709 title without an honest component route (the §6 bare-walkthrough law)")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if re.search(r"i?GCSE\s*/?\s*O\s?-?\s?[Ll]evel\s*Maths?\b|O\s?[Ll]evel\s*[-/]?\s*IGCSE\s*Maths?\b|IGCSE\s*Maths?\b", t, re.I) and not RE_NT_BOARD.search(t):
        maths058_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 0606/9709/0580; bare advice and entry-test content is not a qualification register)")

def law_cswithmrg(vid, t):
    prov = "cswithmrg"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the teaching-tools/trailer remainder)")
        return
    if RE_9618.search(t):
        if cs9618_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9618 title with no distinctive match in cie-a-level-computer-science-19 at the df<=3 bar")
        return
    if RE_0478.search(t):
        if igcse0478_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "0478/0984 title with no distinctive match in cie-igcse-computer-science-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the dual 9618/0478 CIE CS class; bare coding/teaching-tools content is not a qualification register)")

def law_haguin(vid, t):
    prov = "haguin-school"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice register (the exam-structure/advice shorts of the 9618 channel)")
        return
    if RE_9618.search(t):
        if cs9618_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9618 title with no distinctive match in cie-a-level-computer-science-19 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 9618 paper-walkthrough class)")

def law_mrlee(vid, t):
    prov = "mr-lee-business-econ"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the NT x26 IB/Edexcel remainders ride the same class)")
        return
    if re.search(r"Edexcel\s+i?GCSE\s+Economics", t, re.I) or RE_NT_BOARD.search(t):
        skip(prov, vid, t, "Edexcel/IB economics register — no spine course (the P11 Edexcel-econ terminal law)")
        return
    if RE_0455.search(t) or re.search(r"IGCSE\s+Econom", t, re.I):
        if bind_course("cie-igcse-economics-20", vid, prov, t):
            return
        skip(prov, vid, t, "0455 economics title with no distinctive match in cie-igcse-economics-20 at the df<=3 bar")
        return
    if re.search(r"IGCSE\s+Business", t, re.I) or RE_0450.search(t) or RE_0264.search(t):
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
        skip(prov, vid, t, "business title with no distinctive match in cie-igcse-business-25 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 0455 chapter class)")

def law_mrmathew(vid, t):
    prov = "mr-mathew"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board titles (AQA plant/other) — out-of-spine board")
        return
    if RE_0680.search(t):
        em_anchor(vid, prov, t)
        return
    if RE_0460.search(t) or re.search(r"IGCSE[\s_]+Geography|IGCSE\s+GEOGRAPHY", t, re.I):
        if geo0460_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "0460 geography title with no distinctive match in the geo faces at the df<=3 bar")
        return
    if RE_0610.search(t) or re.search(r"IGCSE\s*(?:&\s*WAEC\s*)?Biology", t, re.I):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-biology-23"], vid, prov, t, "0610 session/paper register anchor")
            return
        if bind_course("cie-igcse-biology-23", vid, prov, t):
            return
        skip(prov, vid, t, "0610 biology title with no distinctive match in cie-igcse-biology-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 0680/0460/0610; the 5090 O-Level EM dual and WAEC-only titles have no honest IGCSE bind)")

def law_pla(vid, t):
    prov = "pla-academy-igcse-and-a-level-buddy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"IAL\s+.{0,24}Physics|Edexcel\s+IAL\s+Physics|IA2\s+Physics|\bWPH\s?\d?\d?\b", t, re.I):
        if ial_unit_anchor20(vid, prov, t, subject="phys"):
            return
        if bind_course("ial-physics-19", vid, prov, t):
            return
        skip(prov, vid, t, "IAL physics unit-content title with no distinctive match in ial-physics-19 at the df<=3 bar")
        return
    mod = modsci_route(t)
    if mod and (RE_4WPHMOD.search(t) or RE_4XP.search(t) or re.search(r"physic", t, re.I)):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(mod, vid, prov, t, "Edexcel modular physics paper register anchor (the P17 4WCH-modular law analog)")
            return
        if bind_course(mod[0], vid, prov, t):
            return
    if RE_4PH1.search(t) or re.search(r"Edexcel\s+i?GCSE\s+Physics", t, re.I):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["igcse-physics-19", "igcse-science-double-award-17-physics"], vid, prov, t, "4PH1 session/paper register anchor (the 4SD0 shared-paper law)")
            return
        if bind_course("igcse-physics-19", vid, prov, t):
            if re.search(r"Double\s+[Aa]ward|4SD0", t, re.I):
                bind_course("igcse-science-double-award-17-physics", vid, prov, t)
            return
        skip(prov, vid, t, "Ed-IGCSE physics title with no distinctive match in igcse-physics-19 at the df<=3 bar")
        return
    if RE_0625.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-physics-23"], vid, prov, t, "0625 session/paper register anchor")
            return
        if unit0625_anchor(vid, prov, t, "phys"):
            return
        if bind_course("cie-igcse-physics-23", vid, prov, t):
            return
        skip(prov, vid, t, "0625 physics title with no distinctive match in cie-igcse-physics-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are the WPH/Ed-IGCSE-physics/0625 classes; the 5054 O-Level physics and AQA maths remainders are not International registers)")

def law_refactorlab(vid, t):
    prov = "refactor-lab"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0606.search(t) or re.search(r"#additionalmathematics|Add[- ]?Math|Am[- ]?FM", t, re.I):
        if RE_SESSION.search(t) or re.search(r"\bP1[123]\b|\bP2[123]\b|\bQ[ .]?-?\d", t, re.I) or re.search(r"\bM?J\b|\bO?N\b|20\d\d", t, re.I):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the disclosed 4037/4024 duals exempt)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in cie-igcse-further-maths-additional-maths-25 at the df<=3 bar")
        return
    if RE_9709.search(t):
        if math9709_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9709 title without an honest component route (the §6 bare-walkthrough law)")
        return
    if RE_0580.search(t) or RE_0264.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_0625.search(t):
        if bind_course("cie-igcse-physics-23", vid, prov, t):
            return
        skip(prov, vid, t, "0625 title with no distinctive match in cie-igcse-physics-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 0606/9709/0580/0625)")

def law_mathprep(vid, t):
    prov = "mathprep-with-ahmad-bilal"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board register (A-level bare / AP / IB remainders)")
        return
    if RE_9709.search(t) or re.search(r"\bP[123]\b.{0,40}(Past Paper|Questions|Revision|Concepts)|Pure\s*(Mathematics\s*)?[123]\b", t, re.I):
        if math9709_anchor(vid, prov, t, allow_bare=True):
            return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the disclosed 4037 dual exempt)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in cie-igcse-further-maths-additional-maths-25 at the df<=3 bar")
        return
    if RE_0580.search(t) or re.search(r"O\s?-?\s?[Ll]evel\s+4024", t, re.I):
        maths058_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the CAIE 9709/0606/0580 session-solution class)")

def law_salihath(vid, t):
    prov = "salihath-syed-basheer"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t) or RE_IBDP.search(t):
        skip(prov, vid, t, "NT-board register (#cbse/matric/project content)")
        return
    if RE_9609.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            if re.search(r"\bAS\b", t):
                tb(["cie-as-business-23"], vid, prov, t, "9609 AS session/paper register anchor")
            else:
                tb(["cie-a-level-business-23"], vid, prov, t, "9609 A-level session/paper register anchor (pool-scoped)")
            return
        for c in ("cie-as-business-23", "cie-a-level-business-23"):
            if bind_course(c, vid, prov, t):
                return
    if RE_0450.search(t) or RE_0264.search(t) or re.search(r"IGCSE\s+Business", t, re.I):
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
        skip(prov, vid, t, "0450/0264 business title with no distinctive match in cie-igcse-business-25 at the df<=3 bar")
        return
    if re.search(r"#igcse\s+economics|IGCSE\s+[Ee]conom", t, re.I):
        if bind_course("cie-igcse-economics-20", vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding (the pool's registers are 9609/0450; the bare motivational/date-title remainder is not a qualification register)")

def law_edexworld(vid, t):
    prov = "edex-world"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice register (the study-tips remainder)")
        return
    if RE_9706.search(t):
        if acc9706_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9706 title with no distinctive match in the accounting faces at the df<=3 bar")
        return
    if re.search(r"(AS|A2?)\s?/?\s?[Ll]evel\s+Accounting", t, re.I):
        if bind_course("cie-a-level-accounting-21", vid, prov, t):
            return
        if subtopic_bind("cie-a-level-accounting-21", vid, prov, t):
            return
    if RE_0455.search(t) or re.search(r"IGCSE\s+Econom", t, re.I):
        if bind_course("cie-igcse-economics-20", vid, prov, t):
            return
        skip(prov, vid, t, "0455 economics title with no distinctive match in cie-igcse-economics-20 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the 'Accounting for IGCSE' remainder carries no 0452 code — the ammar-samana law, disclosed)")

def law_biochemlogy(vid, t):
    prov = "biochemlogy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9700.search(t):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        if re.search(r"\bA2\b", t, re.I):
            if bind_course("cie-a-level-biology-25", vid, prov, t):
                return
        if bio9700_content(vid, prov, t):
            return
        skip(prov, vid, t, "9700 title with no distinctive match in the biology faces at the df<=3 bar")
        return
    if RE_9701.search(t):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        for c in ("cie-as-chemistry-25", "cie-a-level-chemistry-25"):
            if bind_course(c, vid, prov, t):
                return
    if RE_4CH1.search(t) or re.search(r"EDEXCEL\s+CHEM", t, re.I):
        if bind_course("igcse-chemistry-19", vid, prov, t):
            return
        skip(prov, vid, t, "4CH1 title with no distinctive match in igcse-chemistry-19 at the df<=3 bar")
        return
    if RE_0620.search(t):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "0620 title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    if re.search(r"Slide\s+\d+/\d+|ENZYMES|enzymes", t):
        if bind_course("cie-a-level-biology-25", vid, prov, t):
            return
        skip(prov, vid, t, "the slide-series biology content with no distinctive match in cie-a-level-biology-25 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 9700/9701/4CH1/0620)")

def law_umara(vid, t):
    prov = "umara-ratnayake"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_WIT.search(t) or re.search(r"IAL\s+ICT", t, re.I):
        skip(prov, vid, t, "IAL ICT register (WIT) — no spine course (the P11 Edexcel-IAL terminal law)")
        return
    if RE_4IT0.search(t) or re.search(r"IGCSE\s+ICT", t, re.I):
        if (RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t))) or re.search(r"paper\s+discussion|practical\s+paper|past\s+paper", t, re.I):
            tb(["igcse-ict-17"], vid, prov, t, "4IT1 Edexcel IGCSE ICT session/paper register anchor (the paper-discussion class, disclosed)")
            return
        if bind_course("igcse-ict-17", vid, prov, t):
            return
        skip(prov, vid, t, "4IT1/IGCSE ICT title with no distinctive match in igcse-ict-17 at the df<=3 bar")
        return
    if RE_0417.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-ict-21"], vid, prov, t, "0417 session/paper register anchor")
            return
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
    if RE_9618.search(t):
        if cs9618_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9618 title with no distinctive match in cie-a-level-computer-science-19 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (bare coding/python content and the Edexcel IGCSE CS register — the latter has no spine course)")

def law_aslaug(vid, t):
    prov = "aslaug-eggertsdottir"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4IT0.search(t) or re.search(r"Edexcel\s+i?GCSE\s+ICT", t, re.I):
        if (RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t))) or re.search(r"paper\s+discussion|practical\s+(paper|exam)|past\s+paper", t, re.I):
            tb(["igcse-ict-17"], vid, prov, t, "4IT1 practical-exam register anchor (the practical/paper-discussion class, disclosed)")
            return
        if bind_course("igcse-ict-17", vid, prov, t):
            return
        skip(prov, vid, t, "4IT1 title with no distinctive match in igcse-ict-17 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the non-ICT remainder incl. the Icelandic-language titles carries no qualification register)")

def law_sq(vid, t):
    prov = "s-q"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if re.search(r"i?GCSE\s+ICT", t, re.I):
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
        skip(prov, vid, t, "iGCSE ICT task title with no distinctive match in cie-igcse-ict-21 at the df<=3 bar (the bare 'iGCSE ICT' series read as the 0417 register per the gate's classification, disclosed)")
        return
    if RE_0417.search(t):
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
    if RE_4IT0.search(t):
        if bind_course("igcse-ict-17", vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding (bare python/office-skills content is not a qualification register)")

def law_lightup(vid, t):
    prov = "the-lightup-hub"
    lit_law(vid, t, prov)

def law_egeo(vid, t):
    prov = "e-geo"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0460.search(t) or re.search(r"IGCSE[\s_]+GEOGRAPHY|IGCSE\s+Geography", t, re.I):
        if geo0460_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "0460 geography title with no distinctive match in the geo faces at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (generic geography/current-affairs titles without the IGCSE 0460 register)")

def law_ilm(vid, t):
    prov = "ilm-online-academy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the hashtag-promo remainder)")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_0620.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-chemistry-23"], vid, prov, t, "0620 session/paper register anchor")
            return
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "0620 title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    if RE_0625.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-physics-23"], vid, prov, t, "0625 session/paper register anchor")
            return
        if unit0625_anchor(vid, prov, t, "phys"):
            return
        if bind_course("cie-igcse-physics-23", vid, prov, t):
            return
        skip(prov, vid, t, "0625 title with no distinctive match in cie-igcse-physics-23 at the df<=3 bar")
        return
    if RE_0610.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-biology-23"], vid, prov, t, "0610 session/paper register anchor")
            return
        if bind_course("cie-igcse-biology-23", vid, prov, t):
            return
        skip(prov, vid, t, "0610 title with no distinctive match in cie-igcse-biology-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's registers are 0580/0620/0625/0610)")

def law_ymxc(vid, t):
    prov = "y-mx-c"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0606.search(t) or re.search(r"relative\s+velocity|velocity\s+vectors|ADDMATHS|Add[- ]?Maths?\b", t, re.I):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the relative-velocity vectors series)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in cie-igcse-further-maths-additional-maths-25 at the df<=3 bar")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (bare maths/KBAT content without the pool's 0606/0580 register — the 86-absolute thin-ratio disclosure)")

def law_missestruch(vid, t):
    prov = "miss-estruch-biology"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board titles (AQA A-level biology dominant) — out-of-spine board")
        return
    if re.search(r"\bCIE\b|Cambridge|9700", t, re.I):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        if estruch_cie_topic(vid, prov, t):
            return
        if bind_course("cie-a-level-biology-25", vid, prov, t):
            return
        if bind_course("cie-as-biology-25", vid, prov, t):
            return
        skip(prov, vid, t, "CIE-tokened title with no distinctive match in the biology faces at the df<=3 bar")
        return
    skip(prov, vid, t, "bare 'A-Level Biology' register with no CIE token — board-agnostic (the P19 academic-plus law; the AQA-dominant channel's bare-AL subset)")

def law_wimzee(vid, t):
    prov = "wimzee-cambridge-academy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board titles (OCR A-level chemistry) — out-of-spine board")
        return
    if re.search(r"AS\s?[Ll]evel\s+[Cc]hemistry", t, re.I):
        if bind_course("cie-as-chemistry-25", vid, prov, t):
            return
        skip(prov, vid, t, "AS chemistry title with no distinctive match in cie-as-chemistry-25 at the df<=3 bar")
        return
    if re.search(r"IGCSE\s+[Cc]hemistry", t, re.I) or RE_0620.search(t):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE chemistry title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    if re.search(r"IGCSE\s+[Bb]iology", t, re.I) or RE_0610.search(t):
        if bind_course("cie-igcse-biology-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE biology title with no distinctive match in cie-igcse-biology-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the bare 'IGCSE chemistry/biology' subject-name series binds at the CIE subject-name posture only where tokens are distinctive)")

def law_mysecondteacher(vid, t):
    prov = "mysecondteacher"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the school onboarding/training remainder)")
        return
    if re.search(r"A\s?[Ll]evel\s+Economics|AS\s?&\s?A\s?[Ll]evel\s+Economics", t, re.I):
        if bind_course("cie-a-level-economics-23", vid, prov, t):
            return
        skip(prov, vid, t, "A-level economics title with no distinctive match in cie-a-level-economics-23 at the df<=3 bar")
        return
    if re.search(r"A\s?[Ll]evel\s+Accounting", t, re.I):
        if bind_course("cie-a-level-accounting-21", vid, prov, t):
            return
        skip(prov, vid, t, "A-level accounting title with no distinctive match in cie-a-level-accounting-21 at the df<=3 bar")
        return
    if re.search(r"(A\s?[Ll]evel|AS\s?&\s?A\s?[Ll]evel)\s+Math", t, re.I):
        if math9709_anchor(vid, prov, t, allow_bare=True):
            return
        skip(prov, vid, t, "A-level maths title with no distinctive match in the maths faces at the df<=3 bar")
        return
    if re.search(r"Cambridge\s+IGCSE\s+Biology|IGCSE\s+Biology", t, re.I):
        if bind_course("cie-igcse-biology-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE biology title with no distinctive match in cie-igcse-biology-23 at the df<=3 bar")
        return
    if re.search(r"Cambridge\s+IGCSE\s+Chemistry|IGCSE\s+Chemistry", t, re.I):
        if bind_course("cie-igcse-chemistry-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE chemistry title with no distinctive match in cie-igcse-chemistry-23 at the df<=3 bar")
        return
    if re.search(r"Cambridge\s+IGCSE\s+Physics|IGCSE\s+Physics", t, re.I):
        if bind_course("cie-igcse-physics-23", vid, prov, t):
            return
        skip(prov, vid, t, "IGCSE physics title with no distinctive match in cie-igcse-physics-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the numbered Cambridge lesson series binds where the section/topic tokens are distinctive)")

def law_tfp(vid, t):
    prov = "the-future-professionals"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate; the motivation/highlights remainder)")
        return
    if RE_NT_BOARD.search(t) or re.search(r"Matric\b|Pakistan\s+Studies|2059\b", t, re.I):
        skip(prov, vid, t, "NT/matric register (O-Level Pakistan Studies and the mislabelled 0610-chemistry class)")
        return
    if RE_9706.search(t):
        if acc9706_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9706 title with no distinctive match in the accounting faces at the df<=3 bar")
        return
    if RE_9609.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-a-level-business-23", "cie-as-business-23"], vid, prov, t, "9609 session/paper register anchor (pool-scoped)")
            return
        for c in ("cie-as-business-23", "cie-a-level-business-23"):
            if bind_course(c, vid, prov, t):
                return
    if RE_0450.search(t) or re.search(r"IGCSE\s+Business", t, re.I):
        if bind_course("cie-igcse-business-25", vid, prov, t):
            return
    if RE_0610.search(t):
        if bind_course("cie-igcse-biology-23", vid, prov, t):
            return
    if re.search(r"W1?\d\s*/\s*P\d{2}\s*/\s*Q\d|P\d{2}\s*/\s*Q\d|\bQ\d+\b.{0,30}(Mensuration|Similarity)|Mensuration|Similarity", t, re.I):
        maths058_anchor(vid, prov, t)
        return
    if re.search(r"Depreciation|Disposal|Part\s+Exchange|Financial\s+Statement|Trade\s+receivable", t, re.I):
        if bind_course("cie-igcse-accounting-25", vid, prov, t):
            return
        skip(prov, vid, t, "accounting lecture with no distinctive match in cie-igcse-accounting-25 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (thin-multi pool; the bare O-Level/5070-mislabelled remainder is not an honest IGCSE register)")

def law_chembase(vid, t):
    prov = "chembase-school-of-chemistry"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_WCH.search(t):
        if ial_unit_anchor20(vid, prov, t, subject="chem"):
            return
        if bind_course("ial-chemistry-17", vid, prov, t):
            return
        skip(prov, vid, t, "WCH title with no distinctive match in ial-chemistry-17 at the df<=3 bar")
        return
    if RE_9701.search(t):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        for c in ("cie-a-level-chemistry-25", "cie-as-chemistry-25"):
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "9701 title with no distinctive match in the chemistry faces at the df<=3 bar")
        return
    as_ = bool(re.search(r"AS\s+[Ll]evel\s+Chemistry|Advanced\s+Subsidiary", t, re.I))
    al = bool(re.search(r"Advanced\s+Level|\bAL\s+Chemistry|A\s?[Ll]evel\s+Chemistry", t, re.I))
    if as_ or al:
        faces = ["cie-as-chemistry-25"] if (as_ and not al) else (["cie-a-level-chemistry-25"] if al and not as_ else ["cie-a-level-chemistry-25", "cie-as-chemistry-25"])
        for c in faces:
            if bind_course(c, vid, prov, t):
                return
        skip(prov, vid, t, "Cambridge A/AS chemistry title with no distinctive match in the chemistry faces at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the Cambridge A/AS chemistry subject-name class)")

def law_sayo(vid, t):
    prov = "sayo-enoch-aluko"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t) or RE_IBDP.search(t):
        skip(prov, vid, t, "NT/IB register (GCSE/AP/IB-HL mixed-board dominant) — the revwise mixed-NT precedent")
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the disclosed 4037 dual exempt)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match in cie-igcse-further-maths-additional-maths-25 at the df<=3 bar")
        return
    if RE_0417.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-ict-21"], vid, prov, t, "0417 session/paper register anchor")
            return
        if bind_course("cie-igcse-ict-21", vid, prov, t):
            return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (bare python/robotics/account-automation content is not a qualification register)")

def law_hendrik(vid, t):
    prov = "hendrik-academy"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IBDP.search(t) or re.search(r"TZ\d|Higher\s+Level|Standard\s+Level", t, re.I):
        skip(prov, vid, t, "IBDP register (Analysis & Approaches / Applications & Interpretation) — no spine course")
        return
    if RE_9709.search(t):
        if math9709_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9709 title without an honest component route (the §6 bare-walkthrough law; the IBDP-dominant channel's bare-maths remainder rides the same class)")
        return
    if RE_9702.search(t):
        if cie_alevel_sci_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9702 title with no honest AS/A2 route")
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
    if RE_0625.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-physics-23"], vid, prov, t, "0625 session/paper register anchor")
            return
    skip(prov, vid, t, "no honest binding (bare maths/physics content of the IBDP-dominant channel is not an honest CAIE register)")

def law_walter(vid, t):
    prov = "walter-maths-tutoring"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9231.search(t):
        skip(prov, vid, t, "9231 further-maths register — no spine course (the P18 4PM0-analog terminal call)")
        return
    if RE_9709.search(t) or re.search(r"CAIE\s+A/AS\s+Level\s+Mathematics?\s+Pure", t, re.I):
        if math9709_anchor(vid, prov, t, allow_bare=True):
            return
        skip(prov, vid, t, "9709 title with no distinctive match in the maths faces at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the t-test/confidence-interval series is the 9231 register — no spine course)")

def law_mathscamp(vid, t):
    prov = "maths-camp"
    has_code = bool(RE_SESSION.search(t))
    # register-first ordering (the P18 fiifi amendment precedent): the S1/9709
    # subject-name register adjudicates before the guidance gate — the
    # 'Everything You Need to Know about X for AS Level Probability & Statistics 1'
    # series is topic-structured teaching, not advice
    if RE_9709.search(t) or re.search(r"Probability\s*&?\s*[Ss]tatistics\s*[12]|AS\s+[Ll]evel\s+Mathematics", t, re.I):
        if math9709_anchor(vid, prov, t, allow_bare=True):
            return
        skip(prov, vid, t, "9709/S1 title with no distinctive match in the maths faces at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (bare IGCSE trig/geometry content without the pool's 9709 register)")

def law_ishan(vid, t):
    prov = "ishan"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9708.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-a-level-economics-23"], vid, prov, t, "9708 session/paper register anchor")
            return
        if bind_course("cie-a-level-economics-23", vid, prov, t):
            return
        skip(prov, vid, t, "9708 title with no distinctive match in cie-a-level-economics-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the psychology case-study remainder has no spine course)")

def law_biologybox(vid, t):
    prov = "biology-box"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_NT_BOARD.search(t):
        skip(prov, vid, t, "NT-board titles (AQA GCSE biology) — out-of-spine board")
        return
    if re.search(r"International\s+GCSE\s+Biology|Edexcel\s+i?GCSE\s+Biology|\b4BI1\b", t, re.I):
        mod = modsci_route(t)
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            cl = ["igcse-biology-19"] + mod + (["igcse-science-double-award-17-biology"] if re.search(r"Double\s+[Aa]ward|4SD0", t, re.I) else [])
            tb(cl, vid, prov, t, "Edexcel International GCSE biology paper register anchor (the modular/DA faces where tokened)")
            return
        if bind_course("igcse-biology-19", vid, prov, t):
            if mod:
                bind_course(mod[0], vid, prov, t)
            if re.search(r"Double\s+[Aa]ward|4SD0", t, re.I):
                bind_course("igcse-science-double-award-17-biology", vid, prov, t)
            return
        skip(prov, vid, t, "Edexcel International GCSE biology title with no distinctive match in igcse-biology-19 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (the pool's register is the 'International GCSE Biology (Edexcel) Lesson N' series)")

def law_thecsclassroom(vid, t):
    prov = "the-cs-classroom"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IBDP.search(t) or RE_NT_BOARD.search(t):
        skip(prov, vid, t, "IB/NT register (IB Computer Science 2027) — no spine course")
        return
    if RE_9618.search(t):
        if cs9618_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "9618 title with no distinctive match in cie-a-level-computer-science-19 at the df<=3 bar")
        return
    if RE_0478.search(t):
        if igcse0478_anchor(vid, prov, t):
            return
        skip(prov, vid, t, "0478 title with no distinctive match in cie-igcse-computer-science-23 at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding (bare programming/life content is not a qualification register)")
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
    "otterbiotutor": law_otterbiotutor,
    "ptet-chemistry": law_ptet,
    "study-with-prashna": law_studywithprashna,
    "adam-viceroy": law_adamviceroy,
    "miss-natalie-chemistry": law_missnatalie,
    "mathlete-by-saad": law_mathlete,
    "cswithmrg": law_cswithmrg,
    "haguin-school": law_haguin,
    "mr-lee-business-econ": law_mrlee,
    "mr-mathew": law_mrmathew,
    "pla-academy-igcse-and-a-level-buddy": law_pla,
    "refactor-lab": law_refactorlab,
    "mathprep-with-ahmad-bilal": law_mathprep,
    "salihath-syed-basheer": law_salihath,
    "edex-world": law_edexworld,
    "biochemlogy": law_biochemlogy,
    "umara-ratnayake": law_umara,
    "aslaug-eggertsdottir": law_aslaug,
    "s-q": law_sq,
    "the-lightup-hub": law_lightup,
    "e-geo": law_egeo,
    "ilm-online-academy": law_ilm,
    "y-mx-c": law_ymxc,
    "miss-estruch-biology": law_missestruch,
    "wimzee-cambridge-academy": law_wimzee,
    "mysecondteacher": law_mysecondteacher,
    "the-future-professionals": law_tfp,
    "chembase-school-of-chemistry": law_chembase,
    "sayo-enoch-aluko": law_sayo,
    "hendrik-academy": law_hendrik,
    "walter-maths-tutoring": law_walter,
    "maths-camp": law_mathscamp,
    "ishan": law_ishan,
    "biology-box": law_biologybox,
    "the-cs-classroom": law_thecsclassroom,
}
assert set(LAWS) == set(JUDGMENT_POOLS)

# pools whose registers honestly carry the CIE 9709/IAL-maths component law
# (the pre-gate's blanket section-6 skip would kill them before their laws run —
# the P20 component routing of record owns the honest call instead)
IALMATHS_EXEMPT = {"mathlete-by-saad", "refactor-lab", "mathprep-with-ahmad-bilal",
                   "hendrik-academy", "walter-maths-tutoring", "maths-camp",
                   "study-with-prashna"}

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
               "p20bCourses": P20B, "keepsByCourse": by_course},
              open(f"{WORK}/judgment_summary.json", "w"), indent=1)

if __name__ == "__main__":
    main()
