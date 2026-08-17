---
title: "Tutorial 04: Indexing and Logging"
type: "tutorial"
tags:
  - tutorial
  - indexing
  - logging
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 04"
---

# Tutorial 04: Indexing and Logging

This tutorial covers keeping `index.md` and `log.md` up to date on every operation.

## 1. Master Index (`index.md`)
- Serves as the table of contents for both human navigation and LLM fast retrieval.
- Organizes pages into:
  - Synthesis & Topics
  - Concepts
  - Entities & Tools
  - Source Summaries

## 2. Chronological Log (`log.md`)
- Append-only format.
- Structured entries: `## [YYYY-MM-DD] <operation> | <Title>`
- Enables quick inspection via Git history or terminal tools.

## Next Step
Proceed to [[tutorials/05-synthesis-and-filing|Tutorial 05: Synthesis and Filing]].
