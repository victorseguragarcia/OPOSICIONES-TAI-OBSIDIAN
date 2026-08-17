---
title: "Test de Autoevaluación: Bloque 2 - Tema 03 (Estructuras de Datos, Algoritmos y Ficheros)"
type: "test"
target: "wiki/sources/bloque2-tema03.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - estructuras-datos
  - arboles-avl
  - algoritmos
  - quicksort
  - big-o
sources:
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 03: Estructuras de Datos, Algoritmos y Ficheros

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---

## ❓ Preguntas

### 1. ¿Cuál es la complejidad temporal en el PEOR CASO del algoritmo de ordenación Quicksort?
- [ ] a) $O(n \log n)$
- [ ] b) $O(n^2)$
- [ ] c) $O(n)$
- [ ] d) $O(\log n)$

### 2. ¿Qué algoritmo de ordenación basado en 'Divide y Vencerás' garantiza una complejidad de $O(n \log n)$ tanto en el caso medio como en el peor caso, siendo además ESTABLE?
- [ ] a) Quicksort.
- [ ] b) Mergesort (Ordenación por mezcla).
- [ ] c) Heapsort (Ordenación por montículos).
- [ ] d) Selección directa.

### 3. En un Árbol AVL (Adelson-Velsky y Landis), ¿cuáles son los únicos valores permitidos para el factor de equilibrio ($FE = h_{izq} - h_{der}$) de cualquier nodo?
- [ ] a) Solo $0$.
- [ ] b) $\{-1, 0, +1\}$
- [ ] c) $\{-2, -1, 0, +1, +2\}$
- [ ] d) Cualquier valor positivo.

### 4. ¿Qué estructura de datos abstracta sigue una política de acceso LIFO (*Last In, First Out*)?
- [ ] a) Cola (*Queue*).
- [ ] b) Pila (*Stack*).
- [ ] c) Lista doblemente enlazada.
- [ ] d) Árbol binario de búsqueda.

### 5. En un fichero con organización secuencial indexada (ISAM / VSAM):
- [ ] a) Los registros solo pueden leerse desde el primer registro hasta el último sin acceso directo.
- [ ] b) Se dispone de una tabla de índices ordenada que permite el acceso directo a bloques de registros, manteniendo los datos ordenados secuencialmente.
- [ ] c) Los registros se dispersan mediante una función hash sin tabla de índices.
- [ ] d) Solo admite almacenamiento en cintas magnéticas.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: En Quicksort, si el pivote elegido es el menor o mayor elemento sistemáticamente (array ya ordenado sin pivote aleatorio), el árbol degenera en lista con complejidad $O(n^2)$.
> - **Pregunta 2 (b)**: Mergesort divide el array recursivamente en mitades y mezcla en tiempo lineal, garantizando $O(n \log n)$ siempre y preservando el orden relativo de elementos iguales (estable).
> - **Pregunta 3 (b)**: En AVL, la diferencia de alturas entre subárboles no puede superar 1 ($FE \in \{-1, 0, +1\}$). Si llega a $\pm 2$ se aplican rotaciones (simple o doble).
> - **Pregunta 4 (b)**: Una Pila (Stack) es LIFO (último en entrar, primero en salir con operaciones `push` y `pop`). La Cola es FIFO.
> - **Pregunta 5 (b)**: La organización secuencial indexada combina el acceso secuencial tradicional con un índice para accesos aleatorios directos rápidos.
