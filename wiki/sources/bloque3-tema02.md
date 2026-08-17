---
title: "Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas y Compiladores"
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
  - gramaticas
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Lenguajes de Programación y Compiladores"
  - "bloque3-tema02"
---

# Resumen Fuente: Bloque 3 - Tema 02 (UD012109): Lenguajes de Programación, Paradigmas y Compiladores

Resumen procesado desde la fuente oficial [[raw/sources/bloque3-tema02-lenguajes-programacion.md|bloque3-tema02-lenguajes-programacion.md]] (114 páginas).

---

## 📖 Resumen Ejecutivo

Este tema analiza los fundamentos de los lenguajes de programación: la evolución de generaciones (1GL máquina, 2GL ensamblador, 3GL alto nivel, 4GL declarativos SQL, 5GL IA/lógica), los paradigmas de programación (imperativo, estructurado, orientado a objetos, funcional y lógico), la teoría de traductores (diferencias entre **Compiladores** e **Intérpretes**) y las fases formales del proceso de compilación: **Análisis Léxico** (tokens con autómatas finitos), **Análisis Sintáctico** (árboles de derivación con gramáticas libres de contexto), **Análisis Semántico** (comprobación de tipos con tabla de símbolos), **Generación de Código Intermedio**, **Optimización de Código** y **Generación de Código Máquina Objeto**.

---

## 🎯 Datos Clave para Oposiciones TAI

| Fase del Compilador | Tarea Principal |
|---------------------|-----------------|
| **Análisis Léxico (Scanner)** | Lee caracteres y genera **Tokens** (elimina espacios y comentarios) |
| **Análisis Sintáctico (Parser)** | Verifica la gramática y construye el **Árbol de Sintaxis Abstracta (AST)** |
| **Análisis Semántico** | Comprueba la coherencia lógica, concordancia de tipos y tabla de símbolos |
| **Generación de Código Intermedio** | Genera código independiente de la máquina (ej. código de 3 direcciones, Bytecode) |
| **Compilador vs Intérprete** | Compilador: Traduce todo el programa a ejecutable binario \| Intérprete: Traduce y ejecuta línea a línea |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/programming-languages-and-compilers|Lenguajes de Programación, Paradigmas y Compiladores]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3: Desarrollo de Sistemas (TAI)]]
