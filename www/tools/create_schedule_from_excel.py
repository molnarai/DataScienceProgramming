#!/usr/bin/env python
TITLE = r"""
  ____       _              _       _
 / ___|  ___| |__   ___  __| |_   _| | ___
 \___ \ / __| '_ \ / _ \/ _` | | | | |/ _ \
  ___) | (__| | | |  __/ (_| | |_| | |  __/
 |____/ \___|_| |_|\___|\__,_|\__,_|_|\___|

"""
import os
jp = os.path.join
import sys
import re
import pandas as pd
import argparse

WWW_DIR = os.path.abspath(jp(os.path.dirname(__file__), ".."))

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert_to_json import _fix_mojibake


def _clean(value):
    return _fix_mojibake(value) if isinstance(value, str) else value


def main(filename: str, dry_run: bool = False, over_write: bool = False):
    schedule_df = pd.read_excel(filename)
    columns_to_keep = ["Session", "Topic", "InClass", "Milestone"]
    available_columns = [col for col in columns_to_keep if col in schedule_df.columns]
    missing = [col for col in columns_to_keep if col not in schedule_df.columns]
    if missing:
        print(f"Warning: missing columns in {filename}: {', '.join(missing)}")
    schedule_df = schedule_df[available_columns]
    # Sessions are numeric in Excel but render as plain integers here; blank
    # rows (e.g. "-- no class --") keep an empty Session cell.
    if "Session" in schedule_df.columns:
        schedule_df['Session'] = schedule_df['Session'].map(
            lambda x: str(int(float(x))) if x != "" else "", na_action="ignore")
    schedule_df = schedule_df.fillna("")
    schedule_df = schedule_df.map(_clean)

    markdown = schedule_df.rename(lambda s: s.replace(' ', ''), axis=1).to_markdown(index=False)
    html = schedule_df.to_html(index=False, classes="table table-striped table-hover")

    markdown_file = jp(WWW_DIR, "content", "schedule.md")
    html_file = jp(WWW_DIR, "content", "schedule.html")

    print(f"Read {len(schedule_df)} rows, {len(available_columns)} columns from {filename}")

    if dry_run:
        print(markdown)
        print("Done.")
        return

    ###
    ### Markdown
    ###
    if not over_write and os.path.exists(markdown_file):
        print(f"Skipping {markdown_file}")
    else:
        print(f"Writing to {markdown_file}")
        with open(markdown_file, "w", encoding="utf-8") as f:
            f.write(markdown)
            f.write("\n")

    ###
    ### HTML
    ###
    if not over_write and os.path.exists(html_file):
        print(f"Skipping {html_file}")
    else:
        print(f"Writing to {html_file}")
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)
            f.write("\n")

    print("Done.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create the class schedule from an Excel schedule.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    parser.add_argument("--test", action="store_true", help="Enable dry run mode")
    parser.add_argument("--force", action="store_true", help="Force overwriting existing files")
    args = parser.parse_args()
    print(TITLE)
    main(args.filename, args.test, args.force)
