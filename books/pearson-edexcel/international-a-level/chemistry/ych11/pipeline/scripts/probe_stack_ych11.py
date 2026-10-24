"""Model-artifact pre-fetch + stack smoke test for the YCH11 lane.

Converts ONE front-matter page ONLINE (models download into
DOCLING_ARTIFACTS_PATH on first use), then re-runs offline to prove the
local cache is complete (L-019 discipline: verify before trusting).
"""
import os, sys, time

os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["OMP_NUM_THREADS"] = "2"
os.environ["MKL_NUM_THREADS"] = "2"
if os.environ.get("PHASE") == "offline":
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"

PDF = "/home/z/my-project/scratch/ych11/ych11_sb1_taleem360.pdf"
PAGE = int(sys.argv[1]) if len(sys.argv) > 1 else 5

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions, AcceleratorOptions

opts = PdfPipelineOptions()
opts.do_ocr = True
opts.ocr_options = RapidOcrOptions(lang=["en"])
opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
opts.do_table_structure = True
opts.do_formula_enrichment = False  # lane decision: 2.33 formula text is empty either way (D-7/L-020); manual rescue owns display equations
if os.environ.get("PHASE") == "offline":
    opts.artifacts_path = "/home/z/my-project/data/models"

conv = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})
t0 = time.time()
res = conv.convert(PDF, page_range=(PAGE, PAGE))
dt = time.time() - t0
texts = []
for item, _lvl in res.document.iterate_items():
    t = getattr(item, "text", "") or ""
    if t.strip():
        texts.append(t.strip()[:90])
print(f"page {PAGE} converted in {dt:.1f}s, {len(texts)} non-empty items")
for t in texts[:12]:
    print("  |", t)
print("OK")
