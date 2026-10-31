#!/usr/bin/env python3
"""caption-revalidate.py — F189 P2 optional unblock path, step 2 (any machine).

Consumes the .vtt files produced by caption-harvest.py and produces LEXICAL
per-row verdicts for the 37 worksheet rows, keyed `lessonRef|video|rowIdx`
(rowIdx disambiguates lesson 8.8's two rows that share lessonRef + video).

For each row: content words of (spec statement titles + lesson title) are
looked up in the video's transcript tokens.

    covered  hit ratio >= 0.34   transcript speaks to the bound statements
    thin     0.15 <= ratio <0.34 partial overlap, read the quotes
    absent   ratio < 0.15        transcript does not cover the statements
    no-track no transcript file  (harvest failed for that video)

Each verdict carries <=3 timestamped quotes of matched terms. Output:
drafts/igcse-biology-19/caption-verdicts.json.

EVIDENCE ONLY — this script never changes confidence or `reviewed` flags;
semantic judgement stays with the owner.
"""
from __future__ import annotations

import json
import re
import time
from pathlib import Path

VIDEOS_DIR = Path(__file__).resolve().parents[1]
DRAFTS = VIDEOS_DIR / "drafts" / "igcse-biology-19"
TX_DIR = VIDEOS_DIR / ".cache" / "p2" / "transcripts"

STOP = {"the", "a", "an", "of", "and", "in", "on", "for", "to", "with", "by",
        "is", "are", "as", "at", "or", "be", "that", "this", "it", "from",
        "gcse", "biology", "international", "edexcel", "part", "lesson"}


def toks(s: str) -> set[str]:
    s = re.sub(r"\((?:19|20)\d\d/\d\d exams\)", " ", s, flags=re.I)
    s = re.sub(r"[|/–—-]+", " ", s)
    out = set()
    for t in re.findall(r"[a-z0-9']+", s.lower()):
        if t in STOP or len(t) <= 2:
            continue
        if t.endswith("s") and len(t) > 3:
            t = t[:-1]
        out.add(t)
    return out


def load_vtt_tokens(path: Path) -> tuple[set[str], list[tuple[float, str]]]:
    """Return (all tokens, [(timestamp, cue text)])."""
    cues: list[tuple[float, str]] = []
    for block in path.read_text(errors="replace").split("\n\n"):
        m = re.search(r"(\d\d:\d\d:\d\d\.\d\d\d) --> ", block)
        lines = [ln for ln in block.splitlines()
                 if ln.strip() and "-->" not in ln and not ln.strip().isdigit()
                 and ln.strip() != "WEBVTT"]
        if m and lines:
            def hms(t: str) -> float:
                hh, mm, ss = t.split(":")
                return int(hh) * 3600 + int(mm) * 60 + float(ss)
            cues.append((hms(m.group(1)), " ".join(lines)))
    return toks(" ".join(txt for _, txt in cues)), cues


def quotes_for(missed_terms: set[str], cues, limit: int = 3) -> list[dict]:
    out = []
    for term in list(missed_terms)[:limit]:
        for ts, txt in cues:
            if re.search(rf"\b{re.escape(term)}\b", txt.lower()):
                mm, ss = divmod(int(ts), 60)
                out.append({"term": term, "at": f"{mm}:{ss:02d}", "quote": txt[:160]})
                break
    return out


def main() -> int:
    ws = json.loads((DRAFTS / "caption-worksheet.json").read_text())
    verdicts: dict[str, dict] = {}
    for idx, row in enumerate(ws["rows"]):
        key = f"{row['lessonRef']}|{row['video']}|{idx}"
        want = set()
        for st in row["statements"].values():
            want |= toks(st.get("title") or "")
        vtt = TX_DIR / f"{row['video']}.vtt"
        if not vtt.exists():
            verdicts[key] = {"verdict": "no-track", "hitRatio": None,
                             "row": {"lessonRef": row["lessonRef"], "video": row["video"],
                                     "specs": row["specs"], "confidence": row["confidence"]}}
            continue
        got, cues = load_vtt_tokens(vtt)
        hits = want & got
        ratio = round(len(hits) / len(want), 3) if want else 0.0
        v = "covered" if ratio >= 0.34 else ("thin" if ratio >= 0.15 else "absent")
        verdicts[key] = {
            "verdict": v, "hitRatio": ratio,
            "matched": sorted(hits)[:25], "missed": sorted(want - got)[:25],
            "quotes": quotes_for(want - got, cues),
            "row": {"lessonRef": row["lessonRef"], "video": row["video"],
                    "specs": row["specs"], "confidence": row["confidence"]},
        }
    from collections import Counter
    tally = Counter(v["verdict"] for v in verdicts.values())
    out = {
        "schema": "syllabai.caption-verdicts/1",
        "task": "T-VIDEOMAP-P2", "course": "igcse-biology-19",
        "generatedUtc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": "LEXICAL evidence only — semantic judgement + any reviewed-flag changes stay owner-gated.",
        "tally": dict(tally),
        "verdicts": verdicts,
    }
    (DRAFTS / "caption-verdicts.json").write_text(json.dumps(out, indent=1) + "\n")
    print(f"rows: {len(verdicts)} | tally: {dict(tally)}")
    print("wrote caption-verdicts.json (evidence only — no draft files touched)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
