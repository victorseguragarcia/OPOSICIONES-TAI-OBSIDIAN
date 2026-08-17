---
title: "Test de Autoevaluación: Bloque 2 - Tema 04 (Sistemas Operativos, Planificación y Memoria)"
type: "test"
target: "wiki/sources/bloque2-tema04.md"
date: "2026-08-17"
score: ""
tags:
  - test
  - bloque-2
  - sistemas-operativos
  - planificacion-cpu
  - memoria-virtual
  - paginacion
  - deadlocks
sources:
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
created: "2026-08-17"
updated: "2026-08-17"
---

# 🔴 Test Tema 04: Sistemas Operativos: Planificación de CPU, Memoria Virtual y Deadlocks

Cuestionario de 10 preguntas tipo test con formato oficial de examen de la AGE (4 opciones, respuesta única, penalización de $-0.33$ por fallo).

---


> [!info] 🎯 **Registro de Puntuación y Autoevaluación**
> - **Aciertos (+1.0)**: ____ | **Fallos (-0.33)**: ____ | **En Blanco (0.0)**: ____
> - **Nota Final**: **____ / 10.0** (Mínimo para aprobar: **5.0**)

---

## ❓ Preguntas

### 1. ¿Cuál de los siguientes algoritmos de planificación de CPU es apropiativo (*preemptive*) y asigna a cada proceso un intervalo de tiempo fijo de CPU denominado *quantum*?
- [ ] a) FCFS (First-Come, First-Served).
- [ ] b) SJF no apropiativo.
- [ ] c) Round Robin (Turno Rotatorio).
- [ ] d) Prioridad no apropiativa.

### 2. ¿Qué fenómeno o anomalía describe la situación en la que aumentar el número de marcos de memoria física asignados a un proceso produce un MAYOR número de fallos de página en el algoritmo FIFO?
- [ ] a) Hiperpaginación (*Thrashing*).
- [ ] b) Anomalía de Belady.
- [ ] c) Efecto Convoy.
- [ ] d) Inversión de Prioridades.

### 3. ¿Cuáles son las 4 condiciones necesarias de Coffman para que se produzca un Interbloqueo (*Deadlock*)?
- [ ] a) Exclusión mutua, Retención y espera, No apropiación y Espera circular.
- [ ] b) Apropiación forzosa, Concurrencia, Paralelismo y Sincronización.
- [ ] c) Memoria virtual, Paginación, Segmentación e Interrupciones.
- [ ] d) Bloqueo, Semáforos, Monitores y Sección crítica.

### 4. ¿Qué algoritmo clásico de evasión de deadlocks analiza el estado de asignación de recursos y solicitudes máximas para garantizar que el sistema siempre permanezca en un 'Estado Seguro'?
- [ ] a) Algoritmo de Peterson.
- [ ] b) Algoritmo del Banquero de Dijkstra.
- [ ] c) Algoritmo de Dekker.
- [ ] d) Algoritmo de Lamport (Panadería).

### 5. ¿Qué componente hardware actúa como memoria caché de traducción rápida para almacenar las entradas más recientes de la tabla de páginas y acelerar la traducción de direcciones virtuales a físicas?
- [ ] a) MMU.
- [ ] b) TLB (Translation Lookaside Buffer).
- [ ] c) DMA (Direct Memory Access).
- [ ] d) APIC.

---

> [!question]- 🔍 Ver Plantilla y Solucionario Argumentado
> ### Plantilla de Respuestas:
> 1. **c** | 2. **b** | 3. **a** | 4. **b** | 5. **b**
>
> ### Explicación Técnica:
> - **Pregunta 1 (c)**: Round Robin es el algoritmo por excelencia para tiempo compartido con quantum de CPU $q$.
> - **Pregunta 2 (b)**: La Anomalía de Belady ocurre en FIFO cuando más memoria física genera más fallos de página.
> - **Pregunta 3 (a)**: Las 4 condiciones de Coffman (1971): Exclusión mutua, retención y espera, no desapropiación y espera circular.
> - **Pregunta 4 (b)**: El Algoritmo del Banquero de Dijkstra evalúa si conceder recursos mantiene el sistema en estado seguro.
> - **Pregunta 5 (b)**: La TLB es una memoria asociativa de alta velocidad dentro de la MMU que cachea las traducciones página $
ightarrow$ marco.
