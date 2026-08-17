---
title: "Memoria Virtual, Paginación, Segmentación y Algoritmos de Reemplazo"
type: "entity"
tags:
  - sistemas-operativos
  - memoria-virtual
  - paginacion
  - tlb
  - belady
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Memoria Virtual y Paginación"
  - "Paginación y Reemplazo de Páginas"
---

# Memoria Virtual, Paginación, Segmentación y Algoritmos de Reemplazo

Mecanismo que permite a los programas ejecutar con un espacio de direccionamiento lógico mayor que la memoria física real mediante el intercambio de páginas entre RAM y almacenamiento secundario.

---

## 🏛️ Componentes y Algoritmos de Reemplazo

- **Páginas y Marcos**: Páginas lógicas de tamaño fijo ($4	ext{ KB}$) mapeadas a marcos físicos mediante la **Tabla de Páginas** y aceleradas por la **TLB**.
- **Algoritmos de Reemplazo**: **FIFO** (sufre la anomalía de Belady), **LRU** (menos recientemente usada), **Óptimo de Belady** y **Reloj** (segunda oportunidad).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/page-replacement-algorithms-and-thrashing|Algoritmos de Reemplazo de Páginas e Hiperpaginación]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual y Paginación]]
