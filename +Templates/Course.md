<%*
const name = await tp.system.prompt("Course name:");
if (name) {
  await tp.file.rename("Course - " + name);
}
_%>
---
type: Course
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
provider: # Course provider (Udemy, Coursera, etc.)
url: # Course URL
project: null  # Related project if applicable
status: not-started  # not-started | in-progress | completed
start-date: null
end-date: null
certificate: null  # Link to certificate when completed
---

# <% name %>

## Overview

- **Provider:**
- **URL:**
- **Duration:**
- **Status:** Not Started | In Progress | Completed

## Learning Objectives

- Objective 1
- Objective 2
- Objective 3

## Modules / Sections

### Module 1: [Title]

#### Key Points

- Point 1
- Point 2

#### Notes

<!-- Notes from this module -->

### Module 2: [Title]

#### Key Points

- Point 1
- Point 2

#### Notes

<!-- Notes from this module -->

## Key Takeaways

- Takeaway 1
- Takeaway 2
- Takeaway 3

## Action Items

- [ ] Apply concept X to project Y
- [ ] Research topic Z further

## Resources

- [[Related Note]]
- [[Weblink - Resource]]

## Certificate

<!-- Link to certificate if completed -->
