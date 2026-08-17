#!/usr/bin/env python3
"""
PDF Text Extractor for Raw Sources
Extracts text from PDF documents using PyMuPDF (fitz) and saves them as
individual Markdown files in raw/sources/ with standard LLM Wiki YAML frontmatter.
"""

import os
import sys
import re
import datetime
from pathlib import Path

# Force UTF-8 on Windows stdout
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    import fitz  # PyMuPDF
except ImportError:
    print("[X] PyMuPDF (fitz) is not installed. Trying pypdf...")
    try:
        import pypdf
    except ImportError:
        print("[X] Neither PyMuPDF nor pypdf is available. Please install PyMuPDF.")
        sys.exit(1)

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / "raw"
OUTPUT_DIR = RAW_DIR / "sources"

# Pre-defined known official syllabus topics for TAI Bloque 4 for high-quality titles
TAI_BLOQUE_4_TITLES = {
    "1": "Administración del Sistema Operativo y Software de Base",
    "2": "Administración de Bases de Datos, Virtualización y Cloud",
    "3": "Administración de Servidores de Correo, Contenedores y Middleware",
    "4": "Administración de Redes de Área Local",
    "5": "Seguridad de Sistemas, Infraestructura CPD, Gestión de Incidentes",
    "6": "Comunicaciones: Modos, Medios, Equipos, Redes Móviles e Inalámbricas",
    "7": "Modelo ISO-OSI, Modelo TCP-IP, Protocolo IP (IPv4 e IPv6)",
    "8": "Internet: Arquitectura, Servicios, Protocolos HTTP, HTTPS, TLS y OSPF",
    "9": "Seguridad en Redes, CCN, Seguridad Perimetral, VPN, Accesos",
    "10": "Redes Locales: Tipología, Técnicas de Transmisión, Métodos de Acceso",
}

def clean_text(text):
    # Normalize multiple newlines and spaces
    text = re.sub(r'\r\n', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def extract_pdf_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages_text = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text("text")
        if text.strip():
            pages_text.append(f"### Página {page_num + 1}\n\n{clean_text(text)}")
    doc.close()
    return "\n\n---\n\n".join(pages_text)

def get_topic_number(filename):
    match = re.search(r'tema\s*(\d+)', filename.lower())
    if match:
        return match.group(1)
    return None

def process_all_pdfs():
    print("=" * 60)
    print("[*] STARTING PDF EXTRACTION FOR RAW SOURCES")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Locate all PDFs in raw/
    pdf_files = list(RAW_DIR.rglob("*.pdf"))
    if not pdf_files:
        # Also check raw/files if specified
        files_dir = RAW_DIR / "files"
        if files_dir.exists():
            pdf_files = list(files_dir.rglob("*.pdf"))
            
    if not pdf_files:
        print("[!] No PDF files found in raw/ or subdirectories.")
        return

    print(f"[*] Found {len(pdf_files)} PDF file(s) to process.\n")
    
    today_str = datetime.date.today().strftime("%Y-%m-%d")
    processed_count = 0

    for pdf_path in sorted(pdf_files):
        filename = pdf_path.name
        rel_pdf_path = pdf_path.relative_to(ROOT_DIR).as_posix()
        topic_num = get_topic_number(filename)
        
        # Build Title and Filename Slug
        if topic_num:
            topic_pad = f"{int(topic_num):02d}"
            topic_title = TAI_BLOQUE_4_TITLES.get(topic_num, f"Tema {topic_pad}")
            doc_title = f"Bloque 4 - Tema {topic_pad}: {topic_title}"
            slug = f"bloque4-tema{topic_pad}.md"
            alias_title = f"Bloque 4 Tema {topic_pad}"
            tags = [
                "oposiciones",
                "tai",
                "bloque-4",
                f"tema-{topic_pad}",
                "raw-source-extracted"
            ]
        else:
            clean_stem = re.sub(r'[^a-zA-Z0-9_-]', '-', pdf_path.stem).strip('-').lower()
            doc_title = pdf_path.stem.replace('_', ' ').replace('-', ' ').title()
            slug = f"{clean_stem}.md"
            alias_title = doc_title
            tags = ["oposiciones", "tai", "raw-source-extracted"]

        print(f"[*] Processing: {filename} -> {slug} ...")

        # Extract text content
        extracted_content = extract_pdf_pymupdf(pdf_path)

        # Build YAML Frontmatter
        frontmatter = f"""---
title: "{doc_title}"
type: "source"
tags:
"""
        for tag in tags:
            frontmatter += f"  - {tag}\n"
        
        frontmatter += f"""sources:
  - "{rel_pdf_path}"
created: "{today_str}"
updated: "{today_str}"
aliases:
  - "{alias_title}"
  - "{filename}"
---

# {doc_title}

> **Fuente Original**: `{rel_pdf_path}`  
> **Tipo**: Extracción completa de documento PDF  
> **Fecha de Ingesta**: {today_str}

---

## Contenido Extraído

{extracted_content}
"""

        output_file = OUTPUT_DIR / slug
        output_file.write_text(frontmatter, encoding="utf-8")
        processed_count += 1
        print(f"    [OK] Saved {len(extracted_content)} chars to {output_file.relative_to(ROOT_DIR)}")

    print("\n" + "=" * 60)
    print(f"[OK] COMPLETED: Successfully extracted {processed_count} PDF(s) to raw/sources/")
    print("=" * 60)

if __name__ == "__main__":
    process_all_pdfs()
