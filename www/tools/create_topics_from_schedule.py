#!/usr/bin/env python
TITLE = r"""
  _____           _             __                       ____       _              _       _      
 |_   _|__  _ __ (_) ___ ___   / _|_ __ ___  _ __ ___   / ___|  ___| |__   ___  __| |_   _| | ___ 
   | |/ _ \| '_ \| |/ __/ __| | |_| '__/ _ \| '_ ` _ \  \___ \ / __| '_ \ / _ \/ _` | | | | |/ _ \
   | | (_) | |_) | | (__\__ \ |  _| | | (_) | | | | | |  ___) | (__| | | |  __/ (_| | |_| | |  __/
   |_|\___/| .__/|_|\___|___/ |_| |_|  \___/|_| |_| |_| |____/ \___|_| |_|\___|\__,_|\__,_|_|\___|
           |_|                                                                                    
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
    df = pd.read_excel(filename, sheet_name="Sheet1")
    df = df.dropna(subset=['Session'])
    df = df.fillna("")
    df = df.map(_clean)
    
    # Ensure output directory exists
    output_dir = jp(WWW_DIR, "content", "topics")
    os.makedirs(output_dir, exist_ok=True)
    
    for j, row in df.iterrows():
        session = int(row['Session'])
        topic = row['Topic']
        theoretical_brief = row['TheoreticalBrief']
        technical_brief = row['TechnicalBrief']
        theoretical = row['TheoreticalDetailed']
        technical = row['TechnicalDetailed']
        # monday = row['Monday'].strftime("%Y-%m-%d") if row['Monday'] != "" and hasattr(row['Monday'], 'strftime') else ""
        datefld = row['Date'].strftime("%Y-%m-%d") if row['Date'] != "" and hasattr(row['Date'], 'strftime') else ""
        # dt = f"Monday {monday}, Wednesday {wednesday}"
        dt = f"{datefld}"
        # Use a proper Hugo date format for the first date
        # hugo_date = monday if monday else wednesday
        hugo_date = datefld
        if not hugo_date:
            hugo_date = "2024-01-01"  # fallback date
        output_file = jp(WWW_DIR, "content", "topics", f"topic-{session:02d}.md")
        print(f"Session {session:2d} on {dt}: {topic}")
        if not over_write and os.path.exists(output_file):
            print(f"Skipping {output_file}")
            continue
        print(f"Writing to {output_file}")
        if not dry_run:
            with open(output_file, "w", encoding="utf-8") as f:
                txt = f"""---
date: {hugo_date}
classdates: '{dt}'
draft: false
title: '{topic}'
concept: "{theoretical_brief}"
practice: "{technical_brief}"
weight: {10*session}
numsession: {session}
---
## Concept
{theoretical}

## Practice
{technical}

"""
                f.write(txt)

    print("Done.")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some files.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    parser.add_argument("--test", action="store_true", help="Enable dry run mode")
    parser.add_argument("--force", action="store_true", help="Force overwriting existing files")
    args = parser.parse_args()
    print(TITLE)
    main(args.filename, args.test, args.force)