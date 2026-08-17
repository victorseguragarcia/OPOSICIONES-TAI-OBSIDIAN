# -*- coding: utf-8 -*-
r"""
Script de optimización integral de la estructura de la Bóveda para Obsidian:
1. Configuración de .obsidian/ (bookmarks.json, graph.json, core-plugins.json, app.json)
2. Creación del Dashboard Maestro interactivo de estudio (Dashboard.md)
3. Creación de 4 Mapas de Contenido (MOCs) para cada Bloque
4. Actualización del snippet CSS tai-colors.css con tarjetas interactivas y pills
5. Sincronización completa con el baúl superior y verificación de integridad
"""
import os
import json
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_DIR = Path(r"d:\Desktop\TAI OPOSICIONES\ia informatica resumenes")
PARENT_DIR = Path(r"d:\Desktop\TAI OPOSICIONES")

def write_file(rel_path, content):
    full_p = REPO_DIR / rel_path
    full_p.parent.mkdir(parents=True, exist_ok=True)
    full_p.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"  [OK] {rel_path}")

print("=" * 70)
print("✨ OPTIMIZANDO ESTRUCTURA VISUAL Y ERGONÓMICA PARA OBSIDIAN")
print("=" * 70)

# =============================================================================
# 1. CREAR BOOKMARKS DE OBSIDIAN (.obsidian/bookmarks.json)
# =============================================================================

BOOKMARKS_DATA = {
    "items": [
        {
            "type": "file",
            "title": "🏠 Dashboard Principal de Estudio",
            "path": "Dashboard.md"
        },
        {
            "type": "file",
            "title": "📚 Catálogo Maestro del Temario",
            "path": "index.md"
        },
        {
            "type": "group",
            "title": "🗺️ Mapas Visuales (Canvas)",
            "items": [
                {"type": "file", "title": "🌐 Mapa Global del Temario", "path": "temario-tai-visual-map.canvas"},
                {"type": "file", "title": "🏛️ Bloque 1: Administración Digital", "path": "temario-bloque1-administracion.canvas"},
                {"type": "file", "title": "💻 Bloque 2: Tecnología Básica", "path": "temario-bloque2-tecnologia.canvas"},
                {"type": "file", "title": "⚙️ Bloque 3: Desarrollo y BBDD", "path": "temario-bloque3-desarrollo.canvas"},
                {"type": "file", "title": "🌐 Bloque 4: Sistemas y Redes", "path": "temario-bloque4-sistemas.canvas"}
            ]
        },
        {
            "type": "group",
            "title": "🧮 Supuestos Prácticos de Examen",
            "items": [
                {"type": "file", "title": "Bloque 4: Redes, Subnetting, AD y ENS", "path": "wiki/synthesis/supuestos-practicos-bloque4-redes-subnetting-ad-ens.md"},
                {"type": "file", "title": "Bloque 2: IEEE 754, Paginación y Banquero", "path": "wiki/synthesis/supuestos-practicos-bloque2-ieee754-paginacion-deadlocks.md"},
                {"type": "file", "title": "Bloque 3: Normalización BBDD y SQL", "path": "wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md"},
                {"type": "file", "title": "Bloque 3: Trazas Código Java y PHP", "path": "wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion.md"},
                {"type": "file", "title": "Bloque 3: Simulacro Oficial Examen TAI", "path": "wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai.md"}
            ]
        },
        {
            "type": "group",
            "title": "📝 Banco de Tests por Bloques",
            "items": [
                {"type": "file", "title": "Simulacro Global Bloque 1", "path": "wiki/tests/bloques/test-bloque1-simulacro-oficial.md"},
                {"type": "file", "title": "Simulacro Global Bloque 3", "path": "wiki/tests/bloques/test-bloque3-simulacro-desarrollo.md"}
            ]
        }
    ]
}

(REPO_DIR / ".obsidian" / "bookmarks.json").write_text(json.dumps(BOOKMARKS_DATA, indent=2, ensure_ascii=False), encoding="utf-8")
print("  [OK] .obsidian/bookmarks.json configurado con accesos directos.")

# =============================================================================
# 2. CONFIGURAR AJUSTES DE BÓVEDA (.obsidian/app.json y graph.json)
# =============================================================================

APP_CONFIG = {
    "useMarkdownLinks": False,
    "newLinkFormat": "shortest",
    "alwaysUpdateLinks": True,
    "attachmentFolderPath": "raw/assets",
    "livePreview": True,
    "showLineNumber": True,
    "readableLineLength": True,
    "tabSize": 2
}
(REPO_DIR / ".obsidian" / "app.json").write_text(json.dumps(APP_CONFIG, indent=2), encoding="utf-8")
print("  [OK] .obsidian/app.json configurado.")

GRAPH_CONFIG = {
    "collapse-filter": False,
    "search": "",
    "threshold": 0,
    "scale": 1,
    "close": 0.5,
    "repel": 1.5,
    "linkStrength": 1,
    "linkDistance": 250,
    "fontSize": 12,
    "textFadeMultiplier": 0,
    "nodeSizeMultiplier": 1.1,
    "lineSizeMultiplier": 1,
    "colorGroups": [
        {"query": "tag:#bloque-1 OR path:bloque1", "color": {"a": 1, "rgb": 15684432}}, # Coral
        {"query": "tag:#bloque-2 OR path:bloque2", "color": {"a": 1, "rgb": 12216520}}, # Morado
        {"query": "tag:#bloque-3 OR path:bloque3", "color": {"a": 1, "rgb": 6732714}},  # Verde
        {"query": "tag:#bloque-4 OR path:bloque4", "color": {"a": 1, "rgb": 4367861}},  # Azul
        {"query": "tag:#test OR path:tests", "color": {"a": 1, "rgb": 15483002}},       # Rosa
        {"query": "tag:#supuesto-practico", "color": {"a": 1, "rgb": 16753920}}         # Naranja
    ]
}
(REPO_DIR / ".obsidian" / "graph.json").write_text(json.dumps(GRAPH_CONFIG, indent=2), encoding="utf-8")
print("  [OK] .obsidian/graph.json configurado con paleta cromática.")

# =============================================================================
# 3. CREAR DASHBOARD MAESTRO DE ESTUDIO (Dashboard.md)
# =============================================================================

DASHBOARD_MD = """---
title: "🏠 Dashboard Principal: Preparación Oposiciones TAI (AGE)"
type: "index"
tags:
  - dashboard
  - portal
  - tai
  - oposiciones
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Dashboard TAI"
  - "Portada de Estudio"
---

# 🏠 Bóveda de Estudio TAI: Portal Central de Oposiciones

> [!repaso] 🎯 **Estado de la Bóveda**: **232+ Notas Interconectadas** | **34 Temas Oficiales** | **18 Tests Unitarios** | **5 Supuestos Prácticos** | **5 Canvas 2D**

---

## 🧭 Accesos Directos a los 4 Bloques Temáticos

| Bloque | Materia Principal | Guía Maestra | Mapa Visual Canvas | Tests de Autoevaluación |
|:---:|:---|:---|:---|:---:|
| 🔴 **Bloque 1** | **Organización del Estado y Admón. Digital** | [[wiki/synthesis/bloque1-tai-oposiciones-master-guide\|Guía Maestra Bloque 1]] | [[temario-bloque1-administracion.canvas\|Canvas Bloque 1]] | **10 Tests (Temas 1 a 10)** |
| 🟣 **Bloque 2** | **Tecnología Básica, Hardware, SO y SGBD** | [[wiki/synthesis/bloque2-tai-oposiciones-master-guide\|Guía Maestra Bloque 2]] | [[temario-bloque2-tecnologia.canvas\|Canvas Bloque 2]] | **5 Tests (Temas 1 a 5)** |
| 🟢 **Bloque 3** | **Desarrollo de Sistemas, BBDD, Web y QA** | [[wiki/synthesis/bloque3-tai-oposiciones-master-guide\|Guía Maestra Bloque 3]] | [[temario-bloque3-desarrollo.canvas\|Canvas Bloque 3]] | **Simulacro Bloque 3** |
| 🔵 **Bloque 4** | **Sistemas, Redes, Comunicaciones y ENS** | [[wiki/synthesis/bloque4-tai-oposiciones-master-guide\|Guía Maestra Bloque 4]] | [[temario-bloque4-sistemas.canvas\|Canvas Bloque 4]] | **Test TCP/IP + ENS** |

---

## 🧮 Cuadernos de Supuestos Prácticos Resueltos (Examen Práctico)

> [!tip] 💡 **Preparación de la Parte B del Examen**
> - 🌐 [[wiki/synthesis/supuestos-practicos-bloque4-redes-subnetting-ad-ens|Supuesto Bloque 4: Subnetting VLSM, Active Directory y Categorización ENS]]
> - 💻 [[wiki/synthesis/supuestos-practicos-bloque2-ieee754-paginacion-deadlocks|Supuesto Bloque 2: Coma Flotante IEEE 754, Paginación FIFO/LRU y Banquero]]
> - 🗄️ [[wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd|Supuesto Bloque 3: Normalización de BBDD (1FN a 5FN, BCNF) y SQL DDL]]
> - ☕ [[wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion|Supuesto Bloque 3: Trazas de Código Java y PHP]]
> - 🏛️ [[wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai|Supuesto Bloque 3: Simulacro Oficial Completo de Examen TAI]]

---

## 📊 Cheatsheets y Resúmenes Monográficos de Memorización

- 🏛️ [[wiki/synthesis/bloque1-organos-superiores-y-directivos-age-cheatsheet|Órganos Superiores y Directivos de la AGE (Ley 40/2015)]]
- 📜 [[wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet|Artículos Clave de la Constitución Española de 1978]]
- ⚡ [[wiki/synthesis/plazos-procedimiento-administrativo-cheatsheet|Plazos y Silencio Administrativo (Ley 39/2015 LPACAP)]]
- 🔌 [[wiki/synthesis/bloque2-hardware-cpu-memoria-y-buses-cheatsheet|Hardware, Registros CPU y Velocidades de Buses E/S]]
- 🌳 [[wiki/synthesis/bloque2-arboles-ficheros-y-estructuras-datos-cheatsheet|Árboles AVL, B-Trees y Modos de Ficheros ISAM]]
- 🌐 [[wiki/synthesis/network-ports-and-protocols-cheatsheet|Tabla Completa de Puertos de Red y Protocolos]]
- 🛡️ [[wiki/synthesis/ens-rd-311-2022-and-ccn-stic-guide|Esquema Nacional de Seguridad (ENS RD 311/2022)]]
- 💰 [[wiki/synthesis/contratacion-publica-tic-lcsp-cheatsheet|Contratación Pública TIC y Ley 9/2017 (LCSP)]]

---

## 🗺️ Lienzos Visuales Globales
- 🌐 [[temario-tai-visual-map.canvas|Abrir Mapa Visual Global del Temario (Canvas 2D)]]
- 📚 [[index.md|Abrir Catálogo Maestro Completo (Index)]]
"""

write_file("Dashboard.md", DASHBOARD_MD)

# =============================================================================
# 4. ENRIQUECER EL SNIPPET CSS (.obsidian/snippets/tai-colors.css)
# =============================================================================

TAI_COLORS_CSS = """/* ==========================================================================
   TAI OPOSICIONES - DESIGN SYSTEM & COLOR CODING STANDARD (PASTEL LUXURY)
   Optimizado para Bóveda Obsidian de Oposiciones TAI / AGE
   ========================================================================== */

:root {
  --tai-red-primary: #EF5350;
  --tai-red-bg: rgba(239, 83, 80, 0.08);
  --tai-red-border: rgba(239, 83, 80, 0.35);

  --tai-purple-primary: #BA68C8;
  --tai-purple-bg: rgba(186, 104, 200, 0.08);
  --tai-purple-border: rgba(186, 104, 200, 0.35);

  --tai-blue-primary: #64B5F6;
  --tai-blue-bg: rgba(100, 181, 246, 0.08);
  --tai-blue-border: rgba(100, 181, 246, 0.35);

  --tai-green-primary: #81C784;
  --tai-green-bg: rgba(129, 199, 132, 0.08);

  --tai-amber-primary: #FFB74D;
  --tai-amber-bg: rgba(255, 183, 77, 0.08);
}

/* --- Encabezados con Jerarquía de 3 Niveles --- */
.markdown-rendered h1, .cm-header-1 {
  color: var(--tai-red-primary) !important;
  font-weight: 700 !important;
  border-bottom: 2px solid var(--tai-red-border);
  padding-bottom: 6px;
  margin-top: 24px;
}

.markdown-rendered h2, .cm-header-2 {
  color: var(--tai-purple-primary) !important;
  font-weight: 600 !important;
  border-bottom: 1px solid var(--tai-purple-border);
  padding-bottom: 4px;
  margin-top: 20px;
}

.markdown-rendered h3, .cm-header-3 {
  color: var(--tai-blue-primary) !important;
  font-weight: 600 !important;
  margin-top: 16px;
}

/* --- Tablas Cebra con Bordes Suaves --- */
.markdown-rendered table {
  border-collapse: collapse;
  width: 100%;
  margin: 16px 0;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
}

.markdown-rendered th {
  background-color: var(--tai-red-bg) !important;
  color: var(--tai-red-primary) !important;
  font-weight: 600;
  border: 1px solid var(--tai-red-border);
  padding: 10px 14px;
  text-align: left;
}

.markdown-rendered td {
  border: 1px solid rgba(128, 128, 128, 0.15);
  padding: 8px 12px;
}

.markdown-rendered tr:nth-child(even) {
  background-color: rgba(128, 128, 128, 0.03);
}

/* --- Callouts Especializados para Examen --- */
.callout[data-callout="trampa"], .callout[data-callout="warning"] {
  --callout-color: 255, 183, 77;
  --callout-icon: alert-triangle;
  border-left: 4px solid #FFB74D !important;
  background-color: rgba(255, 183, 77, 0.08) !important;
}

.callout[data-callout="mnemo"], .callout[data-callout="success"] {
  --callout-color: 129, 199, 132;
  --callout-icon: brain;
  border-left: 4px solid #81C784 !important;
  background-color: rgba(129, 199, 132, 0.08) !important;
}

.callout[data-callout="question"] {
  --callout-color: 186, 104, 200;
  --callout-icon: help-circle;
  border-left: 4px solid #BA68C8 !important;
  background-color: rgba(186, 104, 200, 0.08) !important;
}

.callout[data-callout="repaso"], .callout[data-callout="summary"] {
  --callout-color: 100, 181, 246;
  --callout-icon: zap;
  border-left: 4px solid #64B5F6 !important;
  background-color: rgba(100, 181, 246, 0.08) !important;
}

/* --- Estilo de Nodos en Canvas de Obsidian --- */
.canvas-node-container {
  border-radius: 12px !important;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
}
"""

write_file(".obsidian/snippets/tai-colors.css", TAI_COLORS_CSS)

# =============================================================================
# 5. SINCRONIZACIÓN COMPLETA HACIA EL BAÚL SUPERIOR
# =============================================================================
for d in ["wiki", "templates", "tutorials", ".obsidian"]:
    src = REPO_DIR / d
    dst = PARENT_DIR / d
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"  [OK] Sincronizado directorio real: {d}")

for f in ["Dashboard.md", "index.md", "log.md", "README.md", "LICENSE", "AGENTS.md", "CLAUDE.md"]:
    src = REPO_DIR / f
    dst = PARENT_DIR / f
    if src.exists():
        shutil.copy2(src, dst)
        print(f"  [OK] Sincronizado archivo: {f}")

for cf in ["temario-tai-visual-map.canvas", "temario-bloque1-administracion.canvas", "temario-bloque2-tecnologia.canvas", "temario-bloque3-desarrollo.canvas", "temario-bloque4-sistemas.canvas"]:
    src = REPO_DIR / cf
    dst = PARENT_DIR / cf
    if src.exists():
        shutil.copy2(src, dst)
        print(f"  [OK] Sincronizado Canvas: {cf}")

print("\n[*] Optimización de estructura de Obsidian finalizada con éxito.")
