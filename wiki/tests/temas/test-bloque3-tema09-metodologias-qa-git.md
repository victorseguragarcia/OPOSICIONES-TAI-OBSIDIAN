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

# 🔴 Test de Autoevaluación: Bloque 3 - Tema 09 (MÉTRICA v3, QA McCabe y Git)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 3 - Tema 09 (MÉTRICA v3, QA McCabe y Git)",
  "questions": [
    {
      "question": "En la metodología oficial del Consejo Superior de Administración Electrónica MÉTRICA Versión 3, ¿cuál es el proceso principal encargado de analizar los requisitos y elaborar el catálogo de requisitos y casos de uso?",
      "options": [
        "EVS (Estudio de Viabilidad del Sistema).",
        "ASI (Análisis del Sistema de Información).",
        "DSI (Diseño del Sistema de Información).",
        "CSI (Construcción del Sistema de Información)."
      ],
      "answer": "b",
      "explanation": "ASI genera el catálogo de requisitos, modelo conceptual de datos y especificación de casos de uso."
    },
    {
      "question": "¿Cuál es la fórmula para calcular la Complejidad Ciclomática $V(G)$ de McCabe a partir del grafo de flujo con $E$ aristas, $N$ nodos y $P=1$ componentes conexos?",
      "options": [
        "$V(G) = E + N - 2$",
        "$V(G) = E - N + 2 = D + 1$ (donde $D$ es el número de nodos de decisión/predicado)",
        "$V(G) = E \times N / 2$",
        "$V(G) = N - E + 1$"
      ],
      "answer": "b",
      "explanation": "McCabe: $V(G) = E - N + 2P = D + 1$."
    },
    {
      "question": "En el marco ágil Scrum, ¿quién es el responsable exclusivo de gestionar, priorizar y ordenar los elementos del Product Backlog?",
      "options": [
        "El Scrum Master.",
        "El Product Owner.",
        "El Equipo de Desarrollo (Developers).",
        "El Project Manager."
      ],
      "answer": "b",
      "explanation": "El Product Owner maximiza el valor del producto y es el único dueño del Product Backlog."
    },
    {
      "question": "¿Qué tipo de pruebas de software verifican que las modificaciones o correcciones recientes en el código no hayan introducido errores involuntarios en funcionalidades existentes previamente operativas?",
      "options": [
        "Pruebas Unitarias.",
        "Pruebas de Estrés.",
        "Pruebas de Regresión.",
        "Pruebas de Humo (*Smoke Tests*)."
      ],
      "answer": "c",
      "explanation": "Las pruebas de regresión aseguran que los cambios no rompan funcionalidades ya validadas."
    },
    {
      "question": "En el sistema de control de versiones Git, ¿qué comando traslada los cambios confirmados de la rama de trabajo actual a la rama destino aplicando los commits uno a uno encima del historial de la rama base?",
      "options": [
        "`git merge --no-ff`",
        "`git rebase`",
        "`git cherry-pick`",
        "`git stash pop`"
      ],
      "answer": "b",
      "explanation": "`git rebase` reescribe la base de la rama actual situándola sobre el commit más reciente de la rama base."
    }
  ]
}
```
