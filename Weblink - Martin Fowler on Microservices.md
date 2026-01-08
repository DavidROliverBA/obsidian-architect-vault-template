---
type: Weblink
title: Martin Fowler on Microservices
created: 2024-02-15
modified: 2024-02-15
tags: [microservices, architecture, reference]
url: https://martinfowler.com/articles/microservices.html
author: James Lewis and Martin Fowler
source: martinfowler.com
---

# Martin Fowler on Microservices

## Source

- **URL:** https://martinfowler.com/articles/microservices.html
- **Author:** James Lewis and Martin Fowler
- **Source:** martinfowler.com
- **Date:** March 2014 (updated regularly)
- **Type:** Foundational article

## Summary

Comprehensive guide to microservices architecture defining characteristics, benefits, and trade-offs. This is one of the seminal articles that popularized the microservices pattern and remains a valuable reference for understanding when (and when not) to use microservices.

**Main Thesis:**
Microservices architecture is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms (HTTP APIs). Each service is built around business capabilities and independently deployable.

## Key Points

**Nine Characteristics of Microservices:**
1. **Componentization via Services** - Components as independently deployable services
2. **Organized Around Business Capabilities** - Cross-functional teams owning full stack
3. **Products not Projects** - Teams own services long-term, not just build and hand off
4. **Smart Endpoints and Dumb Pipes** - Simple protocols (HTTP REST, messaging)
5. **Decentralized Governance** - Teams choose their own tools and technologies
6. **Decentralized Data Management** - Each service manages its own database
7. **Infrastructure Automation** - CI/CD, automated testing, deployment
8. **Design for Failure** - Resilience and graceful degradation expected
9. **Evolutionary Design** - Services can be replaced or deprecated independently

**Benefits:**
- Strong module boundaries
- Independent deployment
- Technology diversity (polyglot architecture)
- Organizational alignment (Conway's Law)

**Costs:**
- Distributed systems complexity
- Operational overhead
- Data consistency challenges
- Network latency and reliability issues
- Increased testing complexity

## Quotes

> "The microservice architectural style is an approach to developing a single application as a suite of small services, each running in its own process and communicating with lightweight mechanisms, often an HTTP resource API."

> "Microservices are not a free lunch. The price you pay is in complexity."

> "Don't even consider microservices unless you have a system that's too complex to manage as a monolith."

> "The microservice community favours an alternative approach: smart endpoints and dumb pipes. Microservice applications aim to be as decoupled and as cohesive as possible - they own their own domain logic."

## Related

**Our Learnings:**
- [[ADR - Microservices vs Monolith Decision]] - Our experience (superseded)
- [[Project - Legacy System Decommission]] - Learned microservices not always best choice

**Related Resources:**
- [[Weblink - AWS Well-Architected Framework]]
- Sam Newman's "Building Microservices" book
- Chris Richardson's Microservices Patterns

**Key Takeaway:**
Microservices solve organizational and scaling challenges but introduce distributed systems complexity. Only adopt when benefits (team autonomy, independent deployment, scale) justify costs (operational complexity, distributed transactions, network overhead).

**Personal Note:**
Re-reading this after our microservices experience ([[ADR - Microservices vs Monolith Decision]]), Fowler's warnings about complexity and "microservice envy" are spot-on. We fell into the trap of copying patterns from large organizations without their context. The section on "Decentralized Governance" requires organizational maturity we didn't have.

**Recommended For:**
- Anyone considering microservices
- Architects designing distributed systems
- Teams transitioning from monolith
- Understanding when NOT to use microservices
