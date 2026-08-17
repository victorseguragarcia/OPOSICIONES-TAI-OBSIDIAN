---
title: "Test Tema 02: Lenguajes de Programación, Compiladores y Paradigmas"
type: "test"
target: "wiki/sources/bloque3-tema02-lenguajes-compiladores.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 02: Lenguajes de Programación, Compiladores y Paradigmas

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 02: Lenguajes de Programación, Compiladores y Paradigmas",
  "questions": [
    {
      "question": "¿Cuál es la fase del proceso de compilación encargada de agrupar los caracteres del código fuente en componentes léxicos o 'tokens'?",
      "options": [
        "Análisis Sintáctico (Parser).",
        "Análisis Léxico (Scanner).",
        "Análisis Semántico.",
        "Generación de código intermedio."
      ],
      "answer": "b",
      "explanation": "El análisis léxico (Scanner) lee el flujo de caracteres y produce una secuencia de tokens eliminando espacios y comentarios."
    },
    {
      "question": "¿Cuál de los siguientes paradigmas de programación se caracteriza por describir 'qué' problema se desea resolver en lugar de especificar 'cómo' resolverlo paso a paso (ej. Prolog o SQL)?",
      "options": [
        "Paradigma Imperativo.",
        "Paradigma Declarativo.",
        "Paradigma Estructurado.",
        "Paradigma Concurrente."
      ],
      "answer": "b",
      "explanation": "El paradigma declarativo (lógico como Prolog o funcional como Haskell/SQL) expresa la lógica del cómputo sin describir el flujo de control explícito."
    },
    {
      "question": "¿Qué estructura de datos genera el analizador sintáctico (parser) para representar la estructura gramatical jerárquica del programa?",
      "options": [
        "Tabla de símbolos lineal.",
        "Árbol de Sintaxis Abstracta (AST - Abstract Syntax Tree).",
        "Grafo de flujo de control.",
        "Matriz de adyacencia de estados."
      ],
      "answer": "b",
      "explanation": "El parser genera el árbol sintáctico (AST) validando que los tokens cumplan la gramática libre de contexto del lenguaje."
    },
    {
      "question": "En un lenguaje fuertemente tipado como Java o C#, ¿qué fase del compilador detecta errores de incompatibilidad de tipos (ej. sumar un String y un Objeto no convertible)?",
      "options": [
        "Análisis Léxico.",
        "Análisis Sintáctico.",
        "Análisis Semántico.",
        "Optimización de código."
      ],
      "answer": "c",
      "explanation": "El análisis semántico comprueba la coherencia de tipos, declaraciones previas de variables y concordancia de parámetros."
    },
    {
      "question": "¿Qué diferencia fundamental existe entre un compilador y un intérprete tradicional?",
      "options": [
        "El compilador traduce el código fuente completo a código máquina ejecutable antes de la ejecución; el intérprete traduce y ejecuta instrucción por instrucción en tiempo real.",
        "El compilador no detecta errores sintácticos y el intérprete sí.",
        "El intérprete genera siempre archivos ejecutables `.exe` independientes.",
        "Los lenguajes compilados no admiten depuración de código."
      ],
      "answer": "a",
      "explanation": "El compilador produce código objeto/máquina antes de ejecutarse; el intérprete procesa el código fuente línea a línea en tiempo de ejecución."
    }
  ]
}
```
