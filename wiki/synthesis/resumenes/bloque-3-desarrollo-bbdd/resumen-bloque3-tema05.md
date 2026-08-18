---
title: "Resumen Exhaustivo Tema 05 (Bloque 3): Desarrollo Web Frontend (HTML5, CSS3, JavaScript ES6+)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-05
  - desarrollo
  - bbdd
  - ingenieria-software
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema05.md]]"
  - "[[wiki/sources/bloque3-tema05]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema06|Tema 06 ➡️]]

# 🔴 Resumen Exhaustivo Tema 05 (Bloque 3): Desarrollo Web Frontend (HTML5, CSS3, JavaScript ES6+)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 05**
> Estructura semántica HTML5, APIs HTML5 (Canvas, Geolocation, Web Storage), CSS3 (Modelo de cajas, Flexbox, Grid Layout, Media Queries, animaciones), JavaScript ES6+ (let/const, arrow functions, promesas, async/await, DOM, Event Bubbling) y arquitecturas SPA.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. HTML5 Semántico y Nuevas APIs
- **Elementos Semánticos**: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<figure>`, `<figcaption>`.
- **APIs Nativas HTML5**:
  - *Web Storage API*:
    - **localStorage**: Almacena datos sin fecha de caducidad (persisten tras cerrar el navegador). Capacidad típica: ~5-10 MB.
    - **sessionStorage**: Almacena datos solo durante la sesión actual de la pestaña (se borran al cerrar la pestaña).
  - *Web Workers*: Permite ejecutar scripts JavaScript en segundo plano en hilos separados sin bloquear el hilo principal de la UI.
  - *Canvas 2D / WebGL*: Renderizado gráfico bitmap mediante JavaScript vs **SVG** (vectorial basado en XML escalable sin pérdida).

### 2. CSS3: Flexbox, Grid y Diseño Responsivo
- **Modelo de Cajas (Box Model)**: `Content` $\rightarrow$ `Padding` (relleno) $\rightarrow$ `Border` (borde) $\rightarrow$ `Margin` (margen).
  - `box-sizing: border-box`: El ancho (`width`) y alto (`height`) incluyen el contenido, el padding y el borde (evita desbordamientos indeseados).
- **CSS Flexbox (Unidimensional - Filas o Columnas)**:
  - Contenedor: `display: flex`, `flex-direction: row | column`, `justify-content` (alineación eje principal), `align-items` (alineación eje transversal), `flex-wrap`.
  - Elementos: `flex-grow`, `flex-shrink`, `flex-basis`.
- **CSS Grid Layout (Bidimensional - Filas y Columnas simultáneas)**:
  - `display: grid`, `grid-template-columns: repeat(3, 1fr)`, `grid-template-rows`, `gap`, `grid-area`.

### 3. JavaScript Moderno (ES6+) y Manipulación del DOM
- **Declaración de Variables**:
  - `var`: Ámbito de función (*function scope*), permite redeclaración y sufre *hoisting*.
  - `let`: Ámbito de bloque (*block scope*), no permite redeclaración, reasignable.
  - `const`: Ámbito de bloque (*block scope*), no permite redeclaración ni reasignación (los objetos declarados con const sí son mutables en sus propiedades).
- **Asincronía en JavaScript**:
  - *Promesas (Promises)*: Objetos que representan la finalización o fracaso eventual de una operación asíncrona (estados: `Pending`, `Fulfilled/Resolved`, `Rejected`).
  - *async / await*: Azúcar sintáctico sobre promesas que permite escribir código asíncrono con sintaxis síncrona y estructurado mediante `try...catch`.
- **Event Bubbling vs Event Capturing**:
  - *Capturing (Fase de captura)*: El evento desciende desde `window` hasta el elemento objetivo.
  - *Bubbling (Fase de burbujeo - por defecto)*: El evento se propaga hacia arriba desde el elemento objetivo hasta la raíz del DOM. Método para detenerlo: `event.stopPropagation()`.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 05 (Bloque 3)**
> 1. **localStorage vs sessionStorage**: `sessionStorage` se destruye al **cerrar la pestaña/navegador**; `localStorage` nunca caduca a menos que se borre por código o usuario.
> 2. **box-sizing: border-box**: El cálculo del ancho total de la caja incluye `width = content + padding + border` (el margen queda fuera).
> 3. **Propagación de Eventos**: El modo por defecto en `addEventListener` es la fase de **burbujeo (Bubbling)**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Flexbox vs Grid**: **Flexbox $= 1D$ (1 Eje)** / **Grid $= 2D$ (Filas y Columnas)**.
> - **Estados de una Promesa**: **P - F - R** $\rightarrow$ **P**ending, **F**ulfilled, **R**ejected.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema05|Fuente Oficial del Tema 05]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema05|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema05-componentes-java-dotnet|Test Tema 05]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema06|Tema 06 ➡️]]
