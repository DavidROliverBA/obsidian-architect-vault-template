<%*
const name = await tp.system.prompt("Task name:");
if (name) {
await tp.file.rename("Task - " + name);
}
_%>

---
type: Task
title: "<% name %>"
created: '<% tp.date.now("YYYY-MM-DD") %>'
modified: '<% tp.date.now("YYYY-MM-DD") %>'
tags: []
summary: null
completed: false
completedDate: null
priority: medium # high | medium | low
doDate: null
dueBy: null
project: null # "[[Project - X]]"
assignedTo: []
parentTask: null
subtasks: []
relatedTo: []
---

# <% name %>

## Description

## Acceptance Criteria

- [ ]

## Subtasks

## Notes
