---
title: "Cheatsheet de Cálculo Binario, Complemento a 2 y Coma Flotante IEEE 754"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - ieee-754
  - complemento-a-dos
  - binario
sources:
  - "raw/sources/bloque2-tema03.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet IEEE 754"
  - "Cálculo en Complemento a 2"
---

# Cheatsheet de Cálculo Binario, Complemento a 2 y Coma Flotante IEEE 754

Guía práctica de resolución paso a paso para preguntas prácticas de cálculo en oposiciones TAI.

---

## 🔢 1. Procedimiento de Cálculo en Complemento a 2 (8 bits)
- **Representar un número positivo (ej. $+25$)**:
  - $25_{10} = 16 + 8 + 1 = 00011001_2$ (Bit MSB 0).
- **Representar el negativo correspondiente (ej. $-25$)**:
  - Invertir todos los bits (C1): $11100110_2$.
  - Sumar 1: $11100110 + 1 = \mathbf{11100111_2}$.
- **Rango en $n=8$ bits**: $[-128, +127]$. El valor $-128 = 10000000_2$, $-1 = 11111111_2$.

---

## 📐 2. Procedimiento de Conversión a IEEE 754 Simple Precisión (32 bits)

Ejemplo: Convertir el número decimal **$-13.625$** a formato IEEE 754 de 32 bits.
1. **Determinar el Signo**: Al ser negativo, **$S = 1$**.
2. **Convertir la parte entera y fraccionaria a binario**:
   - $13_{10} = 1101_2$.
   - $0.625_{10} = 0.5 + 0.125 = 0.101_2$.
   - Número en binario sin signo: $1101.101_2$.
3. **Normalizar en formato $1.M 	imes 2^e$**:
   - Desplazar la coma 3 posiciones a la izquierda: $1.101101_2 	imes 2^3$.
   - Mantisa ($M$): $10110100000000000000000_2$ (rellenada con ceros hasta 23 bits).
4. **Calcular el Exponente sesgado ($E$)**:
   - Exponente real $e = 3$.
   - $E = e + 127 = 3 + 127 = 130_{10} = 10000010_2$.
5. **Ensamblar los 32 bits ($S + E + M$)**:
   - `1 | 10000010 | 10110100000000000000000`
   - Agrupado en hexadecimal: `1100 0001 0101 1010 0000 0000 0000 0000` $\rightarrow$ **`0xC15A0000`**.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema03|Resumen Bloque 2 - Tema 03]]
- Entidad: [[wiki/entities/ieee-754-floating-point|IEEE 754]]
