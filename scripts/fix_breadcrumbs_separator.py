# -*- coding: utf-8 -*-
r"""
Script para corregir el separador &nbsp;|&nbsp; en todas las barras de navegación
de los resúmenes, sustituyéndolo por un separador limpio Markdown ( • | • ).
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")
RESUMENES_DIR = REPO_DIR / "wiki" / "synthesis" / "resumenes"

print("=" * 70)
print("🧹 CORRIGIENDO SEPARADORES &nbsp;|&nbsp; EN LAS BARRAS DE NAVEGACIÓN")
print("=" * 70)

fixed_count = 0

for root, dirs, files in os.walk(RESUMENES_DIR):
    for file in files:
        if not file.endswith(".md"):
            continue
        fp = Path(root) / file
        content = fp.read_text(encoding="utf-8")
        original = content
        
        # Reemplazar &nbsp;|&nbsp; por un separador limpio
        content = content.replace("&nbsp;|&nbsp;", " · ")
        content = content.replace("&nbsp;", " ")
        
        if content != original:
            fp.write_text(content, encoding="utf-8")
            fixed_count += 1
            print(f"  [Fixed Breadcrumb] {fp.relative_to(REPO_DIR)}")

# Sincronizar directorio de síntesis en el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print(f"\n[*] Limpieza completada. Total notas corregidas: {fixed_count}")
