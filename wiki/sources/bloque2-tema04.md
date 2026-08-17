---
title: "Resumen Fuente: Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema04
  - estructuras-datos
  - arboles-avl
  - algoritmos-ordenacion
  - big-o
sources:
  - "raw/sources/bloque2-tema04.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Estructuras de Datos y Algoritmos"
  - "bloque2-tema04"
---

# Resumen Fuente: Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema04.md|bloque2-tema04.md]].

---

## 📖 Resumen Ejecutivo

Este tema constituye la base algorítmica de la informática: las estructuras de datos lineales (**listas**, **pilas LIFO**, **colas FIFO** y colas de prioridad), las estructuras no lineales (**árboles binarios de búsqueda BST**, recorridos preorden/inorden/postorden, **árboles balanceados AVL** con rotaciones simples y dobles, **árboles B y B+**, y **grafos** con matrices/listas de adyacencia y algoritmos de caminos mínimos como **Dijkstra**), el análisis de complejidad asintótica mediante **notación Big-O**, y el estudio comparativo exhaustivo de los algoritmos de ordenación (**Quicksort**, **Mergesort**, **Heapsort**, Burbuja, Inserción y Selección) evaluando tiempo, memoria auxiliar y estabilidad.

---

## 🎯 Datos Clave para Oposiciones TAI

| Algoritmo / Estructura | Complejidad Temporal Promedio | Peor Caso | Complejidad Espacial | ¿Estable? |
|------------------------|-------------------------------|-----------|----------------------|-----------|
| **Quicksort** | **$O(n \log n)$** | **$O(n^2)$** | $O(\log n)$ | No |
| **Mergesort** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(n)$** | **Sí** |
| **Heapsort** | **$O(n \log n)$** | **$O(n \log n)$** | **$O(1)$** | No |
| **Búsqueda Binaria** | **$O(\log n)$** | **$O(\log n)$** | $O(1)$ | N/A (requiere array ordenado) |
| **Tabla Hash (Búsqueda)**| **$O(1)$** | **$O(n)$** | $O(n)$ | N/A |
| **Árbol AVL (Búsqueda/Ins)**| **$O(\log n)$** | **$O(\log n)$** | $O(n)$ | Auto-balanceado (Factor $\pm 1$) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación y Búsqueda]]
- Entidad: [[wiki/entities/data-structures-trees-and-graphs|Estructuras de Datos: Árboles y Grafos]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Computacional y Notación Big-O]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz Comparativa de Algoritmos de Ordenación]]
