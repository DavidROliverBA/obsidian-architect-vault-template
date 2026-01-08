---
type: MOC
title: Projects MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, projects, portfolio]
---

# 🎯 Projects MOC

> **Portfolio view of all projects and initiatives**

Last Updated: 2026-01-07

---

## Overview

This MOC provides comprehensive views of projects organized by status, priority, and category. Use this to understand the project portfolio and track progress across initiatives.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - Tasks MOC]] - View project tasks
- [[MOC - ADRs MOC]] - View project architecture decisions

---

## 🚀 Active Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  priority as "Priority",
  start-date as "Started",
  end-date as "Target End",
  category as "Category"
FROM ""
WHERE type = "Project" AND status = "active"
SORT priority ASC, start-date DESC
```

**Active Project Count:** Projects currently in execution

---

## ⏸️ Paused Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  priority as "Priority",
  start-date as "Started",
  category as "Category"
FROM ""
WHERE type = "Project" AND status = "paused"
SORT priority ASC
```

**Note:** Review paused projects quarterly to decide: resume, cancel, or keep paused.

---

## ✅ Completed Projects (Last 12 Months)

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  priority as "Priority",
  start-date as "Started",
  end-date as "Completed",
  category as "Category"
FROM ""
WHERE type = "Project"
  AND status = "completed"
  AND end-date >= date(today) - dur(365 days)
SORT end-date DESC
```

**Recent Completions:** Review for lessons learned and best practices.

---

## 🔴 High Priority Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  start-date as "Started",
  end-date as "Target End",
  category as "Category"
FROM ""
WHERE type = "Project" AND priority = "high"
SORT status ASC, start-date DESC
```

---

## 🟡 Medium Priority Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  start-date as "Started",
  end-date as "Target End",
  category as "Category"
FROM ""
WHERE type = "Project" AND priority = "medium"
SORT status ASC, start-date DESC
```

---

## 🟢 Low Priority Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  start-date as "Started",
  category as "Category"
FROM ""
WHERE type = "Project" AND priority = "low"
SORT status ASC, start-date DESC
```

---

## 📁 Projects by Category

### Digital Transformation

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND contains(category, "Digital Transformation")
SORT status ASC, priority ASC
```

### Platform Engineering

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND contains(category, "Platform Engineering")
SORT status ASC, priority ASC
```

### Research & Innovation

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND contains(category, "Research")
SORT status ASC, priority ASC
```

### Technical Debt Reduction

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND contains(category, "Technical Debt")
SORT status ASC, priority ASC
```

### Uncategorized Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project" AND (category = null OR category = "")
SORT status ASC, priority ASC
```

---

## 📊 Project Deep Dives

### Cloud Migration

**Project:** [[Project - Cloud Migration]]
**Status:** Active | **Priority:** High

**Recent Tasks:**
```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due"
FROM ""
WHERE type = "Task"
  AND contains(project, "Cloud Migration")
SORT completed ASC, priority ASC
LIMIT 5
```

**Related Meetings:**
```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  summary as "Summary"
FROM ""
WHERE type = "Meeting"
  AND contains(project, "Cloud Migration")
SORT date DESC
LIMIT 5
```

**Architecture Decisions:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category"
FROM ""
WHERE type = "Adr"
  AND contains(project, "Cloud Migration")
SORT status ASC
```

---

### API Gateway Modernization

**Project:** [[Project - API Gateway Modernization]]
**Status:** Active | **Priority:** Medium

**Recent Tasks:**
```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due"
FROM ""
WHERE type = "Task"
  AND contains(project, "API Gateway")
SORT completed ASC, priority ASC
LIMIT 5
```

**Related Meetings:**
```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  summary as "Summary"
FROM ""
WHERE type = "Meeting"
  AND contains(project, "API Gateway")
SORT date DESC
LIMIT 5
```

**Architecture Decisions:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category"
FROM ""
WHERE type = "Adr"
  AND contains(project, "API Gateway")
SORT status ASC
```

---

## 📈 Project Statistics

### Status Breakdown

```dataview
TABLE WITHOUT ID
  status as "Status",
  length(rows) as "Count"
FROM ""
WHERE type = "Project"
GROUP BY status
SORT status ASC
```

### Priority Distribution

```dataview
TABLE WITHOUT ID
  priority as "Priority",
  length(rows) as "Count"
FROM ""
WHERE type = "Project"
GROUP BY priority
SORT priority ASC
```

### Projects by Start Year

```dataview
TABLE WITHOUT ID
  dateformat(start-date, "yyyy") as "Year",
  length(rows) as "Projects Started"
FROM ""
WHERE type = "Project" AND start-date != null
GROUP BY dateformat(start-date, "yyyy")
SORT dateformat(start-date, "yyyy") DESC
```

---

## 🎯 Project Health Dashboard

### Projects Without End Dates

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND status = "active"
  AND (end-date = null OR end-date = "")
SORT priority ASC
```

**Action:** Active projects should have target end dates for planning.

### Projects Without Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority"
FROM ""
WHERE type = "Project"
  AND status = "active"
  AND !contains(file.outlinks, "Task")
SORT priority ASC
```

**Action:** Active projects need tasks for execution tracking.

### Projects Without Recent Activity (90+ days)

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  modified as "Last Updated"
FROM ""
WHERE type = "Project"
  AND status = "active"
  AND modified < date(today) - dur(90 days)
SORT modified ASC
```

**Action:** Review these projects - are they truly active or should status change?

---

## 📝 Project Management Tips

### Project Lifecycle

1. **Initiation**: Define objectives, stakeholders, success criteria
2. **Planning**: Break down into tasks, set timeline, identify risks
3. **Execution**: Work tasks, track progress, hold regular check-ins
4. **Monitoring**: Review metrics, adjust plan as needed
5. **Closure**: Document outcomes, lessons learned, celebrate wins

### Best Practices

**Project Setup:**
- Clear, measurable objectives
- Identified stakeholders and decision makers
- Target timeline (even if approximate)
- Success criteria defined upfront

**During Execution:**
- Weekly status updates
- Link related tasks, meetings, ADRs
- Document decisions and trade-offs
- Regular stakeholder communication

**Project Closure:**
- Document lessons learned
- Archive or transition deliverables
- Celebrate team achievements
- Update status to "completed"

### Project Templates

Use `+Templates/Project.md` to create new projects with consistent structure.

**Recommended Sections:**
- Overview and objectives
- Key stakeholders
- Timeline and milestones
- Related tasks (auto-populated via Dataview)
- Meetings (auto-populated via Dataview)
- Architecture decisions (auto-populated via Dataview)
- Notes and updates

---

## 🔍 Cross-Project Views

### All Project Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  project as "Project",
  priority as "Priority",
  due as "Due",
  completed as "Done"
FROM ""
WHERE type = "Task" AND project != null
SORT project ASC, completed ASC, priority ASC
```

### All Project Meetings

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM ""
WHERE type = "Meeting" AND project != null
SORT date DESC
LIMIT 20
```

### All Project ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  project as "Project",
  category as "Category"
FROM ""
WHERE type = "Adr" AND project != null
SORT status ASC, project ASC
```

---

## 📅 Timeline View

### Projects Started This Year (2026)

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  start-date as "Started"
FROM ""
WHERE type = "Project"
  AND start-date >= date(2026-01-01)
SORT start-date DESC
```

### Projects Ending This Quarter

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority",
  end-date as "Target End"
FROM ""
WHERE type = "Project"
  AND end-date >= date(today)
  AND end-date <= date(today) + dur(90 days)
SORT end-date ASC
```

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Tasks MOC]] - Detailed task views
- [[MOC - Meetings MOC]] - Project meetings
- [[MOC - ADRs MOC]] - Project architecture decisions

**Project Resources:**
- [[Page - Architecture Principles]] - Decision-making framework
- [[Page - Tech Stack Overview]] - Technology standards
- Template: `+Templates/Project.md`

**Portfolio Management:**
- Review project portfolio monthly
- Align projects with strategic objectives
- Balance capacity across priorities
- Archive completed projects for reference
