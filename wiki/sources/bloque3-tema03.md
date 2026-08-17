---
title: "Resumen Fuente: Bloque 3 - Tema 03 (UD012110): Lenguajes de Interrogación SQL, Stored Procedures y Triggers"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema03
  - sql
  - ddl
  - dml
  - stored-procedures
  - triggers
  - transacciones
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen SQL, Stored Procedures y Triggers"
  - "bloque3-tema03"
---

# Resumen Fuente: Bloque 3 - Tema 03 (UD012110): Lenguajes de Interrogación SQL, Stored Procedures y Triggers

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md|bloque3-tema03-sql-interrogacion-bbdd.md]] (140 páginas).

---

## 📖 Resumen Ejecutivo

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
