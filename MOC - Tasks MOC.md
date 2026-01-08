---
type: MOC
title: Tasks MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, tasks, productivity]
---

# 📋 Tasks MOC

> **Comprehensive task management and tracking**

Last Updated: 2026-01-07

---

## Overview

This MOC provides different views of tasks to help you prioritize and manage your work effectively. Tasks are organized by priority, status, due date, and project.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - Projects MOC]] - View tasks by project

---

## 🔥 High Priority Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  due as "Due Date",
  project as "Project",
  assignee as "Assignee"
FROM ""
WHERE type = "Task" AND priority = "high"
SORT completed ASC, due ASC
```

**Total High Priority:** `= length(filter(file.tasks, (t) => contains(t.text, "priority: high")))`

---

## 📌 Medium Priority Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  due as "Due Date",
  project as "Project",
  assignee as "Assignee"
FROM ""
WHERE type = "Task" AND priority = "medium"
SORT completed ASC, due ASC
```

---

## 📝 Low Priority Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  due as "Due Date",
  project as "Project",
  assignee as "Assignee"
FROM ""
WHERE type = "Task" AND priority = "low"
SORT completed ASC, due ASC
```

---

## ⚠️ Overdue Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date",
  project as "Project",
  assignee as "Assignee"
FROM ""
WHERE type = "Task" AND !completed AND due < date(today)
SORT due ASC, priority ASC
```

**Action Required:** These tasks need immediate attention or rescheduling.

---

## 📅 Due This Week

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date",
  project as "Project",
  assignee as "Assignee"
FROM ""
WHERE type = "Task"
  AND !completed
  AND due >= date(today)
  AND due <= date(today) + dur(7 days)
SORT due ASC, priority ASC
```

---

## 📅 Due This Month

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date",
  project as "Project"
FROM ""
WHERE type = "Task"
  AND !completed
  AND due >= date(today)
  AND due <= date(today) + dur(30 days)
SORT due ASC, priority ASC
```

---

## 🎯 Tasks by Project

### Cloud Migration Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task"
  AND contains(project, "Cloud Migration")
SORT completed ASC, priority ASC, due ASC
```

### API Gateway Modernization Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task"
  AND contains(project, "API Gateway")
SORT completed ASC, priority ASC, due ASC
```

### Unassigned to Project

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task" AND (project = null OR project = "")
SORT completed ASC, priority ASC, due ASC
```

**Note:** Consider assigning these tasks to projects for better organization.

---

## 👤 Tasks by Assignee

### My Tasks (Assigned to You)

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date",
  project as "Project"
FROM ""
WHERE type = "Task" AND contains(assignee, "Your Name")
SORT completed ASC, priority ASC, due ASC
```

**Tip:** Replace "Your Name" with your actual name to see your tasks.

### Jane Smith's Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task" AND contains(assignee, "Jane Smith")
SORT completed ASC, priority ASC, due ASC
```

### Alex Johnson's Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task" AND contains(assignee, "Alex Johnson")
SORT completed ASC, priority ASC, due ASC
```

### Unassigned Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date",
  project as "Project"
FROM ""
WHERE type = "Task" AND (assignee = null OR assignee = "")
SORT priority ASC, due ASC
```

---

## ✅ Completed Tasks (Last 30 Days)

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  modified as "Completed",
  project as "Project"
FROM ""
WHERE type = "Task"
  AND completed = true
  AND modified >= date(today) - dur(30 days)
SORT modified DESC
LIMIT 20
```

**Recent Wins:** Review completed tasks to track progress and celebrate achievements.

---

## 📊 Task Statistics

### Task Breakdown

```dataview
TABLE WITHOUT ID
  priority as "Priority",
  length(rows) as "Total Tasks",
  length(filter(rows, (r) => r.completed)) as "Completed",
  length(filter(rows, (r) => !r.completed)) as "Open"
FROM ""
WHERE type = "Task"
GROUP BY priority
SORT priority ASC
```

### Completion Rate

**Total Tasks:** `= length(filter(this.file.tasks, (t) => contains(t.type, "Task")))`
**Completed:** `= length(filter(this.file.tasks, (t) => contains(t.type, "Task") and t.completed))`
**Completion Rate:** Calculate manually or use custom script

---

## 🔍 Task Views by Tag

### High-Priority ADR Reviews

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  due as "Due Date",
  project as "Project"
FROM ""
WHERE type = "Task"
  AND contains(tags, "adr-review")
  AND !completed
SORT due ASC
```

### Documentation Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task"
  AND contains(tags, "documentation")
  AND !completed
SORT priority ASC, due ASC
```

### Research Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  priority as "Priority",
  due as "Due Date"
FROM ""
WHERE type = "Task"
  AND contains(tags, "research")
  AND !completed
SORT priority ASC, due ASC
```

---

## 📝 Task Management Tips

### Creating Tasks
- Use template: `+Templates/Task.md`
- Include clear description and acceptance criteria
- Set realistic due dates
- Assign to specific person or team
- Link to related project

### Prioritization Framework
- **High**: Urgent and important (do first)
- **Medium**: Important but not urgent (schedule)
- **Low**: Nice to have (do if time permits)

### Task Lifecycle
1. **Created**: Task identified and documented
2. **Assigned**: Owner designated
3. **In Progress**: Work started
4. **Blocked**: Dependencies or issues
5. **Completed**: Acceptance criteria met

### Best Practices
- Review tasks weekly
- Update status regularly
- Break large tasks into smaller ones
- Archive completed tasks monthly
- Use tags for easy filtering

---

## 🔗 Quick Actions

**Create New Task:**
1. Use Templater: Insert `+Templates/Task.md`
2. Enter task name when prompted
3. Fill in priority, due date, project, assignee
4. Add description and acceptance criteria

**Bulk Operations:**
- Archive completed tasks: Move to archive folder
- Update priorities: Use find/replace on frontmatter
- Reassign tasks: Update assignee field

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Projects MOC]] - View tasks by project context
- [[MOC - People MOC]] - See tasks assigned to team members

**Task Management:**
- Use daily notes ([[+Daily/2026/2026-01-07]]) to track daily progress
- Link tasks to meetings where they were created
- Update project status based on task completion

**Customization:**
- Modify Dataview queries to match your workflow
- Add custom task statuses in templates
- Create additional task views as needed
