# -*- coding: utf-8 -*-
"""
Script generador de las notas fuente estructuradas para wiki/sources/ del Bloque 1 (TAI).
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def write_file(rel_path, content):
    full_path = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content.strip() + "\n")
    print(f"    [OK] {rel_path}")

WIKI_SOURCES = {
    "wiki/sources/bloque1-tema01.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 01: La Constitución Española de 1978"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema01
  - constitucion
  - derechos-fundamentales
  - corona
  - cortes-generales
  - tribunal-constitucional
sources:
  - "raw/sources/bloque1-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen La Constitución Española de 1978"
  - "bloque1-tema01"
---

# Resumen Fuente: Bloque 1 - Tema 01: La Constitución Española de 1978

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema01.md|bloque1-tema01.md]].

---

## 📖 Resumen Ejecutivo

Este tema abarca la norma suprema del ordenamiento jurídico español: la **Constitución Española de 1978**. Se analiza su estructura sistemática (169 artículos, Título Preliminar y 10 Títulos), los valores superiores y principios del Estado social y democrático de Derecho, la declaración y catálogo de derechos y deberes fundamentales (Título I) con su triple nivel de protección constitucional y el Defensor del Pueblo, la institución de la Corona y el refrendo de los actos regios (Título II), la composición bicameral y potestades de las Cortes Generales (Título III), las competencias y composición del Tribunal Constitucional (Título IX), y los procedimientos de reforma ordinario y agravado (Título X).

---

## 🧩 Estructura y Desglose Temático

### 1. Estructura y Principios Constitucionales
- **Fechas Clave de Aprobación**:
  - Aprobada por las Cortes Generales: **31 de octubre de 1978**.
  - Ratificada en referéndum por el pueblo español: **6 de diciembre de 1978**.
  - Sancionada y promulgada por el Rey: **27 de diciembre de 1978**.
  - Publicada en el BOE y entrada en vigor: **29 de diciembre de 1978**.
- **Estructura Numérica**: 1 Preámbulo, 169 Artículos, 1 Título Preliminar, 10 Títulos numerados, 4 Disposiciones Adicionales, 9 Disposiciones Transitorias, 1 Disposición Derogatoria y 1 Disposición Final.
- **Principios del Título Preliminar**:
  - Art. 1.1: Estado social y democrático de Derecho. Valores superiores: **Libertad, Justicia, Igualdad y Pluralismo político**.
  - Art. 1.2: Soberanía nacional reside en el pueblo español.
  - Art. 1.3: Forma política: **Monarquía parlamentaria**.
  - Art. 2: Indisoluble unidad de la Nación española y derecho a la autonomía de nacionalidades y regiones.
  - Art. 9.3: Principios de legalidad, jerarquía normativa, publicidad, irretroactividad de sanciones desfavorables, seguridad jurídica e interdicción de la arbitrariedad.

### 2. Título I: Derechos y Deberes Fundamentales y Garantías
- **Estructura del Título I (Art. 10 a 55)**:
  - Art. 14: Principio de igualdad ante la ley.
  - **Sección 1ª (Art. 15-29)**: Derechos Fundamentales y Libertades Públicas (Vida, integridad, libertad ideológica/religiosa, libertad personal y detención máx 72h, intimidad/domicilio, libre expresión, reunión, asociación, sufragio, tutela judicial efectiva art. 24, educación, sindicación y huelga, petición).
  - **Sección 2ª (Art. 30-38)**: Derechos y Deberes de los ciudadanos (Objeción de conciencia art. 30, tributos justos art. 31, propiedad privada art. 33, trabajo art. 35, libertad de empresa art. 38).
  - **Capítulo III (Art. 39-52)**: Principios rectores de la política social y económica.
- **Sistema de Garantías (Art. 53)**:
  - **Nivel Máximo (Art. 14 + Art. 15-29 + Art. 30.2)**: Reserva de **Ley Orgánica** (art. 15-29), tutela judicial preferente y sumaria, y **Recurso de Amparo ante el Tribunal Constitucional**.
  - **Nivel Medio (Art. 30-38)**: Reserva de ley ordinaria (respetando contenido esencial) y Recurso de Inconstitucionalidad.
  - **Nivel Básico (Art. 39-52)**: Solo alegables ante la jurisdicción ordinaria según las leyes que los desarrollen.
- **El Defensor del Pueblo (Art. 54)**: Alto comisionado de las Cortes Generales regulado por LO 3/1981. Elegido por mayoría de **3/5 del Congreso y 3/5 del Senado** por mandato de **5 años**.

### 3. La Corona (Título II, Art. 56 a 65)
- El Rey es el Jefe del Estado, símbolo de su unidad y permanencia.
- **Inviolabilidad y Refrendo (Art. 56.3 y 64)**: La persona del Rey es inviolable y no está sujeta a responsabilidad. Sus actos están siempre **refrendados** por el Presidente del Gobierno, Ministros competentes o el Presidente del Congreso (propuesta/nombramiento de Presidente y disolución art. 99). Carecen de validez sin refrendo.
- **Sucesión (Art. 57)**: Primogenitura y representación (línea anterior a posteriores, grado más próximo, varón a mujer, mayor a menor edad).

### 4. Las Cortes Generales (Título III, Art. 66 a 96)
- **Congreso de los Diputados (Art. 68)**: 350 Diputados elegidos por sufragio universal proporcional (regla D'Hondt) en circunscripciones provinciales por mandato de **4 años**.
- **Senado (Art. 69)**: Cámara de representación territorial por mandato de **4 años** (4 senadores por provincia peninsular + senadores insulares + senadores designados por Asambleas de CCAA: 1 fijo + 1 por millón de habitantes).
- **Tipos de Normas Legales**:
  - **Leyes Orgánicas (Art. 81)**: Desarrollo de DDFF (art. 15-29), Estatutos de Autonomía y Régimen Electoral General. Exigen **mayoría absoluta del Congreso** en votación final de conjunto.
  - **Reales Decretos-Leyes (Art. 86)**: Extraordinaria y urgente necesidad. Sometidos a convalidación del Congreso en **30 días**.

### 5. El Tribunal Constitucional (Título IX, Art. 159 a 165)
- **Composición**: **12 magistrados** nombrados por el Rey por **9 años** (renovación de 4 miembros cada 3 años): 4 Congreso (3/5), 4 Senado (3/5), 2 Gobierno y 2 CGPJ.
- **Procesos**: Recurso de Inconstitucionalidad, Cuestión de Inconstitucionalidad, Recurso de Amparo y Conflictos de Competencia.

### 6. Reforma Constitucional (Título X, Art. 166 a 169)
- **Ordinaria (Art. 167)**: Mayoría de **3/5 de cada Cámara**. Referéndum facultativo si lo pide el 10% de Diputados o Senadores en 15 días.
- **Agravada (Art. 168)**: Revisión total o de Título Preliminar, Título I Secc. 1ª (15-29) o Título II (Corona). Mayoría de **2/3 de cada Cámara** $\rightarrow$ Disolución de Cortes $\rightarrow$ Ratificación por nuevas Cortes (2/3) $\rightarrow$ **Referéndum obligatorio y vinculante**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Parámetro / Artículo | Especificación Constitucional |
|----------------------|-------------------------------|
| Fecha Ratificación Referéndum | **6 de diciembre de 1978** |
| Fecha Entrada en Vigor | **29 de diciembre de 1978** (publicación BOE) |
| Número de Artículos | **169 artículos** |
| Mayoría Ley Orgánica (Art. 81) | **Mayoría Absoluta del Congreso** |
| Convalidación Real Decreto-Ley | **30 días naturales** ante el Congreso |
| Mandato Defensor del Pueblo | **5 años** (Mayoría de 3/5 en ambas Cámaras) |
| Composición Tribunal Constitucional | **12 miembros** por mandato de **9 años** (renovación 1/3 cada 3 años) |
| Reforma Agravada (Art. 168) | Mayoría de **2/3**, disolución de Cortes y **referéndum preceptivo** |

---

## 🔗 Enlaces del Grafo de Conocimiento

### Entidades Relacionadas:
- [[wiki/entities/constitucion-espanola-1978|Constitución Española de 1978]]
- [[wiki/entities/cortes-generales|Cortes Generales y Procedimiento Legislativo]]

### Conceptos Teóricos:
- [[wiki/concepts/derechos-fundamentales-y-libertades-publicas|Derechos Fundamentales, Garantías y Recurso de Amparo]]

### Síntesis de Estudio:
- [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1: Administración Pública y Normativa (TAI)]]
- [[wiki/synthesis/constitucion-espanola-articulos-clave-cheatsheet|Cheatsheet de Artículos Clave de la Constitución Española]]
""",

    "wiki/sources/bloque1-tema02.md": """---
title: "Resumen Fuente: Bloque 1 - Tema 02: El Gobierno y la Administración General del Estado"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-1
  - tema02
  - gobierno
  - age
  - consejo-ministros
  - ley-40-2015
  - ley-50-1997
sources:
  - "raw/sources/bloque1-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen El Gobierno y la AGE"
  - "bloque1-tema02"
---

# Resumen Fuente: Bloque 1 - Tema 02: El Gobierno y la Administración General del Estado

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque1-tema02.md|bloque1-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la regulación constitucional y legal del Poder Ejecutivo y de la Administración General del Estado: la composición y funcionamiento del Gobierno bajo la **Ley 50/1997**, los procedimientos parlamentarios de investidura (Art. 99 CE), cuestión de confianza y moción de censura constructiva, los órganos de apoyo y colaboración (Comisión General de Secretarios de Estado y Subsecretarios), la estructura organizativa de la AGE según la **Ley 40/2015** distinguiendo entre órganos superiores y directivos, y el despliegue territorial (Delegados y Subdelegados del Gobierno) y exterior.

---

## 🧩 Estructura y Desglose Temático

### 1. El Gobierno y el Consejo de Ministros (Ley 50/1997)
- **Composición (Art. 98 CE)**: Presidente, Vicepresidentes (opcionales), Ministros y demás miembros que establezca la ley.
- **Consejo de Ministros**: Órgano colegiado superior del Gobierno. Sus deliberaciones son **secretas**.
- **Comisión General de Secretarios de Estado y Subsecretarios**: Órgano preparatorio preceptivo de las sesiones del Consejo de Ministros (presidida por el Vicepresidente o Ministro de la Presidencia). Ningún asunto puede someterse al Consejo de Ministros sin su examen previo (salvo urgencia declarada).

### 2. Investidura, Confianza y Moción de Censura
- **Investidura del Presidente del Gobierno (Art. 99 CE)**:
  - Propuesto por el Rey tras consultas con los grupos parlamentarios.
  - Votación 1: **Mayoría absoluta** (176 votos).
  - Votación 2 (48 horas después): **Mayoría simple**.
  - Si en **2 meses** desde la primera votación nadie es investido $\rightarrow$ Disolución automática de Cortes y convocatoria de elecciones.
- **Cuestión de Confianza (Art. 112 CE)**: Planteada por el Presidente previa deliberación del Consejo de Ministros. Se gana por **mayoría simple**. Si se pierde, dimisión del Gobierno.
- **Moción de Censura (Art. 113 CE)**:
  - Constructiva (con candidato alternativo a Presidente).
  - Propuesta por al menos **1/10 de los Diputados (35 Diputados)**.
  - Periodo de enfriamiento: votación tras **5 días** (2 primeros días para mociones alternativas).
  - Exige **mayoría absoluta del Congreso** para su aprobación.

### 3. Estructura de la AGE (Ley 40/2015, Art. 55)
- **Órganos Superiores** (Fijan los planes de actuación):
  - **Ministros**: Jefes del departamento ministerial.
  - **Secretarios de Estado**: Dirección de sectores de actividad específicos.
  - *Nombramiento*: Libre designación política por Real Decreto (no se exige condición de funcionario).
- **Órganos Directivos** (Desarrollo y ejecución de planes):
  - **Subsecretarios** y **Secretarios Generales Técnicos**: Nombramiento por RD entre **funcionarios de carrera del Subgrupo A1**.
  - **Directores Generales**: Nombramiento por RD entre funcionarios del **Subgrupo A1** (salvo excepciones motivadas en el RD de estructura).
  - **Subdirectores Generales**: Nombramiento entre **funcionarios del Subgrupo A1** (sin excepciones).
- **Organización Territorial**:
  - **Delegados del Gobierno en las CCAA** (Rango de Subsecretario, nombrados libremente por RD).
  - **Subdelegados del Gobierno en las provincias** (Rango de Subdirector General, nombrados por el Delegado del Gobierno obligatoriamente entre **funcionarios del Subgrupo A1**).

---

## 🎯 Datos Clave para Oposiciones TAI

| Órgano / Procedimiento | Requisito / Mayoría / Rango |
|------------------------|-----------------------------|
| Primera Votación Investidura | **Mayoría Absoluta** del Congreso |
| Segunda Votación Investidura (48h) | **Mayoría Simple** |
| Plazo Bloqueo Investidura | **2 meses** (disolución de Cortes) |
| Firmas Moción de Censura | **1/10 de los Diputados (35 Diputados)** |
| Votación Moción de Censura | **Mayoría Absoluta del Congreso** tras **5 días** |
| Requisito Funcionario A1 | **Subsecretarios, SGT, Directores Generales, Subdirectores y Subdelegados del Gobierno** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/gobierno-y-age|El Gobierno y la Administración General del Estado]]
- Entidad: [[wiki/entities/ley-40-2015-lrjsp|Ley 40/2015 LRJSP]]
- Síntesis: [[wiki/synthesis/bloque1-tai-oposiciones-master-guide|Guía Maestra de Bloque 1 (TAI)]]
"""
}

print("[*] Escribiendo notas fuente ampliadas en wiki/sources/bloque1-tema01 y tema02...")
for path, content in WIKI_SOURCES.items():
    write_file(path, content)

print("[*] Fuentes iniciales generadas exitosamente.")
