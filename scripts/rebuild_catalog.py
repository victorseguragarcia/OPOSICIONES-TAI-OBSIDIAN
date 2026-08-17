# -*- coding: utf-8 -*-
"""
Script para reconstruir dinámicamente index.md y log.md tras la expansión masiva de la wiki.
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
    sources = []
    entities = []
    concepts = []
    syntheses = []

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
                sources.append(item)
            elif ntype == "entity":
                entities.append(item)
            elif ntype == "concept":
                concepts.append(item)
            elif ntype == "synthesis":
                syntheses.append(item)

    index_content = f"""# Master Wiki Index

Bienvenido al catálogo maestro del **LLM Wiki** de Informática y Comunicaciones para Oposiciones TAI.
Este repositorio compila de forma exhaustiva, estructurada y bidireccionalmente enlazada todos los temas del **Bloque 4 (Sistemas y Comunicaciones)**.

---

## 📑 1. Fuentes Resumidas (`wiki/sources/`)
Resúmenes ejecutivos, desglose temático detallado y tablas de datos clave extraídas directamente de los documentos PDF oficiales:

{chr(10).join(sources)}

---

## ⚙️ 2. Entidades (`wiki/entities/`)
Fichas técnicas de sistemas operativos, protocolos, arquitecturas de hardware, estándares IEEE/RFC, comandos y herramientas:

{chr(10).join(entities)}

---

## 🧠 3. Conceptos Teóricos (`wiki/concepts/`)
Explicaciones en profundidad sobre arquitecturas de sistemas, algoritmos, modelos de capas, criptografía, topologías y gobernanza TI:

{chr(10).join(concepts)}

---

## 📚 4. Síntesis y Guías de Estudio (`wiki/synthesis/`)
Matrices comparativas, resúmenes monográficos de alto nivel y tablas maestras para memorización de examen:

{chr(10).join(syntheses)}

---

## 🛠️ Herramientas y Scripts de Automatización
- `scripts/query.py`: Motor de búsqueda y consulta en consola sobre la base de conocimiento.
- `scripts/lint.py`: Linter de integridad de grafo, enlaces rotos y formato frontmatter.
- `scripts/test_tutorials.py`: Suite de validación automatizada de los tutoriales del wiki.
"""

    index_path = os.path.join(BASE_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(index_content.strip() + "\n")
    print(f"[OK] index.md reconstruido con {len(sources)} fuentes, {len(entities)} entidades, {len(concepts)} conceptos y {len(syntheses)} síntesis.")

    # Actualizar log.md
    log_path = os.path.join(BASE_DIR, "log.md")
    today = datetime.now().strftime("%Y-%m-%d")
    log_entry = f"""

## [{today}] expansion | Ampliación Exhaustiva de Contenidos del Bloque 4
- Ampliación masiva de contenido técnico a partir de las ~37.000 líneas de los 10 PDFs del Bloque 4.
- Generadas notas de alta densidad técnica (100-250 líneas por fichero) con puertos, RFCs, comandos, tablas de examen y algoritmos.
- 10 Fuentes ampliadas en `wiki/sources/` (Temas 01 al 10).
- 25 Entidades ampliadas y creadas en `wiki/entities/` (incluyendo `active-directory`, `ldap-protocol`, `raid-storage`, `http-protocol`).
- 15 Conceptos ampliados y creados en `wiki/concepts/` (incluyendo `cryptography-and-digital-signatures`, `directory-services-and-identity`, `incident-management-and-itil`).
- 10 Síntesis monográficas en `wiki/synthesis/` (incluyendo `network-ports-and-protocols-cheatsheet`, `cryptography-algorithms-comparison`, `active-directory-and-ldap-guide`, `cpd-tier-levels-and-disaster-recovery`, `email-protocols-smtp-pop-imap-guide`, `security-frameworks-ens-magerit-ccn`).
- Catálogo maestro `index.md` reconstruido y sincronizado.
"""
    with open(log_path, "a", encoding="utf-8", newline="\n") as f:
        f.write(log_entry)
    print("[OK] log.md actualizado.")

if __name__ == "__main__":
    rebuild()
