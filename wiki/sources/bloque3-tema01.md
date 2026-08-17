---
title: "Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo E/R y Normalización"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema01
  - modelado-datos
  - modelo-er
  - normalizacion
  - formas-normales
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Modelado de Datos y Normalización"
  - "bloque3-tema01"
---

# Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo Entidad-Relación y Normalización

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema01-modelado-datos-bbdd.md|bloque3-tema01-modelado-datos-bbdd.md]] (90 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en las fases de diseño de bases de datos (Conceptual, Lógico y Físico): el **Modelo Entidad-Relación (E/R de Peter Chen)** (entidades fuertes y débiles, atributos simples/compuestos/multivaluados/derivados, relaciones 1:1, 1:N, M:N, cardinalidades mínimas y máximas), las reglas de transformación del modelo conceptual al **Modelo Lógico Relacional de Codd** (tablas, tuplas, atributos, dominios, claves primarias PK y foráneas FK, integridad de entidad e integridad referencial), y la **Teoría de la Normalización** (Dependencias Funcionales, 1FN, 2FN, 3FN, Forma Normal de Boyce-Codd BCNF, 4FN con dependencias multivaluadas y 5FN con dependencias de unión).

---

## 🎯 Datos Clave para Oposiciones TAI

| Fase / Regla | Concepto / Fórmula de Examen |
|--------------|------------------------------|
| **Fases de Diseño BBDD** | 1. **Conceptual** (Modelo E/R) $ightarrow$ 2. **Lógico** (Relacional) $ightarrow$ 3. **Físico** (Tablas, índices y archivos) |
| **Primera Forma Normal (1FN)** | Todos los atributos son **atómicos** (valores indivisibles, sin grupos repetitivos) |
| **Segunda Forma Normal (2FN)** | Está en 1FN y todo atributo no clave tiene **dependencia funcional completa** de la PK (sin dependencias parciales) |
| **Tercera Forma Normal (3FN)** | Está en 2FN y **no existen dependencias transitivas** entre atributos no clave ($X ightarrow Y ightarrow Z$) |
| **Forma Normal de Boyce-Codd (BCNF)** | Para toda dependencia funcional $X ightarrow Y$, $X$ es **superclave / clave candidata** |
| **Integridad Referencial** | Toda clave foránea (FK) debe coincidir con un valor de clave primaria (PK) existente o ser nula |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado de Datos Relacional y Normalización]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias Funcionales]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]
