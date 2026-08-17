# LLM Wiki Operation Log

Append-only chronological timeline of wiki operations.

---

## [2026-08-17] init | LLM Wiki Initialized
- Initialized core repository structure, schemas, and indexing guidelines.
- Configured `AGENTS.md`, `CLAUDE.md`, `.gitignore`, `index.md`, and `log.md`.

## [2026-08-17] tools | Added CLI Tooling
- Added `scripts/lint.py` for graph integrity and frontmatter validation.
- Added `scripts/query.py` for keyword and tag search over the wiki.

## [2026-08-17] ingest | Transformer Architecture and LLM Knowledge Systems
- Ingested source from `raw/transformers-and-llms-overview.md`.
- Generated source summary: `wiki/sources/transformers-and-llms-overview.md`.
- Extracted entities: `wiki/entities/transformer-architecture.md`, `wiki/entities/attention-mechanism.md`.
- Extracted concepts: `wiki/concepts/retrieval-augmented-generation.md`, `wiki/concepts/persistent-llm-wiki.md`.
- Generated synthesis: `wiki/synthesis/llm-wiki-vs-rag-comparison.md`.
- Created tutorials 01 through 06 in `tutorials/`.
- Updated `index.md` master catalog.

## [2026-08-17] skills | Installed Obsidian Skills (kepano/obsidian-skills)
- Installed skills into `.agents/skills/` and `.claude/skills/`:
  - `obsidian-markdown`: Obsidian syntax, wikilinks, callouts, embeds, frontmatter properties.
  - `obsidian-bases`: Obsidian Bases (`.base`) format, views, filters, formulas.
  - `json-canvas`: JSON Canvas (`.canvas`) diagramming and graph nodes.
  - `obsidian-cli`: CLI automation for vault interaction.
  - `defuddle`: Web content extraction and clutter removal.

## [2026-08-17] tutorial | Tutorial 02: Schema and Agents
- Documented YAML frontmatter standard and agent execution routines in `tutorials/02-schema-and-agents.md`.
- Updated `index.md` catalog and test suites.
- Passed full integrity lint check.

## [2026-08-17] tutorial | Tutorial 03: Entity and Concept Extraction
- Created comprehensive guide in `tutorials/03-entity-and-concept-extraction.md`.
- Documented ontology differentiation (Entities in `wiki/entities/` vs. Concepts in `wiki/concepts/`).
- Streamlined full tutorial sequence (01 to 07) and updated master index.
- All integrity and linter checks passed with zero errors.

## [2026-08-17] tutorial | Tutorial 04: Cross-Referencing and Graph Topology
- Documented associative linking mechanics, wikilink syntax, and graph topology guidelines in `tutorials/04-cross-referencing.md`.
- Defined hub node patterns, bidirectional linking rules, and anti-orphan policies.
- Validated complete graph integrity with `scripts/lint.py`.

## [2026-08-17] tutorial | Tutorial 05: Indexing and Logging
- Documented dual tracking architecture: content-oriented catalog (`index.md`) vs. chronological audit trail (`log.md`).
- Established categorized index schema and machine-parseable log prefixes (`## [YYYY-MM-DD] <op> | <title>`).
- Validated complete index synchronization via `scripts/lint.py`.

## [2026-08-17] extract | Extracted 10 PDFs from raw/bloque 4 to raw/sources/
- Created `scripts/extract_pdfs.py` using PyMuPDF (`fitz`).
- Extracted all 10 PDF topics from `raw/bloque 4/` into individual Markdown files in `raw/sources/`.
- Embedded YAML frontmatter with standardized schema (`title`, `type: "source"`, `tags`, `sources`, timestamps, `aliases`).

## [2026-08-17] ingest | Bloque 4 TAI Oposiciones (Temas 01 al 10)
- Ingested 10 raw sources from `raw/sources/bloque4-tema01.md` through `bloque4-tema10.md`.
- Created 10 structured summaries in `wiki/sources/`.
- Extracted 21 specialized entities in `wiki/entities/` covering operating systems, databases, containers, protocols and cybersecurity standards.
- Extracted 12 foundational concepts in `wiki/concepts/` covering networking models, memory management, architectures and security paradigms.
- Generated 4 high-level synthesis documents in `wiki/synthesis/` (Master guide, OSI vs TCP/IP, IPv4 vs IPv6, VMs vs Containers).
- Rebuilt `index.md` master catalog.


## [2026-08-17] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.


## [2026-08-17] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.


## [2026-08-17] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.


## [2026-08-17] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.


## [2026-08-17] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.
