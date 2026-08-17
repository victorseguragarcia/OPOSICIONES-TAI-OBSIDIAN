---
title: "Test de Autoevaluación: Bloque 2 - Tema 01 (Informática Básica y Representación de Datos)"
type: "test"
target: "wiki/sources/bloque2-tema01.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - representacion-datos
  - complemento-a-2
  - ieee-754
  - unicode
  - von-neumann
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 01: Informática Básica y Representación de Datos

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. ¿Cuál es el rango de valores enteros representables en Complemento a 2 utilizando un registro de $n = 8$ bits?
- [ ] a) $[-127, +128]$
- [ ] b) $[-128, +127]$
- [ ] c) $[0, 255]$
- [ ] d) $[-256, +255]$

### 2. En el estándar IEEE 754 para representación en Coma Flotante de Simple Precisión (32 bits), ¿cuántos bits se asignan al Signo, al Exponente y a la Mantisa respectivamente?
- [ ] a) Signo: 1 bit | Exponente: 8 bits | Mantisa: 23 bits
- [ ] b) Signo: 1 bit | Exponente: 11 bits | Mantisa: 20 bits
- [ ] c) Signo: 1 bit | Exponente: 8 bits | Mantisa: 24 bits
- [ ] d) Signo: 2 bits | Exponente: 7 bits | Mantisa: 23 bits

### 3. ¿Cuál es el valor del sesgo (*bias*) aplicado al exponente en el estándar IEEE 754 de Simple Precisión (32 bits)?
- [ ] a) $128$
- [ ] b) $127$
- [ ] c) $1023$
- [ ] d) $255$

### 4. ¿Cuántos bytes puede ocupar un carácter codificado en UTF-8 según el estándar Unicode?
- [ ] a) Siempre exactamente 2 bytes.
- [ ] b) Siempre exactamente 4 bytes.
- [ ] c) De 1 a 4 bytes de longitud variable.
- [ ] d) De 1 a 2 bytes únicamente.

### 5. ¿Cuál es la principal diferencia entre la arquitectura Von Neumann y la arquitectura Harvard?
- [ ] a) Von Neumann usa memoria compartida para datos e instrucciones; Harvard dispone de memorias y buses físicamente separados para datos e instrucciones.
- [ ] b) Von Neumann no utiliza registros de CPU y Harvard sí.
- [ ] c) Von Neumann solo admite procesamiento en paralelo y Harvard secuencial.
- [ ] d) Harvard no requiere reloj de sincronización.

### 6. En la CPU, ¿qué registro contiene la dirección de memoria de la siguiente instrucción que debe ser leída y ejecutada?
- [ ] a) Registro de Instrucción (IR - *Instruction Register*).
- [ ] b) Contador de Programa (PC - *Program Counter*).
- [ ] c) Registro de Dirección de Memoria (MAR - *Memory Address Register*).
- [ ] d) Acumulador (ACC).

### 7. Al representar el número decimal $+45$ en binario natural de 8 bits se obtiene `00101101`. ¿Cuál es su representación en Complemento a 2 para el valor $-45$?
- [ ] a) `11010010`
- [ ] b) `11010011`
- [ ] c) `10101101`
- [ ] d) `11101101`

### 8. En la jerarquía de memoria, ¿cuál de los siguientes elementos presenta el MENOR tiempo de acceso (mayor velocidad)?
- [ ] a) Memoria Caché L1.
- [ ] b) Registros internos de la CPU.
- [ ] c) Memoria Caché L2.
- [ ] d) Memoria Principal RAM (DDR5).

### 9. ¿Qué código de caracteres amplió el estándar ASCII original de 7 bits a 8 bits para incluir caracteres de lenguas de Europa occidental como la 'ñ' o vocales con tilde?
- [ ] a) EBCDIC.
- [ ] b) ISO/IEC 8859-1 (Latin-1).
- [ ] c) ASCII-7.
- [ ] d) UTF-32.

### 10. En coma flotante IEEE 754 de 32 bits, ¿qué valor especial representa un número con exponente todo a 1s (`11111111`) y mantisa distinta de cero?
- [ ] a) $+\infty$ (Infinito positivo).
- [ ] b) $-\infty$ (Infinito negativo).
- [ ] c) NaN (*Not a Number*).
- [ ] d) Cero desnormalizado.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **b** | 2. **a** | 3. **b** | 4. **c** | 5. **a** | 6. **b** | 7. **b** | 8. **b** | 9. **b** | 10. **c**
>
> ### Explicación Técnica:
> - **Pregunta 1 (b)**: Rango C2 con $n$ bits: $[-2^{n-1}, +2^{n-1}-1]$. Para 8 bits: $[-2^7, 2^7-1] = [-128, +127]$.
> - **Pregunta 2 (a)**: IEEE 754 Simple Precisión (32 bits): 1 bit de signo, 8 bits de exponente y 23 bits de mantisa fraccionaria (con 1 implícito).
> - **Pregunta 3 (b)**: El sesgo en simple precisión es $2^{8-1}-1 = 127$. (En doble precisión de 64 bits es $1023$).
> - **Pregunta 4 (c)**: UTF-8 es de longitud variable de 1 a 4 bytes (los primeros 128 caracteres ASCII ocupan exactamente 1 byte).
> - **Pregunta 5 (a)**: Von Neumann comparte bus y memoria de datos/instrucciones (cuello de botella de Von Neumann); Harvard utiliza memorias y buses independientes.
> - **Pregunta 6 (b)**: El PC almacena la dirección de la siguiente instrucción. El IR almacena la instrucción en curso de decodificación.
> - **Pregunta 7 (b)**: Complemento a 2 de $+45$ (`00101101`): invertimos bits (C1 = `11010010`) y sumamos 1 $
ightarrow$ `11010011`.
> - **Pregunta 8 (b)**: Los registros de la CPU operan en $< 1$ ciclo de reloj ($< 0.5	ext{ ns}$), siendo más rápidos que la caché L1 (1-4 ciclos).
> - **Pregunta 9 (b)**: ISO 8859-1 (Latin-1) usa 8 bits (256 caracteres) para caracteres de Europa Occidental.
> - **Pregunta 10 (c)**: Exponente todo 1s y mantisa no nula codifica NaN. Si la mantisa fuera todo ceros, codificaría $\pm\infty$.
