#!/usr/bin/env python3
"""Walk a directory tree and repair mojibake in text files in place.

Reuses the fix table from ``convert_to_json`` so behavior stays in sync with
the spreadsheet -> JSON converter. Prints each modified file and a summary
of how many sequences were replaced. Pass --dry-run to preview without
writing.
"""

import argparse
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from convert_to_json import _fix_mojibake  # noqa: E402

DEFAULT_GLOBS = ("*.md", "*.markdown", "*.html", "*.json", "*.txt", "*.yaml", "*.yml", "*.toml")


def iter_files(root: Path, globs):
    for pattern in globs:
        yield from root.rglob(pattern)


def main(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default="content",
        help="Directory to walk (default: content). Resolved relative to CWD.",
    )
    parser.add_argument(
        "--glob",
        action="append",
        default=None,
        help=f"File glob to include (repeatable). Default: {' '.join(DEFAULT_GLOBS)}",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    args = parser.parse_args(argv[1:])

    root = Path(args.root).resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    globs = args.glob or DEFAULT_GLOBS
    changed = 0
    scanned = 0
    char_counts: Counter = Counter()

    for fp in iter_files(root, globs):
        if not fp.is_file():
            continue
        scanned += 1
        try:
            original = fp.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"skip (not utf-8): {fp}", file=sys.stderr)
            continue
        fixed = _fix_mojibake(original)
        if fixed == original:
            continue
        diff_chars = sum(1 for a, b in zip(original, fixed) if a != b) + abs(len(original) - len(fixed))
        char_counts[fp.suffix] += diff_chars
        changed += 1
        if args.dry_run:
            print(f"would fix: {fp} ({diff_chars} char delta)")
        else:
            fp.write_text(fixed, encoding="utf-8")
            print(f"fixed: {fp} ({diff_chars} char delta)")

    suffix = " (dry-run)" if args.dry_run else ""
    print(f"scanned {scanned} files, {changed} changed{suffix}")
    if char_counts:
        breakdown = ", ".join(f"{ext or '<none>'}={n}" for ext, n in char_counts.most_common())
        print(f"char-delta by extension: {breakdown}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
