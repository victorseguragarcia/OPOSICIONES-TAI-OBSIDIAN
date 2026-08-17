---
title: "Normalización de Bases de Datos y Principios ACID"
type: "concept"
tags:
  - databases
  - acid
  - normalization
  - sql
  - transactions
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "ACID"
  - "Normalización"
  - "Transacciones SQL"
---

# Normalización de Bases de Datos y Principios ACID

Fundamentos de diseño y consistencia en sistemas gestores de bases de datos relacionales.

## Formas Normales (Normalización)
- **1FN**: Todos los atributos contienen valores atómicos y no existen grupos repetitivos.
- **2FN**: Está en 1FN y todos los atributos no clave tienen dependencia funcional completa de la clave primaria.
- **3FN**: Está en 2FN y no existen dependencias funcionales transitivas entre atributos no clave.
- **FNBC (Boyce-Codd)**: Refinamiento estricto donde todo determinante es superclave.

## Principios ACID de las Transacciones
1. **Atomicidad (Atomicity)**: La transacción se ejecuta completamente o no se ejecuta en absoluto (*Commit* o *Rollback*).
2. **Consistencia (Consistency)**: La base de datos pasa de un estado válido a otro cumpliendo todas las restricciones de integridad.
3. **Aislamiento (Isolation)**: Las transacciones concurrentes se ejecutan sin interferencias mutuas (niveles: Read Uncommitted, Read Committed, Repeatable Read, Serializable).
4. **Durabilidad (Durability)**: Una vez confirmada la transacción, sus efectos persisten ante fallos del sistema (Write-Ahead Logging / WAL).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]

