#!/usr/bin/env python3
"""Build the external-channels draft (rows, videos, census) + review file for owner review."""
import json, datetime, hashlib

NOW = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
DRAFT_DIR = "/home/z/my-project/repos/syllabai-resources/Videos/drafts/igcse-biology-19"

# flat-playlist durations
durs = {}
for name in ("cognito", "fsl", "malmesbury", "amoeba", "doodle"):
    d = json.load(open(f"/home/z/my-project/work/channels/{name}-uploads.json"))
    for v in d["videos"]:
        if v.get("duration"):
            durs[v["id"]] = v["duration"]

oe = json.load(open("/home/z/my-project/work/channels/candidate-oembed.json"))

# (id, provider, levelTag, boardNote)
VIDEOS = [
    ("Lomr_t5Pdjs", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; content generic GCSE biology"),
    ("vWZWPlFmua4", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; content generic GCSE biology"),
    ("QekStThHD2M", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); cloning content generic"),
    ("hNq-y2Kg5CE", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); adult-cell cloning generic"),
    ("nrbJl3R4YJU", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); farming methods generic"),
    ("u59Eg1uNr5g", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); fish farming generic"),
    ("DbLVB_EDnRs", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); kidney/urine generic"),
    ("kmRh_yRbAR4", "freesciencelessons", "gcse", "AQA-aligned GCSE channel (Triple); ADH/water balance generic"),
    ("iXswGsfeHJg", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; menstrual hormones generic"),
    ("yLHz2Ea10Mg", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; RP9 quadrats/transects generic"),
    ("1Z405uGDZGo", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; waste/pollution generic"),
    ("9yTDokLRZs0", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; transpiration stream generic"),
    ("gu9T91GJXDo", "freesciencelessons", "gcse", "AQA-aligned GCSE channel; genetic engineering generic"),
    ("1Dx7LDwINLU", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("ALFE2tNIY5c", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("NHqEthRCqQ4", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("QMBGMUgAqCs", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("YbdkbCU20_M", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("YJHGfbW55l0", "amoeba-sisters", "us-intro", "US-curriculum channel; non-Mendelian genetics, US scope"),
    ("CDw4WPng2iE", "amoeba-sisters", "us-intro", "US-curriculum channel; NGSS vocabulary, concept animations"),
    ("RNLceVI8jcc", "amoeba-sisters", "us-intro", "US-curriculum channel; neuron/synapse intro, US scope"),
    ("DGpPHrLF-5M", "amoeba-sisters", "us-intro", "US-curriculum channel; 2016 'OLD VIDEO' — superseded style"),
    ("UrTchvRUMW0", "cognito", "ks3", "Cognito's own channel, KS3 tier — below IGCSE level"),
    ("als-gv_D7bc", "cognito", "ks3", "Cognito's own channel, KS3 tier — below IGCSE level"),
    ("BIf0sIKQm_E", "cognito", "ks3", "Cognito's own channel, KS3 tier — below IGCSE level"),
]

# (video, specs, confidence, evidence, lessonRef, lessonUrl)  — lessonRef/Url only for the extension row
ROWS = [
    ("Lomr_t5Pdjs", ["3.26", "3.27"], "medium",
     "title 'Inheritance of Sex' = the XX/XY sex-chromosome determination of 3.26 and the genetic-diagram offspring sex of 3.27; clause detail title-only (unverified)"),
    ("vWZWPlFmua4", ["4.11B"], "medium",
     "title 'The Nitrogen Cycle' names the exact process of 4.11B; bacterial roles (fixing/nitrifying/denitrifying) not title-evidenced"),
    ("QekStThHD2M", ["3.7"], "medium",
     "title 'Cloning Plants' covers the artificial methods clause (cuttings/tissue culture); natural runners clause not title-evidenced"),
    ("QekStThHD2M", ["5.17B", "5.18B"], "medium",
     "AQA 'Cloning Plants' includes tissue culture = micropropagation of 5.17B and commercial-quantity identical plants of 5.18B; explant/in-vitro detail title-only"),
    ("hNq-y2Kg5CE", ["5.19B"], "medium",
     "title 'Cloning Animals' = AQA adult-cell cloning = the diploid-nucleus-transfer stages of 5.19B; enucleated-egg/electric-stimulus clauses title-only"),
    ("nrbJl3R4YJU", ["5.1", "5.2"], "medium",
     "title 'Modern Farming Methods' covers glasshouse/polytunnel yield methods (5.1) and CO2/temperature management (5.2); clause coverage title-only"),
    ("nrbJl3R4YJU", ["5.3", "5.4"], "medium",
     "same title covers fertiliser use (5.3) and pest control incl. pesticides vs biological (5.4); pros/cons detail title-only"),
    ("u59Eg1uNr5g", ["5.9B"], "medium",
     "title 'Sustainable Fisheries' covers fish-farming methods = 5.9B (maintaining water quality/feeding); intraspecific-predation control clause title-only"),
    ("DbLVB_EDnRs", ["2.79B"], "medium",
     "title 'The Kidneys' covers urine production = water/urea/ions composition of 2.79B; the three-component clause itself title-only"),
    ("kmRh_yRbAR4", ["2.95B"], "medium",
     "title 'Maintaining the Body's Water Balance' = the ADH clause of 2.95B (source/role/effects); FSH/LH clauses are separate row (iXswGsfeHJg)"),
    ("iXswGsfeHJg", ["2.95B"], "medium",
     "title 'The Menstrual Cycle' = FSH and LH roles of 2.95B; pituitary source + effects detail title-only; ADH clause separate row (kmRh_yRbAR4)"),
    ("yLHz2Ea10Mg", ["4.4B"], "medium",
     "AQA 'Required Practical 9: Sampling Organisms' = quadrats/transects for distribution (4.4B); biodiversity measurement clause title-only"),
    ("RhMOCxXcDrQ", ["4.4B"], "medium",
     "already-mapped Malmesbury quadrats practical (committed 4.2 binding) — distribution-by-quadrat content directly serves 4.4B; second binding of a vetted video"),
    ("1Dx7LDwINLU", ["2.7"], "medium",
     "title 'Biomolecules' = elements/structure of carbohydrates, proteins, lipids (2.7); per-molecule element lists title-only; US channel"),
    ("ALFE2tNIY5c", ["2.8"], "medium",
     "title 'Dehydration Synthesis and Hydrolysis' = large molecules built from smaller units (2.8); monomer-per-polymer naming title-only; US channel"),
    ("NHqEthRCqQ4", ["4.11B"], "medium",
     "title 'Carbon and Nitrogen Cycles' includes the 4.11B nitrogen cycle; alternative to vWZWPlFmua4 — pick one; bacterial roles title-only; US channel"),
    ("QMBGMUgAqCs", ["3.4"], "medium",
     "title 'Angiosperm (Flowering Plants) Reproduction' covers pollen tube, fertilisation, seed and fruit formation (3.4); clause order title-only; US channel"),
    ("YbdkbCU20_M", ["5.5"], "medium",
     "title 'Fermentation' = yeast anaerobic respiration incl. bread/food production (5.5); yoghurt is bacterial (separate spec 5.7) — not title-evidenced here; US channel"),
    ("YJHGfbW55l0", ["3.21B"], "medium",
     "title names 'Codominance' = the definition-and-crosses of 3.21B; US non-Mendelian framing, content on-point"),
    ("1Z405uGDZGo", ["4.16"], "low",
     "title 'Waste Management' implies sewage treatment/pollution (4.16) but the sewage clause is NOT title-evidenced — HISTORY: the only prior 4.16 binding (cickRHnPKvc) was rejected by owner because the video didn't teach sewage; this row is the only candidate found on 5 channels; owner should scrutinise or keep 4.16 unmapped"),
    ("9yTDokLRZs0", ["2.58B"], "low",
     "title 'Transpiration' covers the process; the 2.58B practical clause (potometer/environmental factors) is not title-evidenced — the video may be concept-only"),
    ("gu9T91GJXDo", ["5.20B"], "low",
     "title 'Genetic Engineering' covers transgenic organisms but 5.20B is specifically cloned TRANSGENIC ANIMALS producing human proteins — animal example clause title-only"),
    ("CDw4WPng2iE", ["5.20B"], "low",
     "US 'Genetic Engineering' covers transgenic organisms incl. animals conceptually; cloned-transgenic-animal protein-production clause title-only"),
    ("RNLceVI8jcc", ["2.89"], "low",
     "title 'Nervous System' covers neuron signalling and likely synapses, but 'neurotransmitters at synapses' (2.89) is not title-evidenced; A-level alternates exist but are level-mismatched"),
    ("DGpPHrLF-5M", ["2.55B"], "low",
     "title 'Plant Structure and Adaptations' likely covers root hair absorption, but 'water absorbed by root hair cells' (2.55B) is not title-evidenced; OLD VIDEO flag"),
    ("UrTchvRUMW0", ["2.49"], "low",
     "Cognito's own channel, KS3 tier: title names Smoking = 2.49 topic, but video is below IGCSE level; lungs/circulatory clause detail unverified; only smoking candidate found"),
    ("als-gv_D7bc", ["3.8"], "low",
     "Cognito KS3 tier: title 'Human Reproductive Systems' = the structure/function of 3.8, but below IGCSE level; adaptation language unverified"),
    ("BIf0sIKQm_E", ["3.11", "3.12"], "low",
     "Cognito KS3 tier: title 'Fertilisation & Pregnancy' covers placenta nutrition (3.11) and amniotic protection (3.12) contextually, below IGCSE level; clause detail unverified"),
]

videos = []
for vid, prov, tag, note in VIDEOS:
    o = oe[vid]
    assert o["ok"], vid
    videos.append({
        "id": vid,
        "title": o["title"],
        "provider": prov,
        "watchUrl": f"https://www.youtube.com/watch?v={vid}",
        "lessonRef": None,
        "lessonUrl": None,
        "levelTag": tag,
        "boardNote": note,
        "durationS": durs.get(vid),
        "guestVisible": None,
        "subelementOfPrimary": False,
        "oembedAuthor": o["author"],
        "oembedVerifiedUtc": NOW,
    })

mappings = []
for vid, specs, conf, ev, *lr in ROWS:
    row = {
        "video": vid,
        "lessonRef": None,
        "lessonUrl": None,
        "specs": specs,
        "confidence": conf,
        "evidence": ev,
        "method": "llm-draft-external",
        "reviewed": False,
        "reviewer": None,
        "reviewedUtc": None,
        "boardMismatch": True,
    }
    if vid == "RhMOCxXcDrQ":
        row["lessonRef"] = "10.13"
        row["lessonUrl"] = "https://cognitoedu.org/courses/gcse/biology-triple/iedexcel/notes/S0NkdUJaRWg/10.13-field-sampling-with-quadrats"
        row["note"] = "extension of an already-committed video (existing 4.2 binding); no new video row"
    mappings.append(row)

covered = sorted({s for _, sp, *_ in ROWS for s in sp}, key=lambda x: (x.split(".")[0], x))
draft = {
    "schema": "syllabai.video-map-draft/1",
    "draftOf": "hub.video-map/1 igcse-biology-19",
    "task": "T-VIDEOMAP-P2B (external channels sweep)",
    "course": "igcse-biology-19",
    "qual": "IGCSE",
    "reviewState": "draft-external-sweep",
    "draftLaw": "never enters content/ without owner review; every row reviewed:false; flipping to reviewed:true requires an explicit owner ruling recorded in owner-review-verdicts.json (same law as P2)",
    "source": {
        "provider": "multi (freesciencelessons, malmesbury-education, amoeba-sisters, cognito-ks3)",
        "method": "yt-dlp flat channel enumeration + oEmbed identity sweep (27/27 verified) + LLM title-to-spec adjudication; no transcripts/descriptions available from sandbox (watch pages consent-walled, per-video extraction bot-walled) — evidence is TITLE-ONLY and rows carry confidence accordingly",
        "channelsEnumerated": {
            "cognito": {"uploads": 529, "channelOnlyVsSiteInventory": 122},
            "freesciencelessons": {"uploads": 776, "biologyTitled": 349},
            "malmesbury-education": {"uploads": 72},
            "amoeba-sisters": {"uploads": 179},
            "doodlescience": {"uploads": 58, "note": "all physics — zero biology, excluded"},
            "primrose-kitten": {"note": "no videos tab — not enumerable, excluded"},
        },
        "enumeratedUtc": NOW,
    },
    "videos": videos,
    "mappings": mappings,
    "coverage": {
        "specPointsTotal": 176,
        "specPointsMappedCommitted": 136,
        "specPointsDraftedHere": len(covered),
        "specPointsWouldBeMapped": 136 + len(covered),
        "stillHonestUnmapped": ["2.22", "2.33B", "2.39", "2.45B", "2.70", "3.5", "3.6", "4.17", "5.6", "5.7", "5.8"],
        "rows": len(mappings),
        "byConfidence": {
            "high": 0,
            "medium": sum(1 for r in mappings if r["confidence"] == "medium"),
            "low": sum(1 for r in mappings if r["confidence"] == "low"),
        },
        "note": "ALL rows title-evidence-only, so no high rows — same honesty law as P2 (high required keyPoints evidence, which external channels cannot provide from this sandbox)",
    },
    "inputs": {
        "oembedSweep": "27/27 verified (work/channels/candidate-oembed.json, mirrored in scripts/oembed_candidates.py)",
        "committedMap": "SyllabAI/syllabai-v2 apps/hub/content/video-map/igcse-biology-19.json @ 51ec8ffe",
        "spine": "apps/hub/spines/igcse-biology-19.json (sha 9902a87a443e…)",
    },
    "generatedUtc": NOW,
}

with open(f"{DRAFT_DIR}/video-map.draft.external.json", "w") as f:
    json.dump(draft, f, ensure_ascii=False, indent=1)

print(f"videos: {len(videos)}  mappings: {len(mappings)}")
print(f"new specs drafted: {len(covered)} -> would-be coverage {136+len(covered)}/176 = {(136+len(covered))/176:.1%}")
print("by confidence:", draft["coverage"]["byConfidence"])
