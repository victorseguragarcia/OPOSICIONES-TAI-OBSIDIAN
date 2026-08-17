---
title: "Resumen Fuente: Bloque 3 - Tema 02: Análisis y Diseño OO, UML 2.x y Patrones de Diseño GoF"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema02
  - uml
  - patrones-diseno
  - gof
  - solid
  - poo
sources:
  - "raw/sources/bloque3-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen UML y Patrones GoF"
  - "bloque3-tema02"
---

# Resumen Fuente: Bloque 3 - Tema 02: Análisis y Diseño OO, UML 2.x y Patrones de Diseño GoF

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema02.md|bloque3-tema02.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el diseño orientado a objetos: los pilares de la POO (abstracción, encapsulamiento, herencia y polimorfismo con ligadura dinámica) y los **principios SOLID**, el estándar de modelado **UML 2.x** con su doble división entre diagramas estructurales (clases con relaciones de asociación, agregación $\diamondsuit$, composición $lacklozenge$, generalización $artriangle$; componentes, despliegue, paquetes) y diagramas de comportamiento (casos de uso con `<<include>>` y `<<extend>>`, secuencia con líneas de vida, actividades, máquinas de estados), y el catálogo completo de los 23 patrones de diseño **Gang of Four (GoF)** clasificados en Creacionales, Estructurales y de Comportamiento.

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Diagrama UML | Categoría / Definición de Examen |
|-----------------------|----------------------------------|
| **Singleton** | Creacional: Garantiza una **única instancia** con punto de acceso global |
| **Factory Method / Abstract Factory** | Creacional: Creación de objetos o familias de objetos mediante interfaces polimórficas |
| **Adapter** | Estructural: **Convierte la interfaz** de una clase en otra esperada por el cliente |
| **Composite** | Estructural: Jerarquías parte-todo (árboles) tratando a hojas y compuestos uniformemente |
| **Decorator** | Estructural: Añade responsabilidades dinámicamente sin modificar la clase original |
| **Facade** | Estructural: Interfaz simplificada y de alto nivel a un subsistema complejo |
| **Observer** | Comportamiento: Dependencia 1 a N donde el cambio de estado del sujeto notifica a observadores |
| **Strategy** | Comportamiento: Encapsula una familia de algoritmos haciéndolos intercambiables en ejecución |
| **UML `<<include>>` vs `<<extend>>`** | `<<include>>`: Ejecución **obligatoria** \| `<<extend>>`: Ejecución **opcional / condicional** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/uml-diagrams-and-modeling|Diagramas UML 2.x y Modelado]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones de Diseño GoF (Gang of Four)]]
- Síntesis: [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones de Diseño GoF]]
