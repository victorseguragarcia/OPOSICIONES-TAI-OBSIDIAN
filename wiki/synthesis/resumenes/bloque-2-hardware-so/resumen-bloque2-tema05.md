---
title: "Resumen Exhaustivo Tema 05 (Bloque 2): Bases de Datos Relacionales y NoSQL (Teorema CAP, Familias NoSQL)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-2
  - tema-05
  - hardware
  - sistemas-operativos
  - bbdd
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque2-tema05.md]]"
  - "[[wiki/sources/bloque2-tema05]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏁 Fin de Bloque 2 ➡️]]

# 🔴 Resumen Exhaustivo Tema 05 (Bloque 2): Bases de Datos Relacionales y NoSQL (Teorema CAP, Familias NoSQL)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 05**
> Modelo Relacional de Codd (relaciones, tuplas, atributos, claves primarias y foráneas, integridad de entidad y referencial), propiedades ACID de las transacciones, niveles de aislamiento ANSI SQL (Read Uncommitted, Read Committed, Repeatable Read, Serializable) y anomalías de concurrencia, Teorema CAP de Eric Brewer (Consistencia, Disponibilidad, Tolerancia a Particiones), modelo BASE y clasificación de BBDD NoSQL (Clave-Valor, Documentales, Columnar/Wide-Column y Grafos).

---

## 🟣 1. Desarrollo Técnico y Arquitectónico Exhaustivo

### 1. El Modelo Relacional y Reglas de Integridad de Codd
- **Conceptos Fundamentales**:
  - *Relación*: Tabla bidimensional compuesta por filas (**tuplas**) y columnas (**atributos**).
  - *Grado*: Número de atributos (columnas) de una relación.
  - *Cardinalidad*: Número de tuplas (filas) de una relación.
  - *Clave Primaria (Primary Key - PK)*: Atributo o conjunto mínimo de atributos que identifica unívocamente a cada tupla.
  - *Clave Foránea (Foreign Key - FK)*: Atributo en una relación que hace referencia a la clave primaria de otra relación (o de la misma).
- **Reglas de Integridad Fundamentales**:
  - **Integridad de Entidad**: Ningún componente de la clave primaria puede aceptar valores nulos (`NOT NULL`).
  - **Integridad Referencial**: Si una relación tiene una clave foránea, el valor de la clave foránea debe coincidir con un valor existente de la clave primaria en la relación referenciada o bien ser nulo (siempre que la FK no forme parte de su propia PK). Opciones de borrado/actualización: `CASCADE`, `RESTRICT / NO ACTION`, `SET NULL`, `SET DEFAULT`.
  - **Integridad de Dominio**: Todos los valores de una columna deben pertenecer al conjunto de valores permitidos para ese tipo de dato (restricciones `CHECK`, tipo de dato, rangos).

### 2. Propiedades ACID y Niveles de Aislamiento Transaccional
- **Propiedades ACID de las Transacciones**:
  - **Atomicidad (Atomicity)**: La transacción se ejecuta en su totalidad o no se ejecuta nada (*todo o nada*). Si falla una instrucción se hace `ROLLBACK`.
  - **Consistencia (Consistency)**: La transacción lleva a la base de datos de un estado válido a otro estado válido, respetando todas las reglas de integridad y restricciones.
  - **Aislamiento (Isolation)**: La ejecución concurrente de transacciones produce el mismo resultado que si se ejecutaran secuencialmente sin interferir entre sí.
  - **Durabilidad (Durability)**: Una vez que una transacción confirma sus cambios con `COMMIT`, los resultados son permanentes y no se perderán incluso ante una caída del sistema (gestionado mediante logs transaccionales WAL - Write-Ahead Logging).
- **Anomalías de Concurrencia y Niveles de Aislamiento (ANSI SQL)**:

| Nivel de Aislamiento | Lectura Sucia (*Dirty Read*) | Lectura No Repetible (*Non-Repeatable Read*) | Lectura Fantasma (*Phantom Read*) | Mecanismo de Bloqueo |
|:---|:---:|:---:|:---:|:---|
| **Read Uncommitted** | ⚠️ **Permitida** | ⚠️ **Permitida** | ⚠️ **Permitida** | Sin bloqueos de lectura compartidos. Lee cambios no confirmados. |
| **Read Committed** (Nivel por defecto en PostgreSQL y Oracle) | ❌ **Prevenida** | ⚠️ **Permitida** | ⚠️ **Permitida** | Solo lee datos confirmados (`COMMIT`). Una segunda lectura dentro de la misma transacción puede ver datos modificados por otra. |
| **Repeatable Read** (Nivel por defecto en MySQL InnoDB) | ❌ **Prevenida** | ❌ **Prevenida** | ⚠️ **Permitida** *(InnoDB la previene con MVCC y Next-Key Locks)* | Garantiza que leer la misma fila dos veces devuelva siempre el mismo valor. |
| **Serializable** | ❌ **Prevenida** | ❌ **Prevenida** | ❌ **Prevenida** | **Máximo aislamiento**. Ejecución estrictamente equivalente a secuencial mediante bloqueo de rangos o control de concurrencia optimista. |

### 3. El Teorema CAP de Brewer y el Modelo BASE
- **Teorema CAP (Eric Brewer, 2000)**:
  En cualquier sistema distribuido de almacenamiento de datos es **imposible garantizar simultáneamente las 3 propiedades**. Ante la presencia obligada de particiones de red (**P**), solo se puede elegir entre:
  - **Consistencia (C - Consistency)**: Todos los nodos ven exactamente los mismos datos en el mismo instante.
  - **Disponibilidad (A - Availability)**: Cada petición no fallida recibe una respuesta (sin garantía de que contenga la escritura más reciente).
  - **Tolerancia a Particiones (P - Partition Tolerance)**: El sistema sigue funcionando a pesar de la pérdida o caída de mensajes entre nodos.
  - *Sistemas CP*: Priorizan la consistencia frente a la disponibilidad (MongoDB, HBase, Redis Cluster).
  - *Sistemas AP*: Priorizan la disponibilidad aceptando consistencia eventual (Cassandra, CouchDB, Amazon DynamoDB).
  - *Sistemas CA*: Sistemas no distribuidos tradicionales (PostgreSQL, MySQL sobre un único nodo).
- **Modelo BASE de NoSQL**:
  - **Basically Available**: Disponibilidad básica garantizada.
  - **Soft state**: El estado del sistema puede cambiar con el tiempo sin interacción del usuario.
  - **Eventual consistency**: El sistema alcanzará la consistencia en algún momento futuro si no entran nuevas escrituras.

### 4. Familias de Bases de Datos NoSQL

| Familia NoSQL | Modelo de Datos y Estructura | Casos de Uso Óptimos | Gestores SGBD Destacados |
|:---|:---|:---|:---|
| **Clave-Valor (Key-Value)** | Estructura asociativa clave $ightarrow$ valor binario/string/JSON. Acceso directo ultra rápido $O(1)$ por clave primaria. | Caché de sesiones, carritos de compra, contadores en tiempo real, rankings. | **Redis** (in-memory con persistencia), **Memcached**, **AWS DynamoDB**, **Riak**. |
| **Documentales (Document Stores)** | Almacena datos semiestructurados en documentos jerárquicos (**JSON, BSON, XML**) con esquemas flexibles y consultas secundarias. | Catálogos de productos, CMS, portales web, gestión de perfiles de usuario. | **MongoDB** (formato binario BSON), **CouchDB**, **Elasticsearch** (orientado a búsqueda de texto completo), **RavenDB**. |
| **Orientadas a Columnas (Wide-Column / Columnar)** | Tablas donde los datos se almacenan por familias de columnas en lugar de por filas. Alta compresión y agregación masiva. | Big Data, análisis de series temporales, telemetría IoT, logs a gran escala. | **Apache Cassandra** (modelo AP multimaestro), **Apache HBase** (sobre HDFS), **Google Bigtable**, **Scans/ClickHouse**. |
| **Orientadas a Grafos (Graph Databases)** | Nodos (entidades), Relaciones (aristas con dirección y tipo) y Propiedades. Consultas eficientes de relaciones complejas. | Redes sociales, detección de fraudes financieros, motores de recomendación, grafos de conocimiento. | **Neo4j** (lenguaje de consulta Cypher), **Amazon Neptune**, **OrientDB**, **ArangoDB**. |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 05 (Bloque 2)**
> 1. **Nivel de Aislamiento por Defecto en SQL**: *PostgreSQL y Oracle* usan por defecto **Read Committed**; *MySQL (InnoDB)* usa **Repeatable Read**.
> 2. **Teorema CAP**: En un sistema distribuido la **Tolerancia a Particiones (P) es obligatoria**, por lo que la elección real es **CP o AP** (no existe un sistema distribuido CA perfecto en redes reales).
> 3. **Formato Interno de MongoDB**: Almacena los documentos en formato **BSON** (Binary JSON), no en texto plano JSON.
> 4. **Integridad de Entidad**: Exige que ningún campo de la clave primaria sea `NULL` (la clave foránea sí puede ser `NULL` salvo que forme parte de la clave primaria).

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Propiedades Transaccionales**: **ACID** $ightarrow$ **A**tomicidad, **C**onsistencia, **I**solation (Aislamiento), **D**urabilidad.
> - **Teorema CAP**: **CAP** $ightarrow$ **C**onsistencia, **A**vailability (Disponibilidad), **P**artición de red.
> - **Familias NoSQL**: **K-D-C-G** $ightarrow$ **K**ey-Value (Redis), **D**ocumental (MongoDB), **C**olumnar (Cassandra), **G**rafos (Neo4j).

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque2-tema05|Fuente Oficial del Tema 05]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema05-sgbd-nosql|Test Tema 05]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque 2**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema04|⬅️ Tema 04]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏁 Fin de Bloque 2 ➡️]]
