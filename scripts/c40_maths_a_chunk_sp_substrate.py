#!/usr/bin/env python3
"""c40 — the maths-a chunk→SpecificationPoint mapping substrate (T-C40 K2 Lane B;
the c13-chunk-convention-1 construction instantiated for the SME JSON notes corpus).

T-C42 R3 AMENDMENT (2026-10-02, dated per P5 — this generator re-pinned, landed
records never edited): substrate re-build over the C42-R1-amended resolution via
the R2-refreshed T-C32 join. Three semantic changes, everything else untouched:
  a. the pinned join census moves 202+1 -> 200+3 (the C31 §3 residual + the 2
     anchors the R1 operator verdict round cleared UNRESOLVED: Mathematical
     Symbols, Problem Solving with Areas); the cleared spans' chunks become
     worklist rows, RECORDED never forced;
  b. the operator section-override map scripts/c42_section_overrides.yaml
     (surface 3 of the R1 verdict round: 12 REATTRIBUTE + 4 RETAIN over 16
     section-level rows) is consumed FAIL-CLOSED: every entry must hit exactly
     one emitted chunk row, its current_code must equal the join-derived code
     (the map was authored against the post-R1 projection — drift is a bug),
     REATTRIBUTE targets must sit in the ratified registry, and any override
     naming a code outside the ratified 188 fails the build. Applied rows carry
     provenance.override with the map sha — the R4 re-fill sees exactly what
     the operator ruled;
  c. coverage + the uncovered-SP worklist are RECOMPUTED from the refreshed
     surface (the C40-era 111-code bound stays on its own record as a
     measurement under the defective mapping).
CHUNK IDENTITY INVARIANT: the chunker, the c40-chunk-convention-1 convention
and the corpus are untouched — note_path/ordinal/heading/sha256_16 never move;
only code attribution changes. Verified old-blob vs new-file by
scripts/c42_r2_r3_join_substrate_check.py against the pinned pre-R3 blob
f3b2cc2be76934ee3b547a9b4e75d41581ceb6a6.

C31 §6 prescribes Lane B as the T-C13 pattern replayed over the maths-a notes
corpus, emitting graph/igcse-maths-a/spec_chunk_mappings.yaml behind a review
sheet whose class precision must reach >=90% before any promotion. The maths-a
upstream differs from chemistry's and the difference is carried honestly:

  chemistry  upstream = T-C10 note-level spec_map, 209 rows HUMAN_VALIDATED
             (operator, 2026-09-11); quote-anchor construction refined each
             mapping's verbatim evidence quote into its passage chunk.
  maths-a    upstream = the T-C32 K2-A notes-join (200 joins / 3 unresolved
             post-C42-R1; AI_VALIDATED operator-delegated chain — the honesty
             tier C31 §4.5 requires on record). The join carries NO evidence
             quotes, so the anchoring axis is the corpus's OWN structure: every
             note is a sequence of SP spans, each introduced by a `spec_point`
             block (203 blocks / 191 notes, machine-censused); the span marker
             plus the T-C32 id-join gives the chunk→SP identity and the row's
             evidence quote is a deterministic verbatim self-slice of the chunk
             (match_type "span-marker"). Nothing is invented: the SP identity is
             the corpus's own anchor + the recorded join, and the quote is the
             chunk's own text.

Construction (deterministic, zero-LLM, fail-closed):
  1. Chunk every note at the PINNED convention (c40-chunk-convention-1):
     a note = one or more SP spans split at `spec_point` blocks; within a
     span, leaf sections cut at heading blocks of level 2..4; chunk text =
     its own heading + the rendered content blocks (the C10 heading-quote
     lesson: chunks must be retrievable by their heading words). A span's
     non-heading preamble (before its first heading) is an intro chunk and is
     NEVER an anchor target.
  2. Emit one anchored row per content chunk of every RESOLVED span
     (span marker → T-C32 join → ratified 4MA1 code) + worklist rows for the
     three unresolved spans' chunks and for every SP the notes corpus does not
     cover; apply the operator section-override map fail-closed. NO row is
     ever emitted HUMAN_VALIDATED: promotion is the operator review-sheet gate
     (anti-forgery, C10/C11/C13 norm).
  3. Emit the construction report + the operator review sheet (seeded
     stratified sample; scripts/c40_maths_a_substrate_report.py).

Gates (fail-closed; negative-tested by construction in this build's battery):
  G1 corpus shape     191 notes, 203 spec_point blocks, every note's first
                      block is its span marker, manifest counts == blocks
  G2 join shape       200 resolved + 3 unresolved (exact post-R1 id set);
                      every note-block anchor is joined or one of THE three
                      unresolved rows; every join anchor exists
  G3 code validity    every emitted code ∈ the ratified 188-point store
                      (override REATTRIBUTE targets included)
  G4 anchor fidelity  every emitted row re-verifies quote-in-chunk against a
                      fresh re-chunking after emit
  G5 anti-forgery     zero HUMAN_VALIDATED rows; tier RULE_DERIVED; the
                      upstream validation tier is recorded verbatim as
                      AI_VALIDATED (operator-delegated chain) — never human
  G6 worklist complete  every uncovered SP + every unresolved-span chunk
                      enumerated with a disposition
  G7 idempotency      two in-process runs byte-identical
"""
from __future__ import annotations

import hashlib
import json
import re
import statistics
import subprocess
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

import yaml

TOOL = "scripts/c40_maths_a_chunk_sp_substrate.py"
TOOL_VERSION = "2.0.0"
CONVENTION_ID = "c40-chunk-convention-1"
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
CORPUS = f"SME-RevisionNotes/{COURSE}"
JOIN = ("Official-Specifications/parsed/_derived/notes-join/"
        "igcse-maths-a-18-higher.json")
OVERRIDES = "scripts/c42_section_overrides.yaml"
# surface 1 of the C42 R1 verdict round: 2 anchors cleared UNRESOLVED (their
# wrong T-SPEC-7-era codes removed, never forced) — distinct from the C31 §3
# residual that was already unresolved
R1_CLEARED = {"spcpt_8Wtthy9gt8B5xsVW", "spcpt_3fMGfNtg3hXMg6gC"}
UPSTREAM_TIER = "AI_VALIDATED (operator-delegated chain)"
MAX_CUT_LEVEL = 4
INTRO_HEADING = "(intro)"
QUOTE_CHARS = 240

_TRANS = {ord("‘"): "'", ord("’"): "'", ord("“"): '"', ord("”"): '"',
          ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    """Markdown-insensitive normalization shared with the C10/C13 evidence
    gates: apply to BOTH sides, then substring-match."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def sha16(s) -> str:
    data = s.encode("utf-8") if isinstance(s, str) else s
    return hashlib.sha256(data).hexdigest()[:16]


class R:
    """disk-first / git-fallback reader over ONE persistent cat-file batch
    (the c32 convention — the corpus lives in-repo behind skip-worktree)."""

    def __init__(self):
        self.methods: dict[str, str] = {}
        self._cache: dict[str, bytes] = {}
        self._proc = None

    def _show(self, rel: str) -> bytes:
        if self._proc is None:
            self._proc = subprocess.Popen(
                ["git", "-C", str(GP_REPO), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        self._proc.stdin.write(f"HEAD:{rel}\n".encode())
        self._proc.stdin.flush()
        parts = self._proc.stdout.readline().decode().split()
        if len(parts) < 3 or parts[1] == "missing":
            raise FileNotFoundError(rel)
        body = self._proc.stdout.read(int(parts[2]))
        self._proc.stdout.read(1)
        return body

    def close(self):
        if self._proc is not None:
            try:
                self._proc.stdin.close()
                self._proc.terminate()
            except Exception:
                pass
            self._proc = None

    def read_bytes(self, rel: str) -> bytes:
        if rel not in self._cache:
            p = GP_REPO / rel
            if p.is_file():
                self.methods[rel] = "disk"
                self._cache[rel] = p.read_bytes()
            else:
                self.methods[rel] = "git-show"
                self._cache[rel] = self._show(rel)
        return self._cache[rel]

    def read_json(self, rel: str):
        return json.loads(self.read_bytes(rel).decode("utf-8"))


GP_REPO = Path(__file__).resolve().parent.parent


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


# ------------------------------------------------------------------ chunking --
def render_block(b: dict) -> str:
    """Deterministic text rendering of one content block (zero invention:
    only the block's own payload fields, verbatim)."""
    t = b["type"]
    if t in ("bullets", "paragraph", "table"):
        return (b.get("md") or "").strip()
    if t == "callout":
        label, md = (b.get("label") or "").strip(), (b.get("md") or "").strip()
        return f"{label}: {md}" if label else md
    if t == "figure":
        return ((b.get("caption") or "").strip()
                or (b.get("alt") or "").strip())
    return ""


def chunk_note(note: dict):
    """Return the note's chunks under the pinned c40 convention.

    A note = SP spans split at `spec_point` blocks (the corpus's own span
    markers); within a span, sections cut at heading blocks level 2..4; chunk
    text = its own heading + rendered content (the C10 heading-quote lesson).
    Ordinals are per NOTE — stable chunk identity for the forward contract —
    sequential across spans. A span's non-heading preamble before its first
    heading is an intro chunk and is NEVER an anchor target (the C13 intro
    discipline). Every chunk carries the span marker id (anchor_id) scoping
    it and the span's own name.
    """
    chunks: list[dict] = []

    cur: dict | None = None  # {anchor_id, span_name, heading, level, buf}

    def open_span(b: dict):
        return {"anchor_id": b["id"], "span_name": (b.get("name") or "").strip(),
                "heading": None, "level": 0, "buf": []}

    def flush():
        nonlocal cur
        if cur is None:
            return
        if cur["heading"] is None:
            text = "\n".join(cur["buf"]).strip()
            if text:
                chunks.append({"ordinal": len(chunks), "is_intro": True,
                               "anchor_id": cur["anchor_id"],
                               "span_name": cur["span_name"],
                               "heading": INTRO_HEADING, "heading_level": 0,
                               "text": text})
        else:
            text = (cur["heading"] + "\n" + "\n".join(cur["buf"])).strip()
            chunks.append({"ordinal": len(chunks), "is_intro": False,
                           "anchor_id": cur["anchor_id"],
                           "span_name": cur["span_name"],
                           "heading": cur["heading"],
                           "heading_level": cur["level"], "text": text})
        cur = None

    for b in note["blocks"]:
        t = b["type"]
        if t == "spec_point":
            flush()
            cur = open_span(b)
        elif t == "heading" and 2 <= int(b.get("level") or 0) <= MAX_CUT_LEVEL:
            # close whatever is open (span intro or previous section); the
            # new section inherits the OPEN SPAN's anchor
            anchor_id = cur["anchor_id"] if cur else None
            span_name = cur["span_name"] if cur else ""
            if anchor_id is None:
                fail("heading outside any span (no spec_point marker seen)")
            flush()
            cur = {"anchor_id": anchor_id, "span_name": span_name,
                   "heading": (b.get("text") or "").strip(),
                   "level": int(b["level"]), "buf": []}
        else:
            if cur is None:
                fail(f"content block before the first spec_point marker: {t}")
            rendered = render_block(b)
            if rendered:
                cur["buf"].append(rendered)
    flush()
    return chunks


def self_quote(text: str) -> str:
    """Deterministic verbatim self-slice: the chunk's own first <=QUOTE_CHARS
    characters, cut at a whitespace boundary (never mid-word).

    Fail-safe against markdown constructs: a raw prefix cut can land inside a
    link/emphasis span, where norm() of the slice diverges from norm() of the
    whole text (an unclosed '[...]' is not link-stripped). The cut therefore
    walks BACK over whitespace boundaries until norm(quote) is a verbatim
    substring of norm(text); never fabricated, only shortened. Deterministic
    and fail-closed if no boundary >= 40 chars verifies."""
    if norm(text) == "":
        fail("self_quote on an empty chunk")
    ntext = norm(text)
    if len(text) <= QUOTE_CHARS:
        return text
    cut = text[:QUOTE_CHARS]
    while True:
        nq = norm(cut)
        if nq and nq in ntext:
            return cut
        sp = cut.rfind(" ")
        if sp < 40:
            fail(f"self_quote: no verifiable boundary in chunk "
                 f"({len(text)} chars) — fail closed")
        cut = cut[:sp]


# ------------------------------------------------------------------- loading --
def load_corpus(r: R):
    man = r.read_json(f"{CORPUS}/manifest.json")
    pages = man.get("pages") or []
    notes = []
    for p in pages:
        rel = f"{CORPUS}/{p['path']}"
        note = r.read_json(rel)
        notes.append({"manifest": p, "note": note, "rel": rel})
    return man, notes


def load_join(r: R) -> dict:
    return r.read_json(JOIN)


def load_registry() -> dict:
    sp_store = GP.store("specification_points", QUAL)
    doc = yaml.safe_load(sp_store.read_text(encoding="utf-8"))
    return {p["code"]: p for p in doc["specification_points"]}


def span_chunks(notes):
    """Chunk every note; return per-note chunk lists + structural census."""
    by_note, n_markers, n_intros, n_sections = {}, 0, 0, 0
    for n in notes:
        note = n["note"]
        blocks = note["blocks"]
        if not blocks or blocks[0]["type"] != "spec_point":
            fail(f"G1 {n['rel']}: first block is not a spec_point marker")
        cs = chunk_note(note)
        for c in cs:
            c["note_path"] = n["manifest"]["path"]
            c["note_title"] = note.get("title") or ""
        by_note[n["manifest"]["path"]] = cs
        n_markers += sum(1 for b in blocks if b["type"] == "spec_point")
        n_intros += sum(1 for c in cs if c["is_intro"])
        n_sections += sum(1 for c in cs if not c["is_intro"])
    return by_note, {"markers": n_markers,
                     "intro_chunks": n_intros, "section_chunks": n_sections}


# --------------------------------------------------------------------- build --
def construct() -> dict:
    """The full deterministic construction: reads corpus + join + registry,
    applies the G1-G6 gates, returns the store document (not yet written)."""
    r = R()
    man, notes = load_corpus(r)
    join = load_join(r)
    registry = load_registry()
    _manifest_pin = sha16(r.read_bytes(f"{CORPUS}/manifest.json"))

    # ---- G1 corpus shape -----------------------------------------------------
    if len(notes) != 191:
        fail(f"G1: {len(notes)} notes != 191")
    man_anchor_sum = sum(int(p.get("spec_point_ids") or 0) for p in man["pages"])
    by_note, census = span_chunks(notes)
    if census["markers"] != 203:
        fail(f"G1: {census['markers']} spec_point markers != 203")
    if man_anchor_sum != 203:
        fail(f"G1: manifest spec_point_ids sum {man_anchor_sum} != 203")
    for n in notes:
        ids = [b["id"] for b in n["note"]["blocks"] if b["type"] == "spec_point"]
        mcount = int(n["manifest"].get("spec_point_ids") or 0)
        if len(ids) != mcount:
            fail(f"G1 {n['rel']}: manifest says {mcount} anchors, note carries {len(ids)}")

    # ---- G2 join shape ---------------------------------------------------------
    jrows = join.get("joins") or []
    urows = join.get("unresolved") or []
    unresolved_ids = {u["anchor_id"] for u in urows}
    if len(jrows) != 200 or len(urows) != 3:
        fail(f"G2: join {len(jrows)}+{len(urows)} != 200+3")
    jby_anchor = {row["anchor_id"]: row for row in jrows}
    if len(jby_anchor) != 200:
        fail("G2: duplicate anchor_id in the join artifact")
    if unresolved_ids != {"spcpt_QWXhzVp2S3VYZdZc"} | R1_CLEARED:
        fail(f"G2: unresolved id set drift: {sorted(unresolved_ids)}")
    block_anchors = {c["anchor_id"] for cs in by_note.values() for c in cs}
    if block_anchors != set(jby_anchor) | unresolved_ids:
        fail("G2: note-block anchors != join anchors + THE three unresolved")
    for row in jrows:
        if row["note_path"] not in by_note:
            fail(f"G2: join note_path not in corpus: {row['note_path']}")

    # ---- G3 code validity -------------------------------------------------------
    foreign = sorted({row["store_row_code"] for row in jrows} - set(registry))
    if foreign:
        fail(f"G3: joined codes outside the ratified registry: {foreign}")

    # ---- emit rows ---------------------------------------------------------------
    rows: list[dict] = []
    n_anchored = 0
    n_unres_chunks = 0
    for path in sorted(by_note):
        for c in by_note[path]:
            if c["is_intro"] or not c["text"]:
                continue  # intro chunks are never anchor targets (C13 discipline)
            aid = c["anchor_id"]
            if aid in unresolved_ids:
                n_unres_chunks += 1
                if aid in R1_CLEARED:
                    reason = (
                        f"span anchor {aid} ('{c['span_name']}') was cleared "
                        "UNRESOLVED by the C42 R1 operator verdict round — no "
                        "canonical 188 row teaches this note's content, the wrong "
                        "T-SPEC-7-era code was removed, never forced")
                    disp = ("WORKLIST — chunk-level mapping waits on fresh notes "
                            "coverage or a new operator anchor; recorded, not "
                            "forced (C42 R1 surface 1)")
                else:
                    reason = (
                        f"span anchor {aid} ('{c['span_name']}') is the T-C32 join's "
                        "residual unresolved anchor — operator adjudication pending "
                        "(PROPOSAL-ONLY; never fabricated)")
                    disp = ("WORKLIST — chunk-level mapping waits on the "
                            "anchor's operator adjudication (C32 §3 residual)")
                rows.append({
                    "mapping_id": sha16(f"unresolved|{path}|{c['ordinal']}"),
                    "spec_code": None,
                    "note_slug": Path(path).stem,
                    "note_path": path,
                    "chunk": {"ordinal": c["ordinal"], "heading": c["heading"],
                              "sha256_16": sha16(c["text"]), "chars": len(c["text"]),
                              "convention": CONVENTION_ID},
                    "evidence_quote": self_quote(c["text"]),
                    "worklist_reason": reason,
                    "provenance": {"tier": "RULE_DERIVED", "tool": f"{TOOL}@{TOOL_VERSION}",
                                   "upstream": {"store": "T-C32 K2-A notes-join",
                                                "anchor_id": aid,
                                                "validation_tier": UPSTREAM_TIER}},
                    "validation_status": "SUGGESTED",
                    "disposition": disp,
                })
                continue
            row_code = jby_anchor[aid]["store_row_code"]
            n_anchored += 1
            j = jby_anchor[aid]
            rows.append({
                "mapping_id": sha16(f"{path}|{row_code}|{norm(self_quote(c['text']))}"),
                "spec_code": row_code,
                "sp_title": registry[row_code].get("official_wording") or "",
                "note_slug": Path(path).stem,
                "note_path": path,
                "chunk": {"ordinal": c["ordinal"], "heading": c["heading"],
                          "sha256_16": sha16(c["text"]), "chars": len(c["text"]),
                          "convention": CONVENTION_ID},
                "anchor": {"match_type": "span-marker", "ambiguous_hits": 0},
                "evidence_quote": self_quote(c["text"]),
                "provenance": {
                    "tier": "RULE_DERIVED",
                    "derivation": (
                        "span-marker chunk mapping of the T-C32 K2-A notes-join: the "
                        "corpus's own spec_point block scopes the SME span, the join "
                        "resolves it to the ratified code, and the chunk (deterministic "
                        "c40-chunk-convention-1) sits inside that span; evidence quote "
                        "is the chunk's own verbatim self-slice; zero-LLM"),
                    "tool": f"{TOOL}@{TOOL_VERSION}",
                    "upstream": {
                        "store": "T-C32 K2-A notes-join (AI_VALIDATED operator-delegated chain)",
                        "join_row": f"{path}::{aid}",
                        "anchor_id": aid,
                        "sme_name": j.get("sme_name"),
                        "official_id": j.get("official_id"),
                        "join_tier": j.get("tier"),
                        "join_method": j.get("method"),
                        "join_score": j.get("score"),
                        "wording_check": j.get("wording_check"),
                        "validation_tier": UPSTREAM_TIER,
                    },
                },
                "rationale": (
                    f"SME span '{c['span_name']}' on note '{c['note_title']}' is "
                    f"anchored by the corpus spec_point block {aid} and joined to "
                    f"{row_code} via {j.get('method')}; this section chunk sits "
                    "inside that span."),
                "validation_status": "SUGGESTED",
            })

    # ---- T-C42 R3: operator section-override map, consumed FAIL-CLOSED ---------
    # surface 3 of the C42 R1 verdict round (16 section-level rows: 12
    # REATTRIBUTE + 4 RETAIN). Contract (scripts/c42_section_overrides.yaml):
    # an override naming a code outside the ratified 188 fails the build; every
    # entry must hit exactly one emitted chunk row; the entry's current_code
    # must equal the join-derived code (the map was authored against the
    # post-R1 projection — drift is a defect, not a judgement call).
    ov_bytes = r.read_bytes(OVERRIDES)
    ov_doc = yaml.safe_load(ov_bytes.decode("utf-8"))
    ov_sha = sha16(ov_bytes)
    ov_entries = ov_doc.get("overrides") or []
    if not ov_entries:
        fail("R3: empty section-override map")
    ov_seen = set()
    n_ov_reattr, n_ov_retain = 0, 0
    keyed = {(rw.get("note_slug"),
              (rw.get("chunk") or {}).get("ordinal")): rw
             for rw in rows if "chunk" in rw}
    for e in ov_entries:
        k = (e.get("note_slug"), e.get("chunk_ordinal"))
        action = (e.get("action") or "").upper()
        if k in ov_seen:
            fail(f"R3: duplicate override entry {k}")
        ov_seen.add(k)
        rw = keyed.get(k)
        if rw is None:
            fail(f"R3: override {k} hits no emitted chunk row")
        if action not in ("REATTRIBUTE", "RETAIN"):
            fail(f"R3: override {k} unknown action {action!r}")
        cur = e.get("current_code")
        if cur != rw.get("spec_code"):
            fail(f"R3: override {k} current_code {cur!r} != join-derived "
                 f"{rw.get('spec_code')!r}")
        block = {"source": f"{OVERRIDES}@{ov_sha}",
                 "operator_round": "T-C42 R1 (surface 3, section-level)",
                 "action": action,
                 "evidence": e.get("evidence") or ""}
        if action == "REATTRIBUTE":
            oc = e.get("override_code")
            if not oc or oc not in registry:
                fail(f"R3: override {k} target {oc!r} outside the ratified 188")
            if oc == cur:
                fail(f"R3: override {k} REATTRIBUTE to the same code")
            rw["spec_code"] = oc
            rw["sp_title"] = registry[oc].get("official_wording") or ""
            rw["mapping_id"] = sha16(
                f"{rw['note_path']}|{oc}|{norm(rw['evidence_quote'])}")
            rw["provenance"]["override"] = block
            rw["rationale"] = (
                rw.get("rationale") or "") + \
                " Section-level REATTRIBUTE applied per the C42 R1 operator " \
                "verdict round (provenance.override) — the span-level join is " \
                "coarse for this section; the operator re-attributed the chunk."
            n_ov_reattr += 1
        else:  # RETAIN — no code change; recorded so the R4 re-fill sees the ruling
            if e.get("override_code") is not None:
                fail(f"R3: override {k} RETAIN carries override_code")
            rw["provenance"]["override"] = block
            n_ov_retain += 1
    if len(ov_entries) != 16 or n_ov_reattr != 12 or n_ov_retain != 4:
        fail(f"R3: override census {len(ov_entries)}/{n_ov_reattr}/{n_ov_retain} "
             f"!= 16/12/4")

    # worklist: uncovered SPs (registry minus notes-covered codes)
    covered = sorted({x["spec_code"] for x in rows if x.get("spec_code")})
    unmapped_sps = sorted(set(registry) - set(covered))
    for code in unmapped_sps:
        rows.append({
            "mapping_id": sha16(f"unmapped|{code}"),
            "spec_code": code,
            "sp_title": registry[code].get("official_wording") or "",
            "worklist_reason": ("no notes-corpus anchor resolves to this SP in the "
                                "T-C32 join (coverage bounded by the refreshed "
                                "join's code census; the C40-era 111-code bound "
                                "stays on its own record)"),
            "provenance": {"tier": "RULE_DERIVED", "tool": f"{TOOL}@{TOOL_VERSION}"},
            "validation_status": "SUGGESTED",
            "disposition": "WORKLIST — chunk-level mapping needs notes coverage or "
                           "an operator-authored anchor; recorded, not forced (C31 §6)",
        })

    # fail-closed uniqueness of mapping ids
    ids = [x["mapping_id"] for x in rows]
    if len(ids) != len(set(ids)):
        fail("duplicate mapping_id emitted (note|code|quote collision)")

    # ---- G4 anchor fidelity — re-chunk fresh and re-verify every row -------------
    by_note2, _ = span_chunks(load_corpus(R())[1])
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note2[n["manifest"]["path"]]}
    for rw in rows:
        if "chunk" not in rw:
            continue
        key = (rw["note_path"], rw["chunk"]["ordinal"])
        if key not in idx:
            fail(f"G4: unknown chunk ref {key}")
        if sha16(idx[key]) != rw["chunk"]["sha256_16"]:
            fail(f"G4: chunk hash mismatch {key}")
        if norm(rw["evidence_quote"]) not in norm(idx[key]):
            fail(f"G4: quote not in chunk {key}")

    # ---- G5 anti-forgery ----------------------------------------------------------
    for i, rw in enumerate(rows):
        if rw.get("validation_status") == "HUMAN_VALIDATED" or \
                rw.get("provenance", {}).get("tier") == "HUMAN_VALIDATED":
            fail(f"G5: row {i} ({rw.get('mapping_id')}) claims human authority")
        up = rw.get("provenance", {}).get("upstream") or {}
        if up and up.get("validation_tier") != UPSTREAM_TIER:
            fail(f"G5: row {i} upstream tier drift")

    # ---- G6 worklist completeness ---------------------------------------------------
    anchored_codes = {x["spec_code"] for x in rows if x.get("spec_code") and "chunk" in x}
    for code in set(registry) - anchored_codes:
        if not any(x.get("spec_code") == code and x.get("worklist_reason") for x in rows):
            fail(f"G6: uncovered SP {code} missing from the worklist")
    for rw in rows:
        if "worklist_reason" in rw and not rw.get("disposition"):
            fail(f"G6: worklist row {rw.get('mapping_id')} has no disposition")

    # deterministic ordering: per note by chunk ordinal; unmapped SPs last
    rows.sort(key=lambda rw: (rw.get("note_path") or "zzz",
                              rw["chunk"]["ordinal"] if "chunk" in rw else -1,
                              rw["spec_code"] or ""))
    n_unmapped = len(unmapped_sps)

    return {
        "meta": {
            "store": "c40 maths-a chunk→SpecificationPoint mapping substrate "
                     "(span-marker construction over the SME JSON notes corpus)",
            "stage": "T-C42 R3: substrate re-build over the C42-R1-amended "
                     "resolution via the R2-refreshed T-C32 join — chunk identity "
                     "invariant, only code attribution moves; the operator "
                     "section-override map consumed fail-closed; coverage + the "
                     "uncovered-SP worklist recomputed (the C40-era 111-code "
                     "bound stays on its own record as a measurement under the "
                     "defective mapping)",
            "convention": CONVENTION_ID,
            "convention_spec": (
                "a note = SP spans split at the corpus's own `spec_point` blocks; "
                "within a span, leaf sections cut at heading blocks level 2..4; chunk "
                "text = its own heading + rendered content blocks (the C10 "
                "heading-quote lesson); a span preamble before its first heading is an "
                "intro chunk and is never an anchor target; ordinals are per note; "
                "evidence quote = the chunk's own verbatim self-slice (<=240 chars, "
                "whitespace-cut); anchoring axis = span marker + T-C32 id-join "
                "(chemistry's c13-chunk-convention-1 quote-anchor analog, adapted to "
                "the JSON block corpus — no quotes exist upstream to anchor)"),
            "curriculum": "4MA1-2016",
            "registry_size": len(registry),
            "notes": len(notes),
            "spans": census["markers"],
            "chunks_total": census["intro_chunks"] + census["section_chunks"],
            "chunks_intro": census["intro_chunks"],
            "chunks_section": census["section_chunks"],
            "joins_resolved": len(jrows),
            "joins_unresolved": len(urows),
            "rows_anchored": n_anchored,
            "rows_worklist_anchor_unresolved": n_unres_chunks,
            "rows_worklist_unmapped_sps": n_unmapped,
            "sp_codes_covered": len(covered),
            "sp_codes_uncovered": unmapped_sps,
            "tool": f"{TOOL}@{TOOL_VERSION}",
            "notes_corpus": CORPUS,
            "notes_manifest_sha256_16": _manifest_pin,
            "join_artifact": JOIN,
            "r3_section_overrides": {
                "path": OVERRIDES, "sha256_16": ov_sha,
                "entries": len(ov_entries),
                "reattribute": n_ov_reattr, "retain": n_ov_retain,
                "consumption": "fail-closed: exact (note_slug, chunk_ordinal) hit, "
                               "current_code == join-derived code, targets within "
                               "the ratified 188; applied rows carry provenance.override",
            },
            "upstream_store": f"T-C32 K2-A notes-join ({len(jrows)} joins / "
                              f"{len(urows)} unresolved; AI_VALIDATED "
                              "operator-delegated chain — recorded honestly per "
                              "C31 §4.5; C42 R1-amended resolution, refreshed at R2)",
            "upstream_validation_tier": UPSTREAM_TIER,
            "promotion_rule": "rows are SUGGESTED; HUMAN_VALIDATED only via the "
                              "operator review-sheet gate "
                              "(graph/reports/C40_MATHS_A_CHUNK_SP_SUBSTRATE_REVIEW_SHEET.md) "
                              "in a recorded deterministic apply step",
            "forward_contract": "chunk identity (note_path, ordinal, heading, "
                                "sha256_16 of chunk text) must survive T-C06 "
                                "ingestion — the converter/ChunkingService must "
                                "reproduce this convention or the rows fail closed "
                                "at join time",
        },
        "rows": rows,
    }


def run():
    # ---- G7 idempotency: two INDEPENDENT constructions, byte-identical rows ----
    doc = construct()
    rows_a = yaml.safe_dump(doc["rows"], allow_unicode=True, sort_keys=False)
    doc2 = construct()
    rows_b = yaml.safe_dump(doc2["rows"], allow_unicode=True, sort_keys=False)
    if rows_a != rows_b:
        fail("G7: construction is not deterministic (rows differ between runs)")

    out = GP.store("spec_chunk_mappings", QUAL)
    out.parent.mkdir(parents=True, exist_ok=True)
    text = ("# SyllabAI 4MA1 chunk→SP mapping substrate — T-C40 K2 Lane B, "
            "graph-as-code (C31 §6, C13 pattern)\n"
            "# Generated by scripts/c40_maths_a_chunk_sp_substrate.py — DO NOT "
            "hand-edit: re-run the script.\n"
            "# All rows SUGGESTED / RULE_DERIVED; HUMAN_VALIDATED is operator-only "
            "via the C40 review sheet.\n\n" +
            yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100))
    out.write_text(text, encoding="utf-8")

    m = doc["meta"]
    stats = {
        "notes": m["notes"], "spans": m["spans"],
        "chunks_total": m["chunks_total"], "chunks_intro": m["chunks_intro"],
        "chunks_section": m["chunks_section"],
        "rows_anchored": m["rows_anchored"],
        "rows_worklist_unresolved": m["rows_worklist_anchor_unresolved"],
        "rows_worklist_unmapped": m["rows_worklist_unmapped_sps"],
        "rows_total": len(doc["rows"]),
        "covered": m["sp_codes_covered"], "uncovered": len(m["sp_codes_uncovered"]),
        "registry": m["registry_size"],
    }
    return doc, stats


def main():
    doc, stats = run()
    print("C40 MATHS-A CHUNK→SP SUBSTRATE — construction OK (G1–G7 green)")
    for k in ("notes", "spans", "chunks_total", "rows_anchored",
              "rows_worklist_unresolved", "rows_worklist_unmapped", "covered"):
        print(f"  {k}: {stats[k]}")
    print(f"  store: {GP.store('spec_chunk_mappings', QUAL)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
