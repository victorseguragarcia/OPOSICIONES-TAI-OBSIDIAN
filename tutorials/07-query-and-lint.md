---
title: "Tutorial 07: Query and Lint"
type: "tutorial"
tags:
  - tutorial
  - query
  - lint
  - validation
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 07"
  - "tutorial-06-query-and-lint"
  - "tutorial-07-query-and-lint"
---

# Tutorial 07: Query and Lint

This final tutorial validates the full lifecycle of the LLM Wiki: querying indexed knowledge and running automated health checks.

## 1. Querying Knowledge
Execute query tool to retrieve notes by topic, tag, or keyword:
```bash
python scripts/query.py "transformer architecture attention"
```

Expected output:
- Returns matching notes ranked by relevance:
  - [[wiki/entities/transformer-architecture|Transformer Architecture]]
  - [[wiki/entities/attention-mechanism|Attention Mechanism]]
  - [[wiki/synthesis/llm-wiki-vs-rag-comparison|LLM Wiki vs RAG Comparison]]

## 2. Running Automated Lint Check
Run the integrity linter to verify wiki health:
```bash
python scripts/lint.py
```

Validation criteria:
- [x] All wiki and tutorial files contain valid YAML frontmatter.
- [x] Zero broken wikilinks or Markdown links.
- [x] Zero unindexed wiki notes.
- [x] Zero orphan notes in `wiki/`.

## Result
When `python scripts/lint.py` returns code `0` and all links resolve cleanly, **tutorial-06-query-and-lint is verified as PASSED.**
