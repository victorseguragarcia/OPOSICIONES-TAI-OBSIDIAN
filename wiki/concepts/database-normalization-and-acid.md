---
title: "Normalización de Bases de Datos y Propiedades ACID"
type: "concept"
tags:
  - databases
  - normalization
  - acid
  - transactions
  - sql
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Normalización y ACID"
  - "Database Normalization"
---

# Normalización de Bases de Datos y Propiedades ACID

El diseño formal de bases de datos relacionales garantiza la integridad de los datos, la eliminación de anomalías de inserción/borrado/actualización y la fiabilidad de las transacciones.

---

## 🏛️ Formas Normales (1FN a BCNF)

1. **Primera Forma Normal (1FN)**:
   - Todos los atributos contienen valores atómicos e indivisibles (sin grupos repetitivos o listas).
   - Existe una clave primaria definida para la tabla.
2. **Segunda Forma Normal (2FN)**:
   - Cumple 1FN.
   - Todo atributo no principal tiene **dependencia funcional completa** de la clave primaria (no depende de una parte de una clave compuesta).
3. **Tercera Forma Normal (3FN)**:
   - Cumple 2FN.
   - No existen **dependencias transitivas** entre atributos no clave (ningún atributo no clave depende de otro atributo no clave).
4. **Forma Normal de Boyce-Codd (BCNF)**:
   - Versión estricta de 3FN.
   - Para toda dependencia funcional no trivial $X ightarrow Y$, el determinante $X$ debe ser una **superclave** (o clave candidata).

---

## 🧩 Propiedades ACID de las Transacciones

- **A (Atomicidad / Atomicity)**: Principio del "todo o nada". La transacción se ejecuta completamente con éxito (`COMMIT`) o sus efectos se revierten íntegramente (`ROLLBACK`).
- **C (Consistencia / Consistency)**: La transacción traslada la base de datos de un estado válido y consistente a otro estado válido, respetando todas las reglas de integridad.
- **I (Aislamiento / Isolation)**: La ejecución concurrente de múltiples transacciones produce el mismo resultado que si se ejecutaran secuencialmente.
  - **Niveles de Aislamiento SQL-92**:
    - *Read Uncommitted*: Permite lecturas sucias (*Dirty Reads*).
    - *Read Committed*: Evita lecturas sucias; permite lecturas no repetibles.
    - *Repeatable Read*: Evita lecturas no repetibles; permite lecturas fantasma (*Phantom Reads*).
    - *Serializable*: Máximo aislamiento; previene todos los fenómenos anómalos.
- **D (Durabilidad / Durability)**: Una vez confirmada una transacción (`COMMIT`), sus cambios persisten permanentemente en el almacenamiento no volátil mediante el registro de transacciones (*Write-Ahead Logging / WAL*).

---

## 🎯 Datos Clave para Oposiciones TAI

| Nivel de Aislamiento SQL | Lectura Sucia | Lectura No Repetible | Lectura Fantasma |
|--------------------------|---------------|----------------------|------------------|
| **Read Uncommitted** | Sí | Sí | Sí |
| **Read Committed** | **No** | Sí | Sí |
| **Repeatable Read** | **No** | **No** | Sí |
| **Serializable** | **No** | **No** | **No** |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
