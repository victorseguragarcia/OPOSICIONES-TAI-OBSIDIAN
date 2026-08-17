---
title: "Modelado de Datos Relacional, Modelo E/R y Normalización Rigurosa"
type: "entity"
tags:
  - modelado-datos
  - bases-datos
  - modelo-er
  - normalizacion
  - armstrong
  - sql
sources:
  - "raw/sources/bloque3-tema01-modelado-datos-bbdd.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Modelado Relacional y Normalización"
  - "Teoría de Normalización y Armstrong"
---

# Modelado de Datos Relacional, Modelo E/R y Normalización Rigurosa

El modelado relacional estructura los datos mediante relaciones (tablas) formadas por tuplas (filas) y atributos (columnas), garantizando la integridad de entidad e integridad referencial y eliminando redundancias mediante la teoría formal de la normalización.

---

## 🏛️ 1. Fases del Diseño de Bases de Datos

```
[ Requisitos de Negocio ]
           │
           ▼
1. DISEÑO CONCEPTUAL ──> Modelo Entidad-Relación (E/R de Chen)
           │             • Entidades (fuertes / débiles)
           │             • Atributos (simples, compuestos, multivaluados, derivados)
           │             • Relaciones (1:1, 1:N, M:N; cardinalidades mín/máx)
           ▼
2. DISEÑO LÓGICO ──────> Transformación al Modelo Relacional (Codd)
           │             • Tablas, Claves Primarias (PK), Claves Foráneas (FK)
           │             • Aplicación de Reglas de Normalización (1FN a BCNF)
           ▼
3. DISEÑO FÍSICO ──────> Estructuras de Almacenamiento en RDBMS
                         • Espacios de tablas (Tablespaces), Particionamiento
                         • Índices (B-Tree, Bitmap, Hash), Clústeres
```

---

## 📐 2. Axiomas de Armstrong (Reglas de Inferencia de Dependencias Funcionales)

Dado un conjunto de dependencias funcionales $F$, las reglas de Armstrong permiten derivar el cierre $F^+$:

1. **Axioma de Reflexividad**: Si $Y \subseteq X$, entonces $X ightarrow Y$.
2. **Axioma de Aumento**: Si $X ightarrow Y$, entonces $XZ ightarrow YZ$.
3. **Axioma de Transitividad**: Si $X ightarrow Y$ y $Y ightarrow Z$, entonces $X ightarrow Z$.

### Reglas Derivadas:
- **Unión (Aditividad)**: Si $X ightarrow Y$ y $X ightarrow Z$, entonces $X ightarrow YZ$.
- **Descomposición (Proyectividad)**: Si $X ightarrow YZ$, entonces $X ightarrow Y$ y $X ightarrow Z$.
- **Pseudotransitividad**: Si $X ightarrow Y$ y $WY ightarrow Z$, entonces $WX ightarrow Z$.

---

## 📋 3. Formas Normales (1FN a 5FN)

| Forma Normal | Condición Rigurosa de Examen | Anomalía que Elimina |
|--------------|------------------------------|----------------------|
| **1FN** | Todos los dominios de los atributos son **atómicos** (valores escalares indivisibles, sin arrays ni tablas anidadas). | Multivalores y grupos repetitivos |
| **2FN** | Cumple 1FN y **todo atributo no principal tiene dependencia funcional completa de cada clave candidata** (no depende de un subconjunto propio de una clave compuesta). | Dependencias parciales |
| **3FN** | Cumple 2FN y **ningún atributo no principal depende transitivamente de ninguna clave** (para todo $X ightarrow A$, $X$ es superclave o $A$ es atributo primo). | Dependencias transitivas ($X ightarrow Y ightarrow Z$) |
| **BCNF (Boyce-Codd)** | Para **toda** dependencia funcional no trivial $X ightarrow A$, $X$ es una **superclave** (clave candidata). | Anomalías en claves candidatas compuestas solapadas |
| **4FN** | Cumple BCNF y para toda **dependencia multivaluada** $X 	woheadrightarrow Y$ no trivial, $X$ es superclave. | Redundancia por atributos multivaluados independientes |
| **5FN (Proyección-Unión)** | Cumple 4FN y no puede descomponerse en esquemas menores sin perder información mediante **dependencias de unión (JD)**. | Anomalías de unión en relaciones $N$-arias ($N \ge 3$) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema01|Resumen Bloque 3 - Tema 01]]
- Concepto: [[wiki/concepts/normalization-and-normal-forms|Formas Normales y Dependencias]]
- Síntesis: [[wiki/synthesis/database-normalization-and-sql-cheatsheet|Cheatsheet de Normalización y SQL]]
