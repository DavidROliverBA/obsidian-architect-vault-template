---
type: MOC
title: Weblinks MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, weblinks, resources, references]
---

# 🔗 Weblinks MOC

> **Curated external resources and references**

Last Updated: 2026-01-07

---

## Overview

This MOC organizes saved web resources, articles, documentation, and external references. Use this as your personal library of valuable online content.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - Technology & Architecture MOC]] - Technical standards

---

## 📚 All Weblinks

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
SORT created DESC
```

---

## 🏷️ By Category/Tags

### Architecture & Patterns

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source"
FROM ""
WHERE type = "Weblink"
  AND (contains(tags, "architecture") OR contains(tags, "patterns"))
SORT created DESC
```

### Microservices

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source"
FROM ""
WHERE type = "Weblink"
  AND contains(tags, "microservices")
SORT created DESC
```

### Cloud & AWS

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source"
FROM ""
WHERE type = "Weblink"
  AND (contains(tags, "aws") OR contains(tags, "cloud"))
SORT created DESC
```

### Best Practices

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source"
FROM ""
WHERE type = "Weblink"
  AND contains(tags, "best-practices")
SORT created DESC
```

### Reference Documentation

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source"
FROM ""
WHERE type = "Weblink"
  AND contains(tags, "reference")
SORT created DESC
```

---

## 👤 By Author

### Martin Fowler

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  source as "Source",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND contains(author, "Fowler")
SORT created DESC
```

### AWS Documentation

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  source as "Source",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND contains(author, "AWS")
SORT created DESC
```

---

## 🌐 By Source

### martinfowler.com

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND contains(source, "martinfowler.com")
SORT created DESC
```

### aws.amazon.com

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND contains(source, "aws.amazon.com")
SORT created DESC
```

---

## 📅 Recently Saved

### Last 30 Days

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND created >= date(today) - dur(30 days)
SORT created DESC
```

### Last 90 Days

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  author as "Author",
  source as "Source",
  created as "Saved"
FROM ""
WHERE type = "Weblink"
  AND created >= date(today) - dur(90 days)
SORT created DESC
```

---

## 🔗 Most Referenced

### Weblinks Linked from Other Notes

```dataview
TABLE WITHOUT ID
  file.link as "Resource",
  length(file.inlinks) as "Referenced By",
  source as "Source"
FROM ""
WHERE type = "Weblink"
SORT length(file.inlinks) DESC
LIMIT 15
```

**Highly Referenced:** These resources are frequently cited in your notes.

---

## 📊 Weblink Statistics

### Count by Source

```dataview
TABLE WITHOUT ID
  source as "Source",
  length(rows) as "Weblinks Saved"
FROM ""
WHERE type = "Weblink"
GROUP BY source
SORT length(rows) DESC
LIMIT 10
```

### Weblinks by Month

```dataview
TABLE WITHOUT ID
  dateformat(created, "yyyy-MM") as "Month",
  length(rows) as "Weblinks Saved"
FROM ""
WHERE type = "Weblink" AND created != null
GROUP BY dateformat(created, "yyyy-MM")
SORT dateformat(created, "yyyy-MM") DESC
LIMIT 12
```

---

## 📝 Weblink Management

### Saving Weblinks

**When to Save:**
- Valuable articles you'll reference multiple times
- Official documentation for technologies you use
- Best practices guides
- Case studies relevant to your work
- Research papers and technical deep dives

**Don't Save:**
- News articles (ephemeral content)
- Resources you won't revisit
- Content duplicated elsewhere
- Simple Stack Overflow answers (copy code to notes instead)

**Template:** Use `+Templates/Weblink.md` for consistent format.

### Weblink Fields

**Required:**
- **Title** - Descriptive title
- **URL** - Full URL to resource
- **Source** - Website/publication name

**Optional:**
- **Author** - Content creator
- **Summary** - Brief description
- **Key Points** - Main takeaways
- **Quotes** - Notable excerpts
- **Tags** - Categories for filtering

### Best Practices

**Adding Context:**
- Write summary in your own words
- Extract key points relevant to your work
- Note how it relates to your projects
- Add personal insights or reflections

**Organization:**
- Tag by topic for filtering
- Link from relevant project notes
- Reference in ADRs when applicable
- Group by author or source

**Maintenance:**
- Periodically check for dead links
- Update if content moves
- Archive outdated resources
- Remove duplicates

---

## 🎯 Curated Collections

### Essential Reading

Must-read resources for architects:

- [[Weblink - Martin Fowler on Microservices]]
- [[Weblink - AWS Well-Architected Framework]]

**Tip:** Create custom collections by creating a Page note and linking relevant weblinks.

### Getting Started Guides

Resources for new team members:

```dataview
LIST
FROM ""
WHERE type = "Weblink"
  AND (contains(tags, "getting-started") OR contains(tags, "onboarding"))
SORT created ASC
```

---

## 🔍 Quick Search

**Common Searches:**
- Find articles by keyword: Use Obsidian search
- Articles by author: See "By Author" section
- Recent saves: See "Recently Saved" section
- Most referenced: See "Most Referenced" section

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Technology & Architecture MOC]] - Tech stack documentation
- [[MOC - ADRs MOC]] - Reference weblinks in ADRs

**Integration:**
- Link weblinks from project notes
- Reference in ADRs to support decisions
- Include in meeting notes when discussed
- Add to daily notes when discovered

**External Tools:**
- Browser bookmarks: Import important ones here
- Pocket/Instapaper: Migrate saved content
- Notion: Export web clips as markdown

**Tips:**
- Use `/weblink` Claude skill to save URLs with AI-generated summaries
- Include weblinks in literature review for projects
- Create thematic weblink collections for specific topics
- Share valuable resources with team in meeting notes
