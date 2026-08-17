---
title: "Attention Mechanism"
type: "entity"
tags:
  - deep-learning
  - attention
  - transformers
sources:
  - "raw/transformers-and-llms-overview.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Self-Attention"
  - "Multi-Head Attention"
---

# Attention Mechanism

The **Attention Mechanism** allows neural networks to focus selectively on relevant parts of input sequences.

## Mathematical Formulation
Scaled Dot-Product Attention:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

Where:
- $Q$: Query matrix
- $K$: Key matrix
- $V$: Value matrix
- $d_k$: Dimension of keys

## Importance in Architecture
Attention enables [[wiki/entities/transformer-architecture|Transformer Architecture]] to achieve global contextual awareness across large token windows without sequential processing.

## References
- Source: [[wiki/sources/transformers-and-llms-overview|Summary: Transformers & LLMs]]
