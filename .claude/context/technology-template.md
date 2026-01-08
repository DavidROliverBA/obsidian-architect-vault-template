# Technology Stack Context Template

This file provides Claude Code with quick context about your technology stack and standards. Update with your organization's technologies.

## How to Use This File

Replace the example content below with your actual tech stack. Claude will load this file when users ask about technologies, architecture, or standards.

---

## Cloud Platforms

### Primary Cloud
**AWS** (Amazon Web Services)
- Regions: us-east-1 (primary), us-west-2 (DR)
- Services: EC2, ECS, EKS, S3, RDS, Lambda, API Gateway
- IAM: Centralized with SSO integration

### Other Clouds (if applicable)
- Azure: Limited use for specific SaaS integrations
- GCP: Not currently used

---

## Compute & Container Orchestration

### Containers
- **Docker** - Standard container runtime
- **Amazon EKS** - Managed Kubernetes for production
- **ECR** - Container registry

### Serverless
- **AWS Lambda** - Event-driven functions
- **Step Functions** - Workflow orchestration

### Virtual Machines
- **EC2** - Legacy applications, specific workloads

---

## Databases & Data Storage

### Relational Databases
- **PostgreSQL** (Standard) - Primary RDBMS for new applications
  - Version: 14+
  - Hosting: Amazon RDS
  - [[ADR - Standardize on PostgreSQL]]

### NoSQL Databases
- **DynamoDB** - Serverless applications, high-scale key-value
- **Redis** - Caching, session storage
- **MongoDB** - Document storage (limited use cases)

### Data Warehouse
- **Redshift** - Analytics and reporting
- **S3 + Athena** - Data lake queries

### Object Storage
- **Amazon S3** - All file storage, data lake foundation

---

## APIs & Integration

### API Standards
- **REST** - Current standard for most APIs
- **GraphQL** - Pilot phase ([[ADR - Adopt GraphQL for API Layer]])
- **gRPC** - Service-to-service communication (limited use)

### API Gateway
- **Kong** - API management platform (current evaluation)
- **AWS API Gateway** - Serverless APIs

### Messaging & Events
- **Amazon SQS** - Asynchronous messaging
- **Amazon SNS** - Pub/sub notifications
- **Amazon EventBridge** - Event bus
- **Apache Kafka** - Under evaluation for event streaming

---

## Frontend Technologies

### Web Applications
- **React** - Standard frontend framework
- **TypeScript** - Preferred over JavaScript
- **Next.js** - Server-side rendering (new projects)

### Mobile Applications
- **React Native** - Cross-platform mobile development

### State Management
- **Redux Toolkit** - Complex state
- **React Context** - Simple state

---

## Backend Technologies

### Languages
- **Python** - Primary backend language, data engineering
- **TypeScript/Node.js** - API services, serverless functions
- **Go** - High-performance services (limited use)
- **Java** - Legacy systems only

### Frameworks
- **FastAPI** (Python) - REST APIs
- **Express** (Node.js) - Web services
- **Django** (Python) - Full-stack applications (legacy)

---

## Infrastructure as Code

### Primary Tool
- **Terraform** - All infrastructure provisioning
  - Version: 1.5+
  - State: S3 backend with DynamoDB locking

### Other Tools
- **CloudFormation** - AWS-specific resources (limited use)
- **AWS CDK** - Under evaluation

---

## CI/CD & DevOps

### Version Control
- **GitHub** - Source code, pull requests, code review

### CI/CD
- **GitHub Actions** - Build and test pipelines
- **ArgoCD** - GitOps deployment to Kubernetes

### Artifact Storage
- **Amazon ECR** - Container images
- **S3** - Build artifacts

---

## Monitoring & Observability

### Metrics
- **Prometheus** - Metrics collection
- **Grafana** - Visualization and dashboards

### Logging
- **CloudWatch Logs** - Centralized logging
- **ELK Stack** - Under evaluation

### Tracing
- **AWS X-Ray** - Distributed tracing

### APM
- **DataDog** - Limited use, cost evaluation ongoing

---

## Security Tools

### Secrets Management
- **AWS Secrets Manager** - Application secrets
- **Parameter Store** - Configuration values

### Scanning
- **Snyk** - Dependency scanning
- **SonarQube** - Static code analysis
- **Trivy** - Container vulnerability scanning

### Identity & Access
- **AWS IAM** - Cloud access control
- **OAuth 2.0 + OpenID Connect** - Application authentication
- **Okta** - Identity provider (SSO)

---

## Development Tools

### IDEs
- VS Code - Standard editor
- IntelliJ IDEA - Java development (legacy)

### API Testing
- Postman - Manual API testing
- Insomnia - Alternative API client

### Load Testing
- k6 - Performance testing
- JMeter - Legacy load tests

---

## Standards & Decisions

### Active ADRs
- [[ADR - Use Kubernetes for Container Orchestration]]
- [[ADR - Standardize on PostgreSQL]]
- [[ADR - Adopt GraphQL for API Layer]] (proposed)

### Deprecated Technologies
- **MySQL** → Migrating to PostgreSQL
- **MongoDB** → Limited to specific use cases only
- **Jenkins** → Replaced by GitHub Actions

---

## Customization Instructions

1. **Update with your stack**: Replace all example technologies with your actual tools
2. **Link ADRs**: Ensure technology decisions reference relevant ADR notes
3. **Keep current**: Update when adopting new tools or deprecating old ones
4. **Add versions**: Note minimum versions or standards
5. **Document exceptions**: Note when/why non-standard tools are used

## Usage by Claude

When user asks:
- "What database should I use?" → Claude recommends PostgreSQL per standard
- "How do we deploy to Kubernetes?" → Claude knows you use ArgoCD
- "What's our CI/CD tool?" → Claude knows it's GitHub Actions
- "Can we use MongoDB?" → Claude knows it's limited use only

**Benefits:**
- Consistent technology recommendations
- Quick answers without searching ADRs
- Standards enforcement
- Onboarding efficiency
