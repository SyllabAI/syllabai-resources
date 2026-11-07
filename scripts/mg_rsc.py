#!/usr/bin/env python3
"""mg_rsc — shared MathsGenie flight-payload decoding + polite fetching.
Based on SyllabAI/MathsGenie research/06-parsing-methodology.md (self.__next_f chunks)."""
import re, json, time, hashlib, os, sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = "Mozilla/5.0 (X11; Linux x86_64) SyllabAI-corpus-bot/0.1 (operator-authorized; contact via SyllabAI)"
CHUNK_RE = re.compile(r'self\.__next_f\.push\(\[1,(".*?")\]\)</script>', re.S)
CACHE = "/tmp/mg_cache"

def flight(html: str) -> str:
    """Decode all self.__next_f chunks into the concatenated flight payload."""
    out = []
    for m in CHUNK_RE.finditer(html):
        try:
            out.append(json.loads(m.group(1)))
        except Exception:
            pass
    return "".join(out)

def fetch(url: str, cache_key: str = None, binary: bool = False, retries: int = 3, timeout: int = 30):
    """Polite fetch with on-disk cache. Returns bytes (or str for html)."""
    if cache_key:
        ck = os.path.join(CACHE, cache_key)
        if os.path.exists(ck):
            with open(ck, "rb") as f:
                data = f.read()
            return data if binary else data.decode("utf-8", errors="replace")
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            if cache_key:
                os.makedirs(os.path.dirname(ck), exist_ok=True)
                with open(ck, "wb") as f:
                    f.write(data)
            return data if binary else data.decode("utf-8", errors="replace")
        except Exception as e:
            last = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"fetch failed after {retries}: {url}: {last}")

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def scan_objects(payload: str, marker: str = None):
    """Yield (pos, obj) for JSON objects parsed via raw_decode.
    If marker given, only objects whose serialized text contains it."""
    dec = json.JSONDecoder()
    i, n = 0, len(payload)
    while i < n:
        c = payload.find("{", i)
        if c < 0:
            break
        try:
            obj, end = dec.raw_decode(payload, c)
            if isinstance(obj, dict):
                if marker is None or marker in payload[c:end]:
                    yield c, obj
                i = end
            else:
                i = c + 1
        except Exception:
            i = c + 1

def pool_map(fn, items, workers=6):
    results = {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(fn, it): it for it in items}
        for f in as_completed(futs):
            it = futs[f]
            try:
                results[it] = (True, f.result())
            except Exception as e:
                results[it] = (False, str(e))
    return results
