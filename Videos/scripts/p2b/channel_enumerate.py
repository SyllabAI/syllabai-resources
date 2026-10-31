#!/usr/bin/env python3
"""Enumerate a YouTube channel's uploads via yt-dlp flat playlist (no API key).
Usage: python3 channel_enumerate.py <channel_url> <out.json>
Writes: {"channel": url, "count": N, "videos": [{"id","title","duration","viewCount","timestamp"}]}
"""
import json, sys, yt_dlp

url, out = sys.argv[1], sys.argv[2]
opts = {
    "quiet": True, "no_warnings": True, "extract_flat": True,
    "playlist_items": "1-2000", "ignoreerrors": True, "socket_timeout": 20,
}
with yt_dlp.YoutubeDL(opts) as ydl:
    info = ydl.extract_info(url, download=False)

entries = info.get("entries") or []
vids = []
for e in entries:
    if not e or not e.get("id"):
        continue
    vids.append({
        "id": e["id"],
        "title": e.get("title"),
        "duration": e.get("duration"),
        "viewCount": e.get("view_count"),
        "timestamp": e.get("timestamp"),
    })
result = {"channel": url, "playlistTitle": info.get("title"), "count": len(vids), "videos": vids}
with open(out, "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print(f"count={len(vids)} title={info.get('title')}")
