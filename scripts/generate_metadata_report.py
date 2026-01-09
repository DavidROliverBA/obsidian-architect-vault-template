#!/usr/bin/env python3
"""
Generate a human-readable markdown report from metadata analysis results.
"""

import json
from pathlib import Path
from collections import defaultdict
from datetime import datetime


def load_analysis_data(vault_root: Path) -> dict:
    """Load the JSON analysis data."""
    analysis_file = vault_root / 'METADATA_ANALYSIS.json'
    with open(analysis_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def generate_report(data: dict) -> str:
    """Generate markdown report from analysis data."""
    summary = data['summary']
    notes = data['notes']

    report = []
    report.append("# Metadata Completeness Analysis Report")
    report.append(f"\n**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"\n---\n")

    # Executive Summary
    report.append("## Executive Summary\n")
    report.append(f"- **Total Notes Analyzed:** {summary['totalNotes']}")
    report.append(f"- **Average Metadata Score:** {summary['averageScore']}/100")
    report.append(f"- **Notes Missing Frontmatter:** {summary['missingFrontmatter']}")
    report.append("")

    # Score Distribution
    report.append("### Score Distribution\n")
    dist = summary['scoreDistribution']
    total = sum(dist.values())
    if total > 0:
        report.append(f"- **Excellent (90-100):** {dist['excellent']} ({dist['excellent']/total*100:.1f}%)")
        report.append(f"- **Good (70-89):** {dist['good']} ({dist['good']/total*100:.1f}%)")
        report.append(f"- **Fair (50-69):** {dist['fair']} ({dist['fair']/total*100:.1f}%)")
        report.append(f"- **Poor (0-49):** {dist['poor']} ({dist['poor']/total*100:.1f}%)")
    report.append("")

    # Type Distribution
    report.append("### Note Type Distribution\n")
    type_dist = summary['typeDistribution']
    for note_type, count in sorted(type_dist.items(), key=lambda x: x[1], reverse=True):
        report.append(f"- **{note_type}:** {count}")
    report.append("\n---\n")

    # Notes with Issues
    report.append("## Notes Requiring Attention\n")

    # Missing frontmatter
    missing_fm = [n for n in notes.values() if 'error' in n and 'No frontmatter' in n.get('error', '')]
    if missing_fm:
        report.append(f"### Missing Frontmatter ({len(missing_fm)} notes)\n")
        for note in sorted(missing_fm, key=lambda x: x['path']):
            report.append(f"- `{note['path']}`")
        report.append("")

    # Low scores (< 50)
    low_scores = [n for n in notes.values() if 'error' not in n and n['metadataScore'] < 50]
    if low_scores:
        report.append(f"### Low Metadata Scores (<50) - {len(low_scores)} notes\n")
        for note in sorted(low_scores, key=lambda x: x['metadataScore']):
            missing = ', '.join(note['missingRequired'])
            report.append(f"- **{note['path']}** (Score: {note['metadataScore']}/100)")
            if note['missingRequired']:
                report.append(f"  - Missing: {missing}")
        report.append("")

    # Missing required fields by type
    report.append("### Missing Required Fields by Type\n")
    by_type = defaultdict(lambda: defaultdict(list))

    for note in notes.values():
        if 'error' not in note and note['missingRequired']:
            note_type = note['type'] or 'unknown'
            for field in note['missingRequired']:
                by_type[note_type][field].append(note['path'])

    for note_type in sorted(by_type.keys()):
        report.append(f"\n#### {note_type}\n")
        for field, paths in sorted(by_type[note_type].items()):
            report.append(f"**Missing `{field}` ({len(paths)} notes):**")
            for path in sorted(paths)[:5]:  # Show first 5
                report.append(f"- `{path}`")
            if len(paths) > 5:
                report.append(f"- ...and {len(paths) - 5} more")
            report.append("")

    report.append("---\n")

    # Quality indicators
    report.append("## Quality Indicators\n")

    # Notes missing quality fields
    missing_tags = [n for n in notes.values() if 'error' not in n and not n.get('hasTags', False)]
    missing_description = [n for n in notes.values() if 'error' not in n and not n.get('hasDescription', False)]
    missing_modified = [n for n in notes.values() if 'error' not in n and not n.get('hasModified', False)]

    report.append(f"- **Notes Missing Tags:** {len(missing_tags)}")
    report.append(f"- **Notes Missing Description:** {len(missing_description)}")
    report.append(f"- **Notes Missing Modified Date:** {len(missing_modified)}")
    report.append("")

    # ADR quality
    adr_notes = [n for n in notes.values() if n.get('type') == 'Adr']
    if adr_notes:
        report.append("### ADR Quality Indicators\n")
        adr_with_confidence = len([n for n in adr_notes if n.get('adrQualityIndicators', 0) >= 3])
        report.append(f"- **ADRs with All Quality Indicators (confidence, freshness, source):** {adr_with_confidence}/{len(adr_notes)}")
        report.append("")

    report.append("---\n")

    # Top performers
    report.append("## Top Performing Notes\n")
    top_notes = sorted(
        [n for n in notes.values() if 'error' not in n],
        key=lambda x: x['metadataScore'],
        reverse=True
    )[:10]

    for note in top_notes:
        report.append(f"- **{note['path']}** - Score: {note['metadataScore']}/100 (Type: {note['type']})")
    report.append("")

    report.append("---\n")

    # Recommendations
    report.append("## Recommendations\n")

    if missing_fm:
        report.append(f"1. **Add Frontmatter:** {len(missing_fm)} notes are missing YAML frontmatter. Add basic frontmatter with `type`, `title`, and `created` fields.")

    if len(low_scores) > 0:
        report.append(f"2. **Improve Low Scores:** {len(low_scores)} notes have scores below 50. Focus on adding missing required fields.")

    if len(missing_tags) > len(notes) * 0.3:
        report.append(f"3. **Add Tags:** {len(missing_tags)} notes are missing tags. Tags improve discoverability and organization.")

    if len(missing_description) > len(notes) * 0.5:
        report.append(f"4. **Add Descriptions:** {len(missing_description)} notes lack descriptions. Brief descriptions improve search and context.")

    if len(missing_modified) > len(notes) * 0.3:
        report.append(f"5. **Update Modified Dates:** {len(missing_modified)} notes are missing `modified` dates. Keep these current for freshness tracking.")

    if adr_notes and adr_with_confidence < len(adr_notes) * 0.7:
        report.append(f"6. **Enhance ADR Quality:** Only {adr_with_confidence}/{len(adr_notes)} ADRs have quality indicators. Add `confidence`, `freshness`, and `source` fields.")

    report.append("")
    report.append("---\n")

    # Scoring methodology
    report.append("## Scoring Methodology\n")
    report.append("\nMetadata scores are calculated as follows:\n")
    report.append("- **Required Fields (60 points):** Proportional based on presence of required fields")
    report.append("  - Universal: `type`, `title`, `created`")
    report.append("  - Type-specific: varies by note type (e.g., Task requires `completed`, `priority`)")
    report.append("- **Quality Fields (30 points):** 10 points each for `tags`, `description`, `modified`")
    report.append("- **ADR Quality Indicators (10 points):** 3.33 points each for `confidence`, `freshness`, `source`")
    report.append("\n**Total Possible:** 100 points\n")

    return '\n'.join(report)


def main():
    """Generate and save the markdown report."""
    vault_root = Path(__file__).parent.parent.resolve()

    # Load analysis data
    data = load_analysis_data(vault_root)

    # Generate report
    report = generate_report(data)

    # Save report
    output_path = vault_root / 'METADATA_ANALYSIS.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Markdown report generated: {output_path}")


if __name__ == '__main__':
    main()
