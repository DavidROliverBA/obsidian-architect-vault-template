# Metadata Completeness Analysis

## Overview

This document describes the metadata analysis tools available for assessing the completeness and quality of frontmatter metadata across all notes in your Obsidian vault.

## Tools

### 1. Python Analysis Script

**Location:** `scripts/analyze_metadata.py`

**Purpose:** Analyzes all markdown files in the vault and generates a comprehensive JSON report with metadata scores.

**Usage:**
```bash
python3 scripts/analyze_metadata.py
```

**Output:** `METADATA_ANALYSIS.json` - Structured data with scores and details for each note

### 2. Node.js Analysis Script

**Location:** `scripts/analyze_metadata.js`

**Purpose:** Alternative JavaScript implementation for environments with Node.js available.

**Usage:**
```bash
node scripts/analyze_metadata.js
```

**Output:** `METADATA_ANALYSIS.json` - Same format as Python script

### 3. Report Generator

**Location:** `scripts/generate_metadata_report.py`

**Purpose:** Converts the JSON analysis into a human-readable markdown report.

**Usage:**
```bash
# First run the analysis
python3 scripts/analyze_metadata.py

# Then generate the report
python3 scripts/generate_metadata_report.py
```

**Output:** `METADATA_ANALYSIS.md` - Human-readable report with recommendations

## Metadata Scoring System

Each note receives a score from 0-100 based on metadata completeness:

### Required Fields (60 points)

**Universal (all notes):**
- `type` - Note type (required)
- `title` - Display title (required)
- `created` - Creation date (required)

**Type-Specific Required Fields:**

| Type | Required Fields |
|------|----------------|
| Task | `completed`, `priority` |
| Project | `status`, `priority` |
| Adr | `status`, `relatedTo`, `supersedes`, `dependsOn` |
| Meeting | `date` |
| Person | `role` |
| Weblink | `url`, `domain` |
| DailyNote | `date` |
| Page | (none beyond universal) |
| Organisation | (none beyond universal) |

### Quality Fields (30 points)

Each field worth 10 points:
- `tags` - Categorization tags (improves discoverability)
- `description` - Brief summary (improves search context)
- `modified` - Last modified date (tracks freshness)

### ADR Quality Indicators (10 points)

For ADR notes only, 3.33 points each:
- `confidence` - Decision confidence level (high/medium/low)
- `freshness` - Currency status (current/stale)
- `source` - Information source (primary/secondary/tertiary)

## Score Interpretation

| Score Range | Quality Level | Meaning |
|-------------|---------------|---------|
| 90-100 | Excellent | Complete metadata with quality indicators |
| 70-89 | Good | Has required fields and some quality fields |
| 50-69 | Fair | Basic requirements met, missing quality fields |
| 0-49 | Poor | Missing critical required fields |

## Example Analysis Output

### JSON Structure

```json
{
  "summary": {
    "totalNotes": 50,
    "averageScore": 82,
    "scoreDistribution": {
      "excellent": 15,
      "good": 25,
      "fair": 8,
      "poor": 2
    },
    "typeDistribution": {
      "Project": 4,
      "Task": 3,
      "Adr": 3,
      "Person": 3,
      "Meeting": 2
    },
    "missingFrontmatter": 0
  },
  "notes": {
    "Jane Smith.md": {
      "metadataScore": 90,
      "type": "Person",
      "requiredFields": ["type", "title", "created", "role"],
      "missingRequired": [],
      "hasDescription": false,
      "hasTags": true,
      "hasModified": true,
      "qualityIndicators": 2
    },
    "ADR - Use Kubernetes.md": {
      "metadataScore": 100,
      "type": "Adr",
      "requiredFields": ["type", "title", "created", "status", "relatedTo", "supersedes", "dependsOn"],
      "missingRequired": [],
      "hasDescription": true,
      "hasTags": true,
      "hasModified": true,
      "qualityIndicators": 3,
      "adrQualityIndicators": 3
    }
  }
}
```

## Common Issues and Fixes

### Issue 1: Missing Frontmatter
**Problem:** Note has no YAML frontmatter block
**Fix:** Add basic frontmatter:
```yaml
---
type: <note-type>
title: <note-title>
created: YYYY-MM-DD
---
```

### Issue 2: Missing Required Fields
**Problem:** Note lacks type-specific required fields
**Fix:** Check requirements for the note type and add missing fields

**Example - Task missing fields:**
```yaml
---
type: Task
title: Review ADR
created: 2026-01-01
completed: false  # ADD THIS
priority: high     # ADD THIS
---
```

### Issue 3: Low Quality Score
**Problem:** Has required fields but missing quality indicators
**Fix:** Add tags, description, and modified date:
```yaml
---
type: Page
title: Architecture Principles
created: 2025-07-01
tags: [architecture, standards]     # ADD THIS
description: Core principles        # ADD THIS
modified: 2026-01-07                # ADD THIS
---
```

### Issue 4: ADR Missing Quality Indicators
**Problem:** ADR note missing confidence/freshness/source
**Fix:** Add ADR quality fields:
```yaml
---
type: Adr
title: Standardize on PostgreSQL
status: accepted
relatedTo: []
supersedes: []
dependsOn: []
confidence: high     # ADD THIS
freshness: current   # ADD THIS
source: primary      # ADD THIS
---
```

## Automation Opportunities

### 1. Git Pre-commit Hook
Validate metadata before committing:
```bash
#!/bin/bash
# .git/hooks/pre-commit
python3 scripts/analyze_metadata.py
# Fail commit if average score < 70
```

### 2. CI/CD Integration
Add to GitHub Actions workflow:
```yaml
- name: Check Metadata Quality
  run: |
    python3 scripts/analyze_metadata.py
    python3 scripts/validate_scores.py --min-score 70
```

### 3. Weekly Reports
Schedule automated analysis:
```bash
# crontab entry
0 9 * * 1 cd /path/to/vault && python3 scripts/analyze_metadata.py
```

## Best Practices

### When Creating New Notes

1. **Always use templates** - Templates ensure required fields are present
2. **Fill in metadata immediately** - Don't leave placeholders
3. **Add tags thoughtfully** - Use consistent taxonomy
4. **Write clear descriptions** - Brief, searchable summaries
5. **Set created date** - Use ISO format (YYYY-MM-DD)

### When Updating Existing Notes

1. **Update modified date** - Keep freshness current
2. **Review tags** - Add/remove as context evolves
3. **Enhance descriptions** - Improve searchability
4. **Complete missing fields** - Fix validation issues

### For ADRs Specifically

1. **Set confidence level** - high/medium/low based on evidence
2. **Track freshness** - current/stale based on review cadence
3. **Document source** - primary (first-hand) vs secondary
4. **Link relationships** - relatedTo, supersedes, dependsOn
5. **Review quarterly** - Update freshness and confidence

## Integration with Vault Quality Dashboard

The metadata analysis feeds into the main quality dashboard:

**Location:** `MOC - Vault Quality Dashboard.md`

**Features:**
- Real-time metadata scores via Dataview queries
- Notes requiring attention (low scores, missing fields)
- Quality trends over time
- Type-specific breakdowns

## Maintenance

### Regular Tasks

- **Weekly:** Review notes with scores < 70
- **Monthly:** Run full analysis and generate report
- **Quarterly:** Review and update scoring criteria
- **Annually:** Audit type-specific required fields

### Continuous Improvement

1. Monitor average vault score
2. Set targets (e.g., maintain average > 80)
3. Address systematic issues (common missing fields)
4. Update templates to prevent future issues
5. Train team on metadata best practices

## Technical Details

### Excluded from Analysis

**Directories:**
- `.obsidian` - Obsidian configuration
- `node_modules` - NPM dependencies
- `.git` - Git repository data
- `.claude` - Claude Code configuration
- `+Templates` - Note templates
- `scripts` - Utility scripts
- `screenshots` - Documentation images

**Files:**
- `README.md` - Repository documentation
- `CHANGELOG.md` - Version history
- `CONTRIBUTING.md` - Contribution guidelines
- Other documentation files

### Field Validation Rules

A field is considered "present" if:
- Not `null`
- Not empty string (`""`)
- Not empty array (`[]`)
- Has actual content

A field is considered "missing" if:
- Undefined in frontmatter
- Set to `null`
- Empty string or whitespace-only
- Empty array

## Support and Troubleshooting

### Common Errors

**"No frontmatter found"**
- Ensure frontmatter is between `---` markers
- Check YAML syntax is valid
- Verify frontmatter at start of file

**"Failed to read file"**
- Check file permissions
- Verify file encoding (should be UTF-8)
- Ensure file exists and is accessible

**"Invalid YAML"**
- Validate YAML syntax
- Check for special characters in values
- Ensure proper quoting of strings with colons

### Getting Help

1. Check this documentation first
2. Review example notes with high scores
3. Examine templates for correct structure
4. Run analysis in verbose mode for details

## Future Enhancements

Potential improvements:
- Web dashboard for interactive exploration
- Historical trending (track scores over time)
- Automated field suggestions based on content
- Integration with Obsidian Publish validation
- Custom scoring rules per vault
- Field value validation (e.g., date formats)

---

**Last Updated:** 2026-01-09
**Maintained By:** Vault Administrator
**Questions:** See main README or contact support
