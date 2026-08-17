---
title: "Test Tema 07: Aplicaciones Web, HTML5, CSS3, DOM y JavaScript"
type: "test"
target: "wiki/sources/bloque3-tema07-aplicaciones-web-frontend.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 07: Aplicaciones Web, HTML5, CSS3, DOM y JavaScript

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 07: Aplicaciones Web, HTML5, CSS3, DOM y JavaScript",
  "questions": [
    {
      "question": "En JavaScript (ECMAScript 6+), ¿cuál es la diferencia fundamental entre declarar una variable con `let` y con `var`?",
      "options": [
        "`let` tiene ámbito de bloque (*block scope*) y no permite redeclaración en el mismo ámbito; `var` tiene ámbito de función (*function scope*) y sufre de *hoisting*.",
        "`let` solo permite almacenar valores constantes inmutables.",
        "`var` no permite almacenar cadenas de texto.",
        "`let` solo puede utilizarse en el lado del servidor con Node.js."
      ],
      "answer": "a",
      "explanation": "`let` y `const` introducen ámbito de bloque en ES6, evitando problemas de alcance de `var`."
    },
    {
      "question": "¿Qué objeto de la API estándar de JavaScript moderna se utiliza para realizar peticiones HTTP asíncronas basadas en Promesas sustituyendo a XMLHttpRequest?",
      "options": [
        "API Fetch (`fetch()`).",
        "Web Workers.",
        "WebSocket.",
        "Service Worker."
      ],
      "answer": "a",
      "explanation": "La API Fetch proporciona una interfaz moderna basada en Promesas (`fetch(url).then(...)` o `await fetch(url)`) para peticiones HTTP."
    },
    {
      "question": "En HTML5, ¿qué mecanismo de almacenamiento local en el navegador permite guardar datos clave-valor de forma persistente SIN fecha de caducidad que sobreviven al cierre del navegador?",
      "options": [
        "`sessionStorage`",
        "`localStorage`",
        "`IndexedDB` exclusivamente en memoria.",
        "Cookies de sesión."
      ],
      "answer": "b",
      "explanation": "`localStorage` almacena datos en el cliente sin expiración; `sessionStorage` se borra al cerrar la pestaña o ventana."
    },
    {
      "question": "En CSS3, ¿qué modelo de maquetación unidimensional distribuye el espacio y alinea elementos a lo largo de un eje principal (fila o columna)?",
      "options": [
        "CSS Grid Layout.",
        "CSS Flexbox (Flexible Box Layout).",
        "CSS Float.",
        "CSS Positioning."
      ],
      "answer": "b",
      "explanation": "Flexbox es un sistema de diseño unidimensional (1D: fila o columna); CSS Grid es bidimensional (2D: filas y columnas simultáneas)."
    },
    {
      "question": "En el DOM (Document Object Model), ¿qué método estándar de JavaScript selecciona el PRIMER elemento que coincide con un selector CSS especificado?",
      "options": [
        "`document.getElementById()`",
        "`document.querySelector()`",
        "`document.getElementsByClassName()`",
        "`document.getElementsByTagName()`"
      ],
      "answer": "b",
      "explanation": "`document.querySelector()` devuelve el primer elemento coincidente con cualquier selector CSS (ej. `#id`, `.clase`, `div > p`)."
    }
  ]
}
```
