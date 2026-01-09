# Wiki-Link Connectivity and Density Analysis

**Generated:** 2026-01-09
**Vault:** obsidian-architect-vault-template

---

## Executive Summary

This analysis examines wiki-link connectivity across 45 content notes in the vault, evaluating how well notes are interconnected through bidirectional linking.

### Key Metrics

| Metric | Value |
|--------|-------|
| **Total Notes Analyzed** | 45 |
| **Average Link Density Score** | 48.1 / 100 |
| **Average Outgoing Links** | 10.0 per note |
| **Average Backlinks** | 8.2 per note |
| **Orphaned Notes** | 13 (28.9%) |
| **Hub Notes** | 4 (8.9%) |
| **Total Broken Links** | 82 |

### Health Assessment

**Overall Vault Connectivity: MODERATE (48.1%)**

The vault shows moderate connectivity with good hub-and-spoke structure around key entities (people, projects, dashboard). However, nearly 29% of notes are orphaned (no incoming links), and there are 82 broken links that need attention.

---

## Link Density Scoring Methodology

Each note receives a score from 0-100 based on:

- **Outgoing Links (40 points max)**: Links from the note to others (capped at 5+ links = 40 pts)
- **Backlinks (30 points max)**: Links from other notes to this one (capped at 3+ backlinks = 30 pts)
- **Orphan Penalty (-20 points)**: No incoming links from any note
- **Broken Link Penalty (-10 points)**: Contains links to non-existent notes
- **Hub Bonus (+10 points)**: Top 10% of notes by backlink count

---

## Hub Notes (Knowledge Graph Centers)

These notes serve as central connection points in the knowledge graph:

| Note | Backlinks | Score | Type |
|------|-----------|-------|------|
| **Jane Smith.md** | 39 | 56.0 | Person |
| **Alex Johnson.md** | 32 | 72.0 | Person |
| **Dashboard - Dashboard.md** | 25 | 80.0 | MOC |
| **Project - Cloud Migration.md** | 25 | 64.0 | Project |

### Insights

- **People notes are primary hubs**: Jane Smith and Alex Johnson are referenced across the vault, showing they're key stakeholders
- **Dashboard is the navigation hub**: As expected, the main dashboard serves as a central navigation point
- **Cloud Migration is the main project**: Most referenced project, indicating it's a major initiative

---

## Orphaned Notes (Zero Backlinks)

These 13 notes have no incoming links and may be difficult to discover:

### Critical Orphans (Should Be Linked)

| Note | Outgoing | Score | Issue |
|------|----------|-------|-------|
| **+Daily/2026/2026-01-07.md** | 15 | 20.0 | Daily note with good outgoing links, needs linking from Dashboard/MOCs |
| **+Meetings/Meeting - 2026-01-07 Project Kickoff.md** | 16 | 20.0 | Meeting note, should be linked from project/attendees |
| **+Meetings/Meeting - 2026-01-08 Architecture Review.md** | 16 | 20.0 | Meeting note, should be linked from project/attendees |
| **Task - Research service mesh options.md** | 5 | 10.0 | Active task, should be in Tasks MOC |
| **Project - Research - Event-Driven Architecture.md** | 4 | 12.0 | Research project, should be in Projects MOC |

### Documentation Orphans (Expected)

| Note | Outgoing | Score | Context |
|------|----------|-------|---------|
| **VAULT_AUTOMATION_SETUP.md** | 0 | 0 | Repository documentation |
| **CHANGELOG.md** | 0 | 0 | Repository documentation |
| **CONTRIBUTING.md** | 2 | 0 | Repository documentation |
| **README.md** | 8 | 10.0 | Repository documentation |
| **VALIDATION_REPORT.md** | 1 | 0 | Generated report |
| **BLOG_POST.md** | 17 | 10.0 | Sample content |
| **+Daily/README.md** | 12 | 10.0 | Directory documentation |
| **+Meetings/README.md** | 24 | 10.0 | Directory documentation |

### Recommendations

1. **Link daily notes from Dashboard**: Add recent daily notes section to Dashboard MOC
2. **Link meetings from projects/people**: Ensure meeting notes are linked from attendee Person notes and related Project notes
3. **Add orphan tasks to Tasks MOC**: Include "Research service mesh options" in active tasks query
4. **Link research projects**: Add "Event-Driven Architecture" research to Projects MOC

---

## Broken Links Analysis

**Total Broken Links: 82 across 14 notes**

### High-Priority Fixes

| Note | Broken Links | Examples |
|------|--------------|----------|
| **MOC - Data Platform.md** | 20 | "Page - Data Architecture Overview", "Page - Data Governance Framework" |
| **MOC - Cloud Architecture.md** | 17 | "Page - Cloud Landing Zone Architecture", "Page - Cloud Security Standards" |
| **README.md** | 8 | "Person Name", "Project - Name", "ADR - Related Decision" |
| **+Meetings/README.md** | 7 | "Project - Name", "Person 1", "Task - Draft GraphQL ADR" |
| **+Daily/README.md** | 5 | "Meeting - 2026-01-07 Architecture Review", "Task - Update API documentation" |

### Types of Broken Links

1. **Placeholder links** (37 links): Generic names like "Person Name", "Project - Name", "Note Title"
2. **Missing documentation pages** (37 links): MOCs reference architecture pages that don't exist yet
3. **Incorrect link format** (4 links): Malformed links like `"[[Other ADR"` (missing closing brackets)
4. **Missing meeting** (4 links): "Meeting - 2026-01-07 Architecture Review" referenced but not found

### Recommendations

1. **Create missing Page notes**: Prioritize "Data Architecture Overview", "Cloud Landing Zone Architecture"
2. **Fix placeholder links**: Replace generic "Person Name" with actual person note links
3. **Fix malformed links**: Correct syntax errors in BLOG_POST.md
4. **Update README examples**: Use real note names instead of placeholders

---

## Link Density Distribution

### Excellent Connectivity (70-100 points)

| Note | Score | Out | In | Type |
|------|-------|-----|----|----|
| Dashboard - Dashboard.md | 80.0 | 30 | 25 | MOC |
| Alex Johnson.md | 72.0 | 4 | 32 | Person |
| ADR - Use Kubernetes for Container Orchestration.md | 70.0 | 12 | 14 | ADR |
| ADR - Adopt GraphQL for API Layer.md | 70.0 | 12 | 16 | ADR |
| ADR - Standardize on PostgreSQL.md | 70.0 | 6 | 10 | ADR |
| ADR - Microservices vs Monolith Decision.md | 70.0 | 5 | 5 | ADR |
| Page - Architecture Principles.md | 70.0 | 9 | 13 | Page |
| Page - Tech Stack Overview.md | 70.0 | 10 | 14 | Page |
| MOC - ADRs MOC.md | 70.0 | 8 | 18 | MOC |
| MOC - Projects MOC.md | 70.0 | 11 | 19 | MOC |
| MOC - Tasks MOC.md | 70.0 | 6 | 8 | MOC |
| MOC - Weblinks MOC.md | 70.0 | 7 | 6 | MOC |
| MOC - Vault Quality Dashboard.md | 70.0 | 7 | 8 | MOC |
| Organisation - Your Company.md | 70.0 | 5 | 4 | Organisation |
| Weblink - AWS Well-Architected Framework.md | 70.0 | 5 | 6 | Weblink |
| Task - Review GraphQL ADR.md | 70.0 | 6 | 8 | Task |
| Task - Document API standards.md | 70.0 | 9 | 7 | Task |

**Pattern**: ADRs, MOCs, and well-established architecture pages show excellent connectivity

### Good Connectivity (60-69 points)

| Note | Score | Out | In | Type |
|------|-------|-----|----|----|
| Project - Cloud Migration.md | 64.0 | 3 | 25 | Project |
| Weblink - Martin Fowler on Microservices.md | 62.0 | 4 | 5 | Weblink |
| MOC - People MOC.md | 60.0 | 17 | 9 | MOC |
| MOC - Organisations MOC.md | 60.0 | 9 | 6 | MOC |
| MOC - Meetings MOC.md | 60.0 | 10 | 6 | MOC |
| MOC - Technology & Architecture MOC.md | 60.0 | 27 | 16 | MOC |
| MOC - Cloud Architecture.md | 60.0 | 30 | 7 | MOC |
| MOC - Data Platform.md | 60.0 | 33 | 5 | MOC |
| Page - How to Use This Vault.md | 60.0 | 28 | 3 | Page |
| Page - Vault Setup Checklist.md | 60.0 | 5 | 4 | Page |
| Organisation - CloudVendor Inc.md | 60.0 | 7 | 2 | Organisation |

**Pattern**: MOCs with broken links score 60 (penalty applied), but still well-connected

### Moderate Connectivity (30-59 points)

| Note | Score | Out | In | Type |
|------|-------|-----|----|----|
| Jane Smith.md | 56.0 | 2 | 39 | Person |
| Dr. Sarah Chen.md | 54.0 | 3 | 13 | Person |
| Project - API Gateway Modernization.md | 46.0 | 2 | 13 | Project |
| Project - Legacy System Decommission.md | 30.0 | 0 | 4 | Project |

**Pattern**: Person notes have many backlinks but few outgoing links (expected for contact notes)

### Poor Connectivity (0-29 points)

| Note | Score | Out | In | Type |
|------|-------|-----|----|----|
| +Daily/2026/2026-01-07.md | 20.0 | 15 | 0 | Daily |
| +Meetings/Meeting - 2026-01-07 Project Kickoff.md | 20.0 | 16 | 0 | Meeting |
| +Meetings/Meeting - 2026-01-08 Architecture Review.md | 20.0 | 16 | 0 | Meeting |
| Project - Research - Event-Driven Architecture.md | 12.0 | 4 | 0 | Project |
| BLOG_POST.md | 10.0 | 17 | 0 | Sample |
| Task - Research service mesh options.md | 10.0 | 5 | 0 | Task |
| README.md | 10.0 | 8 | 0 | Documentation |
| +Daily/README.md | 10.0 | 12 | 0 | Documentation |
| +Meetings/README.md | 10.0 | 24 | 0 | Documentation |
| VAULT_AUTOMATION_SETUP.md | 0 | 0 | 0 | Documentation |
| CHANGELOG.md | 0 | 0 | 0 | Documentation |
| CONTRIBUTING.md | 0 | 2 | 0 | Documentation |
| VALIDATION_REPORT.md | 0 | 1 | 0 | Documentation |

**Pattern**: Orphaned notes (daily notes, meetings, documentation) need integration into the knowledge graph

---

## Recommendations by Priority

### Priority 1: Fix Orphaned Content Notes

**Action**: Ensure all daily notes and meeting notes are discoverable

1. **Daily notes**: Add to Dashboard MOC with recent daily notes query
2. **Meeting notes**: Link from attendee Person notes and Project notes
3. **Tasks**: Add "Research service mesh options" to Tasks MOC
4. **Research projects**: Add "Event-Driven Architecture" to Projects MOC

**Expected Impact**: +4 points average score increase for 5 notes

### Priority 2: Create Missing Documentation Pages

**Action**: Create placeholder Page notes referenced by MOCs

1. **Cloud Architecture** (17 broken links): Create infrastructure documentation pages
2. **Data Platform** (20 broken links): Create data governance and architecture pages
3. Use templates to create consistent structure
4. Link back to respective MOCs

**Expected Impact**: -10 penalty removal from 2 MOCs, +20 points total

### Priority 3: Fix Placeholder Links in Documentation

**Action**: Update README and example files with real note links

1. Replace "Person Name" with actual person notes (e.g., "Jane Smith")
2. Replace "Project - Name" with actual projects (e.g., "Project - Cloud Migration")
3. Replace "Task - Name" with actual tasks
4. Update documentation examples to reference real vault content

**Expected Impact**: -10 penalty removal from 5 documentation notes

### Priority 4: Strengthen Hub Connections

**Action**: Increase bidirectional linking for hub notes

1. **Jane Smith** (56.0 score): Add more outgoing links to projects/meetings she's involved in
2. **Dashboard**: Already strong, maintain by keeping queries updated
3. **Project - Cloud Migration**: Continue referencing in related notes

**Expected Impact**: Maintain healthy 70+ scores for hub notes

---

## Vault Connectivity Trends

### Strong Patterns

1. **ADR connectivity is excellent**: All ADRs have 70+ scores with good bidirectional linking
2. **MOC structure is solid**: Most MOCs have 60-70 scores, serving as navigation hubs
3. **People notes are hub centres**: Jane Smith (39 backlinks) and Alex Johnson (32 backlinks) are heavily referenced
4. **Project linking is good**: Main projects (Cloud Migration) are well-connected

### Weak Patterns

1. **Daily notes are orphaned**: Recent daily notes not linked from Dashboard
2. **Meeting notes are orphaned**: Not linked from attendees or projects
3. **Broken link concentration**: 37 broken links in two MOCs (Cloud Architecture, Data Platform)
4. **Documentation isolation**: README files contain many placeholders instead of real links

---

## Next Steps

1. **Run broken links fix**: Use `/broken-links` skill to systematically fix 82 broken links
2. **Update Dashboard**: Add recent daily notes and recent meetings sections
3. **Link meetings from people**: Add meetings to Person note "Recent Meetings" sections
4. **Create missing pages**: Prioritize Cloud and Data Platform documentation pages
5. **Monthly review**: Re-run this analysis monthly to track connectivity improvements

---

## Technical Details

### Analysis Scope

- **Files analyzed**: 45 markdown files
- **Excluded directories**: `.git`, `.obsidian`, `node_modules`, `.claude`, `scripts`, `+Templates`
- **Link extraction**: Standard Obsidian `[[wiki-link]]` syntax
- **Broken link detection**: Links to notes that don't exist in the vault

### Link Density Calculation

```
Score = 0-100 (constrained)

Components:
+ min(outgoing_links / 5, 1) * 40     # Max 40 points for 5+ outgoing links
+ min(backlinks / 3, 1) * 30           # Max 30 points for 3+ backlinks
- 20 if is_orphaned                    # Penalty for zero backlinks
- 10 if has_broken_links               # Penalty for any broken links
+ 10 if is_hub                         # Bonus for top 10% by backlinks
```

### Hub Note Threshold

Hub notes are the top 10% of notes by backlink count. For 45 notes, this is the top 4-5 notes.

Threshold: 25+ backlinks

---

## Appendix: Full Note Listing by Score

See `/Users/david.oliver/Documents/GitHub/obsidian-architect-vault-template/link_analysis.json` for complete data including:

- Individual note metrics (outgoing links, backlinks, broken links)
- Word counts and link density percentages
- Full broken link lists by note
- Detailed orphaned note analysis

---

**Generated by**: Claude Code wiki-link analysis script
**Data file**: `link_analysis.json`
**Script**: `analyze_links.py`
