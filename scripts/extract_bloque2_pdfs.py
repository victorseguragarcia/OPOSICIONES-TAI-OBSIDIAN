# -*- coding: utf-8 -*-
"""
Extractor de texto de los 5 PDFs de raw/bloque 2 a raw/sources/ con metadatos estructurados.
"""
import os
import sys
import fitz  # PyMuPDF

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B2_DIR = os.path.join(BASE_DIR, "raw", "bloque 2")
RAW_SOURCES_DIR = os.path.join(BASE_DIR, "raw", "sources")

PDF_MAPPING_B2 = [
    {
        "filename": "624446.pdf",
        "slug": "bloque2-tema01-informatica-basica-representacion",
        "title": "Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores",
        "topic": "informatica-basica-representacion"
    },
    {
        "filename": "624459 (1).pdf",
        "slug": "bloque2-tema02-perifericos-conectividad-interfaces",
        "title": "Bloque 2 - Tema 02 (UD012103): Periféricos, Conectividad, Puertos Físicos y Buses de Expansión",
        "topic": "perifericos-conectividad-interfaces"
    },
    {
        "filename": "635935 (2).pdf",
        "slug": "bloque2-tema03-estructuras-ficheros-algoritmos",
        "title": "Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Complejidad Algorítmica",
        "topic": "estructuras-ficheros-algoritmos"
    },
    {
        "filename": "625749.pdf",
        "slug": "bloque2-tema04-sistemas-operativos-procesos-memoria",
        "title": "Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Arquitectura, Gestión de Procesos, Memoria y Sistemas de Archivos",
        "topic": "sistemas-operativos-procesos-memoria"
    },
    {
        "filename": "624479 (1).pdf",
        "slug": "bloque2-tema05-sgbd-relacionales-nosql-cap",
        "title": "Bloque 2 - Tema 05 (UD012106): Sistemas Gestores de Bases de Datos Relacionales, Objeto-Relacionales, NoSQL y Teorema CAP",
        "topic": "sgbd-relacionales-nosql-cap"
    }
]

print(f"[*] Extrayendo {len(PDF_MAPPING_B2)} PDFs de raw/bloque 2/...")

for item in PDF_MAPPING_B2:
    pdf_path = os.path.join(B2_DIR, item["filename"])
    out_md_path = os.path.join(RAW_SOURCES_DIR, f"{item['slug']}.md")
    
    if not os.path.exists(pdf_path):
        print(f"    [!] Error: No se encuentra {pdf_path}")
        continue
        
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    text_content = []
    
    for page_num in range(total_pages):
        page = doc[page_num]
        text_content.append(f"\n\n<!-- Page {page_num + 1} -->\n\n" + page.get_text())
        
    full_text = "".join(text_content)
    
    frontmatter = f"""---
title: "{item['title']}"
type: "raw-source"
topic: "{item['topic']}"
source_pdf: "raw/bloque 2/{item['filename']}"
pages: {total_pages}
date: "2026-08-17"
---

# {item['title']}

{full_text}
"""
    with open(out_md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(frontmatter)
        
    print(f"    [OK] Extraído: {item['slug']}.md ({total_pages} páginas, {len(full_text)} caracteres)")

print("[*] Extracción de PDFs de Bloque 2 completada con éxito.")
