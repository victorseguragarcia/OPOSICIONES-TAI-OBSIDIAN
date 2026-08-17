# 🏛️ Guía Maestra y Ecosistema de Estudio TAI (AGE) - LLM Wiki

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Obsidian Vault](https://img.shields.io/badge/Obsidian-Vault%20Ready-purple.svg)](https://obsidian.md)
[![Notes Count](https://img.shields.io/badge/Notes-213%2B%20Interconnected-success.svg)](index.md)
[![Tests Passing](https://img.shields.io/badge/Linter%20&%20Health-100%25%20Passed-brightgreen.svg)](scripts/lint.py)

> **Base de Conocimiento Persistente, Grafo de Estudio Interactivo y Banco de Autoevaluación**  
> Diseñado según la arquitectura **LLM Wiki Pattern** para la preparación del Cuerpo de **Técnicos Auxiliares de Informática (TAI)** de la Administración General del Estado (AGE).

---

## 📖 Índice General de la Guía
1. [¿Qué es este repositorio y qué contiene?](#-1-qué-es-este-repositorio-y-qué-contiene)
2. [Guía de Inicio Rápido (Quickstart en 3 Pasos)](#-2-guía-de-inicio-rápido-quickstart-en-3-pasos)
3. [Cómo Explorar y Navegar por el Temario](#-3-cómo-explorar-y-navegar-por-el-temario)
4. [El Sistema Visual de Estudio (Colores y Callouts)](#-4-el-sistema-visual-de-estudio-colores-y-callouts)
5. [Metodología y Flujo de Estudio Recomendado](#-5-metodología-y-flujo-de-estudio-recomendado)
6. [Banco de Tests y Supuestos Prácticos](#-6-banco-de-tests-y-supuestos-prácticos)
7. [Lienzos Interactivos (Obsidian Canvas)](#-7-lienzos-interactivos-obsidian-canvas)
8. [Herramientas CLI y Scripts Automatizados](#-8-herramientas-cli-y-scripts-automatizados)
9. [Cómo Crear y Añadir Nuevos Contenidos](#-9-cómo-crear-y-añadir-nuevos-contenidos)
10. [Plugins y Ajustes Recomendados para Obsidian](#-10-plugins-y-ajustes-recomendados-para-obsidian)

---

## 📌 1. ¿Qué es este repositorio y qué contiene?

Este repositorio es una **base de conocimiento viva y estructurada** que contiene todo el temario oficial de las oposiciones TAI (Bloques 1, 2, 3 y 4), descompuesto en un **grafo de notas enlazadas (`[[...]]`)** sin lagunas ni enlaces rotos.

```
                                TEMARIO OFICIAL TAI (AGE)
                                            │
       ┌────────────────────┬───────────────┴───────────────┬────────────────────┐
       ▼                    ▼                               ▼                    ▼
   🔴 BLOQUE 1          🔴 BLOQUE 2                     🔴 BLOQUE 3          🔴 BLOQUE 4
Organización del     Tecnología Básica               Desarrollo de       Sistemas y Redes
Estado y Normativa   Hardware, SO y SGBD             Sistemas y Web      Comunicaciones y ENS
 • CE 1978 y AGE      • C2, IEEE 754, Unicode         • Normalización     • Pila OSI y TCP/IP
 • LPACAP y LRJSP     • PCIe, NVMe, USB4              • UML 2.x y GoF     • Subnetting IPv4/IPv6
 • TREBEP y Personal  • Algoritmos Big-O              • Java / .NET       • Windows Server / AD
 • Red SARA y eIDAS   • Planificación CPU y Memoria   • REST vs SOAP      • Linux y SysAdmin
 • RGPD / LOPDGDD     • NoSQL y Teorema CAP           • MÉTRICA v3 y QA   • Seguridad y ENS RD 311
```

### 📊 Contenido en Cifras:
- **213+ Notas Markdown**: 100% interconectadas y categorizadas.
- **35 Temas Oficiales Resumidos** (`wiki/sources/`).
- **113 Fichas de Entidades y Conceptos** (`wiki/entities/` y `wiki/concepts/`).
- **50 Guías de Síntesis y Cheatsheets** (`wiki/synthesis/`).
- **3 Cuadernos de Supuestos Prácticos Resueltos** (BBDD, Código Java/PHP y Examen TAI).
- **Banco de Autoevaluación** con soluciones ocultas (`wiki/tests/`).
- **5 Mapas Conceptuales Interactivos** (`.canvas`).

---

## 🚀 2. Guía de Inicio Rápido (Quickstart en 3 Pasos)

### Paso 1: Clonar el Repositorio
Abre tu terminal o consola Git y clona el proyecto en tu equipo:
```bash
git clone https://github.com/victorseguragarcia/OPOSICIONES-TAI-OBSIDIAN.git
cd OPOSICIONES-TAI-OBSIDIAN
```

### Paso 2: Abrir en Obsidian
1. Descarga e instala [Obsidian](https://obsidian.md/) (gratuito para uso personal).
2. En la pantalla inicial de Obsidian, haz clic en **"Abrir carpeta como bóveda" (*Open folder as vault*)**.
3. Selecciona la carpeta donde clonaste el repositorio.

### Paso 3: Activar el Snippet Visual de Colores
1. En Obsidian, ve a **Ajustes (icono de engranaje) $\rightarrow$ Apariencia (*Appearance*)**.
2. Desplázate hacia abajo hasta la sección **"Fragmentos CSS" (*CSS snippets*)**.
3. Asegúrate de que el snippet `tai-colors` esté **activado (interruptor en verde)**.  
   *(Esto aplicará automáticamente la jerarquía visual de colores, tablas cebra y callouts).*

---

## 🧭 3. Cómo Explorar y Navegar por el Temario

Existen **4 formas complementarias** de navegar por el contenido según tu objetivo de estudio:

```
                                MÉTODOS DE NAVEGACIÓN
                                          │
       ┌──────────────────┬───────────────┴───────────────┬──────────────────┐
       ▼                  ▼                               ▼                  ▼
1. CATÁLOGO MAESTRO  2. MAPAS CANVAS (Visual)        3. GRAPH VIEW      4. MOTOR CLI
   `index.md`        `.canvas` por Bloque            (Grafo Global)     `python query.py`
```

1. [**Catálogo Maestro (`index.md`)**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/index.md):  
   La portada central del repositorio. Contiene el listado completo de temas, entidades, síntesis y tests con accesos directos de un clic.
2. [**Lienzo Visual Global (`temario-tai-visual-map.canvas`)**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-tai-visual-map.canvas):  
   Permite hacer zoom, arrastrar y abrir notas directamente en un lienzo interactivo 2D.
3. **Vista de Grafo de Obsidian (*Graph View*)**:  
   Pulsa `Ctrl + G` en Obsidian para ver cómo los conceptos, protocolos y leyes se relacionan entre sí en un grafo tridimensional coloreado.
4. **Búsqueda Instantánea por Terminal (Motor de Consulta)**:  
   Si necesitas consultar un dato rápidamente mientras programas o estudias, usa el script CLI:
   ```bash
   python scripts/query.py "Red SARA SIR GEISER"
   python scripts/query.py "Teorema CAP MongoDB Redis"
   python scripts/query.py "Complejidad McCabe"
   ```

---

## 🎨 4. El Sistema Visual de Estudio (Colores y Callouts)

Todo el contenido utiliza una **jerarquía cromática de 3 niveles** definida en `.obsidian/snippets/tai-colors.css` para potenciar la memoria fotográfica:

### 🌈 Jerarquía de Niveles:
- 🔴 **Nivel 1 (H1 / Bloques / Leyes Principales)**: Color **Coral Pastel** (`#EF5350`). Identifica portadas y grandes leyes.
- 🟣 **Nivel 2 (H2 / Subtemas / Entidades)**: Color **Orquídea Pastel** (`#BA68C8`). Identifica componentes, tecnologías y clasificaciones.
- 🔵 **Nivel 3 (H3 / Tablas / Datos Concretos)**: Color **Azul Cielo** (`#64B5F6`). Identifica datos precisos de examen (puertos, RFCs, artículos, plazos).

### 💬 Callouts Especializados de Examen:

| Tipo de Callout | Sintaxis en Markdown | Visualización y Utilidad |
|:---|:---|:---|
| ⚠️ **Trampa de Examen** | `> [!trampa]` o `> [!warning]` | **Ámbar**: Avisa de distractores engañosos y errores frecuentes de test. |
| 🧠 **Mnemotecnia** | `> [!mnemo]` o `> [!success]` | **Menta**: Reglas mnemotécnicas para memorizar listas y secuencias. |
| ❓ **Pregunta Test** | `> [!question]-` | **Lavanda**: Desplegable con solución oculta para **Active Recall**. |
| ⚡ **Resumen Express** | `> [!repaso]` o `> [!summary]` | **Cian**: Resumen en 30 segundos con las 3-4 ideas clave del tema. |

---

## 🎓 5. Metodología y Flujo de Estudio Recomendado

Para aprovechar al máximo esta base de conocimiento, sigue este **flujo de 5 pasos por cada tema**:

```
[1. Resumen Fuente]  ──►  [2. Grafo de Conceptos]  ──►  [3. Síntesis / Cheatsheet]  ──►  [4. Supuestos]  ──►  [5. Test Autoevaluación]
 (wiki/sources/)           (wiki/entities/)             (wiki/synthesis/)               (Casos Prácticos)      (wiki/tests/)
```

1. **Lectura Base**: Abre el resumen del tema en `wiki/sources/` (ej. `bloque3-tema01.md`).
2. **Profundización Asociativa**: Haz clic en los wikilinks `[[...]]` de las entidades o conceptos que no domines (ej. `[[relational-database-modeling-and-normalization]]`).
3. **Consolidación de Datos de Examen**: Acude a la guía de síntesis en `wiki/synthesis/` (ej. `database-normalization-and-sql-cheatsheet.md`) para memorizar tablas, fórmulas y plazos.
4. **Práctica Real**: Resuelve los ejercicios de los cuadernos de supuestos prácticos en `wiki/synthesis/`.
5. **Autoevaluación con Active Recall**: Realiza el test temático en `wiki/tests/temas/` respondiendo las 10 preguntas antes de desplegar el solucionario.

---

## 📝 6. Banco de Tests y Supuestos Prácticos

### 📂 Supuestos Prácticos Monográficos Resueltos:
- 💻 [**Supuesto Práctico: Normalización de BBDD y SQL DDL**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md): Casos reales de descomposición de 1FN a 5FN, BCNF, dependencias multivaluadas y sentencias DDL.
- ☕ [**Supuesto Práctico: Trazas de Código Java y PHP**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion.md): Trazas de bucles `while`/`for`, postincrementos `i++`, operadores ternarios y estructuras de control.
- 🏛️ [**Supuesto Práctico Oficial TAI: Simulacro Examen Bloque III**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai.md): 20 preguntas reales con plantilla argumentada cubriendo MÉTRICA v3, UML, REST/SOAP, McCabe, ACID y RD 1112/2018.

### 📝 Banco de Autoevaluación:
- `wiki/tests/temas/`: Cuestionarios específicos por temas individuales (ej. `test-bloque1-tema01-constitucion.md`).
- `wiki/tests/bloques/`: Simulacros de exámenes completos integrando todos los temas de un bloque con límite de tiempo y puntuación oficial ($+1.0$ acierto, $-0.33$ fallo).

---

## 🗺️ 7. Lienzos Interactivos (Obsidian Canvas)

El repositorio incluye 5 lienzos Canvas listos para abrir en Obsidian:

1. 🌐 [**`temario-tai-visual-map.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-tai-visual-map.canvas): Mapa global con los 4 bloques interconectados.
2. 🏛️ [**`temario-bloque1-administracion.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque1-administracion.canvas): Bloque 1 (Constitución, AGE, UE, TREBEP, Red SARA, Cl@ve, eIDAS, RGPD).
3. 💻 [**`temario-bloque2-tecnologia.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque2-tecnologia.canvas): Bloque 2 (C2, IEEE 754, Periféricos, Algoritmos Big-O, SO, Paginación, NoSQL).
4. ⚙️ [**`temario-bloque3-desarrollo.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque3-desarrollo.canvas): Bloque 3 (MÉTRICA v3, Scrum, Normalización, SQL, UML, Java/.NET, QA).
5. 🌐 [**`temario-bloque4-sistemas.canvas`**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/temario-bloque4-sistemas.canvas): Bloque 4 (Redes OSI/TCP-IP, Subnetting, Windows Server, Linux, ENS).

---

## 🛠️ 8. Herramientas CLI y Scripts Automatizados

El repositorio cuenta con una suite de scripts en Python en la carpeta `scripts/`:

| Script | Comando de Ejecución | Qué hace |
|:---|:---|:---|
| **Buscador Temático** | `python scripts/query.py "<términos>"` | Búsqueda por relevancia en toda la wiki con snippets y puntuación. |
| **Linter y Health Check** | `python scripts/lint.py` | Detecta enlaces rotos, notas huérfanas y errores en el frontmatter YAML. |
| **Reconstructor de Índice** | `python scripts/rebuild_catalog.py` | Regenera automáticamente `index.md` y registra notas nuevas. |
| **Auditoría de Archivos** | `python scripts/deep_filesystem_audit.py` | Auditoría de 7 niveles sobre directorios, canvas, links y metadatos. |
| **Suite de Tutoriales** | `python scripts/test_tutorials.py` | Ejecuta las pruebas automatizadas del flujo de trabajo LLM Wiki. |

---

## ➕ 9. Cómo Crear y Añadir Nuevos Contenidos

Si deseas crear nuevos tests o notas de síntesis respetando el estándar del repositorio:

### A. Para crear un nuevo Test de Tema o Bloque:
1. Copia la plantilla correspondiente desde `templates/test-tema.md` o `templates/test-bloque.md`.
2. Guarda el nuevo archivo en `wiki/tests/temas/` o `wiki/tests/bloques/`.
3. Rellena las preguntas con checkboxes `- [ ] a)` y las soluciones en el callout desplegable `> [!question]-`.
4. Ejecuta `python scripts/rebuild_catalog.py` para añadirlo automáticamente a `index.md`.

### B. Estándar de Frontmatter YAML:
Toda nota debe comenzar con este bloque YAML:
```yaml
---
title: "Título de la Nota"
type: "source | entity | concept | synthesis | test"
tags:
  - oposiciones
  - tai
  - bloque-X
sources:
  - "raw/sources/nombre-fuente.md"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
aliases:
  - "Nombre Alternativo"
---
```

---

## ⚙️ 10. Plugins y Ajustes Recomendados para Obsidian

Para una experiencia óptima en Obsidian, se recomienda configurar:

1. **Ajustes de Enlaces (*Files and links*)**:
   - *Default location for new notes*: Misma carpeta que el archivo actual.
   - *New link format*: **Shortest path when possible**.
   - *Use [[Wikilinks]]*: **Activado**.
2. **Plugins de la Comunidad Recomendados**:
   - **Dataview**: Para generar tablas dinámicas automáticas basadas en etiquetas y frontmatter.
   - **Omnisearch**: Motor de búsqueda indexada ultrarrápida con previsualización en Obsidian.
   - **Editing Toolbar**: Barra flotante para dar formato rápido a tablas y callouts.
   - **Paste URL into Selection**: Facilita la creación de enlaces markdown.

---

## 📜 11. Créditos, Reconocimientos y Licencia

### 👤 Autoría y Mantenedor
- **Autor**: **Víctor Segura García** ([@victorseguragarcia](https://github.com/victorseguragarcia))
- **Objetivo**: Proyecto libre y abierto para la comunidad de opositores al Cuerpo de **Técnicos Auxiliares de Informática (TAI) de la Administración General del Estado (AGE)**.

### 🌟 Créditos y Reconocimientos
- **Arquitectura de Base de Conocimiento**: Basado en el concepto y diseño arquitectónico del **LLM Wiki Pattern** formulado por **[Andrej Karpathy](https://github.com/karpathy)** (*ex-OpenAI / Tesla AI*) para sistemas de conocimiento persistente con modelos de lenguaje.
- **Programa Oficial y Normativa**: Basado en las convocatorias y temarios oficiales del **[INAP](https://www.inap.es/)** (*Instituto Nacional de Administración Pública*) y del **Ministerio para la Transformación Digital y de la Función Pública**.
- **Entorno de Visualización**: Diseñado para y optimizado sobre el ecosistema de notas enlazadas de **[Obsidian.md](https://obsidian.md/)**.

### 📄 Licencia
Este proyecto se distribuye bajo la licencia **MIT License**. Puedes consultar los términos completos en el archivo [`LICENSE`](LICENSE).

```
MIT License - Copyright (c) 2026 Víctor Segura García
```
