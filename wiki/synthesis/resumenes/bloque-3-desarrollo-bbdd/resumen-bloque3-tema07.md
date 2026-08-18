---
title: "Resumen Exhaustivo Tema 07 (Bloque 3): Accesibilidad Web (WCAG 2.1 POUR y RD 1112/2018 Nivel AA)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-07
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema07.md]]"
  - "[[wiki/sources/bloque3-tema07]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema06|⬅️ Tema 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema08|Tema 08 ➡️]]

# 🔴 Resumen Exhaustivo Tema 07 (Bloque 3): Accesibilidad Web (WCAG 2.1 POUR y RD 1112/2018 Nivel AA)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 07**
> Iniciativa WAI del W3C, pautas WCAG 2.1, los 4 principios de accesibilidad POUR (Perceptible, Operable, Comprensible, Robusto), los 3 niveles de conformidad (A, AA, AAA), Real Decreto 1112/2018 para el sector público en España, declaración de accesibilidad y herramientas de validación.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Pautas WCAG 2.1 y los Cuatro Principios POUR
- **Iniciativa WAI (Web Accessibility Initiative)** del W3C: Define las directrices **WCAG 2.1** (Web Content Accessibility Guidelines) estructuradas en **4 principios fundamentales (POUR)**:

| Principio WCAG | Nombre Oficial | Significado y Requisitos Clave de Examen |
|:---|:---|:---|
| **P** | **Perceptible** | La información y los componentes de la interfaz deben ser presentados a los usuarios de modo que puedan percibirlos (no pueden ser invisibles a todos sus sentidos).<br>• Alternativas textuales para contenido no textual (`alt` en imágenes).<br>• Subtítulos y audiodescripción en multimedia.<br>• Contraste mínimo de color entre texto y fondo. |
| **O** | **Operable** | Los componentes de la interfaz y la navegación deben ser operables por cualquier usuario.<br>• **Accesibilidad total mediante teclado** (sin trampas de foco).<br>• Tiempo suficiente para leer y usar el contenido.<br>• No diseñar contenido que pueda provocar ataques epilépticos (máx. 3 destellos por segundo).<br>• Ayudas para la navegación y enlaces claros. |
| **U** | **Understandable (Comprensible)** | La información y el manejo de la interfaz de usuario deben ser comprensibles.<br>• Texto legible y comprensible (idioma de la página declarado con atributo `lang`).<br>• Páginas predecibles en aspecto y funcionamiento.<br>• Ayuda a la introducción de datos y prevención/corrección de errores en formularios. |
| **R** | **Robust (Robusto)** | El contenido debe ser suficientemente robusto como para ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluyendo tecnologías de asistencia (lectores de pantalla NVDA, JAWS).<br>• Marcado HTML válido y compatible con ARIA (Accessible Rich Internet Applications). |

### 2. Niveles de Conformidad y Requisitos de Contraste de Color

| Nivel de Conformidad | Descripción y Alcance | Contraste de Color Texto Normal | Contraste de Color Texto Grande ($\ge 18\text{pt}$ o $\ge 14\text{pt}$ negrita) |
|:---|:---|:---:|:---:|
| **Nivel A** | Requisitos básicos imprescindibles de accesibilidad web. | Requisitos mínimos | Requisitos mínimos |
| **Nivel AA** | **Nivel legalmente exigible para el Sector Público** en la UE y España. | **Mínimo 4.5:1** | **Mínimo 3:1** |
| **Nivel AAA** | Máximo nivel de accesibilidad especializada. | **Mínimo 7:1** | **Mínimo 4.5:1** |

### 3. Marco Normativo Español: Real Decreto 1112/2018
- **Ámbito de Aplicación**: Todos los sitios web y aplicaciones para dispositivos móviles del **Sector Público** (AGE, CCAA, Entidades Locales, Universidades y empresas públicas).
- **Exigencia Legal**: Cumplimiento obligatorio del **NIVEL AA de las WCAG 2.1** (norma europea armonizada **EN 301 549**).
- **Obligaciones Periódicas**:
  - Publicación y mantenimiento de una **Declaración de Accesibilidad** periódicamente revisada.
  - Mecanismo de comunicación para que los usuarios reporten incumplimientos o soliciten información accesible.
  - Designación de una **Unidad Responsable de Accesibilidad (URA)** en cada departamento ministerial o entidad pública.
  - Informes anuales de seguimiento ante el Ministerio de Asuntos Económicos y Transformación Digital.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 07 (Bloque 3)**
> 1. **Nivel Legal Exigido en España (RD 1112/2018)**: Es el **NIVEL AA** (no el nivel A ni el AAA).
> 2. **Ratios de Contraste en Nivel AA**: Para texto normal es **4.5:1**; para texto grande es **3:1**.
> 3. **Los 4 Principios WCAG**: Son **POUR** (Perceptible, Operable, Comprensible/Understandable, Robusto). Los distractores suelen poner *"Usable"*, *"Accesible"* o *"Navegable"*.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Principios WCAG**: **POUR** $\rightarrow$ **P**erceptible, **O**perable, **U**nderstandable, **R**obust.
> - **Contraste Nivel AA**: **4.5 a 1 (normal) / 3 a 1 (grande)**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema07|Fuente Oficial del Tema 07]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema07|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema07-aplicaciones-web-frontend|Test Tema 07]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema06|⬅️ Tema 06]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema08|Tema 08 ➡️]]
