#!/usr/bin/env python3
"""P2F execution step 3: delegated self-review + verdicts + apply.

Standing ruling (owner chat 2026-11-09 'approve and review yourself'; owner chat
2026-11-12 'Go'). Programmatic re-verification of every emitted row, plus an
oEmbed-author cross-check against the claimed provider channel. Rejects are
written into owner-review-verdicts.p2f.json; approved rows flip reviewed:true;
reviewState becomes owner-reviewed-external. Review file:
drafts/review-file-external-p2f.md.
"""
import datetime, json, re, pathlib

ROOT = pathlib.Path("/home/z/my-project")
OUT = ROOT / "repos/syllabai-resources/Videos/drafts"
NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

COURSES = ["ial-biology-18", "ial-chemistry-17", "ial-physics-19", "igcse-chemistry-19"]
CODE_OF_COURSE = {"ial-biology-18": "WBI1", "ial-chemistry-17": "WCH1",
                  "ial-physics-19": "WPH1", "igcse-chemistry-19": "4CH1"}
CODE_RE = re.compile(r"\b(WCH1[1-6]|WBI1[1-6]|WPH1[1-6]|4CH1|4BI1|4PH1|9CH0|9BI0|9PH0)\b", re.I)
SEWAGE_RE = re.compile(
    r"free notes|mocks\s*&?\s*worksheets|redefine|intensive past paper solving|enrol|enroll"
    r"|premium|booklet|results day|must.?study|registration|subscribe|sub for|#\w+"
    r"|face ?time|vlog|funny|reels|cooking|award|giveaway", re.I)
AUTHOR_OF_PROVIDER = {
    "Exam Essentials (YouTube)": "Exam Essentials",
    "Sergei's Chemistry (YouTube)": "Sergei",
    "Allery Chemistry (YouTube)": "Allery",
    "Omar's Biology Lab (YouTube)": "Omar",
    "A-star Solution (YouTube)": "A-star",
    "MedDude (YouTube)": "MedDude",
}

REJECTS = {  # judgment rejects after row-by-row pass (empty = none)
}


def main():
    summary = {}
    for course in COURSES:
        dpath = OUT / course / "video-map.draft.external-p2f.json"
        draft = json.loads(dpath.read_text())
        vbyid = {v["id"]: v for v in draft["videos"]}
        problems, rejects = [], []
        seen_video = set()
        for m in draft["mappings"]:
            vid = m["video"]
            v = vbyid.get(vid)
            if v is None:
                problems.append(f"row references unknown video {vid}")
                continue
            if vid in seen_video:
                problems.append(f"duplicate p2f row for video {vid} in {course}")
            seen_video.add(vid)
            # anchor invariants
            a = m.get("anchor")
            if not a or a.get("level") not in ("course", "topic", "subtopic", "subject"):
                problems.append(f"{vid}: missing/bad anchor")
            elif a["level"] == "course" and a["ref"] != course:
                problems.append(f"{vid}: course anchor ref {a['ref']} != {course}")
            elif a["level"] in ("topic", "subtopic") and (m["specs"] or m["lessonRef"] is not None):
                problems.append(f"{vid}: topic anchor must carry specs:[] and lessonRef:null")
            # identity
            if v.get("identityMethod") not in ("oembed", "thumbnail-liveness"):
                problems.append(f"{vid}: identity unverified")
            author = (v.get("oembedAuthor") or "").lower()
            expect = AUTHOR_OF_PROVIDER.get(v.get("provider"), "").lower()
            if expect and expect.split()[0] not in author:
                problems.append(f"{vid}: oEmbed author '{v.get('oembedAuthor')}' "
                                f"does not match provider '{v.get('provider')}'")
            # sewage
            if SEWAGE_RE.search(v.get("title", "")):
                problems.append(f"{vid}: sewage pattern in title '{v['title'][:60]}'")
            # paper-code rows: re-verify the code is in the title
            if m["method"] == "paper-code":
                code = CODE_OF_COURSE[course]
                codes = [c.upper() for c in CODE_RE.findall(v.get("title", ""))]
                ok = any(c[:4] == code or (code == "4CH1" and c == "4CH1") for c in codes)
                if not ok:
                    problems.append(f"{vid}: paper-code row but {code} not in title")
                if m["confidence"] != "high" or m["boardMismatch"] is not False:
                    problems.append(f"{vid}: paper-code row must be high/false")
            # topic rows: containment evidence present, boardMismatch consistent
            if a and a["level"] in ("topic", "subtopic"):
                if "idf containment" not in m.get("evidence", ""):
                    problems.append(f"{vid}: topic row missing containment evidence")
                if m["confidence"] not in ("medium", "low"):
                    problems.append(f"{vid}: topic row confidence {m['confidence']}")
            if not isinstance(m.get("boardMismatch"), bool):
                problems.append(f"{vid}: boardMismatch must be boolean")
        rejects = list(REJECTS.get(course, []))
        verdicts = {
            "task": "T-VIDEOMAP-P2F", "ruledUtc": NOW,
            "source": "delegated self-review per owner chat 2026-11-09 'approve and review "
                      "yourself' (standing ruling); owner chat 2026-11-12 'Go'",
            "reviewer": "delegated-self-review",
            "evidenceBasis": "title-only; paper codes machine-verified against Edexcel code "
                             "grammar (re-checked at review); oEmbed identity sweep 100% with "
                             "author-vs-provider cross-check; topic anchors via idf title-token "
                             "containment (tier 1 >= 3 tokens >= 0.55 medium; tier 2 >= 2 "
                             "idf-distinctive tokens low); sewage filter re-scanned at review",
            "rejects": rejects,
        }
        if problems:
            verdicts["rejects"] = rejects + [{"video": p.split(":")[0], "reason": p}
                                             for p in problems]
        (OUT / course / "owner-review-verdicts.p2f.json").write_text(
            json.dumps(verdicts, indent=1, ensure_ascii=False) + "\n")
        # apply: flip approved rows
        rej_vids = {r["video"] for r in verdicts["rejects"]}
        approved = 0
        for m in draft["mappings"]:
            if m["video"] not in rej_vids and not problems:
                m["reviewed"] = True
                m["reviewer"] = "delegated-self-review"
                m["reviewedUtc"] = NOW
                approved += 1
        if not problems:
            draft["reviewState"] = "owner-reviewed-external"
            draft["reviewedUtc"] = NOW
        draft["coverage"]["rows"] = len(draft["mappings"])
        dpath.write_text(json.dumps(draft, indent=1, ensure_ascii=False) + "\n")
        summary[course] = {
            "rows": len(draft["mappings"]), "approved": approved,
            "rejected": len(verdicts["rejects"]), "problems": problems,
        }
        print(f"{course}: rows={len(draft['mappings'])} approved={approved} "
              f"rejected={len(verdicts['rejects'])} problems={problems[:3]}")
    print(json.dumps({c: {"approved": s["approved"], "rejected": s["rejected"]}
                      for c, s in summary.items()}))


if __name__ == "__main__":
    main()
