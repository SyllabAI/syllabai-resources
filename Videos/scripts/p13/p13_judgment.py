#!/usr/bin/env python3
"""P13 judgment: route the 8-pool Alt Academy family (897 in-cluster candidates) onto
21 spine targets. Classes (the P12 law, extended per cluster):
  Tier B  paper-code anchors  — machine-checkable session/paper codes in titles
                                (method paper-code, confidence high, specs [], kind
                                past-paper-walkthrough, boardMismatch false)
  Class L  topic-complete lectures — full-topic lectures bind the topic's SPEC_POINTs
                                as ONE multi-spec row, confidence low (disclosed bar)
  Class M  section markers    — "N.M" titles bind that subtopic's points, confidence low
  Tier A  distinctive-token   — df<=3 token binds, confidence medium/low
  skips    honest ledger      — guidance/advice registers, O-Level register (census-out),
                                psychology no-target, meta, no-binding
Routing:
  chem/phys/bio  — title register routes AS ("AS Level") vs A-level; AS courses are
                   inherit children (cie-as-{chemistry,physics,biology}-25) -> P13B
  maths          — unit codes decide (P1/P2/P3/M1/S1/S2 + paper numbers); shared units
                   bind BOTH the AS and A-level course (one row per course)
  econ           — no AS economics course in the spine; all 9708 -> a-level-economics-23
  acct           — register routes as-accounting-21 (real course) vs a-level-accounting-21
  biz            — the P12 heuristic (A2 topic index > 5 or strategy register -> A-level)
  psych9990      — no spine course: honest no-target skip
"""
import json, os, re
from collections import Counter

WORK = "/home/z/my-project/work/p13"
HUB = "/home/z/my-project/repos/syllabai-v2-fresh/apps/hub/content"
UTC = "2026-11-14T15:40:00Z"

CHANNELS = ["alt-academy-main", "alt-academy-chemistry", "alt-academy-economics",
            "alt-academy-maths", "alt-academy-physics", "alt-academy-biology",
            "alt-academy-psychology", "alt-academy-accounting"]

P13 = {  # cluster -> [(course, is_p13b), ...]
    "chem9701": [("cie-a-level-chemistry-25", False), ("cie-as-chemistry-25", True)],
    "econ9708": [("cie-a-level-economics-23", False)],
    "maths9709": [("cie-a-level-maths-20-mechanics", False), ("cie-as-maths-20-mechanics", False),
                  ("cie-a-level-maths-20-probability-and-statistics-1", False), ("cie-as-maths-20-probability-and-statistics-1", False),
                  ("cie-a-level-maths-20-probability-and-statistics-2", False),
                  ("cie-a-level-maths-20-pure-1", False), ("cie-as-maths-20-pure-1", False),
                  ("cie-a-level-maths-20-pure-2", False), ("cie-as-maths-20-pure-2", False),
                  ("cie-a-level-maths-20-pure-3", False)],
    "phys9702": [("cie-a-level-physics-25", False), ("cie-as-physics-25", True)],
    "bio9700": [("cie-a-level-biology-25", False), ("cie-as-biology-25", True)],
    "acct9706": [("cie-a-level-accounting-21", False), ("cie-as-accounting-21", False)],
    "biz9609": [("cie-a-level-business-23", False), ("cie-as-business-23", False)],
    "psych9990": [],
}
COURSES = [c for cs in P13.values() for c, _ in cs]

STOP = set("""the a an of and or to in on for with your how what why when from as is are be
you i we they it its their our my this that these those at by not no do does using use
explained simply vs versus part guide tips tricks answer answering level as a2 igcse
cambridge international caie complete full everything need know revision exam exams
prepare preparation skill skills study lesson lectures lecture course class class-watcher
watch before september october november may june feb march oct nov jun may uk etc new
updated best top must topics topic questions question paper papers as-level solved
solution walkthrough selected crash practice problems problem basics intro introduction
introduction-to overview basic
chemistry physics biology maths math economics economic business accounting accounts
psychology 9701 9708 9709 9702 9700 9706 9609 9990
p1 p2 p3 m1 s1 s2""".split())

def toks(s):
    return [w for w in re.findall(r"[a-z0-9]+", s.lower()) if w not in STOP and len(w) > 2]

specs = {}
for course in COURSES:
    nodes = json.load(open(f"{HUB}/{course}/curriculum.json"))["nodes"]
    topic_of, cur = {}, None
    for n in nodes:
        if n["family"] == "TOPIC":
            cur = n["title"]
        topic_of[n["code"]] = cur
    pts = [n for n in nodes if n["family"] == "SPEC_POINT"]
    subs = [n for n in nodes if n["family"] == "SUBTOPIC"]
    df = Counter()
    for n in nodes:
        for w in set(toks(n["title"] or "")):
            df[w] += 1
    specs[course] = {"pts": pts, "subs": subs, "df": df, "nodes": nodes, "topic_of": topic_of}

TDF = {}
for course in COURSES:
    c = Counter()
    for n in specs[course]["nodes"]:
        if n["family"] in ("TOPIC", "SUBTOPIC"):
            for w in set(toks(n["title"] or "")):
                c[w] += 1
    TDF[course] = c

def sub_points(course, subcode):
    num = subcode.split(":")[-1].replace("SUB", "")
    return [p for p in specs[course]["pts"] if re.match(rf"^{re.escape(num)}\.\d+$", p["code"])]

def topic_points(course, topic_title):
    keep = [p for p in specs[course]["pts"] if specs[course]["topic_of"].get(p["code"]) == topic_title]
    return keep

def best_point(course, title, max_df=3):
    vt = set(toks(title))
    best, best_score = None, 0
    for p in specs[course]["pts"]:
        pt = set(toks(p["title"] or ""))
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

def section_by_field(course, title):
    """Alt Academy format: 'Topic | Section | register' — the middle field names the
    syllabus section. Bind when a pipe-field's STOP-stripped norm EQUALS a TOPIC or
    SUBTOPIC title's norm (SUBTOPIC preferred, node norm len >= 8 chars).
    Returns (node, points) or None."""
    fields = [norm_stop(f) for f in title.split("|") if f.strip()]
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
    vt = set(toks(title))
    vt_stripped = " " + " ".join(re.findall(r"[a-z0-9]+", title.lower())) + " "
    tdf = {}
    for n in specs[course]["nodes"]:
        if n["family"] == "TOPIC":
            for w in set(toks(n["title"] or "")):
                tdf[w] = tdf.get(w, 0) + 1
    best = None
    for n in specs[course]["nodes"]:
        if n["family"] != "TOPIC":
            continue
        tset = set(toks(n["title"] or ""))
        subtoks, seen = set(), False
        for m in specs[course]["nodes"]:
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

# ---------------- pools ----------------
pool = []
_seen_pool = set()
for slug in CHANNELS:
    for v in json.load(open(f"{WORK}/inl-{slug}.json")):
        if v["id"] in _seen_pool:
            continue  # YouTube upload enumerations can repeat a video row
        _seen_pool.add(v["id"])
        pool.append({**v, "provider": slug})

tier_b, skips = [], []
judgment = {c: [] for c in COURSES}

def skip(provider, vid, title, reason):
    skips.append({"video": vid, "title": title, "provider": provider, "reason": reason})

def route(course, vid, provider, specs_list, confidence, reason, p13b=False):
    judgment[course].append({"id": vid, "provider": provider, "action": "keep",
                             "specs": specs_list, "confidence": confidence, "reason": reason,
                             "p13b": p13b})

# ---------------- guidance / advice / meta registers ----------------
RE_GUIDE = re.compile(
    r"tips|tricks?\b|ace your|how to (ace|finish|overcome|stop|prepare|revise)|how (do i|this student)|"
    r"survival guide|preparation course|orientation|watch (this|before)|podcast|success|result day|"
    r"interview|vision|challenge|parents? of|update|tour|platform|worried|nervous|resit|message|"
    r"days? left|30 days|60 days|join now|score an a\*|a\* in|game.?chang|blended|covid|urdu|hindi|"
    r"studysmart|aitutor|revision in|month left|marking schemes|what you (need|can)|can't miss|"
    r"paper breakdown|important topics|fix of|lifesaver|one thing|stress|focus on what", re.I)

def is_guidance(title, has_code):
    if RE_GUIDE.search(title):
        # code-bearing walkthroughs keep their machine-checkable route
        if has_code and re.search(r"solved|solution|walkthrough|selected questions|crash course|Q\s?\d", title, re.I):
            return False
        if has_code and re.search(r"\d{1,2}\.\d{1,2}", title):
            return False
        return True
    return False

def has_code(title):
    return bool(re.search(r"\b(9701|9708|9709|9702|9700|9706|9609|9990)\b", title))

# ---------------- Tier B: machine-checkable session/paper codes ----------------
SESS = re.compile(r"(may\s*[/ ]?\s*june|oct(?:ober)?\s*[/ -]?\s*nov(?:ember)?|feb(?:ruary)?\s*[/ -]?\s*march|\b(jan|jun|nov)\s*20\d\d|20\d\d\s*(jan|jun|nov)|m/j|o/n\s*20\d\d|20\d\d\s*m/j|20\d\d\s*o/n)", re.I)
PAPER = re.compile(r"\bpaper\s*(\d{1,2})\b|\bP(\d{1,2})\b(?=[\s,]|$)", re.I)

def paper_num(title):
    m = PAPER.search(title)
    if not m:
        return None
    raw = int(m.group(1) or m.group(2))
    if 1 <= raw <= 6:
        return raw
    if 11 <= raw <= 66 and raw % 10 in (1, 2, 3):
        return raw // 10  # CIE two-digit "Paper 53" = paper 5 variant 3
    return None

def tb_route(cluster, n, title):
    """Tier B course routing by paper number. Returns list of (course, p13b)."""
    if cluster == "maths9709":
        u = {1: [("cie-a-level-maths-20-pure-1", False), ("cie-as-maths-20-pure-1", False)],
             2: [("cie-a-level-maths-20-pure-2", False), ("cie-as-maths-20-pure-2", False)],
             3: [("cie-a-level-maths-20-pure-3", False)],
             4: [("cie-a-level-maths-20-mechanics", False), ("cie-as-maths-20-mechanics", False)],
             5: [("cie-a-level-maths-20-probability-and-statistics-1", False), ("cie-as-maths-20-probability-and-statistics-1", False)],
             6: [("cie-a-level-maths-20-probability-and-statistics-2", False)]}
        return u.get(n, [])
    if cluster == "biz9609":
        return [("cie-as-business-23", False)] if n in (1, 2) else ([("cie-a-level-business-23", False)] if n in (3, 4) else [])
    if cluster == "econ9708":
        return [("cie-a-level-economics-23", False)] if n in (1, 2, 3, 4) else []
    if cluster == "chem9701":
        if n in (1, 2):
            return [("cie-as-chemistry-25", True)]
        if n in (4, 5):
            return [("cie-a-level-chemistry-25", False)]
        return []
    if cluster == "phys9702":
        if n in (1, 2, 3):
            return [("cie-as-physics-25", True)]
        if n in (4, 5):
            return [("cie-a-level-physics-25", False)]
        return []
    if cluster == "bio9700":
        if n in (1, 2, 3):
            return [("cie-as-biology-25", True)]
        if n in (4, 5):
            return [("cie-a-level-biology-25", False)]
        return []
    if cluster == "acct9706":
        if n in (1, 2):
            return [("cie-as-accounting-21", False)]
        if n == 3:
            return [("cie-a-level-accounting-21", False)]
        return []
    return []

for v in pool:
    t = v["title"]
    prov = v["provider"]
    bs = set(v["buckets"])
    code = has_code(t)
    n = paper_num(t)
    # Tier B: code-bearing session/paper walkthroughs
    if code and n and SESS.search(t) and re.search(r"solved|solution|walkthrough|selected questions|crash course|Q\s?\d+", t, re.I):
        courses = []
        for cl in ("maths9709", "biz9609", "econ9708", "chem9701", "phys9702", "bio9700", "acct9706"):
            if cl in bs:
                courses = tb_route(cl, n, t)
                if courses:
                    break
        if courses:
            for course, p13b in courses:
                tier_b.append({"id": v["id"], "title": t, "provider": prov,
                               "courses": [course], "p13b": p13b,
                               "code": f"paper {n} + session '{SESS.search(t).group(0)}'",
                               "kind": "past-paper-walkthrough"})
            continue

tb_ids = {x["id"] for x in tier_b}

# ---------------- Tier A / class rows ----------------
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

def bind_course(course, vid, prov, t, p13b=False):
    """the P12 gate ladder + the P13 section-name gate on one course; returns True if routed."""
    sm = section_marker(course, t)
    if sm:
        num, sub, pts = sm
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-marker narrowing: title names section {num} '{sub['title'][:60]}' — section points bound at the disclosed higher title-only bar", p13b)
        return True
    sg = section_by_field(course, t)
    if sg:
        node, pts = sg
        route(course, vid, prov, [p["code"] for p in pts], "low",
              f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p13b)
        return True
    b = best_point(course, t)
    if b:
        p, hits, dmax, nh = b
        conf = "medium" if sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3) >= 2 else "low"
        route(course, vid, prov, [p["code"]], conf,
              f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p13b)
        return True
    tb2 = topic_by_unique_token(course, t)
    if tb2:
        ttitle, uniq, allhits, cls = tb2
        pts = topic_points(course, ttitle)
        if pts:
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"topic-complete lecture ({cls}): title names topic '{ttitle[:60]}' via topic-unique token(s) {uniq[:5]} — topic points bound at the disclosed title-only bar", p13b)
            return True
    return False

RE_AS_REG = re.compile(r"\bAS\s+Level\b|\bAS\s+Chem(istry)?\b|\bAS\s+Physic|\bAS\s+Biolog|\bAS\s+Account|\bAS\s+Econom|\bAS\s+Math", re.I)

# unit tokens for maths routing
RE_UNIT = {"S2": re.compile(r"\bS2\b"), "S1": re.compile(r"\bS1\b"), "M1": re.compile(r"\bM1\b"),
           "P3": re.compile(r"\bP3\b"), "P2": re.compile(r"\bP2\b"), "P1": re.compile(r"\bP1\b")}
UNIT_COURSES = {
    "S2": [("cie-a-level-maths-20-probability-and-statistics-2", False)],
    "S1": [("cie-a-level-maths-20-probability-and-statistics-1", False), ("cie-as-maths-20-probability-and-statistics-1", False)],
    "M1": [("cie-a-level-maths-20-mechanics", False), ("cie-as-maths-20-mechanics", False)],
    "P3": [("cie-a-level-maths-20-pure-3", False)],
    "P2": [("cie-a-level-maths-20-pure-2", False), ("cie-as-maths-20-pure-2", False)],
    "P1": [("cie-a-level-maths-20-pure-1", False), ("cie-as-maths-20-pure-1", False)],
}

seen_rows = set()  # (course, vid) dedup

for v in pool:
    vid, t, prov = v["id"], v["title"], v["provider"]
    if vid in tb_ids:
        continue
    bs = set(v["buckets"])
    if is_guidance(t, has_code(t)):
        skip(prov, vid, t, "teacher-guidance/advice/marketing register — excluded as bind target")
        continue

    # ---- psychology no-target ----
    if "psych9990" in bs:
        skip(prov, vid, t, "CIE 9990 psychology — no psychology course exists in the spine (honest no-target)")
        continue

    # ---- maths by unit tokens ----
    if "maths9709" in bs:
        unit = None
        for u, rx in RE_UNIT.items():
            if rx.search(t):
                unit = u
                break
        ok = False
        if unit:
            for course, p13b in UNIT_COURSES[unit]:
                if (course, vid) in seen_rows:
                    continue
                if bind_course(course, vid, prov, t, p13b):
                    seen_rows.add((course, vid))
                    ok = True
            if ok:
                continue
        else:
            best = None
            sec_hits = []
            for course, p13b in P13["maths9709"]:
                sg = section_by_field(course, t)
                if sg:
                    sec_hits.append((course, p13b, sg))
                    continue
                b = best_point(course, t)
                if b:
                    p, hits, dmax, nh = b
                    dist = sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3)
                    cand = (dist, -dmax, course)
                    if best is None or cand > best[0]:
                        best = (cand, course, p13b, p, hits, dmax)
            if sec_hits:
                for course, p13b, (node, pts) in sec_hits[:2]:  # cap 2 courses per video
                    route(course, vid, prov, [p["code"] for p in pts], "low",
                          f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar", p13b)
                continue
            if best and best[0][0] >= 2:
                _, course, p13b, p, hits, dmax = best
                conf = "medium" if best[0][0] >= 2 else "low"
                route(course, vid, prov, [p["code"]], conf,
                      f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); unit inferred cross-course", p13b)
                continue
        if not ok:
            skip(prov, vid, t, "maths title without unit tokens and no cross-course distinctive match at the df<=3 bar")
            continue

    # ---- chemistry by register ----
    if "chem9701" in bs:
        as_reg = bool(RE_AS_REG.search(t))
        course, p13b = ("cie-as-chemistry-25", True) if as_reg else ("cie-a-level-chemistry-25", False)
        if bind_course(course, vid, prov, t, p13b):
            continue
        skip(prov, vid, t, "no distinctive chemistry match at the df<=3 bar and no topic-unique token")
        continue

    # ---- physics by register ----
    if "phys9702" in bs:
        as_reg = bool(RE_AS_REG.search(t))
        course, p13b = ("cie-as-physics-25", True) if as_reg else ("cie-a-level-physics-25", False)
        if bind_course(course, vid, prov, t, p13b):
            continue
        skip(prov, vid, t, "no distinctive physics match at the df<=3 bar and no topic-unique token")
        continue

    # ---- biology by register ----
    if "bio9700" in bs:
        as_reg = bool(RE_AS_REG.search(t))
        course, p13b = ("cie-as-biology-25", True) if as_reg else ("cie-a-level-biology-25", False)
        if bind_course(course, vid, prov, t, p13b):
            continue
        skip(prov, vid, t, "no distinctive biology match at the df<=3 bar and no topic-unique token")
        continue

    # ---- economics (A-level only) ----
    if "econ9708" in bs:
        if bind_course("cie-a-level-economics-23", vid, prov, t, False):
            continue
        skip(prov, vid, t, "no distinctive economics match at the df<=3 bar and no topic-unique token")
        continue

    # ---- accounting by register ----
    if "acct9706" in bs:
        as_reg = bool(RE_AS_REG.search(t))
        course = "cie-as-accounting-21" if as_reg else "cie-a-level-accounting-21"
        if bind_course(course, vid, prov, t, False):
            continue
        # try the other register's course before skipping (mislabelled registers happen)
        other = "cie-a-level-accounting-21" if as_reg else "cie-as-accounting-21"
        if bind_course(other, vid, prov, t, False):
            continue
        skip(prov, vid, t, "no distinctive accounting match at the df<=3 bar and no topic-unique token")
        continue

    # ---- business (the P12 heuristic + the section-name gate) ----
    if "biz9609" in bs:
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
            course = al_c if (tnum > 5 or node["family"] == "SUBTOPIC" and tnum > 5) else as_c
            route(course, vid, prov, [p["code"] for p in pts], "low",
                  f"section-name binding (verbatim field match): title field names {node['family'].lower()} '{node['title'][:60]}' — section points bound at the disclosed title-only bar; {'A2 register' if course == al_c else 'AS register'}", False)
            continue
        b = best_point(al_c, t)
        strategy = bool(re.search(r"strategy|external influences|\ba2\b", t, re.I))
        if b:
            p, hits, dmax, nh = b
            tnum = 0
            for nd in specs[al_c]["nodes"]:
                if nd["family"] == "TOPIC":
                    tnum += 1
                if nd["code"] == p["code"]:
                    break
            course = al_c if (tnum > 5 or strategy) else as_c
            conf = "medium" if sum(1 for w in hits if specs[al_c]["df"].get(w, 99) <= 3) >= 2 else "low"
            route(course, vid, prov, [p["code"]], conf,
                  f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); {'A2/strategy register' if course == al_c else 'AS register'}", False)
            continue
        b = best_point(as_c, t)
        if b:
            p, hits, dmax, nh = b
            conf = "medium" if sum(1 for w in hits if specs[as_c]["df"].get(w, 99) <= 3) >= 2 else "low"
            route(as_c, vid, prov, [p["code"]], conf,
                  f"title names {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax}); AS register", False)
            continue
        skip(prov, vid, t, "no distinctive business spec-token match at the df<=3 bar")
        continue

    # ---- terse (level phrase but no subject word): cross-cluster distinctive matcher ----
    if "terse" in bs:
        best = None
        for cl, courses in P13.items():
            if not courses or cl == "psych9990":
                continue
            for course, p13b in courses:
                b = best_point(course, t)
                if b:
                    p, hits, dmax, nh = b
                    dist = sum(1 for w in hits if specs[course]["df"].get(w, 99) <= 3)
                    cand = (dist, -dmax, course)
                    if best is None or cand > best[0]:
                        best = (cand, course, p13b, p, hits, dmax)
        if best and best[0][0] >= 2:
            _, course, p13b, p, hits, dmax = best
            route(course, vid, prov, [p["code"]], "low",
                  f"terse register title; cross-cluster distinctive match {p['code']} '{p['title'][:60]}' via token(s) {hits[:5]} (df {dmax})", p13b)
            continue
        skip(prov, vid, t, "terse register title with no unambiguous cross-cluster distinctive match")
        continue

    skip(prov, vid, t, "no cluster binding at the df<=3 bar")

# ---------------- re-adjudication (the review layer) ----------------
# Degenerate binds found on review are demoted to honest skips:
#  1. wkgmdRfd-44 — S2 title bound to 6.5.1 via generic tokens ['between','two'] only
#  2. 37C0JfDSheY — terse "Pricing strategies Short term" bound to 5.1.1 business finance
#     via generic tokens ['short','term']; the honest pricing-strategy spec match failed
#     on morphology (strategies vs strategy) — a generic-token bind is not evidence
READJUDICATE = {
    "wkgmdRfd-44": "degenerate bind re-adjudicated to skip on review: only evidence tokens were generic ('between','two') — the title carries no distinctive hypothesis-test tokens",
    "37C0JfDSheY": "degenerate bind re-adjudicated to skip on review: terse title matched business-finance spec via generic tokens ('short','term'); the honest pricing-strategy match fails on strategies/strategy morphology — a generic-token bind is not evidence",
}
for vid, why in READJUDICATE.items():
    removed = False
    for course, rows in judgment.items():
        keep = []
        for r in rows:
            if r["id"] == vid and not removed:
                removed = True
                skip("alt-academy-family", vid, r["reason"][:100], why)
                continue
            keep.append(r)
        judgment[course] = keep

# ---------------- outputs ----------------
json.dump(tier_b, open(f"{WORK}/tier-b.json", "w"), indent=1, ensure_ascii=False)
json.dump(skips, open(f"{WORK}/skips.json", "w"), indent=1, ensure_ascii=False)
ta = {}
for course, rows in judgment.items():
    for r in rows:
        ta[r["id"]] = r
json.dump(ta, open(f"{WORK}/tier-a.json", "w"), indent=1, ensure_ascii=False)
json.dump(judgment, open(f"{WORK}/judgment.json", "w"), indent=1, ensure_ascii=False)

print("Tier B anchors:", len(tier_b))
for c, rows in sorted(judgment.items()):
    conf = Counter(r["confidence"] for r in rows)
    b = sum(1 for r in rows if r.get("p13b"))
    print(f"{c}: routed {len(rows)} {dict(conf)} p13b-rows {b}")
print("skips:", len(skips), "| routed total:", sum(len(v) for v in judgment.values()))
routed_ids = set(ta) | {x["id"] for x in tier_b}
print("disposition check: routed", len(routed_ids), "+ skips", len(skips), "=", len(routed_ids) + len(skips), "vs pool", len(pool))
dup = [k for k, n in Counter([x["id"] for x in tier_b] + list(ta)).items() if n > 1]
print("exactly-once violations:", dup[:5] if dup else "none")
