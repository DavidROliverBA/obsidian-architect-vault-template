# Find Orphaned Notes Skill

Identify notes with no backlinks (potential isolated content).

## Instructions

When the user invokes `/orphans` or asks to find orphaned notes:

1. **Use Task tool to launch exploration agent**:
   - Create comprehensive search for notes with zero backlinks
   - Exclude: MOCs, Daily notes, Templates, system folders
   - Group by note type

2. **Analysis to perform**:
   - Count total orphaned notes
   - Categorize by type (Project, ADR, Page, etc.)
   - Identify age of orphaned notes (older = more concerning)
   - Suggest integration strategies

3. **Report format**:
   ```markdown
   # Orphaned Notes Report

   **Total Orphaned:** X notes
   **Last Run:** YYYY-MM-DD

   ## Summary by Type
   - Projects: X notes
   - ADRs: X notes
   - Pages: X notes
   - Tasks: X notes
   - People: X notes
   - Other: X notes

   ## Recommendations

   ### High Priority (Archive or Integrate)
   [Older notes with no connections]

   ### Medium Priority (Review)
   [Recent notes that may need linking]

   ### Low Priority (Monitor)
   [Intentionally standalone content]
   ```

4. **Provide actionable recommendations**:
   - **Archive**: Move to archive folder if no longer relevant
   - **Integrate**: Add links from relevant notes
   - **Delete**: Remove if truly obsolete
   - **Keep**: Some notes (reference docs) are OK orphaned

## Example Interaction

**User:** `/orphans`

**Claude:**
"Searching for orphaned notes (notes with no backlinks)...

Found 8 orphaned notes:

**Projects (2):**
- [[Project - Research - Event-Driven Architecture]] (paused, 60 days old)
  → Recommendation: Link from [[MOC - Cloud Architecture]] or archive if research complete
- [[Project - Mobile App Prototype]] (completed, 180 days old)
  → Recommendation: Archive to keep vault clean

**Pages (3):**
- [[Page - Database Migration Checklist]] (45 days old)
  → Recommendation: Link from [[ADR - Standardize on PostgreSQL]]
- [[Page - Onboarding Guide]] (30 days old)
  → Recommendation: Link from [[Dashboard - Dashboard]]
- [[Page - API Standards]] (90 days old)
  → Recommendation: Link from [[MOC - Technology & Architecture MOC]]

**ADRs (1):**
- [[ADR - Microservices vs Monolith Decision]] (superseded)
  → Recommendation: This is OK - superseded ADRs can be orphaned

**Tasks (2):**
- [[Task - Research GraphQL alternatives]] (completed, 120 days old)
  → Recommendation: Archive or delete
- [[Task - Update documentation]] (completed, 90 days old)
  → Recommendation: Delete if done

**Actions to take:**
1. Archive completed projects and tasks
2. Link Page notes from relevant MOCs
3. Review paused projects for relevance

Would you like me to help link any of these notes?"

## What Makes a Note an Orphan?

**Criteria:**
- Zero backlinks (no other notes link to it)
- Not a MOC (MOCs are navigation hubs)
- Not a Daily note (standalone by nature)
- Not in +Templates folder

**Not Necessarily Bad:**
- Reference documentation may stand alone
- Recently created notes haven't been linked yet
- Completed projects may naturally orphan over time

## Integration Strategies

**For Projects:**
- Link from relevant MOCs
- Link from team member Person notes
- Link from related ADRs

**For ADRs:**
- Link from Project notes that implement them
- Link from technology MOCs
- Cross-link related ADRs

**For Pages:**
- Link from MOCs
- Link from Project notes as documentation
- Cross-reference in ADRs

**For Tasks:**
- Archive completed tasks older than 90 days
- Link active tasks to projects
- Delete obsolete tasks

## Regular Maintenance

Suggest to user:
"Run `/orphans` monthly to keep vault connected. Goal is <5% orphaned content (excluding intentional standalone docs)."

## Error Handling

- If no orphans found, congratulate user on well-connected vault
- If many orphans (>20%), suggest focused linking session
- Handle large vaults gracefully (may take time to analyze)
