---
type: MOC
title: Technology & Architecture MOC
created: 2026-01-07
modified: 2026-01-07
tags: [moc, technology, architecture, standards]
---

# 🛠️ Technology & Architecture MOC

> **Technology stack, architectural patterns, and technical standards**

Last Updated: 2026-01-07

---

## Overview

This MOC serves as the hub for all technology and architecture-related content, including standards, ADRs, tech stack documentation, and architectural patterns.

**Quick Links:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[Page - Architecture Principles]] - Core principles
- [[Page - Tech Stack Overview]] - Approved technologies
- [[MOC - ADRs MOC]] - Architecture decisions

---

## 📚 Core Documentation

### Standards & Principles

- [[Page - Architecture Principles]] - Guiding principles for all decisions
- [[Page - Tech Stack Overview]] - Approved technologies and tools
- API Standards (create this page for your organization)
- Security Standards (create this page for your organization)
- Data Standards (create this page for your organization)

### Architecture Documentation

**Create these pages based on your needs:**
- System Architecture Overview
- Deployment Architecture
- Network Architecture
- Security Architecture
- Data Architecture
- Integration Architecture

---

## 🎯 Architecture Decisions

### All ADRs

```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  category as "Category",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
SORT status ASC, modified DESC
```

**Full ADR Library:** See [[MOC - ADRs MOC]] for detailed views.

### Recent Architecture Decisions

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

---

## 🏗️ By Technology Domain

### Cloud & Infrastructure

**ADRs:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
  AND (category = "infrastructure" OR contains(tags, "cloud") OR contains(tags, "kubernetes") OR contains(tags, "aws"))
SORT status ASC, modified DESC
```

**Resources:**
- [[Weblink - AWS Well-Architected Framework]]
- AWS Documentation
- Kubernetes best practices

**Pages to Create:**
- Cloud Infrastructure Design
- Kubernetes Patterns
- Infrastructure as Code Standards

### Databases & Data

**ADRs:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
  AND (contains(tags, "database") OR contains(tags, "postgresql") OR contains(tags, "data"))
SORT status ASC, modified DESC
```

**Key Decision:**
- [[ADR - Standardize on PostgreSQL]]

**Pages to Create:**
- Database Design Patterns
- Data Modeling Standards
- Backup & Recovery Procedures

### APIs & Integration

**ADRs:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
  AND (contains(tags, "api") OR contains(tags, "graphql") OR contains(tags, "integration"))
SORT status ASC, modified DESC
```

**Key Decisions:**
- [[ADR - Adopt GraphQL for API Layer]]

**Pages to Create:**
- API Design Standards
- Authentication & Authorization Patterns
- API Versioning Strategy

### Application Architecture

**ADRs:**
```dataview
TABLE WITHOUT ID
  file.link as "ADR",
  status as "Status",
  modified as "Updated"
FROM ""
WHERE type = "Adr"
  AND (contains(tags, "microservices") OR contains(tags, "architecture-pattern"))
SORT status ASC, modified DESC
```

**Key Decisions:**
- [[ADR - Use Kubernetes for Container Orchestration]]
- [[ADR - Microservices vs Monolith Decision]]

**Resources:**
- [[Weblink - Martin Fowler on Microservices]]

---

## 🏷️ By Technology

### Kubernetes

**ADRs:**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND (contains(title, "Kubernetes") OR contains(tags, "kubernetes"))
SORT status ASC
```

**Pages to Create:**
- Kubernetes Deployment Patterns
- Helm Chart Standards
- Kubernetes Security Best Practices

### PostgreSQL

**ADRs:**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND (contains(title, "PostgreSQL") OR contains(title, "Database") OR contains(tags, "postgresql"))
SORT status ASC
```

**Pages to Create:**
- PostgreSQL Tuning Guide
- Database Migration Procedures
- Query Optimization Patterns

### GraphQL

**ADRs:**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND (contains(title, "GraphQL") OR contains(tags, "graphql"))
SORT status ASC
```

**Pages to Create:**
- GraphQL Schema Design Guide
- GraphQL Performance Optimization
- GraphQL Security Patterns

---

## 📐 Architectural Patterns

### Design Patterns in Use

**Document these based on your architecture:**
- Microservices patterns
- Event-driven architecture
- API gateway patterns
- CQRS (Command Query Responsibility Segregation)
- Saga pattern for distributed transactions
- Circuit breaker pattern
- Strangler fig pattern (legacy migration)

### Anti-Patterns to Avoid

**Learn from mistakes:**
- [[ADR - Microservices vs Monolith Decision]] - Lessons on premature microservices
- Distributed monolith
- God classes/services
- Shared mutable state
- Tight coupling

---

## 🔍 Technology Research

### Active Research Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  priority as "Priority",
  status as "Status"
FROM ""
WHERE type = "Project"
  AND (contains(title, "Research") OR contains(tags, "research"))
SORT status ASC, priority ASC
```

### Emerging Technologies

**Under Evaluation:**
- Service Mesh (Istio, Linkerd)
- Serverless patterns
- Edge computing
- AI/ML infrastructure

**Pages to Create:**
- Technology Radar (ThoughtWorks-style)
- Proof of Concept Results
- Technology Evaluation Framework

---

## 📊 Technology Inventory

### Tech Stack Summary

**See:** [[Page - Tech Stack Overview]] for comprehensive documentation.

**Quick Reference:**
- **Cloud**: AWS (primary)
- **Containers**: Docker + Kubernetes (EKS)
- **Databases**: PostgreSQL (standard), DynamoDB, Redis
- **Languages**: Python, TypeScript, Go
- **Frontend**: React, React Native
- **APIs**: REST (current), GraphQL (pilot)

### Technology Adoption Lifecycle

**Standard (Approved for All New Projects):**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND status = "accepted"
  AND category = "technology"
SORT file.name ASC
```

**Pilot (Limited Use with Approval):**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND status = "proposed"
  AND category = "technology"
SORT file.name ASC
```

**Deprecated (Maintenance Only):**
```dataview
LIST
FROM ""
WHERE type = "Adr"
  AND (status = "deprecated" OR status = "superseded")
  AND category = "technology"
SORT file.name ASC
```

---

## 🎯 Architecture Projects

### Infrastructure Projects

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority"
FROM ""
WHERE type = "Project"
  AND (contains(tags, "infrastructure") OR contains(tags, "cloud") OR contains(tags, "domain/infrastructure"))
SORT status ASC, priority ASC
```

### Platform Engineering

```dataview
TABLE WITHOUT ID
  file.link as "Project",
  status as "Status",
  priority as "Priority"
FROM ""
WHERE type = "Project"
  AND (contains(category, "Platform") OR contains(tags, "platform"))
SORT status ASC, priority ASC
```

---

## 📚 Learning Resources

### Architecture Books

**Recommended Reading:**
- Building Microservices (Sam Newman)
- Designing Data-Intensive Applications (Martin Kleppmann)
- The Phoenix Project (Gene Kim, et al.)
- Site Reliability Engineering (Google)
- Domain-Driven Design (Eric Evans)

### Online Resources

**Essential Weblinks:**
- [[Weblink - Martin Fowler on Microservices]]
- [[Weblink - AWS Well-Architected Framework]]

**Additional Resources:**
- ThoughtWorks Technology Radar
- AWS Architecture Center
- CNCF Landscape
- Microsoft Azure Architecture Center

### Training & Certifications

**Recommended Certifications:**
- AWS Solutions Architect (Associate/Professional)
- Certified Kubernetes Administrator (CKA)
- Certified Kubernetes Application Developer (CKAD)

**Internal Training:**
- Architecture Office Hours (weekly)
- Tech Talks (monthly)
- Workshops (quarterly)

---

## 🔧 Tools & Platforms

### Development Tools

**Standard Tooling:**
- Version Control: GitHub
- CI/CD: GitHub Actions, ArgoCD
- IaC: Terraform
- Containerization: Docker
- API Testing: Postman, Insomnia
- Load Testing: k6, JMeter

### Monitoring & Observability

**Observability Stack:**
- Metrics: Prometheus + Grafana
- Logging: CloudWatch Logs
- Tracing: AWS X-Ray
- APM: DataDog (limited use)
- Dashboards: Grafana

### Security Tools

**Security Tooling:**
- Dependency Scanning: Dependabot, Snyk
- SAST: SonarQube
- Secrets Management: AWS Secrets Manager
- Vulnerability Scanning: Trivy

---

## 📋 Standards & Checklists

### Architecture Review Checklist

**Create page for:**
- Pre-implementation architecture review
- Security review checklist
- Performance review checklist
- Cost review checklist
- Operational readiness review

### Definition of Done

**Technical Standards:**
- Code review completed
- Unit tests (80%+ coverage)
- Integration tests passing
- Security scan clean
- Documentation updated
- ADR created (if applicable)

---

## Related

**Navigation:**
- [[Dashboard - Dashboard]] - Main dashboard
- [[MOC - ADRs MOC]] - All architecture decisions
- [[MOC - Projects MOC]] - Technology projects
- [[MOC - Weblinks MOC]] - External resources

**Key Pages:**
- [[Page - Architecture Principles]] - Decision framework
- [[Page - Tech Stack Overview]] - Approved technologies

**Domain MOCs** (examples you can create):
- [[MOC - Cloud Architecture]] - Cloud-specific patterns
- [[MOC - Data Platform]] - Data engineering
- [[MOC - Security Architecture]] - Security patterns
- [[MOC - Mobile Architecture]] - Mobile app patterns

**Maintenance:**
- Review technology standards quarterly
- Update tech stack documentation when changes occur
- Archive deprecated technology ADRs
- Keep learning resources current
