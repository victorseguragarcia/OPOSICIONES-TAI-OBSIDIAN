---
title: "Resumen Fuente: Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Algoritmos"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema03
  - estructuras-datos
  - arboles-avl
  - grafos
  - algoritmos-ordenacion
  - organizacion-ficheros
  - big-o
sources:
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Estructuras de Datos y Ficheros"
  - "bloque2-tema03"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 03 (DOCUMENTO3): Tipos y Estructuras de Datos, Organización de Ficheros y Algoritmos

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md|bloque2-tema03-estructuras-ficheros-algoritmos.md]] (99 páginas).

---

## 📖 1. Estructuras de Datos Lineales y No Lineales

- **Estructuras Lineales**:
  - **Arrays (Vectores/Matrices)**: Colección contigua en memoria con acceso aleatorio en tiempo constante $O(1)$.
  - **Listas Enlazadas**: Nodos enlazados por punteros (simples, dobles, circulares). Inserción/borrado en $O(1)$ conocida la posición; búsqueda en $O(n)$.
  - **Pilas (Stack - LIFO)**: *Last-In, First-Out*. Operaciones `push`, `pop`, `peek` en $O(1)$.
  - **Colas (Queue - FIFO)**: *First-In, First-Out*. Operaciones `enqueue`, `dequeue` en $O(1)$.
- **Estructuras No Lineales**:
  - **Árboles Binarios de Búsqueda (BST)**: El subárbol izquierdo contiene valores menores y el derecho mayores. Búsqueda en promedio $O(\log n)$, peor caso $O(n)$ si está desbalanceado.
  - **Árboles AVL**: BST auto-balanceados donde la diferencia de alturas entre subárboles (Factor de Equilibrio $FE = h_d - h_i$) pertenece a $\{-1, 0, +1\}$. Balanceo mediante 4 tipos de rotaciones: Simple Izquierda (LL), Simple Derecha (RR), Doble Izquierda-Derecha (LR) y Doble Derecha-Izquierda (RL). Búsqueda garantizada en $O(\log n)$.
  - **Árboles B / B+**: Árboles multicamino balanceados diseñados para almacenamiento secundario e índices de bases de datos.
  - **Grafos**: Nodos (Vértices) y Aristas (dirigidas o no dirigidas, ponderadas). Representación mediante **Matriz de Adyacencia** (espacio $O(V^2)$, eficiente para grafos densos) o **Listas de Adyacencia** (espacio $O(V + E)$, eficiente para grafos dispersos).

---

## 🟣 2. Complejidad Algorítmica y Algoritmos de Ordenación

| Algoritmo | Mejor Caso | Caso Medio | Peor Caso | Complejidad Espacial | Estable | Método / Estrategia |
|-----------|------------|------------|-----------|----------------------|---------|---------------------|
| **Burbuja (Bubble Sort)** | $O(n)$ (optimizado) | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Intercambio directo |
| **Inserción Directa** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Inserción ordenada |
| **Selección Directa** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | NO | Búsqueda del mínimo |
| **Quicksort** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ (pivote malo) | $O(\log n)$ | NO | Divide y Vencerás (partición) |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **SÍ** | Divide y Vencerás (mezcla) |
| **Heapsort** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | NO | Estructura Montículo (*Heap*) |
| **Búsqueda Lineal** | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | - | Recorrido secuencial |
| **Búsqueda Binaria** | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | - | Divide y Vencerás (requiere array ordenado) |

---

## 🔵 3. Tipos y Métodos de Organización de Ficheros

- **Estructura**: Registros lógicos (unidad de información de la aplicación) agrupados en **registros físicos o bloques** (unidad de transferencia de E/S con factor de bloqueo $FB = \text{Tamaño Bloque} / \text{Tamaño Registro}$).
- **Métodos de Organización**:
  1. **Secuencial**: Los registros se graban uno tras otro. Búsqueda secuencial $O(n)$. Rápido para procesamiento por lotes (*batch*); ineficiente para acceso aleatorio.
  2. **Secuencial Encadenado**: Los registros se enlazan mediante punteros físicos.
  3. **Secuencial Indexado (ISAM)**: Área de datos secuencial + Área de índices ordenada por clave + Área de desbordamiento (*overflow*). Permite acceso tanto secuencial como directo en $O(\log n)$.
  4. **Directa / Aleatoria (Hash / Direccionamiento Calculado)**: La posición física en disco se calcula mediante una función matemática de dispersión $H(\text{clave})$.
     - **Resolución de Colisiones**: Direccionamiento abierto (prueba lineal/cuadrática, doble hashing) o encadenamiento separado en listas.

---

## 🎯 Datos Clave para Oposiciones TAI

| Pregunta / Concepto | Respuesta / Especificación |
|---------------------|---------------------------|
| **Factor de Equilibrio AVL** | $FE = \text{Altura(Derecho)} - \text{Altura(Izquierdo)} \in \{-1, 0, +1\}$ |
| **Peor caso de Quicksort** | **$O(n^2)$** cuando el array está ordenado y se elige el primer/último elemento como pivote |
| **Algoritmo de ordenación con $O(n \log n)$ garantizado y estable** | **Mergesort** (a costa de $O(n)$ de memoria auxiliar) |
| **Condición de Búsqueda Binaria** | La colección debe estar previamente **ordenada** y permitir **acceso aleatorio** ($O(1)$). |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/data-structures-trees-and-graphs|Estructuras de Datos: Árboles AVL, B-Trees y Grafos]]
- Entidad: [[wiki/entities/sorting-and-searching-algorithms|Algoritmos de Ordenación, Búsqueda y Complejidad]]
- Concepto: [[wiki/concepts/computational-complexity-and-big-o|Complejidad Computacional y Notación Big-O]]
- Concepto: [[wiki/concepts/file-organization-and-access-methods|Organización y Métodos de Acceso a Ficheros]]
- Síntesis: [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Algoritmos de Ordenación y Complejidad]]
