# Vault Freshness & Tag Quality Analysis

**Analysis Date:** 2026-01-09
**Total Notes Analyzed:** 54
**Average Freshness Score:** 84.81/100

---

## Executive Summary

The vault is in **excellent health** with:
- **No stale notes** requiring immediate attention
- **87% freshness rate** (47/54 notes are fresh)
- **68.5% of notes properly tagged** (37/54 notes have tags)
- Strong recent activity across all note types

### Recommendations
1. **Add tags to 17 untagged notes** (primarily templates and documentation files)
2. **Monitor 3 recent notes** that may become stale in next 30-60 days
3. Consider establishing tag governance for template files

---

## Distribution by Note Type

| Type | Count | Percentage |
|------|-------|------------|
| Unknown (Documentation/Markdown) | 17 | 31.5% |
| MOC (Maps of Content) | 12 | 22.2% |
| Adr (Architecture Decisions) | 4 | 7.4% |
| Page (Documentation) | 4 | 7.4% |
| Project | 4 | 7.4% |
| Task | 3 | 5.6% |
| Person | 3 | 5.6% |
| Weblink | 2 | 3.7% |
| Organisation | 2 | 3.7% |
| Meeting | 2 | 3.7% |
| DailyNote | 1 | 1.9% |

---

## Distribution by Freshness Category

| Category | Count | Description |
|----------|-------|-------------|
| **Fresh** | 47 | Recently updated, active content |
| **Recent** | 3 | Updated within acceptable timeframe |
| **Archived** | 3 | Meetings/daily notes (age expected) |
| **Stable** | 1 | ADR or reference content (stable by design) |
| **Stale** | 0 | Needs attention |

---

## Tag Quality Analysis

### Tagging Statistics
- **Notes with tags:** 37 (68.5%)
- **Notes without tags:** 17 (31.5%)

### Optimal Tag Distribution
- **Optimal tagging (2-5 tags):** 33 notes
- **Single tag:** 4 notes
- **Excessive tags (>5):** 0 notes
- **No tags:** 17 notes

### Notes Without Tags (Improvement Opportunities)

These 17 notes would benefit from adding tags:

1. **Documentation Files:**
   - `VAULT_AUTOMATION_SETUP.md`
   - `BLOG_POST.md`
   - `CHANGELOG.md`
   - `VALIDATION_REPORT.md`
   - Various README files

2. **Template Files (11 files):**
   - `+Templates/ADR.md`
   - `+Templates/AtomicNote.md`
   - `+Templates/CodeSnippet.md`
   - `+Templates/Course.md`
   - `+Templates/Daily.md`
   - `+Templates/Meeting.md`
   - `+Templates/Organisation.md`
   - `+Templates/Page.md`
   - `+Templates/Person.md`
   - `+Templates/Project.md`
   - `+Templates/Task.md`
   - `+Templates/Weblink.md`
   - `+Templates/Zettel.md`

3. **Context Files:**
   - `.claude/context/` files (6 files)

---

## Top Performing Notes (Score: 100/100)

The following notes demonstrate excellent freshness and tag quality:

### Architecture Decision Records
- `ADR - Adopt GraphQL for API Layer.md` - 2 days old
- `ADR - Microservices vs Monolith Decision.md` - 2 days old
- `ADR - Standardize on PostgreSQL.md` - 116 days old (fresh for ADR)
- `ADR - Use Kubernetes for Container Orchestration.md` - 71 days old

### Maps of Content (MOCs)
- `MOC - ADRs MOC.md` - 2 days old
- `MOC - Cloud Architecture.md` - 2 days old (6 tags, slightly excessive)
- `MOC - Data Platform.md` - 2 days old
- `MOC - Meetings MOC.md` - 2 days old
- `MOC - Organisations MOC.md` - 2 days old
- `MOC - People MOC.md` - 2 days old
- `MOC - Projects MOC.md` - 2 days old
- `MOC - Tasks MOC.md` - 2 days old
- `MOC - Technology & Architecture MOC.md` - 2 days old
- `MOC - Vault Quality Dashboard.md` - 2 days old
- `MOC - Weblinks MOC.md` - 2 days old

### Projects
- `Project - API Gateway Modernization.md` - 2 days old
- `Project - Cloud Migration.md` - 2 days old
- `Project - Legacy System Decommission.md` - 2 days old
- `Project - Research - Event-Driven Architecture.md` - 2 days old

### People
- `Alex Johnson.md` - 2 days old
- `Dr. Sarah Chen.md` - 2 days old
- `Jane Smith.md` - 2 days old

### Pages
- `Page - Architecture Principles.md` - 2 days old
- `Page - How to Use This Vault.md` - 2 days old
- `Page - Tech Stack Overview.md` - 2 days old
- `Page - Vault Setup Checklist.md` - 2 days old

### Tasks
- `Task - Document API standards.md` - 2 days old
- `Task - Research service mesh options.md` - 2 days old
- `Task - Review GraphQL ADR.md` - 2 days old

### Organisations
- `Organisation - CloudVendor Inc.md` - 2 days old
- `Organisation - Your Company.md` - 2 days old

### Weblinks
- `Weblink - AWS Well-Architected Framework.md` - 2 days old
- `Weblink - Martin Fowler on Microservices.md` - 2 days old

---

## Recent Activity Notes (Score: 60-99)

These notes are recent but could benefit from better tagging:

### Dashboard (Score: 90/100)
- `Dashboard - Dashboard.md` - 2 days old, 6 tags (slightly excessive)

---

## Freshness Scoring Methodology

### Freshness Points (0-60)

Points awarded based on days since last modification:

| Note Type | Fresh | Recent | Aging | Stale |
|-----------|-------|--------|-------|-------|
| **Task** | <7 days (60 pts) | 7-30 days (40 pts) | 30-60 days (20 pts) | >60 days (10 pts) |
| **Project** | <30 days (60 pts) | 30-90 days (40 pts) | 90-180 days (20 pts) | >180 days (10 pts) |
| **Adr** | <180 days (60 pts) | 180-365 days (40 pts) | >365 days (20 pts) | N/A (stable) |
| **Page** | <90 days (60 pts) | 90-180 days (40 pts) | 180-365 days (20 pts) | >365 days (10 pts) |
| **Meeting** | N/A (50 pts baseline - age expected) | | | |
| **DailyNote** | N/A (50 pts baseline - age expected) | | | |
| **Person/Org/Weblink** | <90 days (60 pts) | 90-180 days (40 pts) | >180 days (30 pts) | N/A (stable) |

### Tag Quality Points (0-40)

- **Has tags:** +20 pts
- **Optimal count (2-5 tags):** +20 pts (total: 40 pts)
- **Single tag:** +10 pts (total: 30 pts)
- **Excessive tags (>5):** +10 pts (total: 30 pts)
- **No tags:** 0 pts

### Total Score Calculation

**Total Freshness Score = Freshness Points (0-60) + Tag Points (0-40) = 0-100**

---

## Recommendations for Improvement

### Priority 1: Template Tagging
Add consistent tags to all template files to improve discoverability:

**Suggested tags for templates:**
```yaml
tags:
  - template
  - [type-specific-tag]
```

Example:
- `+Templates/ADR.md` → `tags: [template, adr, architecture]`
- `+Templates/Meeting.md` → `tags: [template, meeting]`
- `+Templates/Project.md` → `tags: [template, project]`

### Priority 2: Documentation File Tagging
Add tags to documentation files:
- `VAULT_AUTOMATION_SETUP.md` → `tags: [documentation, automation, setup]`
- `BLOG_POST.md` → `tags: [documentation, blog, publishing]`
- `CHANGELOG.md` → `tags: [documentation, changelog, history]`
- `VALIDATION_REPORT.md` → `tags: [documentation, validation, quality]`

### Priority 3: Monitor Recent Notes
Keep an eye on these 3 notes that are currently "recent" and may need updates:

1. Notes with 30-90 day age (check in 30 days)
2. Notes with 90-180 day age (check in 60 days)
3. Pages older than 90 days (consider review)

### Priority 4: Establish Tag Governance
Consider creating guidelines for:
- Minimum tag count (recommendation: 2-3 tags per note)
- Maximum tag count (recommendation: 5 tags)
- Tag taxonomy/hierarchy (e.g., `domain/`, `activity/`, `technology/`)
- Required tags by note type

---

## Vault Health Score: A (Excellent)

### Scoring Breakdown
- **Content Freshness:** A+ (87% fresh notes, 0 stale)
- **Tag Coverage:** B+ (68.5% tagged)
- **Tag Quality:** A (optimal distribution)
- **Overall Score:** 84.81/100

### Health Indicators
✅ **No stale notes** requiring immediate attention
✅ **High average freshness score** (84.81/100)
✅ **Strong recent activity** (47 fresh notes)
✅ **Good tag adoption** (37/54 notes tagged)
⚠️ **Some untapped potential** (17 notes could benefit from tags)

---

## Next Steps

1. **Week 1:** Add tags to template files (11 files)
2. **Week 2:** Add tags to documentation files (6 files)
3. **Week 3:** Review and update any notes approaching staleness
4. **Week 4:** Establish tag governance guidelines
5. **Ongoing:** Monitor freshness scores monthly using this analysis

---

*Analysis generated by: `/Users/david.oliver/Documents/GitHub/obsidian-architect-vault-template/scripts/analyze_freshness.py`*
