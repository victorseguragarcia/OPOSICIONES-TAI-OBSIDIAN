---
title: "Complejidad Computacional y Notación Asintótica Big-O"
type: "concept"
tags:
  - complejidad-algoritmica
  - big-o
  - algoritmos
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Notación Big-O"
  - "Complejidad Asintótica"
---

# Complejidad Computacional y Notación Asintótica Big-O

La notación asintótica describe el comportamiento del tiempo de ejecución y el consumo de memoria de un algoritmo a medida que el tamaño de entrada $n$ tiende a infinito.

---

## 🏛️ Jerarquía de Complejidades (de Mejor a Peor)

$$O(1) < O(\log n) < O(n) < O(n \log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)$$

- **$O(1)$ Constante**: Acceso a vector por índice, `push`/`pop` en pila.
- **$O(\log n)$ Logarítmica**: Búsqueda binaria, operaciones en árbol AVL.
- **$O(n)$ Lineal**: Búsqueda secuencial, recorrido de lista enlazada.
- **$O(n \log n)$ Cuasi-lineal**: Mergesort, Heapsort, Quicksort promedio (límite teórico de ordenación por comparaciones).
- **$O(n^2)$ Cuadrática**: Ordenación por burbuja, selección o inserción.
- **$O(2^n)$ Exponencial**: Torres de Hanoi, subconjuntos.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación]]
