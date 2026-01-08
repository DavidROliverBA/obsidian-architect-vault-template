# Acronyms & Terminology Template

Domain-specific acronyms, abbreviations, and terminology for your organization.

## How to Use

Add your organization's acronyms and jargon. Claude loads this when encountering unfamiliar terms.

---

## Technology Acronyms

### Cloud & Infrastructure
- **EC2** - Elastic Compute Cloud (AWS virtual machines)
- **EKS** - Elastic Kubernetes Service (AWS managed Kubernetes)
- **RDS** - Relational Database Service (AWS managed databases)
- **S3** - Simple Storage Service (AWS object storage)
- **IAM** - Identity and Access Management
- **VPC** - Virtual Private Cloud
- **CDN** - Content Delivery Network
- **IaC** - Infrastructure as Code

### Development & Operations
- **CI/CD** - Continuous Integration / Continuous Deployment
- **API** - Application Programming Interface
- **REST** - Representational State Transfer
- **GraphQL** - Graph Query Language
- **gRPC** - gRPC Remote Procedure Call
- **YAML** - YAML Ain't Markup Language
- **JSON** - JavaScript Object Notation
- **SDK** - Software Development Kit

### Data & Analytics
- **ETL** - Extract, Transform, Load
- **ELT** - Extract, Load, Transform
- **OLTP** - Online Transaction Processing
- **OLAP** - Online Analytical Processing
- **DW** - Data Warehouse
- **BI** - Business Intelligence
- **ML** - Machine Learning
- **AI** - Artificial Intelligence

---

## Architecture Patterns

- **ADR** - Architecture Decision Record
- **CQRS** - Command Query Responsibility Segregation
- **SAGA** - Distributed transaction pattern
- **SLA** - Service Level Agreement
- **SLO** - Service Level Objective
- **SLI** - Service Level Indicator
- **RTO** - Recovery Time Objective
- **RPO** - Recovery Point Objective
- **HA** - High Availability
- **DR** - Disaster Recovery

---

## Security & Compliance

- **SSO** - Single Sign-On
- **MFA** - Multi-Factor Authentication
- **OAuth** - Open Authorization
- **OIDC** - OpenID Connect
- **JWT** - JSON Web Token
- **TLS** - Transport Layer Security
- **SSL** - Secure Sockets Layer (deprecated, use TLS)
- **PII** - Personally Identifiable Information
- **GDPR** - General Data Protection Regulation
- **SOC 2** - Service Organization Control 2
- **HIPAA** - Health Insurance Portability and Accountability Act
- **PCI-DSS** - Payment Card Industry Data Security Standard

---

## Organizational Terms

### Departments
- **IT** - Information Technology
- **R&D** - Research and Development
- **HR** - Human Resources
- **P&L** - Profit and Loss

### Roles
- **PM** - Product Manager or Project Manager (context-dependent)
- **TPM** - Technical Program Manager
- **EM** - Engineering Manager
- **IC** - Individual Contributor
- **SME** - Subject Matter Expert
- **DRI** - Directly Responsible Individual

---

## Project-Specific Terms

### Project Alpha (Cloud Migration)
- **Lift and Shift** - Move applications without re-architecture
- **Refactor** - Re-architect for cloud-native patterns
- **Landing Zone** - Standard account structure and networking

### Project Beta (API Gateway)
- **Rate Limiting** - Restrict API calls per time period
- **Circuit Breaker** - Fault tolerance pattern
- **Blue-Green Deployment** - Zero-downtime deployment strategy

---

## Industry-Specific Terms

*Replace with your industry's terminology:*

### Example: Financial Services
- **KYC** - Know Your Customer
- **AML** - Anti-Money Laundering
- **ACH** - Automated Clearing House
- **Wire Transfer** - Electronic funds transfer

### Example: Healthcare
- **EHR** - Electronic Health Record
- **HL7** - Health Level 7 (data standard)
- **FHIR** - Fast Healthcare Interoperability Resources

### Example: Retail/E-Commerce
- **SKU** - Stock Keeping Unit
- **POS** - Point of Sale
- **OMS** - Order Management System

---

## Customization Instructions

1. **Add your acronyms**: Include all domain-specific terms
2. **Define clearly**: Write definitions for non-technical stakeholders
3. **Organize by category**: Group related terms
4. **Update regularly**: Add new terms as they emerge
5. **Include context**: Note when terms have multiple meanings

## Usage by Claude

When user asks or mentions:
- "What does EKS mean?" → Claude explains Elastic Kubernetes Service
- "We need to improve our RTO" → Claude knows it's Recovery Time Objective
- "Set up SSO" → Claude knows it's Single Sign-On
- References project-specific jargon → Claude understands context

**Benefits:**
- Consistent terminology usage
- Quick definitions without searching
- Onboarding efficiency
- Cross-team communication
