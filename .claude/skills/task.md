---
context: fork
---

# Quick Task Creation Skill

Quickly create a task note with minimal prompts.

## Instructions

When the user invokes `/task <title>` or asks to create a task:

1. **Gather information** (prompt if not provided):
   - Task title
   - Priority: high | medium | low
   - Due date (optional)
   - Project (optional, link to Project note)
   - Assignee (optional, link to Person note)

2. **Create the note**:
   - Filename: `Task - [Title].md`
   - Example: `Task - Review GraphQL ADR.md`
   - Use template: `+Templates/Task.md`

3. **Populate frontmatter**:
   ```yaml
   type: Task
   title: "[Title]"
   completed: false
   priority: [high|medium|low]
   due: YYYY-MM-DD  # or null
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   project: "[[Project Name]]"  # or null
   assignee: "[[Person Name]]"  # or null
   tags: [task]
   ```

4. **Create basic structure**:
   - Brief description section
   - Acceptance criteria (checklist)
   - Notes section

5. **Open the note** for user to add details

## Example Interaction

**User:** `/task Review GraphQL ADR`

**Claude:**
"Creating task 'Review GraphQL ADR'.

- Priority? (high/medium/low)
  → high
- Due date? (YYYY-MM-DD or skip)
  → 2026-01-15
- Related project? (optional)
  → [[Project - API Gateway Modernization]]
- Assignee? (optional)
  → [[Jane Smith]]

Created task at `Task - Review GraphQL ADR.md`.

The task is ready with priority: high, due: 2026-01-15."

## Quick Task Mode

For rapid task capture, allow minimal input:

**User:** `/task Fix login bug - high priority`

**Claude:**
"Created high-priority task `Task - Fix login bug.md` with due date set to today + 3 days."

## Integration with Daily Notes

Suggest to user:
"You can also track this task in your daily notes by linking to it: `[[Task - Review GraphQL ADR]]`"

## Tips for Task Management

- **High priority**: Critical, urgent work
- **Medium priority**: Important but not urgent
- **Low priority**: Nice to have, future work
- **Due dates**: Set realistic deadlines
- **Projects**: Link tasks to projects for context
- **Assignees**: Track who's responsible
- **Completion**: Update `completed: true` when done

## Error Handling

- If template doesn't exist, create basic structure
- Default priority to medium if not specified
- Sanitize filename
