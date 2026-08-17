---
title: "Bloque 2 - Tema 03: Representación de la Información: C2, IEEE 754, ASCII y Unicode"
type: "raw-source"
topic: "representacion-informacion"
date: "2026-08-17"
---

# Bloque 2 - Tema 03: Sistemas de Numeración, Representación de Enteros y Reales (IEEE 754) y Codificación de Caracteres

## 1. Sistemas de Numeración y Conversiones
- **Sistema Binario (Base 2)**: Dígitos 0 y 1.
- **Sistema Octal (Base 8)**: Dígitos 0 a 7. Cada dígito octal equivale a un grupo de 3 bits binarios.
- **Sistema Hexadecimal (Base 16)**: Dígitos 0 a 9 y letras A ($=10$), B ($=11$), C ($=12$), D ($=13$), E ($=14$), F ($=15$). Cada dígito hexadecimal equivale a un cuarteto (*nibble*) de 4 bits binarios.
- **Decimal Codificado en Binario (BCD - Binary-Coded Decimal)**: Cada dígito decimal (0-9) se codifica de forma independiente en 4 bits binarios (ej. $25_{10} = 0010\ 0101_{BCD}$).

## 2. Representación de Números Enteros con Signo en $n$ bits
1. **Signo y Magnitud (SM)**:
   - El bit más significativo (MSB) es el bit de signo: 0 para positivo, 1 para negativo. Los $n-1$ bits restantes representan el valor absoluto.
   - Rango en $n$ bits: $[-(2^{n-1}-1), +(2^{n-1}-1)]$.
   - Inconveniente: Doble representación del cero ($+0 = 0000$ y $-0 = 1000$).
2. **Complemento a 1 (C1)**:
   - Los números positivos se representan en binario natural con bit de signo 0.
   - Los números negativos se obtienen invirtiendo todos los bits (bit a bit) del número positivo correspondiente.
   - Rango en $n$ bits: $[-(2^{n-1}-1), +(2^{n-1}-1)]$. Doble cero ($+0 = 0000$, $-0 = 1111$).
3. **Complemento a 2 (C2) - Estándar Universal en CPUs**:
   - Los positivos comienzan con bit 0 seguido de la magnitud en binario natural.
   - Los negativos se obtienen aplicando la operación lógica: $\text{C2}(X) = \text{C1}(X) + 1$ (invertir todos los bits y sumar 1 al bit menos significativo).
   - **Regla Práctica Inmediata**: Dejar invariables todos los bits de derecha a izquierda hasta encontrar el primer '1' inclusive, e invertir todos los bits restantes a su izquierda.
   - **Rango Asimétrico en $n$ bits**: $[-2^{n-1}, +(2^{n-1}-1)]$. Posee **una única representación para el cero** ($0000\dots0$).
   - *Ejemplo en 8 bits ($n=8$)*: Rango $[-128, +127]$. El valor $-128 = 10000000_2$, $-1 = 11111111_2$, $0 = 00000000_2$, $+127 = 01111111_2$.

## 3. Representación de Números Reales: Estándar IEEE 754
Estándar internacional que normaliza la representación binaria en coma flotante según la fórmula:
$$X = (-1)^S \times 1.M \times 2^{E - \text{Sesgo}}$$
Donde $S$ es el bit de signo (0 positivo, 1 negativo), $E$ es el exponente desplazado/polarizado con un sesgo (*bias*), y $M$ es la mantisa fraccionaria con bit implícito ('1.M').

### Precisión Simple (32 bits / Single Precision - `float`)
- **Estructura de 32 bits**:
  - **1 bit de Signo ($S$)**: Bit 31.
  - **8 bits de Exponente ($E$)**: Bits 30 a 23. **Sesgo = 127** ($2^{8-1}-1$). Exponente real $e = E - 127$.
  - **23 bits de Mantisa ($M$)**: Bits 22 a 0.
- **Valores Especiales en Precisión Simple**:
  - **Cero ($\pm 0$)**: $E = 00000000_2$ ($0$), $M = 0$.
  - **Números Desnormalizados / Subnormales**: $E = 00000000_2$ ($0$), $M \neq 0$. Valor: $(-1)^S \times 0.M \times 2^{-126}$.
  - **Infinito ($\pm\infty$)**: $E = 11111111_2$ ($255$), $M = 0$.
  - **No es un Número (NaN - Not a Number)**: $E = 11111111_2$ ($255$), $M \neq 0$ (errores como $0/0$ o $\sqrt{-1}$).

### Precisión Doble (64 bits / Double Precision - `double`)
- **Estructura de 64 bits**:
  - **1 bit de Signo ($S$)**: Bit 63.
  - **11 bits de Exponente ($E$)**: Bits 62 a 52. **Sesgo = 1023** ($2^{11-1}-1$). Exponente real $e = E - 1023$.
  - **52 bits de Mantisa ($M$)**: Bits 51 a 0.

## 4. Codificación de Caracteres
- **ASCII (American Standard Code for Information Interchange)**: Estándar de **7 bits** (128 caracteres del 0 al 127). Contiene caracteres de control (0-31: NUL, CR, LF, TAB) y caracteres imprimibles (32 espacio a 126 tilde, '0' en 48 / 0x30, 'A' en 65 / 0x41, 'a' en 97 / 0x61).
- **ASCII Extendido / ISO 8859-1 (Latin-1)**: Código de **8 bits** (256 caracteres). Añade caracteres de idiomas de Europa occidental (ñ, acentos, diéresis).
- **EBCDIC (Extended BCD Interchange Code)**: Código de **8 bits** desarrollado por IBM para sus mainframes System/360. Incompatible con ASCII.
- **Unicode**: Estándar universal que asigna a cada carácter un identificador único denominado punto de código (*Code Point*, notación `U+XXXX`), cubriendo más de 149.000 caracteres de todas las lenguas y símbolos.
  - **UTF-8**: Codificación de **longitud variable de 1 a 4 bytes**. Totalmente compatible hacia atrás con ASCII (los primeros 128 caracteres ocupan exactamente 1 byte: `0xxxxxxx`). Caracteres latinos europeos ocupan 2 bytes (`110xxxxx 10xxxxxx`), caracteres asiáticos 3 bytes (`1110xxxx 10xxxxxx 10xxxxxx`) y emojis 4 bytes (`11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`). Es la codificación estándar dominante en Internet (>98% de la web).
  - **UTF-16**: Codificación de 2 o 4 bytes (utiliza pares sustitutos para caracteres fuera del plano multilingüe básico BMP).
  - **UTF-32**: Codificación de longitud fija de 4 bytes (32 bits) por carácter.
