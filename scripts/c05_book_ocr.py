#!/usr/bin/env python3
"""T-C05: convert the Student Book (1-up, 383 pp, image-only) to CMC-shaped
per-page Markdown using baidu/Unlimited-OCR.

Two backends:
  --backend space  Hugging Face demo Space (baidu/Unlimited-OCR, ZeroGPU A10G).
                  Works from anywhere; anonymous quota is small — use for
                  pilots and small batches (a few pages per sitting).
  --backend vllm   Local vLLM server started from the official image:
                    docker run --rm --gpus all --network host --ipc host \
                      vllm/vllm-openai:unlimited-ocr baidu/Unlimited-OCR \
                      --trust-remote-code \
                      --logits_processors vllm.model_executor.models.unlimited_ocr:NGramPerReqLogitsProcessor \
                      --no-enable-prefix-caching --mm-processor-cache-gb 0
                  Then: python3 c05_book_ocr.py --backend vllm --range 1-383
                  Keeps the RAW output (with <|det|> bboxes) as a sidecar for
                  later figure extraction.

Output (CMC v1.0 aligned):
  <out>/pages/page-NNN.md     per-page markdown + front matter (status: raw_ocr)
  <out>/raw/page-NNN.raw.txt  raw model output incl. grounding tokens (vllm only)
  <out>/manifest.json         checkpoint: page -> {book_page, chapter, status, sha}
  <out>/pages-assets/         page PNGs (200 DPI) — also the figure source

Resumable: pages already in the manifest with status ok are skipped.
Book page = pdf page - OFFSET (9 for our 1-up scan, verified: pdf 87 = book 78).

Usage:
  python3 c05_book_ocr.py --pdf <path> --out <dir> --backend space --range 83-84
  python3 c05_book_ocr.py --pdf <path> --out <dir> --backend vllm --range 1-383 --concurrency 8
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

# ---------------------------------------------------------------- constants
PDF_DEFAULT = ("edexcel-international-gcse-9-1-chemistry-student-book-"
               "pdf-free.pdf")
OFFSET_DEFAULT = 9          # book_page = pdf_page - 9 (verified on this scan)
DPI_DEFAULT = 200
SPACE_ID = "baidu/Unlimited-OCR"

# Chapter map from the book's course-structure page (start book page -> title).
# End ranges inferred from the next start; last chapter ends at the index.
CHAPTERS = [
    ("u1", 1, 3, "States of Matter"),
    ("u1", 2, 14, "Elements, Compounds and Mixtures"),
    ("u1", 3, 24, "Atomic Structure"),
    ("u1", 4, 30, "The Periodic Table"),
    ("u1", 5, 38, "Chemical Formulae, Equations and Calculations Part 1"),
    ("u1", 6, 64, "Chemical Formulae, Equations and Calculations Part 2"),
    ("u1", 7, 75, "Ionic Bonding"),
    ("u1", 8, 85, "Covalent Bonding"),
    ("u1", 9, 98, "Metallic Bonding"),
    ("u1", 10, 101, "Electrolysis"),
    ("u2", 11, 123, "The Alkali Metals"),
    ("u2", 12, 130, "The Halogens"),
    ("u2", 13, 137, "Gases in the Atmosphere"),
    ("u2", 14, 145, "Reactivity Series"),
    ("u2", 15, 160, "Extraction and Uses of Metals"),
    ("u2", 16, 167, "Acids, Alkalis and Titrations"),
    ("u2", 17, 173, "Acids, Bases and Salt Preparations"),
    ("u2", 18, 190, "Chemical Tests"),
    ("u3", 19, 207, "Energetics"),
    ("u3", 20, 227, "Rates of Reaction"),
    ("u3", 21, 240, "Reversible Reactions and Equilibria"),
    ("u4", 22, 255, "Introduction to Organic Chemistry"),
    ("u4", 23, 268, "Crude Oil"),
    ("u4", 24, 277, "Alkanes"),
    ("u4", 25, 282, "Alkenes"),
    ("u4", 26, 287, "Alcohols"),
    ("u4", 27, 291, "Carboxylic Acids"),
    ("u4", 28, 295, "Esters"),
    ("u4", 29, 302, "Synthetic Polymers"),
]
FRONT_MATTER_END = 302  # book pages past the last chapter start = last chapter

def chapter_for(book_page: int):
    if book_page < CHAPTERS[0][2]:
        return ("front", 0, 0, "Front matter")
    cur = CHAPTERS[0]
    for ch in CHAPTERS:
        if book_page >= ch[2]:
            cur = ch
        else:
            break
    return cur

# ---------------------------------------------------------------- helpers
def render_pages(pdf: str, pages_dir: str, wanted: list, dpi: int):
    os.makedirs(pages_dir, exist_ok=True)
    for p in wanted:
        out = os.path.join(pages_dir, f"page-{p:03d}.png")
        if os.path.exists(out):
            continue
        subprocess.run(
            ["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi),
             "-png", "-singlefile", pdf, out[:-4]],
            check=True)
        print(f"  rendered page {p}")
    return {p: os.path.join(pages_dir, f"page-{p:03d}.png") for p in wanted}

def clean_markdown(raw: str) -> str:
    """vllm backend: unwrap <|ref|>, drop <|det|> boxes (space already clean)."""
    raw = re.sub(r"<\|ref\|>(.*?)<\|/ref\|>", r"\1", raw, flags=re.S)
    raw = re.sub(r"<\|det\|>.*?<\|/det\|>", "", raw, flags=re.S)
    raw = re.sub(r"<\|box_start\|>.*?<\|box_end\|>", "", raw, flags=re.S)
    return raw.strip()

def front_matter(pdf_page: int, book_page: int, dpi: int, backend: str) -> str:
    unit, ch_no, _, title = chapter_for(book_page)
    return f"""---
source_type: textbook
book_title: "Edexcel International GCSE (9-1) Chemistry Student Book"
authors: "Jim Clark, Steve Owen, Rachel Yu"
publisher: "Pearson Education Limited"
edition_year: 2017
source_file: {os.path.basename(PDF_DEFAULT)}
pdf_page: {pdf_page}
book_page: {book_page}
unit: {unit}
chapter: {ch_no}
chapter_title: "{title}"
ocr:
  tool: Unlimited-OCR (baidu/Unlimited-OCR)
  mode: document parsing
  dpi: {dpi}
  backend: {backend}
  date: {time.strftime("%Y-%m-%d")}
status: raw_ocr
notes: >
  Not reviewed or validated. Chemistry notation is preserved as inline LaTeX
  (parenthesized) and display blocks; tables as HTML; figures appear as
  image placeholders — actual figure extraction happens at ingest from the
  page PNGs / raw sidecar, not from this file.
---
"""

# ---------------------------------------------------------------- backends
def run_space(png: str) -> tuple:
    from gradio_client import Client, handle_file
    if not hasattr(run_space, "_client"):
        run_space._client = Client(SPACE_ID, verbose=False)
    r = run_space._client.predict(
        image_path=handle_file(png), mode="base",
        prompt="document parsing.", api_name="/run_ocr")
    text = r["text"] if isinstance(r, dict) else str(r)
    return clean_markdown(text), None

def run_vllm(png: str, base_url: str) -> tuple:
    from openai import OpenAI
    if not hasattr(run_vllm, "_client"):
        run_vllm._client = OpenAI(api_key="EMPTY", base_url=base_url,
                                  timeout=3600)
    with open(png, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    resp = run_vllm._client.chat.completions.create(
        model="baidu/Unlimited-OCR",
        messages=[{"role": "user", "content": [
            {"type": "text", "text": "<image>document parsing."},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{b64}"}},
        ]}],
        max_tokens=8192, temperature=0.0,
        extra_body={"skip_special_tokens": False,
                    "vllm_xargs": {"ngram_size": 35, "window_size": 128}},
    )
    raw = resp.choices[0].message.content
    return clean_markdown(raw), raw

# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", default=PDF_DEFAULT)
    ap.add_argument("--out", default="student-book")
    ap.add_argument("--backend", choices=["space", "vllm"], default="space")
    ap.add_argument("--range", dest="page_range", default="1-383",
                    help="pdf page range, e.g. 83-84")
    ap.add_argument("--dpi", type=int, default=DPI_DEFAULT)
    ap.add_argument("--offset", type=int, default=OFFSET_DEFAULT,
                    help="book_page = pdf_page - offset")
    ap.add_argument("--base-url", default="http://localhost:8000/v1",
                    help="vllm server url")
    ap.add_argument("--retries", type=int, default=2)
    ap.add_argument("--concurrency", type=int, default=4,
                    help="parallel workers (vllm backend only)")
    args = ap.parse_args()

    lo, hi = (int(x) for x in args.page_range.split("-"))
    wanted = list(range(lo, hi + 1))

    pages_dir = os.path.join(args.out, "pages-assets")
    raw_dir = os.path.join(args.out, "raw")
    md_dir = os.path.join(args.out, "pages")
    for d in (pages_dir, raw_dir, md_dir):
        os.makedirs(d, exist_ok=True)

    manifest_path = os.path.join(args.out, "manifest.json")
    manifest = {}
    if os.path.exists(manifest_path):
        manifest = json.load(open(manifest_path, encoding="utf-8"))
        print(f"manifest: {sum(1 for v in manifest.values() if v.get('status')=='ok')} "
              f"pages already done — resuming")

    pngs = render_pages(args.pdf, pages_dir, wanted, args.dpi)

    import threading
    lock = threading.Lock()

    def save_manifest():
        with lock:
            json.dump(manifest, open(manifest_path, "w", encoding="utf-8"),
                      indent=1)

    def process_page(p: int):
        key = f"page-{p:03d}"
        if manifest.get(key, {}).get("status") == "ok":
            return
        book_page = p - args.offset
        png = pngs[p]
        for attempt in range(args.retries + 1):
            try:
                t0 = time.time()
                if args.backend == "space":
                    text, raw = run_space(png)
                else:
                    text, raw = run_vllm(png, args.base_url)
                if not text or len(text) < 40:
                    raise RuntimeError(
                        f"suspiciously short output ({len(text)} chars)")
                if raw is not None:
                    with open(os.path.join(raw_dir, f"{key}.raw.txt"),
                              "w", encoding="utf-8") as f:
                        f.write(raw)
                md = (front_matter(p, book_page, args.dpi, args.backend)
                      + "\n" + text + "\n")
                with open(os.path.join(md_dir, f"{key}.md"), "w",
                          encoding="utf-8") as f:
                    f.write(md)
                manifest[key] = {
                    "pdf_page": p, "book_page": book_page,
                    "chapter": chapter_for(book_page)[1],
                    "status": "ok", "chars": len(text),
                    "sha256": hashlib.sha256(text.encode()).hexdigest()[:16],
                    "secs": round(time.time() - t0, 1),
                }
                save_manifest()
                print(f"[{key}] book p.{book_page} ok "
                      f"({len(text)} chars, {time.time()-t0:.0f}s)")
                return
            except Exception as e:
                wait = 10 * (attempt + 1)
                print(f"[{key}] attempt {attempt+1} failed: {e} "
                      f"(retry in {wait}s)", file=sys.stderr)
                time.sleep(wait)
        manifest[key] = {"pdf_page": p, "book_page": book_page,
                         "status": "failed"}
        save_manifest()

    if args.concurrency > 1 and args.backend == "vllm":
        from concurrent.futures import ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=args.concurrency) as pool:
            list(pool.map(process_page, wanted))
    else:
        for p in wanted:
            process_page(p)

    done = sum(1 for v in manifest.values() if v.get("status") == "ok")
    failed = sum(1 for v in manifest.values() if v.get("status") == "failed")
    print(f"\nDONE {done} pages ok, {failed} failed "
          f"(rerun to retry failures — manifest is the checkpoint)")

if __name__ == "__main__":
    main()
