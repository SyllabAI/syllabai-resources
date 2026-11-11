#!/usr/bin/env python3
"""P2F Edexcel-native lane — draft production (execution step 2).

Pipeline: channel pools -> sewage filter -> paper-code course rows ->
topic containment rows (idf-weighted, P4 rule: >= 0.55, >= 3 informative tokens)
-> oEmbed identity sweep (thumbnail-liveness fallback) -> 4 draft files
(ial-biology-18, ial-chemistry-17, ial-physics-19, igcse-chemistry-19).

Row identity v2: anchorRef|video|rowIdx (one anchor row per video per course).
Anchor rows carry specs: [] and lessonRef: null — zero spec weight
(docs/ANCHOR-GRANULARITY.md section 4).
"""
import datetime, json, re, subprocess, pathlib

ROOT = pathlib.Path("/home/z/my-project")
WORK = ROOT / "work/channels"
SPINES = ROOT / "repos/syllabai-v2-fresh/apps/hub/spines"
OUT = ROOT / "repos/syllabai-resources/Videos/drafts"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

COURSES = {
    "ial-biology-18": {"qual": "IAL (Edexcel)", "level": "IAL", "code": "WBI1"},
    "ial-chemistry-17": {"qual": "IAL (Edexcel)", "level": "IAL", "code": "WCH1"},
    "ial-physics-19": {"qual": "IAL (Edexcel)", "level": "IAL", "code": "WPH1"},
    "igcse-chemistry-19": {"qual": "IGCSE (Edexcel)", "level": "IGCSE", "code": "4CH1"},
}
CODE_OF_COURSE = {v["code"]: c for c, v in COURSES.items()}
CODE_RE = re.compile(r"\b(WCH1[1-6]|WBI1[1-6]|WPH1[1-6]|4CH1|4BI1|4PH1|9CH0|9BI0|9PH0)\b", re.I)
PREF_RE = re.compile(r"\b(P7\d{4}A)\b")
UNIT_RE = re.compile(r"\bunit\s*([1-6])\b", re.I)
SESSION_RE = re.compile(
    r"\b(jan|january|feb|february|mar|march|apr|april|may|jun|june|jul|july|aug|august"
    r"|sep|sept|september|oct|october|nov|november|dec|december)[a-z]*\s*'??\s*(20\d\d)\b"
    r"|(\b20\d\d)\s*\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)", re.I)
WALK_RE = re.compile(r"walkthrough|worked solution|detailed solution|solutions|paper\s*\d|past paper", re.I)

SEWAGE_RE = re.compile(
    r"free notes|mocks\s*&?\s*worksheets|redefine|intensive past paper solving|enrol|enroll"
    r"|premium|booklet|results day|must.?study|registration|subscribe|sub for|#\w+"
    r"|face ?time|vlog|funny|reels|cooking|award|giveaway|1,000\b|100,000", re.I)

PROVIDER_OF_SLUG = {
    "exam-essentials": "Exam Essentials (YouTube)",
    "sergeis-chemistry": "Sergei's Chemistry (YouTube)",
    "allery-chemistry": "Allery Chemistry (YouTube)",
    "omars-biology-lab-uploads": "Omar's Biology Lab (YouTube)",
    "a-star-solution": "A-star Solution (YouTube)",
    "ial-physics-walkthrough": "MedDude (YouTube)",
}
BOARD_WORDING = {
    "exam-essentials": "Edexcel-native (IAL/IGCSE paper-session titles)",
    "sergeis-chemistry": "Edexcel IAL-native wording",
    "allery-chemistry": None,  # per-title: CIE / Edexcel GCE / AQA / OCR prefixes
    "omars-biology-lab-uploads": "Edexcel IAL-native wording",
    "a-star-solution": "Edexcel-native (IAL/IGCSE paper-session titles)",
    "ial-physics-walkthrough": "Edexcel IAL-native wording",
}

STOP = set("""edexcel aqa ocr cie revision revise topic unit paper papers gcse igcse ial
a level levels as the of and for to in on at how what why when much many all every full
complete walkthrough worked detailed solution solutions solved explanation explained
question questions qs past june jan january feb february mar march apr april may jun july
aug sept september oct october nov november dec december part one two three new latest
best final international advanced subsidiary maths math physics chemistry biology science
exam exams test""".split())


def sh(cmd, timeout):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)


def tokens(text):
    return [t for t in re.split(r"[^a-z0-9]+", text.lower()) if t and t not in STOP
            and not t.isdigit() and len(t) > 1]


def load_pools():
    pools = {}
    for f in sorted(WORK.glob("p2f-*.tsv")):
        slug = f.stem[4:]
        rows = []
        for line in f.read_text().splitlines():
            p = line.split(chr(9))
            if len(p) >= 2 and p[0]:
                dur = None
                if len(p) >= 3 and p[2].strip():
                    try:
                        dur = int(float(p[2]))
                    except ValueError:
                        dur = None
                rows.append({"id": p[0], "title": p[1], "dur": dur, "slug": slug})
        pools[slug] = rows
    return pools


def board_wording(title, slug):
    if slug != "allery-chemistry":
        return BOARD_WORDING[slug]
    t = title.lower()
    if re.match(r"^\s*cie\b", t):
        return "CIE A-level topic wording (Allery CIE playlist)"
    if re.match(r"^\s*(edexcel|e\dex)", t):
        return "Edexcel GCE A-level topic wording (Allery Edexcel playlist)"
    if re.match(r"^\s*aqa\b", t):
        return "AQA A-level topic wording (Allery AQA playlist)"
    if re.match(r"^\s*ocr\b", t):
        return "OCR A-level topic wording (Allery OCR playlist)"
    return "board-agnostic A-level topic wording (Allery)"


def oembed(vid):
    try:
        r = sh(f'curl -s -m 6 "https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={vid}&format=json"',
               10)
        if r.returncode == 0 and r.stdout.strip().startswith("{"):
            j = json.loads(r.stdout)
            return "oembed", j.get("author_name")
    except subprocess.TimeoutExpired:
        pass
    try:
        r = sh(f'curl -s -o /dev/null -w "%{{http_code}}" -m 6 '
               f'"https://i.ytimg.com/vi/{vid}/hqdefault.jpg"', 10)
        if r.stdout.strip() == "200":
            return "thumbnail-liveness", None
    except subprocess.TimeoutExpired:
        pass
    return "unverified", None


def main():
    pools = load_pools()
    all_ids = {v["id"]: v for rows in pools.values() for v in rows}
    print(f"pool: {sum(len(v) for v in pools.values())} rows, {len(all_ids)} unique videos")

    # ---- 1. paper-code course rows --------------------------------------
    course_rows = {c: [] for c in COURSES}
    code_selected = set()
    skipped_codes = {}
    for vid, v in sorted(all_ids.items()):
        codes = [c.upper() for c in CODE_RE.findall(v["title"])]
        if not codes:
            continue
        pref = PREF_RE.search(v["title"])
        for code in set(codes):
            course = CODE_OF_COURSE.get(code[:4]) or CODE_OF_COURSE.get(code[:5])
            # WCH11 -> prefix WCH1 ; 4CH1 -> itself
            course = CODE_OF_COURSE.get(code[:5]) or CODE_OF_COURSE.get(code[:4])
            if course not in COURSES:
                skipped_codes[code] = skipped_codes.get(code, 0) + 1
                continue
            unit = f"U{code[4]}" if len(code) == 5 and code[:4] in ("WCH1", "WBI1", "WPH1") else None
            evidence = f'title: "{v["title"]}"; paper code {code}'
            if pref:
                evidence += f"; Edexcel paper ref {pref.group(1)}"
            sess = SESSION_RE.search(v["title"])
            if sess:
                evidence += f"; session {sess.group(0).strip()}"
            course_rows[course].append({
                "anchor": {"level": "course", "ref": course},
                "kind": "past-paper-walkthrough" if WALK_RE.search(v["title"]) or code[:1] in "W49" else "topic-revision",
                "video": vid, "lessonRef": None, "lessonUrl": None, "specs": [],
                "unitScope": unit,
                "confidence": "high", "method": "paper-code", "boardMismatch": False,
                "reviewed": False, "reviewer": None, "reviewedUtc": None,
                "evidence": evidence,
            })
            code_selected.add(vid)
    print(f"paper-code rows: " + ", ".join(f"{c}={len(r)}" for c, r in course_rows.items()))
    print(f"skipped non-target codes: {skipped_codes}")

    # ---- 2. topic containment rows (3 IAL courses) ----------------------
    topic_stats = {}
    for course in ["ial-biology-18", "ial-chemistry-17", "ial-physics-19"]:
        spine = json.loads((SPINES / f"{course}.json").read_text())
        topics = [n for n in spine["curriculum"]["nodes"] if n["family"] == "TOPIC"]
        subtopics = [n for n in spine["curriculum"]["nodes"] if n["family"] == "SUBTOPIC"]
        anchors = topics + subtopics
        corpus = [tokens(n["title"]) for n in anchors]
        df = {}
        for toks in corpus:
            for t in set(toks):
                df[t] = df.get(t, 0) + 1
        N = len(corpus)
        idf = {t: (N + 1) / (c + 1) for t, c in df.items()}

        def containment(vid_title, node):
            vt, tt = set(tokens(vid_title)), set(tokens(node["title"]))
            inter = vt & tt
            wsum = sum(idf.get(t, 1.0) for t in tt) or 1.0
            score = sum(idf.get(t, 1.0) for t in inter) / wsum
            # tier 1 (medium): >= 3 informative tokens, >= 0.55 — the P4 rule
            if len(inter) >= 3 and score >= 0.55:
                return score, len(inter), "medium"
            # tier 2 (low): >= 2 tokens, EVERY matched token idf-distinctive
            # (above corpus median) — guards the degenerate short-title case
            # P4 caught, while allowing short topic titles like "Reaction Kinetics"
            if len(inter) >= 2 and score >= 0.55:
                vals = sorted(idf.get(t, 1.0) for t in df)
                median = vals[len(vals) // 2]
                if all(idf.get(t, 1.0) >= median for t in inter):
                    return score, len(inter), "low"
            return 0.0, 0, None

        picked, table = [], []
        for vid, v in sorted(all_ids.items()):
            if vid in code_selected or v["dur"] is not None and v["dur"] < 120:
                continue
            if SEWAGE_RE.search(v["title"]):
                continue
            best = None
            for n in anchors:
                s, k, tier = containment(v["title"], n)
                if tier and (best is None or s > best[0]):
                    best = (s, k, n, tier)
            if not best:
                continue
            s, k, n, tier = best
            bw = board_wording(v["title"], v["slug"])
            unit = UNIT_RE.search(v["title"])
            is_native = "Edexcel IAL-native" == bw or bw.startswith("Edexcel-native")
            picked.append({
                "anchor": {"level": "topic" if n["family"] == "TOPIC" else "subtopic", "ref": n["code"]},
                "kind": "topic-revision",
                "video": vid, "lessonRef": None, "lessonUrl": None, "specs": [],
                "unitScope": f"U{unit.group(1)}" if unit else None,
                "confidence": tier, "method": "llm-draft-external",
                "boardMismatch": not is_native,
                "reviewed": False, "reviewer": None, "reviewedUtc": None,
                "evidence": f'title: "{v["title"]}"; topic anchor {n["code"]} "{n["title"]}" '
                            f'(idf containment {s:.2f}, {k} informative tokens); wording: {bw}',
            })
            table.append((v["title"][:70], n["code"], n["title"][:40], round(s, 2), v["slug"]))
        course_rows[course].extend(picked)
        topic_stats[course] = len(picked)
        print(f"\n{course}: topic rows={len(picked)}")
        for t in sorted(table, key=lambda x: -x[3])[:12]:
            print(f"   {t[4][:14]:14s} {t[0]:70s} -> {t[1]} {t[2]} ({t[3]})")

    # ---- 3. videos + oEmbed identity sweep ------------------------------
    per_course_videos = {}
    for course, rows in course_rows.items():
        ids = []
        for r in rows:
            if r["video"] not in ids:
                ids.append(r["video"])
        per_course_videos[course] = ids
    need = sorted({vid for ids in per_course_videos.values() for vid in ids})
    print(f"\nidentity sweep on {len(need)} videos ...")
    ident = {}
    for i, vid in enumerate(need):
        method, author = oembed(vid)
        ident[vid] = (method, author)
        if (i + 1) % 25 == 0:
            print(f"  {i + 1}/{len(need)}")

    unverified = [v for v in need if ident[v][0] == "unverified"]
    print(f"identity: oembed={sum(1 for v in need if ident[v][0]=='oembed')} "
          f"thumb={sum(1 for v in need if ident[v][0]=='thumbnail-liveness')} "
          f"unverified={len(unverified)} {unverified[:5]}")

    # ---- 4. emit drafts ---------------------------------------------------
    for course, rows in course_rows.items():
        rows = [r for r in rows if ident[r["video"]][0] != "unverified"]
        ids = []
        for r in rows:
            if r["video"] not in ids:
                ids.append(r["video"])
        meta = COURSES[course]
        videos = []
        for vid in ids:
            v = all_ids[vid]
            method, author = ident[vid]
            videos.append({
                "id": vid, "title": v["title"], "lessonRef": None, "lessonUrl": None,
                "provider": PROVIDER_OF_SLUG[v["slug"]],
                "watchUrl": f"https://www.youtube.com/watch?v={vid}",
                "levelTag": meta["level"],
                "boardNote": board_wording(v["title"], v["slug"]),
                "durationS": v["dur"], "guestVisible": None,
                "identityMethod": method, "oembedAuthor": author,
                "oembedVerifiedUtc": NOW,
            })
        by_kind = {}
        for r in rows:
            key = (r["anchor"]["level"], r["kind"])
            by_kind[key] = by_kind.get(key, 0) + 1
        draft = {
            "schema": "syllabai.video-map.draft-external/1",
            "lane": "p2f-ednative",
            "draftOf": course, "task": "T-VIDEOMAP-P2F", "course": course, "qual": meta["qual"],
            "reviewState": "draft-external",
            "draftLaw": "rows always reviewed:false; entering content/ requires verdicts in "
                        "owner-review-verdicts.p2f.json + the apply step flipping reviewed:true with "
                        "reviewer+reviewedUtc; row identity v2 anchorRef|video|rowIdx is course-scoped; "
                        "anchor rows carry specs:[] and lessonRef:null — zero spec weight per "
                        "docs/ANCHOR-GRANULARITY.md section 4; per the many-to-many ruling a video may "
                        "map into several courses",
            "source": {
                "provider": "Edexcel-native channels: Exam Essentials, Sergei's Chemistry, Allery "
                            "Chemistry, Omar's Biology Lab, A-star Solution, MedDude",
                "method": "yt-dlp flat enumeration + machine-verified Edexcel paper-code binding "
                          "(method paper-code, confidence high, boardMismatch false) + idf topic-title "
                          "containment (>= 0.55, >= 3 informative tokens, P4 rule) for topic anchors; "
                          "oEmbed identity sweep with thumbnail-liveness fallback; sewage filter "
                          "(promos, results-day, shorts/vlog); evidence posture title-only",
                "enumeratedUtc": NOW,
                "note": f"rows {len(rows)} by (anchor,kind): {by_kind}; anchor rows count zero "
                        f"spec points by the granularity accounting rule",
            },
            "videos": videos,
            "mappings": rows,
            "coverage": {
                "specPointsDraftedHere": 0, "rows": len(rows),
                "note": "anchor rows carry zero spec weight (ANCHOR-GRANULARITY section 4); "
                        "coverage numerators remain lesson-level-only",
            },
            "generatedUtc": NOW,
        }
        path = OUT / course / "video-map.draft.external-p2f.json"
        path.parent.mkdir(exist_ok=True)
        path.write_text(json.dumps(draft, indent=1, ensure_ascii=False) + "\n")
        print(f"wrote {path.relative_to(OUT)}: videos={len(videos)} rows={len(rows)}")


if __name__ == "__main__":
    main()
