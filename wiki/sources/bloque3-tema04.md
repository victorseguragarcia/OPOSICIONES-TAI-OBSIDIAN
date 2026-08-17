---
title: "Resumen Fuente: Bloque 3 - Tema 04 (UD012111): POO, Patrones de Diseño GoF y UML"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema04
  - poo
  - solid
  - patrones-gof
  - uml
sources:
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen POO, Patrones GoF y UML"
  - "bloque3-tema04"
---

# Resumen Fuente: Bloque 3 - Tema 04 (UD012111): POO, Patrones de Diseño GoF y UML

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema04-poo-patrones-uml.md|bloque3-tema04-poo-patrones-uml.md]] (68 páginas).

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el diseño orientado a objetos: los pilares de la POO (abstracción, encapsulamiento, herencia y polimorfismo con ligadura dinámica), los principios **SOLID**, el lenguaje de modelado **UML 2.x** distinguiendo diagramas estructurales (clases, objetos, componentes, despliegue, paquetes) y de comportamiento (casos de uso con `<<include>>` obligatoria y `<<extend>>` opcional, secuencia, actividades, estados), y el catálogo de **23 Patrones de Diseño GoF** clasificados en Creacionales (Singleton, Factory Method, Abstract Factory, Builder, Prototype), Estructurales (Adapter, Composite, Decorator, Facade, Proxy, Bridge, Flyweight) y de Comportamiento (Observer, Strategy, Command, Template Method, Iterator, State).

---

## 🎯 Datos Clave para Oposiciones TAI

| Patrón / Diagrama UML | Categoría / Definición de Examen |
|-----------------------|----------------------------------|
| **Singleton** | Creacional: Garantiza una **única instancia** con punto de acceso global |
| **Factory Method** | Creacional: Delega la instanciación de objetos en las subclases |
| **Adapter** | Estructural: **Convierte la interfaz** de una clase en otra esperada por el cliente |
| **Decorator** | Estructural: **Añade responsabilidades dinámicamente** sin modificar la clase |
| **Observer** | Comportamiento: Dependencia 1 a N donde el cambio de estado del sujeto notifica a observadores |
| **Strategy** | Comportamiento: Encapsula una familia de algoritmos haciéndolos intercambiables |
| **UML `<<include>>` vs `<<extend>>`** | `<<include>>`: Ejecución **obligatoria** \| `<<extend>>`: Ejecución **opcional / condicional** |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/uml-diagrams-and-modeling|Diagramas UML 2.x y Modelado]]
- Entidad: [[wiki/entities/gof-design-patterns|Patrones de Diseño GoF (Gang of Four)]]
- Síntesis: [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet de Patrones de Diseño GoF]]
