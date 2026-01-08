<%*
const name = await tp.system.prompt("Meeting name:");
if (name) {
  const date = tp.date.now("YYYY-MM-DD");
  const filename = "Meeting - " + date + " " + name;
  await tp.file.move("+Meetings/" + filename);
}
_%>
---
type: Meeting
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
date: <% tp.date.now("YYYY-MM-DD") %>
project: null  # Link to project: "[[Project - Name]]"
attendees: []  # List of attendees: ["[[Person Name]]"]
summary: # Brief one-line summary of the meeting
meetingType: null  # Optional: Recurring meeting series name (e.g., "Weekly Standup")
---

# <% name %>

**Date:** <% tp.date.now("dddd, MMMM Do YYYY") %>

## Attendees

- [[Person Name]]
- [[Person Name]]

## Agenda

1. Item 1
2. Item 2
3. Item 3

## Discussion Notes

<!-- Key points discussed during the meeting -->

## Action Items

- [ ] Action item 1 - [[Assignee]]
- [ ] Action item 2 - [[Assignee]]

## Decisions Made

- Decision 1
- Decision 2

## Follow-up

<!-- Next steps and future meeting plans -->
