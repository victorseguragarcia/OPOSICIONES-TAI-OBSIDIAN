---
title: "Bloque 3 - Tema 06: Accesibilidad Web, WCAG 2.1/2.2, EN 301 549 y RD 1112/2018"
type: "raw-source"
topic: "accesibilidad-wcag-rd1112"
date: "2026-08-17"
---

# Bloque 3 - Tema 06: Accesibilidad Web y Usabilidad, Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018

## 1. Concepto de Accesibilidad Web y W3C / WAI
La accesibilidad web implica que personas con discapacidad puedan percibir, entender, navegar e interactuar con la web, aportando al mismo tiempo contenidos. Desarrollada por la iniciativa **WAI (Web Accessibility Initiative)** del consorcio **W3C**.

## 2. Pautas de Accesibilidad para el Contenido Web (WCAG 2.1 / 2.2)
Las pautas WCAG se estructuran en **4 Principios Fundamentales (Acrónimo POUR)**:
1. **Perceptible**: La información y los componentes de la interfaz de usuario deben presentarse a los usuarios de modo que puedan percibirlos.
   - *Alternativas textuales* para contenido no textual (imágenes con atributo `alt`).
   - *Subtítulos y audiodescripción* para contenido multimedia temporal.
   - *Adaptable*: Contenido estructurado semánticamente (etiquetas HTML5 `header`, `nav`, `main`, `footer`, encabezados `h1-h6`).
   - *Distinguible*: Contraste de color adecuado (mínimo ratio **4.5:1** para texto normal y **3:1** para texto grande en nivel AA), tamaño de texto ajustable sin pérdida de contenido, y no usar el color como único medio visual.
2. **Operable**: Los componentes de la interfaz de usuario y la navegación deben ser manejables.
   - *Accesible por teclado*: Toda la funcionalidad disponible mediante teclado sin trampas de foco.
   - *Tiempo suficiente*: Permitir al usuario ajustar o desactivar límites de tiempo.
   - *Ataques y convulsiones*: No diseñar contenido que parpadee más de 3 veces por segundo.
   - *Navegable*: Enlaces con propósito claro, orden de foco lógico, mecanismos para saltar bloques repetitivos (*skip links*) y múltiples vías para localizar páginas.
   - *Modalidades de entrada*: Soporte para gestos táctiles simples sin movimientos complejos.
3. **Comprensible**: La información y el manejo de la interfaz de usuario deben ser comprensibles.
   - *Legible*: Declaración del idioma principal de la página (`<html lang="es">`).
   - *Predecible*: Las páginas operan de forma predecible sin cambios de contexto automáticos al recibir el foco.
   - *Ayuda a la entrada de datos*: Identificación y descripción clara de errores en formularios, sugerencias de corrección y confirmación previa en envíos legales o financieros.
4. **Robusto**: El contenido debe ser suficientemente robusto para ser interpretado de forma fiable por una amplia variedad de aplicaciones de usuario, incluidas las tecnologías de asistencia (lectores de pantalla como NVDA o JAWS).
   - Marcado HTML válido, elementos con etiquetas de inicio y fin correctas y soporte de atributos **WAI-ARIA** (`role`, `aria-label`, `aria-expanded`).

### Niveles de Conformidad WCAG:
- **Nivel A**: Requisitos mínimos básicos indispensables.
- **Nivel AA**: Nivel estándar exigido internacional y legalmente para administraciones públicas y sitios corporativos.
- **Nivel AAA**: Máximo nivel de accesibilidad especializada.

## 3. Marco Normativo de Accesibilidad en el Sector Público
- **Estándar Europeo EN 301 549**: Norma europea sobre requisitos de accesibilidad adecuados para la contratación pública de productos y servicios TIC en Europa (adopta los criterios de WCAG 2.1 nivel AA).
- **Real Decreto 1112/2018, de 7 de septiembre**: Sobre accesibilidad de los sitios web y aplicaciones para dispositivos móviles del sector público (transposición de la Directiva UE 2016/2102).
  - **Ámbito de Aplicación**: Toda la Administración Pública española (AGE, CCAA, Entidades Locales), organismos públicos, universidades públicas y empresas que gestionen servicios públicos.
  - **Nivel de Exigencia**: Obliga al cumplimiento del **Nivel AA de las WCAG** (mediante la norma EN 301 549).
  - **Obligaciones Principales**:
    - Publicar una **Declaración de Accesibilidad** periódicamente actualizada en cada sitio web y app móvil.
    - Establecer un **Mecanismo de Comunicación** para que los ciudadanos puedan presentar sugerencias, quejas y reclamaciones sobre accesibilidad.
    - Designar una **Unidad Responsable de Accesibilidad (URA)** encargada de garantizar el cumplimiento y remitir informes periódicos de seguimiento al Ministerio.
    - Revisiones periódicas de accesibilidad obligatorias (autoevaluaciones y auditorías externas).
