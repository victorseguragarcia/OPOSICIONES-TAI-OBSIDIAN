---
title: "Gestión de Procesos y Memoria en Sistemas Operativos"
type: "concept"
tags:
  - processes
  - memory-management
  - virtual-memory
  - operating-systems
sources:
  - "raw/sources/bloque4-tema01.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Gestión de Procesos y Memoria"
  - "Process and Memory Management"
---

# Gestión de Procesos y Memoria en Sistemas Operativos

La gestión eficiente de los procesadores y de la memoria principal constituye una de las tareas esenciales de cualquier sistema operativo multiprogramado.

---

## 🏛️ Gestión de Procesos y Planificación

- **Definición de Proceso**: Programa en ejecución junto con su espacio de memoria (código, datos, pila, montículo) y su **PCB (Process Control Block)**.
- **Transición de Estados de un Proceso**:
  - `Nuevo` $\rightarrow$ `Listo (Ready)` $\leftrightarrow$ `Ejecución (Running)` $\rightarrow$ `Terminado (Zombie/Exit)`.
  - `Ejecución` $\rightarrow$ `Bloqueado/Esperando (Waiting/Sleep)` $\rightarrow$ `Listo`.
- **Algoritmos de Planificación de CPU**:
  - **FCFS (First-Come, First-Served)**: No apropiativo; sufre del efecto convoy.
  - **SJF (Shortest Job First)**: Óptimo en tiempo medio de espera; puede causar inanición (*Starvation*).
  - **Round Robin (RR)**: Apropiativo basado en un cuanto de tiempo (*Quantum*).
  - **Colas Multinivel con Realimentación (MLFQ)**: Prioridades dinámicas según el comportamiento del proceso (I/O bound vs. CPU bound).
  - **CFS (Completely Fair Scheduler)**: Planificador de Linux basado en tiempo de ejecución virtual (*vruntime*) y árboles rojo-negro.

---

## 🧩 Gestión de Memoria Virtual y Paginación

- **Memoria Virtual**: Permite ejecutar procesos cuyo tamaño supera la memoria RAM física disponible mediante la abstracción del espacio de direcciones.
- **Paginación**:
  - La memoria lógica se divide en **Páginas** de tamaño fijo (típicamente 4 KB).
  - La memoria física se divide en **Marcos de Página (Frames)** del mismo tamaño.
  - La **MMU (Memory Management Unit)** traduce direcciones virtuales a físicas mediante la **Tabla de Páginas** y acelera las consultas con la **TLB (Translation Lookaside Buffer)**.
- **Fallo de Página (Page Fault)**: Ocurre cuando un proceso intenta acceder a una página que no está cargada en RAM física. El SO suspende el proceso, lee la página desde el disco (área de *Swap* o fichero de paginación) y actualiza la tabla de páginas.
- **Hiperpaginación (Thrashing)**: Situación crítica donde el sistema dedica más tiempo a transferir páginas entre RAM y disco que a ejecutar instrucciones útiles.

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Detalle Técnico |
|----------|-----------------|
| Tamaño Página Estándar | **4 Kilobytes (4096 bytes)** |
| Planificador Linux | **CFS (Completely Fair Scheduler)** |
| Acelerador de Traducción MMU | **TLB (Translation Lookaside Buffer)** |
| Algoritmo de Reemplazo Óptimo Teórico | Algoritmo de **Belady** (reemplaza la página que tardará más en usarse) |

---

## 🔗 Referencias Cruzadas
- Fuente: [[wiki/sources/bloque4-tema01|Resumen Bloque 4 - Tema 01]]
- Entidad: [[wiki/entities/linux-kernel|Linux Kernel]]
- Concepto: [[wiki/concepts/operating-system-architecture|Arquitectura de Sistemas Operativos]]
