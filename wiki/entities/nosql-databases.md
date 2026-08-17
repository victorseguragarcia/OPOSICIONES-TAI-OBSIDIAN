---
title: "Bases de Datos NoSQL y Big Data"
type: "entity"
tags:
  - nosql
  - big-data
  - cap-theorem
  - databases
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "NoSQL"
  - "Bases de Datos No Relacionales"
---

# Bases de Datos NoSQL y Big Data

Las bases de datos **NoSQL ("Not Only SQL")** son sistemas de gestión de datos no relacionales diseñados para ofrecer alto rendimiento, escalabilidad horizontal y esquemas flexibles para el tratamiento de datos masivos (*Big Data*).

---

## 🏛️ Teorema CAP y Modelo BASE

- **Teorema CAP (Eric Brewer)**: En un sistema distribuido de datos solo es posible garantizar simultáneamente **dos de las tres propiedades**:
  - **C (Consistency / Consistencia)**: Todos los nodos ven los mismos datos en el mismo instante.
  - **A (Availability / Disponibilidad)**: Cada petición no fallida recibe una respuesta.
  - **P (Partition Tolerance / Tolerancia a Particiones)**: El sistema continúa operando pese a pérdidas de comunicación entre nodos.
- **Modelo BASE (frente a ACID)**:
  - **BA (Basically Available)**: Disponibilidad básica garantizada.
  - **S (Soft State)**: El estado del sistema puede cambiar sin interacción del usuario debido a replicación en curso.
  - **E (Eventual Consistency)**: Consistencia eventual alcanzada cuando cesan las escrituras.

---

## 🧩 Familias NoSQL Principales

1. **Documentales**: Almacenan documentos semiestructurados JSON/BSON (ej. **MongoDB**, CouchDB).
2. **Clave-Valor**: Almacenes ultrarrápidos en memoria (ej. **Redis**, Memcached, AWS DynamoDB).
3. **Columnares / Familias de Columnas**: Optimizadas para analítica masiva (ej. **Apache Cassandra**, HBase).
4. **Grafos**: Nodos y relaciones para análisis de redes (ej. **Neo4j**, Amazon Neptune).

---

## 🎯 Datos Clave para Oposiciones TAI

| Modelo | Ejemplos Líderes | Caso de Uso |
|--------|------------------|-------------|
| Documental | MongoDB, Couchbase | Catálogos, CMS, JSON |
| Clave-Valor | Redis, DynamoDB | Sesiones, Caché ultrarrápida |
| Columnar | Cassandra, HBase | Time-series, Big Data OLAP |
| Grafos | Neo4j, ArangoDB | Redes sociales, Detección de fraude |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
