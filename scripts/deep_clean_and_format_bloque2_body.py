# -*- coding: utf-8 -*-
r"""
Script para limpiar a fondo el cuerpo de los 5 Temas Completos de Bloque 2:
- Elimina índices de portada duplicados
- Elimina publicidad de academia ('Recuerda ver las clases...', 'ACCEDE DIRECTAMENTE...')
- Elimina cabeceras y pies de página recurrentes del PDF
- Convierte viñetas '•' en '- '
- Da formato limpio a definiciones y párrafos
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
print("🧼 LIMPIEZA PROFUNDA DEL CUERPO DE TEXTO - TEMAS COMPLETOS BLOQUE 2")
print("=" * 70)

# Cabeceras y frases de ruido conocidas
ACADEMIA_NOISE = [
    r"Recuerda ver las clases emitidas en Temario\s+Audiovisual.*?(?:ACCEDE DIRECTAMENTE DESDE AQUÍ|aquí)",
    r"Las clases impartidas en directo y disponibles en Campus.*?(?:ACCEDE DIRECTAMENTE DESDE AQUÍ|aquí)",
    r"ACCEDE DIRECTAMENTE DESDE AQUÍ",
    r"Temario Audiovisual",
    r"Campus Virtual",
    r"Informática básica\.\s+Representación y comunicación de la información:\s+elementos constitutivos de un sistema\s+de información",
    r"Estructura y componentes de los sistemas informáticos[^\n]+",
    r"Periféricos:[^\n]+",
    r"Estructuras de datos[^\n]+",
    r"Sistemas operativos[^\n]+",
    r"Bases de datos[^\n]+"
]

def deep_clean_body(content):
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    frontmatter = parts[1]
    body = parts[2]
    
    # 1. Eliminar ruido publicitario y avisos de campus
    for pat in ACADEMIA_NOISE:
        body = re.sub(pat, "", body, flags=re.IGNORECASE | re.DOTALL)
        
    # 2. Localizar y eliminar el índice inicial duplicado si existe antes del primer contenido real
    # Si encontramos una secuencia densa de títulos sin párrafos intermedios
    lines = body.split("\n")
    cleaned_lines = []
    
    in_initial_index_dump = True
    for idx, line in enumerate(lines):
        stripped = line.strip()
        
        # Saltamos líneas vacías iniciales
        if in_initial_index_dump:
            # Si vemos párrafos explicativos largos (más de 60 caracteres y no es un título)
            if len(stripped) > 60 and not stripped.startswith("#"):
                in_initial_index_dump = False
            elif "La mayoría de las fuentes" in stripped or "En inglés:" in stripped or "Un ordenador es" in stripped:
                in_initial_index_dump = False
            elif re.match(r"^## 🟣 1\.", stripped) and idx > 25:
                in_initial_index_dump = False
                cleaned_lines.append(line)
                continue
            else:
                # Si estamos en el índice inicial duplicado y es solo un título o numeración suelta, saltar
                if re.match(r"^(#{1,6}\s+|[0-9\.\s]+|\bÍNDICE\b)", stripped) and idx < 100:
                    continue
                    
        # Normalizar viñetas '•' a '- '
        if stripped.startswith("•"):
            line = "- " + stripped[1:].strip()
        elif stripped.startswith(""):
            line = "- " + stripped[1:].strip()
            
        # Limpiar números de página aislados
        if re.match(r"^\d{1,3}$", stripped):
            continue
            
        cleaned_lines.append(line)
        
    body_text = "\n".join(cleaned_lines)
    
    # 3. Eliminar cabeceras de página repetidas (líneas aisladas con el título de la unidad)
    body_text = re.sub(r"\nInformática básica\.\s+Representación[^\n]+\n", "\n", body_text, flags=re.IGNORECASE)
    body_text = re.sub(r"\nPeriféricos\.\s+Conectividad[^\n]+\n", "\n", body_text, flags=re.IGNORECASE)
    body_text = re.sub(r"\nEstructuras de datos\.\s+Ficheros[^\n]+\n", "\n", body_text, flags=re.IGNORECASE)
    body_text = re.sub(r"\nSistemas operativos\.\s+Gestión[^\n]+\n", "\n", body_text, flags=re.IGNORECASE)
    body_text = re.sub(r"\nBases de datos\.\s+SGBD[^\n]+\n", "\n", body_text, flags=re.IGNORECASE)
    
    # 4. Formatear llamadas clave (Definición, Resumen, etc.)
    body_text = re.sub(r"\nDefinición\n", "\n\n> [!info] **Definición**\n", body_text)
    body_text = re.sub(r"\nResumiendo\n", "\n\n> [!repaso] **Resumen**\n", body_text)
    body_text = re.sub(r"\n¡Ojo!\n", "\n\n> [!warning] **¡Atención!**\n", body_text)
    body_text = re.sub(r"\nImportante\n", "\n\n> [!important] **Importante**\n", body_text)
    
    # 5. Normalizar saltos de línea rotos en medio de frases
    body_text = re.sub(r"([a-záéíóúA-ZÁÉÍÓÚ0-9,\(\)])\n([a-záéíóú])", r"\1 \2", body_text)
    
    # 6. Normalizar espacios en blanco
    body_text = re.sub(r"\n{3,}", "\n\n", body_text)
    
    # 7. Asegurar que las fórmulas LaTeX no tengan tabuladores
    body_text = body_text.replace("\text", "\\text").replace("\times", "\\times")
    
    return f"---{frontmatter}---\n{body_text.strip()}\n"

for tnum in range(1, 6):
    fname = f"tema-completo-bloque2-tema{tnum:02d}.md"
    fpath = B2_TC_DIR / fname
    if not fpath.exists():
        continue
    raw_content = fpath.read_text(encoding="utf-8")
    cleaned_content = deep_clean_body(raw_content)
    fpath.write_text(cleaned_content, encoding="utf-8")
    print(f"  [Deep Cleaned] {fname} ({len(cleaned_content.splitlines())} líneas)")

# Sincronizar con el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
