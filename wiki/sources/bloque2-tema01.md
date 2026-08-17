---
title: "Resumen Fuente: Bloque 2 - Tema 01: Arquitectura de Ordenadores, CPU, Memoria y Buses"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema01
  - arquitectura-ordenadores
  - cpu
  - jerarquia-memoria
  - buses
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Arquitectura de Ordenadores y CPU"
  - "bloque2-tema01"
---

# Resumen Fuente: Bloque 2 - Tema 01: Arquitectura de Ordenadores, CPU, Memoria y Buses

Resumen exhaustivo procesado desde la fuente oficial [[raw/sources/bloque2-tema01.md|bloque2-tema01.md]].

---

## 📖 Resumen Ejecutivo

Este tema profundiza en la estructura y funcionamiento interno de un sistema informático: los modelos arquitectónicos **Von Neumann** (memoria única compartida para datos e instrucciones) frente a **Harvard** (memorias y buses físicos separados), los componentes y registros de la **CPU** (Unidad de Control con PC, IR, decodificador; Unidad Aritmético-Lógica ALU con acumulador y registro de estado PSW; y registros de memoria MAR/MBR), el ciclo de instrucción (*fetch-decode-execute*), las filosofías **CISC vs RISC**, la **jerarquía de memoria** (registros, cachés L1/L2/L3, memoria RAM DRAM y almacenamiento secundario) con sus principios de localidad y políticas de correspondencia/reemplazo/escritura, y la clasificación y capacidad de direccionamiento de los **buses del sistema** (datos, direcciones y control).

---

## 🎯 Datos Clave para Oposiciones TAI

| Componente / Concepto | Función / Fórmula de Examen |
|-----------------------|-----------------------------|
| **Modelo Von Neumann** | Memoria **única compartida** para datos e instrucciones (Cuello de botella de bus único) |
| **Modelo Harvard** | Memorias y buses **separados físicamente** para datos e instrucciones |
| **Contador de Programa (PC)** | Contiene la **dirección de memoria de la siguiente instrucción** a ejecutar |
| **Registro de Instrucción (IR)** | Almacena la **instrucción que se está ejecutando** actualmente |
| **Registro MAR / MBR** | **MAR**: Dirección física conectada al bus de direcciones \| **MBR**: Datos conectados al bus de datos |
| **Espacio Direccionable Bus Direcciones** | $2^N$ bytes, donde $N$ es el número de líneas de dirección ($2^{32} = 4\text{ GB}$) |
| **Caché Write-Through vs Write-Back** | **Write-Through**: Escribe en caché y RAM a la vez \| **Write-Back**: Escribe solo en caché (bit sucio) |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/cpu-architecture-von-neumann|Arquitectura de CPU y Modelo Von Neumann]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria y Memoria RAM]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
- Síntesis: [[wiki/synthesis/bloque2-tai-oposiciones-master-guide|Guía Maestra de Bloque 2: Tecnología Básica (TAI)]]
