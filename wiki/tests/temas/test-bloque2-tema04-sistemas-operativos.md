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

# 🔴 Test de Autoevaluación: Bloque 2 - Tema 04 (Sistemas Operativos, Planificación y Memoria)

> [!info] 🎯 **Simulador Interactivo de Examen (Motor Nativo)**
> Selecciona las opciones que consideres correctas y pulsa el botón **"✅ Corregir Examen"** al final para calcular tu nota oficial (Acierto: $+1.0$ \| Fallo: $-0.33$) con corrección visual verde/rojo y justificaciones.

```tai-quiz
{
  "title": "Test de Autoevaluación: Bloque 2 - Tema 04 (Sistemas Operativos, Planificación y Memoria)",
  "questions": [
    {
      "question": "¿Cuál de los siguientes algoritmos de planificación de CPU es apropiativo (*preemptive*) y asigna a cada proceso un intervalo de tiempo fijo de CPU denominado *quantum*?",
      "options": [
        "FCFS (First-Come, First-Served).",
        "SJF no apropiativo.",
        "Round Robin (Turno Rotatorio).",
        "Prioridad no apropiativa."
      ],
      "answer": "c",
      "explanation": "Round Robin es el algoritmo por excelencia para tiempo compartido con quantum de CPU $q$."
    },
    {
      "question": "¿Qué fenómeno o anomalía describe la situación en la que aumentar el número de marcos de memoria física asignados a un proceso produce un MAYOR número de fallos de página en el algoritmo FIFO?",
      "options": [
        "Hiperpaginación (*Thrashing*).",
        "Anomalía de Belady.",
        "Efecto Convoy.",
        "Inversión de Prioridades."
      ],
      "answer": "b",
      "explanation": "La Anomalía de Belady ocurre en FIFO cuando más memoria física genera más fallos de página."
    },
    {
      "question": "¿Cuáles son las 4 condiciones necesarias de Coffman para que se produzca un Interbloqueo (*Deadlock*)?",
      "options": [
        "Exclusión mutua, Retención y espera, No apropiación y Espera circular.",
        "Apropiación forzosa, Concurrencia, Paralelismo y Sincronización.",
        "Memoria virtual, Paginación, Segmentación e Interrupciones.",
        "Bloqueo, Semáforos, Monitores y Sección crítica."
      ],
      "answer": "a",
      "explanation": "Las 4 condiciones de Coffman (1971): Exclusión mutua, retención y espera, no desapropiación y espera circular."
    },
    {
      "question": "¿Qué algoritmo clásico de evasión de deadlocks analiza el estado de asignación de recursos y solicitudes máximas para garantizar que el sistema siempre permanezca en un 'Estado Seguro'?",
      "options": [
        "Algoritmo de Peterson.",
        "Algoritmo del Banquero de Dijkstra.",
        "Algoritmo de Dekker.",
        "Algoritmo de Lamport (Panadería)."
      ],
      "answer": "b",
      "explanation": "El Algoritmo del Banquero de Dijkstra evalúa si conceder recursos mantiene el sistema en estado seguro."
    },
    {
      "question": "¿Qué componente hardware actúa como memoria caché de traducción rápida para almacenar las entradas más recientes de la tabla de páginas y acelerar la traducción de direcciones virtuales a físicas?",
      "options": [
        "MMU.",
        "TLB (Translation Lookaside Buffer).",
        "DMA (Direct Memory Access).",
        "APIC."
      ],
      "answer": "b",
      "explanation": "La TLB es una memoria asociativa de alta velocidad dentro de la MMU que cachea las traducciones página $"
    }
  ]
}
```
