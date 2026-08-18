---
title: "Guía de Pruebas de Software, Métricas de Cobertura y McCabe"
type: "synthesis"
tags:
  - synthesis
  - testing
  - caja-blanca
  - mccabe
  - qa
sources:
  - "raw/sources/bloque3-tema05.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía de Testing"
  - "Pruebas de Software QA"
---

# Guía de Pruebas de Software, Métricas de Cobertura y McCabe

Manual de diseño de casos de prueba y niveles de verificación para oposiciones TAI.

---

## 🔢 1. Cálculo de la Complejidad Ciclomática de McCabe ($V(G)$)

Fórmula fundamental para determinar el número de casos de prueba de caminos independientes:
$$V(G) = E - N + 2P$$
- $E$: Aristas (*Edges*).
- $N$: Nodos (*Nodes*).
- $P$: Componentes conexos ($P=1$ para un único programa).
- **Regla Inmediata**: $V(G) = \text{Nodos de Decisión (if/while/for)} + 1$.

---

## 📋 2. Jerarquía de Pruebas de Software

1. **Unitarias**: Módulos/métodos aislados.
2. **Integración**: Interfaces y comunicación entre módulos.
3. **Sistema**: Requisitos funcionales y no funcionales globales.
4. **Aceptación**: Validación final del usuario de negocio (*Alpha/Beta*).
5. **Regresión**: Comprobación tras modificaciones o corrección de bugs.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema05|Resumen Bloque 3 - Tema 05]]
- Concepto: [[wiki/concepts/white-box-and-black-box-testing|Caja Blanca y Caja Negra]]
