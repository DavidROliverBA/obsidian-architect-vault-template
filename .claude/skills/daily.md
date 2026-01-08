# Daily Note Skill

Create today's daily note from template.

## Instructions

When the user invokes `/daily` or asks to create today's daily note:

1. **Check if today's note exists**:
   - Path: `+Daily/[YEAR]/YYYY-MM-DD.md`
   - Example: `+Daily/2026/2026-01-07.md`
   - If exists, open it and inform user

2. **If note doesn't exist, create it**:
   - Create year subfolder if needed: `+Daily/[YEAR]/`
   - Create note from template: `+Templates/Daily.md`
   - Filename: `YYYY-MM-DD.md` (e.g., `2026-01-07.md`)

3. **Populate template**:
   - Set `date` to today's date (YYYY-MM-DD format)
   - Set `created` and `modified` to today
   - Leave other sections for user to fill

4. **Open the note** and inform user it's ready

## Example Response

"Created today's daily note at `+Daily/2026/2026-01-07.md`. Ready for you to capture your day!"

## Error Handling

- If year folder doesn't exist, create it
- If template doesn't exist, inform user to create `+Templates/Daily.md`
- If note already exists, just open it

## Notes

- Daily notes are for personal reflection, task tracking, and journaling
- They don't follow "DailyNote - " prefix naming convention
- They're organized by year in subdirectories for scalability
