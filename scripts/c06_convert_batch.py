#!/usr/bin/env python3
"""T-C06 batch conversion driver (repo-side, environment-parameterized).

Converts a mirrored SME-RevisionNotes tranche (see c06_lint_corpus.py for the
mirror shape) into canonical schema 1.0 JSON using the committed
syllabai-parser SME adapter, then verifies:

  1. double-run byte-identity (pinned --extracted-at),
  2. cross-language documentId conformance (Python re-derivation of the
     CanonicalIdentity formula for EVERY note),
  3. documentId uniqueness,
and emits BUNDLE_MANIFEST.json (per-note source-md sha256, documentId,
canonical sha256, counts) — the integrity spine c06_ingest_notes.py consumes.

Prereqs: JDK 25, Maven; syllabai-parser checked out and `mvn -q package
-DskipTests` run. Jackson jars come from the local ~/.m2.

Usage:
  python3 c06_convert_batch.py <corpus-dir> <out-dir> \
      --parser-classes <syllabai-parser>/target/classes \
      [--extracted-at 2026-09-18T00:00:00Z] [--engine sme-revision-note --version 1.0.0]
"""
import argparse
import glob
import hashlib
import json
import os
import subprocess
import sys
import time
import uuid


def jackson_cp():
    parts = []
    for name in ("jackson-databind", "jackson-core", "jackson-annotations",
                 "jackson-datatype-jsr310"):
        hits = sorted(glob.glob(os.path.expanduser(f"~/.m2/**/{name}-*.jar")),
                      recursive=False)
        hits = sorted(glob.glob(os.path.expanduser(f"~/.m2/**/{name}-*.jar"),
                                recursive=True))
        if not hits:
            sys.exit(f"missing {name} in ~/.m2")
        parts.append(hits[-1])
    return ":".join(parts)


def expected_document_id(md_sha256_hex, engine, version):
    material = f"sha256:{md_sha256_hex}|engine:{engine}|version:{version}"
    h = bytearray(hashlib.sha256(material.encode()).digest()[:16])
    h[6] = (h[6] & 0x0F) | 0x50
    h[8] = (h[8] & 0x3F) | 0x80
    return str(uuid.UUID(bytes=bytes(h)))


def batch(index, out_dir, cp, java, extracted_at):
    os.makedirs(out_dir, exist_ok=True)
    failures = []
    for i, entry in enumerate(index):
        md_path = os.path.join(corpus, entry["md_path"])
        js_path = os.path.join(corpus, entry["path"])
        r = subprocess.run(
            [java, "-cp", cp, "com.syllabai.parser.ParserCli", "SME",
             md_path, out_dir, f"--sidecar={js_path}",
             f"--extracted-at={extracted_at}"],
            capture_output=True, text=True)
        if r.returncode != 0:
            failures.append((entry["path"], r.stderr[-300:]))
        if (i + 1) % 50 == 0:
            print(f"  converted {i + 1}/{len(index)}")
        time.sleep(0)
    return failures


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("corpus")
    ap.add_argument("out")
    ap.add_argument("--parser-classes", required=True)
    ap.add_argument("--extracted-at", default="2026-09-18T00:00:00Z")
    ap.add_argument("--engine", default="sme-revision-note")
    ap.add_argument("--version", default="1.0.0")
    ap.add_argument("--java", default="java")
    args = ap.parse_args()

    global corpus
    corpus = args.corpus
    cp = f"{args.parser_classes}:{jackson_cp()}"
    index = json.load(open(f"{corpus}/mirror_index.json"))["pages"]
    print(f"converting {len(index)} notes (extractedAt pinned {args.extracted_at})")

    for run in (1, 2):
        fails = batch(index, os.path.join(args.out, f"run{run}"), cp, args.java,
                      args.extracted_at)
        if fails:
            print(f"RUN{run} FAILURES:", fails[:5])
            sys.exit(1)

    manifest_entries, mismatches = [], []
    totals = {"textBlocks": 0, "figures": 0, "tables": 0, "sections": 0}
    for entry in index:
        leaf = os.path.basename(entry["md_path"])[:-3]
        name = leaf + ".canonical.json"
        b1 = open(os.path.join(args.out, "run1", name), "rb").read()
        b2 = open(os.path.join(args.out, "run2", name), "rb").read()
        if b1 != b2:
            print(f"BYTE-DRIFT: {name}")
            sys.exit(1)
        doc = json.loads(b1)
        exp = expected_document_id(entry["md_sha256"], args.engine, args.version)
        if doc["documentId"] != exp:
            mismatches.append((entry["path"], doc["documentId"], exp))
        totals["textBlocks"] += len(doc["textBlocks"])
        totals["figures"] += len(doc["figures"])
        totals["tables"] += len(doc["tables"])
        totals["sections"] += len(doc["sections"])
        manifest_entries.append({
            "note_path": entry["md_path"],
            "note_id": entry["rn_id"],
            "title": entry["title"],
            "source_md_sha256": entry["md_sha256"],
            "document_id": doc["documentId"],
            "canonical_sha256": hashlib.sha256(b1).hexdigest(),
            "canonical_bytes": len(b1),
            "text_blocks": len(doc["textBlocks"]),
            "figures": len(doc["figures"]),
            "tables": len(doc["tables"]),
            "sections": len(doc["sections"]),
        })
    if mismatches:
        print("IDENTITY MISMATCHES:", mismatches[:5])
        sys.exit(1)
    ids = [e["document_id"] for e in manifest_entries]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate document_id in batch")

    pinned = ""
    try:
        pinned = subprocess.run(["git", "rev-parse", "HEAD"], cwd=corpus,
                                capture_output=True, text=True).stdout.strip()
    except Exception:
        pass
    manifest = {
        "tool": "syllabai-parser SmeRevisionNoteParser",
        "engine": args.engine,
        "engine_version": args.version,
        "canonical_schema": "1.0",
        "pinned_resources_commit": pinned,
        "extracted_at": args.extracted_at,
        "notes": len(manifest_entries),
        "totals": totals,
        "double_run_byte_identical": True,
        "cross_language_identity_verified": True,
        "entries": sorted(manifest_entries, key=lambda e: e["note_path"]),
    }
    out = os.path.join(args.out, "BUNDLE_MANIFEST.json")
    with open(out, "w") as f:
        json.dump(manifest, f, indent=1)
    print(f"OK: {len(manifest_entries)} canonical docs, byte-identical double-run, "
          f"identity verified for all notes; totals {totals}")
    print(f"manifest: {out}")


if __name__ == "__main__":
    main()
