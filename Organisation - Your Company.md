---
type: Organisation
title: Your Company
created: 2025-06-01
modified: 2026-01-07
tags: [organisation, internal]
website: https://example.com
industry: Technology
relationship: internal
---

# Your Company

## Overview

- **Website:** https://example.com
- **Industry:** Technology / Software
- **Relationship:** Internal (our organization)
- **Size:** 500+ employees
- **Founded:** 2010

## Description

Your Company is a technology company providing [describe your business]. The Engineering organization consists of ~100 engineers across Platform, Product, and Data teams.

**Engineering Organization Structure:**
- **Platform Engineering** (20 engineers): Infrastructure, DevOps, SRE
- **Product Engineering** (60 engineers): Customer-facing applications
- **Data Engineering** (15 engineers): Data platform, analytics, ML
- **Architecture** (5 architects): Solutions Architecture, Enterprise Architecture

**Technology Focus:**
- Cloud-native applications (AWS)
- Microservices architecture
- Modern web and mobile applications
- Data-driven decision making
- AI/ML capabilities

**Engineering Culture:**
- Strong documentation culture (ADRs, runbooks)
- Continuous improvement mindset
- Blameless postmortems
- Knowledge sharing (tech talks, office hours)
- Work-life balance emphasis

## Key Contacts

```dataview
TABLE role, email AS "Email"
FROM ""
WHERE type = "Person" AND contains(organisation, this.file.name)
SORT role ASC
```

## Active Projects

```dataview
TABLE status, priority, start-date AS "Start Date"
FROM ""
WHERE type = "Project" AND status = "active"
SORT priority ASC, start-date DESC
```

## Technology Stack

See [[Page - Tech Stack Overview]] for comprehensive technology standards.

**Key Technologies:**
- **Cloud**: AWS (primary)
- **Containers**: Docker + Kubernetes (EKS)
- **Databases**: PostgreSQL (standard), DynamoDB, Redis
- **Languages**: Python, TypeScript, Go
- **Frontend**: React, React Native

## Engineering Principles

See [[Page - Architecture Principles]] for detailed principles.

**Core Values:**
1. Simplicity over complexity
2. Security by default
3. Measure everything
4. Automate repetition

## Notes

**Architecture Governance:**
- Monthly Architecture Board meetings
- ADR process for significant technical decisions
- Quarterly technology reviews
- Annual strategic planning

**Engineering Rituals:**
- Daily standups (team level)
- Weekly engineering all-hands
- Monthly tech talks
- Quarterly retrospectives

**Training & Development:**
- Annual training budget per engineer
- Conference attendance encouraged
- Internal workshop series
- Mentorship program

## Related

- [[MOC - People MOC]] - Team directory
- [[MOC - Projects MOC]] - Current initiatives
- [[MOC - Technology & Architecture MOC]] - Tech standards
