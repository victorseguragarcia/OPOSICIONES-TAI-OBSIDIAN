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

# 🔴 Test de Autoevaluación: Bloque 3 - Tema 01 (Modelado de Datos y Normalización)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 3 - Tema 01 (Modelado de Datos y Normalización)",
  "questions": [
    {
      "question": "Una relación está en Segunda Forma Normal (2FN) si y solo si:",
      "options": [
        "Está en 1FN y no contiene dependencias transitivas entre atributos no primos.",
        "Está en 1FN y todo atributo no primo tiene dependencia funcional completa de cada una de las claves candidatas.",
        "Para toda dependencia funcional $X",
        "Todos sus dominios contienen exclusivamente valores atómicos y no existen grupos repetitivos."
      ],
      "answer": "b",
      "explanation": "2FN elimina dependencias funcionales parciales respecto a claves compuestas."
    },
    {
      "question": "¿Qué condición define que una relación esté en Tercera Forma Normal (3FN)?",
      "options": [
        "Está en 2FN y no existen dependencias funcionales transitivas de atributos no primos respecto de la clave primaria.",
        "No existen dependencias multivaluadas no triviales.",
        "Está en 1FN y la clave primaria es siempre simple (un solo atributo).",
        "Todas las claves foráneas tienen integridad referencial en cascada."
      ],
      "answer": "a",
      "explanation": "3FN exige 2FN y que ningún atributo no primo dependa transitivamente de la clave ($X"
    },
    {
      "question": "La Forma Normal de Boyce-Codd (BCNF) se diferencia de la 3FN estricta en que:",
      "options": [
        "Solo aplica a relaciones con claves foráneas compuestas.",
        "Exige que para TODA dependencia funcional no trivial $X",
        "Permite dependencias parciales de atributos primos.",
        "Requiere la ausencia total de valores nulos (NOT NULL) en toda la tabla."
      ],
      "answer": "b",
      "explanation": "En BCNF todo determinante debe ser superclave, sin excepción para atributos primos."
    },
    {
      "question": "¿Qué tipo de anomalía elimina la Cuarta Forma Normal (4FN)?",
      "options": [
        "Dependencias parciales de la clave.",
        "Dependencias transitivas entre no primos.",
        "Dependencias multivaluadas independientes ($X \twoheadrightarrow Y \\mid Z$).",
        "Dependencias de reunión o producto cartesiano (*join dependencies*)."
      ],
      "answer": "c",
      "explanation": "4FN trata las dependencias multivaluadas independientes de Fagin ($X \twoheadrightarrow Y$)."
    },
    {
      "question": "En el modelo Entidad/Relación de Chen, ¿cómo se representa gráficamente una relación o interrelación entre entidades?",
      "options": [
        "Mediante un rectángulo.",
        "Mediante una elipse u óvalo.",
        "Mediante un rombo.",
        "Mediante un hexágono doble."
      ],
      "answer": "c",
      "explanation": "En E/R de Chen: Entidades = Rectángulos, Atributos = Elipses, Relaciones = Rombos."
    }
  ]
}
```
