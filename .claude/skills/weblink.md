---
context: fork
---

# Weblink Capture Skill

Save a URL with AI-generated summary and analysis.

## Instructions

When the user invokes `/weblink <url>` or asks to save a URL:

1. **Fetch and analyze the URL**:
   - Use WebFetch tool to retrieve content
   - Extract: title, author, publication date, domain
   - Generate: summary, key points, relevance

2. **Create the note**:
   - Filename: `Weblink - [Title].md`
   - Example: `Weblink - AWS Well-Architected Framework.md`
   - Use template: `+Templates/Weblink.md`

3. **Populate frontmatter**:
   ```yaml
   type: Weblink
   title: "[Page Title]"
   url: "[Full URL]"
   domain: "[example.com]"
   author: "[Author Name]"  # if available
   source: "[Publication/Site Name]"
   createdAt: [ISO timestamp from page]
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   tags: [weblink, <inferred-topics>]
   ```

4. **Generate content sections**:
   - **Summary**: 2-3 sentence overview in your own words
   - **Key Points**: Bullet list of main takeaways
   - **Relevance**: Why this is valuable for your work
   - **Quotes**: Notable excerpts (if any)
   - **Related**: Links to relevant vault notes (projects, ADRs, etc.)

5. **Suggest connections**:
   - Search vault for related content
   - Suggest linking from: relevant Project notes, ADRs, Page notes
   - Suggest tags based on content

## Example Interaction

**User:** `/weblink https://aws.amazon.com/architecture/well-architected/`

**Claude:**
*Fetches and analyzes content*

"Created weblink note at `Weblink - AWS Well-Architected Framework.md`.

**Summary:** AWS Well-Architected Framework provides architectural best practices across six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

**Key Points:**
- Framework for evaluating cloud architectures
- Six pillars of well-architected workloads
- Questions and best practices for each pillar
- Regular reviews recommended

**Suggested connections:**
- Link from [[MOC - Cloud Architecture]]
- Reference in [[Project - Cloud Migration]]
- Related to [[ADR - Use Kubernetes for Container Orchestration]]

Would you like me to add this link to any of these notes?"

## When to Save Weblinks

**Save for:**
- Valuable articles you'll reference multiple times
- Official documentation for technologies you use
- Best practices guides
- Case studies relevant to your work
- Research papers and technical deep dives

**Don't Save:**
- News articles (ephemeral content)
- Resources you won't revisit
- Content duplicated elsewhere
- Simple Stack Overflow answers (copy code to notes instead)

## Integration with Vault

Explain to user:
- **Reference in ADRs**: Support decisions with external sources
- **Link from projects**: Add to project documentation
- **Tag by topic**: Use hierarchical tags for organization
- **Update regularly**: Check for dead links periodically

## Error Handling

- If URL is inaccessible, create note with basic info and note fetch failure
- If WebFetch fails, create note with URL and prompt user to add content manually
- Handle redirects gracefully
- Sanitize title for filename
