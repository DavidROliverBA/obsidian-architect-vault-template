#!/usr/bin/env python3
"""
Analyze wiki-link connectivity and density across all notes.
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Directories to exclude
EXCLUDE_DIRS = {
    '.git', '.obsidian', 'node_modules', '.claude', 'scripts',
    '+Templates', 'screenshots', '.smart-env'
}

def should_process_file(file_path):
    """Check if file should be processed."""
    parts = Path(file_path).parts
    return not any(excluded in parts for excluded in EXCLUDE_DIRS)

def extract_wiki_links(content):
    """Extract all [[wiki-links]] from content, handling display text."""
    # Pattern matches [[link]] or [[link|display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    links = re.findall(pattern, content)
    # Clean up links (remove .md extension if present)
    return [link.replace('.md', '').strip() for link in links]

def count_words(content):
    """Count words in content (excluding frontmatter)."""
    # Remove frontmatter
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    # Remove code blocks
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    # Count words
    words = re.findall(r'\b\w+\b', content)
    return len(words)

def normalize_filename(filename):
    """Normalize filename to match wiki-link format."""
    # Remove .md extension and path
    return Path(filename).stem

def main():
    vault_path = Path('/Users/david.oliver/Documents/GitHub/obsidian-architect-vault-template')

    # Step 1: Find all markdown files
    all_files = []
    for root, dirs, files in os.walk(vault_path):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if should_process_file(file_path):
                    all_files.append(file_path)

    print(f"Found {len(all_files)} markdown files to analyze")

    # Step 2: Build maps
    file_to_outgoing = {}  # filename -> list of links
    file_to_content = {}   # filename -> content
    all_note_names = set() # all note names (without .md)

    for file_path in all_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            rel_path = os.path.relpath(file_path, vault_path)
            note_name = normalize_filename(file_path)

            all_note_names.add(note_name)
            file_to_outgoing[rel_path] = extract_wiki_links(content)
            file_to_content[rel_path] = content

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    # Step 3: Build backlink index
    backlink_index = defaultdict(list)  # target_note -> [source_files]

    for source_file, links in file_to_outgoing.items():
        for link in links:
            backlink_index[link].append(source_file)

    # Step 4: Calculate metrics for each note
    notes_data = {}
    backlink_counts = []

    for file_path in all_files:
        rel_path = os.path.relpath(file_path, vault_path)
        note_name = normalize_filename(file_path)
        content = file_to_content.get(rel_path, '')

        outgoing_links = file_to_outgoing.get(rel_path, [])
        outgoing_count = len(outgoing_links)

        # Find broken links (links to notes that don't exist)
        broken_links = [link for link in outgoing_links if link not in all_note_names]
        broken_count = len(broken_links)

        # Count backlinks
        backlinks = backlink_index.get(note_name, [])
        backlink_count = len(backlinks)
        backlink_counts.append(backlink_count)

        # Calculate link density (links per 100 words)
        word_count = count_words(content)
        link_density = (outgoing_count / word_count * 100) if word_count > 0 else 0

        # Store data
        notes_data[rel_path] = {
            'noteName': note_name,
            'outgoingLinks': outgoing_count,
            'backlinks': backlink_count,
            'brokenLinks': broken_count,
            'brokenLinkList': broken_links,
            'wordCount': word_count,
            'linkDensityPercentage': round(link_density, 2),
            'isOrphaned': backlink_count == 0,
            'isHub': False  # Will calculate after sorting
        }

    # Step 5: Identify hub notes (top 10% by backlinks)
    backlink_counts.sort(reverse=True)
    hub_threshold_index = max(0, int(len(backlink_counts) * 0.1) - 1)
    hub_threshold = backlink_counts[hub_threshold_index] if backlink_counts else 0

    for file_path, data in notes_data.items():
        if data['backlinks'] >= hub_threshold and hub_threshold > 0:
            data['isHub'] = True

    # Step 6: Calculate link density score (0-100)
    for file_path, data in notes_data.items():
        score = 0

        # Base: outgoing links (cap at 5 links = 40 points)
        score += min(data['outgoingLinks'] / 5, 1) * 40

        # Backlinks (cap at 3 backlinks = 30 points)
        score += min(data['backlinks'] / 3, 1) * 30

        # Penalty: orphaned
        if data['isOrphaned']:
            score -= 20

        # Penalty: broken links
        if data['brokenLinks'] > 0:
            score -= 10

        # Bonus: hub note
        if data['isHub']:
            score += 10

        # Ensure score stays in 0-100 range
        score = max(0, min(100, score))

        data['linkDensityScore'] = round(score, 1)

    # Step 7: Generate summary lists
    orphaned_notes = [fp for fp, data in notes_data.items() if data['isOrphaned']]
    hub_notes = sorted(
        [(fp, data['backlinks']) for fp, data in notes_data.items() if data['isHub']],
        key=lambda x: x[1],
        reverse=True
    )

    # Step 8: Create output
    output = {
        'summary': {
            'totalNotes': len(notes_data),
            'orphanedCount': len(orphaned_notes),
            'hubCount': len(hub_notes),
            'totalBrokenLinks': sum(data['brokenLinks'] for data in notes_data.values()),
            'averageLinkDensityScore': round(sum(data['linkDensityScore'] for data in notes_data.values()) / len(notes_data), 1) if notes_data else 0,
            'averageOutgoingLinks': round(sum(data['outgoingLinks'] for data in notes_data.values()) / len(notes_data), 1) if notes_data else 0,
            'averageBacklinks': round(sum(data['backlinks'] for data in notes_data.values()) / len(notes_data), 1) if notes_data else 0
        },
        'notes': notes_data,
        'orphanedNotes': orphaned_notes,
        'hubNotes': [{'file': fp, 'backlinks': count} for fp, count in hub_notes],
        'brokenLinks': {
            fp: data['brokenLinkList']
            for fp, data in notes_data.items()
            if data['brokenLinks'] > 0
        }
    }

    # Write to file
    output_path = vault_path / 'link_analysis.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nAnalysis complete!")
    print(f"Total notes analyzed: {output['summary']['totalNotes']}")
    print(f"Orphaned notes: {output['summary']['orphanedCount']}")
    print(f"Hub notes: {output['summary']['hubCount']}")
    print(f"Total broken links: {output['summary']['totalBrokenLinks']}")
    print(f"Average link density score: {output['summary']['averageLinkDensityScore']}")
    print(f"Average outgoing links: {output['summary']['averageOutgoingLinks']}")
    print(f"Average backlinks: {output['summary']['averageBacklinks']}")
    print(f"\nResults written to: {output_path}")

    # Print top 10 hub notes
    print("\n=== Top 10 Hub Notes ===")
    for item in hub_notes[:10]:
        print(f"{item[0]}: {item[1]} backlinks")

    # Print bottom 10 by link density score
    print("\n=== Bottom 10 by Link Density Score ===")
    sorted_by_score = sorted(notes_data.items(), key=lambda x: x[1]['linkDensityScore'])
    for file_path, data in sorted_by_score[:10]:
        print(f"{file_path}: {data['linkDensityScore']} (out: {data['outgoingLinks']}, in: {data['backlinks']}, broken: {data['brokenLinks']})")

if __name__ == '__main__':
    main()
