---
title: "Resumen Exhaustivo Tema 03 (Bloque 3): Lenguaje SQL ANSI, Subconsultas y Transacciones ACID"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-03
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema03.md]]"
  - "[[wiki/sources/bloque3-tema03]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|Tema 04 ➡️]]

# 🔴 Resumen Exhaustivo Tema 03 (Bloque 3): Lenguaje SQL ANSI, Subconsultas y Transacciones ACID

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 03**
> Sublenguajes SQL (DDL, DML, DCL, TCL), tipos de datos, restricciones de tabla, consultas complejas (JOINs, GROUP BY, HAVING), subconsultas correlacionadas, operadores relacionales (UNION, INTERSECT, EXCEPT), control de transacciones (COMMIT, ROLLBACK, SAVEPOINT) y vistas.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Clasificación del Lenguaje SQL ANSI/ISO
- **DDL (Data Definition Language)**: `CREATE`, `ALTER`, `DROP`, `TRUNCATE` (elimina todas las filas sin activar triggers DML ni registrar fila a fila en el log de transacciones).
- **DML (Data Manipulation Language)**: `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL (Data Control Language)**: `GRANT` (concede permisos), `REVOKE` (retira permisos).
- **TCL (Transaction Control Language)**: `COMMIT` (confirma cambios permanentes), `ROLLBACK` (revierte cambios), `SAVEPOINT` (punto de restauración intermedio).

### 2. Consultas Avanzadas, Agregaciones y Tipos de JOINs
- **Cláusula WHERE vs HAVING**:
  - `WHERE`: Filtra filas **individuales ANTES** de que se aplique el agrupamiento (`GROUP BY`). ❌ **NO puede contener funciones de agregación** (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`).
  - `HAVING`: Filtra **grupos de filas DESPUÉS** de aplicar el agrupamiento. **SÍ admite funciones de agregación**.
- **Tipos de JOINs**:
  - `INNER JOIN`: Devuelve solo filas que tienen coincidencia exacta en ambas tablas.
  - `LEFT (OUTER) JOIN`: Devuelve todas las filas de la tabla izquierda y las coincidentes de la derecha (rellenando con `NULL` si no hay match).
  - `RIGHT (OUTER) JOIN`: Devuelve todas las filas de la derecha y las coincidentes de la izquierda.
  - `FULL (OUTER) JOIN`: Devuelve todas las filas de ambas tablas con `NULL` donde no haya coincidencia.
  - `CROSS JOIN`: Producto cartesiano ($M \times N$ filas).
- **Operadores de Conjuntos (exigen mismo número de columnas y tipos compatibles)**:
  - `UNION`: Combina resultados **eliminando duplicados** (`UNION ALL` conserva duplicados y es más rápido).
  - `INTERSECT`: Devuelve solo las filas comunes a ambas consultas.
  - `EXCEPT` (o `MINUS` en Oracle): Devuelve las filas de la primera consulta que no están en la segunda.

### 3. Subconsultas y Operadores de Comparación Múltiple
- **Operadores de Subconsulta**:
  - `IN / NOT IN`: Comprueba si un valor pertenece a un conjunto devuelto por la subconsulta.
  - `EXISTS / NOT EXISTS`: Devuelve verdadero si la subconsulta devuelve **al menos una fila** (evaluación booleana ultra eficiente).
  - `ALL`: La condición debe ser verdadera para **todos** los valores devueltos.
  - `ANY / SOME`: La condición debe ser verdadera para **al menos uno** de los valores devueltos.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 03 (Bloque 3)**
> 1. **TRUNCATE vs DELETE**: `DELETE` es DML, admite cláusula `WHERE`, dispara triggers y permite `ROLLBACK`; `TRUNCATE` es DDL, borra la tabla completa instantáneamente, no admite `WHERE` y reinicia los contadores de secuencia (`AUTO_INCREMENT`).
> 2. **Funciones de Agregación en WHERE**: La consulta `SELECT * FROM tabla WHERE AVG(salario) > 1000` produce un **ERROR de sintaxis**; debe usarse `HAVING AVG(salario) > 1000`.
> 3. **UNION vs UNION ALL**: `UNION` realiza un filtrado implícito de duplicados (mayor coste de CPU/ordenación); `UNION ALL` une directamente sin eliminar repetidos.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Orden de Ejecución Lógico en SQL**: **FROM $\rightarrow$ WHERE $\rightarrow$ GROUP BY $\rightarrow$ HAVING $\rightarrow$ SELECT $\rightarrow$ DISTINCT $\rightarrow$ ORDER BY $\rightarrow$ LIMIT/OFFSET**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema03|Fuente Oficial del Tema 03]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema03|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema03-sql-interrogacion|Test Tema 03]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|⬅️ Tema 02]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema04|Tema 04 ➡️]]
