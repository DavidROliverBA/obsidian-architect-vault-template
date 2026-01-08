---
type: Weblink
title: AWS Well-Architected Framework
created: 2025-09-01
modified: 2025-09-01
tags: [aws, architecture, cloud, reference, best-practices]
url: https://aws.amazon.com/architecture/well-architected/
author: AWS
source: aws.amazon.com
---

# AWS Well-Architected Framework

## Source

- **URL:** https://aws.amazon.com/architecture/well-architected/
- **Author:** Amazon Web Services
- **Source:** aws.amazon.com
- **Date:** Updated regularly (latest 2023)
- **Type:** Best practices framework

## Summary

The AWS Well-Architected Framework provides a consistent approach for customers and partners to evaluate architectures and implement scalable designs. It consists of six pillars that represent different focuses for architecting workloads in the cloud.

**Purpose:**
- Evaluate cloud architectures against AWS best practices
- Identify architectural risks and areas for improvement
- Build secure, high-performing, resilient, and efficient infrastructure

**Tool:** AWS provides a Well-Architected Tool for self-service architecture reviews.

## Key Points

**Six Pillars:**

1. **Operational Excellence**
   - Operations as code
   - Frequent, small, reversible changes
   - Anticipate failure
   - Learn from operational events

2. **Security**
   - Implement strong identity foundation
   - Enable traceability
   - Apply security at all layers
   - Automate security best practices
   - Protect data in transit and at rest
   - Prepare for security events

3. **Reliability**
   - Automatically recover from failure
   - Test recovery procedures
   - Scale horizontally
   - Stop guessing capacity
   - Manage change through automation

4. **Performance Efficiency**
   - Use advanced technologies (go serverless where appropriate)
   - Go global in minutes
   - Use serverless architectures
   - Experiment more often
   - Mechanical sympathy (understand how cloud services work)

5. **Cost Optimization**
   - Implement cloud financial management
   - Adopt consumption model
   - Measure overall efficiency
   - Stop spending on undifferentiated heavy lifting
   - Analyze and attribute expenditure

6. **Sustainability** (added 2021)
   - Understand your impact
   - Establish sustainability goals
   - Maximize utilization
   - Use managed services
   - Reduce downstream impact

**Design Principles (General):**
- Stop guessing your capacity needs
- Test systems at production scale
- Automate to make architectural experimentation easier
- Allow for evolutionary architectures
- Drive architectures using data
- Improve through game days

## Quotes

> "The AWS Well-Architected Framework helps you understand the pros and cons of decisions you make while building systems on AWS."

> "By adopting the practices in this framework, you can build architectures that are secure, reliable, efficient, cost-effective, and sustainable."

> "Architecture is not a one-time event. As your workload evolves, so should your architecture."

## Related

**Our Application:**
- [[ADR - Use Kubernetes for Container Orchestration]] - Reliability pillar (self-healing)
- [[ADR - Standardize on PostgreSQL]] - Cost optimization pillar
- [[Project - Cloud Migration]] - Using framework for migration planning
- [[Page - Architecture Principles]] - Informed by Well-Architected Framework

**How We Use It:**
1. **Architecture Reviews**: Quarterly reviews of major systems
2. **New Projects**: Well-Architected Review in planning phase
3. **Migration Planning**: Assessment of on-prem systems before cloud migration
4. **Training**: Framework used in architecture training program

**Related AWS Resources:**
- AWS Architecture Center
- AWS Solutions Library
- AWS Reference Architectures
- AWS Prescriptive Guidance

**Personal Notes:**

**Reliability Pillar:** Most relevant for our [[Project - Cloud Migration]]. Key takeaways:
- Multi-AZ deployments standard
- Automated backups with tested restore
- Chaos engineering to validate resilience

**Cost Optimization:** Regular reviews identified:
- Rightsizing opportunities (saved $15K/month)
- Reserved Instance purchases (20% discount)
- S3 lifecycle policies (40% storage cost reduction)

**Security Pillar:** Influenced our approach to:
- IAM least-privilege policies
- Encryption by default
- Network segmentation
- Security monitoring and alerting

**Performance Efficiency:** Led to adoption of:
- Auto-scaling for variable workloads
- CloudFront CDN for global performance
- ElastiCache for database offloading

**Recommended Reading Order:**
1. Start with overview and design principles
2. Read pillars relevant to immediate concerns
3. Use Well-Architected Tool for structured review
4. Engage AWS Solutions Architect for deep dive

**Caution:**
Framework is AWS-centric and may recommend AWS-specific services over alternatives. Use as guidance, not prescriptive rules. Some recommendations may not apply to small-scale deployments.
