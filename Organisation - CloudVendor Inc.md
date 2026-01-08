---
type: Organisation
title: CloudVendor Inc
created: 2025-09-01
modified: 2026-01-07
tags: [organisation, vendor, consulting]
website: https://cloudvendor.example.com
industry: Cloud Consulting
relationship: vendor
---

# CloudVendor Inc

## Overview

- **Website:** https://cloudvendor.example.com
- **Industry:** Cloud Consulting & Professional Services
- **Relationship:** Vendor / Consulting Partner
- **Contract Term:** 2025-09-01 to 2026-08-31 (renewable)
- **Primary Contact:** [[Dr. Sarah Chen]]

## Description

CloudVendor Inc is a cloud consulting firm specializing in large-scale cloud migrations and architecture transformation. We engaged them to support [[Project - Cloud Migration]] with their expertise in AWS cloud architecture and migration best practices.

**Services Provided:**
- Cloud migration strategy and roadmap
- AWS Well-Architected Review
- Architecture design and review
- Team training and knowledge transfer
- Migration execution support

**Expertise Areas:**
- AWS cloud architecture
- Large-scale migration projects
- Cost optimization
- Security and compliance
- DevOps and automation

**Engagement Model:**
- Monthly retainer for advisory services
- Additional hours for hands-on migration support
- Knowledge transfer sessions with internal teams

## Key Contacts

```dataview
TABLE role, email AS "Email"
FROM ""
WHERE type = "Person" AND contains(organisation, this.file.name)
SORT role ASC
```

**Primary:** [[Dr. Sarah Chen]] - Principal Consultant
- Email: sarah.chen@cloudvendor.com
- Phone: +1-555-0123
- Specialization: Cloud migration, AWS architecture

**Account Manager:** Michael Torres
- Email: michael.torres@cloudvendor.com
- Phone: +1-555-0124
- Responsibilities: Contract, billing, escalations

## Projects

```dataview
TABLE status, priority
FROM ""
WHERE type = "Project" AND contains(file.outlinks, this.file.link)
SORT status ASC
```

## Deliverables

**Completed:**
- [x] Cloud Readiness Assessment (October 2025)
- [x] AWS Landing Zone Design (November 2025)
- [x] Migration Playbook (December 2025)
- [x] Team Training - AWS Fundamentals (December 2025)

**In Progress:**
- [ ] Application Migration Support (January-June 2026)
- [ ] Architecture Reviews (ongoing)
- [ ] Weekly office hours (ongoing)

**Upcoming:**
- [ ] Cost Optimization Review (March 2026)
- [ ] Security Posture Assessment (April 2026)

## Performance & Satisfaction

**Overall Rating:** 4.5/5

**Strengths:**
- Deep AWS expertise
- Excellent knowledge transfer
- Responsive and collaborative
- Realistic planning and expectations

**Areas for Improvement:**
- Sometimes over-engineers solutions
- Documentation could be more detailed
- Billing transparency could improve

**Testimonials:**
> "Dr. Chen's expertise saved us from several costly mistakes in our landing zone design. Her experience with large-scale migrations has been invaluable." - [[Jane Smith]], Head of Architecture

## Contract & Commercial

**Contract Type:** Time & Materials with monthly retainer
- **Retainer:** $15,000/month (40 hours advisory)
- **Hourly Rate:** $250/hour for additional services
- **Annual Value:** ~$300,000

**Payment Terms:** Net 30
**Renewal Date:** 2026-08-31
**Notice Period:** 90 days

**Insurance:**
- Professional Liability: $5M
- General Liability: $2M
- Cyber Insurance: $3M

## Notes

**2026-01-07:** Mid-engagement review scheduled for end of January. Overall very satisfied with CloudVendor's contribution to the migration. Dr. Chen's guidance has been exceptional.

**2025-12-15:** Team training session well-received. 4.8/5 satisfaction from participants. Recommend continuing knowledge transfer sessions.

**2025-11-01:** AWS landing zone review completed. Identified 12 improvements before production deployment - caught potential security and cost issues early.

**Renewal Considerations:**
- Strong performance to date
- Continue for migration completion (through June 2026)
- Evaluate ongoing advisory needs after migration
- Consider reduced retainer post-migration

## Related

- [[Project - Cloud Migration]] - Primary engagement
- [[Dr. Sarah Chen]] - Principal consultant
- [[MOC - Organisations MOC]]

**Vendor Management:**
- Quarterly business reviews
- Monthly invoice reconciliation
- Annual contract renewal evaluation
