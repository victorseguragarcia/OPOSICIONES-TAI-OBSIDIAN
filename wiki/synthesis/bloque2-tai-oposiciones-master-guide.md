---
title: "Guía Maestra de Bloque 2: Tecnología Básica, Hardware, Algoritmos, SO y SGBD (TAI)"
type: "synthesis"
tags:
  - synthesis
  - master-guide
  - bloque-2
  - oposiciones
  - tai
  - hardware
  - sistemas-operativos
  - sgbd
  - nosql
  - algoritmos
sources:
  - "raw/sources/bloque2-tema01-informatica-basica-representacion.md"
  - "raw/sources/bloque2-tema02-perifericos-conectividad-interfaces.md"
  - "raw/sources/bloque2-tema03-estructuras-ficheros-algoritmos.md"
  - "raw/sources/bloque2-tema04-sistemas-operativos-procesos-memoria.md"
  - "raw/sources/bloque2-tema05-sgbd-relacionales-nosql-cap.md"
created: "2026-08-17"
updated: "2026-08-17"
aliases:
  - "Guía Maestra Bloque 2"
  - "Bloque 2 TAI Master Guide"
---

# 🔴 Guía Maestra de Bloque 2: Tecnología Básica, Hardware, Algoritmos, SO y SGBD (TAI)

Compendio estructurado de estudio para el **Bloque 2**, cubriendo representación de datos, hardware de procesador y buses, estructuras de datos y algoritmos, gestión interna de sistemas operativos y bases de datos relacionales y NoSQL.

---

## 🗺️ 1. Matriz de Temas Oficiales del Bloque 2 (5 Temas)

| Tema | Materia Oficial | Fuente Oficial | Entidades Clave | Guías de Síntesis |
|:---|:---|:---|:---|:---|
| **Tema 01** | Informática Básica y Representación | [[wiki/sources/bloque2-tema01|Resumen Tema 01]] | [[wiki/entities/cpu-architecture-von-neumann|Von Neumann / Harvard]], [[wiki/entities/ieee-754-floating-point|IEEE 754]] | [[wiki/synthesis/ieee-754-and-binary-representation-cheatsheet|Cheatsheet C2 y Coma Flotante]] |
| **Tema 02** | Periféricos, Puertos y Conectividad | [[wiki/sources/bloque2-tema02|Resumen Tema 02]] | [[wiki/entities/peripheral-interfaces-usb-pcie-nvme|USB, PCIe, NVMe, Thunderbolt]] | [[wiki/synthesis/hardware-ports-and-buses-cheatsheet|Cheatsheet Puertos y Buses]] |
| **Tema 03** | Estructuras de Datos, Algoritmos y Ficheros | [[wiki/sources/bloque2-tema03|Resumen Tema 03]] | [[wiki/entities/data-structures-trees-and-graphs|Árboles AVL, B-Trees]], [[wiki/entities/sorting-and-searching-algorithms|Algoritmos]] | [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz Algoritmos Big-O]] |
| **Tema 04** | Sistemas Operativos: Procesos y Memoria | [[wiki/sources/bloque2-tema04|Resumen Tema 04]] | [[wiki/entities/operating-systems-architecture-and-scheduling|Planificación CPU]], [[wiki/entities/virtual-memory-paging-and-segmentation|Memoria Virtual]] | [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet CPU / Deadlocks]], [[wiki/synthesis/virtual-memory-and-paging-algorithms-guide|Paginación]] |
| **Tema 05** | SGBD Relacionales, NoSQL y Teorema CAP | [[wiki/sources/bloque2-tema05|Resumen Tema 05]] | [[wiki/entities/nosql-databases-and-cap-theorem|NoSQL y CAP]], [[wiki/entities/relational-databases-rdbms|RDBMS]] | [[wiki/synthesis/nosql-families-and-cap-theorem-guide|Guía NoSQL y Teorema CAP]] |

---

## 🟣 2. Núcleos Conceptuales de Alta Frecuencia de Examen

### A. Representación Numérica y Buses
- **Complemento a 2 ($n$ bits)**: Rango $[-2^{n-1}, +2^{n-1}-1]$. Para 8 bits: **$-128$ a $+127$**. El cero es único (`00000000`).
- **IEEE 754 Coma Flotante**:
  - Simple (32 bits): Signo (1), Exponente (8, sesgo **127**), Mantisa (23).
  - Doble (64 bits): Signo (1), Exponente (11, sesgo **1023**), Mantisa (52).
- **Puertos de E/S**:
  - **USB 2.0**: 480 Mbps | **USB 3.0 (3.1 Gen 1)**: 5 Gbps | **USB 3.1 Gen 2**: 10 Gbps | **USB4 / Thunderbolt 4**: **40 Gbps**.
  - **NVMe**: Protocolo sobre PCIe que soporta hasta **64.000 colas con 64.000 comandos** cada una en paralelo (frente a 1 cola de 32 comandos en AHCI/SATA).

---

### B. Algoritmos de Ordenación y Complejidad
| Algoritmo | Caso Medio | Peor Caso | Espacio | Estable | Estrategia |
|:---|:---:|:---:|:---:|:---:|:---|
| **Quicksort** | $O(n \log n)$ | $O(n^2)$ (pivote extremo) | $O(\log n)$ | NO | Divide y Vencerás (Partición) |
| **Mergesort** | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | **SÍ** | Divide y Vencerás (Mezcla) |
| **Heapsort** | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | NO | Árbol Montículo |
| **Búsqueda Binaria** | $O(\log n)$ | $O(\log n)$ | $O(1)$ | - | Divide y Vencerás (requiere array ordenado) |

---

### C. Sistemas Operativos (Procesos, Memoria y Deadlocks)
- **Planificación CPU**: FCFS (efecto convoy), SJF/SRTF (óptimo en tiempo de espera), Round Robin (quantum $q$).
- **Deadlocks**: 4 condiciones de Coffman (*Exclusión mutua, Retención y espera, No apropiación, Espera circular*). Evasión: **Algoritmo del Banquero de Dijkstra**.
- **Memoria Virtual**: Páginas ($4\text{ KB}$) $\rightarrow$ Marcos de página (*Frames*). TLB (*Translation Lookaside Buffer*).
  - Reemplazo de páginas: **FIFO** (sufre la **Anomalía de Belady**), **LRU** (*Least Recently Used*), Reloj / Segunda oportunidad.

---

### D. NoSQL y Teorema CAP de Brewer
- **Teorema CAP**: Ante una partición de red ($P$), los sistemas deben elegir entre **Consistencia (CP)** o **Disponibilidad (AP)**.
- **Familias NoSQL**:
  - *Clave-Valor*: **Redis** (en memoria RAM, CP/AP).
  - *Documentales*: **MongoDB** (almacenamiento en **BSON**, CP).
  - *Columnas Anchas*: **Apache Cassandra** (alta disponibilidad, AP con modelo BASE).
  - *Grafos*: **Neo4j** (nodos y relaciones, CA).

---

## 🔵 3. Recursos de Evaluación del Bloque 2
- [[wiki/synthesis/algorithms-complexity-and-sorting-matrix|Matriz de Algoritmos Big-O]]
- [[wiki/synthesis/cpu-scheduling-and-deadlocks-cheatsheet|Cheatsheet de Planificación de CPU y Deadlocks]]
- [[wiki/tests/bloques/index-tests-bloques|Simulacros Globales de Bloque 2]]
