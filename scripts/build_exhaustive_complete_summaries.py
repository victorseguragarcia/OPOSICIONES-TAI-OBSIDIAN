# -*- coding: utf-8 -*-
r"""
Script para generar Resúmenes Exhaustivos, Profundos y Completos (100% del temario)
para los 34 temas de la oposición TAI en wiki/synthesis/resumenes/.
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
RESUMENES_DIR = REPO_DIR / "wiki" / "synthesis" / "resumenes"

BLOCK_DIRS = {
    1: RESUMENES_DIR / "bloque-1-administracion",
    2: RESUMENES_DIR / "bloque-2-hardware-so",
    3: RESUMENES_DIR / "bloque-3-desarrollo-bbdd",
    4: RESUMENES_DIR / "bloque-4-sistemas-redes"
}

for bdir in BLOCK_DIRS.values():
    bdir.mkdir(parents=True, exist_ok=True)

# 1. Indexar tests temáticos reales
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

# 2. Indexar simuladores y tarjetas
TESTS_BLOQUES = {
    1: "simulacro-bloque1-50-preguntas-maestro",
    2: "simulacro-oficial-tai-100-preguntas-bloque1-4",
    3: "simulacro-oficial-tai-100-preguntas-bloque1-4",
    4: "simulacro-oficial-tai-100-preguntas-bloque1-4"
}

FLASHCARDS_BLOCKS = {
    1: "tarjetas-memoria-flashcards-bloque1-administracion",
    2: "tarjetas-memoria-flashcards-bloque2-tecnologia-hardware",
    3: "tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd",
    4: "tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad"
}

NUM_TOPICS_PER_BLOCK = {1: 10, 2: 5, 3: 9, 4: 10}

print("=" * 70)
print("🚀 GENERANDO RESÚMENES EXHAUSTIVOS Y COMPLETOS DE LOS 34 TEMAS")
print("=" * 70)

# Mapeo de títulos oficiales
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

# Procesar cada uno de los 34 temas
for blk in range(1, 5):
    max_t = NUM_TOPICS_PER_BLOCK[blk]
    folder_slug = BLOCK_DIRS[blk].name
    
    for tnum in range(1, max_t + 1):
        src_slug = f"bloque{blk}-tema{tnum:02d}"
        src_path = REPO_DIR / "wiki" / "sources" / f"{src_slug}.md"
        raw_path = REPO_DIR / "raw" / "sources" / f"{src_slug}.md"
        
        # Leer contenido de la fuente para extraer todo el cuerpo estructurado
        raw_body = ""
        if src_path.exists():
            full_src = src_path.read_text(encoding="utf-8")
            # Extraer desde "## 📖 Resumen Ejecutivo" o después del frontmatter
            if "## 📖 Resumen Ejecutivo" in full_src:
                raw_body = full_src.split("## 📖 Resumen Ejecutivo", 1)[1]
            elif "## 🧩 Estructura y Desglose Temático" in full_src:
                raw_body = full_src.split("## 🧩 Estructura y Desglose Temático", 1)[1]
            else:
                # Quitar frontmatter
                parts = full_src.split("---", 2)
                raw_body = parts[2] if len(parts) > 2 else full_src
                
            # Quitar la sección de Entidades y Conceptos Asociados del final para integrarla limpiamente
            if "## 🔵 4. Entidades" in raw_body:
                raw_body = raw_body.split("## 🔵 4. Entidades")[0]
            elif "## 🔵 3. Entidades" in raw_body:
                raw_body = raw_body.split("## 🔵 3. Entidades")[0]
        elif raw_path.exists():
            raw_body = raw_path.read_text(encoding="utf-8")
            
        raw_body = raw_body.strip()
        
        # Corregir escapes de LaTeX
        raw_body = raw_body.replace("$\n\tightarrow$", " $\\rightarrow$ ").replace("$\n ightarrow$", " $\\rightarrow$ ")
        raw_body = raw_body.replace("\r\n", "\n")
        
        # Breadcrumbs
        if tnum > 1:
            nav_prev = f"[[wiki/synthesis/resumenes/{folder_slug}/resumen-bloque{blk}-tema{tnum-1:02d}|⬅️ Tema {tnum-1:02d}]]"
        else:
            nav_prev = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Portada Bloque {blk}]]"
            
        if tnum < max_t:
            nav_next = f"[[wiki/synthesis/resumenes/{folder_slug}/resumen-bloque{blk}-tema{tnum+1:02d}|Tema {tnum+1:02d} ➡️]]"
        else:
            nav_next = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏁 Fin de Bloque ➡️]]"
            
        nav_home = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Índice Bloque {blk}]]"
        breadcrumb_bar = f"> {nav_prev} &nbsp;|&nbsp; {nav_home} &nbsp;|&nbsp; {nav_next}"
        
        title = TOPIC_TITLES.get((blk, tnum), f"Tema {tnum:02d}")
        test_slug = TESTS_TEMAS.get((blk, tnum), f"test-bloque{blk}-tema{tnum:02d}")
        flash_slug = FLASHCARDS_BLOCKS[blk]
        
        summary_content = f"""---
title: "Resumen Completo Tema {tnum:02d} (Bloque {blk}): {title}"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-{blk}
  - tema-{tnum:02d}
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/{src_slug}]]"
created: "2026-08-18"
updated: "2026-08-18"
---

{breadcrumb_bar}

# 🔴 Resumen Completo Tema {tnum:02d} (Bloque {blk}): {title}

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema {tnum:02d}**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

{raw_body}

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/{src_slug}|Nota Fuente del Tema {tnum:02d}]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/{test_slug}|Test Tema {tnum:02d}]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/{flash_slug}|Mazo Flashcards Bloque {blk}]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|Resumen Maestro Bloque {blk}]]

---

{breadcrumb_bar}
"""
        target_file = BLOCK_DIRS[blk] / f"resumen-bloque{blk}-tema{tnum:02d}.md"
        target_file.write_text(summary_content.strip() + "\n", encoding="utf-8")
        print(f"  [OK Exhaustive Summary] {folder_slug}/resumen-bloque{blk}-tema{tnum:02d}.md ({len(summary_content.splitlines())} líneas)")

# Sincronizar directorio de síntesis en el baúl superior
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("\n[*] Sincronización completa con el baúl superior finalizada.")
