#!/usr/bin/env python
TITLE = r'''
  __  __ _ _           _                        
 |  \/  (_) | ___  ___| |_ ___  _ __   ___  ___ 
 | |\/| | | |/ _ \/ __| __/ _ \| '_ \ / _ \/ __|
 | |  | | | |  __/\__ \ || (_) | | | |  __/\__ \
 |_|  |_|_|_|\___||___/\__\___/|_| |_|\___||___/
                                                
'''
import os
jp = os.path.join
import sys
import re
import pandas as pd
import argparse
import json
import datetime

WWW_DIR = os.path.abspath(jp(os.path.dirname(__file__), ".."))


def _slugify(s: str, max_len: int = 50) -> str:
    s = s.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > max_len:
        s = s[:max_len].rsplit("-", 1)[0]
    return s


def _format_date(value) -> str:
    if value is None or value == "":
        return ""
    try:
        return pd.Timestamp(value).strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        return str(value)


def _split_frontmatter(text: str):
    """Return (had_frontmatter, body_text). If the file starts with a YAML
    frontmatter block (``---`` ... ``---``), strip it and return the body;
    otherwise treat the whole file as body."""
    if not text.startswith("---"):
        return False, text
    lines = text.split("\n", 1)
    if len(lines) < 2:
        return False, text
    rest = lines[1]
    end = rest.find("\n---")
    if end < 0:
        return False, text
    body = rest[end + len("\n---"):]
    if body.startswith("\n"):
        body = body[1:]
    return True, body

def main(filename: str, dry_run: bool = False, over_write: bool = False):
    schedule_df = pd.read_excel(filename)
    # columns_to_keep = ["Session", "Monday", "Wednesday", "Topic", "InClass", "Milestone"]
    columns_to_keep = ["Session", "Date", "Topic", "InClass", "Milestone", "MilestonePercent"]
    available_columns = [col for col in columns_to_keep if col in schedule_df.columns]
    schedule_df = schedule_df[available_columns]
    schedule_df['Session'] = schedule_df['Session'].map(lambda x: str(int(float(x))) if x != "" else "", na_action="ignore")
    schedule_df = schedule_df.fillna("")
    has_percent = "MilestonePercent" in schedule_df.columns
    rows_iter = schedule_df.itertuples(index=False)

    milestone_data = []
    per_milestone_pages = []
    for row in rows_iter:
        milestone = row.Milestone
        datefld = row.Date
        if not milestone or milestone == "":
            continue
        # Extract milestone name
        match = re.match(r'(M(\d+)[^.]*)', milestone)
        if not match:
            continue
        name = match.group(1)
        number = int(match.group(2))
        percent_raw = getattr(row, "MilestonePercent", "") if has_percent else ""
        try:
            percent = int(percent_raw) if percent_raw not in ("", None) else None
        except (ValueError, TypeError):
            percent = None

        milestone_data.append({'Milestone': name, 'Date': datefld})
        per_milestone_pages.append({
            'number': number,
            'name': name,
            'date': datefld,
            'milestone_text': milestone,
            'percent': percent,
        })

    milestone_df = pd.DataFrame(milestone_data)

    data = milestone_df.to_dict(orient='records')
    markdown = milestone_df.rename(lambda s: s.replace(' ', ''), axis=1).to_markdown(index=False)
    html = milestone_df.to_html(index=False, classes="table table-striped table-hover")

    output_file = jp(WWW_DIR, "data", "milestones_schedule.json")
    html_file = jp(WWW_DIR, "content", "milestones_schedule.html")
    markdown_file = jp(WWW_DIR, "content", "milestones_schedule.md")
    tex_file = jp(WWW_DIR, "static", "files", "milestones_schedule.tex")

    if not dry_run:
        ###
        ### Markdown

        if not over_write and os.path.exists(markdown_file):
            print(f"Skipping {markdown_file}")
        else:
            print(f"Writing to {markdown_file}")
            with open(markdown_file, "w") as f:
                f.write(markdown)
                f.write("\n")
        
        ###
        ### HTML
        ###
        if not over_write and os.path.exists(html_file):
            print(f"Skipping {html_file}")
        else:
            print(f"Writing to {html_file}")
            with open(html_file, "w") as f:
                f.write(html)
                f.write("\n")
        
        ###
        ### Tex
        ###
        if not over_write and os.path.exists(tex_file):
            print(f"Skipping {tex_file}")
        else:
            amp = chr(38)  # ASCII ampersand
            with open(tex_file, "w", encoding='utf-8') as io:
                for i, row in milestone_df.iterrows():
                    io.write(f"{row.Milestone} {amp} {row.Date}  \\\\\n")

        ###
        ### JSON
        ###
        if not over_write and os.path.exists(output_file):
            print(f"File already exists: {output_file}")
        else:
            output = {
                "metadata": {
                    "title": "Schedule",
                    "source": filename,
                    "created": datetime.datetime.now().isoformat(),
                },
                "records": data
            }
            print(f"Writing to {output_file}")
            if not dry_run:
                with open(output_file, "w") as f:
                    json.dump(output, f, default=str, indent=2)
                    f.write("\n")
            else:
                print(json.dumps(output, default=str, indent=2))

        ###
        ### Per-milestone content pages
        ###
        project_dir = jp(WWW_DIR, "content", "project")
        os.makedirs(project_dir, exist_ok=True)
        for page in per_milestone_pages:
            number = page['number']
            short_name = page['name']  # e.g. "M01: Team roster, project choice, ..."
            after_colon = short_name.split(":", 1)[1].strip() if ":" in short_name else short_name
            description = after_colon if after_colon.endswith(".") else after_colon + "."
            slug = _slugify(after_colon)
            date_str = _format_date(page['date'])
            percent = page['percent']
            page_file = jp(project_dir, f"project-m{number:02d}-{slug}.md")
            existing_body = None
            if os.path.exists(page_file):
                with open(page_file, "r", encoding="utf-8") as f:
                    existing = f.read()
                _, existing_body = _split_frontmatter(existing)
                print(f"Updating header of {page_file}")
            else:
                print(f"Writing to {page_file}")
            lines = [
                "---",
                f"title: 'M{number:02d}'",
                f"date: {date_str or '2024-01-01'}",
                f"due_date: {date_str}",
                f"weight: {10 * number}",
                "draft: false",
                f"milestone: M{number:02d}",
                f"description: '{description.replace(chr(39), chr(39)*2)}'",
                f"submission: {date_str}",
            ]
            if percent is not None:
                lines.append(f"percent: {percent}")
            lines.append("---")
            new_text = "\n".join(lines) + "\n"
            if existing_body is not None:
                new_text += existing_body if existing_body.startswith("\n") else "\n" + existing_body
            else:
                new_text += "\n(Content not yet posted. Please check back.)\n"
            with open(page_file, "w", encoding="utf-8") as f:
                f.write(new_text)

    print("Done.")
        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create milestones from Excel schedule.")
    parser.add_argument("filename", type=str, help="The name of the file to process")
    parser.add_argument("--test", action="store_true", help="Enable dry run mode")
    parser.add_argument("--force", action="store_true", help="Force overwriting existing files")
    args = parser.parse_args()
    main(args.filename, args.test, args.force)