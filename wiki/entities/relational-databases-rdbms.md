---
title: "Bases de Datos Relacionales (RDBMS)"
type: "entity"
tags:
  - rdbms
  - sql
  - codd-rules
  - databases
sources:
  - "raw/sources/bloque4-tema02.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "RDBMS"
  - "SGBD Relacional"
---

# Bases de Datos Relacionales (RDBMS)

Un **Sistema de Gestión de Bases de Datos Relacionales (RDBMS)** es un software basado en el modelo relacional introducido por **Edgar F. Codd** en 1970, donde los datos se organizan en tablas bidimensionales compuestas por filas (tuplas) y columnas (atributos).

---

## 🏛️ Las 12 Reglas de Codd (13 Reglas: 0 a 12)

1. **Regla 0 (Regla Fundacional)**: El sistema debe gestionar la base de datos enteramente mediante sus capacidades relacionales.
2. **Regla 1 (Regla de la Información)**: Toda la información se representa explícitamente en el nivel lógico en tablas mediante valores en posiciones de filas y columnas.
3. **Regla 2 (Acceso Garantizado)**: Cada dato atómico es direccionable lógicamente especificando el nombre de la tabla, la clave primaria (PK) y el nombre de la columna.
4. **Regla 3 (Tratamiento Sistemático de Valores Nulos)**: El SGBD debe soportar valores `NULL` para representar información faltante o inaplicable de forma independiente del tipo de datos.
5. **Regla 4 (Catálogo Dinámico en Línea)**: La descripción de la base de datos (metadatos) se almacena a nivel lógico en tablas relacionales consultables mediante el mismo lenguaje relacional.
6. **Regla 5 (Sublenguaje Comprensivo de Datos)**: Debe existir al menos un lenguaje (como SQL) que soporte DDL, DML, DCL, restricciones de integridad y gestión de transacciones.
7. **Regla 6 (Actualización de Vistas)**: Todas las vistas que sean teóricamente actualizables deben ser actualizables por el sistema.
8. **Regla 7 (Inserción, Actualización y Borrado de Alto Nivel)**: El sistema debe permitir manipular conjuntos de registros (*set-at-a-time*) en una sola sentencia.
9. **Regla 8 (Independencia Física de Datos)**: Los cambios en el almacenamiento físico o métodos de acceso no afectan a las aplicaciones a nivel lógico.
10. **Regla 9 (Independencia Lógica de Datos)**: Los cambios en las tablas base (añadir columnas, particionar tablas) que preserven la información no afectan a las vistas ni aplicaciones.
11. **Regla 10 (Independencia de Integridad)**: Las restricciones de integridad (PK, FK, CHECK, NOT NULL) deben almacenarse en el catálogo, no en los programas de aplicación.
12. **Regla 11 (Independencia de Distribución)**: La distribución de datos en múltiples sedes es transparente para el usuario.
13. **Regla 12 (No Subversión)**: Si el sistema dispone de interfaces de bajo nivel (registro a registro), no pueden utilizarse para sortear las reglas de seguridad o integridad relacionales.

---

## 🎯 Datos Clave para Oposiciones TAI

| Elemento | Definición Técnica |
|----------|--------------------|
| Creador Modelo Relacional | **Edgar F. Codd** (IBM, 1970) |
| Componentes SQL | **DDL** (Definición), **DML** (Manipulación), **DCL** (Control), **TCL** (Transacciones) |
| Propiedades Transaccionales | **ACID** (Atomicidad, Consistencia, Aislamiento, Durabilidad) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema02|Resumen Bloque 4 - Tema 02]]
- Concepto: [[wiki/concepts/database-normalization-and-acid|Normalización de Bases de Datos y Propiedades ACID]]
- Entidad: [[wiki/entities/nosql-databases|Bases de Datos NoSQL]]
