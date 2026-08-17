---
title: "Tutorial 02: Entity & Concept Extraction"
type: "tutorial"
tags:
  - tutorial
  - extraction
  - entities
  - concepts
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 02"
---

# Tutorial 02: Entity & Concept Extraction

This tutorial explains how the LLM extracts core entities and conceptual abstractions from ingested sources.

## Principles
- **Entities** (`wiki/entities/`): Concrete components, architectures, tools, protocols (e.g. [[wiki/entities/transformer-architecture|Transformer Architecture]], [[wiki/entities/attention-mechanism|Attention Mechanism]]).
- **Concepts** (`wiki/concepts/`): High-level ideas, paradigms, design patterns (e.g. [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki]], [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]).

## Workflow
1. Identify key recurring terms in the source.
2. Check if a wiki page already exists for that term.
3. If new, initialize the page with frontmatter. If existing, enrich it with new citations.

## Next Step
Proceed to [[tutorials/03-cross-referencing|Tutorial 03: Cross-Referencing]].
