---
title: "Resumen Exhaustivo Tema 01 (Bloque 3): Diseño y Normalización de Bases de Datos (1FN a 5FN, BCNF)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-01
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema01.md]]"
  - "[[wiki/sources/bloque3-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Portada Bloque 3]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|Tema 02 ➡️]]

# 🔴 Resumen Exhaustivo Tema 01 (Bloque 3): Diseño y Normalización de Bases de Datos (1FN a 5FN, BCNF)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 01**
> Modelo Entidad-Relación (E/R extendido), paso del modelo E/R al modelo relacional, dependencias funcionales, formas normales de Codd (1FN, 2FN, 3FN), Forma Normal de Boyce-Codd (BCNF), dependencias multivaluadas y 4FN, y 5FN.

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Modelo Entidad-Relación y Transformación al Modelo Relacional
- **Elementos del Modelo E/R Extendido de Chen**:
  - *Entidades*: Fuertes (existencia independiente con clave primaria propia) vs Débiles (dependencia de existencia o en identificación de una entidad fuerte).
  - *Atributos*: Simples, Compuestos, Monovalorados, Multivalorados (doble elipse), Derivados/Calculados (elipse discontinua).
  - *Relaciones y Cardinalidad*: Binarias, Ternarias o Reflexivas (recursivas). Cardinalidades: $1:1$, $1:N$, $N:M$.
- **Reglas Estándar de Transformación al Modelo Relacional**:
  - *Relación $1:N$*: Se propaga la clave primaria del lado $1$ como **clave foránea (FK)** a la tabla del lado $N$.
  - *Relación $N:M$*: Se transforma en una **nueva tabla intermedia** cuya clave primaria compuesta está formada por las claves foráneas de ambas entidades.
  - *Relación $1:1$*: Se propaga la PK de cualquiera de las entidades como FK a la otra (preferentemente hacia la entidad con participación total) añadiendo restricción `UNIQUE`.
  - *Atributos Multivalorados*: Se crea una nueva tabla con el atributo y la PK de la entidad propietaria como FK.

### 2. Formas Normales de Codd y BCNF

| Forma Normal | Requisitos y Condiciones Estrictas | Anomalía que Elimina / Corrige |
|:---|:---|:---|
| **Primera Forma Normal (1FN)** | • Todos los atributos deben ser **atómicos e indivisibles** (sin grupos repetitivos ni arrays dentro de una columna).<br>• Existencia de una clave primaria única. | Elimina redundancia por repetición de atributos y columnas multivaloradas. |
| **Segunda Forma Normal (2FN)** | • Está en **1FN**.<br>• Todos los atributos no principales tienen **dependencia funcional completa** de la clave primaria (ningún atributo no clave depende de una parte de una clave primaria compuesta).<br>*(Si la PK es simple de un solo campo, 1FN $\rightarrow$ 2FN es automática)*. | Elimina redundancias debidas a dependencias funcionales parciales. |
| **Tercera Forma Normal (3FN)** | • Está en **2FN**.<br>• **Ningún atributo no clave depende transitivamente de la clave primaria** ($X \rightarrow Y$ y $Y \rightarrow Z$, con $Z$ dependiendo de $X$ a través de $Y$).<br>• Formalmente: Para toda $X \rightarrow A$, o bien $X$ es superclave, o bien $A$ es atributo principal. | Elimina anomalías de inserción, borrado y modificación causadas por dependencias transitivas. |
| **Forma Normal de Boyce-Codd (BCNF / FNBC)** | • Versión estricta de 3FN.<br>• Para **TODA dependencia funcional no trivial $X \rightarrow A$, el determinante $X$ debe ser estrictamente una SUPERCLAVE**. | Resuelve solapamientos de claves candidatas compuestas no detectados en 3FN. |
| **Cuarta Forma Normal (4FN)** | • Está en **BCNF**.<br>• No existen **dependencias multivaluadas no triviales ($X \twoheadrightarrow Y$)** a menos que $X$ sea superclave (Teorema de Fagin). | Elimina redundancias causadas por atributos independientes multivalued. |
| **Quinta Forma Normal (5FN / PJNF)** | • Está en **4FN**.<br>• No existen **dependencias de unión (Join Dependencies)** que no estén implícitas en las superclaves. | Garantiza descomposición sin pérdida (Lossless-Join) en relaciones ternarias. |

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 01 (Bloque 3)**
> 1. **Paso a 2FN con Clave Simple**: Si una tabla está en 1FN y su **clave primaria es de un solo atributo**, pasa **automáticamente a 2FN** (no pueden existir dependencias parciales).
> 2. **3FN vs BCNF**: En 3FN se permite que $A$ sea atributo primo; en **BCNF el determinante $X$ DEBE ser obligatoriamente superclave**, sin excepciones.
> 3. **4FN**: Se aplica a **dependencias multivaluadas** ($X \twoheadrightarrow Y$), no funcionales simples.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Las 3 Primeras Formas Normales**:
>   - **1FN**: Atributos **Atómicos** (sin listas).
>   - **2FN**: Dependencia **Completa** (sin dependencias parciales).
>   - **3FN**: Sin dependencia **Transitiva**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema01|Fuente Oficial del Tema 01]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema01|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema01-normalizacion-bbdd|Test Tema 01]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Portada Bloque 3]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema02|Tema 02 ➡️]]
