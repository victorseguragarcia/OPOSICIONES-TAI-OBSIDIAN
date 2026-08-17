---
title: "Resumen Fuente: Bloque 3 - Tema 03: Lenguajes, Plataforma Java/JVM y Git"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema03
  - java
  - jvm
  - git
  - control-versiones
  - spring
sources:
  - "raw/sources/bloque3-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes, Java y Git"
  - "bloque3-tema03"
---

# Resumen Fuente: Bloque 3 - Tema 03: Lenguajes, Plataforma Java/JVM y Git

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema03.md|bloque3-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema analiza los lenguajes de programación y herramientas de desarrollo: los paradigmas (imperativo, POO, funcional y declarativo), la arquitectura de la **Plataforma Java / JVM** (*WORA*, Bytecode `.class`, compilador JIT, gestión de memoria Stack vs Heap con Young/Old Generation y Metaspace, y recolector de basura Garbage Collector), el ecosistema empresarial con **Spring Boot** (Inversión de Control e Inyección de Dependencias) y JPA/Hibernate, y el sistema de control de versiones distribuido **Git** (las tres zonas: Working Tree, Staging Area y Repositorio Local; comandos esenciales, diferencias entre `git merge` y `git rebase`, y el modelo de ramas GitFlow).

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Comando | Especificación Técnica |
|--------------------|------------------------|
| **Java Bytecode** | Código intermedio ejecutable por la **JVM** (`.class` generado por `javac`) |
| **Java Heap vs Stack** | **Heap**: Objetos e instancias gestionados por GC \| **Stack**: Variables locales y llamadas |
| **Spring IoC / DI** | Inversión de Control delegando la creación y enlace de objetos al contenedor Spring |
| **Git: Staging Area (Index)** | Zona intermedia donde se preparan los cambios con `git add` antes del commit |
| **`git rebase` vs `git merge`** | `rebase`: Reescribe la base creando un historial lineal \| `merge`: Crea un commit de unión |
| **`git cherry-pick`** | Aplica un commit específico de otra rama sobre la rama actual |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/java-platform-and-jvm|Plataforma Java, JVM y Ecosistema Spring]]
- Entidad: [[wiki/entities/git-version-control-system|Sistema de Control de Versiones Git]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
