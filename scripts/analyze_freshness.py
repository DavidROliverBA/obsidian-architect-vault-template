#!/usr/bin/env python3
"""
Analyze content freshness and tag quality for all notes in the vault.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime, timedelta
import yaml

# Define the vault root
VAULT_ROOT = Path("/Users/david.oliver/Documents/GitHub/obsidian-architect-vault-template")

# Directories to exclude
EXCLUDE_DIRS = {
    'node_modules', '.obsidian', '.git', '.smart-env',
    '.claude', 'scripts', 'screenshots'
}

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return {}

    try:
        # Find the closing ---
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1]
            return yaml.safe_load(frontmatter_text) or {}
    except Exception as e:
        print(f"Error parsing frontmatter: {e}")

    return {}

def get_file_mtime(filepath):
    """Get file modification time in days since modified."""
    mtime = os.path.getmtime(filepath)
    mtime_date = datetime.fromtimestamp(mtime)
    days_since = (datetime.now() - mtime_date).days
    return days_since

def parse_date(date_str):
    """Parse date string to datetime."""
    if not date_str:
        return None

    # Handle various date formats
    formats = ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S']

    for fmt in formats:
        try:
            return datetime.strptime(str(date_str), fmt)
        except:
            continue

    return None

def calculate_freshness_score(note_type, days_since_modified, has_tags, tag_count):
    """Calculate freshness score based on note type and modification date."""

    # Freshness points (0-60)
    freshness_pts = 0
    freshness_category = "stale"

    if note_type == "Task":
        if days_since_modified < 7:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 30:
            freshness_pts = 40
            freshness_category = "recent"
        elif days_since_modified < 60:
            freshness_pts = 20
            freshness_category = "aging"
        else:
            freshness_pts = 10
            freshness_category = "stale"

    elif note_type == "Project":
        if days_since_modified < 30:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 90:
            freshness_pts = 40
            freshness_category = "recent"
        elif days_since_modified < 180:
            freshness_pts = 20
            freshness_category = "aging"
        else:
            freshness_pts = 10
            freshness_category = "stale"

    elif note_type == "Adr":
        if days_since_modified < 180:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 365:
            freshness_pts = 40
            freshness_category = "recent"
        else:
            freshness_pts = 20
            freshness_category = "stable"

    elif note_type == "Meeting":
        # Meetings age naturally
        freshness_pts = 50
        freshness_category = "archived"

    elif note_type == "Page":
        if days_since_modified < 90:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 180:
            freshness_pts = 40
            freshness_category = "recent"
        elif days_since_modified < 365:
            freshness_pts = 20
            freshness_category = "aging"
        else:
            freshness_pts = 10
            freshness_category = "stale"

    elif note_type == "DailyNote":
        # Daily notes age naturally
        freshness_pts = 50
        freshness_category = "archived"

    elif note_type in ["Person", "Organisation", "Weblink"]:
        if days_since_modified < 90:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 180:
            freshness_pts = 40
            freshness_category = "recent"
        else:
            freshness_pts = 30
            freshness_category = "stable"

    else:
        # Default for unknown types
        if days_since_modified < 60:
            freshness_pts = 60
            freshness_category = "fresh"
        elif days_since_modified < 120:
            freshness_pts = 40
            freshness_category = "recent"
        else:
            freshness_pts = 20
            freshness_category = "aging"

    # Tag points (0-40)
    tag_pts = 0
    if has_tags:
        tag_pts += 20  # Has tags at all
        if 2 <= tag_count <= 5:
            tag_pts += 20  # Optimal count
        elif tag_count == 1:
            tag_pts += 10  # Okay
        elif tag_count > 5:
            tag_pts += 10  # Excessive but still tagged

    total_score = freshness_pts + tag_pts

    return {
        "freshnessScore": total_score,
        "freshnessPts": freshness_pts,
        "tagPts": tag_pts,
        "freshnessCategory": freshness_category
    }

def analyze_note(filepath):
    """Analyze a single note for freshness and tag quality."""

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter = parse_frontmatter(content)

        # Get note type
        note_type = frontmatter.get('type', 'Unknown')

        # Get modification date
        modified_date = frontmatter.get('modified') or frontmatter.get('created')

        if modified_date:
            modified_dt = parse_date(modified_date)
            if modified_dt:
                days_since_modified = (datetime.now() - modified_dt).days
            else:
                days_since_modified = get_file_mtime(filepath)
        else:
            days_since_modified = get_file_mtime(filepath)

        # Get tags
        tags = frontmatter.get('tags', [])
        if isinstance(tags, str):
            tags = [tags]
        elif not isinstance(tags, list):
            tags = []

        has_tags = len(tags) > 0
        tag_count = len(tags)

        # Calculate scores
        scores = calculate_freshness_score(note_type, days_since_modified, has_tags, tag_count)

        return {
            "freshnessScore": scores["freshnessScore"],
            "type": note_type,
            "daysSinceModified": days_since_modified,
            "freshnessCategory": scores["freshnessCategory"],
            "hasTags": has_tags,
            "tagCount": tag_count,
            "tags": tags,
            "isStale": scores["freshnessCategory"] in ["stale", "aging"],
            "freshnessPts": scores["freshnessPts"],
            "tagPts": scores["tagPts"]
        }

    except Exception as e:
        print(f"Error analyzing {filepath}: {e}")
        return None

def main():
    """Main analysis function."""

    results = {
        "notes": {},
        "staleNotes": [],
        "summary": {
            "totalNotes": 0,
            "byType": {},
            "byFreshnessCategory": {},
            "averageScore": 0,
            "notesWithTags": 0,
            "notesWithoutTags": 0
        }
    }

    # Find all markdown files
    for root, dirs, files in os.walk(VAULT_ROOT):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith('.md') and not file.startswith('.'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, VAULT_ROOT)

                # Skip README files
                if file == 'README.md' or file.startswith('CONTRIBUTING'):
                    continue

                analysis = analyze_note(filepath)

                if analysis:
                    results["notes"][rel_path] = analysis
                    results["summary"]["totalNotes"] += 1

                    # Track by type
                    note_type = analysis["type"]
                    if note_type not in results["summary"]["byType"]:
                        results["summary"]["byType"][note_type] = 0
                    results["summary"]["byType"][note_type] += 1

                    # Track by freshness category
                    category = analysis["freshnessCategory"]
                    if category not in results["summary"]["byFreshnessCategory"]:
                        results["summary"]["byFreshnessCategory"][category] = 0
                    results["summary"]["byFreshnessCategory"][category] += 1

                    # Track stale notes
                    if analysis["isStale"]:
                        results["staleNotes"].append(rel_path)

                    # Track tags
                    if analysis["hasTags"]:
                        results["summary"]["notesWithTags"] += 1
                    else:
                        results["summary"]["notesWithoutTags"] += 1

    # Calculate average score
    if results["summary"]["totalNotes"] > 0:
        total_score = sum(note["freshnessScore"] for note in results["notes"].values())
        results["summary"]["averageScore"] = round(total_score / results["summary"]["totalNotes"], 2)

    # Output results
    print(json.dumps(results, indent=2))

    # Also save to file
    output_file = VAULT_ROOT / "freshness_analysis.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"\n\nAnalysis complete. Results saved to: {output_file}")
    print(f"Total notes analyzed: {results['summary']['totalNotes']}")
    print(f"Average freshness score: {results['summary']['averageScore']}/100")
    print(f"Stale notes: {len(results['staleNotes'])}")

if __name__ == "__main__":
    main()
