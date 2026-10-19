"""Sample-run Docling on a few pages with two OCR backends; print quality comparison."""
import sys, time, json

PDF = "/home/z/my-project/data/chemistry_book.pdf"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TesseractCliOcrOptions, RapidOcrOptions
from docling.datamodel.accelerator_options import AcceleratorOptions

PAGES = [12, 13, 40]  # PDF page numbers: ch1 opener, body text w/ equations, body/table


def build_converter(backend: str) -> DocumentConverter:
    opts = PdfPipelineOptions()
    opts.do_ocr = True
    opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
    opts.do_table_structure = True
    if backend == "tesseract":
        opts.ocr_options = TesseractCliOcrOptions(lang=["eng"])
    else:
        opts.ocr_options = RapidOcrOptions(lang=["en"])
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})


def run(backend: str):
    conv = build_converter(backend)
    t0 = time.time()
    parts = []
    for rng in [(12, 13), (40, 40)]:
        res = conv.convert(PDF, page_range=rng)
        parts.append(res)
    t1 = time.time()
    md = "\n\n".join(r.document.export_to_markdown() for r in parts)
    out_md = f"/home/z/my-project/data/docling_test_{backend}.md"
    with open(out_md, "w") as f:
        f.write(md)
    n_pages = sum(len(r.pages) for r in parts)
    print(f"[{backend}] pages={n_pages} time={t1 - t0:.1f}s  ({(t1 - t0) / max(1, n_pages):.1f}s/page)")
    print(f"[{backend}] markdown chars={len(md)} -> {out_md}")
    return t1 - t0


if __name__ == "__main__":
    backend = sys.argv[1] if len(sys.argv) > 1 else "rapid"
    run(backend)
