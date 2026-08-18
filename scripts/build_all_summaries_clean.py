# -*- coding: utf-8 -*-
r"""
Script limpio y definitivo para generar los 34 resúmenes temáticos y los 4 resúmenes de bloque
con resolución estricta de enlaces existentes en el sistema de archivos.
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
RESUMENES_DIR.mkdir(parents=True, exist_ok=True)

# 1. Indexar todos los tests temáticos reales existentes
TESTS_TEMAS = {}
for tf in (REPO_DIR / "wiki" / "tests" / "temas").glob("*.md"):
    name = tf.stem
    # ej: test-bloque1-tema01-constitucion
    parts = name.split("-")
    if len(parts) >= 3 and parts[0] == "test" and parts[1].startswith("bloque") and parts[2].startswith("tema"):
        blk_num = int(parts[1].replace("bloque", ""))
        t_num = int(parts[2].replace("tema", ""))
        TESTS_TEMAS[(blk_num, t_num)] = name

# 2. Indexar simuladores de bloque reales existentes
TESTS_BLOQUES = {
    1: "simulador-bloque1-administracion-age",
    2: "simulador-bloque2-tecnologia-hardware",
    3: "simulador-bloque3-desarrollo-metrica",
    4: "simulador-bloque4-sistemas-redes-seguridad"
}

# 3. Indexar mazos de tarjetas reales existentes
FLASHCARDS_BLOCKS = {
    1: "tarjetas-memoria-flashcards-bloque1-administracion",
    2: "tarjetas-memoria-flashcards-bloque2-tecnologia-hardware",
    3: "tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd",
    4: "tarjetas-memoria-flashcards-bloque4-sistemas-redes-seguridad"
}

# 4. Importar datos de temas
from generate_all_topic_and_block_summaries import TEMAS_DATA, BLOCKS_MASTER

# Generar los 34 resúmenes temáticos
for (tid, blk, tnum, title, desc, tag, src_slug, _, body) in TEMAS_DATA:
    fname = f"resumen-bloque{blk}-tema{tnum:02d}.md"
    fpath = RESUMENES_DIR / fname
    
    test_slug = TESTS_TEMAS.get((blk, tnum), f"test-bloque{blk}-tema{tnum:02d}")
    flash_slug = FLASHCARDS_BLOCKS[blk]
    
    note_content = f"""---
title: "Resumen Tema {tnum:02d} (Bloque {blk}): {title}"
type: "synthesis"
tags:
  - resumen
  - resumen-tema
  - bloque-{blk}
  - tema-{tnum:02d}
sources:
  - "[[wiki/sources/{src_slug}]]"
created: "2026-08-18"
updated: "2026-08-18"
---

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
"""
    fpath.write_text(note_content.strip() + "\n", encoding="utf-8")

# Generar los 4 resúmenes maestros de bloque
for (bnum, btitle, bdesc, synth_ref, flash_ref, _, num_topics) in BLOCKS_MASTER:
    bfilename = f"resumen-maestro-bloque{bnum}.md"
    bfpath = RESUMENES_DIR / bfilename
    
    sim_slug = TESTS_BLOQUES[bnum]
    
    topic_links = []
    for t in range(1, num_topics + 1):
        t_slug = TESTS_TEMAS.get((bnum, t), f"test-bloque{bnum}-tema{t:02d}")
        topic_links.append(f"- [[wiki/synthesis/resumenes/resumen-bloque{bnum}-tema{t:02d}|📄 Resumen Tema {t:02d}]] | 📝 [[wiki/tests/temas/{t_slug}|Test Tema {t:02d}]]")
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
- 🃏 **Tarjetas de Memoria**: [[wiki/synthesis/{flash_ref}|Mazo de Flashcards Bloque {bnum}]]
- 🎯 **Simulacro Global del Bloque**: [[wiki/tests/bloques/{sim_slug}|Examen Simulacro Completo Bloque {bnum}]]
"""
    bfpath.write_text(bcontent.strip() + "\n", encoding="utf-8")

# Sincronizar directorio de síntesis en el baúl superior
for d in ["wiki/synthesis"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado directorio en baúl superior: {d}")

print("\n[*] Todos los resúmenes generados y sincronizados.")
