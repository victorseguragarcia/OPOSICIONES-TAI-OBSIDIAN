---
title: "Estándar IEEE 754 de Representación en Coma Flotante"
type: "entity"
tags:
  - ieee-754
  - coma-flotante
  - representacion-datos
  - float
  - double
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "IEEE 754"
  - "Coma Flotante"
---

# Estándar IEEE 754 de Representación en Coma Flotante

El estándar **IEEE 754** normaliza la representación binaria de números reales mediante la descomposición en **Signo ($S$)**, **Exponente sesgado ($E$)** y **Mantisa normalizada ($M$)**:
$$X = (-1)^S \times 1.M \times 2^{E - \text{Sesgo}}$$

---

## 🏛️ Formatos de Precisión

| Precisión | Tamaño Total | Signo ($S$) | Exponente ($E$) | Sesgo (*Bias*) | Mantisa ($M$) |
|-----------|--------------|-------------|-----------------|----------------|---------------|
| **Simple (`float`)** | **32 bits** | 1 bit (bit 31) | 8 bits (bits 30-23) | **127** | 23 bits (bits 22-0) |
| **Doble (`double`)** | **64 bits** | 1 bit (bit 63) | 11 bits (bits 62-52) | **1023** | 52 bits (bits 51-0) |

---

## 🎯 Valores Especiales

- **Cero ($\pm 0$)**: $E = 0$, $M = 0$.
- **Infinito ($\pm\infty$)**: $E = 255$ (simple) / $E = 2047$ (doble), $M = 0$.
- **NaN (Not a Number)**: $E = 255$ (simple) / $E = 2047$ (doble), $M \neq 0$.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo IEEE 754]]
