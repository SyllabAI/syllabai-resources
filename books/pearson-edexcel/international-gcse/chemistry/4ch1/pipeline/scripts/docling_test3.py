"""Test do_formula_enrichment with RapidOCR on formula-heavy pages."""
import time, os, resource

PDF = "/home/z/my-project/data/chemistry_book.pdf"

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions
from docling.datamodel.accelerator_options import AcceleratorOptions

opts = PdfPipelineOptions()
opts.do_ocr = True
opts.ocr_options = RapidOcrOptions(lang=["en"])
opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
opts.do_table_structure = True
opts.do_formula_enrichment = True

conv = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})
t0 = time.time()
res = conv.convert(PDF, page_range=(50, 51))
dt = time.time() - t0
md = res.document.export_to_markdown()
open("/home/z/my-project/data/docling_test_rapid_formula.md", "w").write(md)
peak_mb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
print(f"time={dt:.1f}s ({dt / len(res.pages):.1f}s/page)  peakRSS={peak_mb:.0f}MB")
print("formula placeholders remaining:", md.count("formula-not-decoded"))
