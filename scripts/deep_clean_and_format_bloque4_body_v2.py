# -*- coding: utf-8 -*-
r"""
Script maestro v2 para limpiar a fondo, formatear y estructurar profesionalmente
los 10 Temas Completos del Bloque 4 (Sistemas, Redes y Seguridad):
- Elimina el índice inicial duplicado
- Conecta el desarrollo directamente con el Capítulo 1
- Limpia cortes de página y cabeceras
- Formatea callouts y viñetas
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
B4_TC_DIR = REPO_DIR / "wiki" / "synthesis" / "temas-completos" / "bloque-4-sistemas-redes"

print("=" * 70)
print("🧼 LIMPIEZA DEFINITIVA DEL CUERPO - TEMAS COMPLETOS BLOQUE 4")
print("=" * 70)

def strip_index_and_clean_b4(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Localizar la primera aparición del contenido real (después del índice de bibliografía o primer párrafo sustancial)
    m = re.search(r"(Podemos clasificar el software|Un servicio de directorio|La virtualización es|Un Centro de Proceso de Datos|Las copias de seguridad son|Los medios de transmisión son|El protocolo IP|El protocolo TCP|La seguridad de la información|Un cortafuegos es|A lo largo de|En este tema)", body)
    if m:
        start_pos = m.start()
        preceding = body[:start_pos]
        last_h2 = preceding.rfind("## 🟣 1.")
        if last_h2 != -1:
            h1_match = re.search(r"(# 🔴[^\n]+\n+> \[!repaso\][^\n]+\n+>[^\n]+\n+---)", body)
            if h1_match:
                top_part = body[:h1_match.end()]
                real_body = body[last_h2:]
                body = top_part + "\n\n" + real_body
                
    # 2. Formatear términos clave sueltos en encabezados
    body = re.sub(r"\n([A-ZÁÉÍÓÚ][A-Za-zÁÉÍÓÚáéíóú\s]{3,40})\n(?=[A-ZÁÉÍÓÚ“\"'¿])", r"\n### 🔵 \1\n", body)
    
    # 3. Formatear llamadas
    body = re.sub(r"\n### 🔵 Definición\n", "\n\n> [!info] **Definición**\n", body)
    body = re.sub(r"\n### 🔵 Resumiendo\n", "\n\n> [!repaso] **Resumen**\n", body)
    body = re.sub(r"\n### 🔵 Importante\n", "\n\n> [!important] **Importante**\n", body)
    body = re.sub(r"\n### 🔵 Recuerda\n", "\n\n> [!tip] **Recuerda**\n", body)
    
    # 4. Limpiar múltiples líneas vacías
    body = re.sub(r"\n{3,}", "\n\n", body)
    
    # 5. Pulido de LaTeX
    body = body.replace("\text", "\\text").replace("\times", "\\times")
    
    return f"---{frontmatter}---\n{body.strip()}\n"

for tnum in range(1, 11):
    fname = f"tema-completo-bloque4-tema{tnum:02d}.md"
    fpath = B4_TC_DIR / fname
    if not fpath.exists():
        continue
    raw_content = fpath.read_text(encoding="utf-8")
    cleaned_content = strip_index_and_clean_b4(raw_content)
    fpath.write_text(cleaned_content, encoding="utf-8")
    print(f"  [Deep Cleaned Bloque 4] {fname} ({len(cleaned_content.splitlines())} líneas)")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
