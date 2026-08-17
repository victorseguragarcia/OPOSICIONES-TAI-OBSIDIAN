#!/usr/bin/env python3
"""
LLM Wiki Linter & Health Check Tool
Validates wiki integrity:
1. YAML frontmatter completeness
2. Link integrity (wikilinks and markdown links)
3. Orphan page detection (unreachable notes)
4. Master Index coverage
"""

import os
import re
import sys
import yaml
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT_DIR / "wiki"
INDEX_FILE = ROOT_DIR / "index.md"
TUTORIALS_DIR = ROOT_DIR / "tutorials"

WIKILINK_PATTERN = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]')
MDLINK_PATTERN = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
FRONTMATTER_PATTERN = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def get_all_md_files():
    files = {}
    if WIKI_DIR.exists():
        for f in WIKI_DIR.rglob("*.md"):
            files[f.resolve()] = f.relative_to(ROOT_DIR)
    if TUTORIALS_DIR.exists():
        for f in TUTORIALS_DIR.rglob("*.md"):
            files[f.resolve()] = f.relative_to(ROOT_DIR)
    if INDEX_FILE.exists():
        files[INDEX_FILE.resolve()] = INDEX_FILE.relative_to(ROOT_DIR)
    return files

def parse_frontmatter(content, rel_path):
    errors = []
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return None, [f"Missing YAML frontmatter in {rel_path}"]
    
    yaml_text = match.group(1)
    try:
        data = yaml.safe_load(yaml_text)
    except Exception as e:
        return None, [f"Invalid YAML in {rel_path}: {e}"]
    
    if not isinstance(data, dict):
        return None, [f"YAML frontmatter in {rel_path} is not a dictionary"]
        
    required_fields = ["title", "type", "created", "updated"]
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required frontmatter field '{field}' in {rel_path}")
            
    valid_types = ["source", "entity", "concept", "synthesis", "tutorial", "index"]
    if data.get("type") and data.get("type") not in valid_types:
        errors.append(f"Invalid type '{data.get('type')}' in {rel_path}. Allowed: {valid_types}")
        
    return data, errors

def extract_links(content, file_path):
    links = []
    # Strip frontmatter first
    content_no_fm = FRONTMATTER_PATTERN.sub('', content)
    
    # 1. Wikilinks [[target]]
    for match in WIKILINK_PATTERN.finditer(content_no_fm):
        target = match.group(1).strip()
        links.append(('wikilink', target))
        
    # 2. Markdown links [text](target)
    for match in MDLINK_PATTERN.finditer(content_no_fm):
        target = match.group(2).strip()
        if not target.startswith(("http://", "https://", "mailto:", "#")):
            links.append(('mdlink', target))
            
    return links

def resolve_target(source_file, target_str, link_type, all_files):
    # Normalize
    clean_target = target_str.split('#')[0].strip()
    if not clean_target:
        return True
    
    if link_type == 'mdlink':
        # Resolve relative to source file
        try:
            target_path = (source_file.parent / clean_target).resolve()
            if target_path in all_files or target_path.exists():
                return target_path
        except Exception:
            pass

    # Try matching filename / path in wiki
    candidates = [
        ROOT_DIR / clean_target,
        ROOT_DIR / f"{clean_target}.md",
        WIKI_DIR / clean_target,
        WIKI_DIR / f"{clean_target}.md",
        TUTORIALS_DIR / clean_target,
        TUTORIALS_DIR / f"{clean_target}.md",
    ]
    for c in candidates:
        if c.resolve() in all_files or c.resolve().exists():
            return c.resolve()
            
    # Search by basename without extension
    stem_target = Path(clean_target).stem.lower()
    for abs_path in all_files:
        if abs_path.stem.lower() == stem_target:
            return abs_path
            
    return None

def run_lint():
    print("=" * 60)
    print(" 🔍 RUNNING LLM WIKI LINT & HEALTH CHECK")
    print("=" * 60)
    
    all_files = get_all_md_files()
    errors = []
    warnings = []
    inbound_links = {f: set() for f in all_files}
    
    index_content = ""
    if INDEX_FILE.exists():
        index_content = INDEX_FILE.read_text(encoding="utf-8")
    else:
        errors.append("Critical: index.md does not exist at root!")

    # Check each file
    for abs_path, rel_path in all_files.items():
        try:
            content = abs_path.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"Cannot read {rel_path}: {e}")
            continue
            
        # Validate frontmatter for files in wiki/ and tutorials/
        if "wiki" in rel_path.parts or "tutorials" in rel_path.parts:
            _, fm_errors = parse_frontmatter(content, rel_path)
            errors.extend(fm_errors)
            
        # Check if indexed in index.md (for wiki/ pages)
        if "wiki" in rel_path.parts:
            stem = abs_path.stem
            rel_str = str(rel_path).replace("\\", "/")
            if stem not in index_content and rel_str not in index_content:
                warnings.append(f"Page '{rel_path}' is not listed in index.md")
                
        # Parse links
        links = extract_links(content, abs_path)
        for link_type, target in links:
            resolved = resolve_target(abs_path, target, link_type, all_files)
            if resolved:
                if resolved in inbound_links:
                    inbound_links[resolved].add(abs_path)
            else:
                errors.append(f"Broken link in {rel_path}: '{target}' (type: {link_type})")

    # Check for orphan pages in wiki/
    for abs_path, rel_path in all_files.items():
        if "wiki" in rel_path.parts:
            inbound = inbound_links.get(abs_path, set())
            if len(inbound) == 0:
                warnings.append(f"Orphan note with 0 inbound links: {rel_path}")

    # Summary Output
    print(f"\n📁 Scanned {len(all_files)} markdown files.")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
            
    if errors:
        print(f"\n❌ {len(errors)} ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        print("\n❌ LINT FAILED")
        return 1
    else:
        print("\n✅ ALL CHECKS PASSED: Wiki structure is healthy and fully connected!")
        return 0

if __name__ == "__main__":
    sys.exit(run_lint())
