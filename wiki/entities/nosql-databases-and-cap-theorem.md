---
title: "Bases de Datos NoSQL, Familias y Teorema CAP"
type: "entity"
tags:
  - nosql
  - sgbd
  - mongodb
  - redis
  - cassandra
  - neo4j
  - teorema-cap
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "NoSQL y Teorema CAP"
  - "Bases de Datos NoSQL"
---

# Bases de Datos NoSQL, Familias y Teorema CAP

Sistemas de almacenamiento no relacionales diseñados para alta concurrencia, escalabilidad horizontal y esquemas dinámicos.

---

## 🏛️ Familias de Bases de Datos NoSQL

1. **Clave-Valor (*Key-Value*)**: Acceso de baja latencia por clave única (**Redis**, **Memcached**, DynamoDB).
2. **Documentales (*Document-Store*)**: Documentos JSON/BSON con esquemas flexibles (**MongoDB**, **CouchDB**).
3. **Columnas Anchas (*Column-Family*)**: Tablas dispersas particionadas por claves de fila (**Apache Cassandra**, **HBase**).
4. **Grafos (*Graph Databases*)**: Nodos y aristas optimizados para consultas de relaciones complejas (**Neo4j**).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema05|Resumen Bloque 2 - Tema 05]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP de Brewer y Modelo BASE]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía de Familias NoSQL y Teorema CAP]]
