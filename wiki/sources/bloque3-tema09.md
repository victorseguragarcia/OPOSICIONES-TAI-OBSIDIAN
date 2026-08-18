---
title: "Resumen Fuente: Bloque 3 - Tema 09 (UD012116): Repositorios, Metodologías, Pruebas y Git"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema09
  - metrica-v3
  - scrum
  - testing
  - git
  - cicd
sources:
  - "raw/sources/bloque3-tema09-metodologias-pruebas-git.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Metodologías, Pruebas y Git"
  - "bloque3-tema09"
---

# Resumen Fuente: Bloque 3 - Tema 09 (UD012116): Repositorios, Metodologías, Pruebas y Git

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema09-metodologias-pruebas-git.md|bloque3-tema09-metodologias-pruebas-git.md]] (124 páginas).

---

## 📖 Resumen Ejecutivo

Este tema engloba la ingeniería de desarrollo colaborativo: los modelos de ciclo de vida (**MÉTRICA v3** con sus procesos PSI, EVS, ASI, DSI, CSI, IAS y marcos ágiles **Scrum**, **Kanban** y **XP**), las técnicas y niveles de **Pruebas de Software** (Unitarias, Integración, Sistema, Aceptación, Regresión; Caja Blanca con la métrica de **Complejidad Ciclomática de McCabe** $V(G) = E - N + 2P$ y Caja Negra con particiones y valores límite), y los sistemas de control de versiones y plataformas colaborativas (**Git** con sus tres zonas, ramas, merge/rebase, GitFlow y pipelines **CI/CD** con Jenkins y SonarQube).

---

## 🎯 Datos Clave para Oposiciones TAI

| Proceso / Herramienta | Función / Fórmula |
|-----------------------|-------------------|
| **Métrica v3 Procesos** | **PSI**, **EVS**, **ASI**, **DSI**, **CSI**, **IAS** |
| **Complejidad de McCabe** | **$V(G) = E - N + 2P = 	ext{Nodos Predicado} + 1$** |
| **Zonas de Git** | **Working Directory** $
ightarrow$ `git add` $
ightarrow$ **Staging Area (Index)** $
ightarrow$ `git commit` $
ightarrow$ **Local Repo** |
| **`git rebase` vs `merge`** | `rebase`: Historial lineal sin commit de merge \| `merge`: Conserva historial con commit de unión |
| **SonarQube** | Análisis estático de código para calidad, cobertura, olores de código y *Quality Gates* |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/metrica-v3-methodology|Metodología MÉTRICA Versión 3]]
- Entidad: [[wiki/entities/git-version-control-system|Sistema de Control de Versiones Git]]
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Pruebas de Caja Blanca, Caja Negra y McCabe]]
- Síntesis: [[wiki/synthesis/metrica-v3-processes-and-artifacts-guide|Guía de Procesos y Artefactos de MÉTRICA v3]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software y QA]]

> [!trampa] ⚠️ Trampas Frecuentes de Examen: MÉTRICA v3 y QA
> 1. **Fórmula de Complejidad Ciclomática de McCabe**:
>    $$V(G) = E - N + 2P$$
>    Donde $E$ = Número de aristas, $N$ = Número de nodos, $P$ = Componentes conexos (para un programa simple $P=1 \implies V(G) = E - N + 2$).
>    También es igual a: $V(G) = 	ext{Regiones del grafo plano} = 	ext{Nodos predicado (condiciones simples)} + 1$.
> 2. **Procesos de MÉTRICA v3**:
>    - **EVS**: Estudio de Viabilidad del Sistema.
>    - **ASI**: Análisis del Sistema de Información.
>    - **DSI**: Diseño del Sistema de Información (incluye diseño de interfaz y arquitectura física).
>    - **CSI**: Construcción del Sistema de Información (codificación, pruebas unitarias y de integración).
>    - **IAS**: Implantación y Aceptación del Sistema (pruebas de aceptación y paso a producción).
>    - **MSI**: Mantenimiento del Sistema de Información.
