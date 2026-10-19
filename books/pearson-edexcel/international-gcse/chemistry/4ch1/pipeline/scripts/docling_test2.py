"""Compare RapidOCR vs TesseractCLI backends on formula-heavy pages (PDF 50-51)."""
import time

PDF = "/home/z/my-project/data/chemistry_book.pdf"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TesseractCliOcrOptions, RapidOcrOptions
from docling.datamodel.accelerator_options import AcceleratorOptions

RNG = (50, 51)


def build(backend: str) -> DocumentConverter:
    opts = PdfPipelineOptions()
    opts.do_ocr = True
    opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
    opts.do_table_structure = True
    if backend == "tesseract":
        opts.ocr_options = TesseractCliOcrOptions(lang=["eng"])
    else:
        opts.ocr_options = RapidOcrOptions(lang=["en"])
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})


for backend in ("rapid", "tesseract"):
    conv = build(backend)
    t0 = time.time()
    res = conv.convert(PDF, page_range=RNG)
    dt = time.time() - t0
    md = res.document.export_to_markdown()
    out = f"/home/z/my-project/data/docling_test_{backend}_eq.md"
    open(out, "w").write(md)
    print(f"[{backend}] {dt:.1f}s for {len(res.pages)} pages ({dt / len(res.pages):.1f}s/page), {len(md)} chars -> {out}", flush=True)
