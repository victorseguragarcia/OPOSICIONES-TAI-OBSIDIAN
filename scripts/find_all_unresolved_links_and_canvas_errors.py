# -*- coding: utf-8 -*-
r"""
Script de rastreo exhaustivo de errores 'No se encontró' / enlaces no resueltos en Obsidian.
Verifica:
1. Todos los archivos .canvas en el workspace y en el baúl padre.
2. Todas las referencias 'file' de nodos Canvas.
3. Todos los wikilinks [[...]] e incrustaciones ![[...]] en todas las notas Markdown.
4. Coincidencias exactas e insensibles a mayúsculas/minúsculas.
"""
import os
import re
import sys
import json
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

WIKILINK_REGEX = re.compile(r"!?\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MDLINK_REGEX = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
CODE_BLOCK_REGEX = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_REGEX = re.compile(r"`[^`]+`")

def run_scan():
    print("=" * 70)
    print("🔍 RASTREO EXHAUSTIVO DE ERRORES 'NO SE ENCONTRÓ' EN OBSIDIAN")
    print("=" * 70)

    # 1. Indexar todos los archivos existentes en ambos directorios
    repo_files = {}
    for p in REPO_DIR.rglob("*"):
        if p.is_file() and not any(part.startswith(".git") for part in p.parts):
            rel = p.relative_to(REPO_DIR).as_posix().lower()
            repo_files[rel] = p
            repo_files[p.name.lower()] = p
            repo_files[p.stem.lower()] = p

    parent_files = {}
    for p in PARENT_DIR.rglob("*"):
        if p.is_file() and not any(part.startswith(".git") for part in p.parts):
            rel = p.relative_to(PARENT_DIR).as_posix().lower()
            parent_files[rel] = p
            parent_files[p.name.lower()] = p
            parent_files[p.stem.lower()] = p

    errors = []

    # 2. Revisar archivos Canvas (.canvas)
    canvas_dirs = [REPO_DIR, PARENT_DIR]
    scanned_canvas = set()
    
    print("\n--- 1. ESCANEANDO ARCHIVOS OBSIDIAN CANVAS (.canvas) ---")
    for cdir in canvas_dirs:
        for cfile in cdir.glob("*.canvas"):
            if cfile.resolve() in scanned_canvas:
                continue
            scanned_canvas.add(cfile.resolve())
            
            try:
                data = json.loads(cfile.read_text(encoding="utf-8"))
            except Exception as e:
                errors.append(f"Error JSON en {cfile}: {e}")
                continue

            nodes = data.get("nodes", [])
            print(f"[*] Analizando {cfile.name} ({len(nodes)} nodos) en '{cfile.parent.name}'...")
            
            for node in nodes:
                if node.get("type") == "file":
                    target = node.get("file", "")
                    clean_target = target.replace("\\", "/").lower()
                    
                    # Comprobar si existe en REPO_DIR o en PARENT_DIR
                    found_in_repo = (
                        clean_target in repo_files or
                        Path(clean_target).name.lower() in repo_files or
                        Path(clean_target).stem.lower() in repo_files or
                        (REPO_DIR / target).exists()
                    )
                    found_in_parent = (
                        clean_target in parent_files or
                        Path(clean_target).name.lower() in parent_files or
                        Path(clean_target).stem.lower() in parent_files or
                        (PARENT_DIR / target).exists()
                    )

                    if not found_in_repo and not found_in_parent:
                        errors.append(f"[CANVAS] En '{cfile.name}': Nodo 'file' NO encontrado: '{target}'")
                    else:
                        print(f"    ✓ Nodo válido: '{target}'")

    # 3. Revisar notas Markdown (.md)
    print("\n--- 2. ESCANEANDO WIKILINKS E INCRUSTACIONES EN MARKDOWN ---")
    md_files = list(REPO_DIR.rglob("*.md"))
    print(f"[*] Analizando {len(md_files)} notas Markdown...")
    
    for md_file in md_files:
        if any(part.startswith(".git") for part in md_file.parts):
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            errors.append(f"Error leyendo {md_file}: {e}")
            continue

        clean_content = CODE_BLOCK_REGEX.sub("", content)
        clean_content = INLINE_CODE_REGEX.sub("", clean_content)

        # Buscar todos los [[...]]
        for match in WIKILINK_REGEX.finditer(clean_content):
            raw_target = match.group(1).strip()
            clean_t = raw_target.replace("\\", "/").strip().lower()
            if not clean_t:
                continue

            # Comprobar resolución en repo_files
            resolved = (
                clean_t in repo_files or
                f"{clean_t}.md" in repo_files or
                Path(clean_t).name in repo_files or
                Path(clean_t).stem in repo_files or
                (REPO_DIR / raw_target).exists() or
                (REPO_DIR / f"{raw_target}.md").exists()
            )

            if not resolved:
                errors.append(f"[MARKDOWN] En '{md_file.relative_to(REPO_DIR)}': Enlace roto: '[[{raw_target}]]'")

    # 4. Reporte final
    print("\n" + "=" * 70)
    print("📊 RESULTADO DEL RASTREO")
    print("=" * 70)
    if errors:
        print(f"❌ SE ENCONTRARON {len(errors)} ERRORES DE 'NO SE ENCONTRÓ':")
        for err in errors:
            print(f"  - {err}")
        return 1
    else:
        print("✅ CERO ERRORES: Todos los archivos de Canvas, enlaces [[...]] e incrustaciones resuelven al 100%.")
        return 0

if __name__ == "__main__":
    sys.exit(run_scan())
