#!/usr/bin/env python3
"""T-C05: repair Obsidian Web Clipper template-variable image refs in the
SME 'Chemistry IGCSE Revision Notes' corpus.

Problem: the clipper saved all images into a literal `{pageTitle}/` folder at
the corpus root, while every note references them as `%7BpageTitle%7D/<file>`
(URL-encoded, resolved relative to EACH note's directory -> always broken).

Fix (idempotent, re-runnable after every new clip batch):
  1. move `{pageTitle}/` -> `assets/` (if not already done)
  2. URL-decode percent-encoded filenames inside assets/ (e.g. %E2%80%93 -> dash)
  3. rewrite every image ref to the correct relative path to assets/
     (target names kept decoded; encoded only if they contain spaces/parens)
  4. repair broken clipper syntax `!alt](` -> `![alt](`
  5. if the referenced file is missing, try sibling extensions (.webp -> .png)
  6. else append a CMC `<!-- figure-missing: ... -->` marker (only if not
     already present)

Content (prose, tables, whitespace) is never touched.
Run: python3 c05_repair_clipper_refs.py [--root <notes-dir>]
"""
import os
import re
import sys
import glob
from urllib.parse import unquote, quote

ROOT = sys.argv[sys.argv.index("--root") + 1] if "--root" in sys.argv else \
    "/home/z/my-project/work/syllabai-resources/Chemistry IGCSE Revision Notes"

MARKER_RE = re.compile(
    r"<!-- figure-missing: (?P<fname>.+?) \(download failed during clipping\) -->")

def relpath_prefix(md_path: str) -> str:
    # md paths are relative to ROOT (cwd); note dirs are "S/T", "S/T/U", ...
    d = os.path.dirname(md_path)
    depth = d.count(os.sep) + 1 if d else 0
    return "../" * depth

def md_ref(name: str) -> str:
    """Encode only chars that break markdown link targets."""
    if re.search(r"[ ()]", name):
        return quote(name)
    return name

def main():
    os.chdir(ROOT)

    # 1. rename template folder
    if os.path.isdir("{pageTitle}"):
        if os.path.isdir("assets"):
            sys.exit("both {pageTitle}/ and assets/ exist; merge manually first")
        os.rename("{pageTitle}", "assets")
        print("renamed {pageTitle}/ -> assets/")
    if not os.path.isdir("assets"):
        sys.exit("no assets/ folder found")

    # 2. decode percent-encoded filenames on disk
    present = set(os.listdir("assets"))
    for name in sorted(present):
        if "%" in name:
            dec = unquote(name)
            if dec in present:
                print(f"  kept encoded (decoded exists): {name}")
                continue
            os.rename(os.path.join("assets", name), os.path.join("assets", dec))
            print(f"  decoded filename: {name} -> {dec}")
    files = set(os.listdir("assets"))

    # 3-6. rewrite refs
    PATTERNS = [
        # (regex, is_broken_syntax)
        (re.compile(r"!\[([^\]]*)\]\(%7BpageTitle%7D/([^)]+)\)"), False),
        (re.compile(r"!\[([^\]]*)\]\(\{pageTitle\}/([^)]+)\)"), False),
        (re.compile(r"(?<!\[)!([^\]\s]{1,80})\]\(%7BpageTitle%7D/([^)]+)\)"), True),
        # already-localized refs from a previous run (fix wrong prefixes too)
        (re.compile(r"!\[([^\]]*)\]\((?:\.\./)*assets/([^)]+)\)"), False),
    ]

    stats = {"refs": 0, "syntax": 0, "markers": 0, "ext_rescue": 0, "files": 0}
    for md in glob.glob("**/*.md", recursive=True):
        with open(md, encoding="utf-8", errors="replace") as f:
            text = orig = f.read()
        prefix = relpath_prefix(md)

        def resolve(alt: str, target: str) -> str:
            fname = unquote(target)
            stats["refs"] += 1
            if fname not in files:
                stem, ext = os.path.splitext(fname)
                for alt_ext in (".png", ".jpg", ".jpeg", ".webp", ".svg"):
                    cand = stem + alt_ext
                    if cand in files:
                        fname = cand
                        stats["ext_rescue"] += 1
                        break
            if fname not in files:
                marker = (f"<!-- figure-missing: {fname} "
                          f"(download failed during clipping) -->")
                if marker not in text:
                    stats["markers"] += 1
                    return f"![{alt}]({prefix}assets/{md_ref(fname)}){marker}"
                return f"![{alt}]({prefix}assets/{md_ref(fname)})"
            return f"![{alt}]({prefix}assets/{md_ref(fname)})"

        def sub_factory(is_broken):
            def sub(m):
                if is_broken:
                    stats["syntax"] += 1
                return resolve(m.group(1), m.group(2))
            return sub

        for pat, is_broken in PATTERNS:
            text = pat.sub(sub_factory(is_broken), text)

        if text != orig:
            stats["files"] += 1
            with open(md, "w", encoding="utf-8") as f:
                f.write(text)

    # drop markers whose file appeared after a later step within this same run
    # (safety net; second pass, cheap)
    for md in glob.glob("**/*.md", recursive=True):
        text = open(md, encoding="utf-8", errors="replace").read()
        def strip_stale(m):
            return "" if m.group("fname").strip() in files else m.group(0)
        new = MARKER_RE.sub(strip_stale, text)
        if new != text:
            with open(md, "w", encoding="utf-8") as f:
                f.write(new)

    # report
    refd = set()
    for md in glob.glob("**/*.md", recursive=True):
        for m in re.finditer(
                r"!\[[^\]]*\]\(\s*(?:[^)]*assets/)([^)/]+)\s*\)",
                open(md, encoding="utf-8", errors="replace").read()):
            refd.add(unquote(m.group(1)))
    print(f"md files modified: {stats['files']}/"
          f"{len(glob.glob('**/*.md', recursive=True))}")
    print(f"refs rewritten: {stats['refs']} "
          f"(broken-syntax repaired: {stats['syntax']}, "
          f"extension-rescued: {stats['ext_rescue']})")
    print(f"figure-missing markers: {stats['markers']}")
    print(f"images in assets/: {len(files)}; referenced: {len(refd)}; "
          f"orphans: {len(files - refd)}")

if __name__ == "__main__":
    main()
