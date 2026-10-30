#!/usr/bin/env python3
"""SIB-ASSESS-r3-silver — quote-fail adjudication (three-way).

For every quoted span that failed verbatim binding to held pack excerpts:
  1. BINDS_PACK      — found in pack excerpts under extended normalization
  2. BINDS_RAW       — found in the raw source file at the live tip, but not
                       in held excerpts -> window-discipline finding (class W)
  3. FUZZY_<ratio>   — near-match in pack text (OCR/parse-level drift)
  4. UNRESOLVED      — found nowhere -> fabrication-class (class X), manual read

Raw plane: syllabai-resources via git cat-file (blobless, fetch-on-demand),
syllabai-pastpapers via its sparse working tree; PDFs text-extracted with
pymupdf when available.
"""
import json, re, os, glob, subprocess, difflib, collections

LIB = "/home/z/my-project/syllabai-resources/SubjectIntelligence/CHEMISTRY_4CH1"
RES = "/home/z/my-project/syllabai-resources"
PP = "/home/z/my-project/syllabai-pastpapers"
RECEIPT = os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-ASSESS-R3", "silver_receipt.json")
OUT = os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-ASSESS-R3", "quote_adjudication.json")

try:
    import fitz  # pymupdf
    HAVE_FITZ = True
except Exception:
    HAVE_FITZ = False

def norm(s):
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2212", "-").replace("\u00a0", " ")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\u2010", "-").replace("\u2011", "-")
    s = re.sub(r"[^A-Za-z0-9 ]+", " ", s)   # aggressive: strip all punct
    return re.sub(r"\s+", " ", s).strip().lower()

def artifact_id_of(path):
    m = re.search(r"CHEMISTRY_4CH1_([A-Z]+-\d+)_", os.path.basename(path))
    return m.group(1) if m else None

def pack_path_for(art):
    cands = sorted(glob.glob(os.path.join(LIB, "runs", "*", "evidence", art, "evidence_pack.json")))
    return cands[-1] if cands else None

def pack_files(pack_path):
    j = json.load(open(pack_path))
    out = []
    for s in j["sources"]:
        for f in s.get("files", []):
            out.append({"repo": f.get("repo", "syllabai-resources"),
                        "path": f["path"],
                        "sha256": f.get("sha256"),
                        "excerpts": f.get("excerpts", [])})
    return out

def read_raw(repo, path):
    if repo == "syllabai-pastpapers":
        p = os.path.join(PP, path)
        if os.path.exists(p):
            if p.lower().endswith(".pdf") and HAVE_FITZ:
                try:
                    d = fitz.open(p)
                    return "\n".join(pg.get_text() for pg in d)
                except Exception:
                    return None
            return open(p, encoding="utf-8", errors="replace").read()
        return None
    # syllabai-resources: worktree if present, else git cat-file (fetch on demand)
    p = os.path.join(RES, path)
    if os.path.exists(p):
        if p.lower().endswith(".pdf") and HAVE_FITZ:
            try:
                d = fitz.open(p)
                return "\n".join(pg.get_text() for pg in d)
            except Exception:
                return None
        return open(p, encoding="utf-8", errors="replace").read()
    r = subprocess.run(["git", "cat-file", "blob", f"HEAD:{path}"],
                       cwd=RES, capture_output=True, timeout=300)
    if r.returncode == 0:
        return r.stdout.decode("utf-8", errors="replace")
    return None

def fuzz_best(nq, texts):
    best, where = 0.0, None
    for name, t in texts.items():
        nt = norm(t)
        if not nt:
            continue
        # windowed comparison for long texts
        L = len(nq)
        step = max(1000, L)
        for i in range(0, max(1, len(nt) - L + 1), step):
            seg = nt[i:i + L + 200]
            r = difflib.SequenceMatcher(None, nq, seg).ratio()
            if r > best:
                best, where = r, name
    return best, where

fails = json.load(open(RECEIPT))["L3_quotes"]["fail_detail"]
pack_texts_cache, raw_cache = {}, {}
result = []
counts = collections.Counter()
for ent in fails:
    art, q = ent["artifact"], ent["quote"]
    nq = norm(q)
    pp = pack_path_for(art)
    texts = {}
    if pp:
        key = pp
        if key not in pack_texts_cache:
            pack_texts_cache[key] = [(f["repo"], f["path"], f["excerpts"]) for f in pack_files(pp)]
        for repo, path, exc in pack_texts_cache[key]:
            texts[f"pack:{path}"] = "\n".join(e.get("text", "") for e in exc)
    hit = [n for n, t in texts.items() if nq in norm(t)]
    if hit:
        counts["BINDS_PACK"] += 1
        result.append({"artifact": art, "quote": q[:120], "verdict": "BINDS_PACK", "where": hit[0]})
        continue
    # raw plane
    raw_texts = {}
    if pp:
        for repo, path, exc in pack_texts_cache[pp]:
            ck = (repo, path)
            if ck not in raw_cache:
                raw_cache[ck] = read_raw(repo, path)
            if raw_cache[ck]:
                raw_texts[f"raw:{repo}:{path}"] = raw_cache[ck]
    hit_raw = [n for n, t in raw_texts.items() if nq in norm(t)]
    if hit_raw:
        counts["BINDS_RAW_window_miss"] += 1
        result.append({"artifact": art, "quote": q[:120], "verdict": "BINDS_RAW_window_miss",
                       "where": hit_raw[0]})
        continue
    ratio, where = fuzz_best(nq, {**texts, **raw_texts})
    if ratio >= 0.90:
        counts[f"FUZZY_{int(ratio*100)/100:.2f}"] += 1
        result.append({"artifact": art, "quote": q[:120], "verdict": "FUZZY",
                       "ratio": round(ratio, 3), "where": where})
    else:
        counts["UNRESOLVED"] += 1
        result.append({"artifact": art, "quote": q[:120], "verdict": "UNRESOLVED",
                       "best_ratio": round(ratio, 3), "best_where": where})

json.dump({"have_fitz": HAVE_FITZ, "counts": dict(counts), "detail": result},
          open(OUT, "w"), indent=1)
print("have_fitz:", HAVE_FITZ)
print("ADJUDICATION:", dict(counts))
for r in result:
    if r["verdict"] in ("UNRESOLVED", "BINDS_RAW_window_miss"):
        print(f"  [{r['verdict']}] {r['artifact']}: {r['quote'][:90]}"
              + (f" ratio={r.get('best_ratio')}" if "best_ratio" in r else "")
              + (f" -> {r.get('where','')[:60]}" if r.get("where") else ""))
