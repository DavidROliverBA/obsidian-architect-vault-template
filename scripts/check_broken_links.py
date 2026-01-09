#!/usr/bin/env python3
"""
Scan Obsidian vault for broken wiki-links.
Checks all markdown files in root directory (excluding specific folders).
"""

import re
import os
import json
from pathlib import Path
from typing import List, Dict, Set

# Directories to exclude from scanning
EXCLUDE_DIRS = {'+Templates', '.obsidian', '.claude', 'scripts', 'node_modules', '.git', 'screenshots'}

def get_all_markdown_files(vault_path: Path) -> List[Path]:
    """Get all markdown files in the vault."""
    all_files = []
    for file_path in vault_path.rglob('*.md'):
        # Skip files in excluded directories
        if any(excluded in file_path.parts for excluded in EXCLUDE_DIRS):
            continue
        all_files.append(file_path)
    return all_files

def get_root_files(vault_path: Path) -> List[Path]:
    """Get only markdown files in root directory."""
    return [f for f in vault_path.glob('*.md') if f.is_file()]

def build_note_inventory(all_files: List[Path]) -> Set[str]:
    """Build set of all note names (without .md extension)."""
    note_names = set()
    for file_path in all_files:
        note_name = file_path.stem  # filename without extension
        note_names.add(note_name)
    return note_names

def extract_wiki_links_from_content(content: str) -> List[tuple]:
    """
    Extract all wiki-links from content.
    Returns list of tuples: (target_note, display_text, context)
    """
    links = []

    # Pattern: [[Note Name]] or [[Note Name|Display Text]]  or [[Note Name#heading]]
    pattern = r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]'

    for match in re.finditer(pattern, content):
        target = match.group(1).strip()
        display = match.group(2).strip() if match.group(2) else None

        # Get context (50 chars before and after)
        start = max(0, match.start() - 50)
        end = min(len(content), match.end() + 50)
        context = content[start:end].replace('\n', ' ')

        links.append((target, display, context))

    return links

def extract_wiki_links_from_frontmatter(content: str) -> List[tuple]:
    """Extract wiki-links from YAML frontmatter."""
    links = []

    # Extract frontmatter
    frontmatter_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not frontmatter_match:
        return links

    frontmatter = frontmatter_match.group(1)

    # Find all wiki-links in frontmatter
    pattern = r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|([^\]]+))?\]\]'

    for match in re.finditer(pattern, frontmatter):
        target = match.group(1).strip()
        display = match.group(2).strip() if match.group(2) else None

        # Get field context
        lines = frontmatter[:match.start()].split('\n')
        field_line = lines[-1] if lines else ""
        context = f"frontmatter: {field_line}[[{target}]]"

        links.append((target, display, context))

    return links

def check_broken_links(vault_path: Path, files_to_check: List[Path], note_inventory: Set[str]) -> List[Dict]:
    """Check for broken wiki-links in specified files."""
    broken_links = []

    for file_path in files_to_check:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue

        # Extract links from frontmatter
        frontmatter_links = extract_wiki_links_from_frontmatter(content)

        # Extract links from content
        content_links = extract_wiki_links_from_content(content)

        # Check each link
        all_links = []
        all_links.extend([(target, display, context, 'frontmatter') for target, display, context in frontmatter_links])
        all_links.extend([(target, display, context, 'content') for target, display, context in content_links])

        for target, display, context, location in all_links:
            # Check if target note exists (case-sensitive)
            if target not in note_inventory:
                broken_links.append({
                    'source': file_path.name,
                    'target': target,
                    'context': context,
                    'location': location
                })

    return broken_links

def main():
    # Get vault path
    vault_path = Path(__file__).parent.parent

    print(f"Scanning vault: {vault_path}")
    print(f"Excluded directories: {', '.join(EXCLUDE_DIRS)}\n")

    # Get all markdown files (for building inventory)
    all_files = get_all_markdown_files(vault_path)
    print(f"Total markdown files found: {len(all_files)}")

    # Build note inventory (all notes that exist)
    note_inventory = build_note_inventory(all_files)
    print(f"Note inventory size: {len(note_inventory)}\n")

    # Get root files to check
    root_files = get_root_files(vault_path)
    print(f"Checking root directory files: {len(root_files)}\n")

    # Check for broken links
    broken_links = check_broken_links(vault_path, root_files, note_inventory)

    # Output results
    print(f"\n{'='*80}")
    print(f"BROKEN LINKS FOUND: {len(broken_links)}")
    print(f"{'='*80}\n")

    if broken_links:
        # Group by source file
        by_source = {}
        for link in broken_links:
            source = link['source']
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(link)

        for source, links in sorted(by_source.items()):
            print(f"\n{source}:")
            print(f"{'-'*80}")
            for link in links:
                print(f"  Target: {link['target']}")
                print(f"  Location: {link['location']}")
                print(f"  Context: ...{link['context']}...")
                print()

        # Output JSON for programmatic use
        json_output = {
            'brokenLinks': broken_links,
            'summary': {
                'total': len(broken_links),
                'bySource': {source: len(links) for source, links in by_source.items()}
            }
        }

        output_file = vault_path / 'broken_links_report.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=2)

        print(f"\nDetailed report saved to: {output_file}")
    else:
        print("No broken links found! Vault is healthy.")

if __name__ == '__main__':
    main()
