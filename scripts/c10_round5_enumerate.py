#!/usr/bin/env python3
"""T-C10 Round 5 — enumerate the 150 unreviewed mappings and build review dossiers.

READ-ONLY with respect to the authoritative mapping store (decisions JSON +
note front matter). Writes only:
  /home/z/my-project/scripts/round5/round5_targets.json   (enumeration, 150)
  /home/z/my-project/scripts/round5/dossiers/batch_*.md   (review dossiers)

The 150 = all (note, code) pairs in the decisions store MINUS the 59
round-4-surviving ratification targets (C10_RATIFICATION_AUDIT.json
reviewed_pairs) MINUS the 2 round-4 rejected pairs (verified absent — they
were removed from the store in commit bc52c93).

Dossier format per mapping (grouped by note, ordered by subsection then note):
  - spec code + leading verb + official wording (+ practical/command flags)
  - confidence, evidence quote, rationale (from the decisions store)
  - sibling mappings for the same code elsewhere in the corpus
  - the note's heading outline
  - the full markdown section containing the evidence quote (image lines
    compressed to [IMG: ...]), plus the preceding section for premise context
Evidence matching reuses the applier's norm() so the section-finder agrees
with the G3 verbatim gate.
"""

import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT = Path("/home/z/my-project/scripts/round5")
DOSS = OUT / "dossiers"

_TRANS = {ord("‘"): "'", ord("’"): "'", ord("“"): '"', ord("”"): '"',
          ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:  # identical to c10_map_notes.py G3 gate
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


RE_IMG = re.compile(r"!\[([^\]]*)\]\(([^)]*)\)")
RE_CRUFT = re.compile(r"^\s*(Was this revision note helpful\?|---\s*)\s*$")
RE_HEADING = re.compile(r"^(#{1,4})\s+(.*)$")


def compress(body: str) -> str:
    """Strip images/cruft, collapse blanks — keep everything else verbatim."""
    lines = []
    for ln in body.splitlines():
        m = RE_IMG.search(ln)
        if m:
            name = (m.group(2).rsplit("/", 1)[-1] or m.group(1) or "image")
            ln = RE_IMG.sub(f" [IMG: {name}] ", ln)
        if RE_CRUFT.match(ln):
            continue
        lines.append(ln.rstrip())
    out = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return out.strip("\n")


def sections(body: str):
    """Split body into (heading_path, text) chunks at every heading."""
    chunks, cur_title, cur = [], "INTRO", []
    for ln in body.splitlines():
        m = RE_HEADING.match(ln)
        if m:
            if cur:
                chunks.append((cur_title, "\n".join(cur).strip()))
            cur_title, cur = m.group(2).strip(), []
        else:
            cur.append(ln)
    if cur:
        chunks.append((cur_title, "\n".join(cur).strip()))
    return [(t, x) for t, x in chunks if x.strip()]


def load_targets():
    import yaml
    sp = yaml.safe_load((REPO / "graph/specification_points.yaml").read_text(encoding="utf-8"))
    points = {p["code"]: p for p in sp["specification_points"]}

    store = {}  # (note, code) -> mapping dict, in subsection order
    order = []
    for s in ["S1", "S2", "S3", "S4"]:
        d = json.loads((REPO / f"scripts/c10_decisions/{s}.json").read_text(encoding="utf-8"))
        for note, v in d.items():
            for m in v["mappings"]:
                store[(note, m["code"])] = m
                order.append((note, m["code"]))

    audit = json.loads((REPO / "graph/reports/C10_RATIFICATION_AUDIT.json").read_text(encoding="utf-8"))
    reviewed = {(p["note"], p["code"]) for p in audit["reviewed_pairs"]}
    rejected = {(p["note"], p["code"]) for p in audit["rejected_pairs"]}

    # hard identity checks
    assert len(store) == 209, f"store size {len(store)} != 209"
    assert len(reviewed) == 59 and all(p in store for p in reviewed), "reviewed set mismatch"
    still = [p for p in rejected if p in store]
    assert not still, f"rejected pairs still in store: {still}"

    unrev = [(n, c) for (n, c) in order if (n, c) not in reviewed]
    assert len(unrev) == 150, f"unreviewed {len(unrev)} != 150"

    # sibling info: other notes mapping the same code
    from collections import defaultdict
    code2notes = defaultdict(list)
    for (n, c) in order:
        code2notes[c].append(n)

    targets = []
    for i, (note, code) in enumerate(unrev, 1):
        m = store[(note, code)]
        p = points[code]
        siblings = [
            {"note": Path(n).name.replace(".md", ""), "reviewed": (n, code) in reviewed}
            for n in code2notes[code] if n != note
        ]
        targets.append({
            "idx": i,
            "note": note,
            "code": code,
            "confidence": m["confidence"],
            "evidence": m["evidence"],
            "rationale": m["rationale"],
            "leading_verb": p.get("leading_verb", ""),
            "official_wording": p["official_wording"],
            "spec_subsection": p.get("subsection", ""),
            "c_point": p.get("c_point", False),
            "practical": p.get("practical", False),
            "command_words": p.get("command_words", []),
            "siblings": siblings,
        })
    return targets


def build_dossiers(targets):
    DOSS.mkdir(parents=True, exist_ok=True)
    # group by note, preserving global order
    by_note, note_seq = {}, []
    for t in targets:
        if t["note"] not in by_note:
            by_note[t["note"]] = []
            note_seq.append(t["note"])
        by_note[t["note"]].append(t)

    # batches: fixed assignment by corpus subpath (note keys carry the
    # "Chemistry IGCSE Revision Notes/" prefix — strip it before matching)
    def sub_of(note):
        return note.split("/", 1)[1] if "/" in note else note

    BATCHES = [
        ("batch_01_S1a_S1c.md", lambda sub: sub.startswith(("1. Principles of Chemistry/a.", "1. Principles of Chemistry/b.", "1. Principles of Chemistry/c."))),
        ("batch_02_S1d_S1e.md", lambda sub: sub.startswith(("1. Principles of Chemistry/d.", "1. Principles of Chemistry/e."))),
        ("batch_03_S1f_S1i.md", lambda sub: sub.startswith(("1. Principles of Chemistry/f.", "1. Principles of Chemistry/g.", "1. Principles of Chemistry/h.", "1. Principles of Chemistry/i."))),
        ("batch_04_S2a_S2d.md", lambda sub: sub.startswith(("2. Inorganic Chemistry/a.", "2. Inorganic Chemistry/b.", "2. Inorganic Chemistry/c.", "2. Inorganic Chemistry/d."))),
        ("batch_05_S2e_S2h.md", lambda sub: sub.startswith(("2. Inorganic Chemistry/e.", "2. Inorganic Chemistry/f.", "2. Inorganic Chemistry/g.", "2. Inorganic Chemistry/h."))),
        ("batch_06_S3.md", lambda sub: sub.startswith("3. Physical Chemistry/")),
        ("batch_07_S4a_S4d.md", lambda sub: sub.startswith(("4. Organic Chemistry/a.", "4. Organic Chemistry/b.", "4. Organic Chemistry/c.", "4. Organic Chemistry/d."))),
        ("batch_08_S4e_S4h.md", lambda sub: sub.startswith(("4. Organic Chemistry/e.", "4. Organic Chemistry/f.", "4. Organic Chemistry/g.", "4. Organic Chemistry/h."))),
    ]

    tally = {}
    for fname, pred in BATCHES:
        notes = [n for n in note_seq if pred(sub_of(n))]
        nmaps = sum(len(by_note[n]) for n in notes)
        tally[fname] = nmaps
        if not notes:
            continue
        parts = [f"# Round-5 dossier — {fname} ({nmaps} mappings, {len(notes)} notes)\n"]
        for note in notes:
            raw = (REPO / note).read_text(encoding="utf-8")
            m = re.match(r"^---\n.*?\n---\n", raw, flags=re.S)
            body = compress(raw[m.end():] if m else raw)
            secs = sections(body)
            outline = " | ".join(f"{t}" for t, _ in secs)
            stem = Path(note).name
            parts.append(f"\n\n==================== NOTE: {stem}\nSUBDIR: {Path(note).parent.name}\nOUTLINE: {outline}\n")
            norm_secs = [(t, x, norm(x)) for t, x in secs]
            for t in by_note[note]:
                idx = t["idx"]
                sibs = ("; ".join(f"{s['note']}{' (R4-reviewed)' if s['reviewed'] else ''}" for s in t["siblings"])) or "none — this note is the ONLY mapping for this code"
                parts.append(
                    f"\n### R5-{idx:03d} | {t['code']} | conf={t['confidence']} | verb={t['leading_verb']}"
                    f"{' | PRACTICAL' if t['practical'] else ''}{' | C-point' if t['c_point'] else ''}\n"
                    f"SPEC: {t['official_wording']}\n"
                    f"EVIDENCE: \"{t['evidence']}\"\n"
                    f"RATIONALE: \"{t['rationale']}\"\n"
                    f"SIBLINGS for {t['code']}: {sibs}\n")
                # locate the section containing the evidence
                n_ev = norm(t["evidence"])
                hit = None
                for si, (title, txt, ntxt) in enumerate(norm_secs):
                    if n_ev in ntxt:
                        hit = si
                        break
                if hit is None:  # evidence may span sections (heading inside); search whole body
                    parts.append("!! EVIDENCE NOT FOUND IN A SINGLE SECTION — whole-note body follows\n")
                    parts.append(body[:3500] + ("\n...[truncated]" if len(body) > 3500 else ""))
                else:
                    parts.append(f"--- SECTION CONTAINING EVIDENCE [{norm_secs[hit][0]}]:\n")
                    txt = norm_secs[hit][1]
                    parts.append(txt[:3200] + (f"\n...[section truncated, {len(txt)} chars total]" if len(txt) > 3200 else ""))
                    if hit > 0:
                        prev = norm_secs[hit - 1][1]
                        parts.append(f"\n--- PREVIOUS SECTION [{norm_secs[hit-1][0]}] (context):\n" + prev[:700])
        (DOSS / fname).write_text("".join(parts), encoding="utf-8")
    return tally


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    targets = load_targets()
    (OUT / "round5_targets.json").write_text(
        json.dumps(targets, indent=1, ensure_ascii=False), encoding="utf-8")
    tally = build_dossiers(targets)
    print(f"targets: {len(targets)}")
    for k, v in sorted(tally.items()):
        print(f"  {k}: {v} mappings")
    # summary
    from collections import Counter
    print("confidence:", Counter(t["confidence"] for t in targets))
    print("verbs:", Counter(t["leading_verb"] for t in targets).most_common())


if __name__ == "__main__":
    sys.exit(main())
