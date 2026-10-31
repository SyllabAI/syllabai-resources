#!/usr/bin/env python3
"""Parse Pearson international grade-boundary PDFs -> parsed/<family>/<Session>.json.

WHY POSITIONAL PARSING: pdftotext renders blank (greyed-out) cells as plain
whitespace, so a text-token parser silently SHIFTS columns on tiered rows
(Maths A Foundation prints only grades 5..1; Higher prints 9..3) and on
R-variant rows. The correct join is geometric: every grade label on a
"Max Mark" header line has an x-position, and every value on a boundary row
sits under exactly one label. This parser matches values to their grade
columns by x-distance and never by token order. The MathsGenie golden-master
parity gate (scripts/validate.py) exists precisely to catch any residual
mis-alignment — fail-loud, never silent.

Document grammars (one state machine):
  LINEAR  subject-header ladder lines + rows "<code> <name> Subject <max> <vals>"
          + "Paper(s) 1C 2C" note lines. Tiered subjects carry
          "(Foundation)"/"(Higher)" in the row name; blank cells = None.
  MODULAR/IAL  per-subject sections: AS-unit / A2-unit ladder headers +
          "<code> <title> Raw <max> <vals>" rows with a bare "UMS <max> <vals>"
          twin line, then "Cash-in grade boundaries" + "<code> <title> UMS ..."
          rows. Bare letters-only lines are subject headings.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import pdfplumber

from gb_common import (PARSED, RAW, fail, manifest_lookup, monotonic_ok,
                       norm_ws, now_utc)

CODE_LIKE = re.compile(r"^[4W][A-Z0-9]{1,6}$")
CASHIN_LIKE = re.compile(r"^[XY4W][A-Z0-9]{1,6}$")
HEADING_LIKE = re.compile(r"^[A-Za-z &/'\u2019.-]{3,35}$")
# [1-9]{2} covers the Double Award pair grades (99 98 88 ... 21 11) printed
# on split-ladder cash-in tables; it can only ever appear AFTER "Max Mark"
# on a header line, so extending the label alphabet is safe.
GRADE_LABEL = re.compile(r"^(?:9|[1-8Uu]|a\*|[a-gA-G]|[1-9]{2})$")
# the fixed second segment of the Double Award pair ladder (grades below
# 5-4): 4-4 4-3 3-3 3-2 2-2 2-1 1-1 + U — printed left-to-right in this
# order in every session of the split-ladder cash-in table
PAIR_LADDER_TAIL = ["44", "43", "33", "32", "22", "21", "11", "U"]


def cluster_lines(words: list[dict]) -> list[list[dict]]:
    """pdfplumber words -> visual lines ((page, top) clusters, x-sorted)."""
    words = sorted(words, key=lambda w: (w["page"], w["top"], w["x0"]))
    lines: list[list[dict]] = []
    cur: list[dict] = []
    cur_key = None
    for w in words:
        key = (w["page"], round(w["top"] / 3))
        if cur_key is not None and key != cur_key and abs(w["top"] - cur[-1]["top"]) > 3:
            lines.append(sorted(cur, key=lambda x: x["x0"]))
            cur = []
        cur.append(w)
        cur_key = key
    if cur:
        lines.append(sorted(cur, key=lambda x: x["x0"]))
    return lines


def line_text(line: list[dict]) -> str:
    return norm_ws(" ".join(w["text"] for w in line))


def xc(w: dict) -> float:
    return (w["x0"] + w["x1"]) / 2


def parse_values(line: list[dict], ladder: list[tuple[str, float]],
                 first_value_idx: int) -> dict:
    """Assign each value word after first_value_idx to its nearest grade
    column; unmatched columns -> None (blank/greyed cell)."""
    values = line[first_value_idx:]
    bounds: dict = {g: None for g, _ in ladder}
    for v in values:
        if not re.fullmatch(r"\d{1,4}|[\u2013\u2014\-*.,]", v["text"]):
            continue
        best_g, best_d = None, 1e9
        for g, gx in ladder:
            d = abs(xc(v) - gx)
            if d < best_d:
                best_g, best_d = g, d
        if best_g is not None and best_d <= 16 and bounds[best_g] is None:
            bounds[best_g] = None if not v["text"].isdigit() \
                else int(v["text"])
    return bounds


def ladder_of(line: list[dict]) -> list[tuple[str, float]] | None:
    """'Overall grade boundaries Max Mark 9 8 ... U' -> [(grade, x), ...]"""
    idx = None
    for i, w in enumerate(line):
        if w["text"] == "Mark" and i > 0 and line[i - 1]["text"] == "Max":
            idx = i + 1
            break
    if idx is None:
        return None
    out = []
    for w in line[idx:]:
        if GRADE_LABEL.match(w["text"]):
            out.append((w["text"].upper() if not w["text"].isdigit()
                        else w["text"], xc(w)))
    return out if len(out) >= 4 else None


def parse_doc(pdf: Path, family: str) -> tuple[list[dict], list[str]]:
    subjects: list[dict] = []
    warns: list[str] = []
    ladder: list[tuple[str, float]] | None = None
    ladder_labels: list[str] = []
    section = "units"            # units | cashins (modular/IAL only)
    current: dict | None = None
    # split-ladder stitch state (Double Award 4XSD1: the 17-grade pair
    # ladder is printed as two segments — 99..54 values on a bare line
    # under the header, then the code row carrying the 44..11+U labels,
    # then those values on the next line)
    split_ctx = False            # current cash-in header used a pair ladder
    split_bounds1: dict | None = None
    split_row: dict | None = None
    split_head1: dict | None = None   # shape B: code/title/max stashed from
                                      # the standard-parsed seg1 row

    words: list[dict] = []
    with pdfplumber.open(pdf) as doc:
        for pi, page in enumerate(doc.pages):
            try:
                for w in page.extract_words(keep_blank_chars=False):
                    words.append({**w, "page": pi})
            except Exception as e:                       # noqa: BLE001
                warns.append(f"page {pi + 1}: extract failed ({e})")
    lines = cluster_lines(words)

    # prepass: a TRUE subject heading is a letters-only line whose next
    # non-empty line is a section header ("… grade boundaries  Max Mark …").
    # Wrapped unit-title fragments ("and Gene Technology") fail this test,
    # which is exactly what they were breaking before.
    texts = [line_text(ln) for ln in lines]
    heading_at: set[int] = set()
    for i, t in enumerate(texts):
        if not HEADING_LIKE.match(t) or "grade" in t.lower() \
                or "boundaries" in t.lower():
            continue
        j = i + 1
        while j < len(texts) and not texts[j].strip():
            j += 1
        if j < len(texts) and "grade boundaries" in texts[j] \
                and "Max Mark" in texts[j]:
            heading_at.add(i)

    def flush() -> None:
        nonlocal current
        if current and (current["units"] or current["cashIns"]
                        or current.get("overall")):
            subjects.append(current)
        current = None

    def new_subject(title: str | None) -> None:
        nonlocal current
        flush()
        current = {
            "code": None, "title": title,
            "gradeLadder": None, "papersNote": None,
            "overall": None, "units": [], "cashIns": [],
            "reviewRequired": False,
        }

    for li, line in enumerate(lines):
        text = line_text(line)
        toks = [w["text"] for w in line]

        # ---- ladder header lines ----
        if "Max" in toks and "Mark" in toks:
            cand = ladder_of(line)
            if cand:
                pre = norm_ws(" ".join(toks[:toks.index("Max")])).lower()
                if "cash-in" in pre:
                    section = "cashins"
                elif "unit" in pre:
                    kind = "as" if ("as unit" in pre or pre.endswith("as unit grade boundaries")) else "a2"
                    if kind == "as" and current is not None \
                            and (current["cashIns"] or current["units"]):
                        flush()          # next subject's AS section begins
                    section = "units"
                elif "overall" in pre:
                    section = "overall"
                # else: a subject-name ladder line (linear legacy header) —
                # the section never changes on it
                ladder = cand
                ladder_labels = [g for g, _ in cand]
                split_ctx = (section == "cashins"
                             and any(re.fullmatch(r"[1-9]{2}", g)
                                     for g, _ in cand))
                split_bounds1 = None
                split_row = None
                split_head1 = None
                continue

        labels = ladder_labels

        # ---- LINEAR subject row ----
        if section == "overall" and ladder and len(toks) >= 6 \
                and CODE_LIKE.match(toks[0]) and "Subject" in toks:
            si = toks.index("Subject")
            max_i = si + 1
            try:
                max_mark = int(toks[max_i])
            except (ValueError, IndexError):
                continue
            name = norm_ws(" ".join(toks[1:si]))
            bounds = parse_values(line, ladder, max_i + 1)
            if current is None:
                new_subject(name)
            elif current.get("overall"):
                # a second variant row for the same subject (R papers) or a
                # tier sibling — both become their own subject record joined
                # by code+name at import time
                flush()
                new_subject(name)
            code = toks[0]
            ok = monotonic_ok(bounds, labels)
            current.update({
                "code": code, "title": name, "gradeLadder": labels,
                "overall": {"scale": "raw", "maxMark": max_mark,
                            "boundaries": bounds},
                "tier": ("foundation" if "foundation" in name.lower()
                         else "higher" if "higher" in name.lower() else None),
                "ok": ok,
            })
            current["reviewRequired"] = not ok
            continue

        # ---- papers note (linear) ----
        if toks and toks[0].startswith("Paper(s)") and current is not None \
                and current.get("overall") is not None \
                and current.get("papersNote") is None:
            current["papersNote"] = norm_ws(" ".join(toks[1:])
                                            if len(toks) > 1 else
                                            text.replace("Paper(s)", "").strip())
            continue

        # ---- split-ladder stitch (Double Award 4XSD1) ----
        if section == "cashins" and split_ctx and toks \
                and all(t.isdigit() for t in toks):
            if split_row is None and split_bounds1 is None \
                    and ladder is not None and len(toks) == len(ladder):
                seg1 = parse_values(line, ladder, 0)
                if any(v is not None for v in seg1.values()):
                    split_bounds1 = seg1
                    continue
            if split_row is not None:
                seg2 = parse_values(line, split_row["labels"], 0)
                bounds = {**(split_bounds1 or {}), **seg2}
                ok = monotonic_ok(bounds, [g for g, _ in split_row["labels"]])
                if current is None:
                    new_subject(None)
                current["cashIns"].append({
                    "code": split_row["code"], "title": split_row["title"],
                    "maxMark": split_row["maxMark"], "boundaries": bounds,
                    "ok": ok})
                current["reviewRequired"] = current["reviewRequired"] or not ok
                split_row = None
                continue
            if split_row is None and split_bounds1 is None and split_head1 is not None \
                    and len(toks) == len(PAIR_LADDER_TAIL):
                # June-2025 shape: the second segment's grade labels are not
                # in the text layer at all — only the values line is. The
                # pair-ladder tail is fixed by the qualification structure
                # (4-4, 4-3, 3-3, 3-2, 2-2, 2-1, 1-1, U) and the values are
                # printed left-to-right, so they pair in order (verified
                # equal to the June 2026 session where the labels ARE
                # present and align positionally: 192/168/144/120/96/72/48/0).
                bounds = {**split_head1["bounds"], **dict(zip(
                    PAIR_LADDER_TAIL, (int(t) for t in toks)))}
                ok = monotonic_ok(bounds, PAIR_LADDER_TAIL)
                if current is None:
                    new_subject(None)
                current["cashIns"].append({
                    "code": split_head1["code"],
                    "title": split_head1["title"],
                    "maxMark": split_head1["maxMark"],
                    "boundaries": bounds, "ok": ok})
                current["reviewRequired"] = current["reviewRequired"] or not ok
                split_head1 = None
                continue

        # ---- split-ladder code row (Double Award 4XSD1): the trailing
        # tokens are the second segment's grade labels, and the 'UMS' scale
        # word may or may not cluster onto this line
        if section == "cashins" and split_ctx and split_bounds1 is not None \
                and split_row is None and toks \
                and CASHIN_LIKE.match(toks[0]):
            run = len(toks)
            while run > 0 and GRADE_LABEL.match(toks[run - 1]):
                run -= 1
            if len(toks) - run >= 4 and run > 0 \
                    and toks[run - 1].isdigit():
                label_words = line[-(len(toks) - run):]
                title_toks = [t for t in toks[1:run - 1] if t != "UMS"]
                split_row = {
                    "code": toks[0],
                    "title": norm_ws(" ".join(title_toks)),
                    "maxMark": int(toks[run - 1]),
                    "labels": [(w["text"], xc(w)) for w in label_words],
                }
                continue

        # ---- MODULAR / IAL unit row (glue-aware: pdfplumber can fuse the
        # title with the scale word, e.g. '…Organic ChemistryRaw 80 59 …') ----
        if section == "units" and ladder and toks \
                and CODE_LIKE.match(toks[0]):
            scale_i = scale = None
            glued = None
            for i, t in enumerate(toks[1:], start=1):
                if t in ("Raw", "UMS"):
                    scale_i, scale = i, t.lower()
                    break
                m = re.match(r"^(.+?)(Raw|UMS)$", t)
                if m and len(m.group(1)) >= 3:
                    scale_i, scale, glued = i, m.group(2).lower(), m.group(1)
                    break
            if scale_i is not None:
                # glued max mark first ('…ChemistryRaw80 59 …') — the next
                # token is already a VALUE in that shape, so trying it first
                # would silently eat a boundary as the max mark
                m2 = re.match(r"^(.+?)(?:Raw|UMS)(\d+)$", toks[scale_i])
                if m2 and toks[scale_i] not in ("Raw", "UMS"):
                    max_mark = int(m2.group(2))
                    val_start = scale_i + 1
                else:
                    try:
                        max_mark = int(toks[scale_i + 1])
                        val_start = scale_i + 2
                    except (ValueError, IndexError):
                        continue
                code = toks[0]
                title = norm_ws(" ".join(toks[1:scale_i])
                                + (f" {glued}" if glued else ""))
                bounds = parse_values(line, ladder, val_start)
                if current is None:
                    new_subject(None)
                ok = monotonic_ok(bounds, labels)
                if scale == "raw":
                    current["units"].append({
                        "code": code, "title": title, "maxMark": max_mark,
                        "boundaries": bounds, "ums": None, "ok": ok})
                elif current["units"]:
                    last = current["units"][-1]
                    last["ums"] = {"maxMark": max_mark, "boundaries": bounds}
                    if not ok:
                        last["ok"] = False
                if current["code"] is None:
                    current["code"] = code
                if current["gradeLadder"] is None:
                    current["gradeLadder"] = labels
                current["reviewRequired"] = current["reviewRequired"] or not ok
                continue

        # ---- MODULAR / IAL bare UMS twin ----
        if section == "units" and ladder and toks and toks[0] == "UMS" \
                and current is not None and current["units"] \
                and current["units"][-1]["ums"] is None:
            try:
                max_mark = int(toks[1])
            except (ValueError, IndexError):
                continue
            bounds = parse_values(line, ladder, 2)
            last = current["units"][-1]
            last["ums"] = {"maxMark": max_mark, "boundaries": bounds}
            ok = monotonic_ok(bounds, labels)
            if not ok:
                last["ok"] = False
                current["reviewRequired"] = True
            continue

        # ---- cash-in row (glue-aware, same law as unit rows) ----
        if section == "cashins" and ladder and toks \
                and CASHIN_LIKE.match(toks[0]):
            ums_i = None
            glued = None
            for i, t in enumerate(toks[1:], start=1):
                if t == "UMS":
                    ums_i = i
                    break
                m = re.match(r"^(.+?)(Raw|UMS)$", t)
                if m and len(m.group(1)) >= 3:
                    ums_i, glued = i, m.group(1)
                    break
            if ums_i is None:
                continue
            m2 = re.match(r"^(.+?)(?:Raw|UMS)(\d+)$", toks[ums_i])
            if m2 and toks[ums_i] not in ("Raw", "UMS"):
                max_mark = int(m2.group(2))
                val_start = ums_i + 1
            else:
                try:
                    max_mark = int(toks[ums_i + 1])
                    val_start = ums_i + 2
                except (ValueError, IndexError):
                    continue
            code = toks[0]
            title = norm_ws(" ".join(toks[1:ums_i])
                            + (f" {glued}" if glued else ""))
            bounds = parse_values(line, ladder, val_start)
            if current is None:
                new_subject(None)
            # shape B (June 2025): a pair-ladder code row carries the seg1
            # VALUES — stash instead of appending, the seg2 values line
            # completes it
            if split_ctx and split_row is None and split_bounds1 is None \
                    and split_head1 is None and ladder_labels \
                    and re.fullmatch(r"[1-9]{2}", ladder_labels[0]) \
                    and set(bounds) == set(ladder_labels) \
                    and all(v is not None for v in bounds.values()):
                split_head1 = {"code": code, "title": title,
                               "maxMark": max_mark, "bounds": bounds}
                continue
            ok = monotonic_ok(bounds, labels)
            current["cashIns"].append({
                "code": code, "title": title, "maxMark": max_mark,
                "boundaries": bounds, "ok": ok})
            if current["gradeLadder"] is None:
                current["gradeLadder"] = labels
            current["reviewRequired"] = current["reviewRequired"] or not ok
            continue

        # ---- subject heading (prepass-verified: followed by a section
        # header, so wrapped unit-title fragments can never create one) ----
        if li in heading_at:
            new_subject(text)
    flush()

    # repair: title/code fallbacks from cash-ins
    for s in subjects:
        if s["code"] is None:
            if s["cashIns"]:
                s["code"] = s["cashIns"][-1]["code"]
            elif s["units"]:
                s["code"] = s["units"][0]["code"]
        ycash = next((c for c in reversed(s["cashIns"])
                      if c["code"].startswith("Y")), None)
        if ycash:
            s["code"] = ycash["code"]
            if not s.get("title"):
                s["title"] = ycash["title"]
        if not s.get("title"):
            anyc = s["cashIns"][0] if s["cashIns"] else None
            s["title"] = (anyc["title"] if anyc else s["code"] or "Unknown")
        if not s.get("ok", True):
            s["reviewRequired"] = True
        s.pop("ok", None)
    return subjects, warns


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--families", nargs="*", default=[
        "pearson-int-gcse-linear", "pearson-int-gcse-modular", "pearson-ial"])
    ap.add_argument("--sessions", nargs="*")
    args = ap.parse_args()

    total_files, total_subjects, total_warns = 0, 0, 0
    for fam in args.families:
        raw_dir = RAW / fam
        if not raw_dir.exists():
            continue
        pdfs = sorted(raw_dir.glob("*.pdf"))
        if args.sessions:
            want = set(args.sessions)
            pdfs = [p for p in pdfs if p.stem in want]
        out_dir = PARSED / fam
        out_dir.mkdir(parents=True, exist_ok=True)
        for pdf in pdfs:
            session = pdf.stem
            subjects, warns = parse_doc(pdf, fam)
            meta = manifest_lookup(fam, session) or {}
            doc = {
                "schema": "syllabai.grade-boundaries.source/1",
                "family": fam,
                "session": session,
                "source": {
                    "url": meta.get("url"),
                    "file": meta.get("file", f"raw/{fam}/{session}.pdf"),
                    "sha256": meta.get("sha256"),
                    "bytes": meta.get("bytes"),
                    "fetched_at": meta.get("fetched_at"),
                },
                "subjects": subjects,
                "parse_warnings": warns,
                "parsed_at": now_utc(),
            }
            (out_dir / f"{session}.json").write_text(
                json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
            total_files += 1
            total_subjects += len(subjects)
            total_warns += len(warns)
            print(f"{fam}/{session}: {len(subjects)} subjects, "
                  f"{len(warns)} warnings")
    print(f"PARSED {total_files} docs, {total_subjects} subjects, "
          f"{total_warns} warnings")
    sys.exit(0 if total_files > 0 else 2)


if __name__ == "__main__":
    main()
