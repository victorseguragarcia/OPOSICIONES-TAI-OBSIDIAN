---
title: "Lenguajes de Programación, Paradigmas y Compiladores"
type: "entity"
tags:
  - lenguajes-programacion
  - compiladores
  - interpretes
  - gramaticas
sources:
  - "raw/sources/bloque3-tema02-lenguajes-programacion.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Lenguajes de Programación"
  - "Compiladores e Intérpretes"
---

# Lenguajes de Programación, Paradigmas y Compiladores

Fundamentos teóricos de los lenguajes informáticos, paradigmas de desarrollo y fases del proceso de traducción de código fuente a código máquina.

---

## 🏛️ Fases de la Compilación

```
Código Fuente ──> [ Análisis Léxico (Tokens) ]
                        │
                  [ Análisis Sintáctico (AST) ]
                        │
                  [ Análisis Semántico (Tipos) ]
                        │
                  [ Código Intermedio ]
                        │
                  [ Optimización de Código ]
                        │
                        ▼
                  Código Máquina Objeto (.exe / .o)
```

- **Compilador vs Intérprete**: Compilador traduce el código completo a binario independiente antes de la ejecución; el Intérprete traduce y ejecuta instrucción a instrucción en tiempo real.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque3-tema02|Resumen Bloque 3 - Tema 02]]
- Síntesis: [[wiki/synthesis/bloque3-tai-oposiciones-master-guide|Guía Maestra de Bloque 3 (TAI)]]
