# Master Index - LLM Wiki

Welcome to the Master Index of the LLM Wiki. This catalog indexes all knowledge pages organized by category with concise descriptions and metadata.

---

## 📚 Synthesis & Topics
*High-level overviews, comparison matrices, and consolidated domain guides.*

- [[wiki/synthesis/llm-wiki-vs-rag-comparison|Comparison: LLM Wiki vs Retrieval-Augmented Generation (RAG)]] — Comprehensive trade-off matrix and architectural comparison between naive RAG and compounding persistent wikis.

---

## 🧠 Concepts
*Theoretical concepts, architectural models, and foundational principles.*

- [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki Pattern]] — Principles of building compounding personal knowledge bases maintained by LLM agents.
- [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation (RAG)]] — Mechanics and limitations of traditional stateless chunk retrieval.

---

## ⚙️ Entities & Tools
*Specific systems, libraries, protocols, standards, and tools.*

- [[wiki/entities/transformer-architecture|Transformer Architecture]] — Deep learning backbone model using parallel self-attention.
- [[wiki/entities/attention-mechanism|Attention Mechanism]] — Scaled dot-product and multi-head attention mechanisms.

---

## 📑 Source Summaries
*Ingested source summaries from `raw/`.*

- [[wiki/sources/transformers-and-llms-overview|Summary: Transformer Architecture and LLM Knowledge Systems]] — Processed overview of transformers, attention, and knowledge persistence.

---

## 🛠️ Tutorials & Operations
- [[tutorials/01-raw-ingest|Tutorial 01: Raw Source Ingestion]] — Ingestion pipeline from `raw/` to `wiki/sources/`.
- [[tutorials/02-entity-concept-extraction|Tutorial 02: Entity & Concept Extraction]] — Extracting structured entities and concepts.
- [[tutorials/03-cross-referencing|Tutorial 03: Cross-Referencing and Graph Topology]] — Building bidirectional links and graph density.
- [[tutorials/04-index-and-logging|Tutorial 04: Indexing and Logging]] — Maintaining `index.md` and `log.md`.
- [[tutorials/05-synthesis-and-filing|Tutorial 05: Synthesis and Filing Back]] — Generating syntheses and filing back into `wiki/synthesis/`.
- [[tutorials/06-query-and-lint|Tutorial 06: Query and Lint]] — Querying the wiki and validating health with linter.
