---
title: "Test de Autoevaluación: Bloque 3 - Tema 09 (MÉTRICA v3, QA McCabe y Git)"
type: "test"
target: "wiki/sources/bloque3-tema09.md"
date: "2026-08-18"
score: ""
tags:
  - test
  - bloque-3
  - metrica-v3
  - qa
  - mccabe
  - git
sources:
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-18"
updated: "2026-08-18"
---

# 🔴 Test Tema 09: Metodologías (MÉTRICA v3, Scrum), Pruebas QA y Git

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. En la metodología oficial del Consejo Superior de Administración Electrónica MÉTRICA Versión 3, ¿cuál es el proceso principal encargado de analizar los requisitos y elaborar el catálogo de requisitos y casos de uso?
- [ ] a) EVS (Estudio de Viabilidad del Sistema).
- [ ] b) ASI (Análisis del Sistema de Información).
- [ ] c) DSI (Diseño del Sistema de Información).
- [ ] d) CSI (Construcción del Sistema de Información).

### 2. ¿Cuál es la fórmula para calcular la Complejidad Ciclomática $V(G)$ de McCabe a partir del grafo de flujo con $E$ aristas, $N$ nodos y $P=1$ componentes conexos?
- [ ] a) $V(G) = E + N - 2$
- [ ] b) $V(G) = E - N + 2 = D + 1$ (donde $D$ es el número de nodos de decisión/predicado)
- [ ] c) $V(G) = E 	imes N / 2$
- [ ] d) $V(G) = N - E + 1$

### 3. En el marco ágil Scrum, ¿quién es el responsable exclusivo de gestionar, priorizar y ordenar los elementos del Product Backlog?
- [ ] a) El Scrum Master.
- [ ] b) El Product Owner.
- [ ] c) El Equipo de Desarrollo (Developers).
- [ ] d) El Project Manager.

### 4. ¿Qué tipo de pruebas de software verifican que las modificaciones o correcciones recientes en el código no hayan introducido errores involuntarios en funcionalidades existentes previamente operativas?
- [ ] a) Pruebas Unitarias.
- [ ] b) Pruebas de Estrés.
- [ ] c) Pruebas de Regresión.
- [ ] d) Pruebas de Humo (*Smoke Tests*).

### 5. En el sistema de control de versiones Git, ¿qué comando traslada los cambios confirmados de la rama de trabajo actual a la rama destino aplicando los commits uno a uno encima del historial de la rama base?
- [ ] a) `git merge --no-ff`
- [ ] b) `git rebase`
- [ ] c) `git cherry-pick`
- [ ] d) `git stash pop`

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **b** | 3. **b** | 4. **c** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: ASI genera el catálogo de requisitos, modelo conceptual de datos y especificación de casos de uso.
> - **Pregunta 2 (b)**: McCabe: $V(G) = E - N + 2P = D + 1$.
> - **Pregunta 3 (b)**: El Product Owner maximiza el valor del producto y es el único dueño del Product Backlog.
> - **Pregunta 4 (c)**: Las pruebas de regresión aseguran que los cambios no rompan funcionalidades ya validadas.
> - **Pregunta 5 (b)**: `git rebase` reescribe la base de la rama actual situándola sobre el commit más reciente de la rama base.
