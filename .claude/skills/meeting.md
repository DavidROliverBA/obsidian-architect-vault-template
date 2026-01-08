---
context: fork
---

# Meeting Note Skill

Create a meeting note with guided prompts.

## Instructions

When the user invokes `/meeting <title>` or asks to create a meeting note:

1. **Gather information** (prompt user if not provided):
   - Meeting title
   - Date (default: today)
   - Project (optional, link to Project note)
   - Attendees (optional, list of Person note links)

2. **Create the note**:
   - Location: `+Meetings/Meeting - YYYY-MM-DD [Title].md`
   - Example: `+Meetings/Meeting - 2026-01-07 Architecture Review.md`
   - Use template: `+Templates/Meeting.md`

3. **Populate frontmatter**:
   ```yaml
   type: Meeting
   title: "[Title]"
   date: 'YYYY-MM-DD'
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   project: "[[Project Name]]"  # if provided
   attendees: ["[[Person 1]]", "[[Person 2]]"]  # if provided
   summary: null  # User fills after meeting
   meetingType: null  # Optional: recurring meeting series
   tags: [meeting]
   ```

4. **Structure the note** with sections:
   - Attendees
   - Agenda
   - Discussion Notes
   - Decisions Made
   - Action Items
   - Follow-up

5. **Open the note** for user to complete

## Example Interaction

**User:** `/meeting Architecture Review`

**Claude:**
"Creating meeting note for 'Architecture Review'.

- Date: 2026-01-07 (today)
- Project to link? (optional)
- Attendees? (optional, separate with commas)"

*User provides or skips*

**Claude:**
"Created meeting note at `+Meetings/Meeting - 2026-01-07 Architecture Review.md`.

The note is ready with sections for agenda, discussion, decisions, and action items."

## Tips for Users

- **Link attendees**: Use Person notes like `[[Jane Smith]]`
- **Link project**: Connect meeting to relevant project
- **Add summary**: One-line summary after meeting for searchability
- **Action items**: Use checkboxes `- [ ]` for tasks
- **Create Task notes**: For important follow-ups, create formal Task notes

## Error Handling

- If +Meetings folder doesn't exist, create it
- If template doesn't exist, create basic structure
- Sanitize filename (remove special characters)
