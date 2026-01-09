#!/usr/bin/env python3
"""
Comprehensive structure analysis for Obsidian vault notes.
Analyzes content sections based on note type requirements.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
import yaml


class StructureAnalyzer:
    """Analyzes note structure completeness based on type."""

    # Expected sections by type
    SECTION_REQUIREMENTS = {
        'Adr': {
            'required': ['Context', 'Decision', 'Rationale', 'Consequences'],
            'optional': ['Alternatives Considered', 'Alternatives', 'Status', 'Related Decisions',
                        'Compliance', 'Production Implementation', 'Risks and Mitigations'],
            'points_per_section': 25
        },
        'Meeting': {
            'recommended': ['Agenda', 'Discussion', 'Action Items'],
            'alternatives': {
                'Discussion': ['Discussion', 'Notes', 'Discussion Notes', 'Summary'],
                'Action Items': ['Action Items', 'Actions', 'Next Steps', 'Follow-up', 'Follow-up']
            },
            'points_per_section': 33
        },
        'Project': {
            'recommended': ['Overview', 'Status', 'Timeline'],
            'alternatives': {
                'Overview': ['Overview', 'Summary', 'Description', 'Problem Statement'],
                'Status': ['Status', 'Progress', 'Current State', 'Current Focus'],
                'Timeline': ['Timeline', 'Milestones', 'Schedule', 'Key Dates']
            },
            'points_per_section': 33
        }
    }

    # Directories to skip
    SKIP_DIRS = {
        'node_modules', '.git', '.obsidian', '.claude', '.smart-env',
        'PDFs', 'screenshots'
    }

    # Files to skip
    SKIP_FILES = {
        'README.md', 'CHANGELOG.md', 'CONTRIBUTING.md', 'VALIDATION_REPORT.md',
        'BLOG_POST.md', 'VAULT_AUTOMATION_SETUP.md'
    }

    def __init__(self, vault_path: str):
        self.vault_path = Path(vault_path)
        self.results = {
            'notes': {},
            'summary': {
                'total': 0,
                'analyzed': 0,
                'perfect': 0,
                'needsImprovement': 0,
                'byType': {}
            }
        }

    def should_skip(self, file_path: Path) -> bool:
        """Check if file should be skipped."""
        # Check if in template directory
        if '+Templates' in file_path.parts:
            return True

        # Check if in skip directories
        for skip_dir in self.SKIP_DIRS:
            if skip_dir in file_path.parts:
                return True

        # Check if skip file
        if file_path.name in self.SKIP_FILES:
            return True

        # Check if in context or skills directories
        relative = file_path.relative_to(self.vault_path)
        if '.claude/context' in str(relative) or '.claude/skills' in str(relative):
            return True

        return False

    def extract_frontmatter(self, content: str) -> Optional[Dict]:
        """Extract and parse YAML frontmatter."""
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            return None

        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None

    def extract_headings(self, content: str) -> List[str]:
        """Extract all level 1 and 2 headings."""
        # Remove frontmatter first
        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

        # Extract headings (# or ##)
        headings = []
        for match in re.finditer(r'^#{1,2}\s+(.+)$', content, re.MULTILINE):
            headings.append(match.group(1).strip())

        return headings

    def normalize_section(self, section: str) -> str:
        """Normalize section name for comparison."""
        # Remove special characters and convert to lowercase
        normalized = re.sub(r'[^\w\s]', '', section.lower()).strip()
        return normalized

    def check_section_match(self, heading: str, expected_sections: List[str]) -> Optional[str]:
        """Check if heading matches any expected section."""
        normalized_heading = self.normalize_section(heading)

        for expected in expected_sections:
            normalized_expected = self.normalize_section(expected)
            if normalized_heading == normalized_expected or normalized_expected in normalized_heading:
                return expected

        return None

    def analyze_adr(self, headings: List[str]) -> Tuple[int, List[str], List[str]]:
        """Analyze ADR structure."""
        requirements = self.SECTION_REQUIREMENTS['Adr']
        expected = requirements['required']
        present = []
        missing = []

        for section in expected:
            found = False
            for heading in headings:
                if self.check_section_match(heading, [section]):
                    present.append(section)
                    found = True
                    break

            if not found:
                missing.append(section)

        score = round((len(present) / len(expected)) * 100) if expected else 100
        return score, present, missing

    def analyze_meeting(self, headings: List[str]) -> Tuple[int, List[str], List[str]]:
        """Analyze Meeting structure."""
        requirements = self.SECTION_REQUIREMENTS['Meeting']
        expected = requirements['recommended']
        alternatives = requirements['alternatives']
        present = []
        missing = []

        for section in expected:
            found = False
            alt_sections = alternatives.get(section, [section])

            for heading in headings:
                if self.check_section_match(heading, alt_sections):
                    present.append(section)
                    found = True
                    break

            if not found:
                missing.append(section)

        score = round((len(present) / len(expected)) * 100) if expected else 100
        return score, present, missing

    def analyze_project(self, headings: List[str]) -> Tuple[int, List[str], List[str]]:
        """Analyze Project structure."""
        requirements = self.SECTION_REQUIREMENTS['Project']
        expected = requirements['recommended']
        alternatives = requirements['alternatives']
        present = []
        missing = []

        for section in expected:
            found = False
            alt_sections = alternatives.get(section, [section])

            for heading in headings:
                if self.check_section_match(heading, alt_sections):
                    present.append(section)
                    found = True
                    break

            if not found:
                missing.append(section)

        score = round((len(present) / len(expected)) * 100) if expected else 100
        return score, present, missing

    def analyze_note(self, file_path: Path) -> Optional[Dict]:
        """Analyze a single note file."""
        try:
            content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {file_path}: {e}", file=sys.stderr)
            return None

        frontmatter = self.extract_frontmatter(content)
        if not frontmatter or 'type' not in frontmatter:
            return None

        note_type = frontmatter['type']
        headings = self.extract_headings(content)

        # Analyze based on type
        if note_type == 'Adr':
            score, present, missing = self.analyze_adr(headings)
            return {
                'structureScore': score,
                'type': note_type,
                'expectedSections': self.SECTION_REQUIREMENTS['Adr']['required'],
                'presentSections': present,
                'missingSections': missing,
                'hasStructureRequirements': True,
                'requirementType': 'required'
            }

        elif note_type == 'Meeting':
            score, present, missing = self.analyze_meeting(headings)
            return {
                'structureScore': score,
                'type': note_type,
                'expectedSections': self.SECTION_REQUIREMENTS['Meeting']['recommended'],
                'presentSections': present,
                'missingSections': missing,
                'hasStructureRequirements': True,
                'requirementType': 'recommended'
            }

        elif note_type == 'Project':
            score, present, missing = self.analyze_project(headings)
            return {
                'structureScore': score,
                'type': note_type,
                'expectedSections': self.SECTION_REQUIREMENTS['Project']['recommended'],
                'presentSections': present,
                'missingSections': missing,
                'hasStructureRequirements': True,
                'requirementType': 'recommended'
            }

        else:
            # No structure requirements for other types
            return {
                'structureScore': 100,
                'type': note_type,
                'expectedSections': [],
                'presentSections': [],
                'missingSections': [],
                'hasStructureRequirements': False
            }

    def analyze_vault(self) -> Dict:
        """Analyze all markdown files in vault."""
        md_files = self.vault_path.rglob('*.md')

        for file_path in md_files:
            if self.should_skip(file_path):
                continue

            self.results['summary']['total'] += 1

            analysis = self.analyze_note(file_path)
            if analysis:
                relative_path = str(file_path.relative_to(self.vault_path))
                self.results['notes'][relative_path] = analysis
                self.results['summary']['analyzed'] += 1

                # Track by type
                note_type = analysis['type']
                if note_type not in self.results['summary']['byType']:
                    self.results['summary']['byType'][note_type] = {
                        'count': 0,
                        'avgScore': 0,
                        'perfect': 0,
                        'needsImprovement': 0,
                        'scores': []
                    }

                type_stats = self.results['summary']['byType'][note_type]
                type_stats['count'] += 1
                type_stats['scores'].append(analysis['structureScore'])

                if analysis['structureScore'] == 100:
                    self.results['summary']['perfect'] += 1
                    type_stats['perfect'] += 1
                elif analysis['structureScore'] < 100 and analysis['hasStructureRequirements']:
                    self.results['summary']['needsImprovement'] += 1
                    type_stats['needsImprovement'] += 1

        # Calculate average scores
        for note_type, stats in self.results['summary']['byType'].items():
            if stats['scores']:
                stats['avgScore'] = round(sum(stats['scores']) / len(stats['scores']))
                del stats['scores']  # Remove raw scores from output

        return self.results


def main():
    """Main entry point."""
    vault_path = sys.argv[1] if len(sys.argv) > 1 else '/Users/david.oliver/Documents/GitHub/obsidian-architect-vault-template'

    analyzer = StructureAnalyzer(vault_path)
    results = analyzer.analyze_vault()

    print(json.dumps(results, indent=2))


if __name__ == '__main__':
    main()
