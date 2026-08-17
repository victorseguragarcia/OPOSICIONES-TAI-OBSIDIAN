---
title: "Test de Autoevaluación: Bloque 3 - Tema 01 (Modelado de Datos y Normalización)"
type: "test"
target: "wiki/sources/bloque3-tema01.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-3
  - normalizacion
  - modelo-relacional
  - bcnf
  - dependencias-funcionales
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 01: Modelado de Datos y Formas Normales (1FN a 5FN y BCNF)

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. Una relación está en Segunda Forma Normal (2FN) si y solo si:
- [ ] a) Está en 1FN y no contiene dependencias transitivas entre atributos no primos.
- [ ] b) Está en 1FN y todo atributo no primo tiene dependencia funcional completa de cada una de las claves candidatas.
- [ ] c) Para toda dependencia funcional $X 
ightarrow Y$, $X$ es superclave.
- [ ] d) Todos sus dominios contienen exclusivamente valores atómicos y no existen grupos repetitivos.

### 2. ¿Qué condición define que una relación esté en Tercera Forma Normal (3FN)?
- [ ] a) Está en 2FN y no existen dependencias funcionales transitivas de atributos no primos respecto de la clave primaria.
- [ ] b) No existen dependencias multivaluadas no triviales.
- [ ] c) Está en 1FN y la clave primaria es siempre simple (un solo atributo).
- [ ] d) Todas las claves foráneas tienen integridad referencial en cascada.

### 3. La Forma Normal de Boyce-Codd (BCNF) se diferencia de la 3FN estricta en que:
- [ ] a) Solo aplica a relaciones con claves foráneas compuestas.
- [ ] b) Exige que para TODA dependencia funcional no trivial $X 
ightarrow A$, el determinante $X$ sea superclave (incluso si $A$ es un atributo primo).
- [ ] c) Permite dependencias parciales de atributos primos.
- [ ] d) Requiere la ausencia total de valores nulos (NOT NULL) en toda la tabla.

### 4. ¿Qué tipo de anomalía elimina la Cuarta Forma Normal (4FN)?
- [ ] a) Dependencias parciales de la clave.
- [ ] b) Dependencias transitivas entre no primos.
- [ ] c) Dependencias multivaluadas independientes ($X 	woheadrightarrow Y \mid Z$).
- [ ] d) Dependencias de reunión o producto cartesiano (*join dependencies*).

### 5. En el modelo Entidad/Relación de Chen, ¿cómo se representa gráficamente una relación o interrelación entre entidades?
- [ ] a) Mediante un rectángulo.
- [ ] b) Mediante una elipse u óvalo.
- [ ] c) Mediante un rombo.
- [ ] d) Mediante un hexágono doble.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **a** | 3. **b** | 4. **c** | 5. **c**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: 2FN elimina dependencias funcionales parciales respecto a claves compuestas.
> - **Pregunta 2 (a)**: 3FN exige 2FN y que ningún atributo no primo dependa transitivamente de la clave ($X 
ightarrow Y 
ightarrow Z$).
> - **Pregunta 3 (b)**: En BCNF todo determinante debe ser superclave, sin excepción para atributos primos.
> - **Pregunta 4 (c)**: 4FN trata las dependencias multivaluadas independientes de Fagin ($X 	woheadrightarrow Y$).
> - **Pregunta 5 (c)**: En E/R de Chen: Entidades = Rectángulos, Atributos = Elipses, Relaciones = Rombos.
