<%*
const name = await tp.system.prompt("Task name:");
if (name) {
  await tp.file.rename("Task - " + name);
}
_%>
---
type: Task
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
completed: false
priority: medium  # high | medium | low
due: null  # YYYY-MM-DD or null
project: null  # Link to project: "[[Project - Name]]"
assignee: null  # Link to person: "[[Person Name]]"
---

# <% name %>

## Description

<!-- What needs to be done and why? -->

## Acceptance Criteria

- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

## Notes

<!-- Additional context, blockers, or progress updates -->
