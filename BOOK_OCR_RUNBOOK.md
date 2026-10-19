# Student Book OCR Runbook — Unlimited-OCR (baidu/Unlimited-OCR)

Decision record + execution guide for converting the 383-page image-only
Student Book PDF (`edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf`)
to CMC-shaped Markdown. This replaces ocr.z.ai for this book (too large for
the service).

## 1. Pilot verdict — STRONG YES (5 pages, 2026-09-10)

Tested via the official Hugging Face demo Space (ZeroGPU A10G, `base` mode,
200 DPI). Evidence in `student-book-pilot/`:

| Book page | Content stress | Result |
|---|---|---|
| 51 | titration masses table, empirical formula | HTML table perfect, `\( H_2O \)` subscript correct |
| 74 | full display equations + state symbols | `\[ 2 \mathrm{H}_{2}\mathrm{O}_{2} (\mathrm{aq}) \rightarrow ... \]` — states preserved |
| 75 | learning objectives = spec 1.38 ion list | `Cu \( ^{2+} \)`, `\( CO_{3}^{2-} \)`, `\( (NH_{4})_{2}SO_{4} \)` — charge+subscript both correct |
| 76 | key-point boxes, figure captions | structure + reading order clean |
| 78 | dot-and-cross diagrams, lattice text | `Li \( ^{+} \)`, `\(\mathrm{CaCl}_2\)` correct |

**Side-by-side vs ocr.z.ai (same content, the spec conversion):**
- ocr.z.ai: `CO32-` / `Ag+，Cu2+` / CJK punctuation leaks
- Unlimited-OCR: `\( CO_{3}^{2-} \)` / `Cu \( ^{2+} \)`

**Known residual damage (lint-owned, not hand-fixed):**
- state symbol `(l)` sometimes read as `()` or `(1)` — deterministic regex check
- occasional `Aᵣ` → `A,` (subscript r lost) — check against spec symbols
- figure bodies NOT extracted (placeholders `![](images/N.jpg)` in order) —
  extraction happens at ingest from page PNGs / raw `<|det|>` bbox sidecar
- headings/headers/footers inline (book page number, unit banner lines) —
  strip at ingest

## 2. Execution paths

### Path A (RECOMMENDED for the full 383 pages): rented GPU + official vLLM image

Any host with Docker + an NVIDIA GPU ≥ 16 GB (A10G / L4 / A100 / 4090).
Rent by the hour (vast.ai / runpod / lambda); estimated **30–60 min of GPU
time at concurrency 4–8** — a few dollars total.

```bash
# on the rented GPU host
docker run --rm --gpus all --network host --ipc host \
  vllm/vllm-openai:unlimited-ocr \
  baidu/Unlimited-OCR \
  --trust-remote-code \
  --logits_processors vllm.model_executor.models.unlimited_ocr:NGramPerReqLogitsProcessor \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0
# server listens on :8000

# from this repo (CPU side — can be your laptop)
python3 scripts/c05_book_ocr.py \
  --backend vllm --base-url http://<gpu-host>:8000/v1 \
  --range 1-383 --concurrency 8 \
  --pdf edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf \
  --out student-book
```

Interrupted? Re-run the same command — `manifest.json` is the checkpoint,
done pages are skipped, failed pages retried.

### Path B: Hugging Face demo Space (pilots / small batches only)

```bash
python3 scripts/c05_book_ocr.py --backend space --range 83-90 --out student-book
```

**Empirically confirmed limit (2026-09-10):** anonymous ZeroGPU quota ran out
after ~8 single-page calls. With a logged-in HF token it rises somewhat; HF
PRO (~$9/mo) more. Fine for sampling, NOT for 383 pages in one go.

### Path C: your own GPU (≥ 12–16 GB VRAM)

Transformers route per the repo README (bf16). Slowest per-page but free if
you already have the card; `c05_book_ocr.py --backend space` shape can be
re-pointed, or use the repo's own `infer.py`.

## 3. Output shape (CMC v1.0)

```
student-book/
  manifest.json          page -> {book_page, chapter, status, sha256, chars}
  pages/page-NNN.md      CMC front matter (source_type: textbook, pdf/book
                         page, unit, chapter, ocr tool/date, status: raw_ocr)
                         + body (LaTeX notation, HTML tables, figure
                         placeholders)
  raw/page-NNN.raw.txt   vllm only: raw model output WITH <|det|> bboxes —
                         the figure-extraction source
  pages-assets/*.png     200 DPI page renders — figure crop source
```

- `book_page = pdf_page − 9` (verified on this scan; `--offset` to override)
- Chapter map (29 chapters, 4 units) is built into the script and stamped per
  page; chapter-level file assembly happens at ingest (T-C06), so page-map
  corrections never require re-OCR
- Do **not** hand-fix the `(l)`/`A,` damage — the ingestion lint flags it for
  review with page provenance intact

## 4. Ingest implications (registered for T-C06)

1. LaTeX → HTML `<sub>/<sup>` normalization is a deterministic transform
   (KaTeX-style scanner), not AI interpretation — safe for the converter
2. Figure extraction: crop page PNGs by `<|det|>` image bboxes from
   `raw/*.raw.txt`, name `fig-<book-page>-<seq>.png`, replace placeholders
3. The 192-page 2-up PDF is now redundant — keep only as a text-layer
   cross-check
