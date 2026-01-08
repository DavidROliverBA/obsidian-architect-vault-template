---
context: fork
---

# Person Note Creation Skill

Create a person note for a colleague, stakeholder, or contact.

## Instructions

When the user invokes `/person <name>` or asks to create a person note:

1. **Gather information** (prompt user):
   - Person's full name
   - Role/title
   - Organization (link to Organisation note or text)
   - Email address (optional)
   - Phone (optional)

2. **Create the note**:
   - Filename: `[Full Name].md` (NO "Person -" prefix!)
   - Example: `Jane Smith.md`
   - Use template: `+Templates/Person.md`

3. **Populate frontmatter**:
   ```yaml
   type: Person
   title: "[Full Name]"
   role: "[Job Title]"
   organisation: "[[Organisation Name]]"  # or plain text
   emailAddress: "<email>"  # or null
   phone: null  # optional
   created: YYYY-MM-DD
   modified: YYYY-MM-DD
   tags: [person]
   ```

4. **Create basic structure**:
   - Contact Information
   - Role & Responsibilities
   - Notes (working style, expertise, preferences)
   - Meetings (auto-populated by Dataview)
   - Related Projects (auto-populated by Dataview)

5. **Explain linking convention**:
   "Person notes use just the name (no 'Person -' prefix) for cleaner wiki-links like `[[Jane Smith]]`."

## Example Interaction

**User:** `/person Jane Smith`

**Claude:**
"Creating person note for 'Jane Smith'.

- Role/title?
  → Head of Architecture
- Organization?
  → Your Company
- Email? (optional)
  → jane.smith@company.com

Created person note at `Jane Smith.md`.

You can now link to this person in meeting notes and task assignments using `[[Jane Smith]]`."

## When to Create Person Notes

**Create for:**
- Regular collaborators or stakeholders
- External consultants or vendor contacts
- Anyone you meet with multiple times
- Key decision makers
- Team members

**Don't Create for:**
- One-time contacts
- People mentioned once
- Generic roles without specific individuals

## Integration Tips

Explain to user:
- **In meetings**: Add to attendees list: `attendees: ["[[Jane Smith]]"]`
- **In tasks**: Assign work: `assignee: "[[Jane Smith]]"`
- **In projects**: List stakeholders
- **Daily notes**: Mention in context of conversations

## Auto-Populated Sections

The template includes Dataview queries that automatically show:
- All meetings attended (from Meeting notes)
- All assigned tasks (from Task notes)
- Related projects (from Project notes)

## Error Handling

- If template doesn't exist, create basic structure
- Handle names with special characters
- Sanitize filename while preserving readability
