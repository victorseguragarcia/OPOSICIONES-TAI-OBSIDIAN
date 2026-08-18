---
title: "Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-3
  - tema02
  - lenguajes-programacion
  - compiladores
  - interpretes
  - chomsky
  - gramaticas
  - parsers
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes de Programación y Compiladores"
  - "bloque3-tema02"
---

# 🔴 Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas, Compiladores y Jerarquía de Chomsky

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque3-tema02-lenguajes-programacion.md|bloque3-tema02-lenguajes-programacion.md]] (114 páginas).

---

## 📖 1. Clasificación y Paradigmas de Lenguajes de Programación

### Evolución por Generaciones:
- **1GL (Primera Generación)**: Lenguaje Máquina (código binario directo ejecutado por la CPU).
- **2GL (Segunda Generación)**: Lenguaje Ensamblador (mnemónicos traducidos por un ensamblador).
- **3GL (Tercera Generación)**: Lenguajes de Alto Nivel estructurados/imperativos (C, Pascal, Fortran, Java).
- **4GL (Cuarta Generación)**: Lenguajes declarativos orientados a bases de datos y gestión (SQL, ABAP, PL/SQL).
- **5GL (Quinta Generación)**: Lenguajes basados en restricciones, lógica e inteligencia artificial (Prolog, Lisp).

### Paradigmas de Programación:
- **Imperativo / Estructurado**: Secuencias de instrucciones que modifican el estado de la memoria (C, Pascal).
- **Orientado a Objetos (POO)**: Encapsulación de estado y comportamiento en objetos (Java, C++, C#, Python).
- **Funcional**: Basado en funciones puras sin efectos secundarios y evaluación de expresiones (Haskell, Scala, Clojure).
- **Lógico / Declarativo**: Basado en hechos, reglas y deducción matemática (Prolog).

---

## 🟣 2. Jerarquía de Chomsky de Gramáticas y Autómatas

La teoría de lenguajes formales de Noam Chomsky clasifica las gramáticas y sus reconocedores automáticos:

| Tipo | Tipo de Gramática | Reglas de Producción ($lpha 
ightarrow eta$) | Autómata Reconocedor | Aplicación en Compilación |
|------|-------------------|---------------------------------------------------|----------------------|---------------------------|
| **Tipo 0** | **No Restringida** | Sin restricciones ($lpha 
ightarrow eta$) | **Máquina de Turing** | Computabilidad universal |
| **Tipo 1** | **Sensible al Contexto** | $|lpha| \le |eta|$ ($uAv 
ightarrow uwv$) | **Autómata Lineal Acotado (LBA)** | Análisis semántico complejo |
| **Tipo 2** | **Libre de Contexto (Incontextual)** | $A 
ightarrow \gamma$ ($A \in V_N$, $\gamma \in (V_N \cup V_T)^*$) | **Autómata con Pila (PDA)** | **Análisis Sintáctico (Parser)** |
| **Tipo 3** | **Regular** | $A 
ightarrow aB$ o $A 
ightarrow a$ (Lineal) | **Autómata Finito (DFA / NFA)** | **Análisis Léxico (Scanner / Tokens)** |

---

## 🔵 3. Arquitectura y Fases de un Compilador

```
                   ESTRUCTURA DE UN COMPILADOR
                               │
       ┌───────────────────────┴───────────────────────┐
       ▼                                               ▼
FRONTEND (Depende del Lenguaje)              BACKEND (Depende de la CPU)
  1. Análisis Léxico (Scanner)                 4. Generación de Código Intermedio
     • Lee caracteres $\rightarrow$ Tokens        • Código 3 direcciones / Bytecode
  2. Análisis Sintáctico (Parser)              5. Optimización de Código
     • Gramática Tipo 2 $\rightarrow$ AST         • Eliminación de código muerto/bucles
  3. Análisis Semántico                        6. Generación de Código Máquina
     • Tipos y Tabla de Símbolos                  • Binario ejecutable objeto (.obj / .exe)
```

---

## 🔵 4. Analizadores Sintácticos (Parsers): Top-Down vs Bottom-Up

### A. Analizadores Descendentes (*Top-Down*):
- Construyen el árbol sintáctico desde la raíz (símbolo inicial) hacia las hojas.
- **LL(k)**: Lectura de **I**zquierda a derecha, derivación más a la **I**zquierda (*Leftmost*), con $k$ símbolos de anticipación (*lookahead*).
- Requieren gramáticas no ambiguas y sin recursividad por la izquierda.

### B. Analizadores Ascendentes (*Bottom-Up*):
- Construyen el árbol sintáctico desde las hojas (tokens) hacia la raíz mediante operaciones de desplazamiento (*Shift*) y reducción (*Reduce*).
- **LR(k)**: Lectura de **I**zquierda a derecha, derivación más a la **D**erecha invertida (*Rightmost*).
- Tipos de Parsers LR:
  - **LR(0)**: Sin símbolos de anticipación.
  - **SLR(1)** (*Simple LR*): Utiliza conjuntos *FOLLOW* para resolver conflictos desplazamiento/reducción.
  - **LALR(1)** (*Lookahead LR*): Combina estados equivalentes de LR(1) (base de herramientas como **Yacc** / **Bison**).
  - **LR(1)**: Máxima potencia sintáctica pero con tablas de gran tamaño.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| **Compilador** | Traduce todo el código fuente de una vez a código objeto ejecutable nativo antes de la ejecución. |
| **Intérprete** | Traduce y ejecuta las instrucciones línea por línea en tiempo real (mayor portabilidad, menor velocidad). |
| **JIT (Just-In-Time)** | Compilación híbrida en tiempo de ejecución (compila bytecode frecuentemente usado a código máquina nativo, ej. JVM y CLR). |
| **Gestión de Memoria** | **Stack** (registros de activación, variables locales) vs **Heap** (memoria dinámica gestionada por punteros o Garbage Collector). |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/programming-languages-and-compilers|Lenguajes de Programación, Paradigmas y Compiladores]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
