---
title: "Algoritmos de Planificación de CPU en Sistemas Operativos"
type: "concept"
tags:
  - planificacion-cpu
  - round-robin
  - sjf
  - fcfs
  - mlfq
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Planificación de CPU"
  - "Algoritmos de Planificación"
---

# Algoritmos de Planificación de CPU en Sistemas Operativos

Estrategias del planificador de corto plazo (*dispatcher*) para seleccionar el siguiente proceso a ejecutar en la CPU.

---

## 🏛️ Métricas y Criterios
- **Tiempo de Espera (*Waiting Time*)**: Tiempo total que un proceso pasa en la cola de listos.
- **Tiempo de Retorno (*Turnaround Time*)**: Tiempo transcurrido desde la creación hasta la terminación.
- **Rendimiento (*Throughput*)**: Procesos completados por unidad de tiempo.

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Sistemas Operativos y Planificación]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU]]
