#!/usr/bin/env python3
"""
LLM Wiki Search & Query Tool
Performs fast hybrid matching across frontmatter (tags, aliases, title) and body content.
"""

import sys
import os
import re
from pathlib import Path

# Force UTF-8 on Windows stdout if possible
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def search_wiki(query):
    query_terms = query.lower().split()
    results = []
    
    if not WIKI_DIR.exists():
        print("Wiki directory does not exist yet.")
        return

    for md_file in WIKI_DIR.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue
            
        frontmatter = {}
        body = content
        fm_match = FRONTMATTER_PATTERN.match(content)
        if fm_match:
            try:
                frontmatter = yaml.safe_load(fm_match.group(1)) or {}
            except Exception:
                pass
            body = content[fm_match.end():]
            
        title = frontmatter.get("title", md_file.stem)
        page_type = frontmatter.get("type", "page")
        tags = [str(t).lower() for t in frontmatter.get("tags", [])]
        aliases = [str(a).lower() for a in frontmatter.get("aliases", [])]
        
        score = 0
        matching_snippets = []
        
        for term in query_terms:
            if term in title.lower():
                score += 10
            for tag in tags:
                if term in tag:
                    score += 8
            for alias in aliases:
                if term in alias:
                    score += 8
            if term in body.lower():
                score += 2
                
        if score > 0:
            # Extract snippet
            for line in body.splitlines():
                if any(t in line.lower() for t in query_terms) and len(line.strip()) > 10:
                    matching_snippets.append(line.strip())
                    if len(matching_snippets) >= 2:
                        break
                        
            results.append({
                "path": md_file.relative_to(ROOT_DIR),
                "title": title,
                "type": page_type,
                "score": score,
                "snippets": matching_snippets,
                "tags": tags
            })
            
    results.sort(key=lambda x: x["score"], reverse=True)
    
    print("=" * 60)
    print(f"[*] WIKI QUERY RESULTS FOR: '{query}'")
    print("=" * 60)
    
    if not results:
        print("No matching notes found.")
        return
        
    print(f"Found {len(results)} relevant note(s):\n")
    for r in results:
        print(f"[*] [{r['type'].upper()}] {r['title']} (Score: {r['score']})")
        print(f"    Path: {r['path']}")
        if r['tags']:
            print(f"    Tags: {', '.join(r['tags'])}")
        for s in r['snippets']:
            print(f"    > {s[:120]}...")
        print("-" * 50)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/query.py <query string>")
        sys.exit(1)
    search_query = " ".join(sys.argv[1:])
    search_wiki(search_query)
