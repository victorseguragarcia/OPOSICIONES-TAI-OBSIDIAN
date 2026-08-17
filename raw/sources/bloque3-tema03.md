---
title: "Bloque 3 - Tema 03: Lenguajes de Programación, Plataforma Java y Control de Versiones con Git"
type: "raw-source"
topic: "lenguajes-java-git"
date: "2026-08-17"
---

# Bloque 3 - Tema 03: Lenguajes de Programación, Paradigmas, Plataforma Java / JVM y Control de Versiones Distribuido con Git

## 1. Paradigmas y Lenguajes de Programación
- **Imperativo / Estructurado**: Basado en secuencias de órdenes, instrucciones de control de flujo y estados mutables (C, Pascal).
- **Orientado a Objetos (POO)**: Basado en objetos que encapsulan estado y comportamiento (Java, C++, C#, Python).
- **Funcional**: Basado en funciones matemáticas puras sin efectos secundarios ni mutabilidad de variables (Haskell, Lisp, Scala, funciones Lambda en Java/Python).
- **Declarativo / Lógico**: Se describe el resultado deseado sin detallar el flujo de control paso a paso (SQL, Prolog).

## 2. La Plataforma Java y la Máquina Virtual (JVM)
- **Filosofía**: *"Write Once, Run Anywhere"* (WORA). El código fuente (`.java`) es compilado por `javac` a código intermedio multiplataforma denominado **Bytecode** (`.class`), ejecutado por la **JVM (Java Virtual Machine)**.
- **Componentes**:
  - **JDK (Java Development Kit)**: Herramientas de compilación, depuración y librerías para desarrolladores.
  - **JRE (Java Runtime Environment)**: Entorno mínimo para ejecutar aplicaciones Java (contiene la JVM y librerías estándar).
  - **JIT (Just-In-Time Compiler)**: Compila partes frecuentes de bytecode a código máquina nativo en tiempo de ejecución para máximo rendimiento.
- **Gestión de Memoria y Recolector de Basura (Garbage Collector - GC)**:
  - **Stack (Pila)**: Almacena referencias a objetos, llamadas a métodos y variables primitivas locales. Rápida y de gestión automática por ámbito.
  - **Heap (Montículo)**: Almacena todos los objetos e instancias creadas con `new`. Gestionado por el GC.
    - *Young Generation*: Eden y Survivor Spaces (S0/S1). Objetos nuevos; se limpian mediante *Minor GC*.
    - *Old Generation (Tenured)*: Objetos que han sobrevivido a varios ciclos de recolección; se limpian mediante *Major GC / Full GC*.
    - *Metaspace (desde Java 8)*: Memoria nativa para metadatos de clases (reemplazó al antiguo *PermGen*).
- **Tipos de Datos en Java**: Primitivos (byte, short, int, long, float, double, boolean, char) y por Referencia (Objetos, Arrays, Interfaces).
- **Frameworks Empresariales**: **Spring Framework** e **Inversión de Control (IoC) / Inyección de Dependencias (DI)**; **Spring Boot** para microservicios y APIs REST; **JPA (Java Persistence API) / Hibernate** para mapeo objeto-relacional (ORM).

## 3. Control de Versiones Distribuido con Git
Git es un sistema de control de versiones distribuido (DVCS) creado por Linus Torvalds en 2005. Cada desarrollador tiene un clon completo del repositorio local con todo el historial.
- **Las Tres Zonas de Git**:
  1. **Working Directory (Directorio de Trabajo)**: Archivos locales que se están editando.
  2. **Staging Area / Index (Área de Preparación)**: Zona intermedia donde se seleccionan los cambios antes de confirmar (`git add`).
  3. **Local Repository (Repositorio Local / `.git`)**: Base de datos de objetos y commits confirmados (`git commit`).
  - *Remote Repository*: Servidor remoto compartido (GitHub, GitLab, Bitbucket) sincronizado mediante `git push` y `git fetch/pull`.
- **Comandos Esenciales de Git**:
  - `git init`: Inicializa un nuevo repositorio local.
  - `git clone <url>`: Clona un repositorio remoto.
  - `git status` y `git diff`: Muestra el estado del árbol de trabajo y las diferencias.
  - `git add <archivo>` o `git add .`: Añade archivos al área de Staging.
  - `git commit -m "mensaje"`: Registra una instantánea de los cambios en el historial local.
  - `git branch <nombre>` / `git checkout -b <nombre>` / `git switch -c <nombre>`: Gestión de ramas.
  - `git merge <rama>`: Fusiona una rama en la rama actual creando un commit de merge (o *fast-forward*).
  - `git rebase <rama>`: Reescribe la base de la rama actual situándola sobre el extremo de otra rama, creando un historial lineal y limpio.
  - `git cherry-pick <commit-hash>`: Aplica un commit específico de otra rama en la rama actual.
  - `git stash` / `git stash pop`: Guarda temporalmente cambios sin confirmar en una pila auxiliar.
  - `git reset` (soft, mixed, hard) y `git revert` (crea un nuevo commit que deshace los cambios sin alterar el historial).
- **Modelo de Ramas GitFlow**:
  - `main` / `master` (código en producción).
  - `develop` (integración de desarrollo).
  - `feature/*` (nuevas características).
  - `release/*` (preparación de versiones).
  - `hotfix/*` (parches urgentes sobre producción).
