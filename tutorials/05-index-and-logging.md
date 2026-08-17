---
title: "Tutorial 05: Indexing and Logging"
type: "tutorial"
tags:
  - tutorial
  - indexing
  - logging
  - bookkeeping
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Tutorial 05"
  - "tutorial-05"
  - "tutorial-05-index-and-logging"
---

# Tutorial 05: Indexing and Logging

This tutorial covers the dual tracking system of the LLM Wiki: **`index.md`** (content-oriented catalog) and **`log.md`** (chronological event stream).

---

## 1. The Dual Navigation System

An effective knowledge base must answer two distinct questions:
1. *"What knowledge exists in this vault right now?"* ➔ **`index.md`**
2. *"What actions were performed and when?"* ➔ **`log.md`**

```
┌─────────────────────────────────────────────────────────────┐
│                       LLM AGENT / HUMAN                     │
└──────────────┬───────────────────────────────┬──────────────┘
               │                               │
       Reads / Updates                 Appends Timeline
               ▼                               ▼
    ┌────────────────────┐          ┌────────────────────┐
    │     index.md       │          │      log.md        │
    │  (Content Catalog) │          │ (Chronological Log)│
    ├────────────────────┤          ├────────────────────┤
    │ • Synthesis Notes  │          │ [2026-08-17] init  │
    │ • Concepts         │          │ [2026-08-17] ingest│
    │ • Entities         │          │ [2026-08-17] query │
    │ • Source Summaries │          │ [2026-08-17] lint  │
    └────────────────────┘          └────────────────────┘
```

---

## 2. Master Index Standard (`index.md`)

The [[index|Master Index]] organizes all notes into 5 clear categories:

### Structure:
```markdown
# Master Index - LLM Wiki

## 📚 Synthesis & Topics
- [[wiki/synthesis/slug|Title]] — One-line description.

## 🧠 Concepts
- [[wiki/concepts/slug|Title]] — One-line description.

## ⚙️ Entities & Tools
- [[wiki/entities/slug|Title]] — One-line description.

## 📑 Source Summaries
- [[wiki/sources/slug|Title]] — One-line description.

## 🛠️ Tutorials & Operations
- [[tutorials/slug|Title]] — One-line description.
```

### Automation & Linter Enforcement:
`scripts/lint.py` automatically scans every markdown note in `wiki/` and warns if a note is missing from `index.md`.

---

## 3. Chronological Log Standard (`log.md`)

The [[log|Operation Log]] is strictly append-only. Each entry follows a machine-parseable header:

```markdown
## [YYYY-MM-DD] <operation> | <Title / Subject>
- Key action item 1
- Key action item 2
```

### Supported Operation Types:
- `init`: Repository initialization.
- `ingest`: Ingestion of raw sources.
- `query`: Query execution and synthesized responses.
- `lint`: Health check passes and fixes.
- `synthesis`: Filing novel comparative guides back into `wiki/synthesis/`.
- `skills`: Tooling or skill package installations.
- `tutorial`: Step-by-step tutorial milestone completion.

### Inspecting Log History:
Using PowerShell or Bash:
```powershell
Get-Content log.md | Select-String "^## \["
```
```bash
grep "^## \[" log.md | tail -5
```

---

## 4. Verification Check

Run the linter to verify that `index.md` is 100% synchronized with all wiki notes:
```bash
python scripts/lint.py
```

## Next Step
Proceed to [[tutorials/06-synthesis-and-filing|Tutorial 06: Synthesis and Filing Back]].
