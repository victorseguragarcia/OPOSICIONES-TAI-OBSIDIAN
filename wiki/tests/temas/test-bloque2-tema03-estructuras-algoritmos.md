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

# 🔴 Test de Autoevaluación: Bloque 2 - Tema 03 (Estructuras de Datos, Algoritmos y Ficheros)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 2 - Tema 03 (Estructuras de Datos, Algoritmos y Ficheros)",
  "questions": [
    {
      "question": "¿Cuál es la complejidad temporal en el PEOR CASO del algoritmo de ordenación Quicksort?",
      "options": [
        "$O(n \\log n)$",
        "$O(n^2)$",
        "$O(n)$",
        "$O(\\log n)$"
      ],
      "answer": "b",
      "explanation": "En Quicksort, si el pivote elegido es el menor o mayor elemento sistemáticamente (array ya ordenado sin pivote aleatorio), el árbol degenera en lista con complejidad $O(n^2)$."
    },
    {
      "question": "¿Qué algoritmo de ordenación basado en 'Divide y Vencerás' garantiza una complejidad de $O(n \\log n)$ tanto en el caso medio como en el peor caso, siendo además ESTABLE?",
      "options": [
        "Quicksort.",
        "Mergesort (Ordenación por mezcla).",
        "Heapsort (Ordenación por montículos).",
        "Selección directa."
      ],
      "answer": "b",
      "explanation": "Mergesort divide el array recursivamente en mitades y mezcla en tiempo lineal, garantizando $O(n \\log n)$ siempre y preservando el orden relativo de elementos iguales (estable)."
    },
    {
      "question": "En un Árbol AVL (Adelson-Velsky y Landis), ¿cuáles son los únicos valores permitidos para el factor de equilibrio ($FE = h_{izq} - h_{der}$) de cualquier nodo?",
      "options": [
        "Solo $0$.",
        "$\\{-1, 0, +1\\}$",
        "$\\{-2, -1, 0, +1, +2\\}$",
        "Cualquier valor positivo."
      ],
      "answer": "b",
      "explanation": "En AVL, la diferencia de alturas entre subárboles no puede superar 1 ($FE \\in \\{-1, 0, +1\\}$). Si llega a $\\pm 2$ se aplican rotaciones (simple o doble)."
    },
    {
      "question": "¿Qué estructura de datos abstracta sigue una política de acceso LIFO (*Last In, First Out*)?",
      "options": [
        "Cola (*Queue*).",
        "Pila (*Stack*).",
        "Lista doblemente enlazada.",
        "Árbol binario de búsqueda."
      ],
      "answer": "b",
      "explanation": "Una Pila (Stack) es LIFO (último en entrar, primero en salir con operaciones `push` y `pop`). La Cola es FIFO."
    },
    {
      "question": "En un fichero con organización secuencial indexada (ISAM / VSAM):",
      "options": [
        "Los registros solo pueden leerse desde el primer registro hasta el último sin acceso directo.",
        "Se dispone de una tabla de índices ordenada que permite el acceso directo a bloques de registros, manteniendo los datos ordenados secuencialmente.",
        "Los registros se dispersan mediante una función hash sin tabla de índices.",
        "Solo admite almacenamiento en cintas magnéticas."
      ],
      "answer": "b",
      "explanation": "La organización secuencial indexada combina el acceso secuencial tradicional con un índice para accesos aleatorios directos rápidos."
    }
  ]
}
```
