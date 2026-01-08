<%*
const name = await tp.system.prompt("Weblink title:");
if (name) {
  await tp.file.rename("Weblink - " + name);
}
_%>
---
type: Weblink
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
url: # Full URL
author: # Author name (if applicable)
source: # Website/publication name
---

# <% name %>

## Source

- **URL:**
- **Author:**
- **Source:**
- **Date:**

## Summary

<!-- Brief summary of the content -->

## Key Points

- Point 1
- Point 2
- Point 3

## Quotes

<!-- Notable quotes from the article -->

## Related

- [[Related Note 1]]
- [[Related Note 2]]
