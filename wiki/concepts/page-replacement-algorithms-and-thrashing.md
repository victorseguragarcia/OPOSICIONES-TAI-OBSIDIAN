---
title: "Algoritmos de Reemplazo de Páginas e Hiperpaginación (Thrashing)"
type: "concept"
tags:
  - memoria-virtual
  - paginacion
  - lru
  - fifo
  - belady
  - thrashing
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Reemplazo de Páginas y Thrashing"
  - "Hiperpaginación"
---

# Algoritmos de Reemplazo de Páginas e Hiperpaginación (Thrashing)

Políticas de desalojo de páginas en memoria física cuando ocurre un fallo de página y no existen marcos libres disponibles.

---

## 🏛️ Anomalía de Belady e Hiperpaginación
- **Anomalía de Belady**: Fenómeno en el algoritmo **FIFO** donde aumentar el número de marcos asignados provoca más fallos de página.
- **Hiperpaginación (*Thrashing*)**: Condición crítica donde los procesos pasan la mayor parte del tiempo paginando entre disco y RAM debido a falta de marcos en su *Working Set*.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual y Paginación]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual]]
