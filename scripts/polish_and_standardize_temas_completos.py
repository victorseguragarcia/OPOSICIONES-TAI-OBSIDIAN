# -*- coding: utf-8 -*-
r"""
Script para revisar, pulir y estandarizar la estructura de todos los 34 Temas Completos
en 'wiki/synthesis/temas-completos/' aplicando la jerarquía cromática (🔴 H1, 🟣 H2, 🔵 H3),
limpieza de encabezados duplicados, tipografía, negritas clave y tablas.
"""
import os
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")
TC_DIR = REPO_DIR / "wiki" / "synthesis" / "temas-completos"

print("=" * 70)
print("🎨 PULIENDO Y ESTANDARIZANDO ESTRUCTURA DE 'TEMAS-COMPLETOS'")
print("=" * 70)

def polish_content(content):
    # 1. Corregir escapes de LaTeX
    content = content.replace("$\n\tightarrow$", " $\\rightarrow$ ").replace("$\n ightarrow$", " $\\rightarrow$ ")
    content = content.replace("\r\n", "\n")
    
    # 2. Separar frontmatter y cuerpo
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 3. Eliminar el encabezado genérico duplicado '## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro'
    # si inmediatamente sigue otro encabezado de nivel 2 o 1
    body = re.sub(r"## 🟣 1\. Desarrollo Teórico[^\n]+\n+", "", body)
    
    # 4. Asegurar jerarquía cromática en encabezados del cuerpo
    lines = body.split("\n")
    new_lines = []
    
    for line in lines:
        # H1 principal
        if line.startswith("# ") and not line.startswith("# 🔴"):
            line = re.sub(r"^#\s+(?:🔴\s*)?", "# 🔴 ", line)
        # H2 secciones
        elif line.startswith("## ") and not line.startswith("## 🟣") and not line.startswith("## 🔵"):
            line = re.sub(r"^##\s+", "## 🟣 ", line)
        # H3 subsecciones
        elif line.startswith("### ") and not line.startswith("### 🔵"):
            line = re.sub(r"^###\s+", "### 🔵 ", line)
        # H4 subpuntos
        elif line.startswith("#### ") and not line.startswith("#### 🔹"):
            line = re.sub(r"^####\s+", "#### 🔹 ", line)
            
        new_lines.append(line)
        
    polished_body = "\n".join(new_lines)
    
    # Normalizar espaciado de separadores horizontales
    polished_body = re.sub(r"\n{3,}", "\n\n", polished_body)
    
    return f"---{frontmatter}---\n{polished_body.strip()}\n"

polished_count = 0

for root, dirs, files in os.walk(TC_DIR):
    for file in sorted(files):
        if not file.endswith(".md"):
            continue
        fp = Path(root) / file
        raw_text = fp.read_text(encoding="utf-8")
        polished_text = polish_content(raw_text)
        
        if polished_text != raw_text:
            fp.write_text(polished_text, encoding="utf-8")
            polished_count += 1
            print(f"  [Polished Theme] {fp.relative_to(TC_DIR)}")

# Sincronizar directorio de síntesis en el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print(f"\n[*] Estandarización completada. Total archivos pulidos: {polished_count}")
