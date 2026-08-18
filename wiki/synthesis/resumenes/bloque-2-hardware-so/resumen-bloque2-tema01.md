---
title: "Resumen Completo Tema 01 (Bloque 2): Estructura y Componentes de un Sistema Informático (C2, IEEE 754, Buses)"
type: "synthesis"
tags:
  - resumen
  - resumen-completo
  - bloque-2
  - tema-01
estado: "🔴 Pendiente"
dificultad: "⭐⭐⭐"
prioridad: "Alta"
sources:
  - "[[wiki/sources/bloque2-tema01]]"
created: "2026-08-18"
updated: "2026-08-18"
---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Portada Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|Tema 02 ➡️]]

# 🔴 Resumen Completo Tema 01 (Bloque 2): Estructura y Componentes de un Sistema Informático (C2, IEEE 754, Buses)

> [!repaso] ⚡ **Puntos Clave y Objetivos de Examen del Tema 01**
> Guía completa y exhaustiva que recopila todos los conceptos teóricos, marco legal/normativo, tablas técnicas, comandos y casos de examen oficiales de este tema.

---

## 🟣 1. Desarrollo Temático Completo y Exhaustivo

# 🔴 Resumen Fuente: Bloque 2 - Tema 01 (UD011929): Informática Básica, Representación de la Información y Arquitectura de Computadores

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema01-informatica-basica-representacion.md|bloque2-tema01-informatica-basica-representacion.md]] (88 páginas).

---

## 📖 1. Unidades de Medida y Sistemas de Numeración

- **Unidades de Medida (SI vs IEC)**:
  - Sistema Internacional (decimal): $1	ext{ KB} = 10^3 = 1.000	ext{ bytes}$, $1	ext{ MB} = 10^6	ext{ bytes}$, $1	ext{ GB} = 10^9	ext{ bytes}$.
  - Estándar IEC (binario): $1	ext{ KiB} = 2^{10} = 1.024	ext{ bytes}$, $1	ext{ MiB} = 2^{20}	ext{ bytes}$, $1	ext{ GiB} = 2^{30}	ext{ bytes}$, $1	ext{ TiB} = 2^{40}	ext{ bytes}$.
- **Sistemas de Numeración**: Binario (base 2), Octal (base 8: grupos de 3 bits), Decimal (base 10) y Hexadecimal (base 16: grupos de 4 bits).

---

## 🟣 2. Representación de Datos: Enteros y Coma Flotante

### A. Representación de Enteros con Signo ($n$ bits):
1. **Signo y Magnitud (SM)**: Bit más significativo (MSB) para el signo ($0$ positivo, $1$ negativo). Rango: $[-(2^{n-1}-1), +(2^{n-1}-1)]$. Doble cero ($+0$ y $-0$).
2. **Complemento a 1 (C1)**: Se invierten todos los bits para números negativos. Doble cero ($+0$ y $-0$).
3. **Complemento a 2 (C2)**: Estándar universal. Se calcula invirtiendo los bits y sumando $1$ ($	ext{C2}(x) = \overline{x} + 1 = 2^n - |x|$).
   - Rango: $[-2^{n-1}, +(2^{n-1}-1)]$. **Cero único** ($00...0$). Para 8 bits: $[-128, +127]$.

### B. Coma Flotante Estándar IEEE 754:
$$N = (-1)^S 	imes 1.M 	imes 2^{E - 	ext{Sesgo}}$$
- **Simple Precisión (32 bits)**: 1 bit de signo ($S$), **8 bits de exponente ($E$)** con sesgo **127**, y **23 bits de mantisa ($M$)**.
- **Doble Precisión (64 bits)**: 1 bit de signo ($S$), **11 bits de exponente ($E$)** con sesgo **1023**, y **52 bits de mantisa ($M$)**.
- **Valores Especiales**:
  - Exponente todo 1s y Mantisa 0: **$\pm\infty$** (Infinito).
  - Exponente todo 1s y Mantisa $
e 0$: **NaN** (*Not a Number*).
  - Exponente todo 0s y Mantisa $
e 0$: **Números desnormalizados** (sin el 1 implícito).

---

## 🔵 3. Codificación de Caracteres

- **ASCII (7 bits)**: 128 caracteres (0 a 127). Códigos de control 0 a 31; 'A' = 65 (0x41), 'a' = 97 (0x61), '0' = 48 (0x30).
- **ASCII Extendido / ISO 8859-1 (Latin-1 - 8 bits)**: 256 caracteres para lenguas de Europa occidental (incluye 'ñ', 'ç', vocales con tilde).
- **ISO 8859-15 (Latin-9)**: Reemplaza caracteres poco usados de ISO 8859-1 para incorporar el símbolo del **Euro (€)** y las letras 'Š', 'š', 'Ž', 'ž', 'Œ', 'œ', 'Ÿ'.
- **Unicode**:
  - **UTF-8**: Longitud variable (1 a 4 bytes). Totalmente compatible hacia atrás con ASCII (los primeros 128 caracteres ocupan 1 byte).
  - **UTF-16**: Longitud variable (2 o 4 bytes mediante pares sustitutos / *surrogates*).
  - **UTF-32**: Longitud fija de 4 bytes (32 bits) por carácter.

---

## 🔵 4. Arquitectura de Computadores (Von Neumann vs Harvard)

- **Von Neumann**: Memoria unificada para instrucciones de programa y datos. Un único bus compartido genera el **cuello de botella de Von Neumann**.
- **Harvard**: Memorias y buses físicos separados para instrucciones y datos (permite lecturas simultáneas).
- **Componentes CPU**:
  - **Unidad de Control (UC)**: Contador de Programa (PC), Registro de Instrucción (RI), Decodificador, Reloj.
  - **Unidad Aritmético-Lógica (ALU)**: Operaciones lógicas y aritméticas, Acumulador, Registro de Estado (*Flags*).
  - **Buses del Sistema**: Bus de Datos (bidireccional), Bus de Direcciones (unidireccional desde CPU hacia memoria/periféricos) y Bus de Control.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica de Examen |
|----------|----------------------------------|
| **Rango C2 en 8 bits** | **$-128$ a $+127$** ($-128$ se representa como `10000000`) |
| **Sesgo IEEE 754 32 bits** | **127** ($2^{8-1} - 1$) \| 64 bits: **1023** ($2^{11-1} - 1$) |
| **UTF-8 Longitud** | **1 a 4 bytes** (compatible con ASCII en el byte 1) |
| **Bus de Direcciones** | Si el bus tiene $N$ líneas, puede direccionar un espacio de memoria de $2^N$ posiciones. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/cpu-architecture-von-neumann|Arquitectura de CPU Von Neumann y Harvard]]
- Entidad: [[wiki/entities/ieee-754-floating-point|Estándar IEEE 754 de Coma Flotante]]
- Entidad: [[wiki/entities/character-encoding-unicode-utf8|Codificación de Caracteres: ASCII, ISO 8859 y Unicode]]
- Concepto: [[wiki/concepts/two-complement-and-binary-arithmetic|Complemento a Dos y Aritmética Binaria]]
- Síntesis: [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet de IEEE 754 y Representación Binaria]]

> [!trampa] ⚠️ Trampas Frecuentes de Examen: Informática Básica y C2
> 1. **Rango de Complemento a 2**: En $n$ bits el rango es $[-2^{n-1}, +(2^{n-1}-1)]$. Para 8 bits: $[-128, +127]$. Ojo: el valor $-128$ se representa como `10000000` y **no tiene equivalente positivo en 8 bits** (desbordamiento / *overflow* si se intenta negar).
> 2. **Sesgo IEEE 754**: En simple precisión (32 bits), el sesgo es **127** ($2^{8-1}-1$). El exponente almacenado es $E = e + 127$. Los exponentes $E=0$ (números desnormalizados/cero) y $E=255$ (infinito/NaN) están reservados.
> 3. **Bit Implícito**: En números normalizados IEEE 754, la mantisa siempre comienza por `1.` que **NO se almacena** en los 23 bits de fracción, ganando 1 bit extra de precisión efectiva (24 bits totales).

---

## 🔵 2. Enlaces de Autoevaluación y Recursos de Estudio
- 📖 **Fuente Oficial Íntegra**: [[wiki/sources/bloque2-tema01|Nota Fuente del Tema 01]]
- 📝 **Test Interactivo del Tema (10 Preguntas)**: [[wiki/tests/temas/test-bloque2-tema01-informatica-basica|Test Tema 01]]
- 🃏 **Tarjetas de Memoria Rápida**: [[wiki/synthesis/tarjetas-memoria-flashcards-bloque2-tecnologia-hardware|Mazo Flashcards Bloque 2]]
- 🏠 **Índice del Bloque**: [[wiki/synthesis/resumenes/resumen-maestro-bloque2|Resumen Maestro Bloque 2]]

---

> [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Portada Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/resumen-maestro-bloque2|🏠 Índice Bloque 2]] &nbsp;|&nbsp; [[wiki/synthesis/resumenes/bloque-2-hardware-so/resumen-bloque2-tema02|Tema 02 ➡️]]
