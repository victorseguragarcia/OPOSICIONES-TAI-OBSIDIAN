---
title: "Tutorial 01: Raw Source Ingestion"
type: "tutorial"
tags:
  - tutorial
  - workflow
  - ingest
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 01"
---

# Tutorial 01: Raw Source Ingestion

This tutorial guides you through ingesting raw, immutable source materials into the LLM Wiki.

## Steps
1. Place raw documents (Markdown, text, or web clippings) in `raw/`.
2. Instruct the LLM agent to read the source:
   > *"Ingest `raw/transformers-and-llms-overview.md` and generate a structured summary note."*
3. The LLM creates `wiki/sources/<filename>.md` containing key takeaways, quotes, and metadata.
4. Verify source summary exists: [[wiki/sources/transformers-and-llms-overview|Summary: Transformers & LLMs]].

## Next Step
Proceed to [[tutorials/02-entity-concept-extraction|Tutorial 02: Entity & Concept Extraction]].
