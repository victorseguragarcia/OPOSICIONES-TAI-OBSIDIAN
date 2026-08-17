---
title: "Gestión de Procesos, Hilos y Memoria Virtual"
type: "concept"
tags:
  - processes
  - memory
  - virtual-memory
  - threads
  - operating-systems
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Gestión de Procesos y Memoria"
  - "Process and Memory Management"
---

# Gestión de Procesos, Hilos y Memoria Virtual

Mecanismos de control y aislamiento que permiten la multiprogramación concurrente y segura en sistemas operativos modernos.

## Planificación de Procesos
- **Estados de Proceso**: Nuevo, Listo (Ready), Ejecutando (Running), Bloqueado (Waiting), Terminado (Zombie).
- **Algoritmos de Planificación**: Round Robin (RR), Shortest Job First (SJF), Colas Multinivel con Retroalimentación (MLFQ), Completely Fair Scheduler (CFS).
- **Concurrencia y Sincronización**: Semáforos, Mutex, Monitores, problemas clásicos (Sección Crítica, Bloqueo Mutuo / *Deadlock* - Condiciones de Coffman).

## Memoria Virtual
- **Paginación**: División de memoria en marcos físicos (*frames*) y páginas lógicas (*pages*), gestionadas mediante tablas de páginas y la MMU (*Memory Management Unit*).
- **Fallo de Página (Page Fault)**: Interrupción generada cuando una página requerida no reside en RAM física y debe cargarse desde el espacio de intercambio (*swap*).
- **Algoritmos de Reemplazo**: LRU (Least Recently Used), FIFO, Segunda Oportunidad (Reloj).

## Referencias
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Arquitectura: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]

