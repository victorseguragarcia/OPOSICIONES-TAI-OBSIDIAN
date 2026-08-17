---
title: "Tutorial 04: Cross-Referencing and Graph Topology"
type: "tutorial"
tags:
  - tutorial
  - cross-referencing
  - graph
  - topology
  - obsidian
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 04"
  - "tutorial-04"
  - "tutorial-04-cross-referencing"
---

# Tutorial 04: Cross-Referencing and Graph Topology

This tutorial explores the associative linking mechanics of the LLM Wiki and how to build a connected knowledge graph in Obsidian.

---

## 1. The Associative Web Philosophy
Traditional note collections become stagnant silos because they rely on hierarchical folder trees. In contrast, the **LLM Wiki Pattern** builds an associative graph (inspired by Vannevar Bush's *Memex*):
- Information is connected contextually within text rather than buried in deep folders.
- Knowledge discovery happens by traversing links across entities, concepts, and source summaries.
- The AI maintainer proactively creates links between newly ingested notes and existing knowledge.

---

## 2. Obsidian Wikilink Conventions

We standardize on Obsidian-compatible Markdown links:

### A. Direct Page Links
```markdown
[[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki]]
```
- **Syntax**: `[[Target File Path | Display Alias]]`
- Enables click-through navigation and displays clean alias text.

### B. In-Text Concept Anchoring
When introducing core ideas in notes, link directly inside natural paragraphs:
> *"Unlike traditional [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation (RAG)]], a compiled knowledge base persists synthesis over time."*

### C. Standard "See Also" / "References" Section
Every note ends with an explicit references block connecting:
1. The **grounding source** in `raw/` or `wiki/sources/`.
2. Complementary **entities** and **concepts**.
3. High-level **syntheses** and **comparison matrices**.

---

## 3. Graph Topologies & Anti-Patterns

```
              ┌──────────────────────────┐
              │  wiki/sources/source.md  │
              └────────────┬─────────────┘
                           │ ingests
             ┌─────────────┴─────────────┐
             ▼                           ▼
  ┌───────────────────────┐   ┌───────────────────────┐
  │  wiki/entities/A.md   │◄─►│  wiki/entities/B.md   │
  └──────────┬────────────┘   └──────────┬────────────┘
             │ relates to                │ relates to
             └─────────────┬─────────────┘
                           ▼
              ┌──────────────────────────┐
              │  wiki/concepts/core.md   │
              └────────────┬─────────────┘
                           │ synthesizes
                           ▼
              ┌──────────────────────────┐
              │  wiki/synthesis/comp.md  │
              └──────────────────────────┘
```

### Critical Rules:
1. **No Orphan Notes**: Every note in `wiki/` must have at least one inbound link from another wiki page, synthesis, or master index.
2. **Dense Bidirectionality**: If Entity A relies on Concept B, Concept B should mention Entity A in its examples or references.
3. **Hub Nodes**: Syntheses (e.g. [[wiki/synthesis/llm-wiki-vs-rag-comparison|LLM Wiki vs RAG Comparison]]) act as graph hubs connecting related concept and entity clusters.

---

## 4. Live Graph Verification

Verify cross-references present in our active wiki:
- [[wiki/entities/transformer-architecture|Transformer Architecture]] $\longleftrightarrow$ [[wiki/entities/attention-mechanism|Attention Mechanism]]
- [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki]] $\longleftrightarrow$ [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]
- [[wiki/synthesis/llm-wiki-vs-rag-comparison|LLM Wiki vs RAG Comparison]] (Hub note)

Run the automated graph and link health check:
```bash
python scripts/lint.py
```

## Next Step
Proceed to [[tutorials/05-index-and-logging|Tutorial 05: Indexing and Logging]].
