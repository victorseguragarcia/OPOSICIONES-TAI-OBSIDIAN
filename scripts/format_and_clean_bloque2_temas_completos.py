# -*- coding: utf-8 -*-
r"""
Script para formatear, limpiar y estructurar profesionalmente los 5 Temas Completos
de 'wiki/synthesis/temas-completos/bloque-2-hardware-so/', eliminando ruido OCR,
índices en crudo, cortes de página y formateando títulos, párrafos y listas.
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
print("🧹 FORMATEANDO Y LIMPIANDO TEXTO EN TEMAS COMPLETOS BLOQUE 2")
print("=" * 70)

def clean_ocr_and_format_text(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Eliminar páginas e índices en crudo
    body = re.sub(r"<!--\s*Page\s*\d+\s*-->", "", body, flags=re.IGNORECASE)
    body = re.sub(r"###\s*Página\s*\d+", "", body, flags=re.IGNORECASE)
    body = re.sub(r"DV\.TextoHTML\([^\)]+\)\.Esp\.dot\s+\|\s+UD\d+_[^\n]+", "", body)
    body = re.sub(r"davante\.es\s+\|\s+UD\d+_[^\n]+", "", body)
    body = re.sub(r"administracion\.gob\.es\s+\|\s+UD\d+_[^\n]+", "", body)
    
    # 2. Eliminar el bloque de ÍNDICE con números de página
    # Buscamos desde ÍNDICE hasta el primer título real
    lines = body.split("\n")
    cleaned_lines = []
    in_raw_index = False
    
    for line in lines:
        stripped = line.strip()
        
        # Detectar inicio de índice en crudo
        if stripped.upper() == "ÍNDICE" or stripped.upper() == "INDICE":
            in_raw_index = True
            continue
            
        if in_raw_index:
            # Salir del índice cuando encontramos contenido real (párrafo largo o título de nivel 1 con texto sustancial)
            if (len(stripped) > 40 and not re.match(r"^\d+(\.\d+)*\s+.*\s+\d+$", stripped)) or "## 🟣" in stripped:
                in_raw_index = False
            elif re.match(r"^\d+\.\s+[A-ZÁÉÍÓÚ]", stripped) and not any(c.isdigit() for c in stripped[-4:]):
                in_raw_index = False
            else:
                continue # Saltar líneas del índice en crudo
                
        # Filtrar números sueltos de página (ej. líneas con solo "4", "12", "58")
        if re.match(r"^\d{1,3}$", stripped):
            continue
            
        # Convertir títulos numerados en encabezados Markdown con jerarquía cromática
        # Nivel 1: "1. Título" -> "## 🟣 1. Título"
        m1 = re.match(r"^(\d+)\.\s+([A-ZÁÉÍÓÚ].*)$", stripped)
        if m1 and len(stripped) < 80 and not stripped.endswith("."):
            line = f"## 🟣 {m1.group(1)}. {m1.group(2)}"
            
        # Nivel 2: "1.1. Título" -> "### 🔵 1.1. Título"
        m2 = re.match(r"^(\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m2 and len(stripped) < 90 and not stripped.endswith("."):
            line = f"### 🔵 {m2.group(1)}. {m2.group(2)}"
            
        # Nivel 3: "1.1.1. Título" -> "#### 🔹 1.1.1. Título"
        m3 = re.match(r"^(\d+\.\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m3 and len(stripped) < 100 and not stripped.endswith("."):
            line = f"#### 🔹 {m3.group(1)}. {m3.group(2)}"
            
        # Nivel 4: "1.1.1.1. Título" -> "##### 1.1.1.1. Título"
        m4 = re.match(r"^(\d+\.\d+\.\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m4 and len(stripped) < 110 and not stripped.endswith("."):
            line = f"##### {m4.group(1)}. {m4.group(2)}"
            
        cleaned_lines.append(line)
        
    cleaned_body = "\n".join(cleaned_lines)
    
    # 3. Unir saltos de línea rotos en medio de oraciones (soft line breaks de OCR)
    # Si una línea no termina en punto, dos puntos, interrogación o exclamación, y la siguiente empieza en minúscula
    cleaned_body = re.sub(r"([a-záéíóúA-ZÁÉÍÓÚ0-9,\(\)])\n([a-záéíóú])", r"\1 \2", cleaned_body)
    
    # 4. Normalizar múltiples líneas en blanco
    cleaned_body = re.sub(r"\n{3,}", "\n\n", cleaned_body)
    
    # 5. Pulido de LaTeX
    cleaned_body = cleaned_body.replace("\text", "\\text").replace("\times", "\\times")
    cleaned_body = cleaned_body.replace("$\n\tightarrow$", " $\\rightarrow$ ").replace("$\n ightarrow$", " $\\rightarrow$ ")
    
    return f"---{frontmatter}---\n{cleaned_body.strip()}\n"

for tnum in range(1, 6):
    fname = f"tema-completo-bloque2-tema{tnum:02d}.md"
    fpath = B2_TC_DIR / fname
    if not fpath.exists():
        continue
    raw_content = fpath.read_text(encoding="utf-8")
    cleaned_content = clean_ocr_and_format_text(raw_content)
    fpath.write_text(cleaned_content, encoding="utf-8")
    print(f"  [Cleaned & Formatted] {fname} ({len(cleaned_content.splitlines())} líneas)")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
