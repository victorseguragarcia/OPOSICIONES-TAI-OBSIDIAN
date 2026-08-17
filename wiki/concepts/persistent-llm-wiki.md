---
title: "Persistent LLM Wiki Pattern"
type: "concept"
tags:
  - knowledge-management
  - agentic-workflows
  - llm-wiki
sources:
  - "raw/transformers-and-llms-overview.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "LLM Wiki"
  - "Karpathy LLM Wiki"
---

# Persistent LLM Wiki Pattern

The **Persistent LLM Wiki Pattern** is a knowledge management paradigm where an LLM incrementally builds, structures, cross-references, and maintains a persistent, interlinked collection of markdown files.

## Key Principles
1. **Compounding Knowledge Layer**: Information is synthesized once upon ingestion and updated as new facts arrive.
2. **Immutable Raw Sources**: Original documents in `raw/` remain untouched.
3. **LLM as the Compiler/Maintainer**: The AI handles bookkeeping, cross-linking, and index synchronization.
4. **Obsidian as the IDE**: Provides graph visualizers, backlink panels, and human-in-the-loop navigation.

## Contrast with RAG
Unlike [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]], the LLM Wiki does not start from raw fragments on every question. The synthesis already exists in the graph.

## See Also
- Deep-dive: [[wiki/synthesis/llm-wiki-vs-rag-comparison|LLM Wiki vs RAG Comparison]]
- Underlying Models: [[wiki/entities/transformer-architecture|Transformer Architecture]]
