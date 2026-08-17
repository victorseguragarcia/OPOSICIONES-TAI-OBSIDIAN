---
title: "Arquitectura de CPU y Modelo Von Neumann"
type: "entity"
tags:
  - cpu
  - von-neumann
  - harvard
  - hardware
  - registros
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Arquitectura de CPU"
  - "Modelo Von Neumann"
  - "Procesador"
---

# Arquitectura de CPU y Modelo Von Neumann

La **Unidad Central de Proceso (CPU)** es el núcleo computacional del ordenador encargado de interpretar y ejecutar las instrucciones de los programas almacenados en memoria.

---

## 🏛️ Componentes y Registros de la CPU

```
                         Estructura Interna de la CPU
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
Unidad de Control (UC)      Unidad Aritmético-Lógica (ALU)     Banco de Registros
• Contador de Programa (PC) • Acumulador (ACC)                 • MAR (Direcciones)
• Registro Instrucción (IR) • Flags / Estado (PSW)             • MBR / MDR (Datos)
• Decodificador y Reloj     • Circuitos Operacionales          • Propósito General (R0-Rn)
```

---

## 🎯 Datos Clave para Oposiciones TAI

| Registro / Arquitectura | Definición Técnica |
|-------------------------|--------------------|
| **Contador de Programa (PC)** | Contiene la dirección de la **siguiente instrucción a ejecutar** |
| **Registro de Instrucción (IR)** | Almacena el código de operación de la **instrucción actual** |
| **Registro MAR** | Contiene la dirección física conectada al **bus de direcciones** |
| **Registro MBR/MDR** | Contiene la palabra de datos conectada al **bus de datos** |
| **CISC vs RISC** | CISC: Instrucciones complejas variables \| RISC: Instrucciones simples fijas tipo *Load/Store* |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Entidad: [[wiki/entities/memory-hierarchy-and-ram|Jerarquía de Memoria]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
