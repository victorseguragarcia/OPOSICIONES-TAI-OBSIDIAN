---
title: "Cheatsheet: Árboles, Complejidad Big-O y Organización de Ficheros (Bloque II)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-2
  - arboles-avl
  - b-trees
  - ficheros
  - big-o
sources:
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Árboles y Ficheros Cheatsheet"
  - "Estructuras de Datos TAI"
---

# 🔴 Cheatsheet: Árboles, Complejidad Big-O y Organización de Ficheros

Resumen de conceptos de árboles balanceados, árboles B y organización física de ficheros para examen.

---

## 🌳 1. Tipos de Árboles en Informática

| Tipo de Árbol | Definición y Propiedades | Factor de Equilibrio / Reglas | Complejidad Búsqueda |
|:---|:---|:---|:---:|
| **Árbol Binario de Búsqueda (ABB)** | Para todo nodo $N$, claves del subárbol izquierdo $< N <$ claves del subárbol derecho. | No balanceado. Puede degenerar en lista lineal. | $O(\log n)$ medio / $O(n)$ peor |
| **Árbol AVL** | ABB estrictamente autobalanceado en altura. | $FE = h_{izq} - h_{der} \in \{-1, 0, +1\}$. Rotaciones simples (LL, RR) o dobles (LR, RL). | **$O(\log n)$ garantizado** |
| **Árbol B (Orden $m$)** | Árbol multicamino balanceado para almacenamiento secundario (disco). | Cada nodo (salvo raíz) tiene al menos $\lceil m/2 ceil$ hijos y máximo $m$ hijos. Todas las hojas en el mismo nivel. | **$O(\log_m n)$** |
| **Árbol B+** | Variante donde **todos los datos se almacenan exclusivamente en las hojas**; los nodos internos solo contienen claves de índice. Las hojas están unidas en lista enlazada secuencial. | Ideal para bases de datos relacionales y sistemas de ficheros (permite barridos secuenciales rápidos por rango). | **$O(\log_m n)$** |

---

## 📁 2. Modos de Organización de Ficheros

| Modo de Organización | Acceso Soportado | Soporte Físico | Ventajas | Desventajas |
|:---|:---:|:---:|:---|:---|
| **Secuencial** | Solo Secuencial | Cintas y Discos | Compacto, sin sobrecarga de punteros. | Búsqueda lenta ($O(n)$), inserción costosa. |
| **Directa / Relativa (Hash)** | Directo por clave | Solo Disco | Acceso inmediato en $O(1)$. | No permite listados ordenados eficientes. Colisiones hash. |
| **Secuencial Indexada (ISAM/VSAM)** | Secuencial y Directo | Solo Disco | Permite tanto búsquedas puntuales como listados por rango. | Sobrecarga de espacio para índices y necesidad de reorganización. |
