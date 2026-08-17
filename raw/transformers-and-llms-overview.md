# Transformer Architecture and LLM Knowledge Systems: An Overview

## Introduction
Modern Large Language Models (LLMs) are based on the Transformer architecture introduced by Vaswani et al. in 2017. Transformers leverage self-attention mechanisms to process sequential data in parallel, overcoming the bottleneck of recurrent neural networks (RNNs).

## Key Components
1. **Self-Attention Mechanism**: Calculates dynamic attention weights across all tokens in a sequence, allowing the model to capture long-range contextual relationships.
2. **Multi-Head Attention**: Allows the model to jointly attend to information from different representation subspaces at different positions.
3. **Feed-Forward Networks and Layer Normalization**: Provides non-linear transformations and stabilizes training across deep layers.

## Knowledge Retrieval vs. Persistent Knowledge Bases
Traditional information systems pair LLMs with Retrieval-Augmented Generation (RAG). In naive RAG:
- Raw documents are chunked and embedded into vector spaces.
- At query time, top-k chunks are retrieved and fed into the prompt context.
- Drawback: The LLM recalculates synthesis from scratch on every query without memory accumulation.

In contrast, the **LLM Wiki Pattern** uses LLMs to incrementally construct, cross-reference, and maintain a structured markdown wiki. Rather than re-deriving synthesis on every question, knowledge is compiled once, continually updated, and kept logically coherent over time.
