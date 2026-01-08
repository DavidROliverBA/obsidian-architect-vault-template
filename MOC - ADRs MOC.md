---
type: MOC
title: ADRs MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, adr, architecture, decisions]
---

# 📐 ADRs MOC

> **Architecture Decision Records - Track significant technical decisions**

Last Updated: 2026-01-07

---

## Overview

This MOC provides comprehensive views of Architecture Decision Records (ADRs) to track the evolution of technical decisions and architectural patterns.

**What are ADRs?**
Architecture Decision Records document significant architectural and technical decisions, including context, options considered, and rationale. They create an immutable record of why decisions were made.

**Quick Links:**
- [[Dashboard - Dashboard]] - Back to main dashboard
- [[Page - Architecture Principles]] - Decision-making framework
- [[MOC - Projects MOC]] - View ADRs by project

---

## 🎯 ADRs by Status

### Proposed (Pending Approval)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  category as "Category",
  project as "Project",
  created as "Created"
FROM ""
WHERE type = "Adr" AND status = "proposed"
SORT created DESC
```

**Action Required:** Review and approve or reject these ADRs.

### Accepted (In Force)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  category as "Category",
  project as "Project",
  modified as "Last Updated"
FROM ""
WHERE type = "Adr" AND status = "accepted"
SORT modified DESC
```

**Current Standards:** These ADRs represent active architectural decisions.

### Draft (In Progress)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  category as "Category",
  project as "Project",
  created as "Created"
FROM ""
WHERE type = "Adr" AND status = "draft"
SORT created DESC
```

**In Development:** These ADRs are being written and refined.

### Deprecated (Replaced)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  category as "Category",
  project as "Project",
  modified as "Deprecated Date"
FROM ""
WHERE type = "Adr" AND status = "deprecated"
SORT modified DESC
```

### Superseded (Historical)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  category as "Category",
  project as "Project",
  modified as "Superseded Date"
FROM ""
WHERE type = "Adr" AND status = "superseded"
SORT modified DESC
```

**Historical Record:** These ADRs document past decisions and lessons learned.

---

## 🏷️ ADRs by Category

### Technology Decisions

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  project as "Project",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND category = "technology"
SORT status ASC, modified DESC
```

**Scope:** Technology selections (databases, languages, frameworks, tools)

### Architecture Patterns

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  project as "Project",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND category = "architecture"
SORT status ASC, modified DESC
```

**Scope:** Architectural patterns and system design decisions

### Process & Governance

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND category = "process"
SORT status ASC, modified DESC
```

**Scope:** Development processes, workflows, governance

### Security

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  project as "Project",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND category = "security"
SORT status ASC, modified DESC
```

**Scope:** Security architecture, policies, authentication/authorization

### Infrastructure

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  project as "Project",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND category = "infrastructure"
SORT status ASC, modified DESC
```

**Scope:** Infrastructure, deployment, operations, cloud architecture

---

## 🎯 ADRs by Project

### Cloud Migration

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND contains(project, "Cloud Migration")
SORT status ASC, modified DESC
```

### API Gateway Modernization

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND contains(project, "API Gateway")
SORT status ASC, modified DESC
```

### Legacy System Decommission

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND contains(project, "Legacy System")
SORT status ASC, modified DESC
```

### Unassigned to Project

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND (project = null OR project = "")
SORT status ASC, modified DESC
```

**Note:** These may be organization-wide standards not specific to a project.

---

## 🔗 ADR Relationships

### ADRs with Dependencies

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  dependsOn as "Depends On"
FROM ""
WHERE type = "Adr" AND dependsOn != null AND dependsOn != []
SORT status ASC
```

**Dependency Chain:** These ADRs build on other decisions.

### ADRs That Supersede Others

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  supersedes as "Supersedes"
FROM ""
WHERE type = "Adr" AND supersedes != null AND supersedes != []
SORT status ASC
```

**Decision Evolution:** Track how decisions change over time.

### ADRs with Related Decisions

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  relatedTo as "Related To"
FROM ""
WHERE type = "Adr" AND relatedTo != null AND relatedTo != []
SORT status ASC
```

**Decision Network:** See how decisions interconnect.

---

## 📊 Quality Indicators

### High Confidence ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  verified as "Verified"
FROM ""
WHERE type = "Adr" AND confidence = "high"
SORT status ASC, modified DESC
```

**Authoritative:** These decisions are well-validated and proven.

### Medium Confidence ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  verified as "Verified"
FROM ""
WHERE type = "Adr" AND confidence = "medium"
SORT status ASC, modified DESC
```

**Moderate Certainty:** Monitor these decisions for validation.

### Low Confidence ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  verified as "Verified"
FROM ""
WHERE type = "Adr" AND confidence = "low"
SORT status ASC, modified DESC
```

**Uncertain:** These decisions may need revisiting as we learn more.

---

## 📅 Recent Activity

### Recently Created (Last 90 Days)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  created as "Created"
FROM ""
WHERE type = "Adr" AND created >= date(today) - dur(90 days)
SORT created DESC
```

### Recently Updated (Last 30 Days)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr" AND modified >= date(today) - dur(30 days)
SORT modified DESC
```

---

## 🔍 ADR Quality Checks

### ADRs Without Categories

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  created as "Created"
FROM ""
WHERE type = "Adr" AND (category = null OR category = "")
SORT created DESC
```

**Action:** Categorize for better organization and filtering.

### ADRs Without Confidence Ratings

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  created as "Created"
FROM ""
WHERE type = "Adr" AND (confidence = null OR confidence = "")
SORT created DESC
```

**Action:** Add confidence ratings for quality tracking.

### Stale ADRs (Not Reviewed in 12+ Months)

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  reviewed as "Last Reviewed"
FROM ""
WHERE type = "Adr"
  AND status = "accepted"
  AND reviewed < date(today) - dur(365 days)
SORT reviewed ASC
```

**Action:** Review these ADRs - are they still valid and current?

---

## 📊 ADR Statistics

### Status Distribution

```dataview
TABLE WITHOUT ID
  status as "Status",
  length(rows) as "Count"
FROM ""
WHERE type = "Adr"
GROUP BY status
SORT status ASC
```

### Category Distribution

```dataview
TABLE WITHOUT ID
  category as "Category",
  length(rows) as "Count"
FROM ""
WHERE type = "Adr"
GROUP BY category
SORT length(rows) DESC
```

### ADRs by Year

```dataview
TABLE WITHOUT ID
  dateformat(created, "yyyy") as "Year",
  length(rows) as "ADRs Created"
FROM ""
WHERE type = "Adr" AND created != null
GROUP BY dateformat(created, "yyyy")
SORT dateformat(created, "yyyy") DESC
```

---

## 📝 ADR Best Practices

### When to Create an ADR

**Create an ADR for:**
- Technology selections (databases, frameworks, languages)
- Architectural patterns (microservices, event-driven, etc.)
- Security decisions (authentication methods, encryption)
- Major infrastructure choices (cloud providers, deployment strategies)
- Process changes affecting technical work

**Don't Create an ADR for:**
- Trivial implementation details
- Decisions easily reversed
- Personal coding preferences
- Temporary solutions

### ADR Writing Guide

**Essential Sections:**
1. **Context** - Why is this decision needed?
2. **Decision** - What did we decide?
3. **Rationale** - Why did we choose this?
4. **Consequences** - What are the impacts?
5. **Alternatives** - What else did we consider?

**Optional Sections:**
- Compliance requirements
- Implementation approach
- Risks and mitigations
- Cost analysis
- Performance implications

**Template:** Use `+Templates/ADR.md` for consistent structure.

### ADR Lifecycle

1. **Draft** - ADR being written
2. **Proposed** - ADR complete, awaiting approval
3. **Accepted** - ADR approved and in force
4. **Deprecated** - Decision no longer recommended but still in use
5. **Superseded** - Decision replaced by newer ADR

### Review Process

**Before Approval:**
- Technical review by architecture team
- Stakeholder review (affected teams)
- Security review if applicable
- Cost approval if significant budget impact

**After Approval:**
- Communicate decision to affected teams
- Update related documentation
- Link from relevant projects
- Set review date (typically 6-12 months)

---

## 🔗 Decision Tracing

### Find Decisions About...

**Kubernetes:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category"
FROM ""
WHERE type = "Adr"
  AND (contains(title, "Kubernetes") OR contains(tags, "kubernetes"))
SORT status ASC
```

**Databases:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category"
FROM ""
WHERE type = "Adr"
  AND (contains(title, "Database") OR contains(title, "PostgreSQL") OR contains(title, "MySQL") OR contains(tags, "database"))
SORT status ASC
```

**APIs:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category"
FROM ""
WHERE type = "Adr"
  AND (contains(title, "API") OR contains(title, "GraphQL") OR contains(title, "REST"))
SORT status ASC
```

---

## 🎯 Decision Timeline

View how architectural decisions evolved chronologically:

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  created as "Created",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
SORT created DESC
LIMIT 20
```

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - Projects MOC]] - ADRs by project
- [[MOC - Technology & Architecture MOC]] - Technology standards

**Reference:**
- [[Page - Architecture Principles]] - Decision framework
- [[Page - Tech Stack Overview]] - Approved technologies
- Template: `+Templates/ADR.md`

**Governance:**
- Review ADRs monthly for new proposals
- Quarterly review of accepted ADRs
- Annual strategic architecture planning
- Archive superseded ADRs for historical reference

**Tips:**
- Link ADRs from project notes
- Reference ADRs in code comments (URL or title)
- Share ADRs with affected teams after approval
- Use ADRs in onboarding to explain "why we do things this way"
