# Architecture Context Template

Architecture principles, patterns, governance, and standards for your organization.

## How to Use

Document your architecture framework, principles, and governance model. Claude loads this for architecture questions.

---

## Architecture Principles

### 1. Simplicity Over Complexity
- Choose the simplest solution that meets requirements
- Avoid over-engineering for scale you don't have yet
- Prefer boring, proven technology over new, exciting tech
- **Reference:** [[Page - Architecture Principles]]

### 2. Build vs Buy vs Rent
- **Buy/Rent:** Commodity capabilities (auth, payments, email)
- **Build:** Core differentiators and unique business logic
- **Evaluation criteria:** TCO, time to market, maintenance burden

### 3. Security by Default
- Encrypt data at rest and in transit
- Principle of least privilege for access control
- Security reviews required for all new systems
- **Reference:** [[Page - Security Standards]]

### 4. Design for Failure
- Assume everything fails eventually
- Implement circuit breakers, retries, timeouts
- Graceful degradation over complete failure
- Regular chaos engineering exercises

### 5. Data is an Asset
- Treat data as a valuable company asset
- Data governance framework enforced
- Data quality metrics tracked
- **Reference:** [[Page - Data Governance Framework]]

### 6. Measure Everything
- Instrument all systems with metrics, logs, traces
- SLOs defined for critical systems
- Performance baselines established
- Cost tracking by service/team

### 7. APIs are Contracts
- Backward compatibility required
- Versioning strategy documented
- API design reviews mandatory
- **Reference:** [[Page - API Standards]]

### 8. Automate Repetition
- Infrastructure as Code (Terraform)
- GitOps deployment workflows
- Automated testing (unit, integration, e2e)
- CI/CD for all services

---

## Architecture Patterns in Use

### Microservices
- **When:** Independent scaling, team autonomy needed
- **Tradeoff:** Operational complexity vs deployment flexibility
- **Standard:** [[ADR - Microservices vs Monolith Decision]]

### Event-Driven Architecture
- **When:** Asynchronous processing, loose coupling
- **Tools:** SQS, SNS, EventBridge, Kafka (evaluation)
- **Pattern:** Event sourcing for audit trails

### API Gateway Pattern
- **Purpose:** Centralized routing, auth, rate limiting
- **Implementation:** Kong (current), AWS API Gateway (serverless)
- **Standard:** [[ADR - Adopt GraphQL for API Layer]]

### CQRS (Command Query Responsibility Segregation)
- **When:** Read/write performance requirements differ
- **Implementation:** Separate read models from write models
- **Use case:** High-read analytics dashboards

### Strangler Fig Pattern
- **Purpose:** Gradually replace legacy systems
- **Approach:** Route traffic incrementally to new system
- **Active:** [[Project - Legacy System Decommission]]

---

## Technology Standards

### Approved for All New Projects
- **Languages:** Python, TypeScript/Node.js
- **Databases:** PostgreSQL (RDBMS), DynamoDB (NoSQL)
- **Cloud:** AWS (standard), Azure (limited cases)
- **Containers:** Docker + Kubernetes (EKS)
- **IaC:** Terraform

### Pilot / Limited Use (Requires Approval)
- **Languages:** Go (performance-critical services only)
- **Databases:** MongoDB (specific document use cases)
- **APIs:** GraphQL (pilot projects)

### Deprecated (Migration Required)
- **Databases:** MySQL → PostgreSQL
- **CI/CD:** Jenkins → GitHub Actions
- **Monitoring:** Legacy tools → Prometheus/Grafana

---

## Governance Model

### Architecture Review Board
- **Members:** Jane Smith (Head of Architecture), Marcus Chen, Alex Johnson
- **Frequency:** Bi-weekly
- **Scope:** Review all ADRs, major technology decisions
- **Process:** Submit ADR 3 days before meeting

### ADR Workflow
1. Engineer creates ADR in **draft** status
2. Team reviews and refines
3. Update status to **proposed**
4. Submit to Architecture Review Board
5. Board approves/rejects/requests changes
6. Update status to **accepted** if approved
7. Set review date (6-12 months)

### Security Reviews
- **When:** All new systems, public APIs, PII handling
- **Reviewer:** Michael Torres (Security Architect)
- **Checklist:** [[Page - Security Review Checklist]]
- **Timeline:** 1 week lead time

### Cost Approval
- **Threshold:** $5k/month or $50k/year
- **Approver:** Engineering Manager (Alex Johnson)
- **Process:** Cost estimate in ADR, quarterly review

---

## Quality Attributes (Architecture Characteristics)

### Performance
- **API Response:** p95 < 200ms
- **Page Load:** p95 < 2 seconds
- **Batch Jobs:** Defined SLAs per pipeline

### Scalability
- **Horizontal:** Auto-scaling for stateless services
- **Vertical:** Database sizing based on usage patterns
- **Testing:** Load tests before production launch

### Reliability
- **Availability:** 99.9% uptime for critical systems
- **MTTR:** Mean time to recovery < 1 hour
- **Backups:** Daily backups, 30-day retention

### Security
- **Encryption:** TLS 1.2+ for transit, AES-256 for rest
- **Auth:** OAuth 2.0 + OIDC standard
- **Scanning:** Automated dependency and container scanning

### Maintainability
- **Documentation:** ADRs for decisions, READMEs for repos
- **Code Review:** Required for all changes
- **Testing:** 80% code coverage target

---

## Compliance Requirements

### GDPR (if applicable)
- Data residency in EU regions
- Right to erasure implementation
- Data processing agreements with vendors
- **Reference:** [[Page - GDPR Compliance Checklist]]

### SOC 2 (if applicable)
- Access control policies
- Change management process
- Incident response plan
- Annual audit

---

## Architecture Documentation Standards

### System Documentation
- **Architecture diagrams:** Use C4 model (Context, Container, Component, Code)
- **Tools:** Lucidchart, draw.io, Mermaid
- **Storage:** +Attachments folder, linked from ADRs/Projects

### ADR Standards
- **Template:** [[+Templates/ADR.md]]
- **Sections:** Context, Decision, Rationale, Consequences, Alternatives
- **Approval:** All ADRs reviewed by Architecture Board
- **Review:** Accepted ADRs reviewed every 6-12 months

---

## Customization Instructions

1. **Add your principles**: Document your organization's architecture principles
2. **List patterns**: Note which patterns you use and when
3. **Define governance**: Explain your review and approval processes
4. **Set standards**: Document technology standards and approval tiers
5. **Link ADRs**: Reference actual ADR notes for key decisions

## Usage by Claude

When user asks:
- "What are our architecture principles?" → Claude lists from this file
- "Can I use MongoDB?" → Claude knows it requires approval
- "How do I get an ADR approved?" → Claude explains workflow
- "What's our API response time target?" → Claude knows it's p95 < 200ms

**Benefits:**
- Consistent architecture guidance
- Standards enforcement
- Clear governance processes
- Faster decision-making
