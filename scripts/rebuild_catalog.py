# -*- coding: utf-8 -*-
"""
Script para reconstruir dinámicamente index.md y log.md aplicando la jerarquía
de colores de estudio, enlaces a Canvas y catálogo de tests y autoevaluaciones.
"""
import os
import re
import sys
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parse_frontmatter(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("-"):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm

def rebuild():
    wiki_dir = os.path.join(BASE_DIR, "wiki")
    
    sources_b1 = []
    sources_b2 = []
    sources_b3 = []
    sources_b4 = []
    sources_other = []
    
    entities = []
    concepts = []
    syntheses = []
    
    tests_bloques = []
    tests_temas = []

    for root, _, files in os.walk(wiki_dir):
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, BASE_DIR).replace("\\", "/")
            fm = parse_frontmatter(full)
            title = fm.get("title", f)
            ntype = fm.get("type", "unknown")
            slug = rel.replace(".md", "")
            
            item = f"- [[{slug}|{title}]]"
            
            if ntype == "source":
                if "bloque1" in f:
                    sources_b1.append(item)
                elif "bloque2" in f:
                    sources_b2.append(item)
                elif "bloque3" in f:
                    sources_b3.append(item)
                elif "bloque4" in f:
                    sources_b4.append(item)
                else:
                    sources_other.append(item)
            elif ntype == "entity":
                entities.append(item)
            elif ntype == "concept":
                concepts.append(item)
            elif ntype == "synthesis":
                syntheses.append(item)
            elif ntype == "test":
                if "bloques" in rel:
                    tests_bloques.append(item)
                else:
                    tests_temas.append(item)

    all_sources_count = len(sources_b1) + len(sources_b2) + len(sources_b3) + len(sources_b4) + len(sources_other)
    all_tests_count = len(tests_bloques) + len(tests_temas)

    tests_section = ""
    if all_tests_count > 0:
        tests_section = f"""---

## 📝 4. Banco de Tests y Autoevaluaciones ({all_tests_count} Baterías)

### 📝 Tests y Simulacros por Bloques ({len(tests_bloques)} Recursos)
{chr(10).join(tests_bloques) if tests_bloques else "- *No hay tests por bloques registrados aún.*"}

### 📝 Tests por Temas Individuales ({len(tests_temas)} Recursos)
{chr(10).join(tests_temas) if tests_temas else "- *No hay tests por temas registrados aún.*"}
"""

    index_content = f"""# 🏛️ Catálogo Maestro del Temario Oficial TAI (AGE)

> [!important]
> **Esquema de Estudio Visual y Jerarquía de Colores**
> - 🔴 **Temas Principales (Nivel 1 / H1 / Bloques)**: Coral Pastel (`#EF5350`)
> - 🟣 **Subtemas (Nivel 2 / H2 / Entidades & Conceptos)**: Orquídea Pastel (`#BA68C8`)
> - 🔵 **Conocimientos Concretos (Nivel 3+ / H3 / Síntesis & Tablas)**: Azul Cielo (`#64B5F6`)
> - ⚠️ **Trampas de Examen**: Ámbar (`#FFB74D`) | 🧠 **Mnemotecnias**: Menta (`#81C784`)
>
> 🗺️ **Lienzos Gráficos Interactivos (Obsidian Canvas)**:
> - 🌐 [[temario-tai-visual-map.canvas|Mapa Global del Temario TAI]]
> - 🏛️ [[temario-bloque1-administracion.canvas|Lienzo Bloque 1: Administración y Marco Digital]]
> - 💻 [[temario-bloque2-tecnologia.canvas|Lienzo Bloque 2: Tecnología Básica y Hardware]]
> - ⚙️ [[temario-bloque3-desarrollo.canvas|Lienzo Bloque 3: Desarrollo de Sistemas]]
> - 🌐 [[temario-bloque4-sistemas.canvas|Lienzo Bloque 4: Sistemas y Comunicaciones]]

---

# 🔴 1. Temas Principales del Temario Oficial ({all_sources_count} Fuentes)

## 🔴 Bloque 1: Administración Pública y Normativa (10 Temas)
{chr(10).join(sources_b1)}

## 🔴 Bloque 2: Tecnología Básica (5 Temas)
{chr(10).join(sources_b2)}

## 🔴 Bloque 3: Desarrollo de Sistemas (9 Temas)
{chr(10).join(sources_b3)}

## 🔴 Bloque 4: Sistemas y Comunicaciones (10 Temas)
{chr(10).join(sources_b4)}

{"## 🔴 Otras Fuentes" + chr(10) + chr(10).join(sources_other) if sources_other else ""}

---

## 🟣 2. Subtemas: Entidades y Conceptos Teóricos ({len(entities) + len(concepts)} Fichas)

### 🟣 Entidades Técnicas y Normativas ({len(entities)} Fichas)
{chr(10).join(entities)}

### 🟣 Conceptos Teóricos y Arquitecturas ({len(concepts)} Fichas)
{chr(10).join(concepts)}

---

### 🔵 3. Conocimientos Concretos, Guías de Síntesis y Tablas de Examen ({len(syntheses)} Guías)

{chr(10).join(syntheses)}
{tests_section}
---

## 🛠️ Herramientas y Scripts del Repositorio
- `scripts/query.py`: Motor de búsqueda y consulta en consola sobre la base de conocimiento.
- `scripts/lint.py`: Linter de integridad de grafo, enlaces rotos y formato frontmatter.
- `scripts/test_tutorials.py`: Suite de validación automatizada de los tutoriales del wiki.
"""

    index_path = os.path.join(BASE_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(index_content.strip() + "\n")
    print(f"[OK] index.md reconstruido con {all_sources_count} fuentes, {len(entities)} entidades, {len(concepts)} conceptos, {len(syntheses)} síntesis y {all_tests_count} tests.")

if __name__ == "__main__":
    rebuild()
