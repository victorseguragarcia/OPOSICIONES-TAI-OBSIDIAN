---
title: "Test de Autoevaluación: Bloque 2 - Tema 05 (SGBD Relacionales, NoSQL y Teorema CAP)"
type: "test"
target: "wiki/sources/bloque2-tema05.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - sgbd
  - sql
  - nosql
  - cap-theorem
  - mongodb
  - redis
sources:
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test de Autoevaluación: Bloque 2 - Tema 05 (SGBD Relacionales, NoSQL y Teorema CAP)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 2 - Tema 05 (SGBD Relacionales, NoSQL y Teorema CAP)",
  "questions": [
    {
      "question": "Según el Teorema CAP de Eric Brewer para sistemas distribuidos, ante la presencia inevitable de una partición de red ($P$), ¿qué dos garantías son mutuamente excluyentes?",
      "options": [
        "Atomicidad y Durabilidad.",
        "Consistencia estricta ($C$) y Disponibilidad ($A$).",
        "Rendimiento y Seguridad.",
        "Concurrencia y Aislamiento."
      ],
      "answer": "b",
      "explanation": "El Teorema CAP establece que en un sistema distribuido particionado ($P$) solo se puede garantizar Consistencia ($CP$) o Disponibilidad ($AP$)."
    },
    {
      "question": "¿A qué familia de bases de datos NoSQL pertenece MongoDB, almacenando la información en documentos semiestructurados BSON (JSON binario)?",
      "options": [
        "Clave-Valor.",
        "Documental (*Document-oriented*).",
        "Columnas Anchas (*Wide-Column Store*).",
        "Grafos (*Graph Database*)."
      ],
      "answer": "b",
      "explanation": "MongoDB es el motor NoSQL documental líder y utiliza BSON (*Binary JSON*)."
    },
    {
      "question": "¿Qué modelo alternativo a ACID caracteriza a las bases de datos NoSQL distribuidas de alta disponibilidad (AP) como Apache Cassandra?",
      "options": [
        "Modelo REST.",
        "Modelo BASE (*Basically Available, Soft state, Eventual consistency*).",
        "Modelo ANSI SPARC.",
        "Modelo CRUD."
      ],
      "answer": "b",
      "explanation": "BASE: Disponibilidad básica, estado flexible y consistencia eventual."
    },
    {
      "question": "¿Cuál de los siguientes motores de base de datos NoSQL es un almacén Clave-Valor en memoria RAM de ultra alto rendimiento utilizado frecuentemente para caché y colas de mensajes?",
      "options": [
        "Neo4j.",
        "Redis.",
        "PostgreSQL.",
        "Apache CouchDB."
      ],
      "answer": "b",
      "explanation": "Redis es un almacén Clave-Valor en memoria RAM con soporte para estructuras complejas."
    },
    {
      "question": "En el modelo relacional tradicional, ¿qué propiedad de las transacciones ACID garantiza que las modificaciones realizadas por una transacción confirmada persistan incluso ante fallos catastróficos del sistema?",
      "options": [
        "Atomicidad.",
        "Consistencia.",
        "Aislamiento.",
        "Durabilidad (*Durability*)."
      ],
      "answer": "d",
      "explanation": "Durabilidad asegura que los cambios de un `COMMIT` queden grabados permanentemente en almacenamiento no volátil."
    }
  ]
}
```
