---
title: "Test Tema 05: Componentes Software, Java EE / Jakarta EE y Plataforma .NET"
type: "test"
target: "wiki/sources/bloque3-tema05-componentes-java-dotnet.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - examen-interactivo
  - simulador
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 05: Componentes Software, Java EE / Jakarta EE y Plataforma .NET

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test Tema 05: Componentes Software, Java EE / Jakarta EE y Plataforma .NET",
  "questions": [
    {
      "question": "En la arquitectura Java EE / Jakarta EE, ¿qué tipo de Enterprise JavaBean (EJB) gestiona procesos de negocio con estado persistente asociado a una sesión de usuario concreta?",
      "options": [
        "Stateless Session Bean.",
        "Stateful Session Bean.",
        "Singleton Session Bean.",
        "Message-Driven Bean (MDB)."
      ],
      "answer": "b",
      "explanation": "Stateful Session Beans mantienen el estado conversacional del cliente durante múltiples llamadas a lo largo de una sesión."
    },
    {
      "question": "En el entorno de ejecución de Microsoft .NET Framework y .NET Core, ¿qué componente es el motor de ejecución encargado de compilar el código CIL (Common Intermediate Language) a código máquina nativo mediante compilación JIT?",
      "options": [
        "CLR (Common Language Runtime).",
        "CLS (Common Language Specification).",
        "CTS (Common Type System).",
        "MSBuild."
      ],
      "answer": "a",
      "explanation": "El CLR (Common Language Runtime) administra la memoria (Garbage Collector), seguridad y compilación JIT del código intermedio en .NET."
    },
    {
      "question": "En Java, ¿qué mecanismo de persistencia estándar gestiona el mapeo objeto-relacional (ORM) entre entidades Java y tablas de base de datos relacional?",
      "options": [
        "JSP.",
        "JPA (Java Persistence API / Hibernate).",
        "JNDI.",
        "JAAS."
      ],
      "answer": "b",
      "explanation": "JPA (Java Persistence API) es la especificación estándar de Jakarta EE para el mapeo objeto-relacional (ORM)."
    },
    {
      "question": "¿Qué tipo de EJB se activa de forma asíncrona mediante la llegada de mensajes JMS (Java Message Service)?",
      "options": [
        "Stateless Bean.",
        "Stateful Bean.",
        "Message-Driven Bean (MDB).",
        "Entity Bean."
      ],
      "answer": "c",
      "explanation": "Los MDBs (Message-Driven Beans) actúan como consumidores de mensajes asíncronos desacoplados del emisor."
    },
    {
      "question": "En el marco de desarrollo Spring Framework, ¿qué patrón de diseño fundamental desacopla la creación de dependencias inyectándolas automáticamente en tiempo de ejecución?",
      "options": [
        "Inversión de Control (IoC) / Inyección de Dependencias (DI).",
        "Patrón Command.",
        "Patrón Adapter.",
        "Patrón Memento."
      ],
      "answer": "a",
      "explanation": "El contenedor IoC de Spring administra el ciclo de vida de los beans e inyecta sus dependencias (DI)."
    }
  ]
}
```
