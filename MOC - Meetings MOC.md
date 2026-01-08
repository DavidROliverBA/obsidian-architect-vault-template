---
type: MOC
title: Meetings MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, meetings, collaboration]
---

# 📅 Meetings MOC

> **Comprehensive meeting history and insights**

Last Updated: 2026-01-07

---

## Overview

This MOC provides different views of meetings to help track discussions, decisions, and action items. Meetings are organized by date, project, attendees, and type.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - Projects MOC]] - View meetings by project
- [[MOC - People MOC]] - View meetings by attendee

---

## 📅 Recent Meetings

### Last 30 Days

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  attendees as "Attendees",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

### This Week

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(today) - dur(7 days)
SORT date DESC
```

### Today

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  project as "Project",
  attendees as "Attendees",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date = date(today)
SORT date DESC
```

---

## 🎯 Meetings by Project

### Cloud Migration

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  attendees as "Attendees",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(project, "Cloud Migration")
SORT date DESC
LIMIT 10
```

### API Gateway Modernization

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  attendees as "Attendees",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(project, "API Gateway")
SORT date DESC
LIMIT 10
```

### Unassigned to Project

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  attendees as "Attendees",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (project = null OR project = "")
SORT date DESC
LIMIT 10
```

**Action:** Consider linking these meetings to relevant projects for better organization.

---

## 👥 Meetings by Attendee

### With Jane Smith

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(attendees, "Jane Smith")
SORT date DESC
LIMIT 10
```

### With Alex Johnson

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(attendees, "Alex Johnson")
SORT date DESC
LIMIT 10
```

### With Dr. Sarah Chen

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(attendees, "Sarah Chen")
SORT date DESC
LIMIT 10
```

---

## 📋 Meetings by Type

### Project Kickoff Meetings

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND contains(meetingType, "Kickoff")
SORT date DESC
```

### Architecture Reviews

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (contains(meetingType, "Architecture Review") OR contains(tags, "architecture-review"))
SORT date DESC
```

### Technical Reviews

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (contains(meetingType, "Technical Review") OR contains(tags, "technical-review"))
SORT date DESC
```

### 1:1 Meetings

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  attendees as "With",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (contains(meetingType, "1:1") OR contains(meetingType, "One-on-One"))
SORT date DESC
LIMIT 10
```

---

## 📊 Meeting Analytics

### Meeting Frequency

**Meetings This Month:**
```dataview
TABLE WITHOUT ID
  dateformat(date, "yyyy-MM") as "Month",
  length(rows) as "Meeting Count"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(today) - dur(180 days)
GROUP BY dateformat(date, "yyyy-MM")
SORT dateformat(date, "yyyy-MM") DESC
```

### Most Frequent Attendees

```dataview
TABLE WITHOUT ID
  person as "Person",
  length(rows) as "Meetings Attended"
FROM "+Meetings"
WHERE type = "Meeting"
FLATTEN attendees as person
WHERE person != null AND person != ""
GROUP BY person
SORT length(rows) DESC
LIMIT 15
```

### Meetings by Day of Week

```dataview
TABLE WITHOUT ID
  dateformat(date, "EEEE") as "Day",
  length(rows) as "Meeting Count"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(today) - dur(90 days)
GROUP BY dateformat(date, "EEEE")
SORT length(rows) DESC
```

---

## 🔍 Meeting Quality Checks

### Meetings Without Summaries

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (summary = null OR summary = "")
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

**Action:** Add one-line summaries for quick reference and searchability.

### Meetings Without Project Links

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  attendees as "Attendees"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (project = null OR project = "")
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

**Action:** Link meetings to relevant projects for context.

### Meetings Without Attendees

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (attendees = null OR attendees = [] OR attendees = "")
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

**Action:** Add attendee list for tracking who was present.

---

## 📅 Meeting Timeline

### 2026 Meetings

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(2026-01-01)
SORT date DESC
```

### 2025 Meetings

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(2025-01-01)
  AND date < date(2026-01-01)
SORT date DESC
LIMIT 20
```

---

## 🔗 Action Items from Meetings

### Recent Action Items

Extract tasks created from meetings:

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project"
FROM "+Meetings"
WHERE type = "Meeting"
  AND file.tasks
  AND date >= date(today) - dur(30 days)
SORT date DESC
```

**Tip:** Use checkboxes in meeting notes for action items, then create formal Task notes for important follow-ups.

---

## 📝 Meeting Best Practices

### Before the Meeting

**Preparation:**
- Create meeting note from template (`+Templates/Meeting.md`)
- Add clear agenda items
- Link to related project
- Invite attendees (add to frontmatter)
- Review previous meeting notes if recurring

### During the Meeting

**Capture:**
- Key discussion points
- Decisions made (clear and actionable)
- Action items with owners
- Follow-up topics
- Questions raised

**Tips:**
- Use bullet points for readability
- Link to people: `[[Person Name]]`
- Link to projects: `[[Project - Name]]`
- Note action items with checkboxes: `- [ ] Action item`

### After the Meeting

**Follow-up:**
- Add one-line summary to frontmatter
- Create Task notes for important action items
- Share notes with attendees (if needed)
- Update related project notes
- Schedule follow-up if needed

### Meeting Note Structure

Recommended sections (included in template):
1. **Attendees** - Who was present
2. **Agenda** - What we planned to discuss
3. **Discussion Notes** - What was discussed
4. **Action Items** - What needs to be done
5. **Decisions Made** - What was decided
6. **Follow-up** - Next steps

---

## 🔍 Search Tips

**Finding Meetings:**
- By person: Search for `[[Person Name]]` in meeting notes
- By project: Filter meetings by project field
- By date: Use YYYY-MM-DD format in frontmatter
- By keyword: Full-text search in meeting content

**Common Queries:**
- Recent meetings with someone: See "Meetings by Attendee" section
- Project meeting history: See "Meetings by Project" section
- Decisions made in meetings: Search for "Decisions Made" headings

---

## 📁 Meeting Organization

**File Location:**
All meeting notes stored in `+Meetings/` directory.

**Naming Convention:**
`Meeting - YYYY-MM-DD Title.md`

Examples:
- `Meeting - 2026-01-07 Project Kickoff.md`
- `Meeting - 2026-01-08 Architecture Review.md`

**Benefits:**
- Chronological sorting
- Easy to find by date
- Clear context from title
- Consistent structure

---

## 🎯 Recurring Meetings

### Weekly Standups

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (contains(title, "Standup") OR contains(meetingType, "Standup"))
SORT date DESC
LIMIT 10
```

### Monthly Reviews

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  summary as "Summary"
FROM "+Meetings"
WHERE type = "Meeting"
  AND (contains(title, "Review") OR contains(meetingType, "Review"))
SORT date DESC
LIMIT 10
```

**Tip:** Use `meetingType` field to group recurring meeting series.

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Projects MOC]] - Project-specific meetings
- [[MOC - People MOC]] - Meeting participants
- [[MOC - Tasks MOC]] - Action items from meetings

**Templates:**
- `+Templates/Meeting.md` - Create new meeting note

**Best Practices:**
- Create meeting note before or during meeting
- Link attendees using Person notes
- Extract important action items as Tasks
- Link meetings to relevant Projects
- Add one-line summary for searchability
