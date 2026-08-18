# -*- coding: utf-8 -*-
r"""
Script para crear la sección maestra 'wiki/synthesis/temas-completos/'
con el desarrollo enciclopédico y extendido al 100% de cada uno de los 34 temas
de la oposición TAI a partir de todas las fuentes oficiales completas.
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
RAW_DIR = REPO_DIR / "raw" / "sources"
WIKI_SRC_DIR = REPO_DIR / "wiki" / "sources"
TC_DIR = REPO_DIR / "wiki" / "synthesis" / "temas-completos"

BLOCK_DIRS = {
    1: TC_DIR / "bloque-1-administracion",
    2: TC_DIR / "bloque-2-hardware-so",
    3: TC_DIR / "bloque-3-desarrollo-bbdd",
    4: TC_DIR / "bloque-4-sistemas-redes"
}

for bdir in BLOCK_DIRS.values():
    bdir.mkdir(parents=True, exist_ok=True)

# 1. Indexar tests temáticos reales existentes
TESTS_TEMAS = {}
for tf in (REPO_DIR / "wiki" / "tests" / "temas").glob("*.md"):
    name = tf.stem
    parts = name.split("-")
    if len(parts) >= 3 and parts[0] == "test" and parts[1].startswith("bloque") and parts[2].startswith("tema"):
        try:
            blk_num = int(parts[1].replace("bloque", ""))
            t_num = int(parts[2].replace("tema", ""))
            TESTS_TEMAS[(blk_num, t_num)] = name
        except ValueError:
            pass

FLASHCARDS_BLOCKS = {
    1: "tarjetas-memoria-flashcards-bloque1-administracion",
    2: "tarjetas-memoria-flashcards-bloque2-tecnologia-hardware",
    3: "tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd",
    4: "tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad"
}

NUM_TOPICS_PER_BLOCK = {1: 10, 2: 5, 3: 9, 4: 10}

RAW_FILES_MAP = {
    (1, 1): "bloque1-tema01.md",
    (1, 2): "bloque1-tema02.md",
    (1, 3): "bloque1-tema03.md",
    (1, 4): "bloque1-tema04.md",
    (1, 5): "bloque1-tema05.md",
    (1, 6): "bloque1-tema06.md",
    (1, 7): "bloque1-tema07.md",
    (1, 8): "bloque1-tema08.md",
    (1, 9): "bloque1-tema09.md",
    (1, 10): "bloque1-tema10.md",

    (2, 1): "bloque2-tema01-informatica-basica-representacion.md",
    (2, 2): "bloque2-tema02-perifericos-conectividad-interfaces.md",
    (2, 3): "bloque2-tema03-estructuras-ficheros-algoritmos.md",
    (2, 4): "bloque2-tema04-sistemas-operativos-procesos-memoria.md",
    (2, 5): "bloque2-tema05-sgbd-relacionales-nosql-cap.md",

    (3, 1): "bloque3-tema01-modelado-datos-bbdd.md",
    (3, 2): "bloque3-tema02-lenguajes-programacion.md",
    (3, 3): "bloque3-tema03-sql-interrogacion-bbdd.md",
    (3, 4): "bloque3-tema04-poo-patrones-uml.md",
    (3, 5): "bloque3-tema05-componentes-javaee-dotnet.md",
    (3, 6): "bloque3-tema06-arquitecturas-servicios-web.md",
    (3, 7): "bloque3-tema07-desarrollo-web-frontend.md",
    (3, 8): "bloque3-tema08-accesibilidad-usabilidad-seguridad.md",
    (3, 9): "bloque3-tema09-metodologias-pruebas-git.md",

    (4, 1): "bloque4-tema01.md",
    (4, 2): "bloque4-tema02.md",
    (4, 3): "bloque4-tema03.md",
    (4, 4): "bloque4-tema04.md",
    (4, 5): "bloque4-tema05.md",
    (4, 6): "bloque4-tema06.md",
    (4, 7): "bloque4-tema07.md",
    (4, 8): "bloque4-tema08.md",
    (4, 9): "bloque4-tema09.md",
    (4, 10): "bloque4-tema10.md"
}

TOPIC_TITLES = {
    (1, 1): "La Constitución Española de 1978 y Derechos Fundamentales",
    (1, 2): "La Corona, las Cortes Generales y el Gobierno (AGE)",
    (1, 3): "Organización Territorial del Estado y Comunidades Autónomas",
    (1, 4): "La Unión Europea, sus Instituciones y el Derecho Comunitario",
    (1, 5): "El Régimen Jurídico del Empleado Público y el TREBEP",
    (1, 6): "Políticas de Igualdad de Género y Contra la Violencia de Género",
    (1, 7): "El Procedimiento Administrativo Común (Ley 39/2015 - LPACAP)",
    (1, 8): "Régimen Jurídico del Sector Público y Administración Digital (Ley 40/2015)",
    (1, 9): "Protección de Datos Personales (RGPD y LOPDGDD 3/2018)",
    (1, 10): "Transparencia, Acceso a la Información y Buen Gobierno (Ley 19/2013)",

    (2, 1): "Estructura y Componentes de un Sistema Informático (C2, IEEE 754, Buses)",
    (2, 2): "Arquitectura de Computadores, Procesadores y Memoria (Von Neumann, RISC)",
    (2, 3): "Estructuras de Datos, Árboles y Algoritmos (AVL, B+, Big-O)",
    (2, 4): "Sistemas Operativos: Gestión de Procesos, Memoria y Ficheros",
    (2, 5): "Bases de Datos Relacionales y NoSQL (Teorema CAP, Familias NoSQL)",

    (3, 1): "Diseño y Normalización de Bases de Datos (1FN a 5FN, BCNF)",
    (3, 2): "Lenguajes de Programación y Paradigmas (POO, SOLID, Patrones GoF)",
    (3, 3): "Lenguaje SQL ANSI, Subconsultas y Transacciones ACID",
    (3, 4): "Arquitectura de Software y Plataformas Empresariales (Java EE, .NET)",
    (3, 5): "Desarrollo Web Frontend (HTML5, CSS3, JavaScript ES6+)",
    (3, 6): "Servicios Web y Arquitecturas Orientadas a Servicios (SOAP vs REST)",
    (3, 7): "Accesibilidad Web (WCAG 2.1 POUR y RD 1112/2018 Nivel AA)",
    (3, 8): "Control de Versiones con Git y Metodologías Ágiles (Scrum, Kanban)",
    (3, 9): "Metodología MÉTRICA Versión 3, Complejidad de McCabe y QA",

    (4, 1): "Administración de Sistemas Operativos Servidor (Linux SysAdmin, Windows Server)",
    (4, 2): "Servicios de Directorio, Active Directory DS y Kerberos v5",
    (4, 3): "Virtualización, Contenedores (Docker, Kubernetes) y Cloud Computing",
    (4, 4): "Centros de Proceso de Datos (TIER I-IV), Almacenamiento y RAID",
    (4, 5): "Copias de Seguridad, Regla 3-2-1, RPO/RTO y Continuidad de Negocio",
    (4, 6): "Medios de Transmisión, Fibra Óptica, LAN Ethernet, Wi-Fi 6 y VLANs",
    (4, 7): "Protocolo IP, Subnetting IPv4/IPv6, ICMP, DHCP y DNS",
    (4, 8): "Protocolos de Transporte (TCP vs UDP) y Tabla Maestra de Puertos",
    (4, 9): "Seguridad de la Información, Criptografía y ENS (RD 311/2022)",
    (4, 10): "Seguridad Perimetral, Firewall IPTables, IDS/IPS y VPN"
}

def clean_pdf_text(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) > 2:
            text = parts[2]
            
    text = re.sub(r"### Página \d+", "", text)
    text = re.sub(r"DV\.TextoHTML\([^\)]+\)\.Esp\.dot\s+\|\s+UD\d+_[^\n]+", "", text)
    text = re.sub(r"administracion\.gob\.es\s+\|\s+UD\d+_[^\n]+", "", text)
    text = re.sub(r"davante\.es\s+\|\s+UD\d+_[^\n]+", "", text)
    text = re.sub(r"> \*\*Fuente Original\*\*:[^\n]+", "", text)
    text = re.sub(r"> \*\*Tipo\*\*:[^\n]+", "", text)
    text = re.sub(r"> \*\*Fecha de Ingesta\*\*:[^\n]+", "", text)
    text = re.sub(r"## Contenido Extraído", "", text)
    text = re.sub(r"# Bloque \d+ - Tema \d+:[^\n]+", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text.replace("$\n\tightarrow$", " $\\rightarrow$ ").replace("$\n ightarrow$", " $\\rightarrow$ ")
    text = text.replace("\r\n", "\n")
    return text.strip()

print("=" * 70)
print("📚 CONSTRUYENDO EL APARTADO DE 'TEMAS COMPLETOS' (EXTENDIDO ÍNTEGRO)")
print("=" * 70)

for blk in range(1, 5):
    max_t = NUM_TOPICS_PER_BLOCK[blk]
    folder_slug = BLOCK_DIRS[blk].name
    
    for tnum in range(1, max_t + 1):
        raw_name = RAW_FILES_MAP.get((blk, tnum))
        raw_path = RAW_DIR / raw_name if raw_name else None
        
        wiki_src_slug = f"bloque{blk}-tema{tnum:02d}"
        wiki_src_path = WIKI_SRC_DIR / f"{wiki_src_slug}.md"
        
        # Obtener contenido íntegro y extendido
        extended_body = ""
        if raw_path and raw_path.exists():
            raw_txt = raw_path.read_text(encoding="utf-8")
            extended_body = clean_pdf_text(raw_txt)
        elif wiki_src_path.exists():
            w_txt = wiki_src_path.read_text(encoding="utf-8")
            extended_body = clean_pdf_text(w_txt)
            
        # Breadcrumbs
        if tnum > 1:
            nav_prev = f"[[wiki/synthesis/temas-completos/{folder_slug}/tema-completo-bloque{blk}-tema{tnum-1:02d}|⬅️ Tema Completo {tnum-1:02d}]]"
        else:
            nav_prev = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Portada Bloque {blk}]]"
            
        if tnum < max_t:
            nav_next = f"[[wiki/synthesis/temas-completos/{folder_slug}/tema-completo-bloque{blk}-tema{tnum+1:02d}|Tema Completo {tnum+1:02d} ➡️]]"
        else:
            nav_next = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏁 Fin Bloque {blk} ➡️]]"
            
        nav_home = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Índice Bloque {blk}]]"
        breadcrumb_bar = f"> {nav_prev}  ·  {nav_home}  ·  {nav_next}"
        
        title = TOPIC_TITLES.get((blk, tnum), f"Tema {tnum:02d}")
        test_slug = TESTS_TEMAS.get((blk, tnum), f"test-bloque{blk}-tema{tnum:02d}")
        flash_slug = FLASHCARDS_BLOCKS[blk]
        
        full_topic_md = f"""---
title: "Tema Completo Extendido {tnum:02d} (Bloque {blk}): {title}"
type: "synthesis"
tags:
  - tema-completo
  - temario-extendido
  - bloque-{blk}
  - tema-{tnum:02d}
  - oposiciones-tai
estado: "🔴 Por Estudiar"
dificultad: "⭐⭐⭐"
prioridad: "Máxima"
sources:
  - "[[raw/sources/{raw_name}]]"
  - "[[wiki/sources/{wiki_src_slug}]]"
created: "2026-08-18"
updated: "2026-08-18"
---

{breadcrumb_bar}

# 🔴 Tema Completo Extendido {tnum:02d} (Bloque {blk}): {title}

> [!repaso] ⚡ **Temario Oficial Completo y Extendido**
> Esta nota contiene el desarrollo enciclopédico íntegro, exhaustivo y detallado del Tema {tnum:02d} correspondiente al Bloque {blk} de las Oposiciones TAI / AGE. Incluye todos los artículos normativos, fundamentos teóricos, arquitecturas, tablas de especificaciones, diagramas y casos de examen oficiales.

---

## 🟣 1. Desarrollo Teórico, Jurídico y Técnico Íntegro

{extended_body}

---

## 🔵 2. Enlaces Rápidos de Estudio y Autoevaluación
- 📑 **Resumen de Repaso Rápido**: [[wiki/synthesis/resumenes/bloque-{blk}-*/resumen-bloque{blk}-tema{tnum:02d}|Ficha Resumen del Tema {tnum:02d}]]
- 📖 **Fuente Raw Original**: [[wiki/sources/{wiki_src_slug}|Nota Fuente Oficial del Tema {tnum:02d}]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/{test_slug}|Test Tema {tnum:02d}]]
- 🃏 **Mazo de Tarjetas de Memoria**: [[wiki/synthesis/{flash_slug}|Flashcards Bloque {blk}]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|Resumen Maestro Bloque {blk}]]

---

{breadcrumb_bar}
"""
        # Ajuste de link exacto a la ficha resumen
        resumen_folder_slug = ""
        if blk == 1: resumen_folder_slug = "bloque-1-administracion"
        elif blk == 2: resumen_folder_slug = "bloque-2-hardware-so"
        elif blk == 3: resumen_folder_slug = "bloque-3-desarrollo-bbdd"
        elif blk == 4: resumen_folder_slug = "bloque-4-sistemas-redes"
        full_topic_md = full_topic_md.replace(f"bloque-{blk}-*", resumen_folder_slug)
        
        target_file = BLOCK_DIRS[blk] / f"tema-completo-bloque{blk}-tema{tnum:02d}.md"
        target_file.write_text(full_topic_md.strip() + "\n", encoding="utf-8")
        line_count = len(full_topic_md.splitlines())
        print(f"  [OK Tema Completo Extendido] {folder_slug}/tema-completo-bloque{blk}-tema{tnum:02d}.md ({line_count} líneas, {len(full_topic_md)} bytes)")

# Sincronizar directorio de síntesis en el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
