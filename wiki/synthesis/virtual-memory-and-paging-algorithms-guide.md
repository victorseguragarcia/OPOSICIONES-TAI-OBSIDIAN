---
title: "Guía de Memoria Virtual, Paginación y Algoritmos de Reemplazo"
type: "synthesis"
tags:
  - synthesis
  - memoria-virtual
  - paginacion
  - tlb
  - lru
  - belady
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Memoria Virtual y Paginación"
  - "Paginación y Reemplazo Guía"
---

# 🔴 Guía de Memoria Virtual, Paginación y Algoritmos de Reemplazo

Manual de resolución de problemas de traducción de direcciones virtuales, tablas de páginas y políticas de reemplazo para TAI.

---

## 📐 1. Estructura de Dirección Virtual

$$\text{Dirección Virtual} = \text{Número de Página (p)} \mathbin{\Vert} \text{Desplazamiento (d)}$$
- Con páginas de $4\text{ KB} = 2^{12}\text{ bytes}$, el desplazamiento $d$ ocupa **12 bits**.
- Si el bus de direcciones es de 32 bits, el número de página $p$ ocupa **20 bits** ($2^{20} = 1.048.576\text{ páginas}$).

---

## 🔄 2. Resumen de Algoritmos de Reemplazo de Página

- **FIFO**: Fácil de implementar, pero sufre la **Anomalía de Belady**.
- **LRU**: Excelente rendimiento, pero requiere soporte hardware (marcas de tiempo o pila).
- **Reloj (Segunda Oportunidad)**: Aproximación a LRU eficiente mediante un bit de referencia circular.
- **Óptimo de Belady (OPT)**: Mínimo número de fallos de página posible (usado como patrón de comparación teórico).

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual]]
- Concepto: [[wiki/concepts/page-replacement-algorithms-and-thrashing|Reemplazo de Páginas y Thrashing]]
