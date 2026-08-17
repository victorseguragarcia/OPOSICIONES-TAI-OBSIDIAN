---
title: "Guía Maestra de Bloque 3: Desarrollo de Sistemas, Metodologías, BBDD y Software (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-3
  - oposiciones
  - tai
  - metrica-v3
  - uml
  - patrones-diseno
  - normalizacion
  - java
  - dotnet
  - web
  - qa
  - git
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
  - "raw/sources/bloque3-tema04-poo-patrones-uml.md"
  - "raw/sources/bloque3-tema05-componentes-javaee-dotnet.md"
  - "raw/sources/bloque3-tema06-arquitecturas-servicios-web.md"
  - "raw/sources/bloque3-tema07-front-html5-css-js.md"
  - "raw/sources/bloque3-tema08-accesibilidad-usabilidad-seguridad.md"
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 3"
  - "Bloque 3 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 3: Desarrollo de Sistemas, Metodologías, BBDD y Software (TAI)

Compendio estructurado de estudio para el **Bloque 3**, abarcando el ciclo de vida del software, bases de datos relacionales, POO, patrones GoF, plataformas Java/.NET, arquitecturas web y testing.

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 3 (9 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis y Supuestos |
|:---|:---|:---|:---|:---|
| **Tema 01** | Modelado de Datos y Normalización | [[wiki/sources/bloque3-tema01|Resumen Tema 01]] | [[wiki/entities/relational-database-modeling-and-normalization|Modelado E/R y Formas Normales]] | [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet Normalización]], [[wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd|Supuesto Normalización]] |
| **Tema 02** | Lenguajes, Compiladores y Chomsky | [[wiki/sources/bloque3-tema02|Resumen Tema 02]] | [[wiki/entities/programming-languages-and-compilers|Compiladores y Chomsky]] | [[wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion|Supuesto Código Java/PHP]] |
| **Tema 03** | SQL ANSI, DDL, DML y Procedimientos | [[wiki/sources/bloque3-tema03|Resumen Tema 03]] | [[wiki/entities/sql-ansi-and-stored-procedures|SQL ANSI y Transacciones]] | [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet SQL]] |
| **Tema 04** | POO, Patrones GoF y Diagramas UML | [[wiki/sources/bloque3-tema04|Resumen Tema 04]] | [[wiki/entities/gof-design-patterns|Patrones GoF]], [[wiki/entities/uml-diagrams-and-modeling|UML 2.x]] | [[wiki/synthesis/gof-design-patterns-cheatsheet|Cheatsheet Patrones GoF]] |
| **Tema 05** | Plataformas Java EE y Microsoft .NET | [[wiki/sources/bloque3-tema05|Resumen Tema 05]] | [[wiki/entities/java-platform-and-jvm|Java / JVM]], [[wiki/entities/dotnet-framework-and-clr|CLR / .NET]] | [[wiki/synthesis/java-ee-vs-dotnet-comparison-guide|Comparativa Java vs .NET]] |
| **Tema 06** | Arquitecturas Web, REST y SOAP | [[wiki/sources/bloque3-tema06|Resumen Tema 06]] | [[wiki/entities/rest-and-soap-web-services|REST y SOAP]] | [[wiki/synthesis/rest-vs-soap-comparison-guide|Comparativa REST vs SOAP]] |
| **Tema 07** | Tecnologías Front: HTML5, CSS y JS | [[wiki/sources/bloque3-tema07|Resumen Tema 07]] | [[wiki/entities/web-technologies-html5-css-javascript|HTML5, CSS3, ES6+]] | Semántica Web y DOM |
| **Tema 08** | Accesibilidad WCAG y RD 1112/2018 | [[wiki/sources/bloque3-tema08|Resumen Tema 08]] | [[wiki/entities/web-accessibility-wcag-and-rd-1112-2018|WCAG 2.1 y RD 1112/2018]] | [[wiki/synthesis/wcag-accessibility-principles-pour-cheatsheet|Cheatsheet POUR y Plazos]] |
| **Tema 09** | Metodologías, QA y Control de Versiones | [[wiki/sources/bloque3-tema09|Resumen Tema 09]] | [[wiki/entities/metrica-v3-methodology|MÉTRICA v3]], [[wiki/entities/git-version-control-system|Git]] | [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía MÉTRICA v3]], [[wiki/synthesis/software-testing-and-qa-guide|Guía Testing McCabe]] |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Normalización Relacional (1FN a 5FN y BCNF)
- **1FN**: Valores atómicos, sin grupos repetitivos.
- **2FN**: 1FN + Todo atributo no primo tiene **dependencia funcional completa** de toda la clave (elimina dependencias parciales en claves compuestas).
- **3FN**: 2FN + Ningún atributo no primo depende transitivamente de la clave ($X ightarrow Y ightarrow Z$).
- **BCNF (Boyce-Codd)**: Para toda dependencia funcional $X ightarrow A$, $X$ debe ser superclave.
- **4FN**: Elimina dependencias multivaluadas independientes ($X 	woheadrightarrow Y$).
- **5FN**: Elimina dependencias de reunión (*join dependencies*).

---

### B. Patrones de Diseño GoF (Gang of Four)
- **Creacionales**: *Singleton* (instancia única), *Factory Method*, *Abstract Factory*, *Builder*, *Prototype*.
- **Estructurales**: *Adapter* (convierte interfaces), *Decorator* (añade responsabilidades dinámicamente), *Facade* (interfaz simplificada), *Composite* (estructura de árbol), *Proxy*.
- **Comportamiento**: *Observer* (suscripción 1:N), *Strategy* (familia de algoritmos intercambiables), *Command*, *Iterator*, *State*, *Template Method*.

---

### C. Metodología MÉTRICA Versión 3
- **Procesos Principales**:
  1. **PSI**: Planificación de Sistemas de Información (marco estratégico global).
  2. **EVS**: Estudio de Viabilidad del Sistema.
  3. **ASI**: Análisis del Sistema de Información (especificación de requisitos funcionales y casos de uso).
  4. **DSI**: Diseño del Sistema de Información (arquitectura técnica, modelo físico de datos).
  5. **CSI**: Construcción del Sistema de Información (codificación, pruebas unitarias y de integración).
  6. **IAS**: Implantación y Aceptación del Sistema (puesta en producción y paso a mantenimiento).
  7. **CAL / MNT**: Mantenimiento del Sistema de Información (correctivo, adaptativo, perfectivo, evolutivo).

---

### D. Testing y Métrica de Complejidad de McCabe
- **Complejidad Ciclomática**: Cantidad de caminos linealmente independientes en un grafo de control de flujo:
  $$V(G) = E - N + 2P = D + 1$$
  - $E$: Número de aristas (*Edges*).
  - $N$: Número de nodos (*Nodes*).
  - $P$: Componentes conexos (habitualmente $P=1$).
  - $D$: Número de nodos predicado (puntos de decisión condicional `if`, `while`).

---

## 🔵 3. Batería de Supuestos Prácticos de Examen (Bloque 3)
- [**Supuesto Práctico: Normalización de BBDD y SQL DDL**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-normalizacion-bbdd.md)
- [**Supuesto Práctico: Trazas de Código Java y PHP**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-java-php-programacion.md)
- [**Supuesto Práctico Oficial TAI: Simulacro Completo de Examen Bloque III**](file:///d:/Desktop/TAI%20OPOSICIONES/ia%20informatica%20resumenes/wiki/synthesis/supuestos-practicos-bloque3-simulacro-examen-tai.md)
