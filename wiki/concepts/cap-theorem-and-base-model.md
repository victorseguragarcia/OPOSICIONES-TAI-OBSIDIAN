---
title: "Teorema CAP de Brewer y Modelo BASE"
type: "concept"
tags:
  - teorema-cap
  - base-model
  - consistencia-eventual
  - nosql
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Teorema CAP"
  - "Modelo BASE"
---

# Teorema CAP de Brewer y Modelo BASE

Teorema fundamental de la computación distribuida formulado por Eric Brewer que demuestra la imposibilidad de garantizar simultáneamente Consistencia, Disponibilidad y Tolerancia a Particiones.

---

## 🏛️ Principios CAP y BASE

- **Teorema CAP**: Ante una partición de red ($P$), los sistemas deben priorizar **Consistencia (CP)** (ej. HBase, MongoDB, Redis) o **Disponibilidad (AP)** (ej. Cassandra, CouchDB).
- **Modelo BASE**:
  - **Basically Available**: Disponibilidad básica ante fallos.
  - **Soft State**: El estado puede cambiar por propagación interna.
  - **Eventual Consistency**: Los nodos convergen tras un tiempo determinado.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía NoSQL y Teorema CAP]]
