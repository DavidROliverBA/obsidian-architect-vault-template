---
type: MOC
title: Vault Quality Dashboard
created: 2026-01-07
modified: 2026-01-07
tags: [moc, quality, maintenance, health]
aliases: [Quality Dashboard, Vault Health]
---

# 📊 Vault Quality Dashboard

> **Monitor vault health and content quality**

Last Updated: 2026-01-07

---

## Overview

This dashboard provides quality metrics, identifies maintenance needs, and tracks vault health over time. Use this weekly to keep your knowledge base clean and valuable.

**Quick Links:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Tasks MOC]] - Tasks needing attention
- [[MOC - Projects MOC]] - Project health

---

## 🎯 Quick Health Summary

### Vault Statistics

```dataview
TABLE WITHOUT ID
  type as "Note Type",
  length(rows) as "Count"
FROM ""
WHERE type != null
GROUP BY type
SORT length(rows) DESC
```

**Total Notes:** Use vault-wide search or count above rows

### Recent Activity (Last 7 Days)

```dataview
TABLE WITHOUT ID
  type as "Type",
  length(rows) as "Created",
  list(rows.file.link, 5) as "Recent Notes"
FROM ""
WHERE created >= date(today) - dur(7 days)
GROUP BY type
SORT length(rows) DESC
```

### Content Freshness

```dataview
TABLE WITHOUT ID
  dateformat(modified, "yyyy-MM") as "Month",
  length(rows) as "Notes Updated"
FROM ""
WHERE modified >= date(today) - dur(180 days)
GROUP BY dateformat(modified, "yyyy-MM")
SORT dateformat(modified, "yyyy-MM") DESC
```

---

## ⚠️ Critical Issues

### Broken Links

**Notes with potential broken links:**
```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  length(file.outlinks) as "Outbound Links"
FROM ""
WHERE length(file.outlinks) > 0
  AND any(map(file.outlinks, (link) =>
    !link.path OR link.path = ""
  ))
SORT file.name ASC
LIMIT 20
```

**Action:** Use `/broken-links` skill for comprehensive analysis.

### Notes Without Type

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  created as "Created",
  modified as "Modified"
FROM ""
WHERE (type = null OR type = "")
  AND !contains(file.path, "+Templates")
  AND !contains(file.path, ".obsidian")
SORT modified DESC
```

**Action:** Add `type` field to frontmatter for proper organization.

### Orphaned Notes (No Backlinks)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  created as "Created"
FROM ""
WHERE length(file.inlinks) = 0
  AND type != "MOC"
  AND type != "DailyNote"
  AND !contains(file.path, "+Templates")
SORT created DESC
LIMIT 15
```

**Action:** Use `/orphans` skill for full analysis. Link from relevant notes or archive.

---

## 📋 Metadata Quality

### ADRs Without Required Fields

**Missing Status:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  created as "Created"
FROM ""
WHERE type = "Adr"
  AND (status = null OR status = "")
SORT created DESC
```

**Missing Category:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  created as "Created"
FROM ""
WHERE type = "Adr"
  AND (category = null OR category = "")
SORT created DESC
```

**Missing Confidence:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  created as "Created"
FROM ""
WHERE type = "Adr"
  AND (confidence = null OR confidence = "")
SORT created DESC
```

**Action:** Update ADRs with required metadata for quality tracking.

### Projects Without Status

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  priority as "Priority",
  created as "Created"
FROM ""
WHERE type = "Project"
  AND (status = null OR status = "")
SORT created DESC
```

**Action:** Set project status (active/paused/completed).

### Tasks Without Priority

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  due as "Due"
FROM ""
WHERE type = "Task"
  AND (priority = null OR priority = "")
SORT due ASC
LIMIT 15
```

**Action:** Assign priority (high/medium/low) for better triage.

### People Without Roles

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  organisation as "Organization"
FROM ""
WHERE type = "Person"
  AND (role = null OR role = "")
SORT file.name ASC
```

**Action:** Add role/title for context.

### Meetings Without Summaries

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (summary = null OR summary = "")
  AND date >= date(today) - dur(60 days)
SORT date DESC
LIMIT 10
```

**Action:** Add one-line summaries for quick reference.

---

## 🕒 Stale Content

### ADRs Not Reviewed in 12+ Months

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  reviewed as "Last Reviewed",
  round((date(today) - reviewed).days / 30, 0) + " months ago" as "Age"
FROM ""
WHERE type = "Adr"
  AND status = "accepted"
  AND (reviewed = null OR reviewed < date(today) - dur(365 days))
SORT reviewed ASC
LIMIT 10
```

**Action:** Review and update `reviewed` date. Consider if decision is still valid.

### Active Projects Not Updated in 30+ Days

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  modified as "Last Updated",
  round((date(today) - modified).days, 0) + " days ago" as "Age"
FROM ""
WHERE type = "Project"
  AND status = "active"
  AND modified < date(today) - dur(30 days)
SORT modified ASC
LIMIT 10
```

**Action:** Update project status or mark as paused/completed.

### Old Open Tasks (60+ Days)

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  created as "Created",
  round((date(today) - created).days, 0) + " days old" as "Age"
FROM ""
WHERE type = "Task"
  AND !completed
  AND created < date(today) - dur(60 days)
SORT created ASC
LIMIT 15
```

**Action:** Complete, re-prioritize, or close if no longer relevant.

### People Without Recent Contact (90+ Days)

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  role as "Role",
  organisation as "Organization",
  modified as "Last Update"
FROM ""
WHERE type = "Person"
  AND modified < date(today) - dur(90 days)
SORT modified ASC
LIMIT 10
```

**Action:** Reach out for relationship maintenance or archive if inactive.

---

## 📊 Quality Indicators

### Low Confidence ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  verified as "Verified"
FROM ""
WHERE type = "Adr"
  AND confidence = "low"
SORT status ASC, modified DESC
```

**Monitor:** These decisions may need revisiting as you learn more.

### Unverified High-Impact ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  confidence as "Confidence",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
  AND status = "accepted"
  AND (verified = null OR verified = false)
SORT modified DESC
```

**Action:** Validate decisions in production and update `verified` field.

### High Priority Tasks Without Due Dates

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  project as "Project",
  created as "Created"
FROM ""
WHERE type = "Task"
  AND !completed
  AND priority = "high"
  AND (due = null OR due = "")
SORT created ASC
```

**Action:** Set realistic due dates for tracking.

---

## 🔗 Link Health

### Most Linked Notes (Hub Content)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  length(file.inlinks) as "Backlinks"
FROM ""
WHERE length(file.inlinks) > 0
SORT length(file.inlinks) DESC
LIMIT 15
```

**Hub Notes:** Most referenced content - ensure these are high quality.

### Notes with Many Outlinks (Potential Splitters)

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  length(file.outlinks) as "Outbound Links"
FROM ""
WHERE length(file.outlinks) > 20
SORT length(file.outlinks) DESC
LIMIT 10
```

**Consider:** Large notes with many links might be candidates for splitting into focused notes.

### Unlinked Content Notes

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  type as "Type",
  created as "Created"
FROM ""
WHERE length(file.inlinks) = 0
  AND length(file.outlinks) = 0
  AND type != null
  AND type != "MOC"
  AND type != "DailyNote"
  AND !contains(file.path, "+Templates")
SORT created DESC
LIMIT 10
```

**Action:** Integrate with vault by adding links from related notes.

---

## 📈 Content Growth

### Notes Created per Month (Last 6 Months)

```dataview
TABLE WITHOUT ID
  dateformat(created, "yyyy-MM") as "Month",
  length(rows) as "Notes Created",
  type as "Type"
FROM ""
WHERE created >= date(today) - dur(180 days)
GROUP BY type, dateformat(created, "yyyy-MM")
SORT dateformat(created, "yyyy-MM") DESC
```

### Most Productive Days (Last 90 Days)

```dataview
TABLE WITHOUT ID
  created as "Date",
  length(rows) as "Notes Created",
  list(rows.file.link) as "Notes"
FROM ""
WHERE created >= date(today) - dur(90 days)
GROUP BY created
SORT length(rows) DESC
LIMIT 10
```

---

## 🎯 Maintenance Recommendations

### Weekly Maintenance (15 minutes)

**Priority:**
1. Review Critical Issues section
2. Check for broken links
3. Add type to untyped notes
4. Update stale active projects
5. Close or re-prioritize old open tasks

### Monthly Maintenance (30 minutes)

**Deep Dive:**
1. Review all Metadata Quality sections
2. Update ADR review dates
3. Archive completed projects
4. Clean up orphaned notes
5. Review and update stale People notes
6. Check attachment usage and cleanup

### Quarterly Maintenance (1 hour)

**Strategic Review:**
1. Analyze content growth trends
2. Review ADR portfolio for patterns
3. Update architecture documentation
4. Clean up old meeting notes
5. Review and refine MOCs
6. Update templates based on usage patterns

### Annual Maintenance (2 hours)

**Major Cleanup:**
1. Archive completed/deprecated content
2. Review all ADRs for relevance
3. Update all stale relationships
4. Reorganize if patterns have shifted
5. Export important content for backup
6. Update vault conventions documentation

---

## 📊 Health Scoring

### Overall Vault Health

**Calculate manually or use custom Dataview queries:**

| Metric | Target | Status |
|--------|--------|--------|
| Notes with type | 100% | Check "Notes Without Type" |
| ADRs with status | 100% | Check "ADRs Without Required Fields" |
| Active projects updated <30 days | >90% | Check "Active Projects Not Updated" |
| Orphaned notes | <5% of total | Check "Orphaned Notes" |
| Notes with backlinks | >80% | Check "Unlinked Content Notes" |
| Broken links | 0 | Check "Broken Links" |

**Health Status:**
- 🟢 Green: All targets met
- 🟡 Yellow: 1-2 targets missed
- 🔴 Red: 3+ targets missed

---

## 🔧 Quality Improvement Tools

### Claude Code Skills for Maintenance

| Skill | Purpose |
|-------|---------|
| `/orphans` | Find unlinked notes with recommendations |
| `/broken-links` | Identify and fix broken wiki-links |
| `/rename <pattern>` | Batch rename files with link updates |
| `/attachment-audit` | Analyze all vault attachments |
| `/sync-notion` | Sync external meeting notes |

### Recommended Obsidian Plugins

**Quality Helpers:**
- **Dataview** (required) - Powers all MOC queries
- **Templater** (required) - Automates note creation
- **Link** - Find broken links and unlinked mentions
- **Consistent attachments** - Organize attachment files
- **Tag Wrangler** - Manage hierarchical tags
- **Linter** - Auto-format frontmatter

### Manual Checks

**Periodically:**
- Run Obsidian's built-in "Unreferenced files" search
- Use "Orphaned files" command
- Check vault file size and cleanup large attachments
- Verify all critical MOCs load without errors
- Test that Dataview queries execute

---

## 📝 Quality Standards

### Note Quality Criteria

**High Quality Note:**
- [ ] Has type in frontmatter
- [ ] Created/modified dates present
- [ ] Appropriate tags applied
- [ ] At least one inbound link (not orphaned)
- [ ] Clear title and summary
- [ ] Links to related notes
- [ ] Content is current and accurate

**ADR Quality Criteria:**
- [ ] Status is current
- [ ] Category assigned
- [ ] Confidence level set
- [ ] Alternatives section completed
- [ ] Consequences documented
- [ ] Reviewed within 12 months
- [ ] Related to project (if applicable)

**Project Quality Criteria:**
- [ ] Status reflects reality
- [ ] Priority assigned
- [ ] Updated within 30 days (if active)
- [ ] Has stakeholders/people linked
- [ ] Key decisions documented/linked
- [ ] Success metrics defined
- [ ] Timeline information present

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Tasks MOC]] - Task health and priorities
- [[MOC - Projects MOC]] - Project status tracking
- [[MOC - ADRs MOC]] - ADR quality metrics

**Maintenance:**
- Review this dashboard weekly
- Update stale content monthly
- Run quality audits quarterly
- Archive annually

**Tips:**
- Pin this MOC for easy access
- Create recurring calendar reminders for maintenance
- Track improvements over time
- Celebrate progress (fewer red flags!)
- Don't aim for perfection - aim for improvement
- Use quality metrics to guide knowledge work priorities
