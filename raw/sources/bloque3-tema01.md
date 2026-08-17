---
title: "Bloque 3 - Tema 01: Ciclo de Vida del Software, Metodologías Ágiles y MÉTRICA Versión 3"
type: "raw-source"
topic: "ciclo-de-vida-metrica3"
date: "2026-08-17"
---

# Bloque 3 - Tema 01: Modelos de Ciclo de Vida, Metodologías de Desarrollo (Tradicionales y Ágiles) y MÉTRICA Versión 3

## 1. Modelos del Ciclo de Vida del Software
- **Modelo en Cascada Clásico (Royce, 1970)**: Secuencial y rígido. Fases: Análisis de requisitos $\rightarrow$ Diseño $\rightarrow$ Implementación $\rightarrow$ Pruebas $\rightarrow$ Despliegue y Mantenimiento. No permite retroceso fácil; los errores de requisitos se detectan muy tarde.
- **Modelo en V (Verificación y Validación)**: Establece una correspondencia directa y simétrica entre cada fase de desarrollo y su correspondiente fase de pruebas (Requisitos $\leftrightarrow$ Pruebas de Aceptación, Diseño General $\leftrightarrow$ Pruebas de Sistema, Diseño Detallado $\leftrightarrow$ Pruebas de Integración, Codificación $\leftrightarrow$ Pruebas Unitarias).
- **Modelo Prototipado**: Construcción rápida de maquetas y prototipos interactivos para clarificar requisitos ambiguos con el usuario.
- **Modelo en Espiral (Boehm, 1986)**: Ciclo iterativo guiado por el **análisis y gestión de riesgos**. Cuatro cuadrantes por ciclo: 1. Fijar objetivos y alternativas $\rightarrow$ 2. Análisis y evaluación de riesgos $\rightarrow$ 3. Desarrollo y verificación del producto $\rightarrow$ 4. Planificación de la siguiente iteración.

## 2. Metodologías Ágiles
Basadas en el **Manifiesto Ágil (2001)**: Valora a los individuos y sus interacciones sobre los procesos y herramientas; software funcionando sobre documentación exhaustiva; colaboración con el cliente sobre negociación contractual; y respuesta al cambio sobre seguimiento de un plan.
- **Scrum**:
  - **Roles**: **Product Owner (PO)** (representa al negocio y prioriza el Product Backlog), **Scrum Master (SM)** (líder servicial que elimina impedimentos y vela por el marco Scrum) y **Developers / Equipo de Desarrollo** (autoorganizado y multifuncional).
  - **Artefactos**: **Product Backlog** (lista priorizada de requisitos/historias de usuario), **Sprint Backlog** (tareas seleccionadas para el Sprint) e **Incremento** (software potencialmente desplegable que cumple la *Definition of Done* - DoD).
  - **Eventos**: **Sprint** (contenedor de 1 a 4 semanas), **Sprint Planning** (planificación del trabajo), **Daily Scrum** (reunión diaria de sincronización de 15 minutos), **Sprint Review** (demostración del incremento al PO y *stakeholders*) y **Sprint Retrospective** (mejora continua del equipo).
- **Kanban**: Sistema visual de gestión de flujo de trabajo basado en tableros. Principios: visualización del flujo, **límite del trabajo en curso (WIP - Work In Progress)** y optimización del *Lead Time* y *Cycle Time*.
- **eXtreme Programming (XP - Kent Beck)**: Enfatiza la excelencia técnica. Prácticas: Programación en Parejas (*Pair Programming*), Desarrollo Guiado por Pruebas (**TDD - Test-Driven Development**), Integración Continua, Refactorización constante, Propiedad colectiva del código y entregas pequeñas (*small releases*).

## 3. Metodología MÉTRICA Versión 3 (MÉTRICA v3)
Metodología oficial de desarrollo de sistemas de información del Ministerio de Administraciones Públicas (MAP / actual Ministerio de Transformación Digital y Función Pública) para las Administraciones Públicas españolas. Abarca tanto el enfoque Estructurado como el Orientado a Objetos.

### Estructura de Procesos de MÉTRICA v3:
1. **Planificación de Sistemas de Información (PSI)**:
   - Objetivo: Definir el marco estratégico y la arquitectura global de sistemas de información que dé soporte a los objetivos de la organización.
   - Actividades: Iniciación del PSI, Definición de requisitos, Estudio de sistemas de información actuales, Diseño de la arquitectura de información, Selección de la arquitectura tecnológica y Plan de proyectos.
2. **Estudio de Viabilidad del Sistema (EVS)**:
   - Objetivo: Analizar las necesidades del negocio para proponer alternativas de solución técnica y organizativa, evaluando su viabilidad económica, técnica, legal y operativa.
   - Actividades: Establecimiento del alcance del sistema, Estudio de la situación actual, Definición de requisitos del sistema, Estudio de alternativas de solución, Valoración de alternativas y Selección de la solución.
3. **Análisis del Sistema de Información (ASI)**:
   - Objetivo: Obtener la especificación detallada del sistema (modelo lógico de datos y procesos o modelo de clases y casos de uso).
   - Actividades: Definición del sistema, Establecimiento de requisitos, Identificación de subsistemas, Análisis de casos de uso / procesos y Elaboración del modelo de datos / clases.
4. **Diseño del Sistema de Información (DSI)**:
   - Objetivo: Diseñar la arquitectura física del sistema, módulos, interfaces de usuario y esquemas de base de datos relacional u OO.
   - Actividades: Definición de la arquitectura tecnológica, Diseño de la arquitectura de soporte, Diseño de casos de uso / módulos, Diseño de la base de datos, Diseño de interfaces de usuario y Plan de pruebas.
5. **Construcción del Sistema de Información (CSI)**:
   - Objetivo: Codificación de componentes, generación del esquema físico de BD, ejecución de pruebas unitarias, pruebas de integración y pruebas del sistema, y elaboración de manuales (usuario y explotación).
6. **Implantación y Aceptación del Sistema (IAS)**:
   - Objetivo: Puesta en producción del sistema, migración y carga inicial de datos, formación de usuarios y pruebas de aceptación final por parte del cliente.

### Procesos de Soporte / Interfaces de MÉTRICA v3:
- **Gestión de Proyectos (GP)**.
- **Seguridad (SEG)** (alineada con Magerit y el Esquema Nacional de Seguridad).
- **Garantía de Calidad (GC)** (aseguramiento de la calidad de procesos y productos).
- **Gestión de la Configuración (GCF)**.
