---
title: "Bloque 2 - Tema 04: Estructuras de Datos, Algoritmos de Ordenación y Complejidad Big-O"
type: "raw-source"
topic: "estructuras-datos-algoritmos"
date: "2026-08-17"
---

# Bloque 2 - Tema 04: Estructuras de Datos Lineales y No Lineales, Algoritmos de Ordenación y Búsqueda, y Complejidad Computacional

## 1. Estructuras de Datos Lineales
- **Listas Enlazadas**: Colección de nodos donde cada nodo contiene un dato y uno o más punteros al siguiente (simple) o anterior y siguiente (doblemente enlazada). Inserción y borrado en $O(1)$ con puntero; acceso aleatorio en $O(n)$.
- **Pilas (Stacks - LIFO: Last In, First Out)**: Inserción y extracción se realizan exclusivamente por el mismo extremo (la cima / *top*). Operaciones elementales: `push` (apilar) y `pop` (desapilar) en $O(1)$. Aplicaciones: gestión de llamadas a funciones (pila de llamadas), evaluación de expresiones en notación polaca inversa (RPN), algoritmos de *backtracking*.
- **Colas (Queues - FIFO: First In, First Out)**: Inserción por el final (*rear/tail*) y extracción por el frente (*front/head*). Operaciones: `enqueue` (encolar) y `dequeue` (desencolar) en $O(1)$. Aplicaciones: colas de impresión, planificación de procesos CPU (Round Robin), buffers de E/S.
- **Colas de Prioridad (Priority Queues)**: Los elementos se extraen según su nivel de prioridad, implementadas típicamente mediante montículos binarios (*Heaps*).

## 2. Estructuras de Datos No Lineales
- **Árboles Binarios**: Estructura jerárquica donde cada nodo tiene a lo sumo dos hijos (izquierdo y derecho).
  - **Árbol Binario de Búsqueda (BST - Binary Search Tree)**: Para cada nodo $X$, todos los elementos de su subárbol izquierdo son menores que $X$, y todos los de su subárbol derecho son mayores que $X$. Búsqueda, inserción y borrado promedio en $O(\log n)$, pero degrada a $O(n)$ si está desbalanceado (árbol degenerado en lista).
  - **Recorridos de Árboles**:
    - *Preorden*: Raíz $\rightarrow$ Izquierda $\rightarrow$ Derecha.
    - *Inorden*: Izquierda $\rightarrow$ Raíz $\rightarrow$ Derecha (produce la secuencia ordenada en un BST).
    - *Postorden*: Izquierda $\rightarrow$ Derecha $\rightarrow$ Raíz.
    - *Por Niveles (Anchura / BFS)*: Nivel 0, nivel 1, nivel 2...
  - **Árboles Balanceados AVL**: Árbol BST auto-balanceable donde para cada nodo la diferencia de altura entre sus subárboles izquierdo y derecho (factor de equilibrio) es a lo sumo $\pm 1$. Restablece el equilibrio mediante **rotaciones simples (LL, RR)** o **rotaciones dobles (LR, RL)**. Garantiza operaciones en $O(\log n)$ en el peor caso.
  - **Árboles B y B+**: Árboles multicamino balanceados de orden $M$. Cada nodo puede contener múltiples claves y múltiples hijos. Diseñados para sistemas de archivos y motores de bases de datos relacionales para minimizar accesos a disco. En el árbol B+, todos los datos se almacenan exclusivamente en las hojas enlazadas secuencialmente.
- **Grafos**: Conjunto de vértices (nodos) y aristas (relaciones).
  - Tipos: Dirigidos (Dígrafos), No dirigidos, Ponderados/Valorados.
  - Representaciones: **Matriz de Adyacencia** (espacio $O(V^2)$, eficiente para grafos densos) y **Lista de Adyacencia** (espacio $O(V+E)$, eficiente para grafos dispersos).
  - Algoritmos: Búsqueda en Anchura (BFS con cola), Búsqueda en Profundidad (DFS con pila/recursión), Camino Mínimo (**Dijkstra** para aristas con pesos positivos en $O((V+E)\log V)$, Bellman-Ford para aristas con pesos negativos) y Árbol de Recubrimiento Mínimo (Kruskal, Prim).

## 3. Algoritmos de Ordenación y Complejidad Big-O

| Algoritmo de Ordenación | Mejor Caso | Caso Promedio | Peor Caso | Complejidad Espacial | ¿Estable? | Técnica Algorítmica |
|-------------------------|------------|---------------|-----------|----------------------|-----------|---------------------|
| **Burbuja (Bubble Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Intercambio |
| **Inserción (Insertion Sort)** | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | **Sí** | Inserción directa |
| **Selección (Selection Sort)** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | No | Selección |
| **Quicksort (Hoare)** | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$* | $O(\log n)$ | No | Divide y Vencerás |
| **Mergesort (Von Neumann)** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **Sí** | Divide y Vencerás |
| **Heapsort (Williams)** | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | No | Selección sobre Montículo |

*\*El peor caso de Quicksort ($O(n^2)$) ocurre cuando el pivote seleccionado es sistemáticamente el elemento mínimo o máximo (ej. lista ya ordenada sin pivote aleatorio).*

## 4. Algoritmos de Búsqueda
- **Búsqueda Secuencial / Lineal**: Recorre el vector elemento a elemento. Complejidad: Mejor caso $O(1)$, promedio y peor caso $O(n)$. Funciona sobre listas desordenadas.
- **Búsqueda Binaria / Dicotómica**: Requiere que el vector esté **previamente ordenado**. Compara con el elemento central y descarta la mitad del vector en cada paso. Complejidad: Mejor caso $O(1)$, promedio y peor caso **$O(\log n)$**.
- **Búsqueda por Dispersión (Hashing)**: Aplica una función hash $h(K)$ sobre la clave para obtener la dirección directa del índice en la tabla hash. Acceso en **$O(1)$ caso promedio**; degrada a $O(n)$ en el peor caso de colisiones masivas. Métodos de resolución de colisiones: encadenamiento separado (listas enlazadas) y direccionamiento abierto (sondeo lineal, cuadrático o doble hashing).
