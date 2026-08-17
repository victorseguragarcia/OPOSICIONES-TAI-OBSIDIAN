---
title: "Diagramas UML 2.x y Lenguaje de Modelado"
type: "entity"
tags:
  - uml
  - modelado
  - poo
  - diagramas
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "UML"
  - "Diagramas UML"
---

# Diagramas UML 2.x y Lenguaje de Modelado

Estándar de la OMG (Object Management Group) para la especificación, visualización y documentación de artefactos de software orientado a objetos.

---

## 🏛️ Clasificación de Diagramas en UML 2.x

1. **Diagramas Estructurales (Estáticos)**:
   - **Diagrama de Clases**: Clases, interfaces, relaciones de asociación, agregación ($\diamondsuit$), composición ($lacklozenge$) y generalización/herencia ($artriangle$).
   - **Diagrama de Componentes**: Módulos ejecutables y dependencias.
   - **Diagrama de Despliegue**: Asignación de artefactos de software sobre nodos físicos de hardware.
   - **Diagrama de Objetos**, **Paquetes** y **Estructura Compuesta**.
2. **Diagramas de Comportamiento (Dinámicos)**:
   - **Diagrama de Casos de Uso**: Actores y casos de uso con relaciones `<<include>>` (obligatoria) y `<<extend>>` (opcional con condición).
   - **Diagrama de Secuencia**: Interacción temporal entre objetos mediante líneas de vida.
   - **Diagrama de Actividades**: Flujos de trabajo con bifurcaciones y barras *fork/join*.
   - **Diagrama de Máquina de Estados**: Estados y transiciones disparadas por eventos.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones GoF]]
