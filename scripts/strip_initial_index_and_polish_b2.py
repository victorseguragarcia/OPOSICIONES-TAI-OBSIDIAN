# -*- coding: utf-8 -*-
r"""
Script definitivo para limpiar la cabecera/índice inicial duplicado y dejar el texto
100% limpio, profesional y estructurado en los 5 Temas Completos de Bloque 2.
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
B2_TC_DIR = REPO_DIR / "wiki" / "synthesis" / "temas-completos" / "bloque-2-hardware-so"

print("=" * 70)
print("🧼 ELIMINANDO ÍNDICE INICIAL Y FORMATEANDO CUERPO BLOQUE 2")
print("=" * 70)

def strip_initial_index_and_polish(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Si encontramos el índice inicial que termina antes de que empiece el texto real
    # Buscamos patrones como "## 🟣 5. Bibliografía" o secuencias de títulos antes de párrafos largos
    # Buscamos la primera aparición de un párrafo explicativo de más de 120 caracteres o frases características
    m = re.search(r"(La mayoría de las fuentes|El concepto de computador|Las estructuras de datos|Un sistema operativo|El modelo de base de datos|Un periférico es|En este tema|A lo largo de la historia)", body)
    if m:
        start_pos = m.start()
        # retroceder al título inmediatamente anterior
        preceding = body[:start_pos]
        last_h2 = preceding.rfind("## 🟣 1.")
        if last_h2 != -1:
            header_part = body[:body.find("# 🔴")] # breadcrumbs y encabezado H1
            # Reconstruir desde H1 hasta el título real
            h1_match = re.search(r"(# 🔴[^\n]+\n+> \[!repaso\][^\n]+\n+>[^\n]+\n+---)", body)
            if h1_match:
                top_part = body[:h1_match.end()]
                real_body = body[last_h2:]
                body = top_part + "\n\n" + real_body
                
    # 2. Formatear términos clave sueltos en negrita o encabezados
    body = re.sub(r"\n([A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚáéíóú\s]{3,40})\n(?=[A-ZÁÉÍÓÚ“\"'¿])", r"\n### 🔵 \1\n", body)
    
    # 3. Limpiar múltiples líneas vacías
    body = re.sub(r"\n{3,}", "\n\n", body)
    
    # 4. Asegurar formato de llamadas Obsidian
    body = re.sub(r"\n### 🔵 Definición\n", "\n\n> [!info] **Definición**\n", body)
    body = re.sub(r"\n### 🔵 Resumiendo\n", "\n\n> [!repaso] **Resumen**\n", body)
    body = re.sub(r"\n### 🔵 Importante\n", "\n\n> [!important] **Punto Clave de Examen**\n", body)
    body = re.sub(r"\n### 🔵 Recuerda\n", "\n\n> [!tip] **Recuerda**\n", body)
    
    # 5. Pulido de LaTeX
    body = body.replace("\text", "\\text").replace("\times", "\\times")
    
    return f"---{frontmatter}---\n{body.strip()}\n"

for tnum in range(1, 6):
    fname = f"tema-completo-bloque2-tema{tnum:02d}.md"
    fpath = B2_TC_DIR / fname
    if not fpath.exists():
        continue
    raw_content = fpath.read_text(encoding="utf-8")
    cleaned_content = strip_initial_index_and_polish(raw_content)
    fpath.write_text(cleaned_content, encoding="utf-8")
    print(f"  [Polished Theme Body] {fname} ({len(cleaned_content.splitlines())} líneas)")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
