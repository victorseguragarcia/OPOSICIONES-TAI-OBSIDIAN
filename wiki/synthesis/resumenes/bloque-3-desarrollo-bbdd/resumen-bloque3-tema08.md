---
title: "Resumen Exhaustivo Tema 08 (Bloque 3): Control de Versiones con Git y Metodologías Ágiles (Scrum, Kanban)"
type: "synthesis"
tags:
  - resumen
  - resumen-exhaustivo
  - bloque-3
  - tema-08
  - desarrollo
  - bbdd
  - ingenieria-software\nestado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[raw/sources/bloque3-tema08.md]]"
  - "[[wiki/sources/bloque3-tema08]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|⬅️ Tema 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema09|Tema 09 ➡️]]

# 🔴 Resumen Exhaustivo Tema 08 (Bloque 3): Control de Versiones con Git y Metodologías Ágiles (Scrum, Kanban)

> [!repaso] ⚡ **Puntos Clave y Objetivos Oficiales del Tema 08**
> Sistemas de control de versiones centralizados (SVN) vs distribuidos (Git), áreas de trabajo en Git (Working Tree, Staging/Index, Local Repository, Remote), comandos avanzados (merge, rebase, cherry-pick, reset soft/mixed/hard, revert), modelos de ramas (GitFlow) y metodologías ágiles (Manifiesto Ágil, Scrum roles/eventos/artefactos, Kanban y límites WIP).

---

## 🟣 1. Desarrollo Técnico y Metodológico Exhaustivo

### 1. Sistema de Control de Versiones Git
- **Arquitectura de las 3 Áreas Locales + Remoto**:
  1. **Working Directory (Directorio de Trabajo)**: Archivos locales en disco donde se edita el código.
  2. **Staging Area / Index**: Área intermedia donde se preparan los cambios que formarán parte del siguiente commit (`git add`).
  3. **Local Repository (.git)**: Base de datos de objetos (commits, trees, blobs, tags) confirmados localmente (`git commit`).
  4. **Remote Repository**: Repositorio compartido en servidor remoto (`git push` / `git fetch` / `git pull`).
- **Comandos Clave de Operaciones Avanzadas en Git**:
  - `git merge --no-ff <rama>`: Fusiona ramas creando siempre un commit de merge explícito conservando el historial de la rama.
  - `git rebase <rama_base>`: Reaplica los commits de la rama actual encima de la punta de la rama base, generando un **historial lineal y limpio**. ⚠️ *Regla de oro*: No hacer rebase sobre ramas públicas compartidas.
  - `git cherry-pick <hash>`: Aplica un commit específico de otra rama a la rama actual sin fusionar toda la rama.
  - `git reset`: Mueve la referencia de `HEAD`:
    - `--soft`: Mueve `HEAD`, **mantiene los cambios en Staging/Index** y Working Directory.
    - `--mixed` (por defecto): Mueve `HEAD`, **saca los cambios de Staging**, pero los mantiene en Working Directory.
    - `--hard`: Mueve `HEAD` y **destruye todos los cambios** tanto en Staging como en Working Directory.
  - `git revert <hash>`: Crea un **nuevo commit que invierte exactamente los cambios** del commit indicado (seguro para ramas públicas).

### 2. Metodologías Ágiles de Desarrollo: Scrum y Kanban
- **El Manifiesto Ágil (4 Valores Fundamentales)**:
  1. **Individuos e interacciones** sobre procesos y herramientas.
  2. **Software funcionando** sobre documentación extensiva.
  3. **Colaboración con el cliente** sobre negociación contractual.
  4. **Respuesta ante el cambio** sobre seguimiento de un plan.
- **Marco de Trabajo Scrum**:
  - **Los 3 Roles**:
    - *Product Owner*: Responsable de maximizar el valor del producto y gestionar el Product Backlog.
    - *Scrum Master*: Líder servicial que facilita los eventos, elimina impedimentos y asegura el marco Scrum.
    - *Developers (Equipo de Desarrollo)*: Profesionales multidisciplinares y autoorganizados que crean el incremento.
  - **Los 5 Eventos**:
    - *Sprint*: Contenedor temporal fijo de 1 a 4 semanas (habitualmente 2 semanas).
    - *Sprint Planning*: Planificación del trabajo del Sprint (Sprint Goal).
    - *Daily Scrum*: Sincronización diaria de 15 minutos.
    - *Sprint Review*: Inspección del incremento terminado con los interesados (*Demo*).
    - *Sprint Retrospective*: Inspección y mejora continua interna del equipo.
  - **Los 3 Artefactos y sus Compromisos**:
    - *Product Backlog* $\rightarrow$ Compromiso: **Product Goal**.
    - *Sprint Backlog* $\rightarrow$ Compromiso: **Sprint Goal**.
    - *Increment* $\rightarrow$ Compromiso: **Definition of Done (DoD)**.
- **Metodología Kanban**:
  - Basada en el sistema de producción Toyota. Principios: **Visualizar el flujo de trabajo**, **Limitar el trabajo en curso (Límites WIP - Work In Progress)** y gestionar el flujo continuo mediante tarjetas en tablero.

> [!trampa] ⚠️ **Trampas Oficiales del Tribunal en el Tema 08 (Bloque 3)**
> 1. **git reset --soft vs --hard**: `--soft` no pierde nada y deja los cambios en *Staging*; `--hard` destruye y borra todo cambio no confirmado.
> 2. **git revert vs git reset**: `git revert` es seguro en ramas públicas porque **crea un nuevo commit** hacia adelante; `git reset` reescribe el historial hacia atrás.
> 3. **Roles en Scrum**: El *Scrum Master* NO es el jefe de proyecto; es un facilitador. El equipo es autoorganizado.
> 4. **Daily Scrum**: Duración máxima prefijada (*time-box*) de **15 minutos**.

> [!mnemo] 🧠 **Reglas Mnemotécnicas de Retención Visual**
> - **Scrum 3-5-3**: **3 Roles** (PO, SM, Devs), **5 Eventos** (Sprint, Planning, Daily, Review, Retro), **3 Artefactos** (Product Backlog, Sprint Backlog, Increment).
> - **Git Reset**: **Soft (Index) / Mixed (Working) / Hard (Destroy)**.

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Nota Fuente Oficial Completa**: [[wiki/sources/bloque3-tema08|Fuente Oficial del Tema 08]]
- 📚 **Tema Extendido Íntegro**: [[wiki/synthesis/temas-completos/bloque-3-desarrollo-bbdd/tema-completo-bloque3-tema08|Ver Tratado Completo Extendido]]
- 📝 **Test Interactivo de Examen (10 Preguntas)**: [[wiki/tests/temas/test-bloque3-tema08-accesibilidad-wcag-usabilidad|Test Tema 08]]
- 🃏 **Tarjetas de Memoria Rápida (Flashcards)**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque3-desarrollo-bbdd|Mazo Flashcards Bloque 3]]
- 🏠 **Índice del Bloque 3**: [[wiki/synthesis/resumenes/resumen-maestro-bloque3|Resumen Maestro Bloque 3]]

---

> [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema07|⬅️ Tema 07]]  ·  [[wiki/synthesis/resumenes/resumen-maestro-bloque3|🏠 Índice Bloque 3]]  ·  [[wiki/synthesis/resumenes/bloque-3-desarrollo-bbdd/resumen-bloque3-tema09|Tema 09 ➡️]]
