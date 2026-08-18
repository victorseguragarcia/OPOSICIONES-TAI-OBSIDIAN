---
title: "Resumen Completo Tema 03 (Bloque 3): Lenguaje SQL ANSI, Subconsultas y Transacciones ACID"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-3
  - tema-03
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque3-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|⬅️ Tema 02]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|Tema 04 ➡️]]

# 🔴 Resumen Completo Tema 03 (Bloque 3): Lenguaje SQL ANSI, Subconsultas y Transacciones ACID

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 03**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

Este tema aborda el estándar **ANSI SQL** para sistemas relacionales: sublenguajes **DDL** (`CREATE`, `ALTER`, `DROP`, `TRUNCATE`), **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), **DCL** (`GRANT`, `REVOKE`) y **TCL** (`COMMIT`, `ROLLBACK`, `SAVEPOINT`), consultas avanzadas con agregación (`GROUP BY`, `HAVING`), tipos de combinaciones (**INNER JOIN**, **LEFT/RIGHT/FULL OUTER JOIN**, **CROSS JOIN**, **NATURAL JOIN**), subconsultas correlacionadas, objetos de programación en servidor: **Procedimientos Almacenados (Stored Procedures)**, **Funciones de Usuario (UDF)** y **Disparadores (Triggers `BEFORE`/`AFTER`/`INSTEAD OF`)**, y las propiedades transaccionales **ACID** y niveles de aislamiento SQL.

---

## 🎯 Datos Clave para Oposiciones TAI

| Objeto / Comando SQL | Función / Definición |
|----------------------|----------------------|
| **`WHERE` vs `HAVING`** | `WHERE`: Filtra filas antes de agrupar \| `HAVING`: Filtra grupos tras el `GROUP BY` |
| **`TRUNCATE` vs `DELETE`** | `TRUNCATE`: DDL rápido, reinicia identidad, sin WHERE \| `DELETE`: DML fila a fila con rollback |
| **Triggers (Disparadores)** | Procedimientos automáticos ejecutados ante eventos DML (`INSERT`, `UPDATE`, `DELETE`) |
| **Propiedades ACID** | **Atomicidad** (todo o nada), **Consistencia**, **Aislamiento** y **Durabilidad** |
| **Niveles de Aislamiento** | *Read Uncommitted*, *Read Committed*, *Repeatable Read*, *Serializable* |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/sql-ansi-and-stored-procedures|Estándar ANSI SQL, Procedimientos Almacenados y Triggers]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque3-tema03|Nota Fuente del Tema 03]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema03-sql-interrogacion|Test Tema 03]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|⬅️ Tema 02]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|Tema 04 ➡️]]
