---
title: "Resumen Completo Tema 01 (Bloque 3): Diseño y Normalización de Bases de Datos (1FN a 5FN, BCNF)"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-3
  - tema-01
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque3-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Portada Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|Tema 02 ➡️]]

# 🔴 Resumen Completo Tema 01 (Bloque 3): Diseño y Normalización de Bases de Datos (1FN a 5FN, BCNF)

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 01**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

# 🔴 Resumen Fuente: Bloque 3 - Tema 01 (UD012107): Modelado de Datos, Modelo E/R, Diseño Relacional y Normalización

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque3-tema01-modelado-datos-bbdd.md|bloque3-tema01-modelado-datos-bbdd.md]] (90 páginas).

---

## 📖 1. Arquitectura ANSI/SPARC y Fases de Diseño de BBDD

### Arquitectura de 3 Niveles ANSI/SPARC:
1. **Nivel Externo**: Esquemas de usuario (vistas parciales y adaptadas a cada perfil o aplicación).
2. **Nivel Conceptual**: Esquema global lógico independiente del SGBD físico (entidades, relaciones y restricciones).
3. **Nivel Interno / Físico**: Estructuras de almacenamiento en disco, métodos de acceso, índices y organización de archivos.
- **Independencia Lógica**: Capacidad de modificar el esquema conceptual sin alterar los esquemas externos.
- **Independencia Física**: Capacidad de modificar el esquema interno (añadir índices, reorganizar ficheros) sin alterar el esquema conceptual.

---

## 🟣 2. Modelo Entidad-Relación Extendido (E/R de Peter Chen)

- **Entidades**:
  - **Fuertes (Regulares)**: Poseen existencia propia e identificación unívoca mediante su clave primaria.
  - **Débiles**: Dependen de otra entidad para existir (dependencia de existencia) o para identificarse (dependencia de identificación, representada con doble rectángulo).
- **Atributos**:
  - *Simples* (atómicos) vs *Compuestos* (ej. dirección compuesta por calle, número y CP).
  - *Monovaluados* vs *Multivaluados* (ej. varios teléfonos de un usuario, representados con doble elipse).
  - *Derivados / Calculados* (ej. edad calculada a partir de la fecha de nacimiento, elipse con trazo discontinuo).
- **Relaciones y Cardinalidad**:
  - Notación `(min, max)`: Participación obligatoria `(1, 1)` o `(1, N)` vs opcional `(0, 1)` o `(0, N)`.
- **Jerarquías de Generalización / Especialización**:
  - **Total**: Toda instancia de la superclase debe pertenecer obligatoriamente a alguna subclase.
  - **Parcial**: Pueden existir instancias de la superclase que no pertenezcan a ninguna subclase.
  - **Exclusiva (Disjunta)**: Una instancia puede pertenecer como máximo a una subclase.
  - **Solapada (Superpuesta)**: Una instancia puede pertenecer simultáneamente a varias subclases.

---

## 🔵 3. Reglas de Transformación del Modelo E/R al Modelo Relacional

| Elemento / Tipo de Relación | Regla Formal de Transformación Relacional |
|-----------------------------|-------------------------------------------|
| **Entidad Fuerte** | Se convierte en una **Tabla**, cuyos atributos son las columnas y la clave primaria (PK) es el identificador principal. |
| **Relación 1:N** | Se **propaga la clave primaria** del lado 1 como **clave foránea (FK)** en la tabla del lado N. |
| **Relación M:N** | Se genera una **nueva tabla** intermedia cuya clave primaria compuesta está formada por las claves foráneas de ambas entidades. |
| **Relación 1:1** | Se propaga la clave primaria de cualquiera de las entidades a la otra (preferentemente hacia la entidad con participación obligatoria `(1,1)`). |
| **Atributo Multivaluado** | Se crea una **tabla separada** que contiene el atributo multivaluado y la clave primaria de la entidad propietaria como clave foránea. |
| **Jerarquía (Opción A: Tabla Única)** | Una sola tabla con todos los atributos de la superclase y subclases, más un campo **discriminador** (genera nulos). |
| **Jerarquía (Opción B: Superclase + Subclases)** | Tabla para la superclase (con atributos comunes) y tablas para subclases (con atributos específicos y PK=FK apuntando a la superclase). |

---

## 🔵 4. Teoría de la Normalización y Formas Normales (1FN a 5FN)

### Definición de Dependencia Funcional (DF):
Dado un esquema $R$, existe una dependencia funcional $X 
ightarrow Y$ si y solo si para cualquier par de tuplas $t_1, t_2 \in R$, si $t_1[X] = t_2[X]$ entonces $t_1[Y] = t_2[Y]$.

```
  1FN ──> 2FN ──> 3FN ──> BCNF (Boyce-Codd) ──> 4FN ──> 5FN
```

1. **Primera Forma Normal (1FN)**:
   - Todos los atributos son atómicos (valores indivisibles).
   - No existen grupos repetitivos ni atributos multivaluados.
2. **Segunda Forma Normal (2FN)**:
   - Cumple 1FN.
   - Todo atributo no principal posee **dependencia funcional completa** respecto a cada clave candidata (elimina dependencias parciales de claves compuestas).
3. **Tercera Forma Normal (3FN)**:
   - Cumple 2FN.
   - Ningún atributo no principal depende **transitivamente** de una clave candidata ($X 
ightarrow Y 
ightarrow Z$).
   - Condición formal: Para toda DF no trivial $X 
ightarrow A$, $X$ es superclave o $A$ es un atributo primo (pertenece a alguna clave candidata).
4. **Forma Normal de Boyce-Codd (BCNF / FNBC)**:
   - Condición formal más estricta: Para **toda** dependencia funcional no trivial $X 
ightarrow A$, $X$ debe ser **superclave**.
5. **Cuarta Forma Normal (4FN)**:
   - Cumple BCNF y no contiene **dependencias multivaluadas (MVD)** no triviales ($X 	woheadrightarrow Y$).
6. **Quinta Forma Normal (5FN / Proyección-Unión)**:
   - No puede descomponerse en esquemas menores sin pérdida mediante **dependencias de unión (Join Dependencies)**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Definición de Examen |
|----------|----------------------|
| **Clave Candidata** | Conjunto mínimo de atributos que identifica unívocamente a cada tupla en una relación. |
| **Clave Primaria (PK)** | Clave candidata elegida por el diseñador como identificador principal (no admite nulos). |
| **Clave Foránea (FK)** | Atributo en una relación que hace referencia a la clave primaria de otra (o de la misma) relación. |
| **Integridad de Entidad** | Ningún componente de la clave primaria puede tener valor nulo (`NOT NULL`). |
| **Integridad Referencial** | El valor de una clave foránea debe coincidir con un valor de clave primaria existente o ser nulo. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/relational-database-modeling-and-normalization|Modelado de Datos Relacional y Normalización]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias Funcionales]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización de BBDD y SQL]]

> [!trampa] ⚠️ Trampas Frecuentes de Examen: Normalización de Bases de Datos
> 1. **Diferencia Crítica entre 3FN y BCNF (Boyce-Codd)**: En 3FN se permite que para una dependencia funcional $X 
ightarrow A$, si $X$ no es superclave, $A$ sea un **atributo primo** (parte de alguna clave candidata). En **BCNF NO HAY EXCEPCIONES**: **TODO determinante $X$ debe ser obligatoriamente una superclave**.
> 2. **2FN (Segunda Forma Normal)**: Exige estar en 1FN y que **no existan dependencias funcionales parciales** (los atributos no primos deben depender de la TOTALIDAD de la clave primaria, no de una parte). Ojo: Si la clave primaria es simple (de 1 solo atributo), la tabla en 1FN **está automáticamente en 2FN**.
> 3. **4FN (Cuarta Forma Normal)**: Elimina las **dependencias multivaluadas (DMV)** no triviales ($X 	woheadrightarrow Y$).

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque3-tema01|Nota Fuente del Tema 01]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema01-normalizacion-bbdd|Test Tema 01]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Portada Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|Tema 02 ➡️]]
