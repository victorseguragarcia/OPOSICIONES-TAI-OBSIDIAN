---
title: "Bases de Datos NoSQL y Almacenamiento Distribuido"
type: "entity"
tags:
  - databases
  - nosql
  - mongodb
  - redis
  - cassandra
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "NoSQL"
  - "Non-relational Databases"
---

# Bases de Datos NoSQL y Almacenamiento Distribuido

Las **Bases de Datos NoSQL** están diseñadas para modelos de datos flexibles, escalabilidad horizontal masiva y gestión de datos no estructurados o semiestructurados.

## Familias de Modelos NoSQL
1. **Documentales** (MongoDB, CouchDB): Almacenamiento en documentos JSON/BSON con esquemas dinámicos.
2. **Clave-Valor** (Redis, Memcached): Acceso ultra-rápido en memoria para caché y sesiones.
3. **Columnares** (Apache Cassandra, ScyllaDB): Optimizado para consultas analíticas sobre grandes volúmenes distribuidos.
4. **Grafos** (Neo4j): Optimizado para relaciones complejas entre entidades y redes.

## Teorema CAP y Consistencia
- Teorema de Brewer (CAP): En un sistema distribuido solo se pueden garantizar dos de las tres propiedades: Consistencia (C), Disponibilidad (A) y Tolerancia a Particiones (P).
- Modelo **BASE** (Basically Available, Soft state, Eventual consistency).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Alternativa Relacional: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]

