#!/usr/bin/env python3
"""SIB-ASSESS-r3-silver — INDEPENDENT silver-tier ER review verifier.

Fresh tooling written for this review: implements its own citation grammar,
pack chain and census logic from the corpus's primary artifacts. It does not
import or execute the pipeline validator (tools/sib); pipeline gate outputs
are used only as reconciliation comparators, never as evidence of correctness.

Legs implemented here (local, deterministic):
  L1 pack-of-record chain integrity (zero-append carry assertions, re-derived)
  L2 full-corpus citation resolution (all 95 published artifacts, not sampled)
  L3 quoted-span binding (verbatim membership in held excerpt text)
  L4 census arithmetic recount (records / words / medians)
  L5 T5 OCR-fidelity caveat audit (TUT family)
  L6 receipt/red-state coherence (scoreboard byte-identity, qa-reports 95/95)

Emits: JSON receipt + human verdict line per leg.
"""
import json, re, hashlib, glob, os, sys, statistics, collections

LIB = "/home/z/my-project/syllabai-resources/SubjectIntelligence/CHEMISTRY_4CH1"
OUT = "/home/z/my-project/syllabai-resources/SubjectIntelligence/CHEMISTRY_4CH1/runs/SIB-CHEMISTRY_4CH1-ASSESS-R3"
os.makedirs(OUT, exist_ok=True)

def sha256_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

# ---------------------------------------------------------------- inventory
def artifact_id_of(path):
    m = re.search(r"CHEMISTRY_4CH1_([A-Z]+-\d+)_", os.path.basename(path))
    return m.group(1) if m else None

published = sorted(glob.glob(os.path.join(LIB, "published", "*.md")))
art_ids = [artifact_id_of(p) for p in published]
fm_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)

def frontmatter(text):
    m = fm_re.match(text)
    out = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                out[k.strip()] = v.strip().strip('"')
    return out

# ---------------------------------------------------------------- L1 pack chain
def run_no(run_id):
    m = re.search(r"RUN-(\d+)", run_id or "")
    return int(m.group(1)) if m else -1

pack_timeline = {}          # art -> [(run_no, run_id, sha256)]
carry_asserts = []          # from D3 runs' pack_carry.json
for rd in sorted(glob.glob(os.path.join(LIB, "runs", "*"))):
    rid = os.path.basename(rd).replace("SIB-CHEMISTRY_4CH1-", "")
    for ev in sorted(glob.glob(os.path.join(rd, "evidence", "*", "evidence_pack.json"))):
        art = os.path.basename(os.path.dirname(ev))
        pack_timeline.setdefault(art, []).append((run_no(rid), rid, sha256_file(ev)))
carry_fail = []
for rd in sorted(glob.glob(os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-RUN-01[7-9]"))) + \
          sorted(glob.glob(os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-RUN-02[0-2]"))):
    pc = os.path.join(rd, "pack_carry.json")
    if not os.path.exists(pc):
        continue
    cj = json.load(open(pc))
    rid = cj.get("run_id", "")
    for ent in cj.get("carried", []):
        art, want, origin = ent["artifact_id"], ent["pack_sha256"], ent["origin_run"]
        actual = os.path.join(rd, "evidence", art, "evidence_pack.json")
        got = sha256_file(actual) if os.path.exists(actual) else None
        ok = (got == want)
        origin_pack = os.path.join(LIB, "runs", origin, "evidence", art, "evidence_pack.json")
        ok_origin = (os.path.exists(origin_pack) and sha256_file(origin_pack) == want)
        carry_asserts.append({"run": rid, "artifact": art, "assert_ok": ok, "origin_ok": ok_origin})
        if not (ok and ok_origin):
            carry_fail.append({"run": rid, "artifact": art, "want": want, "got": got,
                               "origin_ok": ok_origin})

# of-record pack = pack at the artifact's generation_run_id (front matter) if present,
# else the latest run's pack; require byte-identity across all D3-era copies (>=RUN-017)
pack_of_record, pack_chain_report = {}, []
for art, tl in pack_timeline.items():
    tl.sort()
    deep = [t for t in tl if t[0] >= 17]
    if deep:
        shas = {t[2] for t in deep}
        d3_ok = len(shas) == 1
    else:
        shas = {t[2] for t in tl}
        d3_ok = True  # artifact untouched by D3; chain report only
    rec = tl[-1]
    pack_of_record[art] = os.path.join(
        LIB, "runs", f"SIB-CHEMISTRY_4CH1-RUN-{rec[1].split('RUN-')[-1]}",
        "evidence", art, "evidence_pack.json")
    pack_chain_report.append({"artifact": art, "copies": len(tl),
                              "distinct_shas_all": len({t[2] for t in tl}),
                              "d3_byte_identical": d3_ok})

# ---------------------------------------------------------------- citation grammar
SRC_RE = re.compile(r"SRC-[A-Z0-9_-]+")
def top_level_groups(text):
    depth, start, out = 0, None, []
    for i, ch in enumerate(text):
        if ch == "(":
            if depth == 0:
                start = i
            depth += 1
        elif ch == ")":
            if depth == 1 and start is not None:
                out.append((start, i + 1))
            depth = max(0, depth - 1)
    return out

def parse_citations(text):
    toks = []
    for a, b in top_level_groups(text):
        seg = text[a + 1:b - 1]
        if "SRC-" not in seg:
            continue
        ids = list(SRC_RE.finditer(seg))
        for k, m in enumerate(ids):
            end = ids[k + 1].start() if k + 1 < len(ids) else len(seg)
            raw_id = m.group(0)
            tail = seg[m.end():end]
            tail = re.sub(r"\([^()]*\)", "", tail)  # drop nested prose parens
            if not re.fullmatch(r"SRC-[A-Z0-9_-]+", raw_id):
                continue
            loc = tail.split(",", 1)[1] if "," in tail else None
            if loc is None:
                toks.append({"src": raw_id, "locator": None, "form": "identity",
                             "token": seg[m.start():end].strip()})
                continue
            loc = " ".join(loc.split()).strip()
            if not loc:
                toks.append({"src": raw_id, "locator": None, "form": "identity",
                             "token": seg[m.start():end].strip()})
                continue
            toks.append({"src": raw_id, "locator": loc, "form": "located",
                         "token": seg[m.start():end].strip()})
    return toks

PATH_RE = re.compile(r"([A-Za-z0-9_\-./ ]+?\.(?:pdf|PDF|md|yaml|yml|jsonl|json))")
PAGE_RE = re.compile(r"\bpp?(\d+)(?:\s*[-–]\s*(\d+))?")
LOOSE_P_RE = re.compile(r"(?:^|[,\s])p(\d+)\b")
LINES_RE = re.compile(r"\blines?\s+(\d+)\s*(?:[-–]\s*(\d+))?", re.I)

def locator_directives(loc):
    """-> (path|None, [(kind, a, b)]) with kind in page/lines"""
    m = PATH_RE.search(loc)
    path = m.group(1).strip() if m else None
    dirs = []
    rest = loc[m.end():] if m else loc
    if path:
        pm = PAGE_RE.search(rest[:60]) or PAGE_RE.search(loc)
        if pm:
            a = int(pm.group(1)); b = int(pm.group(2) or pm.group(1))
            dirs.append(("page", a, b))
            extra = LOOSE_P_RE.findall(rest[pm.end():][:40])
            for e in extra:
                dirs.append(("page", int(e), int(e)))
        lm = LINES_RE.search(rest)
        if lm:
            a = int(lm.group(1)); b = int(lm.group(2) or lm.group(1))
            dirs.append(("lines", a, b))
        if not dirs:
            lm = LINES_RE.search(loc)
            if lm:
                a = int(lm.group(1)); b = int(lm.group(2) or lm.group(1))
                dirs.append(("lines", a, b))
    return path, dirs

def pack_index(pack_path):
    p = json.load(open(pack_path))
    src_ids, files = set(), []
    for s in p["sources"]:
        src_ids.add(s["source_id"])
        for f in s.get("files", []):
            exc = f.get("excerpts", [])
            pages, spans, linemap, blob = set(), [], {}, []
            for e in exc:
                locstr = e.get("locator", "")
                blob.append(e.get("text", ""))
                pm = re.search(r"page\s+(\d+)", locstr)
                if pm:
                    pages.add(int(pm.group(1)))
                lm = re.search(r"lines\s+(\d+)\s*[-–]\s*(\d+)", locstr)
                if lm:
                    spans.append((int(lm.group(1)), int(lm.group(2))))
                cm = re.match(r"line\s+(\d+)", locstr)
                if cm:
                    linemap[int(cm.group(1))] = e.get("text", "")
            files.append({"path": f["path"], "pages": pages, "spans": spans,
                          "linemap": linemap,
                          "text": "\n<<<EXC>>>\n".join(blob)})
    return {"src_ids": src_ids, "files": files}

def norm(s):
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2212", "-").replace("\u00a0", " ")
    s = s.replace("\ufb01", "fi").replace("\ufb02", "fl")
    s = s.replace("\u2010", "-").replace("\u2011", "-")
    return re.sub(r"\s+", " ", s).strip()

def _merge(spans):
    out = []
    for a, b in sorted(spans):
        if out and a <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out

def resolve_token(tok, idx):
    src = tok["src"]
    if src not in idx["src_ids"]:
        return "source_id_absent_from_pack", None
    if tok["locator"] is None:
        return None, "identity"
    loc = tok["locator"]
    # identity keyword
    if re.fullmatch(r"identity([, ].*)?", loc):
        return None, "identity"
    path, dirs = locator_directives(loc)
    if path is None:
        return None, "prose"
    cands = [f for f in idx["files"] if f["path"].endswith(path)]
    if not cands:
        cands = [f for f in idx["files"] if os.path.basename(f["path"]) == os.path.basename(path)]
    if not cands:
        return "locator_file_not_in_pack", None
    f = cands[0]
    for kind, a, b in dirs:
        if kind == "page":
            for n in range(a, b + 1):
                if n not in f["pages"]:
                    return f"page_not_held:{path}:p{n}", None
        elif kind == "lines":
            if a == b:
                if a not in f["linemap"] and not any(c <= a and d >= b for c, d in _merge(f["spans"])):
                    return f"lines_not_held:{path}:{a}", None
            elif not any(c <= a and d >= b for c, d in _merge(f["spans"])):
                return f"lines_not_held:{path}:{a}-{b}", None
    return None, "located"

def quote_spans(text, minlen=30):
    """Quoted prose spans from the BODY only (front matter stripped).
    Excludes identifiers, hashes, citation tokens and ellipsis spans."""
    body = fm_re.sub("", text, count=1) if fm_re.match(text) else text
    spans = []
    for m in re.finditer(r'"([^"\n]{30,600})"', body):
        spans.append(m.group(1))
    for m in re.finditer(r"\u201c([^\u201d\n]{30,600})\u201d", body):
        spans.append(m.group(1))
    out = []
    for s in spans:
        if "SRC-" in s or "..." in s or "\u2026" in s:
            continue
        if re.fullmatch(r"[A-Za-z0-9_\-./]{30,}", s):
            continue  # run ids / hex / paths
        out.append(s)
    return out

# ---------------------------------------------------------------- L2/L3 sweep
violations, forms = collections.Counter(), collections.Counter()
quote_fail, quote_ok = [], 0
per_art = []
recon = []
for pfile, art in zip(published, art_ids):
    text = open(pfile).read()
    idx = pack_index(pack_of_record[art]) if art in pack_of_record else None
    toks = parse_citations(text)
    stat = {"artifact": art, "tokens": len(toks), "identity": 0, "located": 0,
            "prose": 0, "violations": 0, "quotes": 0, "quote_fail": 0}
    if idx is None:
        stat["violations"] = -1
        per_art.append(stat)
        continue
    for t in toks:
        err, cls = resolve_token(t, idx)
        if err:
            stat["violations"] += 1
            violations[f"{art}: {t['token'][:60]} -> {err}"] += 1
            forms["VIOLATION"] += 1
        elif cls == "identity":
            stat["identity"] += 1; forms["identity"] += 1
        elif cls == "prose":
            stat["prose"] += 1; forms["prose"] += 1
        else:
            stat["located"] += 1; forms["located"] += 1
    for qs in quote_spans(text):
        nq = norm(qs)
        hit = any(nq in norm(f["text"]) for f in idx["files"])
        stat["quotes"] += 1
        if hit:
            quote_ok += 1
        else:
            stat["quote_fail"] += 1
            quote_fail.append({"artifact": art, "quote": nq[:110]})
    per_art.append(stat)

# ---------------------------------------------------------------- L4 census
fam_words, fam_records = collections.defaultdict(list), collections.defaultdict(int)
total_words = total_records = 0
req_words = req_records = req_arts = 0
rec_re = re.compile(r"^###\s+([A-Z]+)-(\d+)\b", re.M)
census_rows = []
for pfile, art in zip(published, art_ids):
    text = open(pfile).read()
    body = fm_re.sub("", text, count=1) if fm_re.match(text) else text
    ap = frontmatter(text)
    fam = art.split("-")[0]
    w = len(body.split())
    recs = rec_re.findall(text)
    fam_words[fam].append(w); fam_records[fam] += len(recs)
    total_words += w; total_records += len(recs)
    if ap.get("applicability") == "REQUIRED":
        req_words += w; req_records += len(recs); req_arts += 1
    census_rows.append({"artifact": art, "words": w, "records": len(recs),
                        "version": ap.get("artifact_version"),
                        "applicability": ap.get("applicability"),
                        "status": ap.get("status")})
medians = {f: int(statistics.median(v)) for f, v in sorted(fam_words.items())}

# ---------------------------------------------------------------- L5 OCR caveat
ocr_rows = []
for pfile, art in zip(published, art_ids):
    if art.startswith("TUT-"):
        text = open(pfile).read()
        ocr_rows.append({"artifact": art, "ocr_mentioned": "OCR" in text,
                         "sb1_mentioned": "SRC-BOOK-4CH1-SB1" in text})
gate_res = os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-RUN-021",
                        "gate_resolution_sb1_ebook.json")

# ---------------------------------------------------------------- L6 red state
sb_shas = {}
for rn in range(17, 23):
    p = os.path.join(LIB, "runs", f"SIB-CHEMISTRY_4CH1-RUN-{rn:03d}",
                     "post_lifecycle_scoreboard.json")
    sb_shas[f"RUN-{rn:03d}"] = sha256_file(p) if os.path.exists(p) else None
redstate_ok = len({v for v in sb_shas.values() if v}) == 1
qa_count = len(glob.glob(os.path.join(LIB, "qa-reports", "*.json")))
manifest_claim = {"SIB-MANI-007": 88, "SIB-MANI-011": 4, "SIB-MANI-012": 7}

def walk_counts(o, acc):
    if isinstance(o, dict):
        for k, v in o.items():
            if isinstance(v, int) and k.startswith("SIB-MANI"):
                acc[k] = acc.get(k, 0) + v
            else:
                walk_counts(v, acc)
    elif isinstance(o, list):
        for x in o: walk_counts(x, acc)

sb_counts, sb_topkeys = {}, {}
for rn in range(17, 23):
    p = os.path.join(LIB, "runs", f"SIB-CHEMISTRY_4CH1-RUN-{rn:03d}",
                     "post_lifecycle_scoreboard.json")
    if os.path.exists(p):
        sbj = json.load(open(p))
        acc = {}
        walk_counts(sbj, acc)
        sb_counts[f"RUN-{rn:03d}"] = acc
        sb_topkeys[f"RUN-{rn:03d}"] = sorted(sbj.keys()) if isinstance(sbj, dict) else ["<list>"]
redstate_ok = all(c == manifest_claim for c in sb_counts.values())

# F4a red-state stability: scoreboards vs RUN-016 of-record, modulo run_id stamp
p16 = os.path.join(LIB, "runs", "SIB-CHEMISTRY_4CH1-RUN-016", "report_post_lifecycle.json")

def _strip_runid(o):
    if isinstance(o, dict):
        return {k: ("<RUN>" if k == "run_id" else _strip_runid(v)) for k, v in o.items()}
    if isinstance(o, list):
        return [_strip_runid(x) for x in o]
    return o

f4a_variants = {}
if os.path.exists(p16):
    f4a_variants["RUN-016"] = json.dumps(_strip_runid(json.load(open(p16))), sort_keys=True)
for rn in range(17, 23):
    p = os.path.join(LIB, "runs", f"SIB-CHEMISTRY_4CH1-RUN-{rn:03d}",
                     "post_lifecycle_scoreboard.json")
    if os.path.exists(p):
        f4a_variants[f"RUN-{rn:03d}"] = json.dumps(_strip_runid(json.load(open(p))), sort_keys=True)
f4a_ok = dict(collections.Counter(f4a_variants.values()))

# ---------------------------------------------------------------- receipt
receipt = {
    "schema": "sib-assess-r3-silver/1.0",
    "review": "independent silver-tier ER review (operator trace 1a18bf09d58eea5d)",
    "independence": "fresh verifier, no pipeline gate code executed; pipeline outputs used only for reconciliation",
    "corpus": {"published": len(published), "artifacts": len(art_ids)},
    "L1_pack_chain": {
        "carry_asserts": len(carry_asserts),
        "carry_fail": carry_fail,
        "artifacts": len(pack_chain_report),
        "non_d3_identical": [r for r in pack_chain_report if not r["d3_byte_identical"]],
    },
    "L2_citations": {
        "total_tokens": sum(a["tokens"] for a in per_art),
        "forms": dict(forms),
        "violation_detail": dict(violations),
        "per_artifact": per_art,
    },
    "L3_quotes": {"ok": quote_ok, "fail": len(quote_fail),
                  "fail_by_family": dict(collections.Counter(
                      x["artifact"].split("-")[0] for x in quote_fail)),
                  "fail_detail": quote_fail[:200]},
    "L4_census": {
        "published_files": len(published),
        "records_total": total_records,
        "required_core": {"artifacts": req_arts, "words": req_words, "records": req_records},
        "words_total_all": total_words,
        "family_medians": medians,
        "rows": census_rows,
    },
    "L5_ocr": {"tut": ocr_rows, "gate_resolution_present": os.path.exists(gate_res)},
    "L6_redstate": {"scoreboard_shas": sb_shas, "file_byte_identical_17_22": len(set(sb_shas.values())) == 1,
                    "per_run_manifest_counts": sb_counts,
                    "redstate_counts_match_F4a_all_runs": redstate_ok,
                    "modulo_runid_form_counts": f4a_ok,
                    "top_key_variance": sb_topkeys,
                    "qa_reports": qa_count},
}
with open(os.path.join(OUT, "silver_receipt.json"), "w") as f:
    json.dump(receipt, f, indent=1)

print("== SIB-ASSESS-r3-silver (independent verifier) ==")
print(f"published: {len(published)}")
print(f"L1 pack chain: carry asserts {len(carry_asserts)}, FAIL {len(carry_fail)}, "
      f"non-D3-identical {len(receipt['L1_pack_chain']['non_d3_identical'])}")
print(f"L2 citations: {receipt['L2_citations']['total_tokens']} tokens, forms {dict(forms)}")
print(f"L3 quotes: ok {quote_ok}, FAIL {len(quote_fail)}")
print(f"L4 census: records {total_records}, REQUIRED-core {req_arts} arts / "
      f"{req_records} recs / {req_words} words; medians {medians}")
print(f"L5 OCR: TUT disclosed {sum(1 for r in ocr_rows if r['ocr_mentioned'])}/{len(ocr_rows)}, "
      f"gate_resolution present {os.path.exists(gate_res)}")
print(f"L6 redstate: F4a counts match all runs {redstate_ok}, "
      f"file-sha distinct {len(set(sb_shas.values()))}, qa-reports {qa_count}")
print(f"L6 modulo-run-id forms: { {v[:60]: k for k, v in f4a_variants.items()} }")
print(f"L6 modulo-run-id distinct forms: {len(f4a_ok)}")
