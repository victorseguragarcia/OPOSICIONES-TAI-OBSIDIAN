---
title: "Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky"
type: "entity"
tags:
  - lenguajes-programacion
  - compiladores
  - interpretes
  - gramaticas
  - chomsky
  - parsers
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Lenguajes de Programación"
  - "Compiladores e Intérpretes"
  - "Jerarquía de Chomsky"
---

# Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky

Fundamentos teóricos de los lenguajes informáticos, paradigmas de desarrollo, teoría de gramáticas formales y fases del proceso de traducción de código fuente a código máquina.

---

## 🏛️ 1. Jerarquía de Chomsky de Gramáticas y Autómatas

| Tipo | Gramática | Regla de Producción ($\alpha \rightarrow \beta$) | Autómata Reconocedor | Fase del Compilador |
|------|-----------|--------------------------------------------------|----------------------|---------------------|
| **Tipo 0** | **No Restringida** | Sin restricciones ($\alpha \rightarrow \beta$) | **Máquina de Turing** | Lenguajes recursivamente enumerables |
| **Tipo 1** | **Sensible al Contexto** | $|\alpha| \le |\beta|$ ($uAv \rightarrow uwv$) | **Autómata Linealmente Acotado (LBA)** | Análisis semántico avanzado |
| **Tipo 2** | **Libre de Contexto (Incontextual)** | $A \rightarrow \gamma$ ($A \in V_N$, $\gamma \in (V_N \cup V_T)^*$) | **Autómata con Pila (PDA)** | **Análisis Sintáctico (Parser)** |
| **Tipo 3** | **Regular** | $A \rightarrow aB$ o $A \rightarrow a$ | **Autómata Finito (DFA / NFA)** | **Análisis Léxico (Scanner / Tokens)** |

---

## ⚙️ 2. Fases de la Compilación

```
Código Fuente
      │
      ▼
[ Análisis Léxico (Scanner) ] ──> Tokens (elimina comentarios y espacios)
      │
      ▼
[ Análisis Sintáctico (Parser) ] ──> Árbol de Sintaxis Abstracta (AST)
      │
      ▼
[ Análisis Semántico ] ──> Comprobación de tipos y Tabla de Símbolos
      │
      ▼
[ Generación Código Intermedio ] ──> Código 3 direcciones / Bytecode
      │
      ▼
[ Optimización de Código ] ──> Simplificación algebraica, propagación de constantes
      │
      ▼
[ Generación de Código Objeto ] ──> Binario máquina ejecutable (.obj / .exe)
```

---

## 🧩 3. Tipos de Analizadores Sintácticos (Parsers)

- **Descendentes (*Top-Down*)**:
  - **LL(k)**: Lectura de Izquierda a derecha, derivación más a la Izquierda (*Leftmost*), con $k$ tokens de anticipación.
  - No admiten recursividad por la izquierda en las reglas de gramática.
- **Ascendentes (*Bottom-Up*)**:
  - **LR(k)**: Lectura de Izquierda a derecha, derivación más a la Derecha invertida (*Rightmost*).
  - Variantes: **LR(0)**, **SLR(1)**, **LALR(1)** (usado en **Yacc/Bison**), **LR(1)**.
  - Resuelven conflictos desplazamiento/reducción (*Shift/Reduce*).

---

## 🧠 4. Organización de Memoria en Tiempo de Ejecución

```
+------------------------------------+  (Direcciones Altas)
|               STACK                |  Variables locales y Registros de Activación (Frames)
|                 │                  |
|                 ▼                  |  Crece hacia abajo
|                                    |
|                 ▲                  |  Crece hacia arriba
|                 │                  |
|               HEAP                 |  Memoria dinámica (malloc / new / objetos GC)
+------------------------------------+
|            BSS / DATA              |  Variables globales y estáticas
+------------------------------------+
|               TEXT                 |  Instrucciones de código binario (solo lectura)
+------------------------------------+  (Direcciones Bajas: 0x00000000)
```

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
