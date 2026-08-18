---
title: "Complemento a Dos y Aritmética Binaria"
type: "concept"
tags:
  - complemento-a-dos
  - aritmetica-binaria
  - enteros-signo
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Complemento a 2"
  - "Aritmética en Complemento a Dos"
---

# Complemento a Dos y Aritmética Binaria

El sistema de **Complemento a 2 (C2)** es el estándar universal en arquitectura de computadores para la representación de números enteros con signo.

---

## 🏛️ Propiedades y Reglas

- **Rango en $n$ bits**: $[-2^{n-1}, +(2^{n-1}-1)]$. Para 8 bits: $[-128, +127]$.
- **Cero Único**: $0 = 00000000_2$ (a diferencia de Signo y Magnitud y C1 que tienen doble cero).
- **Cálculo Negativo**: Invertir todos los bits (C1) y sumar 1 al bit menos significativo ($\text{C2} = \text{C1} + 1$).
- **Regla Rápida**: Conservar los bits desde la derecha hasta el primer '1' inclusive, e invertir todos los demás.
- **Detección de Overflow en Sumas**: Se produce desbordamiento cuando al sumar dos números del mismo signo se obtiene un resultado de signo contrario.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo Binario e IEEE 754]]
