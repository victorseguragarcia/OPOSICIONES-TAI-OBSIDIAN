# -*- coding: utf-8 -*-
"""
Extractor de texto de los 9 PDFs de raw/bloque 3 a raw/sources/ con metadatos estructurados.
"""
import os
import sys
import fitz  # PyMuPDF

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
B3_DIR = os.path.join(BASE_DIR, "raw", "bloque 3")
RAW_SOURCES_DIR = os.path.join(BASE_DIR, "raw", "sources")

PDF_MAPPING = [
    {
        "filename": "626687 (2).pdf",
        "slug": "bloque3-tema01-modelado-datos-bbdd",
        "title": "Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo Entidad-Relación, Diseño Lógico/Físico y Normalización",
        "topic": "modelado-datos-bbdd"
    },
    {
        "filename": "625778 (1).pdf",
        "slug": "bloque3-tema02-lenguajes-programacion",
        "title": "Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas, Compiladores e Intérpretes",
        "topic": "lenguajes-programacion"
    },
    {
        "filename": "627358 (2).pdf",
        "slug": "bloque3-tema03-sql-interrogacion-bbdd",
        "title": "Bloque 3 - Tema 03 (UD012110): Lenguajes de Interrogación de BBDD, Estándar ANSI SQL, Procedimientos Almacenados y Triggers",
        "topic": "sql-interrogacion-bbdd"
    },
    {
        "filename": "625751 (1).pdf",
        "slug": "bloque3-tema04-poo-patrones-uml",
        "title": "Bloque 3 - Tema 04 (UD012111): Diseño y Programación Orientada a Objetos, Patrones de Diseño GoF y UML",
        "topic": "poo-patrones-uml"
    },
    {
        "filename": "627470 (1).pdf",
        "slug": "bloque3-tema05-componentes-javaee-dotnet",
        "title": "Bloque 3 - Tema 05 (UD012112): Desarrollo Basado en Componentes, Java EE / Jakarta EE y Plataforma .NET",
        "topic": "componentes-javaee-dotnet"
    },
    {
        "filename": "625753 (1).pdf",
        "slug": "bloque3-tema06-arquitecturas-servicios-web",
        "title": "Bloque 3 - Tema 06 (UD012113): Arquitecturas de Sistemas, Cliente/Servidor, Multicapa, Servicios Web SOAP y REST",
        "topic": "arquitecturas-servicios-web"
    },
    {
        "filename": "625755 (1).pdf",
        "slug": "bloque3-tema07-desarrollo-web-frontend",
        "title": "Bloque 3 - Tema 07 (UD012114): Aplicaciones y Desarrollo Web: HTML5, DOM, CSS, JavaScript, Servlets y JSP",
        "topic": "desarrollo-web-frontend"
    },
    {
        "filename": "625757.pdf",
        "slug": "bloque3-tema08-accesibilidad-usabilidad-seguridad",
        "title": "Bloque 3 - Tema 08 (UD012115): Accesibilidad, Diseño Universal, Usabilidad, Confidencialidad y Seguridad en Puesto de Usuario",
        "topic": "accesibilidad-usabilidad-seguridad"
    },
    {
        "filename": "625759 (1).pdf",
        "slug": "bloque3-tema09-metodologias-pruebas-git",
        "title": "Bloque 3 - Tema 09 (UD012116): Repositorios, Metodologías de Desarrollo, Pruebas de Software y Control de Versiones con Git",
        "topic": "metodologias-pruebas-git"
    }
]

print(f"[*] Extrayendo {len(PDF_MAPPING)} PDFs de raw/bloque 3/...")

for item in PDF_MAPPING:
    pdf_path = os.path.join(B3_DIR, item["filename"])
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
source_pdf: "raw/bloque 3/{item['filename']}"
pages: {total_pages}
date: "2026-08-17"
---

# {item['title']}

{full_text}
"""
    with open(out_md_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(frontmatter)
        
    print(f"    [OK] Extraído: {item['slug']}.md ({total_pages} páginas, {len(full_text)} caracteres)")

print("[*] Extracción de PDFs de Bloque 3 completada con éxito.")
