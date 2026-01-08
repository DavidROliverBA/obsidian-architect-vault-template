<%*
const today = tp.date.now("YYYY-MM-DD");
const year = tp.date.now("YYYY");
await tp.file.move("+Daily/" + year + "/" + today);
_%>
---
type: DailyNote
title: <% tp.date.now("YYYY-MM-DD") %>
created: <% tp.date.now("YYYY-MM-DD") %>
date: <% tp.date.now("YYYY-MM-DD") %>
tags: [daily]
---

# <% tp.date.now("dddd, MMMM Do YYYY") %>

## Today's Focus

<!-- Top 1-3 priorities for today -->
-

## Tasks

### Due Today

```dataview
TASK
FROM ""
WHERE type = "Task" AND due = date("<% tp.date.now("YYYY-MM-DD") %>") AND !completed
```

### Completed Today

- [ ]

## Notes

<!-- Meeting notes, discoveries, ideas, learnings -->

## Reflections

<!-- End-of-day reflections, wins, challenges -->
