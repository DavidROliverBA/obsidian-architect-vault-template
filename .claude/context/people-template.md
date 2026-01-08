# People & Teams Context Template

Quick reference for key people, teams, and organizational structure.

## How to Use

Replace examples with your organization's people and teams. Claude loads this when users ask about people, teams, or stakeholders.

---

## Leadership

### Architecture Team
- **Jane Smith** - Head of Architecture
  - Focus: Enterprise architecture, standards, governance
  - Contact: jane.smith@company.com
  - Note: [[Jane Smith]]

- **Marcus Chen** - Principal Solution Architect
  - Focus: Cloud architecture, security
  - Contact: marcus.chen@company.com

### Engineering Leadership
- **Alex Johnson** - Senior Engineering Manager
  - Focus: Platform engineering, DevOps
  - Teams: 4 engineering teams (30 engineers)
  - Contact: alex.johnson@company.com
  - Note: [[Alex Johnson]]

---

## Key Teams

### Platform Engineering Team
- **Lead:** Alex Johnson
- **Size:** 8 engineers
- **Focus:** Infrastructure, Kubernetes, CI/CD
- **Slack:** #platform-eng

### Data Engineering Team
- **Lead:** Lisa Park
- **Size:** 6 engineers
- **Focus:** Data pipelines, analytics, data platform
- **Slack:** #data-eng

### API Team
- **Lead:** David Kumar
- **Size:** 5 engineers
- **Focus:** API gateway, GraphQL, integration
- **Slack:** #api-team

---

## External Consultants

### Dr. Sarah Chen - CloudVendor Inc
- **Role:** Cloud Architecture Consultant
- **Expertise:** AWS, Kubernetes, cost optimization
- **Engagement:** Part-time, ad-hoc advisory
- **Contact:** sarah.chen@cloudvendor.com
- **Note:** [[Dr. Sarah Chen]]

### Michael Torres - Security Consultant
- **Role:** Security Architect
- **Expertise:** Application security, compliance
- **Engagement:** Quarterly security reviews
- **Contact:** michael.torres@securityco.com

---

## Stakeholder Matrix

### Project Approvers
- **Technical Decisions:** Jane Smith (Head of Architecture)
- **Budget/Resources:** Alex Johnson (Engineering Manager)
- **Security:** Michael Torres (Security Architect)
- **Compliance:** Legal team (legal@company.com)

### ADR Approvers
- **Architecture ADRs:** Jane Smith, Marcus Chen
- **Technology ADRs:** Marcus Chen, Alex Johnson
- **Security ADRs:** Jane Smith, Michael Torres

---

## On-Call Rotation

### Platform Team On-Call
- **Primary:** Rotating weekly (see PagerDuty)
- **Escalation:** Alex Johnson
- **Slack:** #incidents

### Application Support
- **Primary:** Rotating daily
- **Escalation:** Team leads
- **Slack:** #app-support

---

## Vendor Contacts

### AWS Account Team
- **Account Manager:** Jennifer Lee (jennifer.lee@amazon.com)
- **Solutions Architect:** Bob Williams (bob.w@amazon.com)

### Key Vendors
- **CloudVendor Inc:** Main consulting partner
- **Security Co:** Security assessments
- **Data Tools Inc:** Analytics platform vendor

---

## Customization Instructions

1. **Add your people**: Replace examples with actual team members
2. **Update teams**: Document your org structure
3. **Link notes**: Create Person notes for key individuals
4. **Keep current**: Update when people change roles
5. **Add contact info**: Include email, Slack, phone as appropriate

## Usage by Claude

When user asks:
- "Who's our head of architecture?" → Jane Smith
- "Who should approve this ADR?" → Claude knows approval workflow
- "Who's on the platform team?" → Claude lists team members
- "How do I contact AWS support?" → Claude provides account manager info

**Benefits:**
- Quick stakeholder identification
- Correct approval routing
- Team structure clarity
- Contact information readily available
