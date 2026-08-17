---
title: "Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU"
type: "entity"
tags:
  - sistemas-operativos
  - procesos
  - planificacion-cpu
  - round-robin
  - pcb
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Sistemas Operativos y Planificación CPU"
  - "Gestión de Procesos SO"
---

# Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU

El subsistema de gestión de procesos del sistema operativo administra la asignación de la CPU entre los procesos listos para ejecución mediante algoritmos de planificación.

---

## 🏛️ Algoritmos de Planificación de CPU

- **FCFS**: Primero en llegar, primero en ser servido (no apropiativo).
- **SJF / SRTF**: Menor tiempo restante primero (óptimo en tiempo medio de espera).
- **Round Robin (RR)**: Rodaja de tiempo / quantum ($q$) circular apropiativo.
- **Prioridades y MLFQ**: Colas multinivel con realimentación dinámica.

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque2-tema04|Resumen Bloque 2 - Tema 04]]
- Concepto: [[wiki/concepts/cpu-scheduling-algorithms|Algoritmos de Planificación de CPU]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
