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

# 🔴 Test de Autoevaluación: Bloque 2 - Tema 01 (Informática Básica y Representación de Datos)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 2 - Tema 01 (Informática Básica y Representación de Datos)",
  "questions": [
    {
      "question": "¿Cuál es el rango de valores enteros representables en Complemento a 2 utilizando un registro de $n = 8$ bits?",
      "options": [
        "$[-127, +128]$",
        "$[-128, +127]$",
        "$[0, 255]$",
        "$[-256, +255]$"
      ],
      "answer": "b",
      "explanation": "Rango C2 con $n$ bits: $[-2^{n-1}, +2^{n-1}-1]$. Para 8 bits: $[-2^7, 2^7-1] = [-128, +127]$."
    },
    {
      "question": "En el estándar IEEE 754 para representación en Coma Flotante de Simple Precisión (32 bits), ¿cuántos bits se asignan al Signo, al Exponente y a la Mantisa respectivamente?",
      "options": [
        "Signo: 1 bit | Exponente: 8 bits | Mantisa: 23 bits",
        "Signo: 1 bit | Exponente: 11 bits | Mantisa: 20 bits",
        "Signo: 1 bit | Exponente: 8 bits | Mantisa: 24 bits",
        "Signo: 2 bits | Exponente: 7 bits | Mantisa: 23 bits"
      ],
      "answer": "a",
      "explanation": "IEEE 754 Simple Precisión (32 bits): 1 bit de signo, 8 bits de exponente y 23 bits de mantisa fraccionaria (con 1 implícito)."
    },
    {
      "question": "¿Cuál es el valor del sesgo (*bias*) aplicado al exponente en el estándar IEEE 754 de Simple Precisión (32 bits)?",
      "options": [
        "$128$",
        "$127$",
        "$1023$",
        "$255$"
      ],
      "answer": "b",
      "explanation": "El sesgo en simple precisión es $2^{8-1}-1 = 127$. (En doble precisión de 64 bits es $1023$)."
    },
    {
      "question": "¿Cuántos bytes puede ocupar un carácter codificado en UTF-8 según el estándar Unicode?",
      "options": [
        "Siempre exactamente 2 bytes.",
        "Siempre exactamente 4 bytes.",
        "De 1 a 4 bytes de longitud variable.",
        "De 1 a 2 bytes únicamente."
      ],
      "answer": "c",
      "explanation": "UTF-8 es de longitud variable de 1 a 4 bytes (los primeros 128 caracteres ASCII ocupan exactamente 1 byte)."
    },
    {
      "question": "¿Cuál es la principal diferencia entre la arquitectura Von Neumann y la arquitectura Harvard?",
      "options": [
        "Von Neumann usa memoria compartida para datos e instrucciones; Harvard dispone de memorias y buses físicamente separados para datos e instrucciones.",
        "Von Neumann no utiliza registros de CPU y Harvard sí.",
        "Von Neumann solo admite procesamiento en paralelo y Harvard secuencial.",
        "Harvard no requiere reloj de sincronización."
      ],
      "answer": "a",
      "explanation": "Von Neumann comparte bus y memoria de datos/instrucciones (cuello de botella de Von Neumann); Harvard utiliza memorias y buses independientes."
    },
    {
      "question": "En la CPU, ¿qué registro contiene la dirección de memoria de la siguiente instrucción que debe ser leída y ejecutada?",
      "options": [
        "Registro de Instrucción (IR - *Instruction Register*).",
        "Contador de Programa (PC - *Program Counter*).",
        "Registro de Dirección de Memoria (MAR - *Memory Address Register*).",
        "Acumulador (ACC)."
      ],
      "answer": "b",
      "explanation": "El PC almacena la dirección de la siguiente instrucción. El IR almacena la instrucción en curso de decodificación."
    },
    {
      "question": "Al representar el número decimal $+45$ en binario natural de 8 bits se obtiene `00101101`. ¿Cuál es su representación en Complemento a 2 para el valor $-45$?",
      "options": [
        "`11010010`",
        "`11010011`",
        "`10101101`",
        "`11101101`"
      ],
      "answer": "b",
      "explanation": "Complemento a 2 de $+45$ (`00101101`): invertimos bits (C1 = `11010010`) y sumamos 1 $"
    },
    {
      "question": "En la jerarquía de memoria, ¿cuál de los siguientes elementos presenta el MENOR tiempo de acceso (mayor velocidad)?",
      "options": [
        "Memoria Caché L1.",
        "Registros internos de la CPU.",
        "Memoria Caché L2.",
        "Memoria Principal RAM (DDR5)."
      ],
      "answer": "b",
      "explanation": "Los registros de la CPU operan en $< 1$ ciclo de reloj ($< 0.5\text{ ns}$), siendo más rápidos que la caché L1 (1-4 ciclos)."
    },
    {
      "question": "¿Qué código de caracteres amplió el estándar ASCII original de 7 bits a 8 bits para incluir caracteres de lenguas de Europa occidental como la 'ñ' o vocales con tilde?",
      "options": [
        "EBCDIC.",
        "ISO/IEC 8859-1 (Latin-1).",
        "ASCII-7.",
        "UTF-32."
      ],
      "answer": "b",
      "explanation": "ISO 8859-1 (Latin-1) usa 8 bits (256 caracteres) para caracteres de Europa Occidental."
    },
    {
      "question": "En coma flotante IEEE 754 de 32 bits, ¿qué valor especial representa un número con exponente todo a 1s (`11111111`) y mantisa distinta de cero?",
      "options": [
        "$+\\infty$ (Infinito positivo).",
        "$-\\infty$ (Infinito negativo).",
        "NaN (*Not a Number*).",
        "Cero desnormalizado."
      ],
      "answer": "c",
      "explanation": "Exponente todo 1s y mantisa no nula codifica NaN. Si la mantisa fuera todo ceros, codificaría $\\pm\\infty$."
    }
  ]
}
```
