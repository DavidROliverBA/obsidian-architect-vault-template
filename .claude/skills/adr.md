# ADR Creation Skill

Create a new Architecture Decision Record with guided workflow.

## Instructions

When the user invokes `/adr <title>` or asks to create an ADR:

1. **Gather information** (prompt user):
   - ADR title (what decision is being made)
   - Category: technology | architecture | process | security | infrastructure
   - Status: draft | proposed | accepted
   - Project (optional, if ADR is project-specific)

2. **Generate ADR number**:
   - Count existing ADRs: Find all notes with `type: Adr`
   - Next number: Count + 1 (padded to 3 digits)
   - Example: If 12 ADRs exist, new one is ADR-013

3. **Create the note**:
   - Filename: `ADR - [Title].md`
   - Example: `ADR - Use Kubernetes for Container Orchestration.md`
   - Use template: `+Templates/ADR.md`

4. **Populate frontmatter**:
   ```yaml
   type: Adr
   title: "[Title]"
   status: draft  # or proposed based on user input
   category: [technology|architecture|etc]
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   project: "[[Project Name]]"  # if provided
   approvers:
     - Architecture Lead
     - Tech Lead / Principal Architect
     - Security Architect (if applicable)
   externalRef: null  # JIRA ticket, GitHub issue, etc.
   confidence: medium  # low | medium | high
   verified: false
   reviewed: null
   relatedTo: []
   supersedes: []
   dependsOn: []
   tags: [adr]
   ```

5. **Guide user through sections**:
   Provide this guidance in the note:

   **Required Sections:**
   - **Context**: Why is this decision needed? What's the background?
   - **Decision**: What did we decide to do?
   - **Rationale**: Why did we choose this option?
   - **Consequences**: What are the positive and negative impacts?
   - **Alternatives Considered**: What other options did we evaluate?

   **Optional Sections:**
   - Compliance requirements
   - Implementation approach
   - Risks and mitigations
   - Cost analysis
   - Performance implications

6. **Next steps guidance**:
   Inform user:
   ```
   Your ADR is created in draft status.

   Next steps:
   1. Fill out the required sections (Context, Decision, Rationale, Consequences, Alternatives)
   2. Update status to 'proposed' when ready for review
   3. Share with approvers listed in frontmatter
   4. After approval, update status to 'accepted'
   5. Set 'reviewed' date for future reviews (typically 6-12 months)
   ```

## Example Interaction

**User:** `/adr Use GraphQL for API Layer`

**Claude:**
"Creating new ADR for 'Use GraphQL for API Layer'.

- Category? (technology/architecture/process/security/infrastructure)
  → technology
- Initial status? (draft/proposed)
  → draft
- Related to specific project? (optional)
  → [[Project - API Gateway Modernization]]

Generated ADR-013.

Created at `ADR - Use GraphQL for API Layer.md` in draft status.

The template includes all required sections. Fill out Context, Decision, Rationale, Consequences, and Alternatives. Update to 'proposed' status when ready for review."

## ADR Lifecycle

Explain to user if asked:
1. **draft** - Being written
2. **proposed** - Complete, awaiting approval
3. **accepted** - Approved and in force
4. **deprecated** - No longer recommended but still in use
5. **superseded** - Replaced by newer ADR (link via `supersedes` field)

## Tips for Quality ADRs

- **Context**: Explain the problem or opportunity clearly
- **Decision**: Be specific about what was decided
- **Rationale**: Focus on "why" not just "what"
- **Consequences**: Include both positive and negative impacts
- **Alternatives**: Show what else was considered and why rejected
- **Confidence**: Be honest about certainty level
- **Review Date**: Set for 6-12 months to revisit decision

## Error Handling

- If template doesn't exist, provide basic ADR structure
- If unable to count ADRs, use timestamp-based ID
- Sanitize filename (remove special characters)
