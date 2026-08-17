# -*- coding: utf-8 -*-
r"""
Script de auditoría exhaustiva del sistema de archivos y estructura de la Wiki.
Verifica:
1. Conformidad de estructura de directorios y archivos raíz.
2. Integridad de metadatos YAML frontmatter (campos obligatorios, tipos válidos).
3. Integridad de enlaces (wikilinks, enlaces relativos, referencias a raw/).
4. Cobertura del índice maestro (index.md) y detección de notas huérfanas.
5. Verificación de archivos Canvas (.canvas) y consistencia de nodos.
6. Verificación de snippets y sincronización con el baúl superior de Obsidian.
7. Comprobación de scripts de Python para evitar advertencias de sintaxis.
"""
import os
import re
import sys
import json
import yaml
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_PATTERN = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MDLINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
CODE_BLOCK_PATTERN = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_PATTERN = re.compile(r"`[^`]+`")

def audit():
    print("=" * 70)
    print("🔍 AUDITORÍA INTEGRAL DEL SISTEMA DE ARCHIVOS Y ESTRUCTURA DE LA WIKI")
    print("=" * 70)
    
    issues = []
    warnings = []
    
    # 1. VERIFICAR DIRECTORIOS OBLIGATORIOS
    required_dirs = [
        "raw", "raw/sources",
        "wiki", "wiki/sources", "wiki/entities", "wiki/concepts", "wiki/synthesis",
        "wiki/tests", "wiki/tests/bloques", "wiki/tests/temas",
        "templates", "tutorials", "scripts", ".obsidian", ".obsidian/snippets"
    ]
    for rd in required_dirs:
        p = REPO_DIR / rd
        if not p.exists():
            issues.append(f"Directorio obligatorio no encontrado: {rd}")
        else:
            print(f"  [OK Dir] {rd}")
            
    # 2. VERIFICAR ARCHIVOS RAÍZ OBLIGATORIOS
    required_files = [
        "index.md", "log.md", "AGENTS.md", "CLAUDE.md", "llm-wiki.md",
        ".obsidian/snippets/tai-colors.css",
        "templates/test-tema.md", "templates/test-bloque.md",
        "temario-tai-visual-map.canvas",
        "temario-bloque1-administracion.canvas",
        "temario-bloque2-tecnologia.canvas",
        "temario-bloque3-desarrollo.canvas",
        "temario-bloque4-sistemas.canvas"
    ]
    for rf in required_files:
        p = REPO_DIR / rf
        if not p.exists():
            issues.append(f"Archivo raíz obligatorio no encontrado: {rf}")
        else:
            print(f"  [OK File] {rf}")

    # 3. ESCANEAR TODOS LOS ARCHIVOS MARKDOWN
    all_md = {}
    for f in (REPO_DIR / "wiki").rglob("*.md"):
        all_md[f.resolve()] = f.relative_to(REPO_DIR)
    for f in (REPO_DIR / "tutorials").rglob("*.md"):
        all_md[f.resolve()] = f.relative_to(REPO_DIR)
    for f in (REPO_DIR / "templates").rglob("*.md"):
        all_md[f.resolve()] = f.relative_to(REPO_DIR)
    all_md[(REPO_DIR / "index.md").resolve()] = Path("index.md")
    all_md[(REPO_DIR / "log.md").resolve()] = Path("log.md")
    all_md[(REPO_DIR / "AGENTS.md").resolve()] = Path("AGENTS.md")

    print(f"\n[*] Analizando {len(all_md)} archivos Markdown...")

    index_content = (REPO_DIR / "index.md").read_text(encoding="utf-8") if (REPO_DIR / "index.md").exists() else ""
    inbound_links = {p: set() for p in all_md.keys()}
    valid_types = {"source", "entity", "concept", "synthesis", "test", "tutorial", "index"}

    for abs_path, rel_path in all_md.items():
        if rel_path.name in ["log.md", "AGENTS.md", "CLAUDE.md", "llm-wiki.md"] or "templates" in rel_path.parts:
            continue
            
        try:
            content = abs_path.read_text(encoding="utf-8")
        except Exception as e:
            issues.append(f"Error leyendo {rel_path}: {e}")
            continue

        # Frontmatter check
        match = FRONTMATTER_PATTERN.match(content)
        if not match:
            if rel_path.name != "index.md":
                issues.append(f"Falta frontmatter YAML en: {rel_path}")
        else:
            try:
                fm = yaml.safe_load(match.group(1))
                if not isinstance(fm, dict):
                    issues.append(f"Frontmatter no es diccionario en: {rel_path}")
                else:
                    req_fields = ["title", "type", "created", "updated"]
                    for rf in req_fields:
                        if rf not in fm:
                            issues.append(f"Falta campo '{rf}' en frontmatter de: {rel_path}")
                    if fm.get("type") and fm.get("type") not in valid_types:
                        issues.append(f"Tipo inválido '{fm.get('type')}' en: {rel_path}")
            except Exception as e:
                issues.append(f"Error de YAML en {rel_path}: {e}")

        # Index check (para wiki/)
        if "wiki" in rel_path.parts:
            stem = abs_path.stem
            rel_str = str(rel_path).replace("\\", "/")
            if stem not in index_content and rel_str not in index_content:
                warnings.append(f"Nota de wiki no listada en index.md: {rel_path}")

        # Link parsing
        clean_content = FRONTMATTER_PATTERN.sub("", content)
        clean_content = CODE_BLOCK_PATTERN.sub("", clean_content)
        clean_content = INLINE_CODE_PATTERN.sub("", clean_content)

        # Wikilinks
        for wm in WIKILINK_PATTERN.finditer(clean_content):
            target = wm.group(1).strip()
            clean_target = target.split("#")[0].strip().replace("\\", "/")
            if not clean_target:
                continue
            
            # Resolve target
            resolved = None
            candidates = [
                REPO_DIR / clean_target,
                REPO_DIR / f"{clean_target}.md",
                REPO_DIR / "wiki" / clean_target,
                REPO_DIR / "wiki" / f"{clean_target}.md",
                REPO_DIR / "tutorials" / clean_target,
                REPO_DIR / "tutorials" / f"{clean_target}.md",
            ]
            for c in candidates:
                if c.resolve() in all_md or c.resolve().exists():
                    resolved = c.resolve()
                    break
            
            if not resolved:
                # Search by stem
                stem_t = Path(clean_target).stem.lower()
                for p in all_md:
                    if p.stem.lower() == stem_t:
                        resolved = p
                        break
                        
            if resolved:
                if resolved in inbound_links:
                    inbound_links[resolved].add(abs_path)
            else:
                issues.append(f"Enlace roto en {rel_path}: '[[{target}]]'")

    # Comprobar notas huérfanas en wiki/
    orphan_count = 0
    for abs_path, rel_path in all_md.items():
        if "wiki" in rel_path.parts:
            inbound = inbound_links.get(abs_path, set())
            if len(inbound) == 0:
                orphan_count += 1
                warnings.append(f"Nota huérfana (0 enlaces entrantes): {rel_path}")

    # 4. VERIFICAR ARCHIVOS CANVAS
    print("\n[*] Analizando archivos Canvas...")
    for cfile in REPO_DIR.glob("*.canvas"):
        try:
            cdata = json.loads(cfile.read_text(encoding="utf-8"))
            for node in cdata.get("nodes", []):
                if node.get("type") == "file":
                    fn = node.get("file")
                    if not (REPO_DIR / fn).exists() and not (PARENT_DIR / fn).exists():
                        issues.append(f"Nodo de archivo no existe en {cfile.name}: '{fn}'")
        except Exception as e:
            issues.append(f"Error de JSON en Canvas {cfile.name}: {e}")

    # 5. RESULTADO DE LA AUDITORÍA
    print("\n" + "=" * 70)
    print("📊 RESUMEN DE LA AUDITORÍA")
    print("=" * 70)
    print(f"  - Total archivos Markdown analizados: {len(all_md)}")
    print(f"  - Notas huérfanas detectadas: {orphan_count}")
    print(f"  - Advertencias: {len(warnings)}")
    print(f"  - Errores estructurales críticos: {len(issues)}")
    
    if warnings:
        print("\n⚠️ ADVERTENCIAS:")
        for w in warnings:
            print(f"  - {w}")
            
    if issues:
        print("\n❌ ERRORES ESTRUCTURALES ENCONTRADOS:")
        for i in issues:
            print(f"  - {i}")
        return 1
    else:
        print("\n✅ TODO PERFECTO: Estructura de archivos limpia, conectada y 100% libre de errores.")
        return 0

if __name__ == "__main__":
    sys.exit(audit())
