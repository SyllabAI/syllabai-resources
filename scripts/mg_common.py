#!/usr/bin/env python3
"""mg_common.py — shared helpers for the MG RG/FC/LS extraction waves.

Fetch-with-retry + HTML cache, sitemap-derived per-lane mode URL lists,
mirror-catalog loading, and small text utils. Used by the T-MG-RG/FC/LS
extractors.
"""
import json
import os
import re
import ssl
import time
import urllib.error
import urllib.request

WORK = "/home/z/my-project/mg_work"
CACHE = f"{WORK}/cache/rgls"
LOGS = f"{WORK}/logs"
CORPUS = f"{WORK}/corpus"
CTX = ssl.create_default_context()
UA = "Mozilla/5.0 (X11; Linux x86_64) syllabai-corpus-bot/1.0"

LANES = {
    "gcse-maths-edexcel": "gcse/maths/edexcel",
    "igcse-maths-edexcel": "igcse/maths/edexcel",
    "a-level-maths-edexcel": "a-level/maths/edexcel",
}
MODES = ("revision-guides", "flashcards", "lessons")


def http_get(url, timeout=40, tries=3, binary=False):
    """GET with retry/backoff. Returns bytes or str; raises on final failure."""
    last = None
    for a in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
                data = r.read()
                return data if binary else data.decode("utf-8", "ignore")
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                raise
            last = e
        except Exception as e:
            last = e
        time.sleep(1.5 * (a + 1))
    raise last


def cache_path(lane_dir: str, topic: str, mode: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9._-]", "_", topic)
    return f"{CACHE}/{lane_dir}/{safe}~{mode}.html"


def fetch_mode_page(lane_dir: str, topic: str, mode: str, base: str) -> str:
    """Fetch (or load from cache) one topic mode page."""
    cp = cache_path(lane_dir, topic, mode)
    if os.path.exists(cp) and os.path.getsize(cp) > 1000:
        return open(cp, encoding="utf-8", errors="ignore").read()
    html = http_get(f"https://www.mathsgenie.co.uk/{base}/{topic}/{mode}")
    os.makedirs(os.path.dirname(cp), exist_ok=True)
    with open(cp, "w", encoding="utf-8") as f:
        f.write(html)
    time.sleep(0.25)
    return html


def sitemap_urls(force=False):
    """All sitemap URLs (3 shards), cached locally."""
    p = f"{CACHE}/sitemap_urls.json"
    if os.path.exists(p) and not force:
        return json.load(open(p))
    urls = []
    for n in (0, 1, 2):
        sm = http_get(f"https://mathsgenie.co.uk/sitemap/{n}.xml", timeout=90)
        urls += re.findall(r"<loc>(.*?)</loc>", sm)
    os.makedirs(CACHE, exist_ok=True)
    json.dump(urls, open(p, "w"))
    return urls


def lane_mode_urls(lane_dir: str):
    """{mode: {topic_slug: url}} for one lane from the sitemap."""
    urls = sitemap_urls()
    out = {m: {} for m in MODES}
    for u in urls:
        u = u.split("?")[0].rstrip("/")
        pref = f"mathsgenie.co.uk/{lane_dir}/"
        k = u.find(pref)
        if k == -1:
            continue
        rest = u[k + len(pref):]
        parts = rest.split("/")
        if len(parts) != 2:
            continue
        topic, mode = parts
        if mode in MODES:
            out[mode][topic] = u if u.startswith("http") else f"https://{u}"
    return out


def mirror_raw(path: str):
    """Fetch a raw file from the SyllabAI/MathsGenie mirror via GitHub API."""
    tok = os.environ.get("GH_TOKEN", "")
    req = urllib.request.Request(
        f"https://api.github.com/repos/SyllabAI/MathsGenie/contents/{path}?ref=main",
        headers={
            "Authorization": f"token {tok}",
            "User-Agent": "syllabai-corpus-bot",
            "Accept": "application/vnd.github.raw",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def gcse_catalog():
    """GCSE maths Edexcel catalog: {slug: {title, grade}} (mirror of record)."""
    t = json.loads(mirror_raw("data/gcse-maths/topics-edexcel.json"))
    out = {}
    for grade, topics in t["grades"].items():
        for tp in topics:
            out[tp["slug"]] = {"title": tp["title"], "grade": grade}
    return out


def slug_grade(slug: str):
    m = re.match(r"grade-(\d+)-", slug)
    return m.group(1) if m else None


def strip_inline_html(s: str) -> str:
    """Display-text cleanup: keep <br> and math, drop layout tags."""
    if s is None:
        return None
    t = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    t = re.sub(r"</?(strong|em|b|i|sub|sup|span|u)>", "", t, flags=re.I)
    t = re.sub(r"<[^>]+>", "", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
          .replace("&gt;", ">").replace("&#39;", "'").replace("&quot;", '"')
          .replace("£", "£"))
    return re.sub(r"[ \t]+", " ", t).strip()


def sha256_file(path: str) -> str:
    import hashlib
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_str(s: str) -> str:
    import hashlib
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def now_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
