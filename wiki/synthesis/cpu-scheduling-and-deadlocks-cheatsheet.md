---
title: "Cheatsheet de Planificación de CPU, Algoritmos y Bloqueos Mutuos (Deadlocks)"
type: "synthesis"
tags:
  - synthesis
  - cheatsheet
  - bloque-2
  - planificacion-cpu
  - deadlocks
  - coffman
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Cheatsheet Planificación CPU y Deadlocks"
  - "Planificación y Deadlocks Guía"
---

# 🔴 Cheatsheet de Planificación de CPU, Algoritmos y Bloqueos Mutuos (Deadlocks)

Tabla de repaso rápido de algoritmos de CPU, condiciones de Coffman y algoritmo del banquero.

---

## 📋 1. Matriz de Algoritmos de Planificación

| Algoritmo | Tipo | Ventajas | Inconvenientes / Riesgos |
|-----------|------|----------|--------------------------|
| **FCFS** | No Apropiativo | Sencillo de implementar | Efecto convoy (tiempos de espera altos) |
| **SJF** | No Apropiativo | Óptimo en tiempo medio de espera | Inanición (*starvation*) de procesos largos |
| **SRTF** | **Apropiativo** | Variante apropiativa de SJF | Sobrecarga de cambios de contexto |
| **Round Robin (RR)** | **Apropiativo** | Justo y óptimo para tiempo compartido | Sensible al tamaño del quantum ($q$) |
| **MLFQ** | **Apropiativo** | Dinámico y adaptable | Complejo de configurar |

---

## 🔒 2. Las 4 Condiciones de Coffman para Deadlocks

1. **Exclusión Mutua**
2. **Retención y Espera (*Hold & Wait*)**
3. **No Apropiación (*No Preemption*)**
4. **Espera Circular**

---

## 🔗 Referencias Cruzadas
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Planificación de CPU]]
- Entidad: [[wiki/entities/process-synchronization-and-deadlocks|Sincronización y Deadlocks]]
