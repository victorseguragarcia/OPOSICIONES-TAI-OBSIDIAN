---
title: "Cheatsheet de Normalización de Bases de Datos y Estándar ANSI SQL"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - normalizacion
  - sql
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet SQL y Normalización"
  - "Normalización y SQL Guía"
---

# Cheatsheet de Normalización de Bases de Datos y Estándar ANSI SQL

Tabla de referencia rápida sobre reglas de normalización y comandos SQL para exámenes TAI.

---

## 📋 1. Reglas de Normalización

| Forma Normal | Requisito Principal | Error que Elimina |
|--------------|---------------------|-------------------|
| **1FN** | Atributos **atómicos**, sin grupos repetitivos | Tablas anidadas y listas en campos |
| **2FN** | 1FN + **Dependencia funcional completa** de la PK | Redundancia por atributos que dependen de parte de una PK compuesta |
| **3FN** | 2FN + **Sin dependencias transitivas** ($X ightarrow Y ightarrow Z$) | Redundancia por dependencias entre campos no clave |
| **BCNF** | Para todo $X ightarrow Y$, $X$ es **superclave** | Dependencias anómalas en tablas con múltiples claves candidatas compuestas solapadas |

---

## 💻 2. Tabla de Tipos de JOINs en SQL

- **INNER JOIN**: Devuelve solo las filas que tienen coincidencia en ambas tablas.
- **LEFT OUTER JOIN**: Devuelve todas las filas de la tabla izquierda y las coincidentes de la derecha (NULL si no hay coincidencia).
- **RIGHT OUTER JOIN**: Devuelve todas las filas de la tabla derecha y las coincidentes de la izquierda.
- **FULL OUTER JOIN**: Devuelve todas las filas cuando hay coincidencia en cualquiera de las dos tablas.
- **CROSS JOIN**: Producto cartesiano de ambas tablas ($N 	imes M$ filas).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Entidad: [[wiki/entities/sql-ansi-and-stored-procedures|ANSI SQL]]
