#!/usr/bin/env python3
"""Convert an Excel or CSV file into the project's JSON record format.

Records are built dynamically from the input's column headers — every column
in the spreadsheet becomes a field in each record, using the original header
name as the key. No column mapping or filtering is performed.
"""

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from datetime import datetime, date
from pathlib import Path
from typing import Optional, Union

import pandas as pd

# xlsx encodes control characters as literal _xNNNN_ inside string cells.
_XLSX_ESCAPE_RE = re.compile(r"_x([0-9A-Fa-f]{4})_")


# Mojibake markers: short substrings that strongly suggest UTF-8 bytes were
# decoded as cp1252, latin1, or mac_roman somewhere upstream. Examples: "Ã©"
# for é (cp1252 misread); "‚Äú"/"‚Äù" for smart quotes (mac_roman misread);
# "‚Äì"/"‚Äî" for en/em dashes; "‚Ä¶" for ellipsis.
_MOJIBAKE_MARKERS = (
    "Ã", "Â",
    "‚Ä", "‚Äú", "‚Äù", "‚Äì", "‚Äî", "‚Ä¶", "‚Äô", "‚Äò",
    "â€", "â€œ", "â€\x9d", "â€“", "â€”", "â€¦", "â€™", "â€˜",
    "Î", "Å", "Ÿ",
)

# Map common non-ASCII typography to ASCII equivalents ("find matching").
_TRANSLIT = {
    "‘": "'", "’": "'", "‚": "'", "‛": "'",
    "“": '"', "”": '"', "„": '"', "‟": '"',
    "–": "-", "—": "-", "―": "-", "−": "-",
    "…": "...",
    " ": " ", " ": " ", " ": " ", " ": " ",
    "​": "",  "﻿": "",
    "•": "*", "·": "*",
    "≤": "<=", "≥": ">=", "≠": "!=", "≈": "~",
    "×": "x", "÷": "/",
    "±": "+/-", "°": " deg",
    "→": "->", "←": "<-", "↔": "<->",
    "«": '"', "»": '"',
    "¼": "1/4", "½": "1/2", "¾": "3/4",
}
_TRANSLIT_TABLE = str.maketrans(_TRANSLIT)


_MOJIBAKE_ENCODINGS = ("cp1252", "mac_roman", "latin1")

# Direct substring fixes for known mojibake sequences. These work even when
# the surrounding text contains characters outside cp1252/mac_roman (which
# would make the strict whole-string encode round-trip fail).
_MOJIBAKE_FIXES = {
    # Mac-Roman misread of UTF-8 bytes for U+201X smart-typography
    "‚Äú": "“",  # ‚Äú -> "
    "‚Äù": "”",  # ‚Äù -> "
    "‚Äò": "‘",  # ‚Äò -> '
    "‚Äô": "’",  # ‚Äô -> '
    "‚Äì": "–",  # ‚Äì -> –
    "‚Äî": "—",  # ‚Äî -> —
    "‚Ä¶": "…",  # ‚Ä¶ -> …
    "‚Ä¢": "•",  # ‚Ä¢ -> •
    # cp1252 misread of UTF-8 bytes for U+201X
    "â€œ": "“",  # â€œ -> "
    "â€": "”",  # â€<9d> -> "
    "â€˜": "‘",  # â€˜ -> '
    "â€™": "’",  # â€™ -> '
    "â€“": "–",  # â€“ -> –
    "â€”": "—",  # â€” -> —
    "â€¦": "…",  # â€¦ -> …
    "â€¢": "•",  # â€¢ -> •
    # cp1252 misread of common accented Latin lowercase
    "Ã¡": "á",  # Ã¡ -> á
    "Ã©": "é",  # Ã© -> é
    "Ã­": "í",  # Ã­ -> í
    "Ã³": "ó",  # Ã³ -> ó
    "Ãº": "ú",  # Ãº -> ú
    "Ã±": "ñ",  # Ã± -> ñ
    "Ã¼": "ü",  # Ã¼ -> ü
    "Ã¶": "ö",  # Ã¶ -> ö
    "Ã¤": "ä",  # Ã¤ -> ä
    "Ã«": "ë",  # Ã« -> ë
    "Ã¯": "ï",  # Ã¯ -> ï
    # cp1252 misread of UTF-8 leading 0xC2 byte (Â + symbol)
    "Â ": " ",  # Â<NBSP> -> NBSP
    "Â°": "°",  # Â° -> °
    "Â±": "±",  # Â± -> ±
    "Â§": "§",  # Â§ -> §
    "Â©": "©",  # Â© -> ©
    "Â®": "®",  # Â® -> ®
    "Â«": "«",  # Â« -> «
    "Â»": "»",  # Â» -> »
    "Â¿": "¿",  # Â¿ -> ¿
    "Â¡": "¡",  # Â¡ -> ¡
}


def _weirdness(s: str) -> int:
    return sum(s.count(m) for m in _MOJIBAKE_MARKERS)


_MOJIBAKE_FIXES_SORTED = sorted(_MOJIBAKE_FIXES.items(), key=lambda kv: -len(kv[0]))


def _apply_known_fixes(s: str) -> str:
    for src, dst in _MOJIBAKE_FIXES_SORTED:
        if src in s:
            s = s.replace(src, dst)
    return s


def _fix_mojibake(s: str) -> str:
    """Undo UTF-8 bytes that were misread as cp1252, mac_roman, or latin1.

    Two-pass: (1) replace known mojibake substrings with their correct chars
    (works regardless of surrounding text); (2) try whole-string encode round-
    trips through cp1252/mac_roman/latin1 to clean up anything left, picking
    whichever pass most reduces the count of mojibake markers.
    """
    if not s:
        return s
    for _ in range(3):
        prev = s
        s = _apply_known_fixes(s)
        base_w = _weirdness(s)
        if base_w == 0:
            return s
        best, best_w = s, base_w
        for enc in _MOJIBAKE_ENCODINGS:
            try:
                candidate = s.encode(enc, errors="strict").decode("utf-8", errors="strict")
            except (UnicodeEncodeError, UnicodeDecodeError):
                continue
            w = _weirdness(candidate)
            if w < best_w:
                best, best_w = candidate, w
        if best is not s:
            s = best
        if s == prev:
            break
    return s


def _clean_text(s: str, dropped: Counter) -> str:
    """Return a UTF-8-safe version of *s*.

    Mojibake is repaired, then common typography is mapped to ASCII. Any
    remaining character that is neither printable ASCII, a tab/newline, nor a
    standard Unicode letter/digit/mark is replaced with a blank. Dropped
    characters are recorded in *dropped* for a summary at the end.
    """
    if not isinstance(s, str) or not s:
        return s
    s = _fix_mojibake(s)

    def _decode_xlsx_escape(match):
        cp = int(match.group(1), 16)
        # Control chars in this escape form are noise; drop them. Anything
        # else may have been a literal "_xNNNN_" so reconstruct as a real char.
        if cp < 0x20 or cp == 0x7F:
            dropped[chr(cp)] += 1
            return ""
        return chr(cp)

    s = _XLSX_ESCAPE_RE.sub(_decode_xlsx_escape, s)
    s = s.translate(_TRANSLIT_TABLE)

    out = []
    for ch in s:
        cp = ord(ch)
        if cp == 0x09 or cp == 0x0A or cp == 0x0D:
            out.append(ch)
            continue
        if cp < 0x20 or cp == 0x7F:
            dropped[ch] += 1
            continue
        if cp < 0x80:
            out.append(ch)
            continue
        cat = unicodedata.category(ch)
        if cat[0] in ("L", "N", "M"):
            # letters/numbers/marks — keep as valid UTF-8
            out.append(ch)
            continue
        # Try NFKD decomposition to find an ASCII equivalent.
        decomposed = unicodedata.normalize("NFKD", ch)
        ascii_part = "".join(c for c in decomposed if ord(c) < 0x80 and not unicodedata.combining(c))
        if ascii_part:
            out.append(ascii_part)
        else:
            dropped[ch] += 1  # replace with blank
    return "".join(out)


def _stringify(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and pd.isna(value):
        return ""
    if isinstance(value, pd.Timestamp):
        if value.normalize() == value:
            return value.date().isoformat()
        return value.isoformat()
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def load_dataframe(input_path: Path, sheet: Optional[Union[str, int]]) -> pd.DataFrame:
    suffix = input_path.suffix.lower()
    if suffix in {".xlsx", ".xls", ".xlsm", ".xlsb", ".ods"}:
        return pd.read_excel(
            input_path,
            sheet_name=sheet if sheet is not None else 0,
            dtype=object,
        )
    if suffix in {".csv", ".tsv"}:
        sep = "\t" if suffix == ".tsv" else ","
        last_err: Optional[Exception] = None
        for encoding in ("utf-8-sig", "utf-8", "cp1252", "latin1"):
            try:
                return pd.read_csv(input_path, sep=sep, dtype=object, encoding=encoding)
            except UnicodeDecodeError as exc:
                last_err = exc
                continue
        # All strict attempts failed — fall back to replacement so the load
        # still succeeds; sanitization downstream will scrub the placeholders.
        print(
            f"warning: could not decode {input_path} cleanly ({last_err}); "
            "falling back to utf-8 with character replacement",
            file=sys.stderr,
        )
        return pd.read_csv(
            input_path, sep=sep, dtype=object, encoding="utf-8", encoding_errors="replace"
        )
    raise ValueError(f"Unsupported file extension: {suffix}")


def build_payload(df: pd.DataFrame, title: str, source: str, script: str, command: str):
    dropped: Counter = Counter()
    columns = [_clean_text(str(col), dropped) for col in df.columns]
    records = []
    for _, row in df.iterrows():
        record = {}
        for original, cleaned in zip(df.columns, columns):
            record[cleaned] = _clean_text(_stringify(row[original]), dropped)
        records.append(record)
    payload = {
        "metadata": {
            "title": title,
            "source": source,
            "created": datetime.now().isoformat(),
            "script": script,
            "command": command,
        },
        "records": records,
    }
    return payload, dropped


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Path to the .xlsx, .xls, .csv, or .tsv input file")
    parser.add_argument("output", help="Path to the output .json file")
    parser.add_argument("--title", help="Title to embed in metadata (defaults to input filename stem)")
    parser.add_argument("--source", help="Source path to embed in metadata (defaults to input path as given)")
    parser.add_argument("--sheet", help="Sheet name or zero-based index for Excel inputs")
    args = parser.parse_args(argv[1:])

    input_path = Path(args.input)
    output_path = Path(args.output)
    if not input_path.exists():
        parser.error(f"input file not found: {input_path}")

    sheet: Optional[Union[str, int]] = None
    if args.sheet is not None:
        sheet = int(args.sheet) if args.sheet.lstrip("-").isdigit() else args.sheet

    df = load_dataframe(input_path, sheet)

    title = args.title or input_path.stem
    source = args.source or args.input
    script = str(Path(__file__).resolve())
    command = " ".join(argv)

    payload, dropped = build_payload(df, title, source, script, command)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"wrote {len(payload['records'])} records, {len(df.columns)} columns to {output_path}")
    if dropped:
        sample = ", ".join(f"{repr(ch)}x{n}" for ch, n in dropped.most_common(8))
        print(f"replaced {sum(dropped.values())} unmappable character(s) with blanks: {sample}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
