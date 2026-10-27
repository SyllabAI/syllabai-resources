#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-1 — CIE join lane: SME spec-point tags -> official CIE codes.

For each of the 44 cie-* SME course lanes (mapped to their 33 parsed Cambridge
qualifications via Official-Specifications/manifest.json sme_courses), builds
the learner spec-links sidecar `spec-links/<lane>.json` in the EXACT
`syllabai.learner-spec-links/1.0` shape of the Edexcel precedent
(scripts/build_learner_spec_links.py), plus additive CIE blocks.

The Edexcel lane resolved spcpt ids through per-course spec_point_map.json
maps built by earlier operator lanes. No CIE map exists — THIS lane builds
the mapping deterministically and lands it as SUGGESTED (AGENT.md rule 2:
agent-generated mappings remain suggestions until the review/promotion gate
accepts them; rule 3: no coverage manufactured through semantic similarity).

Mechanism (deterministic, zero-LLM):
  1. Universe reconstruction — every CIE note JSON embeds its spec-point
     block(s) (`type: "spec_point"`, id `spcpt_*`, name, definition). The
     lane universe is collected from the lane's notes directly from git
     blobs (cat-file --batch; no worktree materialization, no assets).
  2. Candidate generation — the SME Cambridge path numbering mirrors the
     official syllabus numbering (section "1-...", topic "1-1-...", leaf
     "1-1-1-..."). Candidates = official points whose canonical code equals
     the leaf code (X.Y.Z), else the subsection code (X.Y.*), else the whole
     registry (text-only subjects). Co-ordinated-science lanes filter by
     point scope (Biology/Chemistry/Physics); core/extended maths lanes
     prefer their tier.
  3. Text confirmation (tiers frozen):
       T1_verbatim — a normalized definition line equals a normalized
                     official point text (or containment with >=8 tokens);
       T2_near     — token Jaccard >= 0.55 (path-restricted) or >= 0.75
                     (global), or the unique-single-point subsection head
                     whose title equals the SME spec-point name;
       otherwise   — the anchor stays pending (never invented).
     method: "cie_definition_text_join" (path-restricted) /
             "cie_text_join" (global).

Outputs: spec-links/cie-*.json (44) + spec-links/manifest.json (additive;
Edexcel rows value-identical) + spec-links/README.md CIE section appended.
All sidecars carry review_state SUGGESTED.

Usage: python3 scripts/cie_spec_join.py [--stamp <UTC>] [--lanes a,b,...]
"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
SPEC_LINKS = REPO / "spec-links"
SCHEMA = "syllabai.learner-spec-links/1.0"
MANIFEST_SCHEMA = "syllabai.learner-spec-links-manifest/1.0"
LANE_ID = "T-SPECS-CIE-JOIN-1"

TIERS = ("T1_verbatim", "T2_near")
METHODS = ("cie_definition_text_join", "cie_text_join")
SCIENCES = {"biology": "Biology", "chemistry": "Chemistry", "physics": "Physics"}


def now_utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def norm(s: str) -> str:
    if not s:
        return ""
    s = (s.replace("&", " and ")
           .replace("\u2019", "'").replace("\u2018", "'")
           .replace("\u201c", '"').replace("\u201d", '"')
           .replace("\u2013", "-").replace("\u2014", "-")
           .replace("\xa0", " "))
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return " ".join(s.split())


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def slug_nums(slug: str) -> list:
    m = re.match(r"^(\d+(?:-\d+)*)(?:-.*)?$", slug or "")
    return m.group(1).split("-") if m else []


def canon_code(c) -> str:
    """'C2.1'->'2.1', 'Biology-1.1'->'1.1', '6.3.1'->'6.3.1', 'S2.041'->'2.041'?"""
    c = str(c or "").strip()
    c = re.sub(r"^[A-Za-z]+(?=[0-9])", "", c)   # leading C/E tier letter
    c = re.sub(r"^[A-Za-z]+-", "", c)           # leading 'Biology-' scope
    return c


def code_nums(c) -> list:
    m = re.match(r"^(\d+(?:\.\d+)*)", str(c or ""))
    return m.group(1).split(".") if m else []


# ----------------------------------------------------------------------------
# git blob streaming
# ----------------------------------------------------------------------------

def git(*args, binary=False):
    r = subprocess.run(["git", "-C", str(REPO), *args],
                       capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode("utf-8")


def ls_tree() -> dict:
    """path -> blob sha for the whole tree at HEAD (one call)."""
    out = git("ls-tree", "-r", "HEAD")
    files = {}
    for line in out.splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) >= 3 and parts[1] == "blob":
            files[path] = parts[2]
    return files


def cat_blobs(sha_to_path: dict, chunk: int = 400) -> "dict[str, str]":
    """Read many blobs in chunked cat-file --batch processes (avoids any
    pipe-buffer deadlock on large lanes). Returns path->text."""
    if not sha_to_path:
        return {}
    texts = {}
    shas = list(sha_to_path.keys())
    for i in range(0, len(shas), chunk):
        batch = shas[i:i + chunk]
        r = subprocess.run(
            ["git", "-C", str(REPO), "cat-file", "--batch"],
            input="".join(s + "\n" for s in batch).encode(),
            capture_output=True, check=True)
        buf = r.stdout
        pos = 0
        for s in batch:
            nl = buf.index(b"\n", pos)
            header = buf[pos:nl].decode().strip()
            parts = header.split()
            size = int(parts[2]) if len(parts) >= 3 and parts[2].isdigit() else 0
            body = buf[nl + 1:nl + 1 + size]
            pos = nl + 1 + size + 1  # trailing newline
            texts[sha_to_path[s]] = body.decode("utf-8", "replace")
    return texts


# ----------------------------------------------------------------------------
# lane inputs
# ----------------------------------------------------------------------------

def load_manifest():
    m = json.loads((REPO / "Official-Specifications" / "manifest.json")
                   .read_text(encoding="utf-8"))
    lane_to_qual = {}
    quals = {}
    for q in m["qualifications"]:
        if not str(q.get("slug", "")).startswith("cie-"):
            continue
        quals[q["slug"]] = q
        for lane in q.get("sme_courses") or []:
            if lane in lane_to_qual:
                sys.exit(f"FATAL: lane {lane} maps to two qualifications")
            lane_to_qual[lane] = q["slug"]
    return lane_to_qual, quals


def registry_path(qual: dict) -> Path:
    pdf = Path(qual["pdf"])
    return REPO / "Official-Specifications" / "parsed" / qual["slug"] / \
        (pdf.stem + ".parsed.json")


class Registry:
    def __init__(self, qual: dict):
        d = json.loads(registry_path(qual).read_text(encoding="utf-8"))
        self.raw = d
        self.reg_id = d["id"]
        self.family = d["family"]
        self.points = d["spec_points"]
        self.subsections = d["subsections"]
        self.by_id = {p["id"]: p for p in self.points}
        scopes = {p.get("scope") for p in self.points} - {None}
        self.scoped = bool(scopes)
        for p in self.points:
            p["_canon"] = canon_code(p.get("official_code"))
            p["_nums"] = code_nums(p.get("official_code"))
            pools = [set(norm(p.get("text")).split())]
            sub = " ".join(p.get("sub_items") or [])
            if sub:
                pools.append(set(norm((p.get("text") or "") + " " + sub).split()))
            if pools[1:] == pools[:1]:
                pools = pools[:1]
            p["_tok_pools"] = pools
            # 0580/0607 parser artifact: subsection titles carry a trailing
            # 'Notes and examples' column-header suffix — strip for head match
            t = norm((p.get("subsection") or {}).get("title"))
            t = re.sub(r"\s*(notes|examples|notes and examples)\s*$", "", t)
            p["_ss_tok"] = set(t.split())

    def canon_map(self) -> dict:
        m = {}
        for p in self.points:
            if p["_canon"]:
                m.setdefault(p["_canon"], []).append(p)
        return m

    def build_postings(self) -> None:
        """Exact candidate-prune index: token -> [(point_idx, pool_idx)].
        A point pool can only match a line (any rule) if it shares >= 0.35*|line|
        tokens (the loosest rule floor; all tokens indexed) and has size >=
        that same floor — both enforced, so pruning is lossless. Also an
        exact-equality index pool-tokens -> [(point_idx, pool_idx)] for the
        record-dependent name rule."""
        post = {}
        eq = {}
        psize = {}
        for pi, p in enumerate(self.points):
            for k, pool in enumerate(p.get("_tok_pools") or []):
                psize[(pi, k)] = len(pool)
                fs = frozenset(pool)
                eq.setdefault(fs, []).append((pi, k))
                for tok in pool:
                    post.setdefault(tok, []).append((pi, k))
        self._post = post
        self._psize = psize
        self._eq = eq

    def scan_line(self, lt: set, thr_t2: float) -> dict:
        """Record-independent scan: pi -> {k: (eq, containment, jaccard)}
        for every candidate point. Lossless for all four matching rules."""
        lts = len(lt)
        vote_thr = min(8, math.ceil(0.35 * lts))
        votes = Counter()
        for tok in lt:
            for pk in self._post.get(tok, ()):
                if self._psize[pk] >= vote_thr:
                    votes[pk] += 1
        cand = {}
        for (pi, k), v in votes.items():
            if v < vote_thr:
                continue
            pool = self.points[pi]["_tok_pools"][k]
            inter = len(lt & pool)
            cand.setdefault(pi, {})[k] = (
                inter == lts == len(pool),
                inter >= 8 and (lt <= pool or pool <= lt),
                inter / len(lt | pool) if (lt or pool) else 0.0,
            )
        return cand


# ----------------------------------------------------------------------------
# the join
# ----------------------------------------------------------------------------

def lane_scope(lane: str) -> str:
    for suf, scope in SCIENCES.items():
        if lane.endswith("-" + suf):
            return scope
    return ""


def lane_tier_pref(lane: str) -> str:
    if re.search(r"-(core)(-\d+)?$", lane):
        return "Core"
    if re.search(r"-(extended)(-\d+)?$", lane):
        return "Extended"
    return ""


def candidate_points(rec: dict, reg: Registry, canon_map: dict,
                     scope: str, tier_pref: str, section_nums: list,
                     topic_nums: list, leaf_nums: list):
    """Return (base, restricted) — base = candidate point list,
    restricted = True when path/scope-derived (lower T2 threshold)."""

    def ok(p):
        if scope and reg.scoped and (p.get("scope") or "") != scope:
            return False
        return True

    leaf_code = ".".join(leaf_nums) if len(leaf_nums) >= 3 else ""
    topic_code = ".".join(topic_nums) if len(topic_nums) >= 2 else ""

    if leaf_code and leaf_code in canon_map:
        base = [p for p in canon_map[leaf_code] if ok(p)]
        if base:
            return _tier_filter(base, tier_pref), True
    if topic_code:
        pref = [p for p in reg.points
                if ok(p) and p["_nums"][:len(topic_nums)] == topic_nums]
        if pref:
            return _tier_filter(pref, tier_pref), True
    glob = [p for p in reg.points if ok(p)]
    return _tier_filter(glob, tier_pref), False


def _tier_filter(pts, tier_pref):
    if tier_pref:
        pref = [p for p in pts if p.get("tier") == tier_pref]
        if pref:
            return pref
    return pts


def resolve_spcpt(rec: dict, reg: Registry, canon_map: dict,
                  scope: str, tier_pref: str) -> list:
    """Deterministic text join for one SME spec-point record.
    Returns list of {official_id, official_code, tier, method}."""
    name = rec.get("name") or ""
    definition = rec.get("definition") or ""
    lines = [ln for ln in definition.split("\n") if ln.strip()]
    sec_n = slug_nums(rec.get("_section_slug") or "")
    top_n = slug_nums(rec.get("_topic_slug") or "")
    leaf_n = slug_nums(rec.get("_leaf_slug") or "")

    base, restricted = candidate_points(rec, reg, canon_map, scope,
                                        tier_pref, sec_n, top_n, leaf_n)
    thr_t2 = 0.55 if restricted else 0.75
    method = "cie_definition_text_join" if restricted else "cie_text_join"

    best = {}  # official_id -> (rank, tier_str)
    rank = {"T1_verbatim": 0, "T2_near": 1}

    def offer(p, tier_str):
        cur = best.get(p["id"])
        if cur is None or rank[tier_str] < rank[cur]:
            best[p["id"]] = tier_str

    if not hasattr(reg, "_line_cache"):
        reg._line_cache = {}

    name_tok = set(norm(name).split())

    # unique-single-point subsection-head rule (for definition-less records)
    if not lines:
        subs = {}
        for p in base:
            subs.setdefault((p.get("subsection") or {}).get("official_code"),
                            []).append(p)
        for code, pts in subs.items():
            if len(pts) == 1 and name_tok and \
                    name_tok == (pts[0].get("_ss_tok") or set()):
                offer(pts[0], "T2_near")

    cache = reg._line_cache
    base_ids = {p["id"] for p in base}
    name_pools = set(reg._eq.get(frozenset(name_tok), ())) \
        if name_tok else set()
    for ln in lines:
        lt = set(norm(ln).split())
        if not lt:
            continue
        cand = cache.get((thr_t2, ln))
        if cand is None:
            cand = reg.scan_line(lt, thr_t2)
            cache[(thr_t2, ln)] = cand
        for pi in sorted(cand):
            p = reg.points[pi]
            if p["id"] not in base_ids:
                continue
            verdict = None
            for k in sorted(cand[pi]):
                eq, cont, jac = cand[pi][k]
                if eq or cont:
                    verdict = "T1_verbatim"
                    break
                if jac >= thr_t2:
                    verdict = "T2_near"
                    break
                # name as a weak signal only alongside weak-but-real overlap
                if (pi, k) in name_pools and jac >= 0.35:
                    verdict = "T2_near"
                    break
            if verdict:
                offer(p, verdict)

    out = []
    for pid in sorted(best):
        p = reg.by_id[pid]
        out.append({"official_id": pid,
                    "official_code": str(p.get("official_code")),
                    "tier": best[pid],
                    "method": method})
    return out


# ----------------------------------------------------------------------------
# lane bundle
# ----------------------------------------------------------------------------

def lane_bundle(lane: str, qual: dict, reg: Registry, files: dict,
                stamp: str) -> dict:
    scope = lane_scope(lane)
    tier_pref = lane_tier_pref(lane)
    canon_map = reg.canon_map()
    reg.build_postings()
    if not hasattr(reg, "_line_cache"):
        reg._line_cache = {}

    note_paths = sorted(p for p in files
                        if p.startswith(f"SME-RevisionNotes/{lane}/notes/")
                        and p.endswith(".json"))
    eq_paths = sorted(p for p in files
                      if p.startswith(f"SME-ExamQuestion/{lane}/")
                      and p.endswith("/topic.json"))
    fc_paths = sorted(p for p in files
                      if p.startswith(f"SME-Flashcards/{lane}/")
                      and p.endswith("/deck.json"))

    blobs = cat_blobs({files[p]: p for p in note_paths + eq_paths + fc_paths})

    # ---- universe from the notes' embedded spec-point blocks
    universe = {}   # spcpt_id -> rec (name/definition/path of its note)
    notes_anchored = []
    for p in note_paths:
        try:
            n = json.loads(blobs[p])
        except Exception:
            continue
        spids = n.get("spec_point_ids") or []
        path = n.get("path") or {}
        for b in n.get("blocks") or []:
            if b.get("type") == "spec_point" and b.get("id"):
                rec = universe.setdefault(b["id"], {
                    "name": b.get("name"), "definition": b.get("definition"),
                    "_section_slug": path.get("section"),
                    "_topic_slug": path.get("topic"),
                    "_leaf_slug": path.get("leaf"),
                })
                # prefer the richer record if seen twice
                if (rec.get("definition") or "") == "" and b.get("definition"):
                    rec["definition"] = b["definition"]
                if not rec.get("name") and b.get("name"):
                    rec["name"] = b["name"]
        if spids:
            notes_anchored.append((n, spids, path))

    mappings = {}
    for sid in sorted(universe):
        mappings[sid] = resolve_spcpt(universe[sid], reg, canon_map,
                                      scope, tier_pref)

    def resolve(spids):
        codes, pending = [], []
        for s in spids or []:
            m = mappings.get(s)
            if m:
                codes.extend(m)
            else:
                pending.append(s)
        seen, uniq = set(), []
        for c in sorted(codes, key=lambda c: c["official_id"]):
            if c["official_id"] in seen:
                continue
            seen.add(c["official_id"])
            uniq.append(c)
        return uniq, pending

    items = {}
    stats = Counter()
    anchors = Counter()

    # ---- revision notes (anchored only, per the Edexcel build contract)
    for n, spids, path in notes_anchored:
        codes, pending = resolve(spids)
        anchors["notes"] += len(spids)
        anchors["notes_pending"] += len(pending)
        items[n["note_id"]] = {
            "kind": "note",
            "label": n.get("page_title") or n.get("title"),
            "section": path.get("section"),
            "topic": path.get("topic"),
            "codes": codes,
            "pending": pending,
        }
        stats["notes"] += 1
        stats["notes_coded"] += 1 if codes else 0

    # ---- exam question parts (anchored only)
    for p in eq_paths:
        try:
            t = json.loads(blobs[p])
        except Exception:
            continue
        topic = (t.get("topic") or {}).get("slug")
        sec = t.get("section")
        section = sec.get("slug") if isinstance(sec, dict) else sec
        for q in t.get("questions") or []:
            for part in q.get("parts") or []:
                spids = part.get("spec_point_ids") or []
                if not spids:
                    continue
                codes, pending = resolve(spids)
                anchors["parts"] += len(spids)
                anchors["parts_pending"] += len(pending)
                items[part["id"]] = {
                    "kind": "question_part",
                    "label": f"{(q.get('reference') or q.get('id') or 'question')} / part {part.get('order')}",
                    "section": section,
                    "topic": topic,
                    "codes": codes,
                    "pending": pending,
                }
                stats["question_parts"] += 1
                stats["question_parts_coded"] += 1 if codes else 0

    # ---- flashcards: substrate exists (deck.json spec_links) but every CIE
    # card carries none — honest zeros; discovered count recorded additively.
    fc_cards = 0
    for p in fc_paths:
        try:
            d = json.loads(blobs[p])
        except Exception:
            continue
        fc_cards += int(d.get("card_count") or len(d.get("cards") or []))

    resolved_total = sum(1 for v in mappings.values() if v)
    bundle = {
        "schema": SCHEMA,
        "generated_utc": stamp,
        "course": lane,
        "qual": qual["slug"],
        "board": "cambridge-cie",
        "review_state": {
            "state": "SUGGESTED",
            "lane": LANE_ID,
            "gate": "pending",
            "note": "agent-generated mapping (AGENT.md rule 2); not "
                    "authoritative until the review/promotion gate accepts; "
                    "unresolved anchors stay pending (rule 3)",
        },
        "registry": {
            "id": reg.reg_id,
            "family": reg.family,
            "official_points": len(reg.points),
        },
        "totals": {
            "items": len(items),
            "items_with_codes": sum(1 for v in items.values() if v["codes"]),
            "by_kind": {
                "notes": stats["notes"],
                "question_parts": stats["question_parts"],
                "flashcards": 0,
            },
            "coded_by_kind": {
                "notes": stats["notes_coded"],
                "question_parts": stats["question_parts_coded"],
                "flashcards": 0,
            },
        },
        "anchors": {
            "notes": anchors["notes"],
            "parts": anchors["parts"],
            "universe_ids": len(universe),
            "universe_resolved": resolved_total,
            "pending_refs": anchors["notes_pending"] + anchors["parts_pending"],
            "flashcards_discovered_uncoded": fc_cards,
        },
        "items": items,
    }
    return bundle


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stamp", default=now_utc())
    ap.add_argument("--lanes", default="")
    args = ap.parse_args()

    lane_to_qual, quals = load_manifest()
    lanes = sorted(lane_to_qual)
    if args.lanes:
        want = {x.strip() for x in args.lanes.split(",") if x.strip()}
        lanes = [l for l in lanes if l in want]

    files = ls_tree()
    SPEC_LINKS.mkdir(parents=True, exist_ok=True)

    mpath = SPEC_LINKS / "manifest.json"
    manifest = json.loads(mpath.read_text(encoding="utf-8"))
    pre_courses = json.loads(json.dumps(manifest.get("courses", {})))

    tot = Counter()
    for lane in lanes:
        print(f"  .. {lane}", flush=True)
        qual = quals[lane_to_qual[lane]]
        reg = Registry(qual)
        b = lane_bundle(lane, qual, reg, files, args.stamp)
        (SPEC_LINKS / f"{lane}.json").write_text(
            json.dumps(b, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
        manifest["courses"][lane] = {"qual": b["qual"], **b["totals"]}
        for k in ("items", "items_with_codes"):
            tot[k] += b["totals"][k]
        for k in ("notes", "question_parts", "flashcards"):
            tot[k] += b["totals"]["by_kind"][k]
            tot[k + "_coded"] += b["totals"]["coded_by_kind"][k]
        t = b["totals"]
        print(f"[{lane}] items={t['items']} coded={t['items_with_codes']} "
              f"(notes {t['coded_by_kind']['notes']}/{t['by_kind']['notes']}, "
              f"parts {t['coded_by_kind']['question_parts']}/{t['by_kind']['question_parts']})",
              flush=True)

    manifest["generated_utc"] = args.stamp
    manifest["cie_join"] = {
        "lane": LANE_ID,
        "review_state": "SUGGESTED",
        "lanes": len(lanes),
    }
    mpath.write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8")

    # Edexcel-row stability telemetry (values must be untouched)
    changed = [k for k, v in pre_courses.items()
               if manifest["courses"].get(k) != v]
    print(f"TOTAL items={tot['items']} coded={tot['items_with_codes']} | "
          f"notes {tot['notes_coded']}/{tot['notes']}, "
          f"parts {tot['question_parts_coded']}/{tot['question_parts']} | "
          f"edexcel_rows_changed={len(changed)}")
    if changed:
        print("FATAL: pre-existing manifest rows changed:", changed)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
