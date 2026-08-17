---
title: "Resumen Fuente: Bloque 2 - Tema 05 (UD012106): Sistemas Gestores de Bases de Datos, NoSQL y Teorema CAP"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema05
  - sgbd
  - rdbms
  - nosql
  - teorema-cap
  - base-model
  - big-data
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen SGBD, NoSQL y Teorema CAP"
  - "bloque2-tema05"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 05 (UD012106): Sistemas Gestores de Bases de Datos, NoSQL y Teorema CAP

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md|bloque2-tema05-sgbd-relacionales-nosql-cap.md]] (46 páginas).

---

## 📖 1. Arquitectura y Componentes de un SGBD

Un Sistema Gestor de Bases de Datos (SGBD / DBMS) proporciona una interfaz unificada entre los usuarios/aplicaciones y los datos físicos almacenados.
- **Componentes Principales**:
  1. **Motor de Almacenamiento (*Storage Engine*)**: Gestiona la asignación de espacio en disco, buffers en RAM y estructuras de datos de bajo nivel.
  2. **Procesador y Optimizador de Consultas**: Traduce las sentencias SQL en un árbol algebraico relacional y selecciona el plan de ejecución de menor coste (**CBO - Cost-Based Optimizer**).
  3. **Gestor de Transacciones y Recuperación**: Garantiza las propiedades **ACID** mediante el registro de transacciones (*Write-Ahead Logging* / WAL).
  4. **Gestor de Concurrencia y Bloqueos**: Controla el acceso simultáneo mediante bloqueos compartidos (S) y exclusivos (X) y control de versiones multi-versión (**MVCC**).
  5. **Diccionario de Datos / Catálogo del Sistema**: Almacena metadatos (definiciones de tablas, columnas, índices, vistas, permisos).

---

## 🟣 2. Clasificación de SGBD: Relacionales, Orientados a Objetos y NoSQL

- **Relacionales (RDBMS)**: Basados en el modelo de Codd y álgebra relacional (PostgreSQL, Oracle, MySQL, SQL Server, MariaDB).
- **Orientados a Objetos (OODBMS)**: Almacenan objetos complejos de forma nativa sin necesidad de mapeo relacional (estándar ODMG).
- **Objeto-Relacionales (ORDBMS)**: Híbridos que combinan el modelo relacional con tipos de datos definidos por el usuario, herencia y métodos (PostgreSQL, Oracle).
- **NoSQL (*Not Only SQL*)**: Diseñados para escalabilidad horizontal en clústeres distribuidos, alta velocidad y esquemas flexibles/dinámicos (*Schema-less*).

---

## 🔵 3. El Teorema CAP de Brewer y el Modelo BASE

### A. Teorema CAP (Eric Brewer, 2000):
En cualquier sistema de datos distribuido, es imposible garantizar simultáneamente las tres propiedades:
1. **Consistencia (C - Consistency)**: Todos los nodos ven exactamente los mismos datos en el mismo instante.
2. **Disponibilidad (A - Availability)**: Cada petición no fallida recibe una respuesta (sin garantía de ser la más reciente).
3. **Tolerancia a Particiones (P - Partition Tolerance)**: El sistema sigue funcionando a pesar de la pérdida o retraso de mensajes entre nodos.

> [!important]
> Como las redes reales siempre pueden sufrir particiones ($P$), los sistemas distribuidos deben elegir entre **Consistencia y Partición (CP)** o **Disponibilidad y Partición (AP)**.

```
                          TEOREMA CAP DE BREWER
                                    ▲
                                   /                                   /                                    /  P  \  (Tolerancia a Particiones)
                                /                                      /                                       /  HBase                                 /   MongoDB                               /     Redis                                /                                           / CP             AP                          /                            (Consistencia)   /                       \   (Disponibilidad)
               C <─────────────────────────────────> A
                    \                             /
                     \           CA              /
                      \     PostgreSQL, MySQL   /
                       \     Oracle, SQL Server/
                        ───────────────────────
```

### B. Modelo BASE frente a ACID:
- **ACID** (RDBMS tradicionales): *Atomicity, Consistency, Isolation, Durability* (Consistencia inmediata y estricta).
- **BASE** (Sistemas NoSQL distribuidos):
  - **Basically Available**: Disponibilidad básica del sistema garantizada.
  - **Soft state**: El estado del sistema puede cambiar con el tiempo sin interacción del usuario.
  - **Eventual consistency**: Consistencia eventual (los datos convergen a un estado coherente tras un periodo de tiempo).

---

## 🔵 4. Familias de Bases de Datos NoSQL

| Familia NoSQL | Modelo de Datos | Casos de Uso Típicos | Tecnologías Líderes |
|---------------|-----------------|----------------------|---------------------|
| **Clave-Valor (*Key-Value*)** | Pares clave-valor opacos; acceso ultrarrápido por clave | Cachés de sesión, carritos de compra, contadores | **Redis**, **Memcached**, AWS DynamoDB |
| **Documentales (*Document-Store*)** | Documentos semiestructurados jerárquicos (**JSON**, **BSON**, XML) | Catálogos de productos, CMS, perfiles de usuario | **MongoDB**, **CouchDB** |
| **Columnas Anchas (*Column-Family*)** | Tablas bidimensionales dispersas orientadas a columnas | Análisis de series temporales, telemetría, IoT | **Apache Cassandra**, **Apache HBase**, Google Bigtable |
| **Grafos (*Graph Databases*)** | Nodos (entidades), Relaciones (aristas con propiedades) | Redes sociales, detección de fraude, motores de recomendación | **Neo4j**, Amazon Neptune |

---

## 🎯 Datos Clave para Oposiciones TAI

| Pregunta / Concepto | Respuesta de Examen |
|---------------------|---------------------|
| **Elección en Teorema CAP** | En sistemas distribuidos, ante una partición de red se elige entre **CP** (Consistencia) o **AP** (Disponibilidad). |
| **MongoDB y BSON** | MongoDB almacena internamente los documentos en formato **BSON** (Binary JSON). |
| **Cassandra** | Base de datos NoSQL columnar distribuida orientada a **AP** (Alta disponibilidad y consistencia eventual). |
| **Redis** | Base de datos clave-valor en memoria RAM de altísimo rendimiento con soporte de estructuras complejas. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/nosql-databases-and-cap-theorem|Bases de Datos NoSQL, Familias y Teorema CAP]]
- Entidad: [[wiki/entities/relational-databases-rdbms|Bases de Datos Relacionales (RDBMS)]]
- Concepto: [[wiki/concepts/cap-theorem-and-base-model|Teorema CAP de Brewer y Modelo BASE]]
- Síntesis: [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía de Familias NoSQL y Teorema CAP]]
- Síntesis: [[wiki/synthesis/bloque2-tai-oposiciones-master-guide|Guía Maestra de Bloque 2: Tecnología Básica (TAI)]]
