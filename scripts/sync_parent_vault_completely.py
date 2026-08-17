# -*- coding: utf-8 -*-
import os
import shutil
import json
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes"
PARENT_DIR = r"d:\Desktop\TAI OPOSICIONES"

# 1. Eliminar junction si existe
parent_wiki = os.path.join(PARENT_DIR, "wiki")
if os.path.exists(parent_wiki):
    subprocess.run(f'cmd /c rmdir "{parent_wiki}"', shell=True)

# 2. Copiar directorios completos
for d in ["wiki", "templates", "tutorials", ".obsidian"]:
    src = os.path.join(REPO_DIR, d)
    dst = os.path.join(PARENT_DIR, d)
    if os.path.exists(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"[OK] Sincronizado directorio real: {d}")

# 3. Copiar archivos raíz
for f in ["index.md", "log.md", "README.md", "LICENSE", "AGENTS.md", "CLAUDE.md"]:
    src = os.path.join(REPO_DIR, f)
    dst = os.path.join(PARENT_DIR, f)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"[OK] Sincronizado archivo: {f}")

# 4. Actualizar Canvas en ambos sitios
canvas_names = [
    "temario-tai-visual-map.canvas",
    "temario-bloque1-administracion.canvas",
    "temario-bloque2-tecnologia.canvas",
    "temario-bloque3-desarrollo.canvas",
    "temario-bloque4-sistemas.canvas",
]

for cf in canvas_names:
    src_cf = os.path.join(REPO_DIR, cf)
    dst_cf = os.path.join(PARENT_DIR, cf)
    if os.path.exists(src_cf):
        shutil.copy2(src_cf, dst_cf)
        print(f"[OK] Sincronizado Canvas: {cf}")

print("\n[*] Sincronización completa con el baúl superior finalizada con éxito.")
