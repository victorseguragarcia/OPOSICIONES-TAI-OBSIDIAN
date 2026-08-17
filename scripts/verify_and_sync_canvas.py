# -*- coding: utf-8 -*-
import os
import json
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes"
PARENT_DIR = r"d:\Desktop\TAI OPOSICIONES"

canvas_files = [
    "temario-bloque1-administracion.canvas",
    "temario-bloque2-tecnologia.canvas",
    "temario-bloque3-desarrollo.canvas",
    "temario-bloque4-sistemas.canvas",
    "temario-tai-visual-map.canvas"
]

print("[*] Verificando archivos de Canvas...")
for cf in canvas_files:
    fpath = os.path.join(REPO_DIR, cf)
    if not os.path.exists(fpath):
        print(f"  [!] No existe {cf}")
        continue
    with open(fpath, "r", encoding="utf-8") as f:
        data = json.load(f)
    print(f"\n--- {cf} ({len(data.get('nodes', []))} nodos) ---")
    for n in data.get("nodes", []):
        if n.get("type") == "file":
            target_f = n.get("file")
            full_target = os.path.join(REPO_DIR, target_f)
            exists_in_repo = os.path.exists(full_target)
            parent_target = os.path.join(PARENT_DIR, target_f)
            exists_in_parent = os.path.exists(parent_target)
            print(f"  [File Node] '{target_f}' | Repo: {exists_in_repo} | Parent: {exists_in_parent}")
            
    # Sincronizar hacia el directorio padre
    parent_cf = os.path.join(PARENT_DIR, cf)
    shutil.copy2(fpath, parent_cf)
    print(f"  [OK] Sincronizado a {parent_cf}")

print("\n[*] Sincronización de Canvas completada.")
