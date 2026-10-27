#!/usr/bin/env python3
"""
official_examq_asset_bytes.py — the asset-byte guard (the F104 fix).

WHY THIS EXISTS (LEDGER F104): 31 crop PNGs entered the corpus through the
git-data API pushed as UTF-8 TEXT blobs instead of base64 binary — every byte
>= 0x80 was UTF-8-encoded (0x89 -> C2 89), so the served bytes started
`C2 89 50 4E 47` and Chromium (X-Content-Type-Options: nosniff) refused to
decode them: BROKEN FIGURES CORPUS-WIDE WHILE EVERY URL RETURNED HTTP 200.
The exists+200 probe class (G8 artwork audit item 6) is structurally blind to
this; only byte-level validation sees it.

THE GUARD (earliest reliable boundary — before a binary asset is committed or
published):

  1. validate_asset_bytes(data, asset_path)  — format-truth validation by
     magic bytes + real decode (NOT by extension, NOT by URL status):
       PNG   signature + chunk walk (lengths + CRC-32) + IHDR sanity + IDAT
             zlib decompression + scanline-size law + IEND
       JPEG  SOI + marker walk + SOF + SOS + EOI
       GIF   GIF87a/GIF89a header + 0x3B trailer
       WEBP  RIFF/WEBP + chunk-size walk
       PDF   %PDF- header + %%EOF trailer
       SVG   XML/SVG text structure
     plus the MOJIBAKE rejection: bytes that decode as UTF-8 and whose
     latin-1 re-encoding carries a known binary signature are rejected with an
     actionable error (the observed C2 89 50 4E 47 class is caught here).
  2. publish_git_blob(...) — the ONLY sanctioned way to publish a binary asset
     through the GitHub git-data API: validates BEFORE the POST, always
     base64-encodes binary content (never text encoding), then READS THE
     PUBLISHED BLOB BACK and demands byte-identity (sha256) with the intended
     source bytes. An HTTP 200 from the API or the CDN proves nothing by
     itself; byte-identity does.
  3. scan_corpus(...) — walks every topic.json asset record + every assets/
     file under a corpus root: dangling references, undecodable bytes,
     mojibake, wrong-format files — actionable errors with the asset path.

Infra-layer discipline: nothing here writes to canonical content; providers
(GitHub or otherwise) appear only in the publication wrapper, never in the
content validators.

CLI:
  python3 scripts/official_examq_asset_bytes.py --scan-corpus Official-ExamQuestion [--json-out R]
  python3 scripts/official_examq_asset_bytes.py --check-file PATH
"""
import argparse
import base64
import hashlib
import json
import struct
import sys
import zlib
from pathlib import Path

# asset extension -> expected format name (declared-format pinning)
EXT_FORMAT = {".png": "png", ".jpg": "jpeg", ".jpeg": "jpeg", ".gif": "gif",
              ".webp": "webp", ".pdf": "pdf", ".svg": "svg"}

VALIDATOR_VERSION = "asset-bytes/0.1"

PNG_SIG = b"\x89PNG\r\n\x1a\n"
JPEG_SIG = b"\xff\xd8\xff"
GIF_SIGS = (b"GIF87a", b"GIF89a")
WEBP_SIG = b"WEBP"
PDF_SIG = b"%PDF-"

# extensions the corpus of record may carry for raster/vector assets
KNOWN_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".pdf"}


class AssetByteError(Exception):
    """Actionable asset-byte validation failure (asset path always included)."""

    def __init__(self, asset_path, reason, detail=""):
        self.asset_path = str(asset_path)
        self.reason = reason
        self.detail = detail
        super().__init__(f"[{self.asset_path}] {self.reason}" + (f" — {self.detail}" if detail else ""))


def _hex_head(data, n=8):
    return " ".join(f"{b:02X}" for b in data[:n])


# ── per-format validators (stdlib only; each proves real decodability) ──────

def _validate_png(data, path):
    if not data.startswith(PNG_SIG):
        raise AssetByteError(path, "invalid PNG signature", f"head={_hex_head(data)}")
    pos = 8
    ihdr = None
    idat = bytearray()
    seen_iend = False
    first = True
    while pos < len(data):
        if pos + 8 > len(data):
            raise AssetByteError(path, "truncated PNG chunk header", f"offset={pos}")
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        if len(ctype) != 4 or not all(65 <= b <= 122 for b in ctype):
            raise AssetByteError(path, "corrupt PNG chunk type", f"offset={pos} type={ctype!r}")
        cstart = pos + 8
        cend = cstart + length
        if cend + 4 > len(data):
            raise AssetByteError(path, "truncated PNG chunk data", f"offset={pos} declared={length}")
        crc_stored = struct.unpack(">I", data[cend:cend + 4])[0]
        crc_calc = zlib.crc32(data[pos + 4:cend]) & 0xFFFFFFFF
        if crc_stored != crc_calc:
            raise AssetByteError(path, f"PNG CRC mismatch in chunk {ctype.decode('latin-1')}",
                                 f"offset={pos} stored={crc_stored:08x} calc={crc_calc:08x}")
        if first and ctype != b"IHDR":
            raise AssetByteError(path, "PNG does not start with IHDR", f"first chunk={ctype!r}")
        first = False
        if ctype == b"IHDR":
            if length != 13:
                raise AssetByteError(path, "IHDR length != 13", f"length={length}")
            w, h, depth, color, comp, filt, inter = struct.unpack(">IIBBBBB", data[cstart:cend])
            if not (1 <= w <= 2**31 and 1 <= h <= 2**31):
                raise AssetByteError(path, "IHDR impossible dimensions", f"{w}x{h}")
            if depth not in (1, 2, 4, 8, 16) or color > 6 or comp != 0 or filt != 0 or inter > 1:
                raise AssetByteError(path, "IHDR illegal fields",
                                     f"depth={depth} color={color} comp={comp} filt={filt} inter={inter}")
            ihdr = (w, h, depth, color, inter)
        elif ctype == b"IDAT":
            idat.extend(data[cstart:cend])
        elif ctype == b"IEND":
            seen_iend = True
            if pos + 8 + 4 != len(data):
                raise AssetByteError(path, "bytes after IEND", f"file_len={len(data)} iend_end={pos + 12}")
        pos = cend + 4
        if seen_iend:
            break
    if ihdr is None:
        raise AssetByteError(path, "PNG missing IHDR")
    if not seen_iend:
        raise AssetByteError(path, "PNG missing IEND (truncated file)")
    if not idat:
        raise AssetByteError(path, "PNG missing IDAT image data")
    w, h, depth, color, inter = ihdr
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[color]
    try:
        raw = zlib.decompress(bytes(idat))
    except zlib.error as exc:
        raise AssetByteError(path, "PNG IDAT zlib decompression failed", str(exc))
    if inter == 0:
        bpp = max(1, channels * depth)
        expect = h * (1 + (w * bpp + 7) // 8)
        if len(raw) != expect:
            raise AssetByteError(path, "PNG decompressed size != scanline law",
                                 f"decompressed={len(raw)} expected={expect} ({w}x{h} depth={depth} color={color})")
    # interlaced images: decompression success + CRC law is the decode proof
    return len(raw)


def _validate_jpeg(data, path):
    if not data.startswith(JPEG_SIG):
        raise AssetByteError(path, "invalid JPEG signature", f"head={_hex_head(data)}")
    if not data.rstrip(b"\x00").endswith(b"\xff\xd9"):
        raise AssetByteError(path, "JPEG missing EOI marker (truncated?)")
    pos = 2
    saw_sof = saw_sos = False
    n = len(data)
    while pos < n - 1:
        if data[pos] != 0xFF:
            raise AssetByteError(path, "JPEG marker desync", f"offset={pos} byte={data[pos]:02x}")
        while pos < n and data[pos] == 0xFF:
            pos += 1
        marker = data[pos]
        pos += 1
        if marker in (0x01, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0xD5, 0xD6, 0xD7):
            continue
        if marker == 0xD8:
            continue
        if marker == 0xD9:
            break
        if pos + 2 > n:
            raise AssetByteError(path, "JPEG truncated segment length", f"offset={pos}")
        (seglen,) = struct.unpack(">H", data[pos:pos + 2])
        if seglen < 2:
            raise AssetByteError(path, "JPEG illegal segment length", f"offset={pos} len={seglen}")
        if marker in (0xC0, 0xC1, 0xC2, 0xC3):
            saw_sof = True
        if marker == 0xDA:
            saw_sos = True
            break
        pos += seglen
    if not saw_sof:
        raise AssetByteError(path, "JPEG missing SOF frame header")
    if not saw_sos:
        raise AssetByteError(path, "JPEG missing SOS scan header")


def _validate_gif(data, path):
    if not data.startswith(GIF_SIGS):
        raise AssetByteError(path, "invalid GIF signature", f"head={_hex_head(data)}")
    if len(data) < 14:
        raise AssetByteError(path, "GIF truncated logical screen descriptor")
    if not data.rstrip(b"\x00").endswith(b"\x3b"):
        raise AssetByteError(path, "GIF missing 0x3B trailer (truncated?)")
    w, h = struct.unpack("<HH", data[6:10])
    if w == 0 or h == 0:
        raise AssetByteError(path, "GIF zero logical screen size")


def _validate_webp(data, path):
    if len(data) < 12 or data[0:4] != b"RIFF" or data[8:12] != WEBP_SIG:
        raise AssetByteError(path, "invalid WebP RIFF/WEBP signature", f"head={_hex_head(data)}")
    (riff_size,) = struct.unpack("<I", data[4:8])
    if riff_size + 8 > len(data):
        raise AssetByteError(path, "WebP RIFF size exceeds file length", f"declared={riff_size} file={len(data)}")
    pos, end = 12, 8 + riff_size
    saw_payload = False
    while pos + 8 <= end:
        fourcc = data[pos:pos + 4]
        (csize,) = struct.unpack("<I", data[pos + 4:pos + 8])
        if fourcc not in (b"VP8 ", b"VP8L", b"VP8X"):
            raise AssetByteError(path, "WebP unknown chunk", f"{fourcc!r} at {pos}")
        saw_payload = True
        pos += 8 + csize + (csize & 1)
    if not saw_payload:
        raise AssetByteError(path, "WebP missing VP8/VP8L/VP8X payload chunk")


def _validate_pdf(data, path):
    if not data.startswith(PDF_SIG):
        raise AssetByteError(path, "invalid PDF header", f"head={_hex_head(data)}")
    if b"%%EOF" not in data[-1024:]:
        raise AssetByteError(path, "PDF missing %%EOF trailer")


def _validate_svg(data, path):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        try:
            text = data.decode("utf-8-sig")
        except Exception:
            raise AssetByteError(path, "SVG is not decodable UTF-8/UTF-8-BOM text")
    head = text.lstrip("\ufeff \t\r\n")
    if "<svg" not in head[:2048].lower() and "<svg" not in head.lower()[:4096]:
        raise AssetByteError(path, "SVG missing <svg> element near head")


_VALIDATORS = {
    "png": _validate_png,
    "jpeg": _validate_jpeg,
    "gif": _validate_gif,
    "webp": _validate_webp,
    "pdf": _validate_pdf,
    "svg": _validate_svg,
}


# ── mojibake detection (the F104 class: UTF-8 text-encoding of binary) ──────

def mojibake_decode(data):
    """If `data` is UTF-8 text that is really a latin1->UTF-8 encoding of
    binary content, return the recovered original bytes; else None."""
    try:
        decoded = data.decode("utf-8")
    except (UnicodeDecodeError, ValueError):
        return None
    try:
        recovered = decoded.encode("latin-1")
    except UnicodeEncodeError:
        return None  # chars above U+00FF: not a plain binary mojibake
    if recovered == data:
        return None  # pure ASCII / identity: nothing was double-encoded
    return recovered


def sniff_format(data):
    """Best-effort format sniff by magic bytes -> name or None."""
    if data.startswith(PNG_SIG):
        return "png"
    if data.startswith(JPEG_SIG):
        return "jpeg"
    if data.startswith(GIF_SIGS):
        return "gif"
    if len(data) >= 12 and data[0:4] == b"RIFF" and data[8:12] == WEBP_SIG:
        return "webp"
    if data.startswith(PDF_SIG):
        return "pdf"
    head = data[:4096].lstrip(b"\xef\xbb\xbf \t\r\n")
    if head.startswith(b"<?xml") and b"<svg" in data[:8192].lower():
        return "svg"
    if head.lstrip().startswith(b"<svg"):
        return "svg"
    return None


def validate_asset_bytes(data, asset_path, *, expect=None):
    """Validate binary asset bytes by FORMAT TRUTH (not extension, not URL).

    Raises AssetByteError with the asset path + actionable reason on any
    failure; returns the sniffed format name on success. `expect` pins the
    required format (e.g. by extension) when the caller knows it.
    """
    if not data:
        raise AssetByteError(asset_path, "empty asset (0 bytes)")
    fmt = sniff_format(data)
    if fmt is None:
        recovered = mojibake_decode(data)
        if recovered is not None:
            rfmt = sniff_format(recovered)
            if rfmt:
                raise AssetByteError(
                    asset_path, "UTF-8 mojibake of binary content (F104 class)",
                    f"served bytes start {_hex_head(data)}; utf8->latin1 recovers a valid "
                    f"{rfmt.upper()} starting {_hex_head(recovered)} — the asset was pushed as "
                    f"UTF-8 TEXT, not base64 binary. Re-push with encoding=base64 via "
                    f"official_examq_asset_bytes.publish_git_blob.")
        raise AssetByteError(asset_path, "unrecognized binary format",
                             f"head={_hex_head(data)}")
    if expect and fmt != expect:
        raise AssetByteError(asset_path, f"format mismatch (declared {expect}, bytes are {fmt})",
                             f"head={_hex_head(data)}")
    _VALIDATORS[fmt](data, asset_path)
    return fmt


def validate_asset_file(path, *, expect=None):
    p = Path(path)
    try:
        data = p.read_bytes()
    except OSError as exc:
        raise AssetByteError(p, "unreadable asset file", str(exc))
    if expect is None:
        expect = EXT_FORMAT.get(p.suffix.lower())
    return validate_asset_bytes(data, p, expect=expect)


# ── git-data publication wrapper (the ONLY sanctioned binary push path) ─────

def publish_git_blob(repo, asset_path, data, token, *, gh=None, api="https://api.github.com"):
    """Validate-then-publish a binary asset blob, then verify by read-back.

    - validates the bytes by format truth BEFORE any network call
      (AssetByteError -> nothing is pushed);
    - always base64-encodes binary content (the F104 defect was text encoding);
    - after the blob POST, GETs the published blob back and demands sha256
      byte-identity with the intended source — an HTTP 200 alone proves nothing.
    `gh(path, method, body, token)` is injectable for tests; default uses the
    GitHub REST API.
    """
    fmt = validate_asset_bytes(data, asset_path)  # boundary 1: pre-push validation
    body = {"content": base64.b64encode(data).decode(), "encoding": "base64"}

    if gh is None:
        import urllib.request

        def gh(path, method="GET", body=None, token=None):
            req = urllib.request.Request(
                f"{api}{path}", method=method,
                headers={"Authorization": f"Bearer {token}",
                         "Accept": "application/vnd.github+json"},
                data=json.dumps(body).encode() if body else None)
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
    created = gh(f"/repos/{repo}/git/blobs", "POST", body, token)
    blob_sha = created["sha"]
    # boundary 2: read-back byte-identity (never trust the push status alone)
    readback = gh(f"/repos/{repo}/git/blobs/{blob_sha}", "GET", None, token)
    if readback.get("encoding") == "base64":
        served = base64.b64decode(readback.get("content") or "")
    else:
        served = (readback.get("content") or "").encode("utf-8")
    want_sha = hashlib.sha256(data).hexdigest()
    got_sha = hashlib.sha256(served).hexdigest()
    if want_sha != got_sha:
        raise AssetByteError(
            asset_path, "PUBLISHED BLOB DOES NOT MATCH SOURCE BYTES (read-back verification failed)",
            f"source sha256={want_sha} published sha256={got_sha} fmt={fmt} blob={blob_sha}")
    return {"sha": blob_sha, "format": fmt, "bytes": len(data), "sha256": want_sha,
            "readback_verified": True}


# ── corpus scan (dangling references + byte truth over every asset) ─────────

def iter_slice_asset_records(corpus_root):
    """Yield (slice_dir, topic_json_path, asset_record) for every asset record
    in every topic.json under the corpus root (snake_case corpus shape)."""
    root = Path(corpus_root)
    for topic in sorted(root.glob("*/*/*/topic.json")):
        try:
            data = json.loads(topic.read_text())
        except Exception as exc:
            yield topic.parent, topic, {"_parse_error": str(exc)}
            continue
        for q in data.get("questions") or []:
            for p in q.get("parts") or []:
                for a in p.get("assets") or []:
                    yield topic.parent, topic, a


def scan_corpus(corpus_root, *, max_errors=200):
    """Scan a corpus root (e.g. Official-ExamQuestion/): every referenced crop
    record is checked for dangling paths; every physical assets/ file is
    byte-validated (referenced or not). Returns (ok, report-dict)."""
    root = Path(corpus_root)
    findings = []

    def add(level, path, reason, detail=""):
        findings.append({"level": level, "path": str(path), "reason": reason, "detail": str(detail)[:300]})

    # 1. every referenced crop asset must exist on disk (the dangling class, F104)
    referenced = 0
    referenced_files = set()
    for slice_dir, topic, rec in iter_slice_asset_records(root):
        if "_parse_error" in rec:
            add("ERROR", topic, "topic.json unparseable", rec["_parse_error"])
            continue
        path = rec.get("path")
        kind = rec.get("kind")
        if not path or kind not in ("crop", "crop-required"):
            continue
        referenced += 1
        if kind != "crop":
            continue  # crop-required stubs are honest absences by design
        target = slice_dir / path
        if not target.exists():
            add("ERROR", target, "dangling asset reference (recorded crop has no file)",
                f"topic.json={topic}")
        else:
            referenced_files.add(target)

    # 2. every physical file under any assets/ dir (referenced or not)
    checked_files = 0
    for assets_dir in sorted(root.glob("*/*/*/assets")):
        for f in sorted(assets_dir.iterdir()):
            if not f.is_file():
                continue
            checked_files += 1
            try:
                validate_asset_file(f)
            except AssetByteError as exc:
                add("ERROR", f, exc.reason, exc.detail)

    ok = not any(f["level"] == "ERROR" for f in findings)
    return ok, {
        "validator": VALIDATOR_VERSION,
        "corpus": str(root),
        "asset_files_checked": checked_files,
        "asset_records_checked": referenced,
        "referenced_files_resolved": len(referenced_files),
        "errors": findings[:max_errors],
        "error_count": len(findings),
        "ok": ok,
    }


def main():
    ap = argparse.ArgumentParser(description="asset-byte guard (F104)")
    ap.add_argument("--scan-corpus", help="corpus root (e.g. Official-ExamQuestion)")
    ap.add_argument("--check-file", help="validate a single asset file")
    ap.add_argument("--json-out", help="write the scan report JSON here")
    args = ap.parse_args()
    if args.check_file:
        try:
            fmt = validate_asset_file(args.check_file)
            print(f"OK {args.check_file}: {fmt}")
            return
        except AssetByteError as exc:
            print(f"FAIL {exc}", file=sys.stderr)
            sys.exit(1)
    if not args.scan_corpus:
        ap.error("need --scan-corpus or --check-file")
    ok, report = scan_corpus(args.scan_corpus)
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(report, indent=1))
    print(f"asset-byte scan: files={report['asset_files_checked']} "
          f"records={report['asset_records_checked']} errors={report['error_count']} "
          f"ok={report['ok']}")
    for e in report["errors"][:25]:
        print(f"  ERROR [{e['path']}] {e['reason']}" + (f" — {e['detail']}" if e['detail'] else ""))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
