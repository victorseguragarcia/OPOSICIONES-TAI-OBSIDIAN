---
title: "Guía de Familias NoSQL, Teorema CAP de Brewer y Modelo BASE"
type: "synthesis"
tags:
  - synthesis
  - nosql
  - teorema-cap
  - mongodb
  - redis
  - cassandra
  - neo4j
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía NoSQL y Teorema CAP"
  - "Comparativa NoSQL y Teorema CAP"
---

# 🔴 Guía de Familias NoSQL, Teorema CAP de Brewer y Modelo BASE

Comparativa técnica de las 4 familias NoSQL y su clasificación según el Teorema CAP de Eric Brewer.

---

## 🏛️ Matriz Técnica NoSQL vs Teorema CAP

| Familia NoSQL | Tecnologías | Clasificación CAP | Formato / Estructura de Datos |
|---------------|-------------|-------------------|-------------------------------|
| **Clave-Valor** | **Redis**, Memcached, DynamoDB | **CP** / **AP** | Cadenas, hashes, listas, sets en RAM |
| **Documental** | **MongoDB**, CouchDB | **CP** (Consistencia fuerte) | **BSON** / **JSON** |
| **Columnar** | **Apache Cassandra**, HBase | **AP** (Alta disponibilidad) | Familias de columnas dispersas |
| **Grafos** | **Neo4j**, Amazon Neptune | **CA** (Clústeres locales) | Nodos, relaciones y propiedades |

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP]]
