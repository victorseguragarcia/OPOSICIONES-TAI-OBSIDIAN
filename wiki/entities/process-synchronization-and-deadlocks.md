---
title: "Sincronización de Procesos, Condiciones de Coffman y Deadlocks"
type: "entity"
tags:
  - sistemas-operativos
  - deadlocks
  - coffman
  - exclusion-mutua
  - dijkstra
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Deadlocks y Sincronización"
  - "Condiciones de Coffman"
---

# Sincronización de Procesos, Condiciones de Coffman y Deadlocks

Situación de bloqueo mutuo donde un conjunto de procesos se encuentra permanentemente esperando por recursos asignados a otros procesos del mismo conjunto.

---

## 🏛️ Las 4 Condiciones de Coffman

1. **Exclusión Mutua**: Recursos de uso exclusivo.
2. **Retención y Espera**: Proceso retiene recursos mientras solicita nuevos.
3. **No Apropiación**: Los recursos no pueden ser expropiados forzosamente.
4. **Espera Circular**: Cadena cerrada de dependencias entre procesos y recursos.

- **Evasión**: **Algoritmo del Banquero de Dijkstra** (mantiene el sistema en estado seguro).

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
