---
title: "Estándar ANSI SQL, Procedimientos Almacenados, Triggers y Transacciones ACID"
type: "entity"
tags:
  - sql
  - ddl
  - dml
  - acid
  - triggers
  - stored-procedures
sources:
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ANSI SQL y Programación BBDD"
  - "SQL Transacciones y Triggers"
---

# Estándar ANSI SQL, Procedimientos Almacenados, Triggers y Transacciones ACID

Lenguaje estructurado de consultas normalizado por ANSI/ISO (SQL-86, SQL-92, SQL:1999 con soporte OO, SQL:2016 con JSON) para gestión y programación de bases de datos relacionales.

---

## 🏛️ 1. Clasificación de Sentencias SQL

```
                               Sublenguajes SQL
                                       │
     ┌──────────────────┬──────────────┴─────┬──────────────────┐
     ▼                  ▼                    ▼                  ▼
  [ DDL ]            [ DML ]              [ DCL ]            [ TCL ]
Definición         Manipulación           Control          Transacciones
 • CREATE           • SELECT               • GRANT            • COMMIT
 • ALTER            • INSERT               • REVOKE           • ROLLBACK
 • DROP             • UPDATE                                  • SAVEPOINT
 • TRUNCATE         • DELETE                                  • SET TRANS.
```

---

## ⚙️ 2. Disparadores (Triggers) y Objetos Programables

- **Tipos de Triggers según Momento**:
  - `BEFORE`: Se ejecuta antes de la operación DML (ideal para validaciones o cálculo de valores por defecto).
  - `AFTER`: Se ejecuta después de la operación DML (ideal para auditoría, replicación o actualización de tablas resumen).
  - `INSTEAD OF`: Reemplaza la sentencia DML (utilizado obligatoriamente para permitir modificaciones en **Vistas complejas no actualizables**).
- **Ámbito de Ejecución**:
  - `FOR EACH ROW`: Disparador de fila (utiliza las pseudotablas / registros `:OLD` y `:NEW` en Oracle/PostgreSQL o `INSERTED`/`DELETED` en SQL Server).
  - `FOR EACH STATEMENT`: Disparador de sentencia (se ejecuta una única vez por instrucción independientemente del número de filas afectadas).

---

## 🔒 3. Transacciones y Propiedades ACID

1. **Atomicidad (Atomicity)**: La transacción se ejecuta en su totalidad o no se ejecuta nada (*All or Nothing*).
2. **Consistencia (Consistency)**: La transacción traslada la base de datos de un estado válido a otro estado válido cumpliendo todas las restricciones de integridad.
3. **Aislamiento (Isolation)**: Las operaciones de transacciones concurrentes son invisibles entre sí hasta su confirmación.
4. **Durabilidad (Durability)**: Una vez confirmada (`COMMIT`), los cambios persisten de forma permanente incluso ante caídas del sistema (*Write-Ahead Logging* / WAL).

### Niveles de Aislamiento SQL ANSI vs Anomalías Concurrencia:

| Nivel de Aislamiento | Lectura Sucia (*Dirty Read*) | Lectura No Repetible (*Non-Repeatable Read*) | Lectura Fantasma (*Phantom Read*) |
|----------------------|------------------------------|---------------------------------------------|-----------------------------------|
| **Read Uncommitted** | Permitida | Permitida | Permitida |
| **Read Committed** | **Prevenida** | Permitida | Permitida |
| **Repeatable Read** | **Prevenida** | **Prevenida** | Permitida |
| **Serializable** | **Prevenida** | **Prevenida** | **Prevenida** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
