---
title: "Pruebas de Caja Blanca, Caja Negra y Complejidad Ciclomática de McCabe"
type: "concept"
tags:
  - testing
  - caja-blanca
  - caja-negra
  - mccabe
  - qa
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Caja Blanca y Caja Negra"
  - "Complejidad de McCabe"
---

# Pruebas de Caja Blanca, Caja Negra y Complejidad Ciclomática de McCabe

Estrategias fundamentales de diseño de casos de prueba en ingeniería de software.

---

## 🏛️ Comparativa y Fórmulas

- **Caja Blanca (Estructural)**: Analiza el código interno.
  - **Fórmula de McCabe**: $$V(G) = E - N + 2P = 	ext{Nodos Predicado} + 1$$
  - Determina el número de caminos independientes básicos para cobertura total.
- **Caja Negra (Funcional)**: Basada en especificación.
  - **Técnicas**: Particiones de equivalencia (clases válidas/inválidas) y análisis de valores límite (BVA).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Síntesis: [[wiki/synthesis/software-testing-and-qa-guide|Guía de Pruebas de Software]]
