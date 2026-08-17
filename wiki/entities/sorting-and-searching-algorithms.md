---
title: "Algoritmos de Ordenación y Búsqueda"
type: "entity"
tags:
  - algoritmos
  - ordenacion
  - busqueda
  - quicksort
  - mergesort
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Algoritmos de Ordenación"
  - "Quicksort y Mergesort"
---

# Algoritmos de Ordenación y Búsqueda

Estudio comparativo de los métodos fundamentales para organizar y localizar información en estructuras de datos.

---

## 🏛️ Matriz de Rendimiento

| Algoritmo | Tiempo Promedio | Peor Caso | Espacio Auxiliar | ¿Estabilidad? |
|-----------|-----------------|-----------|------------------|---------------|
| **Quicksort** | **$O(n \log n)$** | **$O(n^2)$** | $O(\log n)$ | No |
| **Mergesort** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n)$** | **Sí** |
| **Heapsort** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(1)$** | No |
| **Búsqueda Binaria** | **$O(\log n)$** | **$O(\log n)$** | $O(1)$ | Requiere vector ordenado |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Big-O]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Complejidad de Algoritmos]]
