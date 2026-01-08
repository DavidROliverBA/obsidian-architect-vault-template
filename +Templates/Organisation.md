<%*
const name = await tp.system.prompt("Organisation name:");
if (name) {
  await tp.file.rename("Organisation - " + name);
}
_%>
---
type: Organisation
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
website: # Company website URL
industry: # Industry/sector
relationship: null  # customer | partner | vendor | competitor | internal
---

# <% name %>

## Overview

- **Website:**
- **Industry:**
- **Relationship:** Customer | Partner | Vendor | Competitor | Internal

## Description

<!-- About the organization, what they do, relevance to your work -->

## Key Contacts

```dataview
TABLE role, email AS "Email"
FROM ""
WHERE type = "Person" AND contains(organisation, this.file.name)
SORT role ASC
```

## Projects

```dataview
TABLE status, priority
FROM ""
WHERE type = "Project" AND contains(file.outlinks, this.file.link)
SORT status ASC
```

## Notes

<!-- Notes about the organization, collaboration history, etc. -->

## Related

- [[Related Organisation]]
- [[Related Project]]
