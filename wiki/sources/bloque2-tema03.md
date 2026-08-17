---
title: "Resumen Fuente: Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema03
  - complemento-a-dos
  - ieee-754
  - ascii
  - unicode
  - utf-8
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Representación de la Información"
  - "bloque2-tema03"
---

# Resumen Fuente: Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema03.md|bloque2-tema03.md]].

---

## 📖 Resumen Ejecutivo

Este tema aborda la codificación matemática y digital de los datos: la conversión entre sistemas de numeración (binario, octal, hexadecimal y BCD), la representación de números enteros con signo destacando el **Complemento a 2 (C2)** (rango asimétrico $[-2^{n-1}, +2^{n-1}-1]$, cero único y regla de cálculo), la representación de números reales en coma flotante bajo el estándar **IEEE 754** (precisión simple de 32 bits con sesgo 127 y precisión doble de 64 bits con sesgo 1023, junto a valores especiales $\pm 0, \pm\infty$, NaN y desnormalizados), y la evolución de los códigos de caracteres desde **ASCII** (7 bits / 128 caracteres) e **ISO 8859-1 (Latin-1)** (8 bits), hasta **Unicode** y la codificación de longitud variable **UTF-8** (1 a 4 bytes, compatible hacia atrás con ASCII).

---

## 🎯 Datos Clave para Oposiciones TAI

| Sistema / Norma | Estructura / Rango / Sesgo |
|-----------------|----------------------------|
| **Rango C2 en 8 bits ($n=8$)** | **$[-128, +127]$** (Cero único: `00000000`) |
| **IEEE 754 Precisión Simple (32 bits)** | **1 bit Signo** + **8 bits Exponente (Sesgo = 127)** + **23 bits Mantisa** |
| **IEEE 754 Precisión Doble (64 bits)** | **1 bit Signo** + **11 bits Exponente (Sesgo = 1023)** + **52 bits Mantisa** |
| **IEEE 754 Infinito ($\pm\infty$)** | Exponente todo a '1' ($E=255$) y Mantisa todo a '0' ($M=0$) |
| **IEEE 754 NaN (Not a Number)** | Exponente todo a '1' ($E=255$) y Mantisa **distinta de cero** ($M \neq 0$) |
| **ASCII Estándar** | **7 bits** (128 caracteres del 0 al 127) |
| **UTF-8** | Longitud variable de **1 a 4 bytes** (primeros 128 caracteres idénticos a ASCII en 1 byte) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/ieee-754-floating-point|Estándar IEEE 754 de Coma Flotante]]
- Entidad: [[wiki/entities/character-encoding-unicode-utf8|Codificación de Caracteres: ASCII y Unicode/UTF-8]]
- Concepto: [[wiki/concepts/two-complement-and-binary-arithmetic|Complemento a Dos y Aritmética Binaria]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de Cálculo IEEE 754 y Binario]]
