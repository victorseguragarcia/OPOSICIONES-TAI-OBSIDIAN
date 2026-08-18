# -*- coding: utf-8 -*-
r"""
Script maestro para limpiar a fondo, formatear y estructurar profesionalmente
los 9 Temas Completos del Bloque 3 (Desarrollo y BBDD):
- Elimina índices de portada duplicados y números de página
- Elimina publicidad de academia ('Recuerda ver las clases...', 'ACCEDE DIRECTAMENTE...')
- Elimina cortes de página <!-- Page X --> y cabeceras recurrentes del PDF
- Convierte títulos numerados a jerarquía cromática (## 🟣, ### 🔵, #### 🔹)
- Convierte viñetas '•' en '- '
- Formatea definiciones, resúmenes y avisos en callouts de Obsidian
- Corrige saltos de línea partidos a mitad de frase
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
B3_TC_DIR = REPO_DIR / "wiki" / "synthesis" / "temas-completos" / "bloque-3-desarrollo-bbdd"

print("=" * 70)
print("🧼 LIMPIEZA PROFUNDA Y FORMATEO - TEMAS COMPLETOS BLOQUE 3")
print("=" * 70)

# Cabeceras y frases de ruido conocidas
ACADEMIA_NOISE = [
    r"<!--\s*Page\s*\d+\s*-->",
    r"###\s*Página\s*\d+",
    r"Recuerda ver las clases emitidas en Temario\s+Audiovisual.*?(?:ACCEDE DIRECTAMENTE DESDE AQUÍ|aquí)",
    r"Las clases impartidas en directo y disponibles en Campus.*?(?:ACCEDE DIRECTAMENTE DESDE AQUÍ|aquí)",
    r"ACCEDE DIRECTAMENTE DESDE AQUÍ",
    r"Temario Audiovisual",
    r"Campus Virtual",
    r"Modelado de datos,\s+metodologías y reglas[^\n]+",
    r"Lenguajes de programación[^\n]+",
    r"El lenguaje SQL[^\n]+",
    r"Programación orientada a objetos[^\n]+",
    r"Arquitectura de sistemas web[^\n]+",
    r"Servicios web[^\n]+",
    r"Diseño web y accesibilidad[^\n]+",
    r"Metodologías de desarrollo[^\n]+",
    r"Calidad del software y pruebas[^\n]+"
]

def clean_and_format_b3_topic(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Eliminar ruido publicitario y avisos de campus
    for pat in ACADEMIA_NOISE:
        body = re.sub(pat, "", body, flags=re.IGNORECASE | re.DOTALL)
        
    lines = body.split("\n")
    cleaned_lines = []
    in_raw_index = False
    
    for idx, line in enumerate(lines):
        stripped = line.strip()
        
        # Detectar inicio del índice en crudo del PDF
        if stripped.upper() == "ÍNDICE" or stripped.upper() == "INDICE":
            in_raw_index = True
            continue
            
        if in_raw_index:
            # Salir del índice cuando encontramos contenido real o párrafo explicativo largo
            if (len(stripped) > 50 and not re.match(r"^\d+(\.\d+)*\s+.*\s+\d+$", stripped)) or ("## 🟣" in stripped and idx > 15):
                in_raw_index = False
            elif re.match(r"^\d+\.\s+[A-ZÁÉÍÓÚ]", stripped) and not any(c.isdigit() for c in stripped[-4:]):
                in_raw_index = False
            else:
                continue # Saltar líneas del índice en crudo
                
        # Filtrar números de página sueltos
        if re.match(r"^\d{1,3}$", stripped):
            continue
            
        # Convertir títulos numerados en encabezados Markdown con jerarquía cromática
        m1 = re.match(r"^(\d+)\.\s+([A-ZÁÉÍÓÚ].*)$", stripped)
        if m1 and len(stripped) < 80 and not stripped.endswith("."):
            line = f"## 🟣 {m1.group(1)}. {m1.group(2)}"
            
        m2 = re.match(r"^(\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m2 and len(stripped) < 90 and not stripped.endswith("."):
            line = f"### 🔵 {m2.group(1)}. {m2.group(2)}"
            
        m3 = re.match(r"^(\d+\.\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m3 and len(stripped) < 100 and not stripped.endswith("."):
            line = f"#### 🔹 {m3.group(1)}. {m3.group(2)}"
            
        m4 = re.match(r"^(\d+\.\d+\.\d+\.\d+)\.\s+([A-ZÁÉÍÓÚa-záéíóú¿].*)$", stripped)
        if m4 and len(stripped) < 110 and not stripped.endswith("."):
            line = f"##### {m4.group(1)}. {m4.group(2)}"
            
        # Normalizar viñetas '•' a '- '
        if stripped.startswith("•"):
            line = "- " + stripped[1:].strip()
        elif stripped.startswith(""):
            line = "- " + stripped[1:].strip()
            
        cleaned_lines.append(line)
        
    body_text = "\n".join(cleaned_lines)
    
    # 2. Localizar y eliminar el índice inicial duplicado si existe antes del primer contenido real
    m = re.search(r"(A lo largo de la historia|El concepto de|En este tema|Una base de datos|El diseño de bases|Los lenguajes de|El estándar SQL|La programación orientada|La arquitectura de|Un servicio web|La accesibilidad web|El control de versiones|La metodología MÉTRICA|El ciclo de vida)", body_text)
    if m:
        start_pos = m.start()
        preceding = body_text[:start_pos]
        last_h2 = preceding.rfind("## 🟣 1.")
        if last_h2 != -1:
            h1_match = re.search(r"(# 🔴[^\n]+\n+> \[!repaso\][^\n]+\n+>[^\n]+\n+---)", body_text)
            if h1_match:
                top_part = body_text[:h1_match.end()]
                real_body = body_text[last_h2:]
                body_text = top_part + "\n\n" + real_body
                
    # 3. Formatear llamadas clave
    body_text = re.sub(r"\nDefinición\n", "\n\n> [!info] **Definición**\n", body_text)
    body_text = re.sub(r"\nResumiendo\n", "\n\n> [!repaso] **Resumen**\n", body_text)
    body_text = re.sub(r"\n¡Ojo!\n", "\n\n> [!warning] **¡Atención!**\n", body_text)
    body_text = re.sub(r"\nImportante\n", "\n\n> [!important] **Importante**\n", body_text)
    body_text = re.sub(r"\nRecuerda\n", "\n\n> [!tip] **Recuerda**\n", body_text)
    
    # 4. Normalizar saltos de línea rotos en medio de frases
    body_text = re.sub(r"([a-záéíóúA-ZÁÉÍÓÚ0-9,\(\)])\n([a-záéíóú])", r"\1 \2", body_text)
    
    # 5. Normalizar espacios en blanco
    body_text = re.sub(r"\n{3,}", "\n\n", body_text)
    
    # 6. Pulido de LaTeX
    body_text = body_text.replace("\text", "\\text").replace("\times", "\\times")
    
    return f"---{frontmatter}---\n{body_text.strip()}\n"

for tnum in range(1, 10):
    fname = f"tema-completo-bloque3-tema{tnum:02d}.md"
    fpath = B3_TC_DIR / fname
    if not fpath.exists():
        continue
    raw_content = fpath.read_text(encoding="utf-8")
    cleaned_content = clean_and_format_b3_topic(raw_content)
    fpath.write_text(cleaned_content, encoding="utf-8")
    print(f"  [Cleaned & Formatted Bloque 3] {fname} ({len(cleaned_content.splitlines())} líneas)")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
