---
title: "Tutorial 03: Entity and Concept Extraction"
type: "tutorial"
tags:
  - tutorial
  - extraction
  - entities
  - concepts
  - ontology
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 03"
  - "tutorial-03"
  - "tutorial-03-entity-and-concept-extraction"
---

# Tutorial 03: Entity and Concept Extraction

In this tutorial, we cover how the LLM decomposes ingested sources into atomic, reusable **Entities** and **Concepts**.

---

## 1. Entities vs. Concepts Distinction

Understanding the distinction is key to maintaining a clean taxonomy:

| Category | Folder | Nature | Examples |
| :--- | :--- | :--- | :--- |
| **Entities** | `wiki/entities/` | Concrete tools, specific architectures, protocols, libraries, organizations, hardware. | [[wiki/entities/transformer-architecture\|Transformer Architecture]], [[wiki/entities/attention-mechanism\|Attention Mechanism]] |
| **Concepts** | `wiki/concepts/` | Abstract patterns, theoretical paradigms, mental models, methodologies. | [[wiki/concepts/persistent-llm-wiki\|Persistent LLM Wiki]], [[wiki/concepts/retrieval-augmented-generation\|Retrieval-Augmented Generation (RAG)]] |

---

## 2. Extraction Pipeline

When a raw source like `raw/transformers-and-llms-overview.md` is processed:

1. **Scan for Core Nouns & Terminology**: Identify architectural components and conceptual themes.
2. **Check Existing Knowledge Base**: Search `wiki/` using `scripts/query.py` or consult `index.md` to see if a note already exists.
3. **Branching Strategy**:
   - **If New**: Create a dedicated page in `wiki/entities/<slug>.md` or `wiki/concepts/<slug>.md` with YAML frontmatter and ground it in the source (`sources: ["raw/..."]`).
   - **If Existing**: Enrich the existing note by appending new insights, updating the `updated` date, and recording the new source citation.

---

## 3. Practical Example

From our source summary [[wiki/sources/transformers-and-llms-overview|Summary: Transformers & LLMs]], the following notes were extracted and populated:
- **Entity**: [[wiki/entities/transformer-architecture|Transformer Architecture]]
- **Entity**: [[wiki/entities/attention-mechanism|Attention Mechanism]]
- **Concept**: [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki Pattern]]
- **Concept**: [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation]]

---

## 4. Verification
Run the query tool to verify that all extracted entities and concepts are searchable:
```bash
python scripts/query.py "attention transformer"
```

## Next Step
Proceed to [[tutorials/04-cross-referencing|Tutorial 04: Cross-Referencing and Graph Topology]].
