#!/usr/bin/env python3
"""P12 judgment: route the 11-pool in-cluster candidates onto the five uncovered
CIE targets. Classes:
  Tier B  paper-code anchors  — machine-checkable session/paper codes in titles
                                (method paper-code, confidence high, specs [], kind
                                past-paper-walkthrough, boardMismatch false)
  Class L  topic-complete lectures — full-topic "Complete Lesson"/topic-name lectures
                                bind the topic's SPEC_POINTs as ONE multi-spec row,
                                confidence low (disclosed granularity, title-only bar)
  Class M  section markers    — titles naming an "N.M" section bind that subtopic's
                                points as ONE multi-spec row, confidence low
  Tier A  distinctive-token   — df<=3 token binds, 1 best SPEC_POINT per row,
                                confidence medium (>=2 distinctive) / low (>=3 informative
                                at the disclosed higher title-only bar)
  skips    honest ledger      — everything else (technique register, generic course
                                mentions, out-of-lane registers, no-binding)
"""
import json, os, re
from collections import Counter

WORK = "/home/z/my-project/work/p12"
UTC = "2026-11-13T14:40:00Z"

TARGETS = {
    "cie-as-business-23": "9609",
    "cie-a-level-business-23": "9609",
    "cie-a-level-geography-21": "9696",
    "cie-as-environmental-management-20": "8291",
    "cie-as-english-general-paper-21": "8021",
}
CHANNELS = {
    "cambridge-business-essentials": "Cambridge Business Essentials A-level & IGCSE",
    "bizedmadesimple": "BizEdMadeSimple",
    "alt-academy": "A Level Business | Alt Academy",
    "the-teaching-student": "The Teaching Student",
    "the-geography-academy": "The Geography Academy",
    "virtual-pathways": "Virtual Pathways",
    "polymath-institute": "Polymath Institute",
    "mini-lessons-gp": "Mini Lessons",
    "english-with-ms-irum": "English with Ms Irum",
    "ace-the-exam": "Ace The Exam Cambridge IGCSE O & A Levels",
    "miss-cutu": "Miss Cutu Bilingual Help",
}
CLUSTER = {
    "cambridge-business-essentials": "business9609", "bizedmadesimple": "business9609",
    "alt-academy": "business9609", "the-teaching-student": "business9609",
    "the-geography-academy": "geo9696",
    "virtual-pathways": "em8291", "polymath-institute": "em8291",
    "mini-lessons-gp": "gp8021", "english-with-ms-irum": "gp8021",
    "ace-the-exam": "gp8021", "miss-cutu": "gp8021",
}
CLUSTER_TARGETS = {
    "business9609": ["cie-as-business-23", "cie-a-level-business-23"],
    "geo9696": ["cie-a-level-geography-21"],
    "em8291": ["cie-as-environmental-management-20"],
    "gp8021": ["cie-as-english-general-paper-21"],
}

STOP = set("""the a an of and or to in on for with your how what why when from as is are be
you i we they it its their our my this that these those at by not no do does using use
explained simply vs versus part guide tips tricks answer answering level as a2 igcse
cambridge international caie complete full everything need know revision exam exams
prepare preparation preparation skill skills study lesson lectures lecture course class
watch before september october november may june feb march oct nov jun may uk etc new
updated best top must topics topic questions question paper papers as-level
business 9609 9696 8291 8021""".split())

ACR = {"hrm": ["human", "resource", "management"], "em": ["environmental", "management"]}

def toks(s):
    s = s.lower()
    for ac, exp in ACR.items():
        s = re.sub(rf"\b{ac}\b", " ".join(exp), s)
    return [w for w in re.findall(r"[a-z0-9]+", s) if w not in STOP and len(w) > 2]

specs = json.load(open(f"{WORK}/target-specs.json"))
# per-target: SPEC_POINT list (code, title, topic-title, topic-index) + df over all bindable titles
SP = {}
for course in TARGETS:
    nodes = specs[course]
    topic_of, torder, cur = {}, {}, 0
    for n in nodes:
        if n["family"] == "TOPIC":
            cur += 1
            torder[n["code"]] = cur
        topic_of[n["code"]] = None
    cur_t = None
    t_idx = {}
    for n in nodes:
        if n["family"] == "TOPIC":
            cur_t = n["title"]
        t_idx[n["code"]] = cur_t
    pts = [n for n in nodes if n["family"] == "SPEC_POINT"]
    subs = [n for n in nodes if n["family"] == "SUBTOPIC"]
    df = Counter()
    for n in nodes:
        for w in set(toks(n["title"] or "")):
            df[w] += 1
    SP[course] = {"pts": pts, "subs": subs, "df": df, "t_idx": t_idx, "nodes": nodes,
                  "topic_order": torder}

def sub_points(course, subcode):
    """spec points of a subtopic (code prefix match on hierarchical numbering)"""
    num = subcode.split(":")[-1].replace("SUB", "")  # e.g. SUB1.3 -> 1.3
    return [p for p in SP[course]["pts"] if re.match(rf"^{re.escape(num)}\.\d+$", p["code"])]

def topic_points(course, topic_title):
    """spec points under a topic (by topic title)"""
    keep, cur_t = [], None
    for n in SP[course]["nodes"]:
        if n["family"] == "TOPIC":
            cur_t = n["title"]
        elif n["family"] == "SPEC_POINT" and cur_t == topic_title:
            keep.append(n)
    return keep

def best_point(course, title, max_df=3):
    """distinctive-token best SPEC_POINT match; returns (point, tokens, df-max, informative-n)"""
    vt = set(toks(title))
    best, best_score = None, 0
    for p in SP[course]["pts"]:
        pt = set(toks(p["title"] or ""))
        if not pt:
            continue
        hits = vt & pt
        if not hits:
            continue
        dmax = max(SP[course]["df"].get(w, 99) for w in hits)
        distinctive = [w for w in hits if SP[course]["df"].get(w, 99) <= max_df]
        score = len(distinctive) * 10 + len(hits)
        if len(distinctive) >= 2 or (len(hits) >= 3 and dmax <= 6):
            if score > best_score:
                best, best_score = (p, sorted(hits), dmax, len(hits)), score
    return best

def topic_tdf(course):
    """df over TOPIC+SUBTOPIC titles only (for the topic-unique lecture class)"""
    from collections import Counter as C
    c = C()
    for n in SP[course]["nodes"]:
        if n["family"] in ("TOPIC", "SUBTOPIC"):
            for w in set(toks(n["title"] or "")):
                c[w] += 1
    return c

TDF = {c: topic_tdf(c) for c in TARGETS}

def topic_by_unique_token(course, title):
    """the topic the title names honestly, by four gates:
    (a) verbatim: STOP-stripped title contains the STOP-stripped topic title
    (b) multi-uniq: >=2 tokens of the topic's scope unique among all topics' scopes
    (c) title-token: 1 unique token that belongs to the TOPIC TITLE itself
    (d) title-pair: >=2 tokens hitting the TOPIC TITLE, each unique among TOPIC titles
    returns (topic_title, uniq, all_hits, cls) or None"""
    vt = set(toks(title))
    vt_stripped = " " + " ".join(w for w in re.findall(r"[a-z0-9]+", title.lower())) + " "
    # df over TOPIC TITLES alone
    tdf = {}
    for n in SP[course]["nodes"]:
        if n["family"] == "TOPIC":
            for w in set(toks(n["title"] or "")):
                tdf[w] = tdf.get(w, 0) + 1
    best = None
    for n in SP[course]["nodes"]:
        if n["family"] != "TOPIC":
            continue
        tset = set(toks(n["title"] or ""))
        subtoks = set()
        seen = False
        for m in SP[course]["nodes"]:
            if m is n:
                seen = True
                continue
            if seen and m["family"] == "TOPIC":
                break
            if seen and m["family"] == "SUBTOPIC":
                subtoks |= set(toks(m["title"] or ""))
        scope = tset | subtoks
        hits = vt & scope
        uniq = [w for w in hits if TDF[course].get(w, 99) <= 1]
        tpair = sorted(w for w in hits if w in tset and tdf.get(w, 99) <= 1)
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

def best_sub(course, title, max_df=3):
    vt = toks(title)
    best, best_score = None, 0
    for s in SP[course]["subs"]:
        st = set(toks(s["title"] or ""))
        hits = [w for w in vt if w in st]
        if not hits:
            continue
        distinctive = [w for w in hits if SP[course]["df"].get(w, 99) <= max_df]
        score = len(distinctive) * 10 + len(hits)
        if len(distinctive) >= 2:
            if score > best_score:
                best, best_score = (s, hits), score
    return best

tier_b, tier_a, skips = [], [], []
judgment = {c: [] for c in TARGETS}

def skip(slug, vid, title, reason):
    skips.append({"video": vid, "title": title, "provider": slug, "reason": reason})

def route(course, vid, provider, specs_list, confidence, reason):
    judgment[course].append({"id": vid, "provider": provider, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason})

pool = []
for slug, cluster in CLUSTER.items():
    for v in json.load(open(f"{WORK}/inl-{slug}.json")):
        pool.append({**v, "provider": slug, "cluster": cluster})

# ---------- Tier B: machine-checkable paper codes ----------
SESS = re.compile(r"(\b\d{4}/\d{2}/(?:[smw]\d{2,4})\b)|(\b9609/\d{2}/[A-Za-z]/[A-Za-z]/\d{2}\b)|((may\s*june|oct(?:ober)?\s*[- ]?nov(?:ember)?|feb(?:ruary)?\s*[- ]?march)\s*\d{4})", re.I)
CODE = re.compile(r"\b(9609|9696|8291|8021)/(\d{2})", re.I)
PRED = re.compile(r"9609/(\d{2})/[A-Za-z]/[A-Za-z]/(\d{2})", re.I)

for v in pool:
    t = v["title"]
    if v["cluster"] == "business9609":
        m = PRED.search(t)
        if m:
            course = ("cie-a-level-business-23" if re.search(r"\bA Level\b", t, re.I) or "/4" in m.group(0)
                      else "cie-as-business-23")
            tier_b.append({"id": v["id"], "title": t, "provider": v["provider"], "code": m.group(0),
                           "courses": [course], "kind": "past-paper-walkthrough"})
            continue
    if v["cluster"] == "geo9696":
        m = CODE.search(t)
        if m and re.search(r"walkthrough|solved|solution", t, re.I):
            tier_b.append({"id": v["id"], "title": t, "provider": v["provider"], "code": m.group(0),
                           "courses": ["cie-a-level-geography-21"], "kind": "past-paper-walkthrough"})
            continue
    if v["cluster"] == "gp8021":
        has_code = re.search(r"\b8021\b", t)
        has_sess = re.search(r"(may\s*june|oct(?:ober)?\s*[- ]?nov(?:ember)?)\s*\d{4}", t, re.I)
        has_paper = re.search(r"paper\s*[12]", t, re.I)
        if has_sess and has_paper and re.search(r"comprehension|essay|paper\s*[12]\b.*\|", t, re.I) and v["provider"] == "english-with-ms-irum":
            tier_b.append({"id": v["id"], "title": t, "provider": v["provider"],
                           "code": ("8021 " if has_code else "") + (has_sess.group(0) + " " if has_sess else "") + (has_paper.group(0) if has_paper else ""),
                           "courses": ["cie-as-english-general-paper-21"], "kind": "past-paper-walkthrough"})
            continue

tb_ids = {x["id"] for x in tier_b}

# ---------- per-cluster Tier A / class rows ----------
for v in pool:
    vid, t, prov = v["id"], v["title"], v["provider"]
    if vid in tb_ids:
        continue

    # ---- 9696 geography ----
    if v["cluster"] == "geo9696":
        course = "cie-a-level-geography-21"
        if re.search(r"case study|how to answer|exam skills|why your|changes to|top in the world|exam preparation", t, re.I) and not re.search(r"9696/\d{2}", t):
            skip(prov, vid, t, "case-study/technique register without machine-checkable code or distinctive topic tokens")
            continue
        m = re.search(r"\b(\d{1,2})\.(\d{1,2})\s", t + " ")
        if m and re.search(r"9696|cambridge|geograph", t, re.I):
            num = f"{m.group(1)}.{m.group(2)}"
            subs = [s for s in SP[course]["subs"]
                    if s["code"].split(":")[-1].replace("SUB", "") == num]
            if subs:
                pts = sub_points(course, subs[0]["code"])
                if pts:
                    route(course, vid, prov, [p["code"] for p in pts], "low",
                          f"section-marker narrowing: title names section {num} '{subs[0]['title'][:60]}' — section points bound at the disclosed higher title-only bar")
                    continue
        b = best_point(course, t)
        if b:
            p, hits, dmax, nh = b
            conf = "medium" if sum(1 for w in hits if SP[course]["df"].get(w, 99) <= 3) >= 2 else "low"
            route(course, vid, prov, [p["code"]], conf,
                  f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})")
            continue
        tb2 = topic_by_unique_token(course, t)
        if tb2:
            ttitle, uniq, allhits, cls = tb2
            pts = topic_points(course, ttitle)
            if pts:
                route(course, vid, prov, [p["code"] for p in pts], "low",
                      f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} (all hits {allhits[:7]}) — topic points bound at the disclosed title-only bar")
                continue
        skip(prov, vid, t, "no distinctive-topic match at the df<=3 bar and no topic-unique token")
        continue

    # ---- 8291 EM ----
    if v["cluster"] == "em8291":
        course = "cie-as-environmental-management-20"
        if re.search(r"\b0680\b|igcse", t, re.I):
            skip(prov, vid, t, "IGCSE-register EM (0680) — out of AS 8291 lane scope; the IGCSE course is already covered (P11)")
            continue
        if re.search(r"preparation course|orientation", t, re.I) and not re.search(r"unit|topic|\d\.\d", t, re.I):
            skip(prov, vid, t, "generic course-preparation mention without topic content")
            continue
        tb2 = topic_by_unique_token(course, t)
        if tb2:
            ttitle, uniq, allhits, cls = tb2
            pts = topic_points(course, ttitle)
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar")
            continue
        skip(prov, vid, t, "no distinctive topic match at the df<=3 bar and no topic-unique token")
        continue

    # ---- 8021 GP ----
    if v["cluster"] == "gp8021":
        course = "cie-as-english-general-paper-21"
        if re.search(r"essay\b|comprehension|strategy|mistakes|tips|prepare|how (i|to)|overview|score|key points|breaking down|watch before", t, re.I):
            skip(prov, vid, t, "teacher-guidance/technique register — spine GP specs are topic lists, not skills; guidance excluded as bind target")
            continue
        # topic-list bind by normalized SUBSTRING of the spec title (no token degeneracy)
        tn = re.sub(r"[^a-z0-9 ]+", " ", t.lower())
        tn = re.sub(r"\s+", " ", tn).strip()
        hit = None
        for p in SP[course]["pts"]:
            pn = re.sub(r"[^a-z0-9 ]+", " ", (p["title"] or "").lower())
            pn = re.sub(r"\s+", " ", pn).strip()
            base = pn.replace(" continued", "").strip()
            if len(base) >= 10 and base in tn:
                hit = p
                break
        if hit:
            route(course, vid, prov, [hit["code"]], "medium",
                  f"title contains topic-list item {hit['code']} '{(hit['title'] or '')[:60]}' verbatim")
            continue
        skip(prov, vid, t, "no verbatim topic-list match (GP spine is topic lists — token binds are degenerate by construction)")
        continue

    # ---- 9609 business ----
    as_c, al_c = "cie-as-business-23", "cie-a-level-business-23"
    if re.search(r"\bigcse\b", t, re.I):
        skip(prov, vid, t, "IGCSE-register business title — out of AS/A lane scope (IGCSE business courses covered by P11)")
        continue
    if re.search(r"paper\s*[1234]\b.*(answer structure|survival|complete guide|exam technique)|exam technique|a\* in|chains of analysis", t, re.I):
        skip(prov, vid, t, "paper-technique/guidance register without session code — guidance excluded as bind target")
        continue
    if re.search(r"how (i|to)|study|award|advice|predict(ed|ion)?\b", t, re.I) and not re.search(r"9609/\d{2}", t):
        skip(prov, vid, t, "study-advice/prediction register without machine-checkable code")
        continue
    b = best_point(al_c, t)
    strategy = bool(re.search(r"strategy|external influences|\ba2\b", t, re.I))
    if b:
        p, hits, dmax, nh = b
        # route by topic family: A2 topics (6-10 in the A-level spine) -> a-level course
        tnum = 0
        for n in SP[al_c]["nodes"]:
            if n["family"] == "TOPIC":
                tnum += 1
            if n["code"] == p["code"]:
                break
        course = al_c if (tnum > 5 or strategy) else as_c
        conf = "medium" if sum(1 for w in hits if SP[al_c]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); {'A2/strategy register' if course == al_c else 'AS register'}")
        continue
    b = best_point(as_c, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if SP[as_c]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(as_c, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); AS register")
        continue
    skip(prov, vid, t, "no distinctive spec-token match at the df<=3 bar")

# ---------- outputs ----------
json.dump(tier_b, open(f"{WORK}/tier-b.json", "w"), indent=1)
json.dump(skips, open(f"{WORK}/skips.json", "w"), indent=1)
ta = {}
for course, rows in judgment.items():
    for r in rows:
        ta[r["id"]] = r
json.dump(ta, open(f"{WORK}/tier-a.json", "w"), indent=1)
json.dump(judgment, open(f"{WORK}/judgment.json", "w"), indent=1)

print("Tier B anchors:", len(tier_b))
for x in tier_b:
    print("   ", x["courses"][0], x["code"], "|", x["title"][:70])
for c, rows in judgment.items():
    conf = Counter(r["confidence"] for r in rows)
    print(f"{c}: routed {len(rows)} {dict(conf)}")
print("skips:", len(skips), "| routed total:", sum(len(v) for v in judgment.values()))
routed_ids = set(ta) | {x["id"] for x in tier_b}
print("disposition check: routed", len(routed_ids), "+ skips", len(skips), "= ", len(routed_ids) + len(skips), "vs pool", len(pool))
dup = [k for k, n in Counter([x['id'] for x in tier_b] + list(ta)).items() if n > 1]
print("exactly-once violations:", dup[:5] if dup else "none")
