---
title: "Modelado de Datos Relacional, Modelo E/R y Formas Normales"
type: "entity"
tags:
  - modelado-datos
  - bases-datos
  - modelo-er
  - normalizacion
  - sql
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelado Relacional"
  - "Modelo Entidad-Relación"
  - "Normalización"
---

# Modelado de Datos Relacional, Modelo E/R y Formas Normales

Metodología de diseño conceptual, lógico y físico de bases de datos relacionales basada en el modelo Entidad-Relación de Chen y las reglas de normalización de Codd.

---

## 🏛️ Fases de Diseño y Formas Normales

1. **1FN (Primera Forma Normal)**: Todos los valores de los atributos son **atómicos** e indivisibles (sin campos multivaluados ni arrays).
2. **2FN (Segunda Forma Normal)**: Cumple 1FN y todos los atributos no clave dependen funcionalmente de **toda la clave primaria** (sin dependencias parciales de partes de una PK compuesta).
3. **3FN (Tercera Forma Normal)**: Cumple 2FN y **no existen dependencias funcionales transitivas** entre atributos no clave ($X ightarrow Y ightarrow Z$).
4. **BCNF (Forma Normal de Boyce-Codd)**: Para cada dependencia funcional $X ightarrow Y$, $X$ debe ser **superclave / clave candidata**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
