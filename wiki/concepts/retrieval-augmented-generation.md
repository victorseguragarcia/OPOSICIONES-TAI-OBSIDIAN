---
title: "Retrieval-Augmented Generation"
type: "concept"
tags:
  - ai-patterns
  - rag
  - search
  - knowledge-bases
sources:
  - "raw/transformers-and-llms-overview.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RAG"
  - "Naive RAG"
---

# Retrieval-Augmented Generation (RAG)

**Retrieval-Augmented Generation (RAG)** is an architecture where an external retriever fetches relevant passages from a document corpus and feeds them into the prompt of an LLM at query time.

## Limitations of Naive RAG
1. **No Compounding Knowledge**: Every question requires the model to re-synthesize information from disparate chunks.
2. **Context Fragmentation**: Nuanced queries spanning multiple documents can miss cross-connections.
3. **Redundant Computation**: Insights discovered in prior queries are lost once the chat session ends.

## Evolution: Towards Persistent Knowledge Bases
The [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wiki]] addresses RAG's limitations by compiling sources into an interconnected, pre-synthesized markdown base.

## See Also
- Comparison: [[wiki/synthesis/llm-wiki-vs-rag-comparison|LLM Wiki vs RAG Comparison]]
- Ingestion Source: [[wiki/sources/transformers-and-llms-overview|Summary: Transformers & LLMs]]
