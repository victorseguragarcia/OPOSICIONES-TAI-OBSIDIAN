# -*- coding: utf-8 -*-
r"""
Script para reorganizar la carpeta wiki/synthesis/resumenes/ en subcarpetas por bloque,
añadir barra de navegación rápida (breadcrumbs) y estructura de 4 secciones en cada tema.
"""
import os
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")
RESUMENES_DIR = REPO_DIR / "wiki" / "synthesis" / "resumenes"

# Limpiar archivos planos antiguos en resumenes/ si existen
for old_file in RESUMENES_DIR.glob("resumen-bloque*.md"):
    old_file.unlink()

# Subcarpetas por bloque
BLOCK_DIRS = {
    1: RESUMENES_DIR / "bloque-1-administracion",
    2: RESUMENES_DIR / "bloque-2-hardware-so",
    3: RESUMENES_DIR / "bloque-3-desarrollo-bbdd",
    4: RESUMENES_DIR / "bloque-4-sistemas-redes"
}

for bdir in BLOCK_DIRS.values():
    bdir.mkdir(parents=True, exist_ok=True)

# 1. Indexar todos los tests temáticos reales
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

# 2. Indexar simuladores de bloque reales
TESTS_BLOQUES = {
    1: "simulacro-bloque1-50-preguntas-maestro",
    2: "simulacro-oficial-tai-100-preguntas-bloque1-4",
    3: "simulacro-oficial-tai-100-preguntas-bloque1-4",
    4: "simulacro-oficial-tai-100-preguntas-bloque1-4"
}

# 3. Indexar mazos de tarjetas reales
FLASHCARDS_BLOCKS = {
    1: "tarjetas-memoria-flashcards-bloque1-administracion",
    2: "tarjetas-memoria-flashcards-bloque2-tecnologia-hardware",
    3: "tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd",
    4: "tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad"
}

# Importar datos de temas
from generate_all_topic_and_block_summaries import TEMAS_DATA, BLOCKS_CONFIG

# Contar número total de temas por bloque
NUM_TOPICS_PER_BLOCK = {1: 10, 2: 5, 3: 9, 4: 10}

print("=" * 70)
print("📂 REORGANIZANDO RESÚMENES EN SUBCARPETAS Y AÑADIENDO BREADCRUMBS")
print("=" * 70)

# Generar cada resumen temático con barra de navegación superior e inferior
for (blk, tnum, title, desc, src_slug, body) in TEMAS_DATA:
    target_dir = BLOCK_DIRS[blk]
    fname = f"resumen-bloque{blk}-tema{tnum:02d}.md"
    fpath = target_dir / fname
    
    test_slug = TESTS_TEMAS.get((blk, tnum), f"test-bloque{blk}-tema{tnum:02d}")
    flash_slug = FLASHCARDS_BLOCKS[blk]
    max_t = NUM_TOPICS_PER_BLOCK[blk]
    
    # Construcción de la barra de navegación rápida
    nav_prev = f"[[wiki/synthesis/resumenes/bloque-{blk}-*/resumen-bloque{blk}-tema{tnum-1:02d}|⬅️ Tema {tnum-1:02d}]]" if tnum > 1 else "⬅️ Inicio Bloque"
    # Corrección de link relativo exacto
    if tnum > 1:
        prev_folder_slug = BLOCK_DIRS[blk].name
        nav_prev = f"[[wiki/synthesis/resumenes/{prev_folder_slug}/resumen-bloque{blk}-tema{tnum-1:02d}|⬅️ Tema {tnum-1:02d}]]"
    else:
        nav_prev = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Portada Bloque {blk}]]"
        
    if tnum < max_t:
        next_folder_slug = BLOCK_DIRS[blk].name
        nav_next = f"[[wiki/synthesis/resumenes/{next_folder_slug}/resumen-bloque{blk}-tema{tnum+1:02d}|Tema {tnum+1:02d} ➡️]]"
    else:
        nav_next = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏁 Fin de Bloque ➡️]]"
        
    nav_home = f"[[wiki/synthesis/resumenes/resumen-maestro-bloque{blk}|🏠 Índice Bloque {blk}]]"
    
    breadcrumb_bar = f"> {nav_prev} &nbsp;|&nbsp; {nav_home} &nbsp;|&nbsp; {nav_next}"
    
    note_content = f"""---
title: "Resumen Tema {tnum:02d} (Bloque {blk}): {title}"
type: "synthesis"
tags:
  - resumen
  - resumen-tema
  - bloque-{blk}
  - tema-{tnum:02d}
estado: "🔴 Pendiente"
dificultad: "⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/{src_slug}]]"
created: "2026-08-18"
updated: "2026-08-18"
---

{breadcrumb_bar}

# 🔴 Resumen Tema {tnum:02d} (Bloque {blk}): {title}

> [!repaso] ⚡ **Puntos Clave de Examen en 60 Segundos**
> {desc}

---

## 🟣 1. Síntesis Teórica y Conceptos Fundamentales

{body}

---

## 🔵 2. Enlaces y Recursos de Estudio del Tema
- 📖 **Tema Completo**: [[wiki/sources/{src_slug}|Fuente Oficial del Tema {tnum:02d}]]
- 📝 **Test Interactivo (10 Preguntas)**: [[wiki/tests/temas/{test_slug}|Test Tema {tnum:02d}]]
- 🃏 **Tarjetas de Memoria**: [[wiki/synthesis/{flash_slug}|Mazo Flashcards Bloque {blk}]]

---

{breadcrumb_bar}
"""
    fpath.write_text(note_content.strip() + "\n", encoding="utf-8")
    print(f"  [OK Topic Summary in Subfolder] {BLOCK_DIRS[blk].name}/{fname}")

# Generar los 4 resúmenes maestros de bloque en la raíz de resumenes/
for (bnum, btitle, bdesc, synth_ref, num_topics) in BLOCKS_CONFIG:
    bfilename = f"resumen-maestro-bloque{bnum}.md"
    bfpath = RESUMENES_DIR / bfilename
    
    sim_slug = TESTS_BLOQUES[bnum]
    flash_slug = FLASHCARDS_BLOCKS[bnum]
    folder_slug = BLOCK_DIRS[bnum].name
    
    topic_links = []
    for t in range(1, num_topics + 1):
        t_slug = TESTS_TEMAS.get((bnum, t), f"test-bloque{bnum}-tema{t:02d}")
        topic_links.append(f"- [[wiki/synthesis/resumenes/{folder_slug}/resumen-bloque{bnum}-tema{t:02d}|📄 Resumen Tema {t:02d}]] | 📝 [[wiki/tests/temas/{t_slug}|Test Tema {t:02d}]]")
    topic_list_str = "\n".join(topic_links)
    
    bcontent = f"""---
title: "Resumen Maestro Bloque {bnum}: {btitle}"
type: "synthesis"
tags:
  - resumen-bloque
  - bloque-{bnum}
  - guia-maestra
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Resumen Maestro Bloque {bnum}: {btitle}

> [!repaso] ⚡ **Visión General del Bloque {bnum}**
> {bdesc}

---

## 🟣 1. Índice de Resúmenes por Tema (Temas 01 a {num_topics:02d})

{topic_list_str}

---

## 🔵 2. Herramientas Maestras de Estudio y Repaso
- 📊 **Guía / Tabla Maestra**: [[wiki/synthesis/{synth_ref}|Guía de Referencia Rápida del Bloque {bnum}]]
- 🃏 **Tarjetas de Memoria**: [[wiki/synthesis/{flash_slug}|Mazo de Flashcards Bloque {bnum}]]
- 🎯 **Simulacro Global del Bloque**: [[wiki/tests/bloques/{sim_slug}|Examen Simulacro Completo Bloque {bnum}]]
"""
    bfpath.write_text(bcontent.strip() + "\n", encoding="utf-8")
    print(f"  [OK Master Block Summary] {bfilename}")

# Sincronizar directorio de síntesis en el baúl superior eliminando archivos antiguos
src = REPO_DIR / "wiki" / "synthesis"
dst = PARENT_DIR / "wiki" / "synthesis"
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(src, dst, dirs_exist_ok=True)
print("  [OK] Sincronizado y limpiado directorio de síntesis en el baúl superior")

print("\n[*] Reorganización completa de resúmenes finalizada con éxito.")
