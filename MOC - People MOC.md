---
type: MOC
title: People MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, people, contacts, directory]
---

# 👥 People MOC

> **Contact directory and relationship management**

Last Updated: 2026-01-07

---

## Overview

This MOC provides comprehensive views of people you work with, organized by role, organization, and interaction history. Use this to maintain relationships and track collaborations.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - Meetings MOC]] - See meeting attendees
- [[MOC - Organisations MOC]] - View by organization

---

## 🏢 Internal Team

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND contains(organisation, "Your Company")
SORT role ASC, file.name ASC
```

---

## 🤝 External Contacts

### Consultants & Contractors

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND !contains(organisation, "Your Company")
  AND (contains(tags, "consultant") OR contains(tags, "external"))
SORT organisation ASC, file.name ASC
```

### Vendors & Partners

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND (contains(tags, "vendor") OR contains(tags, "partner"))
SORT organisation ASC, file.name ASC
```

---

## 📋 By Role

### Leadership & Management

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND (contains(role, "Head") OR contains(role, "Director") OR contains(role, "VP") OR contains(role, "CTO") OR contains(role, "CEO"))
SORT role ASC, file.name ASC
```

### Architecture & Engineering

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company"
FROM ""
WHERE type = "Person"
  AND (contains(role, "Architect") OR contains(role, "Engineer") OR contains(role, "Developer"))
SORT role ASC, file.name ASC
```

### Product & Business

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company"
FROM ""
WHERE type = "Person"
  AND (contains(role, "Product") OR contains(role, "Business") OR contains(role, "Manager"))
SORT role ASC, file.name ASC
```

---

## 🏢 By Organisation

### Your Company

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND contains(organisation, "Your Company")
SORT role ASC, file.name ASC
```

### CloudVendor Inc

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  email as "Email"
FROM ""
WHERE type = "Person"
  AND contains(organisation, "CloudVendor")
SORT role ASC, file.name ASC
```

### Other Organizations

```dataview
TABLE WITHOUT ID
  file.link as "Name",
  role as "Role",
  organisation as "Company"
FROM ""
WHERE type = "Person"
  AND !contains(organisation, "Your Company")
  AND !contains(organisation, "CloudVendor")
SORT organisation ASC, file.name ASC
```

---

## 📅 Recent Interactions

### People Met With Recently (Last 30 Days)

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  role as "Role",
  organisation as "Company",
  length(rows.file.link) as "Meetings"
FROM ""
WHERE type = "Meeting"
  AND date >= date(today) - dur(30 days)
FLATTEN attendees as person
WHERE person != null AND person != ""
GROUP BY person
SORT length(rows.file.link) DESC
LIMIT 10
```

### Most Frequent Collaborators (All Time)

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  length(rows.file.link) as "Total Meetings"
FROM ""
WHERE type = "Meeting"
FLATTEN attendees as person
WHERE person != null AND person != ""
GROUP BY person
SORT length(rows.file.link) DESC
LIMIT 15
```

---

## 📊 People Interaction Matrix

### Jane Smith's Meetings

**Person:** [[Jane Smith]] - Head of Architecture

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM ""
WHERE type = "Meeting"
  AND contains(attendees, "Jane Smith")
SORT date DESC
LIMIT 10
```

### Alex Johnson's Meetings

**Person:** [[Alex Johnson]] - Senior Engineer

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM ""
WHERE type = "Meeting"
  AND contains(attendees, "Alex Johnson")
SORT date DESC
LIMIT 10
```

### Dr. Sarah Chen's Meetings

**Person:** [[Dr. Sarah Chen]] - External Consultant

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM ""
WHERE type = "Meeting"
  AND contains(attendees, "Sarah Chen")
SORT date DESC
LIMIT 10
```

---

## 📋 Task Assignments

### Tasks by Assignee

#### Jane Smith's Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due",
  project as "Project"
FROM ""
WHERE type = "Task"
  AND contains(assignee, "Jane Smith")
SORT completed ASC, priority ASC, due ASC
```

#### Alex Johnson's Tasks

```dataview
TABLE WITHOUT ID
  file.link as "Task",
  completed as "Done",
  priority as "Priority",
  due as "Due",
  project as "Project"
FROM ""
WHERE type = "Task"
  AND contains(assignee, "Alex Johnson")
SORT completed ASC, priority ASC, due ASC
```

---

## 🔍 People Without Recent Contact

### No Meetings in Last 90 Days

```dataview
TABLE WITHOUT ID
  file.link as "Person",
  role as "Role",
  organisation as "Company",
  modified as "Last Note Update"
FROM ""
WHERE type = "Person"
  AND !contains(file.outlinks.file.name, "Meeting")
  OR ALL(map(file.outlinks, (link) =>
      meta(link).type != "Meeting"
      OR meta(link).date < date(today) - dur(90 days)
    ))
SORT modified ASC
LIMIT 10
```

**Action:** Consider reaching out for relationship maintenance or archiving inactive contacts.

---

## 📊 People Statistics

### People by Organization

```dataview
TABLE WITHOUT ID
  organisation as "Organization",
  length(rows) as "People Count"
FROM ""
WHERE type = "Person"
GROUP BY organisation
SORT length(rows) DESC
```

### Role Distribution

```dataview
TABLE WITHOUT ID
  role as "Role",
  length(rows) as "Count"
FROM ""
WHERE type = "Person"
GROUP BY role
SORT length(rows) DESC
LIMIT 15
```

### Contact Information Completeness

```dataview
TABLE WITHOUT ID
  "Email Address" as "Field",
  length(filter(rows, (r) => r.email != null AND r.email != "")) as "Populated",
  length(rows) as "Total",
  round((length(filter(rows, (r) => r.email != null AND r.email != "")) / length(rows)) * 100, 1) + "%" as "Completeness"
FROM ""
WHERE type = "Person"
```

---

## 📝 People Management Tips

### Adding New Contacts

**When to Create a Person Note:**
- Regular collaborator or stakeholder
- External consultant or vendor contact
- Anyone you meet with multiple times
- Key decision makers

**What to Include:**
- Role and organization
- Contact information (email, phone)
- Notes about expertise, working style
- Meeting history (auto-populated via Dataview)

**Template:** Use `+Templates/Person.md` for consistent format

### Maintaining Contact Information

**Regular Reviews:**
- Monthly: Update recently active contacts
- Quarterly: Review for outdated information
- Annually: Archive inactive contacts

**Best Practices:**
- Update after significant role changes
- Add notes after key interactions
- Link to relevant meetings and projects
- Tag by relationship type (stakeholder, vendor, etc.)

### Naming Convention

**Person notes don't use "Person -" prefix** for cleaner wiki-links:
- ✅ Good: `[[Jane Smith]]`
- ❌ Bad: `[[Person - Jane Smith]]`

This allows natural references in meeting notes and daily logs.

---

## 🔗 Relationship Mapping

### Key Stakeholders

List your most important relationships by area:

**Architecture:**
- [[Jane Smith]] - Head of Architecture (manager)
- Architecture Board members

**Engineering:**
- [[Alex Johnson]] - Senior Engineer (collaborator)
- Platform Engineering team

**External:**
- [[Dr. Sarah Chen]] - CloudVendor Inc (consultant)
- Vendor account managers

### Communication Preferences

Track how people prefer to communicate:
- Email: Formal updates, documentation
- Slack: Quick questions, informal
- Meetings: Complex discussions, decisions
- Async: Written proposals, ADRs

Add this to person note "Notes" section.

---

## 🌐 Network Map

### Cross-Organization Connections

```dataview
TABLE WITHOUT ID
  organisation as "Organization",
  length(rows) as "Contacts",
  list(rows.file.link) as "People"
FROM ""
WHERE type = "Person"
GROUP BY organisation
SORT length(rows) DESC
```

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Organisations MOC]] - View by organization
- [[MOC - Meetings MOC]] - See who you've met with
- [[MOC - Projects MOC]] - Project stakeholders

**Templates:**
- `+Templates/Person.md` - Create new person note

**Tips:**
- Link people in meeting notes: `[[Person Name]]`
- Assign tasks to people: `assignee: "[[Person Name]]"`
- Tag important stakeholders in your notes
- Maintain 1:1 meeting notes as separate documents
