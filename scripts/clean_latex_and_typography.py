# -*- coding: utf-8 -*-
r"""
Script de limpieza y pulido tipográfico:
Corrige automáticamente cualquier escape roto de LaTeX (\rightarrow, \implies, etc.),
saltos de línea accidentales dentro de fórmulas matemáticas y normaliza la tipografía en toda la wiki.
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

print("=" * 70)
print("🧹 LIMPIEZA Y PULIDO TIPOGRÁFICO DE TODAS LAS NOTAS DE LA WIKI")
print("=" * 70)

fixed_files = []

for root, dirs, files in os.walk(REPO_DIR):
    if ".git" in root or "node_modules" in root or ".quartz" in root:
        continue
    for file in files:
        if not file.endswith(".md"):
            continue
        fp = Path(root) / file
        content = fp.read_text(encoding="utf-8")
        original = content

        # 1. Corregir \rightarrow roto con saltos de línea \r\n o \n
        content = re.sub(r"\$\s*[\r\n]+\s*ightarrow\s*\$", r" $\\rightarrow$ ", content)
        content = re.sub(r"\$\s*[\r\n]+\s*rightarrow\s*\$", r" $\\rightarrow$ ", content)
        content = re.sub(r"\$\s*[\r\n]+\s*	arrow\s*\$", r" $\\rightarrow$ ", content)
        content = re.sub(r"[\r\n]+\s*ightarrow\$", r" $\\rightarrow$", content)
        content = re.sub(r"\$\s*ightarrow\s*", r" $\\rightarrow$ ", content)
        
        # 2. Corregir \implies rotos
        content = re.sub(r"\$\s*[\r\n]+\s*implies\s*\$", r" $\\implies$ ", content)
        
        # 3. Limpiar espacios dobles alrededor de flechas
        content = re.sub(r"\s+\$\\rightarrow\$\s+", r" $\\rightarrow$ ", content)

        if content != original:
            fp.write_text(content, encoding="utf-8")
            rel_p = fp.relative_to(REPO_DIR)
            fixed_files.append(rel_p)
            print(f"  [Fixed Typography] {rel_p}")

print(f"\n[*] Limpieza finalizada. Total de archivos pulidos y corregidos: {len(fixed_files)}")

# Sincronizar directorio wiki con el baúl superior
for d in ["wiki"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado directorio en baúl superior: {d}")
