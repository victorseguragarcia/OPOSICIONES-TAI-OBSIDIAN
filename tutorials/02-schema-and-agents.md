---
title: "Tutorial 02: Schema and Agents"
type: "tutorial"
tags:
  - tutorial
  - schema
  - agents
  - configuration
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 02"
  - "tutorial-02-schema-and-agents"
---

# Tutorial 02: Schema and Agents

This tutorial explains how the **Schema Layer** (`AGENTS.md`, `CLAUDE.md`) defines rules, templates, and conventions for AI agents acting as wiki maintainers.

---

## 1. The Role of the Schema
The schema document is the constitution of the LLM Wiki:
- It transforms a generic chatbot into a **disciplined knowledge base compiler**.
- Defines directory boundaries (`raw/` is immutable; `wiki/` is agent-maintained).
- Standardizes frontmatter metadata, link syntax, and catalog updates.

---

## 2. YAML Frontmatter Specification

Every note created in `wiki/` must adhere to this schema:

```yaml
---
title: "Human-Readable Title"
type: "source | entity | concept | synthesis | test"
tags:
  - primary-topic
  - sub-topic
sources:
  - "raw/path-to-source-file.md"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
aliases:
  - "Alternative Name 1"
  - "Alternative Name 2"
---
```

### Field Descriptions
| Field | Type | Description |
| :--- | :--- | :--- |
| `title` | `string` | The official name of the note. |
| `type` | `enum` | One of `source`, `entity`, `concept`, `synthesis`, `test`, `tutorial`. |
| `tags` | `list` | Categorical and searchable keywords. |
| `sources`| `list` | Relative paths to immutable files in `raw/` that ground this note. |
| `created`| `date` | Creation timestamp (`YYYY-MM-DD`). |
| `updated`| `date` | Last modification timestamp (`YYYY-MM-DD`). |
| `aliases`| `list` | Alternative names for autocomplete and hybrid search. |

---

## 3. Agent Directives & Workflows

Agents operating on this repository must execute these four core routines:

1. **Ingest Pipeline**: Read new items from `raw/`, generate structured summaries in `wiki/sources/`, and extract entities/concepts.
2. **Catalog Synchronization**: Automatically append new notes to [[index|index.md]] with one-line descriptions.
3. **Audit Trail**: Record every ingest, query, and maintenance operation in [[log|log.md]].
4. **Integrity Checks**: Ensure zero broken links (`[[...]]`) and zero orphan pages.
5. **Test Generation**: Generate grounded 4-option multiple-choice tests for Temas/Bloques using strictly ingested concepts and raw sources, filing them into `wiki/tests/`.

---

## 4. Verification Check
Run the linter to verify that all existing notes conform to the schema:
```bash
python scripts/lint.py
```

## Next Step
Proceed to [[tutorials/03-entity-and-concept-extraction|Tutorial 03: Entity and Concept Extraction]].
