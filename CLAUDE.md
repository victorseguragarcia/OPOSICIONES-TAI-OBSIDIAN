# Claude Code Instructions - LLM Wiki

Please follow the conventions and workflow defined in `AGENTS.md` and `llm-wiki.md`.

## Key Commands
- Run lint health checks: `python scripts/lint.py`
- Query the wiki: `python scripts/query.py "<query term>"`
- Run test tutorials: `python scripts/test_tutorials.py`

## Rules
- Keep `raw/` immutable.
- Always maintain `index.md` and `log.md` when creating or modifying wiki pages.
- Ensure all pages in `wiki/` contain valid frontmatter and inbound links.
