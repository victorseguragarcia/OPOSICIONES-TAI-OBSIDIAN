---
title: "Formas Normales, Dependencias Funcionales y Descomposición Relacional"
type: "concept"
tags:
  - normalizacion
  - formas-normales
  - dependencias-funcionales
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Formas Normales"
  - "Teoría de la Normalización"
---

# Formas Normales, Dependencias Funcionales y Descomposición Relacional

El proceso de normalización organiza los atributos y relaciones de una base de datos relacional para **evitar la redundancia de datos, anomalías de inserción/borrado/modificación y garantizar la integridad referencial**.

---

## 🏛️ Jerarquía de Formas Normales

$$	ext{1FN} \subset 	ext{2FN} \subset 	ext{3FN} \subset 	ext{BCNF} \subset 	ext{4FN} \subset 	ext{5FN}$$

- **1FN**: Atributos con valores atómicos indivisibles.
- **2FN**: 1FN + sin dependencias parciales de claves primarias compuestas.
- **3FN**: 2FN + sin dependencias transitivas entre atributos no clave.
- **BCNF**: Todo determinante en una dependencia funcional es clave candidata.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado Relacional]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
