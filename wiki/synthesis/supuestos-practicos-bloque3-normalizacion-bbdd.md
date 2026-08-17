---
title: "Supuesto Práctico Resuelto: Normalización de Bases de Datos (1FN a 5FN) y SQL DDL"
type: "synthesis"
tags:
  - synthesis
  - supuesto-practico
  - bloque-3
  - normalizacion
  - sql
  - bases-datos
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
  - "raw/sources/bloque3-tema03-sql-interrogacion-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Supuesto Práctico Normalización"
  - "Casos Prácticos BBDD Bloque 3"
---

# 🔴 Supuesto Práctico Resuelto: Normalización de Bases de Datos (1FN a 5FN) y SQL DDL

Guía práctica de resolución de supuestos de examen sobre normalización relacional, dependencias funcionales y definición de esquemas en SQL ANSI.

---

## 📋 Caso 1: Identificación de Formas Normales en Tablas Reales

### Enunciado 1.1: Atomicidad de Atributos (1FN)
Dada la siguiente tabla `PERSONAS`:
| id | nombre | fecha_nacimiento | pais |
|---|---|---|---|
| 1 | José Pérez Fernández | 21/10/1970 | España |
| 2 | María López Ruiz | 01/01/1974 | Perú |

> [!question]- ❓ ¿Cumple la tabla la Primera Forma Normal (1FN)?
> **Respuesta Correcta**: **b) Sí, pues cada campo contiene un valor atómico dentro del dominio definido.**
>
> **Justificación Técnica**: 
> En el modelo relacional, un atributo es atómico si no contiene listas, conjuntos repetitivos o subtablas anidadas. A nivel de diseño, guardar `nombre y apellidos` en un campo de texto no viola formalmente 1FN salvo que el modelo exija explícitamente la descomposición por requisitos de negocio.

---

### Enunciado 1.2: Dependencias Parciales (2FN)
Dada la tabla `MATRICULAS` con clave primaria compuesta `(dni, curso, modulo)`:
| dni | nombre | apellidos | direccion | curso | modulo | nota |
|---|---|---|---|---|---|---|
| 12345678A | Almudena | Cantero Leal | Calle Sur | AD | DAM1 | 5.1 |
| 23456789B | Luis | López Ruiz | Calle Norte | PSP | DAM1 | 5.5 |

> [!question]- ❓ ¿Cumple la tabla la Segunda Forma Normal (2FN)?
> **Respuesta Correcta**: **a) No, existen dependencias funcionales parciales.**
>
> **Justificación Técnica**: 
> La clave primaria es `(dni, curso, modulo)`. Los atributos `nombre`, `apellidos` y `direccion` dependen únicamente de una parte de la clave (`dni`), es decir: `dni -> {nombre, apellidos, direccion}`. Para cumplir 2FN, todo atributo no principal debe tener **dependencia funcional completa** de toda la clave.

---

### Enunciado 1.3: Dependencias Transitivas (3FN) y Descomposición
Partiendo de las tablas resultantes:
- `USUARIOS(dni, nombre, apellidos, direccion)`
- `CURSOS(idcurso, curso, modulo)`
- `USUARIO_CURSOS(dni, idcurso, nota)`

> [!question]- ❓ ¿En qué forma normal se encuentra el esquema descompuesto?
> **Respuesta Correcta**: **3FN y BCNF**.
>
> **Justificación Técnica**:
> - Cada tabla representa una única entidad o relación.
> - No existen atributos multivaluados (1FN).
> - No existen dependencias parciales (2FN).
> - No existen dependencias transitivas entre atributos no clave ($X ightarrow Y ightarrow Z$) (3FN).

---

## 📋 Caso 2: Esquema Comercial Completo y 4FN

Dadas las siguientes tablas:
```sql
Cliente (idCliente, nombre, direccion)
Vendedor (idVendedor, nombre)
Venta (idVenta, Fecha, idCliente, idVendedor)
Articulos (idArticulo, nombre, precio)
ArticulosVendidos (idVenta, idArticulo, cantidad)
```

> [!question]- ❓ ¿En qué Forma Normal se encuentra este esquema? ¿Requiere 4FN?
> **Respuesta Correcta**: Se encuentra en **3FN / BCNF**. No requiere transformaciones para 4FN porque **no existen dependencias multivaluadas independientes** ($X 	woheadrightarrow Y$).

---

## 💻 Caso 3: Sintaxis SQL DDL para Creación de Esquema

> [!question]- ❓ Escribe la sentencia SQL ANSI para crear la tabla `Estudiante` con clave primaria autoincremental:
> ```sql
> CREATE TABLE Estudiante (
>     CodEstudiante INT AUTO_INCREMENT,
>     nombre VARCHAR(120) NOT NULL,
>     CONSTRAINT pk_estudiante PRIMARY KEY (CodEstudiante)
> );
> ```

> [!warning] ⚠️ Trampas Típicas de Examen en Normalización
> 1. **Confundir 2FN con 3FN**: 2FN solo aplica a tablas con **claves primarias compuestas** (si la PK es de un solo atributo y está en 1FN, automáticamente está en 2FN).
> 2. **BCNF vs 3FN**: La 3FN permite $X ightarrow A$ si $A$ es atributo primo; la BCNF exige estrictamente que $X$ sea superclave sin excepciones.
> 3. **4FN**: Se aplica exclusivamente cuando existen **dos o más atributos multivaluados independientes** en la misma relación.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado Relacional y Normalización]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
