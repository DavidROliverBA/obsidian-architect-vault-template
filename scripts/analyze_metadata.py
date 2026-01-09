#!/usr/bin/env python3
"""
Analyze frontmatter metadata completeness across all vault notes.
Generates a comprehensive report with metadata scores for each note.
"""

import os
import re
import json
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any, Optional

# Required fields by note type
REQUIRED_FIELDS = {
    'universal': ['type', 'title', 'created'],
    'Task': ['completed', 'priority'],
    'Project': ['status', 'priority'],
    'Adr': ['status', 'relatedTo', 'supersedes', 'dependsOn'],
    'Meeting': ['date'],
    'Person': ['role'],
    'Page': [],
    'Weblink': ['url', 'domain'],
    'Organisation': [],
    'DailyNote': ['date'],
    'AtomicNote': [],
    'Course': [],
    'CodeSnippet': [],
    'Zettel': [],
    'MOC': []
}

# Quality fields (optional but recommended)
QUALITY_FIELDS = ['tags', 'description', 'modified']

# ADR-specific quality indicators
ADR_QUALITY_INDICATORS = ['confidence', 'freshness', 'source']

# Directories to exclude
EXCLUDE_DIRS = {
    '.obsidian', 'node_modules', '.git', '.claude', '+Templates',
    'scripts', 'screenshots', 'PDFs'
}

# Files to exclude
EXCLUDE_FILES = {
    'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'BLOG_POST.md',
    'VALIDATION_REPORT.md', 'VAULT_AUTOMATION_SETUP.md', 'METADATA_ANALYSIS.md'
}


def find_markdown_files(vault_root: Path) -> List[Path]:
    """Find all markdown files, excluding system directories."""
    markdown_files = []

    for root, dirs, files in os.walk(vault_root):
        # Remove excluded directories from traversal
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith('.')]

        for file in files:
            if file.endswith('.md') and file not in EXCLUDE_FILES:
                file_path = Path(root) / file
                markdown_files.append(file_path)

    return markdown_files


def extract_frontmatter(content: str) -> Optional[Dict[str, Any]]:
    """Extract YAML frontmatter from markdown content."""
    # Match frontmatter between --- markers
    pattern = r'^---\s*\n(.*?)\n---'
    match = re.search(pattern, content, re.DOTALL)

    if not match:
        return None

    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def check_field_value(value: Any) -> bool:
    """Check if a field has a meaningful value."""
    if value is None:
        return False
    if isinstance(value, str) and value.strip() == '':
        return False
    if isinstance(value, list) and len(value) == 0:
        return False
    return True


def calculate_metadata_score(
    note_type: Optional[str],
    frontmatter: Dict[str, Any],
    required_fields: List[str],
    missing_required: List[str]
) -> int:
    """
    Calculate metadata completeness score (0-100).

    Scoring:
    - Required fields: 60 points (proportional)
    - Quality fields: 30 points (10 points each for tags, description, modified)
    - ADR indicators: 10 points (3.33 points each for confidence, freshness, source)
    """
    score = 0

    # Required fields: 60 points
    if len(required_fields) > 0:
        required_present = len(required_fields) - len(missing_required)
        score += (required_present / len(required_fields)) * 60
    else:
        # No type-specific required fields, give full credit
        score += 60

    # Quality fields: 30 points (10 each)
    quality_count = 0
    for field in QUALITY_FIELDS:
        if check_field_value(frontmatter.get(field)):
            quality_count += 1
    score += quality_count * 10

    # ADR quality indicators: 10 points (3.33 each)
    if note_type == 'Adr':
        adr_quality_count = 0
        for field in ADR_QUALITY_INDICATORS:
            if check_field_value(frontmatter.get(field)):
                adr_quality_count += 1
        score += adr_quality_count * 3.33

    return min(round(score), 100)


def analyze_note(file_path: Path, vault_root: Path) -> Dict[str, Any]:
    """Analyze a single note's metadata completeness."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        return {
            'path': str(file_path.relative_to(vault_root)),
            'metadataScore': 0,
            'type': None,
            'error': f'Failed to read file: {str(e)}'
        }

    frontmatter = extract_frontmatter(content)

    if not frontmatter:
        return {
            'path': str(file_path.relative_to(vault_root)),
            'metadataScore': 0,
            'type': None,
            'requiredFields': REQUIRED_FIELDS['universal'],
            'missingRequired': REQUIRED_FIELDS['universal'],
            'hasDescription': False,
            'hasTags': False,
            'hasModified': False,
            'qualityIndicators': 0,
            'error': 'No frontmatter found'
        }

    note_type = frontmatter.get('type')
    type_required_fields = REQUIRED_FIELDS.get(note_type, [])
    all_required_fields = REQUIRED_FIELDS['universal'] + type_required_fields

    # Check for missing required fields
    missing_required = []
    for field in all_required_fields:
        if not check_field_value(frontmatter.get(field)):
            missing_required.append(field)

    # Check quality fields
    has_description = check_field_value(frontmatter.get('description'))
    has_tags = check_field_value(frontmatter.get('tags'))
    has_modified = check_field_value(frontmatter.get('modified'))
    quality_count = sum([has_description, has_tags, has_modified])

    # Check ADR quality indicators
    adr_quality_count = 0
    if note_type == 'Adr':
        for field in ADR_QUALITY_INDICATORS:
            if check_field_value(frontmatter.get(field)):
                adr_quality_count += 1

    # Calculate metadata score
    metadata_score = calculate_metadata_score(
        note_type, frontmatter, all_required_fields, missing_required
    )

    result = {
        'path': str(file_path.relative_to(vault_root)),
        'metadataScore': metadata_score,
        'type': note_type,
        'requiredFields': all_required_fields,
        'missingRequired': missing_required,
        'hasDescription': has_description,
        'hasTags': has_tags,
        'hasModified': has_modified,
        'qualityIndicators': quality_count
    }

    if note_type == 'Adr':
        result['adrQualityIndicators'] = adr_quality_count

    return result


def generate_summary(results: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """Generate summary statistics from analysis results."""
    summary = {
        'totalNotes': 0,
        'averageScore': 0,
        'scoreDistribution': {
            'excellent': 0,  # 90-100
            'good': 0,       # 70-89
            'fair': 0,       # 50-69
            'poor': 0        # 0-49
        },
        'typeDistribution': defaultdict(int),
        'missingFrontmatter': 0
    }

    scores = []

    for note_data in results.values():
        summary['totalNotes'] += 1

        if 'error' in note_data:
            summary['missingFrontmatter'] += 1
        else:
            score = note_data['metadataScore']
            scores.append(score)

            # Score distribution
            if score >= 90:
                summary['scoreDistribution']['excellent'] += 1
            elif score >= 70:
                summary['scoreDistribution']['good'] += 1
            elif score >= 50:
                summary['scoreDistribution']['fair'] += 1
            else:
                summary['scoreDistribution']['poor'] += 1

            # Type distribution
            note_type = note_data.get('type', 'unknown')
            if note_type is None:
                note_type = 'unknown'
            summary['typeDistribution'][note_type] += 1

    # Calculate average score
    if scores:
        summary['averageScore'] = round(sum(scores) / len(scores))

    # Convert defaultdict to regular dict
    summary['typeDistribution'] = dict(summary['typeDistribution'])

    return summary


def main():
    """Main analysis function."""
    vault_root = Path(__file__).parent.parent.resolve()
    markdown_files = find_markdown_files(vault_root)

    print(f"Found {len(markdown_files)} markdown files to analyze\n")

    # Analyze all notes
    results = {}
    for file_path in markdown_files:
        result = analyze_note(file_path, vault_root)
        results[result['path']] = result

    # Generate summary
    summary = generate_summary(results)

    # Create output
    output = {
        'summary': summary,
        'notes': results
    }

    # Write JSON output
    output_path = vault_root / 'METADATA_ANALYSIS.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n=== METADATA ANALYSIS SUMMARY ===\n")
    print(f"Total Notes: {summary['totalNotes']}")
    print(f"Average Score: {summary['averageScore']}/100")
    print(f"Missing Frontmatter: {summary['missingFrontmatter']}")
    print(f"\nScore Distribution:")
    print(f"  Excellent (90-100): {summary['scoreDistribution']['excellent']}")
    print(f"  Good (70-89): {summary['scoreDistribution']['good']}")
    print(f"  Fair (50-69): {summary['scoreDistribution']['fair']}")
    print(f"  Poor (0-49): {summary['scoreDistribution']['poor']}")
    print(f"\nType Distribution:")
    for note_type, count in sorted(summary['typeDistribution'].items()):
        print(f"  {note_type}: {count}")

    print(f"\nDetailed results written to: {output_path}")


if __name__ == '__main__':
    main()
