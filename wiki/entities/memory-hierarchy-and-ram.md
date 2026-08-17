---
title: "Jerarquía de Memoria, Memoria RAM y Memorias ROM"
type: "entity"
tags:
  - memoria
  - ram
  - rom
  - cache
  - dram
sources:
  - "raw/sources/bloque2-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Jerarquía de Memoria"
  - "Memoria RAM"
  - "DRAM y SRAM"
---

# Jerarquía de Memoria, Memoria RAM y Memorias ROM

La jerarquía de memoria organiza los diferentes tipos de dispositivos de almacenamiento en función de la velocidad, coste y capacidad.

---

## 🏛️ Niveles de la Jerarquía de Memoria

1. **Registros de CPU**: $<1$ ns, Bytes.
2. **Caché L1 / L2 / L3 (SRAM)**: 1 a 20 ns, Kilobytes a Megabytes.
3. **Memoria Principal (DRAM - DDR4/DDR5)**: 50 a 100 ns, Gigabytes (requiere refresco periódico de condensadores).
4. **Almacenamiento Secundario (SSD NVMe / SATA, HDD)**: Microsegundos a Milisegundos, Terabytes (no volátil).

---

## 🎯 Datos Clave para Oposiciones TAI

| Tecnología | Características |
|------------|-----------------|
| **SRAM (Static RAM)** | Celdas de biestables (flip-flops, 4-6 transistores), muy rápida, sin refresco, usada en **memorias caché** |
| **DRAM (Dynamic RAM)** | Celdas de 1 transistor + 1 condensador, requiere **refresco periódico**, usada en **memoria principal** |
| **ROM / EEPROM / Flash** | No volátiles; Flash permite borrado y reescritura eléctrica por bloques |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema01|Resumen Bloque 2 - Tema 01]]
- Concepto: [[wiki/concepts/cache-memory-and-coherence|Memoria Caché y Coherencia]]
