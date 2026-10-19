#!/usr/bin/env python3
"""
T-C09/T-C23 — graph_check.py: validator for the Phase-1 graph-as-code output
(graph/*.yaml; spec points now emitted by scripts/c23_emit_definitive_specpoints.py
from the PDF-direct-parse canonical JSON — definitive lineage per the operator's
2026-09-19 directive; the 2026-09-10 OCR-md lineage is retired and only its
provenance schema remains admissible for the not-yet-refreshed graph files).

Validates, with zero core-repo dependencies:
  1. file/schema      — all six YAML files parse; every record carries the
                        required keys with the right types and vocabularies
  2. namespace        — every node code and every edge endpoint is in the
                        4CH1-* namespace; no foreign curriculum codes
                        (WPH-style unit codes, IAL) anywhere; 4SD0 is allowed
                        in prose only (Double-Award applicability rule, spec
                        PDF pp. 7/13/14), never as a node code
  3. provenance       — every record has complete provenance (tier, source
                        file, spec issue, extraction method, generator, date,
                        md-line anchor where the record class requires one)
  4. referential      — every edge endpoint resolves to a declared node; the
                        210 PART_OF edges exactly cover 28 subtopic->topic +
                        182 spec_point->subtopic; subtopic.spec_points equals
                        exactly the points declaring that subsection
  5. consistency      — counts in meta match the records; orderings are
                        unique and contiguous; damage flags and skill tags
                        come from the declared vocabularies; the official
                        PDF cross-check has zero mismatches
  6. notes-mapping    — T-C10 state: all 112 SME notes carry a spec_map
                        front-matter block (PROVIDER subsection anchor from
                        the source-URL slug + AI_SUGGESTED point mappings with
                        complete provenance); every mapped code is in the
                        182-point registry; every note has >=1 mapping; no
                        foreign curriculum codes in front matter; all 182
                        points covered; totals match the T-C10 baseline
 10. c11-concepts    — T-C11 pilot (phase 3): graph/igcse-chemistry/concepts +
                        graph/igcse-chemistry/spec_command_kinds — node schema, 4CH1
                        namespace, families/roles/states/confidence caps,
                        evidence anchors byte-verified (T-C10 norm),
                        attachment rule (SPEC quote inside the SP wording or
                        a NOTE whose T-C10 mapping to that SP is
                        HUMAN_VALIDATED), pilot scope + 4.15 negative
                        control, misconception source-quote gate, frozen
                        command-kind tags (guide §8)
 11. c11-concept-edges — T-C11 pilot: graph/igcse-chemistry/concept_edges — relation
                        vocabulary, endpoint resolution (concepts ∪ pilot
                        SPs ∪ practicals), no self/duplicate edges, relation
                        discipline incl. the frozen §8A.11 misconception
                        triple distinction, REQUIRES_PREREQUISITE
                        acyclicity, PART_OF set == declared attachments,
                        anchor admissibility (NOTE anchors must resolve
                        through T-C10 HUMAN_VALIDATED coverage; MARK_SCHEME
                        anchors misconception-class only), anti-forgery
                        (no HUMAN_VALIDATED from generation; promoted edges
                        must match the operator-side promotion record
                        scripts/c11_promotions.yaml exactly — c11.13
                        validates that record and the frozen decision
                        record, always reading the REAL repo files so the
                        negative-test graph copies cannot cheat them)

Exit code 0 = all checks pass; 1 = failures (listed).
Usage: python3 scripts/graph_check.py [--graph DIR]
       python3 scripts/graph_check.py [--notes-root DIR]  (negative tests)
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from c10_worksheets import parse_slug, SECTION_LETTERS  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

REPO = Path(__file__).resolve().parent.parent
GRAPH_DEFAULT = GP.qual_dir()  # C28 registry-resolved ratified store dir
NOTES_ROOT_DEFAULT = REPO / "Chemistry IGCSE Revision Notes"

FILES = ["specification_points.yaml", "topics.yaml", "relationships.yaml",
         "command_words.yaml", "practicals.yaml", "assessment_objectives.yaml"]

GENERATOR = "scripts/c23_emit_definitive_specpoints.py"   # definitive lineage (T-C23)
LEGACY_GENERATOR = "scripts/c09_spec_graph_extract.py"    # retired OCR lineage (T-C09)
# Session-55 expectation repair (2026-09-22, dated; protective intent unchanged):
# T-C26 (b4e4d91) re-emitted the 5 SIBLING stores from the PDF-direct lineage
# via scripts/c26_emit_definitive_sibling_stores.py (verified by c26_postcheck
# + the C27 sweep S1/S2 at the time); this checker's meta gate was simply not
# re-run after C26 and still listed only the T-C23/T-C09 emitters. The C26
# emitter is admissible for EXACTLY those 5 sibling stores — never for
# specification_points.yaml (its definitive-generator requirement below is
# untouched).
C26_EMITTER = "scripts/c26_emit_definitive_sibling_stores.py"
C26_SIBLING_STORES = {"topics.yaml", "relationships.yaml", "command_words.yaml",
                      "practicals.yaml", "assessment_objectives.yaml"}
SOURCE_MD = "international-gcse-chemistry-2017-specification-2026-09-10_12-18-50.md"
SOURCE_PDF = "international-gcse-chemistry-2017-specification.pdf"
CANON_SPEC_JSON = "Official-Specifications/parsed/igcse-chemistry/spec_points.json"
PDF_SHA1 = "3ad641b7c60b314fa3b10680feda30bf56280a53"
# spec points whose colon-ending wording legitimately has no sub_items bullets
COLON_EXCEPTION_CODES = {"4CH1-4.49C"}

# --- T-C10 baseline (Phase 2 mapping state, 2026-09-11) -----------------------
# Round-4 (2026-09-11): 2 mappings rejected & removed (4CH1-4.15 @ NOx,
# 4CH1-1.17 @ Calculate Relative Mass) — 211 -> 209 mappings, 182 -> 181
# covered points (4.15 = honest zero-coverage corpus gap; review sheet §12).
C10_COUNTS = {"notes": 112, "mappings": 209, "points_covered": 181}
C10_CONFIDENCE = {"high", "medium", "low"}
C10_TIERS = {"PROVIDER", "AI_SUGGESTED"}

# --- expected counts (Phase-1 amended baseline) -------------------------------
COUNTS = {
    "spec_points": 182, "c_points": 52, "topics": 4, "subtopics": 28,
    "practicals": 12, "command_words": 25, "edges": 210, "papers": 2,
    "aos": 3,
}
PER_SECTION = {1: 60, 2: 50, 3: 22, 4: 50}

# --- vocabularies (must mirror the extractor; never invented here) -----------
LIVE_EDGE_ENUM = ["PART_OF", "REQUIRES_PREREQUISITE", "RELATED_TO",
                  "MISCONCEPTION_OF", "EXPLAINED_BY", "REMEDIATED_BY"]
SKILL_TAGS = {"PRACTICAL", "KNOW", "UNDERSTAND", "DESCRIBE", "EXPLAIN",
              "CALCULATE", "DRAW", "WRITE", "DEDUCE", "COMPARE",
              "INTERPRET", "PREDICT", "INVESTIGATE", "DETERMINE",
              "MEASURE", "RECALL"}
DAMAGE_FLAG_VOCAB = {
    "cjk-leak", "full-width-punct", "lost-subscript", "lost-superscript",
    "latex-fragment", "lost-space", "statement-continuation-row",
    "orphaned-outside-table", "code-space-damage",
    "superseded-truncated-table-row", "equation-rendered-as-latex-block",
    "subsection-reassigned-from-pdf", "subsection-header-missing-in-md",
    "ao-range-dash-missing", "unknown-leading-verb", "title-differs-md-vs-pdf",
    "possible-superscript-loss",
}
ROW_SHAPES = {"two-col", "colspan-cell", "single-cell", "orphan-line"}
MATCH_LEVELS = {"exact", "normalized", "fuzzy", "mismatch", "pdf-missing"}
CW_CATEGORIES = {"main", "verb-preceding-command-word", "multiple-choice-questions"}
# Session-55 expectation repair (2026-09-22, dated; protective intent unchanged):
# 'canonical-pdf-direct-parse' is the C26 sibling-store header_source vocabulary
# (scripts/c26_field_map.yaml wording_source) carried by all 28 subtopics since
# the T-C26 PDF-direct refresh; the vocabulary predates C26 and is extended,
# not relaxed — every pre-existing value remains admissible exactly as before.
HEADER_SOURCES = {"md-table", "pdf-recovered", "canonical-pdf-direct-parse"}
SECTION_TITLES = {1: "Principles of chemistry", 2: "Inorganic chemistry",
                  3: "Physical chemistry", 4: "Organic chemistry"}

RE_TOPIC_CODE = re.compile(r"^4CH1-S[1-4]$")
RE_SUBTOPIC_CODE = re.compile(r"^4CH1-S[1-4]-[a-i]$")
RE_POINT_CODE = re.compile(r"^4CH1-([1-4]\.\d{1,2}C?)$")
RE_CW_CODE = re.compile(r"^4CH1-CW-[A-Z0-9-]+$")
RE_PR_CODE = re.compile(r"^4CH1-PR-\d{2}$")
RE_AO_CODE = re.compile(r"^4CH1-AO[1-3]$")
RE_PAPER_CODE = re.compile(r"^4CH1-P[12]C$")
# foreign-curriculum leakage in prose: WPH11/WCH12-style unit codes, IAL,
# other 4-series subject codes. 4SD0 is whitelisted (Double Award context).
RE_FOREIGN = re.compile(r"\b(?:W[A-Z]{2}\d{1,2}|IAL|4SD0[^/]|4SC0|4CH0)\b")
RE_4SD0_ANY = re.compile(r"\b4SD0\b")

PROV_BASE_KEYS = ["tier", "source_file", "spec_issue", "extraction_method",
                  "generated_by", "generated_date"]


class Check:
    def __init__(self, name):
        self.name = name
        self.failures = []

    def fail(self, msg):
        self.failures.append(msg)

    @property
    def ok(self):
        return not self.failures


def is_int(x):
    return isinstance(x, int) and not isinstance(x, bool)


def check_provenance(chk, prov, ctx, want_line=False):
    if not isinstance(prov, dict):
        chk.fail(f"{ctx}: provenance is not a mapping")
        return
    for k in PROV_BASE_KEYS:
        if k not in prov or prov[k] in (None, ""):
            chk.fail(f"{ctx}: provenance missing '{k}'")
    if prov.get("tier") != "RULE_DERIVED":
        chk.fail(f"{ctx}: provenance tier '{prov.get('tier')}' != RULE_DERIVED")
    if prov.get("spec_issue") != 3:
        chk.fail(f"{ctx}: provenance spec_issue != 3")
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", str(prov.get("generated_date", ""))):
        chk.fail(f"{ctx}: provenance generated_date not ISO: {prov.get('generated_date')!r}")
    if prov.get("source_file") == CANON_SPEC_JSON:
        # definitive lineage (T-C23): PDF-span anchors + retirement pointer
        if prov.get("generated_by") != GENERATOR:
            chk.fail(f"{ctx}: provenance generated_by != {GENERATOR}")
        pg, oy, sha = prov.get("pdf_page"), prov.get("pdf_oy"), prov.get("pdf_sha1")
        if not is_int(pg) or pg < 1:
            chk.fail(f"{ctx}: provenance pdf_page missing/not positive: {pg!r}")
        if not isinstance(oy, (int, float)) or isinstance(oy, bool):
            chk.fail(f"{ctx}: provenance pdf_oy missing: {oy!r}")
        if sha != PDF_SHA1:
            chk.fail(f"{ctx}: provenance pdf_sha1 {sha!r} != {PDF_SHA1}")
        sup = prov.get("supersedes") or {}
        if sup.get("source_file") != SOURCE_MD or sup.get("retired") is not True:
            chk.fail(f"{ctx}: provenance supersedes block missing/incorrect")
    elif prov.get("source_file") == SOURCE_MD:
        # legacy OCR lineage (other graph files until their own refresh)
        if prov.get("generated_by") != LEGACY_GENERATOR:
            chk.fail(f"{ctx}: provenance generated_by != {LEGACY_GENERATOR}")
        if want_line:
            ln = prov.get("md_line")
            if not is_int(ln) or ln < 1:
                chk.fail(f"{ctx}: provenance md_line missing/not positive: {ln!r}")
    else:
        chk.fail(f"{ctx}: provenance source_file '{prov.get('source_file')}' is "
                 f"neither the definitive canonical JSON nor the retired OCR md")


def check_damage_flags(chk, flags, ctx):
    if not isinstance(flags, list):
        chk.fail(f"{ctx}: damage_flags is not a list")
        return
    for f in flags:
        if f not in DAMAGE_FLAG_VOCAB:
            chk.fail(f"{ctx}: damage flag '{f}' outside vocabulary")


def check_base_record(chk, rec, ctx):
    if rec.get("validation_status") != "RULE_DERIVED":
        chk.fail(f"{ctx}: validation_status '{rec.get('validation_status')}' != RULE_DERIVED")
    if rec.get("confidence") != 1.0:
        chk.fail(f"{ctx}: confidence {rec.get('confidence')!r} != 1.0")
    if rec.get("version") != 1:
        chk.fail(f"{ctx}: version {rec.get('version')!r} != 1")
    check_damage_flags(chk, rec.get("damage_flags"), ctx)


def scan_foreign(chk, value, ctx):
    """Prose fields may mention 4SD0 (Double-Award rule) but nothing foreign."""
    if not isinstance(value, str):
        return
    m = RE_FOREIGN.search(value)
    if m:
        chk.fail(f"{ctx}: foreign-curriculum token '{m.group(0)}' in text: {value[:100]!r}")


def load_all(graph_dir):
    data = {}
    for fn in FILES:
        p = graph_dir / fn
        if not p.exists():
            print(f"FATAL: missing {p}", file=sys.stderr)
            sys.exit(1)
        try:
            data[fn] = yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            print(f"FATAL: {fn} does not parse: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(data[fn], dict) or "meta" not in data[fn]:
            print(f"FATAL: {fn} is not a mapping with a 'meta' key", file=sys.stderr)
            sys.exit(1)
    return data


def check_meta(data):
    chk = Check("meta")
    for fn, d in data.items():
        meta = d["meta"]
        for k in ("curriculum_code", "phase", "generator", "generated"):
            if k not in meta:
                chk.fail(f"{fn}: meta missing '{k}'")
        if meta.get("curriculum_code") != "4CH1-2017":
            chk.fail(f"{fn}: meta.curriculum_code '{meta.get('curriculum_code')}' != '4CH1-2017'")
        if meta.get("phase") != 1:
            chk.fail(f"{fn}: meta.phase != 1")
        # Session-55 repair (dated): the 5 C26 sibling stores may carry the
        # C26 emitter; every other store keeps the original generator set.
        gen_ok = meta.get("generator") in (GENERATOR, LEGACY_GENERATOR) or (
            fn in C26_SIBLING_STORES and meta.get("generator") == C26_EMITTER)
        if not gen_ok:
            chk.fail(f"{fn}: meta.generator '{meta.get('generator')}' outside "
                     f"the definitive/legacy generator set")
        if fn == "specification_points.yaml" and meta.get("generator") != GENERATOR:
            chk.fail(f"{fn}: meta.generator must be the definitive {GENERATOR}")
        if meta.get("edge_vocabulary") and "PART_OF" not in meta["edge_vocabulary"]:
            chk.fail(f"{fn}: meta.edge_vocabulary lacks PART_OF")
    # counts vs records
    pts = data["specification_points.yaml"]["specification_points"]
    tops = data["topics.yaml"]["topics"]
    subs = data["topics.yaml"]["subtopics"]
    edges = data["relationships.yaml"]["edges"]
    cws = data["command_words.yaml"]["command_words"]
    prs = data["practicals.yaml"]["practicals"]
    aos = data["assessment_objectives.yaml"]["assessment_objectives"]
    papers = data["assessment_objectives.yaml"]["papers"]
    meta = data["specification_points.yaml"]["meta"].get("counts", {})
    expect = {
        "spec_points": len(pts), "c_points": sum(1 for p in pts if p.get("c_point")),
        "topics": len(tops), "subtopics": len(subs),
        "practicals": len(prs), "command_words": len(cws),
    }
    for k, v in expect.items():
        if meta.get(k) != v:
            chk.fail(f"meta.counts.{k} = {meta.get(k)!r} != actual {v}")
        if COUNTS.get(k) is not None and v != COUNTS[k]:
            chk.fail(f"actual {k} count {v} != expected {COUNTS[k]}")
    if len(edges) != COUNTS["edges"]:
        chk.fail(f"edges {len(edges)} != {COUNTS['edges']}")
    if len(aos) != COUNTS["aos"]:
        chk.fail(f"assessment objectives {len(aos)} != {COUNTS['aos']}")
    if len(papers) != COUNTS["papers"]:
        chk.fail(f"papers {len(papers)} != {COUNTS['papers']}")
    per_sec = {}
    for p in pts:
        per_sec[int(str(p["official_code"])[0])] = per_sec.get(int(str(p["official_code"])[0]), 0) + 1
    for sec, n in PER_SECTION.items():
        if per_sec.get(sec, 0) != n:
            chk.fail(f"section S{sec} has {per_sec.get(sec, 0)} points != {n}")
    return chk


def check_spec_points(data):
    chk = Check("specification_points")
    pts = data["specification_points.yaml"]["specification_points"]
    codes, gorders = set(), set()
    for i, p in enumerate(pts):
        ctx = f"point[{i}]"
        for k in ("code", "official_code", "official_wording", "section",
                  "subsection", "ordering", "global_order", "c_point",
                  "practical", "applicability", "leading_verb",
                  "draft_skill_tags", "validation_status", "confidence",
                  "version", "provenance", "damage_flags"):
            if k not in p:
                chk.fail(f"{ctx}: missing key '{k}'")
        m = RE_POINT_CODE.match(str(p.get("code", "")))
        if not m:
            chk.fail(f"{ctx}: code '{p.get('code')}' not in 4CH1-* point namespace")
            continue
        code = p["code"]
        if code in codes:
            chk.fail(f"{ctx}: duplicate code {code}")
        codes.add(code)
        if p.get("official_code") != m.group(1):
            chk.fail(f"{ctx}: official_code {p.get('official_code')!r} != {m.group(1)!r}")
        # namespace of structural refs
        if not RE_TOPIC_CODE.match(str(p.get("section", ""))):
            chk.fail(f"{code}: section '{p.get('section')}' not a 4CH1-S[1-4] topic code")
        if not RE_SUBTOPIC_CODE.match(str(p.get("subsection", ""))):
            chk.fail(f"{code}: subsection '{p.get('subsection')}' not a 4CH1-S[1-4]-[a-i] code")
        # c-point semantics
        c = str(p["official_code"]).endswith("C")
        if p.get("c_point") is not c:
            chk.fail(f"{code}: c_point {p.get('c_point')} != suffix semantics {c}")
        app = p.get("applicability", {})
        if not isinstance(app, dict):
            chk.fail(f"{code}: applicability not a mapping")
        else:
            if app.get("double_award_shared") is not False if c else app.get("double_award_shared") is not True:
                chk.fail(f"{code}: double_award_shared inconsistent with C-suffix")
            if app.get("papers") != (["2C"] if c else ["1C", "2C"]):
                chk.fail(f"{code}: applicability.papers {app.get('papers')} wrong for C={c}")
        # ordering
        if not is_int(p.get("ordering")) or p["ordering"] < 1:
            chk.fail(f"{code}: ordering {p.get('ordering')!r} not positive int")
        if not is_int(p.get("global_order")) or p["global_order"] < 1:
            chk.fail(f"{code}: global_order {p.get('global_order')!r} not positive int")
        elif p["global_order"] in gorders:
            chk.fail(f"{code}: duplicate global_order {p['global_order']}")
        gorders.add(p["global_order"])
        # skill tags
        tags = p.get("draft_skill_tags", [])
        if not isinstance(tags, list):
            chk.fail(f"{code}: draft_skill_tags not a list")
        else:
            for t in tags:
                mm = re.match(r"^4CH1-SK-([A-Z]+)$", str(t))
                if not mm or mm.group(1) not in SKILL_TAGS:
                    chk.fail(f"{code}: skill tag '{t}' outside vocabulary")
            if p.get("practical") and "4CH1-SK-PRACTICAL" not in tags:
                chk.fail(f"{code}: practical point lacks 4CH1-SK-PRACTICAL tag")
        # provenance
        prov = p.get("provenance", {})
        lineage_canon = prov.get("source_file") == CANON_SPEC_JSON
        check_provenance(chk, prov, code, want_line=not lineage_canon)
        if not lineage_canon:
            shape = prov.get("row_shape")
            if shape not in ROW_SHAPES:
                chk.fail(f"{code}: row_shape '{shape}' outside vocabulary")
            elif shape == "orphan-line":
                if prov.get("table_index") is not None or prov.get("row_index") is not None:
                    chk.fail(f"{code}: orphan-line carries table/row indices")
            else:
                if not is_int(prov.get("table_index")) or not is_int(prov.get("row_index")):
                    chk.fail(f"{code}: table_index/row_index missing for in-table row")
            xc = prov.get("pdf_crosscheck", {})
            if not isinstance(xc, dict):
                chk.fail(f"{code}: pdf_crosscheck not a mapping")
            else:
                if xc.get("file") != SOURCE_PDF:
                    chk.fail(f"{code}: pdf_crosscheck.file != {SOURCE_PDF}")
                if not is_int(xc.get("page")) or xc.get("page", 0) < 1:
                    chk.fail(f"{code}: pdf_crosscheck.page missing/not positive: {xc.get('page')!r}")
                if xc.get("match") not in MATCH_LEVELS:
                    chk.fail(f"{code}: pdf_crosscheck.match '{xc.get('match')}' outside vocabulary")
                elif xc.get("match") in ("mismatch", "pdf-missing"):
                    chk.fail(f"{code}: PDF cross-check match '{xc.get('match')}' — gate regression")
        # wording: verbatim + foreign scan (4SD0 allowed in applicability.rule only)
        if not isinstance(p.get("official_wording"), str) or not p["official_wording"].strip():
            chk.fail(f"{code}: official_wording empty")
        else:
            scan_foreign(chk, p["official_wording"], code)
        # definitive-lineage bullets (T-C23): PDF sub_items carried verbatim
        bullets = p.get("official_bullets")
        if bullets is not None:
            if not isinstance(bullets, list) or not all(
                    isinstance(b, str) and b.strip() for b in bullets):
                chk.fail(f"{code}: official_bullets must be a list of non-empty strings")
            else:
                for b in bullets:
                    scan_foreign(chk, b, code)
        if str(p.get("official_wording", "")).rstrip().endswith(":") \
                and not bullets and code not in COLON_EXCEPTION_CODES:
            chk.fail(f"{code}: colon-ending wording without official_bullets "
                     f"(bullet-truncation guard)")
        check_base_record(chk, p, code)
    if len(pts) != COUNTS["spec_points"]:
        chk.fail(f"point count {len(pts)} != {COUNTS['spec_points']}")
    if gorders and sorted(gorders) != list(range(1, len(pts) + 1)):
        chk.fail("global_order values are not exactly 1..N")
    return chk, codes


def check_topics(data, point_codes):
    chk = Check("topics")
    d = data["topics.yaml"]
    tops = d["topics"]
    subs = d["subtopics"]
    topic_codes = set()
    for i, t in enumerate(tops):
        ctx = f"topic[{i}]"
        if not RE_TOPIC_CODE.match(str(t.get("code", ""))):
            chk.fail(f"{ctx}: code '{t.get('code')}' not in 4CH1-S[1-4] namespace")
        else:
            sec = int(t["code"][-1])
            if t.get("title") != SECTION_TITLES.get(sec):
                chk.fail(f"{ctx}: title {t.get('title')!r} != canonical section title")
            if t.get("ordering") != sec:
                chk.fail(f"{ctx}: ordering {t.get('ordering')} != section number {sec}")
            topic_codes.add(t["code"])
        check_provenance(chk, t.get("provenance", {}), t.get("code", ctx), want_line=True)
        check_base_record(chk, t, t.get("code", ctx))
    if len(tops) != COUNTS["topics"]:
        chk.fail(f"topic count {len(tops)} != {COUNTS['topics']}")

    sub_codes = set()
    sub_members = {}
    for i, s in enumerate(subs):
        code = str(s.get("code", ""))
        ctx = f"subtopic[{i}] {code}"
        if not RE_SUBTOPIC_CODE.match(code):
            chk.fail(f"{ctx}: not in 4CH1-S[1-4]-[a-i] namespace")
            continue
        if code in sub_codes:
            chk.fail(f"{ctx}: duplicate subtopic code")
        sub_codes.add(code)
        if s.get("parent") != f"4CH1-S{code[-3]}":
            chk.fail(f"{ctx}: parent {s.get('parent')!r} inconsistent with code")
        if s.get("letter") != code[-1]:
            chk.fail(f"{ctx}: letter {s.get('letter')!r} != {code[-1]!r}")
        if s.get("header_source") not in HEADER_SOURCES:
            chk.fail(f"{ctx}: header_source '{s.get('header_source')}' outside vocabulary")
        if not isinstance(s.get("title"), str) or not s["title"].strip():
            chk.fail(f"{ctx}: PDF title missing")
        else:
            scan_foreign(chk, s["title"], ctx)
        members = s.get("spec_points", [])
        if not isinstance(members, list) or not members:
            chk.fail(f"{ctx}: spec_points list missing/empty")
            continue
        for ref in members:
            if ref not in point_codes:
                chk.fail(f"{ctx}: spec_points ref '{ref}' is not a declared spec point")
        if len(members) != len(set(members)):
            chk.fail(f"{ctx}: duplicate refs in spec_points")
        sub_members[code] = members
        if not is_int(s.get("ordering")) or s["ordering"] < 1:
            chk.fail(f"{ctx}: ordering not positive int")
        prov = s.get("provenance", {})
        check_provenance(chk, prov, code)
        if not is_int(prov.get("pdf_header_page")) or prov.get("pdf_header_page", 0) < 1:
            chk.fail(f"{ctx}: provenance pdf_header_page missing/not positive")
        if s.get("header_source") == "md-table" and not is_int(prov.get("md_line")):
            chk.fail(f"{ctx}: md-table header lacks provenance md_line")
        check_base_record(chk, s, ctx)

    # membership equivalence with the points' own declarations
    declared = {}
    for p in data["specification_points.yaml"]["specification_points"]:
        declared.setdefault(str(p.get("subsection")), []).append(p["code"])
    if sub_codes != set(declared):
        chk.fail(f"subtopic code set != subsections declared by points: "
                 f"only-in-subtopics={sorted(sub_codes - set(declared))} "
                 f"only-in-points={sorted(set(declared) - sub_codes)}")
    for code, members in sub_members.items():
        if sorted(members) != sorted(declared.get(code, [])):
            chk.fail(f"{code}: spec_points membership != points' declared subsection")
    # per-subsection ordering contiguity (1..n)
    pts = {p["code"]: p for p in data["specification_points.yaml"]["specification_points"]}
    for code, members in sub_members.items():
        orders = sorted(pts[m]["ordering"] for m in members if m in pts)
        if orders != list(range(1, len(orders) + 1)):
            chk.fail(f"{code}: per-subsection ordering not contiguous 1..n: {orders}")
    if len(subs) != COUNTS["subtopics"]:
        chk.fail(f"subtopic count {len(subs)} != {COUNTS['subtopics']}")
    return chk, topic_codes, sub_codes, sub_members


def check_relationships(data, point_codes, topic_codes, sub_codes, sub_members):
    chk = Check("relationships")
    edges = data["relationships.yaml"]["edges"]
    nodes = point_codes | topic_codes | sub_codes
    seen = set()
    sub_to_topic, point_to_sub = {}, {}
    for i, e in enumerate(edges):
        ctx = f"edge[{i}]"
        fr, rel, to = e.get("from"), e.get("relation"), e.get("to")
        if rel not in LIVE_EDGE_ENUM:
            chk.fail(f"{ctx}: relation '{rel}' not in live V2 knowledge_edges enum")
        if fr not in nodes:
            chk.fail(f"{ctx}: 'from' {fr!r} does not resolve to a declared node")
        if to not in nodes:
            chk.fail(f"{ctx}: 'to' {to!r} does not resolve to a declared node")
        key = (fr, rel, to)
        if key in seen:
            chk.fail(f"{ctx}: duplicate edge {key}")
        seen.add(key)
        if rel == "PART_OF":
            if fr in sub_codes:
                if to not in topic_codes:
                    chk.fail(f"{ctx}: subtopic PART_OF target {to!r} is not a topic")
                sub_to_topic[fr] = to
            elif fr in point_codes:
                if to not in sub_codes:
                    chk.fail(f"{ctx}: spec point PART_OF target {to!r} is not a subtopic")
                point_to_sub[fr] = to
            else:
                chk.fail(f"{ctx}: unexpected PART_OF source {fr!r}")
        if not is_int(e.get("order")) or e["order"] < 1:
            chk.fail(f"{ctx}: order not positive int")
        check_provenance(chk, e.get("provenance", {}), f"edge {fr}->{to}")
        check_base_record(chk, e, ctx)
    # exact coverage
    if sub_to_topic.keys() != sub_codes:
        chk.fail(f"PART_OF subtopic->topic coverage incomplete: missing "
                 f"{sorted(sub_codes - set(sub_to_topic))}")
    if point_to_sub.keys() != point_codes:
        missing = sorted(point_codes - set(point_to_sub))
        chk.fail(f"PART_OF point->subtopic coverage incomplete: {len(missing)} missing "
                 f"(first: {missing[:5]})")
    # agreement with declared structure
    pts = {p["code"]: p for p in data["specification_points.yaml"]["specification_points"]}
    for pc, sub in point_to_sub.items():
        if pts[pc].get("subsection") != sub:
            chk.fail(f"{pc}: edge target {sub} != declared subsection {pts[pc].get('subsection')}")
    subs = {s["code"]: s for s in data["topics.yaml"]["subtopics"]}
    for sc, tc in sub_to_topic.items():
        if subs[sc].get("parent") != tc:
            chk.fail(f"{sc}: edge target {tc} != declared parent {subs[sc].get('parent')}")
    # order fields follow the source structures
    for sc, members in sub_members.items():
        expected = {m: pts[m]["global_order"] for m in members}
        for e in edges:
            if e.get("from") in expected:
                if e.get("order") != expected[e["from"]]:
                    chk.fail(f"edge {e['from']}: order {e.get('order')} != global_order "
                             f"{expected[e['from']]}")
    return chk


def check_command_words(data):
    chk = Check("command_words")
    cws = data["command_words.yaml"]["command_words"]
    seen = set()
    for i, cw in enumerate(cws):
        ctx = f"cw[{i}]"
        code = str(cw.get("code", ""))
        if not RE_CW_CODE.match(code):
            chk.fail(f"{ctx}: code '{code}' not in 4CH1-CW-* namespace")
        if code in seen:
            chk.fail(f"{ctx}: duplicate code {code}")
        seen.add(code)
        if not isinstance(cw.get("command_word"), str) or not cw["command_word"].strip():
            chk.fail(f"{ctx}: command_word empty")
        if cw.get("category") not in CW_CATEGORIES:
            chk.fail(f"{ctx}: category '{cw.get('category')}' outside vocabulary")
        if not isinstance(cw.get("definition"), str) or not cw["definition"].strip():
            chk.fail(f"{ctx}: definition empty")
        else:
            scan_foreign(chk, cw["definition"], code)
        if cw.get("ordering") != i + 1:
            chk.fail(f"{ctx}: ordering {cw.get('ordering')} != position {i + 1}")
        prov = cw.get("provenance", {})
        check_provenance(chk, prov, code, want_line=True)
        if not is_int(prov.get("table_index")) or not is_int(prov.get("row_index")):
            chk.fail(f"{code}: provenance table_index/row_index missing")
        check_base_record(chk, cw, code)
    if len(cws) != COUNTS["command_words"]:
        chk.fail(f"command-word count {len(cws)} != {COUNTS['command_words']}")
    return chk


def check_practicals(data, point_codes):
    chk = Check("practicals")
    prs = data["practicals.yaml"]["practicals"]
    pts = {p["code"]: p for p in data["specification_points.yaml"]["specification_points"]}
    flagged = {p["code"] for p in pts.values() if p.get("practical")}
    covered = set()
    for i, pr in enumerate(prs):
        ctx = f"practical[{i}]"
        code = str(pr.get("code", ""))
        if not RE_PR_CODE.match(code):
            chk.fail(f"{ctx}: code '{code}' not in 4CH1-PR-## namespace")
        if pr.get("ordering") != i + 1:
            chk.fail(f"{ctx}: ordering {pr.get('ordering')} != position {i + 1}")
        sp = pr.get("spec_point")
        if sp not in point_codes:
            chk.fail(f"{ctx}: spec_point {sp!r} not a declared spec point")
        else:
            if sp not in flagged:
                chk.fail(f"{ctx}: spec_point {sp} is not practical-flagged")
            if sp in covered:
                chk.fail(f"{ctx}: spec_point {sp} covered twice")
            covered.add(sp)
            if pr.get("subsection") != pts[sp].get("subsection"):
                chk.fail(f"{ctx}: subsection {pr.get('subsection')!r} != point's "
                         f"{pts[sp].get('subsection')!r}")
        if not isinstance(pr.get("summary"), str) or not pr["summary"].strip():
            chk.fail(f"{ctx}: summary empty")
        prov = pr.get("provenance", {})
        check_provenance(chk, prov, code, want_line=True)
        check_base_record(chk, pr, code)
    if covered != flagged:
        chk.fail(f"practical coverage != practical-flagged points: missing "
                 f"{sorted(flagged - covered)}")
    if len(prs) != COUNTS["practicals"]:
        chk.fail(f"practical count {len(prs)} != {COUNTS['practicals']}")
    return chk


def check_assessment(data):
    chk = Check("assessment_objectives")
    d = data["assessment_objectives.yaml"]
    aos = d["assessment_objectives"]
    papers = d["papers"]
    for i, ao in enumerate(aos):
        code = str(ao.get("code", ""))
        if not RE_AO_CODE.match(code):
            chk.fail(f"ao[{i}]: code '{code}' not in 4CH1-AO[1-3] namespace")
        if not isinstance(ao.get("title"), str) or not ao["title"].strip():
            chk.fail(f"{code}: title empty")
        if not isinstance(ao.get("weighting_overall"), str):
            chk.fail(f"{code}: weighting_overall missing")
        wbp = ao.get("weighting_by_paper")
        if not isinstance(wbp, dict) or set(wbp) != {"paper_1", "paper_2"}:
            chk.fail(f"{code}: weighting_by_paper keys != paper_1/paper_2")
        else:
            for pk, pv in wbp.items():
                if not isinstance(pv, dict) or set(pv) != {"ao1", "ao2", "ao3"}:
                    chk.fail(f"{code}: weighting_by_paper.{pk} keys != ao1/ao2/ao3")
        check_provenance(chk, ao.get("provenance", {}), code)
        check_base_record(chk, ao, code)
    if len(aos) != COUNTS["aos"]:
        chk.fail(f"AO count {len(aos)} != {COUNTS['aos']}")

    seen = set()
    expected_codes = {"4CH1-P1C", "4CH1-P2C"}
    for i, p in enumerate(papers):
        ctx = f"paper[{i}]"
        code = str(p.get("code", ""))
        if not RE_PAPER_CODE.match(code):
            chk.fail(f"{ctx}: code '{code}' not in 4CH1-P[12]C namespace")
        if code in seen:
            chk.fail(f"{ctx}: duplicate paper code {code}")
        seen.add(code)
        if p.get("paper_code") not in ("4CH1/1C", "4CH1/2C"):
            chk.fail(f"{ctx}: paper_code {p.get('paper_code')!r} not a 4CH1 paper code")
        for k in ("marks", "duration_minutes"):
            if not is_int(p.get(k)) or p[k] < 1:
                chk.fail(f"{ctx}: {k} {p.get(k)!r} not a positive int")
        if not isinstance(p.get("weighting"), str) or not p["weighting"].endswith("%"):
            chk.fail(f"{ctx}: weighting {p.get('weighting')!r} not a percentage")
        if not isinstance(p.get("content_rule"), str) or not p["content_rule"].strip():
            chk.fail(f"{ctx}: content_rule empty")
        else:
            scan_foreign(chk, p["content_rule"], code)
        check_provenance(chk, p.get("provenance", {}), code, want_line=True)
        check_base_record(chk, p, code)
    if seen != expected_codes:
        chk.fail(f"paper codes {sorted(seen)} != {sorted(expected_codes)}")
    return chk


def check_namespace_prose(data):
    """4SD0 may appear ONLY in the applicability rule prose (Double Award)."""
    chk = Check("namespace_prose")
    pts = data["specification_points.yaml"]["specification_points"]
    for p in pts:
        rule = p.get("applicability", {}).get("rule", "")
        if isinstance(rule, str) and RE_4SD0_ANY.search(rule) and "Double Award" not in rule:
            chk.fail(f"{p['code']}: 4SD0 mentioned outside the Double-Award rule")
    return chk


def check_notes_mapping(data, point_codes, sub_codes, notes_root=None):
    """Check group 6 — T-C10 note->spec-point mapping state (front matter)."""
    chk = Check("c10-notes-mapping")
    notes_root = Path(notes_root) if notes_root else NOTES_ROOT_DEFAULT

    note_files = sorted(p for p in notes_root.rglob("*.md")
                        if "assets" not in p.parts)
    if len(note_files) != C10_COUNTS["notes"]:
        chk.fail(f"note count {len(note_files)} != {C10_COUNTS['notes']}")

    total_maps, covered = 0, set()
    n_notes = 0
    for path in note_files:
        rel = path.relative_to(notes_root.parent)
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            chk.fail(f"c10.1 no front matter: {rel}")
            continue
        try:
            close = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
            fm = yaml.safe_load("\n".join(lines[1:close])) or {}
        except (StopIteration, yaml.YAMLError):
            chk.fail(f"c10.1 unparseable front matter: {rel}")
            continue
        sm = fm.get("spec_map")
        if not isinstance(sm, dict):
            chk.fail(f"c10.1 missing spec_map: {rel}")
            continue
        n_notes += 1
        # c10.1 schema
        for key in ("curriculum_code", "phase", "subsection", "spec_points",
                    "mapped_date", "mapper"):
            if key not in sm:
                chk.fail(f"c10.1 spec_map missing key {key}: {rel}")
        if sm.get("curriculum_code") != "4CH1-2017":
            chk.fail(f"c10.1 wrong curriculum_code {sm.get('curriculum_code')!r}: {rel}")
        # c10.4 PROVIDER anchor vs slug
        sub = sm.get("subsection")
        if sub not in sub_codes:
            chk.fail(f"c10.4 unknown subsection {sub!r}: {rel}")
        sp = sm.get("subsection_provenance", {})
        for key in ("tier", "signal", "slug", "validation_status"):
            if key not in sp:
                chk.fail(f"c10.4 subsection_provenance missing {key}: {rel}")
        if sp.get("tier") != "PROVIDER" or sp.get("signal") != "source-url-slug":
            chk.fail(f"c10.4 bad subsection provenance tier/signal: {rel}")
        url = fm.get("source") or ""
        parsed = parse_slug(url) if url else None
        if parsed:
            sec, grp, group_slug, _, _ = parsed
            want_sub = f"4CH1-S{sec}-{SECTION_LETTERS[grp - 1]}"
            if sub != want_sub:
                chk.fail(f"c10.4 anchor {sub} != slug-derived {want_sub}: {rel}")
            if sp.get("slug") != group_slug:
                chk.fail(f"c10.4 provenance slug {sp.get('slug')!r} != URL group "
                         f"{group_slug!r}: {rel}")
        # c10.5 mappings present, unique
        sps = sm.get("spec_points") or []
        if not sps:
            chk.fail(f"c10.5 zero mappings: {rel}")
        codes = [m.get("code") for m in sps]
        if len(codes) != len(set(codes)):
            chk.fail(f"c10.5 duplicate codes: {rel}")
        # c10.2 registry + c10.3 provenance completeness
        for m in sps:
            c = m.get("code")
            if c not in point_codes:
                chk.fail(f"c10.2 code not in 182-registry: {c} ({rel})")
            prov = m.get("provenance", {})
            if prov.get("tier") != "AI_SUGGESTED":
                chk.fail(f"c10.3 wrong tier {prov.get('tier')!r} for {c}: {rel}")
            if prov.get("confidence") not in C10_CONFIDENCE:
                chk.fail(f"c10.3 bad confidence {prov.get('confidence')!r} for {c}: {rel}")
            for key in ("model_version", "evidence", "rationale"):
                if not prov.get(key):
                    chk.fail(f"c10.3 missing {key} for {c}: {rel}")
            # validation state: SUGGESTED (clean, no stray promotion fields)
            # or HUMAN_VALIDATED (validated_by + ISO date required; tier must
            # still be AI_SUGGESTED — origin is immutable, checked above)
            vs = prov.get("validation_status")
            if vs == "HUMAN_VALIDATED":
                if not prov.get("validated_by"):
                    chk.fail(f"c10.3 HUMAN_VALIDATED missing validated_by "
                             f"for {c}: {rel}")
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}",
                                    str(prov.get("validated_date", ""))):
                    chk.fail(f"c10.3 bad validated_date "
                             f"{prov.get('validated_date')!r} for {c}: {rel}")
            elif vs != "SUGGESTED":
                chk.fail(f"c10.3 validation_status {vs!r} "
                         f"for {c}: {rel}")
            else:
                for key in ("validated_by", "validated_date"):
                    if prov.get(key):
                        chk.fail(f"c10.3 stray {key} on SUGGESTED mapping "
                                 f"{c}: {rel}")
            if c in point_codes:
                covered.add(c)
                total_maps += 1
        # c10.6 foreign codes in front matter (Wxx unit codes, 4CH0, IAL)
        fm_text = "\n".join(lines[1:close])
        for m in re.finditer(r"\b(W[A-Z]{2}\d{1,2}|4CH0|IAL|4SC0)\b", fm_text):
            chk.fail(f"c10.6 foreign curriculum code {m.group(1)!r} in front matter: {rel}")

    # c10.7 totals
    if n_notes != C10_COUNTS["notes"]:
        chk.fail(f"c10.7 notes with spec_map {n_notes} != {C10_COUNTS['notes']}")
    if total_maps != C10_COUNTS["mappings"]:
        chk.fail(f"c10.7 total mappings {total_maps} != {C10_COUNTS['mappings']}")
    if len(covered) != C10_COUNTS["points_covered"]:
        chk.fail(f"c10.7 covered points {len(covered)} != "
                 f"{C10_COUNTS['points_covered']}")
    return chk


# --- T-C11 pilot (Phase 3, 2026-09-11) ----------------------------------------
# Concept/prerequisite/misconception graph for the frozen pilot slice
# 1.25-1.36. Contract: graph/reports/C11_ARCHITECTURE.md. Generated by
# scripts/c11_concept_pilot.py from scripts/c11_pilot_decisions.yaml.
C11_FILES = ["concepts.yaml", "concept_edges.yaml", "spec_command_kinds.yaml"]
C11_GENERATOR = "scripts/c11_concept_pilot.py"
# Session-47 (§16 batch 1, 2026-09-12): the store covers the pilot slice PLUS
# the first authorized expansion batch (4CH1-1.1-1.12, decision record
# scripts/c11_batch1_decisions.yaml, extraction_pass c11-s16-batch-1) per the
# §16 authorization (scripts/c11_s16_authorization.yaml). Batch-1 content is
# SUGGESTED until its own operator review gate + §18 promotion.
C11_PILOT_SPS = ["4CH1-1.25", "4CH1-1.26", "4CH1-1.27", "4CH1-1.28",
                 "4CH1-1.29", "4CH1-1.30", "4CH1-1.31", "4CH1-1.32",
                 "4CH1-1.33", "4CH1-1.34C", "4CH1-1.35C", "4CH1-1.36"]
C11_BATCH1_SPS = ["4CH1-1.1", "4CH1-1.2", "4CH1-1.3", "4CH1-1.4", "4CH1-1.5C",
                   "4CH1-1.6C", "4CH1-1.7C", "4CH1-1.8", "4CH1-1.9",
                   "4CH1-1.10", "4CH1-1.11", "4CH1-1.12"]
# session-49: batch-2 slice (paper-chromatography practical + atomic
# structure + the Periodic Table)
C11_BATCH2_SPS = ["4CH1-1.13", "4CH1-1.14", "4CH1-1.15", "4CH1-1.16",
                   "4CH1-1.17", "4CH1-1.18", "4CH1-1.19", "4CH1-1.20",
                   "4CH1-1.21", "4CH1-1.22", "4CH1-1.23", "4CH1-1.24"]
# session-51: batch-3 slice (the full S1 remainder — ionic + covalent +
# metallic bonding + electrolysis, 24 SPs + practical PR-04; commissioned by
# the operator's session-51 move-forward directive)
C11_BATCH3_SPS = ["4CH1-1.37", "4CH1-1.38", "4CH1-1.39", "4CH1-1.40",
                   "4CH1-1.41", "4CH1-1.42", "4CH1-1.43", "4CH1-1.44",
                   "4CH1-1.45", "4CH1-1.46", "4CH1-1.47", "4CH1-1.48",
                   "4CH1-1.49", "4CH1-1.50", "4CH1-1.51", "4CH1-1.52C",
                   "4CH1-1.53C", "4CH1-1.54C", "4CH1-1.55C", "4CH1-1.56C",
                   "4CH1-1.57C", "4CH1-1.58C", "4CH1-1.59C", "4CH1-1.60C"]
# session-53: batch-4 slice (Section 3 — Physical Chemistry: Energetics /
# Rates of Reaction / Reversibility & Equilibria, 22 SPs + practicals
# PR-09/PR-10/PR-11; commissioned by the operator's session-53 batch-4
# directive under the session-52 cross-slice boundary ruling)
C11_BATCH4_SPS = ["4CH1-3.1", "4CH1-3.2", "4CH1-3.3", "4CH1-3.4",
                   "4CH1-3.5C", "4CH1-3.6C", "4CH1-3.7C", "4CH1-3.8",
                   "4CH1-3.9", "4CH1-3.10", "4CH1-3.11", "4CH1-3.12",
                   "4CH1-3.13", "4CH1-3.14C", "4CH1-3.15", "4CH1-3.16",
                   "4CH1-3.17", "4CH1-3.18", "4CH1-3.19C", "4CH1-3.20C",
                   "4CH1-3.21C", "4CH1-3.22C"]
# session-55: batch-5 slice (Section 2 — Inorganic Chemistry, FIRST slice:
# a Group 1 (Alkali Metals) / b Group 7 (Halogens) / c Gases in the
# Atmosphere, 14 SPs + the 2.14 practical PR-05; commissioned by the
# operator's "run batch 5" directive under the session-55 cross-slice
# boundary ruling)  # 306 edges = 130 PART_OF + 176 semantic (18 authored)
C11_BATCH5_SPS = ["4CH1-2.1", "4CH1-2.2", "4CH1-2.3", "4CH1-2.4C",
                   "4CH1-2.5", "4CH1-2.6", "4CH1-2.7", "4CH1-2.8C",
                   "4CH1-2.9", "4CH1-2.10", "4CH1-2.11", "4CH1-2.12",
                   "4CH1-2.13", "4CH1-2.14"]
# session-57: batch-6 slice (Section 2 — Inorganic Chemistry, SECOND slice:
# d Reactivity Series / e Extraction & Uses of Metals, 13 SPs + the 2.21
# practical PR-06; commissioned by the operator's "commission batch 6"
# directive under the session-57 cross-slice boundary ruling)
C11_BATCH6_SPS = ["4CH1-2.15", "4CH1-2.16", "4CH1-2.17", "4CH1-2.18",
                  "4CH1-2.19", "4CH1-2.20", "4CH1-2.21", "4CH1-2.22C",
                  "4CH1-2.23C", "4CH1-2.24C", "4CH1-2.25C", "4CH1-2.26C",
                  "4CH1-2.27C"]
# session-59: batch-7 slice (Section 2 — Inorganic Chemistry, THIRD slice:
# f Acids, Alkalis & Titrations / g Acids, Bases & Salt Preparations, 16 SPs
# + the two in-slice practicals PR-07 (2.42) / PR-08 (2.43C); commissioned
# by the operator's "Proceed with batch 7" directive under the session-59
# cross-slice boundary ruling)
C11_BATCH7_SPS = ["4CH1-2.28", "4CH1-2.29", "4CH1-2.30", "4CH1-2.31",
                  "4CH1-2.32", "4CH1-2.33C", "4CH1-2.34", "4CH1-2.35",
                  "4CH1-2.36", "4CH1-2.37", "4CH1-2.38", "4CH1-2.39",
                  "4CH1-2.40C", "4CH1-2.41C", "4CH1-2.42", "4CH1-2.43C"]
# session-61 (§16 batch 8): the S2-h Chemical Tests slice 4CH1-2.44-2.50.
C11_BATCH8_SPS = ["4CH1-2.44", "4CH1-2.45", "4CH1-2.46", "4CH1-2.47",
                  "4CH1-2.48", "4CH1-2.49", "4CH1-2.50"]
# session-62 (§16 batch 9): the S4-a/b/c slice 4CH1-4.1-4.22 minus the
# 4CH1-4.15 negative-control carve-out (21 authorable SPs; 4.15 stays
# uncovered — the D12 control continues).
C11_BATCH9_SPS = ["4CH1-4.1", "4CH1-4.2", "4CH1-4.3", "4CH1-4.4",
                  "4CH1-4.5", "4CH1-4.6", "4CH1-4.7", "4CH1-4.8",
                  "4CH1-4.9", "4CH1-4.10", "4CH1-4.11", "4CH1-4.12",
                  "4CH1-4.13", "4CH1-4.14", "4CH1-4.16", "4CH1-4.17",
                  "4CH1-4.18", "4CH1-4.19", "4CH1-4.20", "4CH1-4.21",
                  "4CH1-4.22"]
# session-64: batch 10 = the S4 Organic SECOND slice (S4-d Alkenes 4.23-4.28
# + S4-e Alcohols 4.29C-4.33C + S4-f Carboxylic acids 4.34C-4.37C = 15
# authorable SPs; none practical-typed — the 4.43C practical belongs to
# batch 11; the 4.15 negative control sits in S4-b and stays carved out).
C11_BATCH10_SPS = ["4CH1-4.23", "4CH1-4.24", "4CH1-4.25", "4CH1-4.26",
                   "4CH1-4.27", "4CH1-4.28", "4CH1-4.29C", "4CH1-4.30C",
                   "4CH1-4.31C", "4CH1-4.32C", "4CH1-4.33C", "4CH1-4.34C",
                   "4CH1-4.35C", "4CH1-4.36C", "4CH1-4.37C"]
# session-66 (§16 batch 11): the S4 Organic THIRD slice (S4-g Esters
# 4.38C-4.43C incl. the 4.43C practical-typed SP + S4-h Synthetic polymers
# 4.44-4.50C = 13 authorable SPs; the practical SP rides the scoped T-C10
# practical 4CH1-PR-12 — the batch-3 1.60C/PR-04 precedent; the 4.15
# negative control sits in S4-b and stays carved out). Batch 11 completes S4.
C11_BATCH11_SPS = ["4CH1-4.38C", "4CH1-4.39C", "4CH1-4.40C", "4CH1-4.41C",
                   "4CH1-4.42C", "4CH1-4.43C", "4CH1-4.44", "4CH1-4.45",
                   "4CH1-4.46", "4CH1-4.47", "4CH1-4.48C", "4CH1-4.49C",
                   "4CH1-4.50C"]
C11_SCOPE_SPS = C11_PILOT_SPS + C11_BATCH1_SPS + C11_BATCH2_SPS \
    + C11_BATCH3_SPS + C11_BATCH4_SPS + C11_BATCH5_SPS + C11_BATCH6_SPS \
    + C11_BATCH7_SPS + C11_BATCH8_SPS + C11_BATCH9_SPS + C11_BATCH10_SPS \
    + C11_BATCH11_SPS
C11_STAGE = ("pilot+s16-batch-1+s16-batch-2+s16-batch-3+s16-batch-4"
             "+s16-batch-5+s16-batch-6+s16-batch-7+s16-batch-8"
             "+s16-batch-9+s16-batch-10+s16-batch-11")
C11_NEGATIVE_CONTROL = "4CH1-4.15"
# State after the session-55 batch-5 AUTHORING (extraction_pass
# c11-s16-batch-5, authored to its operator gate): 129
# nodes (29 pilot + 24 batch-1 + 14 batch-2 + 24 batch-3 + 22 batch-4 + 16
# batch-5 = 13 CONCEPT + 3 MISCONCEPTION), 306 edges (130 PART_OF + 176
# semantic — 18 authored, the pass-2 re-authoring included), 153 HUMAN_VALIDATED UNCHANGED (authoring promotes nothing; 28
# pilot session-45 + 28 batch-1 session-48 + 23 batch-2 session-50 + 39
# batch-3 session-52 + 35 batch-4 session-54 — all operator §18 promotions).
# The 35 batch-4 SUGGESTED edges were promoted to HUMAN_VALIDATED at session
# 54; the batch-5 authored edges were SUGGESTED pending the operator's
# batch-5 verdicts (recorded session 56 — see below); batch nodes stay
# SUGGESTED (nodes have no §18 pathway).
# 2 REVIEW_REQUIRED (the frozen pilot RR operator-HOLD edge + the settled
# batch-1 RR quarantine HOLD_REVIEW_REQUIRED; batch 5 authored no new RR —
# every doubt was held at authoring: 14 held candidates).
# (Session-53 note: the store was 91/220/97 at the session-52 state; batch 4
# adds 22 nodes + 20 PART_OF + 35 authored semantic edges — statuses only,
# zero promotions. Session-54 note: the 35 batch-4 SUGGESTED edges were
# promoted to HUMAN_VALIDATED by the operator's batch-4 verdicts via §18;
# counts 118 -> 153, graph shape unchanged. Session-55 note: batch 5 adds
# 16 nodes + 13 PART_OF + 18 authored semantic edges — statuses only, zero
# promotions; the PART_OF HV layer (117 -> 130) rides the T-C19 G19 record
# pattern: new PART_OF rows inherit the C19-class attachment promotion
# pathway at their own lane, not here. Session-56 note: the operator's
# batch-5 verdicts (completed review sheet §6: 18 edge CONFIRM / 16 node
# CONFIRM / 6 identity KEEP_AS_IS / 14 held acknowledged) were APPLIED
# through §18 — the 18 batch-5 authored semantic edges promoted to
# HUMAN_VALIDATED (171 semantic HV total = 28+28+23+39+35+18, all
# operator); graph shape unchanged; the only live SUGGESTED semantic
# edges are again the 3 frozen pilot operator HOLDs.)
# (Session-57 note: batch 6 adds 13 nodes (12 CONCEPT + 1 MISCONCEPTION)
# + 12 PART_OF + 16 authored semantic edges (14 RP + 1 WAP + 1 RB) —
# statuses only, zero promotions; the PART_OF HV layer rides the T-C19 G19
# record pattern (new PART_OF rows SUGGESTED pending their own
# attachment-promotion lane); the live SUGGESTED semantic surface is now
# the 3 frozen pilot operator HOLDs + the 16 batch-6 authored edges,
# pending the operator's batch-6 verdicts; 171 semantic HV unchanged.)
# (Session-58 note: the operator's batch-6 verdicts (completed review
# sheet §6: 16 edge CONFIRM with the B6-E-09 route-specific guardrail /
# 13 node CONFIRM / 6 identity KEEP_AS_IS / 9 held acknowledged) were
# APPLIED through §18 — the 16 batch-6 authored semantic edges promoted
# to HUMAN_VALIDATED (187 semantic HV total = 28+28+23+39+35+18+16, all
# operator); graph shape unchanged; the only live SUGGESTED semantic
# edges are again the 3 frozen pilot operator HOLDs.)
# (Session-59 note: batch 7 adds 15 nodes (13 CONCEPT + 2 MISCONCEPTION)
# + 14 PART_OF (one per attached SP; CON-PROTON-TRANSFER attaches 2.35 AND
# 2.36) + 19 authored semantic edges (15 RP incl. the 2 sanctioned
# boundary edges + the 2 practical edges, 2 WAP, 2 RB) — statuses only,
# zero promotions; the PART_OF HV layer rides the T-C19 G19 record
# pattern (new PART_OF rows SUGGESTED pending their own
# attachment-promotion lane); the live SUGGESTED semantic surface is now
# the 3 frozen pilot operator HOLDs + the 19 batch-7 authored edges,
# pending the operator's batch-7 verdicts; 187 semantic HV unchanged.)
# session-61 state note (dated, no test weakened): the batch-8 authored-to-
# gate record (S2-h Chemical Tests 4CH1-2.44-2.50: 8 nodes = 6 CONCEPT + 2
# MISCONCEPTION, 17 edges = 7 PART_OF + 10 authored semantic — 5 RP + 1
# RELATED_TO + 2 WAP + 2 REMEDIATED_BY, ZERO promotions) joins the store;
# 206 semantic HV unchanged (authoring promotes nothing); the live SUGGESTED
# semantic surface is now the 3 frozen pilot operator HOLDs + the 10 batch-8
# authored edges, pending the operator's batch-8 verdicts.
# session-62 state note (dated, no test weakened): the batch-8 verdicts were
# APPLIED through §18 (10 operator promotions, c11_batch8_verdicts, applied
# 2026-09-24 via the B8 diff-review bundle — the operator's completed-sheet
# §6/§7 verdict: PASS WITH NOTES); 216 semantic HV; the live SUGGESTED
# semantic surface is again EXACTLY the 3 frozen pilot operator HOLDs.
# session-62 state note (dated, no test weakened): the batch-9 authored-to-
# gate record (Section 4 Organic FIRST slice S4-a/b/c 4CH1-4.1-4.22 minus
# the 4.15 carve-out: 15 nodes = 14 CONCEPT + 1 MISCONCEPTION, 41 edges =
# 21 PART_OF + 20 authored semantic — 18 RP + 1 WAP + 1 REMEDIATED_BY,
# ZERO promotions) joins the store; 216 semantic HV unchanged (authoring
# promotes nothing); the live SUGGESTED semantic surface is now the 3
# frozen pilot operator HOLDs + the 20 batch-9 authored edges, pending the
# operator's batch-9 verdicts.
# session-63 state note (dated, no test weakened): the batch-9 verdicts
# were APPLIED through §18 (20 operator promotions, c11_batch9_verdicts,
# applied 2026-09-25 via the B9 diff-review bundle — the operator's
# completed-sheet §6/§7 verdict: PASS WITH NOTES, intake via the zai-web
# chat lane); 236 semantic HV; the live SUGGESTED semantic surface is
# again EXACTLY the 3 frozen pilot operator HOLDs; graph shape unchanged
# (statuses only; the 21 batch-9 PART_OF rows stay SUGGESTED pending
# their own lane).
# session-64 state note (dated, no test weakened): the batch-10 authored-to-
# gate record (Section 4 Organic SECOND slice S4-d/e/f 4.23-4.37C: 8 nodes =
# 7 CONCEPT + 1 MISCONCEPTION, 34 edges = 15 PART_OF + 19 authored semantic
# — 17 RP incl. the 13 sanctioned boundary rows + 1 WAP + 1 REMEDIATED_BY,
# ZERO promotions) joins the store; 236 semantic HV unchanged (authoring
# promotes nothing); the live SUGGESTED semantic surface is now the 3
# frozen pilot operator HOLDs + the 19 batch-10 authored edges, pending the
# operator's batch-10 verdicts.
# session-65 state note (dated, no test weakened): the batch-10 verdicts
# were APPLIED through §18 (19 operator promotions, c11_batch10_verdicts,
# 2026-09-25, the B10 diff-review bundle) — semantic HV 236 -> 255; the
# live SUGGESTED semantic surface is again EXACTLY the 3 frozen pilot
# operator HOLDs; graph shape unchanged (statuses only; the batch-9/10
# PART_OF rows stay SUGGESTED pending their own lane).
# session-66 state note (dated, no test weakened): the batch-11 authored-to-
# gate record (Section 4 Organic THIRD slice S4-g/h 4.38C-4.50C: 5 nodes =
# 4 CONCEPT + 1 MISCONCEPTION, 29 edges = 12 PART_OF + 17 authored semantic
# — 15 RP incl. the 12 sanctioned boundary rows + 1 WAP + 1 REMEDIATED_BY,
# ZERO promotions; the 4.43C practical SP rides the scoped 4CH1-PR-12) joins
# the store; 255 semantic HV unchanged (authoring promotes nothing); the
# live SUGGESTED semantic surface is now the 3 frozen pilot operator HOLDs
# + the 17 batch-11 authored edges, pending the operator's batch-11
# verdicts. Batch 11 completes S4 (49 of 50 S4 SPs covered; only the 4.15
# negative control remains uncovered).
# session-66 re-anchor (dated): the store grew 188/459/199 -> 193/488/211
# by the SANCTIONED batch-11 authored-to-gate record (4 nodes-worth of
# PART_OF rows ride the SP attachments; 17 authored semantic edges; 13 new
# command kinds); no test weakened.
# session-67 state note (dated, no test weakened): the operator's batch-11
# verdict (PASS WITH NOTES / Batch 11: ACCEPTED, session 67, the GitHub-
# direct sheet review + inline verdict lane) was APPLIED through §18 — 17
# operator promotions (the CONFIRM set, review_ref = the B11 diff-review
# bundle) move the semantic HV count 255 -> 272 (389 with the 117 T-C19
# G19 PART_OF rows); shape 193/488/211 unchanged (statuses only); the
# live SUGGESTED semantic surface is the 3 frozen pilot operator HOLDs
# again; the batch-11 PART_OF rows stay SUGGESTED pending their own lane;
# the operator's SCOPED-RP semantic guardrail (REQUIRES_PREREQUISITE = a
# scoped teaching/route dependency, not a universal ontological
# prerequisite) is recorded per-row in the verdict record and is binding
# for every downstream consumer.
C11_COUNTS = {"nodes": 193, "concepts": 167, "misconceptions": 26,
              "edges": 488,
              "part_of": 211, "requires_prerequisite": 209,
              "explained_by": 12,
              "related_to": 2, "commonly_confused_with": 2,
              "misconception_of": 2, "wrong_answer_pattern": 24,
              "remediated_by": 26, "review_required": 2,
              "command_kinds": 181}
# Post-operator-REJECT state (session 41, 2026-09-11): the operator rejected
# `4CH1-PR-03 REQUIRES_PREREQUISITE 4CH1-CON-MOLE` — it was re-authored out of
# the decision record (preserved as rejected candidate HELD-13; architecture
# §7: REJECTED is not a graph state). 66->65 edges, RP 26->25, RR 2->1.
C11_FAMILIES = {"CONCEPT", "MISCONCEPTION"}
C11_PATTERN_CLASSES = {"ERRONEOUS_BELIEF", "WRONG_ANSWER_PATTERN"}
C11_ROLES = {"CORE", "SUPPORTING", "ENRICHMENT"}
C11_RELATIONS = {"PART_OF", "REQUIRES_PREREQUISITE", "RELATED_TO",
                 "MISCONCEPTION_OF", "EXPLAINED_BY", "REMEDIATED_BY",
                 "COMMONLY_CONFUSED_WITH", "WRONG_ANSWER_PATTERN"}
C11_MISCONCEPTION_RELATIONS = {"MISCONCEPTION_OF", "WRONG_ANSWER_PATTERN",
                               "REMEDIATED_BY"}
C11_ANCHOR_KINDS = {"NOTE", "SPEC", "MARK_SCHEME"}
C11_STATES = {"SUGGESTED", "REVIEW_REQUIRED"}
C11_EDGE_STATES = {"SUGGESTED", "REVIEW_REQUIRED", "HUMAN_VALIDATED"}
C11_PROMOTIONS_FILE = REPO / "scripts" / "c11_promotions.yaml"
# Session-47: the decision-record REGISTRY (pilot + each authorized §16 batch
# record). The generator's registry and this list must stay in lockstep.
# session-55: the registry grows by the batch-5 record (same list as the
# generator's DECISION_RECORDS — lockstep contract).
C11_DECISIONS_FILES = [REPO / "scripts" / "c11_pilot_decisions.yaml",
                       REPO / "scripts" / "c11_batch1_decisions.yaml",
                       REPO / "scripts" / "c11_batch2_decisions.yaml",
                       REPO / "scripts" / "c11_batch3_decisions.yaml",
                       REPO / "scripts" / "c11_batch4_decisions.yaml",
                       REPO / "scripts" / "c11_batch5_decisions.yaml",
                       REPO / "scripts" / "c11_batch6_decisions.yaml",
                       REPO / "scripts" / "c11_batch7_decisions.yaml",
                       REPO / "scripts" / "c11_batch8_decisions.yaml",
                       REPO / "scripts" / "c11_batch9_decisions.yaml",
                       REPO / "scripts" / "c11_batch10_decisions.yaml",
                       REPO / "scripts" / "c11_batch11_decisions.yaml"]
C11_DECISIONS_FILE = C11_DECISIONS_FILES[0]
_C11_AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                             r"|llm|agent|model|bot", re.I)
C11_BANDS = {"high", "medium", "low"}
C11_DERIVATION_CAPS = {
    "SPEC_VERBATIM": "high", "DEFINITIONAL_DEPENDENCY": "high",
    "USED_WITHOUT_RETEACHING": "high", "EXPLICIT_TEACH_SEQUENCE": "high",
    "SINGLE_SOURCE_CAUSAL_TEACHING": "high", "ASSESSMENT_DOCUMENTED": "high",
    "EXAMINER_TIP_EXPLICIT": "high", "TEACH_SEQUENCE_WITHIN_NOTE": "medium",
    "IMPLICIT_USE": "medium", "EXAMINER_TIP_IMPLIED": "low",
    "RELATED_RESIDUAL": "medium"}
C11_GUIDE_CLASSES = {"KNOW_TERM", "EXPLAIN_HOW", "CALCULATE", "DESCRIBE_EXPERIMENT",
                     "REPRESENT_DIAGRAM", "UNDERSTAND_RELATION", "PRODUCE_EQUATION"}
RE_C11_NODE = re.compile(r"^4CH1-(CON|MIS)-[A-Z0-9-]+$")

# T-C10 norm() convention (anti-hallucination quote normalisation, shared with
# c10_map_notes.py and c11_concept_pilot.py — see those files for the source).
_C11_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def c11_norm(s):
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_C11_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def load_c11(graph_dir):
    data = {}
    for fn in C11_FILES:
        p = graph_dir / fn
        if not p.exists():
            print(f"FATAL: missing {p}", file=sys.stderr)
            sys.exit(1)
        try:
            data[fn] = yaml.safe_load(p.read_text(encoding="utf-8"))
        except yaml.YAMLError as e:
            print(f"FATAL: {fn} does not parse: {e}", file=sys.stderr)
            sys.exit(1)
        if not isinstance(data[fn], dict) or "meta" not in data[fn]:
            print(f"FATAL: {fn} is not a mapping with a 'meta' key",
                  file=sys.stderr)
            sys.exit(1)
    return data


_C11_TC10_INDEX = None
_C11_PROMO_STATE = None


def c11_promotion_state():
    """Operator-side promotion state, read from the REAL repo files (the
    negative-test graph copies cannot cheat them, same guarantee as the
    T-C10 notes crosscheck). Returns (promo_entries, problems, authored):
      promo_entries: {(src, rel, tgt): entry} from scripts/c11_promotions.yaml
      problems:      c11.13 failures (schema/anti-forgery/resolution)
      authored:      {(src, rel, tgt): validation_status} merged across
                     the decision-record registry (drift detection vs the
                     generated graph)
    """
    global _C11_PROMO_STATE
    if _C11_PROMO_STATE is not None:
        return _C11_PROMO_STATE
    problems, entries, authored = [], {}, {}
    dec = {"held": []}

    # decision-record REGISTRY (session-47: pilot + each authorized §16 batch
    # record): authored-edge identities + statuses + anti-forgery + held
    # candidates, MERGED across records
    for dec_file in C11_DECISIONS_FILES:
        if not dec_file.exists():
            problems.append(f"c11.13 decision record missing: {dec_file}")
            continue
        try:
            d = yaml.safe_load(dec_file.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            problems.append(f"c11.13 decision record does not parse: "
                            f"{dec_file}: {e}")
            continue
        for e in d.get("edges", []):
            key = (e.get("source"), e.get("relation"), e.get("target"))
            if key in authored:
                problems.append(f"c11.13 registry: edge identity {key} "
                                f"duplicated across decision records")
                continue
            authored[key] = e.get("validation_status")
            if e.get("validation_status") == "HUMAN_VALIDATED":
                problems.append(
                    f"c11.13 decision record carries HUMAN_VALIDATED on "
                    f"{key[0]} {key[1]} {key[2]} — the AI decision record may "
                    f"never carry it (anti-forgery; promotion is operator-only "
                    f"via scripts/c11_promotions.yaml)")
        for n in d.get("nodes", []):
            if n.get("validation_status") == "HUMAN_VALIDATED":
                problems.append(
                    f"c11.13 decision record carries HUMAN_VALIDATED on node "
                    f"{n.get('code')} — anti-forgery (node promotion pathway "
                    f"not built; nodes are SUGGESTED/REVIEW_REQUIRED only)")
        dec.setdefault("held", []).extend(d.get("held") or [])

    # promotions file: schema + attribution + resolution
    if C11_PROMOTIONS_FILE.exists():
        try:
            data = yaml.safe_load(C11_PROMOTIONS_FILE.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            data = {}
            problems.append(f"c11.13 promotions file does not parse: {e}")
        for i, p in enumerate(data.get("promotions") or []):
            where = f"c11.13 promotion[{i}]"
            if not isinstance(p, dict):
                problems.append(f"{where}: entry must be a mapping")
                continue
            edge = p.get("edge")
            if not isinstance(edge, dict):
                problems.append(f"{where}: 'edge' must be a mapping "
                                f"{{source, relation, target}}")
                continue
            src, rel, tgt = edge.get("source"), edge.get("relation"), \
                edge.get("target")
            if not all(isinstance(x, str) and x.strip() for x in (src, rel, tgt)):
                problems.append(f"{where}: exact identity missing/empty — "
                                f"promotion by node or relation type alone is "
                                f"forbidden")
                continue
            key = (src, rel, tgt)
            if rel not in C11_RELATIONS:
                problems.append(f"{where}: unknown relation {rel!r}")
                continue
            if rel == "PART_OF":
                problems.append(f"{where}: PART_OF is derived — not promotable "
                                f"via this pathway")
                continue
            if key in entries:
                problems.append(f"{where}: duplicate promotion for "
                                f"{src} {rel} {tgt}")
                continue
            by, dt = p.get("validated_by"), p.get("validated_date")
            if not isinstance(by, str) or not by.strip():
                problems.append(f"{where}: validated_by missing — promotion is "
                                f"operator-only")
            elif _C11_AI_NAME_RE.search(by):
                problems.append(f"{where}: validated_by {by!r} fails the "
                                f"attribution gate — AI cannot promote")
            if not isinstance(dt, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$",
                                                       dt or ""):
                problems.append(f"{where}: validated_date must be "
                                f"YYYY-MM-DD, got {dt!r}")
            ref = p.get("review_reference")
            if not isinstance(ref, str) or not ref.strip():
                problems.append(f"{where}: review_reference must name the "
                                f"ratifying review artifact")
            else:
                first = ref.split()[0]
                if first.endswith((".md", ".json", ".yaml")) \
                        and not (REPO / first).exists():
                    problems.append(f"{where}: review_reference file not "
                                    f"found: {first}")
            if key not in authored:
                # held-candidate texts use the compact no-prefix form
                s_, t_ = src.removeprefix("4CH1-"), tgt.removeprefix("4CH1-")
                hit = next((h.get("id") for h in dec.get("held", [])
                            if s_ in str(h.get("candidate", ""))
                            and t_ in str(h.get("candidate", ""))
                            and rel in str(h.get("candidate", ""))), None)
                if hit:
                    problems.append(f"{where}: {src} {rel} {tgt} is held "
                                    f"candidate {hit} — held/rejected "
                                    f"candidates are not promotable")
                else:
                    problems.append(f"{where}: no authored edge matches the "
                                    f"exact identity {src} {rel} {tgt} — "
                                    f"promotion operates on existing "
                                    f"authored-edge identities only")
                continue
            entries[key] = p

    _C11_PROMO_STATE = (entries, problems, authored)
    return _C11_PROMO_STATE


_C19_PROMO_STATE = None


def c19_promotion_state():
    """T-C19 attachment-promotion state, read from the REAL repo file (same
    guarantee as c11_promotion_state). Returns (entries, problems):
      entries: {(concept, spec_point): entry} from scripts/c19_promotions.yaml
      problems: c19.1 failures (schema/anti-forgery/resolution)
    The record is the ONLY authority that lets a derived PART_OF edge carry
    HUMAN_VALIDATED (the expansion round c11_promote.py names; nodes themselves
    are NEVER promoted — the scope guard holds).
    """
    global _C19_PROMO_STATE
    if _C19_PROMO_STATE is not None:
        return _C19_PROMO_STATE
    problems, entries = [], {}
    f = REPO / "scripts" / "c19_promotions.yaml"
    if f.exists():
        try:
            data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            data = {}
            problems.append(f"c19.1 attachment promotions file does not parse: {e}")
        for i, p in enumerate(data.get("promotions") or []):
            where = f"c19.1 promotion[{i}]"
            if not isinstance(p, dict):
                problems.append(f"{where}: entry must be a mapping")
                continue
            att = p.get("attachment")
            if not isinstance(att, dict) or not all(
                    isinstance(att.get(k), str) and att.get(k).strip()
                    for k in ("concept", "spec_point")):
                problems.append(f"{where}: 'attachment' must be a mapping "
                                f"{{concept, spec_point}} with non-empty strings")
                continue
            con, spc = att["concept"], att["spec_point"]
            key = (con, spc)
            if key in entries:
                problems.append(f"{where}: duplicate promotion for "
                                f"{con} PART_OF {spc}")
                continue
            by, dt = p.get("validated_by"), p.get("validated_date")
            if not isinstance(by, str) or not by.strip():
                problems.append(f"{where}: validated_by missing — promotion is "
                                f"operator-only")
            elif _C11_AI_NAME_RE.search(by):
                problems.append(f"{where}: validated_by {by!r} fails the "
                                f"attribution gate — AI cannot promote")
            if not isinstance(dt, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$",
                                                       dt or ""):
                problems.append(f"{where}: validated_date must be "
                                f"YYYY-MM-DD, got {dt!r}")
            ref = p.get("review_reference")
            if not isinstance(ref, str) or not ref.strip():
                problems.append(f"{where}: review_reference must name the "
                                f"ratifying review artifact")
            else:
                first = ref.split()[0]
                if first.endswith((".md", ".json", ".yaml")) \
                        and not (REPO / first).exists():
                    problems.append(f"{where}: review_reference file not "
                                    f"found: {first}")
            entries[key] = p
    _C19_PROMO_STATE = (entries, problems)
    return _C19_PROMO_STATE


def tc10_index():
    """note rel-path -> {SP codes with HUMAN_VALIDATED T-C10 mapping}."""
    global _C11_TC10_INDEX
    if _C11_TC10_INDEX is None:
        idx = {}
        for path in NOTES_ROOT_DEFAULT.rglob("*.md"):
            if "assets" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
                m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
                if not m:
                    continue
                fm = yaml.safe_load(m.group(1)) or {}
                for sp in (fm.get("spec_map") or {}).get("spec_points", []):
                    if (sp.get("provenance") or {}).get("validation_status") \
                            == "HUMAN_VALIDATED":
                        idx.setdefault(str(path.relative_to(REPO)), set()).add(
                            sp.get("code"))
            except (yaml.YAMLError, OSError):
                continue
        _C11_TC10_INDEX = idx
    return _C11_TC10_INDEX


def check_c11_concepts(c11, c09_data):
    """Check group 10 — T-C11 pilot concept nodes + command-kind tags."""
    chk = Check("c11-concepts")
    d = c11["concepts.yaml"]
    meta = d["meta"]
    sps = {sp["code"]: sp for sp in c09_data["specification_points.yaml"]
           ["specification_points"]}
    idx = tc10_index()

    def meta_checks(m, kind):
        for k in ("task", "stage", "curriculum_code", "phase", "scope",
                  "spec_points", "practicals", "negative_control", "generator",
                  "decision_record", "extraction_pass", "model_version",
                  "contract", "generated", "provenance_default",
                  "validation_gate", "edge_vocabulary", "counts"):
            if k not in m:
                chk.fail(f"c11.1 {kind}: meta missing {k!r}")
        # session-47: merged store (pilot + §16 batch 1); stage is the
        # registry-joined value emitted by the generator
        if m.get("task") != "T-C11" or m.get("stage") != C11_STAGE:
            chk.fail(f"c11.1 {kind}: not the T-C11 {C11_STAGE} store")
        if m.get("curriculum_code") != "4CH1-2017" or m.get("phase") != 3:
            chk.fail(f"c11.1 {kind}: curriculum/phase wrong")
        if m.get("generator") != C11_GENERATOR:
            chk.fail(f"c11.1 {kind}: generator {m.get('generator')!r}")
        if m.get("negative_control") != C11_NEGATIVE_CONTROL:
            chk.fail(f"c11.1 {kind}: negative_control must be 4CH1-4.15")
        if sorted(m.get("spec_points") or []) != sorted(C11_SCOPE_SPS):
            chk.fail(f"c11.1 {kind}: meta.spec_points != the 24 registry SPs "
                     f"(pilot + batch 1)")
        if m.get("provenance_default") != "AI_SUGGESTED":
            chk.fail(f"c11.1 {kind}: provenance_default must be AI_SUGGESTED")

    meta_checks(meta, "concepts")
    nodes = d["nodes"]
    if len(nodes) != C11_COUNTS["nodes"]:
        chk.fail(f"c11.2 nodes {len(nodes)} != {C11_COUNTS['nodes']}")
    if sum(1 for n in nodes if n.get("family") == "CONCEPT") \
            != C11_COUNTS["concepts"]:
        chk.fail("c11.2 concept count mismatch")
    if sum(1 for n in nodes if n.get("family") == "MISCONCEPTION") \
            != C11_COUNTS["misconceptions"]:
        chk.fail("c11.2 misconception count mismatch")
    if (meta.get("counts") or {}).get("nodes") != len(nodes):
        chk.fail("c11.1 concepts meta.counts.nodes != actual")

    seen = set()
    for n in nodes:
        code = n.get("code")
        where = f"node {code}"
        if not RE_C11_NODE.match(str(code)):
            chk.fail(f"c11.1 {where}: code not in 4CH1-(CON|MIS)-* namespace")
        if code in seen:
            chk.fail(f"c11.1 {where}: duplicate node code")
        seen.add(code)
        if n.get("family") not in C11_FAMILIES:
            chk.fail(f"c11.1 {where}: family {n.get('family')!r}")
        if n.get("validation_status") not in C11_STATES:
            chk.fail(f"c11.10 {where}: validation_status "
                     f"{n.get('validation_status')!r} (generation may emit "
                     f"SUGGESTED/REVIEW_REQUIRED only — HUMAN_VALIDATED is "
                     f"operator-only, promotion pathway not yet built)")
        if n.get("confidence") not in C11_BANDS:
            chk.fail(f"c11.1 {where}: confidence {n.get('confidence')!r}")
        # c11.14 dual-track alias discipline (operator alias policy
        # RETRIEVAL_EXEMPT, session 44, applied session 45): a term may sit on
        # exactly one track — aliases (corpus-evidenced / merge input) or
        # retrieval_only_aliases (marked unevidenced) — never both.
        ro = n.get("retrieval_only_aliases")
        if ro is not None:
            if not isinstance(ro, list) or not all(
                    isinstance(a, str) and a.strip() for a in ro):
                chk.fail(f"c11.14 {where}: retrieval_only_aliases must be a "
                         f"list of non-empty strings")
            overlap = {str(a).casefold() for a in ro} \
                & {str(a).casefold() for a in (n.get("aliases") or [])}
            if overlap:
                chk.fail(f"c11.14 {where}: dual-track violation — "
                         f"{sorted(overlap)} on BOTH alias tracks")
        prov = n.get("provenance") or {}
        for k in ("tier", "model_version", "extraction_pass", "derivation_method",
                  "derivation_notes", "upstream", "generated_date"):
            if not prov.get(k):
                chk.fail(f"c11.3 {where}: provenance.{k} missing")
        if prov.get("tier") != "AI_SUGGESTED":
            chk.fail(f"c11.3 {where}: tier must be AI_SUGGESTED")
        if prov.get("derivation_method") not in C11_DERIVATION_CAPS:
            chk.fail(f"c11.3 {where}: derivation_method not in vocabulary")
        else:
            cap = C11_DERIVATION_CAPS[prov["derivation_method"]]
            rank = {"low": 0, "medium": 1, "high": 2}
            if rank[n["confidence"]] > rank[cap]:
                chk.fail(f"c11.9 {where}: confidence {n['confidence']!r} "
                         f"exceeds cap {cap!r}")
        if n.get("family") == "MISCONCEPTION":
            if n.get("pattern_class") not in C11_PATTERN_CLASSES:
                chk.fail(f"c11.1 {where}: pattern_class required")
            if not (n.get("evidence")):
                chk.fail(f"c11.11 {where}: misconception without source-quoted "
                         f"evidence")
            if not (n.get("remediation_evidence")):
                chk.fail(f"c11.11 {where}: misconception without remediation "
                         f"evidence")
            for a in (n.get("evidence") or []) + (n.get("remediation_evidence")
                                                   or []):
                _c11_anchor_check(chk, a, where, idx, sps)
        else:
            for att in n.get("spec_points") or []:
                aw = f"{where} @ {att.get('code')}"
                if att.get("code") == C11_NEGATIVE_CONTROL:
                    chk.fail(f"c11.5 {aw}: NEGATIVE CONTROL — no node may "
                             f"attach to 4CH1-4.15")
                elif att.get("code") not in C11_SCOPE_SPS:
                    chk.fail(f"c11.5 {aw}: outside the decision-record "
                             f"registry scope (pilot + batch 1)")
                if att.get("role") not in C11_ROLES:
                    chk.fail(f"c11.1 {aw}: role {att.get('role')!r}")
                _c11_attachment_check(chk, att, aw, idx, sps)

    # command kinds
    ck = c11["spec_command_kinds.yaml"]
    meta_checks(ck["meta"], "command_kinds")
    cks = ck["command_kinds"]
    if len(cks) != C11_COUNTS["command_kinds"]:
        chk.fail(f"c11.12 {len(cks)} command-kind tags != "
                 f"{C11_COUNTS['command_kinds']}")
    if sorted(c.get("code") for c in cks) != sorted(C11_SCOPE_SPS):
        chk.fail("c11.12 command-kind codes != the pilot + batch-1 SPs")
    for c in cks:
        where = f"command_kind {c.get('code')}"
        if c.get("guide_class") not in C11_GUIDE_CLASSES:
            chk.fail(f"c11.12 {where}: guide_class {c.get('guide_class')!r}")
        if c.get("verb") != sps.get(c.get("code"), {}).get("leading_verb"):
            chk.fail(f"c11.12 {where}: verb != registry leading_verb")
        for k in ("verb", "guide_class", "demanded_substance"):
            if not c.get(k):
                chk.fail(f"c11.12 {where}: missing {k!r}")
    return chk


def _c11_anchor_check(chk, a, where, idx, sps):
    if not isinstance(a, dict) or a.get("kind") not in C11_ANCHOR_KINDS:
        chk.fail(f"c11.1 {where}: bad anchor {a!r}")
        return
    rel, quote = a.get("file"), a.get("quote")
    if not rel or not quote:
        chk.fail(f"c11.1 {where}: anchor missing file/quote")
        return
    # Session-55 repair (2026-09-22, dated): frozen decision records carry the
    # historical root-form SPEC anchor path; the C28 registry legacy_map
    # resolves it to the canonical store location (C28 P5 — records stay
    # historical, checkers resolve; one resolver for all checkers).
    rel = GP.resolve_rel(rel)
    p = REPO / rel
    if not p.exists():
        chk.fail(f"c11.4 {where}: anchor file missing: {rel}")
        return
    if a["kind"] == "NOTE" and "Chemistry IGCSE Revision Notes" not in rel:
        chk.fail(f"c11.1 {where}: NOTE anchor outside the notes corpus: {rel}")
    if a["kind"] == "SPEC" and rel != GP.store_rel("specification_points"):
        chk.fail(f"c11.1 {where}: SPEC anchor must be "
                 f"{GP.store_rel('specification_points')}: {rel}")
    if a["kind"] == "MARK_SCHEME" and not rel.startswith("scripts/c11_evidence/"):
        chk.fail(f"c11.1 {where}: MARK_SCHEME anchor outside the pinned "
                 f"extractions: {rel}")
    if c11_norm(quote) not in c11_norm(p.read_text(encoding="utf-8")):
        chk.fail(f"c11.4 {where}: quote NOT found in {rel} :: {quote[:60]!r}")


def _sp_anchor_text(sp):
    """Definitive anchor text for a spec point: official wording + PDF bullets."""
    t = sp["official_wording"]
    b = sp.get("official_bullets")
    if b:
        t += " " + " ".join(b)
    return t


def _c11_attachment_check(chk, att, where, idx, sps):
    ok = False
    for a in att.get("evidence") or []:
        _c11_anchor_check(chk, a, where, idx, sps)
        kind, rel, quote = a.get("kind"), a.get("file"), a.get("quote")
        if kind == "SPEC":
            sp = sps.get(att.get("code"))
            if sp and c11_norm(quote) in c11_norm(_sp_anchor_text(sp)):
                ok = True
        elif kind == "NOTE":
            if att.get("code") in idx.get(rel, set()):
                ok = True
    if not ok:
        chk.fail(f"c11.6 {where}: no anchor resolves to the SP (SPEC quote "
                 f"inside its official wording, or a NOTE whose T-C10 mapping "
                 f"to this SP is HUMAN_VALIDATED)")


def check_c11_concept_edges(c11, c09_data):
    """Check group 11 — T-C11 pilot concept edges (derived PART_OF + authored)."""
    chk = Check("c11-concept-edges")
    d = c11["concept_edges.yaml"]
    meta = d["meta"]
    sps = {sp["code"]: sp for sp in c09_data["specification_points.yaml"]
           ["specification_points"]}
    prs = {p["code"]: p for p in c09_data["practicals.yaml"]["practicals"]}
    idx = tc10_index()
    nodes = {n["code"]: n for n in c11["concepts.yaml"]["nodes"]}
    # §18 promotion crosscheck state — always read from the REAL repo files
    # (promotions record + frozen decision record), corruption-proof for the
    # negative-test graph copies
    promo_entries, promo_problems, authored_states = c11_promotion_state()
    for msg in promo_problems:
        chk.fail(msg)
    c19_entries, c19_problems = c19_promotion_state()
    for msg in c19_problems:
        chk.fail(msg)

    for k in ("counts",):
        if k not in meta:
            chk.fail(f"c11.1 edges: meta missing {k!r}")
    edges = d["edges"]
    counts = meta.get("counts") or {}
    if counts.get("edges") != len(edges):
        chk.fail(f"c11.1 edges: meta.counts.edges {counts.get('edges')} "
                 f"!= actual {len(edges)}")
    if len(edges) != C11_COUNTS["edges"]:
        chk.fail(f"c11.2 edges {len(edges)} != {C11_COUNTS['edges']}")
    by_rel = {}
    for e in edges:
        by_rel[e.get("relation")] = by_rel.get(e.get("relation"), 0) + 1
    for r in C11_RELATIONS:
        want = C11_COUNTS[r.lower()]
        if by_rel.get(r, 0) != want:
            chk.fail(f"c11.2 {r} edges {by_rel.get(r, 0)} != {want}")
    # REVIEW_REQUIRED is decision-record state minus promotions settled on the
    # two RR edges (derived, not frozen: promotion of an RR edge consumes it)
    expected_rr = sum(1 for k, st in authored_states.items()
                      if st == "REVIEW_REQUIRED" and k not in promo_entries)
    if sum(1 for e in edges if e.get("validation_status") == "REVIEW_REQUIRED") \
            != expected_rr:
        chk.fail(f"c11.2 REVIEW_REQUIRED edge count mismatch (expected "
                 f"{expected_rr} from decisions-promotions)")

    universe = set(nodes) | set(C11_SCOPE_SPS) | set(prs)
    seen = set()
    prereq = {}
    part_of_derived = set()
    for e in edges:
        src, rel, tgt = e.get("source"), e.get("relation"), e.get("target")
        where = f"edge {src} -[{rel}]-> {tgt}"
        if rel not in C11_RELATIONS:
            chk.fail(f"c11.1 {where}: unknown relation type")
            continue
        if src == tgt:
            chk.fail(f"c11.8 {where}: self-edge")
        key = (src, rel, tgt)
        if key in seen:
            chk.fail(f"c11.8 {where}: duplicate edge")
        seen.add(key)
        for end in (src, tgt):
            if end not in universe:
                chk.fail(f"c11.7 {where}: endpoint {end!r} not in the pilot "
                         f"node universe")
        if e.get("validation_status") not in C11_EDGE_STATES:
            chk.fail(f"c11.10 {where}: validation_status "
                     f"{e.get('validation_status')!r} (operator-only promotion)")
        else:
            status = e.get("validation_status")
            promo = promo_entries.get(key)
            if status == "HUMAN_VALIDATED":
                if rel == "PART_OF":
                    # T-C19: legal ONLY via an exact attachment-promotion
                    # record match (the expansion round; the concept NODE's
                    # own status is untouched by this pathway)
                    c19p = c19_entries.get((src, tgt))
                    if c19p is None:
                        chk.fail(f"c11.10 {where}: PART_OF HUMAN_VALIDATED "
                                 f"without a matching attachment promotion "
                                 f"record in scripts/c19_promotions.yaml "
                                 f"(operator-only promotion; "
                                 f"graph/promotions mismatch)")
                    elif (e.get("validated_by") != c19p.get("validated_by")
                          or e.get("validated_date") != c19p.get("validated_date")):
                        chk.fail(f"c11.10 {where}: attribution mismatch vs "
                                 f"the attachment promotion record (graph: "
                                 f"{e.get('validated_by')!r}/"
                                 f"{e.get('validated_date')!r}; record: "
                                 f"{c19p.get('validated_by')!r}/"
                                 f"{c19p.get('validated_date')!r})")
                elif not promo:
                    chk.fail(f"c11.10 {where}: HUMAN_VALIDATED without a "
                             f"matching promotion record in "
                             f"scripts/c11_promotions.yaml (operator-only "
                             f"promotion; graph/promotions mismatch)")
                elif (e.get("validated_by") != promo.get("validated_by")
                      or e.get("validated_date") != promo.get("validated_date")):
                    chk.fail(f"c11.10 {where}: attribution mismatch vs the "
                             f"promotion record (graph: "
                             f"{e.get('validated_by')!r}/"
                             f"{e.get('validated_date')!r}; record: "
                             f"{promo.get('validated_by')!r}/"
                             f"{promo.get('validated_date')!r})")
            elif promo and rel != "PART_OF":
                chk.fail(f"c11.10 {where}: promotion recorded but edge not "
                         f"promoted (stale graph — re-run "
                         f"scripts/c11_concept_pilot.py)")
            if rel == "PART_OF" and status != "HUMAN_VALIDATED" \
                    and (src, tgt) in c19_entries:
                chk.fail(f"c11.10 {where}: attachment promotion recorded but "
                         f"edge not promoted (stale graph — re-run "
                         f"scripts/c11_concept_pilot.py)")
            # status drift vs the frozen decision record + promotions
            if rel != "PART_OF":
                if key not in authored_states:
                    chk.fail(f"c11.10 {where}: not authored in any "
                             f"decision record of the registry "
                             f"(hand-injected edge)")
                else:
                    want_status = ("HUMAN_VALIDATED" if promo
                                   else authored_states[key])
                    if status != want_status:
                        chk.fail(f"c11.10 {where}: status drift — decision "
                                 f"record+promotions say {want_status!r}, "
                                 f"graph says {status!r}")
        if e.get("validation_status") == "REVIEW_REQUIRED" \
                and not e.get("ambiguity_note"):
            chk.fail(f"c11.1 {where}: REVIEW_REQUIRED requires ambiguity_note")
        if e.get("confidence") not in C11_BANDS:
            chk.fail(f"c11.1 {where}: confidence {e.get('confidence')!r}")
        prov = e.get("provenance") or {}
        for k in ("tier", "model_version", "extraction_pass", "derivation_method",
                  "derivation_notes", "upstream", "generated_date"):
            if not prov.get(k):
                chk.fail(f"c11.3 {where}: provenance.{k} missing")
        if prov.get("tier") != "AI_SUGGESTED":
            chk.fail(f"c11.3 {where}: tier must be AI_SUGGESTED")
        if prov.get("derivation_method") not in C11_DERIVATION_CAPS:
            chk.fail(f"c11.3 {where}: derivation_method not in vocabulary")
        else:
            cap = C11_DERIVATION_CAPS[prov["derivation_method"]]
            rank = {"low": 0, "medium": 1, "high": 2}
            if rank[e["confidence"]] > rank[cap]:
                chk.fail(f"c11.9 {where}: confidence exceeds cap {cap!r}")

        sn, tn = nodes.get(src), nodes.get(tgt)
        if rel == "PART_OF":
            if not (sn and sn.get("family") == "CONCEPT"):
                chk.fail(f"c11.8 {where}: PART_OF source must be a CONCEPT")
            if tgt not in C11_SCOPE_SPS:
                chk.fail(f"c11.5 {where}: PART_OF target must be an "
                         f"in-scope SP (pilot or batch 1)")
            if e.get("role") not in C11_ROLES:
                chk.fail(f"c11.1 {where}: PART_OF role {e.get('role')!r}")
            part_of_derived.add((src, tgt, e.get("role")))
        elif rel in C11_MISCONCEPTION_RELATIONS:
            if not (sn and sn.get("family") == "MISCONCEPTION"):
                chk.fail(f"c11.8 {where}: source must be MISCONCEPTION-family")
            want = ("ERRONEOUS_BELIEF" if rel == "MISCONCEPTION_OF"
                    else "WRONG_ANSWER_PATTERN")
            if rel != "REMEDIATED_BY" and sn and sn.get("pattern_class") != want:
                chk.fail(f"c11.8 {where}: pattern_class "
                         f"{sn.get('pattern_class')!r} does not match {rel} "
                         f"(frozen triple distinction)")
            if not (tn and tn.get("family") == "CONCEPT"):
                chk.fail(f"c11.8 {where}: target must be a CONCEPT")
        elif rel == "EXPLAINED_BY":
            if not (sn and sn.get("family") == "CONCEPT" and tn
                    and tn.get("family") == "CONCEPT"):
                chk.fail(f"c11.8 {where}: EXPLAINED_BY must be CONCEPT->CONCEPT")
        elif rel == "REQUIRES_PREREQUISITE":
            if not (sn and sn.get("family") == "CONCEPT") and src not in prs:
                chk.fail(f"c11.8 {where}: source must be a concept or practical")
            if not (tn and tn.get("family") == "CONCEPT"):
                chk.fail(f"c11.8 {where}: target must be a CONCEPT")
            prereq.setdefault(src, set()).add(tgt)
        elif rel in ("RELATED_TO", "COMMONLY_CONFUSED_WITH"):
            if not (sn and tn and sn.get("family") == "CONCEPT"
                    and tn.get("family") == "CONCEPT"):
                chk.fail(f"c11.8 {where}: {rel} must be CONCEPT->CONCEPT")

        # anchor admissibility (rule 2 / §11: NOTE anchors must resolve through
        # T-C10 HUMAN_VALIDATED coverage of an attached SP of source or target;
        # MARK_SCHEME anchors are misconception-class only — this is the gate
        # that makes premise+consequence aggregation from uncovered notes fail)
        attached = set()
        for n_ in (sn, tn):
            if n_ and n_.get("family") == "CONCEPT":
                attached |= {a["code"] for a in n_.get("spec_points") or []}
        if src in prs:
            attached.add(prs[src]["spec_point"])
        ok = False
        for a in e.get("evidence") or []:
            _c11_anchor_check(chk, a, where, idx, sps)
            kind, relf, quote = a.get("kind"), a.get("file"), a.get("quote")
            if kind == "MARK_SCHEME":
                if rel in C11_MISCONCEPTION_RELATIONS:
                    ok = True
                else:
                    chk.fail(f"c11.6 {where}: MARK_SCHEME anchor inadmissible "
                             f"for {rel} (assessment evidence is "
                             f"misconception-class only)")
            elif kind == "SPEC":
                if any(c11_norm(quote) in c11_norm(_sp_anchor_text(sps[sp]))
                       for sp in attached if sp in sps):
                    ok = True
            elif kind == "NOTE":
                if any(sp in idx.get(relf, set()) for sp in attached):
                    ok = True
        if not ok:
            chk.fail(f"c11.6 {where}: no anchor is admissible (NOTE anchors "
                     f"must HUMAN_VALIDATED-map to an attached SP of the "
                     f"source/target; SPEC quotes must sit inside an attached "
                     f"SP's wording)")

    # PART_OF set must equal the attachments declared in concepts.yaml
    declared = set()
    for code, n in nodes.items():
        if n.get("family") == "CONCEPT":
            for att in n.get("spec_points") or []:
                declared.add((code, att["code"], att.get("role")))
    if part_of_derived != declared:
        chk.fail(f"c11.7 PART_OF edges != concepts.yaml attachments "
                 f"(missing {sorted(declared - part_of_derived)[:3]}, "
                 f"extra {sorted(part_of_derived - declared)[:3]})")

    # §18 promotions are audited BOTH ways: every promotion entry must appear
    # in the graph as HUMAN_VALIDATED with the exact recorded attribution
    # (catches stale graphs after a promotion was recorded or a removal)
    for key, p in sorted(promo_entries.items()):
        if key not in seen:
            chk.fail(f"c11.13 promotion for {key[0]} {key[1]} {key[2]} has no "
                     f"edge in the graph (stale or corrupted promotion record)")
            continue
        ge = next(e for e in edges if (e.get("source"), e.get("relation"),
                                       e.get("target")) == key)
        if ge.get("validation_status") != "HUMAN_VALIDATED":
            chk.fail(f"c11.13 promotion for {key[0]} {key[1]} {key[2]} not "
                     f"reflected in the graph (status "
                     f"{ge.get('validation_status')!r} — regenerate)")
    n_promoted = sum(1 for e in edges
                     if e.get("validation_status") == "HUMAN_VALIDATED")
    if promo_entries:
        if meta.get("promotion_record") != "scripts/c11_promotions.yaml":
            chk.fail("c11.13 edges meta.promotion_record must be "
                     "scripts/c11_promotions.yaml when promotions exist")
        if counts.get("promoted_edges") != n_promoted:
            chk.fail(f"c11.13 meta.counts.promoted_edges "
                     f"{counts.get('promoted_edges')} != actual {n_promoted}")
        if counts.get("human_validated_edges") != n_promoted:
            chk.fail(f"c11.13 meta.counts.human_validated_edges "
                     f"{counts.get('human_validated_edges')} != actual "
                     f"{n_promoted}")

    # acyclicity of REQUIRES_PREREQUISITE
    color = {}

    def dfs(u):
        color[u] = 1
        for v in sorted(prereq.get(u, ())):
            if color.get(v) == 1:
                return [u, v]
            if color.get(v, 0) == 0:
                cyc = dfs(v)
                if cyc:
                    return cyc
        color[u] = 2
        return None

    for u in sorted(prereq):
        if color.get(u, 0) == 0:
            cyc = dfs(u)
            if cyc:
                chk.fail(f"c11.8 REQUIRES_PREREQUISITE cycle: {cyc}")
                break
    return chk


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--graph", default=str(GRAPH_DEFAULT))
    ap.add_argument("--notes-root", default=str(NOTES_ROOT_DEFAULT))
    args = ap.parse_args()
    graph_dir = Path(args.graph)

    data = load_all(graph_dir)
    results = []
    results.append(check_meta(data))
    pt_chk, point_codes = check_spec_points(data)
    results.append(pt_chk)
    tp_chk, topic_codes, sub_codes, sub_members = check_topics(data, point_codes)
    results.append(tp_chk)
    results.append(check_relationships(data, point_codes, topic_codes, sub_codes,
                                        sub_members))
    results.append(check_command_words(data))
    results.append(check_practicals(data, point_codes))
    results.append(check_assessment(data))
    results.append(check_namespace_prose(data))
    results.append(check_notes_mapping(data, point_codes, sub_codes,
                                       notes_root=args.notes_root))
    # groups 10-11: T-C11 pilot concept graph (reads the three c11 files from
    # the same graph dir; T-C10 crosscheck always uses the REAL notes root so
    # negative tests can corrupt the graph copy alone)
    c11 = load_c11(graph_dir)
    results.append(check_c11_concepts(c11, data))
    results.append(check_c11_concept_edges(c11, data))

    total_fail = 0
    for chk in results:
        if chk.ok:
            print(f"PASS  {chk.name}")
        else:
            print(f"FAIL  {chk.name} ({len(chk.failures)} issue(s)):")
            for msg in chk.failures[:20]:
                print(f"      - {msg}")
            if len(chk.failures) > 20:
                print(f"      ... and {len(chk.failures) - 20} more")
            total_fail += len(chk.failures)
    print()
    if total_fail:
        print(f"graph_check: {total_fail} failure(s) across "
              f"{sum(1 for c in results if not c.ok)} check group(s).")
        sys.exit(1)
    n_points = len(point_codes)
    c11_promoted = sum(1 for e in c11["concept_edges.yaml"]["edges"]
                       if e.get("validation_status") == "HUMAN_VALIDATED")
    print(f"graph_check: ALL PASS — {n_points} spec points, "
          f"{len(topic_codes)} topics, {len(sub_codes)} subtopics, "
          f"{COUNTS['edges']} edges, {COUNTS['command_words']} command words, "
          f"{COUNTS['practicals']} practicals, {COUNTS['papers']} papers; "
          # session-58: the summary names the batch-6 verdict application
          # (§18 applied — 16 operator promotions); state note, no test
          # weakened
          # session-59: the summary names the batch-7 authored-to-gate
          # state (S2 batches 5-7; the batch-7 verdicts pending — the
          # operator's gate session is next)
          # session-60: the summary names the batch-7 verdict application
          # (§18 applied — 19 operator promotions, the addendum §6/§7
          # verdict PASS WITH NOTES); state note, no test weakened
          # session-61: the summary names the batch-8 authored-to-gate
          # state (S2 batches 5-8; the batch-8 verdicts pending — the
          # operator's gate session is next)
          # session-62: the summary names the batch-8 verdict application
          # (§18 applied — 10 operator promotions, the completed-sheet
          # §6/§7 verdict PASS WITH NOTES); state note, no test weakened
          # session-63: the summary names the batch-9 verdict application
          # (§18 applied — 20 operator promotions, the completed-sheet
          # §6/§7 verdict PASS WITH NOTES); state note, no test weakened
          # session-66: the summary names the batch-11 authored-to-gate
          # slice (S4-g/h — the store's stage string grows; state note, no
          # test weakened)
          # session-67: the summary names the batch-11 verdict application
          # (§18 applied — 17 operator promotions, the session-67 operator
          # verdict PASS WITH NOTES / Batch 11: ACCEPTED); state note, no
          # test weakened
          f"T-C11 store (pilot + §16 batches 1-3 + S3 batch 4 + S2 batches "
          f"5-8 + the batch-9 slice S4-a/b/c 4.1-4.22 + the batch-10 "
          f"authored-to-gate slice S4-d/e/f 4.23-4.37C + the batch-11 "
          f"slice S4-g/h 4.38C-4.50C, "
          f"batch-6 verdicts applied session 58, batch-7 verdicts "
          f"applied session 60, batch-8 verdicts applied session 62, "
          f"batch-9 verdicts applied session 63, batch-10 verdicts "
          f"applied session 65, batch-11 verdicts applied session 67): "
          f"{C11_COUNTS['nodes']} concept "
          f"nodes, "
          f"{C11_COUNTS['edges']} concept edges "
          f"({C11_COUNTS['part_of']} PART_OF + "
          f"{C11_COUNTS['edges'] - C11_COUNTS['part_of']} semantic), "
          f"{c11_promoted} HUMAN_VALIDATED (operator promotions; 0 from "
          f"generation; batch-1 verdicts applied session 48; batch-2 "
          f"verdicts applied session 50; batch-3 verdicts applied session 52; "
          f"batch-4 verdicts applied session 54; batch-5 verdicts applied "
          f"session 56; batch-6 verdicts applied session 58; batch-7 "
          f"verdicts applied session 60; batch-8 verdicts applied "
          f"session 62; batch-9 verdicts applied session 63; batch-10 "
          f"verdicts applied session 65; batch-11 verdicts applied "
          f"session 67 — "
          f"nodes have no §18 pathway), "
          f"negative control "
          f"{C11_NEGATIVE_CONTROL} "
          f"uncovered.")


if __name__ == "__main__":
    main()
