---
title: "Resumen Fuente: Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema05
  - pruebas-software
  - caja-blanca
  - caja-negra
  - mccabe
  - cicd
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Calidad, Pruebas y CI/CD"
  - "bloque3-tema05"
---

# Resumen Fuente: Bloque 3 - Tema 05: Calidad, Pruebas de Software, Complejidad de McCabe y CI/CD

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque3-tema05.md|bloque3-tema05.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en el aseguramiento de la calidad del software: la jerarquía de niveles de pruebas (Unitarias, Integración, Sistema, Aceptación Alpha/Beta y Regresión), las técnicas de diseño de casos de prueba de **Caja Blanca** (coberturas y la métrica de **Complejidad Ciclomática de McCabe** $V(G) = E - N + 2P$ para caminos básicos independientes) frente a **Caja Negra** (particiones de equivalencia y análisis de valores límite), y los pipelines de integración y despliegue continuo (**CI/CD** con Jenkins, GitLab CI, GitHub Actions) integrados con análisis estático de código mediante **SonarQube** para evaluar deuda técnica y *Quality Gates*.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto / Métrica | Fórmula / Definición de Examen |
|--------------------|--------------------------------|
| **Complejidad Ciclomática ($V(G)$)** | **$V(G) = E - N + 2P$** ($E$ aristas, $N$ nodos, $P$ componentes conexos) |
| **Fórmula Alternativa McCabe** | **$V(G) = 	ext{Nodos Predicado} + 1$** |
| **Pruebas de Caja Blanca** | Analizan la **estructura interna y código fuente** (sentencias, ramas, caminos) |
| **Pruebas de Caja Negra** | Basadas en **especificación externa** (clases de equivalencia, valores límite) |
| **Pruebas de Regresión** | Verifican que los cambios nuevos no hayan roto funcionalidades previas |
| **CI vs CD** | **CI**: Integración y tests automáticos \| **CD**: Despliegue automático a producción |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Pruebas de Caja Blanca, Caja Negra y Métrica de McCabe]]
- Concepto: [[wiki/concepts/ci-cd-pipelines-and-devops|Pipelines CI/CD, DevOps y Calidad de Código]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software y QA]]
