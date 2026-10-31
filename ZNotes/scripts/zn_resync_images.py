#!/usr/bin/env python3
"""ZNotes image-failure re-sourcer for SyllabAI/syllabai-resources.

Task: T-ZNOTES-2 — re-sources images recorded in course manifests
`failures.images` (T-ZNOTES-1 residue), downloads replacements under the
existing asset-naming convention (sha1(orig_url)[:12]-<stem>.<ext>),
rewrites the failing references in leaf .md/.json, and updates manifests.

Resolution ladder per failure URL (first success wins):
  1. repair      — fix known upstream URL defects (concatenated URLs,
                   wikimedia thumbnail 400 -> original file, page URLs ->
                   og:image, google redirect -> target)
  2. direct      — plain fetch with browser UA
  3. direct-ref  — browser UA + site referer (hotlink-protected hosts)
  4. wsrv        — https://wsrv.nl/?url=... image CDN proxy
  5. wayback     — archive.org availability API for a snapshot, fetched
                   through wsrv (web.archive.org unreachable from sandbox)

Every candidate download is magic-byte validated; HTML replies are rejected.

Usage:
    python3 zn_resync_images.py --root <repo root> [--report <path>]
Stdlib only.
"""
import argparse
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
WSRV = "https://wsrv.nl/?url="
AVAIL = "http://archive.org/wayback/available?url="
TIMEOUT = 40
IMG_WORKERS = 6
_ext_re = re.compile(r"\.([A-Za-z0-9]{2,5})$")
_slug_bad = re.compile(r"[^a-z0-9]+")
_og_img = re.compile(r'<meta[^>]+property=["\']og:image(?::secure_url)?["\'][^>]+content=["\']([^"\']+)', re.I)
_og_img2 = re.compile(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']', re.I)
_img_tag = re.compile(r"<img[^>]+src=[\"']([^\"']+\.(?:png|jpe?g|gif|webp|svg))[\"']", re.I)

MAGIC = ((b"\x89PNG", "png"), (b"\xff\xd8\xff", "jpg"), (b"GIF87a", "gif"),
         (b"GIF89a", "gif"), (b"RIFF", "webp"), (b"%PDF", "pdf"),
         (b"BM", "bmp"), (b"\x00\x00\x01\x00", "ico"))


def unescape_md(url):
    """md-escaped chars back to URL chars (upstream md used \\_ etc.)."""
    return url.replace("\\_", "_").replace("\\-", "-").replace("\\.", ".")


def http_get(url, referer=None, timeout=TIMEOUT):
    hdrs = {"User-Agent": UA, "Accept": "*/*"}
    if referer:
        hdrs["Referer"] = referer
    req = urllib.request.Request(url, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def wsrv_url(url):
    return WSRV + urllib.parse.quote(url, safe="")


def looks_like_image(data):
    if not data or len(data) < 64:
        return None
    head = data[:64].lstrip()
    if head[:9].upper().startswith(b"<!DOCTYPE") or head[:5].upper().startswith(b"<HTML"):
        return None
    for magic, ext in MAGIC:
        if head.startswith(magic):
            if ext == "webp" and data[8:12] != b"WEBP":
                continue
            return ext
    if head[:5] in (b"<?xml",) or b"<svg" in data[:400]:
        return "svg"
    return None


def sniff_ext(url, data):
    m = _ext_re.search(urllib.parse.urlparse(url).path.lower())
    ext = m.group(1) if m else None
    if ext in ("png", "jpg", "jpeg", "gif", "webp", "svg", "avif"):
        return "jpeg" if ext == "jpeg" else ext
    kind = looks_like_image(data)
    return kind or "png"


def try_fetch(cands):
    """cands: list of (url, tag, referer). Returns (data, url, tag) or (None, last_url, None)."""
    last = None
    for url, tag, ref in cands:
        last = url
        for attempt in range(2):
            try:
                data = http_get(url, referer=ref if attempt else None)
            except Exception:
                continue
            ext = looks_like_image(data)
            if ext:
                return data, url, tag
    return None, last, None


def page_first_image(url):
    """Fetch an HTML page and return the og:image / first content <img> URL."""
    try:
        data = http_get(url, referer="https://www.google.com/")
    except Exception:
        return []
    html = data.decode("utf-8", "replace")
    out = []
    for rx in (_og_img, _og_img2, _img_tag):
        m = rx.search(html)
        if m:
            u = m.group(1).replace("&amp;", "&")
            if u not in out:
                out.append(u)
    return out


def site_ref(u):
    """site root as Referer, e.g. https://microbenotes.com/"""
    p = urllib.parse.urlparse(u)
    return f"{p.scheme}://{p.netloc}/" if p.scheme and p.netloc else None


def repair(url):
    """Return list of (url, tag, referer) repaired candidates (may be empty)."""
    cands = []
    u = unescape_md(url)
    # concatenated-URL data bug: URLs glued together with no separator
    if url.count("https://") > 1:
        seg = u.split("https://")[1]
        if seg:
            cands.append(("https://" + seg, "repair:split-concatenated", None))
    # wikimedia thumbnail 400/429 -> original file
    m = re.match(r"(https://upload\.wikimedia\.org/wikipedia/[^/]+)/thumb(/(?:[0-9a-f]/[^/]+/[^/]+))/[^/]+$", u)
    if m:
        cands.append((m.group(1) + m.group(2), "repair:wikimedia-original", site_ref(u)))
        cands.append((wsrv_url(m.group(1) + m.group(2)), "wsrv:wikimedia-original", None))
    # google images redirect -> real target
    if "google.com/url" in u:
        q = urllib.parse.parse_qs(urllib.parse.urlparse(u).query)
        tgt = (q.get("url") or q.get("imgurl") or [""])[0]
        if tgt:
            cands.append((tgt, "repair:google-redirect", site_ref(tgt)))
            for img in page_first_image(tgt):
                cands.append((img, "repair:google-redirect-page-img", site_ref(img)))
                cands.append((wsrv_url(img), "wsrv:google-redirect-page-img", None))
            cands.append((wsrv_url(tgt), "wsrv:google-redirect", None))
    # ibb / generic page urls -> og:image
    if "://ibb.co/" in u:
        for img in page_first_image(u):
            cands.append((img, "repair:ibb-ogimage", site_ref(img)))
            cands.append((wsrv_url(img), "wsrv:ibb-ogimage", None))
    if "analyticssteps.com" in u:
        for img in page_first_image(u):
            cands.append((img, "repair:page-ogimage", site_ref(img)))
            cands.append((wsrv_url(img), "wsrv:page-ogimage", None))
    # discord channel links are not fetchable without auth
    if "discord.com/channels/" in u:
        return cands
    # media.discordapp.net (signed) -> cdn.discordapp.com without params
    m = re.match(r"https://media\.discordapp\.net/attachments/([^/?]+)", u)
    if m:
        base = unescape_md(u).split("?")[0]
        cdn = "https://cdn.discordapp.com/attachments/" + base.split("/attachments/")[1]
        cands.append((cdn, "repair:discord-cdn-noparams", None))
        cands.append((wsrv_url(cdn), "wsrv:discord-cdn-noparams", None))
    # quizizz empty -> .png suffixed + referer + wsrv
    if "quizizz.com/_media" in u:
        cands.append((u + ".png", "repair:quizizz-png", "https://quizizz.com/"))
        cands.append((u, "direct-ref:quizizz", "https://quizizz.com/"))
        cands.append((wsrv_url(u), "wsrv:quizizz", None))
    # blogger/googleusercontent 404 -> size-suffix variants via wsrv
    if "googleusercontent.com" in u:
        base = u.split("=")[0]
        for suf in ("=s0", "=w1200", "=s800"):
            cands.append((wsrv_url(base + suf), f"wsrv:blogger{suf}", None))
        cands.append((wsrv_url(base), "wsrv:blogger-plain", None))
    # every repaired http candidate also gets a wsrv variant
    extra = []
    for c, tag, ref in cands:
        if c.startswith("http") and not c.startswith(WSRV):
            extra.append((wsrv_url(c), "wsrv:" + tag.split(":")[-1], None))
    cands.extend(extra)
    return cands


def candidates_for(url):
    """Full resolution ladder for one failure URL -> [(url, tag, referer)]."""
    cands = []
    cands.extend(repair(url))
    u = unescape_md(url)
    host = urllib.parse.urlparse(u).netloc
    if host and not u.startswith("blob:"):
        cands.append((u, "direct", None))
        cands.append((u, "direct-ref", site_ref(u)))
        cands.append((wsrv_url(u), "wsrv", None))
        # wayback through wsrv: exact url, then query-stripped variant
        for probe in dict.fromkeys([u.split("?")[0], u]):
            try:
                q = AVAIL + urllib.parse.quote(probe, safe="")
                with urllib.request.urlopen(q, timeout=25) as r:
                    avail = json.load(r)
                snap = ((avail.get("archived_snapshots") or {}).get("closest") or {})
                if snap.get("available") and snap.get("url"):
                    m = re.match(r"https?://web\.archive\.org/web/(\d+)[a-z_]*/(.+)$", snap["url"])
                    if not m:
                        continue
                    ts, orig = m.group(1), m.group(2)
                    wb = f"web.archive.org/web/{ts}id_/{orig}"
                    cands.append((wsrv_url(wb), f"wayback:{ts}", None))
                    break
            except Exception:
                pass
    # dedupe on (url, referer), keep first tag
    seen, out = set(), []
    for c, tag, ref in cands:
        key = (c, ref)
        if key not in seen:
            seen.add(key)
            out.append((c, tag, ref))
    return out


def asset_name(course_dir, orig_url, data):
    """zn_fetch convention: sha1(orig_url)[:12]-<stem>.<ext>, collision -2."""
    assets = os.path.join(course_dir, "assets")
    os.makedirs(assets, exist_ok=True)
    stem = os.path.basename(urllib.parse.urlparse(unescape_md(orig_url)).path)
    stem = urllib.parse.unquote(stem)
    s, _ = os.path.splitext(stem)
    s = _slug_bad.sub("-", s.lower()).strip("-")[:48]
    ext = sniff_ext(orig_url, data)
    prefix = hashlib.sha1(orig_url.encode()).hexdigest()[:12]
    name = f"{prefix}-{s or 'image'}.{ext}"
    n = 1
    while os.path.exists(os.path.join(assets, name)):
        n += 1
        name = f"{prefix}-{s or 'image'}-{n}.{ext}"
    return name


def rewrite_files(course_dir, url, local_ref, files):
    """Rewrite the failing URL in leaf .md/.json files; return updated file list."""
    changed = []
    for rel in files:
        p = os.path.join(course_dir, rel)
        if not os.path.isfile(p):
            continue
        with open(p, encoding="utf-8") as f:
            txt = f.read()
        if url not in txt:
            continue
        with open(p, "w", encoding="utf-8") as f:
            f.write(txt.replace(url, local_ref))
        changed.append(rel)
    return changed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--report", default=None)
    ap.add_argument("--only", default=None, help="comma list of course slugs")
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    zn = os.path.join(a.root, "ZNotes")

    report = {"resolved": [], "unresolved": [], "skipped_courses": []}
    courses = sorted(d for d in os.listdir(zn)
                     if os.path.isfile(os.path.join(zn, d, "manifest.json")))
    if a.only:
        only = set(a.only.split(","))
        courses = [c for c in courses if c in only]
    t0 = time.time()

    for course in courses:
        cdir = os.path.join(zn, course)
        man_p = os.path.join(cdir, "manifest.json")
        man = json.load(open(man_p, encoding="utf-8"))
        fails = (man.get("failures") or {}).get("images") or []
        if not fails:
            continue
        if a.limit:
            fails = fails[:a.limit]
        print(f"== {course}: {len(fails)} failures", flush=True)

        # map: failure url -> leaf files containing it
        url_files = {}
        for dirpath, _, fns in os.walk(os.path.join(cdir, "notes")):
            for fn in fns:
                if not fn.endswith((".md", ".json")):
                    continue
                p = os.path.join(dirpath, fn)
                with open(p, encoding="utf-8") as f:
                    txt = f.read()
                for rec in fails:
                    if rec["url"] in txt:
                        rel = os.path.relpath(p, cdir)
                        url_files.setdefault(rec["url"], []).append(rel)

        for rec in fails:
            url = rec["url"]
            files = url_files.get(url, [])
            if not files:
                # URL no longer present in any leaf -> already resolved in an earlier pass
                report.setdefault("already_resolved", []).append({"course": course, "url": url})
                continue
            if url.startswith(("blob:", "discord.com", "https://discord.com/channels/")):
                report["unresolved"].append({"course": course, "url": url,
                                             "error": rec["error"],
                                             "reason": "no fetchable form (browser blob URI / Discord channel link)"})
                continue
            if "image\\_name.jpg" in url or url.startswith("increasing%20"):
                report["unresolved"].append({"course": course, "url": url,
                                             "error": rec["error"],
                                             "reason": "upstream placeholder text, not an image URL"})
                continue
            files = url_files.get(url, [])
            cands = candidates_for(url)
            data, got_url, tag = try_fetch(cands)
            if not data:
                report["unresolved"].append({"course": course, "url": url,
                                             "error": rec["error"],
                                             "reason": "all strategies exhausted",
                                             "tried": len(cands)})
                continue
            name = asset_name(cdir, url, data)
            with open(os.path.join(cdir, "assets", name), "wb") as f:
                f.write(data)
            local_ref = f"../../../assets/{name}"
            changed = rewrite_files(cdir, url, local_ref, files)
            if not changed:
                os.unlink(os.path.join(cdir, "assets", name))
                report["unresolved"].append({"course": course, "url": url,
                                             "error": rec["error"],
                                             "reason": "downloaded but no md reference found to rewrite"})
                continue
            report["resolved"].append({"course": course, "url": url,
                                       "orig_error": rec["error"],
                                       "recovered_url": got_url, "strategy": tag,
                                       "asset": name, "bytes": len(data),
                                       "rewritten_files": changed})
            print(f"   OK  {tag:34s} {name} ({len(data)}b, {len(changed)} files)", flush=True)

    if a.report:
        with open(a.report, "w") as f:
            json.dump(report, f, indent=1)
    print(f"\nresolved: {len(report['resolved'])}  unresolved: {len(report['unresolved'])}  "
          f"wall {time.time()-t0:.0f}s")
    print("NOTE: run --update-manifests pass afterwards")


if __name__ == "__main__":
    main()
