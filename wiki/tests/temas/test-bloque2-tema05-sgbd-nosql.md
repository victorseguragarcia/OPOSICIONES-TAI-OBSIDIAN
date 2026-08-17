---
title: "Test de Autoevaluación: Bloque 2 - Tema 05 (SGBD Relacionales, NoSQL y Teorema CAP)"
type: "test"
target: "wiki/sources/bloque2-tema05.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - sgbd
  - sql
  - nosql
  - cap-theorem
  - mongodb
  - redis
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 05: SGBD Relacionales, Familias NoSQL y Teorema CAP

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---

## ❓ Preguntas

### 1. Según el Teorema CAP de Eric Brewer para sistemas distribuidos, ante la presencia inevitable de una partición de red ($P$), ¿qué dos garantías son mutuamente excluyentes?
- [ ] a) Atomicidad y Durabilidad.
- [ ] b) Consistencia estricta ($C$) y Disponibilidad ($A$).
- [ ] c) Rendimiento y Seguridad.
- [ ] d) Concurrencia y Aislamiento.

### 2. ¿A qué familia de bases de datos NoSQL pertenece MongoDB, almacenando la información en documentos semiestructurados BSON (JSON binario)?
- [ ] a) Clave-Valor.
- [ ] b) Documental (*Document-oriented*).
- [ ] c) Columnas Anchas (*Wide-Column Store*).
- [ ] d) Grafos (*Graph Database*).

### 3. ¿Qué modelo alternativo a ACID caracteriza a las bases de datos NoSQL distribuidas de alta disponibilidad (AP) como Apache Cassandra?
- [ ] a) Modelo REST.
- [ ] b) Modelo BASE (*Basically Available, Soft state, Eventual consistency*).
- [ ] c) Modelo ANSI SPARC.
- [ ] d) Modelo CRUD.

### 4. ¿Cuál de los siguientes motores de base de datos NoSQL es un almacén Clave-Valor en memoria RAM de ultra alto rendimiento utilizado frecuentemente para caché y colas de mensajes?
- [ ] a) Neo4j.
- [ ] b) Redis.
- [ ] c) PostgreSQL.
- [ ] d) Apache CouchDB.

### 5. En el modelo relacional tradicional, ¿qué propiedad de las transacciones ACID garantiza que las modificaciones realizadas por una transacción confirmada persistan incluso ante fallos catastróficos del sistema?
- [ ] a) Atomicidad.
- [ ] b) Consistencia.
- [ ] c) Aislamiento.
- [ ] d) Durabilidad (*Durability*).

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **b** | 5. **d**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: El Teorema CAP establece que en un sistema distribuido particionado ($P$) solo se puede garantizar Consistencia ($CP$) o Disponibilidad ($AP$).
> - **Pregunta 2 (b)**: MongoDB es el motor NoSQL documental líder y utiliza BSON (*Binary JSON*).
> - **Pregunta 3 (b)**: BASE: Disponibilidad básica, estado flexible y consistencia eventual.
> - **Pregunta 4 (b)**: Redis es un almacén Clave-Valor en memoria RAM con soporte para estructuras complejas.
> - **Pregunta 5 (d)**: Durabilidad asegura que los cambios de un `COMMIT` queden grabados permanentemente en almacenamiento no volátil.
