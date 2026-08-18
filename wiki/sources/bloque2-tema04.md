---
title: "Resumen Fuente: Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Gestión de Procesos, Memoria y Sistemas de Archivos"
type: "source"
tags:
  - source-summary
  - oposiciones
  - tai
  - bloque-2
  - tema04
  - sistemas-operativos
  - procesos
  - planificacion-cpu
  - memoria-virtual
  - deadlocks
  - sistemas-archivos
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Resumen Sistemas Operativos y Procesos"
  - "bloque2-tema04"
---

# 🔴 Resumen Fuente: Bloque 2 - Tema 04 (UD012105): Sistemas Operativos: Gestión de Procesos, Memoria y Sistemas de Archivos

Resumen procesado y profundizado a partir de la fuente oficial [[raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md|bloque2-tema04-sistemas-operativos-procesos-memoria.md]] (122 páginas).

---

## 📖 1. Arquitectura del Sistema Operativo y Estados del Proceso

- **Modos de Ejecución**: **Modo Kernel / Supervisor** (acceso total al hardware e instrucciones privilegiadas) vs **Modo Usuario** (ejecución restringida mediante llamadas al sistema / *system calls*).
- **Estructura del Proceso**: Representado en el SO por el **Bloque de Control de Proceso (PCB / Task Struct)** que almacena: PID, Estado, Contador de Programa (PC), Registros de CPU, Información de Gestión de Memoria y Descriptores de Ficheros abiertos.
- **Transiciones de Estados**:
  - `Nuevo` $\rightarrow$ `Listo (Ready)`: Admitido a la cola de listos.
  - `Listo` $\rightarrow$ `Ejecutando (Running)`: Seleccionado por el planificador de CPU (*Dispatcher*).
  - `Ejecutando` $\rightarrow$ `Listo`: Por expiración de quantum de tiempo (interrupción de reloj).
  - `Ejecutando` $\rightarrow$ `Bloqueado (Waiting)`: Por espera de una operación de E/S o evento.
  - `Bloqueado` $\rightarrow$ `Listo`: Al completarse la operación de E/S.
  - `Ejecutando` $\rightarrow$ `Terminado`: Fin de ejecución (liberación de recursos).

---

## 🟣 2. Algoritmos de Planificación de CPU y Bloqueos Mutuos (Deadlocks)

### A. Algoritmos de Planificación de CPU:
1. **FCFS (First-Come, First-Served)**: No apropiativo. Sufre el *efecto convoy* ante ráfagas largas de CPU.
2. **SJF (Shortest Job First)**: Óptimo en tiempo medio de espera. Versión apropiativa: **SRTF (Shortest Remaining Time First)**.
3. **Round Robin (RR)**: Apropiativo con rodaja de tiempo o **quantum ($q$)**. Si $q$ es muy grande degenera en FCFS; si $q$ es muy pequeño la sobrecarga por cambio de contexto es excesiva.
4. **Colas Multinivel con Realimentación (MLFQ)**: Múltiples colas con prioridades dinámicas según el comportamiento de la ráfaga de CPU.

### B. Interbloqueos (Deadlocks):
- **Las 4 Condiciones Necesarias de Coffman**:
  1. *Exclusión Mutua*: Al menos un recurso no compartible.
  2. *Retención y Espera (Hold and Wait)*: Un proceso retiene recursos mientras espera otros.
  3. *No Apropiación (No Preemption)*: Los recursos no pueden ser arrebatados forzosamente.
  4. *Espera Circular*: Existe una cadena de procesos $\{P_0, P_1, ..., P_n\}$ donde $P_0$ espera un recurso de $P_1$, etc.
- **Tratamiento**:
  - *Prevención*: Invalidar al menos una de las 4 condiciones de Coffman.
  - *Evasión*: **Algoritmo del Banquero de Dijkstra** (asegurar estados siempre seguros).
  - *Detección y Recuperación*: Algoritmo de grafo de asignación de recursos y terminación forzosa de procesos.

---

## 🔵 3. Gestión de Memoria Virtual y Algoritmos de Reemplazo

- **Paginación**: División del espacio lógico en **Páginas** de tamaño fijo ($4\text{ KB}$) y la memoria física en **Marcos de Página (*Frames*)**.
  - **Tabla de Páginas**: Traduce dirección lógica (número de página + desplazamiento) a física.
  - **TLB (Translation Lookaside Buffer)**: Caché hardware asociativa para acelerar la traducción de direcciones.
- **Algoritmos de Reemplazo de Páginas**:
  - **FIFO**: Reemplaza la página más antigua (puede sufrir la **Anomalía de Belady**: más marcos asignados provocan más fallos de página).
  - **LRU (Least Recently Used)**: Reemplaza la página que no ha sido usada durante más tiempo.
  - **Óptimo de Belady (OPT)**: Reemplaza la página que tardará más tiempo en ser usada en el futuro (teórico).
  - **Reloj (Segunda Oportunidad)**: Aproximación a LRU mediante un bit de referencia.
- **Hiperpaginación (*Thrashing*)**: El sistema pasa más tiempo intercambiando páginas entre RAM y disco que ejecutando instrucciones útiles.

---

## 🔵 4. Comparativa de Sistemas de Archivos

| Sistema de Archivos | Tamaño Máximo de Archivo | Tamaño Máximo de Volumen | Características Clave de Examen |
|---------------------|--------------------------|--------------------------|---------------------------------|
| **FAT32** | **4 GB** ($2^{32}-1\text{ bytes}$) | **2 TB** (8 TB teórico) | Sin permisos avanzados, sin journaling, máxima compatibilidad |
| **exFAT** | 16 EB | 128 PB | Diseñado para memorias flash extraíbles |
| **NTFS** | **16 TB** (hasta 8 PB en Win10/Srv) | 256 TB | **Journaling**, permisos **ACLs**, compresión, cifrado nativo **EFS**, cuotas |
| **ext4** | **16 TB** | **1 EB** | **Journaling** (Journal, Ordered, Writeback), asignación multiloque (*Extents*), inodos |
| **XFS** | 8 EB | 8 EB | Sistema de archivos transaccional de 64 bits de alto rendimiento en Linux |
| **Btrfs / ZFS** | 16 EB | 16 EB / 256 ZiB | Copy-on-Write (CoW), snapshots instantáneas, RAID integrado, autorreparación |

---

## 🎯 Datos Clave para Oposiciones TAI

| Concepto | Especificación Técnica |
|----------|------------------------|
| **Límite de archivo FAT32** | **4 GB** (si se intenta copiar un archivo $>4\text{ GB}$ da error) |
| **Anomalía de Belady** | Fenómeno donde aumentar el número de marcos de memoria física incrementa el número de fallos de página (ocurre en **FIFO**). |
| **Condiciones de Coffman** | **4 condiciones simultáneas** para que ocurra un Deadlock. |
| **Journaling** | Registro de transacciones previas a la escritura para garantizar la recuperación rápida tras fallos de energía. |

---

## 🔗 Enlaces del Grafo de Conocimiento
- Entidad: [[wiki/entities/operating-systems-architecture-and-scheduling|Sistemas Operativos: Arquitectura, Procesos y Planificación de CPU]]
- Entidad: [[wiki/entities/process-synchronization-and-deadlocks|Sincronización de Procesos, Condiciones de Coffman y Deadlocks]]
- Entidad: [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual, Paginación y Algoritmos de Reemplazo]]
- Entidad: [[wiki/entities/file-systems-ntfs-ext4-fat32|Sistemas de Archivos: FAT32, NTFS, ext4, XFS y Btrfs]]
- Síntesis: [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
- Síntesis: [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Guía de Memoria Virtual y Algoritmos de Paginación]]
- Síntesis: [[wiki/synthesis/file-systems-comparison-matrix|Matriz Comparativa de Sistemas de Archivos]]

> [!trampa] ⚠️ Trampas Frecuentes de Examen: Sistemas Operativos y Memoria
> 1. **Anomalía de Bélády**: Aumentar el número de marcos de página en memoria física **PUEDE aumentar el número de fallos de página** en el algoritmo **FIFO**. Ojo: los algoritmos de pila como **LRU y Óptimo (OPT) son inmunes** a la anomalía de Bélády.
> 2. **Fragmentación Interna vs Externa**: La paginación sufre únicamente de **fragmentación interna** (en la última página asignada); la segmentación tradicional sufre de **fragmentación externa**.
> 3. **Inanición (*Starvation*)**: Ocurre en **SJF (Shortest Job First)** y en algoritmos por prioridades estrictas si llegan continuamente procesos cortos; se soluciona mediante la técnica de **envejecimiento (*aging*)**.
