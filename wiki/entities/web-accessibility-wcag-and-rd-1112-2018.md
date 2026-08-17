---
title: "Accesibilidad Web: Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018"
type: "entity"
tags:
  - accesibilidad-web
  - wcag
  - pour
  - rd-1112-2018
  - en-301-549
  - administracion-publica
sources:
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Accesibilidad Web Oficial"
  - "WCAG y RD 1112/2018"
---

# Accesibilidad Web: Pautas WCAG 2.1/2.2, Norma EN 301 549 y Real Decreto 1112/2018

Marco normativo y técnico de obligado cumplimiento para garantizar la accesibilidad universal en todos los entornos digitales de las Administraciones Públicas españolas.

---

## 👁️ 1. Los 4 Principios POUR (WCAG 2.1 / 2.2)

1. **Perceptible**: La información y los componentes de la interfaz deben presentarse de forma que los usuarios puedan percibirlos con sus sentidos.
   - Alternativas textuales para contenido no textual (`alt`, `aria-label`).
   - Medios temporales: Subtítulos y audiodescripciones.
   - **Ratio de Contraste Nivel AA**: Mínimo **4.5:1** para texto normal y **3:1** para texto grande ($\ge 18	ext{pt}$ o $\ge 14	ext{pt}$ negrita) y componentes gráficos/UI.
2. **Operable**: Los componentes de navegación e interacción deben ser manejables.
   - **Accesibilidad total por teclado** (sin requerir ratón y sin trampas de foco).
   - Tiempo suficiente para leer y usar el contenido (mecanismos de pausa/ampliación).
   - No diseñar contenido que provoque convulsiones o reacciones físicas (evitar destellos $> 3	ext{ Hz}$).
3. **Comprensible**: La información y el manejo de la interfaz deben ser comprensibles y predecibles.
   - Idioma de la página declarado en HTML (`<html lang="es">`).
   - Navegación e identificación coherentes y predecibles.
   - Asistencia a la entrada de datos: Detección y sugerencia automática de corrección de errores en formularios.
4. **Robusto**: El contenido debe ser lo suficientemente robusto como para ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluidas las tecnologías de asistencia (lectores de pantalla NVDA, JAWS, VoiceOver).
   - Código HTML válido y estandarizado.
   - Uso correcto de especificaciones **WAI-ARIA** (`role`, `aria-expanded`, `aria-hidden`).

---

## 🏛️ 2. Exigencias Legales del Real Decreto 1112/2018 en España

- **Ámbito Subjetivo**: Obliga a la Administración General del Estado, CCAA, Entidades Locales y organismos públicos vinculados o dependientes.
- **Nivel de Conformidad Exigido**: **Nivel AA** (alineado con la norma europea **EN 301 549**).
- **Obligaciones Esenciales**:
  1. **Declaración de Accesibilidad**: Publicada en formato accesible en cada sede electrónica, portal web y aplicación móvil, actualizada anualmente.
  2. **Unidad Responsable de Accesibilidad (URA)**: Cada organismo público debe designar formalmente una URA encargada de garantizar el cumplimiento y canalizar las quejas.
  3. **Mecanismo de Comunicación y Reclamación**: Canal habilitado para consultas ciudadanas sobre accesibilidad.
  4. **Plazo Legal de Respuesta**: Plazo máximo de **20 días hábiles** para responder a quejas y solicitudes de información accesible.
  5. **Informes de Seguimiento**: Informes periódicos cada **3 años** remitidos a la Comisión Europea.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema08|Resumen Bloque 3 - Tema 08]]
- Síntesis: [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet de Principios POUR y RD 1112/2018]]
