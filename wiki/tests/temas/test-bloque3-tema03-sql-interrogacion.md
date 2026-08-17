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

# 🔴 Test de Autoevaluación: Bloque 3 - Tema 03 (SQL ANSI, DDL, DML y Transacciones)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 3 - Tema 03 (SQL ANSI, DDL, DML y Transacciones)",
  "questions": [
    {
      "question": "¿Cuál de las siguientes sentencias SQL pertenece al Lenguaje de Definición de Datos (DDL)?",
      "options": [
        "`INSERT INTO empleados VALUES (...)`",
        "`ALTER TABLE empleados ADD COLUMN sueldo NUMERIC;`",
        "`SELECT * FROM empleados WHERE id = 1;`",
        "`GRANT SELECT ON empleados TO usuario1;`"
      ],
      "answer": "b",
      "explanation": "DDL incluye `CREATE`, `ALTER`, `DROP`, `TRUNCATE`. DML incluye `SELECT`, `INSERT`, `UPDATE`, `DELETE`."
    },
    {
      "question": "En una consulta SQL con cláusula `GROUP BY`, ¿qué cláusula se utiliza para filtrar grupos agregados en lugar de filas individuales?",
      "options": [
        "`WHERE`",
        "`HAVING`",
        "`ORDER BY`",
        "`QUALIFY`"
      ],
      "answer": "b",
      "explanation": "`HAVING` filtra sobre condiciones de grupo agregadas (`COUNT`, `SUM`, `AVG`)."
    },
    {
      "question": "En el estándar SQL ANSI, ¿qué tipo de JOIN devuelve todas las filas de la tabla izquierda y las filas coincidentes de la derecha (o NULL si no hay coincidencia)?",
      "options": [
        "`INNER JOIN`",
        "`LEFT OUTER JOIN`",
        "`FULL OUTER JOIN`",
        "`CROSS JOIN`"
      ],
      "answer": "b",
      "explanation": "`LEFT JOIN` conserva todas las filas de la tabla de la izquierda."
    },
    {
      "question": "¿Cuál de los siguientes niveles de aislamiento de transacciones SQL evita lecturas sucias (*Dirty Reads*), lecturas no repetibles (*Non-Repeatable Reads*) y lecturas fantasma (*Phantom Reads*)?",
      "options": [
        "`READ UNCOMMITTED`",
        "`READ COMMITTED`",
        "`REPEATABLE READ`",
        "`SERIALIZABLE`"
      ],
      "answer": "d",
      "explanation": "`SERIALIZABLE` es el nivel máximo de aislamiento y previene los tres fenómenos anómalos."
    },
    {
      "question": "¿Qué sentencia SQL de control de transacciones confirma permanentemente los cambios realizados durante la transacción en curso?",
      "options": [
        "`ROLLBACK`",
        "`COMMIT`",
        "`SAVEPOINT`",
        "`TRUNCATE`"
      ],
      "answer": "b",
      "explanation": "`COMMIT` hace persistentes las modificaciones de la transacción; `ROLLBACK` las deshace."
    }
  ]
}
```
