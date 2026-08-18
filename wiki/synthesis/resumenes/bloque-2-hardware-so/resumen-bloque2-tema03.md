---
title: "Resumen Exhaustivo Tema 03 (Bloque 2): Estructuras de Datos, Árboles y Algoritmos (AVL, B+, Big-O)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-2
  - tema-03
  - hardware
  - sistemas-operativos
  - bbdd\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema03.md]]"
  - "[[wiki/sources/bloque2-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema04|Tema 04 ➡️]]

# 🔴 Resumen Exhaustivo Tema 03 (Bloque 2): Estructuras de Datos, Árboles y Algoritmos (AVL, B+, Big-O)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 03**
> Estructuras lineales (arrays, listas enlazadas simples/dobles/circulares, pilas LIFO, colas FIFO), tablas Hash (funciones hash, resolución de colisiones por encadenamiento y direccionamiento abierto), árboles binarios de búsqueda (BST), árboles balanceados AVL (rotaciones LL, RR, LR, RL), árboles B y B+ (multicamino para índices en disco), grafos (representaciones, algoritmos de caminos mínimos Dijkstra, Bellman-Ford y árboles de recubrimiento Kruskal, Prim), algoritmos de ordenación (QuickSort, MergeSort, HeapSort) y análisis de complejidad asintótica (Notación Big-O).

---

## 🟣 1. Desarrollo Técnico y Arquitectónico Exhaustivo

### 1. Estructuras de Datos Lineales y Tablas Hash
- **Estructuras Lineales**:
  - *Arrays (Vectores)*: Elementos contiguos en memoria con acceso indexado en tiempo constante $O(1)$. Inserción/borrado en posiciones intermedias $O(n)$.
  - *Listas Enlazadas*: Nodos con punteros. Simples, Doblemente enlazadas y Circulares. Inserción/borrado al inicio $O(1)$; búsqueda secuencial $O(n)$.
  - *Pilas (Stacks)*: Estructura **LIFO (Last In, First Out)**. Operaciones principales: `push` (apilar), `pop` (desapilar), `peek/top` en $O(1)$. Usadas en gestión de llamadas a funciones, recursión y evaluación de expresiones postfijas (RPN).
  - *Colas (Queues)*: Estructura **FIFO (First In, First Out)**. Operaciones principales: `enqueue` (encolar por el final) y `dequeue` (desencolar por el frente) en $O(1)$. Usadas en planificadores de CPU y buffers de impresión. *Colas de Prioridad* (implementadas con Heaps).
- **Tablas Hash (Tablas de Dispersión)**:
  - Asocian claves a valores mediante una función resumen $h(k) = k \pmod m$. Búsqueda, inserción y borrado promedio en tiempo constante **$O(1)$** (en el peor caso de colisiones degenera a $O(n)$).
  - *Resolución de Colisiones*:
    - **Encadenamiento Separado (Chaining)**: Cada posición de la tabla contiene una lista enlazada con todos los elementos colisionados.
    - **Direccionamiento Abierto (Open Addressing)**: Todos los elementos se almacenan en la propia tabla. *Sondeo Lineal* ($h(k, i) = (h'(k) + i) \pmod m$), *Sondeo Cuadrático* ($h(k, i) = (h'(k) + c_1 i + c_2 i^2) \pmod m$) y *Doble Hashing* ($h(k, i) = (h_1(k) + i \cdot h_2(k)) \pmod m$).

### 2. Estructuras Jerárquicas: Árboles y Árboles Balanceados
- **Árbol Binario de Búsqueda (BST)**: Para cada nodo, todos los elementos del subárbol izquierdo son menores y los del subárbol derecho son mayores.
  - *Recorridos*: **Preorden** (Raíz $
ightarrow$ Izq $
ightarrow$ Der), **Inorden** (Izq $
ightarrow$ Raíz $
ightarrow$ Der, **produce la secuencia ordenada de elementos**), **Postorden** (Izq $
ightarrow$ Der $
ightarrow$ Raíz).
- **Árboles AVL (Adelson-Velsky y Landis)**:
  - Árbol BST auto-balanceado donde el **Factor de Equilibrio ($FE = \text{altura}(H_{der}) - \text{altura}(H_{izq})$)** de cualquier nodo debe pertenecer al conjunto $\{-1, 0, +1\}$.
  - Operaciones de reequilibrio mediante **Rotaciones**:
    - **Rotación Simple a la Izquierda (RR)**: Desequilibrio $+2$ por inserción en el subárbol derecho del hijo derecho.
    - **Rotación Simple a la Derecha (LL)**: Desequilibrio $-2$ por inserción en el subárbol izquierdo del hijo izquierdo.
    - **Rotación Doble Izquierda-Derecha (LR)**: Rotación simple izquierda al hijo izquierdo + rotación simple derecha al nodo desequilibrado.
    - **Rotación Doble Derecha-Izquierda (RL)**: Rotación simple derecha al hijo derecho + rotación simple izquierda al nodo desequilibrado.
  - Altura garantizada $O(\log n)$; búsqueda, inserción y borrado en tiempo **$O(\log n)$**.
- **Árboles B y Árboles B+ (Árboles Multicamino Balanceados)**:
  - Optimizados para **sistemas de ficheros y motores de bases de datos relacionales** (acceso a almacenamiento en disco en bloques).
  - *Árbol B de orden $M$*: Cada nodo tiene como máximo $M$ hijos y $M-1$ claves. Todos los nodos hojas se encuentran exactamente en el mismo nivel.
  - *Diferencia Crítica con Árbol B+*: En el **Árbol B+**, las claves intermedias solo actúan como índices guía; **TODOS los datos completos se almacenan exclusivamente en los nodos hoja**, y las hojas están **enlazadas secuencialmente como una lista doblemente enlazada**, permitiendo recorridos por rango ultra eficientes.

### 3. Grafos y Algoritmos Fundamentales
- **Representación**: Matriz de Adyacencia (espacio $O(V^2)$, eficiente para grafos densos) vs Listas de Adyacencia (espacio $O(V+E)$, eficiente para grafos dispersos).
- **Algoritmos Clásicos**:
  - *Caminos Mínimos desde un Origen*:
    - **Algoritmo de Dijkstra**: Caminos mínimos con pesos no negativos utilizando cola de prioridad ($O((V + E) \log V)$).
    - **Algoritmo de Bellman-Ford**: Admite pesos negativos y detecta ciclos negativos ($O(V \cdot E)$).
  - *Árbol de Recubrimiento Mínimo (MST - Minimum Spanning Tree)*:
    - **Algoritmo de Kruskal**: Algoritmo voraz (*greedy*) basado en ordenar aristas y usar conjuntos disjuntos (*Union-Find*) para evitar ciclos ($O(E \log E)$).
    - **Algoritmo de Prim**: Algoritmo voraz que crece desde un nodo inicial añadiendo la arista más barata adyacente ($O(E \log V)$).

### 4. Algoritmos de Ordenación y Complejidad Asintótica (Big-O)

| Algoritmo de Ordenación | Complejidad Mejor Caso | Complejidad Caso Promedio | Complejidad Peor Caso | Complejidad Espacial | ¿Es Estable? | Características Clave |
|:---|:---:|:---:|:---:|:---:|:---:|:---|
| **Burbuja (Bubble Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Intercambios adyacentes continuos. Ineficiente. |
| **Inserción (Insertion Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **SÍ** | Muy rápido para listas pequeñas o casi ordenadas. |
| **Selección (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ❌ NO | Busca el mínimo y lo intercambia. Siempre $O(n^2)$. |
| **MergeSort (Fusión)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n \log n)$** | **$O(n)$** | **SÍ** | Divide y Vencerás. Rendimiento garantizado a costa de memoria extra. |
| **QuickSort (Rápido)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n^2)$** | $O(\log n)$ | ❌ NO | Divide y Vencerás con pivote. Peor caso si el pivote es el extremo en lista ya ordenada. |
| **HeapSort (Montículos)** | $O(n \log n)$ | $O(n \log n)$ | **$O(n \log n)$** | **$O(1)$** | ❌ NO | Utiliza un Max-Heap. $O(n \log n)$ en el peor caso sin requerir memoria auxiliar. |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 03 (Bloque 2)**
> 1. **Recorrido Inorden en un BST**: Es el único recorrido que visita los nodos en **estricto orden ascendente/ordenado**.
> 2. **Árbol B vs Árbol B+**: En el árbol B los datos están repartidos en todos los nodos; en el **Árbol B+ los datos están EXCLUSIVAMENTE en las hojas** y éstas están unidas por una lista enlazada.
> 3. **Peor caso de QuickSort**: Es **$O(n^2)$**, ocurre cuando la lista ya está ordenada y se elige sistemáticamente como pivote el primer o último elemento.
> 4. **Estabilidad en Algoritmos de Ordenación**: Un algoritmo es estable si conserva el orden relativo original de elementos con claves iguales (MergeSort e InsertionSort son estables; QuickSort y HeapSort NO lo son).

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Inorden BST**: **I-R-D = ORDENADO** (Izquierda, Raíz, Derecha).
> - **Complejidades Peor Caso**: **MergeSort y HeapSort SIEMPRE $O(n \log n)$** / **QuickSort PEOR CASO $O(n^2)$**.
> - **Factor de Equilibrio AVL**: **$\{-1, 0, +1\}$**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque2-tema03|Fuente Oficial del Tema 03]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema03-estructuras-algoritmos|Test Tema 03]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque 2**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema04|Tema 04 ➡️]]
