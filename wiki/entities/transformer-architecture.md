---
title: "Transformer Architecture"
type: "entity"
tags:
  - deep-learning
  - nlp
  - transformers
  - architecture
sources:
  - "raw/transformers-and-llms-overview.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Transformers"
  - "Transformer Model"
---

# Transformer Architecture

The **Transformer** is a neural network architecture introduced in the 2017 paper *"Attention Is All You Need"* by Vaswani et al. It replaces recurrence with parallel self-attention.

## Core Components
- **[[wiki/entities/attention-mechanism|Self-Attention Mechanism]]**: Computes contextual weights across all input positions.
- **Positional Encoding**: Injects sequence order information into input representations.
- **Feed-Forward Layers & Normalization**: Non-linear processing and residual normalization per block.

## Applications in Knowledge Systems
Transformers form the backbone of modern LLMs used to construct [[wiki/concepts/persistent-llm-wiki|Persistent LLM Wikis]] and execute [[wiki/concepts/retrieval-augmented-generation|Retrieval-Augmented Generation (RAG)]].

## References
- Source: [[wiki/sources/transformers-and-llms-overview|Summary: Transformers & LLMs]]
- Synthesis: [[wiki/synthesis/llm-wiki-vs-rag-comparison|Comparison: LLM Wiki vs RAG]]
