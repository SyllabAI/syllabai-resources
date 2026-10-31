#!/usr/bin/env python3
"""caption-harvest.py — F189 P2 optional unblock path (owner-side, RESIDENTIAL IP).

YouTube walls datacenter egress (30 logged paths in
drafts/igcse-biology-19/caption-validation.md) but not residential IPs. This
script is meant to run on the owner's machine, ONCE, to harvest English
captions for the 35 worksheet videos:

    python3 caption-harvest.py            # from anywhere; paths are resolved
                                          # relative to this file

For each video:
  1. youtube-transcript-api  -> prefer MANUAL en track, else AUTO-generated en
  2. fallback: yt-dlp --write-auto-subs --sub-langs en (if installed)
Segments are written as WebVTT to Videos/.cache/p2/transcripts/<videoId>.vtt
and a run summary goes to Videos/.cache/p2/transcripts/status.json.

No repo data is modified. Verdicts stay owner-gated (caption-revalidate.py
only produces evidence; it never touches `reviewed` flags).
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

VIDEOS_DIR = Path(__file__).resolve().parents[1]
DRAFTS = VIDEOS_DIR / "drafts" / "igcse-biology-19"
OUT_DIR = VIDEOS_DIR / ".cache" / "p2" / "transcripts"
UA = "SyllabAI-VideoMap/1.0 (F189 P2 caption harvest; contact via github.com/SyllabAI)"
DELAY_S = 1.5  # polite, residential-IP friendly


def worksheet_videos() -> list[str]:
    ws = json.loads((DRAFTS / "caption-worksheet.json").read_text())
    return list(ws["videos"])


def vtt_text(segments) -> str:
    def ts(t: float) -> str:
        ms = int(round(t * 1000))
        h, ms = divmod(ms, 3600_000)
        m, ms = divmod(ms, 60_000)
        s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d}.{ms:03d}"

    cues = []
    for i, seg in enumerate(segments, 1):
        start = seg.get("start", 0.0)
        end = start + seg.get("duration", 0.0)
        cues.append(f"{i}\n{ts(start)} --> {ts(end)}\n{seg.get('text', '').strip()}\n")
    return "WEBVTT\n\n" + "\n".join(cues)


def fetch_via_api(vid: str) -> tuple[str, str] | None:
    """Return (kind, vtt_text) using youtube-transcript-api, or None."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore
    except ImportError:
        return None
    # library >= 1.0 uses an instance API; 0.6.x used static methods
    try:
        tlist = YouTubeTranscriptApi().list(vid)
    except AttributeError:
        tlist = YouTubeTranscriptApi.list_transcripts(vid)
    except Exception as e:  # network/bot errors surface to status.json
        print(f"  api error: {type(e).__name__}: {e}")
        return None

    manual = auto = None
    for t in tlist:
        if t.language_code.startswith("en"):
            if t.is_generated and auto is None:
                auto = t
            elif not t.is_generated and manual is None:
                manual = t
    pick = manual or auto
    if pick is None:
        return None
    segs = pick.fetch().to_raw_data() if hasattr(pick.fetch(), "to_raw_data") else pick.fetch()
    return ("manual-en" if manual else "auto-en", vtt_text(segs))


def fetch_via_ytdlp(vid: str) -> tuple[str, str] | None:
    if shutil.which("yt-dlp") is None:
        return None
    cmd = [
        "yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
        "--sub-langs", "en.*", "--sub-format", "vtt", "-o", str(OUT_DIR / "ytdlp-%(id)s"),
        f"https://www.youtube.com/watch?v={vid}",
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, timeout=120)
    except Exception as e:
        print(f"  yt-dlp error: {type(e).__name__}")
        return None
    for cand in sorted(OUT_DIR.glob(f"ytdlp-{vid}*.vtt")):
        return ("yt-dlp", cand.read_text())
    return None


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    vids = worksheet_videos()
    print(f"harvesting {len(vids)} videos -> {OUT_DIR}")
    status: dict[str, dict] = {}
    for i, vid in enumerate(vids, 1):
        print(f"[{i}/{len(vids)}] {vid}")
        got = fetch_via_api(vid) or fetch_via_ytdlp(vid)
        if got is None:
            status[vid] = {"ok": False, "reason": "no en track / all methods failed"}
            print("  FAIL")
        else:
            kind, vtt = got
            (OUT_DIR / f"{vid}.vtt").write_text(vtt)
            status[vid] = {"ok": True, "source": kind, "bytes": len(vtt)}
            print(f"  ok ({kind}, {len(vtt)} bytes)")
        time.sleep(DELAY_S)
    (OUT_DIR / "status.json").write_text(json.dumps(
        {"generatedUtc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
         "total": len(vids),
         "ok": sum(1 for s in status.values() if s["ok"]),
         "results": status}, indent=1) + "\n")
    ok = sum(1 for s in status.values() if s["ok"])
    print(f"\ndone: {ok}/{len(vids)} harvested. Next: python3 caption-revalidate.py")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
