---
type: MOC
title: Organisations MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, organisations, vendors, partners]
---

# 🏢 Organisations MOC

> **Company and vendor directory**

Last Updated: 2026-01-07

---

## Overview

This MOC provides comprehensive views of organizations you work with - internal divisions, vendors, partners, and consultancies. Use this to track relationships, projects, and key contacts.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[MOC - People MOC]] - View people by organization
- [[MOC - Projects MOC]] - View projects by organization

---

## 📊 All Organisations

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  type as "Type",
  industry as "Industry",
  relationship as "Relationship"
FROM ""
WHERE type = "Organisation"
SORT file.name ASC
```

---

## 🏷️ By Relationship Type

### Internal Divisions

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  industry as "Industry",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND (relationship = "internal" OR contains(tags, "internal"))
SORT file.name ASC
```

**Your Organization:** These are internal business units, divisions, or departments.

### Vendors & Suppliers

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  industry as "Industry",
  description as "Description",
  contract as "Contract Status"
FROM ""
WHERE type = "Organisation"
  AND (relationship = "vendor" OR contains(tags, "vendor"))
SORT file.name ASC
```

**Vendor Relationships:** Companies providing products or services under contract.

### Partners & Integrators

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  industry as "Industry",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND (relationship = "partner" OR contains(tags, "partner"))
SORT file.name ASC
```

**Strategic Partners:** Companies with collaborative relationships, system integrators, consultancies.

### Consultants

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  industry as "Industry",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND (relationship = "consultant" OR contains(tags, "consultant"))
SORT file.name ASC
```

**Consulting Firms:** Advisory and implementation consultancies.

---

## 🏭 By Industry

### Technology & Software

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND (contains(industry, "Technology") OR contains(industry, "Software"))
SORT file.name ASC
```

### Cloud & Infrastructure

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND (contains(industry, "Cloud") OR contains(industry, "Infrastructure"))
SORT file.name ASC
```

### Consulting & Services

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  description as "Description"
FROM ""
WHERE type = "Organisation"
  AND contains(industry, "Consulting")
SORT file.name ASC
```

---

## 👥 People by Organisation

### Contacts per Organization

```dataview
TABLE WITHOUT ID
  organisation as "Organization",
  length(rows) as "Contacts",
  list(rows.file.link) as "People"
FROM ""
WHERE type = "Person"
  AND organisation != null AND organisation != ""
GROUP BY organisation
SORT length(rows) DESC
```

**Network Map:** See which organizations you have the most contacts at.

### Organizations Without Contacts

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  industry as "Industry"
FROM ""
WHERE type = "Organisation"
  AND !any(filter(
    file.inlinks,
    (link) => meta(link).type = "Person"
  ))
SORT file.name ASC
```

**Action:** Consider adding key contacts or archiving if no longer relevant.

---

## 🎯 Projects by Organisation

### Active Projects per Organization

```dataview
TABLE WITHOUT ID
  org as "Organization",
  length(rows) as "Active Projects",
  list(rows.file.link) as "Projects"
FROM ""
WHERE type = "Project"
  AND status = "active"
FLATTEN vendors as org
WHERE org != null AND org != ""
GROUP BY org
SORT length(rows) DESC
```

**Vendor Engagement:** Track which vendors are involved in active projects.

### Project History by Organization

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  length(filter(
    file.inlinks,
    (link) => meta(link).type = "Project"
  )) as "Total Projects"
FROM ""
WHERE type = "Organisation"
SORT length(filter(
  file.inlinks,
  (link) => meta(link).type = "Project"
)) DESC
LIMIT 15
```

**Relationship Depth:** Organizations with most project involvement.

---

## 📅 Recent Interactions

### Meetings with External Organizations (Last 90 Days)

```dataview
TABLE WITHOUT ID
  file.link as "Meeting",
  date as "Date",
  project as "Project",
  attendees as "Attendees"
FROM "+Meetings"
WHERE type = "Meeting"
  AND date >= date(today) - dur(90 days)
  AND any(map(attendees, (a) =>
    !contains(meta(a).organisation, "Your Company")
  ))
SORT date DESC
LIMIT 20
```

**External Engagement:** Recent meetings with vendor/partner representatives.

### Most Frequent External Collaborators

```dataview
TABLE WITHOUT ID
  org as "Organization",
  length(rows) as "Meetings"
FROM "+Meetings"
WHERE type = "Meeting"
FLATTEN attendees as person
WHERE person != null
  AND !contains(meta(person).organisation, "Your Company")
FLATTEN meta(person).organisation as org
WHERE org != null AND org != ""
GROUP BY org
SORT length(rows) DESC
LIMIT 10
```

**Engagement Frequency:** Which external organizations you meet with most.

---

## 📊 Organization Statistics

### Organizations by Type

```dataview
TABLE WITHOUT ID
  relationship as "Relationship Type",
  length(rows) as "Count"
FROM ""
WHERE type = "Organisation"
GROUP BY relationship
SORT length(rows) DESC
```

### Organizations by Industry

```dataview
TABLE WITHOUT ID
  industry as "Industry",
  length(rows) as "Count"
FROM ""
WHERE type = "Organisation"
GROUP BY industry
SORT length(rows) DESC
```

### Organization Engagement Score

Organizations ranked by total interactions (contacts + projects + meetings):

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  length(filter(file.inlinks, (l) => meta(l).type = "Person")) as "Contacts",
  length(filter(file.inlinks, (l) => meta(l).type = "Project")) as "Projects",
  length(filter(file.inlinks, (l) => meta(l).type = "Meeting")) as "Meetings",
  (length(filter(file.inlinks, (l) => meta(l).type = "Person")) +
   length(filter(file.inlinks, (l) => meta(l).type = "Project")) +
   length(filter(file.inlinks, (l) => meta(l).type = "Meeting"))) as "Total Score"
FROM ""
WHERE type = "Organisation"
SORT (length(filter(file.inlinks, (l) => meta(l).type = "Person")) +
      length(filter(file.inlinks, (l) => meta(l).type = "Project")) +
      length(filter(file.inlinks, (l) => meta(l).type = "Meeting"))) DESC
LIMIT 15
```

---

## 🔍 Quality Checks

### Organizations Without Descriptions

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  industry as "Industry"
FROM ""
WHERE type = "Organisation"
  AND (description = null OR description = "")
SORT file.name ASC
```

**Action:** Add brief descriptions for context and searchability.

### Organizations Without Industry Classification

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship"
FROM ""
WHERE type = "Organisation"
  AND (industry = null OR industry = "")
SORT file.name ASC
```

**Action:** Categorize by industry for better filtering.

### Organizations Without Relationship Type

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  industry as "Industry"
FROM ""
WHERE type = "Organisation"
  AND (relationship = null OR relationship = "")
SORT file.name ASC
```

**Action:** Define relationship type (vendor/partner/internal/consultant).

### Stale Organizations (No Interactions in 12+ Months)

```dataview
TABLE WITHOUT ID
  file.link as "Organization",
  relationship as "Relationship",
  modified as "Last Updated"
FROM ""
WHERE type = "Organisation"
  AND modified < date(today) - dur(365 days)
SORT modified ASC
LIMIT 10
```

**Action:** Review for relevance or archive if no longer active.

---

## 📝 Organization Management

### When to Create an Organization Note

**Create for:**
- Vendors you have contracts with
- Strategic partners with ongoing relationships
- Major consultancies you engage
- Internal divisions you collaborate with frequently
- Technology providers (SaaS, cloud, etc.)

**Don't Create for:**
- One-time service providers
- Organizations mentioned once
- Generic tool vendors (unless strategic)

### Organization Note Best Practices

**Key Information to Track:**
- Relationship type (vendor/partner/internal/consultant)
- Industry classification
- Key contacts (link to Person notes)
- Active projects/contracts
- Products/services provided
- Website and contact information
- Notes on working relationship

**Maintenance:**
- Update when contracts change
- Add new contacts as relationships develop
- Link to relevant projects and meetings
- Archive inactive relationships
- Review annually for relevance

### Linking Conventions

**From Other Notes:**
- Link from Person notes: `organisation: "[[Org Name]]"`
- Link from Project notes: `vendors: ["[[Org Name]]"]`
- Mention in Meeting notes when discussing vendor topics
- Reference in ADRs for technology decisions

**In Organization Notes:**
- Link to key contacts (Person notes)
- Link to active projects
- Link to relevant ADRs
- Link to contract/agreement documents (in +Attachments)

---

## 🤝 Vendor Management

### Active Vendor Contracts

**Track:**
- Contract start/end dates
- Services provided
- Key deliverables
- Performance metrics
- Escalation contacts

**Document in Organization note under "Contract Information" section.**

### Vendor Performance Tracking

Create Page notes for vendor assessments:
- `Page - [Vendor Name] Performance Review YYYY-MM.md`
- Link from Organization note
- Update quarterly or annually

### Vendor Onboarding

**New Vendor Checklist:**
1. Create Organization note
2. Add key contacts (Person notes)
3. Document services/products
4. Link to contract documents
5. Add to relevant projects
6. Set review reminders

---

## 🔗 Strategic Partnerships

### Partnership Types

**Technology Partners:**
- Platform providers (cloud, SaaS)
- Integration partners
- Technology vendors

**Service Partners:**
- System integrators
- Managed service providers
- Consultancies

**Document partnership value, joint initiatives, and success metrics in Organization notes.**

---

## 🌐 Industry Landscape

### Competitive Analysis

Track competitors and alternatives:
- Alternative vendors for each category
- Competitive positioning
- Market trends
- Emerging players

**Create Page notes for market analysis:**
- `Page - Cloud Provider Landscape.md`
- `Page - API Gateway Vendor Comparison.md`

Link from relevant Organization notes.

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - People MOC]] - View people by organization
- [[MOC - Projects MOC]] - Projects with vendor involvement
- [[MOC - Weblinks MOC]] - Vendor documentation and resources

**Templates:**
- `+Templates/Organisation.md` - Create new organization note

**Integration:**
- Link organizations from Person notes
- Reference vendors in Project notes
- Mention in Meeting notes
- Cite in ADRs for technology selections

**Best Practices:**
- Create Organization notes for strategic relationships
- Link key contacts via Person notes
- Track contract information and renewal dates
- Review vendor performance quarterly
- Update industry classifications as markets evolve
- Archive inactive relationships to reduce clutter

**Tips:**
- Use Organization notes as hubs linking to all related content
- Track vendor engagement through project and meeting links
- Document lessons learned from vendor relationships
- Maintain contact information for escalations
- Review organization portfolio during strategic planning
