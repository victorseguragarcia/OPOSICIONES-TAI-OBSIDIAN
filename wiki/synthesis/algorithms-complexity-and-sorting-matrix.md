---
title: "Matriz Comparativa de Algoritmos de Ordenación y Complejidad Big-O"
type: "synthesis"
tags:
  - synthesis
  - algoritmos
  - ordenacion
  - complejidad
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Matriz de Algoritmos de Ordenación"
  - "Complejidad de Algoritmos"
---

# Matriz Comparativa de Algoritmos de Ordenación y Complejidad Big-O

Cuadro sinóptico de algoritmos de ordenación y búsqueda para preguntas teóricas de examen.

---

## 🏛️ Matriz Comparativa Completa

| Algoritmo | Mejor Caso | Caso Promedio | Peor Caso | Memoria Auxiliar | ¿Es Estable? | Método |
|-----------|------------|---------------|-----------|------------------|--------------|--------|
| **Burbuja (Bubble Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Intercambio |
| **Inserción (Insertion Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Inserción |
| **Selección (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Selección |
| **Quicksort (Hoare)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n^2)$** | $O(\log n)$ | No | Divide y Vencerás |
| **Mergesort (Von Neumann)**| **$O(n \log n)$** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n)$** | **Sí** | Divide y Vencerás |
| **Heapsort (Montículo)** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(1)$** | No | Selección / Heap |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación]]
