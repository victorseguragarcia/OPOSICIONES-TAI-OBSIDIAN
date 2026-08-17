---
title: "Plataforma Java, JVM y Ecosistema Spring"
type: "entity"
tags:
  - java
  - jvm
  - spring
  - bytecode
  - garbage-collector
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Java"
  - "JVM"
  - "Spring Boot"
---

# Plataforma Java, JVM y Ecosistema Spring

Plataforma de desarrollo empresarial orientada a objetos basada en el paradigma *"Write Once, Run Anywhere"* mediante la compilación de código fuente a **Bytecode** ejecutado por la **JVM**.

---

## 🏛️ Arquitectura de Memoria de la JVM

- **Stack (Pila)**: Hilos de ejecución, variables primitivas locales y referencias a objetos.
- **Heap (Montículo)**: Almacén de objetos gestionado por el **Garbage Collector (GC)**.
  - *Young Generation*: Eden + Survivor Spaces (S0/S1). Limpiado por *Minor GC*.
  - *Old Generation (Tenured)*: Objetos de larga vida. Limpiado por *Major/Full GC*.
  - *Metaspace (Java 8+)*: Metadatos de clases en memoria nativa del sistema operativo.
- **Ecosistema**: **Spring Boot** con Inversión de Control (IoC) e Inyección de Dependencias (DI).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema03|Resumen Bloque 3 - Tema 03]]
- Entidad: [[wiki/entities/git-version-control-system|Git]]
