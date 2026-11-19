#!/usr/bin/env python3
"""P16 assemble: build the lit-21 draft + verdicts per the committed file law
(syllabai.video-map-draft/2 + syllabai.owner-review-verdicts/2), plus the
committed evidence artifacts under Videos/scripts/p16/."""
import json, os, datetime, shutil
from collections import Counter

RES = "/home/z/my-project/repos/syllabai-resources"
WORK = "/home/z/my-project/work/p16"
D = f"{RES}/Videos/drafts/cie-igcse-english-literature-21"
EV = f"{RES}/Videos/scripts/p16"
os.makedirs(D, exist_ok=True)
os.makedirs(EV, exist_ok=True)

UTC = "2026-11-20T00:00:00Z"
REVIEWER = ('delegated self-review (agent, per owner chat 2026-11-09 "approve and review yourself"; '
            'lit-21 owner decision 2026-11-20 "open lit-21" — judgment run 2026-11-20)')

keeps = json.load(open(f"{WORK}/keeps.json"))
skips = json.load(open(f"{WORK}/skips.json"))
oem = json.load(open(f"{WORK}/oembed-p16.json"))
inv = {u['id']: u['title'] for u in json.load(open(f"{RES}/Videos/inventory/channels/claires-notes-uploads.json"))['videos']}
inv.update({u['id']: u['title'] for u in json.load(open(f"{RES}/Videos/inventory/channels/igcsesuccess-uploads.json"))['videos']})

# identity gate: every kept video verified author==channel-of-record
for k in keeps:
    r = oem.get(k['video'])
    assert r and r.get("ok") and r.get("match"), f"identity gate failed for {k['video']}"

TASK = ("T-VIDEOMAP-P16 (lit-21 opening lane: owner decision 2026-11-20 \"open lit-21\" — the P12 "
        "terminal declaration overturned for cie-igcse-english-literature-21; the 252 RESERVED lit-0475 "
        "titles (P14 IGCSESUCCESS 9 + P15 Claire's Notes 243) adjudicated onto the freshly opened course)")

DRAFT_LAW = (
    "P16 lit-21 opening lane (the owner decision admits the first-ever lit-21 content): Class W "
    "set-text work binds — the spine is the 0475 2023-2025 set-text syllabus (Songs of Ourselves "
    "Vol 1 P4 / Vol 2 P3 / Vol 2 P4 poem lists, the Ted Hughes 15 two-per-line pairs, the prose "
    "novels, the Stories of Ourselves Vol 2 per-year lists, the per-year drama set texts), so a "
    "title naming a set-text WORK binds every spec point carrying that work — multi-year "
    "occurrences disclosed per row (df=N, the P13 shared-unit precedent: a repeated set text is "
    "not a discriminative ambiguity); match rule suffix-anchored (a spine work binds a title "
    "work-span iff the span equals the work, ends with it at a word boundary, or the title "
    "dropped a leading article — mid-phrase coincidences like 'night sweat' inside 'the man with "
    "night sweats' and cross-work subsets like 'planners' inside 'The City Planners' do NOT "
    "bind); confidence medium when the title carries author+work matching the spine line, low "
    "under the title-only posture (work-only, scene-commentary, multi-work tips rows bound as "
    "ONE multi-spec row per the four-gate topic-lecture class analog); boardMismatch true on "
    "every spec row (the committed builder law for the title-only posture). Honest skips: "
    "guidance/skills register (technique titles with no set-text bind), out-of-spine board "
    "register (AQA/Eduqas/WJEC/Edexcel/GCSE without a CIE token), works not on the 2023-2025 "
    "set-text lists (Macbeth, Kumukanda, the AQA anthologies, An Inspector Calls, Lord of the "
    "Flies, ...), character-study titles without a set-text token (Malvolio, Caliban, Sybil "
    "Birling — no machine-checkable bind). Rejected/unrouted videos stay out of videos[].")

METHOD = ("Claire's Notes (243 uploads, flat-enumerated 2026-11-19T14:37:11Z) + IGCSESUCCESS (279 uploads, "
          "flat-enumerated 2026-11-17T04:07:29Z, the P14 RESERVED set re-derived by the committed "
          "p14_judgment.py predicate); routing: Class W set-text work binds per the suffix-anchored rule "
          "over every reserved title with the author cross-check; guidance/board/no-binding registers "
          "skipped honestly; exactly-once disposition of all 252 reserved accounts, 0 collisions")

videos, mappings = [], []
for k in keeps:
    vid = k['video']
    r = oem[vid]
    provider = k['provider']
    prov_label = "Claire's Notes" if provider == "claires-notes" else "IGCSESUCCESS"
    videos.append({
        "id": vid, "title": inv[vid], "provider": provider,
        "watchUrl": f"https://www.youtube.com/watch?v={vid}",
        "lessonRef": None, "lessonUrl": None, "levelTag": "igcse",
        "boardNote": f"{prov_label} (oEmbed author verified per video)",
        "identityMethod": "oembed",
    })
    mappings.append({
        "video": vid, "lessonRef": None, "lessonUrl": None,
        "specs": k['specs'], "confidence": k['confidence'],
        "evidence": k['evidence'], "method": "llm-draft-external",
        "boardMismatch": True, "reviewed": True, "reviewer": REVIEWER,
        "reviewedUtc": UTC,
    })

by_conf = Counter(m['confidence'] for m in mappings)
spec_pts = sorted({c for m in mappings for c in m['specs']})
coverage = {
    "specPointsTotal": 203,
    "specPointsDraftedHere": len(spec_pts),
    "rows": len(mappings),
    "byConfidence": {"high": by_conf.get("high", 0), "medium": by_conf.get("medium", 0),
                     "low": by_conf.get("low", 0)},
}

draft = {
    "schema": "syllabai.video-map-draft/2",
    "draftOf": "cie-igcse-english-literature-21",
    "task": TASK,
    "course": "cie-igcse-english-literature-21",
    "qual": "CAMBRIDGE IGCSE ENGLISH LITERATURE",
    "reviewState": "owner-reviewed-external",
    "draftLaw": DRAFT_LAW,
    "source": {
        "provider": "Claire's Notes + IGCSESUCCESS (0475 Literature register; the P14+P15 RESERVED sets admitted by the owner's lit-21 decision)",
        "label": "cie-igcse-english-literature-21",
        "method": METHOD,
        "enumeratedUtc": "2026-11-19T14:37:11Z",
    },
    "videos": videos,
    "mappings": mappings,
    "coverage": coverage,
    "generatedUtc": UTC,
    "reviewedUtc": UTC,
}

EVIDENCE = (
    "Identity: oEmbed sweep 100/100 kept videos author_name == channel-of-record via the committed "
    "inventories' UC ids (0 mismatch, 0 dead, 0 thumbnail fallbacks). Class W binds: suffix-anchored "
    "set-text matching (span == work, or span ends with the work at a word boundary, or the title "
    "dropped a leading article) with author cross-check where the title names an author; multi-year "
    "occurrences bound together and disclosed per row (the P13 shared-unit precedent); scene-by-scene "
    "commentary (Othello x23, A Midsummer Night's Dream x5, Journey's End x8, Twelfth Night x2) binds "
    "the play's set-text spec points per examination year; multi-work tips rows (x3) bound as ONE "
    "multi-spec row at low per the four-gate topic-lecture class analog. Skips ledgered with reasons "
    f"({len(skips)} in scripts/p16/skips.json by class: "
    + json.dumps({k: v for k, v in sorted(Counter(s['cls'] for s in skips).items())})
    + "); the character-study class (Malvolio/Caliban/Sybil Birling) carries no machine-checkable set-text "
    "token and no-binding is honest. Reserved-set lineage: P14 IGCSESUCCESS 0475 x9 re-derived by the "
    "committed p14_judgment.py predicate (2 keeps: Wind -> the three Hughes pair-lines, A Streetcar Named "
    "Desire -> the 2024/2025 drama specs; 7 honest skips incl. the two guidance titles) + P15 Claire's "
    "Notes x243 (scripts/p15/reserved.json == the pool, ids == inventory) — exactly-once disposition of "
    "all 252, 0 collisions machine-checked. The P12 terminal declaration is overturned for this course "
    "only by the owner's 2026-11-20 decision; the other ten terminal courses are untouched.")

verdicts = {
    "schema": "syllabai.owner-review-verdicts/2",
    "task": TASK,
    "course": "cie-igcse-english-literature-21",
    "ruledUtc": UTC,
    "source": ('delegated self-review — owner chat 2026-11-09 "approve and review yourself"; the lit-21 '
               'decision point carried RESERVED through P14 (9 titles) and P15 (243 titles); owner '
               'decision 2026-11-20 "open lit-21"; judgment run 2026-11-20'),
    "default": "keep",
    "reviewer": REVIEWER,
    "evidenceBasis": EVIDENCE,
    "rejects": [],
    "applied": {"rowsApproved": len(mappings), "rowsRejected": 0, "appliedUtc": UTC},
}

json.dump(draft, open(f"{D}/video-map.draft.external-p16.json", "w"), indent=1, ensure_ascii=False)
open(f"{D}/video-map.draft.external-p16.json", "a").write("\n")
json.dump(verdicts, open(f"{D}/owner-review-verdicts.p16.json", "w"), indent=1, ensure_ascii=False)
open(f"{D}/owner-review-verdicts.p16.json", "a").write("\n")

# committed evidence artifacts (the P15 law)
shutil.copy(f"{WORK}/skips.json", f"{EV}/skips.json")
shutil.copy(f"{WORK}/oembed-p16.json", f"{EV}/oembed-p16.json")
summary = {
    "utc": UTC,
    "task": TASK,
    "reserved": 252,
    "reservedSplit": {"igcsesuccess-p14": 9, "claires-notes-p15": 243},
    "keeps": len(mappings),
    "keepConfidence": dict(by_conf),
    "specPointsDrafted": len(spec_pts),
    "specPointsTotal": 203,
    "skipClasses": {k: v for k, v in sorted(Counter(s['cls'] for s in skips).items())},
    "oembed": "100/100 author==channel-of-record, 0 fallbacks",
    "coverage": coverage,
    "specPointsBound": spec_pts,
}
json.dump(summary, open(f"{EV}/judgment_summary.json", "w"), indent=1, ensure_ascii=False)
open(f"{EV}/judgment_summary.json", "a").write("\n")

print("draft:", len(videos), "videos,", len(mappings), "rows,", len(spec_pts), "spec points,", dict(by_conf))
print("verdicts applied:", verdicts['applied'])
print("evidence artifacts:", EV)
