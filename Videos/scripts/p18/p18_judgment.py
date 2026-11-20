#!/usr/bin/env python3
"""P18 judgment: route the 21 admitted gap-profile pools (5,843 uploads) onto the
fresh post-P17 residual spine. Owner order this session: "run P18 judgment"
(2026-11-20), the P18 filing (PR #362) admitted as filed (the P15/P17 convention:
the owner order admits the pools and opens the judgment gate).

The P15/P17 gate ladder unchanged, with the registers the P18 profile surfaced:

  Tier B   paper-code anchors   — session/paper codes in titles: 0610/0620/0625 CIE
                                 IGCSE sciences (0971/0972/0973 + the 5090 O-Level
                                 dual branding); 0654 co-ordinated shared-paper; CIE
                                 A-level sciences 9700/9701/9702 papers 1-3 AS / 4-5
                                 A2 (the P13/P14 paper-number routing law); 0417 /
                                 4IT1+4IT0 + the 'International GCSE ICT' register
                                 text; 4MA1 maths-A H/F + modular-24 4WM paper codes;
                                 4MB1 maths-B; 0580/0980 CIE maths papers 2/4
                                 extended vs 1/3 core (the P9/P14 law, code-required);
                                 4PM0/4PM1 Edexcel IGCSE Further Pure (the NEW P18
                                 register -> igcse-further-maths-19); 0606 (the
                                 disclosed 4037 O-Level dual branding); 0452/0985
                                 (+ the disclosed 7707 O-Level dual); 0455 (+ the
                                 disclosed 2281 dual); 0680; 0460; 9708; 9609; 4BS1;
                                 8021 General Paper (the NEW P18 register ->
                                 cie-as-english-general-paper-21); IAL WPH/WBI/WCH
                                 "Unit N <session>" unit-paper anchors (the P14
                                 Assil law) + the Pearson-pipe format.
  Class W  set-text work binds  — the P16 committed predicate (P17 amendment:
                                 possessive "Author's 'Work'" + hashtag-suffixed
                                 quote lookahead) for the 0475-register titles of
                                 tutoring-with-gavin and no-waffle-gcse.
  Class M/S/Tier A/Class L     — section markers (incl. the '0680/3.4' and
                                 'A Level economics - 3.4' in-title N.M forms),
                                 verbatim section-name binding, distinctive-token
                                 (df<=3), four-gate topic lectures.

  skips    honest ledger        — tuition-marketing/meta registers (grade
                                 thresholds, timetables, teacher profiles), the
                                 digital-literacy certification register (IC3/
                                 Certiport/MOS), CIE AS/A Level IT 9626 (no spine
                                 course), bare maths titles with no syllabus code,
                                 the O-Level register unless a spine-code token is
                                 present (the disclosed 4037/2281/7707/5090 dual
                                 brandings + the generalized spine-code precedence
                                 of the P14 zainematics law), IAL/CIE maths 9709
                                 bare walkthroughs (ANCHOR-GRANULARITY section 6,
                                 the P9/P17 precedent), NT boards, and the
                                 no-binding remainder.

P18 disclosed amendments to the committed regexes (this lane's disclosure duty,
the P17 Class W amendment precedent):
  1. RE_GUIDE 'vision' -> r"\bvision\b": the P14..P17 guidance pattern carried a
     bare 'vision' token that substring-matches inside 'revision' (re-VISION),
     mis-classing on-register revision/topic titles as guidance. Word-bounded
     here; the P17 skips ledger carries the same latent effect (disclosed, not
     re-opened — P17 is shipped).
  2. RE_4IT0 gains the 'International GCSE ICT' register text (the fiifi-aubbin
     lesson-series format) and the bare 'Edexcel GCSE ICT' text (the ict-at-tda
     register; the i?-optional alternative already accepted it — made explicit).
  3. Class W suffix-collision ledger (the P16 NOBIND_CHARS precedent): a span
     tail naming a LONGER off-spine work whose name ends in a short on-spine
     work name must not suffix-bind the short work ('singh song' -> Szirtes'
     'Song' rejected; Nagra's 'Singh Song!' is the AQA Love & Relationships
     poem, not the CIE 0475 set text).

Exactly-once disposition of all 5,843 accounts, 0 collisions machine-checked.
Outputs work/p18/: tier-b.json, judgment.json, skips.json, judgment_summary.json
"""
import json, os, re, datetime
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub"
WORK = "/home/z/my-project/work/p18"
UTC = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
os.makedirs(WORK, exist_ok=True)

JUDGMENT_POOLS = ["my-grade9-maths-tutor", "omar-nassar-accounting", "economics-by-abdul-hadi",
                  "chemistry-that-counts", "brian-kemp", "sense-business-studies",
                  "igcse-a-level-examcrack", "fiifi-aubbin", "the-maths-centre", "watchme-do-math",
                  "ict-at-tda", "a-levels-revision-videos", "really-academics",
                  "jmr-teaching-tech", "sir-usman-econ-business", "indigo-education-group",
                  "tsil-maths", "tutoring-with-gavin", "no-waffle-gcse", "scinova-education",
                  "ial-science-notes-topicals"]

pool = []
_seen = set()
for slug in JUDGMENT_POOLS:
    for v in json.load(open(f"{RES}/Videos/inventory/channels/{slug}-uploads.json"))["videos"]:
        if v["id"] in _seen:
            continue
        _seen.add(v["id"])
        pool.append({"id": v["id"], "title": v["title"], "provider": slug})
assert len(pool) == 5843, f"pool {len(pool)} != 5843"

# ---------------------------------------------------------------- spine
TARGETS = [
    # maths
    "igcse-maths-a-18-higher", "igcse-maths-a-18-foundation",
    "igcse-maths-a-modular-24-higher-unit-1", "igcse-maths-a-modular-24-higher-unit-2",
    "igcse-maths-a-modular-24-foundation-unit-1", "igcse-maths-a-modular-24-foundation-unit-2",
    "igcse-maths-b-16", "igcse-further-maths-19",
    "cie-igcse-further-maths-additional-maths-25",
    "cie-igcse-maths-25-extended", "cie-igcse-maths-25-core",
    # accounting
    "cie-igcse-accounting-25", "cie-igcse-accounting-21",
    # economics
    "cie-igcse-economics-20", "cie-igcse-economics-25", "cie-a-level-economics-23",
    # business
    "igcse-business-19", "cie-as-business-23", "cie-a-level-business-23",
    # geography / EM / general paper
    "cie-igcse-geography-20", "cie-igcse-geography-25",
    "cie-igcse-environmental-management-25", "cie-as-english-general-paper-21",
    # IAL trio
    "ial-physics-19", "ial-biology-18", "ial-chemistry-17",
    # CIE IGCSE sciences
    "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23",
    # CIE AS/A2 sciences (9700/9701/9702 paper routing)
    "cie-as-biology-25", "cie-a-level-biology-25",
    "cie-as-chemistry-25", "cie-a-level-chemistry-25",
    "cie-as-physics-25", "cie-a-level-physics-25",
    # Edexcel IGCSE sciences + double award + co-ordinated
    "igcse-chemistry-19", "igcse-biology-19", "igcse-physics-19",
    "igcse-science-double-award-17-biology", "igcse-science-double-award-17-chemistry",
    "igcse-science-double-award-17-physics",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry",
    # modular chemistry
    "igcse-chemistry-modular-24-unit-1", "igcse-chemistry-modular-24-unit-2",
    # ICT
    "igcse-ict-17", "cie-igcse-ict-21",
]

P4_CHILDREN = set(json.load(open(f"{RES}/Videos/drafts/_p4/inheritance-map.json"))["parents"].keys())
P18B = [c for c in TARGETS if c in P4_CHILDREN]

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
8021 0985 7707 4pm0 4pm1 0980 0983 0971 0972 0973 4wm shorts""".split())

def toks14(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2]

for course in TARGETS:
    df = Counter()
    for n in specs_spine[course]["nodes"]:
        for w in set(toks14(n["title"] or "")):
            df[w] += 1
    specs_spine[course]["df"] = df
    specs_spine[course]["pts"] = [n for n in specs_spine[course]["nodes"] if n["family"] == "SPEC_POINT"]
    specs_spine[course]["subs"] = [n for n in specs_spine[course]["nodes"] if n["family"] == "SUBTOPIC"]

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
    return [x.strip() for x in re.split(r"\|| - | — ", title) if x.strip()]

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
    r"|\b(?:may|june|oct|nov)\s*20\d\d|\bm/j\b|\bo/n\b|\bqp\b)", re.I)
RE_SOLVED = re.compile(r"solved|solution|walkthrough|past[- ]?paper|qp\s*_?\d|mark scheme|\bQ\s?\d|\bQ\(|question\s*\d|exam questions?|predictions?!? paper|\bcomplete\b|paper\s*\d", re.I)
RE_GUIDE = re.compile(
    r"tips|tricks?\b|ace your|how to (ace|finish|overcome|stop|prepare|revise|get full|write|score)|how (do i|this student|did paper)|"
    r"survival guide|preparation course|orientation|watch (this|before)|podcast|success|result day|"
    r"interview|\bvision\b|challenge|parents? of|\bupdates?\b(?!\s*(?:&|and|to)\s+(?:software|devices|systems))|tour|platform|worried|nervous|resit|message|"
    r"days? left|30 days|60 days|join now|score an a\*|a\* in|game.?chang|blended|covid|"
    r"studysmart|aitutor|revision in|month left|marking schemes|what you (need|can)|can't miss|"
    r"paper breakdown|important topics|fix of|lifesaver|one thing|stress|focus on what|predictions?!"
    r"|sneak preview|live class|whatsapp|daily dose|the reality of|full marks|made easy|sneak peek", re.I)
RE_OLEVEL = re.compile(r"\bO\s?-?\s?Levels?\b|\bOL\b|\b4024\b|\b2281\b|\b5070\b|\b5090\b|\b5124\b|\b2210\b|\b4037\b|\b4040\b|\b7707\b", re.I)
RE_NT_BOARD = re.compile(r"\bAQA\b|\bOCR\b|\bIB\b|\bNCERT\b|\bCBSE\b|\bJEE\b|\bNEET\b|\bKS[1-4]\b|\bAP\b|\bSAT\b|\bMEI\b|\bMYP\b|\bH2\b")
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
RE_4MB1 = re.compile(r"\b4MB1\b|IGCSE\s+Maths?\s+B\b|Maths?\s+B\s+(Exam|Paper|Past)", re.I)
RE_4WM = re.compile(r"\b4WM([12])\w*/", re.I)
RE_4XM = re.compile(r"\b4XM\d?\b", re.I)
RE_0606 = re.compile(r"\b0606\b|[Aa]dd(itional)?\s*[Mm]aths", re.I)
RE_0607 = re.compile(r"\b0607\b|international\s+mathematics", re.I)
RE_0580 = re.compile(r"\b0580\b|\b0980\b", re.I)
RE_0452 = re.compile(r"\b0452\b|\b0985\b|IGCSE\s+Account", re.I)
RE_0455 = re.compile(r"\b0455\b|IGCSE\s+Economics|IGCSE\s+Econ", re.I)
RE_0680 = re.compile(r"\b0680\b|[Ee]nvironmental\s+[Mm]anagement|\bE\.?M\.?\b\s*(paper|revision|topic)", re.I)
RE_0460 = re.compile(r"\b0460\b|\b0976\b|IGCSE\s+Geography", re.I)
RE_4GE1 = re.compile(r"\b4GE1\b|International\s+GCSE\s+Geography|Edexcel\s+i?GCSE\s+Geography", re.I)
RE_WPH = re.compile(r"\bWPH\d?\d?\b|IAL\s+[Pp]hysics|IAS\s+[Pp]hysics|IA2\s+[Pp]hysics", re.I)
RE_WBI = re.compile(r"\bWBI\d?\d?\b|IAL\s+[Bb]iology|IAS\s+[Bb]iology|IA2\s+[Bb]iology", re.I)
RE_WCH = re.compile(r"\bWCH\d?\d?\b|IAL\s+[Cc]hemistry|IAS\s+[Cc]hemistry|IA2\s+[Cc]hemistry", re.I)
RE_WIT = re.compile(r"\bWIT\d?\d?\b|IAL\s+Information\s+Technology", re.I)
RE_WEC = re.compile(r"\bWEC\d?\d?\b|IAL\s+Economics", re.I)
RE_9708 = re.compile(r"\b9708\b|A\s?[- ]?\s?[Ll]evel\s*[Ee]conomics", re.I)
RE_9609 = re.compile(r"\b9609\b|A\s?[Ll]evel\s*[Bb]usiness", re.I)
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
RE_IAL_MATHS = re.compile(r"IAL\s+Math|Edexcel\s+Maths?\s*[-\u2013]\s*(Pure|Mechanics|Statistics)|\b9709\b", re.I)
RE_PROMO = re.compile(r"register now|onsite classes|onsite class|money well spent|subscribe|follow (me|us)|visit (our|my)|\bemotional\b|new (course|batch)|enrol|admissions? open|tuition|#GP\w*", re.I)
RE_META = re.compile(r"grade boundar|threshold|timetable|teacher profile|birthday|thanks for (all|your)|2000 subs|celebrat|speedrun|farewell|teacher'?s day", re.I)
RE_CERT = re.compile(r"\bIC3\b|Certiport|\bMOS\b|Microsoft Office Specialist", re.I)
RE_CIE_IT = re.compile(r"(AS|A)\s?[Ll]evel\s+IT\b", re.I)
RE_0500tok = re.compile(r"\b0500\b|first\s+language\s+english", re.I)

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

def route(course, vid, prov, specs_list, confidence, reason, p18b=False, cross=False):
    judgment[course].append({"id": vid, "provider": prov, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p18b": p18b, "crossReg": cross})

def tb(course_list, vid, prov, title, code, cross=False):
    for course in course_list:
        tier_b.append({"id": vid, "title": title, "provider": prov, "courses": [course],
                       "code": code, "kind": "past-paper-walkthrough",
                       "p18b": course in P18B, "crossReg": cross})

def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|Q\s?\d|paper\s*\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

def bind_course(course, vid, prov, t, p18b=None):
    if p18b is None:
        p18b = course in P18B
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p18b)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p18b)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs_spine[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p18b)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p18b)
            return True
    return False

COORD_TRIO = ["cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
              "cie-igcse-science-co-ordinated-sciences-double-award-23-physics",
              "cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry"]
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
        if RE_PROMO.search(t) or len(re.sub(r"\W+", "", t)) < 6:
            skip(slug, vid, t, "channel promo/meta content (no qualification register)")
            continue
        if RE_META.search(t):
            skip(slug, vid, t, "meta announcement (grade thresholds/timetable/results/celebration) — no qualification register")
            continue
        if RE_IAL_MATHS.search(t):
            skip(slug, vid, t, "IAL/CIE maths register (P1-M2/S1/9709) — bare unit/session walkthroughs skip per ANCHOR-GRANULARITY §6 (P9 precedent); the maths spine courses sit outside the P18 pool contract")
            continue
        exempt = olevel_exempt and olevel_exempt(t)
        has_spine_code = bool(RE_0606.search(t) or RE_0607.search(t) or RE_0452.search(t)
                              or RE_0455.search(t) or RE_0610.search(t) or RE_0620.search(t)
                              or RE_0625.search(t) or RE_0580.search(t) or RE_0417.search(t)
                              or RE_9708.search(t) or RE_9609.search(t) or RE_9700.search(t)
                              or RE_9701.search(t) or RE_9702.search(t) or RE_8021.search(t)
                              or RE_0460.search(t) or RE_0680.search(t) or RE_0475.search(t)
                              or RE_4MA1.search(t) or RE_4MB1.search(t) or RE_4PM.search(t)
                              or RE_4BS1.search(t) or RE_0500tok.search(t))
        if not exempt and RE_OLEVEL.search(t) and not has_spine_code:
            skip(slug, vid, t, "O-Level register (4024/2281/5090/7707/...) with no IGCSE spine-code token — no O-Level course in the spine")
            continue
        if RE_ED_CS.search(t):
            skip(slug, vid, t, "Edexcel UK-GCSE Computer Science — no spine course (the spine carries CIE 0478, not the UK GCSE CS)")
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
    """Unit N + session/paper reference -> unit-paper review anchor (P14 Assil law).
    subject: 'bio'|'chem'|'phys'|None (auto from title)."""
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
    """CIE A-level sciences 9700/9701/9702 paper routing (the P13/P14 law:
    papers 1-3 -> the AS course, papers 4-5 -> the A-level course)."""
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
    Code-required — bare 'IGCSE Maths' titles never reach here."""
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

def further_pure_anchor(vid, prov, t):
    """4PM0/4PM1 Edexcel IGCSE Further Pure (the NEW P18 register) — the mathman
    shape (the P17 0606 law): session OR solved OR paper/Q token routes the anchor."""
    if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d|\bQ\s?\d", t, re.I):
        tb(["igcse-further-maths-19"], vid, prov, t,
           "Edexcel IGCSE Further Pure Maths (4PM0/4PM1) session/paper register anchor")
        return True
    if bind_course("igcse-further-maths-19", vid, prov, t):
        return True
    skip(CURRENT_PROV[0], vid, t, "Further Pure title with no distinctive match in igcse-further-maths-19 at the df<=3 bar")
    return True

def gp_anchor(vid, prov, t):
    """8021 General Paper (the NEW P18 register) -> cie-as-english-general-paper-21."""
    if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
        tb(["cie-as-english-general-paper-21"], vid, prov, t, "8021 General Paper session/paper register anchor")
        return True
    if bind_course("cie-as-english-general-paper-21", vid, prov, t):
        return True
    skip(CURRENT_PROV[0], vid, t, "General Paper title with no distinctive match in cie-as-english-general-paper-21 at the df<=3 bar")
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

# ---------------------------------------------------------------- P18 pool laws

def law_mygrade9(vid, t):
    prov = "my-grade9-maths-tutor"
    if RE_4MA1.search(t) or RE_4WM.search(t) or re.search(r"IGCSE\s+Math", t, re.I):
        cl = ma_routes(t)
        pn = paper_num(t)
        sm = RE_SESSION.search(t)
        for c in cl:
            tb([c], vid, prov, t, "4MA1/4WM Edexcel IGCSE maths paper anchor" +
               (f" ({'higher' if 'higher' in c else ('foundation' if 'foundation' in c else 'modular')})" if len(cl) == 1 else " — register not stated in title, both tiers bound (disclosed)") +
               (f", paper {pn}" if pn else "") + (f", session '{sm.group(0)[:24]}'" if sm else ""))
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar (the pool's register is 4MA1 Edexcel IGCSE maths)")

def law_omar(vid, t):
    prov = "omar-nassar-accounting"
    for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the accounting pair (0452/0985/7707 topic register)")

def law_econ(vid, t, prov):
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9708.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d|mcq|variant|paper\s*3|paper\s*4", t, re.I)):
        tb(["cie-a-level-economics-23"], vid, prov, t, "9708 A-level economics paper register anchor")
        return
    if RE_0455.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
            tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-a-level-economics-23", "cie-igcse-economics-20", "cie-igcse-economics-25"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_abdulhadi(vid, t):
    law_econ(vid, t, "economics-by-abdul-hadi")

def law_sirusman(vid, t):
    law_econ(vid, t, "sir-usman-econ-business")

def law_alevelsrevision(vid, t):
    law_econ(vid, t, "a-levels-revision-videos")

def law_chemcounts(vid, t):
    prov = "chemistry-that-counts"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WCH.search(t) or re.search(r"IAL\s*Chem", t, re.I):
        if ial_unit_anchor(vid, prov, t, subject="chem"):
            return
        if bind_course("ial-chemistry-17", vid, prov, t):
            return
        skip(prov, vid, t, "IAL chemistry title with no distinctive match in ial-chemistry-17 at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    ecl = ed_science_anchor(t)
    if ecl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in ecl:
            tb([c], vid, prov, t, "Edexcel IGCSE science paper register anchor (4CH1/4BI1/4PH1/4SD0)")
        return
    for c in ["igcse-chemistry-19", "cie-igcse-chemistry-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_briankemp(vid, t):
    prov = "brian-kemp"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_4MA1.search(t) or RE_4WM.search(t):
        cl = ma_routes(t)
        for c in cl:
            tb([c], vid, prov, t, "4MA1/4WM Edexcel IGCSE maths paper anchor")
        return
    if cie_alevel_sci_anchor(vid, prov, t):
        return
    if RE_0455.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
            tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    if RE_4BS1.search(t):
        tb(["igcse-business-19"], vid, prov, t, "Edexcel IGCSE Business 4BS1 paper register anchor")
        return
    if RE_0460.search(t):
        if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I):
            for c in ["cie-igcse-geography-20", "cie-igcse-geography-25"]:
                tb([c], vid, prov, t, "0460 IGCSE geography paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        if bind_course("cie-igcse-geography-25", vid, prov, t):
            return
        if bind_course("cie-igcse-geography-20", vid, prov, t):
            return
        skip(prov, vid, t, "0460 title with no distinctive match in the geography pair at the df<=3 bar")
        return
    if RE_0452.search(t):
        if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I):
            for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
                tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        if bind_course("cie-igcse-accounting-25", vid, prov, t):
            return
        skip(prov, vid, t, "0452 title with no distinctive match in cie-igcse-accounting-25 at the df<=3 bar")
        return
    if RE_COORDD.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        tb(COORD_TRIO, vid, prov, t, "0654 co-ordinated sciences session/paper anchor — shared-paper binding to all three sciences (disclosed)")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in ["cie-a-level-economics-23", "cie-igcse-economics-20", "cie-igcse-economics-25",
              "igcse-business-19", "cie-igcse-biology-23", "cie-igcse-chemistry-23", "cie-igcse-physics-23"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_sense(vid, t):
    prov = "sense-business-studies"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0580.search(t):
        maths058_anchor(vid, prov, t)
        return
    if RE_0455.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-economics-20", "cie-igcse-economics-25"]:
            tb([c], vid, prov, t, "0455 IGCSE economics paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    if RE_0452.search(t):
        if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I):
            for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
                tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        if bind_course("cie-igcse-accounting-25", vid, prov, t):
            return
        skip(prov, vid, t, "0452 title with no distinctive match in cie-igcse-accounting-25 at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    for c in ["igcse-business-19", "cie-igcse-biology-23", "cie-igcse-physics-23", "cie-igcse-chemistry-23",
              "cie-igcse-economics-25", "cie-igcse-economics-20"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_examcrack(vid, t):
    prov = "igcse-a-level-examcrack"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WPH.search(t) or RE_WCH.search(t) or RE_WBI.search(t):
        if ial_unit_anchor(vid, prov, t):
            return
        course = "ial-physics-19" if RE_WPH.search(t) else ("ial-chemistry-17" if RE_WCH.search(t) else "ial-biology-18")
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, f"IAL title with no distinctive match in {course} at the df<=3 bar")
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
    if RE_4PM.search(t):
        further_pure_anchor(vid, prov, t)
        return
    if cie_alevel_sci_anchor(vid, prov, t):
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    if RE_9708.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d|variant", t, re.I)):
        tb(["cie-a-level-economics-23"], vid, prov, t, "9708 A-level economics paper register anchor")
        return
    if RE_9609.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d|variant", t, re.I)):
        for c in ["cie-as-business-23", "cie-a-level-business-23"]:
            tb([c], vid, prov, t, "9609 business paper register anchor — bound to both AS and A-level courses (shared code, disclosed)")
        return
    if RE_0452.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
            tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — the 7707 token is the O-Level dual branding (disclosed)")
        return
    if RE_0417.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
        return
    if RE_4MA1.search(t) or RE_4WM.search(t) or RE_4MB1.search(t) or RE_4XM.search(t):
        cl = ma_routes(t)
        for c in cl:
            tb([c], vid, prov, t, "Edexcel IGCSE maths paper anchor (4MA1/4WM/4MB1)")
        return
    ecl = ed_science_anchor(t)
    if ecl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in ecl:
            tb([c], vid, prov, t, "Edexcel IGCSE science paper register anchor (4CH1/4BI1/4PH1/4SD0)")
        return
    for c in ["cie-igcse-chemistry-23", "cie-igcse-physics-23", "cie-igcse-biology-23",
              "igcse-chemistry-19", "igcse-physics-19", "igcse-biology-19"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_fiifi(vid, t):
    prov = "fiifi-aubbin"
    # ICT code/register anchors adjudicate BEFORE the guidance gate: the lesson
    # series carries machine-checkable register text ('International GCSE ICT',
    # 4IT1, 0417/0983) and topic titles like 'Communication Software, Updates &
    # Software Review' are content, not guidance (the P18 RE_GUIDE amendment).
    if RE_CERT.search(t):
        skip(prov, vid, t, "digital-literacy certification register (IC3/Certiport/MOS) — out-of-spine register")
        return
    if RE_CIE_IT.search(t) or RE_WIT.search(t):
        skip(prov, vid, t, "CIE AS/A Level IT (9626) / Edexcel IAL IT (WIT) — no spine course")
        return
    it1 = bool(RE_4IT0.search(t))
    it0417 = bool(RE_0417.search(t))
    if it1 and it0417:
        tb(["igcse-ict-17"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — Edexcel side anchor")
        tb(["cie-igcse-ict-21"], vid, prov, t, "dual-register ICT title: 4IT1 + 0417/0983 codes — CIE side anchor (dual-coded, disclosed)")
        return
    if it1:
        tb(["igcse-ict-17"], vid, prov, t, "Edexcel International GCSE ICT (4IT1) register anchor")
        return
    if it0417 and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-igcse-ict-21"], vid, prov, t, "CIE 0417 session/paper register anchor")
        return
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_9708.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        tb(["cie-a-level-economics-23"], vid, prov, t, "9708 A-level economics paper register anchor")
        return
    if RE_4MA1.search(t) or RE_4WM.search(t):
        cl = ma_routes(t)
        for c in cl:
            tb([c], vid, prov, t, "4MA1/4WM Edexcel IGCSE maths paper anchor")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses (digital-skills register)")

def law_mathscentre(vid, t):
    prov = "the-maths-centre"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0606.search(t):
        if RE_SESSION.search(t) and (RE_SOLVED.search(t) or paper_num(t)):
            tb(["cie-igcse-further-maths-additional-maths-25"], vid, prov, t, "0606 session/paper register anchor (the 4037 token is the O-Level dual branding of the same syllabus)")
            return
        if bind_course("cie-igcse-further-maths-additional-maths-25", vid, prov, t):
            return
        skip(prov, vid, t, "0606 title with no distinctive match at the df<=3 bar")
        return
    if RE_4PM.search(t):
        further_pure_anchor(vid, prov, t)
        return
    if RE_4MA1.search(t) or RE_4WM.search(t):
        cl = ma_routes(t)
        for c in cl:
            tb([c], vid, prov, t, "4MA1/4WM Edexcel IGCSE maths paper anchor")
        return
    if RE_0452.search(t):
        if RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I):
            for c in ["cie-igcse-accounting-25", "cie-igcse-accounting-21"]:
                tb([c], vid, prov, t, "0452 IGCSE accounting paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
            return
        if bind_course("cie-igcse-accounting-25", vid, prov, t):
            return
        skip(prov, vid, t, "0452 title with no distinctive match in cie-igcse-accounting-25 at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    if RE_0460.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-geography-20", "cie-igcse-geography-25"]:
            tb([c], vid, prov, t, "0460 IGCSE geography paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    for c in ["cie-igcse-further-maths-additional-maths-25", "cie-igcse-accounting-25"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_watchme(vid, t):
    prov = "watchme-do-math"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4PM.search(t) or re.search(r"Further\s+Pure", t, re.I):
        further_pure_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (the pool's register is 4PM0 Further Pure)")

def law_icttda(vid, t):
    prov = "ict-at-tda"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_WIT.search(t):
        skip(prov, vid, t, "Edexcel IAL Information Technology (WIT) — no spine course")
        return
    if RE_4IT0.search(t) or re.search(r"ICT\s+Paper", t, re.I):
        tb(["igcse-ict-17"], vid, prov, t, "Edexcel IGCSE ICT (4IT1/4IT0 register text) course anchor")
        return
    if bind_course("igcse-ict-17", vid, prov, t):
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over igcse-ict-17")

def law_really(vid, t):
    prov = "really-academics"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WCH.search(t) or RE_WBI.search(t) or RE_WPH.search(t):
        if ial_unit_anchor(vid, prov, t):
            return
        course = "ial-physics-19" if RE_WPH.search(t) else ("ial-chemistry-17" if (RE_WCH.search(t) or re.search(r"chem", t, re.I)) else "ial-biology-18")
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, f"IAL title with no distinctive match in {course} at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_jmr(vid, t):
    prov = "jmr-teaching-tech"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_0680.search(t):
        em_anchor(vid, prov, t)
        return
    if RE_0460.search(t) and (RE_SESSION.search(t) or RE_SOLVED.search(t) or re.search(r"paper\s*\d", t, re.I)):
        for c in ["cie-igcse-geography-20", "cie-igcse-geography-25"]:
            tb([c], vid, prov, t, "0460 IGCSE geography paper register anchor — bound to both syllabus-year courses (shared code, disclosed)")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_indigo(vid, t):
    prov = "indigo-education-group"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_8021.search(t):
        gp_anchor(vid, prov, t)
        return
    skip(prov, vid, t, "no honest binding (the pool's register is 8021 General Paper; the JC-tuition remainder is off-register)")

def law_tsil(vid, t):
    prov = "tsil-maths"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_4PM.search(t):
        further_pure_anchor(vid, prov, t)
        return
    if RE_4MB1.search(t) or RE_4MA1.search(t) or RE_4WM.search(t):
        cl = ma_routes(t)
        for c in cl:
            tb([c], vid, prov, t, "Edexcel IGCSE maths paper anchor (4MA1/4MB1)")
        return
    if RE_4BS1.search(t):
        tb(["igcse-business-19"], vid, prov, t, "Edexcel IGCSE Business 4BS1 paper register anchor")
        return
    for c in ["igcse-further-maths-19", "ial-physics-19"]:
        if bind_course(c, vid, prov, t):
            return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_scinova(vid, t):
    prov = "scinova-education"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WPH.search(t):
        if ial_unit_anchor(vid, prov, t, subject="phys"):
            return
        if bind_course("ial-physics-19", vid, prov, t):
            return
        skip(prov, vid, t, "IAL physics title with no distinctive match in ial-physics-19 at the df<=3 bar")
        return
    cl = ig_science_anchor(vid, prov, t)
    if cl and (RE_SESSION.search(t) or RE_SOLVED.search(t)):
        for c in cl:
            tb([c], vid, prov, t, "CIE IGCSE science session/paper register anchor")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

def law_ialnotes(vid, t):
    prov = "ial-science-notes-topicals"
    has_code = bool(RE_SESSION.search(t))
    if is_guidance(t, has_code):
        skip(prov, vid, t, "guidance/advice/marketing register (P12 gate)")
        return
    if RE_IAL_UNIT.search(t) or RE_WCH.search(t) or RE_WPH.search(t) or RE_WBI.search(t):
        if ial_unit_anchor(vid, prov, t):
            return
        course = "ial-physics-19" if RE_WPH.search(t) else ("ial-chemistry-17" if (RE_WCH.search(t) or re.search(r"chem", t, re.I)) else "ial-biology-18")
        if bind_course(course, vid, prov, t):
            return
        skip(prov, vid, t, f"IAL title with no distinctive match in {course} at the df<=3 bar")
        return
    skip(prov, vid, t, "no honest binding at the df<=3 bar over the pool's target courses")

# ---------------------------------------------------------------- Class W (P16 predicate, P17 amendment)
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
NOBIND_CHARS = ["Malvolio", "Caliban", "Sybil", "Eric Birling", "Mr Hyde", "Scrooge", "Cratchit", "Juliet", "Banquo", "Miranda", "Ferdinand"]
LW_SUFFIX_COLLISIONS = {"singh song": "song"}  # the disclosed P18 amendment ledger
TRAIL_JUNK = re.compile(
    r"\s*(\[?part\s+\d+(\s+of\s+\d+)?\]?|part\s+\d+|analysis|detailed analysis|"
    r"detailed commentary and analysis|commentary and analysis|full analysis|"
    r"line by line analysis|line by line|detailed commentary|commentary|"
    r"study guide.*)$", re.I)

def lw_extract(title):
    """The P16 extract_candidates with the disclosed P17 amendment."""
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
    """The P16 suffix-anchored spine-work match, with the disclosed P18 amendment:
    a small suffix-collision ledger (the NOBIND_CHARS precedent) — a span tail
    naming a LONGER off-spine work whose name ends in a short on-spine work name
    must not bind the short work (e.g. Nagra's 'Singh Song!' — AQA Love &
    Relationships — must not suffix-bind Szirtes' 'Song', CIE 0475 S21.016)."""
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

def law_gavin(vid, t):
    lit_law(vid, t, "tutoring-with-gavin")

def law_nowaffle(vid, t):
    lit_law(vid, t, "no-waffle-gcse")

# ---------------------------------------------------------------- run
LAWS = {
    "my-grade9-maths-tutor": law_mygrade9,
    "omar-nassar-accounting": law_omar,
    "economics-by-abdul-hadi": law_abdulhadi,
    "chemistry-that-counts": law_chemcounts,
    "brian-kemp": law_briankemp,
    "sense-business-studies": law_sense,
    "igcse-a-level-examcrack": law_examcrack,
    "fiifi-aubbin": law_fiifi,
    "the-maths-centre": law_mathscentre,
    "watchme-do-math": law_watchme,
    "ict-at-tda": law_icttda,
    "a-levels-revision-videos": law_alevelsrevision,
    "really-academics": law_really,
    "jmr-teaching-tech": law_jmr,
    "sir-usman-econ-business": law_sirusman,
    "indigo-education-group": law_indigo,
    "tsil-maths": law_tsil,
    "tutoring-with-gavin": law_gavin,
    "no-waffle-gcse": law_nowaffle,
    "scinova-education": law_scinova,
    "ial-science-notes-topicals": law_ialnotes,
}
assert set(LAWS) == set(JUDGMENT_POOLS)

# per-pool O-Level exemptions (the disclosed dual-brandings: 0455/2281, 0452/7707,
# 0610/5090, 0606/4037 — the global gate already exempts 0606/0607/0452/0455/0610)
OLEVEL_EXEMPT = {}

TITLE_OF = {v["id"]: v["title"] for v in pool}

def main():
    for slug, law in LAWS.items():
        CURRENT_PROV[0] = slug
        n0_t, n0_a, n0_s = len(tier_b), sum(len(x) for x in judgment.values()), len(skips)
        judge_pool(slug, law, OLEVEL_EXEMPT.get(slug))
        print(f"[{slug}] anchors +{len(tier_b)-n0_t}, routed +{sum(len(x) for x in judgment.values())-n0_a}, skips +{len(skips)-n0_s}", flush=True)

    # NT/UK-GCSE final sanity pass
    nt_leak = [r for vs in judgment.values() for r in vs if RE_NT_BOARD.search(TITLE_OF[r['id']])]
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
               "p18bCourses": P18B, "keepsByCourse": by_course},
              open(f"{WORK}/judgment_summary.json", "w"), indent=1)

if __name__ == "__main__":
    main()
