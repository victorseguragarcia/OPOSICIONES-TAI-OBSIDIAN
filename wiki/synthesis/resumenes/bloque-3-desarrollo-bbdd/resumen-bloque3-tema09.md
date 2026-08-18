---
title: "Resumen Exhaustivo Tema 09 (Bloque 3): Metodología MÉTRICA Versión 3, Complejidad de McCabe y QA"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-09
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema09.md]]"
  - "[[wiki/sources/bloque3-tema09]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema08|⬅️ Tema 08]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏁 Fin de Bloque 3 ➡️]]

# 🔴 Resumen Exhaustivo Tema 09 (Bloque 3): Metodología MÉTRICA Versión 3, Complejidad de McCabe y QA

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 09**
> Estructura de MÉTRICA Versión 3 (Procesos Principales PSI, EVS, DSI, CSI, IAS y Procesos de Soporte), técnicas y modelos (DFD, Diagramas de Clases, Modelo E/R), tipos de pruebas de software (Unitarias, Integración, Sistema, Aceptación, Regresión), métricas de calidad y Complejidad Ciclomática de Thomas McCabe.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Metodología MÉTRICA Versión 3 (Consejo Superior de Administración Electrónica)
- **Estructura de Procesos Principales del Ciclo de Vida**:
  1. **PSI (Planificación de Sistemas de Información)**: Define el marco estratégico global y la arquitectura tecnológica.
  2. **EVS (Estudio de Viabilidad del Sistema)**: Analiza las necesidades del cliente y evalúa las alternativas técnicas y económicas para seleccionar una solución viable.
  3. **DSI (Análisis y Diseño del Sistema de Información)**:
     - *Análisis del Sistema (ASI)*: Obtención y especificación formal de requisitos funcionales y no funcionales (enfoque estructurado con DFD/Diccionario de datos o enfoque orientado a objetos con Casos de Uso/UML).
     - *Diseño del Sistema (DSI)*: Arquitectura técnica, diseño detallado de módulos, pantallas y modelo físico de BBDD.
  4. **CSI (Construcción del Sistema de Información)**: Codificación de programas, desarrollo de componentes y ejecución de las pruebas unitarias y de integración.
  5. **IAS (Implantación y Aceptación del Sistema)**: Entrega, despliegue, migración de datos, formación a usuarios y **Pruebas de Aceptación**.
  6. **MSI (Mantenimiento del Sistema de Información)**: Correctivo, Evolutivo, Perfectivo y Adaptativo.

### 2. Tipos de Pruebas de Software (Testing)

| Nivel de Prueba | Objetivo y Alcance | Responsable Principal |
|:---|:---|:---|
| **Pruebas Unitarias** | Verifican el correcto funcionamiento de módulos, clases o funciones individuales aisladas (pruebas de caja blanca con JUnit, NUnit, Mockito). | **Desarrolladores** |
| **Pruebas de Integración** | Verifican las interfaces y la comunicación correcta entre módulos combinados (enfoques Top-Down con *Stubs* o Bottom-Up con *Drivers*). | Equipo de desarrollo / QA |
| **Pruebas de Sistema** | Verifican el sistema completo e integrado respecto a los requisitos globales funcionales y no funcionales (rendimiento, carga, estrés, seguridad). | Equipo independiente de **QA** |
| **Pruebas de Aceptación** | Verifican que el sistema cumple los criterios de negocio y necesidades reales del cliente antes de la puesta en producción (Alfa/Beta). | **Usuarios Finales / Cliente** |
| **Pruebas de Regresión** | Se ejecutan tras cualquier cambio o corrección de bugs para asegurar que lo que antes funcionaba no se ha roto. | Automatización CI/CD |

### 3. Complejidad Ciclomática de Thomas McCabe
- **Definición**: Métrica de calidad de software que mide la complejidad lógica cuantitativa de un programa basándose en su grafo de flujo de control ($G$). Representa el **número mínimo de caminos independientes** que deben probarse para garantizar cobertura completa de sentencias.
- **Fórmulas de Cálculo de McCabe**:
  $$\text{Complejidad Ciclomática } V(G) = E - N + 2P$$
  $$\text{O bien: } V(G) = D + 1 \quad (\text{para } P=1)$$
  $$\text{O bien: } V(G) = R \quad (\text{número de regiones cerradas más la región abierta del grafo plano})$$
  - Donde:
    - $E = \text{Número de aristas (Edges/Arcos)}$.
    - $N = \text{Número de nodos (Nodes/Vértices)}$.
    - $P = \text{Número de componentes conexos (habitualmente } P=1 \text{ para un programa principal)}$.
    - $D = \text{Número de nodos predicados/decisión (condicionales tipo } \text{if, while, for, case})$.
- **Interpretación del Valor $V(G)$**:
  - $1 - 10$: Programa simple, bajo riesgo, alta mantenibilidad y testabilidad.
  - $11 - 20$: Complejidad moderada, riesgo moderado.
  - $21 - 50$: Programa complejo, alto riesgo.
  - $> 50$: Programa muy complejo, inestable, prácticamente intratable e imposible de probar adecuadamente.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 09 (Bloque 3)**
> 1. **Fórmula de McCabe**: $V(G) = E - N + 2P$ (los distractores suelen invertir los signos: $N - E + 2P$ o $E - N + P$).
> 2. **Cálculo rápido por Nodos de Decisión**: $V(G) = \text{Nodos de Decisión} + 1$.
> 3. **Pruebas de Aceptación en MÉTRICA V3**: Se realizan formalmente durante el proceso **IAS (Implantación y Aceptación del Sistema)** y las firman los usuarios.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Procesos MÉTRICA V3**: **PSI - EVS - DSI - CSI - IAS - MSI**.
> - **Fórmula McCabe**: **E - N + 2** ($E$ aristas menos $N$ nodos más 2).

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema09|Fuente Oficial del Tema 09]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema09|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema09-metodologias-qa-git|Test Tema 09]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema08|⬅️ Tema 08]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏁 Fin de Bloque 3 ➡️]]
