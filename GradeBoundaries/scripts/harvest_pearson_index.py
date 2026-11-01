#!/usr/bin/env python3
"""T-GRADE-8 — harvest Pearson's own Algolia document index for grade-boundary PDFs.

Pearson's grade-boundaries page searches its DAM through Algolia (appId/key/
index are served to every browser in hidden inputs on the page — public
search-only credentials). The DAM index holds every published session document
including ones no longer reachable by URL-guessing. This script:
  1. paginates the index for type:dam:Asset "grade boundaries" hits,
  2. keeps URLs under Support/Grade-boundaries/{International-GCSE,International-A-level}/,
  3. maps filenames -> (family, session) with the same slug grammar as
     fetch_pearson.py, intersected with raw/fetch-missing.json's want list,
  4. downloads each missing doc (%PDF-verified, soft-404 guard) into raw/
     via fetch_pearson.py's own manifest helpers, so MANIFEST.jsonl and
     fetch-missing.json stay consistent.
Fail-closed: any non-PDF body is rejected, never committed.
"""
import json, re, sys
from pathlib import Path
from urllib.parse import urlencode

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fetch_pearson as fp  # same RAW, manifest_append, pdf_ok, http_get helpers

APP_ID = "L639T95U5A"
API_KEY = "f79c7a8352e9ffbdaec387bf43612ee6"   # public search-only key from the page
INDEX = "qualifications-uk_LIVE_master-content"
ALGOLIA = f"https://{APP_ID}-dsn.algolia.net/1/indexes/{INDEX}/query"
MONTH = {"01": "January", "06": "June", "10": "October", "11": "November"}

def algolia_hits(query: str):
    hits, page = [], 0
    while True:
        params = urlencode({
            "query": query,
            "facetFilters": json.dumps(["type:dam:Asset"]),
            "hitsPerPage": 100,
            "page": page,
            "attributesToRetrieve": "objectID,url,title",
        })
        import urllib.request
        req = urllib.request.Request(
            ALGOLIA, data=json.dumps({"params": params}).encode(),
            headers={
                "x-algolia-application-id": APP_ID,
                "x-algolia-api-key": API_KEY,
                "content-type": "application/json",
            })
        with urllib.request.urlopen(req, timeout=40) as r:
            d = json.loads(r.read())
        hits.extend(d.get("hits", []))
        page += 1
        if page >= d.get("nbPages", 0):
            return hits

def classify(url: str):
    """filename grammar -> (family, session) or None."""
    m = re.search(r"/Support/Grade-boundaries/(International-GCSE|International-A-level)/([^/?#]+\.pdf)$", url, re.I)
    if not m:
        return None
    fam = "pearson-int-gcse-linear"
    name = m.group(2)
    if "modular" in name.lower():
        fam = "pearson-int-gcse-modular"
    elif m.group(1).lower().startswith("international-a"):
        fam = "pearson-ial"
    ym = re.match(r"(\d{4})-", name)
    if ym:
        y, mon = ym.group(1)[:2], ym.group(1)[2:]
        month = MONTH.get(mon)
        if not month:
            return None
        session = f"{month} 20{y}"
    else:
        ms = re.search(r"grade-boundaries-(january|june|october|november)-(20\d{2})-", name, re.I)
        if not ms:
            return None
        session = f"{ms.group(1).capitalize()} {ms.group(2)}"
    return fam, session

def main() -> None:
    hits = algolia_hits("grade boundaries") + algolia_hits("grade-boundaries")
    seen = {}
    for h in hits:
        url = h.get("url") or ""
        c = classify(url)
        if c:
            seen.setdefault(c, url)
    print(f"index hits: {len(hits)}, classified (family, session) pairs: {len(seen)}")
    want = json.load(open(fp.RAW / "fetch-missing.json"))["missing"]
    wantset = {(f, s) for f, s in want}
    fetchable = sorted(seen.items(), key=lambda kv: kv[0])
    targets = [(fam, ses, url) for (fam, ses), url in fetchable if (fam, ses) in wantset]
    print(f"fetch-missing want: {len(wantset)}; recoverable from index: {len(targets)}")
    fetched = []
    for fam, ses, url in sorted(targets):
        full = "https://qualifications.pearson.com" + url if url.startswith("/") else url
        code, body, final = fp.http_get(full)
        ok = code == 200 and fp.pdf_ok(body) and "404" not in (final or "")
        print(f"  {fam} {ses}: {'OK ' + str(len(body)) + 'B' if ok else f'reject code={code}'}")
        if not ok:
            continue
        dest = fp.RAW / fam
        dest.mkdir(parents=True, exist_ok=True)
        (dest / f"{ses}.pdf").write_bytes(body)
        fp.manifest_append(fam, ses, full, final, fp.sha256_bytes(body), len(body))
        fetched.append((fam, ses))
    print(f"RECOVERED {len(fetched)}: " + ", ".join(f"{f}/{s}" for f, s in fetched))

if __name__ == "__main__":
    main()
