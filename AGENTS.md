# LLM Wiki Schema & Agent Instructions

This repository follows the **LLM Wiki Pattern** (inspired by Andrej Karpathy's architecture for persistent personal knowledge bases). The LLM agent acts as the programmer/maintainer, Obsidian/Markdown as the IDE, and the wiki as the compounding codebase.

---

## 1. Directory Structure

- `raw/` : Immutable curated raw source documents (articles, papers, notes, HTML, transcripts). The LLM reads from here but never alters original sources.
  - `raw/assets/` : Local images, diagrams, attachments.
- `wiki/` : Persistent markdown knowledge base written and maintained by the LLM.
  - `wiki/sources/` : Detailed summary & key takeaways for each ingested raw source.
  - `wiki/entities/` : Pages for distinct tools, libraries, hardware, standards, organizations, people.
  - `wiki/concepts/` : Deep-dive concept explanations, theoretical foundations, architectural patterns.
  - `wiki/synthesis/` : Higher-level topic guides, comparison matrices, study notes, structured overviews.
- `index.md` : Master categorized catalog listing all wiki pages with one-line summaries and metadata.
- `log.md` : Append-only chronological timeline of wiki operations (ingest, query, lint, synthesis).
- `scripts/` : Automation scripts for linting, indexing, and querying the wiki.
- `tutorials/` : Step-by-step guides and test scenarios verifying wiki operations.

---

## 2. Page Frontmatter Standard

Every wiki page must include YAML frontmatter:

```yaml
---
title: "Page Title"
type: "source | entity | concept | synthesis"
tags:
  - topic
  - subtopic
sources:
  - "[[raw/source-file-name]]"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
aliases:
  - "Alternative Name"
---
```

---

## 3. Core Operations & Workflows

### A. Ingest (`raw/` -> `wiki/`)
When a new source is added to `raw/`:
1. Read the source completely.
2. Create a structured summary page in `wiki/sources/<source-slug>.md`.
3. Extract core entities and concepts. Create new pages or update existing pages in `wiki/entities/` and `wiki/concepts/` with bidirectional links.
4. Update `index.md` to register new/modified pages.
5. Append an entry to `log.md`:
   ```markdown
   ## [YYYY-MM-DD] ingest | <Source Title>
   - Ingested from `raw/<filename>`
   - Created: `wiki/sources/<slug>.md`
   - Updated entities & concepts: `[[Entity]]`, `[[Concept]]`
   ```

### B. Query (`wiki/` -> Synthesis)
When a user asks a domain question:
1. Consult `index.md` and search relevant wiki pages.
2. Read the referenced pages to synthesize an answer with citations.
3. If the answer contains novel insights, comparisons, or study summaries, file it back into `wiki/synthesis/` and update `index.md` and `log.md`.

### C. Lint & Health Check
Periodically run `scripts/lint.py` to check for:
- Broken internal links (`[[...]]` or `[...](...)`).
- Orphan pages (pages with 0 inbound links).
- Pages missing from `index.md`.
- Malformed YAML frontmatter.
- Stale or contradicting claims between notes.

---

## 4. Linking Conventions
- Prefer standard Obsidian wikilinks: `[[Target Page]]` or `[[Target Page|Display Alias]]`.
- Relative Markdown links `[Display](relative/path.md)` are also fully supported.
- Keep links contextual and dense to build an associative knowledge graph.

---

## 5. Visual Hierarchy & Color Coding Standard

To optimize human study and visual recall in Obsidian, the wiki enforces a strict 3-tier color hierarchy defined in `.obsidian/snippets/tai-colors.css`:

- 🔴 **Temas Principales (Nivel 1 / H1 / Bloques)**: **Rojo** (`#E53935`)
  - Identifica títulos de temas generales, bloques y portadas maestras.
- 🟣 **Subtemas (Nivel 2 / H2 / Entidades & Conceptos)**: **Morado** (`#8E24AA`)
  - Identifica secciones intermedias, clasificaciones de conceptos y entidades.
- 🔵 **Conocimientos Concretos (Nivel 3+ / H3 / H4 / Tablas / Datos Clave)**: **Azul** (`#1E88E5`)
  - Identifica datos precisos de examen (puertos, RFCs, artículos, plazos, fórmulas, tablas y callouts específicos).

