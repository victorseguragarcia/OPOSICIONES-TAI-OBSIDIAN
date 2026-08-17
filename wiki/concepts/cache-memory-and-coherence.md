---
title: "Memoria Caché, Principios de Localidad y Coherencia"
type: "concept"
tags:
  - cache
  - localidad-memoria
  - coherencia-cache
  - hardware
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Memoria Caché"
  - "Coherencia de Caché"
---

# Memoria Caché, Principios de Localidad y Coherencia

La memoria caché es una memoria de alta velocidad intermedia entre la CPU y la RAM principal que aprovecha el principio de localidad.

---

## 🏛️ Principios y Políticas de Caché

- **Principio de Localidad**:
  - *Temporal*: Reutilización de datos recientes (bucles).
  - *Espacial*: Acceso a datos contiguos en memoria (vectores).
- **Políticas de Escritura**:
  - *Write-Through*: Escribe simultáneamente en caché y RAM.
  - *Write-Back*: Escribe solo en caché marcando el *dirty bit*; escribe en RAM al expulsar la línea.
- **Políticas de Reemplazo**: LRU (*Least Recently Used*), FIFO, LFU, Random.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria]]
