#!/usr/bin/env python3
"""
PMT notes -> Markdown++ production converter (pilot batch, 28 notes).

Markdown++ spec:
  <docId>/<docId>.md          source of truth: YAML front matter + body
  <docId>/<docId>.index.json  derived sidecar: blocks, images, audit, markers
  <docId>/images/<sha16>.png  durable sha256-addressed region renders
  <docId>/spec/4CH1-X.Y.md    derived per-spec-point splits (graph-validated)

Fidelity policy (mirrors syllabai-parser rules):
  - text layer is primary (all 141 PDFs are born-digital)
  - never silently repair: removals/omissions are explicit + audited
  - zero-width chars stripped (counted); flattened sub/sup formulas flagged
  - tesseract picture-text junk removed (counted)
  - vector structure figures that survive only as OCR garble inside table
    cells are replaced by an explicit omission marker (audited)
  - spec markers validated against graph/specification_points.yaml namespace
"""
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pymupdf
import pymupdf4llm
import yaml

ROOT = Path(__file__).resolve().parents[1]      # repo root (in-repo copy)
SRC_GLOB = "PMT Edexcel IGCSE Chemistry Resources/Unit */Notes/*.pdf"
OUT_DIRNAME = "Notes (Markdown)"
GRAPH = ROOT / "graph" / "specification_points.yaml"

ZERO_CHARS = dict.fromkeys(map(ord, "\u200b\u200c\u200d\ufeff\u00ad"), None)
PMT_FOOTER = re.compile(r"^\s*_?(www\.pmt\.education|pmt\s*education|resources.*courses)_?\s*$", re.I)
PICTURE_TEXT = re.compile(r"<!--\s*Start of picture text\s*-->(.*?)<!--\s*End of picture text\s*-->", re.S)
SPEC_CODE = re.compile(r"(\d{1,2})\.(\d{1,2})([CP]?)(?=[\s(]|$)")
FORMULA_CANDIDATE = re.compile(r"\b[A-Z][a-z]?\d+[A-Za-z(]|\b[A-Z][a-z]?\d+\b")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")

# ---------------------------------------------------------------- graph
def load_graph():
    d = yaml.safe_load(GRAPH.read_text())
    pts = {}
    for p in d["specification_points"]:
        pts[p["official_code"]] = {
            "code": p["code"],
            "wording": p.get("official_wording", ""),
            "subsection": p.get("subsection", ""),
        }
    return pts


# ---------------------------------------------------------------- cleanup
def strip_zero_width(text):
    n = sum(text.count(c) for c in "\u200b\u200c\u200d\ufeff\u00ad")
    return text.translate(ZERO_CHARS), n


def remove_boilerplate(md_text):
    kept, removed = [], 0
    for line in md_text.splitlines():
        if PMT_FOOTER.match(line.replace("\u200b", "")):
            removed += 1
            continue
        kept.append(line)
    return "\n".join(kept), removed


def strip_picture_text(md_text):
    blocks = PICTURE_TEXT.findall(md_text)
    cleaned = PICTURE_TEXT.sub("", md_text)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned, len(blocks)


STRUCTURE_GARBLE = re.compile(r"^(?:[^\w|]{0,3}[\w\d®©='\"“”«»]{1,6}[\s\S]{0,4}){3,}$")

def flag_and_clean_table_figures(md_text):
    """Table cells that are OCR garble of drawn structures -> explicit omission marker."""
    out_lines, flags = [], []
    for ln_no, line in enumerate(md_text.splitlines(), 1):
        if TABLE_ROW.match(line) and line.count("|") >= 4:
            cells = line.split("|")
            hit = False
            for i, c in enumerate(cells):
                frag = c.replace("<br>", " ").strip()
                # structure garble: short fragments, digits/symbols heavy, no real words
                words = re.findall(r"[A-Za-z]{3,}", frag)
                if frag and len(frag) <= 60 and len(words) == 0 and len(re.findall(r"[0-9©®=«»“”|+–-]", frag)) >= 2:
                    cells[i] = " _[structure figure — see source PDF]_ "
                    hit = True
            if hit:
                flags.append({"line": ln_no, "row": " | ".join(x.strip() for x in cells[:3])[:80]})
                line = "|".join(cells)
        out_lines.append(line)
    return "\n".join(out_lines), flags


# ---------------------------------------------------------------- spec markers
def extract_spec_markers(md_text, graph):
    """Find spec-point marker lines: code starts the (decoration-stripped) line."""
    markers, unknown = [], []
    for ln_no, raw in enumerate(md_text.splitlines(), 1):
        bare = re.sub(r"<[^>]+>", " ", raw)          # strip tags FIRST
        bare = re.sub(r"[#*_`>\-\[\]!]", " ", bare)  # then markdown decoration
        bare = bare.strip()
        m = re.match(r"^(\d{1,2}\.\d{1,2})([CP]?)[\s(]", bare)
        if not m:
            continue
        code = m.group(1) + m.group(2)
        if code not in graph and not m.group(2):
            # PMT renders C-points as "N.P (chemistry only)" — graph stores "N.PC"
            if (re.match(r"\s*\(?\s*chemistry\s+only", bare[m.end():], re.I)
                    and (m.group(1) + "C") in graph):
                code = m.group(1) + "C"
        if code not in graph:
            unknown.append({"line": ln_no, "code": code})
            continue
        markers.append({
            "line": ln_no, "officialCode": code, "code": graph[code]["code"],
            "wording": graph[code]["wording"], "subsection": graph[code]["subsection"],
        })
    # dedupe (same marker may repeat), keep order
    seen, out = set(), []
    for mk in markers:
        if mk["officialCode"] in seen:
            continue
        seen.add(mk["officialCode"])
        out.append(mk)
    return out, unknown


# ---------------------------------------------------------------- images
def collect_region_images(pdf_path, tmp_dir):
    """Region renders (raster + vector) via pymupdf4llm write_images, then
    re-key to sha256 names. Returns (md_text, [img_meta])."""
    tmp_dir.mkdir(parents=True, exist_ok=True)
    md_text = pymupdf4llm.to_markdown(
        str(pdf_path), show_progress=False, write_images=True,
        image_path=str(tmp_dir), image_format="png", image_size_limit=0.02)
    doc = pymupdf.open(pdf_path)
    n_pages = len(doc)
    doc.close()
    imgs = []
    for f in sorted(tmp_dir.glob("*.png")):
        raw = f.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        name = f"{sha[:16]}.png"
        imgs.append({"tmp": f, "file": f"images/{name}", "sha256": sha})
    return md_text, imgs, n_pages


def rewrite_image_refs(md_text, imgs, doc_slug):
    """Replace pymupdf4llm tmp refs with sha256 refs + alt text."""
    tmp_by_name = {im["tmp"].name: im for im in imgs}
    def _sub(m):
        ref = m.group(1)
        name = Path(ref).name
        im = tmp_by_name.get(name)
        if not im:
            return m.group(0)
        return f"![{doc_slug} figure]({im['file']})"
    return re.sub(r"!\[\]\(([^)]+)\)", _sub, md_text)


# ---------------------------------------------------------------- anchors
def add_section_anchors(md_text, doc_id):
    n = 0
    def _sub(m):
        nonlocal n
        n += 1
        return f"{m.group(1).rstrip()} {{#{doc_id}-s{n}}}"
    return re.sub(r"^(#{1,6} .*?)\s*$", _sub, md_text, flags=re.M), n


def build_blocks(md_text, doc_id):
    blocks = []
    for i, para in enumerate(p for p in md_text.split("\n\n") if p.strip()):
        t = ("heading" if para.lstrip().startswith("#")
             else "table" if para.lstrip().startswith("|")
             else "image" if "![" in para else "text")
        blocks.append({
            "elementId": f"{doc_id}-b{i:03d}", "type": t,
            "textSha256": hashlib.sha256(para.strip().encode()).hexdigest()[:16],
            "specRefs": sorted(set(m.group(0) for m in SPEC_CODE.finditer(para)
                                   if m.group(0) in _GRAPH_CODES)),
        })
    return blocks


# ---------------------------------------------------------------- splitter
def split_by_spec(md_text, markers, graph, doc_id):
    """Derived per-spec-point files. Deterministic; ambiguous tail stays in parent."""
    lines = md_text.splitlines()
    # marker line numbers (1-based) that start the marker (first occurrence only)
    mk_lines = sorted({mk["line"] for mk in markers})
    if not mk_lines:
        return {}, {"note": "no spec markers found — nothing to split"}
    segs, preamble = {}, "\n".join(lines[:mk_lines[0] - 1]).strip()
    for i, start in enumerate(mk_lines):
        end = mk_lines[i + 1] - 1 if i + 1 < len(mk_lines) else len(lines)
        segs[start] = "\n".join(lines[start - 1:end]).strip()
    # assign segments to markers
    out = {}
    for mk in markers:
        start = next((s for s in segs if s >= mk["line"]), None)
        if start is None:
            continue
        out[mk["officialCode"]] = {"marker": mk, "body": segs[start]}
    tail = ""
    last = mk_lines[-1]
    # tail after last marker's segment belongs to last marker already; nothing extra
    meta = {"preambleChars": len(preamble), "segments": len(segs), "splitFiles": len(out)}
    return out, meta


def write_split_files(splits, out_dir, doc_id, parent_fm):
    written = []
    for code, seg in splits.items():
        mk = seg["marker"]
        fm = {
            "docId": f"{doc_id}-spec-{code.replace('.', '-')}",
            "type": "notes-spec-split",
            "parent": doc_id,
            "parentSourceSha256": parent_fm["sourceSha256"],
            "specRef": mk["code"],
            "specWording": mk["wording"],
            "subsection": mk["subsection"],
            "mapping": {
                "tier": "PROVIDER",
                "signal": "pmt-spec-marker",
                "validation_status": "SUGGESTED",
            },
            "splitter": "pmt_notes_mdpp.py v1",
        }
        # body minus the marker line itself (heading above restates code+wording)
        seg_lines = seg["body"].splitlines()
        if seg_lines:
            first_bare = re.sub(r"<[^>]+>", " ", seg_lines[0])
            if mk["officialCode"].rstrip("CP") in first_bare:
                seg_lines = seg_lines[1:]
        body = (f"# {mk['code']} — {mk['wording']}\n\n"
                + "\n".join(seg_lines).strip() + "\n")
        p = out_dir / "spec" / f"{mk['code']}.md"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True,
                                              width=100) + "---\n\n" + body)
        written.append(mk["code"])
    return written


# ---------------------------------------------------------------- per-doc
def slugify(name):
    s = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)


def convert_one(pdf_path, graph, repo_root):
    unit = pdf_path.parent.parent.name              # "Unit N"
    base = pdf_path.stem                            # "1a) States of matter"
    doc_id = f"pmt-4ch1-notes-{slugify(unit)}-{slugify(base)}"
    out_dir = repo_root / "PMT Edexcel IGCSE Chemistry Resources" / unit / OUT_DIRNAME / doc_id
    tmp_img = Path("/tmp") / "mdpp_tmp" / doc_id

    md_text, imgs, n_pages = collect_region_images(pdf_path, tmp_img)
    audit = []

    zw = 0
    md_text, zw0 = strip_zero_width(md_text)
    zw += zw0
    md_text, boiler = remove_boilerplate(md_text)
    md_text, pic_removed = strip_picture_text(md_text)
    md_text, fig_flags = flag_and_clean_table_figures(md_text)
    md_text = rewrite_image_refs(md_text, imgs, slugify(base))
    md_text, n_anchors = add_section_anchors(md_text, doc_id)
    if zw: audit.append({"kind": "zero-width-chars-removed", "count": zw})
    if boiler: audit.append({"kind": "boilerplate-lines-removed", "count": boiler})
    if pic_removed: audit.append({"kind": "picture-text-blocks-removed", "count": pic_removed})
    if fig_flags: audit.append({"kind": "structure-figure-omitted", "locations": fig_flags})

    markers, unknown = extract_spec_markers(md_text, graph)
    if unknown: audit.append({"kind": "unknown-spec-code", "items": unknown})
    if not markers: audit.append({"kind": "no-spec-markers"})

    # flattened formula candidates (audit only — never rewrite)
    flat = []
    for ln_no, line in enumerate(md_text.splitlines(), 1):
        if TABLE_ROW.match(line) or line.lstrip().startswith("#"):
            continue
        if FORMULA_CANDIDATE.search(line) and "<sub>" not in line:
            flat.append(ln_no)
    if flat:
        audit.append({"kind": "flattened-formula-candidates", "count": len(flat), "lines": flat[:40]})

    sha = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    fm = {
        "docId": doc_id,
        "type": "notes",
        "provider": "PMT",
        "curriculum": "Edexcel IGCSE Chemistry 4CH1",
        "unit": int(unit.split()[-1]),
        "topic": base,
        "sourcePath": str(pdf_path.relative_to(repo_root)),
        "sourceSha256": sha,
        "pages": n_pages,
        "converter": f"pymupdf4llm/{pymupdf4llm.__version__} (text-layer primary)",
        "convertedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "specRefs": [mk["code"] for mk in markers],
        "audit": {"reviewRequired": any(a["kind"] in (
            "unknown-spec-code", "no-spec-markers", "structure-figure-omitted",
            "flattened-formula-candidates") for a in audit),
            "flagKinds": [a["kind"] for a in audit]},
    }

    splits, split_meta = split_by_spec(md_text, markers, graph, doc_id)
    split_written = write_split_files(splits, out_dir, doc_id, fm)
    fm["splits"] = split_written

    # finalize md + sidecar
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "images").mkdir(parents=True, exist_ok=True)
    for im in imgs:
        dst = out_dir / "images" / Path(im["file"]).name
        if not dst.exists():
            im["tmp"].rename(dst)
        im.pop("tmp")
    md_final = ("---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=100)
                + "---\n\n" + md_text.strip() + "\n")
    (out_dir / f"{doc_id}.md").write_text(md_final)

    blocks = build_blocks(md_text, doc_id)
    index = {
        "docId": doc_id, "schema": "syllabai.index/0.1 (canonical §8 thin profile)",
        "source": {"path": fm["sourcePath"], "sha256": sha, "pages": n_pages,
                   "mimeType": "application/pdf"},
        "specMarkers": markers, "splits": split_meta | {"files": split_written},
        "blocks": blocks, "images": imgs, "audit": audit,
        "provenance": {"engine": fm["converter"], "convertedAt": fm["convertedAt"]},
    }
    (out_dir / f"{doc_id}.index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False))

    return {"docId": doc_id, "unit": fm["unit"], "pages": n_pages,
            "specPoints": len(markers), "splits": len(split_written),
            "images": len(imgs), "blocks": len(blocks),
            "review": fm["audit"]["reviewRequired"],
            "flags": fm["audit"]["flagKinds"]}


_GRAPH = yaml.safe_load(GRAPH.read_text())["specification_points"]
_GRAPH_CODES = {p["official_code"] for p in _GRAPH}


def main():
    graph = load_graph()
    pdfs = sorted(ROOT.glob(SRC_GLOB))
    if len(sys.argv) > 1:                     # single-file test: substring filter
        pdfs = [p for p in pdfs if any(a in str(p) for a in sys.argv[1:])]
    print(f"PMT notes pilot batch — {len(pdfs)} PDFs, graph namespace "
          f"{len(_GRAPH_CODES)} spec points\n")
    rows = []
    for p in pdfs:
        try:
            rows.append(convert_one(p, graph, ROOT))
        except Exception as e:
            rows.append({"docId": p.stem, "error": repr(e)})
            print(f"  !! {p.name}: {e!r}")
    print(f"{'docId':<52} pg  spec split img blk rev flags")
    for r in rows:
        if "error" in r:
            print(f"{r['docId']:<52} ERROR {r['error']}")
            continue
        print(f"{r['docId']:<52} {r['pages']:<3} {r['specPoints']:<4} "
              f"{r['splits']:<5} {r['images']:<3} {r['blocks']:<3} "
              f"{'Y' if r['review'] else '-'}   {','.join(r['flags'])}")
    ok = [r for r in rows if "error" not in r]
    print(f"\nconverted: {len(ok)}/{len(pdfs)} | spec points marked: "
          f"{sum(r['specPoints'] for r in ok)} | split files: "
          f"{sum(r['splits'] for r in ok)} | review-required: "
          f"{sum(1 for r in ok if r['review'])}")
    ROOT / "scripts" / "pmt_mdpp_batch.json".write_text(json.dumps(rows, indent=2))


if __name__ == "__main__":
    main()
