---
title: "Test de Autoevaluación: Bloque 3 - Tema 03 (SQL ANSI, DDL, DML y Transacciones)"
type: "test"
target: "wiki/sources/bloque3-tema03.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-3
  - sql
  - ddl
  - dml
  - acid
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 03: SQL ANSI, DDL, DML y Transacciones

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. ¿Cuál de las siguientes sentencias SQL pertenece al Lenguaje de Definición de Datos (DDL)?
- [ ] a) `INSERT INTO empleados VALUES (...)`
- [ ] b) `ALTER TABLE empleados ADD COLUMN sueldo NUMERIC;`
- [ ] c) `SELECT * FROM empleados WHERE id = 1;`
- [ ] d) `GRANT SELECT ON empleados TO usuario1;`

### 2. En una consulta SQL con cláusula `GROUP BY`, ¿qué cláusula se utiliza para filtrar grupos agregados en lugar de filas individuales?
- [ ] a) `WHERE`
- [ ] b) `HAVING`
- [ ] c) `ORDER BY`
- [ ] d) `QUALIFY`

### 3. En el estándar SQL ANSI, ¿qué tipo de JOIN devuelve todas las filas de la tabla izquierda y las filas coincidentes de la derecha (o NULL si no hay coincidencia)?
- [ ] a) `INNER JOIN`
- [ ] b) `LEFT OUTER JOIN`
- [ ] c) `FULL OUTER JOIN`
- [ ] d) `CROSS JOIN`

### 4. ¿Cuál de los siguientes niveles de aislamiento de transacciones SQL evita lecturas sucias (*Dirty Reads*), lecturas no repetibles (*Non-Repeatable Reads*) y lecturas fantasma (*Phantom Reads*)?
- [ ] a) `READ UNCOMMITTED`
- [ ] b) `READ COMMITTED`
- [ ] c) `REPEATABLE READ`
- [ ] d) `SERIALIZABLE`

### 5. ¿Qué sentencia SQL de control de transacciones confirma permanentemente los cambios realizados durante la transacción en curso?
- [ ] a) `ROLLBACK`
- [ ] b) `COMMIT`
- [ ] c) `SAVEPOINT`
- [ ] d) `TRUNCATE`

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **d** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: DDL incluye `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. DML incluye `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
> - **Pregunta 2 (b)**: `HAVING` filtra sobre condiciones de grupo agregadas (`COUNT`, `SUM`, `AVG`).
> - **Pregunta 3 (b)**: `LEFT JOIN` conserva todas las filas de la tabla de la izquierda.
> - **Pregunta 4 (d)**: `SERIALIZABLE` es el nivel máximo de aislamiento y previene los tres fenómenos anómalos.
> - **Pregunta 5 (b)**: `COMMIT` hace persistentes las modificaciones de la transacción; `ROLLBACK` las deshace.
