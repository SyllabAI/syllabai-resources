#!/usr/bin/env python3
"""P2F Edexcel-native lane recon.

Enumerates candidate Edexcel-native YouTube channels (flat, no download),
scores titles for Edexcel paper-code evidence (WCH1x/WBI1x/WPH1x/4xH1/9xH0/P-refs),
measures overlap with all existing draft video IDs, and writes:
  work/channels/p2f-<slug>.tsv   id \t title \t durationS
  work/channels/p2f-summary.json
Read-only on the repo; evidence for docs/P2F-EDNATIVE-LANE.md.
"""
import json, re, subprocess, pathlib

ROOT = pathlib.Path("/home/z/my-project")
WORK = ROOT / "work/channels"
REPO = ROOT / "repos/syllabai-resources"

CHANNELS = [
    ("exam-essentials", "https://www.youtube.com/channel/UC4qJbWvplEpYsKdc5X1hd9w/videos"),
    ("sergeis-chemistry", "https://www.youtube.com/channel/UClJ5oN30K8OegncMpH7p3tA/videos"),
    ("allery-chemistry", "https://www.youtube.com/c/AlleryChemistry/videos"),
]

# paper-code prefix -> registry course (spine course ids)
COURSE_OF = {
    "WCH1": "ial-chemistry-17", "WBI1": "ial-biology-18", "WPH1": "ial-physics-19",
    "4CH1": "igcse-chemistry-19", "4BI1": "igcse-biology-19", "4PH1": "igcse-physics-19",
    "9CH0": "edexcel-gce-chemistry", "9BI0": "edexcel-gce-biology", "9PH0": "edexcel-gce-physics",
}
CODE_RE = re.compile(r"\b(WCH1[1-6]|WBI1[1-6]|WPH1[1-6]|4CH1|4BI1|4PH1|9CH0|9BI0|9PH0)\b", re.I)
PAPER_REF_RE = re.compile(r"\bP7\d{4}A\b", re.I)
IAL_RE = re.compile(r"\bIAL\b|international\s+a[-\s]?level", re.I)
IGCSE_RE = re.compile(r"\bIGCSE\b", re.I)
ID_RE = re.compile(r'"(?:video|videoId|id)"\s*:\s*"([A-Za-z0-9_-]{11})"')


def sh(cmd, timeout):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)


def enum(url, timeout=300):
    # SEP=chr(9): never rely on literal tab characters surviving source edits
    # (P2F recon bug, 2026-11-12 — tabs in the format string were mangled).
    SEP = chr(9)
    fmt = SEP.join(["%(id)s", "%(title)s", "%(duration)s"])
    r = sh(f'yt-dlp --flat-playlist --print "{fmt}" "{url}"', timeout)
    rows = []
    for line in r.stdout.splitlines():
        parts = line.split(SEP)
        if len(parts) >= 2 and parts[0]:
            rows.append((parts[0], parts[1], parts[2] if len(parts) > 2 else ""))
    return rows


def resolve_channel(query, timeout=120):
    SEP = chr(9)
    fmt = SEP.join(["%(channel_id)s", "%(channel)s"])
    r = sh(f'yt-dlp --flat-playlist --print "{fmt}" "ytsearch5:{query}"', timeout)
    for line in r.stdout.splitlines():
        parts = line.split(SEP)
        if len(parts) == 2 and parts[0].startswith("UC"):
            return parts
    return None


def existing_ids():
    ids = set()
    d = REPO / "Videos/drafts"
    for f in d.rglob("*.json"):
        try:
            ids |= set(ID_RE.findall(f.read_text(errors="ignore")))
        except Exception:
            pass
    return ids


def course_of(code):
    key = code.upper()
    if key.startswith(("WCH1", "WBI1", "WPH1")):
        return COURSE_OF[key[:4]]
    return COURSE_OF.get(key, key)


def main():
    WORK.mkdir(parents=True, exist_ok=True)
    have = existing_ids()
    print(f"existing draft video ids: {len(have)}", flush=True)

    chans = list(CHANNELS)
    om = resolve_channel("Omar's Biology Lab Edexcel IAL")
    if om:
        chans.append(("omars-biology-lab", f"https://www.youtube.com/channel/{om[0]}/videos"))
        print(f"resolved omar: {om[1]} ({om[0]})", flush=True)
    else:
        print("omar: NOT RESOLVED", flush=True)

    summary = {}
    for slug, url in chans:
        try:
            rows = enum(url)
        except subprocess.TimeoutExpired:
            print(f"{slug}: ENUM TIMEOUT after 300s", flush=True)
            rows = []
        seen, dedup = set(), []
        for vid, title, dur in rows:
            if vid and vid not in seen:
                seen.add(vid)
                dedup.append((vid, title, dur))
        (WORK / f"p2f-{slug}.tsv").write_text(
            "\n".join("\t".join(r) for r in dedup), encoding="utf-8")

        codes, units, ial_n, igcse_n, pref = {}, set(), 0, 0, 0
        for vid, title, dur in dedup:
            for c in CODE_RE.findall(title):
                course = course_of(c)
                codes[course] = codes.get(course, 0) + 1
                if len(c) == 5 and c.upper().startswith(("WCH1", "WBI1", "WPH1")):
                    units.add(f"U{c[4]}")
            if PAPER_REF_RE.search(title):
                pref += 1
            if IAL_RE.search(title):
                ial_n += 1
            if IGCSE_RE.search(title):
                igcse_n += 1
        overlap = sum(1 for vid, _, _ in dedup if vid in have)
        samples = [t for _, t, _ in dedup if CODE_RE.search(t)][:8]
        summary[slug] = {
            "url": url, "videos": len(dedup),
            "paper_code_hits_by_course": codes, "unit_scopes": sorted(units),
            "ial_title_hits": ial_n, "igcse_title_hits": igcse_n,
            "edexcel_paper_ref_hits": pref,
            "overlap_with_existing_drafts": overlap,
            "sample_coded_titles": samples,
        }
        print(f"{slug}: videos={len(dedup)} coded={sum(codes.values())} "
              f"units={sorted(units)} overlap={overlap}", flush=True)

    (WORK / "p2f-summary.json").write_text(json.dumps(summary, indent=2))
    print("wrote p2f-summary.json", flush=True)


if __name__ == "__main__":
    main()
