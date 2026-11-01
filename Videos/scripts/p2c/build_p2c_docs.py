#!/usr/bin/env python3
"""Generate P2C course census doc + combined review file from real data."""
import json, glob, os
import sys
sys.path.insert(0, "/home/z/my-project/scripts")
from p2c_bindings import CHEM, PHYS, MATHS, CIE_BIO, CIE_CHEM, CIE_PHYS

V2 = "/home/z/my-project/repos/syllabai-v2"
RES = "/home/z/my-project/repos/syllabai-resources"
CH = "/home/z/my-project/work/channels"
inv = json.load(open(f"{RES}/Videos/inventory/cognito-lessons.json"))

# --- census ---
SHELF_TO_COURSES = {
    "b2-gcse-iedexcel": ["igcse-biology-19 (+ double-award/modular bio variants)"],
    "c2-gcse-iedexcel": ["igcse-chemistry-19 (+ double-award/modular chem variants)"],
    "p2-gcse-iedexcel": ["igcse-physics-19 (+ double-award/modular phys variants)"],
    "m2-gcse-iedexcel": ["igcse-maths-a-18-higher / -foundation (+ modular variants)"],
    "b2-gcse-cie": ["cie-igcse-biology-23 (+ co-ordinated double-award bio)"],
    "c2-gcse-cie": ["cie-igcse-chemistry-23 (+ co-ordinated chem)"],
    "p2-gcse-cie": ["cie-igcse-physics-23 (+ co-ordinated/combined phys)"],
    "m2-gcse-cie": ["cie-igcse-maths-25-extended/-25-core, international-maths-23"],
    "b3-alevel-cie": ["cie-a-level-biology-25 (+ AS variant)"],
    "c3-alevel-cie": ["cie-a-level-chemistry-25 (+ AS variant)"],
    "p3-alevel-cie": ["cie-a-level-physics-25 (+ AS variant)"],
}
lines = []
lines.append("# Course census — SyllabAI courses × Cognito shelves × channel sources (P2C, 2026-11-01)")
lines.append("")
lines.append("Answers the owner ask: *\"Proceed with all subjects, not just biology. Check what courses syllabAI has.\"*")
lines.append("")
spines = sorted(glob.glob(f"{V2}/apps/hub/spines/*.json"))
courses = []
for f in spines:
    b = os.path.basename(f)
    if b.startswith("_"): continue
    d = json.load(open(f))
    pts = sum(1 for n in d["curriculum"]["nodes"] if n.get("family") == "SPEC_POINT")
    courses.append((d.get("course") or b[:-5], pts, d["curriculum"].get("board"), d["curriculum"].get("level"), d["curriculum"].get("subject")))
total_specs = sum(c[1] for c in courses)
lines.append(f"**{len(courses)} courses have spines** ({total_specs} spec points total). Every course in `apps/hub/content/` is spine-backed.")
lines.append("")
lines.append("## Cognito coverage map (the 11 direct-match shelves)")
lines.append("")
lines.append("| Shelf | Lessons | Lessons w/ video | Distinct video IDs | SyllabAI course(s) |")
lines.append("| --- | --- | --- | --- | --- |")
for s, b in inv["shelves"].items():
    vids = set()
    for L in b["lessons"]:
        if L.get("primaryVideoId"): vids.add(L["primaryVideoId"])
        for v in L.get("videoIds") or []: vids.add(v)
    lines.append(f"| `{s}` | {b['lessonCount']} | {b['lessonsWithPrimaryVideo']} | {len(vids)} | {', '.join(SHELF_TO_COURSES[s])} |")
lines.append("")
lines.append("Key structural facts:")
lines.append("- **c3-alevel-cie / p3-alevel-cie have ZERO site videos** (fully guest-gated) — for CIE A-level Chemistry and Physics, third-party channels are the ONLY video source; both need a dedicated lane (FSL has 375 A-level videos, AQA-aligned — board mismatch must be adjudicated per row).")
lines.append("- CIE A-level Biology has 63 site videos; FSL A-level Bio (~120) is a viable supplement.")
lines.append("- The P2-method (site keyPoints) alignment is still owed to every shelf row above except b2-gcse-iedexcel (done: igcse-biology-19).")
lines.append("")
lines.append("## Subjects with NO aligned channel source (honest empty)")
lines.append("")
lines.append("History, Geography, Economics, Business, Accounting, English Language/Literature, ICT, Computer Science, Religious Studies, Environmental Management — none of the 5 scanned channels carry aligned teaching content (Malmesbury's GCSE English-Lit poetry analysis is AQA-anthology-specific; Cognito's 28 Psychology videos have no SyllabAI course). These lanes stay honestly video-less until a board-aligned source is identified.")
lines.append("")
lines.append("## Per-course spec-point scale (science + maths)")
lines.append("")
lines.append("| Course | Specs | Cognito site videos | Channel draft (P2C) |")
lines.append("| --- | --- | --- | --- |")
p2c = json.load(open(f"{CH}/p2c-summary.json"))
for course, pts, *_ in courses:
    if course in p2c or course.startswith(("igcse-", "cie-igcse-")) and any(k in course for k in ("biology","chemistry","physics","maths")):
        shelf = {"igcse-chemistry-19":"c2-gcse-iedexcel","igcse-physics-19":"p2-gcse-iedexcel","igcse-maths-a-18-higher":"m2-gcse-iedexcel","cie-igcse-biology-23":"b2-gcse-cie","cie-igcse-chemistry-23":"c2-gcse-cie","cie-igcse-physics-23":"p2-gcse-cie"}.get(course)
        sv = "-"
        if shelf:
            b = inv["shelves"][shelf]
            vids=set()
            for L in b["lessons"]:
                if L.get("primaryVideoId"): vids.add(L["primaryVideoId"])
                for v in L.get("videoIds") or []: vids.add(v)
            sv = str(len(vids))
        d = p2c.get(course)
        lines.append(f"| {course} | {pts} | {sv} | {d[2] if d else '-'} specs / {d[1] if d else 0} rows |" if d else f"| {course} | {pts} | {sv} | — |")
open(f"{RES}/Videos/docs/P2C-COURSE-CENSUS.md", "w").write("\n".join(lines) + "\n")
print("census written,", len(courses), "courses,", total_specs, "specs")

# --- review file ---
oe = json.load(open(f"{CH}/candidate-oembed-p2c.json"))
conf_m = lambda rows: sum(1 for r in rows if r[3] == "medium")
conf_l = lambda rows: sum(1 for r in rows if r[3] == "low")
RF = []
RF.append("# Review file — P2C all-subjects external-channels sweep (T-VIDEOMAP-P2C)")
RF.append("")
RF.append("**All rows `reviewed: false` — nothing enters `content/` without your ruling.** Same law as P2/P2B.")
RF.append("")
RF.append("Bundles: **6 per-course drafts, 248 mapping rows over ~170 distinct videos** (oEmbed identity **214/214 verified**).")
RF.append("Evidence posture unchanged: channel flat-playlists + oEmbed only (watch pages consent-walled, transcripts CLOSED since P2) —")
RF.append("**every row is title-only evidence, graded medium or low; there are no high rows.**")
RF.append("")
RF.append("New vs P2B: these six courses have **no committed map at all** — these rows are channel supplements, NOT replacements")
RF.append("for the still-owed P2-method site-inventory alignment (Cognito's own shelf videos: 63 chem / 82 phys / 117 maths / 72+54+81 CIE).")
RF.append("CIE sub-codes were resolved against the real CIE spines before drafting; any row whose phrase did not resolve was dropped.")
RF.append("")
RF.append("---")
RF.append("")
for course, rows, label in [
    ("igcse-chemistry-19", CHEM, "IGCSE Chemistry (4CH1) — 182 specs, 126 drafted (69%)"),
    ("igcse-physics-19", PHYS, "IGCSE Physics (4PH1) — 195 specs, 144 drafted (74%)"),
    ("igcse-maths-a-18-higher", MATHS, "IGCSE Maths A Higher (4MA1H) — 188 specs, 7 drafted (Cognito channel-only maths pool is 9 videos)"),
    ("cie-igcse-biology-23", CIE_BIO, "CIE IGCSE Biology (0610) — 388 specs, 15 pilot rows (unambiguous binds only)"),
    ("cie-igcse-chemistry-23", CIE_CHEM, "CIE IGCSE Chemistry (0620) — 252 specs, 17 pilot rows"),
    ("cie-igcse-physics-23", CIE_PHYS, "CIE IGCSE Physics (0625) — 294 specs, 16 pilot rows"),
]:
    RF.append(f"## {label}")
    RF.append("")
    RF.append(f"Rows: {len(rows)} ({conf_m(rows)} medium / {conf_l(rows)} low) · draft: `Videos/drafts/{course}/video-map.draft.external.json`")
    RF.append("")
    med = [r for r in rows if r[3] == "medium"]
    low = [r for r in rows if r[3] == "low"]
    for tag, subset in (("MEDIUM", med), ("LOW", low)):
        if not subset: continue
        RF.append(f"**{tag}**")
        RF.append("")
        for vid, prov, specs, conf, ev in subset:
            t = oe[vid]["title"]
            RF.append(f"- [ ] **{t}** — video `{vid}` ({prov}) → specs {', '.join('`'+s+'`' for s in specs)}")
            RF.append(f"      evidence: {ev}")
            RF.append(f"      source: https://www.youtube.com/watch?v={vid}")
        RF.append("")
    RF.append("---")
    RF.append("")
RF.append("## Not drafted in P2C (with reasons)")
RF.append("")
RF.append("- **CIE A-level Biology/Chemistry/Physics (257/356/303 specs)** — feasibility only. C3/P3 Cognito shelves are fully guest-gated (zero site videos), so channels WILL be those lanes' only source; but FSL's A-level pool is AQA-A-level-aligned and CIE diverges sharply at A-level (esp. physics). Recommend a dedicated lane with per-row board adjudication before any CIE A-level rows exist.")
RF.append("- **igcse-maths-a-18-higher** — the external maths pool is 9 Cognito channel-only videos; Cognito's m2-gcse-iedexcel shelf carries 117 site videos for the real P2-method pass. FSL has no GCSE maths.")
RF.append("- **Double-award / modular variants** — deliberately untouched pending the triple-lane maps (P2 lesson: bind the spine of record, then fold).")
RF.append("- **DoodleScience physics**: 57 physics videos ARE in the physics draft pool (used where titles are exact); the rest of Doodle's list duplicates FSL coverage.")
RF.append("- **Cognito channel-only videos aimed at other boards** (Waste Water Treatment, Nanoparticles, Flame Emission Spectroscopy, LCAs, History of the Atom, Seismic Waves, Atmospheric Pressure…) — AQA-only topics with no 4CH1/4PH1 spec to bind.")
RF.append("")
RF.append("## Post-review pipeline (for when you rule)")
RF.append("")
RF.append("1. Your verdict per course (approve rows / reject rows), recorded in each draft dir as `owner-review-verdicts.json`.")
RF.append("2. Applied rows flipped to `reviewed: true`, then `build-content-map.mjs`-equivalent per course emits `hub.video-map/1` files + registry entries (flag-gated per course as before).")
RF.append("3. Still owed after that: the P2-method site-inventory alignment per shelf (the 63/82/117/72/54/81 Cognito site videos), which carries keyPoints evidence and can upgrade the title-only grades.")
open(f"{RES}/Videos/drafts/review-file-external-p2c.md", "w").write("\n".join(RF) + "\n")
print("review file written")
