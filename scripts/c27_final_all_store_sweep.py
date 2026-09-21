#!/usr/bin/env python3
"""C27: FINAL all-store integrity sweep at the closing head (read-only battery).

Scope:
  S0  repo/remote consistency (HEAD == origin/main, clean tree)
  S1  graph/ 10 stores: YAML parse + damage-class scan + meta/lineage audit
  S2  counts + canonical equality vs Official-Specifications/parsed/igcse-chemistry/
      (every store-vs-canonical deviation must be documented in C26_WORDING_DIFF_LEDGER)
  S3  reference integrity (relationships, chunk mappings, command kinds, concepts, concept_edges)
  S4  sha256 pin verification (C25 + C26 record pins)
  S5  _derived/graph: 23 quals x 4 files KG-loader contract, parse + damage scan
  S6  parsed/: 23 parse_reports gate status + canonical JSON parse + official PDF sha1
  S7  knowledge-graph HTML freshness (FileUpload v76-audit-fixes)

Doctrine: damage is flagged, never fixed. En-dash / curly quotes adopted by C26 are
legitimate. Output: console gate table + JSON + MD record.
"""
import hashlib, json, os, re, subprocess, sys
from collections import Counter
import yaml

REPO = "/home/z/my-project/gh_repos/syllabai-resources"
sys.path.insert(0, os.path.join(REPO, "scripts"))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths
DL = "/home/z/my-project/download"
FU = "/home/z/my-project/gh_repos/FileUpload"
KG_DIR = os.path.join(FU, "syllabai-openhuman-edexcel-chemistry-kg")
PARSE = os.path.join(REPO, "Official-Specifications/parsed")
CANON = os.path.join(PARSE, "igcse-chemistry")
GRAPH = str(GP.qual_dir())  # C28 registry-resolved ratified store dir
PDF_SHA1 = "3ad641b7c60b314fa3b10680feda30bf56280a53"

RESULTS = []  # (section, name, status, detail)

def gate(section, name, ok, detail="", warn_only=False):
    status = "PASS" if ok else ("WARN" if warn_only else "FAIL")
    RESULTS.append((section, name, status, detail))
    return ok

def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()

def nkey(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def sha1(p):
    h = hashlib.sha1()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

# ---------- damage classes ----------
RX = {
    "cjk_ideograph": re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]"),
    "kana_bopomofo": re.compile(r"[\u3040-\u30ff\u3100-\u312f]"),
    "cjk_punct": re.compile(r"[\u3000-\u303f\ufe30-\ufe4f]"),
    "fullwidth_form": re.compile(r"[\uff01-\uff5e\uff58-\uff65]"),
    "replacement_char": re.compile("\ufffd"),
    "literal_u_escape": re.compile(r"\\u[0-9a-fA-F]{4}"),
    "control_char": re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]"),
    "latex_inline_math": re.compile(r"\$[^$\n]{1,120}\$"),
    "mojibake_marker": re.compile(r"Ã[\x80-\xbf€‚ƒ„…†‡ˆ‰Š‹ŒŽ‘’“”•–—˜™š›œžŸ°]|â€[\x80-\xbfœž™š€˜’“”]|Â[\xa0°©®·»«]"),
}

def damage_scan_strings(obj, path="$"):
    """Yield (path, class, sample) for every string scalar hit."""
    if isinstance(obj, str):
        for cls, rx in RX.items():
            m = rx.search(obj)
            if m:
                yield (path, cls, obj[max(0, m.start() - 25):m.end() + 25])
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from damage_scan_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from damage_scan_strings(v, f"{path}[{i}]")

def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from walk_strings(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk_strings(v)

# ---------- S0 repo/remote ----------
def s0():
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=REPO, capture_output=True, text=True).stdout.strip()
    remote = subprocess.run(["git", "rev-parse", "origin/main"], cwd=REPO, capture_output=True, text=True).stdout.strip()
    st = subprocess.run(["git", "status", "--porcelain"], cwd=REPO, capture_output=True, text=True).stdout.strip()
    gate("S0", "HEAD == origin/main", head == remote, f"head={head[:8]} remote={remote[:8]}")
    gate("S0", "working tree clean", st == "", st.splitlines()[:3] if st else "0 dirty paths")
    import check_no_hardcode as cnh  # C28 §3.2 mechanical no-hardcode + registry gates
    bad, _allowed = cnh.scan()
    gate("S0", "no-hardcode: legacy store paths extinct from tooling (C28 §3.2)", not bad,
         "0 hits outside registry allowlist" if not bad else str(bad[:4]))
    reg_ok, reg_detail = cnh.registry_consistency()
    gate("S0", "graph-path registry consistency (C28 §3.2)", reg_ok, reg_detail)
    return head, remote

# ---------- S1 graph stores ----------
STORES = ["specification_points", "topics", "practicals", "assessment_objectives",
          "command_words", "relationships", "concepts", "concept_edges",
          "spec_chunk_mappings", "spec_command_kinds"]

def load_stores():
    stores = {}
    for s in STORES:
        p = os.path.join(GRAPH, f"{s}.yaml")
        stores[s] = yaml.safe_load(open(p, encoding="utf-8"))
    return stores

def s1(stores):
    for s in STORES:
        raw = open(os.path.join(GRAPH, f"{s}.yaml"), encoding="utf-8").read()
        gate("S1", f"parse {s}.yaml", s in stores and isinstance(stores[s], dict))
        hits = list(damage_scan_strings(stores[s]))
        gate("S1", f"damage-scan {s}.yaml", not hits,
             "; ".join(f"{p}:{c}" for p, c, _ in hits[:4]) if hits else "0 hits")
        gate("S1", f"no 'md OCR' residue {s}.yaml", "md ocr" not in raw.lower(), "clean" if "md ocr" not in raw.lower() else "FOUND")
    meta = stores["specification_points"]["meta"]
    pol = meta.get("statement_text_policy", "")
    gate("S1", "spec_points policy = PDF-direct line",
         pol.startswith("verbatim from the official PDF (canonical PDF-direct parse") and "never fixed" in pol,
         pol[:90] + "…")
    sd = meta.get("source_documents", [])
    pdf_ok = any(d.get("role") == "official-pdf" and d.get("sha1") == PDF_SHA1 for d in sd)
    gate("S1", "spec_points source_documents pins official PDF sha1", pdf_ok, PDF_SHA1[:16] + "…")
    rl = (meta.get("definitive_lineage") or {}).get("retired_lineage") or {}
    gate("S1", "retired_lineage documented (OCR md + c09)",
         bool(rl.get("source_file")) and "c09" in str(rl.get("generated_by", "")),
         f"retired={rl.get('source_file', '?')[:60]}")
    gens = {s: (stores[s].get("meta") or {}).get("generator") for s in STORES}
    c09_active = [s for s, g in gens.items() if g and "c09" in str(g)]
    gate("S1", "no store names retired c09 as generator", not c09_active,
         "; ".join(f"{s}:{g}" for s, g in gens.items() if g) if not c09_active else f"c09 active: {c09_active}")
    # informational: per-record provenance still citing the retired md = historical, documented
    hist = 0
    for e in stores["relationships"]["edges"]:
        pr = e.get("provenance") or {}
        if "md" in str(pr.get("source_file", "")):
            hist += 1
    RESULTS.append(("S1", "INFO per-edge provenance citing retired md (history, in-scope of C26 meta-only refresh)", "INFO", f"{hist}/210 edges"))

# ---------- S2 counts + canonical equality ----------
def s2(stores):
    ledger = json.load(open(os.path.join(GRAPH, "reports/C26_WORDING_DIFF_LEDGER.json"), encoding="utf-8"))
    allowed = {}
    for k in ("wording_changes", "field_adoption", "identity_changes"):
        for it in ledger.get(k, []):
            allowed[(it["store"], it["code"], it["field"])] = it["new"]

    def deviates(store, code, field, store_val, canon_val, new_expected_from="ledger"):
        """Return None if OK (equal or documented deviation matching ledger 'new')."""
        if norm(store_val) == norm(canon_val):
            return None
        key = (store, code, field)
        if key in allowed:
            if norm(store_val) == norm(allowed[key]):
                return None
            return f"documented but store value != ledger new: {store_val!r} vs {allowed[key]!r}"
        return f"UNDOCUMENTED diff: store={store_val!r} canon={canon_val!r}"

    # --- spec_points ---
    sp = stores["specification_points"]["specification_points"]
    canon = json.load(open(os.path.join(CANON, "spec_points.json"), encoding="utf-8"))
    cs = canon["spec_points"]
    gate("S2", "spec_points count 182 == canonical", len(sp) == len(cs) == 182, f"store={len(sp)} canon={len(cs)}")
    cmap = {}
    dup = []
    for r in cs:
        oc = r["official_code"]
        if oc in cmap:
            dup.append(oc)
        cmap[oc] = r["text"]
    gate("S2", "canonical official_code unique", not dup, f"dups={dup[:5]}")
    missing = [r["official_code"] for r in sp if r["official_code"] not in cmap]
    gate("S2", "all store spec codes exist in canonical", not missing, f"missing={missing[:5]}")
    diffs = []
    for r in sp:
        t = cmap.get(r["official_code"])
        if t is not None and norm(r["official_wording"]) != norm(t):
            diffs.append((r["code"], r["official_wording"], t))
    gate("S2", "spec_points wording == canonical (182/182, whitespace-normalised)", not diffs,
         "0 wording diffs" if not diffs else f"{len(diffs)} e.g. {diffs[0][0]}")
    c_points = sum(1 for r in sp if r.get("c_point"))
    gate("S2", "c_points = 52", c_points == 52, f"{c_points}")
    prac_flagged = sum(1 for r in sp if r.get("practical"))
    RESULTS.append(("S2", "INFO spec records flagged practical", "INFO", f"{prac_flagged}"))

    # --- topics / subtopics ---
    tp = stores["topics"]
    canT = json.load(open(os.path.join(CANON, "topics.json"), encoding="utf-8"))
    ctopics = sorted(canT["topics"], key=lambda r: r.get("ordering", 0))
    csubs = sorted(canT["subsections"], key=lambda r: (r.get("page", 0), r.get("oy", 0)))
    gate("S2", "topics 4 records (content topics)", len(tp["topics"]) == 4, f"{len(tp['topics'])}")
    gate("S2", "subtopics 28 == canonical subsections", len(tp["subtopics"]) == len(csubs) == 28,
         f"store={len(tp['subtopics'])} canon={len(csubs)}")
    ctitles = {norm(t["title"]) for t in ctopics}
    bad = [t["code"] for t in tp["topics"] if norm(t["title"]) not in ctitles]
    gate("S2", "topic titles ∈ canonical titles", not bad, f"offending={bad}")
    pair = []
    for st_r, cn_r in zip(tp["subtopics"], csubs):
        if st_r["letter"] != cn_r["letter"] or norm(st_r["title"]) != norm(cn_r["title"]):
            pair.append((st_r["code"], st_r["letter"], cn_r["letter"], st_r["title"], cn_r["title"]))
    gate("S2", "subtopics 1:1 (letter+title) vs canonical order", not pair and len(tp["subtopics"]) == 28,
         "28/28 aligned" if not pair else str(pair[:2]))
    badp = [s["code"] for s in tp["subtopics"] if s.get("parent") not in {t["code"] for t in tp["topics"]}]
    gate("S2", "subtopic parents resolve", not badp, f"bad={badp[:5]}")

    # --- practicals ---
    # documented C23/C26 rule: canonical summary's 'practical: ' label prefix is stripped
    # in the store (leading-verb rule; scripts/c26_field_map.yaml practicals.yaml note)
    pr = stores["practicals"]["practicals"]
    canP = json.load(open(os.path.join(CANON, "practicals.json"), encoding="utf-8"))
    cpr = sorted(canP["practicals"], key=lambda r: r.get("ordering", 0))
    gate("S2", "practicals 12 == canonical", len(pr) == len(cpr) == 12, f"store={len(pr)} canon={len(cpr)}")
    prefix_stripped = 0
    diffs = []
    for st_r, cn_r in zip(pr, cpr):
        csum = cn_r["summary"]
        if csum.lower().startswith("practical:") and not st_r["summary"].lower().startswith("practical:"):
            csum = csum[len("practical:"):].strip()
            prefix_stripped += 1
        d = deviates("practicals.yaml", st_r["code"], "summary", st_r["summary"], csum)
        if d:
            diffs.append((st_r["code"], d))
    gate("S2", "practical summaries == canonical minus 'practical: ' label (diff ⊆ C26 ledger)", not diffs,
         f"12/12 (label prefix stripped on {prefix_stripped}; incl. documented PR repairs)" if not diffs else str(diffs[:3]))

    # --- assessment objectives ---
    ao = stores["assessment_objectives"]["assessment_objectives"]
    canA = json.load(open(os.path.join(CANON, "assessment_objectives.json"), encoding="utf-8"))
    caomap = {r["ao"]: r for r in canA["statements"]}
    gate("S2", "AO 3 statements", len(ao) == 3 and len(caomap) == 3, f"store={len(ao)} canon={len(caomap)}")
    diffs = []
    for r in ao:
        suffix = r["code"].rsplit("-", 1)[-1]
        cr = caomap.get(suffix)
        if not cr:
            diffs.append((r["code"], "no canonical match")); continue
        for sf, cf in (("title", "description"), ("weighting_overall", "weighting_overall")):
            d = deviates("assessment_objectives.yaml", r["code"], sf, r.get(sf), cr.get(cf))
            if d:
                diffs.append((r["code"], sf, d))
    gate("S2", "AO title + weighting_overall == canonical (en-dash verbatim)", not diffs,
         "3/3" if not diffs else str(diffs[:3]))
    # canonical matrix: rows = papers, columns = AO1..AO3 (PDF p35 'Relationship of
    # assessment objectives to units'); store = one anchored matrix aliased into all 3 records
    uw = [u for u in canA["unit_weightings"] if not str(u["unit"]).lower().startswith("total")]
    gate("S2", "canonical unit_weightings = 2 paper rows", len(uw) == 2, f"{len(uw)}")
    exp = {"paper_1": {"ao1": uw[0]["weightings"][0], "ao2": uw[0]["weightings"][1], "ao3": uw[0]["weightings"][2]},
           "paper_2": {"ao1": uw[1]["weightings"][0], "ao2": uw[1]["weightings"][1], "ao3": uw[1]["weightings"][2]}}
    wdiffs = []
    for r in ao:
        if r.get("weighting_by_paper") != exp:
            wdiffs.append((r["code"], r.get("weighting_by_paper")))
    gate("S2", "AO weighting_by_paper == canonical full matrix (PDF p35; C27 repair)", not wdiffs,
         "3/3 records share the corrected anchored matrix" if not wdiffs else str(wdiffs[:2]))
    papers = stores["assessment_objectives"].get("papers") or []
    ratified = sum(1 for p in papers if "ratified" in json.dumps(p.get("provenance", {})).lower())
    gate("S2", "papers block = 2 papers (P1C/P2C) with ratified-overlay provenance",
         len(papers) == 2 and ratified == 2,
         f"{len(papers)} papers ({', '.join(p.get('paper_code', '?') for p in papers)}), {ratified} ratified-overlay")

    # --- command words ---
    cw = stores["command_words"]["command_words"]
    canC = json.load(open(os.path.join(CANON, "command_words.json"), encoding="utf-8"))
    ccmap = {nkey(r["command_word"]): r for r in canC["command_words"]}
    gate("S2", "command_words 25 == canonical", len(cw) == len(canC["command_words"]) == 25,
         f"store={len(cw)} canon={len(canC['command_words'])}")
    diffs, unmatched = [], []
    for r in cw:
        cr = ccmap.get(nkey(r["command_word"]))
        if not cr:
            unmatched.append(r["command_word"]); continue
        if norm(r["command_word"]) != norm(cr["command_word"]):
            d = deviates("command_words.yaml", r["code"], "command_word", r["command_word"], cr["command_word"])
            if d: diffs.append((r["code"], d))
        d = deviates("command_words.yaml", r["code"], "definition", r["definition"], cr["definition"])
        if d: diffs.append((r["code"], d))
    gate("S2", "command words 1:1 punctuation-insensitive join", not unmatched, f"unmatched={unmatched[:5]}")
    gate("S2", "command word + definition == canonical (diff ⊆ C26 ledger)", not diffs,
         "25/25 (incl. 7 documented definition repairs)" if not diffs else str(diffs[:3]))
    return cmap

# ---------- S3 reference integrity ----------
def s3(stores):
    sp = stores["specification_points"]["specification_points"]
    spec_ids = {r["code"] for r in sp} | {r["official_code"] for r in sp} | {"IGCSE_CHEMISTRY:" + r["official_code"] for r in sp}
    topic_ids = {t["code"] for t in stores["topics"]["topics"]}
    sub_ids = {s["code"] for s in stores["topics"]["subtopics"]}
    prac_ids = {p["code"] for p in stores["practicals"]["practicals"]}
    ao_ids = {a["code"] for a in stores["assessment_objectives"]["assessment_objectives"]}
    cw_ids = {c["code"] for c in stores["command_words"]["command_words"]}
    node_ids = spec_ids | topic_ids | sub_ids | prac_ids | ao_ids | cw_ids

    edges = stores["relationships"]["edges"]
    gate("S3", "relationships edges = 210", len(edges) == 210, f"{len(edges)}")
    bad = sorted({e[k] for e in edges for k in ("from", "to") if e[k] not in node_ids})
    distinct = {e[k] for e in edges for k in ("from", "to")}
    gate("S3", "all relationship endpoints resolve", not bad,
         f"{len(distinct)} distinct endpoints, 0 unresolved" if not bad else f"unresolved={bad[:6]}")
    gate("S3", "distinct endpoints = 214 (C26 pin)", len(distinct) == 214, f"{len(distinct)}")
    refs = Counter()
    for s in stores["topics"]["subtopics"]:
        for r in s.get("spec_points", []) or []:
            refs[r] += 1
    badrefs = [r for r in refs if r not in spec_ids]
    gate("S3", "subtopic→spec_point refs resolve", not badrefs,
         f"{len(refs)} refs across 28 subtopics, 0 unresolved" if not badrefs else f"bad={badrefs[:5]}")
    badpr = [p["code"] for p in stores["practicals"]["practicals"] if p.get("spec_point") not in spec_ids]
    gate("S3", "practical→spec_point refs resolve", not badpr, f"bad={badpr[:5]}")

    cm = stores["spec_chunk_mappings"]["rows"]
    badcm = sorted({r["spec_code"] for r in cm if r["spec_code"] not in spec_ids})
    sp_wording = {r["code"]: r["official_wording"] for r in sp}
    titlediff = [r["mapping_id"] for r in cm if norm(r.get("sp_title")) != norm(sp_wording.get(r["spec_code"], ""))]
    gate("S3", "chunk-map sp_title == definitive store wording (211/211; C27 refresh)", not titlediff,
         "211/211 aligned to definitive wording" if not titlediff else f"drift={titlediff[:5]}")
    worklist = [r for r in cm if str(r.get("disposition", "")).upper().startswith("WORKLIST") or r.get("validation_status") == "SUGGESTED"]
    mapped = [r for r in cm if r not in worklist]
    noq = [r["mapping_id"] for r in mapped if not norm(r.get("evidence_quote", ""))]
    gate("S3", "chunk-map spec_codes resolve", not badcm,
         f"{len(cm)} rows, 0 unresolved" if not badcm else f"bad={badcm[:5]}")
    gate("S3", "chunk-map evidence quotes non-empty on mapped rows",
         not noq,
         f"{len(mapped)}/{len(cm)} mapped rows all quoted; {len(worklist)} registered WORKLIST gaps (empty by design)" if not noq else f"empty={noq[:5]}")
    missing_notes = [r["note_path"] for r in cm if r.get("note_path") and not os.path.exists(os.path.join(REPO, r["note_path"]))]
    RESULTS.append(("S3", "INFO chunk-map note_paths on disk", "INFO",
                     f"{len(cm) - len(missing_notes)}/{len(cm)} present" + (f"; missing e.g. {missing_notes[:2]}" if missing_notes else "")))

    ck = stores["spec_command_kinds"]["command_kinds"]
    verbs = {r["leading_verb"] for r in sp}
    badck = sorted({r["code"] for r in ck if r["code"] not in spec_ids})
    badv = sorted({r["verb"] for r in ck if r["verb"] not in verbs})
    gate("S3", "command-kind codes resolve into spec points", not badck,
         f"{len(ck)} kinds, 0 unresolved" if not badck else f"bad={badck[:5]}")
    gate("S3", "command-kind verbs ∈ spec leading_verb set", not badv,
         f"verbs={len({r['verb'] for r in ck})} all known" if not badv else f"unknown={badv[:8]}")

    cn = stores["concepts"]["nodes"]
    con_ids = {n["code"] for n in cn}
    def ref_codes(r):
        if isinstance(r, dict):
            return r.get("code")
        return r
    crefs = [ref_codes(r) for n in cn for r in (n.get("spec_points") or [])]
    badsp = sorted({r for r in crefs if r and r not in spec_ids})
    gate("S3", "concept→spec_point refs resolve", not badsp,
         f"{len(crefs)} refs across {len(cn)} concepts, 0 unresolved" if not badsp else f"bad={badsp[:5]}")
    ce = stores["concept_edges"]["edges"]
    ce_ids = con_ids | spec_ids | prac_ids | topic_ids | sub_ids | ao_ids
    badce = sorted({e[k] for e in ce for k in ("source", "target") if e[k] not in ce_ids})
    gate("S3", "concept_edges endpoints resolve (concepts ∪ spec ∪ practicals ∪ topics)", not badce,
         f"{len(ce)} edges, 0 unresolved" if not badce else f"bad={badce[:5]}")
    evfiles = [ev.get("file") for e in ce for ev in (e.get("evidence") or []) if isinstance(ev, dict) and ev.get("file")]
    missing_ev = [f for f in evfiles if f and not os.path.exists(os.path.join(REPO, f))]
    RESULTS.append(("S3", "INFO concept-edge evidence files on disk", "INFO",
                    f"{len(evfiles) - len(missing_ev)}/{len(evfiles)} present" + (f"; missing e.g. {missing_ev[:2]}" if missing_ev else "")))

# ---------- S4 pins ----------
PINS = {
    GP.legacy_rel("specification_points"): "956d276f6e4354fa",
    GP.legacy_rel("topics"): "81a4745760bcce2c",
    GP.legacy_rel("practicals"): "8e0ab9c471937688",
    GP.legacy_rel("assessment_objectives"): "3dc670176f2f5529",  # C27 post (C26 post was 36f361ec…; matrix repair)
    GP.legacy_rel("command_words"): "824c50ee0625672c",
    GP.legacy_rel("relationships"): "6bd3f8236ac2120a",
    GP.legacy_rel("concepts"): "5904c7bc956d6858",  # C28 post (pre was 634a743b65d1612b…; layout canonicalization)
    GP.legacy_rel("concept_edges"): "ca73f7077ba82cc0",  # C28 post (pre was ccc674cf3a94b8e4…; layout canonicalization)
    GP.legacy_rel("spec_chunk_mappings"): "e8b58a7109104bb7",  # C28 post (pre was f36910450bd50726…; layout canonicalization)  # C27 post (pre was 3d4877dd…; sp_title refresh)
    "graph/reports/C26_WORDING_DIFF_LEDGER.json": "b3334f6057ea649a",
    "scripts/c26_emit_definitive_sibling_stores.py": "e9cbf844e9247c07",  # C28 stage-1 re-point (pre was c4ad56a1…; registry refactor)
    "scripts/c26_postcheck.py": "e506e0c9d4478523",  # C28 stage-1 re-point (pre was b309c07b…; registry refactor)
    "scripts/c26_field_map.yaml": "fbbd8836a75d67dd",
    "scripts/c23_emit_definitive_specpoints.py": "886df71645a57bc4",  # C28 stage-1 re-point (pre was 135452dd…; registry refactor)
    "scripts/c09_spec_graph_extract.py": "cf27444eb2ee57c4",
}
def s4():
    bad = []
    for rel, pin in PINS.items():
        p = os.path.join(REPO, GP.resolve_rel(rel))  # C28: legacy pin labels -> canonical paths
        if not os.path.exists(p):
            bad.append((rel, "MISSING")); continue
        cur = sha256(p)[:16]
        if cur != pin:
            bad.append((rel, f"{cur} != {pin}"))
    gate("S4", f"C25+C26+C27 sha256 pins ({len(PINS)} files)", not bad,
         f"{len(PINS)}/{len(PINS)} match" if not bad else str(bad))

# ---------- S5 derived ----------
def s5():
    root = os.path.join(PARSE, "_derived/graph")
    quals = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)))
    gate("S5", "23 quals in _derived/graph", len(quals) == 23, f"{len(quals)}")
    files_needed = ["topics.yaml", "practicals.yaml", "relationships.yaml", "specification_points.yaml"]
    missing, parse_fail, dmg, mdocr = [], [], [], []
    total_points = 0
    for q in quals:
        for f in files_needed:
            p = os.path.join(root, q, f)
            if not os.path.exists(p):
                missing.append(f"{q}/{f}"); continue
            try:
                d = yaml.safe_load(open(p, encoding="utf-8"))
            except Exception as ex:
                parse_fail.append(f"{q}/{f}: {ex}"); continue
            hits = list(damage_scan_strings(d))
            if hits:
                dmg.append(f"{q}/{f}: " + "; ".join(f"{c}" for _, c, _ in hits[:3]))
            raw_p = p
            if "md ocr" in open(raw_p, encoding="utf-8").read().lower():
                mdocr.append(f"{q}/{f}")
            if f == "specification_points.yaml":
                pts = d.get("specification_points") or d.get("spec_points") or []
                total_points += len(pts) if isinstance(pts, list) else 0
    gate("S5", "KG loader contract 4 files x 23 quals", not missing, f"92 files, missing={missing[:4]}")
    gate("S5", "derived YAML parse", not parse_fail, f"fail={parse_fail[:4]}")
    gate("S5", "derived damage sweep", not dmg, f"hits={dmg[:4]}")
    gate("S5", "derived no 'md OCR' residue", not mdocr, f"found={mdocr[:4]}")
    RESULTS.append(("S5", "INFO derived spec-point rows total", "INFO", f"{total_points} across 23 quals"))

# ---------- S6 parsed battery ----------
def s6():
    quals = sorted(d for d in os.listdir(PARSE) if os.path.isdir(os.path.join(PARSE, d)) and not d.startswith("_"))
    gate("S6", "23 qual parse bundles", len(quals) == 23, f"{len(quals)}")
    statuses, parse_fail = [], []
    for q in quals:
        pr = os.path.join(PARSE, q, "parse_report.json")
        if not os.path.exists(pr):
            statuses.append((q, "NO_REPORT")); continue
        try:
            d = json.load(open(pr, encoding="utf-8"))
        except Exception as ex:
            parse_fail.append(f"{q}: {ex}"); continue
        g = d.get("gates") or {}
        vals = [v for v in (g.values() if isinstance(g, dict) else g)]
        flag = None
        if isinstance(g, dict):
            bad = [k for k, v in g.items() if v not in (True, "PASS", "ALL_PASS", "pass", "ok")]
            flag = f"{len(g) - len(bad)}/{len(g)}" if not bad else f"FAILED gates={bad[:3]}"
        else:
            flag = str(g)[:60]
        statuses.append((q, flag))
    gate("S6", "canonical JSON parse x23", not parse_fail, f"fail={parse_fail[:3]}")
    badg = [s for s in statuses if s[1] in ("NO_REPORT",) or (isinstance(s[1], str) and ("FAILED" in s[1]))]
    gate("S6", "parse_reports gates ALL_PASS x23", not badg,
         "23/23 all gates pass" if not badg else str(badg[:4]))
    pdf = os.path.join(REPO, "Official-Specifications/igcse-chemistry/international-gcse-chemistry-2017-specification.pdf")
    cur = sha1(pdf)
    gate("S6", "official chemistry PDF sha1 unchanged", cur == PDF_SHA1, cur[:16] + "…")
    RESULTS.append(("S6", "INFO per-qual gate summary", "INFO", "; ".join(f"{q}:{s}" for q, s in statuses)))

# ---------- S7 KG HTML ----------
LATEST_V = 77
LATEST_NAME = "syllabai-openhuman-edexcel-chemistry-v77-regression-fixes.html"

def s7():
    for v, name in ((77, LATEST_NAME), (76, "syllabai-openhuman-edexcel-chemistry-v76-audit-fixes.html")):
        p = os.path.join(KG_DIR, name)
        ok = os.path.exists(p)
        gate("S7", f"v{v} present in FileUpload clone", ok, p if ok else "MISSING")
        dl = os.path.join(DL, name)
        if ok and os.path.exists(dl):
            gate("S7", f"v{v} download/ copy identical to repo copy", sha256(p) == sha256(dl),
                 f"sha256 {sha256(p)[:16]}…")
        else:
            gate("S7", f"v{v} download/ copy exists", os.path.exists(dl), dl)
    try:
        subprocess.run(["git", "fetch", "origin"], cwd=FU, capture_output=True, timeout=60)
        head = subprocess.run(["git", "rev-parse", "origin/main"], cwd=FU, capture_output=True, text=True).stdout.strip()
        local = subprocess.run(["git", "rev-parse", "HEAD"], cwd=FU, capture_output=True, text=True).stdout.strip()
        tracked = subprocess.run(["git", "ls-tree", "origin/main", "--",
                                  f"syllabai-openhuman-edexcel-chemistry-kg/{LATEST_NAME}"],
                                 cwd=FU, capture_output=True, text=True).stdout.strip()
        gate("S7", f"v{LATEST_V} tracked on FileUpload origin/main", bool(tracked), f"origin/main={head[:8]}")
        gate("S7", "local FileUpload clone == origin/main", head == local,
             f"local={local[:8]} remote={head[:8]}" if head != local else head[:8])
        log = subprocess.run(["git", "log", "--oneline", "-2", "origin/main"], cwd=FU, capture_output=True, text=True).stdout.strip()
        RESULTS.append(("S7", "INFO FileUpload origin/main tail", "INFO", log.replace(chr(10), " | ")))
    except Exception as ex:
        gate("S7", "FileUpload remote check", False, str(ex), warn_only=True)
    vers = []
    for f in os.listdir(KG_DIR):
        if f.endswith(".html"):
            m = re.search(r"-v(\d+)", f)
            if m:
                vers.append((int(m.group(1)), f))
    maxv = max(vers)[0] if vers else 0
    gate("S7", f"v{LATEST_V} is the max version in the kg folder", maxv == LATEST_V,
         f"max=v{maxv}; versions={sorted({v for v, _ in vers})}")

# ---------- main ----------
def main():
    os.chdir(REPO)
    head, remote = s0()
    stores = load_stores()
    s1(stores)
    s2(stores)
    s3(stores)
    s4()
    s5()
    s6()
    s7()
    os.makedirs(DL, exist_ok=True)
    n_pass = sum(1 for _, _, st, _ in RESULTS if st == "PASS")
    n_fail = sum(1 for _, _, st, _ in RESULTS if st == "FAIL")
    n_warn = sum(1 for _, _, st, _ in RESULTS if st == "WARN")
    print("=" * 100)
    for sec, name, st, det in RESULTS:
        mark = {"PASS": "✓", "FAIL": "✗", "WARN": "!", "INFO": "·"}[st]
        print(f"[{mark}] {sec} | {name}" + (f" — {det}" if det else ""))
    print("=" * 100)
    print(f"TOTAL: {n_pass} PASS / {n_fail} FAIL / {n_warn} WARN / {len(RESULTS) - n_pass - n_fail - n_warn} INFO")
    verdict = "ALL_STORES_CLEAN" if n_fail == 0 and n_warn == 0 else ("CLEAN_WITH_WARNINGS" if n_fail == 0 else "DEFECTS_FOUND")
    print(f"VERDICT: {verdict} @ head {head[:12]}")
    out = {"head": head, "origin_main": remote, "verdict": verdict,
           "counts": {"pass": n_pass, "fail": n_fail, "warn": n_warn,
                       "info": len(RESULTS) - n_pass - n_fail - n_warn},
           "results": [{"section": s, "check": n, "status": st, "detail": str(d)} for s, n, st, d in RESULTS]}
    json.dump(out, open("/home/z/my-project/scripts/c27_sweep_results.json", "w"), indent=1)
    sys.exit(0 if n_fail == 0 else 1)

if __name__ == "__main__":
    main()
