<%*
const name = await tp.system.prompt("Page title:");
if (name) {
  await tp.file.rename("Page - " + name);
}
_%>
---
type: Page
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []

# Quality Indicators (for AI discoverability)
summary: # Brief summary of the content
confidence: medium  # low | medium | high - How authoritative is this?
freshness: current  # current | recent | stale - How up-to-date?
source: synthesis  # primary | secondary | synthesis | external
verified: false  # Has this been fact-checked?
reviewed: <% tp.date.now("YYYY-MM-DD") %>

# Semantic Discovery
keywords: []  # Keywords for search and AI context

# Relationships
relatedTo: []  # Related pages, projects, or ADRs
---

# <% name %>

## Overview

<!-- High-level summary of the topic -->

## Details

<!-- Main content goes here -->

## Related

- [[Related Note 1]]
- [[Related Note 2]]
