<%*
const name = await tp.system.prompt("Atomic note title:");
if (name) {
  await tp.file.rename("Atomic Note - " + name);
}
_%>
---
type: AtomicNote
title: <% name %>
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
tags: []
source: # Where did this idea come from?
---

# <% name %>

<!--
Atomic notes contain ONE idea, concept, or fact.
Keep it focused and concise.
Link liberally to related notes.
-->



## Source

- [[Source Note or Weblink]]

## Related

- [[Related Concept 1]]
- [[Related Concept 2]]
