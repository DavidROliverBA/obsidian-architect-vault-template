<%*
const name = await tp.system.prompt("Person's name:");
if (name) {
  await tp.file.rename(name);  // Person notes don't use "Person -" prefix
}
_%>
---
type: Person
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
role: # Job title
organisation: null  # Link to organisation: "[[Organisation - Name]]"
email: # Email address
phone: # Phone number (optional)
---

# <% name %>

## Contact Information

- **Role:**
- **Organisation:**
- **Email:**
- **Phone:**

## Notes

<!-- Notes about this person, their expertise, working style, etc. -->

## Interactions

```dataview
TABLE date, summary
FROM ""
WHERE type = "Meeting" AND contains(attendees, this.file.name)
SORT date DESC
```

## Related Projects

```dataview
TABLE status, priority
FROM ""
WHERE type = "Project" AND contains(file.outlinks, this.file.link)
SORT status ASC
```
