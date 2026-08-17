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
| **Entities** | `wiki/entities/` | Concrete tools, specific architectures, protocols, libraries, organizations, hardware. | [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]], [[wiki/entities/cortes-generales|Cortes Generales]] |
| **Concepts** | `wiki/concepts/` | Abstract patterns, theoretical paradigms, mental models, methodologies. | [[wiki/concepts/derechos-fundamentales-y-libertades-publicas|Derechos Fundamentales]], [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos|Actos Administrativos]] |

---

## 2. Extraction Pipeline

When a raw source like `raw/sources/bloque1-tema01.md` is processed:

1. **Scan for Core Nouns & Terminology**: Identify architectural components and conceptual themes.
2. **Check Existing Knowledge Base**: Search `wiki/` using `scripts/query.py` or consult `index.md` to see if a note already exists.
3. **Branching Strategy**:
   - **If New**: Create a dedicated page in `wiki/entities/<slug>.md` or `wiki/concepts/<slug>.md` with YAML frontmatter and ground it in the source (`sources: ["raw/..."]`).
   - **If Existing**: Enrich the existing note by appending new insights, updating the `updated` date, and recording the new source citation.

---

## 3. Practical Example

From our source summary [[wiki/sources/bloque1-tema01|Resumen Bloque 1 - Tema 01]], the following notes were extracted and populated:
- **Entity**: [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]]
- **Entity**: [[wiki/entities/cortes-generales|Cortes Generales]]
- **Concept**: [[wiki/concepts/derechos-fundamentales-y-libertades-publicas|Derechos Fundamentales, Garantías y Recurso de Amparo]]
- **Concept**: [[wiki/concepts/eficacia-validez-y-nulidad-actos-administrativos|Eficacia, Validez y Nulidad de los Actos Administrativos]]

---

## 4. Verification
Run the query tool to verify that all extracted entities and concepts are searchable:
```bash
python scripts/query.py "Constitucion Derechos"
```

## Next Step
Proceed to [[tutorials/04-cross-referencing|Tutorial 04: Cross-Referencing and Graph Topology]].
